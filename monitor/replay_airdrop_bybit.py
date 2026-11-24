"""
Estudo 93 (o 92 medido no perpetuo da BYBIT). PRE-REGISTRADO em 24/11/2026, antes
de olhar precos da Bybit. Tentativa unica.

- Eventos: os mesmos 110 do estudo 92 (Bybit Launchpool/Launchpad/Token Splash e
  OKX Jumpstart, sem os tokens do 91).
- Perpetuo linear da Bybit TICKERUSDT ou 1000TICKERUSDT (API publica v5, 1h).
- Entrada: a mais tardia entre (anuncio arredondado + 1h) e (primeira hora do
  perpetuo + 1h); se o perpetuo ja negociava 1 dia antes do anuncio, so o anuncio.
  Perpetuo so mais de 30 dias depois: fora. Saida: entrada + 7 dias, sem stop.
- liq = -ret - 0.18% + funding recebido (historico da Bybit);
  excesso = -ret - (vender 20 majors da Binance no mesmo intervalo).
- PASSA se liq E excesso com IC95 > 0. Menos de 30 eventos: SEM AMOSTRA.
- Ressalva conhecida antes: a API nao tem contratos removidos (vies CONTRA a
  hipotese, porque tokens que desabaram e sairam ficam de fora).
"""

import json
import os
import time
import urllib.request
from datetime import datetime, timezone

import replay_deslistagem as D
from replay_airdrop_listagem import linha, CUSTO, H, DIA
from replay_airdrop_outras import eventos, DIR

CACHE = os.path.join(DIR, "bybit_cache")
API = "https://api.bybit.com/v5/market"


def _get(url):
    for t in range(5):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            return json.loads(urllib.request.urlopen(req, timeout=30).read())
        except Exception:
            time.sleep(2 + 3 * t)
    return {}


def velas(sym, t0, t1):
    f = os.path.join(CACHE, f"{sym}_{t0}.json")
    if os.path.exists(f):
        return {int(k): v for k, v in json.load(open(f)).items()}
    out, fim = {}, t1
    while fim > t0:
        r = (_get(f"{API}/kline?category=linear&symbol={sym}&interval=60&start={t0}&end={fim}&limit=1000")
             .get("result") or {}).get("list") or []
        if not r:
            break
        for k in r:
            out[int(k[0])] = float(k[1])
        novo = min(int(k[0]) for k in r) - 1
        if novo >= fim or len(r) < 1000:
            break
        fim = novo
        time.sleep(0.1)
    json.dump(out, open(f, "w"))
    return out


def funding(sym, t0, t1):
    r = (_get(f"{API}/funding/history?category=linear&symbol={sym}&startTime={t0}&endTime={t1 - 1}&limit=200")
         .get("result") or {}).get("list") or []
    return 100 * sum(float(x["fundingRate"]) for x in r if t0 <= int(x["fundingRateTimestamp"]) < t1)


def trade(e, cache):
    ts = e["ts"]
    for sym in (f"{e['token']}USDT", f"1000{e['token']}USDT"):
        s = velas(sym, ts - 2 * DIA, ts + 40 * DIA)
        if not s:
            continue
        primeira = min(s)
        ent_anuncio = (ts // H + 1) * H
        if primeira <= ts - DIA:
            ent, via = ent_anuncio, "anuncio"
        else:
            if primeira > ts + 30 * DIA:
                return None
            ent = max(ent_anuncio, primeira + H)
            via = "anuncio" if ent == ent_anuncio else "listagem_perp"
        sai = ent + 7 * DIA
        a, b = s.get(ent), s.get(sai)
        if not a or not b:
            return None
        bruto = -100 * (b / a - 1)
        c = D.cesta(ent, sai, cache)
        return {**e, "sym": sym, "via": via, "bruto": bruto,
                "liq": bruto - CUSTO + funding(sym, ent, sai), "exc": None if c is None else bruto - c}
    return None


def main():
    os.makedirs(CACHE, exist_ok=True)
    evs = eventos()
    cache, ts = {}, []
    for e in evs:
        t = trade(e, cache)
        if t:
            ts.append(t)
    print(f"Eventos: {len(evs)} · com perpetuo da Bybit e janela completa: {len(ts)}\n")
    l1, lo1 = linha("DECIDE liq (vendido 7d)", [t["liq"] for t in ts])
    l2, lo2 = linha("DECIDE excesso vs cesta", [t["exc"] for t in ts])
    print(l1); print(l2); print("\n  descritivos:")
    for k in sorted({t["tipo"] for t in ts}):
        print(linha(f"liq {k}", [t["liq"] for t in ts if t["tipo"] == k])[0])
    for k in ("anuncio", "listagem_perp"):
        print(linha(f"liq via {k}", [t["liq"] for t in ts if t["via"] == k])[0])
        print(linha(f"exc via {k}", [t["exc"] for t in ts if t["via"] == k])[0])
    ano = lambda t: datetime.fromtimestamp(t["ts"] / 1000, timezone.utc).year
    for y in sorted({ano(t) for t in ts}):
        print(linha(f"liq {y}", [t["liq"] for t in ts if ano(t) == y])[0])
    v = sorted(t["liq"] for t in ts)
    if len(v) > 5:
        print(f"  sem os 5 maiores: {sum(v[:-5]) / (len(v) - 5):+.2f}% · acerto {sum(x > 0 for x in v) / len(v):.0%}")
    print("\nDECISAO:", "SEM AMOSTRA" if len(ts) < 30 else ("PASSA" if lo1 > 0 and lo2 > 0 else "NAO PASSA"))
    json.dump(ts, open(os.path.join(DIR, "estudo93_trades.json"), "w"))


if __name__ == "__main__":
    main()
