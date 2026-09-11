#!/usr/bin/env python3
"""
Backtest de pesquisa pro Setup C (OB/FVG): compara duas fontes de deteccao de
zona sobre o MESMO harness de saida (stop/alvo/RR/desfecho identicos ao Setup
A/B em producao) -- so a deteccao da zona muda:

  A) "lib como esta": smc.ob + smc.fvg (smartmoneyconcepts), com
     swing_highs_lows dela mesma.
  B) "caseiro": mesma logica de OB (ultimo candle oposto antes do rompimento
     de estrutura) so que usando find_confirmed_pivots (PIVOT_WINDOW=3) do
     proprio projeto em vez do swing_highs_lows da lib -- isola exatamente a
     variavel que ja causou a divergencia conhecida em A/B (definicao de
     pivo/swing). FVG usa a mesma definicao matematica (nao ambigua), com
     filtro de tamanho minimo.

POR QUE ISTO EXISTE
--------------------
Ver claude/setup-c-gabarito.md: `smc.ob()`/`smc.fvg()` nao reproduziram os
exemplos do gabarito qualitativo (trades reais do OTS) nos parametros
default. Antes de descartar a lib de vez (como ja aconteceu com o pivo de
A/B) ou de adotar uma deteccao caseira sem checar, este harness testa as
DUAS abordagens sobre o mesmo backtest, nos 10 pares do projeto.

NAO mexe em nada do resto do repo -- so importa fetch_and_check.py como
biblioteca (mesma pratica do replay.py oficial de A/B). So leitura -- nenhum
resultado disto vira trade nem gate nem parametro em producao. Ver
claude/setup-c-testes.md para o relatorio consolidado.

Uso (da raiz do repo, com PYTHONPATH=monitor):
    PYTHONPATH=monitor python monitor/replay_setup_c.py
"""
import sys
from collections import defaultdict

import numpy as np
import pandas as pd

import fetch_and_check as m  # noqa: E402
from smartmoneyconcepts import smc  # noqa: E402

WINDOW = 200          # candles de contexto usados p/ detectar zona a cada passo
FRESH = 3             # zona so conta como "nova" se formada nos ultimos N candles da janela
MIN_GAP_ATR = 0.05    # filtro de tamanho minimo pra FVG caseira (ruido)

# Em producao, fetch_candles() so busca os ultimos 150 candles de 1h (ver
# fetch_and_check.py linha ~2388) -- nearest_target_candidate() NUNCA ve mais
# historico que isso ao vivo. No replay, janela_1h = c1h[:i+1] cresce sem
# limite a cada passo (11/09/2026: achado real, XRP 400 dias -- um candle de
# flash-crash de 10/2025, low=1.1573 num pavio de 1h com volume ~60x o normal,
# virou "pivo confirmado" e foi escolhido como alvo por estar "mais proximo em
# preco" que qualquer pivo de verdade, gerando RR de 22-40 em 3 trades
# distintos meses depois). Sem este limite, o replay mede um comportamento que
# a producao nunca teria.
ALVO_LOOKBACK = 150


def fetch_historico(inst_id, bar, paginas):
    todos = {}
    after = None
    for _ in range(paginas):
        params = {"instId": inst_id, "bar": bar, "limit": 100}
        if after:
            params["after"] = after
        raw = m.okx_get("/api/v5/market/history-candles", params)
        if not raw:
            break
        for row in raw:
            todos[int(row[0])] = {
                "ts": int(row[0]), "open": float(row[1]), "high": float(row[2]),
                "low": float(row[3]), "close": float(row[4]), "vol": float(row[5]),
                "confirm": row[8] if len(row) > 8 else row[-1],
            }
        after = str(min(int(r[0]) for r in raw))
    return [todos[k] for k in sorted(todos)]


def to_df(candles):
    df = pd.DataFrame(candles)
    df = df.rename(columns={"vol": "volume"})
    df.index = pd.to_datetime(df["ts"], unit="ms")
    return df.reset_index(drop=True)


