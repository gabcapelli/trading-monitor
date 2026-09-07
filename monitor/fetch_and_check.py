#!/usr/bin/env python3
"""
Monitoramento automatico BTC-USDT-SWAP (OKX) -- versao gratuita (GitHub Actions).

Replica a parte MECANICA do checklist da secao 4 de plano-trade-price-action.md:
- Le candles 1h e 4h da OKX (endpoint publico, sem API key).
- Classifica tendencia no 4h (HH/HL = alta, LH/LL = baixa, senao lateral) via pivos fractais.
- Mapeia zonas candidatas de Setup A (rompimento + retest) e Setup B (reversao em zona),
  com as mesmas regras de validade da secao 2 do plano (8 candles sem toque OU 3 toques
  sem confirmacao -> zona expira).
- So dispara notificacao (ntfy.sh, gratuito) quando o STATUS muda (zona nova mapeada,
  confirmacao, invalidacao ou expiracao) -- mesma logica de "silencio quando nao muda"
  da automacao original no Cowork.
- Atualiza claude/log-monitoramento-btc-auto.md (uma linha por execucao) e
  claude/status-simulacao.md (resumo do estado atual), no mesmo formato dos arquivos
  do projeto, para que voce (ou uma sessao do Claude) possa ler o contexto depois.

O QUE ESTE SCRIPT NAO FAZ (limitacao deliberada, leia antes de confiar cegamente):
- Nao gera a "leitura" qualitativa em prosa que o Claude fazia (juizo de contexto,
  forca de candle, etc.) -- so registra fatos objetivos (preco, zona, toques, ATR).
- A deteccao de estrutura (pivos fractais, janela=3) e uma APROXIMACAO geometrica,
  igual a usada no backtest (claude/backtest-setup-ab.md) -- nao substitui o seu
  julgamento discricionario. Trate confirmacoes daqui como candidatas a validar
  manualmente antes de contar como um dos 30 trades da secao 3.4 do plano.
- So opera BTC-USDT-SWAP, 1h execucao / 4h contexto -- mesmo escopo do plano atual.

Dependencias: NENHUMA alem da biblioteca padrao do Python (urllib, json, etc.)
-- roda em qualquer runner do GitHub Actions sem "pip install".

--------------------------------------------------------------------------------
CHANGELOG (correcoes desta versao, 07/09/2026):

1. BUG CORRIGIDO -- Setup A nunca disparava mesmo com rompimento claro:
   `try_map_new_zone` checava `lows_1h` (fundos) como condicao de entrada para
   detectar rompimento de RESISTENCIA em tendencia de alta -- lista errada.
   Se nao havia um fundo fractal confirmado recente (comum numa alta sustentada,
   onde pullbacks podem nao formar pivo de 3 candles de cada lado), o codigo caia
   direto em `broke = False`, mesmo com o preco ja tendo rompido a resistencia
   (`highs_1h`) ha varias horas. Corrigido para checar `highs_1h` (alta) /
   `lows_1h` (baixa) -- a lista que de fato define o nivel de rompimento.

2. BUG CORRIGIDO -- Setup B so olhava o swing 4h mais recente:
   o `break` do loop de swings maduros estava no mesmo nivel do `if` de
   maturidade (`STALE_4H_CANDLES`), entao o loop sempre parava depois do
   primeiro swing (mesmo que ainda "jovem demais"), nunca chegando a considerar
   o proximo swing mais antigo, que poderia ja estar maduro e perto do preco.
   Corrigido com `continue` explicito para pular swings imaturos.

3. LOG ENRIQUECIDO (sem custo de LLM, so campos objetivos a mais):
   - High/Low do candle 1h mais recente fechado (antes so tinha o close).
   - Ultimo swing 1h confirmado usado como referencia (nivel + ha quantos
     candles foi confirmado), para dar visibilidade ao que o script esta
     vigiando mesmo quando o status e "sem_zona".
   - ATR 1h atual (calculado internamente, mas antes nunca aparecia no log).
--------------------------------------------------------------------------------
"""

