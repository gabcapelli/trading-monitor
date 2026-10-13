"""
Estudo 65 -- barra elefante a favor da tendencia.
PRE-REGISTRADO em 13/10/2026, antes de rodar. Tentativa unica, mesma regua dos
estudos 57-59 e 63-64 (replay_div_engolfo.py).

UNIVERSO, DADOS, EXECUCAO E CRITERIO: iguais aos do estudo 59 (replay_nr7_pfr.py):
top 50 de volume do dia, 2020-01 a 2026-09, 1d e 4h, stop e alvo checados em 1h,
custo 0.18% + funding, placebo com o mesmo risco %, IC 97.5%.

SINAL (compra; venda no espelho)
- Barra elefante em i: candle de alta, amplitude >= 2x a media das amplitudes dos
  20 candles anteriores e corpo >= 70% da amplitude.
- Tendencia: fechamento[i] acima da MM21 dos fechamentos e MM21[i] > MM21[i-1].
- Compra stop na maxima de i, valida so durante o candle seguinte. Stop na minima
  de i. Alvo 2R. Saida na abertura do 11o candle depois do sinal. 1R minimo 0.3%.

Uso (de dentro de monitor/):
    python replay_elefante.py
"""

import json
import os
import random
import sys
import time
from concurrent.futures import ThreadPoolExecutor

import replay_continuacao_top20 as T
import replay_deslistagem as D
import replay_div_engolfo as E
import replay_fluxo_spot_perp as F
import replay_nr7_pfr as P
import replay_sfp as S

SEED = 42


def sinais(b):
    c = [x[4] for x in b]
    out = []
    for i in range(21, len(b) - 1):
        o, h, l, f = b[i][1:5]
        amp = h - l
        media = sum(x[2] - x[3] for x in b[i - 20:i]) / 20
        if amp <= 0 or amp < 2 * media or abs(f - o) < 0.7 * amp:
            continue
        mm, mm_ant = sum(c[i - 20:i + 1]) / 21, sum(c[i - 21:i]) / 21
        if f > o and f > mm and mm > mm_ant:
            out.append((i, +1, h, l))
        elif f < o and f < mm and mm < mm_ant:
            out.append((i, -1, l, h))
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
    res = {tf: [] for tf in S.TFS}
    E.sinais_div = sinais                                 # rodar() do 63 com o sinal deste estudo
    for s in alguma:
        ms = S.meses(s, rk)
        h1 = {}
        for mm in ms:
            h1.update({ts: v[:5] for ts, v in F.klines_mes("futures/um", s, mm).items() if v[0] > 0})
        if not h1:
            continue
        fund = []
        for mm in ms:
            fp = os.path.join(D.DIR_VISION, f"funding_{s}_{mm}.json")
            if os.path.exists(fp):
                fund += [tuple(x) for x in json.load(open(fp))]
        fund.sort()
        E.rodar("DIV", h1, fund, s, rk, rng, res)
    P.relatorio("ESTUDO 65 BARRA ELEFANTE", res)
    print(f"\n[{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main(sys.argv[1:])