# ---------------------------------------------------------------------------
# Deteccao A: lib como esta
# ---------------------------------------------------------------------------

def lib_zones_novas(window_candles):
    df = to_df(window_candles)
    shl = smc.swing_highs_lows(df, swing_length=10)
    ob = smc.ob(df, shl)
    fvg = smc.fvg(df)
    novas = []
    limite = len(df) - FRESH
    for idx in ob.index:
        if idx >= limite and pd.notna(ob.loc[idx, "OB"]):
            novas.append({
                "tipo": "OB", "direcao": "compra" if ob.loc[idx, "OB"] == 1 else "venda",
                "top": float(ob.loc[idx, "Top"]), "bottom": float(ob.loc[idx, "Bottom"]),
            })
    for idx in fvg.index:
        if idx >= limite and pd.notna(fvg.loc[idx, "FVG"]):
            novas.append({
                "tipo": "FVG", "direcao": "compra" if fvg.loc[idx, "FVG"] == 1 else "venda",
                "top": float(fvg.loc[idx, "Top"]), "bottom": float(fvg.loc[idx, "Bottom"]),
            })
    return novas


# ---------------------------------------------------------------------------
# Deteccao B: caseira -- OB via find_confirmed_pivots do proprio projeto,
# FVG com a mesma definicao matematica + filtro de tamanho minimo
# ---------------------------------------------------------------------------

def home_zones_novas(window_candles, atr_1h):
    closed = [c for c in window_candles if c["confirm"] == "1"]
    if len(closed) < m.PIVOT_WINDOW * 2 + 3:
        return []
    highs, lows, _ = m.find_confirmed_pivots(closed, window=m.PIVOT_WINDOW)
    n = len(closed)
    limite = n - FRESH
    novas = []

    # OB bullish: candle de fechamento cruza acima do topo do ultimo pivo de
    # alta confirmado -> OB = candle de menor low entre o pivo e o rompimento
    # (mesma ideia de smc.ob, trocando o swing dela pelo pivo ja validado aqui).
    for i in range(limite, n):
        if i < 1:
            continue
        pivos_antes = [p for p in highs if p[0] < i]
        if not pivos_antes:
            continue
        piv_idx, piv_val = pivos_antes[-1]
        if closed[i]["close"] > piv_val and piv_idx < i - 1:
            segmento = closed[piv_idx + 1:i]
            ob_candle = min(segmento, key=lambda c: c["low"])
            novas.append({"tipo": "OB", "direcao": "compra",
                          "top": ob_candle["high"], "bottom": ob_candle["low"]})
        elif closed[i]["close"] > piv_val and piv_idx == i - 1:
            ob_candle = closed[i - 1]
            novas.append({"tipo": "OB", "direcao": "compra",
                          "top": ob_candle["high"], "bottom": ob_candle["low"]})

    for i in range(limite, n):
        if i < 1:
            continue
        pivos_antes = [p for p in lows if p[0] < i]
        if not pivos_antes:
            continue
        piv_idx, piv_val = pivos_antes[-1]
        if closed[i]["close"] < piv_val and piv_idx < i - 1:
            segmento = closed[piv_idx + 1:i]
            ob_candle = max(segmento, key=lambda c: c["high"])
            novas.append({"tipo": "OB", "direcao": "venda",
                          "top": ob_candle["high"], "bottom": ob_candle["low"]})
        elif closed[i]["close"] < piv_val and piv_idx == i - 1:
            ob_candle = closed[i - 1]
            novas.append({"tipo": "OB", "direcao": "venda",
                          "top": ob_candle["high"], "bottom": ob_candle["low"]})

    # FVG: mesma definicao matematica do smc.fvg, com filtro de tamanho minimo
    if atr_1h:
        for i in range(max(1, limite), n - 1):
            if closed[i]["close"] > closed[i]["open"] and closed[i - 1]["high"] < closed[i + 1]["low"]:
                gap = closed[i + 1]["low"] - closed[i - 1]["high"]
                if gap >= MIN_GAP_ATR * atr_1h:
                    novas.append({"tipo": "FVG", "direcao": "compra",
                                  "top": closed[i + 1]["low"], "bottom": closed[i - 1]["high"]})
            if closed[i]["close"] < closed[i]["open"] and closed[i - 1]["low"] > closed[i + 1]["high"]:
                gap = closed[i - 1]["low"] - closed[i + 1]["high"]
                if gap >= MIN_GAP_ATR * atr_1h:
                    novas.append({"tipo": "FVG", "direcao": "venda",
                                  "top": closed[i - 1]["low"], "bottom": closed[i + 1]["high"]})
    return novas


