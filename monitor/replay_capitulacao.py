"""
Estudo 31 -- capitulacao (queda forte + open interest despencando) como sinal
de compra, PRE-REGISTRADO em 04/10/2026, antes de calcular qualquer retorno.

HIPOTESE
--------
Queda forte de preco COM queda forte de open interest no mesmo dia = posicoes
alavancadas sendo liquidadas/fechadas a forca (desalavancagem). A venda
forcada se esgota e o preco repica. Mecanismo de fluxo, o tipo que o
CLAUDE.md aponta como o unico que ja deu algo. Contraste natural: a mesma
queda com open interest SUBINDO (vendidos novos entrando, nao capitulacao).

DADOS
-----
- Candles diarios UTC e funding real da Binance (fmz_motor / dados_binance).
- Open interest: data.binance.vision, futures/um/daily/metrics (5 min, desde
  09/2020), campo `sum_open_interest` -- QUANTIDADE de contratos, nao valor
  (o valor cai mecanicamente com o preco). Por dia: primeiro registro (00:00)
  e ultimo (23:55) do proprio dia. So os dias candidatos sao baixados.

REGRA (diario UTC)
------------------
- Candidato: retorno do dia t (fechamento / fechamento anterior - 1) <=
  -2 x desvio-padrao dos retornos diarios dos 60 dias anteriores (60 validos).
- CAPITULACAO (primaria): candidato E open interest do dia t
  (ultimo / primeiro - 1) <= -10%.
- Compra na abertura de t+1, vende na abertura de t+1+H, H = 3. Sem stop. Uma
  posicao por par; sinal com trade aberto e ignorado.
Limiares redondos, fixados sem olhar retorno: 2 sigma = queda forte para o
proprio ativo; -10% de OI num dia = desalavancagem grande.

MEDIDAS (fmz_motor.py, % por trade)
-----------------------------------
`abs` (custo 0.18% + funding real), `excesso` transversal (mesmo lado, mesmas
datas, 30 outros pares), `excesso_par` descritivo. Bootstrap por semana.

CRITERIO
--------
A (20 majors): descritivo. DE (368 perps da Binance): PASSA se `abs` E
`excesso` com IC95 > 0 na regra primaria. Menos de 200 trades no DE: SEM
AMOSTRA PARA DECIDIR.

DESCRITIVOS
-----------
- CONTRASTE: candidato com OI do dia >= +10% (compra igual).
- Queda sem filtro de OI (todo candidato com metrics disponivel).
- H = 1 e H = 7 na capitulacao.
- Por lado nao se aplica (so compra).

Uso (de dentro de monitor/):
    python replay_capitulacao.py --contar
    python replay_capitulacao.py
"""

import io
import json
import math
import os
import random
import sys
import time
import urllib.error
import urllib.request
import zipfile
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

import fmz_motor as M
from replay_funding_squeeze import trades_de

AQUI = os.path.dirname(os.path.abspath(__file__))
DIR_OI = os.path.join(AQUI, "cache_vision", "oi")
URL = "https://data.binance.vision/data/futures/um/daily/metrics/{s}/{s}-metrics-{d}.zip"
JANELA_VOL = 60
SIGMAS = 2.0
OI_CAPIT = -0.10
OI_CONTRASTE = 0.10
H_PRIMARIO = 3
MIN_DECIDIR = 200


def _oi_dia(sym, dia):
    """(oi_inicio, oi_fim) do dia 'AAAA-MM-DD' ou None."""
    url = URL.format(s=sym, d=dia)
    for tentativa in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=30) as r:
                raw = r.read()
            break
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if tentativa == 3:
                return None
        except Exception:
            if tentativa == 3:
                return None
        time.sleep(2 + 2 * tentativa)
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        linhas = z.read(z.namelist()[0]).decode().splitlines()
    vals = []
    for l in linhas:
        p = l.split(",")
        if len(p) > 2 and p[0][:1].isdigit():
            try:
                vals.append(float(p[2]))
            except ValueError:
                pass
    vals = [v for v in vals if v > 0]
    return (vals[0], vals[-1]) if len(vals) >= 200 else None


def oi_dias(sym, dias):
    """{dia: (ini, fim) | None}, com cache por simbolo."""
    os.makedirs(DIR_OI, exist_ok=True)
    fpath = os.path.join(DIR_OI, f"{sym}.json")
    cache = {}
    if os.path.exists(fpath):
        with open(fpath) as f:
            cache = json.load(f)
    falta = [d for d in dias if d not in cache]
    if falta:
        with ThreadPoolExecutor(16) as ex:
            for d, v in zip(falta, ex.map(lambda d: _oi_dia(sym, d), falta)):
                cache[d] = v
        with open(fpath, "w") as f:
            json.dump(cache, f)
    return {d: cache[d] for d in dias}


