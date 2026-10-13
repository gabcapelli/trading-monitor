"""
Estudos 66 (Ponto Continuo) e 67 (rompimento da nuvem do Ichimoku).
PRE-REGISTRADOS em 13/10/2026, antes de rodar. Tentativa unica cada, mesma regua
dos estudos 57-59 e 63-65 (replay_div_engolfo.py).

UNIVERSO, DADOS, EXECUCAO E CRITERIO: iguais aos do estudo 59 (replay_nr7_pfr.py):
top 50 de volume do dia, 2020-01 a 2026-09, 1d e 4h, stop e alvo checados em 1h,
custo 0.18% + funding, placebo com o mesmo risco %, IC 97.5%. Entrada por stop no
rompimento do candle do sinal, valida so no candle seguinte; alvo 2R; saida na
abertura do 11o candle depois do sinal; 1R minimo 0.3%.

ESTUDO 66 -- PONTO CONTINUO (recuo ate a MM21 em tendencia; venda no espelho)
- MM21 dos fechamentos subindo (MM21[i] > MM21[i-1]); o candle i toca a media
  (minima <= MM21[i]) e fecha acima dela.
- Compra stop na maxima de i. Stop na minima de i.

ESTUDO 67 -- ICHIMOKU, ROMPIMENTO DA NUVEM (parametros 9/26/52; venda no espelho)
- Nuvem no candle i: Senkou A = (Tenkan + Kijun)/2 e Senkou B = ponto medio de 52
  candles, ambos calculados em i-26.
- Sinal: fechamento[i] acima do topo da nuvem e fechamento[i-1] nao estava acima;
  Tenkan[i] > Kijun[i]; Chikou acima do preco (fechamento[i] > fechamento[i-26]).
- Compra stop na maxima de i. Stop na Kijun[i]; sem trade se a Kijun nao estiver
  abaixo da maxima de i.

Uso (de dentro de monitor/):
    python replay_pc_ichimoku.py
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


def sinais_pc(b):
    c = [x[4] for x in b]
    out = []
    for i in range(21, len(b) - 1):
        mm, mm_ant = sum(c[i - 20:i + 1]) / 21, sum(c[i - 21:i]) / 21
        h, l, f = b[i][2], b[i][3], b[i][4]
        if mm > mm_ant and l <= mm < f:
            out.append((i, +1, h, l))
        elif mm < mm_ant and h >= mm > f:
            out.append((i, -1, l, h))
    return out


def meio(b, i, n):
    xs = b[i - n + 1:i + 1]
    return (max(x[2] for x in xs) + min(x[3] for x in xs)) / 2


def sinais_ichi(b):
    out = []
    ten = lambda i: meio(b, i, 9)
    kij = lambda i: meio(b, i, 26)

    def nuvem(i):
        j = i - 26
        a, bb = (ten(j) + kij(j)) / 2, meio(b, j, 52)
        return max(a, bb), min(a, bb)

    for i in range(26 + 52, len(b) - 1):
        f, f_ant = b[i][4], b[i - 1][4]
        topo, base = nuvem(i)
        topo_ant, base_ant = nuvem(i - 1)
        t, k = ten(i), kij(i)
        if f > topo and not f_ant > topo_ant and t > k and f > b[i - 26][4] and k < b[i][2]:
            out.append((i, +1, b[i][2], k))
        elif f < base and not f_ant < base_ant and t < k and f < b[i - 26][4] and k > b[i][3]:
            out.append((i, -1, b[i][3], k))
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
    estudos = {"PC": sinais_pc, "ICHI": sinais_ichi}
    res = {e: {tf: [] for tf in S.TFS} for e in estudos}
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
        for e, fn in estudos.items():
            E.sinais_div = fn                             # rodar() do 63 com o sinal deste estudo
            E.rodar("DIV", h1, fund, s, rk, rng, res[e])
    P.relatorio("ESTUDO 66 PONTO CONTINUO", res["PC"])
    P.relatorio("ESTUDO 67 ICHIMOKU NUVEM", res["ICHI"])
    print(f"\n[{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main(sys.argv[1:])
