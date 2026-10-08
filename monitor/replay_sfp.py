"""
Estudo 57 -- SFP / Turtle Soup: o rompimento falso de maxima ou minima.
PRE-REGISTRADO em 08/10/2026, antes de rodar.

HIPOTESE
--------
Em cripto (alavancado), os stops se amontoam logo alem das maximas e minimas.
Um candle que fura a minima (maxima) de 20 candles e FECHA de volta para dentro
consumiu esse estoque e tende a reverter. Turtle Soup da Linda Raschke ("Street
Smarts", 1995); em cripto, "swing failure pattern". O estudo 46 olhou rompimentos
que fecham fora (continuam); os que falham nunca foram testados.

UNIVERSO (point-in-time, como os estudos 46 e 55)
-------------------------------------------------
Perpetuos USDT-M cripto da Binance, inclusive deslistados, entre os 50 de maior
volume (30 dias anteriores) no dia do sinal. 2020-01 a 2026-09. Candles de 1h do
vision (cache do estudo 55), agregados em 4h e 1d (UTC).

SINAL (parametros da Raschke, fixos)
------------------------------------
Compra (venda e o espelho):
- minima do candle < minima dos 20 candles anteriores;
- essa minima anterior foi feita ha pelo menos 4 candles (Raschke);
- o candle FECHA acima da minima anterior (o rompimento falhou).
Entrada na abertura do candle seguinte. Stop 1 tick abaixo do pavio (a minima do
candle do sinal); 1R = entrada - stop, minimo de 0.3%. Alvo 2R. Sem toque: sai na
abertura do 11o candle (10 candles depois da entrada). Stop e alvo sao checados
em barras de 1h; os dois na mesma hora = stop.
Custo 0.18% ida e volta + funding real. Um trade por vez por simbolo e tempo grafico.

DUAS CELULAS (1d e 4h), decididas em separado, IC 97.5% (Bonferroni).

CRITERIO (fixado antes; por celula; todos juntos)
-------------------------------------------------
1. n >= 200.
2. R liquido medio com IC97.5 inteiro > 0 (bootstrap por semana).
3. Excesso sobre placebo com IC97.5 > 0. Placebo: mesmo simbolo, mesmo lado,
   MESMO risco em %, mesma regra de stop/alvo/tempo, entrada em 5 candles
   aleatorios a ate 30 dias, sem sinal no candle anterior (risco igual = custo em
   R igual: evita o artefato do estudo 56).
4. R liquido medio > 0 nas duas metades do periodo.
Descritivo: compras e vendas, por ano, fora das 20 majors de hoje.

Uso (de dentro de monitor/):
    python replay_sfp.py --baixar
    python replay_sfp.py
"""

import math
import random
import sys
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

import replay_continuacao as C
import replay_continuacao_top20 as T
import replay_deslistagem as D
import replay_fluxo_spot_perp as F

DIA = 86_400_000
H = 3_600_000
TOP = 50
N, IDADE = 20, 4
ALVO_R, SAIDA, MIN_RISCO = 2.0, 10, 0.003
CUSTO = 0.18
N_PLACEBO, SEED = 5, 42
TFS = {"1d": 24, "4h": 4}


def meses(sym, rk):
    ms = set()
    for d, s in rk.items():
        if sym in s and F.INICIO <= d < F.FIM:
            for k in range(-26, 13, 2):
                ms.add(datetime.fromtimestamp((d + k * DIA) / 1000, timezone.utc).strftime("%Y-%m"))
    return sorted(m for m in ms if "2019-11" <= m <= "2026-09")


