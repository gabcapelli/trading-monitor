# Calibracao — registro mecanico de sinais (atualizado 2026-10-22 06:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 90 | 89 | 21 (24%) | -10.84R (-0.122R/sinal) |
| Descartados por R:R baixo | 403 | 401 | 259 (65%) | -4.11R (-0.010R/sinal) |
| TODOS | 493 | 490 | 280 (57%) | -14.95R (-0.031R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=280, mediana 0.34R, maximo 0.99R, 8% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=210, mediana 0.41R, 22% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| WLD/USDT | B | compra | nao | proximo | 6.96 | 0.76 | aberto | — | — | — | 2026-10-22 06:06 |
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
| WLD/USDT | B | venda | sim | proximo | 2.21 | 2.21 | aberto | 0.645 | 1.92 | — | 2026-10-21 11:06 |
| WLD/USDT | B | venda | nao | proximo | 0.42 | 0.32 | +0.32 | 0.64 | 0.944 | 1 | 2026-10-21 07:06 |
| BTC/USDT | B | compra | nao | proximo | 0.18 | 0.09 | +0.09 | 0.139 | 1.358 | 1 | 2026-10-21 05:06 |
| UNI/USDT | B | compra | nao | proximo | 3.87 | 0.26 | +0.26 | 0.167 | 1.507 | 1 | 2026-10-21 04:06 |
| WLD/USDT | B | venda | sim | proximo | 5.76 | 5.76 | -1.00 | 1.202 | 0.328 | 1 | 2026-10-20 22:06 |
| UNI/USDT | B | compra | nao | proximo | 0.17 | 0.17 | +0.17 | 0.464 | 0.937 | 1 | 2026-10-20 22:06 |
| BTC/USDT | B | compra | nao | proximo | 1.93 | 0.47 | -1.00 | 1.099 | 0.001 | 1 | 2026-10-20 20:06 |
| WLD/USDT | B | venda | sim | proximo | 8.25 | 8.25 | -1.00 | 1.377 | 1.336 | 6 | 2026-10-20 20:06 |
| UNI/USDT | B | venda | nao | proximo | 3.26 | 0.79 | -1.00 | 1.9 | 0.522 | 2 | 2026-10-20 20:06 |
| BTC/USDT | B | compra | nao | proximo | 1.67 | 0.23 | +0.23 | 0.086 | 0.46 | 1 | 2026-10-20 18:06 |
| UNI/USDT | B | venda | nao | proximo | 2.75 | 0.95 | +0.95 | 0.072 | 1.081 | 1 | 2026-10-20 16:06 |
| BTC/USDT | A | compra | nao | proximo | 0.88 | 0.35 | +0.35 | 0.199 | 0.349 | 1 | 2026-10-20 14:09 |
| DOGE/USDT | B | compra | nao | proximo | 1.73 | 0.47 | +0.47 | 0.259 | 0.508 | 3 | 2026-10-20 14:09 |