import json
import os
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta

# ---------------------------------------------------------------------------
# Configuracao
# ---------------------------------------------------------------------------

OKX_BASE = "https://www.okx.com"
INST_ID = "BTC-USDT-SWAP"

# Regras de zona (secao 2 do plano) -- pontos de partida, recalibrar com dados reais.
ZONE_MAX_CANDLES_1H = 8      # zona expira se nao for tocada em 8 candles de 1h
ZONE_MAX_TOUCHES = 3         # zona expira apos 3 toques sem confirmacao valida
ZONE_ATR_MULT = 0.25         # largura da zona em multiplos de ATR
STALE_4H_CANDLES = 10        # swing 4h so vira candidato a Setup B apos N candles "maduro"

PIVOT_WINDOW = 3             # janela esquerda/direita para pivo fractal confirmado
ATR_PERIOD = 14

BRT = timezone(timedelta(hours=-3))

STATE_PATH = os.path.join("monitor", "state.json")
LOG_PATH = os.path.join("claude", "log-monitoramento-btc-auto.md")
STATUS_PATH = os.path.join("claude", "status-simulacao.md")

NTFY_TOPIC = os.environ.get("NTFY_TOPIC", "").strip()  # definido via GitHub secret


# ---------------------------------------------------------------------------
# Fetch OKX (sem dependencias externas -- so urllib)
# ---------------------------------------------------------------------------

