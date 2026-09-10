#!/usr/bin/env python3
"""
Harness de replay: roda a logica de deteccao inteira sobre historico de candles
e varre parametros, sem esperar acumular trade novo (CHANGELOG v5, item 12).

POR QUE ISTO EXISTE
-------------------
Com ~17 trades resolvidos nao da pra calibrar nada: 2 vitorias em 17 nao
distinguem estatisticamente este sistema de um que so empata (P(<=2 vitorias |
n=17, breakeven) = 0.069). Recalibrar STOP_BUFFER_ATR_MULT ou ZONE_ATR_MULT
com essa amostra e ajustar a duas vitorias.

A saida nao e esperar 100 trades ao vivo -- e rodar a MESMA logica sobre muito
mais historico. As funcoes de deteccao (find_confirmed_pivots, classify_trend_
4h, try_map_new_zone, check_zone_confirmation, compute_suggestion) ja sao puras
e recebem candles como parametro, entao isso e possivel sem reescrever nada.

O QUE ELE NAO E
---------------
Nao substitui o backtest historico do plano (claude/backtest-setup-ab.md, que
vive em outro Projeto). E uma reproducao do que ESTE SCRIPT faz, para medir o
efeito de mexer nos parametros dele -- inclusive pra re-rodar tudo caso um dia
PIVOT_WINDOW mude, que e o risco que o CLAUDE.md levanta ao justificar o
descarte da lib smartmoneyconcepts.

LIMITE CONHECIDO
----------------
ponytail: o funding rate nao entra no replay (a OKX so devolve o valor atual, e
o historico exigiria outro endpoint paginado). Como nenhuma regra atual do
checklist mecanico usa funding pra decidir, isso nao afeta o resultado hoje --
se algum dia virar filtro, este harness precisa buscar o historico primeiro.

Uso:
    python monitor/replay.py                          # parametros atuais, todos os pares
    python monitor/replay.py --pares BTC,ETH          # subconjunto
    python monitor/replay.py --varrer stop_buffer     # varredura de um parametro
    python monitor/replay.py --varrer alvo            # regra de alvo: recente vs proximo
    python monitor/replay.py --varrer min_rr          # varredura de MIN_RR
    python monitor/replay.py --varrer breakeven       # stop no zero a zero apos X de R
                                                        # a favor -- SO TESTE (v6); nada
                                                        # disso esta implementado em
                                                        # producao ate ter dado que sustente.
"""

import sys
from collections import defaultdict

import fetch_and_check as m


# ---------------------------------------------------------------------------
# Fetch de historico (paginado -- /market/candles so devolve os 300 mais
# recentes; history-candles pagina para tras com `after`)
# ---------------------------------------------------------------------------

def fetch_historico(inst_id, bar, paginas=8, por_pagina=100):
    """
    Junta varias paginas de candles, do mais antigo pro mais recente.
    8 x 100 candles de 1h ~= 33 dias. Aumente `paginas` para ir mais fundo.
    """
    todos = {}
    after = None
    for _ in range(paginas):
        params = {"instId": inst_id, "bar": bar, "limit": por_pagina}
        if after:
            params["after"] = after
        try:
            raw = m.okx_get("/api/v5/market/history-candles", params)
        except Exception as e:
            print(f"  [aviso] {inst_id}: parou de paginar ({e})")
            break
        if not raw:
            break
        for row in raw:
            todos[int(row[0])] = {
                "ts": int(row[0]), "open": float(row[1]), "high": float(row[2]),
                "low": float(row[3]), "close": float(row[4]), "vol": float(row[5]),
                "volCcyQuote": float(row[7]) if len(row) > 7 else float(row[6]),
                "confirm": row[8] if len(row) > 8 else row[-1],
            }
        after = str(min(int(r[0]) for r in raw))
    return [todos[k] for k in sorted(todos)]


# ---------------------------------------------------------------------------
# Replay
# ---------------------------------------------------------------------------

