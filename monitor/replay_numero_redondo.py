"""
Estudos 72 (cruzamento de numero redondo, a favor) e 73 (rejeicao no numero
redondo, contra). PRE-REGISTRADOS em 19/10/2026, antes de rodar e antes de olhar
os dados. Tentativa unica cada.

MECANISMO (Osler 2003, cambio): ordens de stop e de take profit se acumulam em
numeros redondos. Take profit parado no numero faz o preco voltar no primeiro
toque; stops logo alem do numero, quando disparados, aceleram o movimento depois
do cruzamento.

NUMERO REDONDO: multiplo de 5 x 10^(k-1), com k = floor(log10(abertura do
candle)). Ex.: BTC 65.000/70.000/100.000; ETH 3.500/4.000; SOL 150/200; XRP
2.5/3.0; DOGE 0.15/0.20. Espaco entre niveis de 5% a 50% do preco.

UNIVERSO, EXECUCAO E CRITERIO: a regua dos estudos 63-71 (replay_div_engolfo.py):
top 50 de volume do dia, perpetuos USDT-M cripto da Binance com deslistados,
2020-01 a 2026-09, 1d e 4h, stop e alvo checados em 1h, custo 0.18% + funding,
placebo com o mesmo risco %, IC 97.5%. Entrada por stop no rompimento do candle
do sinal, valida so no candle seguinte; stop no outro extremo do candle; alvo
2R; saida na abertura do 11o candle depois do sinal; 1R minimo 0.3%.

ESTUDO 72 -- CRUZAMENTO (continuacao)
- Compra: abertura < L < fechamento para algum numero redondo L (o candle cruzou
  e fechou alem). Compra stop na maxima, stop na minima (que fica abaixo de L).
- Venda no espelho: abertura > L > fechamento.

ESTUDO 73 -- REJEICAO (primeiro toque volta)
- Venda: abertura < L, maxima >= L, fechamento < L (tocou por baixo e fechou
  abaixo). Venda stop na minima, stop na maxima.
- Compra no espelho: abertura > L, minima <= L, fechamento > L.

FUNIL PARA O PAPEL (descritivo, proposto em 13/10/2026): R bruto > 0, excesso
com IC95 > 0 e n >= 200.

Uso (de dentro de monitor/):
    python replay_numero_redondo.py
"""

import json
import math
import os
import random
import sys
import time
from concurrent.futures import ThreadPoolExecutor

import replay_continuacao_top20 as T
import replay_deslistagem as D
import replay_div_engolfo as E
import replay_fluxo_spot_perp as F
import replay_nr7_pfr as P
import replay_sfp as S

SEED = 42


def niveis(o, lo, hi):
    """Numeros redondos em [lo, hi], com o passo dado pela abertura o."""
    if o <= 0 or lo <= 0:
        return []
    passo = 5 * 10 ** (math.floor(math.log10(o)) - 1)
    k0, k1 = math.ceil(lo / passo - 1e-9), math.floor(hi / passo + 1e-9)
    return [k * passo for k in range(max(k0, 1), k1 + 1)]


def sinais_72(b):
    out = []
    for i in range(1, len(b) - 1):
        t, o, hi, lo, c = b[i][:5]
        if c > o and any(o < L < c for L in niveis(o, o, c)):
            out.append((i, +1, hi, lo))
        elif c < o and any(c < L < o for L in niveis(o, c, o)):
            out.append((i, -1, lo, hi))
    return out


def sinais_73(b):
    out = []
    for i in range(1, len(b) - 1):
        t, o, hi, lo, c = b[i][:5]
        if any(L > o and L > c for L in niveis(o, max(o, c), hi)):
            out.append((i, -1, lo, hi))
        elif any(L < o and L < c for L in niveis(o, lo, min(o, c))):
            out.append((i, +1, hi, lo))
    return out


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
    estudos = {"72": sinais_72, "73": sinais_73}
    res = {e: {tf: [] for tf in S.TFS} for e in estudos}
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
        for e, fn in estudos.items():
            E.sinais_div = fn
            E.rodar("DIV", h1, fund, s, rk, rng, res[e])
    P.relatorio("ESTUDO 72 CRUZAMENTO DE NUMERO REDONDO", res["72"])
    P.relatorio("ESTUDO 73 REJEICAO NO NUMERO REDONDO", res["73"])
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