def okx_get(path, params):
    query = "&".join(f"{k}={v}" for k, v in params.items())
    url = f"{OKX_BASE}{path}?{query}"
    req = urllib.request.Request(url, headers={"User-Agent": "btc-monitor-script"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    if data.get("code") != "0":
        raise RuntimeError(f"OKX API error: {data}")
    return data["data"]


def fetch_candles(bar, limit=150):
    """
    Retorna lista de candles mais RECENTE -> MAIS ANTIGO (como a OKX devolve),
    cada um: [ts_ms, open, high, low, close, vol, volCcyQuote, confirm]
    Reordena para MAIS ANTIGO -> MAIS RECENTE (mais facil de processar em sequencia).
    """
    raw = okx_get("/api/v5/market/candles", {"instId": INST_ID, "bar": bar, "limit": limit})
    raw = list(reversed(raw))  # antigo -> recente
    candles = []
    for row in raw:
        candles.append({
            "ts": int(row[0]),
            "open": float(row[1]),
            "high": float(row[2]),
            "low": float(row[3]),
            "close": float(row[4]),
            "vol": float(row[5]),
            "volCcyQuote": float(row[7]) if len(row) > 7 else float(row[6]),
            "confirm": row[8] if len(row) > 8 else row[-1],
        })
    return candles


def fetch_funding_rate():
    data = okx_get("/api/v5/public/funding-rate", {"instId": INST_ID})
    return float(data[0]["fundingRate"])


# ---------------------------------------------------------------------------
# Indicadores / estrutura (mesma logica do backtest, simplificada para uso incremental)
# ---------------------------------------------------------------------------

def true_range(c_prev, c):
    return max(
        c["high"] - c["low"],
        abs(c["high"] - c_prev["close"]),
        abs(c["low"] - c_prev["close"]),
    )


def atr(candles, period=ATR_PERIOD):
    closed = [c for c in candles if c["confirm"] == "1"]
    if len(closed) < period + 1:
        return None
    trs = [true_range(closed[i - 1], closed[i]) for i in range(1, len(closed))]
    return sum(trs[-period:]) / period


def find_confirmed_pivots(candles, window=PIVOT_WINDOW):
    """
    Pivos fractais confirmados: candle i e topo se high[i] > high de 'window' candles
    de cada lado; fundo se low[i] < low de 'window' candles de cada lado.
    So considera candles fechados (confirm == '1'). Retorna listas de (idx, price).
    """
    closed = [c for c in candles if c["confirm"] == "1"]
    highs = []
    lows = []
    n = len(closed)
    for i in range(window, n - window):
        seg_h = [closed[j]["high"] for j in range(i - window, i + window + 1)]
        seg_l = [closed[j]["low"] for j in range(i - window, i + window + 1)]
        if closed[i]["high"] == max(seg_h):
            highs.append((i, closed[i]["high"]))
        if closed[i]["low"] == min(seg_l):
            lows.append((i, closed[i]["low"]))
    return highs, lows, closed


def classify_trend_4h(candles_4h):
    highs, lows, closed = find_confirmed_pivots(candles_4h)
    if len(highs) < 2 or len(lows) < 2:
        return "lateral", closed
    h1, h2 = highs[-2][1], highs[-1][1]
    l1, l2 = lows[-2][1], lows[-1][1]
    if h2 > h1 and l2 > l1:
        return "alta", closed
    if h2 < h1 and l2 < l1:
        return "baixa", closed
    return "lateral", closed


# ---------------------------------------------------------------------------
# Estado persistente (zonas candidatas, status atual)
# ---------------------------------------------------------------------------

def load_state():
    if os.path.exists(STATE_PATH):
        with open(STATE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"status": "sem_zona", "zone": None, "last_1h_ts": None}


def save_state(state):
    os.makedirs(os.path.dirname(STATE_PATH), exist_ok=True)
    with open(STATE_PATH, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


# ---------------------------------------------------------------------------
# Logica de checklist mecanico (Setup A / Setup B), secao 2 e 4 do plano
# ---------------------------------------------------------------------------

def last_closed(candles):
    closed = [c for c in candles if c["confirm"] == "1"]
    return closed[-1] if closed else None


def try_map_new_zone(trend, candles_1h, candles_4h, atr_1h):
    """
    Tenta mapear uma nova zona candidata (Setup A se ha tendencia 4h definida,
    Setup B se preco esta perto de um swing 4h "maduro"). Retorna dict da zona
    ou None se nada relevante for encontrado agora.
    """
    highs_1h, lows_1h, closed_1h = find_confirmed_pivots(candles_1h)
    last = closed_1h[-1]

    if trend in ("alta", "baixa") and atr_1h:
        # Setup A: procura o ultimo swing 1h confirmado NA DIRECAO DO ROMPIMENTO
        # (resistencia para alta, suporte para baixa) e verifica se o preco ja
        # rompeu esse nivel (condicao para comecar a vigiar um retest).
        # CORRIGIDO: antes checava a lista errada (lows_1h para tendencia de alta),
        # o que fazia o rompimento nunca ser detectado quando nao havia um fundo
        # fractal confirmado recente -- mesmo com o preco ja tendo rompido a
        # resistencia (highs_1h) ha varias horas.
        ref_swing = None
        broke = False
        if trend == "alta" and highs_1h:
            ref_swing = highs_1h[-1][1]
            broke = last["close"] > ref_swing
        elif trend == "baixa" and lows_1h:
            ref_swing = lows_1h[-1][1]
            broke = last["close"] < ref_swing

        if ref_swing is not None and broke:
            return {
                "setup": "A",
                "direction": "compra" if trend == "alta" else "venda",
                "level": ref_swing,
                "zone_low": ref_swing - ZONE_ATR_MULT * atr_1h,
                "zone_high": ref_swing + ZONE_ATR_MULT * atr_1h,
                "candles_since_creation": 0,
                "touches": 0,
                "created_at": last["ts"],
            }

    # Setup B: swing 4h maduro (>= STALE_4H_CANDLES desde a confirmacao) como zona.
    # CORRIGIDO: o `break` estava fora do `if` de maturidade, entao o loop sempre
    # parava no primeiro swing (mesmo imaturo) em vez de continuar procurando um
    # swing mais antigo que ja estivesse maduro e perto do preco.
    highs_4h, lows_4h, closed_4h = find_confirmed_pivots(candles_4h)
    for idx, price in reversed(highs_4h):
        if len(closed_4h) - 1 - idx < STALE_4H_CANDLES:
            continue  # ainda recente demais -- tenta o proximo swing mais antigo
        if atr_1h and abs(last["close"] - price) <= 3 * ZONE_ATR_MULT * atr_1h:
            return {
                "setup": "B",
                "direction": "venda",
                "level": price,
                "zone_low": price - ZONE_ATR_MULT * atr_1h,
                "zone_high": price + ZONE_ATR_MULT * atr_1h,
                "candles_since_creation": 0,
                "touches": 0,
                "created_at": last["ts"],
            }
        break  # achou o swing maduro mais recente e nao esta perto -- para aqui
    for idx, price in reversed(lows_4h):
        if len(closed_4h) - 1 - idx < STALE_4H_CANDLES:
            continue
        if atr_1h and abs(last["close"] - price) <= 3 * ZONE_ATR_MULT * atr_1h:
            return {
                "setup": "B",
                "direction": "compra",
                "level": price,
                "zone_low": price - ZONE_ATR_MULT * atr_1h,
                "zone_high": price + ZONE_ATR_MULT * atr_1h,
                "candles_since_creation": 0,
                "touches": 0,
                "created_at": last["ts"],
            }
        break

    return None


def check_zone_confirmation(zone, candles_1h):
    """
    Verifica se o candle 1h mais recente fechado confirma a zona (rejeicao clara
    ou higher-low/lower-high), invalida (fechamento contra, alem do stop implicito)
    ou apenas "toca" sem confirmar (conta como 1 toque).
    Retorna: "confirmado" | "invalidado" | "tocou" | "sem_toque"
    """
    closed = [c for c in candles_1h if c["confirm"] == "1"]
    last = closed[-1]
    touched = zone["zone_low"] <= last["low"] <= zone["zone_high"] or \
              zone["zone_low"] <= last["high"] <= zone["zone_high"] or \
              (last["low"] <= zone["zone_low"] and last["high"] >= zone["zone_high"])

    if not touched:
        return "sem_toque"

    body = abs(last["close"] - last["open"])
    rang = max(last["high"] - last["low"], 1e-9)

    if zone["direction"] == "compra":
        rejection = (last["close"] - last["low"]) / rang >= 0.6 and last["close"] > last["open"]
        invalidated = last["close"] < zone["zone_low"]
    else:
        rejection = (last["high"] - last["close"]) / rang >= 0.6 and last["close"] < last["open"]
        invalidated = last["close"] > zone["zone_high"]

    if invalidated:
        return "invalidado"
    if rejection:
        return "confirmado"
    return "tocou"


# ---------------------------------------------------------------------------
# Notificacao gratuita via ntfy.sh (sem custo, sem API key -- so um "topic" secreto)
# ---------------------------------------------------------------------------

def send_ntfy(title, message, priority="default"):
    if not NTFY_TOPIC:
        print("[aviso] NTFY_TOPIC nao configurado -- pulando notificacao push.")
        return
    url = f"https://ntfy.sh/{NTFY_TOPIC}"
    req = urllib.request.Request(
        url,
        data=message.encode("utf-8"),
        headers={"Title": title.encode("utf-8"), "Priority": priority},
        method="POST",
    )
    try:
        urllib.request.urlopen(req, timeout=10)
    except urllib.error.URLError as e:
        print(f"[erro] Falha ao enviar notificacao ntfy: {e}")


# ---------------------------------------------------------------------------
# Escrita dos arquivos de log / status (mesmo formato do projeto)
# ---------------------------------------------------------------------------

def fmt_brt(ts_ms):
    return datetime.fromtimestamp(ts_ms / 1000, tz=BRT).strftime("%Y-%m-%d %H:%M")


def last_swing_ref_text(trend, candles_1h):
    """
    Texto curto descrevendo o ultimo swing 1h confirmado relevante para a
    tendencia atual (resistencia em alta, suporte em baixa) -- so para dar
    visibilidade no log ao que o script esta vigiando, mesmo em sem_zona.
    """
    highs_1h, lows_1h, closed_1h = find_confirmed_pivots(candles_1h)
    n = len(closed_1h)
    if trend == "alta" and highs_1h:
        idx, price = highs_1h[-1]
        return f"res {price:.1f} (ha {n - 1 - idx} candles)"
    if trend == "baixa" and lows_1h:
        idx, price = lows_1h[-1]
        return f"sup {price:.1f} (ha {n - 1 - idx} candles)"
    return "—"


def append_log_line(candles_1h, candles_4h, funding, status_text, trend, atr_1h):
    last_1h = last_closed(candles_1h)
    last_4h = last_closed(candles_4h)
    now_brt = datetime.now(BRT).strftime("%Y-%m-%d %H:%M")
    swing_ref = last_swing_ref_text(trend, candles_1h)
    atr_txt = f"{atr_1h:.1f}" if atr_1h else "—"

    header = (
        "# Log de Monitoramento Automatico -- BTC/USD (script gratuito, GitHub Actions)\n\n"
        "> Gerado por script Python sem LLM (ver monitor/fetch_and_check.py). Fonte: OKX "
        "(BTC-USDT-SWAP). Leitura e MECANICA (regras objetivas da secao 4 do plano), sem "
        "a prosa qualitativa que o Claude gerava -- cole este log numa conversa do Claude "
        "se quiser a leitura interpretativa.\n\n"
        "| Data/Hora (BRT) | Close 1h | High/Low 1h | Close 4h | Swing 1h ref | ATR 1h | Funding | Status checklist |\n"
        "|---|---|---|---|---|---|---|---|\n"
    )

    if not os.path.exists(LOG_PATH):
        os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
        with open(LOG_PATH, "w", encoding="utf-8") as f:
            f.write(header)

    line = (
        f"| {now_brt} | {last_1h['close']:.1f} | {last_1h['high']:.1f}/{last_1h['low']:.1f} | "
        f"{last_4h['close']:.1f} | {swing_ref} | {atr_txt} | {funding*100:.4f}% | {status_text} |\n"
    )
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(line)

    # arquivamento simples: mantem so as ultimas ~200 linhas de dados
    with open(LOG_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()
    data_lines = [l for l in lines if l.startswith("| 2")]
    if len(data_lines) > 200:
        head = [l for l in lines if not l.startswith("| 2")]
        with open(LOG_PATH, "w", encoding="utf-8") as f:
            f.writelines(head)
            f.writelines(data_lines[-200:])


def write_status(state, trend, candles_1h, candles_4h, funding, atr_1h):
    last_1h = last_closed(candles_1h)
    last_4h = last_closed(candles_4h)
    now_brt = datetime.now(BRT).strftime("%Y-%m-%d %H:%M")
    zone = state.get("zone")
    swing_ref = last_swing_ref_text(trend, candles_1h)
    atr_txt = f"{atr_1h:.1f}" if atr_1h else "—"

    zone_txt = "Nenhuma zona candidata mapeada no momento."
    if zone:
        zone_txt = (
            f"Setup {zone['setup']} ({zone['direction']}) -- nivel de referencia "
            f"{zone['level']:.1f}, zona {zone['zone_low']:.1f}-{zone['zone_high']:.1f}. "
            f"Toques: {zone['touches']}/{ZONE_MAX_TOUCHES}. "
            f"Candles desde criacao: {zone['candles_since_creation']}/{ZONE_MAX_CANDLES_1H}."
        )

    content = (
        f"# Situacao atual (script gratuito, sem LLM) -- atualizado {now_brt} BRT\n\n"
        f"> Gerado por `monitor/fetch_and_check.py` via GitHub Actions, sem chamar a API "
        f"do Claude. Registra fatos objetivos; a interpretacao qualitativa fica a seu "
        f"criterio (ou cole este arquivo + o log numa conversa do Claude).\n\n"
        f"**Par:** BTC-USDT-SWAP (OKX, proxy do BTC/USDT Perpetual da Binance).\n\n"
        f"**Tendencia 4h (geometrica, pivos fractais):** {trend}.\n\n"
        f"**Ultimo close 1h:** {last_1h['close']:.1f} (high {last_1h['high']:.1f} / low {last_1h['low']:.1f}) "
        f"| **Ultimo close 4h:** {last_4h['close']:.1f}\n\n"
        f"**Ultimo swing 1h confirmado (referencia de rompimento):** {swing_ref}\n\n"
        f"**ATR 1h:** {atr_txt}\n\n"
        f"**Funding rate atual:** {funding*100:.4f}%\n\n"
        f"**Zona / setup candidato:** {zone_txt}\n\n"
        f"**Status do checklist mecanico:** {state.get('status')}\n"
    )
    os.makedirs(os.path.dirname(STATUS_PATH), exist_ok=True)
    with open(STATUS_PATH, "w", encoding="utf-8") as f:
        f.write(content)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    candles_1h = fetch_candles("1H", limit=150)
    candles_4h = fetch_candles("4H", limit=100)
    funding = fetch_funding_rate()

    trend, _ = classify_trend_4h(candles_4h)
    atr_1h = atr(candles_1h)

    state = load_state()
    zone = state.get("zone")
    prev_status = state.get("status")
    new_status = prev_status
    notify_title = None
    notify_msg = None

    if zone is None:
        candidate = try_map_new_zone(trend, candles_1h, candles_4h, atr_1h)
        if candidate:
            state["zone"] = candidate
            new_status = f"zona_mapeada_setup_{candidate['setup']}"
            notify_title = f"Nova zona candidata -- Setup {candidate['setup']}"
            notify_msg = (
                f"Direcao: {candidate['direction']}\n"
                f"Nivel: {candidate['level']:.1f}\n"
                f"Zona: {candidate['zone_low']:.1f} - {candidate['zone_high']:.1f}\n"
                f"Tendencia 4h: {trend}\n"
                f"Cole este alerta + o log no Claude para leitura qualitativa."
            )
        else:
            new_status = "sem_zona"
    else:
        result = check_zone_confirmation(zone, candles_1h)
        if result == "confirmado":
            new_status = f"CONFIRMADO_setup_{zone['setup']}"
            notify_title = f"CONFIRMACAO -- Setup {zone['setup']} ({zone['direction']})"
            notify_msg = (
                f"Nivel: {zone['level']:.1f} | Zona: {zone['zone_low']:.1f}-{zone['zone_high']:.1f}\n"
                f"Verifique o checklist completo (secao 4 do plano) antes de contar como "
                f"trade #{'?'} da validacao -- este script so checa a parte mecanica."
            )
            state["zone"] = None  # zona consumida, exige nova leitura de contexto
        elif result == "invalidado":
            new_status = f"invalidado_setup_{zone['setup']}"
            notify_title = f"Setup {zone['setup']} invalidado"
            notify_msg = f"Fechamento contra a zona {zone['zone_low']:.1f}-{zone['zone_high']:.1f}."
            state["zone"] = None
        else:
            if result == "tocou":
                zone["touches"] += 1
            zone["candles_since_creation"] += 1
            if zone["touches"] >= ZONE_MAX_TOUCHES or zone["candles_since_creation"] >= ZONE_MAX_CANDLES_1H:
                new_status = f"zona_expirada_setup_{zone['setup']}"
                notify_title = f"Zona do Setup {zone['setup']} expirou"
                notify_msg = "Expirou por limite de toques ou de candles sem confirmacao -- releitura de contexto necessaria."
                state["zone"] = None
            else:
                new_status = prev_status  # sem mudanca -> sem notificacao
            state["zone"] = zone if state.get("zone") else None

    state["status"] = new_status
    save_state(state)

    append_log_line(candles_1h, candles_4h, funding, new_status, trend, atr_1h)
    write_status(state, trend, candles_1h, candles_4h, funding, atr_1h)

    if new_status != prev_status and notify_title:
        send_ntfy(notify_title, notify_msg, priority="high")
        print(f"[status mudou] {prev_status} -> {new_status} -- notificacao enviada.")
    else:
        print(f"[sem mudanca] status = {new_status}")


if __name__ == "__main__":
    main()
