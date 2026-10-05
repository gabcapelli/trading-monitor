"""
Estudo 46 -- a regra do estudo 45 (rompimento de 7 dias com volume, 4h,
segurando 48h), SEM MUDAR NADA, nas 20 moedas de maior volume A CADA DIA,
escolhidas entre TODOS os perpetuos USDT-M da Binance, inclusive os
deslistados depois. PRE-REGISTRADO em 05/10/2026, antes de rodar.

POR QUE
-------
No estudo 45 a regra nao passou nos pares liquidos de DE, mas nas 20 majors
de hoje deu +0.93% por trade (excesso +0.56%, positivo em todos os anos e em
18 de 20 moedas). O Gabriel perguntou: por que nao operar so as principais?
Porque as "20 principais" foram escolhidas olhando para HOJE: sao as que
subiram. Comprar rompimentos nelas tem vies de sobrevivencia (e foi nelas que
a ideia nasceu). O teste justo e o que um robo veria no proprio dia: as 20 de
maior volume naquele dia, sem saber quais sobreviveriam.

UNIVERSO (point-in-time)
------------------------
- Todos os simbolos USDT-M da lista do S3 do data.binance.vision (inclui
  deslistados), sem perpetuos de acao/commodity (underlyingType != COIN na
  exchangeInfo; ausente = deslistado = cripto) e sem stablecoins (base com USD,
  DAI, EUR).
- Volume em dolar diario dos candles de 1d. A cada dia, as 20 de maior volume
  nos 30 dias anteriores. A regra so opera um sinal se o par estiver no top 20
  no dia do sinal.

REGRA E MEDIDAS: identicas ao estudo 45 (replay_continuacao.py): barras de
4h, rompimento de 42 barras com volume >= 2x a media de 180, entrada na barra
seguinte, saida em 48h, sem stop, custo 0.18% + funding real; excesso sobre ate
30 outros pares do top 20 do dia, mesmo lado e horas; bootstrap por semana.

CRITERIO PARA IR AO PAPEL (fixado antes; todos juntos)
------------------------------------------------------
1. `liq` com IC95 inteiro > 0 E `excesso` com IC95 inteiro > 0.
2. Media de `liq` > 0 em cada metade do periodo.
3. Media de `liq` > 0 nos trades em moedas FORA das 20 majors de hoje (para nao
   depender so das que sabemos que sobreviveram).
Ressalva fixa: o periodo (2020-2026) e o mesmo do estudo 45; BTC/ETH estao
sempre no top 20, entao ha sobreposicao com A. Passar aqui autoriza papel, que
e o teste final.

Uso (de dentro de monitor/):
    python replay_continuacao_top20.py --baixar
    python replay_continuacao_top20.py
"""

import json
import os
import re
import sys
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

import replay_continuacao as C
import replay_deslistagem as D
import replay_monitoring_tag as MT

DIA = 86_400_000
H = 3_600_000
TOP = 20
INICIO = int(datetime(2020, 1, 1, tzinfo=timezone.utc).timestamp() * 1000)


def simbolos():
    tp = MT.tipos()
    out = []
    for s in MT.universo():
        base = s[:-4]
        if tp.get(s, "COIN") != "COIN" or re.search(r"USD|DAI|EUR", base):
            continue
        out.append(s)
    return out


