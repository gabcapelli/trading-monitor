"""
Estudos 58 (NR7 do Crabel) e 59 (PFR) -- os dois ultimos setups classicos da fila.
PRE-REGISTRADOS em 08/10/2026, antes de rodar. Mesma regua do estudo 57.

UNIVERSO E DADOS: iguais ao estudo 57 (replay_sfp.py): perpetuos USDT-M cripto da
Binance, inclusive deslistados, entre os 50 de maior volume no dia do sinal,
2020-01 a 2026-09; 1h agregado em 4h e 1d (UTC); stop e alvo checados em 1h.

ENTRADA POR STOP (nos dois setups): a ordem fica valida so durante o candle
seguinte ao sinal. Preenche na primeira hora em que o preco toca o nivel, ao
preco max(nivel, abertura da hora) na compra (espelho na venda). Na hora da
entrada, se o preco tambem tocar o stop, conta como stop (conservador); o alvo
so vale a partir da hora seguinte.
1R = |entrada - stop|, minimo de 0.3%. Custo 0.18% + funding real. Um trade
por vez por simbolo e tempo grafico.

ESTUDO 58 -- NR7 (Toby Crabel, "Day Trading with Short Term Price Patterns", 1990)
- Sinal: a amplitude (max - min) do candle e a menor dos ultimos 7 (ele incluso).
- Candle seguinte: compra stop na maxima do NR7 e venda stop na minima (OCO; o
  primeiro tocado vale; os dois na mesma hora = sem trade, nao da para saber a ordem).
- Stop no outro extremo do NR7. Alvo 2R. Saida no fechamento do candle de
  entrada (regra do Crabel: o NR7 aposta na expansao do proprio dia).

ESTUDO 59 -- PFR (Preco de Fechamento de Reversao)
- Compra: minima < minima anterior E fechamento > fechamento anterior.
  Venda: maxima > maxima anterior E fechamento < fechamento anterior.
- Compra stop na maxima do candle do sinal (venda: na minima). Stop na minima
  (venda: maxima). Alvo 2R. Saida na abertura do 11o candle depois do sinal.

CRITERIO (por estudo; duas celulas, 1d e 4h, IC 97.5%; todos juntos por celula)
1. n >= 200.
2. R liquido medio com IC97.5 inteiro > 0 (bootstrap por semana).
3. Excesso sobre placebo com IC97.5 > 0. Placebo: mesmo simbolo, lado e risco %,
   entrada a mercado na abertura de 5 candles aleatorios a ate 30 dias, mesma
   regra de stop/alvo e mesma duracao.
4. R liquido medio > 0 nas duas metades.

Uso (de dentro de monitor/):
    python replay_nr7_pfr.py
"""

import json
import os
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
import replay_sfp as S

DIA, H = S.DIA, S.H
ALVO_R, MIN_RISCO, CUSTO = 2.0, 0.003, 0.18
N_PLACEBO, SEED = 5, 42


def sinais_nr7(b):
    out = []
    for i in range(6, len(b) - 1):
        amp = [x[2] - x[3] for x in b[i - 6:i + 1]]
        if amp[-1] > 0 and amp[-1] < min(amp[:-1]):
            out.append((i, 0, b[i][2], b[i][3]))          # lado 0 = OCO
    return out


def sinais_pfr(b):
    out = []
    for i in range(1, len(b) - 1):
        p, x = b[i - 1], b[i]
        if x[3] < p[3] and x[4] > p[4]:
            out.append((i, +1, x[2], x[3]))               # nivel de entrada, stop
        elif x[2] > p[2] and x[4] < p[4]:
            out.append((i, -1, x[3], x[2]))
    return out


def preencher(h1, t0, t1, lado, nivel):
    """Primeira hora em [t0, t1) que toca o nivel: (ts, preco). None se nao tocar."""
    for ts in range(t0, t1, H):
        x = h1.get(ts)
        if x is None:
            return None
        if lado > 0 and x[1] >= nivel:
            return ts, max(nivel, x[0])
        if lado < 0 and x[2] <= nivel:
            return ts, min(nivel, x[0])
    return None


def oco(h1, t0, t1, hi, lo):
    for ts in range(t0, t1, H):
        x = h1.get(ts)
        if x is None:
            return None
        a, b = x[1] >= hi, x[2] <= lo
        if a and b:
            return None
        if a:
            return +1, ts, max(hi, x[0])
        if b:
            return -1, ts, min(lo, x[0])
    return None


