#!/usr/bin/env python3
"""
Backfill unico dos trades anteriores a v5 (CHANGELOG v5, item 8).

POR QUE ISTO EXISTE
-------------------
A v4 introduziu `criado_em_ts` (ts do candle 1h de confirmacao) e o
acompanhamento automatico de desfecho, mas foi commitada DEPOIS da ultima
execucao do monitor -- entao nunca rodou. Resultado: os 30 trades ja no diario
tem criado_em_ts, mae_r, mfe_r e motivo_resultado TODOS em NULL, e nunca
seriam preenchidos pelo caminho normal (que exige criado_em_ts pra saber a
partir de qual candle acompanhar).

Sem MAE/MFE nao ha como calibrar STOP_BUFFER_ATR_MULT nem avaliar a regra de
alvo com o dado que ja existe -- so esperando mais trades.

JANELA
------
A OKX devolve 150 candles de 1h por chamada (~6 dias). Em 10/09/2026 essa
janela cobria 04/09 12:00 em diante, ou seja TODOS os 30 trades (o mais antigo
e de 07/09 19:06). Este script foi feito pra rodar dentro dessa janela; para
trades mais velhos que isso seria preciso paginar /market/history-candles.

O QUE ELE FAZ
-------------
1. Deriva criado_em_ts de criado_em: o script roda em HH:05 e le como ultimo
   candle FECHADO o de ts = (hora cheia anterior). Conferido contra os dados
   de estado de 10/09/2026 (zona do ARB criada no run de 14:05 com created_at
   = 13:00; zona do LINK no run de 11:06 com created_at = 10:00).
2. Reconstroi os pivos 1h COMO ELES ERAM no candle de confirmacao (truncando a
   serie ali) pra calcular alvo_proximo/rr_proximo retroativamente -- a regra
   alternativa de alvo da v5, item 5.
3. Calcula desfecho mecanico + mae_r/mfe_r com desfecho_mecanico().
4. Popula `trades` (campos que faltavam) e insere a linha correspondente em
   `sinais_mecanicos`.

NAO E POSSIVEL RECUPERAR: os sinais DESCARTADOS por R:R baixo antes da v5. Eles
nunca foram gravados em lugar nenhum (so incrementavam um contador inteiro no
state.json, que inclusive esta zerado porque a v4 nunca rodou). A tabela de
calibracao comeca a receber descartes so a partir de agora.

Idempotente: rodar duas vezes nao duplica nem sobrescreve resultado_r manual.

Uso:  python monitor/backfill_mecanico.py [--dry-run]
"""

import sqlite3
import sys
from datetime import datetime

from fetch_and_check import (
    BRT, MIN_RR, PAIRS, TRADE_DB_PATH, desfecho_mecanico, ensure_trade_db,
    fetch_candles, find_confirmed_pivots, fmt_price, pair_label, _rr,
)


def confirm_ts_de(criado_em):
    """
    'YYYY-MM-DD HH:MM' (BRT, horario da EXECUCAO) -> ts em ms do candle 1h que
    o script leu como ultimo fechado naquela execucao.

    Um candle de ts=T cobre [T, T+1h) e so fecha em T+1h. Numa execucao em
    HH:MM, o ultimo fechado e portanto o de ts = (HH-1):00.
    """
    dt = datetime.strptime(criado_em, "%Y-%m-%d %H:%M").replace(tzinfo=BRT)
    dt = dt.replace(minute=0, second=0, microsecond=0)
    return int(dt.timestamp() * 1000) - 3600_000


def alvo_proximo_retroativo(direcao, closed_ate_confirmacao, preco_entrada):
    """
    Recalcula o "pivo oposto mais PROXIMO" usando SO os candles que existiam
    ate o momento da confirmacao -- nao vale olhar o futuro pra escolher alvo.
    """
    highs, lows, _ = find_confirmed_pivots(closed_ate_confirmacao)
    if direcao == "venda":
        cand = [p for _, p in lows if p < preco_entrada]
        return max(cand) if cand else None
    cand = [p for _, p in highs if p > preco_entrada]
    return min(cand) if cand else None


