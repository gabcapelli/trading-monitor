"""
Estudo 92 (vender o token distribuido de graca em OUTRAS corretoras). PRE-REGISTRADO
em 24/11/2026, antes de olhar qualquer preco. Tentativa unica.

Hipotese: a mesma do estudo 91 (quem recebe token de graca vende), agora com
eventos da Bybit (Launchpool, Launchpad, Token Splash) e da OKX (Jumpstart).

EVENTOS
- cache_anuncios/outras/bybit.json e okx.json (APIs publicas de anuncios).
- Ticker: Launchpool "Earn a Share of N TICKER"; Launchpad "(TICKER)"; Token
  Splash "share of the N TICKER prize"; Jumpstart "Introducing TICKER (".
- Um evento por ticker (o primeiro). FORA os tickers que ja estavam no estudo 91
  (amostra independente) e stablecoins (USDT, USDC, U, USDE, MNT, BTC, ETH, SOL).

OPERACAO: a regra do papel do 91 (airdrop_paper.py), em 1h
- Vendido no perpetuo da Binance TICKERUSDT/1000TICKERUSDT.
- Entrada = a mais tardia entre (anuncio arredondado + 1h) e (primeira hora
  negociada do perpetuo + 1h). Perpetuo so mais de 30 dias depois: fora.
- Saida: entrada + 7 dias. Sem stop. liq = -ret - 0.18% + funding recebido;
  excesso = -ret - (vender 20 majors).
- PASSA se liq E excesso com IC95 > 0. Menos de 30 eventos: SEM AMOSTRA.
- Descritivos: por corretora/tipo; entrada so pelo anuncio (perp ja negociava)
  vs. pela listagem do perpetuo; por ano.
"""

import json
import os
import re
from collections import defaultdict
from datetime import datetime, timezone

import replay_deslistagem as D
from replay_airdrop_listagem import boot, linha, CUSTO, H, DIA

DIR = os.path.join(D.DIR_ANUNCIOS, "outras")
FORA = {"USDT", "USDC", "U", "USDE", "MNT", "BTC", "ETH", "SOL", "BBSOL", "BNB", "XAUT0"}


def eventos():
    ev = []
    for x in json.load(open(os.path.join(DIR, "bybit.json"), encoding="utf-8")):
        t, ts = x["title"], int(x.get("publishTime") or x["dateTimestamp"])
        m = None
        if "launchpool" in t.lower():
            m, tipo = re.search(r"Share of [\d,.]+\s*([A-Z0-9]+)", t), "bybit_launchpool"
        elif "launchpad" in t.lower():
            m, tipo = re.search(r"\(([A-Z0-9]+)\)", t), "bybit_launchpad"
        elif "token splash" in t.lower():
            m, tipo = re.search(r"of (?:the )?[\d,.]+\s*([A-Z0-9]+)\s+prize", t, re.I), "bybit_splash"
        if m:
            ev.append({"ts": ts, "token": m.group(1).upper(), "tipo": tipo})
    for x in json.load(open(os.path.join(DIR, "okx.json"), encoding="utf-8")):
        m = re.search(r"Introducing (\S+) \(.*Jumpstart", x["title"])
        if m:
            ev.append({"ts": int(x["pTime"]), "token": m.group(1).upper(), "tipo": "okx_jumpstart"})
    usados = {t["token"] for t in json.load(open(os.path.join(D.DIR_ANUNCIOS, "estudo91_trades.json")))}
    import replay_airdrop_listagem as A
    usados |= {e["token"] for e in A.eventos()}
    out, vistos = [], set()
    for e in sorted(ev, key=lambda e: e["ts"]):
        if e["token"] in vistos or e["token"] in usados or e["token"] in FORA:
            continue
        vistos.add(e["token"])
        out.append(e)
    return out


def trade(e, cache):
    tk, ts = e["token"], e["ts"]
    for sym in (f"{tk}USDT", f"1000{tk}USDT"):
        meses = D.meses_disponiveis("futures/um", sym)
        if not meses:
            continue
        mes_ev = datetime.fromtimestamp(ts / 1000, timezone.utc).strftime("%Y-%m")
        lim = datetime.fromtimestamp((ts + 30 * DIA) / 1000, timezone.utc).strftime("%Y-%m")
        if meses[0] > lim or meses[-1] < mes_ev:
            continue
        serie = D.klines("futures/um", sym, min(ts, ts) - 2 * DIA, ts + 40 * DIA)
        primeira = D.meses_disponiveis  # placeholder
        hs = sorted(k for k, v in serie.items() if v[4] > 0)
        if not hs:
            continue
        if meses[0] < mes_ev or hs[0] < ts - DIA:
            t_perp = None                      # perp ja negociava antes do anuncio
            ent = (ts // H + 1) * H
        else:
            t_perp = hs[0]
            if t_perp > ts + 30 * DIA:
                return None
            ent = max((ts // H + 1) * H, t_perp + H)
        sai = ent + 7 * DIA
        a, b = D.abertura(serie, ent), D.abertura(serie, sai)
        if not a or not b:
            return None
        bruto = -100 * (b / a - 1)
        c = D.cesta(ent, sai, cache)
        return {**e, "sym": sym, "via": "anuncio" if t_perp is None or ent == (ts // H + 1) * H else "listagem_perp",
                "liq": bruto - CUSTO + 100 * D.funding(sym, ent, sai),
                "exc": None if c is None else bruto - c}
    return None


def main():
    evs = eventos()
    print(f"Eventos novos (fora do 91): {len(evs)}", dict(sorted(defaultdict(int, {k: sum(e['tipo'] == k for e in evs) for k in {e['tipo'] for e in evs}}).items())))
    cache, ts = {}, []
    for e in evs:
        t = trade(e, cache)
        if t:
            ts.append(t)
    print(f"Com perpetuo da Binance e janela completa: {len(ts)}\n")
    l1, lo1 = linha("DECIDE liq (vendido 7d)", [t["liq"] for t in ts])
    l2, lo2 = linha("DECIDE excesso vs cesta", [t["exc"] for t in ts])
    print(l1); print(l2); print("\n  descritivos:")
    for k in sorted({t["tipo"] for t in ts}):
        print(linha(f"liq {k}", [t["liq"] for t in ts if t["tipo"] == k])[0])
    for k in ("anuncio", "listagem_perp"):
        print(linha(f"liq via {k}", [t["liq"] for t in ts if t["via"] == k])[0])
    for y in sorted({datetime.fromtimestamp(t['ts'] / 1000, timezone.utc).year for t in ts}):
        print(linha(f"liq {y}", [t["liq"] for t in ts if datetime.fromtimestamp(t['ts'] / 1000, timezone.utc).year == y])[0])
    print("\nDECISAO:", "SEM AMOSTRA" if len(ts) < 30 else ("PASSA" if lo1 > 0 and lo2 > 0 else "NAO PASSA"))
    json.dump(ts, open(os.path.join(DIR, "estudo92_trades.json"), "w"))


if __name__ == "__main__":
    main()
