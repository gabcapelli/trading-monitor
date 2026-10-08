"""
Estudo 55 -- salto forte em 1h: quem empurrou, o spot ou o perpetuo?
PRE-REGISTRADO em 08/10/2026, antes de baixar os dados com fluxo.

HIPOTESE
--------
Num salto forte de 1h, se o fluxo agressivo anormal veio do SPOT (dinheiro sem
alavancagem), o movimento continua; se veio do PERPETUO (alavancagem), devolve.
Nenhum estudo anterior separou o fluxo do spot do fluxo do perpetuo (27, 31 e 36
olharam funding, open interest e premio). Setup de giro ativo, horas de duracao,
movimento grande por trade: ataca a causa das falhas 49/52/53 (custo e funding).

UNIVERSO (point-in-time, como o estudo 46)
------------------------------------------
Perpetuos USDT-M cripto da Binance, inclusive deslistados. Um evento so conta se
o perpetuo estiver entre os 50 de maior volume (30 dias anteriores) no dia e tiver
spot USDT na Binance (1000XXX -> XXX). 2020-01 a 2026-09.

EVENTO (barra de 1h do perpetuo, t)
-----------------------------------
- r = fechamento/abertura - 1; sd = desvio dos retornos log de 1h nas 168 barras
  anteriores. Evento se |r| >= 4*sd E volume em dolar >= 3x a media das 168.
- d = sinal de r.
- Fluxo liquido de cada mercado na barra: net = 2*compra_agressiva - volume (US$).
  z = net / media(|net|) das 168 barras anteriores, no proprio mercado.
- lead = d * (z_spot - z_perp). lead > 0: puxado pelo spot. lead < 0: pelo perp.

SETUPS (dois, decididos em separado)
------------------------------------
- S (spot) : lead > 0 -> a favor do salto (lado = d).
- P (perp) : lead < 0 -> contra o salto (lado = -d).
- Entrada na abertura da barra t+1. Risco (1R) = amplitude da barra do evento
  (max-min) em % da entrada. Stop a 1R, alvo a 2R. Barras de 1h a partir de t+1;
  stop e alvo na mesma barra = stop. Sem toque: sai na abertura de t+25 (24h).
- Custo 0.18% ida e volta + funding real. Resultado em R = (bruto% - custo - funding) / risco%.
- Um trade por vez por simbolo (S e P compartilham a fila).

CRITERIO (fixado antes; por setup; todos juntos; IC 97.5% = Bonferroni p/ 2 setups)
------------------------------------------------------------------------------------
1. n >= 200.
2. R liquido medio com IC97.5 inteiro > 0 (bootstrap por semana).
3. Excesso sobre placebo com IC97.5 > 0. Placebo: mesmo simbolo, mesmo lado,
   mesmo risco %, mesma regra de stop/alvo/24h, entrada em 5 horas aleatorias
   a ate 7 dias do evento e fora de 24h de qualquer evento.
4. R liquido medio > 0 nas duas metades do periodo.
Descritivo, sem poder de decisao: continuacao nos dois grupos (o mecanismo),
permutacao dos rotulos spot/perp, por ano, so compras / so vendas.

Uso (de dentro de monitor/):
    python replay_fluxo_spot_perp.py --baixar
    python replay_fluxo_spot_perp.py
"""

import json
import math
import os
import random
import sys
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone

import replay_continuacao_top20 as T
import replay_deslistagem as D

DIA = 86_400_000
H = 3_600_000
TOP = 50
INICIO = int(datetime(2020, 1, 1, tzinfo=timezone.utc).timestamp() * 1000)
FIM = int(datetime(2026, 10, 1, tzinfo=timezone.utc).timestamp() * 1000)
JAN = 168
K_SD, K_VOL = 4.0, 3.0
ALVO_R, SAIDA_H = 2.0, 24
CUSTO = 0.18
N_PLACEBO, SEED, N_BOOT = 5, 42, 5000
CONF = 0.975
DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache_taker")


def spot_de(sym):
    for p in ("1000000", "1000", "1M"):
        if sym.startswith(p) and len(sym) > len(p) + 4:
            return sym[len(p):]
    return sym


