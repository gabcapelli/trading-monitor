"""
Registro em PAPEL da venda antes de desbloqueio de tokens para insiders.
NAO envia ordem. Calcula o que a regra mandaria fazer e registra o resultado
em claude/unlock-paper.md. So biblioteca padrao do Python.

Origem: repo `token-unlocks` (estudo.py, pre-registrado em 23/09/2026).
Teste 2025-2026: vender 7 dias antes rendeu +2.1% de excesso sobre o
universo por evento (IC98.75 [+0.8, +3.4]) e +2.9% absoluto; sobreviveu a
bootstrap por token, placebo e dose-resposta, com ressalva de concentracao.

REGRA CONGELADA (23/09/2026 -- nao alterar durante o teste)
-----------------------------------------------------------
Evento (mesma definicao do estudo, fonte DefiLlama):
- salto de um dia na oferta desbloqueada documentada >= 1% da oferta da
  vespera, com >= 50% para "insiders" ou "privateSale";
- token com perpetuo USDT-M na Binance listado ha >= 30 dias no dia do evento;
- ticker ambiguo na CoinGecko so entra se estiver em VERIFICADOS;
- mesmo token com outro evento registrado a < 14 dias: fica so o primeiro;
- o evento precisa estar no calendario JA no dia da entrada (first_seen <=
  entrada). Evento descoberto depois e descartado ("conhecido tarde").
Operacao (t0 = dia UTC do desbloqueio):
- VENDE o perpetuo na abertura de t0 - 7 (00:00 UTC; 21:00 da vespera no
  Brasil) e recompra na abertura de t0. Sem stop, sem alvo, sem discricao.
- Versao PURA: so a venda. Custo 0.18% ida+volta; funding real (vendido
  recebe funding positivo).
- Versao COM HEDGE (registrada em paralelo): a venda + compra de peso igual
  da cesta dos 20 majors (menos o proprio token), mesmo nocional. Custo
  0.18% em cada perna. E a medida que o estudo demonstrou (excesso).
- Se a data do desbloqueio mudar depois da entrada, o trade segue a data
  original e fica marcado ("adiado?").

FONTES (os runners do GitHub ficam nos EUA, e fapi.binance.com pode
bloquear IP americano): precos pelo data.binance.vision (CDN estatico, sai
no dia seguinte) com a API da Binance como reserva; funding pela API ou pelo
arquivo mensal do vision -- se nenhum estiver disponivel, o trade fica com
funding PENDENTE e e completado nas rodadas seguintes.

CRITERIO DE LEITURA (fixado agora)
----------------------------------
So reavaliar com >= 150 trades fechados. Com desvio de ~11% por evento
(medido no teste), e o minimo para distinguir o +2% do estudo de zero.
No ritmo de 2025-2026 (~250 eventos/ano) sao ~7-8 meses.

Rode sem argumento (o workflow horario chama assim). `--sem-push` nao
notifica; `--seco` nao grava nada. So para teste: `--hoje AAAA-MM-DD` e
`--inicio AAAA-MM-DD` simulam outra data (com `--confiar-calendario`, o
calendario de hoje vale como se ja fosse conhecido na entrada), com UNLOCK_PAPER_DIR apontando para
uma pasta temporaria (e UNLOCK_PAPER_FAPI para simular a API bloqueada).
"""

import csv
import io
import json
import os
import sys
import time
import urllib.error
import urllib.request
import zipfile
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_TESTE = os.environ.get("UNLOCK_PAPER_DIR")     # so para teste: grava estado e registro em outra pasta
LEDGER = os.path.join(_TESTE or os.path.join(RAIZ, "claude"), "unlock-paper.md")
ESTADO = os.path.join(_TESTE or os.path.join(RAIZ, "monitor"), "unlock_paper_state.json")
PROTOCOLOS = os.path.join(RAIZ, "monitor", "unlock_paper_protocolos.json")

