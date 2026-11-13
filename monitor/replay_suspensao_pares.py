"""
Estudos 85 (suspensao de deposito/saque na Upbit) e 86 (remocao de pares a vista
na Binance). PRE-REGISTRADOS em 13/11/2026, antes de olhar qualquer preco.
Tentativa unica cada; a regra de operacao e a do teste de papel da Monitoring
Tag (estudo 38) e da replica 39: entrada 60 min depois do aviso (pior caso do
workflow horario), saida 24h depois do aviso, sem stop.

ESTUDO 85 -- SUSPENSAO DE DEPOSITO/SAQUE NA UPBIT (COMPRA)
Hipotese ("bombeamento de cercado"): com a carteira travada a arbitragem fecha
e o varejo coreano puxa o preco; se o perpetuo da Binance acompanhar, comprar
depois do aviso ganha.
- Feed publico da Upbit, category=wallet (cache_anuncios/upbit_wallet.json).
- Evento = cada "(TKR)" num titulo com "중단" (suspensao) e "입출금", "입금" ou
  "출금". Horario: `first_listed_at` (o titulo e o `listed_at` mudam quando o
  aviso e atualizado para "완료").
- Fora: token com designacao de alerta ou fim de suporte na Upbit (categoria
  trade, titulo com "유의" ou "종료") ou com anuncio da Binance (Monitoring Tag
  ou deslistagem) entre 2 dias antes e 1 dia depois; mesmo token com outro
  evento a menos de 14 dias (fica o primeiro).

ESTUDO 86 -- REMOCAO DE PARES A VISTA NA BINANCE (VENDA)
Hipotese: a Binance remove pares de pouca liquidez; para o token-base e um
aviso antecipado de fraqueza (antes de Monitoring Tag / deslistagem).
- Avisos "Notice of Removal of (Spot) Trading Pairs" do feed ja em cache
  (cat161.json); pares lidos do corpo do aviso (cache em remocao_pares.json).
- Evento = token-base de par removido com cotacao em BTC, ETH ou BNB (remocao
  por falta de liquidez do token; pares em stablecoin/moeda fiduciaria refletem
  a cotacao e ficam de fora). Fora: base BTC, ETH, BNB e stablecoins.
- Fora: token com anuncio de Monitoring Tag ou deslistagem entre 2 dias antes e
  1 dia depois; mesmo token com outro aviso a menos de 30 dias (fica o primeiro).

COMUM
- Perpetuo USDT-M da Binance (TKRUSDT ou 1000TKRUSDT), com candle de 1h com
  volume na entrada e 30 dias antes.
- Entrada: abertura do minuto floor(aviso) + 60. Saida: floor(aviso) + 24h.
- `liq` (decide) = bruto - 0.5% +/- funding real.
- `excesso` (decide) = bruto - a mesma operacao no BTCUSDT nos mesmos minutos.
- Bootstrap por AVISO, IC95, 5000 reamostragens.
- CRITERIO: PASSA se `liq` E `excesso` tiverem IC95 inteiro acima de zero. Com
  menos de 15 avisos com trade: SEM AMOSTRA. Lembrete do estudo 37: com poucos
  grupos e cauda pesada o IC cobre menos que o nominal.
- DESCRITIVOS (nao decidem): entrada com 2 min; placebo 30 dias antes; total
  perdido entre o aviso e a entrada; saida em 7 dias; so 2025-26.

Uso (de dentro de monitor/):
    python replay_suspensao_pares.py --contar
    python replay_suspensao_pares.py
"""

import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone

import replay_deslistagem as D
import replay_latencia as RL
import replay_monitoring_tag as MT
from replay_deslistagem import DIA, H

MIN = 60_000
ARQ_WALLET = os.path.join(D.DIR_ANUNCIOS, "upbit_wallet.json")
ARQ_TRADE = os.path.join(D.DIR_ANUNCIOS, "upbit_trade.json")
ARQ_PARES = os.path.join(D.DIR_ANUNCIOS, "remocao_pares.json")
ESTAVEIS = {"USDT", "USDC", "DAI", "TUSD", "USDP", "FDUSD", "BUSD", "PAX", "USDS", "SUSD", "UST", "USTC",
            "EUR", "EURI", "AEUR", "GBP", "AUD", "WBTC", "WBETH", "BETH", "BNSOL", "PAXG"}
CUSTO = 0.5
ENTRADA_MIN, SAIDA_MIN, SAIDA_LONGA_MIN = 60, 24 * 60, 7 * 24 * 60
PLACEBO_DIAS = 30
MIN_AVISOS = 15


def baixar_wallet():
    out, p = [], 1
    while True:
        u = f"https://api-manager.upbit.com/api/v1/announcements?os=web&page={p}&per_page=20&category=wallet"
        try:
            req = urllib.request.Request(u, headers={"User-Agent": "Mozilla/5.0"})
            d = json.loads(urllib.request.urlopen(req, timeout=30).read())["data"]
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(10)
                continue
            raise
        out += d["notices"]
        if p >= d["total_pages"]:
            break
        p += 1
        time.sleep(2)
    with open(ARQ_WALLET, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False)


