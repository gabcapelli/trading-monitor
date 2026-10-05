"""
Registro em papel -- vender o perpetuo nas 24h apos a Monitoring Tag da Binance.
REGRA CONGELADA em 05/10/2026 (estudo 38 de claude/estudos-avulsos.md). Nenhuma
ordem e enviada.

ORIGEM
------
Estudo 37: vender por 7-14 dias apos a tag nao passa (squeezes). Estudo 38
(descritivo, candles de 1 min): o efeito esta nas primeiras 24h -- vendido do
anuncio ate +24h rende +5.2% [+2.1, +8.1] entrando com 2 min e +3.4% [+1.8,
+5.2] entrando com 60 min (custo 0.5%, sem beta). Eventos ja usados, 24
anuncios, IC otimista: so o teste adiante decide.

REGRA (braco PRINCIPAL, decide)
-------------------------------
- A cada execucao do workflow horario, le a 1a pagina dos catalogos 49 e 161 do
  feed de anuncios da Binance (direto ou pelo proxy, rota /cms).
- Evento: titulo "Binance Will Extend the Monitoring Tag to (Include) A, B & C
  ... on AAAA-MM-DD"; cada token e um trade. Fora: AEUR, VAI (stablecoins) e
  token que ja teve trade neste registro.
- Operavel: perpetuo USDT-M TKRUSDT ou 1000TKRUSDT, status TRADING, cripto
  (underlyingType COIN) e listado ha >= 30 dias na data do anuncio.
- Entrada: VENDE na abertura do minuto em que o script detecta o anuncio
  (latencia de 5-65 min no workflow horario; o estudo cobriu ate 60).
  Anuncio detectado mais de 90 min depois de publicado: descartado.
- Saida: recompra na abertura do minuto floor(anuncio) + 24h.
- Sem stop.

BRACO EXPLORATORIO (nao decide)
-------------------------------
Deslistagem do spot ("Binance Will Delist A, B on AAAA-MM-DD", catalogo 161,
sem stablecoins/wrapped): mesma mecanica, saida em floor(anuncio) + 4h. No
estudo 38 ficou positivo de +5 a +60 min, mas fora da regra pre-registrada.

MEDIDAS (% do nocional, positivo = vendido ganhou)
--------------------------------------------------
- `bruto` = -(saida/entrada - 1).
- `liq` = bruto - 0.5% de custo + funding recebido pelo vendido no periodo.
- `excesso` = bruto - retorno de vender o BTCUSDT nos mesmos minutos.

LEITURA
-------
So reavaliar com 24 ANUNCIOS NOVOS do braco principal com trade fechado (~2
anos no ritmo mensal). Antes disso e ruido. Criterio na leitura: media de
`liq` e de `excesso` com IC95 > 0, bootstrap por anuncio.

Rode sem argumento (o workflow chama assim). Teste: `--simular <id do anuncio>
<minutos de latencia>` reprocessa um anuncio antigo numa pasta temporaria
(MONITORING_PAPER_DIR), com precos reais.
"""

import json
import os
import re
import sys
import time
from datetime import datetime, timedelta, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import unlock_paper as U

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_TESTE = os.environ.get("MONITORING_PAPER_DIR")
LEDGER = os.path.join(_TESTE or os.path.join(RAIZ, "claude"), "monitoring-paper.md")
ESTADO = os.path.join(_TESTE or os.path.join(RAIZ, "monitor"), "monitoring_paper_state.json")

MIN = 60_000
H_SAIDA = {"principal": 24 * 60, "deslistagem": 4 * 60}
MAX_ATRASO = 90 * MIN
MIN_LISTADO = 30 * 86_400_000
CUSTO = 0.5
META = 24
EXCLUIR = {"AEUR", "VAI", "USDS", "SUSD", "RENBTC", "IDRT", "USDP"}
CMS = "https://www.binance.com/bapi/composite/v1/public/cms/article/list/query?type=1&catalogId={}&pageNo=1&pageSize=20"
RE_TAG = re.compile(r"Extend the Monitoring Tag to (?:Include )?(.+?)(?:,? (?:and )?Remove .*)? on \d{4}-\d{2}-\d{2}\s*$")
RE_DELIST = re.compile(r"^Binance (?:Will )?Delist (.+?) on \d{4}[-/]\d{2}[-/]\d{2}\s*$")
BRT = timezone(timedelta(hours=-3))


