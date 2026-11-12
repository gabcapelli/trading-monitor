"""
Estudos 80 (9.2), 81 (9.3), 82 (9.4), 83 (rompimento de volatilidade de Larry
Williams) e 84 (Bollinger: fechou fora, fechou dentro).
PRE-REGISTRADOS em 12/11/2026, antes de rodar. Tentativa unica cada, mesma regua
dos estudos 57-59 e 63-67 (replay_nr7_pfr.py / replay_div_engolfo.py), sem grade
e sem ajuste de parametro depois de ver o resultado.

UNIVERSO, DADOS, EXECUCAO E CRITERIO: iguais aos do estudo 59: perpetuos USDT-M
cripto da Binance, inclusive deslistados, entre os 50 de maior volume no dia do
sinal, 2020-01 a 2026-09; 1h agregado em 4h e 1d (UTC); stop e alvo checados em
1h; custo 0.18% + funding real; 1R minimo de 0.3%; um trade por vez por simbolo
e tempo grafico; placebo com o mesmo risco %; IC 97.5%.

ESTUDOS 80-82 e 84: compra stop na maxima do candle do sinal, valida so durante
o candle seguinte (espelho na venda). Alvo 2R. Saida na abertura do 11o candle
depois do sinal. (O 9.x original conduz pela media; aqui vale a regua comum.)
MME9 = media exponencial de 9 dos fechamentos; "subindo" = MME9[i] > MME9[i-1].

ESTUDO 80 -- 9.2
- Compra: MME9 subindo em i e fechamento[i] < minima[i-1]. Stop na minima de i.
- Venda: MME9 caindo em i e fechamento[i] > maxima[i-1]. Stop na maxima de i.

ESTUDO 81 -- 9.3
- Compra: MME9 subindo em i; fechamento[i-1] < fechamento[i-2] e
  fechamento[i] < fechamento[i-2] (dois fechamentos seguidos abaixo do
  fechamento de referencia). Stop em min(minima[i-1], minima[i]).
- Venda no espelho.

ESTUDO 82 -- 9.4 (o 9.1 de venda que falha)
- Compra: a MME9 vinha subindo e vira para baixo em j (MME9[j] < MME9[j-1],
  MME9[j-1] >= MME9[j-2]); segue caindo ate i-1; nenhum candle de j+1 a i perde
  a minima de j (a venda do 9.1 nao arma); em i a media vira para cima
  (MME9[i] > MME9[i-1]). Stop na minima de j.
- Venda no espelho.

ESTUDO 84 -- BOLLINGER, FECHOU FORA FECHOU DENTRO (20 periodos, 2 desvios)
- Compra: fechamento[i-1] < banda inferior[i-1] e fechamento[i] > banda
  inferior[i]. Stop em min(minima[i-1], minima[i]).
- Venda no espelho (banda superior).

ESTUDO 83 -- ROMPIMENTO DE VOLATILIDADE (Larry Williams), k = 0.5
- Todo candle i com amplitude > 0 arma o candle seguinte: compra stop em
  abertura[i+1] + 0.5 x amplitude[i] e venda stop em abertura[i+1] - 0.5 x
  amplitude[i] (OCO; o primeiro tocado vale; os dois na mesma hora = sem trade).
- Stop na abertura do candle de entrada (1R = 0.5 x amplitude). Alvo 2R. Saida
  na abertura do candle seguinte ao de entrada (como o NR7 do estudo 58).
- Como todo candle e sinal, o placebo nao exclui candles com sinal: e a entrada
  a mercado na abertura de candles ao acaso, mesmo lado, risco % e duracao.

CRITERIO (por estudo; duas celulas, 1d e 4h; todos juntos por celula)
1. n >= 200.
2. R liquido medio com IC97.5 inteiro > 0 (bootstrap por semana).
3. Excesso sobre placebo com IC97.5 > 0.
4. R liquido medio > 0 nas duas metades.

Uso (de dentro de monitor/):
    python replay_lw_bollinger.py
"""

import json
import os
import random
import sys
import time
from concurrent.futures import ThreadPoolExecutor

import replay_continuacao_top20 as T
import replay_deslistagem as D
import replay_fluxo_spot_perp as F
import replay_nr7_pfr as P
import replay_sfp as S

DIA, H = S.DIA, S.H
SEED = 42
K_VOL = 0.5
AQUEC = 40                                             # candles de aquecimento da MME9


def mme(b, n=9):
    k, out = 2 / (n + 1), [b[0][4]]
    for x in b[1:]:
        out.append(out[-1] + k * (x[4] - out[-1]))
    return out


def sinais_92(b):
    m, out = mme(b), []
    for i in range(AQUEC, len(b) - 1):
        if m[i] > m[i - 1] and b[i][4] < b[i - 1][3]:
            out.append((i, +1, b[i][2], b[i][3]))
        elif m[i] < m[i - 1] and b[i][4] > b[i - 1][2]:
            out.append((i, -1, b[i][3], b[i][2]))
    return out


def sinais_93(b):
    m, out = mme(b), []
    for i in range(AQUEC, len(b) - 1):
        ref = b[i - 2][4]
        if m[i] > m[i - 1] and b[i - 1][4] < ref and b[i][4] < ref:
            out.append((i, +1, b[i][2], min(b[i - 1][3], b[i][3])))
        elif m[i] < m[i - 1] and b[i - 1][4] > ref and b[i][4] > ref:
            out.append((i, -1, b[i][3], max(b[i - 1][2], b[i][2])))
    return out