def klines_mes(mercado, sym, mes):
    """{ts: [o, h, l, c, volume US$, compra agressiva US$]} de 1h."""
    os.makedirs(DIR, exist_ok=True)
    fp = os.path.join(DIR, f"{mercado.replace('/', '_')}_{sym}_{mes}.json")
    if os.path.exists(fp):
        return {int(k): v for k, v in json.load(open(fp)).items()}
    raw = D._get(f"{D.VISION}/{mercado}/monthly/klines/{sym}/1h/{sym}-1h-{mes}.zip")
    linhas = D._csv_zip(raw) if raw else []
    out = {D._ms(r[0]): [float(r[1]), float(r[2]), float(r[3]), float(r[4]), float(r[7]), float(r[10])]
           for r in linhas}
    tmp = fp + ".tmp"
    json.dump(out, open(tmp, "w"))
    os.replace(tmp, fp)
    return out


def meses_no_top(sym, rk):
    ms = set()
    for d, s in rk.items():
        if sym in s and INICIO <= d < FIM:
            for x in (d - 8 * DIA, d, d + 2 * DIA):   # janela de 168h antes e 24h depois
                ms.add(datetime.fromtimestamp(x / 1000, timezone.utc).strftime("%Y-%m"))
    return sorted(m for m in ms if m <= "2026-09")


def carregar(sym, rk):
    ms = meses_no_top(sym, rk)
    perp, spot = {}, {}
    for m in ms:
        perp.update(klines_mes("futures/um", sym, m))
        spot.update(klines_mes("spot", spot_de(sym), m))
    fund = []
    if perp:
        D.funding(sym, INICIO - 40 * DIA, FIM)
        for m in ms:
            fp = os.path.join(D.DIR_VISION, f"funding_{sym}_{m}.json")
            if os.path.exists(fp):
                fund += [tuple(x) for x in json.load(open(fp))]
    return {"perp": perp, "spot": spot, "fund": sorted(fund)}


