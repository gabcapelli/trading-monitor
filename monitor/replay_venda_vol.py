"""
Estudo 42 -- vender volatilidade em BTC e ETH (premio de variancia).
PRE-REGISTRADO em 05/10/2026, antes de baixar qualquer dado, com as duas fases
fixadas juntas (o resultado da A nao muda o desenho da B).

POR QUE
-------
Os 41 estudos procuraram PREVISAO de direcao e nada passou. O perfil decidido
com o Gabriel em 05/10/2026 (20-50%/ano, aceita queda de 50%+) permite outra
fonte de retorno: vender seguro. Opcoes costumam embutir volatilidade maior que
a realizada (premio de variancia, documentado em acoes ha decadas e em cripto
na literatura). Quem vende ganha um pouco quase sempre e perde forte em crash.
Nao depende de prever direcao.

DADOS
-----
- Volatilidade implicita: DVOL da Deribit (indice de vol implicita de 30 dias,
  BTC e ETH, desde 03/2021), diario, API publica. Cache em cache_vol/.
- Preco: fechamento diario do perpetuo BTCUSDT/ETHUSDT da Binance
  (data.binance.vision), proxy do indice da Deribit.
- Limitacao assumida: so ha o DVOL (vol no dinheiro, 30 dias), nao a superficie
  inteira. Por isso a fase B vende so opcoes NO DINHEIRO de 30 dias, onde o DVOL
  e a medida certa.

FASE A -- O PREMIO EXISTE?
-------------------------
- VRP(t) = DVOL(t)^2 - variancia realizada nos 30 dias seguintes (log-retornos
  diarios, anualizada x365), em pontos de variancia; reportado tambem como
  "pontos de vol equivalentes" (raiz da media de DVOL^2 - raiz da media de RV^2).
  (Corrigido antes de rodar com dados reais: em pontos de vol, a raiz da
  variancia amostral puxa ~1 ponto a favor do vendedor -- desigualdade de Jensen,
  vista no teste sintetico abaixo.)
- Media com IC95 por bootstrap em blocos de 30 dias (as janelas se sobrepoem).
- Descritivo: % dos dias com DVOL > realizada; por ano.

FASE B -- A ESTRATEGIA RENDE?
-----------------------------
- Todo dia, abre uma "fatia": vende 1 put no dinheiro (strike = preco do dia),
  vencimento em 30 dias, com garantia em caixa igual ao strike (sem
  alavancagem, sem chance de liquidacao). 30 fatias em escada = carteira sempre
  investida, ~1/30 vencendo por dia.
- Preco recebido: Black-Scholes (juro zero) com vol = DVOL - 2 pontos (spread
  de compra/venda, conservador) e taxa da Deribit de 0.03% do subjacente na
  venda e 0.015% na liquidacao (cada uma limitada a 12.5% do premio).
- Resultado da fatia = (premio - max(strike - preco no vencimento, 0) - taxas)
  / strike.
- Carteira: retorno diario = media das fatias abertas, marcadas a mercado todo
  dia por Black-Scholes com o DVOL do dia (para o drawdown ser honesto, nao so
  no vencimento).
- Juro sobre a garantia NAO incluido (rendaria ~4%/ano em stablecoin; e a
  linha de base a vencer).

CRITERIO (fixado antes)
-----------------------
- PASSA (para cada moeda, IC 97.5% por Bonferroni de 2): retorno medio por
  fatia com IC inteiro acima de zero (bootstrap em blocos de 30 dias).
- ATENDE A META do Gabriel: retorno anual composto da carteira >= 20% E queda
  maxima (marcada a mercado) <= 50%. Comparado com comprar e segurar a moeda
  e com 4%/ano de stablecoin.
- Uma moeda que PASSA mas nao atende a meta vale como achado, nao como
  estrategia para este perfil.

DESCRITIVOS
-----------
- Straddle no dinheiro (put + call vendidas, sem hedge): mais premio, risco
  dos dois lados.
- Por ano; pior mes; custo de 4 pontos de vol em vez de 2.

VALIDACAO (feita antes dos dados reais, 05/10/2026)
--------------------------------------------------
Preco sintetico com vol de 60% e DVOL = 60 + haircut (premio zero), 30
sementes de 2000 dias: retorno medio por fatia -0.07% (erro padrao 0.19%;
esperado ~-0.04%, as taxas), nenhum PASSA falso. A carteira em escada teve a
contabilidade corrigida antes (versao inicial descartava o resultado das
fatias que venciam).

Uso (de dentro de monitor/):
    python replay_venda_vol.py
"""

