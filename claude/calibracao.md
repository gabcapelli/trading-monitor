# Calibracao — registro mecanico de sinais (atualizado 2026-10-16 16:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 80 | 80 | 20 (25%) | -5.00R (-0.062R/sinal) |
| Descartados por R:R baixo | 347 | 345 | 224 (65%) | -0.78R (-0.002R/sinal) |
| TODOS | 427 | 425 | 244 (57%) | -5.78R (-0.014R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=244, mediana 0.35R, maximo 0.99R, 8% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=181, mediana 0.41R, 22% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| LINK/USDT | A | venda | nao | proximo | 3.98 | 0.03 | aberto | — | — | — | 2026-10-16 16:06 |
| WLD/USDT | B | venda | nao | proximo | 2.50 | 1.03 | +1.03 | 0.032 | 1.503 | 1 | 2026-10-16 12:06 |
| WLD/USDT | B | venda | nao | proximo | 2.34 | 1.24 | +1.24 | 0.34 | 1.595 | 3 | 2026-10-16 10:06 |
| UNI/USDT | B | venda | nao | proximo | 1.20 | 0.21 | +0.21 | 0.321 | 0.313 | 1 | 2026-10-16 10:06 |
| UNI/USDT | B | compra | nao | proximo | 1.04 | 0.72 | +0.72 | 0.0 | 0.964 | 1 | 2026-10-16 02:06 |
| ARB/USDT | B | venda | sim | proximo | 5.71 | 2.10 | -1.00 | 1.214 | 0.731 | 4 | 2026-10-15 23:06 |
| UNI/USDT | B | venda | nao | proximo | 5.43 | 0.76 | +0.76 | 0.892 | 1.3 | 2 | 2026-10-15 23:06 |
| XRP/USDT | B | compra | nao | proximo | 2.26 | 1.63 | -1.00 | 1.605 | 0.737 | 24 | 2026-10-15 13:06 |
| BTC/USDT | B | compra | nao | proximo | 0.03 | 0.03 | +0.03 | 0.07 | 0.429 | 1 | 2026-10-15 12:06 |
| XRP/USDT | B | compra | sim | proximo | 3.58 | 3.58 | -1.00 | 2.99 | 0.041 | 1 | 2026-10-15 07:06 |
| XRP/USDT | B | compra | nao | proximo | 1.72 | 1.72 | -1.00 | 1.225 | 0.517 | 5 | 2026-10-15 05:06 |
| BTC/USDT | B | compra | sim | proximo | 2.29 | 2.29 | -1.00 | 2.508 | 1.514 | 7 | 2026-10-15 04:06 |
| WLD/USDT | A | venda | nao | proximo | 0.31 | 0.31 | +0.31 | 0.701 | 0.368 | 7 | 2026-10-15 03:06 |
| BTC/USDT | B | compra | nao | proximo | 0.41 | 0.41 | -1.00 | 1.334 | 0.115 | 1 | 2026-10-15 02:06 |
| ARB/USDT | B | compra | nao | proximo | 1.37 | 0.93 | -1.00 | 1.126 | 0.049 | 1 | 2026-10-15 02:06 |
| UNI/USDT | A | venda | nao | proximo | 0.95 | 0.95 | -1.00 | 1.063 | 0.045 | 1 | 2026-10-15 01:06 |
| XRP/USDT | A | venda | nao | proximo | 0.03 | 0.03 | +0.03 | 0.183 | 1.156 | 1 | 2026-10-14 11:06 |
| LINK/USDT | B | venda | nao | proximo | 1.38 | 0.05 | +0.05 | 0.296 | 0.485 | 1 | 2026-10-14 10:06 |
| BTC/USDT | B | compra | nao | proximo | 1.08 | 0.13 | -1.00 | 1.827 | 0.999 | 2 | 2026-10-14 08:06 |
| WLD/USDT | B | compra | nao | proximo | 1.97 | 1.97 | -1.00 | 1.171 | 1.757 | 3 | 2026-10-14 04:06 |
| ETH/USDT | B | venda | nao | proximo | 1.57 | 0.98 | +0.98 | 0.417 | 1.294 | 2 | 2026-10-14 01:06 |
| ARB/USDT | B | compra | sim | proximo | 2.47 | 2.47 | -1.00 | 1.573 | 0.967 | 4 | 2026-10-13 23:06 |
| ARB/USDT | A | compra | sim | proximo | 2.28 | 2.28 | -1.00 | 1.165 | 1.785 | 6 | 2026-10-13 21:06 |
| DOGE/USDT | B | compra | nao | proximo | 1.74 | 1.74 | -1.00 | 1.354 | 0.387 | 3 | 2026-10-13 18:05 |
| WLD/USDT | B | venda | nao | proximo | 2.97 | 1.35 | +1.35 | 0.621 | 1.449 | 9 | 2026-10-13 18:05 |
