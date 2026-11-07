# Calibracao — registro mecanico de sinais (atualizado 2026-11-07 09:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 109 | 109 | 31 (28%) | +8.90R (+0.082R/sinal) |
| Descartados por R:R baixo | 598 | 597 | 379 (63%) | -25.05R (-0.042R/sinal) |
| TODOS | 707 | 706 | 410 (58%) | -16.16R (-0.023R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=410, mediana 0.33R, maximo 0.99R, 7% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=296, mediana 0.36R, 20% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ETH/USDT | B | compra | nao | proximo | 0.65 | 0.53 | aberto | 0.43 | 0.392 | — | 2026-11-07 08:06 |
| DOGE/USDT | A | venda | nao | proximo | 0.52 | 0.03 | +0.03 | 0.29 | 0.61 | 1 | 2026-11-07 07:06 |
| LINK/USDT | A | venda | sim | proximo | 3.64 | 3.64 | -1.00 | 2.727 | 0.127 | 1 | 2026-11-07 02:06 |
| SUI/USDT | B | compra | nao | proximo | 0.79 | 0.79 | -1.00 | 1.472 | 0.194 | 1 | 2026-11-06 23:06 |
| UNI/USDT | B | compra | sim | proximo | 5.77 | 3.09 | +3.09 | 0.0 | 3.66 | 4 | 2026-11-06 22:06 |
| SOL/USDT | B | compra | nao | proximo | 1.76 | 0.13 | +0.13 | 0.489 | 0.517 | 1 | 2026-11-06 19:06 |
| ETH/USDT | B | compra | nao | proximo | 1.85 | 1.78 | +1.78 | 0.571 | 2.237 | 4 | 2026-11-06 16:06 |
| SUI/USDT | B | compra | nao | proximo | 6.31 | 0.65 | -1.00 | 1.31 | 0.461 | 11 | 2026-11-06 14:06 |
| DOGE/USDT | B | compra | nao | proximo | 4.12 | 1.52 | -1.00 | 1.45 | 0.132 | 12 | 2026-11-06 13:06 |
| SUI/USDT | B | compra | nao | proximo | 3.70 | 0.43 | +0.43 | 0.519 | 0.537 | 1 | 2026-11-06 12:06 |
| SOL/USDT | B | compra | nao | proximo | 0.31 | 0.11 | +0.11 | 0.789 | 1.7 | 1 | 2026-11-06 11:06 |
| DOGE/USDT | B | compra | nao | proximo | 0.58 | 0.58 | +0.58 | 0.698 | 1.322 | 1 | 2026-11-06 11:06 |
| UNI/USDT | B | compra | nao | proximo | 0.80 | 0.20 | +0.20 | 0.65 | 1.17 | 1 | 2026-11-06 11:06 |
| DOGE/USDT | B | compra | nao | proximo | 0.45 | 0.45 | +0.45 | 0.878 | 0.771 | 1 | 2026-11-06 09:06 |
| DOGE/USDT | B | compra | nao | proximo | 0.11 | 0.11 | +0.11 | 0.301 | 0.586 | 2 | 2026-11-06 07:06 |
| UNI/USDT | B | compra | nao | proximo | 0.52 | 0.52 | +0.52 | 0.601 | 0.897 | 1 | 2026-11-06 04:06 |
| UNI/USDT | B | venda | nao | proximo | 2.46 | 0.46 | +0.46 | 0.186 | 0.646 | 1 | 2026-11-06 02:06 |
| SOL/USDT | B | compra | nao | proximo | 0.09 | 0.09 | -1.00 | 1.206 | 0.164 | 1 | 2026-11-06 00:06 |
| UNI/USDT | B | compra | nao | proximo | 8.95 | 0.56 | -1.00 | 1.405 | 0.205 | 3 | 2026-11-06 00:06 |
| ARB/USDT | B | compra | nao | proximo | 0.53 | 0.41 | +0.41 | 0.264 | 0.811 | 1 | 2026-11-05 23:06 |
| BTC/USDT | B | compra | nao | proximo | 4.75 | 1.26 | -1.00 | 1.262 | 0.354 | 16 | 2026-11-05 21:06 |
| UNI/USDT | B | compra | sim | proximo | 8.97 | 2.06 | +2.06 | 0.018 | 2.306 | 8 | 2026-11-05 21:06 |
| DOGE/USDT | B | compra | nao | proximo | 4.52 | 2.00 | -1.00 | 1.161 | 0.266 | 3 | 2026-11-05 17:06 |
| SUI/USDT | B | compra | nao | proximo | 5.39 | 1.46 | -1.00 | 1.339 | 0.182 | 2 | 2026-11-05 17:06 |
| UNI/USDT | B | compra | sim | proximo | 11.54 | 2.18 | -1.00 | 1.206 | 0.482 | 2 | 2026-11-05 15:06 |
