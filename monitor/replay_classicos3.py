"""
Estudos 88 (Holy Grail, Linda Raschke), 89 (Double 7s, Larry Connors) e 90 (TTM
Squeeze, John Carter). PRE-REGISTRADOS em 13/11/2026, antes de rodar. Tentativa
unica cada, mesma regua dos estudos 57-59, 63-67 e 80-84, sem grade e sem ajuste
de parametro depois de ver o resultado. Fecham a lista de classicos de grafico.

UNIVERSO, DADOS, EXECUCAO E CRITERIO: iguais aos do estudo 59 e do 80-84:
perpetuos USDT-M cripto da Binance, inclusive deslistados, entre os 50 de maior
volume no dia do sinal, 2020-01 a 2026-09; 1h agregado em 4h e 1d (UTC); stop e
alvo checados em 1h; custo 0.18% + funding real; 1R minimo de 0.3%; um trade por
vez por simbolo e tempo grafico; placebo com o mesmo risco %; IC 97.5%.
Unica diferenca de dados: carrega ate 230 dias antes da entrada no top 50, para
a media de 200 do estudo 89 existir (simbolo sem 200 candles nao da sinal).

EXECUCAO COMUM: compra stop na maxima do candle do sinal, valida so durante o
candle seguinte; stop na minima do candle do sinal (espelho na venda). Alvo 2R.
Saida na abertura do 11o candle depois do sinal. (As saidas originais de cada
autor nao sao usadas; vale a regua comum, como no 80-84.)

ESTUDO 88 -- HOLY GRAIL (ADX 14, MME 20)
- Compra: ADX[i] > 30, +DI[i] > -DI[i], minima[i] <= MME20[i] e
  minima[i-1] > MME20[i-1] (primeiro toque na media depois de ficar acima).
- Venda no espelho (-DI > +DI, maxima toca a media vindo de baixo).

ESTUDO 89 -- DOUBLE 7s (media simples de 200)
- Compra: fechamento[i] > MM200[i] e fechamento[i] e o menor dos ultimos 7
  fechamentos.
- Venda: fechamento[i] < MM200[i] e fechamento[i] e o maior dos ultimos 7.

ESTUDO 90 -- TTM SQUEEZE (Bollinger 20/2, Keltner 20/1.5 ATR simples de 20)
- Compressao em i: banda superior de Bollinger < Keltner superior e banda
  inferior > Keltner inferior.
- Sinal: compressao em i-1 e sem compressao em i (a compressao "solta").
- Lado: sinal de fechamento[i] - media de ((maxima20 + minima20)/2, MM20).
  Positivo compra, negativo vende, zero sem trade.

CRITERIO (por estudo; duas celulas, 1d e 4h; todos juntos por celula)
1. n >= 200.
2. R liquido medio com IC97.5 inteiro > 0 (bootstrap por semana).
3. Excesso sobre placebo com IC97.5 > 0.
4. R liquido medio > 0 nas duas metades.

Uso (de dentro de monitor/):
    python replay_classicos3.py
"""

import json
import os
import random
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

import replay_continuacao_top20 as T
import replay_deslistagem as D
import replay_fluxo_spot_perp as F
import replay_lw_bollinger as LW
import replay_nr7_pfr as P
import replay_sfp as S

DIA = S.DIA
SEED = 42
AQUEC = 60


def mme(c, n):
    k, out = 2 / (n + 1), [c[0]]
    for x in c[1:]:
        out.append(out[-1] + k * (x - out[-1]))
    return out


def adx(b, n=14):
    """Wilder. Devolve (adx, +di, -di), None enquanto nao ha dado."""
    N = len(b)
    out_adx, pdi, mdi = [None] * N, [None] * N, [None] * N
    if N < 2 * n + 2:
        return out_adx, pdi, mdi
    tr, pdm, mdm = [0.0], [0.0], [0.0]
    for i in range(1, N):
        h, l, pc = b[i][2], b[i][3], b[i - 1][4]
        up, dn = h - b[i - 1][2], b[i - 1][3] - l
        tr.append(max(h - l, abs(h - pc), abs(l - pc)))
        pdm.append(up if up > dn and up > 0 else 0.0)
        mdm.append(dn if dn > up and dn > 0 else 0.0)
    a, p, m = sum(tr[1:n + 1]), sum(pdm[1:n + 1]), sum(mdm[1:n + 1])
    dx = []
    for i in range(n, N):
        if i > n:
            a, p, m = a - a / n + tr[i], p - p / n + pdm[i], m - m / n + mdm[i]
        pdi[i], mdi[i] = (100 * p / a, 100 * m / a) if a > 0 else (0.0, 0.0)
        s = pdi[i] + mdi[i]
        dx.append(100 * abs(pdi[i] - mdi[i]) / s if s > 0 else 0.0)
        if len(dx) == n:
            out_adx[i] = sum(dx) / n
        elif len(dx) > n:
            out_adx[i] = (out_adx[i - 1] * (n - 1) + dx[-1]) / n
    return out_adx, pdi, mdi