def sinais_94(b):
    m, out = mme(b), []
    for i in range(AQUEC, len(b) - 1):
        if m[i] > m[i - 1] and m[i - 1] < m[i - 2]:      # virou para cima em i
            j = i - 1
            while j > 2 and m[j - 1] < m[j - 2]:
                j -= 1                                   # j = candle em que a media virou para baixo
            if m[j - 1] > m[j - 2] and all(b[k][3] >= b[j][3] for k in range(j + 1, i + 1)) \
                    and b[i][2] > b[j][3]:
                out.append((i, +1, b[i][2], b[j][3]))
        elif m[i] < m[i - 1] and m[i - 1] > m[i - 2]:
            j = i - 1
            while j > 2 and m[j - 1] > m[j - 2]:
                j -= 1
            if m[j - 1] < m[j - 2] and all(b[k][2] <= b[j][2] for k in range(j + 1, i + 1)) \
                    and b[i][3] < b[j][2]:
                out.append((i, -1, b[i][3], b[j][2]))
    return out


def sinais_fffd(b, n=20, d=2.0):
    c = [x[4] for x in b]

    def bandas(i):
        xs = c[i - n + 1:i + 1]
        mu = sum(xs) / n
        sd = (sum((x - mu) ** 2 for x in xs) / n) ** 0.5
        return mu - d * sd, mu + d * sd

    out = []
    for i in range(n, len(b) - 1):
        (inf0, sup0), (inf1, sup1) = bandas(i - 1), bandas(i)
        if c[i - 1] < inf0 and c[i] > inf1:
            out.append((i, +1, b[i][2], min(b[i - 1][3], b[i][3])))
        elif c[i - 1] > sup0 and c[i] < sup1:
            out.append((i, -1, b[i][3], max(b[i - 1][2], b[i][2])))
    return out


ESTUDOS = {"92": sinais_92, "93": sinais_93, "94": sinais_94, "FFFD": sinais_fffd}


def rodar(fn, h1, fund, s, rk, rng, res):
    """Regua do 59/63: entrada por stop no candle seguinte, alvo 2R, saida no 11o candle."""
    for tf, horas in S.TFS.items():
        b = S.barras(h1, horas)
        sig = fn(b)
        com_sinal = {x[0] for x in sig}
        livre = 0
        for i, lado, nivel, stop_px in sig:
            t = b[i][0]
            if s not in rk.get(t // DIA * DIA, ()) or not (F.INICIO <= t < F.FIM):
                continue
            t0, t1 = b[i + 1][0], b[i + 1][0] + horas * H
            if t0 < livre:
                continue
            p = P.preencher(h1, t0, t1, lado, nivel)
            if p is None:
                continue
            ts, e = p
            fim = t + 11 * horas * H
            y = P.resultado(h1, fund, ts, e, lado, stop_px, fim)
            if y is None:
                continue
            exc = P.placebo(h1, fund, b, i, lado, y["risco"], fim - ts, com_sinal, rng, horas)
            res[tf].append({"sym": s, "ent": ts, "lado": lado, "risco": y["risco"], "r": y["r"],
                            "r_bruto": y["r_bruto"], "excesso": y["r"] - exc if exc is not None else None})
            livre = y["sai"]


def rodar_vol(h1, fund, s, rk, rng, res):
    for tf, horas in S.TFS.items():
        b = S.barras(h1, horas)
        livre = 0
        for i in range(1, len(b) - 1):
            t = b[i][0]
            amp = b[i][2] - b[i][3]
            if amp <= 0 or s not in rk.get(t // DIA * DIA, ()) or not (F.INICIO <= t < F.FIM):
                continue
            t0, t1 = b[i + 1][0], b[i + 1][0] + horas * H
            if t0 < livre or b[i + 1][0] != t + horas * H:   # sem buraco entre o sinal e a entrada
                continue
            ab = b[i + 1][1]
            o = P.oco(h1, t0, t1, ab + K_VOL * amp, ab - K_VOL * amp)
            if o is None:
                continue
            lado, ts, e = o
            y = P.resultado(h1, fund, ts, e, lado, ab, t1)
            if y is None:
                continue
            exc = P.placebo(h1, fund, b, i, lado, y["risco"], t1 - ts, (), rng, horas)
            res[tf].append({"sym": s, "ent": ts, "lado": lado, "risco": y["risco"], "r": y["r"],
                            "r_bruto": y["r_bruto"], "excesso": y["r"] - exc if exc is not None else None})
            livre = y["sai"]


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
    res = {e: {tf: [] for tf in S.TFS} for e in list(ESTUDOS) + ["VOL"]}
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
        for e, fn in ESTUDOS.items():
            rodar(fn, h1, fund, s, rk, rng, res[e])
        rodar_vol(h1, fund, s, rk, rng, res["VOL"])
    P.relatorio("ESTUDO 80 9.2", res["92"])
    P.relatorio("ESTUDO 81 9.3", res["93"])
    P.relatorio("ESTUDO 82 9.4", res["94"])
    P.relatorio("ESTUDO 83 ROMPIMENTO DE VOLATILIDADE", res["VOL"])
    P.relatorio("ESTUDO 84 BOLLINGER FFFD", res["FFFD"])
    print(f"\n[{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main(sys.argv[1:])
