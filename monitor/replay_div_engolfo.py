"""
Estudos 63 (divergencia de IFR) e 64 (engolfo / martelo em suporte).
PRE-REGISTRADOS em 13/10/2026, antes de rodar. Tentativa unica cada um: mesma
regua dos estudos 57-59, sem ajuste de parametro depois de ver o resultado.

UNIVERSO E DADOS: iguais ao estudo 57 (replay_sfp.py): perpetuos USDT-M cripto da
Binance, inclusive deslistados, entre os 50 de maior volume no dia do sinal,
2020-01 a 2026-09; 1h agregado em 4h e 1d (UTC); stop e alvo checados em 1h.

ENTRADA, STOP, ALVO E SAIDA (iguais ao PFR do estudo 59, nos dois estudos):
compra stop na maxima do candle do sinal, valida so durante o candle seguinte
(espelho na venda). Stop no extremo do padrao (abaixo). Alvo 2R. Saida na
abertura do 11o candle depois do sinal. 1R minimo de 0.3%. Custo 0.18% + funding
real. Um trade por vez por simbolo e tempo grafico. Execucao em
replay_nr7_pfr.preencher/resultado.

PIVO (nos dois estudos): fundo em p = minima de p menor que a dos 2 candles de
cada lado (estrito). So e conhecido no fechamento de p+2. Topo no espelho.

ESTUDO 63 -- DIVERGENCIA DE IFR (divergencia regular classica)
- IFR(14) de Wilder sobre os fechamentos do tempo grafico.
- Compra: no fechamento de c = p2+2 fica confirmado o fundo p2. Pega o fundo
  confirmado mais recente p1 com 5 <= p2 - p1 <= 30. Sinal se
  minima[p2] < minima[p1], IFR[p2] > IFR[p1] e IFR[p1] < 30.
- Venda no espelho (topos, maxima maior, IFR menor, IFR[p1] > 70).
- Candle do sinal = c. Stop na minima de p2 (venda: maxima de p2).

ESTUDO 64 -- ENGOLFO / MARTELO EM SUPORTE
- Engolfo de alta em i: candle i-1 de baixa, i de alta, abertura[i] <= fech[i-1],
  fech[i] >= abertura[i-1] e corpo[i] > corpo[i-1]. Minima do padrao =
  min(minima[i-1], minima[i]).
- Martelo em i: sombra inferior >= 2x corpo e >= 60% da amplitude; sombra
  superior <= 15% da amplitude. Minima do padrao = minima[i].
- Suporte: algum fundo (pivo) p com i-100 <= p <= i-10, nivel L = minima[p], tal
  que nenhum fechamento entre p+1 e i-1 ficou abaixo de L (suporte intacto),
  |minima do padrao - L| <= 0.5 x ATR(14) de i, e fech[i] > L.
- Venda no espelho (engolfo de baixa, estrela cadente, resistencia nos topos).
- Candle do sinal = i. Stop na minima do padrao (venda: maxima).

CRITERIO (por estudo; duas celulas, 1d e 4h, IC 97.5%; todos juntos por celula)
1. n >= 200.
2. R liquido medio com IC97.5 inteiro > 0 (bootstrap por semana).
3. Excesso sobre placebo com IC97.5 > 0. Placebo: mesmo simbolo, lado e risco %,
   entrada a mercado na abertura de 5 candles aleatorios a ate 30 dias, mesma
   regra de stop/alvo e mesma duracao.
4. R liquido medio > 0 nas duas metades.

Uso (de dentro de monitor/):
    python replay_div_engolfo.py
"""

import json
import os
import random
import sys
import time
from concurrent.futures import ThreadPoolExecutor

import replay_continuacao_top20 as T
import replay_deslistagem as D
import replay_fluxo_spot_perp as F
import replay_nr7_pfr as P
import replay_sfp as S

DIA, H = S.DIA, S.H
SEED = 42


def ifr(b, n=14):
    out = [None] * len(b)
    if len(b) <= n:
        return out
    d = [b[k][4] - b[k - 1][4] for k in range(1, len(b))]
    g = sum(max(x, 0) for x in d[:n]) / n
    p = sum(max(-x, 0) for x in d[:n]) / n
    for k in range(n, len(b)):
        if k > n:
            x = d[k - 1]
            g = (g * (n - 1) + max(x, 0)) / n
            p = (p * (n - 1) + max(-x, 0)) / n
        out[k] = 100.0 if p == 0 else 100 - 100 / (1 + g / p)
    return out


def pivos(b):
    fundos, topos = set(), set()
    for p in range(2, len(b) - 2):
        viz = (b[p - 2], b[p - 1], b[p + 1], b[p + 2])
        if all(b[p][3] < x[3] for x in viz):
            fundos.add(p)
        if all(b[p][2] > x[2] for x in viz):
            topos.add(p)
    return fundos, topos