def sinais_holy_grail(b):
    c = [x[4] for x in b]
    m, (ad, pdi, mdi), out = mme(c, 20), adx(b), []
    for i in range(AQUEC, len(b) - 1):
        if ad[i] is None or ad[i] <= 30:
            continue
        if pdi[i] > mdi[i] and b[i][3] <= m[i] and b[i - 1][3] > m[i - 1]:
            out.append((i, +1, b[i][2], b[i][3]))
        elif mdi[i] > pdi[i] and b[i][2] >= m[i] and b[i - 1][2] < m[i - 1]:
            out.append((i, -1, b[i][3], b[i][2]))
    return out


def sinais_double7(b):
    c, out = [x[4] for x in b], []
    soma = sum(c[:200])
    for i in range(199, len(b) - 1):
        if i > 199:
            soma += c[i] - c[i - 200]
        mm, jan = soma / 200, c[i - 6:i + 1]
        if c[i] > mm and c[i] == min(jan) and jan.count(c[i]) == 1:
            out.append((i, +1, b[i][2], b[i][3]))
        elif c[i] < mm and c[i] == max(jan) and jan.count(c[i]) == 1:
            out.append((i, -1, b[i][3], b[i][2]))
    return out


def sinais_squeeze(b, n=20):
    c = [x[4] for x in b]
    tr = [b[0][2] - b[0][3]] + [max(b[i][2] - b[i][3], abs(b[i][2] - c[i - 1]), abs(b[i][3] - c[i - 1]))
                                for i in range(1, len(b))]

    def estado(i):
        xs = c[i - n + 1:i + 1]
        mu = sum(xs) / n
        sd = (sum((x - mu) ** 2 for x in xs) / n) ** 0.5
        atr = sum(tr[i - n + 1:i + 1]) / n
        return mu, (mu + 2 * sd < mu + 1.5 * atr and mu - 2 * sd > mu - 1.5 * atr)

    out, antes = [], None
    for i in range(n, len(b) - 1):
        mu, comp = estado(i)
        if antes and not comp and i >= AQUEC:
            jan = b[i - n + 1:i + 1]
            ref = ((max(x[2] for x in jan) + min(x[3] for x in jan)) / 2 + mu) / 2
            if c[i] > ref:
                out.append((i, +1, b[i][2], b[i][3]))
            elif c[i] < ref:
                out.append((i, -1, b[i][3], b[i][2]))
        antes = comp
    return out


ESTUDOS = {"HOLY": sinais_holy_grail, "D7": sinais_double7, "SQZ": sinais_squeeze}


def meses(sym, rk):
    """Como S.meses, mas com 230 dias de historico antes (media de 200 no diario)."""
    ms = set()
    for d, s in rk.items():
        if sym in s and F.INICIO <= d < F.FIM:
            for k in range(-230, 13, 2):
                ms.add(datetime.fromtimestamp((d + k * DIA) / 1000, timezone.utc).strftime("%Y-%m"))
    return sorted(m for m in ms if "2019-09" <= m <= "2026-09")


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
    res = {e: {tf: [] for tf in S.TFS} for e in ESTUDOS}
    for s in alguma:
        ms = meses(s, rk)
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
        for e, fn in ESTUDOS.items():
            LW.rodar(fn, h1, fund, s, rk, rng, res[e])
    P.relatorio("ESTUDO 88 HOLY GRAIL", res["HOLY"])
    P.relatorio("ESTUDO 89 DOUBLE 7S", res["D7"])
    P.relatorio("ESTUDO 90 TTM SQUEEZE", res["SQZ"])
    print(f"\n[{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main(sys.argv[1:])
