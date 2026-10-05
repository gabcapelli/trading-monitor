"""
Estudo 44 -- arbitragem de funding entre Hyperliquid e Binance (neutra em
preco). PRE-REGISTRADO em 05/10/2026, antes de baixar os dados.

CONTEXTO
--------
Em 10/2026 o CLAUDE.md registrava que o Gabriel "nao gostou" da ideia de
diferenca de funding entre corretoras. Em 05/10/2026, depois da pesquisa na
internet (fundos neutros rendendo ~13-19%/ano; relatos de 6-19%/ano nessa
arbitragem especifica), ele liberou testar "na ordem que achar melhor".

MECANISMO
---------
O mesmo token paga funding diferente em cada corretora (publico, regras e
formula diferentes; a Hyperliquid paga de hora em hora). Vendido onde o
funding e mais alto e comprado onde e mais baixo, o preco se cancela e sobra a
diferenca. Nao preve direcao. Riscos: a diferenca inverter, a diferenca de
preco entre as duas pernas (base) andar contra, custo de entrar/sair.

DADOS
-----
- Hyperliquid: fundingHistory (API publica, horario, desde 05/2023), com o
  campo `premium` (preco do perpetuo vs oraculo). Cache em cache_hl/.
- Binance: fundingRate (data.binance.vision) e premiumIndexKlines de 1h
  (premio do perpetuo vs indice), mesma fonte do estudo 36.
- Universo: tokens com perpetuo nas duas (TKR na HL = TKRUSDT na Binance; os
  1000x e nomes divergentes ficam de fora), com >= 30 dias de historico nas duas
  na data.

REGRA (canonica, sem otimizar)
------------------------------
- Todo dia as 00:00 UTC, para cada token: sinal = diferenca media de funding
  (HL - Binance) nas 168 horas anteriores, anualizada.
- Carteira: ate 10 pares de maior |sinal| com |sinal| >= 20%/ano; peso igual.
  Par = vendido na corretora de funding maior, comprado na outra, mesmo
  nocional. Sai quando |sinal| < 5%/ano ou o sinal troca, ou cai fora do top 10
  por outro par >= 20%.
- P&L do par por hora = funding recebido - pago (taxas reais de cada hora) +
  variacao da base entre as pernas, aproximada pela diferenca dos premios de
  cada corretora (premio HL - premio Binance) entre entrada e saida.
- Custo: 0.05% (Binance) + 0.045% (HL) de taxa + 0.05% de slippage por perna,
  na entrada e na saida (~0.39% do nocional ida e volta).
- Capital: cada perna com margem igual ao nocional (1x, sem risco de
  liquidacao) -> capital = 2 x nocional. Retorno sobre o capital.

CRITERIO (fixado antes)
-----------------------
- PASSA: retorno anual sobre o capital com IC95 inteiro acima de 4% (o que a
  stablecoin pagaria parada), bootstrap em blocos de 7 dias do P&L diario.
- Descritivo de META: com alavancagem de 3x por perna (capital = 2/3 do
  nocional), o retorno x3; queda maxima x3. Atende se >= 20%/ano e queda <= 50%
  -- mas so faz sentido se PASSA (alavancagem nao cria vantagem).

DESCRITIVOS
-----------
- Persistencia: correlacao entre a diferenca dos 7 dias anteriores e a dos 7
  seguintes (sem ela nao ha estrategia).
- Por ano; so funding (sem base); custo dobrado; numero de pares ativos.

Uso (de dentro de monitor/):
    python replay_funding_hl.py --baixar   # so dados
    python replay_funding_hl.py
"""

import csv
import io
import json
import math
import os
import random
import sys
import time
import urllib.request
import zipfile
from collections import defaultdict
from datetime import datetime, timezone

import replay_deslistagem as D