def resultado(h1, fund, ts, e, lado, stop_px, fim):
    """Da hora de entrada ts (preco e) ate fim (exclusive) ou stop/alvo."""
    risco = max(lado * (e - stop_px) / e, MIN_RISCO)
    stop, alvo = e * (1 - lado * risco), e * (1 + lado * ALVO_R * risco)
    bruto, sai = None, fim
    for k, t in enumerate(range(ts, fim, H)):
        x = h1.get(t)
        if x is None:
            return None
        if (x[2] <= stop) if lado > 0 else (x[1] >= stop):
            bruto, sai = -risco * 100, t + H
            break
        if k > 0 and ((x[1] >= alvo) if lado > 0 else (x[2] <= alvo)):
            bruto, sai = ALVO_R * risco * 100, t + H
            break
    if bruto is None:
        x = h1.get(fim)
        if x is None:
            return None
        bruto = lado * 100 * (x[0] / e - 1)
    f = -lado * 100 * sum(r for t, r in fund if ts <= t < sai)
    return {"r": (bruto - CUSTO + f) / (risco * 100), "r_bruto": bruto / (risco * 100), "risco": risco, "sai": sai}


def placebo(h1, fund, b, i, lado, risco, dur, com_sinal, rng, horas):
    pl = []
    for _ in range(40):
        if len(pl) >= N_PLACEBO:
            break
        j = i + rng.randint(-30 * 24 // horas, 30 * 24 // horas)
        if j < 1 or j + 1 >= len(b) or j in com_sinal or j == i:
            continue
        ts = b[j + 1][0]
        if ts not in h1:
            continue
        e = h1[ts][0]
        y = resultado(h1, fund, ts, e, lado, e * (1 - lado * risco), ts + dur)
        if y:
            pl.append(y["r"])
    return sum(pl) / len(pl) if pl else None


def rodar(estudo, h1, fund, s, rk, rng, res):
    for tf, horas in S.TFS.items():
        b = S.barras(h1, horas)
        sig = sinais_nr7(b) if estudo == "NR7" else sinais_pfr(b)
        com_sinal = {x[0] for x in sig}
        livre = 0
        for i, lado, a, z in sig:
            t = b[i][0]
            if s not in rk.get(t // DIA * DIA, ()) or not (F.INICIO <= t < F.FIM):
                continue
            t0, t1 = b[i + 1][0], b[i + 1][0] + horas * H
            if t0 < livre:
                continue
            if estudo == "NR7":
                o = oco(h1, t0, t1, a, z)
                if o is None:
                    continue
                lado, ts, e = o
                stop_px = z if lado > 0 else a
                fim = t1                                  # fecha no fim do candle de entrada
            else:
                p = preencher(h1, t0, t1, lado, a)
                if p is None:
                    continue
                ts, e = p
                stop_px = z
                fim = t + 11 * horas * H
            x = resultado(h1, fund, ts, e, lado, stop_px, fim)
            if x is None:
                continue
            exc = placebo(h1, fund, b, i, lado, x["risco"], fim - ts, com_sinal, rng, horas)
            res[tf].append({"sym": s, "ent": ts, "lado": lado, "risco": x["risco"], "r": x["r"],
                            "r_bruto": x["r_bruto"], "excesso": x["r"] - exc if exc is not None else None})
            livre = x["sai"]


def relatorio(nome, res):
    m = lambda v: sum(v) / len(v) if v else float("nan")
    for tf, xs in res.items():
        meio = sorted(t["ent"] for t in xs)[len(xs) // 2]
        b, ex = F.boot(xs, "r"), F.boot(xs, "excesso")
        h1m, h2m = m([t["r"] for t in xs if t["ent"] < meio]), m([t["r"] for t in xs if t["ent"] >= meio])
        print("\n" + "=" * 90 + f"\n{nome} {tf}\n" + "=" * 90)
        print(f"  R liquido  {F.fmt(b)}")
        print(f"  excesso    {F.fmt(ex)}")
        print(f"  R bruto {m([t['r_bruto'] for t in xs]):+.3f}R | risco medio {m([t['risco'] for t in xs])*100:.2f}%"
              f" | acerto {m([t['r'] > 0 for t in xs])*100:.1f}%")
        print(f"  metades: 1a {h1m:+.3f}R | 2a {h2m:+.3f}R")
        for lado, nm in ((1, "compras"), (-1, "vendas")):
            print(f"  {nm:<8} {F.fmt(F.boot([t for t in xs if t['lado'] == lado], 'r', 0.95))}")
        print(f"  fora das majors {F.fmt(F.boot([t for t in xs if t['sym'] not in C.MAJORS], 'r', 0.95))}")
        pa = defaultdict(list)
        for t in xs:
            pa[datetime.fromtimestamp(t["ent"] / 1000, timezone.utc).year].append(t["r"])
        print("  por ano: " + " | ".join(f"{a} {m(v):+.2f} ({len(v)})" for a, v in sorted(pa.items())))
        ok = b and ex and b[3] >= 200 and b[1] > 0 and ex[1] > 0 and h1m > 0 and h2m > 0
        print(f"  DECISAO {nome} {tf}: {'PASSA' if ok else 'NAO PASSA'}")


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
    res = {e: {tf: [] for tf in S.TFS} for e in ("NR7", "PFR")}
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
        for e in ("NR7", "PFR"):
            rodar(e, h1, fund, s, rk, rng, res[e])
    relatorio("ESTUDO 58 NR7", res["NR7"])
    relatorio("ESTUDO 59 PFR", res["PFR"])
    print(f"\n[{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main(sys.argv[1:])
