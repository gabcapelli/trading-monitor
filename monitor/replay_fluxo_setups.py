"""
Estudos 68 (absorcao) e 69 (divergencia de delta acumulado) -- setups de fluxo
de ordens com o volume de compra agressiva (taker) do perpetuo.
PRE-REGISTRADOS em 13/10/2026, antes de rodar. Tentativa unica cada, mesma regua
dos estudos 57-59 e 63-67 (replay_div_engolfo.py).

UNIVERSO, DADOS, EXECUCAO E CRITERIO: iguais aos do estudo 59 (replay_nr7_pfr.py):
top 50 de volume do dia, 2020-01 a 2026-09, 1d e 4h, stop e alvo checados em 1h,
custo 0.18% + funding, placebo com o mesmo risco %, IC 97.5%. Entrada por stop no
rompimento do candle do sinal, valida so no candle seguinte; alvo 2R; saida na
abertura do 11o candle depois do sinal; 1R minimo 0.3%.

DELTA do candle = (compra agressiva - venda agressiva) / volume, em [-1, 1], do
perpetuo (klines da Binance Vision, campo taker buy quote volume).

ESTUDO 68 -- ABSORCAO (venda no espelho)
- Mecanismo: venda agressiva anormal que nao derruba o preco = compradores
  passivos absorvendo; a pressao vendedora se esgota.
- Sinal: z-score do delta do candle i contra os 50 candles anteriores <= -2,
  candle de alta (fech > abertura) e fechamento na metade de cima da amplitude.
- Compra stop na maxima de i; stop na minima de i.

ESTUDO 69 -- DIVERGENCIA DE DELTA ACUMULADO (venda no topo; compra no espelho)
- Mecanismo: alta sem compra agressiva = movimento sem demanda real, tende a falhar.
- Sinal: maxima de i e a maior dos ultimos 20 candles (ela inclusa) e a soma do
  delta x volume dos 20 candles (CVD da janela) e negativa.
- Venda stop na minima de i; stop na maxima de i.

FUNIL PARA O PAPEL (proposto em 13/10/2026; descritivo, nao muda o veredito):
uma celula vira candidata a papel se R bruto > 0, excesso com IC95 > 0 e n >= 200.

Uso (de dentro de monitor/):
    python replay_fluxo_setups.py        # 68 e 69
    python replay_fluxo_setups.py 69b    # correcao de medida do 69
"""

import json
import os
import random
import statistics
import sys
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

import replay_continuacao_top20 as T
import replay_deslistagem as D
import replay_div_engolfo as E
import replay_fluxo_spot_perp as F
import replay_nr7_pfr as P
import replay_sfp as S

H = S.H
SEED = 42