AQUI = os.path.dirname(os.path.abspath(__file__))
DIR_HL = os.path.join(AQUI, "cache_hl")
H = 3_600_000
DIA = 24 * H
HL = "https://api.hyperliquid.xyz/info"
ANO_H = 24 * 365
LIMIAR_ENTRA = 0.20
LIMIAR_SAI = 0.05
MAX_PARES = 10
JANELA_H = 168
CUSTO_LADO = 0.0005 + 0.00045 + 2 * 0.0005     # entrar OU sair do par: taxa Binance + taxa HL + slippage nas 2 pernas
STABLE = 0.04
SEED = 42


# ---------------------------------------------------------------------------
# Dados
# ---------------------------------------------------------------------------

def _post(body):
    for t in range(6):
        try:
            req = urllib.request.Request(HL, data=json.dumps(body).encode(),
                                         headers={"Content-Type": "application/json"})
            return json.loads(urllib.request.urlopen(req, timeout=30).read())
        except Exception:
            time.sleep(2 + 3 * t)
    raise RuntimeError(f"HL falhou: {body}")


def universo_hl():
    return [u["name"] for u in _post({"type": "meta"})["universe"]]


def funding_hl(coin):
    """{hora: (funding por hora, premium)}"""
    os.makedirs(DIR_HL, exist_ok=True)
    fp = os.path.join(DIR_HL, f"{coin}.json")
    serie = {}
    if os.path.exists(fp):
        serie = {int(k): v for k, v in json.load(open(fp)).items()}
    ini = max(serie) + 1 if serie else 0
    while True:
        r = _post({"type": "fundingHistory", "coin": coin, "startTime": ini})
        if not r:
            break
        for x in r:
            serie[int(x["time"]) // H * H] = (float(x["fundingRate"]), float(x["premium"]))
        novo = int(r[-1]["time"]) + 1
        if novo <= ini or len(r) < 500:
            break
        ini = novo
        time.sleep(0.15)
    json.dump(serie, open(fp, "w"))
    return serie


def premio_binance(sym, t0, t1):
    """{hora: premio} de premiumIndexKlines 1h (fechamento)."""
    out = {}
    for mes in D._meses(t0, t1):
        fp = os.path.join(D.DIR_VISION, f"premio_{sym}_{mes}.json")
        if os.path.exists(fp):
            out.update({int(k): v for k, v in json.load(open(fp)).items()})
            continue
        raw = D._get(f"{D.VISION}/futures/um/monthly/premiumIndexKlines/{sym}/1h/{sym}-1h-{mes}.zip")
        linhas = {}
        if raw:
            linhas = {D._ms(r[0]) // H * H: float(r[4]) for r in D._csv_zip(raw)}
        if mes < datetime.now(timezone.utc).strftime("%Y-%m"):
            json.dump(linhas, open(fp, "w"))
        out.update(linhas)
    return out


def funding_binance_horario(sym, t0, t1):
    """{hora: taxa por hora}, espalhando cada pagamento pelo intervalo desde o anterior."""
    pag = []
    for mes in D._meses(t0, t1):
        fp = os.path.join(D.DIR_VISION, f"funding_{sym}_{mes}.json")
        if os.path.exists(fp):
            pag += json.load(open(fp))
        else:
            raw = D._get(f"{D.VISION}/futures/um/monthly/fundingRate/{sym}/{sym}-fundingRate-{mes}.zip")
            linhas = [[D._ms(r[0]), float(r[2])] for r in D._csv_zip(raw)] if raw else []
            if mes < datetime.now(timezone.utc).strftime("%Y-%m"):
                json.dump(linhas, open(fp, "w"))
            pag += linhas
    pag.sort()
    out = {}
    for (a, _), (b, taxa) in zip(pag, pag[1:]):
        n = max(round((b - a) / H), 1)
        for k in range(n):
            out[(a // H + 1 + k) * H] = taxa / n
    return out


# ---------------------------------------------------------------------------
# Estudo
# ---------------------------------------------------------------------------

def carregar():
    agora = int(time.time() * 1000) // H * H
    dados = {}
    coins = universo_hl()
    for i, c in enumerate(coins):
        sym = f"{c}USDT"
        meses = D.meses_disponiveis("futures/um", sym)
        if not meses:
            continue
        hl = funding_hl(c)
        if len(hl) < 24 * 60:
            continue
        t0 = max(min(hl), int(datetime.strptime(meses[0], "%Y-%m").replace(tzinfo=timezone.utc).timestamp() * 1000))
        bf = funding_binance_horario(sym, t0, agora)
        bp = premio_binance(sym, t0, agora)
        if len(bf) < 24 * 60:
            continue
        dados[c] = {"hl": hl, "bf": bf, "bp": bp}
        if i % 20 == 0:
            print(f"  ... {i}/{len(coins)} ({len(dados)} com dados nas duas)", flush=True)
    return dados


def simular(dados, custo_mult=1.0, com_base=True):
    horas = sorted({h for d in dados.values() for h in d["hl"] if h in d["bf"]})
    inicio = horas[0] + 30 * DIA
    dias = list(range((inicio // DIA + 1) * DIA, horas[-1], DIA))
    abertos = {}               # coin -> {"lado": +1 vende HL/compra Binance, -1 o contrario}
    pnl_dia, ativos, persist = [], [], []

    def dif(c, h):
        d = dados[c]
        if h in d["hl"] and h in d["bf"]:
            v = d["hl"][h][0] - d["bf"][h]
            return None if math.isnan(v) else v
        return None

    def base(c, h):
        d = dados[c]
        if h in d["hl"] and h in d["bp"]:
            v = d["hl"][h][1] - d["bp"][h]
            return None if math.isnan(v) else v     # ha horas com premio "nan" no vision
        return None

    for dia in dias:
        # sinais
        sinais = {}
        for c in dados:
            xs = [dif(c, h) for h in range(dia - JANELA_H * H, dia, H)]
            xs = [x for x in xs if x is not None]
            if len(xs) < JANELA_H * 0.8 or dif(c, dia - 30 * DIA) is None:
                continue
            sinais[c] = sum(xs) / len(xs) * ANO_H
            fut = [dif(c, h) for h in range(dia, dia + JANELA_H * H, H)]
            fut = [x for x in fut if x is not None]
            if len(fut) > JANELA_H * 0.8 and dia % (7 * DIA) == 0:
                persist.append((sinais[c], sum(fut) / len(fut) * ANO_H))
        # saidas
        custo = 0.0
        for c in list(abertos):
            s = sinais.get(c)
            if s is None or abs(s) < LIMIAR_SAI or (s > 0) != (abertos[c]["lado"] > 0):
                custo += CUSTO_LADO * custo_mult
                del abertos[c]
        # entradas (top |sinal|)
        cands = sorted((c for c, s in sinais.items() if abs(s) >= LIMIAR_ENTRA and c not in abertos),
                       key=lambda c: -abs(sinais[c]))
        for c in cands:
            if len(abertos) >= MAX_PARES:
                pior = min(abertos, key=lambda x: abs(sinais.get(x, 0)))
                if abs(sinais.get(pior, 0)) >= abs(sinais[c]):
                    break
                custo += CUSTO_LADO * custo_mult
                del abertos[pior]
            abertos[c] = {"lado": 1 if sinais[c] > 0 else -1}
            custo += CUSTO_LADO * custo_mult
        # P&L das 24h seguintes, por par (sobre o nocional de uma perna)
        tot = -custo
        for c, p in abertos.items():
            for h in range(dia, dia + DIA, H):
                x = dif(c, h)
                if x is not None:
                    tot += p["lado"] * x            # vendido onde paga mais: recebe a diferenca
            if com_base:
                b0, b1 = base(c, dia), base(c, dia + DIA)
                if b0 is not None and b1 is not None:
                    tot += -p["lado"] * (b1 - b0)   # vendido na HL perde se o premio da HL subir em relacao ao da Binance
        # capital = 2 x nocional total; nocional por par = capital / (2 * MAX_PARES); caixa ocioso rende zero
        pnl_dia.append((dia, tot / (2 * MAX_PARES)))
        ativos.append(len(abertos))
    return pnl_dia, ativos, persist


def resumo(pnl_dia):
    v = [x for _, x in pnl_dia]
    anos = len(v) / 365
    curva, pico, dd = 1.0, 1.0, 0.0
    for x in v:
        curva *= 1 + x
        pico = max(pico, curva)
        dd = min(dd, curva / pico - 1)
    return curva ** (1 / anos) - 1, dd, sum(v) / len(v) * 365


def boot_anual(v, conf=0.95, bloco=7):
    rng = random.Random(SEED)
    n = len(v)
    ms = []
    for _ in range(5000):
        s, m = 0.0, 0
        while m < n:
            i = rng.randrange(n)
            for j in range(bloco):
                if m >= n:
                    break
                s += v[(i + j) % n]
                m += 1
        ms.append(s / n * 365)
    ms.sort()
    a = (1 - conf) / 2
    return ms[int(a * 5000)], ms[int((1 - a) * 5000) - 1]


def main(argv):
    t0 = time.time()
    dados = carregar()
    print(f"Tokens com historico nas duas corretoras: {len(dados)}")
    if "--baixar" in argv:
        return
    pnl, ativos, persist = simular(dados)
    v = [x for _, x in pnl]
    cagr, dd, media = resumo(pnl)
    lo, hi = boot_anual(v)
    xs, ys = zip(*persist)
    mx, my = sum(xs) / len(xs), sum(ys) / len(ys)
    corr = sum((a - mx) * (b - my) for a, b in persist) / math.sqrt(
        sum((a - mx) ** 2 for a in xs) * sum((b - my) ** 2 for b in ys))
    ini = datetime.fromtimestamp(pnl[0][0] / 1000, timezone.utc)
    print(f"\nJanela: {ini:%Y-%m-%d} a hoje | pares ativos em media {sum(ativos)/len(ativos):.1f}")
    print(f"PERSISTENCIA: correlacao (7 d antes x 7 d depois) = {corr:+.2f} (n={len(persist)})")
    print(f"\nRETORNO SOBRE O CAPITAL (1x por perna, decide): media {100*media:+.1f}%/ano "
          f"IC95 [{100*lo:+.1f}, {100*hi:+.1f}] | composto {100*cagr:+.1f}%/ano | queda maxima {100*dd:.1f}%")
    por_ano = defaultdict(list)
    for d, x in pnl:
        por_ano[datetime.fromtimestamp(d / 1000, timezone.utc).year].append(x)
    print("  por ano: " + " | ".join(f"{a}: {100*sum(x)/len(x)*365:+.1f}%" for a, x in sorted(por_ano.items())))
    so_f, _, _ = simular(dados, com_base=False)
    print(f"  so funding (sem base): {100*resumo(so_f)[2]:+.1f}%/ano")
    c2, _, _ = simular(dados, custo_mult=2.0)
    print(f"  custo dobrado: {100*resumo(c2)[2]:+.1f}%/ano")
    print(f"  com 3x por perna (descritivo): ~{300*media:+.1f}%/ano, queda ~{300*dd:.1f}%")
    dec = "PASSA" if lo > STABLE else "NAO PASSA"
    meta = dec == "PASSA" and 3 * media >= 0.20 and 3 * dd >= -0.50
    print(f"\n  DECISAO: {dec} (IC95 inteiro acima de {100*STABLE:.0f}%/ano) | meta com 3x: "
          f"{'ATENDE' if meta else 'NAO ATENDE'}\n  [{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main(sys.argv[1:])
