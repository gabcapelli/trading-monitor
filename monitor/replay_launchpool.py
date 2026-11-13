"""
Estudo 87 (BNB depois do anuncio de Launchpool). PRE-REGISTRADO em 13/11/2026,
antes de olhar qualquer preco. Tentativa unica.

Hipotese: para "farmar" o token novo e preciso travar BNB; o anuncio cria
demanda de compra de BNB ate o farming comecar. Fluxo forcado, comprador.

EVENTOS
- Avisos "Introducing ... Launchpool" do feed da Binance ja em cache
  (cat48.json); corpo do aviso em cache_anuncios/launchpool_corpos.json.
- Inicio do farming = data/hora depois de "farming starting from" no corpo.
  Aviso sem essa frase (os Megadrop, que nao tem farming) fica de fora.
- Avisos publicados no mesmo minuto contam como um evento so.
- Fora: evento com menos de 60 min entre a entrada e o inicio do farming.

OPERACAO (BNBUSDT perpetuo, comprado, sem stop)
- Entrada: abertura do minuto floor(aviso) + 60 (pior caso do workflow horario).
- Saida: abertura do minuto do inicio do farming.
- `liq` (decide) = bruto - 0.5% - funding real (mesmo custo dos estudos de
  evento 38/39/85/86, conservador para o BNB).
- `excesso` (decide) = bruto - a mesma operacao no BTCUSDT nos mesmos minutos.
- Bootstrap por evento, IC95, 5000 reamostragens.
- CRITERIO: PASSA se `liq` E `excesso` tiverem IC95 inteiro acima de zero. Com
  menos de 15 eventos: SEM AMOSTRA.
- DESCRITIVOS (nao decidem): entrada com 2 min; movimento entre o aviso e a
  entrada; placebo 30 dias antes (mesma janela); liquido com custo de 0.18%;
  saida 24h depois do aviso; saida no fim do farming ("Farming Period ... to");
  so 2024-26.

Uso (de dentro de monitor/):
    python replay_launchpool.py --contar
    python replay_launchpool.py
"""

import html
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
from replay_deslistagem import DIA

MIN = 60_000
ARQ_CORPOS = os.path.join(D.DIR_ANUNCIOS, "launchpool_corpos.json")
URL = "https://www.binance.com/bapi/composite/v1/public/cms/article/detail/query?articleCode="
SYM = "BNBUSDT"
CUSTO, CUSTO_BAIXO = 0.5, 0.18
ENTRADA_MIN = 60
PLACEBO_DIAS = 30
MIN_EVENTOS = 15
DATA = r"(\d{4})[-/](\d{2})[-/](\d{2})\s+(\d{1,2}):(\d{2})\s*(AM|PM)?"


def avisos():
    with open(os.path.join(D.DIR_ANUNCIOS, "cat48.json")) as f:
        arts = json.load(f)
    return sorted((a for a in arts if re.match(r"Introducing .*(Launchpool|Megadrop)", a["title"])),
                  key=lambda a: a["releaseDate"])


def _texto(no):
    """Texto puro do corpo (JSON de nos do CMS da Binance ou HTML)."""
    if isinstance(no, str):
        try:
            no = json.loads(no)
        except ValueError:
            return html.unescape(re.sub(r"<[^>]+>", " ", no))
    if isinstance(no, dict):
        partes = [no.get("text", "")] if no.get("node") == "text" else []
        partes += [_texto(c) for c in no.get("child", [])]
        if no.get("tag") in ("p", "li", "h1", "h2", "h3", "div", "tr", "br"):
            partes.append("\n")
        return "".join(partes)
    if isinstance(no, list):
        return "".join(_texto(c) for c in no)
    return ""


def corpos():
    cache = {}
    if os.path.exists(ARQ_CORPOS):
        with open(ARQ_CORPOS, encoding="utf-8") as f:
            cache = json.load(f)
    for a in avisos():
        if a["code"] in cache:
            continue
        for tentativa in range(8):
            try:
                req = urllib.request.Request(URL + a["code"], headers={"User-Agent": "Mozilla/5.0"})
                raw = urllib.request.urlopen(req, timeout=30).read()
                break
            except urllib.error.HTTPError as e:
                if e.code != 429 or tentativa == 7:
                    raise
                time.sleep(30 * (tentativa + 1))
        cache[a["code"]] = html.unescape(_texto((json.loads(raw)["data"] or {}).get("body") or ""))
        with open(ARQ_CORPOS, "w", encoding="utf-8") as f:
            json.dump(cache, f, ensure_ascii=False)
        time.sleep(2)
    return cache


def _ms(m):
    a, mes, d, h, mi, ampm = m.groups()
    h = int(h)
    if ampm == "PM" and h < 12:
        h += 12
    return int(datetime(int(a), int(mes), int(d), h % 24, int(mi), tzinfo=timezone.utc).timestamp() * 1000)


def eventos():
    c, out, motivos, vistos = corpos(), [], defaultdict(int), set()
    for a in avisos():
        t = c[a["code"]]
        m = re.search(r"farming start\w* from\s+" + DATA, t)
        if not m:
            motivos["sem inicio de farming (Megadrop)"] += 1
            continue
        b = a["releaseDate"] // MIN * MIN
        if b in vistos:
            motivos["mesmo minuto de outro aviso"] += 1
            continue
        ini = _ms(m)
        if ini - (b + ENTRADA_MIN * MIN) < 60 * MIN:
            motivos["menos de 60 min ate o farming"] += 1
            continue
        vistos.add(b)
        f = re.search(r"Farming Period:[^\n]*", t)
        datas = list(re.finditer(DATA, f.group(0))) if f else []
        fim = _ms(datas[1]) + MIN if len(datas) >= 2 else None
        out.append({"ts": b, "ini": ini, "fim": fim, "titulo": a["title"]})
    return out, motivos