def candidatos(c):
    """Indices t com queda >= 2 sigma dos 60 dias anteriores."""
    r = [None] + [c[i][4] / c[i - 1][4] - 1 for i in range(1, len(c))]
    out = []
    for t in range(JANELA_VOL + 1, len(c)):
        jan = r[t - JANELA_VOL:t]
        m = sum(jan) / len(jan)
        sd = math.sqrt(sum((x - m) ** 2 for x in jan) / (len(jan) - 1))
        if sd > 0 and r[t] <= -SIGMAS * sd:
            out.append(t)
    return out


def dia_str(ts):
    return datetime.fromtimestamp(ts / 1000, timezone.utc).strftime("%Y-%m-%d")


VARIANTES = [
    # rotulo, filtro do OI, H
    ("PRIMARIA: capitulacao (OI <= -10%), H=3", lambda d: d <= OI_CAPIT, H_PRIMARIO),
    ("capitulacao, H=1", lambda d: d <= OI_CAPIT, 1),
    ("capitulacao, H=7", lambda d: d <= OI_CAPIT, 7),
    ("CONTRASTE: queda com OI >= +10%, H=3", lambda d: d >= OI_CONTRASTE, H_PRIMARIO),
    ("queda sem filtro de OI, H=3", lambda d: True, H_PRIMARIO),
]


def rodar(nome_universo, contar=False):
    rng = random.Random(M.SEED)
    res = {v[0]: [] for v in VARIANTES}
    precos = M.Precos()
    n_pares = n_cand = n_com_oi = 0
    for i, sym in enumerate(M.universo(nome_universo)):
        try:
            c = M.candles(sym)
        except Exception:
            continue
        if len(c) < 400:
            continue
        n_pares += 1
        precos.add(sym, c)
        cand = candidatos(c)
        n_cand += len(cand)
        oi = oi_dias(sym, [dia_str(c[t][0]) for t in cand])
        delta = {}
        for t in cand:
            v = oi[dia_str(c[t][0])]
            if v:
                delta[t] = v[1] / v[0] - 1
        n_com_oi += len(delta)
        fund = None if contar else M.Funding(sym)
        for rot, filtro, h in VARIANTES:
            sin = [(t, 1) for t in cand if t in delta and filtro(delta[t])]
            tr = trades_de(c, sin, h)
            if contar:
                res[rot] += [{"ts": c[x["j"]][0]} for x in tr]
            else:
                res[rot] += M.medir(c, tr, fund, rng, 1, sym=sym)
        if i % 50 == 0:
            print(f"    ... {i} pares", flush=True)
    if not contar:
        for tr in res.values():
            precos.excesso(tr, rng)
    print(f"  universo {nome_universo}: {n_pares} pares | {n_cand} dias candidatos (queda >= 2 sigma) | "
          f"{n_com_oi} com open interest", flush=True)
    return res


def main(argv):
    t0 = time.time()
    contar = "--contar" in argv
    decisao = None
    for nome, decide in (("A", False), ("DE", True)):
        print("\n" + "=" * 100 + f"\nUNIVERSO {nome} ({'DECIDE' if decide else 'descritivo'})"
              + (" -- SO CONTAGEM" if contar else "") + "\n" + "=" * 100, flush=True)
        res = rodar(nome, contar)
        for rot, tr in res.items():
            if contar:
                print(f"  {rot:<42} trades {len(tr):>6} | semanas {len({x['ts'] // M.MS_SEMANA for x in tr}):>4}")
                continue
            print(f"\n  [{rot}]  trades {len(tr)}")
            for chave, n in (("liq", "liquido (custo)"), ("abs", "absoluto (custo+funding)"),
                             ("excesso", "excesso transversal"), ("excesso_par", "excesso mesmo par (descr.)")):
                print(M.linha(n, tr, chave)[0])
        if decide and not contar:
            tr = res[VARIANTES[0][0]]
            if len(tr) < MIN_DECIDIR:
                decisao = f"SEM AMOSTRA PARA DECIDIR (n={len(tr)} < {MIN_DECIDIR})"
            else:
                _, _, lo_a = M.linha("", tr, "abs")
                _, _, lo_e = M.linha("", tr, "excesso")
                decisao = "PASSA" if (lo_a > 0 and lo_e > 0) else "NAO PASSA"
    if decisao:
        print(f"\n  DECISAO (universo DE, regra primaria): {decisao}")
    print(f"\n  [{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main(sys.argv[1:])
