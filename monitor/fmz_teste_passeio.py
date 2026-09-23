"""Validacao do motor FMZ num passeio aleatorio sem drift (caminho intra-candle
de 480 passos). Sem edge possivel: bruto e excesso devem ficar em torno de zero
em todas as estrategias; desvio consistente = vies do motor ou lookahead."""
import math, random, sys
import fmz_motor as M
from replay_fmz_triagem import ESTRATEGIAS

def serie(rng, n=1500, passos=480, vol_dia=0.04):
    px, c, t = 100.0, [], 0
    s = vol_dia / math.sqrt(passos)
    for i in range(n):
        o = h = l = px
        for _ in range(passos):
            px *= math.exp(rng.gauss(-0.5 * s * s, s))
            h, l = max(h, px), min(l, px)
        c.append([i * M.MS_DIA, o, h, l, px, 0.0])
    return c

rng = random.Random(7)
n_series = int(sys.argv[1]) if len(sys.argv) > 1 else 30
dados = [serie(rng) for _ in range(n_series)]
res = {r: [] for r, _, _ in ESTRATEGIAS}
rb = random.Random(1)
pr = M.Precos()
for i, c in enumerate(dados):
    pr.add(i, c)
for i, c in enumerate(dados):
    for rot, fab, ini in ESTRATEGIAS:
        lg, pyr = fab(c)
        res[rot] += M.medir(c, M.rodar_script(c, lg, ini, pyr), None, rb, ini, sym=i)
for tr in res.values():
    pr.excesso(tr, rb)
for rot, tr in res.items():
    print(f"[{rot}]")
    print(M.linha("bruto", tr, "bruto")[0])
    print(M.linha("excesso_par (antigo)", tr, "excesso_par")[0])
    print(M.linha("excesso transversal", tr, "excesso")[0])