import json
import math
import os
import random
import sys
import time
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone

import replay_deslistagem as D

AQUI = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(AQUI, "cache_vol")
DIA = 86_400_000
PRAZO = 30
HAIRCUT = 2.0
TAXA_VENDA = 0.0003
TAXA_LIQ = 0.00015
TETO_TAXA = 0.125
N_BOOT = 5000
SEED = 42
STABLE = 0.04


# ---------------------------------------------------------------------------
# Dados
# ---------------------------------------------------------------------------

def dvol(moeda):
    os.makedirs(DIR, exist_ok=True)
    fp = os.path.join(DIR, f"dvol_{moeda}.json")
    hoje = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    if os.path.exists(fp):
        d = json.load(open(fp))
        if d.get("baixado") == hoje:
            return {int(k): v for k, v in d["serie"].items()}
    serie, fim = {}, int(time.time() * 1000)
    while True:
        u = ("https://www.deribit.com/api/v2/public/get_volatility_index_data"
             f"?currency={moeda}&start_timestamp=0&end_timestamp={fim}&resolution=1D")
        r = json.loads(urllib.request.urlopen(u, timeout=30).read())["result"]
        for ts, o, h, l, c in r["data"]:
            serie[ts] = c
        if not r.get("continuation") or not r["data"]:
            break
        fim = r["continuation"]
        time.sleep(0.3)
    json.dump({"baixado": hoje, "serie": serie}, open(fp, "w"))
    return serie


def precos(moeda, t0, t1):
    """{dia (ts 00:00 UTC): fechamento do dia} do perpetuo da Binance."""
    k = D.klines("futures/um", f"{moeda}USDT", t0, t1)
    out = {}
    for ts in sorted(k):
        out[ts // DIA * DIA] = k[ts][3]   # ultimo fechamento horario do dia
    return out


# ---------------------------------------------------------------------------
# Black-Scholes (juro zero)
# ---------------------------------------------------------------------------

def _n(x):
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))


def put_bs(s, k, t_anos, vol):
    if t_anos <= 0 or vol <= 0:
        return max(k - s, 0.0)
    d1 = (math.log(s / k) + 0.5 * vol * vol * t_anos) / (vol * math.sqrt(t_anos))
    d2 = d1 - vol * math.sqrt(t_anos)
    return k * _n(-d2) - s * _n(-d1)


def call_bs(s, k, t_anos, vol):
    return put_bs(s, k, t_anos, vol) + s - k


# ---------------------------------------------------------------------------
# Estatistica
# ---------------------------------------------------------------------------

def boot_blocos(xs, conf, bloco=PRAZO):
    n = len(xs)
    rng = random.Random(SEED)
    ms = []
    for _ in range(N_BOOT):
        s = 0.0
        m = 0
        while m < n:
            i = rng.randrange(n)
            for j in range(bloco):
                if m >= n:
                    break
                s += xs[(i + j) % n]
                m += 1
        ms.append(s / n)
    ms.sort()
    a = (1 - conf) / 2
    return sum(xs) / n, ms[int(a * N_BOOT)], ms[int((1 - a) * N_BOOT) - 1]


def dd_max(curva):
    pico, pior = curva[0], 0.0
    for v in curva:
        pico = max(pico, v)
        pior = min(pior, v / pico - 1)
    return pior


# ---------------------------------------------------------------------------
# Estudo
# ---------------------------------------------------------------------------

