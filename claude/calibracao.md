# Calibracao — registro mecanico de sinais (atualizado 2026-10-28 00:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 98 | 98 | 26 (27%) | -1.78R (-0.018R/sinal) |
| Descartados por R:R baixo | 477 | 476 | 303 (64%) | -18.10R (-0.038R/sinal) |
| TODOS | 575 | 574 | 329 (57%) | -19.88R (-0.035R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=329, mediana 0.34R, maximo 0.99R, 8% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=245, mediana 0.36R, 21% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| BTC/USDT | B | compra | nao | proximo | 1.03 | 0.02 | +0.02 | 0.209 | 0.617 | 1 | 2026-10-27 23:06 |
| ETH/USDT | B | compra | nao | proximo | 0.60 | 0.15 | +0.15 | 0.116 | 0.961 | 1 | 2026-10-27 23:06 |
| DOGE/USDT | A | compra | nao | proximo | 2.55 | 1.14 | aberto | 0.398 | 0.578 | — | 2026-10-27 23:06 |
| ARB/USDT | B | compra | nao | proximo | 0.04 | 0.04 | +0.04 | 0.213 | 0.565 | 1 | 2026-10-27 23:06 |
| SUI/USDT | B | compra | nao | proximo | 0.57 | 0.57 | +0.57 | 0.277 | 0.608 | 1 | 2026-10-27 23:06 |
| UNI/USDT | B | compra | nao | proximo | 0.77 | 0.08 | +0.08 | 0.733 | 0.668 | 1 | 2026-10-27 22:06 |
| DOGE/USDT | B | compra | nao | proximo | 0.81 | 0.81 | +0.81 | 0.208 | 1.143 | 1 | 2026-10-27 20:06 |
| BTC/USDT | B | compra | nao | proximo | 0.17 | 0.15 | +0.15 | 0.706 | 2.022 | 2 | 2026-10-27 17:06 |
| DOGE/USDT | A | compra | sim | proximo | 2.26 | 2.26 | +2.26 | 0.167 | 2.617 | 5 | 2026-10-27 16:06 |
| ETH/USDT | B | compra | nao | proximo | 1.50 | 1.50 | -1.00 | 1.146 | 0.689 | 3 | 2026-10-27 14:06 |
| LINK/USDT | A | compra | nao | proximo | 2.02 | 0.83 | +0.83 | 0.827 | 1.568 | 5 | 2026-10-27 14:06 |
| BTC/USDT | B | compra | nao | proximo | 0.78 | 0.04 | +0.04 | 0.309 | 0.303 | 1 | 2026-10-27 13:06 |
| DOGE/USDT | B | compra | nao | proximo | 0.13 | 0.13 | +0.13 | 0.314 | 0.585 | 1 | 2026-10-27 13:06 |
| UNI/USDT | B | compra | nao | proximo | 0.64 | 0.39 | +0.39 | 0.419 | 0.457 | 1 | 2026-10-27 13:06 |
| DOGE/USDT | B | compra | nao | proximo | 0.22 | 0.21 | +0.21 | 0.783 | 0.211 | 2 | 2026-10-27 10:06 |
| XRP/USDT | B | compra | nao | proximo | 0.81 | 0.31 | +0.31 | 0.146 | 0.446 | 1 | 2026-10-27 08:06 |
| DOGE/USDT | B | compra | nao | proximo | 0.97 | 0.18 | +0.18 | 0.178 | 0.246 | 1 | 2026-10-27 08:06 |
| UNI/USDT | B | compra | nao | proximo | 0.55 | 0.31 | +0.31 | 0.246 | 0.382 | 1 | 2026-10-27 08:06 |
| LINK/USDT | B | compra | nao | proximo | 0.53 | 0.47 | +0.47 | 0.435 | 0.716 | 2 | 2026-10-27 08:06 |
| BTC/USDT | B | compra | sim | proximo | 2.88 | 2.88 | -1.00 | 1.16 | 0.119 | 1 | 2026-10-27 06:06 |
| ETH/USDT | B | compra | nao | proximo | 1.77 | 1.77 | -1.00 | 1.35 | 0.081 | 1 | 2026-10-27 03:06 |
| UNI/USDT | B | compra | nao | proximo | 1.76 | 0.04 | +0.04 | 0.744 | 0.117 | 1 | 2026-10-27 03:06 |
| DOGE/USDT | B | venda | nao | proximo | 3.63 | 1.19 | +1.19 | 0.183 | 2.043 | 2 | 2026-10-26 23:06 |
| XRP/USDT | B | compra | nao | proximo | 0.08 | 0.08 | +0.08 | 0.024 | 0.194 | 1 | 2026-10-26 21:06 |
| DOGE/USDT | B | compra | nao | proximo | 0.52 | 0.01 | +0.01 | 0.033 | 0.289 | 1 | 2026-10-26 21:06 |
