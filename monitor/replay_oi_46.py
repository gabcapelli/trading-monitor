"""
Estudos 74 (rompimento do 46 com open interest subindo) e 75 (rompimento do 46
com open interest caindo, operado contra). PRE-REGISTRADOS em 19/10/2026, antes
de rodar. Tentativa unica cada.

MECANISMO: um rompimento feito por posicao nova (open interest subindo) tem
combustivel; um feito por recompra de vendidos (open interest caindo) se esgota
quando a recompra acaba. RESSALVA FIXA: os sinais do 46 ja foram vistos nestes
dados (45, 46, 61, 62). Um PASSA aqui so autoriza papel, nao operacao.

SINAL E DADOS: os do estudo 46 (replay_nr7_46.sinais: top 20 do dia, 4h,
rompimento de 42 barras com volume >= 2x a media de 180; 1h do vision, inclui
deslistados). Periodo 2020-10 a 2026-09 (open interest da Binance Vision desde
2020-09, cache_metrics/). Sinais sem open interest nas duas leituras ficam fora.

OPEN INTEREST: contratos = valor do open interest (ultimo registro de 5 min da
ultima hora da barra) / fechamento dessa hora. dOI = ln(contratos no fim da
barra do rompimento / contratos no fim da barra anterior).

ESTUDO 74 -- OI SUBINDO, A FAVOR: dOI > 0. Trade do estudo 62: entrada na
abertura da barra seguinte, stop no nivel rompido, saida 48h depois.

ESTUDO 75 -- OI CAINDO, CONTRA: dOI < 0. Entrada na abertura da barra seguinte
no lado OPOSTO ao rompimento; stop no extremo da barra do rompimento (maxima
quando vende um rompimento de alta); saida 48h depois.

Nos dois: stop checado em 1h, distancia minima 0.3%, 1R = distancia do stop,
custo 0.18% + funding, um trade por vez por par e por estudo.

CRITERIO (o do estudo 62, por estudo, todos juntos)
1. n >= 200.
2. R liquido com IC95 inteiro > 0 (bootstrap por semana).
3. Excesso sobre placebo com IC95 > 0. Placebo: mesmo par, lado e risco %,
   entrada a mercado em 5 barras de 4h aleatorias a ate 30 dias, mesmo stop % e
   48h.
4. R liquido > 0 nas duas metades e fora das 20 majors de hoje.

Uso (de dentro de monitor/):
    python replay_oi_46.py
"""

import math
import random
import sys
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

import baixar_metrics as B
import replay_continuacao as C
import replay_continuacao_top20 as T
import replay_fluxo_spot_perp as F
import replay_nr7_46 as N

H = 3_600_000
DIA = 86_400_000
INICIO = int(datetime(2020, 10, 1, tzinfo=timezone.utc).timestamp() * 1000)


def contratos(d, met, ts):
    m, x = met.get(ts), d["h"].get(ts)
    if not m or not m[0] or not x or x[4] <= 0:
        return None
    return m[0] / x[4]


def meses(d):
    return sorted({datetime.fromtimestamp(t / 1000, timezone.utc).strftime("%Y-%m")
                   for t in d["h"] if INICIO - 40 * DIA <= t < F.FIM})


def placebo(d, b, i, lado, risco, com_sinal, rng):
    pl = []
    for _ in range(40):
        if len(pl) >= N.N_PLACEBO:
            break
        j = i + rng.randint(-180, 180)
        if j < 1 or j + 1 >= len(b) or j in com_sinal or j == i:
            continue
        y = N.trade(d, b[j + 1][0], lado, risco=risco)
        if y:
            pl.append(y["r"])
    return sum(pl) / len(pl) if pl else None