def estudar(moeda, haircut=HAIRCUT, straddle=False, verbose=True):
    iv = dvol(moeda)
    dias = sorted(iv)
    px = precos(moeda, dias[0] - 2 * DIA, dias[-1] + 2 * DIA)
    # dia d: DVOL de fechamento do dia d e preco de fechamento do dia d = momento da venda
    base = [d for d in dias if d in px]
    idx = {d: i for i, d in enumerate(base)}

    # Fase A
    vrp, por_ano = [], defaultdict(list)
    for d in base:
        fut = [px.get(d + j * DIA) for j in range(PRAZO + 1)]
        if None in fut:
            continue
        r = [math.log(fut[j + 1] / fut[j]) for j in range(PRAZO)]
        rv2 = 1e4 * sum(x * x for x in r) / PRAZO * 365
        vrp.append(iv[d] ** 2 - rv2)
        por_ano[datetime.fromtimestamp(d / 1000, timezone.utc).year].append((iv[d] ** 2, rv2))

    # Fase B: fatias
    fatias = []          # (dia de abertura, retorno da fatia)
    def premio(s, v, t):
        p = put_bs(s, s, t, v)
        if straddle:
            p += call_bs(s, s, t, v)
        return p
    for d in base:
        d_fim = d + PRAZO * DIA
        if d_fim not in px:
            continue
        s, s_t = px[d], px[d_fim]
        v = max(iv[d] - haircut, 1.0) / 100
        p = premio(s, v, PRAZO / 365)
        taxa_v = min(TAXA_VENDA * s * (2 if straddle else 1), TETO_TAXA * p)
        perda = max(s - s_t, 0.0) + (max(s_t - s, 0.0) if straddle else 0.0)
        taxa_l = min(TAXA_LIQ * s_t, TETO_TAXA * p) if perda > 0 else 0.0
        fatias.append((d, (p - perda - taxa_v - taxa_l) / s))

    # carteira em escada, marcada a mercado: cada fatia usa 1/30 do capital como
    # garantia; P&L do dia = soma das variacoes de valor das fatias / 30
    def valor(k, p_liq, s, t, v):
        custo = put_bs(s, k, t, v) + (call_bs(s, k, t, v) if straddle else 0.0)
        if t <= 0 and custo > 0:
            custo += min(TAXA_LIQ * s, TETO_TAXA * p_liq)
        return (p_liq - custo) / k

    abertas = {}         # dia de abertura -> [strike, premio liquido, valor marcado ontem]
    curva, ret_dia = [1.0], []
    for d in base:
        s = px[d]
        v_hoje = max(iv[d] - haircut, 1.0) / 100
        pnl = 0.0
        for d0 in list(abertas):
            k, p_liq, ant = abertas[d0]
            t = max(PRAZO - (d - d0) / DIA, 0) / 365
            novo_v = valor(k, p_liq, s, t, v_hoje)
            pnl += novo_v - ant
            if t <= 0:
                del abertas[d0]          # venceu: resultado realizado ja entrou no pnl
            else:
                abertas[d0][2] = novo_v
        if (d + PRAZO * DIA) in px:
            p = premio(s, v_hoje, PRAZO / 365)
            p_liq = p - min(TAXA_VENDA * s * (2 if straddle else 1), TETO_TAXA * p)
            v0 = valor(s, p_liq, s, PRAZO / 365, v_hoje)
            pnl += v0                    # nasce valendo -taxa (premio recebido = custo de recompra)
            abertas[d] = [s, p_liq, v0]
        if len(ret_dia) or len(abertas) >= PRAZO:
            r_d = pnl / PRAZO
            ret_dia.append(r_d)
            curva.append(curva[-1] * (1 + r_d))
    anos = len(ret_dia) / 365
    cagr = curva[-1] ** (1 / anos) - 1 if anos > 0 else float("nan")

    bh_ini, bh_fim = px[base[0]], px[base[-1]]
    bh_curva = [px[d] / bh_ini for d in base]
    bh_cagr = (bh_fim / bh_ini) ** (365 / len(base)) - 1
    return {"vrp": vrp, "por_ano": por_ano, "fatias": fatias, "cagr": cagr, "dd": dd_max(curva),
            "bh_cagr": bh_cagr, "bh_dd": dd_max(bh_curva), "inicio": base[0], "fim": base[-1]}


