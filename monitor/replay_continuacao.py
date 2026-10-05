"""
Estudo 45 -- continuacao em movimentos fortes nas moedas liquidas, segurando
48h. PRE-REGISTRADO em 05/10/2026, antes de rodar.

POR QUE
-------
O estudo 16 achou que, em cripto, o preco CONTINUA no curto prazo (o bruto do
"espelho" da mean reversion seria Sharpe ~+0.80), mas girar de hora em hora
custa mais do que o sinal rende. A literatura diz o mesmo de outro jeito: moedas
grandes e liquidas tem momentum semanal; as pequenas e iliquidas revertem
(Up or down? Short-term reversal, momentum, and liquidity effects in
cryptocurrency markets, 2021). Ideia: entrar SO em movimentos fortes (rompimento
com volume) das moedas mais liquidas e segurar 48h, girando muito menos.

Pedido do Gabriel (05/10/2026): algo mais rapido que o estudo 43, e so ir
para o papel se mostrar de fato que pode ser lucrativo.

DADOS E AMOSTRAS
----------------
- Candles de 1h dos perpetuos USDT-M da Binance em cache (cache_binance/,
  dados_binance.py), funding real. 388 pares vivos hoje (vies de
  sobrevivencia assumido, como nos estudos anteriores).
- A (20 majors): onde a ideia nasceu (estudo 16) -- descritivo e checagem de sinal.
- DE (os 368 das amostras D e E): DECIDE. Ja usadas em outros estudos; e o
  que ha. Filtro de liquidez no proprio instante: so entram, a cada sinal, os
  50 pares de DE com maior volume em dolar nos 30 dias anteriores.

REGRA (canonica, sem grade)
---------------------------
- Barras de 4h (00, 04, 08... UTC) montadas do 1h.
- COMPRA no fechamento de uma barra de 4h se: fechamento > maxima das 42 barras
  anteriores (7 dias) E volume da barra >= 2x a media das 180 barras anteriores
  (30 dias). VENDA: espelho (fechamento < minima de 7 dias, mesmo volume).
- Entrada na abertura da barra seguinte; saida na abertura 48h depois. Sem stop.
  Um trade por par de cada vez (sinal com trade aberto e ignorado).
- Custo: 0.18% ida e volta + funding real (pago/recebido conforme o lado).

MEDIDAS (% do nocional)
-----------------------
- `liq` = bruto - 0.18% + funding (positivo = o trade ganhou).
- `excesso` = bruto - media do mesmo lado em ate 30 outros pares liquidos nas
  mesmas horas (linha de base transversal, estudo 23).
- Bootstrap por SEMANA de entrada, IC95, 5000 reamostragens.

CRITERIO PARA IR AO PAPEL (fixado antes; todos juntos)
------------------------------------------------------
1. DE liquido, compras + vendas: `liq` com IC95 inteiro > 0 E `excesso` com
   IC95 inteiro > 0.
2. Estabilidade: media de `liq` > 0 em cada metade do periodo (DE).
3. Coerencia: media de `liq` > 0 tambem em A (majors).
Com menos de 300 trades em DE: SEM AMOSTRA. Falhou um item: NAO PASSA, e nao
se monta papel (decisao do Gabriel: nao perder tempo).

VALIDACAO
---------
`--passeio`: precos trocados por passeio aleatorio sem deriva (volume real,
mesmas datas), 10 sementes. O resultado bruto tem de ficar em ~0 e nenhuma
semente pode PASSAR.

DESCRITIVOS
-----------
Compras e vendas separadas; por ano; saida em 24h e 96h; custo de 0.3%.

Uso (de dentro de monitor/):
    python replay_continuacao.py --passeio
    python replay_continuacao.py
"""

import json
import math
import os
import random
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone

from replay_ema_ribbon import UNIVERSO

AQUI = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(AQUI, "cache_binance")
H = 3_600_000
B4 = 4 * H
CUSTO = 0.18
JANELA_MAX = 42
JANELA_VOL = 180
MULT_VOL = 2.0
SAIDA_H = 48
TOP_LIQ = 50
N_BASE = 30
MIN_TRADES = 300
SEED = 42
MAJORS = [s.replace("-SWAP", "").replace("-", "") for s in UNIVERSO]


def carregar(sym, passeio=None):
    fp = os.path.join(CACHE, f"{sym}_1h_3000.json")
    if not os.path.exists(fp):
        return None
    k = json.load(open(fp))
    k = [x for x in k if x[5] > 0]
    if passeio is not None:
        rng = random.Random(f"{sym}{passeio}")
        rets = [math.log(b[4] / a[4]) for a, b in zip(k, k[1:]) if a[4] > 0 and b[4] > 0]
        sd = math.sqrt(sum(r * r for r in rets) / max(len(rets), 1)) or 0.01
        p, out = 1.0, []
        for x in k:
            # caminho intra-hora: 3 passos, maxima/minima do caminho (so afeta a deteccao
            # do rompimento; o resultado usa aberturas, sem stop)
            o, hi, lo = p, p, p
            for _ in range(3):
                p *= math.exp(rng.gauss(-sd * sd / 6, sd / math.sqrt(3)))
                hi, lo = max(hi, p), min(lo, p)
            out.append([x[0], o, hi, lo, p, x[5]])
        k = out
    fpf = os.path.join(CACHE, f"{sym}_funding.json")
    fund = json.load(open(fpf)) if os.path.exists(fpf) and passeio is None else []
    return {"h": {x[0]: x for x in k}, "fund": fund}


