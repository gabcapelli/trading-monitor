"""
Estudo 61 -- a regra do estudo 46 com ENTRADA POR ORDEM LIMITADA no reteste.
PRE-REGISTRADO em 08/10/2026, antes de rodar.

POR QUE
-------
O estudo 46 (rompimento de 7 dias com volume, 4h, top 20 do dia) e o unico
sinal direcional com bruto grande (+0.76% por trade) e ficou "por um fio" no
liquido. O custo (0.18% a mercado) e o preco de entrada pesam. Em vez de comprar
a mercado depois do rompimento, deixar uma ordem limitada no nivel rompido (o
"reteste" classico da resistencia que virou suporte). Paga taxa de maker e
entra melhor. O risco e a selecao adversa: os rompimentos que nao recuam (os
mais fortes) ficam de fora. O teste mede as duas coisas.

SINAL, UNIVERSO E DADOS: identicos ao estudo 46 (replay_continuacao_top20.py):
barras de 4h, fechamento acima da maxima das 42 barras anteriores (7 dias) com
volume >= 2x a media de 180; venda no espelho; so se o par estiver no top 20 do
dia; candles de 1h do vision (inclui deslistados), 2020-2026.

ENTRADA
-------
- Ordem limitada no nivel rompido (a maxima das 42 barras anteriores na compra;
  a minima na venda), valida por 24h a partir da abertura da barra seguinte ao
  sinal (o instante em que o 46 entraria a mercado).
- Preenche na primeira hora em que a minima <= nivel (compra); preco =
  min(nivel, abertura da hora). Espelho na venda.
- Sem preenchimento em 24h: sem trade.

SAIDA: a mesma do 46, na abertura 48h depois da entrada a mercado do 46 (fixa a
data de saida, para isolar o efeito da entrada). Sem stop, como o 46.

CUSTO: 0.11% ida e volta = 0.02% de maker na entrada + 0.09% na saida a mercado
(taxa de taker de 0.05% + 0.04% de slippage), mais funding real do preenchimento
a saida.

CRITERIO PARA IR AO PAPEL (o mesmo do 46; todos juntos; por trade preenchido)
1. liquido com IC95 > 0 E excesso sobre o top 20 do dia (mesmo lado e mesma
   janela, ate 30 pares) com IC95 > 0;
2. media liquida > 0 nas duas metades;
3. media liquida > 0 fora das 20 majors de hoje;
4. n >= 300.
DESCRITIVO: taxa de preenchimento; resultado do 46 (a mercado) nos sinais
preenchidos e nos nao preenchidos (selecao adversa); resultado por SINAL das
duas formas (nao preenchido = 0).

Uso (de dentro de monitor/):
    python replay_46_limitada.py
"""

import random
import sys
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

import replay_continuacao as C
import replay_continuacao_top20 as T

H = 3_600_000
DIA = 86_400_000
VALIDADE_H = 24
CUSTO_LIM = 0.11


def sinais_com_nivel(d):
    b = C.barras4h(d)
    out = []
    for i in range(max(C.JANELA_MAX, C.JANELA_VOL), len(b) - 1):
        t, o, hi, lo, c, v = b[i]
        mx = max(x[2] for x in b[i - C.JANELA_MAX:i])
        mn = min(x[3] for x in b[i - C.JANELA_MAX:i])
        mv = sum(x[5] for x in b[i - C.JANELA_VOL:i]) / C.JANELA_VOL
        if v < C.MULT_VOL * mv:
            continue
        if c > mx:
            out.append((b[i + 1][0], +1, mx))
        elif c < mn:
            out.append((b[i + 1][0], -1, mn))
    return out


def preencher(d, ent, lado, nivel):
    for k in range(VALIDADE_H):
        x = d["h"].get(ent + k * H)
        if x is None:
            return None
        if lado > 0 and x[3] <= nivel:
            return ent + k * H, min(nivel, x[1])
        if lado < 0 and x[2] >= nivel:
            return ent + k * H, max(nivel, x[1])
    return None


