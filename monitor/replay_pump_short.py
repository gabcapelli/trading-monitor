"""Estudo 79 -- venda de pump parabolico em altcoins, com stop.

PRE-REGISTRADO em 30/10/2026 (claude/estudos-avulsos.md, antes de qualquer conta).
Tentativa unica. Sinal: alta de 24h >= +50%, volume em dolar de 24h >= 3x a media
diaria dos 30 dias anteriores e >= US$ 5M. Venda na abertura da barra seguinte,
stop +30% (gap conta), saida em 72 h, custo 0.5% + funding real. Placebo: ate 30
outros simbolos liquidos na mesma hora, mesmo stop/saida/custo.
"""
import bisect
import random
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

import numpy as np

import replay_continuacao_top20 as R
from replay_momentum_ny import boot, fmt

H = 3600_000
T0 = int(datetime(2019, 12, 1, tzinfo=timezone.utc).timestamp() * 1000)
T1 = int(datetime(2026, 10, 1, tzinfo=timezone.utc).timestamp() * 1000)
INI = datetime(2020, 1, 1, tzinfo=timezone.utc).timestamp() * 1000
FIM = datetime(2026, 10, 1, tzinfo=timezone.utc).timestamp() * 1000
CORTE_B = datetime(2024, 1, 1, tzinfo=timezone.utc).timestamp() * 1000
ALTA, MULT_VOL, VOL_MIN, STOP, SAIDA, CUSTO, N_PLAC, MIN_TRADES = 0.50, 3.0, 5e6, 0.30, 72, 0.5, 30, 150


class Ativo:
    def __init__(self, sym, d):
        self.sym = sym
        ts = sorted(d["h"])
        self.t0 = ts[0]
        n = (ts[-1] - self.t0) // H + 1
        self.o, self.h, self.l, self.c, self.v = (np.full(n, np.nan) for _ in range(5))
        for t in ts:
            r = d["h"][t]
            i = (t - self.t0) // H
            self.o[i], self.h[i], self.l[i], self.c[i], self.v[i] = r[1], r[2], r[3], r[4], r[5]
        dv = np.nan_to_num(self.v * self.c)
        cs = np.concatenate([[0.0], np.cumsum(dv)])
        self.vol24 = np.full(n, np.nan)
        self.base = np.full(n, np.nan)
        if n > 24:
            self.vol24[23:] = cs[24:] - cs[:-24]
        w = 720
        if n > 24 + w:
            # soma das 720 barras anteriores as ultimas 24 -> media diaria (/30)
            idx = np.arange(24 + w - 1, n)
            self.base[idx] = (cs[idx - 24 + 1] - cs[idx - 24 - w + 1]) / 30
        self.ret24 = np.full(n, np.nan)
        self.ret24[24:] = self.c[24:] / self.c[:-24] - 1
        f = sorted(d["fund"])
        self.ft = [x[0] for x in f]
        self.fc = np.concatenate([[0.0], np.cumsum([x[1] for x in f])])

    def idx(self, t):
        i = (t - self.t0) // H
        return i if 0 <= i < len(self.o) else None

    def funding(self, ta, tb):
        return 100 * (self.fc[bisect.bisect_left(self.ft, tb)] - self.fc[bisect.bisect_left(self.ft, ta)])

    def vender(self, ie):
        """Venda na abertura do indice ie. Retorna (liq %, saiu_por_stop, bruto) ou None."""
        if ie + SAIDA >= len(self.o) or np.isnan(self.o[ie]) or np.isnan(self.o[ie + SAIDA]):
            return None
        ent = self.o[ie]
        stop = ent * (1 + STOP)
        seg_h = self.h[ie:ie + SAIDA]
        hit = np.where(seg_h >= stop)[0]
        if len(hit):
            j = ie + int(hit[0])
            px = max(stop, self.o[j]) if not np.isnan(self.o[j]) else stop
            ta, tb, stopado = self.t0 + ie * H, self.t0 + j * H, True
        else:
            px, ta, tb, stopado = self.o[ie + SAIDA], self.t0 + ie * H, self.t0 + (ie + SAIDA) * H, False
        bruto = -100 * (px / ent - 1)
        return bruto - CUSTO + self.funding(ta, tb), stopado, bruto


