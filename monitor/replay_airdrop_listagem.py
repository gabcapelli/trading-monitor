"""
Estudo 91 (vender o token novo distribuido de graca). PRE-REGISTRADO em
24/11/2026, antes de olhar qualquer preco. Tentativa unica.

Hipotese: no HODLer Airdrop e no Launchpool/Megadrop da Binance o token chega
de graca a milhares de carteiras, com pouca oferta em circulacao e avaliacao
alta. Quem recebeu de graca vende nos primeiros dias (como o insider no
desbloqueio). Pressao vendedora com data conhecida.

EVENTOS
- Avisos "Introducing ... (HODLer Airdrops|Launchpool|Megadrop)" em cat48.json.
- Ticker = o que vem depois de "Earn"/"Farm" no titulo.
- Listagem = primeira hora com volume > 0 do perpetuo TICKERUSDT (ou 1000TICKER)
  ate 30 dias depois do aviso. Sem perpetuo nesse prazo: fora.

OPERACAO (perpetuo, VENDIDO, sem stop)
- Entrada: abertura da hora listagem + 1h. Saida: entrada + 7 dias.
- `liq` (decide) = -retorno - 0.18% + funding recebido (real).
- `excesso` (decide) = -retorno - (vender a cesta de 20 majors no mesmo intervalo).
- Bootstrap por evento, IC95. PASSA se `liq` E `excesso` com IC95 > 0.
  Menos de 30 eventos: SEM AMOSTRA.
- DESCRITIVOS: so HODLer; so Launchpool/Megadrop; so 2026; saida em 3 e 14 dias;
  entrada 24h depois da listagem; mediana e pior trade.
"""

import json
import os
import random
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone

import replay_deslistagem as D

H, DIA = 3_600_000, 86_400_000
CUSTO = 0.18
SEED, N = 42, 5000


def eventos():
    arts = json.load(open(os.path.join(D.DIR_ANUNCIOS, "cat48.json"), encoding="utf-8"))
    out, vistos = [], set()
    for a in sorted(arts, key=lambda a: a["releaseDate"]):
        t = a["title"]
        if not re.match(r"Introducing .*(HODLer Airdrop|Launchpool|Megadrop)", t):
            continue
        m = re.search(r"(?:Earn|Farm)\s+([A-Z0-9]+)", t)
        if not m or m.group(1) in vistos:
            continue
        vistos.add(m.group(1))
        out.append({"ts": a["releaseDate"], "token": m.group(1),
                    "tipo": "hodler" if "HODLer" in t else "launchpool"})
    return out


def listagem(tk, ts):
    for sym in (f"{tk}USDT", f"1000{tk}USDT"):
        meses = D.meses_disponiveis("futures/um", sym)
        alvo = {datetime.fromtimestamp(x / 1000, timezone.utc).strftime("%Y-%m") for x in (ts, ts + 30 * DIA)}
        if not alvo & set(meses):
            continue
        serie = D.klines("futures/um", sym, ts - 2 * DIA, ts + 50 * DIA)
        hs = sorted(k for k, v in serie.items() if v[4] > 0)
        if hs and ts - 2 * DIA <= hs[0] <= ts + 30 * DIA:
            return sym, hs[0], serie
    return None, None, None


def trade(e, cache):
    sym, t_list, serie = listagem(e["token"], e["ts"])
    if not sym:
        return None
    r = {**e, "sym": sym}
    for nome, atraso, dias in (("p", 1, 7), ("d3", 1, 3), ("d14", 1, 14), ("e24", 24, 7)):
        ti = t_list + atraso * H
        tf = ti + dias * DIA
        a, b = D.abertura(serie, ti), D.abertura(serie, tf)
        if not a or not b:
            r[nome] = r[nome + "_exc"] = None
            continue
        bruto = -100 * (b / a - 1)
        c = D.cesta(ti, tf, cache)
        r[nome] = bruto - CUSTO + 100 * D.funding(sym, ti, tf)
        r[nome + "_exc"] = None if c is None else bruto - c
    return r


def boot(xs):
    xs = [x for x in xs if x is not None]
    if len(xs) < 3:
        return None
    rng = random.Random(SEED)
    ms = sorted(sum(rng.choice(xs) for _ in xs) / len(xs) for _ in range(N))
    s = sorted(xs)
    return sum(xs) / len(xs), ms[int(.025 * N)], ms[int(.975 * N) - 1], len(xs), s[len(s) // 2], s[0], s[-1]


def linha(rot, xs):
    r = boot(xs)
    if not r:
        return f"  {rot:<34} (insuficiente)", None
    m, lo, hi, n, med, mn, mx = r
    return (f"  {rot:<34} n={n:>3} media {m:+7.2f}% IC95 [{lo:+7.2f}, {hi:+7.2f}] "
            f"mediana {med:+6.2f}% pior {mn:+7.1f}% melhor {mx:+6.1f}%"), lo


def main():
    evs = eventos()
    print(f"Avisos com ticker: {len(evs)} (hodler {sum(e['tipo']=='hodler' for e in evs)})")
    cache, ts = {}, []
    for e in evs:
        t = trade(e, cache)
        if t and t["p"] is not None:
            ts.append(t)
    print(f"Com perpetuo e janela completa: {len(ts)}\n")
    l1, lo1 = linha("DECIDE liq (vendido 7d)", [t["p"] for t in ts])
    l2, lo2 = linha("DECIDE excesso vs cesta", [t["p_exc"] for t in ts])
    print(l1); print(l2)
    print("\n  descritivos:")
    for rot, f in (("so HODLer", lambda t: t["tipo"] == "hodler"),
                   ("so Launchpool/Megadrop", lambda t: t["tipo"] == "launchpool"),
                   ("so 2026", lambda t: t["ts"] >= 1767225600000)):
        sub = [t for t in ts if f(t)]
        print(linha(f"liq {rot}", [t["p"] for t in sub])[0])
        print(linha(f"exc {rot}", [t["p_exc"] for t in sub])[0])
    for k, rot in (("d3", "saida 3d"), ("d14", "saida 14d"), ("e24", "entrada +24h, 7d")):
        print(linha(f"liq {rot}", [t[k] for t in ts])[0])
        print(linha(f"exc {rot}", [t[k + '_exc'] for t in ts])[0])
    if len(ts) < 30:
        print("\nDECISAO: SEM AMOSTRA")
    else:
        print(f"\nDECISAO: {'PASSA' if lo1 > 0 and lo2 > 0 else 'NAO PASSA'}")
    json.dump(ts, open(os.path.join(D.DIR_ANUNCIOS, "estudo91_trades.json"), "w"))


if __name__ == "__main__":
    main()
