"""
Registro em papel -- vender o token novo de HODLer Airdrop / Launchpool / Megadrop.
REGRA CONGELADA em 24/11/2026 (estudo 91 de claude/estudos-avulsos.md). Nenhuma
ordem e enviada.

ORIGEM
------
Estudo 91 (pre-registrado, 69 eventos 2020-25): vendido no perpetuo do token
1h depois da primeira hora negociada do perpetuo, por 7 dias: liquido +12.0%,
IC95 [+2.7, +20.6]; excesso sobre vender 20 majors +15.3% [+6.1, +23.5].
Ressalvas: metade dos tokens ja estava nos estudos 29/30 (amostra nao limpa),
2024 deu ~0, squeezes de -100% a -127%.

GATILHO NOVO, ESCOLHIDO DEPOIS DE VER O RESULTADO: em 2026 a Binance abre o
perpetuo antes do anuncio (pre-mercado), e o estudo excluiu esses eventos. Aqui
o gatilho e a ABERTURA DO SPOT, nao testada no historico. O papel testa a regra
como esta, sem ajuste.

REGRA
-----
- Feed: catalogo 48 de anuncios da Binance (direto ou pelo proxy, rota /cms).
- Evento: titulo com "HODLer Airdrop", "Launchpool" ou "Megadrop"; ticker =
  palavra depois de "Earn"/"Farm" (ou entre parenteses). Um trade por ticker.
- Gatilho = o que vier por ultimo entre a abertura do spot e o anuncio do airdrop
  (em 2026 o airdrop costuma ser retroativo, com o token ja negociando):
  a) corpo traz "will (then) list ... at <data> (UTC)": entrada = essa data + 60 min;
  b) sem data no corpo e perpetuo ja negociando na deteccao (ate 90 min do
     anuncio): entrada = minuto da deteccao (como o papel do Launchpool);
  c) sem data e sem perpetuo: espera ate 30 dias por um anuncio "Binance Will
     List ... (TICKER)" no mesmo feed e usa a data do corpo dele + 60 min.
- Entrada: VENDE o perpetuo TICKERUSDT (ou 1000TICKERUSDT). Sem perpetuo no
  minuto da entrada (ate 1 dia depois): descartado.
- Saida: recompra na abertura do minuto entrada + 7 dias. Sem stop.

MEDIDAS (% do nocional, positivo = vendido ganhou)
--------------------------------------------------
- `bruto` = -(saida/entrada - 1).
- `liq` = bruto - 0.18% de custo + funding recebido pelo vendido.
- `excesso` = bruto - (vender a cesta de 20 majors nos mesmos minutos).

LEITURA
-------
So reavaliar com 30 TRADES fechados. Criterio: media de `liq` e de `excesso`
com IC95 > 0 (bootstrap por trade). No ritmo de 2025-26 (~1 a 3 por mes),
cerca de 1 a 2 anos.

Teste: `--simular <code do anuncio>` processa um anuncio antigo numa pasta
temporaria (AIRDROP_PAPER_DIR), com precos reais.
"""

import json
import os
import re
import sys
import time
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import launchpool_paper as LP
import monitoring_paper as MP
import unlock_paper as U

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_TESTE = os.environ.get("AIRDROP_PAPER_DIR")
LEDGER = os.path.join(_TESTE or os.path.join(RAIZ, "claude"), "airdrop-paper.md")
ESTADO = os.path.join(_TESTE or os.path.join(RAIZ, "monitor"), "airdrop_paper_state.json")

MIN, DIA = 60_000, 86_400_000
ATRASO = 60 * MIN
DURACAO = 7 * DIA
CUSTO = 0.18
META = 30
RE_TITULO = re.compile(r"HODLer Airdrop|Launchpool|Megadrop")
RE_TICKER = re.compile(r"(?:Earn|Farm)\s+([A-Z0-9]+)")
RE_PAR = re.compile(r"\(([A-Z0-9]+)\)")
RE_SPOT = re.compile(r"will (?:then )?list .{0,160}? at\s+" + LP.DATA, re.S)
MAJORS = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "XRPUSDT", "DOGEUSDT", "ARBUSDT", "WLDUSDT", "SUIUSDT",
          "UNIUSDT", "LINKUSDT", "BNBUSDT", "TRXUSDT", "ZECUSDT", "HYPEUSDT", "ADAUSDT", "XLMUSDT",
          "NEARUSDT", "AVAXUSDT", "LTCUSDT", "BCHUSDT"]


def ticker(titulo):
    m = RE_TICKER.search(titulo) or RE_PAR.search(titulo)
    return m.group(1) if m else None


def abertura_spot(texto):
    m = RE_SPOT.search(texto or "")
    if not m:
        return None
    a, mes, d, h, mi, ampm = m.groups()
    h = int(h)
    if ampm == "PM" and h < 12:
        h += 12
    if ampm == "AM" and h == 12:
        h = 0
    return int(datetime(int(a), int(mes), int(d), h, int(mi), tzinfo=timezone.utc).timestamp() * 1000)