def sinais_div(b):
    r = ifr(b)
    fundos, topos = pivos(b)
    out = []
    for c in range(4, len(b) - 1):
        p2 = c - 2
        for piv, lado in ((fundos, +1), (topos, -1)):
            if p2 not in piv:
                continue
            p1 = next((q for q in range(p2 - 5, p2 - 31, -1) if q in piv), None)
            if p1 is None or r[p1] is None or r[p2] is None:
                continue
            if lado > 0 and b[p2][3] < b[p1][3] and r[p2] > r[p1] and r[p1] < 30:
                out.append((c, +1, b[c][2], b[p2][3]))
            elif lado < 0 and b[p2][2] > b[p1][2] and r[p2] < r[p1] and r[p1] > 70:
                out.append((c, -1, b[c][3], b[p2][2]))
    return out


def atr(b, i, n=14):
    tr = [max(b[k][2], b[k - 1][4]) - min(b[k][3], b[k - 1][4]) for k in range(i - n + 1, i + 1)]
    return sum(tr) / n


def padrao(b, i, lado):
    """Extremo do padrao de reversao no lado pedido, ou None. Retorna (extremo, tipo)."""
    a, x = b[i - 1], b[i]
    o, h, l, c = x[1], x[2], x[3], x[4]
    amp, corpo = h - l, abs(c - o)
    if lado > 0:
        if a[4] < a[1] and c > o and o <= a[4] and c >= a[1] and corpo > abs(a[4] - a[1]):
            return min(a[3], l), "engolfo"
        if amp > 0 and min(o, c) - l >= 2 * corpo and min(o, c) - l >= 0.6 * amp and h - max(o, c) <= 0.15 * amp:
            return l, "martelo"
    else:
        if a[4] > a[1] and c < o and o >= a[4] and c <= a[1] and corpo > abs(a[4] - a[1]):
            return max(a[2], h), "engolfo"
        if amp > 0 and h - max(o, c) >= 2 * corpo and h - max(o, c) >= 0.6 * amp and min(o, c) - l <= 0.15 * amp:
            return h, "martelo"
    return None


def sinais_eng(b):
    fundos, topos = pivos(b)
    out = []
    for i in range(101, len(b) - 1):
        for piv, lado in ((fundos, +1), (topos, -1)):
            pd = padrao(b, i, lado)
            if pd is None:
                continue
            ext, tipo = pd
            tol = 0.5 * atr(b, i)
            ok = False
            for p in range(i - 100, i - 9):
                if p not in piv:
                    continue
                if lado > 0:
                    L = b[p][3]
                    if all(b[k][4] >= L for k in range(p + 1, i)) and abs(ext - L) <= tol and b[i][4] > L:
                        ok = True
                        break
                else:
                    L = b[p][2]
                    if all(b[k][4] <= L for k in range(p + 1, i)) and abs(ext - L) <= tol and b[i][4] < L:
                        ok = True
                        break
            if ok:
                nivel = b[i][2] if lado > 0 else b[i][3]
                out.append((i, lado, nivel, ext, tipo))
                break                                     # um sinal por candle
    return out


def rodar(estudo, h1, fund, s, rk, rng, res):
    for tf, horas in S.TFS.items():
        b = S.barras(h1, horas)
        sig = sinais_div(b) if estudo == "DIV" else sinais_eng(b)
        com_sinal = {x[0] for x in sig}
        livre = 0
        for x in sig:
            i, lado, nivel, stop_px = x[:4]
            tipo = x[4] if len(x) > 4 else "div"
            t = b[i][0]
            if s not in rk.get(t // DIA * DIA, ()) or not (F.INICIO <= t < F.FIM):
                continue
            t0, t1 = b[i + 1][0], b[i + 1][0] + horas * H
            if t0 < livre:
                continue
            p = P.preencher(h1, t0, t1, lado, nivel)
            if p is None:
                continue
            ts, e = p
            fim = t + 11 * horas * H
            y = P.resultado(h1, fund, ts, e, lado, stop_px, fim)
            if y is None:
                continue
            exc = P.placebo(h1, fund, b, i, lado, y["risco"], fim - ts, com_sinal, rng, horas)
            res[tf].append({"sym": s, "ent": ts, "lado": lado, "risco": y["risco"], "r": y["r"], "tipo": tipo,
                            "r_bruto": y["r_bruto"], "excesso": y["r"] - exc if exc is not None else None})
            livre = y["sai"]


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
    res = {e: {tf: [] for tf in S.TFS} for e in ("DIV", "ENG")}
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
        for e in ("DIV", "ENG"):
            rodar(e, h1, fund, s, rk, rng, res[e])
    P.relatorio("ESTUDO 63 DIVERGENCIA IFR", res["DIV"])
    P.relatorio("ESTUDO 64 ENGOLFO/MARTELO EM SUPORTE", res["ENG"])
    m = lambda v: sum(v) / len(v) if v else float("nan")
    print("\nDescritivo do 64 por padrao (nao decide):")
    for tf, xs in res["ENG"].items():
        for tipo in ("engolfo", "martelo"):
            ys = [t for t in xs if t["tipo"] == tipo]
            print(f"  {tf} {tipo:<8} R liq {m([t['r'] for t in ys]):+.3f} | bruto {m([t['r_bruto'] for t in ys]):+.3f}"
                  f" | excesso {m([t['excesso'] for t in ys if t['excesso'] is not None]):+.3f} | n={len(ys)}")
    print(f"\n[{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main(sys.argv[1:])
