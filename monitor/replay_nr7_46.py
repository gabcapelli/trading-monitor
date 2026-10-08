"""
Estudo 62 -- compressao antes do rompimento: o sinal do 46 so depois de um NR7.
PRE-REGISTRADO em 08/10/2026, antes de rodar. Tentativa unica.

POR QUE
-------
O estudo 61 mostrou que o 46 so ganha nos rompimentos fortes (os que nunca
voltam ao nivel rompido). O estudo 58 mostrou que o NR7 (candle mais estreito
dos ultimos 7) e seguido de expansao (+0.06R sobre o placebo). Hipotese: um
rompimento de 7 dias logo depois de compressao tem mais chance de ser forte.
RESSALVA FIXA: o 46 e o NR7 ja foram vistos nestes dados. Um PASSA aqui so
autoriza papel, nao operacao.

SINAL, UNIVERSO E DADOS: os do estudo 46 (top 20 do dia, 4h, rompimento de 42
barras com volume >= 2x a media de 180; 1h do vision, inclui deslistados;
2020-2026), MAIS: alguma das 3 barras de 4h antes da barra do rompimento e NR7
(amplitude menor que a das 6 anteriores a ela).

TRADE (setup em R)
------------------
Entrada na abertura da barra seguinte (como o 46). Stop no nivel rompido (maxima
das 42 barras anteriores ao sinal; minima na venda), checado em 1h; sai a
min(nivel, abertura da hora). Distancia minima do stop: 0.3%. Sem toque: sai na
abertura 48h depois da entrada. 1R = distancia do stop. Custo 0.18% + funding.
Um trade por vez por par.

CRITERIO (todos juntos)
-----------------------
1. n >= 200.
2. R liquido com IC95 inteiro > 0 (bootstrap por semana).
3. Excesso sobre placebo com IC95 > 0. Placebo: mesmo par, mesmo lado, mesmo
   risco %, entrada a mercado em 5 barras de 4h aleatorias a ate 30 dias, mesmas
   regras de stop e de 48h.
4. R liquido > 0 nas duas metades e fora das 20 majors de hoje.
DESCRITIVO (sem decidir): o 46 com stop no nivel em TODOS os sinais (a hipotese
que esta no papel desde 08/10/2026, aqui dentro da amostra que a gerou) e nos
sinais sem NR7.

Uso (de dentro de monitor/):
    python replay_nr7_46.py
"""

import random
import sys
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

import replay_continuacao as C
import replay_continuacao_top20 as T
import replay_fluxo_spot_perp as F

H = 3_600_000
DIA = 86_400_000
MIN_RISCO = 0.003
N_PLACEBO = 5


def sinais(d):
    """(i, ts_entrada, lado, nivel, tem_nr7) e as barras de 4h."""
    b = C.barras4h(d)
    amp = [x[2] - x[3] for x in b]
    nr7 = [i >= 6 and amp[i] > 0 and amp[i] < min(amp[i - 6:i]) for i in range(len(b))]
    out = []
    for i in range(max(C.JANELA_MAX, C.JANELA_VOL), len(b) - 1):
        t, o, hi, lo, c, v = b[i]
        mx = max(x[2] for x in b[i - C.JANELA_MAX:i])
        mn = min(x[3] for x in b[i - C.JANELA_MAX:i])
        mv = sum(x[5] for x in b[i - C.JANELA_VOL:i]) / C.JANELA_VOL
        if v < C.MULT_VOL * mv:
            continue
        tem = any(nr7[i - 3:i])
        if c > mx:
            out.append((i, b[i + 1][0], +1, mx, tem))
        elif c < mn:
            out.append((i, b[i + 1][0], -1, mn, tem))
    return out, b


