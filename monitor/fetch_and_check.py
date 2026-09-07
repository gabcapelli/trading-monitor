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
CHANGELOG v2 (07/09/2026 -- generalizacao multi-par):

Decisao de escopo (07/09/2026): expandir de BTC-USDT-SWAP unico para os 10
pares definidos em PAIRS abaixo. Os 30 trades de validacao (secao 3.4 do
plano) continuam contados de forma AGREGADA entre todos os pares (nao
separado por par). Limite de posicoes simultaneas (secao 3.3) revisado para
ATE 2 (era 1), ainda GLOBAL entre os 10 pares (nao por par).

1. LOGICA DE ZONA (try_map_new_zone, check_zone_confirmation, find_confirmed_
   pivots, classify_trend_4h) NAO MUDOU -- essas funcoes ja eram agnosticas
   ao par (recebem candles como parametro, nunca leem INST_ID global), entao
   os testes de regressao em tests/test_zone_logic.py continuam validos sem
   nenhuma alteracao. So as funcoes de fetch/estado/log precisaram mudar.

2. FETCH (okx_get, fetch_candles, fetch_funding_rate): fetch_candles e
   fetch_funding_rate passam a receber `inst_id` como parametro em vez de
   usar o global INST_ID (removido). O loop principal chama essas funcoes
   uma vez por par a cada execucao (10 pares x 3 chamadas = 30 requests/
   execucao -- folgado dentro do rate limit publico da OKX).

3. ESTADO (monitor/state.json): schema mudou de single-object
   ({status, zone, last_1h_ts}) para {"posicoes_abertas": [...],
   "pares": {inst_id: {status, zone, last_1h_ts}}}. MIGRACAO AUTOMATICA e
   TRANSPARENTE do schema antigo na primeira execucao desta versao (ver
   load_state()) -- a zona ja mapeada para BTC (Setup B, ativa no momento
   desta mudanca) e preservada, so realocada para dentro de
   pares["BTC-USDT-SWAP"].

4. LOG (claude/log-monitoramento-btc-auto.md): ganhou a coluna "Par" (logo
   apos a data). Linhas do formato antigo (sem essa coluna) sao migradas
   automaticamente no primeiro run desta versao (ver
   migrate_log_header_if_needed()), preenchendo "BTC-USDT-SWAP" retroativamente
   -- unico par que existia antes desta mudanca. O limite de retencao subiu
   de ~200 para LOG_MAX_LINES linhas, ja que cada execucao agora grava ate 10
   linhas (1 por par) em vez de 1.

5. STATUS (claude/status-simulacao.md): passou de "estado de 1 par" para uma
   tabela resumida dos 10 pares por execucao (write_status reescrita).

