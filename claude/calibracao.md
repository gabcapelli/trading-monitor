# Calibracao — registro mecanico de sinais (atualizado 2026-10-22 15:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 90 | 90 | 22 (24%) | -8.63R (-0.096R/sinal) |
| Descartados por R:R baixo | 410 | 409 | 264 (65%) | -4.61R (-0.011R/sinal) |
| TODOS | 500 | 499 | 286 (57%) | -13.24R (-0.027R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=286, mediana 0.34R, maximo 0.99R, 8% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=213, mediana 0.39R, 23% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ETH/USDT | B | compra | nao | proximo | 6.20 | 0.38 | +0.38 | 0.558 | 0.388 | 1 | 2026-10-22 11:06 |
| SUI/USDT | B | compra | nao | proximo | 7.22 | 0.65 | -1.00 | 1.784 | 0.29 | 2 | 2026-10-22 11:06 |
| UNI/USDT | B | compra | nao | proximo | 5.85 | 0.46 | -1.00 | 1.345 | 0.364 | 2 | 2026-10-22 11:06 |
| SOL/USDT | B | compra | nao | proximo | 5.26 | 0.03 | +0.03 | 0.075 | 0.495 | 1 | 2026-10-22 07:06 |
| ARB/USDT | B | compra | nao | proximo | 10.42 | 1.03 | +1.03 | 0.071 | 1.606 | 1 | 2026-10-22 07:06 |
| UNI/USDT | B | compra | nao | proximo | 6.78 | 1.27 | -1.00 | 1.975 | 1.179 | 7 | 2026-10-22 07:06 |
| LINK/USDT | B | compra | nao | proximo | 9.83 | 0.30 | +0.30 | 0.117 | 0.572 | 1 | 2026-10-22 07:06 |
| WLD/USDT | B | compra | nao | proximo | 6.96 | 0.76 | +0.76 | 0.539 | 1.412 | 1 | 2026-10-22 06:06 |
| UNI/USDT | B | compra | nao | proximo | 8.52 | 1.05 | -1.00 | 1.107 | 0.098 | 1 | 2026-10-22 05:06 |
| LINK/USDT | B | compra | nao | proximo | 8.66 | 1.05 | -1.00 | 2.628 | 0.0 | 1 | 2026-10-22 05:06 |
| SOL/USDT | B | compra | nao | proximo | 7.38 | 0.16 | -1.00 | 1.839 | 0.184 | 1 | 2026-10-22 02:06 |
| SUI/USDT | B | compra | nao | proximo | 8.24 | 0.11 | -1.00 | 1.79 | 0.358 | 1 | 2026-10-22 02:06 |
| BTC/USDT | B | compra | nao | proximo | 6.58 | 0.83 | -1.00 | 1.558 | 0.223 | 3 | 2026-10-22 01:06 |
| WLD/USDT | B | venda | nao | proximo | 0.47 | 0.47 | +0.47 | 0.209 | 1.269 | 3 | 2026-10-21 23:06 |
| SOL/USDT | B | compra | nao | proximo | 1.86 | 1.86 | -1.00 | 1.82 | 0.02 | 1 | 2026-10-21 19:06 |
| SOL/USDT | A | compra | nao | proximo | — | — | -1.00 | 1.568 | 0.227 | 4 | 2026-10-21 17:06 |
| SUI/USDT | A | compra | nao | proximo | 1.06 | 0.22 | +0.22 | 0.561 | 0.271 | 1 | 2026-10-21 13:06 |
| ETH/USDT | A | compra | nao | proximo | — | — | -1.00 | 1.405 | 0.924 | 11 | 2026-10-21 12:06 |
| BTC/USDT | A | compra | nao | proximo | — | — | -1.00 | 1.75 | 1.86 | 13 | 2026-10-21 11:06 |
| WLD/USDT | B | venda | sim | proximo | 2.21 | 2.21 | +2.21 | 0.645 | 2.417 | 26 | 2026-10-21 11:06 |
| WLD/USDT | B | venda | nao | proximo | 0.42 | 0.32 | +0.32 | 0.64 | 0.944 | 1 | 2026-10-21 07:06 |
| BTC/USDT | B | compra | nao | proximo | 0.18 | 0.09 | +0.09 | 0.139 | 1.358 | 1 | 2026-10-21 05:06 |
| UNI/USDT | B | compra | nao | proximo | 3.87 | 0.26 | +0.26 | 0.167 | 1.507 | 1 | 2026-10-21 04:06 |
| WLD/USDT | B | venda | sim | proximo | 5.76 | 5.76 | -1.00 | 1.202 | 0.328 | 1 | 2026-10-20 22:06 |
| UNI/USDT | B | compra | nao | proximo | 0.17 | 0.17 | +0.17 | 0.464 | 0.937 | 1 | 2026-10-20 22:06 |