# ---------------------------------------------------------------------------
# Fontes
# ---------------------------------------------------------------------------

def anuncios():
    """Lista de {id, title, releaseDate} dos catalogos 49 e 161, ou None se o feed falhar."""
    out = []
    proxy = U.FAPI.replace("/fapi/v1", "/cms") if "/fapi/v1" in U.FAPI and "fapi.binance.com" not in U.FAPI else None
    for cat in (49, 161):
        d = U._json(CMS.format(cat))
        if not d and proxy:
            d = U._json(f"{proxy}?catalogId={cat}&pageNo=1&pageSize=20")
        try:
            out += [{"id": a["id"], "title": a["title"].strip(), "releaseDate": a["releaseDate"]}
                    for c in d["data"]["catalogs"] for a in c["articles"]]
        except (TypeError, KeyError):
            return None
    return out


def tokens(titulo, padrao):
    m = padrao.search(titulo)
    if not m:
        return []
    out = []
    for tk in re.split(r",|&| and ", m.group(1)):
        tk = re.sub(r".*\((\w+)\)", r"\1", tk.strip())
        if re.fullmatch(r"[A-Z0-9]{1,12}", tk) and tk not in EXCLUIR:
            out.append(tk)
    return out


def info_perps():
    d = U._json(f"{U.FAPI}/exchangeInfo")
    if not d or not d.get("symbols"):
        return None
    return {s["symbol"]: s for s in d["symbols"]}


def abertura_1m(sym, ts):
    k = U._json(f"{U.FAPI}/klines?symbol={sym}&interval=1m&startTime={ts}&limit=1")
    return float(k[0][1]) if k and int(k[0][0]) == ts else None


def funding_recebido(sym, t0, t1):
    """Soma (em %) das taxas pagas em [t0, t1); positivo = o vendido recebeu."""
    r = U._json(f"{U.FAPI}/fundingRate?symbol={sym}&startTime={t0}&endTime={t1 - 1}&limit=1000")
    if r is None:
        return None
    return 100 * sum(float(x["fundingRate"]) for x in r if t0 <= int(x["fundingTime"]) < t1)


# ---------------------------------------------------------------------------
# Regra
# ---------------------------------------------------------------------------

def operavel(tk, release, perps):
    for sym in (f"{tk}USDT", f"1000{tk}USDT"):
        s = perps.get(sym)
        if not s:
            continue
        if s.get("status") != "TRADING":
            return None, "perpetuo nao negociando"
        if s.get("underlyingType", "COIN") != "COIN":
            return None, f"nao-cripto ({s.get('underlyingType')})"
        if s.get("onboardDate", 0) > release - MIN_LISTADO:
            return None, "listado ha menos de 30 dias"
        return sym, None
    return None, "sem perpetuo"


