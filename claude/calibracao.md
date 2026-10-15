# Calibracao — registro mecanico de sinais (atualizado 2026-10-15 15:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 79 | 79 | 20 (25%) | -4.00R (-0.051R/sinal) |
| Descartados por R:R baixo | 341 | 339 | 219 (65%) | -3.75R (-0.011R/sinal) |
| TODOS | 420 | 418 | 239 (57%) | -7.74R (-0.019R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=239, mediana 0.35R, maximo 0.99R, 8% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=179, mediana 0.39R, 22% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| XRP/USDT | B | compra | nao | proximo | 2.26 | 1.63 | aberto | 0.518 | 0.406 | — | 2026-10-15 13:06 |
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
| DOGE/USDT | B | compra | nao | proximo | 1.03 | 1.03 | +1.03 | 0.539 | 1.079 | 6 | 2026-10-13 16:05 |
| ARB/USDT | B | compra | nao | proximo | 0.77 | 0.14 | +0.14 | 0.249 | 0.993 | 1 | 2026-10-13 16:05 |
| LINK/USDT | B | venda | nao | proximo | 2.14 | 0.18 | -1.00 | 1.082 | 0.104 | 1 | 2026-10-13 15:05 |
| UNI/USDT | B | compra | nao | proximo | 0.02 | 0.02 | +0.02 | 0.333 | 0.302 | 1 | 2026-10-13 12:05 |
| ETH/USDT | B | compra | nao | proximo | 2.26 | 0.52 | +0.52 | 0.519 | 1.129 | 1 | 2026-10-13 10:05 |
| SOL/USDT | B | compra | nao | proximo | 2.19 | 1.97 | -1.00 | 1.15 | 1.825 | 24 | 2026-10-13 10:05 |
| UNI/USDT | B | compra | nao | proximo | 1.49 | 0.34 | +0.34 | 0.451 | 0.673 | 1 | 2026-10-13 10:05 |