def cesta(t0, t1):
    rets = []
    for s in MAJORS:
        a, b = MP.abertura_1m(s, t0), MP.abertura_1m(s, t1)
        if a and b:
            rets.append(-100 * (b / a - 1))
    return sum(rets) / len(rets) if len(rets) >= 10 else None


# ---------------------------------------------------------------------------
# Regra
# ---------------------------------------------------------------------------

def registra(estado, a):
    """Cria o trade 'agendado' (ou descartado). False = corpo inacessivel, tentar de novo."""
    tk = ticker(a["title"])
    base = {"anuncio_id": a["id"], "code": a["code"], "titulo": a["title"], "release": a["releaseDate"],
            "token": tk}
    chave = str(a["id"])
    if not tk:
        estado["trades"][chave] = {**base, "status": "descartado", "motivo": "sem ticker no titulo"}
        return True
    if any(t.get("token") == tk for k, t in estado["trades"].items() if k != chave):
        estado["trades"][chave] = {**base, "status": "descartado", "motivo": "ticker ja registrado"}
        return True
    texto, _ = LP.corpo(a["code"])
    if texto is None:
        return False
    spot = abertura_spot(texto)
    if spot is not None:
        agenda(estado["trades"], chave, base, spot // MIN * MIN + ATRASO, "data no anuncio")
        return True
    ent = agora_min(estado)
    if ent - a["releaseDate"] <= 90 * MIN and perp(tk, ent):
        agenda(estado["trades"], chave, base, ent, "ja negociando")
        return True
    estado["trades"][chave] = {**base, "status": "aguardando_listagem"}
    return True


def agora_min(estado):
    return estado["_agora"] // MIN * MIN


def perp(tk, ts):
    for sym in (f"{tk}USDT", f"1000{tk}USDT"):
        if MP.abertura_1m(sym, ts):
            return sym
    return None


def agenda(trades, chave, base, ent, gatilho):
    trades[chave] = {**base, "status": "agendado", "gatilho": gatilho, "entrada_ts": ent,
                     "saida_ts": ent + DURACAO}


def listagem_tardia(estado, a):
    """Anuncio 'Binance Will List ... (TK)' para trade aguardando listagem."""
    if not re.search(r"Will List", a["title"]):
        return
    for chave, t in estado["trades"].items():
        if t["status"] == "aguardando_listagem" and f"({t['token']})" in a["title"]:
            texto, _ = LP.corpo(a["code"])
            spot = abertura_spot(texto)
            base = {k: t[k] for k in ("anuncio_id", "code", "titulo", "release", "token")}
            if spot is not None:
                agenda(estado["trades"], chave, base, spot // MIN * MIN + ATRASO, "anuncio de listagem")


def abre(estado, agora):
    abertos = []
    for t in estado["trades"].values():
        if t["status"] != "agendado" or agora < t["entrada_ts"] + 2 * MIN:
            continue
        for sym in (f"{t['token']}USDT", f"1000{t['token']}USDT"):
            p = MP.abertura_1m(sym, t["entrada_ts"])
            if p:
                t.update({"status": "aberto", "sym": sym, "p_in": p})
                abertos.append(t)
                break
        else:
            if agora - t["entrada_ts"] > DIA:
                t.update({"status": "descartado", "motivo": "sem perpetuo na hora da entrada"})
    return abertos


def fecha(estado, agora):
    fechados = []
    for t in estado["trades"].values():
        if t["status"] != "aberto" or agora < t["saida_ts"] + 2 * MIN:
            continue
        p_out = MP.abertura_1m(t["sym"], t["saida_ts"])
        f = MP.funding_recebido(t["sym"], t["entrada_ts"], t["saida_ts"])
        c = cesta(t["entrada_ts"], t["saida_ts"])
        if p_out is None or f is None or c is None:
            if agora - t["saida_ts"] > 3 * DIA:
                t.update({"status": "descartado", "motivo": "sem preco de saida em 3 dias"})
            continue
        bruto = -100 * (p_out / t["p_in"] - 1)
        t.update({"status": "fechado", "p_out": p_out, "funding": f, "bruto": bruto, "cesta": c,
                  "liq": bruto - CUSTO + f, "excesso": bruto - c})
        fechados.append(t)
    return fechados


def processa(estado, agora, arts):
    if not estado.get("iniciado"):
        estado.update({"iniciado": agora, "vistos": sorted({a["id"] for a in arts}), "trades": {}})
        return [], []
    estado["_agora"] = agora
    vistos = set(estado["vistos"])
    for a in sorted((a for a in arts if a["id"] not in vistos), key=lambda a: a["releaseDate"]):
        listagem_tardia(estado, a)
        if not RE_TITULO.search(a["title"]) or registra(estado, a):
            vistos.add(a["id"])
    estado["vistos"] = sorted(vistos)
    for t in estado["trades"].values():
        if t["status"] == "aguardando_listagem" and agora - t["release"] > 30 * DIA:
            t.update({"status": "descartado", "motivo": "sem listagem em 30 dias"})
    estado.pop("_agora", None)
    return abre(estado, agora), fecha(estado, agora)


# ---------------------------------------------------------------------------
# Registro
# ---------------------------------------------------------------------------

def escreve_ledger(estado, agora):
    tr = list(estado.get("trades", {}).values())
    fe = [t for t in tr if t["status"] == "fechado"]
    ab = [t for t in tr if t["status"] in ("aberto", "agendado", "aguardando_listagem")]
    L = ["# Registro em papel — venda do token novo de HODLer Airdrop / Launchpool", "",
         "> Gerado por `monitor/airdrop_paper.py`. **Nenhuma ordem é enviada.**",
         "> Regra congelada em 24/11/2026 (estudo 91): vender o perpétuo do token 1h depois da abertura",
         "> do spot (ou na detecção do anúncio, se o token já negocia) e recomprar 7 dias depois. Custo 0.18% e funding real; excesso sobre vender 20 majors.",
         "> O gatilho na abertura do spot foi escolhido depois de ver o estudo (lá era a abertura do perpétuo).",
         f"> **Só reavaliar com {META} trades fechados.**", "",
         f"_Atualizado em {MP._h(agora)} (Brasília)._", "",
         f"**Trades fechados:** {len(fe)} de {META} ({100 * len(fe) // META}%)"]
    if fe:
        L.append(f"\n**Média por trade:** líquido {MP._media([t['liq'] for t in fe]):+.2f}% · "
                 f"excesso {MP._media([t['excesso'] for t in fe]):+.2f}% · "
                 f"líquido positivo em {sum(t['liq'] > 0 for t in fe)}/{len(fe)}")
    L += ["\n_Referência do estudo 91: +12.0% líquido, +15.3% de excesso (gatilho na abertura do perpétuo)._", ""]
    if ab:
        L += ["| Token | Status | Venda em | Preço | Recompra em |", "|---|---|---|---|---|"]
        L += [f"| {t['token']} | {t['status']} | {MP._h(t['entrada_ts']) if 'entrada_ts' in t else '—'} | {t.get('p_in', '—')} | {MP._h(t['saida_ts']) if 'saida_ts' in t else '—'} |"
              for t in sorted(ab, key=lambda t: t.get("entrada_ts", t["release"]))]
        L.append("")
    if fe:
        L += ["| Token | Venda | Bruto | Funding | Líquido | Excesso |", "|---|---|---|---|---|---|"]
        L += [f"| {t['token']} | {MP._h(t['entrada_ts'])} | {t['bruto']:+.2f}% | {t['funding']:+.3f}% | "
              f"{t['liq']:+.2f}% | {t['excesso']:+.2f}% |"
              for t in sorted(fe, key=lambda t: t["entrada_ts"], reverse=True)]
        L.append("")
    desc = [t for t in tr if t["status"] == "descartado"]
    if desc:
        L += [f"<details><summary>Descartados ({len(desc)})</summary>", ""]
        L += [f"- {t['titulo'][:70]} ({MP._h(t['release'])}): {t['motivo']}"
              for t in sorted(desc, key=lambda t: t["release"], reverse=True)]
        L += ["", "</details>", ""]
    if not tr:
        L += ["_Nenhum anúncio desde o início do registro "
              f"({MP._h(estado['iniciado']) if estado.get('iniciado') else '—'})._", ""]
    with open(LEDGER, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L))


def notifica(abertos, fechados):
    linhas = [f"Vende {t['sym']} a {t['p_in']:g}; recompra {MP._h(t['saida_ts'])}" for t in abertos]
    linhas += [f"Fecha {t['sym']}: liq {t['liq']:+.2f}%, exc {t['excesso']:+.2f}%" for t in fechados]
    if linhas:
        import fetch_and_check as M
        M.send_ntfy("Airdrop (papel)", "\n".join(linhas))


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
        code = argv[argv.index("--simular") + 1]
        fp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache_anuncios", "cat48.json")
        a = next(x for x in json.load(open(fp, encoding="utf-8")) if x["code"] == code)
        a = {"id": a["id"], "code": a["code"], "title": a["title"].strip(), "releaseDate": a["releaseDate"]}
        estado = {"iniciado": 1, "vistos": [], "trades": {}}
        sim = a["releaseDate"] + 30 * MIN
        abertos, fechados = processa(estado, sim, [a])
        abertos += abre(estado, agora)
        fechados += fecha(estado, agora)
    else:
        arts = LP.anuncios()
        if arts is None:
            print("[airdrop_paper] feed de anuncios inacessivel; nada processado")
            escreve_ledger(estado, agora)
            return
        abertos, fechados = processa(estado, agora, arts)
        notifica(abertos, fechados)
    salva(estado)
    escreve_ledger(estado, agora)
    print(f"[airdrop_paper] abertos agora: {len(abertos)} · fechados agora: {len(fechados)} · "
          f"total: {len(estado.get('trades', {}))}")


if __name__ == "__main__":
    main(sys.argv[1:])