MS_DIA = 86_400_000
LIMIAR = 1.0
FRAC_INS = 0.5
INSIDERS = {"insiders", "privateSale"}
ANTES = 7
DEDUP = 14
MIN_LISTADO = 30
HORIZONTE = 30            # dias a frente no calendario
CUSTO = 0.0018
META = 150
EXCLUIR = {"GRAMUSDT", "REUSDT", "BASEDUSDT"}
# tickers ambiguos conferidos a mao em 23/09/2026 (token-unlocks/estudo.py)
VERIFICADOS = {"ALPHAUSDT", "ALTUSDT", "APEUSDT", "ARBUSDT", "BABYUSDT", "BBUSDT", "BNBUSDT",
               "FILUSDT", "HUSDT", "INITUSDT", "JUPUSDT", "MEGAUSDT", "MEMEUSDT", "MEUSDT",
               "MOVEUSDT", "MUSDT", "NEARUSDT", "OMNIUSDT", "OPNUSDT", "OPUSDT", "PUMPUSDT",
               "RUNEUSDT", "SEIUSDT", "SOLUSDT", "SOPHUSDT", "SUSDT", "TRUMPUSDT", "TRUUSDT",
               "WUSDT", "XAIUSDT"}
CESTA = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "XRPUSDT", "DOGEUSDT", "ARBUSDT", "WLDUSDT", "SUIUSDT",
         "UNIUSDT", "LINKUSDT", "BNBUSDT", "TRXUSDT", "ZECUSDT", "HYPEUSDT", "ADAUSDT", "XLMUSDT",
         "NEARUSDT", "AVAXUSDT", "LTCUSDT", "BCHUSDT"]
LLAMA = "https://defillama-datasets.llama.fi"
VISION = "https://data.binance.vision/data/futures/um"
S3 = "https://s3-ap-northeast-1.amazonaws.com/data.binance.vision"
FAPI = os.environ.get("UNLOCK_PAPER_FAPI", "https://fapi.binance.com/fapi/v1")


# ---------------------------------------------------------------------------
# HTTP
# ---------------------------------------------------------------------------

def _bytes(url, tentativas=3):
    for t in range(tentativas):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 unlock-paper"})
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code in (400, 403, 404, 451):
                return None
            if t == tentativas - 1:
                return None
        except Exception:
            if t == tentativas - 1:
                return None
        time.sleep(1 + 2 * t)


def _json(url):
    b = _bytes(url)
    return json.loads(b.decode("utf-8")) if b else None


def _csv_do_zip(url):
    b = _bytes(url)
    if not b:
        return None
    z = zipfile.ZipFile(io.BytesIO(b))
    return list(csv.reader(io.StringIO(z.read(z.namelist()[0]).decode())))


def _data(dia):
    return time.strftime("%Y-%m-%d", time.gmtime(dia * 86400))


# ---------------------------------------------------------------------------
# Binance: precos, funding, estreia do perpetuo
# ---------------------------------------------------------------------------

def _kline_vision(sym, dia):
    rows = _csv_do_zip(f"{VISION}/daily/klines/{sym}/1d/{sym}-1d-{_data(dia)}.zip")
    if not rows:
        return None
    for r in rows:
        if r and r[0].isdigit():
            return float(r[1]), float(r[4])
    return None


def abertura(sym, dia):
    """Preco de abertura do dia UTC (= fechamento da vespera)."""
    k = _kline_vision(sym, dia)
    if k:
        return k[0]
    k = _kline_vision(sym, dia - 1)
    if k:
        return k[1]
    r = _json(f"{FAPI}/klines?symbol={sym}&interval=1d&startTime={dia * MS_DIA}&limit=1")
    if r and int(r[0][0]) == dia * MS_DIA:
        return float(r[0][1])
    return None


def funding(sym, dia_ini, dia_fim):
    """Soma das taxas com fundingTime em [ini, fim). None = ainda indisponivel."""
    t0, t1 = dia_ini * MS_DIA, dia_fim * MS_DIA
    r = _json(f"{FAPI}/fundingRate?symbol={sym}&startTime={t0}&endTime={t1 - 1}&limit=1000")
    if isinstance(r, list):
        return sum(float(x["fundingRate"]) for x in r)
    meses = sorted({time.strftime("%Y-%m", time.gmtime(d * 86400)) for d in range(dia_ini, dia_fim)})
    tot = 0.0
    for m in meses:
        rows = _csv_do_zip(f"{VISION}/monthly/fundingRate/{sym}/{sym}-fundingRate-{m}.zip")
        if rows is None:
            return None
        for r in rows:
            if r and r[0].isdigit() and r[2] and t0 <= int(r[0]) < t1:
                tot += float(r[2])
    return tot


