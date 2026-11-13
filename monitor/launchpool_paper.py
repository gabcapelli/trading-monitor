"""
Registro em papel -- comprar BNB depois do anuncio de Launchpool da Binance.
REGRA CONGELADA em 13/11/2026 (estudo 87 de claude/estudos-avulsos.md). Nenhuma
ordem e enviada.

ORIGEM
------
Estudo 87 (pre-registrado, 63 anuncios de 2020 a 2026): comprado em BNBUSDT de
+60 min ate o inicio do farming rende +1.23% liquido, IC95 [+0.30, +2.22], e
+1.31% [+0.44, +2.25] de excesso sobre o BTC; placebo em zero. PASSA, com
fragilidade: 5 trades fazem 70% do total, o efeito esta nos eventos com mais de
24h de espera, em 2025-26 deu ~0 (n=9) e a Binance quase parou de fazer
Launchpool. So o teste adiante decide.

REGRA
-----
- A cada execucao do workflow horario, le a 1a pagina do catalogo 48 do feed de
  anuncios da Binance (direto ou pelo proxy, rota /cms).
- Evento: titulo "Introducing ... Launchpool ...". Um trade por anuncio; anuncio
  no mesmo minuto de outro ja registrado e descartado.
- Inicio do farming: data/hora depois de "farming starting from" no corpo do
  anuncio (direto ou pelo proxy, rota /cms com articleCode).
- Entrada: COMPRA BNBUSDT (perpetuo) na abertura do minuto em que o script
  detecta o anuncio e consegue ler o inicio do farming (latencia de 5-65 min no
  workflow horario; o estudo usou 60). Mais de 90 min depois da publicacao, ou
  menos de 60 min ate o farming: descartado.
- Saida: vende na abertura do minuto do inicio do farming. Sem stop.

MEDIDAS (% do nocional, positivo = comprado ganhou)
---------------------------------------------------
- `bruto` = saida/entrada - 1.
- `liq` = bruto - 0.5% de custo - funding pago pelo comprado no periodo.
- `excesso` = bruto - retorno de comprar o BTCUSDT nos mesmos minutos.

LEITURA
-------
So reavaliar com 20 ANUNCIOS NOVOS fechados. Criterio: media de `liq` e de
`excesso` com IC95 > 0, bootstrap por anuncio. No ritmo de 2025-26 (1 a 8 por
ano) isso leva anos; se a Binance encerrar o Launchpool, o registro fica parado.

Rode sem argumento (o workflow chama assim). Teste: `--simular <code do anuncio>
<minutos de latencia>` reprocessa um anuncio antigo numa pasta temporaria
(LAUNCHPOOL_PAPER_DIR), com precos reais.
"""

import html
import json
import os
import re
import sys
import time
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import monitoring_paper as MP
import unlock_paper as U

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_TESTE = os.environ.get("LAUNCHPOOL_PAPER_DIR")
LEDGER = os.path.join(_TESTE or os.path.join(RAIZ, "claude"), "launchpool-paper.md")
ESTADO = os.path.join(_TESTE or os.path.join(RAIZ, "monitor"), "launchpool_paper_state.json")

MIN = 60_000
SYM = "BNBUSDT"
MAX_ATRASO = 90 * MIN
MIN_ESPERA = 60 * MIN
CUSTO = 0.5
META = 20
CAT = 48
LISTA = "https://www.binance.com/bapi/composite/v1/public/cms/article/list/query?type=1&catalogId={}&pageNo=1&pageSize=20"
DETALHE = "https://www.binance.com/bapi/composite/v1/public/cms/article/detail/query?articleCode={}"
RE_TITULO = re.compile(r"^Introducing .*Launchpool")
DATA = r"(\d{4})[-/](\d{2})[-/](\d{2})\s+(\d{1,2}):(\d{2})\s*(AM|PM)?"
RE_FARMING = re.compile(r"farming start\w* from\s+" + DATA)


# ---------------------------------------------------------------------------
# Fontes
# ---------------------------------------------------------------------------

def _proxy_cms():
    return U.FAPI.replace("/fapi/v1", "/cms") if "/fapi/v1" in U.FAPI and "fapi.binance.com" not in U.FAPI else None


def anuncios():
    """Lista de {id, code, title, releaseDate} do catalogo 48, ou None se o feed falhar."""
    d = U._json(LISTA.format(CAT))
    if not d and _proxy_cms():
        d = U._json(f"{_proxy_cms()}?catalogId={CAT}&pageNo=1&pageSize=20")
    try:
        return [{"id": a["id"], "code": a["code"], "title": a["title"].strip(), "releaseDate": a["releaseDate"]}
                for c in d["data"]["catalogs"] for a in c["articles"]]
    except (TypeError, KeyError):
        return None


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