def _ts_upbit(n):
    return int(datetime.fromisoformat(n.get("first_listed_at") or n["listed_at"]).timestamp() * 1000)


def _binance_colado():
    b = defaultdict(list)
    for e in MT.eventos() + D.eventos():
        b[e["token"]].append(e["ts"])
    return b


def _filtra(brutos, colados, dedup_dias):
    """Tira eventos com anuncio colado e repeticoes do mesmo token."""
    out, motivos, ultimo = [], defaultdict(int), {}
    for e in sorted(brutos, key=lambda e: e["ts"]):
        tk, ts = e["token"], e["ts"]
        if any(ts - 2 * DIA <= x <= ts + DIA for fonte in colados for x in fonte.get(tk, [])):
            motivos["anuncio colado"] += 1
            continue
        if tk in ultimo and ts - ultimo[tk] < dedup_dias * DIA:
            motivos["repetido"] += 1
            continue
        ultimo[tk] = ts
        out.append(e)
    return out, motivos


def eventos_upbit():
    if not os.path.exists(ARQ_WALLET):
        baixar_wallet()
    with open(ARQ_WALLET, encoding="utf-8") as f:
        notas = json.load(f)
    alerta = defaultdict(list)
    with open(ARQ_TRADE, encoding="utf-8") as f:
        for n in json.load(f):
            if "유의" in n["title"] or "종료" in n["title"]:
                for tk in re.findall(r"\(([A-Z0-9]{1,12})\)", n["title"]):
                    alerta[tk].append(_ts_upbit(n))
    brutos = []
    for n in notas:
        t = n["title"]
        if "중단" not in t or not re.search(r"입출금|입금|출금", t):
            continue
        ts = _ts_upbit(n)
        for tk in dict.fromkeys(re.findall(r"\(([A-Z0-9]{1,12})\)", t)):
            if tk not in ESTAVEIS:
                brutos.append({"token": tk, "ts": ts, "titulo": t})
    return _filtra(brutos, (alerta, _binance_colado()), 14)


def pares_removidos():
    cache = {}
    if os.path.exists(ARQ_PARES):
        with open(ARQ_PARES) as f:
            cache = json.load(f)
    with open(os.path.join(D.DIR_ANUNCIOS, "cat161.json")) as f:
        arts = [a for a in json.load(f) if re.match(r"(Updated )?Notice of Removal of (Spot )?Trading Pairs", a["title"])]
    url = "https://www.binance.com/bapi/composite/v1/public/cms/article/detail/query?articleCode="
    for a in arts:
        if a["code"] in cache:
            continue
        for tentativa in range(8):                       # a Binance responde 429 em rajada: espera e insiste
            try:
                req = urllib.request.Request(url + a["code"], headers={"User-Agent": "Mozilla/5.0"})
                raw = urllib.request.urlopen(req, timeout=30).read()
                break
            except urllib.error.HTTPError as e:
                if e.code != 429 or tentativa == 7:
                    raise
                time.sleep(30 * (tentativa + 1))
        corpo = (json.loads(raw)["data"] or {}).get("body") or ""
        cache[a["code"]] = sorted(set(re.findall(r"\b([A-Z0-9]{2,12}/[A-Z]{3,6})\b", corpo)))
        with open(ARQ_PARES, "w") as f:
            json.dump(cache, f)
        time.sleep(2)
    return arts, cache


def eventos_pares():
    arts, cache = pares_removidos()
    brutos = []
    for a in arts:
        bases = dict.fromkeys(p.split("/")[0] for p in cache.get(a["code"], []) if p.split("/")[1] in ("BTC", "ETH", "BNB"))
        for tk in bases:
            if tk not in ESTAVEIS and tk not in ("BTC", "ETH", "BNB"):
                brutos.append({"token": tk, "ts": a["releaseDate"], "titulo": a["title"]})
    return _filtra(brutos, (_binance_colado(),), 30)