# ---------------------------------------------------------------------------
# Harness comum: walk-forward, mitigacao, stop/alvo/RR/desfecho identicos a
# producao (fetch_and_check.py) -- so a fonte da zona muda entre A e B.
# ---------------------------------------------------------------------------

def replay_setup_c(c1h, c4h, detector):
    sinais = []
    pendentes = []  # zonas aguardando mitigacao
    vistas = set()
    minimo = m.ATR_PERIOD + m.PIVOT_WINDOW * 2 + 2 + WINDOW

    for i in range(minimo, len(c1h)):
        janela_1h = c1h[:i + 1]
        agora = janela_1h[-1]["ts"]
        janela_4h = [c for c in c4h if c["ts"] <= agora]
        if len(janela_4h) < m.PIVOT_WINDOW * 2 + 3:
            continue
        trend, _ = m.classify_trend_4h(janela_4h)
        atr_1h = m.atr(janela_1h)
        if atr_1h is None:
            continue

        contexto = janela_1h[-WINDOW:]
        if detector == "lib":
            novas = lib_zones_novas(contexto)
        else:
            novas = home_zones_novas(contexto, atr_1h)

        for z in novas:
            chave = (z["tipo"], z["direcao"], round(z["top"], 4), round(z["bottom"], 4))
            if chave in vistas:
                continue
            vistas.add(chave)
            # so aceita zona alinhada com a tendencia 4h (mesma regra de A/B)
            if (z["direcao"] == "compra" and trend == "baixa") or \
               (z["direcao"] == "venda" and trend == "alta"):
                continue
            pendentes.append({**z, "criado_ts": agora})

        preco = janela_1h[-1]
        ainda_pendentes = []
        for z in pendentes:
            tocou = z["bottom"] <= preco["high"] and z["top"] >= preco["low"]
            if not tocou:
                if agora - z["criado_ts"] > m.ZONE_MAX_CANDLES_1H * 3600_000:
                    continue  # expirou sem tocar
                ainda_pendentes.append(z)
                continue
            entrada = preco["close"]
            extremo = z["bottom"] if z["direcao"] == "compra" else z["top"]
            # stop_sug generico de A/B usa a convencao zone["direction"] deles
            # (venda = topo); para OB/FVG de compra o stop fica abaixo do
            # extremo, para venda fica acima -- por isso calculado direto aqui
            # em vez de reusar suggest_stop() sem adaptar.
            stop_s = extremo - m.STOP_BUFFER_ATR_MULT * atr_1h if z["direcao"] == "compra" \
                else extremo + m.STOP_BUFFER_ATR_MULT * atr_1h
            alvo = m.nearest_target_candidate(z["direcao"], janela_1h[-ALVO_LOOKBACK:], entrada, modo="proximo")
            rr = m._rr(entrada, stop_s, alvo)
            aceito = rr is not None and rr >= m.MIN_RR
            r, motivo, mae, mfe, n = m.desfecho_mecanico(
                z["direcao"], entrada, stop_s, alvo, rr, agora, c1h)
            sinais.append({
                "tipo": z["tipo"], "direcao": z["direcao"], "ts": agora,
                "entrada": entrada, "stop": stop_s, "alvo": alvo, "rr": rr,
                "aceito": aceito, "resultado": r, "mae": mae, "mfe": mfe,
            })
        pendentes = ainda_pendentes

    return sinais