def main(dry_run=False):
    ensure_trade_db()
    conn = sqlite3.connect(TRADE_DB_PATH)
    conn.row_factory = sqlite3.Row

    trades = list(conn.execute(
        "SELECT * FROM trades WHERE criado_em_ts IS NULL ORDER BY id"
    ))
    if not trades:
        print("[backfill] nada a fazer -- todos os trades ja tem criado_em_ts.")
        return

    # um fetch por par, reaproveitado por todos os trades daquele par
    candles_por_par = {}
    for inst_id in PAIRS:
        lbl = pair_label(inst_id)
        if any(t["par"] == lbl for t in trades):
            try:
                cs = fetch_candles(inst_id, "1H", limit=150)
            except Exception as e:  # rede -- pula o par, nao derruba o resto
                print(f"[erro] {inst_id}: {e}")
                continue
            candles_por_par[lbl] = [c for c in cs if c["confirm"] == "1"]
            print(f"[fetch] {lbl}: {len(candles_por_par[lbl])} candles fechados")

    n_ok = n_fora = n_sem_sug = 0
    divergencias = []

    for t in trades:
        closed = candles_por_par.get(t["par"])
        if not closed:
            continue
        cts = confirm_ts_de(t["criado_em"])
        if cts < closed[0]["ts"]:
            print(f"[fora da janela] #{t['id']} {t['par']} {t['criado_em']} "
                  f"-- anterior ao primeiro candle disponivel")
            n_fora += 1
            continue

        # RECUPERACAO DE preco_entrada (trades #3..#16, anteriores a v3): a
        # coluna nao existia, mas a definicao dela e "fechamento do candle 1h
        # de confirmacao" -- e agora sabemos exatamente qual candle e esse.
        # Nao e estimativa: e o mesmo numero que a v3 teria gravado.
        preco_entrada = t["preco_entrada"]
        recuperou_entrada = False
        if preco_entrada is None:
            candle_conf = next((c for c in closed if c["ts"] == cts), None)
            if candle_conf is not None:
                preco_entrada = candle_conf["close"]
                recuperou_entrada = True

        if preco_entrada is None or t["stop_sugerido"] is None:
            # #1 e #2: nem stop_sugerido existe (a sugestao mecanica so entrou
            # depois). Nao ha o que medir -- so o timestamp.
            n_sem_sug += 1
            if not dry_run:
                conn.execute("UPDATE trades SET criado_em_ts=? WHERE id=?", (cts, t["id"]))
            print(f"[parcial] #{t['id']:>2} {t['par']:<10} so criado_em_ts "
                  f"(sem stop_sugerido -- anterior a sugestao mecanica)")
            continue

        ate_confirmacao = [c for c in closed if c["ts"] <= cts]
        alvo_prox = alvo_proximo_retroativo(t["direcao"], ate_confirmacao, preco_entrada)
        rr_prox = _rr(preco_entrada, t["stop_sugerido"], alvo_prox)

        resultado, motivo, mae, mfe, ncandles = desfecho_mecanico(
            t["direcao"], preco_entrada, t["stop_sugerido"],
            t["alvo_sugerido"], t["rr_sugerido"], cts, closed,
        )

        # checagem de sanidade: onde voce ja preencheu Resultado (R) a mao, o
        # calculo mecanico deveria concordar. Divergencia nao e erro (voce pode
        # ter operado stop/alvo diferentes), mas merece aparecer.
        if t["resultado_r"] is not None and resultado is not None:
            if abs(t["resultado_r"] - resultado) > 0.01:
                divergencias.append((t["id"], t["par"], t["resultado_r"], resultado))

        # aceito = passou no filtro de R:R do plano. Os trades #6..#14 estao em
        # `trades` com R:R < 2 porque o filtro so entrou na v3 (08/09/2026) --
        # sao descartes retroativos, e marca-los como aceitos apagaria
        # justamente a comparacao que esta tabela existe pra permitir.
        aceito = 1 if (t["rr_sugerido"] or 0) >= MIN_RR else 0
        motivo_desc = None if aceito else (
            f"rr_{t['rr_sugerido']:.2f}_abaixo_de_{MIN_RR:.1f}"
            if t["rr_sugerido"] is not None else "rr_indisponivel")

        if not dry_run:
            conn.execute(
                "UPDATE trades SET criado_em_ts=?, mae_r=?, mfe_r=?, "
                "alvo_proximo=?, rr_proximo=?, preco_entrada=? WHERE id=?",
                (cts, mae, mfe, alvo_prox, rr_prox, preco_entrada, t["id"]),
            )
            # resultado_r do DIARIO so vale pra trade 'entrado': #6, #9, #11,
            # #12 e #14 foram DESCARTADOS por R:R baixo e ainda assim bateram
            # o alvo -- preencher Resultado (R) neles faria um trade que voce
            # nunca tomou aparecer na estatistica dos 30. Esse desfecho existe,
            # mas o lugar dele e sinais_mecanicos (abaixo), nao aqui.
            # Edicao manual tambem nunca e sobrescrita.
            if (resultado is not None and t["resultado_r"] is None
                    and t["status"] == "entrado"):
                conn.execute(
                    "UPDATE trades SET resultado_r=?, motivo_resultado=? WHERE id=?",
                    (resultado, motivo + "_backfill", t["id"]),
                )
            conn.execute(
                """
                INSERT OR IGNORE INTO sinais_mecanicos
                    (trade_id, par, setup, direcao, tendencia_4h, nivel_referencia,
                     atr_1h, preco_entrada, extremo_varredura, stop_sugerido,
                     alvo_sugerido, rr_sugerido, alvo_proximo, rr_proximo, aceito,
                     motivo_descarte, resultado_mecanico_r, motivo_mecanico,
                     mae_r, mfe_r, candles_ate_desfecho, criado_em, criado_em_ts)
                VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                """,
                (t["id"], t["par"], t["setup"], t["direcao"], t["tendencia_4h"],
                 t["nivel_referencia"], None, preco_entrada,
                 t["extremo_varredura"], t["stop_sugerido"], t["alvo_sugerido"],
                 t["rr_sugerido"], alvo_prox, rr_prox, aceito, motivo_desc, resultado,
                 (motivo + "_backfill") if motivo else None, mae, mfe, ncandles,
                 t["criado_em"], cts),
            )

        n_ok += 1
        marca = "*" if recuperou_entrada else " "
        rr_txt = f"{rr_prox:.2f}" if rr_prox is not None else "—"
        res_txt = f"{resultado:.2f}" if resultado is not None else "aberto"
        print(f"[ok]{marca}     #{t['id']:>2} {t['par']:<10} {t['direcao']:<6} "
              f"MAE {mae:>6} | MFE {mfe:>6} | mec {res_txt:>6} "
              f"em {str(ncandles):>4} candles | alvo prox {fmt_price(alvo_prox)} "
              f"(R:R {rr_txt})")

    if not dry_run:
        conn.commit()
    conn.close()

    print(f"\n[backfill] {n_ok} trade(s) com desfecho mecanico, "
          f"{n_sem_sug} so com timestamp (anteriores a v3), {n_fora} fora da janela."
          + ("  [DRY RUN -- nada gravado]" if dry_run else ""))
    if divergencias:
        print("\n[atencao] Resultado (R) manual diverge do calculo mecanico:")
        for tid, par, manual, mec in divergencias:
            print(f"  #{tid} {par}: manual {manual} vs mecanico {mec}")
        print("  (Nao foi sobrescrito. Esperado se voce operou stop/alvo proprios.)")


if __name__ == "__main__":
    main(dry_run="--dry-run" in sys.argv)