def relatorio(nome, xs):
    m = lambda v: sum(v) / len(v) if v else float("nan")
    print("\n" + "=" * 90 + f"\n{nome}\n" + "=" * 90)
    if not xs:
        print("  sem trades")
        return
    meio = sorted(t["ent"] for t in xs)[len(xs) // 2]
    b, ex = F.boot(xs, "r", 0.95), F.boot(xs, "excesso", 0.95)
    h1, h2 = m([t["r"] for t in xs if t["ent"] < meio]), m([t["r"] for t in xs if t["ent"] >= meio])
    fora = m([t["r"] for t in xs if t["sym"] not in C.MAJORS])
    print(f"  R liquido  {F.fmt(b)}")
    print(f"  excesso    {F.fmt(ex)}")
    print(f"  R bruto {m([t['r_bruto'] for t in xs]):+.3f}R | liquido em % {m([t['liq'] for t in xs]):+.3f}%"
          f" | risco medio {m([t['risco'] for t in xs])*100:.2f}% | stopados {m([t['stop'] for t in xs])*100:.0f}%"
          f" | acerto {m([t['r'] > 0 for t in xs])*100:.1f}%")
    print(f"  metades: 1a {h1:+.3f}R | 2a {h2:+.3f}R | fora das majors {fora:+.3f}R")
    for lado, nm in ((1, "compras"), (-1, "vendas")):
        print(f"  {nm:<8} {F.fmt(F.boot([t for t in xs if t['lado'] == lado], 'r', 0.95))}")
    pa = defaultdict(list)
    for t in xs:
        pa[datetime.fromtimestamp(t["ent"] / 1000, timezone.utc).year].append(t["r"])
    print("  por ano: " + " | ".join(f"{a} {m(v):+.2f} ({len(v)})" for a, v in sorted(pa.items())))
    ok = b and ex and b[3] >= 200 and b[1] > 0 and ex[1] > 0 and h1 > 0 and h2 > 0 and fora > 0
    print(f"  DECISAO: {'PASSA -> papel' if ok else 'NAO PASSA'}")


def main(argv):
    t0 = time.time()
    syms = T.simbolos()
    with ThreadPoolExecutor(16) as ex:
        vols = dict(zip(syms, ex.map(T.diario, syms)))
    vols = {s: v for s, v in vols.items() if v}
    rk = T.ranking(vols)
    alguma = sorted({s for d, v in rk.items() if INICIO <= d < F.FIM for s in v})
    with ThreadPoolExecutor(8) as ex:
        dados = dict(zip(alguma, ex.map(lambda s: T.carregar_1h(s, INICIO - 40 * DIA, F.FIM + 3 * DIA), alguma)))
    dados = {s: d for s, d in dados.items() if d["h"]}
    print(f"simbolos {len(dados)} [{time.time()-t0:.0f}s]", flush=True)

    rng = random.Random(C.SEED)
    res = {"74": [], "75": []}
    dois = []
    n_sinais = sem_oi = 0
    for s, d in dados.items():
        met = B.carregar(s, meses(d))
        sg, b = N.sinais(d)
        com_sinal = {i for i, *_ in sg}
        livre = {"74": 0, "75": 0}
        for i, ent, lado, nivel, _ in sg:
            if not (INICIO <= ent < F.FIM) or s not in rk.get(ent // DIA * DIA, set()):
                continue
            n_sinais += 1
            t = b[i][0]
            c1, c0 = contratos(d, met, t + 3 * H), contratos(d, met, t - H)
            if not c1 or not c0:
                sem_oi += 1
                continue
            doi = math.log(c1 / c0)
            dois.append(doi)
            if doi > 0:
                e, lado_t, stop_px = "74", lado, nivel
            elif doi < 0:
                e, lado_t, stop_px = "75", -lado, (b[i][2] if lado > 0 else b[i][3])
            else:
                continue
            if ent < livre[e]:
                continue
            x = N.trade(d, ent, lado_t, stop_px=stop_px)
            if x is None:
                continue
            bruto = x["liq"] + C.CUSTO + lado_t * C.funding(d, ent, x["sai"])
            exc = placebo(d, b, i, lado_t, x["risco"], com_sinal, rng)
            res[e].append({"sym": s, "ent": ent, "lado": lado_t, "r": x["r"], "liq": x["liq"],
                           "r_bruto": bruto / (x["risco"] * 100), "risco": x["risco"], "stop": x["stop"],
                           "excesso": x["r"] - exc if exc is not None else None})
            livre[e] = x["sai"]

    dois.sort()
    print(f"sinais do 46 no periodo: {n_sinais} | sem open interest: {sem_oi} | "
          f"dOI subindo {sum(v > 0 for v in dois)} caindo {sum(v < 0 for v in dois)} | "
          f"mediana dOI {dois[len(dois)//2]*100:+.2f}%" if dois else "sem dOI")
    relatorio("ESTUDO 74: rompimento do 46 com open interest subindo, a favor, stop no nivel, 48h", res["74"])
    relatorio("ESTUDO 75: rompimento do 46 com open interest caindo, contra, stop no extremo, 48h", res["75"])
    print("\nFunil para o papel (descritivo; R bruto > 0, excesso IC95 > 0, n >= 200):")
    for e, xs in res.items():
        ex = F.boot(xs, "excesso", 0.95)
        rb = sum(t["r_bruto"] for t in xs) / len(xs) if xs else float("nan")
        ok = ex and ex[3] >= 200 and ex[1] > 0 and rb > 0
        print(f"  {e}: excesso {F.fmt(ex)} | bruto {rb:+.3f}R -> {'CANDIDATO' if ok else 'nao'}")
    print(f"\n[{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main(sys.argv[1:])