def estreia(sym, cache):
    """Dia UTC do primeiro candle diario do perpetuo (None = nao existe)."""
    if sym in cache:
        return cache[sym]
    b = _bytes(f"{S3}?delimiter=/&prefix=data/futures/um/daily/klines/{sym}/1d/&max-keys=1")
    dia = None
    if b:
        txt = b.decode()
        i = txt.find(f"{sym}-1d-")
        if i >= 0:
            d = txt[i + len(sym) + 4:i + len(sym) + 14]
            dia = int(datetime.strptime(d, "%Y-%m-%d").replace(tzinfo=timezone.utc).timestamp()) // 86400
    if dia is not None:          # "nao existe" nao fica em cache: o perpetuo pode ser listado depois
        cache[sym] = dia
    return dia


def todos_os_perpetuos():
    """Todos os simbolos com klines diarios de futuros USD-M no vision (vivos ou nao)."""
    out, marcador = set(), ""
    while True:
        b = _bytes(f"{S3}?delimiter=/&prefix=data/futures/um/daily/klines/&marker={marcador}")
        if not b:
            return out
        txt = b.decode()
        achados = [x.split("</Prefix>")[0] for x in txt.split("<CommonPrefixes><Prefix>")[1:]]
        for pre in achados:
            out.add(pre.rstrip("/").split("/")[-1])
        if "<IsTruncated>true</IsTruncated>" not in txt or not achados:
            return out
        marcador = achados[-1]


def ativo(sym, hoje):
    """Perpetuo negociando agora: candle de ha <= 3 dias no vision ou na API."""
    for d in range(hoje - 1, hoje - 4, -1):
        if _bytes(f"{VISION}/daily/klines/{sym}/1d/{sym}-1d-{_data(d)}.zip.CHECKSUM"):
            return True
    r = _json(f"{FAPI}/klines?symbol={sym}&interval=1d&limit=1")
    return bool(r)


# ---------------------------------------------------------------------------
# Calendario (DefiLlama)
# ---------------------------------------------------------------------------

def _categoria(label, cats):
    for c, labels in (cats or {}).items():
        if label in labels:
            return c
    return "sem_categoria"