def diario(sym):
    """{dia: volume em dolar} a partir dos candles de 1d do vision (cache)."""
    fp = os.path.join(D.DIR_VISION, f"vol1d_{sym}.json")
    if os.path.exists(fp):
        return {int(k): v for k, v in json.load(open(fp)).items()}
    out = {}
    hoje = datetime.now(timezone.utc).strftime("%Y-%m")
    for mes in D.meses_disponiveis("futures/um", sym):
        if mes < "2019-12":
            continue
        raw = D._get(f"{D.VISION}/futures/um/monthly/klines/{sym}/1d/{sym}-1d-{mes}.zip")
        if raw:
            for r in D._csv_zip(raw):
                out[D._ms(r[0]) // DIA * DIA] = float(r[7])     # quote asset volume
    json.dump(out, open(fp, "w"))
    return out


def ranking(vols):
    """{dia: set dos TOP simbolos por volume dos 30 dias anteriores}"""
    dias = sorted({d for v in vols.values() for d in v if d >= INICIO})
    acum = {s: {} for s in vols}
    for s, v in vols.items():
        ds = sorted(v)
        soma, fila = 0.0, []
        for d in ds:
            acum[s][d] = soma
            fila.append(v[d])
            soma += v[d]
            if len(fila) > 30:
                soma -= fila.pop(0)
    out = {}
    for d in dias:
        cand = sorted(((acum[s].get(d, 0.0), s) for s in vols), reverse=True)[:TOP]
        out[d] = {s for v, s in cand if v > 0}
    return out


def carregar_1h(sym, t0, t1):
    k = D.klines("futures/um", sym, t0, t1)
    h = {ts: [ts] + v for ts, v in k.items() if v[4] > 0}
    D.funding(sym, t0, t1)            # garante o cache mensal de funding
    fund = []
    for mes in D._meses(t0, t1):
        fp = os.path.join(D.DIR_VISION, f"funding_{sym}_{mes}.json")
        if os.path.exists(fp):
            fund += [tuple(x) for x in json.load(open(fp))]
    return {"h": h, "fund": fund}


def main(argv):
    t0 = time.time()
    syms = simbolos()
    with ThreadPoolExecutor(16) as ex:
        vols = dict(zip(syms, ex.map(diario, syms)))
    vols = {s: v for s, v in vols.items() if v}
    rk = ranking(vols)
    alguma_vez = sorted({s for v in rk.values() for s in v})
    print(f"Simbolos cripto USDT-M: {len(syms)} | ja estiveram no top {TOP}: {len(alguma_vez)}", flush=True)
    agora = int(time.time() * 1000)
    with ThreadPoolExecutor(8) as ex:
        dados = dict(zip(alguma_vez, ex.map(lambda s: carregar_1h(s, INICIO - 40 * DIA, agora), alguma_vez)))
    dados = {s: d for s, d in dados.items() if d["h"]}
    if "--baixar" in argv:
        print(f"dados ok [{time.time()-t0:.0f}s]")
        return
    # liquidez no formato do estudo 45: so os do top do dia passam
    trades = []
    for s in dados:
        livre = 0
        for ent, lado in C.sinais(s, dados[s]):
            if ent < livre or s not in rk.get(ent // DIA * DIA, set()):
                continue
            sai = ent + C.SAIDA_H * H
            p0, p1 = C.abertura(dados[s], ent), C.abertura(dados[s], sai)
            if p0 is None or p1 is None:
                continue
            bruto = lado * 100 * (p1 / p0 - 1)
            f = -lado * C.funding(dados[s], ent, sai)
            trades.append({"sym": s, "ent": ent, "lado": lado, "bruto": bruto, "liq": bruto - C.CUSTO + f})
            livre = sai
    import random
    rng = random.Random(C.SEED)
    for t in trades:
        pool = [x for x in rk.get(t["ent"] // DIA * DIA, set()) if x != t["sym"] and x in dados]
        rng.shuffle(pool)
        rets = []
        for x in pool[:C.N_BASE]:
            a, b = C.abertura(dados[x], t["ent"]), C.abertura(dados[x], t["ent"] + C.SAIDA_H * H)
            if a and b:
                rets.append(t["lado"] * 100 * (b / a - 1))
        t["excesso"] = t["bruto"] - sum(rets) / len(rets) if rets else None

    liq, exc = C.boot(trades, "liq"), C.boot(trades, "excesso")
    meio = sorted(t["ent"] for t in trades)[len(trades) // 2]
    m = lambda xs: sum(xs) / len(xs) if xs else float("nan")
    h1 = m([t["liq"] for t in trades if t["ent"] < meio])
    h2 = m([t["liq"] for t in trades if t["ent"] >= meio])
    fora = [t for t in trades if t["sym"] not in C.MAJORS]
    mf = m([t["liq"] for t in fora])
    print("\n" + "=" * 90 + f"\nTOP {TOP} POR VOLUME A CADA DIA (inclui deslistados), regra do estudo 45\n" + "=" * 90)
    print(f"  liq     {C.fmt(liq)}")
    print(f"  excesso {C.fmt(exc)}")
    print(f"  metades: 1a {h1:+.3f}% | 2a {h2:+.3f}%")
    print(f"  fora das 20 majors de hoje: liq medio {mf:+.3f}% (n={len(fora)}) | {C.fmt(C.boot(fora, 'liq'))}")
    for lado, nome in ((1, "so compras"), (-1, "so vendas")):
        sub = [t for t in trades if t["lado"] == lado]
        print(f"  {nome:<11} liq {C.fmt(C.boot(sub, 'liq'))} | excesso {C.fmt(C.boot(sub, 'excesso'))}")
    por_ano = defaultdict(list)
    for t in trades:
        por_ano[datetime.fromtimestamp(t["ent"] / 1000, timezone.utc).year].append(t["liq"])
    print("  por ano: " + " | ".join(f"{a}: {m(v):+.2f}% (n={len(v)})" for a, v in sorted(por_ano.items())))
    ok = (len(trades) >= C.MIN_TRADES and liq and exc and liq[1] > 0 and exc[1] > 0 and h1 > 0 and h2 > 0 and mf > 0)
    print(f"\n  DECISAO: {'PASSA -> vai para o papel' if ok else 'NAO PASSA'}  [{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main(sys.argv[1:])