def main():
    tt = datetime.now()
    syms = R.simbolos()
    with ThreadPoolExecutor(8) as ex:
        dados = dict(zip(syms, ex.map(lambda s: R.carregar_1h(s, T0, T1), syms)))
    ativos = {s: Ativo(s, d) for s, d in dados.items() if d["h"]}
    print(f"simbolos com dado: {len(ativos)} [{(datetime.now()-tt).seconds}s]", flush=True)
    rng = random.Random(42)
    trades = []
    for s, a in ativos.items():
        ok = (a.ret24 >= ALTA) & (a.vol24 >= MULT_VOL * a.base) & (a.vol24 >= VOL_MIN)
        livre = 0
        for i in np.where(ok)[0]:
            t = a.t0 + int(i) * H
            ie = int(i) + 1
            te = t + H
            if te < INI or te >= FIM or te < livre:
                continue
            r = a.vender(ie)
            if r is None:
                continue
            liq, stopado, bruto = r
            tb = te + (SAIDA * H if not stopado else 0)
            livre = te + SAIDA * H     # conservador: so reentra depois da janela
            trades.append({"sym": s, "ent": te, "liq": liq, "stop": stopado, "bruto": bruto})
    print(f"trades: {len(trades)}", flush=True)
    for t in trades:
        pool = []
        for s, a in ativos.items():
            if s == t["sym"]:
                continue
            i = a.idx(t["ent"] - H)
            if i is not None and not np.isnan(a.vol24[i]) and a.vol24[i] >= VOL_MIN:
                pool.append(a)
        rng.shuffle(pool)
        rets = []
        for a in pool[:N_PLAC]:
            r = a.vender(a.idx(t["ent"]))
            if r:
                rets.append(r[0])
        t["plac"] = sum(rets) / len(rets) if rets else None
        t["exc"] = t["liq"] - t["plac"] if rets else None
    m = lambda xs: sum(xs) / len(xs) if xs else float("nan")
    ts = [t for t in trades if t["exc"] is not None]
    liq, exc = boot(trades, "liq"), boot(ts, "exc")
    A = [t["liq"] for t in trades if t["ent"] < CORTE_B]
    B = [t["liq"] for t in trades if t["ent"] >= CORTE_B]
    sem3 = sorted(trades, key=lambda t: t["liq"])[:-3]
    print("\n" + "=" * 90 + "\nVENDA DE PUMP PARABOLICO (>= +50% em 24h), stop +30%, saida 72h, custo 0.5%\n" + "=" * 90)
    print(f"  liq     {fmt(liq)}")
    print(f"  excesso {fmt(exc)}")
    print(f"  A (2020-23) {m(A):+.3f}% (n={len(A)}) | B (2024-26) {m(B):+.3f}% (n={len(B)})")
    print(f"  sem os 3 melhores: {m([t['liq'] for t in sem3]):+.3f}%")
    st = [t for t in trades if t["stop"]]
    print(f"  stopados {len(st)}/{len(trades)} ({100*len(st)/max(len(trades),1):.0f}%) | perda media dos stopados {m([t['liq'] for t in st]):+.2f}% | pior trade {min(t['liq'] for t in trades):+.1f}% | melhor {max(t['liq'] for t in trades):+.1f}%")
    print(f"  R medio {m([t['liq'] for t in trades])/ (STOP*100):+.3f}R | bruto medio {m([t['bruto'] for t in trades]):+.3f}% | placebo medio {m([t['plac'] for t in ts]):+.3f}%")
    por_ano = {}
    for t in trades:
        por_ano.setdefault(datetime.fromtimestamp(t["ent"] / 1000, timezone.utc).year, []).append(t["liq"])
    print("  por ano: " + " | ".join(f"{a}: {m(v):+.2f}% (n={len(v)})" for a, v in sorted(por_ano.items())))
    ok = (liq and exc and liq[1] > 0 and exc[1] > 0 and m(A) > 0 and m(B) > 0 and len(trades) >= MIN_TRADES
          and m([t["liq"] for t in sem3]) > 0)
    print(f"\n  DECISAO: {'PASSA' if ok else 'NAO PASSA'}")


if __name__ == "__main__":
    main()