def main(argv):
    t0 = time.time()
    syms = T.simbolos()
    with ThreadPoolExecutor(16) as ex:
        vols = dict(zip(syms, ex.map(T.diario, syms)))
    vols = {s: v for s, v in vols.items() if v}
    rk = T.ranking(vols)
    alguma = sorted({s for v in rk.values() for s in v})
    agora = int(time.time() * 1000)
    with ThreadPoolExecutor(8) as ex:
        dados = dict(zip(alguma, ex.map(lambda s: T.carregar_1h(s, T.INICIO - 40 * DIA, agora), alguma)))
    dados = {s: d for s, d in dados.items() if d["h"]}
    print(f"simbolos {len(dados)} [{time.time()-t0:.0f}s]", flush=True)

    sinais = []
    for s in dados:
        livre = 0
        for ent, lado, nivel in sinais_com_nivel(dados[s]):
            if ent < livre or s not in rk.get(ent // DIA * DIA, set()):
                continue
            sai = ent + C.SAIDA_H * H
            p0, p1 = C.abertura(dados[s], ent), C.abertura(dados[s], sai)
            if p0 is None or p1 is None:
                continue
            mercado = lado * 100 * (p1 / p0 - 1) - C.CUSTO - lado * C.funding(dados[s], ent, sai)
            sg = {"sym": s, "ent": ent, "lado": lado, "mercado": mercado, "liq": None}
            f = preencher(dados[s], ent, lado, nivel)
            if f:
                tf, pf = f
                bruto = lado * 100 * (p1 / pf - 1)
                sg.update(ent_lim=tf, bruto=bruto, liq=bruto - CUSTO_LIM - lado * C.funding(dados[s], tf, sai))
            sinais.append(sg)
            livre = sai

    rng = random.Random(C.SEED)
    trades = [x for x in sinais if x["liq"] is not None]
    for t in trades:
        pool = [x for x in rk.get(t["ent"] // DIA * DIA, set()) if x != t["sym"] and x in dados]
        rng.shuffle(pool)
        rets = []
        for x in pool[:C.N_BASE]:
            a, b = C.abertura(dados[x], t["ent_lim"]), C.abertura(dados[x], t["ent"] + C.SAIDA_H * H)
            if a and b:
                rets.append(t["lado"] * 100 * (b / a - 1))
        t["excesso"] = t["bruto"] - sum(rets) / len(rets) if rets else None

    m = lambda xs: sum(xs) / len(xs) if xs else float("nan")
    liq, exc = C.boot(trades, "liq"), C.boot(trades, "excesso")
    meio = sorted(t["ent"] for t in trades)[len(trades) // 2]
    h1 = m([t["liq"] for t in trades if t["ent"] < meio])
    h2 = m([t["liq"] for t in trades if t["ent"] >= meio])
    fora = [t for t in trades if t["sym"] not in C.MAJORS]
    mf = m([t["liq"] for t in fora])
    nao = [x for x in sinais if x["liq"] is None]
    print("\n" + "=" * 90 + "\nESTUDO 61: regra do 46 com ordem limitada no nivel rompido\n" + "=" * 90)
    print(f"  sinais {len(sinais)} | preenchidos {len(trades)} ({len(trades)/len(sinais)*100:.1f}%)")
    print(f"  liq     {C.fmt(liq)}")
    print(f"  excesso {C.fmt(exc)}")
    print(f"  metades: 1a {h1:+.3f}% | 2a {h2:+.3f}%")
    print(f"  fora das 20 majors de hoje: {mf:+.3f}% (n={len(fora)})")
    for lado, nome in ((1, "so compras"), (-1, "so vendas")):
        print(f"  {nome:<11} {C.fmt(C.boot([t for t in trades if t['lado'] == lado], 'liq'))}")
    pa = defaultdict(list)
    for t in trades:
        pa[datetime.fromtimestamp(t["ent"] / 1000, timezone.utc).year].append(t["liq"])
    print("  por ano: " + " | ".join(f"{a}: {m(v):+.2f}% ({len(v)})" for a, v in sorted(pa.items())))
    print("\n  DESCRITIVO (selecao adversa e resultado por sinal)")
    print(f"  46 a mercado, todos os sinais:        {C.fmt(C.boot(sinais, 'mercado'))}")
    print(f"  46 a mercado, sinais preenchidos:     {C.fmt(C.boot(trades, 'mercado'))}")
    print(f"  46 a mercado, sinais NAO preenchidos: {C.fmt(C.boot(nao, 'mercado'))}")
    for x in sinais:
        x["por_sinal"] = x["liq"] if x["liq"] is not None else 0.0
    print(f"  limitada por sinal (nao preench. = 0): {C.fmt(C.boot(sinais, 'por_sinal'))}")
    ok = (len(trades) >= C.MIN_TRADES and liq and exc and liq[1] > 0 and exc[1] > 0 and h1 > 0 and h2 > 0 and mf > 0)
    print(f"\n  DECISAO: {'PASSA -> vai para o papel' if ok else 'NAO PASSA'}  [{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main(sys.argv[1:])
