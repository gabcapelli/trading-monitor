"""Estudo 77 -- momentum da primeira meia hora da sessao dos EUA (BTC e ETH).

PRE-REGISTRADO em 30/10/2026 (claude/estudos-avulsos.md, antes de qualquer conta).
Tentativa unica. Sinal: r = fechamento do minuto 09:59 de Nova York / abertura do
minuto 09:30 - 1 (dias uteis, horario de NY com verao). Opera so se |r| >= mediana
dos |r| dos 90 dias uteis anteriores. Entrada: abertura do minuto 10:00 NY, na
direcao de r. Saida: abertura do minuto 16:00 NY. Custo 0.18% + funding real.
Passa se: liq medio > 0 com IC95 > 0 (bootstrap por semana); > 0 em A (2020-2023)
e B (2024-2026); > 0 em BTC e ETH; >= 600 trades por ativo.
"""
import glob
import json
import os
import random
import statistics as st
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from zoneinfo import ZoneInfo

NY = ZoneInfo("America/New_York")
CUSTO, SEED, MIN_TRADES = 0.18, 42, 600
CORTE_B = datetime(2024, 1, 1, tzinfo=timezone.utc).timestamp() * 1000
AQUI = os.path.dirname(os.path.abspath(__file__))


def ms(d: date, h: int, m: int) -> int:
    return int(datetime(d.year, d.month, d.day, h, m, tzinfo=NY).astimezone(timezone.utc).timestamp() * 1000)


def carregar(sym):
    k = {}
    for f in sorted(glob.glob(os.path.join(AQUI, "cache_1m", f"{sym}_20*.json"))):
        for t, v in json.load(open(f)).items():
            k[int(t)] = v
    fund = [tuple(x) for x in json.load(open(os.path.join(AQUI, "cache_binance", f"{sym}_funding.json")))]
    return k, fund


def boot(trades, chave="liq", conf=0.95):
    g = defaultdict(list)
    for t in trades:
        g[t["ent"] // (7 * 86400000)].append(t[chave])
    grupos = list(g.values())
    if len(grupos) < 5:
        return None
    n = sum(map(len, grupos))
    m = sum(map(sum, grupos)) / n
    rng = random.Random(SEED)
    ms_ = []
    for _ in range(5000):
        s = k = 0
        for _ in grupos:
            v = rng.choice(grupos)
            s += sum(v)
            k += len(v)
        ms_.append(s / k)
    ms_.sort()
    a = (1 - conf) / 2
    return m, ms_[int(a * len(ms_))], ms_[int((1 - a) * len(ms_)) - 1], n


def fmt(r):
    return "(insuficiente)" if r is None else f"n={r[3]:>5} media {r[0]:+.3f}% IC95 [{r[1]:+.3f}, {r[2]:+.3f}]"


def rodar(sym):
    k, fund = carregar(sym)
    d0, d1 = date(2019, 12, 2), date(2026, 9, 29)
    hist, trades, sem_dado = [], [], 0
    d = d0
    while d <= d1:
        if d.weekday() < 5:
            t0, t1, te, ts = ms(d, 9, 30), ms(d, 9, 59), ms(d, 10, 0), ms(d, 16, 0)
            a, b, e, s = k.get(t0), k.get(t1), k.get(te), k.get(ts)
            if a and b and e and s and a[0] > 0:
                r = b[3] / a[0] - 1
                if len(hist) >= 90 and abs(r) >= st.median(hist[-90:]) and r != 0:
                    lado = 1 if r > 0 else -1
                    bruto = lado * 100 * (s[0] / e[0] - 1)
                    f = -lado * 100 * sum(x for t, x in fund if te <= t < ts)
                    trades.append({"ent": te, "lado": lado, "bruto": bruto, "liq": bruto - CUSTO + f})
                hist.append(abs(r))
            else:
                sem_dado += 1
        d += timedelta(days=1)
    return trades, sem_dado


def main():
    res = {}
    for sym in ("BTCUSDT", "ETHUSDT"):
        res[sym], sd = rodar(sym)
        t = res[sym]
        A = [x for x in t if x["ent"] < CORTE_B]
        B = [x for x in t if x["ent"] >= CORTE_B]
        m = lambda xs: sum(x["liq"] for x in xs) / len(xs) if xs else float("nan")
        print(f"{sym}: dias sem dado {sd} | todos {fmt(boot(t))} | bruto medio {m([{'liq': x['bruto']} for x in t]):+.3f}%")
        print(f"   A (2020-23): {m(A):+.3f}% (n={len(A)}) | B (2024-26): {m(B):+.3f}% (n={len(B)}) | "
              f"compras {m([x for x in t if x['lado'] == 1]):+.3f}% | vendas {m([x for x in t if x['lado'] == -1]):+.3f}%")
    todos = res["BTCUSDT"] + res["ETHUSDT"]
    liq = boot(todos)
    print(f"\nAMOSTRA TODA (BTC+ETH): {fmt(liq)}")
    A = [x["liq"] for x in todos if x["ent"] < CORTE_B]
    B = [x["liq"] for x in todos if x["ent"] >= CORTE_B]
    mb, me = (sum(x["liq"] for x in res[s]) / len(res[s]) for s in res)
    ok = (liq and liq[1] > 0 and A and B and sum(A) / len(A) > 0 and sum(B) / len(B) > 0
          and mb > 0 and me > 0 and all(len(res[s]) >= MIN_TRADES for s in res))
    print(f"metades: A {sum(A)/len(A):+.3f}% | B {sum(B)/len(B):+.3f}% | BTC {mb:+.3f}% | ETH {me:+.3f}%")
    print(f"\nDECISAO: {'PASSA' if ok else 'NAO PASSA'}")


if __name__ == "__main__":
    main()