def barras4h(d):
    g = defaultdict(list)
    for ts in sorted(d["h"]):
        g[ts // B4 * B4].append(d["h"][ts])
    out = []
    for t in sorted(g):
        xs = g[t]
        if len(xs) < 4:
            continue
        out.append((t, xs[0][1], max(x[2] for x in xs), min(x[3] for x in xs), xs[-1][4],
                    sum(x[5] * x[4] for x in xs)))     # volume em dolar
    return out


def abertura(d, ts):
    x = d["h"].get(ts)
    return x[1] if x else None


def funding(d, t0, t1):
    return 100 * sum(r for ts, r in d["fund"] if t0 <= ts < t1)


def sinais(sym, d):
    b = barras4h(d)
    out = []
    for i in range(max(JANELA_MAX, JANELA_VOL), len(b) - 1):
        t, o, hi, lo, c, v = b[i]
        mx = max(x[2] for x in b[i - JANELA_MAX:i])
        mn = min(x[3] for x in b[i - JANELA_MAX:i])
        mv = sum(x[5] for x in b[i - JANELA_VOL:i]) / JANELA_VOL
        if v < MULT_VOL * mv:
            continue
        if c > mx:
            out.append((b[i + 1][0], +1))
        elif c < mn:
            out.append((b[i + 1][0], -1))
    return out


def liquidez(dados):
    """{sym: {dia: volume em dolar dos 30 dias anteriores}}"""
    out = {}
    for s, d in dados.items():
        por_dia = defaultdict(float)
        for ts, x in d["h"].items():
            por_dia[ts // (24 * H)] += x[5] * x[4]
        dias = sorted(por_dia)
        acc, fila, r = 0.0, [], {}
        for dd in dias:
            r[dd] = acc
            fila.append(por_dia[dd])
            acc += por_dia[dd]
            if len(fila) > 30:
                acc -= fila.pop(0)
        out[s] = r
    return out


def rodar(syms, dados, liq, top, saida_h=SAIDA_H, custo=CUSTO):
    """Trades do universo `syms`, so quando o par esta entre os `top` mais liquidos do universo no dia."""
    trades = []
    por_dia_rank = {}
    for s in syms:
        livre = 0
        for ent, lado in sinais(s, dados[s]):
            if ent < livre:
                continue
            dia = ent // (24 * H)
            if top is not None:
                if dia not in por_dia_rank:
                    vols = sorted(((liq[x].get(dia, 0), x) for x in syms), reverse=True)
                    por_dia_rank[dia] = {x for _, x in vols[:top]}
                if s not in por_dia_rank[dia]:
                    continue
            sai = ent + saida_h * H
            p0, p1 = abertura(dados[s], ent), abertura(dados[s], sai)
            if p0 is None or p1 is None:
                continue
            bruto = lado * 100 * (p1 / p0 - 1)
            f = -lado * funding(dados[s], ent, sai)       # comprado paga funding positivo
            trades.append({"sym": s, "ent": ent, "lado": lado, "bruto": bruto, "liq": bruto - custo + f})
            livre = sai
    # linha de base transversal
    rng = random.Random(SEED)
    for t in trades:
        dia = t["ent"] // (24 * H)
        pool = [x for x in (por_dia_rank.get(dia) or syms) if x != t["sym"]]
        rng.shuffle(pool)
        rets = []
        for x in pool:
            a, b = abertura(dados[x], t["ent"]), abertura(dados[x], t["ent"] + saida_h * H)
            if a and b:
                rets.append(t["lado"] * 100 * (b / a - 1))
            if len(rets) >= N_BASE:
                break
        t["excesso"] = t["bruto"] - sum(rets) / len(rets) if rets else None
    return trades


def boot(trades, chave, conf=0.95):
    g = defaultdict(list)
    for t in trades:
        if t.get(chave) is not None:
            g[t["ent"] // (7 * 24 * H)].append(t[chave])
    grupos = list(g.values())
    if len(grupos) < 5:
        return None
    n = sum(len(v) for v in grupos)
    m = sum(sum(v) for v in grupos) / n
    rng = random.Random(SEED)
    ms = []
    for _ in range(5000):
        s = k = 0
        for _ in range(len(grupos)):
            v = grupos[rng.randrange(len(grupos))]
            s += sum(v)
            k += len(v)
        ms.append(s / k)
    ms.sort()
    a = (1 - conf) / 2
    return m, ms[int(a * 5000)], ms[int((1 - a) * 5000) - 1], n


def fmt(r):
    return "(insuficiente)" if r is None else f"n={r[3]:>5} media {r[0]:+6.3f}% IC95 [{r[1]:+6.3f}, {r[2]:+6.3f}]"


def avaliar(A, DE, imprimir=True):
    liq_de = boot(DE, "liq")
    exc_de = boot(DE, "excesso")
    meio = sorted(t["ent"] for t in DE)[len(DE) // 2] if DE else 0
    h1 = [t["liq"] for t in DE if t["ent"] < meio]
    h2 = [t["liq"] for t in DE if t["ent"] >= meio]
    m1, m2 = (sum(h1) / len(h1) if h1 else float("nan")), (sum(h2) / len(h2) if h2 else float("nan"))
    ma = sum(t["liq"] for t in A) / len(A) if A else float("nan")
    ok = (len(DE) >= MIN_TRADES and liq_de and exc_de and liq_de[1] > 0 and exc_de[1] > 0
          and m1 > 0 and m2 > 0 and ma > 0)
    if imprimir:
        print(f"  DE liquido: liq     {fmt(liq_de)}")
        print(f"  DE liquido: excesso {fmt(exc_de)}")
        print(f"  DE metades: 1a {m1:+.3f}% | 2a {m2:+.3f}%   |   A (majors): liq medio {ma:+.3f}% (n={len(A)})")
    if len(DE) < MIN_TRADES:
        return "SEM AMOSTRA"
    return "PASSA" if ok else "NAO PASSA"


def universos():
    de = []
    for f in ("universo_d.txt", "universo_e.txt"):
        de += open(os.path.join(AQUI, f)).read().split()
    de = [s for s in dict.fromkeys(de) if s not in MAJORS]
    return MAJORS, de


def main(argv):
    t0 = time.time()
    a_syms, de_syms = universos()
    if "--passeio" in argv:
        res = []
        for sem in range(1, 11):
            dados = {s: d for s in a_syms + de_syms if (d := carregar(s, passeio=sem))}
            liq = liquidez(dados)
            A = rodar([s for s in a_syms if s in dados], dados, liq, None)
            DE = rodar([s for s in de_syms if s in dados], dados, liq, TOP_LIQ)
            b = boot(DE, "bruto")
            dec = avaliar(A, DE, imprimir=False)
            res.append(dec)
            print(f"  semente {sem}: DE bruto {fmt(b)} | decisao {dec}", flush=True)
        print(f"\n  PASSEIO: {sum(r == 'PASSA' for r in res)}/10 PASSA falso  [{time.time()-t0:.0f}s]")
        return
    dados = {s: d for s in a_syms + de_syms if (d := carregar(s))}
    a_syms = [s for s in a_syms if s in dados]
    de_syms = [s for s in de_syms if s in dados]
    liq = liquidez(dados)
    A = rodar([s for s in a_syms if s in dados], dados, liq, None)
    DE = rodar([s for s in de_syms if s in dados], dados, liq, TOP_LIQ)
    print(f"Pares com dados: A {sum(s in dados for s in a_syms)} | DE {sum(s in dados for s in de_syms)} "
          f"(top {TOP_LIQ} por liquidez a cada dia)")
    print("\n" + "=" * 90 + "\nDECISAO (compras + vendas, saida 48h, custo 0.18% + funding)\n" + "=" * 90)
    dec = avaliar(A, DE)
    print("\n  Descritivos:")
    for lado, nome in ((1, "so compras"), (-1, "so vendas")):
        sub = [t for t in DE if t["lado"] == lado]
        print(f"    DE {nome:<11} liq {fmt(boot(sub, 'liq'))} | excesso {fmt(boot(sub, 'excesso'))}")
    print(f"    DE bruto (sem custo)   {fmt(boot(DE, 'bruto'))}")
    print(f"    A  todos               liq {fmt(boot(A, 'liq'))}")
    por_ano = defaultdict(list)
    for t in DE:
        por_ano[datetime.fromtimestamp(t["ent"] / 1000, timezone.utc).year].append(t["liq"])
    print("    DE por ano (liq medio): " + " | ".join(f"{a}: {sum(v)/len(v):+.2f}% (n={len(v)})" for a, v in sorted(por_ano.items())))
    for sh in (24, 96):
        print(f"    saida em {sh}h: DE liq {fmt(boot(rodar(de_syms, dados, liq, TOP_LIQ, saida_h=sh), 'liq'))}")
    print(f"    custo 0.3%:  DE liq {fmt(boot(rodar(de_syms, dados, liq, TOP_LIQ, custo=0.3), 'liq'))}")
    print(f"\n  DECISAO: {dec}  [{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main(sys.argv[1:])