def replay_par(inst_id, c1h, c4h, modo_alvo=None, min_rr=None,
               stop_buffer=None, breakeven_apos_r=None):
    """
    Reproduz ciclo a ciclo o que o monitor faria, um candle de 1h por vez, e
    devolve a lista de sinais confirmados com o desfecho mecanico de cada um.

    Usa exatamente as mesmas funcoes do monitor -- se a logica mudar, o replay
    muda junto, que e o ponto.
    """
    min_rr = m.MIN_RR if min_rr is None else min_rr
    # v6: sem modo_alvo explicito, testa a regra AUTORITATIVA de producao
    # (m.ALVO_REGRA_ATUAL), nao mais um default fixo -- se a regra em vigor
    # mudar de novo, o replay padrao acompanha sem precisar editar aqui.
    modo_alvo = m.ALVO_REGRA_ATUAL if modo_alvo is None else modo_alvo
    buffer_orig = m.STOP_BUFFER_ATR_MULT
    if stop_buffer is not None:
        m.STOP_BUFFER_ATR_MULT = stop_buffer

    try:
        sinais = []
        pair_state = m.default_pair_state()
        # precisa de historico suficiente pra ATR(14) e pivos de 4h
        minimo = m.ATR_PERIOD + m.PIVOT_WINDOW * 2 + 2

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

            zone = pair_state.get("zone")
            if zone is None:
                cand = m.try_map_new_zone(trend, janela_1h, janela_4h, atr_1h,
                                          pair_state.get("cooldowns"))
                pair_state["zone"] = cand
                pair_state["last_1h_ts"] = agora
                continue

            res = m.check_zone_confirmation(zone, janela_1h)
            contra = zone["setup"] == "B" and (
                (zone["direction"] == "venda" and trend == "alta")
                or (zone["direction"] == "compra" and trend == "baixa")
            )

            def _cooldown():
                pair_state.setdefault("cooldowns", {})[zone["direction"]] = {
                    "level": zone["level"],
                    "until_ts": agora + m.ZONE_COOLDOWN_CANDLES_1H * 3600_000,
                }

            if res == "confirmado" and not contra:
                sug = m.compute_suggestion(zone, janela_1h, atr_1h)
                stop_s, entrada = sug["stop_sugerido"], sug["preco_entrada"]
                # modo_alvo escolhe explicitamente qual regra testar, INDEPENDENTE
                # de qual e a autoritativa em producao (m.ALVO_REGRA_ATUAL) -- e
                # assim que o --varrer alvo compara as duas sem precisar trocar
                # a configuracao global.
                if modo_alvo == "proximo":
                    alvo, rr = sug["alvo_proximo"], sug["rr_proximo"]
                else:
                    alvo, rr = sug["alvo_recente"], sug["rr_recente"]

                aceito = rr is not None and rr >= min_rr
                r, motivo, mae, mfe, n = m.desfecho_mecanico(
                    zone["direction"], entrada, stop_s, alvo, rr, agora, c1h,
                    breakeven_apos_r=breakeven_apos_r,
                )
                sinais.append({
                    "par": m.pair_label(inst_id), "setup": zone["setup"],
                    "direcao": zone["direction"], "trend": trend, "ts": agora,
                    "entrada": entrada, "stop": stop_s, "alvo": alvo, "rr": rr,
                    "aceito": aceito, "resultado": r, "mae": mae, "mfe": mfe,
                    "candles": n,
                })
                _cooldown()
                pair_state["zone"] = None
            elif res == "invalidado" or (res == "confirmado" and contra):
                _cooldown()
                pair_state["zone"] = None
            else:
                if res == "tocou":
                    zone["touches"] += 1
                    zone["last_touch_ts"] = agora
                ref = zone.get("last_touch_ts") or zone["created_at"]
                sem_toque = int((agora - ref) // 3600_000)
                zone["candles_since_creation"] = sem_toque
                if (zone["touches"] >= m.ZONE_MAX_TOUCHES
                        or sem_toque >= m.ZONE_MAX_CANDLES_1H):
                    _cooldown()
                    pair_state["zone"] = None
            pair_state["last_1h_ts"] = agora

        return sinais
    finally:
        m.STOP_BUFFER_ATR_MULT = buffer_orig


def resumir(sinais, rotulo):
    aceitos = [s for s in sinais if s["aceito"]]
    resolvidos = [s for s in aceitos if s["resultado"] is not None]
    if not resolvidos:
        print(f"{rotulo:<28} {len(sinais):>4} sinais | {len(aceitos):>4} aceitos "
              f"|    - resolvidos")
        return
    wins = [s for s in resolvidos if s["resultado"] > 0]
    soma = sum(s["resultado"] for s in resolvidos)
    mae_wins = [s["mae"] for s in wins if s["mae"] is not None]
    print(f"{rotulo:<28} {len(sinais):>4} sinais | {len(aceitos):>4} aceitos | "
          f"{len(resolvidos):>4} resolv | {len(wins):>3} wins "
          f"({100*len(wins)/len(resolvidos):>5.1f}%) | "
          f"soma {soma:>8.2f}R | exp {soma/len(resolvidos):>6.3f}R"
          + (f" | MAE mediano dos wins {sorted(mae_wins)[len(mae_wins)//2]:.2f}"
             if mae_wins else ""))


def main(argv):
    pares = m.PAIRS
    if "--pares" in argv:
        alvo = argv[argv.index("--pares") + 1].split(",")
        pares = [p for p in m.PAIRS if p.split("-")[0] in alvo]

    varrer = argv[argv.index("--varrer") + 1] if "--varrer" in argv else None

    print(f"Baixando historico de {len(pares)} par(es)...")
    dados = {}
    for p in pares:
        c1 = fetch_historico(p, "1H", paginas=8)
        c4 = fetch_historico(p, "4H", paginas=4)
        if len(c1) < 60 or len(c4) < 30:
            print(f"  [pula] {p}: historico insuficiente ({len(c1)}x1h, {len(c4)}x4h)")
            continue
        dados[p] = (c1, c4)
        print(f"  {m.pair_label(p):<10} {len(c1)} candles 1h, {len(c4)} candles 4h "
              f"({m.fmt_brt(c1[0]['ts'])} -> {m.fmt_brt(c1[-1]['ts'])})")

    if not dados:
        print("Sem dados suficientes.")
        return

    print()
    if varrer == "stop_buffer":
        print("Varredura de STOP_BUFFER_ATR_MULT (atual: "
              f"{m.STOP_BUFFER_ATR_MULT}):\n")
        for buf in (0.0, 0.05, 0.1, 0.2, 0.3, 0.5, 0.75, 1.0):
            todos = []
            for p, (c1, c4) in dados.items():
                todos += replay_par(p, c1, c4, stop_buffer=buf)
            resumir(todos, f"buffer = {buf:.2f} x ATR")
    elif varrer == "alvo":
        print(f"Regra de alvo: mais RECENTE vs mais PROXIMO (autoritativa hoje: "
              f"{m.ALVO_REGRA_ATUAL}):\n")
        for modo in ("recente", "proximo"):
            todos = []
            for p, (c1, c4) in dados.items():
                todos += replay_par(p, c1, c4, modo_alvo=modo)
            resumir(todos, f"alvo = {modo}")
    elif varrer == "min_rr":
        print(f"Varredura de MIN_RR (atual: {m.MIN_RR}, alvo: {m.ALVO_REGRA_ATUAL}):\n")
        base = []
        for p, (c1, c4) in dados.items():
            base += replay_par(p, c1, c4)
        for rr in (0.0, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0):
            filtrados = [dict(s, aceito=(s["rr"] is not None and s["rr"] >= rr))
                         for s in base]
            resumir(filtrados, f"MIN_RR = {rr:.1f}")
    elif varrer == "breakeven":
        print(f"Stop movido pra entrada (breakeven) apos X de R a favor "
              f"(alvo: {m.ALVO_REGRA_ATUAL}) -- SO TESTE, nada disso esta em "
              f"producao:\n")
        for be in (None, 0.5, 0.75, 1.0, 1.5, 2.0):
            todos = []
            for p, (c1, c4) in dados.items():
                todos += replay_par(p, c1, c4, breakeven_apos_r=be)
            rotulo = "sem breakeven (atual)" if be is None else f"breakeven em {be:.2f}R"
            resumir(todos, rotulo)
    else:
        todos = []
        por_par = defaultdict(list)
        for p, (c1, c4) in dados.items():
            s = replay_par(p, c1, c4)
            todos += s
            por_par[m.pair_label(p)] = s
        print("Parametros atuais:\n")
        for par, s in sorted(por_par.items()):
            resumir(s, par)
        print()
        resumir(todos, "TOTAL")

    print("\nLembrete: replay nao e prova de edge. Ele mede o efeito de mexer "
          "num parametro\nsobre a MESMA logica -- nao valida a logica em si, e "
          "nao inclui custo de\nexecucao (taxa, spread, slippage, funding).")


if __name__ == "__main__":
    main(sys.argv[1:])