def corpo(code):
    """(texto do anuncio, fonte) ou (None, 'falhou')."""
    fontes = [("direto", DETALHE.format(code))]
    if _proxy_cms():
        fontes.append(("proxy", f"{_proxy_cms()}?articleCode={code}"))
    for nome, url in fontes:
        try:
            d = U._json(url)
            bruto = ((d or {}).get("data") or {}).get("body")
        except Exception:
            bruto = None
        if bruto:
            return html.unescape(_texto(bruto)), nome
    return None, "falhou"


def inicio_farming(texto):
    m = RE_FARMING.search(texto or "")
    if not m:
        return None
    a, mes, d, h, mi, ampm = m.groups()
    h = int(h)
    if ampm == "PM" and h < 12:
        h += 12
    return int(datetime(int(a), int(mes), int(d), h % 24, int(mi), tzinfo=timezone.utc).timestamp() * 1000)


def funding_pago(t0, t1):
    f = MP.funding_recebido(SYM, t0, t1)      # % somado em [t0, t1); positivo = comprado pagou
    return f


# ---------------------------------------------------------------------------
# Regra
# ---------------------------------------------------------------------------

def abre(estado, a, agora):
    """True se o anuncio foi resolvido (abriu ou descartou); False = tentar de novo."""
    release, ent = a["releaseDate"], agora // MIN * MIN
    base = {"anuncio_id": a["id"], "code": a["code"], "titulo": a["title"], "release": release,
            "detectado": ent, "lado": 1, "sym": SYM}
    chave = str(a["id"])

    def descarta(motivo):
        estado["trades"][chave] = {**base, "status": "descartado", "motivo": motivo}
        return True

    if any(t["release"] // MIN == release // MIN for t in estado["trades"].values()):
        return descarta("mesmo minuto de outro anuncio")
    if ent - release > MAX_ATRASO:
        return descarta(f"detectado {round((ent - release) / MIN)} min depois (ou sem inicio do farming a tempo)")
    texto, fonte = corpo(a["code"])
    if texto is None:
        return False                          # corpo inacessivel agora: tenta de novo (ate 90 min)
    ini = inicio_farming(texto)
    if ini is None:
        return descarta("anuncio sem inicio de farming")
    if ini - ent < MIN_ESPERA:
        return descarta("menos de 60 min ate o farming")
    p_in, b_in = MP.abertura_1m(SYM, ent), MP.abertura_1m("BTCUSDT", ent)
    if p_in is None or b_in is None:
        return False                          # API instavel agora: tenta de novo na proxima execucao
    estado["trades"][chave] = {**base, "status": "aberto", "entrada_ts": ent, "p_in": p_in, "btc_in": b_in,
                               "latencia_min": round((ent - release) / MIN), "saida_ts": ini, "fonte_corpo": fonte}
    return True


def fecha(estado, agora):
    fechados = []
    for t in estado["trades"].values():
        if t["status"] != "aberto" or agora < t["saida_ts"] + 2 * MIN:
            continue
        p_out, b_out = MP.abertura_1m(SYM, t["saida_ts"]), MP.abertura_1m("BTCUSDT", t["saida_ts"])
        f = funding_pago(t["entrada_ts"], t["saida_ts"])
        if p_out is None or b_out is None or f is None:
            if agora - t["saida_ts"] > 3 * 86_400_000:
                t.update({"status": "descartado", "motivo": "sem preco de saida em 3 dias"})
            continue
        bruto = 100 * (p_out / t["p_in"] - 1)
        t.update({"status": "fechado", "p_out": p_out, "btc_out": b_out, "funding": f, "bruto": bruto,
                  "liq": bruto - CUSTO - f, "excesso": bruto - 100 * (b_out / t["btc_in"] - 1)})
        fechados.append(t)
    return fechados


def processa(estado, agora, arts):
    if not estado.get("iniciado"):
        # 1a execucao: o que ja esta no feed e passado, nao vira trade. Aproveita para
        # registrar se o corpo de um anuncio e legivel daqui (direto, proxy ou falhou).
        estado.update({"iniciado": agora, "vistos": sorted({a["id"] for a in arts}), "trades": {},
                       "teste_corpo": corpo(arts[0]["code"])[1] if arts else "sem anuncio"})
        return [], []
    vistos = set(estado["vistos"])
    abertos = []
    for a in sorted((a for a in arts if a["id"] not in vistos), key=lambda a: a["releaseDate"]):
        if not RE_TITULO.search(a["title"]):
            vistos.add(a["id"])
            continue
        if abre(estado, a, agora):
            vistos.add(a["id"])
            t = estado["trades"][str(a["id"])]
            if t["status"] == "aberto":
                abertos.append(t)
    estado["vistos"] = sorted(vistos)
    return abertos, fecha(estado, agora)


# ---------------------------------------------------------------------------
# Registro
# ---------------------------------------------------------------------------

def escreve_ledger(estado, agora):
    tr = list(estado.get("trades", {}).values())
    fe = [t for t in tr if t["status"] == "fechado"]
    ab = [t for t in tr if t["status"] == "aberto"]
    L = ["# Registro em papel — BNB depois do anúncio de Launchpool", "",
         "> Gerado por `monitor/launchpool_paper.py`. **Nenhuma ordem é enviada.**",
         "> Regra congelada em 13/11/2026 (estudo 87): comprar BNBUSDT no minuto em que o anúncio é",
         "> detectado (5–65 min depois) e vender quando o farming começa. Custo 0.5% e funding real;",
         f"> excesso sobre comprar o BTC nos mesmos minutos. **Só reavaliar com {META} anúncios fechados.**", "",
         f"_Atualizado em {MP._h(agora)} (Brasília)._", "",
         f"**Anúncios fechados:** {len(fe)} de {META} ({100 * len(fe) // META}%)"]
    if fe:
        L.append(f"\n**Média por trade:** líquido {MP._media([t['liq'] for t in fe]):+.2f}% · "
                 f"excesso {MP._media([t['excesso'] for t in fe]):+.2f}% · "
                 f"líquido positivo em {sum(t['liq'] > 0 for t in fe)}/{len(fe)}")
    L += ["\n_Referência do estudo 87: +1.23% líquido, +1.31% de excesso; em 2025–26, perto de zero._", ""]
    if ab:
        L += ["| Anúncio | Compra | Preço | Venda (início do farming) |", "|---|---|---|---|"]
        L += [f"| {t['titulo'][:60]} ({MP._h(t['release'])}) | +{t['latencia_min']} min | {t['p_in']:g} | {MP._h(t['saida_ts'])} |"
              for t in sorted(ab, key=lambda t: t["saida_ts"])]
        L.append("")
    if fe:
        L += ["| Anúncio | Latência | Espera | Bruto | Funding | Líquido | Excesso |", "|---|---|---|---|---|---|---|"]
        L += [f"| {t['titulo'][:60]} ({MP._h(t['release'])}) | {t['latencia_min']} min | "
              f"{(t['saida_ts'] - t['entrada_ts']) / 3_600_000:.0f} h | {t['bruto']:+.2f}% | "
              f"{t['funding']:+.3f}% | {t['liq']:+.2f}% | {t['excesso']:+.2f}% |"
              for t in sorted(fe, key=lambda t: t["release"], reverse=True)]
        L.append("")
    desc = [t for t in tr if t["status"] == "descartado"]
    if desc:
        L += [f"<details><summary>Descartados ({len(desc)})</summary>", ""]
        L += [f"- {t['titulo'][:70]} ({MP._h(t['release'])}): {t['motivo']}"
              for t in sorted(desc, key=lambda t: t["release"], reverse=True)]
        L += ["", "</details>", ""]
    if not tr:
        L += ["_Nenhum anúncio de Launchpool desde o início do registro "
              f"({MP._h(estado['iniciado']) if estado.get('iniciado') else '—'})._", ""]
    with open(LEDGER, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L))