def barras(h1, horas):
    """(t, o, h, l, c, volume, delta x volume) agregando 1h."""
    g = defaultdict(list)
    for ts in sorted(h1):
        g[ts // (horas * H) * horas * H].append(h1[ts])
    out = []
    for t in sorted(g):
        xs = g[t]
        if len(xs) < horas:
            continue
        vol = sum(x[4] for x in xs)
        dv = sum(2 * x[5] - x[4] for x in xs)
        out.append((t, xs[0][0], max(x[1] for x in xs), min(x[2] for x in xs), xs[-1][3], vol, dv))
    return out


def sinais_abs(b):
    d = [x[6] / x[5] if x[5] > 0 else 0.0 for x in b]
    out = []
    for i in range(50, len(b) - 1):
        jan = d[i - 50:i]
        sd = statistics.pstdev(jan)
        if sd == 0:
            continue
        z = (d[i] - sum(jan) / 50) / sd
        o, h, l, c = b[i][1:5]
        if h <= l:
            continue
        if z <= -2 and c > o and c >= (h + l) / 2:
            out.append((i, +1, h, l))
        elif z >= 2 and c < o and c <= (h + l) / 2:
            out.append((i, -1, l, h))
    return out


def sinais_cvd(b):
    out = []
    for i in range(19, len(b) - 1):
        jan = b[i - 19:i + 1]
        cvd = sum(x[6] for x in jan)
        if b[i][2] >= max(x[2] for x in jan) and cvd < 0:
            out.append((i, -1, b[i][3], b[i][2]))
        elif b[i][3] <= min(x[3] for x in jan) and cvd > 0:
            out.append((i, +1, b[i][2], b[i][3]))
    return out


def main(argv):
    t0 = time.time()
    syms = T.simbolos()
    with ThreadPoolExecutor(16) as ex:
        vols = dict(zip(syms, ex.map(T.diario, syms)))
    vols = {s: v for s, v in vols.items() if v}
    T.TOP = S.TOP
    rk = T.ranking(vols)
    alguma = sorted({s for d, v in rk.items() if F.INICIO <= d < F.FIM for s in v})
    rng = random.Random(SEED)
    estudos = {"ABS": sinais_abs, "CVD": sinais_cvd}
    res = {e: {tf: [] for tf in S.TFS} for e in estudos}
    S_barras = S.barras
    for s in alguma:
        ms = S.meses(s, rk)
        h1 = {}
        for mm in ms:
            h1.update({ts: v for ts, v in F.klines_mes("futures/um", s, mm).items() if v[0] > 0})
        if not h1:
            continue
        fund = []
        for mm in ms:
            fp = os.path.join(D.DIR_VISION, f"funding_{s}_{mm}.json")
            if os.path.exists(fp):
                fund += [tuple(x) for x in json.load(open(fp))]
        fund.sort()
        S.barras = barras                                 # rodar() do 63 com barras que carregam o delta
        for e, fn in estudos.items():
            E.sinais_div = fn
            E.rodar("DIV", h1, fund, s, rk, rng, res[e])
        S.barras = S_barras
    P.relatorio("ESTUDO 68 ABSORCAO", res["ABS"])
    P.relatorio("ESTUDO 69 DIVERGENCIA DE CVD", res["CVD"])
    print("\nFunil para o papel (descritivo; R bruto > 0, excesso IC95 > 0, n >= 200):")
    for e, nome in (("ABS", "68"), ("CVD", "69")):
        for tf, xs in res[e].items():
            ex = F.boot(xs, "excesso", 0.95)
            rb = sum(t["r_bruto"] for t in xs) / len(xs) if xs else float("nan")
            ok = ex and ex[3] >= 200 and ex[1] > 0 and rb > 0
            print(f"  {nome} {tf}: excesso {F.fmt(ex)} | bruto {rb:+.3f}R -> {'CANDIDATO' if ok else 'nao'}")
    print(f"\n[{time.time()-t0:.0f}s]")




# ---------------------------------------------------------------------------
# 69b -- CORRECAO DE MEDIDA (13/10/2026, depois de ver o 69): o delta do perpetuo
# tem vies negativo (-1% a -4% em media, pior nas altcoins), entao o CVD bruto da
# janela quase sempre e negativo e o 69 virou "vender toda maxima de 20 candles"
# (95% dos sinais foram vendas). Rodada UNICA com o delta descontado da media dos
# 100 candles anteriores: CVD ajustado = soma de (dv - vol x delta medio). Mesma
# regra e criterio do 69 no resto. Como veio depois do resultado, um PASSA aqui so
# autoriza papel.
def sinais_cvd_aj(b):
    out = []
    for i in range(119, len(b) - 1):
        ant = b[i - 119:i - 19]
        md = sum(x[6] for x in ant) / sum(x[5] for x in ant) if sum(x[5] for x in ant) > 0 else 0.0
        jan = b[i - 19:i + 1]
        cvd = sum(x[6] - x[5] * md for x in jan)
        if b[i][2] >= max(x[2] for x in jan) and cvd < 0:
            out.append((i, -1, b[i][3], b[i][2]))
        elif b[i][3] <= min(x[3] for x in jan) and cvd > 0:
            out.append((i, +1, b[i][2], b[i][3]))
    return out


def main_69b():
    t0 = time.time()
    syms = T.simbolos()
    with ThreadPoolExecutor(16) as ex:
        vols = dict(zip(syms, ex.map(T.diario, syms)))
    vols = {s: v for s, v in vols.items() if v}
    T.TOP = S.TOP
    rk = T.ranking(vols)
    alguma = sorted({s for d, v in rk.items() if F.INICIO <= d < F.FIM for s in v})
    rng = random.Random(SEED)
    res = {tf: [] for tf in S.TFS}
    S.barras, E.sinais_div = barras, sinais_cvd_aj
    for s in alguma:
        ms = S.meses(s, rk)
        h1 = {}
        for mm in ms:
            h1.update({ts: v for ts, v in F.klines_mes("futures/um", s, mm).items() if v[0] > 0})
        if not h1:
            continue
        fund = []
        for mm in ms:
            fp = os.path.join(D.DIR_VISION, f"funding_{s}_{mm}.json")
            if os.path.exists(fp):
                fund += [tuple(x) for x in json.load(open(fp))]
        fund.sort()
        E.rodar("DIV", h1, fund, s, rk, rng, res)
    P.relatorio("ESTUDO 69b DIVERGENCIA DE CVD AJUSTADO", res)
    for tf, xs in res.items():
        ex = F.boot(xs, "excesso", 0.95)
        rb = sum(t["r_bruto"] for t in xs) / len(xs) if xs else float("nan")
        ok = ex and ex[3] >= 200 and ex[1] > 0 and rb > 0
        print(f"  funil 69b {tf}: excesso {F.fmt(ex)} | bruto {rb:+.3f}R -> {'CANDIDATO' if ok else 'nao'}")
    print(f"\n[{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main_69b() if sys.argv[1:] == ["69b"] else main(sys.argv[1:])
