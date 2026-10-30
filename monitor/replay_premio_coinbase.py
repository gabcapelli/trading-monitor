"""Estudo 78 -- premio da Coinbase sobre a Binance (BTC e ETH, horario).

PRE-REGISTRADO em 30/10/2026 (claude/estudos-avulsos.md, antes de qualquer conta).
Tentativa unica. prem = fechamento 1h Coinbase (USD) / fechamento 1h Binance spot
(USDT) - 1. z = (prem - mediana das 168 h anteriores) / (1.4826 * MAD das 168 h
anteriores). Compra se z >= 2, venda se z <= -2, na abertura da hora seguinte
(perpetuo USDT-M); saida 4 h depois; um trade por vez por ativo; sem stop.
Custo 0.18% + funding real. Passa se: liq medio > 0 com IC95 > 0 (bootstrap por
semana); > 0 em A (2020-2023) e B (2024-2026); > 0 em BTC e ETH; >= 400 trades por
ativo; liq de compras e de vendas nao ambos <= 0.
"""
import json
import os
import statistics as st
import sys
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

import replay_deslistagem as D
from replay_momentum_ny import boot, fmt

AQUI = os.path.dirname(os.path.abspath(__file__))
CB = os.path.join(AQUI, "cache_coinbase")
H = 3600_000
T0 = int(datetime(2019, 12, 1, tzinfo=timezone.utc).timestamp())
T1 = int(datetime(2026, 9, 30, tzinfo=timezone.utc).timestamp())
CUSTO, MIN_TRADES, CORTE_B, JAN, HOLD = 0.18, 400, datetime(2024, 1, 1, tzinfo=timezone.utc).timestamp() * 1000, 168, 4


def _pedir(prod, a, b):
    url = (f"https://api.exchange.coinbase.com/products/{prod}/candles?granularity=3600"
           f"&start={datetime.fromtimestamp(a, timezone.utc):%Y-%m-%dT%H:%M:%SZ}"
           f"&end={datetime.fromtimestamp(b, timezone.utc):%Y-%m-%dT%H:%M:%SZ}")
    for tent in range(6):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "estudo78"})
            return json.load(urllib.request.urlopen(req, timeout=30))
        except Exception:
            time.sleep(1.5 * (tent + 1))
    raise RuntimeError(f"falhou {prod} {a}")


def coinbase(prod):
    fp = os.path.join(CB, f"{prod}_1h.json")
    if os.path.exists(fp):
        return {int(k): v for k, v in json.load(open(fp)).items()}
    os.makedirs(CB, exist_ok=True)
    passo = 300 * 3600
    janelas = [(a, min(a + passo, T1)) for a in range(T0, T1, passo)]
    out = {}
    with ThreadPoolExecutor(4) as ex:
        for r in ex.map(lambda w: _pedir(prod, *w), janelas):
            for t, lo, hi, op, cl, vol in r:
                out[t * 1000] = [op, hi, lo, cl, vol]
    json.dump({str(k): v for k, v in out.items()}, open(fp, "w"))
    return out


def rodar(sym, prod):
    cb = coinbase(prod)
    t0, t1 = T0 * 1000, T1 * 1000
    sp = D.klines("spot", sym, t0, t1)
    fu = D.klines("futures/um", sym, t0, t1)
    fund = [tuple(x) for x in json.load(open(os.path.join(AQUI, "cache_binance", f"{sym}_funding.json")))]
    horas = sorted(t for t in cb if t in sp and cb[t][3] > 0 and sp[t][3] > 0)
    prem = {t: cb[t][3] / sp[t][3] - 1 for t in horas}
    trades, livre = [], 0
    for i, t in enumerate(horas):
        if i < JAN:
            continue
        # janela de 168 horas CONSECUTIVAS anteriores, so com dado existente
        jan = [prem[x] for x in horas[i - JAN:i] if t - JAN * H <= x < t]
        if len(jan) < JAN * 0.9:
            continue
        med = st.median(jan)
        mad = st.median(abs(x - med) for x in jan)
        if mad <= 0:
            continue
        z = (prem[t] - med) / (1.4826 * mad)
        if abs(z) < 2:
            continue
        ent, sai = t + H, t + H + HOLD * H
        if ent < livre or ent not in fu or sai not in fu:
            continue
        lado = 1 if z > 0 else -1
        bruto = lado * 100 * (fu[sai][0] / fu[ent][0] - 1)
        f = -lado * 100 * sum(x for ts, x in fund if ent <= ts < sai)
        trades.append({"ent": ent, "lado": lado, "bruto": bruto, "liq": bruto - CUSTO + f})
        livre = sai
    return trades


def main():
    res = {}
    mean = lambda xs: sum(xs) / len(xs) if xs else float("nan")
    for sym, prod in (("BTCUSDT", "BTC-USD"), ("ETHUSDT", "ETH-USD")):
        t = res[sym] = rodar(sym, prod)
        A, B = [x["liq"] for x in t if x["ent"] < CORTE_B], [x["liq"] for x in t if x["ent"] >= CORTE_B]
        print(f"{sym}: {fmt(boot(t))} | bruto medio {mean([x['bruto'] for x in t]):+.3f}%")
        print(f"   A (2020-23): {mean(A):+.3f}% (n={len(A)}) | B (2024-26): {mean(B):+.3f}% (n={len(B)}) | "
              f"compras {mean([x['liq'] for x in t if x['lado'] == 1]):+.3f}% | vendas {mean([x['liq'] for x in t if x['lado'] == -1]):+.3f}%")
    todos = res["BTCUSDT"] + res["ETHUSDT"]
    liq = boot(todos)
    A, B = [x["liq"] for x in todos if x["ent"] < CORTE_B], [x["liq"] for x in todos if x["ent"] >= CORTE_B]
    mb, me = (mean([x["liq"] for x in res[s]]) for s in res)
    c, v = mean([x["liq"] for x in todos if x["lado"] == 1]), mean([x["liq"] for x in todos if x["lado"] == -1])
    print(f"\nAMOSTRA TODA (BTC+ETH): {fmt(liq)}")
    print(f"metades: A {mean(A):+.3f}% | B {mean(B):+.3f}% | BTC {mb:+.3f}% | ETH {me:+.3f}% | compras {c:+.3f}% | vendas {v:+.3f}%")
    ok = (liq and liq[1] > 0 and mean(A) > 0 and mean(B) > 0 and mb > 0 and me > 0
          and all(len(res[s]) >= MIN_TRADES for s in res) and not (c <= 0 and v <= 0))
    print(f"\nDECISAO: {'PASSA' if ok else 'NAO PASSA'}")


if __name__ == "__main__":
    main()