def notifica(abertos, fechados):
    linhas = [f"Compra BNB a {t['p_in']:g}, +{t['latencia_min']} min; vende {MP._h(t['saida_ts'])}" for t in abertos]
    linhas += [f"Fecha BNB: liq {t['liq']:+.2f}%, exc {t['excesso']:+.2f}%" for t in fechados]
    if linhas:
        import fetch_and_check as M
        M.send_ntfy("Launchpool (papel)", "\n".join(linhas))


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
        # teste: anuncio antigo `code`, como se fosse detectado `lat` minutos depois, e fechado em seguida
        i = argv.index("--simular")
        code, lat = argv[i + 1], int(argv[i + 2])
        fp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache_anuncios", "cat48.json")
        a = next(x for x in json.load(open(fp, encoding="utf-8")) if x["code"] == code)
        a = {"id": a["id"], "code": a["code"], "title": a["title"].strip(), "releaseDate": a["releaseDate"]}
        estado = {"iniciado": 1, "vistos": [], "trades": {}}
        abertos, _ = processa(estado, a["releaseDate"] + lat * MIN, [a])
        fechados = fecha(estado, agora)
    else:
        arts = anuncios()
        if arts is None:
            print("[launchpool_paper] feed de anuncios inacessivel; nada processado")
            escreve_ledger(estado, agora)
            return
        abertos, fechados = processa(estado, agora, arts)
        notifica(abertos, fechados)
    salva(estado)
    escreve_ledger(estado, agora)
    print(f"[launchpool_paper] abertos agora: {len(abertos)} · fechados agora: {len(fechados)} · "
          f"total de trades: {len(estado.get('trades', {}))}")


if __name__ == "__main__":
    main(sys.argv[1:])