def montar(e, sinal):
    """sinal +1 = compra, -1 = venda. Retornos em % do nocional, positivo = ganhou."""
    sym, _ = D.simbolo_perp(e["token"], e["ts"])
    if not sym:
        return None, "sem perpetuo"
    s1h = D.klines("futures/um", sym, e["ts"] - 31 * DIA, e["ts"] + DIA)
    ent_h = (e["ts"] // H) * H
    if not any(s1h.get(ent_h + k * H, [0] * 5)[4] > 0 for k in (0, 1)) or s1h.get(ent_h - 30 * DIA, [0] * 5)[4] == 0:
        return None, "sem volume ou listado ha menos de 30 dias"
    b = e["ts"] // MIN * MIN
    t = {**e, "sym": sym}
    for nome, desloc in (("", 0), ("placebo_", -PLACEBO_DIAS * DIA)):
        b0 = b + desloc
        s = RL.serie_1m(sym, b0 - MIN, b0 + SAIDA_MIN * MIN + MIN)
        bt = RL.serie_1m("BTCUSDT", b0 - MIN, b0 + SAIDA_MIN * MIN + MIN)
        p0, p_out, b_out = s.get(b0), s.get(b0 + SAIDA_MIN * MIN), bt.get(b0 + SAIDA_MIN * MIN)
        for k in (ENTRADA_MIN, 2):
            p_in, b_in = s.get(b0 + k * MIN), bt.get(b0 + k * MIN)
            if None in (p_in, p_out, b_in, b_out):
                if nome == "" and k == ENTRADA_MIN:
                    return None, "sem candle de 1m"
                continue
            bruto = sinal * 100 * (p_out / p_in - 1)
            suf = "" if k == ENTRADA_MIN else "_2min"
            t[f"{nome}bruto{suf}"] = bruto
            t[f"{nome}excesso{suf}"] = bruto - sinal * 100 * (b_out / b_in - 1)
            if nome == "":
                f = 100 * D.funding(sym, b0 + k * MIN, b0 + SAIDA_MIN * MIN)
                t[f"liq{suf}"] = bruto - CUSTO - sinal * f
        if nome == "":
            p_in = s.get(b0 + ENTRADA_MIN * MIN)
            if p0 is not None and p_in:
                t["perdido"] = sinal * 100 * (p_in / p0 - 1)
            fim = b0 + SAIDA_LONGA_MIN * MIN
            p7 = RL.serie_1m(sym, fim, fim).get(fim)
            b7, b_in = RL.serie_1m("BTCUSDT", fim, fim).get(fim), bt.get(b0 + ENTRADA_MIN * MIN)
            if p7 and b7 and p_in and b_in:
                t["excesso_7d"] = sinal * 100 * (p7 / p_in - 1) - sinal * 100 * (b7 / b_in - 1)
    return t, "ok"


def estudo(nome, evs_motivos, sinal, argv):
    evs, mot = evs_motivos
    lado = "COMPRADO" if sinal > 0 else "VENDIDO"
    print("\n" + "=" * 100 + f"\n{nome}\n" + "=" * 100)
    print(f"Eventos (token x aviso): {len(evs)} em {len({e['ts'] for e in evs})} avisos | fora: {dict(mot)}")
    trades, motivos = [], defaultdict(int)
    for e in evs:
        t, m = montar(e, sinal)
        motivos[m] += 1
        if t:
            trades.append(t)
    n_av = len({t["ts"] for t in trades})
    print("Montagem:", dict(motivos))
    print(f"Trades validos: {len(trades)} em {n_av} avisos")
    por_ano = defaultdict(int)
    for t in trades:
        por_ano[datetime.fromtimestamp(t["ts"] / 1000, timezone.utc).year] += 1
    print("Por ano:", dict(sorted(por_ano.items())))
    if "--contar" in argv:
        return
    print(f"\n{lado}, entrada +{ENTRADA_MIN} min, saida +{SAIDA_MIN // 60}h (positivo = ganhou)")
    lo = {}
    for chave, rot in (("liq", "LIQUIDO, custo 0.5% + funding (decide)"), ("excesso", "EXCESSO sobre o BTC (decide)"),
                       ("bruto", "bruto"), ("liq_2min", "liquido, entrada +2 min"),
                       ("excesso_2min", "excesso, entrada +2 min"), ("placebo_excesso", "PLACEBO -30d: excesso"),
                       ("perdido", "movimento entre o aviso e a entrada"), ("excesso_7d", "excesso, saida em 7 dias")):
        r = RL.boot(trades, chave)
        print(f"  {rot:<42} {RL.fmt(r)}")
        if r:
            lo[chave] = r[1]
    recentes = [t for t in trades if t["ts"] >= 1735689600000]
    print(f"  {'excesso, so 2025-26':<42} {RL.fmt(RL.boot(recentes, 'excesso'))}")
    pos = sum(t["liq"] > 0 for t in trades)
    print(f"  liquido positivo em {pos}/{len(trades)}")
    if n_av < MIN_AVISOS:
        dec = f"SEM AMOSTRA PARA DECIDIR ({n_av} < {MIN_AVISOS} avisos)"
    else:
        dec = "PASSA" if lo.get("liq", -1) > 0 and lo.get("excesso", -1) > 0 else "NAO PASSA"
    print(f"\n  DECISAO {nome}: {dec}")


def main(argv):
    t0 = time.time()
    estudo("ESTUDO 85 SUSPENSAO NA UPBIT", eventos_upbit(), +1, argv)
    estudo("ESTUDO 86 REMOCAO DE PARES NA BINANCE", eventos_pares(), -1, argv)
    print(f"\n[{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main(sys.argv[1:])
