"""
Estudos 70 (top traders contra o varejo) e 71 (varejo extremo, contrario) -- a
proporcao de comprados/vendidos da Binance (metrics da Binance Vision, desde 2020-09;
baixar_metrics.py). PRE-REGISTRADOS em 13/10/2026, antes de rodar e antes de olhar
os dados (so o parser foi conferido). Tentativa unica cada.

UNIVERSO, EXECUCAO E CRITERIO: iguais aos do estudo 59 (replay_nr7_pfr.py), mas o
periodo comeca em 2020-10 (o dado existe desde 2020-09 e o z-score precisa de 30
dias): top 50 de volume do dia, 1d e 4h, stop e alvo checados em 1h, custo 0.18% +
funding, placebo com o mesmo risco %, IC 97.5%. Entrada por stop no rompimento do
candle do sinal, valida so no candle seguinte; stop no outro extremo do candle;
alvo 2R; saida na abertura do 11o candle depois do sinal; 1R minimo 0.3%.

LEITURA DO CANDLE: o ultimo registro de 5 min da ultima hora do candle (estado
5 min antes do fechamento). Sem registro nessa hora = sem sinal. z-score contra os
30 dias anteriores ao candle (30 candles no 1d, 180 no 4h), exigindo >= 80% deles.

ESTUDO 70 -- TOP TRADERS CONTRA O VAREJO
- Mecanismo: os maiores saldos da Binance posicionados de um lado e a massa de
  contas do outro; quem tem mais capital costuma estar do lado certo.
- X = ln(top_posicoes) - ln(contas). Compra se z(X) >= +2 (top traders muito mais
  comprados que o varejo, em relacao ao normal da moeda); venda se z(X) <= -2.

ESTUDO 71 -- VAREJO EXTREMO, CONTRARIO
- Mecanismo: excesso de contas compradas = posicao lotada, combustivel para
  liquidacao em queda.
- X = ln(contas). Venda se z(X) >= +2; compra se z(X) <= -2.

FUNIL PARA O PAPEL (descritivo, proposto em 13/10/2026): R bruto > 0, excesso
com IC95 > 0 e n >= 200.

Uso (de dentro de monitor/):
    python replay_ls_ratio.py
"""

import json
import math
import os
import random
import statistics
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

import baixar_metrics as B
import replay_continuacao_top20 as T
import replay_deslistagem as D
import replay_div_engolfo as E
import replay_fluxo_spot_perp as F
import replay_nr7_pfr as P
import replay_sfp as S

H = S.H
SEED = 42
F.INICIO = int(datetime(2020, 10, 1, tzinfo=timezone.utc).timestamp() * 1000)


def serie(b, met, horas, campo):
    """Valor X por candle (None se faltar)."""
    out = []
    for x in b:
        m = met.get(x[0] + (horas - 1) * H)
        v = campo(m) if m else None
        out.append(v)
    return out


def x_70(m):
    if m[2] and m[3] and m[2] > 0 and m[3] > 0:
        return math.log(m[2]) - math.log(m[3])
    return None


def x_71(m):
    return math.log(m[3]) if m[3] and m[3] > 0 else None


def fabrica(met, horas, campo, sentido):
    """sentido +1: z alto = compra (70); -1: z alto = venda (71)."""
    n = 30 * 24 // horas

    def sinais(b):
        xs = serie(b, met, horas, campo)
        out = []
        for i in range(n, len(b) - 1):
            if xs[i] is None:
                continue
            jan = [v for v in xs[i - n:i] if v is not None]
            if len(jan) < 0.8 * n:
                continue
            sd = statistics.pstdev(jan)
            if sd == 0:
                continue
            z = (xs[i] - sum(jan) / len(jan)) / sd
            lado = sentido if z >= 2 else -sentido if z <= -2 else 0
            if lado > 0:
                out.append((i, +1, b[i][2], b[i][3]))
            elif lado < 0:
                out.append((i, -1, b[i][3], b[i][2]))
        return out
    return sinais


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
    estudos = {"70": (x_70, +1), "71": (x_71, -1)}
    res = {e: {tf: [] for tf in S.TFS} for e in estudos}
    sem_dado = 0
    for s in alguma:
        ms = S.meses(s, rk)
        met = B.carregar(s, ms)
        if not met:
            sem_dado += 1
            continue
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
        for e, (campo, sentido) in estudos.items():
            for tf, horas in S.TFS.items():
                E.sinais_div = fabrica(met, horas, campo, sentido)
                tfs, S.TFS = S.TFS, {tf: horas}
                E.rodar("DIV", h1, fund, s, rk, rng, res[e])
                S.TFS = tfs
    print(f"simbolos sem metrics: {sem_dado} de {len(alguma)}")
    P.relatorio("ESTUDO 70 TOP TRADERS CONTRA O VAREJO", res["70"])
    P.relatorio("ESTUDO 71 VAREJO EXTREMO CONTRARIO", res["71"])
    print("\nFunil para o papel (descritivo; R bruto > 0, excesso IC95 > 0, n >= 200):")
    for e in estudos:
        for tf, xs in res[e].items():
            ex = F.boot(xs, "excesso", 0.95)
            rb = sum(t["r_bruto"] for t in xs) / len(xs) if xs else float("nan")
            ok = ex and ex[3] >= 200 and ex[1] > 0 and rb > 0
            print(f"  {e} {tf}: excesso {F.fmt(ex)} | bruto {rb:+.3f}R -> {'CANDIDATO' if ok else 'nao'}")
    print(f"\n[{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main(sys.argv[1:])