def trade(d, ent, lado, stop_px=None, risco=None):
    """Com stop_px (nivel) ou risco % fixo (placebo). Liquido em % e em R."""
    e = C.abertura(d, ent)
    if e is None:
        return None
    if stop_px is not None:
        risco = max(lado * (e - stop_px) / e, MIN_RISCO)
    stop = e * (1 - lado * risco)
    sai, p_out = ent + C.SAIDA_H * H, None
    for k in range(C.SAIDA_H):
        x = d["h"].get(ent + k * H)
        if x is None:
            return None
        if (x[3] <= stop) if lado > 0 else (x[2] >= stop):
            p_out = min(stop, x[1]) if lado > 0 else max(stop, x[1])
            sai = ent + (k + 1) * H
            break
    if p_out is None:
        p_out = C.abertura(d, sai)
        if p_out is None:
            return None
    liq = lado * 100 * (p_out / e - 1) - C.CUSTO - lado * C.funding(d, ent, sai)
    return {"liq": liq, "r": liq / (risco * 100), "risco": risco, "stop": sai < ent + C.SAIDA_H * H, "sai": sai}


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

    rng = random.Random(C.SEED)
    todos = []
    for s, d in dados.items():
        sg, b = sinais(d)
        com_sinal = {i for i, *_ in sg}
        livre = 0
        for i, ent, lado, nivel, tem in sg:
            if ent < livre or s not in rk.get(ent // DIA * DIA, set()):
                continue
            x = trade(d, ent, lado, stop_px=nivel)
            if x is None:
                continue
            pl = []
            if tem:
                for _ in range(40):
                    if len(pl) >= N_PLACEBO:
                        break
                    j = i + rng.randint(-180, 180)
                    if j < 1 or j + 1 >= len(b) or j in com_sinal or j == i:
                        continue
                    y = trade(d, b[j + 1][0], lado, risco=x["risco"])
                    if y:
                        pl.append(y["r"])
            todos.append({"sym": s, "ent": ent, "lado": lado, "nr7": tem, "r": x["r"], "liq": x["liq"],
                          "risco": x["risco"], "stop": x["stop"],
                          "excesso": x["r"] - sum(pl) / len(pl) if pl else None})
            livre = x["sai"]

    m = lambda v: sum(v) / len(v) if v else float("nan")
    xs = [t for t in todos if t["nr7"]]
    meio = sorted(t["ent"] for t in xs)[len(xs) // 2]
    b, ex = F.boot(xs, "r", 0.95), F.boot(xs, "excesso", 0.95)
    h1, h2 = m([t["r"] for t in xs if t["ent"] < meio]), m([t["r"] for t in xs if t["ent"] >= meio])
    fora = m([t["r"] for t in xs if t["sym"] not in C.MAJORS])
    print("\n" + "=" * 90 + "\nESTUDO 62: sinal do 46 depois de NR7, stop no nivel rompido, 48h\n" + "=" * 90)
    print(f"  R liquido  {F.fmt(b)}")
    print(f"  excesso    {F.fmt(ex)}")
    print(f"  liquido em % {m([t['liq'] for t in xs]):+.3f}% | risco medio {m([t['risco'] for t in xs])*100:.2f}%"
          f" | stopados {m([t['stop'] for t in xs])*100:.0f}% | acerto {m([t['r'] > 0 for t in xs])*100:.1f}%")
    print(f"  metades: 1a {h1:+.3f}R | 2a {h2:+.3f}R | fora das majors {fora:+.3f}R")
    for lado, nm in ((1, "compras"), (-1, "vendas")):
        print(f"  {nm:<8} {F.fmt(F.boot([t for t in xs if t['lado'] == lado], 'r', 0.95))}")
    pa = defaultdict(list)
    for t in xs:
        pa[datetime.fromtimestamp(t["ent"] / 1000, timezone.utc).year].append(t["r"])
    print("  por ano: " + " | ".join(f"{a} {m(v):+.2f} ({len(v)})" for a, v in sorted(pa.items())))
    ok = b and ex and b[3] >= 200 and b[1] > 0 and ex[1] > 0 and h1 > 0 and h2 > 0 and fora > 0
    print(f"\n  DECISAO: {'PASSA -> papel' if ok else 'NAO PASSA'}")
    print("\n  DESCRITIVO (dentro da amostra que gerou a hipotese do papel; nao decide)")
    sem = [t for t in todos if not t["nr7"]]
    print(f"  46 + stop no nivel, todos os sinais: {F.fmt(F.boot(todos, 'r', 0.95))} | liq {m([t['liq'] for t in todos]):+.3f}%")
    print(f"  46 + stop no nivel, sem NR7:         {F.fmt(F.boot(sem, 'r', 0.95))} | liq {m([t['liq'] for t in sem]):+.3f}%")
    print(f"\n[{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main(sys.argv[1:])
