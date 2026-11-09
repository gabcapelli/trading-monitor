# Calibracao — registro mecanico de sinais (atualizado 2026-11-09 10:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 112 | 112 | 31 (28%) | +5.90R (+0.053R/sinal) |
| Descartados por R:R baixo | 612 | 611 | 384 (63%) | -30.14R (-0.049R/sinal) |
| TODOS | 724 | 723 | 415 (57%) | -24.24R (-0.034R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=415, mediana 0.33R, maximo 0.99R, 7% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=308, mediana 0.37R, 20% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| UNI/USDT | B | compra | nao | proximo | 1.78 | 1.74 | aberto | 0.312 | 1.316 | — | 2026-11-09 06:06 |
| LINK/USDT | B | compra | nao | proximo | 0.82 | 0.82 | +0.82 | 0.317 | 1.117 | 4 | 2026-11-09 06:06 |
| XRP/USDT | A | venda | nao | proximo | — | — | -1.00 | 1.407 | 0.095 | 1 | 2026-11-09 05:06 |
| LINK/USDT | B | compra | sim | proximo | 3.00 | 3.00 | -1.00 | 1.342 | 0.37 | 1 | 2026-11-09 00:06 |
| BTC/USDT | B | compra | nao | proximo | 1.18 | 0.85 | -1.00 | 1.138 | 0.443 | 5 | 2026-11-08 22:06 |
| UNI/USDT | B | compra | nao | proximo | 0.47 | 0.22 | +0.22 | 0.292 | 0.235 | 2 | 2026-11-08 22:06 |
| LINK/USDT | B | compra | nao | proximo | 1.22 | 1.22 | -1.00 | 1.203 | 0.375 | 6 | 2026-11-08 22:06 |
| LINK/USDT | B | compra | sim | proximo | 2.71 | 2.71 | -1.00 | 1.019 | 1.636 | 9 | 2026-11-08 20:06 |
| BTC/USDT | B | compra | nao | proximo | 1.09 | 0.23 | -1.00 | 11.005 | 0.007 | 3 | 2026-11-08 16:06 |
| LINK/USDT | B | compra | sim | proximo | 4.19 | 4.19 | -1.00 | 13.491 | 2.223 | 4 | 2026-11-08 15:06 |
| ARB/USDT | B | venda | nao | proximo | 1.45 | 1.45 | -1.00 | 1.083 | 0.0 | 1 | 2026-11-08 10:06 |
| UNI/USDT | B | venda | nao | proximo | 0.70 | 0.70 | +0.70 | 0.511 | 0.974 | 9 | 2026-11-07 22:06 |
| ETH/USDT | B | compra | nao | proximo | 1.44 | 1.26 | -1.00 | 1.321 | 0.0 | 3 | 2026-11-07 21:06 |
| BTC/USDT | B | compra | nao | proximo | 2.44 | 1.66 | +1.66 | 0.466 | 2.157 | 16 | 2026-11-07 19:06 |
| ETH/USDT | B | compra | nao | proximo | 1.62 | 1.50 | -1.00 | 15.546 | 1.154 | 24 | 2026-11-07 19:06 |
| WLD/USDT | A | venda | nao | proximo | — | — | -1.00 | 1.139 | 0.28 | 3 | 2026-11-07 18:06 |
| SUI/USDT | A | venda | nao | proximo | 1.12 | 0.52 | +0.52 | 0.091 | 1.851 | 1 | 2026-11-07 12:06 |
| ETH/USDT | B | compra | nao | proximo | 0.65 | 0.53 | -1.00 | 1.47 | 0.392 | 2 | 2026-11-07 08:06 |
| DOGE/USDT | A | venda | nao | proximo | 0.52 | 0.03 | +0.03 | 0.29 | 0.61 | 1 | 2026-11-07 07:06 |
| LINK/USDT | A | venda | sim | proximo | 3.64 | 3.64 | -1.00 | 2.727 | 0.127 | 1 | 2026-11-07 02:06 |
| SUI/USDT | B | compra | nao | proximo | 0.79 | 0.79 | -1.00 | 1.472 | 0.194 | 1 | 2026-11-06 23:06 |
| UNI/USDT | B | compra | sim | proximo | 5.77 | 3.09 | +3.09 | 0.0 | 3.66 | 4 | 2026-11-06 22:06 |
| SOL/USDT | B | compra | nao | proximo | 1.76 | 0.13 | +0.13 | 0.489 | 0.517 | 1 | 2026-11-06 19:06 |
| ETH/USDT | B | compra | nao | proximo | 1.85 | 1.78 | +1.78 | 0.571 | 2.237 | 4 | 2026-11-06 16:06 |
| SUI/USDT | B | compra | nao | proximo | 6.31 | 0.65 | -1.00 | 1.31 | 0.461 | 11 | 2026-11-06 14:06 |