def saltos(d, dia_min, dia_max):
    """Saltos diarios >= LIMIAR% da oferta com t0 em [dia_min, dia_max]."""
    doc = d.get("documentedData") or {}
    cats = d.get("categories") or {}
    series = []
    for s in doc.get("data", []):
        series.append((_categoria(s["label"], cats),
                       {p["timestamp"] // 86400: (p.get("unlocked") or 0.0) for p in s["data"]}))
    dias = sorted({t for _, pts in series for t in pts})
    out = []
    for a, b in zip(dias, dias[1:]):
        if b < dia_min or b > dia_max:
            continue
        circ = sum(pts.get(a, 0.0) for _, pts in series)
        por_cat = {}
        for cat, pts in series:
            dl = pts.get(b, 0.0) - pts.get(a, 0.0)
            if dl > 0:
                por_cat[cat] = por_cat.get(cat, 0.0) + dl
        tot = sum(por_cat.values())
        if circ <= 0 or tot <= 0 or 100 * tot / circ < LIMIAR:
            continue
        out.append({"t0": b, "pct": 100 * tot / circ,
                    "frac": sum(v for k, v in por_cat.items() if k in INSIDERS) / tot})
    return out


def mapa_ticker():
    cg = _json("https://api.coingecko.com/api/v3/coins/list") or []
    sym_de, n_ids = {}, {}
    for c in cg:
        s = c["symbol"].upper()
        sym_de[c["id"]] = s
        n_ids[s] = n_ids.get(s, 0) + 1
    return sym_de, n_ids


def atualiza_calendario(estado, hoje):
    protos = json.load(open(PROTOCOLOS, encoding="utf-8")) if os.path.exists(PROTOCOLOS) else {}
    lista = _json(f"{LLAMA}/emissionsProtocolsList") or []
    novos = [p for p in lista if p not in protos]
    sym_de, n_ids = mapa_ticker()
    if not sym_de:
        print("  CoinGecko indisponivel; calendario nao atualizado")
        return False
    perps = todos_os_perpetuos()
    if not perps:
        print("  listagem do vision indisponivel; calendario nao atualizado")
        return False
    for nome in novos:                      # protocolo novo: aprende o gecko_id uma vez
        d = _json(f"{LLAMA}/emissions/{nome}")
        if d:
            gid = d.get("gecko_id") or (d.get("metadata") or {}).get("token", "").replace("coingecko:", "")
            protos[nome] = gid or ""
    alvos = []
    for nome in lista:
        s = sym_de.get(protos.get(nome) or "")
        if not s:
            continue
        par = next((p for p in (f"{s}USDT", f"1000{s}USDT", f"1000000{s}USDT")
                    if p in perps and p not in EXCLUIR), None)
        if not par or (n_ids.get(s, 0) > 1 and par not in VERIFICADOS):
            continue
        estreia(par, estado["estreia"])
        alvos.append((nome, par))
    with ThreadPoolExecutor(max_workers=8) as ex:
        docs = list(ex.map(lambda a: _json(f"{LLAMA}/emissions/{a[0]}"), alvos))
    vistos = set()
    for (nome, par), d in zip(alvos, docs):
        if not d:
            continue
        for ev in saltos(d, hoje - 20, hoje + HORIZONTE):
            chave = f"{par}|{ev['t0']}"
            vistos.add(chave)
            c = estado["calendario"].setdefault(chave, {"par": par, "protocolo": nome, "t0": ev["t0"],
                                                        "first_seen": hoje})
            c.update({"pct": ev["pct"], "frac": ev["frac"], "last_seen": hoje})
    json.dump(protos, open(PROTOCOLOS, "w", encoding="utf-8"), indent=0, sort_keys=True)
    # limpa o que ja passou ha muito tempo e nao virou trade
    for k in list(estado["calendario"]):
        if estado["calendario"][k]["t0"] < hoje - 40 and k not in estado["trades"]:
            del estado["calendario"][k]
    estado["ultimo_refresh"] = hoje
    print(f"  calendario: {len(vistos)} eventos >= {LIMIAR}% entre {_data(hoje-20)} e {_data(hoje+HORIZONTE)}")
    return True


# ---------------------------------------------------------------------------
# Trades
# ---------------------------------------------------------------------------

def qualifica(c, estado):
    if c["frac"] < FRAC_INS or c["pct"] < LIMIAR:
        return "nao e de insiders"
    est = estado["estreia"].get(c["par"])
    if est is None or est > c["t0"] - MIN_LISTADO:
        return "perpetuo novo demais"
    for k, t in estado["trades"].items():
        if t["par"] == c["par"] and t["status"] != "descartado" and abs(t["t0"] - c["t0"]) < DEDUP \
                and k != f"{c['par']}|{c['t0']}":
            return "outro evento do mesmo token a < 14 dias"
    return None


def abre(c, hoje):
    ent = c["t0"] - ANTES
    px = abertura(c["par"], ent)
    if px is None:
        return None
    cesta = {s: abertura(s, ent) for s in CESTA if s != c["par"]}
    return {"par": c["par"], "protocolo": c["protocolo"], "t0": c["t0"], "entrada": ent,
            "pct": c["pct"], "frac": c["frac"], "first_seen": c["first_seen"],
            "status": "aberto", "px_in": px, "cesta_in": {k: v for k, v in cesta.items() if v}}


def fecha(t, estado):
    px = abertura(t["par"], t["t0"])
    if px is None:
        return False
    r = px / t["px_in"] - 1
    rc = []
    for s, p0 in t["cesta_in"].items():
        p1 = abertura(s, t["t0"])
        if p1:
            rc.append(p1 / p0 - 1)
    t.update({"px_out": px, "ret": r, "ret_cesta": sum(rc) / len(rc) if rc else 0.0,
              "status": "fechado"})
    cal = estado["calendario"].get(f"{t['par']}|{t['t0']}", {})
    t["confirmado"] = cal.get("last_seen", 0) >= t["t0"] - 1
    completa_funding(t)
    return True


def completa_funding(t):
    f = funding(t["par"], t["entrada"], t["t0"])
    fc = []
    for s in list(t["cesta_in"])[:20]:
        x = funding(s, t["entrada"], t["t0"])
        if x is None:
            f = None
            break
        fc.append(x)
    if f is None:
        t["funding"] = "pendente"
        t["puro"] = -t["ret"] - CUSTO
        t["hedge"] = -t["ret"] + t["ret_cesta"] - 2 * CUSTO
        return
    fcm = sum(fc) / len(fc) if fc else 0.0
    t["funding"] = "ok"
    t["fund"], t["fund_cesta"] = f, fcm
    t["puro"] = -t["ret"] - CUSTO + f
    t["hedge"] = -t["ret"] + t["ret_cesta"] - 2 * CUSTO + f - fcm


def processa(estado, hoje):
    abertos, fechados = [], []
    for k, c in sorted(estado["calendario"].items(), key=lambda kv: (kv[1]["t0"], kv[0])):
        if k in estado["trades"] or hoje < c["t0"] - ANTES:
            continue
        if c["first_seen"] > c["t0"] - ANTES:
            estado["trades"][k] = {**c, "status": "descartado", "motivo": "conhecido tarde"}
            continue
        motivo = qualifica(c, estado)
        if motivo:
            if c["frac"] >= FRAC_INS:      # so registra descarte de evento de insiders
                estado["trades"][k] = {**c, "status": "descartado", "motivo": motivo}
            continue
        if not ativo(c["par"], hoje):
            estado["trades"][k] = {**c, "status": "descartado", "motivo": "perpetuo inativo"}
            continue
        t = abre(c, hoje)
        if t:
            estado["trades"][k] = t
            abertos.append(t)
    for t in estado["trades"].values():
        if t["status"] == "aberto" and hoje >= t["t0"]:
            if fecha(t, estado):
                fechados.append(t)
        elif t["status"] == "fechado" and t.get("funding") == "pendente":
            completa_funding(t)
    return abertos, fechados


# ---------------------------------------------------------------------------
# Registro e notificacao
# ---------------------------------------------------------------------------

def escreve_ledger(estado, hoje):
    tr = estado["trades"].values()
    fech = sorted([t for t in tr if t["status"] == "fechado"], key=lambda t: t["t0"])
    abertos = sorted([t for t in tr if t["status"] == "aberto"], key=lambda t: t["t0"])
    desc = [t for t in tr if t["status"] == "descartado"]
    prox = sorted([c for k, c in estado["calendario"].items()
                   if k not in estado["trades"] and c["t0"] - ANTES > hoje and c["frac"] >= FRAC_INS],
                  key=lambda c: c["t0"])
    L = ["# Registro em papel — venda antes de desbloqueio de tokens",
         "",
         "> Gerado por `monitor/unlock_paper.py`. **Nenhuma ordem é enviada.**",
         "> Regra congelada em 23/09/2026 (repo `token-unlocks`): vender o perpétuo na abertura",
         "> de 7 dias antes de todo desbloqueio ≥ 1% da oferta com ≥ 50% para insiders, e",
         "> recomprar na abertura do dia do desbloqueio. **Puro** = só a venda; **com hedge** =",
         "> venda + compra da cesta dos 20 majors. Custo 0.18% por perna e funding real.",
         f"> **Só reavaliar com {META} trades fechados.** Antes disso é ruído.",
         "",
         f"_Atualizado em {_data(hoje)} (calendário de {_data(estado.get('ultimo_refresh') or hoje)})._",
         ""]
    if fech:
        n = len(fech)
        mp = sum(t["puro"] for t in fech) / n
        mh = sum(t["hedge"] for t in fech) / n
        pos = sum(1 for t in fech if t["hedge"] > 0)
        pend = sum(1 for t in fech if t.get("funding") == "pendente")
        L += [f"**Trades fechados:** {n} de {META} ({100*n/META:.0f}%)"
              + (f" · {pend} com funding pendente" if pend else ""), "",
              f"**Média por trade:** puro {100*mp:+.2f}% · com hedge {100*mh:+.2f}% · "
              f"hedge positivo em {pos}/{n} ({100*pos/n:.0f}%)", "",
              "_Referência do backtest (2025–2026): puro +2.9%, excesso sobre o universo +2.1%._", ""]
    L += ["## Abertos", ""]
    if abertos:
        L += ["| Token | Desbloqueio | % da oferta | Venda em (abertura) | Preço de entrada |", "|---|---|---|---|---|"]
        L += [f"| {t['par'].replace('USDT', '')} | {_data(t['t0'])} | {t['pct']:.1f}% | {_data(t['entrada'])} | "
              f"{t['px_in']:g} |" for t in abertos]
    else:
        L.append("_Nenhum._")
    L += ["", "## Próximas entradas (calendário atual)", ""]
    if prox:
        L += ["| Token | Desbloqueio | % da oferta | % insiders | Entrada prevista |", "|---|---|---|---|---|"]
        L += [f"| {c['par'].replace('USDT', '')} | {_data(c['t0'])} | {c['pct']:.1f}% | {100*c['frac']:.0f}% | "
              f"{_data(c['t0'] - ANTES)} |" for c in prox[:25]]
        L.append("")
        L.append("_Passa pelos filtros (perpétuo com ≥ 30 dias, mesmo token a ≥ 14 dias) só no dia da entrada._")
    else:
        L.append("_Nenhuma nos próximos dias._")
    L += ["", "## Fechados", ""]
    if fech:
        L += ["| Token | Desbloqueio | % da oferta | Retorno do token | Cesta | Puro | Com hedge | Obs. |",
              "|---|---|---|---|---|---|---|---|"]
        for t in reversed(fech):
            obs = []
            if t.get("funding") == "pendente":
                obs.append("funding pendente")
            if not t.get("confirmado", True):
                obs.append("adiado?")
            L.append(f"| {t['par'].replace('USDT', '')} | {_data(t['t0'])} | {t['pct']:.1f}% | {100*t['ret']:+.2f}% | "
                     f"{100*t['ret_cesta']:+.2f}% | {100*t['puro']:+.2f}% | {100*t['hedge']:+.2f}% | {', '.join(obs)} |")
    else:
        L.append("_Nenhum ainda._")
    if desc:
        L += ["", f"<details><summary>Descartados ({len(desc)})</summary>", ""]
        L += [f"- {t['par'].replace('USDT', '')} {_data(t['t0'])}: {t['motivo']}" for t in sorted(desc, key=lambda t: t["t0"])]
        L += ["", "</details>"]
    L.append("")
    with open(LEDGER, "w", encoding="utf-8") as f:
        f.write("\n".join(L))


def notifica(abertos, fechados):
    import fetch_and_check as m
    if abertos:
        m.send_ntfy(f"Desbloqueio: {len(abertos)} venda(s) em papel",
                    "\n".join(f"VENDER {t['par']} a {t['px_in']:g} -- desbloqueio de {t['pct']:.1f}% "
                              f"em {_data(t['t0'])} (recompra na abertura desse dia)" for t in abertos)
                    + "\nRegistro em papel, nao e ordem.")
    if fechados:
        m.send_ntfy(f"Desbloqueio: {len(fechados)} trade(s) fechado(s) em papel",
                    "\n".join(f"{t['par']}: puro {100*t['puro']:+.2f}% | com hedge {100*t['hedge']:+.2f}%"
                              for t in fechados) + "\nVer claude/unlock-paper.md.")


def carrega_estado():
    if os.path.exists(ESTADO):
        return json.load(open(ESTADO, encoding="utf-8"))
    return {"inicio": None, "ultimo_refresh": None, "estreia": {}, "calendario": {}, "trades": {}}


def main():
    agora = datetime.now(timezone.utc)
    hoje = int(agora.timestamp()) // 86400
    arg = lambda nome: sys.argv[sys.argv.index(nome) + 1] if nome in sys.argv else None
    dia_de = lambda d: int(datetime.strptime(d, "%Y-%m-%d").replace(tzinfo=timezone.utc).timestamp()) // 86400
    if arg("--hoje"):
        assert _TESTE, "--hoje so com UNLOCK_PAPER_DIR (nao sujar o registro real)"
        hoje = dia_de(arg("--hoje"))
    estado = carrega_estado()
    if estado["inicio"] is None:
        estado["inicio"] = dia_de(arg("--inicio")) if arg("--inicio") else hoje
        print(f"iniciando registro em {_data(estado['inicio'])}")
    if estado.get("ultimo_refresh") != hoje:
        atualiza_calendario(estado, hoje)
        if "--confiar-calendario" in sys.argv:   # so teste: finge que o calendario ja era conhecido
            assert _TESTE
            for c in estado["calendario"].values():
                c["first_seen"] = min(c["first_seen"], c["t0"] - ANTES)
    # trades so para eventos com entrada a partir do inicio do registro
    for k, c in list(estado["calendario"].items()):
        if c["t0"] - ANTES < estado["inicio"] and k not in estado["trades"]:
            c["antes_do_inicio"] = True
    cal_valido = {k: c for k, c in estado["calendario"].items() if not c.get("antes_do_inicio")}
    abertos, fechados = processa({**estado, "calendario": cal_valido}, hoje)
    for t in abertos:
        print(f"  ABRE  {t['par']} desbloqueio {_data(t['t0'])} ({t['pct']:.1f}%) a {t['px_in']:g}")
    for t in fechados:
        print(f"  FECHA {t['par']} puro {100*t['puro']:+.2f}% | hedge {100*t['hedge']:+.2f}%")
    if "--seco" in sys.argv:
        return
    with open(ESTADO, "w", encoding="utf-8") as f:
        json.dump(estado, f, indent=0, sort_keys=True)
    escreve_ledger(estado, hoje)
    if "--sem-push" not in sys.argv and (abertos or fechados):
        notifica(abertos, fechados)


if __name__ == "__main__":
    main()