def main(argv):
    t0 = time.time()
    conf = 0.975
    for moeda in ("BTC", "ETH"):
        r = estudar(moeda)
        ini = datetime.fromtimestamp(r["inicio"] / 1000, timezone.utc)
        fim = datetime.fromtimestamp(r["fim"] / 1000, timezone.utc)
        print("\n" + "=" * 100 + f"\n{moeda}  ({ini:%Y-%m-%d} a {fim:%Y-%m-%d})\n" + "=" * 100)
        m, lo, hi = boot_blocos(r["vrp"], 0.95)
        pos = sum(x > 0 for x in r["vrp"]) / len(r["vrp"])
        todos = [x for v in r["por_ano"].values() for x in v]
        eq = math.sqrt(sum(a for a, _ in todos) / len(todos)) - math.sqrt(sum(b for _, b in todos) / len(todos))
        print(f"  FASE A  VRP em variancia (DVOL^2 - realizada^2, 30d): media {m:+.0f} IC95 [{lo:+.0f}, {hi:+.0f}] | "
              f"~{eq:+.1f} pts de vol | implicita > realizada em {100*pos:.0f}% dos dias (n={len(r['vrp'])})")
        print("          por ano (pts de vol equivalentes): " + " | ".join(
            f"{a}: {math.sqrt(sum(x for x, _ in v)/len(v)) - math.sqrt(sum(y for _, y in v)/len(v)):+.1f}"
            for a, v in sorted(r["por_ano"].items())))
        rets = [x for _, x in r["fatias"]]
        m, lo, hi = boot_blocos(rets, conf)
        print(f"  FASE B  put no dinheiro 30d, garantia em caixa: retorno por fatia {100*m:+.2f}% "
              f"IC97.5 [{100*lo:+.2f}, {100*hi:+.2f}] | ganhou em {100*sum(x>0 for x in rets)/len(rets):.0f}% | "
              f"pior fatia {100*min(rets):+.1f}%")
        print(f"          carteira em escada: {100*r['cagr']:+.1f}%/ano | queda maxima {100*r['dd']:.1f}%")
        print(f"          comprar e segurar {moeda}: {100*r['bh_cagr']:+.1f}%/ano | queda maxima {100*r['bh_dd']:.1f}%")
        por_ano = defaultdict(list)
        for d, x in r["fatias"]:
            por_ano[datetime.fromtimestamp(d / 1000, timezone.utc).year].append(x)
        print("          por ano (media por fatia): " + " | ".join(f"{a}: {100*sum(v)/len(v):+.2f}%" for a, v in sorted(por_ano.items())))
        r4 = estudar(moeda, haircut=4.0)
        print(f"          custo de 4 pts de vol: por fatia {100*sum(x for _, x in r4['fatias'])/len(r4['fatias']):+.2f}% | "
              f"{100*r4['cagr']:+.1f}%/ano | queda {100*r4['dd']:.1f}%")
        rs = estudar(moeda, straddle=True)
        xs = [x for _, x in rs["fatias"]]
        print(f"  DESCR.  straddle vendido: por fatia {100*sum(xs)/len(xs):+.2f}% | {100*rs['cagr']:+.1f}%/ano | "
              f"queda {100*rs['dd']:.1f}% | pior fatia {100*min(xs):+.1f}%")
        passa = lo > 0
        meta = r["cagr"] >= 0.20 and r["dd"] >= -0.50
        print(f"\n  DECISAO {moeda}: {'PASSA' if passa else 'NAO PASSA'} | meta (>=20%/ano e queda <=50%): "
              f"{'ATENDE' if meta else 'NAO ATENDE'}")
    print(f"\n  [{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main(sys.argv[1:])