6. LIMITE DE POSICOES SIMULTANEAS -- DECISAO DE DESIGN IMPORTANTE: o script
   NAO bloqueia mapeamento nem confirmacao de zona em nenhum par por causa do
   limite de 2 posicoes simultaneas. Isso e deliberado, na mesma linha da
   separacao ja documentada no topo deste arquivo ("automacao so cuida do
   mecanico; risco/execucao ficam manuais"): o script nunca abre uma posicao
   sozinho, so registra candidatos em claude/trade_journal.db com
   status='candidato'. Em vez de travar a deteccao, o script CALCULA quantas
   posicoes estao com status='entrado' e ainda sem resultado_r preenchido
   (count_open_positions()) e expoe esse numero no status e na notificacao de
   confirmacao -- para voce decidir, com essa informacao na mao, se abre ou
   nao mais uma posicao. Se preferir um bloqueio automatico de verdade (o
   script se recusar a mapear zona nova quando ja houver 2 'entrado' sem
   resultado), isso e uma mudanca pequena e localizada em process_single_pair()
   -- fica registrado aqui como opcao nao implementada por padrao.

7. NOTIFICACAO: passou a ser enviada em UMA UNICA chamada por execucao
   (send_batched_notifications), mesmo se varios pares mudarem de status no
   mesmo ciclo -- evita ate 10 pushes separados no mesmo horario.

8. ROBUSTEZ: o loop principal agora captura erro de fetch por par
   individualmente (um par com falha de API nao derruba a execucao inteira
   nem impede os outros 9 de serem processados neste ciclo).

--------------------------------------------------------------------------------
CHANGELOG v1 (correcoes desta versao, 07/09/2026):

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

4. DIARIO DE TRADE EM SQLITE (claude/trade_journal.db), substituindo a
   transcricao manual dos campos mecanicos na tabela markdown da secao 5 do
   plano:
   - Quando uma zona e CONFIRMADA (resultado "confirmado" em
     check_zone_confirmation), o script insere uma linha com status
     'candidato' e os campos mecanicos ja calculados (setup, direcao, zona,
     nivel de referencia, tendencia 4h). Stop/alvo/R:R/alavancagem NAO sao
     calculados automaticamente -- isso continua exigindo julgamento (o alvo,
     por exemplo, e "proxima zona relevante", que nao e mecanico) e fica em
     branco ate voce (ou uma sessao do Claude) decidir e preencher.
   - status muda para 'entrado' ou 'descartado' manualmente, depois do
     checklist completo da secao 4 (que inclui itens nao automatizaveis,
     como estado emocional). So trades com status='entrado' E
     conta_para_validacao=1 entram na estatistica da secao 3.5.
   - O banco e versionado no mesmo repo (commit a cada execucao que
     insere linha nova), mesmo padrao do monitor/state.json.

NOTA sobre a biblioteca smartmoneyconcepts (avaliada e descartada para a
deteccao de pivo/zona nesta versao): testada contra dado sintetico e
encontrada uma divergencia real (fora de casos de borda) na definicao de
swing high/low em relacao a regra estrita ja usada aqui (maximo/minimo dentro
de uma janela de +-3 candles) -- a lib parece usar um algoritmo sequencial
tipo zigue-zague, nao reavaliacao estrita por janela. Trocar a deteccao de
pivo por essa lib mudaria quais zonas de Setup A/B sao geradas, invalidando
a aplicabilidade do backtest ja rodado (claude/backtest-setup-ab.md) sem
re-rodar tudo. Os dois bugs reais (#1 e #2 abaixo) nao tinham relacao com a
qualidade da deteccao de pivo em si -- eram erro de indice/lista, corrigido
sem trocar a definicao de zona. Ver tests/test_zone_logic.py para testes que
travam essa classe de bug daqui pra frente.
--------------------------------------------------------------------------------
"""

import json
import os
import sqlite3
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta

# ---------------------------------------------------------------------------
# Configuracao
# ---------------------------------------------------------------------------

OKX_BASE = "https://www.okx.com"

# Pares decididos na expansao de 07/09/2026 (liquidez OKX + precedente nos 56
# prints catalogados + historico de preco longo o suficiente para leitura
# estrutural). BTC-USDT-SWAP e o par original, mantido primeiro na lista.
PAIRS = [
    "BTC-USDT-SWAP",
    "ETH-USDT-SWAP",
    "SOL-USDT-SWAP",
    "XRP-USDT-SWAP",
    "DOGE-USDT-SWAP",
    "ARB-USDT-SWAP",
    "WLD-USDT-SWAP",
    "SUI-USDT-SWAP",
    "UNI-USDT-SWAP",
    "LINK-USDT-SWAP",
]

# Limite de posicoes simultaneas (secao 3.3 do plano, revisado em 07/09/2026
# de 1 para 2) -- GLOBAL entre os 10 pares, nao por par. Ver CHANGELOG v2,
# item 6, para como esse numero e usado (informativo, nao bloqueia deteccao).
MAX_POSICOES_SIMULTANEAS = 2

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
TRADE_DB_PATH = os.path.join("claude", "trade_journal.db")

# Retencao do log: cada execucao agora grava ate len(PAIRS) linhas (1 por
# par), contra 1 antes -- subiu proporcionalmente de ~200 para manter uma
# janela de historico comparavel (~2 dias com 10 pares horarios).
LOG_MAX_LINES = 480

NTFY_TOPIC = os.environ.get("NTFY_TOPIC", "").strip()  # definido via GitHub secret


def pair_label(inst_id):
    """'ETH-USDT-SWAP' -> 'ETH/USDT' -- rotulo curto para log/status/diario."""
    return inst_id.replace("-USDT-SWAP", "/USDT")


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


def fetch_candles(inst_id, bar, limit=150):
    """
    Retorna lista de candles mais RECENTE -> MAIS ANTIGO (como a OKX devolve),
    cada um: [ts_ms, open, high, low, close, vol, volCcyQuote, confirm]
    Reordena para MAIS ANTIGO -> MAIS RECENTE (mais facil de processar em sequencia).
    """
    raw = okx_get("/api/v5/market/candles", {"instId": inst_id, "bar": bar, "limit": limit})
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


def fetch_funding_rate(inst_id):
    data = okx_get("/api/v5/public/funding-rate", {"instId": inst_id})
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

def default_pair_state():
    return {"status": "sem_zona", "zone": None, "last_1h_ts": None}


def load_state():
    """
    Schema atual: {"posicoes_abertas": [...], "pares": {inst_id: {status, zone,
    last_1h_ts}}}. Migra automaticamente e sem perda de dado o schema antigo
    (single-pair, sempre BTC): {"status", "zone", "last_1h_ts"} direto na raiz
    -- ver CHANGELOG v2, item 3.
    """
    if not os.path.exists(STATE_PATH):
        return {"posicoes_abertas": [], "pares": {p: default_pair_state() for p in PAIRS}}

    with open(STATE_PATH, "r", encoding="utf-8") as f:
        raw = json.load(f)

    if "pares" not in raw:
        raw = {
            "posicoes_abertas": [],
            "pares": {
                "BTC-USDT-SWAP": {
                    "status": raw.get("status", "sem_zona"),
                    "zone": raw.get("zone"),
                    "last_1h_ts": raw.get("last_1h_ts"),
                }
            },
        }
        print("[migracao] state.json antigo (single-pair) migrado para o schema multi-par "
              "-- zona em andamento, se houver, foi preservada em pares['BTC-USDT-SWAP'].")

    # garante entrada para todo par da lista atual (cobre par novo adicionado depois)
    for p in PAIRS:
        raw["pares"].setdefault(p, default_pair_state())
    raw.setdefault("posicoes_abertas", [])
    return raw


def save_state(state):
    os.makedirs(os.path.dirname(STATE_PATH), exist_ok=True)
    with open(STATE_PATH, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


# ---------------------------------------------------------------------------
# Diario de trade em SQLite (claude/trade_journal.db)
#
# Substitui a transcricao manual dos campos mecanicos na tabela markdown da
# secao 5 do plano. Colunas de decisao (checklist_ok, conta_para_validacao,
# stop/alvo/alavancagem finais, resultado) ficam em branco ate voce (ou uma
# sessao do Claude) revisar o candidato e preencher -- o script nunca marca
# um trade como 'entrado' sozinho.
# ---------------------------------------------------------------------------

def ensure_trade_db():
    os.makedirs(os.path.dirname(TRADE_DB_PATH), exist_ok=True)
    conn = sqlite3.connect(TRADE_DB_PATH)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS trades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            status TEXT NOT NULL DEFAULT 'candidato'
                CHECK(status IN ('candidato', 'entrado', 'descartado')),
            data TEXT NOT NULL,
            par TEXT NOT NULL DEFAULT 'BTC/USDT Perpetual (Binance)',
            setup TEXT NOT NULL CHECK(setup IN ('A', 'B')),
            direcao TEXT,
            nivel_referencia REAL,
            zona_entrada TEXT,
            confirmacao TEXT,
            tendencia_4h TEXT,
            stop REAL,
            alvo REAL,
            rr_planejado REAL,
            alavancagem REAL,
            checklist_ok INTEGER,
            conta_para_validacao INTEGER NOT NULL DEFAULT 0,
            resultado_r REAL,
            mae_r REAL,
            mfe_r REAL,
            rr_realizado REAL,
            motivo_resultado TEXT,
            observacoes TEXT,
            criado_em TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()


def insert_candidate_trade(inst_id, zone, trend):
    """
    Insere uma linha 'candidato' quando uma zona e CONFIRMADA (rejeicao
    valida no candle 1h). So os campos mecanicos vem preenchidos -- stop,
    alvo, R:R e alavancagem exigem julgamento (ex.: "proxima zona relevante"
    nao e mecanico) e ficam em branco ate a decisao real.
    """
    ensure_trade_db()
    now_brt = datetime.now(BRT).strftime("%Y-%m-%d %H:%M")
    conn = sqlite3.connect(TRADE_DB_PATH)
    conn.execute(
        """
        INSERT INTO trades
            (status, data, par, setup, direcao, nivel_referencia, zona_entrada,
             confirmacao, tendencia_4h, criado_em)
        VALUES ('candidato', ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            now_brt,
            pair_label(inst_id),
            zone["setup"],
            zone["direction"],
            zone["level"],
            f"{zone['zone_low']:.1f}-{zone['zone_high']:.1f}",
            "Rejeicao confirmada no candle 1h mais recente "
            f"(nivel de referencia {zone['level']:.1f})",
            trend,
            now_brt,
        ),
    )
    conn.commit()
    conn.close()


def count_open_positions():
    """
    Numero de trades com status='entrado' e ainda sem resultado_r preenchido
    -- proxy de "posicao aberta agora" a partir do proprio diario (nao exige
    campo extra no state.json). Ver CHANGELOG v2, item 6: usado so para
    informar, nunca para bloquear a deteccao de zona.
    """
    if not os.path.exists(TRADE_DB_PATH):
        return 0
    conn = sqlite3.connect(TRADE_DB_PATH)
    try:
        cur = conn.execute(
            "SELECT COUNT(*) FROM trades WHERE status='entrado' AND resultado_r IS NULL"
        )
        return cur.fetchone()[0]
    finally:
        conn.close()


def open_positions_detail():
    """Lista os pares (rotulo) com posicao 'entrado' e ainda sem resultado registrado."""
    if not os.path.exists(TRADE_DB_PATH):
        return []
    conn = sqlite3.connect(TRADE_DB_PATH)
    try:
        cur = conn.execute(
            "SELECT par FROM trades WHERE status='entrado' AND resultado_r IS NULL"
        )
        return [row[0] for row in cur.fetchall()]
    finally:
        conn.close()


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
    # CORRIGIDO (07/09, 1a rodada): o `break` estava fora do `if` de maturidade,
    # entao o loop sempre parava no primeiro swing (mesmo imaturo).
    # CORRIGIDO (07/09, 2a rodada -- pego pelo teste automatizado, nao por
    # inspecao manual): mesmo depois do primeiro fix, um `break` sobrava apos
    # o `if` de distancia -- entao o loop ainda desistia no primeiro swing
    # MADURO que encontrasse, mesmo se ele estivesse longe do preco, sem
    # chegar a um swing mais antigo que pudesse estar maduro E perto. Ambos
    # os `break` foram removidos: agora o loop percorre todos os swings
    # maduros (do mais recente ao mais antigo) ate achar um dentro da
    # distancia, ou esgotar a lista.
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
        # maduro mas longe -- nao retorna nem para; tenta o proximo mais antigo
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
# Logica por par (extraida do antigo main() single-pair para ser reutilizada
# em loop, uma vez por par -- ver CHANGELOG v2)
# ---------------------------------------------------------------------------

def process_single_pair(inst_id, pair_state, candles_1h, candles_4h, trend, atr_1h):
    """
    Roda a logica mecanica (mapear zona nova, ou checar confirmacao/invalidacao/
    expiracao de uma zona existente) para UM par, a partir do estado anterior
    desse par. Muta e retorna pair_state; retorna tambem um dict de evento
    (titulo + mensagem) se o status mudou neste ciclo, ou None se nao mudou
    (== sem notificacao para este par).
    """
    zone = pair_state.get("zone")
    prev_status = pair_state.get("status")
    new_status = prev_status
    evento = None

    if zone is None:
        candidate = try_map_new_zone(trend, candles_1h, candles_4h, atr_1h)
        if candidate:
            pair_state["zone"] = candidate
            new_status = f"zona_mapeada_setup_{candidate['setup']}"
            evento = {
                "titulo": f"{pair_label(inst_id)} -- Nova zona candidata -- Setup {candidate['setup']}",
                "mensagem": (
                    f"Direcao: {candidate['direction']}\n"
                    f"Nivel: {candidate['level']:.1f}\n"
                    f"Zona: {candidate['zone_low']:.1f} - {candidate['zone_high']:.1f}\n"
                    f"Tendencia 4h: {trend}\n"
                    f"Cole este alerta + o log no Claude para leitura qualitativa."
                ),
            }
        else:
            new_status = "sem_zona"
    else:
        result = check_zone_confirmation(zone, candles_1h)
        if result == "confirmado":
            new_status = f"CONFIRMADO_setup_{zone['setup']}"
            insert_candidate_trade(inst_id, zone, trend)
            abertas = count_open_positions()
            evento = {
                "titulo": f"{pair_label(inst_id)} -- CONFIRMACAO -- Setup {zone['setup']} ({zone['direction']})",
                "mensagem": (
                    f"Nivel: {zone['level']:.1f} | Zona: {zone['zone_low']:.1f}-{zone['zone_high']:.1f}\n"
                    f"Candidato salvo em claude/trade_journal.db (status='candidato').\n"
                    f"Posicoes abertas no diario agora: {abertas}/{MAX_POSICOES_SIMULTANEAS} "
                    f"-- confira o limite da secao 3.3 antes de decidir entrar.\n"
                    f"Verifique o checklist completo (secao 4 do plano), calcule stop/alvo/R:R "
                    f"e atualize o status para 'entrado' ou 'descartado' antes de contar como "
                    f"trade da validacao -- este script so checa a parte mecanica."
                ),
            }
            pair_state["zone"] = None
        elif result == "invalidado":
            new_status = f"invalidado_setup_{zone['setup']}"
            evento = {
                "titulo": f"{pair_label(inst_id)} -- Setup {zone['setup']} invalidado",
                "mensagem": f"Fechamento contra a zona {zone['zone_low']:.1f}-{zone['zone_high']:.1f}.",
            }
            pair_state["zone"] = None
        else:
            if result == "tocou":
                zone["touches"] += 1
            zone["candles_since_creation"] += 1
            if zone["touches"] >= ZONE_MAX_TOUCHES or zone["candles_since_creation"] >= ZONE_MAX_CANDLES_1H:
                new_status = f"zona_expirada_setup_{zone['setup']}"
                evento = {
                    "titulo": f"{pair_label(inst_id)} -- Zona do Setup {zone['setup']} expirou",
                    "mensagem": "Expirou por limite de toques ou de candles sem confirmacao -- releitura de contexto necessaria.",
                }
                pair_state["zone"] = None
            else:
                new_status = prev_status  # sem mudanca -> sem notificacao

    pair_state["status"] = new_status
    return pair_state, (evento if new_status != prev_status else None)


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


def send_batched_notifications(eventos):
    """
    Envia UMA chamada ao ntfy por execucao, mesmo com varios pares mudando de
    status no mesmo ciclo -- evita ate len(PAIRS) pushes separados na mesma hora.
    """
    if not eventos:
        return
    if len(eventos) == 1:
        send_ntfy(eventos[0]["titulo"], eventos[0]["mensagem"], priority="high")
        return
    titulo = f"{len(eventos)} mudancas de status neste ciclo"
    corpo = "\n\n".join(f"### {ev['titulo']}\n{ev['mensagem']}" for ev in eventos)
    send_ntfy(titulo, corpo, priority="high")


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


LOG_HEADER = (
    "# Log de Monitoramento Automatico -- Multi-Par (script gratuito, GitHub Actions)\n\n"
    "> Gerado por script Python sem LLM (ver monitor/fetch_and_check.py). Fonte: OKX. "
    "Cobre os pares em PAIRS (configuracao no topo do script) -- BTC-USDT-SWAP e os demais "
    "adicionados na expansao de 07/09/2026. Leitura e MECANICA (regras objetivas da secao 4 "
    "do plano), sem a prosa qualitativa que o Claude gerava -- cole este log numa conversa "
    "do Claude se quiser a leitura interpretativa.\n\n"
    "| Data/Hora (BRT) | Par | Close 1h | High/Low 1h | Close 4h | Swing 1h ref | ATR 1h | Funding | Status checklist |\n"
    "|---|---|---|---|---|---|---|---|---|\n"
)


def migrate_log_header_if_needed():
    """
    Se o log existir no formato antigo (sem a coluna 'Par', de antes da
    expansao multi-par de 07/09/2026), reescreve o header e insere
    'BTC-USDT-SWAP' como Par em cada linha de dado ja existente -- unico par
    que existia antes desta versao. Preserva o historico em vez de descarta-lo.
    Idempotente: nao faz nada se o log ja estiver no formato novo.
    """
    if not os.path.exists(LOG_PATH):
        return
    with open(LOG_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    already_migrated = any(l.startswith("| Data/Hora (BRT) | Par |") for l in lines)
    if already_migrated:
        return

    data_lines = [l for l in lines if l.startswith("| 2")]
    migrated = []
    for l in data_lines:
        parts = l.split("|")
        if len(parts) < 3:
            migrated.append(l)  # linha inesperada -- preserva como esta em vez de arriscar corromper
            continue
        new_parts = parts[:2] + [" BTC-USDT-SWAP "] + parts[2:]
        migrated.append("|".join(new_parts))

    with open(LOG_PATH, "w", encoding="utf-8") as f:
        f.write(LOG_HEADER)
        f.writelines(migrated)
    print(f"[migracao] {len(migrated)} linha(s) do log migrada(s) para o formato com coluna 'Par'.")


def append_log_line(inst_id, candles_1h, candles_4h, funding, status_text, trend, atr_1h):
    last_1h = last_closed(candles_1h)
    last_4h = last_closed(candles_4h)
    now_brt = datetime.now(BRT).strftime("%Y-%m-%d %H:%M")
    swing_ref = last_swing_ref_text(trend, candles_1h)
    atr_txt = f"{atr_1h:.1f}" if atr_1h else "—"

    if not os.path.exists(LOG_PATH):
        os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
        with open(LOG_PATH, "w", encoding="utf-8") as f:
            f.write(LOG_HEADER)

    line = (
        f"| {now_brt} | {inst_id} | {last_1h['close']:.1f} | {last_1h['high']:.1f}/{last_1h['low']:.1f} | "
        f"{last_4h['close']:.1f} | {swing_ref} | {atr_txt} | {funding*100:.4f}% | {status_text} |\n"
    )
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(line)


def archive_log_if_needed(max_lines=LOG_MAX_LINES):
    """
    Arquivamento simples: mantem so as ultimas `max_lines` linhas de dados.
    Chamada UMA VEZ por execucao (nao por par) -- ver CHANGELOG v2, evita
    reler/reescrever o arquivo len(PAIRS) vezes no mesmo ciclo.
    """
    if not os.path.exists(LOG_PATH):
        return
    with open(LOG_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()
    data_lines = [l for l in lines if l.startswith("| 2")]
    if len(data_lines) > max_lines:
        head = [l for l in lines if not l.startswith("| 2")]
        with open(LOG_PATH, "w", encoding="utf-8") as f:
            f.writelines(head)
            f.writelines(data_lines[-max_lines:])


def write_status(state, per_pair_data):
    """
    per_pair_data: dict inst_id -> {"trend", "last_1h", "last_4h", "funding", "atr_1h"}
    para os pares processados com sucesso neste ciclo (pares que falharam no
    fetch nao aparecem -- ver comentario no loop principal).
    """
    now_brt = datetime.now(BRT).strftime("%Y-%m-%d %H:%M")
    abertas = count_open_positions()
    detalhe_abertas = open_positions_detail()

    linhas = []
    for inst_id in PAIRS:
        d = per_pair_data.get(inst_id)
        pair_state = state["pares"][inst_id]
        if d is None:
            linhas.append(f"| {pair_label(inst_id)} | — | — | — | — | falha_fetch_neste_ciclo |")
            continue

        zone = pair_state.get("zone")
        if zone:
            zona_txt = (
                f"Setup {zone['setup']} ({zone['direction']}) "
                f"{zone['zone_low']:.1f}-{zone['zone_high']:.1f} "
                f"({zone['touches']}/{ZONE_MAX_TOUCHES} toques, "
                f"{zone['candles_since_creation']}/{ZONE_MAX_CANDLES_1H} candles)"
            )
        else:
            zona_txt = "—"

        linhas.append(
            f"| {pair_label(inst_id)} | {d['trend']} | {d['last_1h']['close']:.1f} | "
            f"{d['funding']*100:.4f}% | {zona_txt} | {pair_state['status']} |"
        )

    detalhe_txt = f" -- {', '.join(detalhe_abertas)}" if detalhe_abertas else ""

    content = (
        f"# Situacao atual -- Multi-Par (script gratuito, sem LLM) -- atualizado {now_brt} BRT\n\n"
        f"> Gerado por `monitor/fetch_and_check.py` via GitHub Actions, sem chamar a API "
        f"do Claude. Registra fatos objetivos; a interpretacao qualitativa fica a seu "
        f"criterio (ou cole este arquivo + o log numa conversa do Claude).\n\n"
        f"**Posicoes abertas (diario, status='entrado' sem resultado ainda):** "
        f"{abertas}/{MAX_POSICOES_SIMULTANEAS}{detalhe_txt}\n\n"
        f"| Par | Tendencia 4h | Close 1h | Funding | Zona / setup candidato | Status |\n"
        f"|---|---|---|---|---|---|\n"
        + "\n".join(linhas) + "\n"
    )
    os.makedirs(os.path.dirname(STATUS_PATH), exist_ok=True)
    with open(STATUS_PATH, "w", encoding="utf-8") as f:
        f.write(content)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    # Garante que claude/trade_journal.db exista desde a PRIMEIRA execucao,
    # mesmo sem nenhuma zona confirmada ainda -- senao o `git add` do workflow
    # falha com "pathspec did not match any files" toda vez que nenhum par
    # confirmar (a maioria das execucoes). O arquivo criado aqui e so o
    # schema vazio; insert_candidate_trade() so roda quando ha de fato uma
    # confirmacao, em qualquer par.
    ensure_trade_db()
    migrate_log_header_if_needed()

    state = load_state()
    eventos = []
    per_pair_data = {}

    for inst_id in PAIRS:
        try:
            candles_1h = fetch_candles(inst_id, "1H", limit=150)
            candles_4h = fetch_candles(inst_id, "4H", limit=100)
            funding = fetch_funding_rate(inst_id)
        except (RuntimeError, urllib.error.URLError, TimeoutError) as e:
            # um par com falha de API nao derruba a execucao inteira nem
            # impede os outros 9 de serem processados neste ciclo -- so fica
            # sem atualizacao (log/status) ate o proximo run.
            print(f"[erro] Falha ao buscar dados de {inst_id}: {e} -- pulando este par neste ciclo.")
            continue

        trend, _ = classify_trend_4h(candles_4h)
        atr_1h = atr(candles_1h)

        pair_state, evento = process_single_pair(
            inst_id, state["pares"][inst_id], candles_1h, candles_4h, trend, atr_1h
        )
        state["pares"][inst_id] = pair_state
        if evento:
            eventos.append(evento)

        append_log_line(inst_id, candles_1h, candles_4h, funding, pair_state["status"], trend, atr_1h)
        per_pair_data[inst_id] = {
            "trend": trend,
            "last_1h": last_closed(candles_1h),
            "last_4h": last_closed(candles_4h),
            "funding": funding,
            "atr_1h": atr_1h,
        }
        print(f"[{inst_id}] status = {pair_state['status']}" + (" (MUDOU)" if evento else ""))

    archive_log_if_needed()
    save_state(state)
    write_status(state, per_pair_data)
    send_batched_notifications(eventos)

    if eventos:
        print(f"[resumo] {len(eventos)} mudanca(s) de status neste ciclo -- notificacao enviada.")
    else:
        print("[resumo] nenhuma mudanca de status neste ciclo.")


if __name__ == "__main__":
    main()
