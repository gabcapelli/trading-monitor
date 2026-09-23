"""Validacao do Dual Thrust (caminho de 1h) e dos pares num passeio aleatorio
sem drift: bruto e excesso devem ficar em torno de zero."""
import math, random, sys
import fmz_motor as M
import replay_fmz_mecanismos as X

def serie_1h(rng, dias=700, passos=int(sys.argv[2]) if len(sys.argv) > 2 else 20, vol_dia=0.04):
    s = vol_dia / math.sqrt(24 * passos)
    px, h = 100.0, []
    for i in range(dias * 24):
        o = hi = lo = px
        for _ in range(passos):
            px *= math.exp(rng.gauss(-0.5 * s * s, s))
            hi, lo = max(hi, px), min(lo, px)
        h.append([i * X.MS_H, o, hi, lo, px, 0.0])
    return h

def diario(h):
    return [[h[i][0], h[i][1], max(k[2] for k in h[i:i+24]), min(k[3] for k in h[i:i+24]), h[i+23][4], 0]
            for i in range(0, len(h), 24)]

rng = random.Random(3); rb = random.Random(1)
N = int(sys.argv[1]) if len(sys.argv) > 1 else 40
hs = [serie_1h(rng) for _ in range(N)]
res = {"SAR": [], "intra": []}
for i, h in enumerate(hs):
    niv = X.niveis_diarios(diario(h))
    res["SAR"] += X.medir_1h(h, X.dual_thrust(h, niv, False), None and 0 or type("F", (), {"soma": lambda *a: 0.0})(), i)
    res["intra"] += X.medir_1h(h, X.dual_thrust(h, niv, True), type("F", (), {"soma": lambda *a: 0.0})(), i)
precos = {i: {k[0]: k for k in h} for i, h in enumerate(hs)}
for tr in res.values():
    X.excesso_transversal(tr, precos, rb)
    for x in tr: x["bruto_slip"] = x["bruto"] - x["slip"]
for r, tr in res.items():
    print(f"[Dual Thrust {r}]")
    print(M.linha("bruto (antes de custo e slip)", tr, "bruto")[0])
    print(M.linha("excesso transversal", tr, "excesso")[0])
# pares: razoes de series diarias independentes
ds = [diario(h) for h in hs]
btc, pr, trades = ds[0], M.Precos(), []
for i, d in enumerate(ds[1:], start=1):
    r = X.razao(d, btc); pr.add(i, r)
    trades += M.medir(r, M.rodar_script(r, X.pares_logica(r), 25), None, rb, 25, sym=i)
pr.excesso(trades, rb)
print("[pares]"); print(M.linha("bruto", trades, "bruto")[0]); print(M.linha("excesso transversal", trades, "excesso")[0])