def eventos(sym, d, rk):
    p, s = d["perp"], d["spot"]
    ts = sorted(p)
    out = []
    for i in range(JAN, len(ts) - 1):
        t = ts[i]
        if ts[i] - ts[i - JAN] != JAN * H or sym not in rk.get(t // DIA * DIA, ()) or not (INICIO <= t < FIM):
            continue
        o, hi, lo, c, v, tb = p[t]
        if o <= 0 or c <= 0:
            continue
        r = c / o - 1
        prev = [p[x] for x in ts[i - JAN:i]]
        lr = [math.log(x[3] / x[0]) for x in prev if x[0] > 0 and x[3] > 0]
        sd = math.sqrt(sum(x * x for x in lr) / len(lr)) if lr else 0
        mv = sum(x[4] for x in prev) / JAN
        if sd <= 0 or abs(r) < K_SD * sd or v < K_VOL * mv:
            continue
        sp = [s.get(x) for x in ts[i - JAN:i + 1]]
        if any(x is None for x in sp):
            out.append({"t": t, "sem_spot": True})
            continue
        net = lambda x: 2 * x[5] - x[4]
        ap = sum(abs(net(x)) for x in prev) / JAN
        as_ = sum(abs(net(x)) for x in sp[:-1]) / JAN
        if ap <= 0 or as_ <= 0:
            continue
        dd = 1 if r > 0 else -1
        lead = dd * (net(sp[-1]) / as_ - net(p[t]) / ap)
        out.append({"t": t, "d": dd, "lead": lead, "risco": (hi - lo) / c, "sem_spot": False})
    return out


def simular(d, ent, lado, risco):
    """Resultado em R (antes do custo) e % bruto; None se faltar dado."""
    p = d["perp"]
    if ent not in p:
        return None
    e = p[ent][0]
    stop, alvo = e * (1 - lado * risco), e * (1 + lado * ALVO_R * risco)
    for k in range(SAIDA_H):
        b = p.get(ent + k * H)
        if b is None:
            return None
        hi, lo = b[1], b[2]
        bate_stop = lo <= stop if lado > 0 else hi >= stop
        bate_alvo = hi >= alvo if lado > 0 else lo <= alvo
        if bate_stop:
            return -risco * 100, ent + (k + 1) * H
        if bate_alvo:
            return ALVO_R * risco * 100, ent + (k + 1) * H
    b = p.get(ent + SAIDA_H * H)
    if b is None:
        return None
    return lado * 100 * (b[0] / e - 1), ent + SAIDA_H * H


def funding(d, lado, t0, t1):
    return -lado * 100 * sum(r for ts, r in d["fund"] if t0 <= ts < t1)


def trade(d, ent, lado, risco):
    x = simular(d, ent, lado, risco)
    if x is None:
        return None
    bruto, sai = x
    liq = bruto - CUSTO + funding(d, lado, ent, sai)
    return {"r": liq / (risco * 100), "r_bruto": bruto / (risco * 100), "sai": sai}


def boot(xs, chave, conf=CONF):
    xs = [x for x in xs if x.get(chave) is not None]
    if len(xs) < 2:
        return None
    sem = defaultdict(list)
    for x in xs:
        sem[x["ent"] // (7 * DIA)].append(x[chave])
    blocos = list(sem.values())
    rng = random.Random(SEED)
    n = len(xs)
    ms = []
    for _ in range(N_BOOT):
        s, k = 0.0, 0
        for _ in range(len(blocos)):
            b = blocos[rng.randrange(len(blocos))]
            s += sum(b)
            k += len(b)
        ms.append(s / k)
    ms.sort()
    a = (1 - conf) / 2
    return sum(x[chave] for x in xs) / n, ms[int(a * N_BOOT)], ms[int((1 - a) * N_BOOT) - 1], n, conf


def fmt(b):
    return "n/a" if b is None else f"{b[0]:+.3f}R  IC{round(b[4] * 100, 1):g}% [{b[1]:+.3f}, {b[2]:+.3f}]  n={b[3]}"


def main(argv):
    t0 = time.time()
    syms = T.simbolos()
    with ThreadPoolExecutor(16) as ex:
        vols = dict(zip(syms, ex.map(T.diario, syms)))
    vols = {s: v for s, v in vols.items() if v}
    T.TOP = TOP
    rk = T.ranking(vols)
    alguma = sorted({s for d, v in rk.items() if INICIO <= d < FIM for s in v})
    print(f"perpetuos cripto: {len(syms)} | ja no top {TOP}: {len(alguma)}", flush=True)
    tarefas = [(mk, sy, m) for s in alguma for m in meses_no_top(s, rk)
               for mk, sy in (("futures/um", s), ("spot", spot_de(s)))]
    with ThreadPoolExecutor(48) as ex:
        list(ex.map(lambda a: klines_mes(*a), tarefas))
    with ThreadPoolExecutor(16) as ex:
        dados = dict(zip(alguma, ex.map(lambda s: carregar(s, rk), alguma)))
    print(f"dados ok [{time.time()-t0:.0f}s]", flush=True)
    if "--baixar" in argv:
        return

    trades, placebos_sem, n_sem_spot, n_ev = [], 0, 0, 0
    rng = random.Random(SEED)
    for s in alguma:
        d = dados[s]
        evs = eventos(s, d, rk)
        n_ev += len(evs)
        n_sem_spot += sum(e["sem_spot"] for e in evs)
        evs = [e for e in evs if not e["sem_spot"]]
        t_ev = sorted(e["t"] for e in evs)
        livre = 0
        for e in evs:
            ent = e["t"] + H
            if ent < livre or e["lead"] == 0 or e["risco"] <= 0:
                continue
            setup = "S" if e["lead"] > 0 else "P"
            lado = e["d"] if setup == "S" else -e["d"]
            x = trade(d, ent, lado, e["risco"])
            if x is None:
                continue
            cont = trade(d, ent, e["d"], e["risco"])   # descritivo: continuacao nos dois grupos
            pl = []
            for _ in range(60):
                if len(pl) >= N_PLACEBO:
                    break
                tp = (e["t"] + rng.randint(-7 * 24, 7 * 24) * H) // H * H
                if any(abs(tp - te) < 24 * H for te in t_ev[max(0, _bis(t_ev, tp) - 2):_bis(t_ev, tp) + 2]):
                    continue
                y = trade(d, tp, lado, e["risco"])
                if y is not None:
                    pl.append(y["r"])
            if not pl:
                placebos_sem += 1
            trades.append({"sym": s, "ent": ent, "setup": setup, "lado": lado, "d": e["d"], "lead": e["lead"],
                           "risco": e["risco"], "r": x["r"], "r_bruto": x["r_bruto"],
                           "cont": cont["r"] if cont else None,
                           "excesso": x["r"] - sum(pl) / len(pl) if pl else None})
            livre = x["sai"]

    print(f"\neventos: {n_ev} | sem spot: {n_sem_spot} | trades: {len(trades)} | sem placebo: {placebos_sem}")
    meio = sorted(t["ent"] for t in trades)[len(trades) // 2]
    m = lambda xs: sum(xs) / len(xs) if xs else float("nan")
    for st, nome in (("S", "S  puxado pelo SPOT -> a favor"), ("P", "P  puxado pelo PERP -> contra")):
        xs = [t for t in trades if t["setup"] == st]
        b, ex = boot(xs, "r"), boot(xs, "excesso")
        h1, h2 = m([t["r"] for t in xs if t["ent"] < meio]), m([t["r"] for t in xs if t["ent"] >= meio])
        print("\n" + "=" * 90 + f"\n{nome}\n" + "=" * 90)
        print(f"  R liquido  {fmt(b)}")
        print(f"  excesso    {fmt(ex)}")
        print(f"  R bruto medio {m([t['r_bruto'] for t in xs]):+.3f}R | risco medio {m([t['risco'] for t in xs])*100:.2f}%"
              f" | acerto {m([t['r'] > 0 for t in xs])*100:.1f}%")
        print(f"  metades: 1a {h1:+.3f}R | 2a {h2:+.3f}R")
        for lado, nm in ((1, "compras"), (-1, "vendas")):
            print(f"  so {nm:<8} {fmt(boot([t for t in xs if t['lado'] == lado], 'r', 0.95))}")
        pa = defaultdict(list)
        for t in xs:
            pa[datetime.fromtimestamp(t["ent"] / 1000, timezone.utc).year].append(t["r"])
        print("  por ano: " + " | ".join(f"{a} {m(v):+.2f} ({len(v)})" for a, v in sorted(pa.items())))
        ok = b and ex and b[3] >= 200 and b[1] > 0 and ex[1] > 0 and h1 > 0 and h2 > 0
        print(f"  DECISAO {st}: {'PASSA' if ok else 'NAO PASSA'}")

    print("\n" + "=" * 90 + "\nDESCRITIVO: continuacao (a favor do salto) por grupo\n" + "=" * 90)
    cs = [t for t in trades if t["setup"] == "S" and t["cont"] is not None]
    cp = [t for t in trades if t["setup"] == "P" and t["cont"] is not None]
    print(f"  spot-led {m([t['cont'] for t in cs]):+.3f}R (n={len(cs)}) | perp-led {m([t['cont'] for t in cp]):+.3f}R (n={len(cp)})")
    dif = m([t["cont"] for t in cs]) - m([t["cont"] for t in cp])
    todos = [t["cont"] for t in cs + cp]
    r2 = random.Random(SEED)
    perm = []
    for _ in range(2000):
        r2.shuffle(todos)
        perm.append(m(todos[:len(cs)]) - m(todos[len(cs):]))
    print(f"  diferenca {dif:+.3f}R | permutacao dos rotulos: p = {sum(x >= dif for x in perm)/len(perm):.3f}")
    qs = sorted(cs + cp, key=lambda t: t["lead"])
    q = len(qs) // 5
    print("  quintis de lead (continuacao): " + " | ".join(
        f"Q{i+1} {m([t['cont'] for t in qs[i*q:(i+1)*q]]):+.3f}" for i in range(5)))
    print(f"\n[{time.time()-t0:.0f}s]")


def _bis(xs, v):
    import bisect
    return bisect.bisect_left(xs, v)


if __name__ == "__main__":
    main(sys.argv[1:])