def barras(h1, horas):
    g = defaultdict(list)
    for ts in sorted(h1):
        g[ts // (horas * H) * horas * H].append(h1[ts])
    out = []
    for t in sorted(g):
        xs = g[t]
        if len(xs) < horas:
            continue
        out.append((t, xs[0][0], max(x[1] for x in xs), min(x[2] for x in xs), xs[-1][3]))
    return out


def sinais(b):
    out = []
    for i in range(N, len(b) - 1):
        if b[i][0] - b[i - N][0] != N * (b[1][0] - b[0][0]):
            continue
        jan = b[i - N:i]
        lo = min(x[3] for x in jan)
        hi = max(x[2] for x in jan)
        k_lo = max(j for j, x in enumerate(jan) if x[3] == lo)
        k_hi = max(j for j, x in enumerate(jan) if x[2] == hi)
        t, o, h, l, c = b[i]
        if l < lo and c > lo and N - k_lo >= IDADE:
            out.append((i, +1, l))
        elif h > hi and c < hi and N - k_hi >= IDADE:
            out.append((i, -1, h))
    return out


def simular(h1, fund, ent, lado, risco, dur):
    if ent not in h1:
        return None
    e = h1[ent][0]
    stop, alvo = e * (1 - lado * risco), e * (1 + lado * ALVO_R * risco)
    sai, bruto = ent + dur, None
    for k in range(dur // H):
        x = h1.get(ent + k * H)
        if x is None:
            return None
        if (x[2] <= stop) if lado > 0 else (x[1] >= stop):
            bruto, sai = -risco * 100, ent + (k + 1) * H
            break
        if (x[1] >= alvo) if lado > 0 else (x[2] <= alvo):
            bruto, sai = ALVO_R * risco * 100, ent + (k + 1) * H
            break
    if bruto is None:
        x = h1.get(sai)
        if x is None:
            return None
        bruto = lado * 100 * (x[0] / e - 1)
    f = -lado * 100 * sum(r for ts, r in fund if ent <= ts < sai)
    return {"r": (bruto - CUSTO + f) / (risco * 100), "r_bruto": bruto / (risco * 100), "sai": sai}


def main(argv):
    t0 = time.time()
    syms = T.simbolos()
    with ThreadPoolExecutor(16) as ex:
        vols = dict(zip(syms, ex.map(T.diario, syms)))
    vols = {s: v for s, v in vols.items() if v}
    T.TOP = TOP
    rk = T.ranking(vols)
    alguma = sorted({s for d, v in rk.items() if F.INICIO <= d < F.FIM for s in v})
    tarefas = [(s, m) for s in alguma for m in meses(s, rk)]
    print(f"simbolos {len(alguma)} | arquivos {len(tarefas)}", flush=True)
    with ThreadPoolExecutor(48) as ex:
        list(ex.map(lambda a: F.klines_mes("futures/um", *a), tarefas))
    print(f"dados ok [{time.time()-t0:.0f}s]", flush=True)
    if "--baixar" in argv:
        return

    rng = random.Random(SEED)
    res = {tf: [] for tf in TFS}
    for s in alguma:
        h1 = {}
        for m in meses(s, rk):
            h1.update({ts: v[:4] for ts, v in F.klines_mes("futures/um", s, m).items() if v[0] > 0})
        if not h1:
            continue
        D.funding(s, F.INICIO - 40 * DIA, F.FIM)
        fund = []
        import json, os
        for m in meses(s, rk):
            fp = os.path.join(D.DIR_VISION, f"funding_{s}_{m}.json")
            if os.path.exists(fp):
                fund += [tuple(x) for x in json.load(open(fp))]
        fund.sort()
        for tf, horas in TFS.items():
            b = barras(h1, horas)
            sig = sinais(b)
            com_sinal = {i for i, _, _ in sig}
            dur = SAIDA * horas * H
            livre = 0
            for i, lado, pavio in sig:
                t = b[i][0]
                ent = b[i + 1][0]
                if ent < livre or s not in rk.get(t // DIA * DIA, ()) or not (F.INICIO <= t < F.FIM):
                    continue
                e = h1.get(ent, [None])[0]
                if not e:
                    continue
                risco = max(lado * (e - pavio) / e, MIN_RISCO)
                x = simular(h1, fund, ent, lado, risco, dur)
                if x is None:
                    continue
                pl = []
                for _ in range(40):
                    if len(pl) >= N_PLACEBO:
                        break
                    j = i + rng.randint(-30 * 24 // horas, 30 * 24 // horas)
                    if j < 1 or j + 1 >= len(b) or j in com_sinal or j == i:
                        continue
                    y = simular(h1, fund, b[j + 1][0], lado, risco, dur)
                    if y:
                        pl.append(y["r"])
                res[tf].append({"sym": s, "ent": ent, "lado": lado, "risco": risco, "r": x["r"],
                                "r_bruto": x["r_bruto"], "excesso": x["r"] - sum(pl) / len(pl) if pl else None})
                livre = x["sai"]

    m = lambda v: sum(v) / len(v) if v else float("nan")
    for tf, xs in res.items():
        meio = sorted(t["ent"] for t in xs)[len(xs) // 2]
        b, ex = F.boot(xs, "r"), F.boot(xs, "excesso")
        h1m, h2m = m([t["r"] for t in xs if t["ent"] < meio]), m([t["r"] for t in xs if t["ent"] >= meio])
        print("\n" + "=" * 90 + f"\nSFP {tf}\n" + "=" * 90)
        print(f"  R liquido  {F.fmt(b)}")
        print(f"  excesso    {F.fmt(ex)}")
        print(f"  R bruto {m([t['r_bruto'] for t in xs]):+.3f}R | risco medio {m([t['risco'] for t in xs])*100:.2f}%"
              f" | acerto {m([t['r'] > 0 for t in xs])*100:.1f}%")
        print(f"  metades: 1a {h1m:+.3f}R | 2a {h2m:+.3f}R")
        for lado, nm in ((1, "compras"), (-1, "vendas")):
            print(f"  {nm:<8} {F.fmt(F.boot([t for t in xs if t['lado'] == lado], 'r', 0.95))}")
        fora = [t for t in xs if t["sym"] not in C.MAJORS]
        print(f"  fora das majors {F.fmt(F.boot(fora, 'r', 0.95))}")
        pa = defaultdict(list)
        for t in xs:
            pa[datetime.fromtimestamp(t["ent"] / 1000, timezone.utc).year].append(t["r"])
        print("  por ano: " + " | ".join(f"{a} {m(v):+.2f} ({len(v)})" for a, v in sorted(pa.items())))
        ok = b and ex and b[3] >= 200 and b[1] > 0 and ex[1] > 0 and h1m > 0 and h2m > 0
        print(f"  DECISAO {tf}: {'PASSA' if ok else 'NAO PASSA'}")
    print(f"\n[{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main(sys.argv[1:])