def _ret(s, a, b):
    pa, pb = s.get(a), s.get(b)
    return None if not pa or not pb else 100 * (pb / pa - 1)


def montar(e):
    t = dict(e)
    for nome, desloc in (("", 0), ("placebo_", -PLACEBO_DIAS * DIA)):
        b, ini = e["ts"] + desloc, e["ini"] + desloc
        ate = max(ini, b + 24 * 60 * MIN) if nome == "" else ini
        s = RL.serie_1m(SYM, b - MIN, ate + MIN)
        bt = RL.serie_1m("BTCUSDT", b - MIN, ate + MIN)
        ent = b + ENTRADA_MIN * MIN
        bruto, btc = _ret(s, ent, ini), _ret(bt, ent, ini)
        if bruto is None or btc is None:
            if nome == "":
                return None, "sem candle de 1m"
            continue
        t[nome + "bruto"], t[nome + "excesso"] = bruto, bruto - btc
        if nome == "placebo_":
            continue
        f = 100 * D.funding(SYM, ent, ini)
        t["liq"], t["liq_018"] = bruto - CUSTO - f, bruto - CUSTO_BAIXO - f
        t["horas"] = (ini - ent) / 3_600_000
        t["perdido"] = _ret(s, b, ent)
        b2, bt2 = _ret(s, b + 2 * MIN, ini), _ret(bt, b + 2 * MIN, ini)
        if b2 is not None and bt2 is not None:
            t["liq_2min"] = b2 - CUSTO - 100 * D.funding(SYM, b + 2 * MIN, ini)
            t["excesso_2min"] = b2 - bt2
        for chave, saida in (("excesso_24h", b + 24 * 60 * MIN), ("excesso_fim", e["fim"])):
            if saida and saida > ent:
                sx = {ent: s.get(ent), **RL.serie_1m(SYM, saida, saida)}
                sy = {ent: bt.get(ent), **RL.serie_1m("BTCUSDT", saida, saida)}
                x, y = _ret(sx, ent, saida), _ret(sy, ent, saida)
                if x is not None and y is not None:
                    t[chave] = x - y
    return t, "ok"


def main(argv):
    t0 = time.time()
    evs, mot = eventos()
    print("ESTUDO 87 BNB DEPOIS DO ANUNCIO DE LAUNCHPOOL")
    print(f"Eventos: {len(evs)} | fora: {dict(mot)}")
    por_ano = defaultdict(int)
    for e in evs:
        por_ano[datetime.fromtimestamp(e["ts"] / 1000, timezone.utc).year] += 1
    print("Por ano:", dict(sorted(por_ano.items())))
    horas = sorted((e["ini"] - e["ts"]) / 3_600_000 - 1 for e in evs)
    print(f"Horas entre a entrada e o farming: mediana {horas[len(horas) // 2]:.1f}, min {horas[0]:.1f}, max {horas[-1]:.1f}")
    if "--contar" in argv:
        return
    trades, motivos = [], defaultdict(int)
    for e in evs:
        t, m = montar(e)
        motivos[m] += 1
        if t:
            trades.append(t)
    print("Montagem:", dict(motivos))
    print(f"\nCOMPRADO em {SYM}, entrada +{ENTRADA_MIN} min, saida no inicio do farming (positivo = ganhou)")
    lo = {}
    for chave, rot in (("liq", "LIQUIDO, custo 0.5% + funding (decide)"), ("excesso", "EXCESSO sobre o BTC (decide)"),
                       ("bruto", "bruto"), ("liq_018", "liquido, custo 0.18% + funding"),
                       ("liq_2min", "liquido, entrada +2 min"), ("excesso_2min", "excesso, entrada +2 min"),
                       ("perdido", "movimento entre o aviso e a entrada"),
                       ("placebo_excesso", "PLACEBO -30d: excesso"), ("placebo_bruto", "PLACEBO -30d: bruto"),
                       ("excesso_24h", "excesso, saida 24h depois do aviso"),
                       ("excesso_fim", "excesso, saida no fim do farming")):
        r = RL.boot([t for t in trades if t.get(chave) is not None], chave)
        print(f"  {rot:<42} {RL.fmt(r)}")
        if r:
            lo[chave] = r[1]
    rec = [t for t in trades if t["ts"] >= 1704067200000]
    print(f"  {'excesso, so 2024-26':<42} {RL.fmt(RL.boot(rec, 'excesso'))}")
    print(f"  {'liquido, so 2024-26':<42} {RL.fmt(RL.boot(rec, 'liq'))}")
    print(f"  liquido positivo em {sum(t['liq'] > 0 for t in trades)}/{len(trades)}")
    if len(trades) < MIN_EVENTOS:
        dec = f"SEM AMOSTRA PARA DECIDIR ({len(trades)} < {MIN_EVENTOS} eventos)"
    else:
        dec = "PASSA" if lo.get("liq", -1) > 0 and lo.get("excesso", -1) > 0 else "NAO PASSA"
    print(f"\n  DECISAO ESTUDO 87: {dec}")
    print(f"\n[{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main(sys.argv[1:])