def bootstrap_ci(valores, n_boot=5000, seed=42):
    if len(valores) < 3:
        return None
    rng = np.random.default_rng(seed)
    arr = np.array(valores)
    medias = [rng.choice(arr, size=len(arr), replace=True).mean() for _ in range(n_boot)]
    return np.percentile(medias, 2.5), np.percentile(medias, 97.5)


def resumir(sinais, rotulo):
    aceitos = [s for s in sinais if s["aceito"]]
    resolvidos = [s for s in aceitos if s["resultado"] is not None]
    print(f"\n{rotulo}")
    print(f"  {len(sinais)} zonas viraram sinal | {len(aceitos)} aceitos (RR>={m.MIN_RR}) "
          f"| {len(resolvidos)} resolvidos")
    if not resolvidos:
        return
    wins = [s for s in resolvidos if s["resultado"] > 0]
    soma = sum(s["resultado"] for s in resolvidos)
    exp = soma / len(resolvidos)
    ci = bootstrap_ci([s["resultado"] for s in resolvidos])
    ci_txt = f" | IC95% [{ci[0]:.3f}, {ci[1]:.3f}]" if ci else " | (amostra pequena p/ IC)"
    print(f"  {len(wins)} wins ({100*len(wins)/len(resolvidos):.1f}%) | "
          f"expectancia {exp:.3f}R{ci_txt}")


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--dias", type=int, default=90,
                     help="dias de historico a baixar (default 90, o original desta pesquisa)")
    args = ap.parse_args()
    paginas_1h = max(22, -(-(args.dias * 24) // 100))   # ceil(candles / 100)
    paginas_4h = max(16, -(-(args.dias * 6) // 100))

    pares = m.PAIRS
    print(f"Baixando historico de {len(pares)} pares (~{args.dias} dias, 1h + 4h)...")
    dados = {}
    for inst in pares:
        c1h = fetch_historico(inst, "1H", paginas=paginas_1h)
        c4h = fetch_historico(inst, "4H", paginas=paginas_4h)
        if len(c1h) < 300 or len(c4h) < 60:
            print(f"  [pula] {inst}: historico insuficiente ({len(c1h)}x1h, {len(c4h)}x4h)")
            continue
        dados[inst] = (c1h, c4h)
        print(f"  {m.pair_label(inst):<10} {len(c1h)} candles 1h, {len(c4h)} candles 4h")

    todos_lib, todos_home = [], []
    for inst, (c1h, c4h) in dados.items():
        s_lib = replay_setup_c(c1h, c4h, "lib")
        s_home = replay_setup_c(c1h, c4h, "home")
        for s in s_lib:
            s["par"] = m.pair_label(inst)
        for s in s_home:
            s["par"] = m.pair_label(inst)
        todos_lib += s_lib
        todos_home += s_home
        print(f"  [{m.pair_label(inst)}] lib: {len(s_lib)} zonas | home: {len(s_home)} zonas")

    resumir(todos_lib, "A) smartmoneyconcepts (swing_highs_lows + ob + fvg, default) -- agregado, 10 pares")
    resumir(todos_home, "B) caseiro (find_confirmed_pivots do projeto + fvg com filtro de tamanho) -- agregado, 10 pares")

    print("\n\n=== Por par ===")
    por_par_lib = defaultdict(list)
    por_par_home = defaultdict(list)
    for s in todos_lib:
        por_par_lib[s["par"]].append(s)
    for s in todos_home:
        por_par_home[s["par"]].append(s)

    print("\n-- A) lib --")
    for par in sorted(por_par_lib):
        resumir(por_par_lib[par], par)
    print("\n-- B) caseiro --")
    for par in sorted(por_par_home):
        resumir(por_par_home[par], par)
