#!/usr/bin/env python3
"""
Testa se o filtro humano (do qual os 3 checks manuais de sinais_mecanicos --
correlacao, regime, qualidade -- sao parte, ver CHANGELOG v7 em
fetch_and_check.py) tem valor real sobre o checklist mecanico puro.

Contexto: a v6 (claude/auditoria-v6.md) e o CLAUDE.md documentam edge NEGATIVO
demonstravel no checklist mecanico puro (A/B), reconfirmado em 14/09/2026 com
300 dias / 10 pares: MIN_RR=2.0, n=534, expectancia -0.146R, IC 95% bootstrap
[-0.283, -0.001]. A aposta do Gabriel e que julgamento humano nos 3 pontos que
a geometria de zona/pivo nao captura reverta isso -- este script compara:

  A) resultado_r dos trades que o Gabriel de fato ACEITOU (status='entrado',
     diario humano em `trades`) -- e o que o julgamento humano de fato
     selecionou, dentre os candidatos que passaram no filtro de R:R.
  B) resultado_mecanico_r de TODO sinal mecanicamente confirmado em
     `sinais_mecanicos` (aceito=1 OU aceito=0 -- ou seja, SEM filtro nenhum,
     nem de R:R nem de julgamento) -- a linha de base "pegar tudo que o
     checklist mecanico confirmar, sem nenhum crivo humano".

IC 95% bootstrap em cada grupo e na DIFERENCA de medias (A - B) -- se o IC da
diferenca nao cruzar zero, ha evidencia de que o filtro humano bate a linha de
base mecanica; se cruzar (o esperado com a amostra pequena de hoje), o
resultado e ruido, nao sinal, e nao decide nada sozinho.

NAO mexe em nada do resto do repo -- so leitura de claude/trade_journal.db via
import de fetch_and_check.py (mesma pratica de monitor/replay_setup_c.py).

Uso (da raiz do repo, com PYTHONPATH=monitor):
    PYTHONPATH=monitor python monitor/analise_filtro_humano.py
"""
import os
import sqlite3

import numpy as np

import fetch_and_check as m  # noqa: E402


def bootstrap_ci(valores, n_boot=5000, seed=42):
    if len(valores) < 3:
        return None
    rng = np.random.default_rng(seed)
    arr = np.array(valores)
    medias = [rng.choice(arr, size=len(arr), replace=True).mean() for _ in range(n_boot)]
    return np.percentile(medias, 2.5), np.percentile(medias, 97.5)


def bootstrap_ci_diferenca(a, b, n_boot=5000, seed=42):
    """IC 95% bootstrap da diferenca de medias (mean(a) - mean(b)), resample
    independente em cada grupo a cada iteracao."""
    if len(a) < 3 or len(b) < 3:
        return None
    rng = np.random.default_rng(seed)
    arr_a, arr_b = np.array(a), np.array(b)
    diffs = [
        rng.choice(arr_a, size=len(arr_a), replace=True).mean()
        - rng.choice(arr_b, size=len(arr_b), replace=True).mean()
        for _ in range(n_boot)
    ]
    return np.percentile(diffs, 2.5), np.percentile(diffs, 97.5)


def resumir(rotulo, valores):
    n = len(valores)
    print(f"\n{rotulo}")
    if n == 0:
        print("  n=0 -- sem dado ainda.")
        return
    exp = sum(valores) / n
    wins = [v for v in valores if v > 0]
    ci = bootstrap_ci(valores)
    ci_txt = f" | IC95% [{ci[0]:.3f}, {ci[1]:.3f}]" if ci else " | (n<3, sem IC)"
    print(f"  n={n} | {len(wins)} wins ({100*len(wins)/n:.1f}%) | "
          f"expectancia {exp:+.3f}R{ci_txt}")


def main():
    if not os.path.exists(m.TRADE_DB_PATH):
        print(f"[erro] {m.TRADE_DB_PATH} nao existe -- nada para analisar.")
        return

    conn = sqlite3.connect(m.TRADE_DB_PATH)
    try:
        humano = [
            r[0] for r in conn.execute(
                "SELECT resultado_r FROM trades "
                "WHERE status='entrado' AND resultado_r IS NOT NULL"
            )
        ]
        mecanico_puro = [
            r[0] for r in conn.execute(
                "SELECT resultado_mecanico_r FROM sinais_mecanicos "
                "WHERE resultado_mecanico_r IS NOT NULL"
            )
        ]
    finally:
        conn.close()

    print("Filtro humano (checklist mecanico + julgamento, inclusive os 3 "
          "checks manuais) vs. linha de base mecanica pura (todo sinal "
          "confirmado, sem filtro de R:R nem de julgamento).")

    resumir("A) resultado_r -- trades que o Gabriel aceitou ('entrado')", humano)
    resumir("B) resultado_mecanico_r -- TODO sinal mecanico confirmado "
            "(aceitos + descartados por R:R)", mecanico_puro)

    if len(humano) >= 3 and len(mecanico_puro) >= 3:
        diff = (sum(humano) / len(humano)) - (sum(mecanico_puro) / len(mecanico_puro))
        ci_diff = bootstrap_ci_diferenca(humano, mecanico_puro)
        print(f"\nDiferenca (A - B): {diff:+.3f}R | IC95% bootstrap "
              f"[{ci_diff[0]:+.3f}, {ci_diff[1]:+.3f}]")
        if ci_diff[0] > 0:
            print("  IC inteiramente positivo -- filtro humano bate a linha de "
                  "base mecanica nesta amostra.")
        elif ci_diff[1] < 0:
            print("  IC inteiramente negativo -- filtro humano fica ABAIXO da "
                  "linha de base mecanica nesta amostra.")
        else:
            print("  IC cruza zero -- ainda nao da para distinguir de ruido "
                  "com esta amostra. Nao decide nada sozinho; ver gate dos 30.")
    else:
        print("\nAmostra pequena demais (n<3 em algum dos grupos) para IC da "
              "diferenca -- rode de novo com mais sinais no diario.")


if __name__ == "__main__":
    main()