def abre_trades(estado, art, braco, tks, agora, perps):
    """True se o anuncio foi resolvido (abriu ou descartou); False = tentar de novo."""
    release = art["releaseDate"]
    ent = agora // MIN * MIN
    ja = {t["token"] for t in estado["trades"].values() if t["braco"] == braco}
    novos = []
    for tk in tks:
        chave = f"{braco}|{tk}|{art['id']}"
        base = {"braco": braco, "token": tk, "anuncio_id": art["id"], "titulo": art["title"],
                "release": release, "detectado": ent}
        if tk in ja:
            estado["trades"][chave] = {**base, "status": "descartado", "motivo": "token ja registrado antes"}
            continue
        if ent - release > MAX_ATRASO:
            estado["trades"][chave] = {**base, "status": "descartado",
                                       "motivo": f"detectado {round((ent - release) / MIN)} min depois"}
            continue
        sym, motivo = operavel(tk, release, perps)
        if not sym:
            estado["trades"][chave] = {**base, "status": "descartado", "motivo": motivo}
            continue
        p_in, b_in = abertura_1m(sym, ent), abertura_1m("BTCUSDT", ent)
        if p_in is None or b_in is None:
            return False          # API instavel agora: tenta de novo na proxima execucao (ate 90 min)
        novos.append((chave, {**base, "status": "aberto", "sym": sym, "entrada_ts": ent, "p_in": p_in,
                              "btc_in": b_in, "latencia_min": round((ent - release) / MIN),
                              "saida_ts": release // MIN * MIN + H_SAIDA[braco] * MIN}))
    for chave, t in novos:
        estado["trades"][chave] = t
    return True


def fecha_trades(estado, agora):
    fechados = []
    for t in estado["trades"].values():
        if t["status"] != "aberto" or agora < t["saida_ts"] + 2 * MIN:
            continue
        p_out, b_out = abertura_1m(t["sym"], t["saida_ts"]), abertura_1m("BTCUSDT", t["saida_ts"])
        f = funding_recebido(t["sym"], t["entrada_ts"], t["saida_ts"])
        if p_out is None or b_out is None or f is None:
            if agora - t["saida_ts"] > 3 * 86_400_000:
                t.update({"status": "descartado", "motivo": "sem preco de saida em 3 dias"})
            continue
        bruto = -100 * (p_out / t["p_in"] - 1)
        t.update({"status": "fechado", "p_out": p_out, "btc_out": b_out, "funding": f, "bruto": bruto,
                  "liq": bruto - CUSTO + f, "excesso": bruto + 100 * (b_out / t["btc_in"] - 1)})
        fechados.append(t)
    return fechados


def processa(estado, agora, arts):
    if not estado.get("iniciado"):
        # 1a execucao: o que ja esta no feed e passado, nao vira trade
        estado.update({"iniciado": agora, "vistos": sorted({a["id"] for a in arts}), "trades": {}})
        return [], []
    vistos = set(estado["vistos"])
    pendentes = [a for a in arts if a["id"] not in vistos]
    perps = info_perps() if pendentes else {}
    abertos = []
    for a in sorted(pendentes, key=lambda a: a["releaseDate"]):
        for braco, padrao in (("principal", RE_TAG), ("deslistagem", RE_DELIST)):
            tks = tokens(a["title"], padrao)
            if not tks:
                continue
            if perps is None:
                if agora - a["releaseDate"] <= MAX_ATRASO:
                    break                     # exchangeInfo fora: tenta de novo na proxima execucao
                tks = []                      # passou do prazo: resolve como descartado abaixo
            antes = set(estado["trades"])
            if perps is not None and not abre_trades(estado, a, braco, tks, agora, perps):
                break
            abertos += [estado["trades"][k] for k in set(estado["trades"]) - antes
                        if estado["trades"][k]["status"] == "aberto"]
        else:
            vistos.add(a["id"])
    estado["vistos"] = sorted(vistos)
    return abertos, fecha_trades(estado, agora)


# ---------------------------------------------------------------------------
# Registro
# ---------------------------------------------------------------------------

def _h(ts):
    return datetime.fromtimestamp(ts / 1000, BRT).strftime("%d/%m/%Y %H:%M")


def _media(xs):
    return sum(xs) / len(xs) if xs else None


def escreve_ledger(estado, agora):
    tr = list(estado.get("trades", {}).values())
    L = ["# Registro em papel — venda nas 24h após a Monitoring Tag", "",
         "> Gerado por `monitor/monitoring_paper.py`. **Nenhuma ordem é enviada.**",
         "> Regra congelada em 05/10/2026 (estudo 38): vender o perpétuo no minuto em que o anúncio",
         "> é detectado (5–65 min depois) e recomprar 24h após o anúncio. Custo 0.5% e funding real;",
         "> excesso sobre vender o BTC nos mesmos minutos. **Só reavaliar com 24 anúncios fechados.**", "",
         f"_Atualizado em {_h(agora)} (Brasília)._", ""]
    for braco, titulo in (("principal", "Monitoring Tag (decide)"), ("deslistagem", "Deslistagem, saída em 4h (exploratório)")):
        fe = [t for t in tr if t["braco"] == braco and t["status"] == "fechado"]
        ab = [t for t in tr if t["braco"] == braco and t["status"] == "aberto"]
        n_an = len({t["anuncio_id"] for t in fe})
        L += [f"## {titulo}", ""]
        meta = f" de {META} ({100 * n_an // META}%)" if braco == "principal" else ""
        L.append(f"**Anúncios fechados:** {n_an}{meta} · trades fechados: {len(fe)}")
        if fe:
            L.append(f"\n**Média por trade:** líquido {_media([t['liq'] for t in fe]):+.2f}% · "
                     f"excesso {_media([t['excesso'] for t in fe]):+.2f}% · "
                     f"líquido positivo em {sum(t['liq'] > 0 for t in fe)}/{len(fe)}")
        if braco == "principal":
            L.append("\n_Referência do estudo 38 (entrando com 60 min): +3.4% líquido._")
        L.append("")
        if ab:
            L += ["| Token | Anúncio | Venda | Preço | Recompra |", "|---|---|---|---|---|"]
            L += [f"| {t['sym']} | {_h(t['release'])} | +{t['latencia_min']} min | {t['p_in']:g} | {_h(t['saida_ts'])} |"
                  for t in sorted(ab, key=lambda t: t["saida_ts"])]
            L.append("")
        if fe:
            L += ["| Token | Anúncio | Latência | Bruto | Funding | Líquido | Excesso |", "|---|---|---|---|---|---|---|"]
            L += [f"| {t['sym']} | {_h(t['release'])} | {t['latencia_min']} min | {t['bruto']:+.2f}% | "
                  f"{t['funding']:+.3f}% | {t['liq']:+.2f}% | {t['excesso']:+.2f}% |"
                  for t in sorted(fe, key=lambda t: t["release"], reverse=True)]
            L.append("")
    desc = [t for t in tr if t["status"] == "descartado"]
    if desc:
        L += [f"<details><summary>Descartados ({len(desc)})</summary>", ""]
        L += [f"- {t['token']} ({t['braco']}, {_h(t['release'])}): {t['motivo']}"
              for t in sorted(desc, key=lambda t: t["release"], reverse=True)]
        L += ["", "</details>", ""]
    if not tr:
        L += ["_Nenhum anúncio novo desde o início do registro "
              f"({_h(estado['iniciado']) if estado.get('iniciado') else '—'})._", ""]
    with open(LEDGER, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L))


def notifica(abertos, fechados):
    linhas = [f"Vende {t['sym']} ({t['braco']}) a {t['p_in']:g}, +{t['latencia_min']} min" for t in abertos]
    linhas += [f"Fecha {t['sym']} ({t['braco']}): liq {t['liq']:+.2f}%, exc {t['excesso']:+.2f}%" for t in fechados]
    if linhas:
        import fetch_and_check as M
        M.send_ntfy("Monitoring Tag (papel)", "\n".join(linhas))


def carrega():
    if os.path.exists(ESTADO):
        with open(ESTADO, encoding="utf-8") as f:
            return json.load(f)
    return {}


def salva(estado):
    with open(ESTADO, "w", encoding="utf-8", newline="\n") as f:
        json.dump(estado, f, indent=1, ensure_ascii=False)


def main(argv):
    agora = int(time.time() * 1000)
    estado = carrega()
    if "--simular" in argv:
        # teste: anuncio antigo `id`, como se fosse detectado `lat` minutos depois, e fechado em seguida
        i = argv.index("--simular")
        alvo, lat = int(argv[i + 1]), int(argv[i + 2])
        arts = anuncios() or []
        for nome in ("monitoring.json", "cat161.json"):   # anuncios antigos, fora da 1a pagina
            fp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache_anuncios", nome)
            if os.path.exists(fp):
                arts += json.load(open(fp, encoding="utf-8"))
        a = next(x for x in arts if x["id"] == alvo)
        a = {"id": a["id"], "title": a["title"].strip(), "releaseDate": a["releaseDate"]}
        estado = {"iniciado": 1, "vistos": [], "trades": {}}
        abertos, _ = processa(estado, a["releaseDate"] + lat * MIN, [a])
        fechados = fecha_trades(estado, agora)
    else:
        arts = anuncios()
        if arts is None:
            print("[monitoring_paper] feed de anuncios inacessivel; nada processado")
            escreve_ledger(estado, agora)
            return
        abertos, fechados = processa(estado, agora, arts)
        notifica(abertos, fechados)
    salva(estado)
    escreve_ledger(estado, agora)
    print(f"[monitoring_paper] abertos agora: {len(abertos)} · fechados agora: {len(fechados)} · "
          f"total de trades: {len(estado.get('trades', {}))}")


if __name__ == "__main__":
    main(sys.argv[1:])
