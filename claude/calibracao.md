# Calibracao — registro mecanico de sinais (atualizado 2026-11-24 08:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 134 | 134 | 42 (31%) | +23.94R (+0.179R/sinal) |
| Descartados por R:R baixo | 688 | 683 | 437 (64%) | -24.04R (-0.035R/sinal) |
| TODOS | 822 | 817 | 479 (59%) | -0.10R (-0.000R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=479, mediana 0.32R, maximo 0.99R, 8% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=338, mediana 0.38R, 20% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| XRP/USDT | B | compra | nao | proximo | 7.16 | 1.25 | -1.00 | 1.028 | 0.052 | 1 | 2026-11-24 03:06 |
| DOGE/USDT | B | compra | nao | proximo | 4.65 | 1.85 | -1.00 | 1.017 | 0.961 | 7 | 2026-11-24 01:06 |
| LINK/USDT | B | compra | nao | proximo | 3.25 | 0.27 | +0.27 | 0.112 | 0.528 | 1 | 2026-11-24 01:06 |
| SOL/USDT | B | venda | nao | proximo | 0.77 | 0.66 | +0.66 | 0.866 | 0.682 | 8 | 2026-11-24 00:06 |
| SUI/USDT | B | compra | sim | proximo | 6.36 | 2.99 | -1.00 | 1.027 | 0.931 | 3 | 2026-11-23 21:06 |
| SOL/USDT | B | venda | nao | proximo | 1.72 | 0.40 | +0.40 | 0.594 | 1.04 | 1 | 2026-11-23 16:06 |
| SOL/USDT | B | venda | sim | proximo | 2.80 | 2.02 | +2.02 | 0.182 | 2.398 | 4 | 2026-11-23 13:06 |
| LINK/USDT | B | venda | nao | proximo | 2.05 | 0.55 | +0.55 | 0.348 | 0.913 | 3 | 2026-11-23 12:06 |
| ETH/USDT | B | compra | nao | proximo | 0.08 | 0.08 | +0.08 | 0.413 | 0.377 | 1 | 2026-11-23 11:06 |
| XRP/USDT | B | compra | nao | proximo | 0.18 | 0.06 | +0.06 | 0.275 | 0.734 | 1 | 2026-11-23 11:06 |
| LINK/USDT | B | compra | nao | proximo | 1.32 | 1.32 | +1.32 | 0.331 | 1.546 | 1 | 2026-11-23 08:06 |
| UNI/USDT | B | venda | nao | proximo | 2.30 | 0.41 | +0.41 | 0.696 | 0.58 | 3 | 2026-11-23 07:06 |
| XRP/USDT | B | compra | sim | proximo | 4.81 | 4.25 | +4.25 | 0.79 | 7.346 | 5 | 2026-11-23 06:06 |
| SUI/USDT | A | compra | nao | proximo | 0.46 | 0.46 | +0.46 | 0.675 | 0.82 | 1 | 2026-11-23 05:06 |
| DOGE/USDT | B | compra | nao | proximo | 0.46 | 0.46 | +0.46 | 0.838 | 5.544 | 8 | 2026-11-23 03:06 |
| LINK/USDT | B | compra | nao | proximo | 0.26 | 0.26 | +0.26 | 0.1 | 0.415 | 1 | 2026-11-23 01:06 |
| ARB/USDT | A | venda | sim | proximo | 6.64 | 3.04 | -1.00 | 3.637 | 2.159 | 3 | 2026-11-22 22:06 |
| ETH/USDT | B | compra | nao | proximo | 0.39 | 0.39 | +0.39 | 0.182 | 0.903 | 1 | 2026-11-22 18:06 |
| DOGE/USDT | B | compra | nao | proximo | 1.07 | 1.07 | -1.00 | 1.316 | 0.727 | 2 | 2026-11-22 18:06 |
| UNI/USDT | A | venda | sim | proximo | 6.64 | 4.67 | -1.00 | 1.416 | 0.834 | 4 | 2026-11-22 02:06 |
| SOL/USDT | B | compra | nao | proximo | 1.59 | 0.86 | -1.00 | 1.14 | 0.209 | 16 | 2026-11-21 11:06 |
| ARB/USDT | A | venda | sim | proximo | 2.16 | 2.16 | -1.00 | 2.165 | 0.042 | 1 | 2026-11-21 10:06 |
| SOL/USDT | B | compra | nao | proximo | 1.50 | 1.50 | +1.50 | 0.157 | 1.683 | 3 | 2026-11-21 07:06 |
| WLD/USDT | A | venda | nao | proximo | — | — | -1.00 | 1.07 | 0.555 | 8 | 2026-11-21 01:06 |
| SOL/USDT | B | compra | nao | proximo | 2.17 | 1.43 | -1.00 | 1.6 | 0.266 | 6 | 2026-11-20 19:06 |
