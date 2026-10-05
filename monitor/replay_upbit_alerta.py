"""
Estudo 39 -- replica da regra do estudo 38 (Monitoring Tag, vendido 24h) num
conjunto INDEPENDENTE de eventos: a designacao de "token de alerta" da Upbit
(유의 종목 지정). PRE-REGISTRADO em 05/10/2026, antes de olhar qualquer preco.

POR QUE
-------
O achado do 38 (+3.4% [+1.8, +5.2] entrando com 60 min) veio de eventos ja
usados, com 24 anuncios e IC bootstrap otimista. A designacao da Upbit e o
mesmo mecanismo (corretora grande marca o token como candidato a deslistagem),
em outro mercado, com outros eventos. Nao ha nada a ajustar: a regra e a do
teste de papel, aplicada como esta.

Leitura combinada, fixada antes:
- passa aqui: o achado do 38 ganha confirmacao independente (o papel segue
  sendo a prova final);
- nao passa: sinal forte de que o 38 foi sorte. Nao mata sozinho (publico e
  regras da Upbit diferem), mas nao se monta nada alem do papel ja rodando.

EVENTOS
-------
- Feed publico da Upbit (api-manager.upbit.com/api/v1/announcements,
  category=trade), cache em cache_anuncios/upbit_trade.json.
- Evento = cada "(TKR)" num titulo com "유의 종목 지정" (designacao), sem
  "해제" (liberacao) nem "연장" (prorrogacao). O "유의 촉구 안내" (apelo a
  cautela, mais brando) fica de fora.
- Horario: `listed_at` (com fuso, KST).
- Fora: token com anuncio da Binance (Monitoring Tag ou deslistagem) entre 2
  dias antes e 1 dia depois -- nao seria evento independente.

REGRA (a do teste de papel monitoring_paper.py, com latencia de 60 min)
-----------------------------------------------------------------------
- Vendido no perpetuo USDT-M da Binance (TKRUSDT ou 1000TKRUSDT), com candle
  de 1h com volume na entrada e 30 dias antes.
- Entrada: abertura do minuto floor(anuncio) + 60 (o pior caso do workflow).
- Saida: abertura do minuto floor(anuncio) + 24h.

MEDIDAS (% do nocional, positivo = vendido ganhou)
--------------------------------------------------
- `liq` (decide) = bruto - 0.5% + funding recebido.
- `excesso` (decide) = bruto - retorno de vender o BTCUSDT nos mesmos minutos.
- Bootstrap por ANUNCIO, IC95, 5000 reamostragens.

CRITERIO
--------
PASSA se `liq` E `excesso` tiverem IC95 inteiro acima de zero. Uma so
hipotese, sem Bonferroni. Com menos de 15 anuncios com trade: SEM AMOSTRA.
Lembrete do estudo 37: com ~20 grupos e caudas pesadas o IC cobre menos que
o nominal; um PASSA no limite e fraco.

DESCRITIVOS
-----------
- Entrada com 2 min de latencia.
- PLACEBO: mesmo token, mesmos minutos, 30 dias antes ("token fraco" x anuncio).
- Total perdido: anuncio -> entrada.
- So 2025-26 (o grosso dos eventos).

Uso (de dentro de monitor/):
    python replay_upbit_alerta.py --contar
    python replay_upbit_alerta.py
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
ARQ = os.path.join(D.DIR_ANUNCIOS, "upbit_trade.json")
EXCLUIDOS = {"USDT", "USDC", "DAI", "TUSD", "USDP"}
CUSTO = 0.5
ENTRADA_MIN = 60
SAIDA_MIN = 24 * 60
PLACEBO_DIAS = 30
MIN_ANUNCIOS = 15


def baixar():
    out, p = [], 1
    while True:
        u = f"https://api-manager.upbit.com/api/v1/announcements?os=web&page={p}&per_page=20&category=trade"
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
    with open(ARQ, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False)


def eventos():
    if not os.path.exists(ARQ):
        baixar()
    with open(ARQ, encoding="utf-8") as f:
        notas = json.load(f)
    binance = defaultdict(list)
    for e in MT.eventos() + D.eventos():
        binance[e["token"]].append(e["ts"])
    out, motivos = [], defaultdict(int)
    for n in notas:
        t = n["title"]
        if not re.search(r"유의 ?종목 ?지정", t) or "해제" in t or "연장" in t:
            continue
        ts = int(datetime.fromisoformat(n["listed_at"]).timestamp() * 1000)
        for tk in re.findall(r"\(([A-Z0-9]{1,12})\)", t):
            if tk in EXCLUIDOS:
                continue
            if any(ts - 2 * DIA <= b <= ts + DIA for b in binance.get(tk, [])):
                motivos["anuncio da Binance colado"] += 1
                continue
            out.append({"token": tk, "ts": ts, "titulo": t})
    return sorted(out, key=lambda e: e["ts"]), motivos


def montar(e):
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
            bruto = -100 * (p_out / p_in - 1)
            suf = "" if k == ENTRADA_MIN else "_2min"
            t[f"{nome}bruto{suf}"] = bruto
            t[f"{nome}excesso{suf}"] = bruto + 100 * (b_out / b_in - 1)
            if nome == "":
                f = 100 * D.funding(sym, b0 + k * MIN, b0 + SAIDA_MIN * MIN)
                t[f"liq{suf}"] = bruto - CUSTO + f
        if nome == "" and p0 is not None and s.get(b0 + ENTRADA_MIN * MIN):
            t["perdido"] = -100 * (s[b0 + ENTRADA_MIN * MIN] / p0 - 1)
    return t, "ok"


def main(argv):
    t0 = time.time()
    evs, mot = eventos()
    print(f"Eventos (token x designacao): {len(evs)} em {len({e['ts'] for e in evs})} anuncios | "
          f"fora por anuncio da Binance colado: {mot.get('anuncio da Binance colado', 0)}")
    trades, motivos = [], defaultdict(int)
    for e in evs:
        t, m = montar(e)
        motivos[m] += 1
        if t:
            trades.append(t)
    n_an = len({t["ts"] for t in trades})
    print("Montagem:", dict(motivos))
    print(f"Trades validos: {len(trades)} em {n_an} anuncios")
    if "--contar" in argv:
        por_ano = defaultdict(int)
        for t in trades:
            por_ano[datetime.fromtimestamp(t["ts"] / 1000, timezone.utc).year] += 1
        print("Por ano:", dict(sorted(por_ano.items())))
        for t in trades:
            print(f"    {datetime.fromtimestamp(t['ts']/1000, timezone.utc):%Y-%m-%d %H:%M} {t['sym']}")
        return

    print("\n" + "=" * 100 + f"\nVENDIDO, entrada +{ENTRADA_MIN} min, saida +{SAIDA_MIN // 60}h "
          "(positivo = vendido ganhou)\n" + "=" * 100)
    lo = {}
    for chave, rot in (("liq", "LIQUIDO, custo 0.5% + funding (decide)"), ("excesso", "EXCESSO sobre o BTC (decide)"),
                       ("bruto", "bruto"), ("liq_2min", "liquido, entrada +2 min"),
                       ("excesso_2min", "excesso, entrada +2 min"),
                       ("placebo_excesso", "PLACEBO -30d: excesso"), ("perdido", "perdido (anuncio -> entrada)")):
        r = RL.boot(trades, chave)
        print(f"  {rot:<42} {RL.fmt(r)}")
        if r:
            lo[chave] = r[1]
    recentes = [t for t in trades if t["ts"] >= 1735689600000]
    print(f"  {'excesso, so 2025-26':<42} {RL.fmt(RL.boot(recentes, 'excesso'))}")
    print("\n  Por trade:")
    for t in trades:
        print(f"    {datetime.fromtimestamp(t['ts']/1000, timezone.utc):%Y-%m-%d} {t['sym']:<14} "
              f"liq {t['liq']:+7.2f}% exc {t['excesso']:+7.2f}%")
    if n_an < MIN_ANUNCIOS:
        dec = f"SEM AMOSTRA PARA DECIDIR ({n_an} < {MIN_ANUNCIOS} anuncios)"
    else:
        dec = "PASSA" if lo.get("liq", -1) > 0 and lo.get("excesso", -1) > 0 else "NAO PASSA"
    print(f"\n  DECISAO: {dec}\n  [{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main(sys.argv[1:])
