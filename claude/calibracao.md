# Calibracao — registro mecanico de sinais (atualizado 2026-11-23 11:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 132 | 132 | 41 (31%) | +22.92R (+0.174R/sinal) |
| Descartados por R:R baixo | 682 | 675 | 431 (64%) | -24.04R (-0.036R/sinal) |
| TODOS | 814 | 807 | 472 (58%) | -1.12R (-0.001R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=472, mediana 0.32R, maximo 0.99R, 7% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=335, mediana 0.38R, 20% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ETH/USDT | B | compra | nao | proximo | 0.08 | 0.08 | aberto | — | — | — | 2026-11-23 11:06 |
| XRP/USDT | B | compra | nao | proximo | 0.18 | 0.06 | aberto | — | — | — | 2026-11-23 11:06 |
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
| ARB/USDT | A | venda | sim | proximo | 2.77 | 2.77 | +2.77 | 0.088 | 5.026 | 7 | 2026-11-20 06:06 |
| SOL/USDT | B | venda | nao | proximo | 0.04 | 0.04 | +0.04 | 0.885 | 0.288 | 1 | 2026-11-20 02:06 |
| UNI/USDT | A | venda | sim | proximo | 2.14 | 2.14 | +2.14 | 0.884 | 4.463 | 12 | 2026-11-20 01:06 |
| XRP/USDT | B | compra | nao | proximo | 2.79 | 0.37 | +0.37 | 0.706 | 0.448 | 1 | 2026-11-20 00:06 |
| DOGE/USDT | B | compra | nao | proximo | 2.03 | 1.29 | -1.00 | 1.02 | 0.143 | 2 | 2026-11-20 00:06 |
| WLD/USDT | B | compra | sim | proximo | 4.90 | 3.62 | -1.00 | 1.789 | 0.817 | 11 | 2026-11-20 00:06 |
| LINK/USDT | B | compra | nao | proximo | 4.06 | 1.84 | -1.00 | 3.158 | 1.127 | 2 | 2026-11-19 21:06 |
| DOGE/USDT | A | compra | nao | proximo | 0.14 | 0.14 | +0.14 | 0.218 | 0.233 | 1 | 2026-11-19 10:06 |
