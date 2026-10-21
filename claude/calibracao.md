# Calibracao — registro mecanico de sinais (atualizado 2026-10-21 09:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 89 | 89 | 21 (24%) | -10.84R (-0.122R/sinal) |
| Descartados por R:R baixo | 391 | 390 | 257 (66%) | +4.20R (+0.011R/sinal) |
| TODOS | 480 | 479 | 278 (58%) | -6.64R (-0.014R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=278, mediana 0.34R, maximo 0.99R, 8% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=201, mediana 0.42R, 23% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
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
| UNI/USDT | B | compra | nao | proximo | 0.31 | 0.31 | +0.31 | 0.16 | 0.522 | 1 | 2026-10-20 14:09 |
| LINK/USDT | B | compra | nao | proximo | 0.82 | 0.68 | -1.00 | 1.011 | 0.037 | 2 | 2026-10-20 14:09 |
| ARB/USDT | B | venda | nao | proximo | 1.76 | 0.15 | +0.15 | 0.163 | 0.319 | 1 | 2026-10-20 13:06 |
| ETH/USDT | B | compra | nao | proximo | 0.20 | 0.20 | +0.20 | 0.089 | 2.21 | 1 | 2026-10-20 11:07 |
| UNI/USDT | B | compra | nao | proximo | 4.43 | 1.17 | +1.17 | 0.926 | 1.22 | 2 | 2026-10-20 08:06 |
| WLD/USDT | B | venda | sim | proximo | 5.52 | 5.52 | -1.00 | 2.768 | 1.442 | 5 | 2026-10-20 05:06 |
| BTC/USDT | B | venda | nao | proximo | 4.10 | 0.69 | +0.69 | 0.092 | 1.776 | 1 | 2026-10-20 02:06 |
| UNI/USDT | B | venda | nao | proximo | 1.95 | 0.37 | +0.37 | 0.087 | 1.675 | 1 | 2026-10-20 02:06 |
| ARB/USDT | B | compra | nao | proximo | 0.15 | 0.05 | -1.00 | 1.045 | 0.016 | 2 | 2026-10-20 01:06 |
| ETH/USDT | B | compra | nao | proximo | 1.20 | 1.20 | -1.00 | 1.569 | 1.168 | 6 | 2026-10-20 00:06 |
| ARB/USDT | B | compra | nao | proximo | 0.96 | 0.29 | +0.29 | 0.916 | 0.375 | 1 | 2026-10-19 22:06 |
| LINK/USDT | A | venda | nao | proximo | 1.73 | 0.22 | +0.22 | 0.125 | 1.785 | 1 | 2026-10-19 22:06 |
| UNI/USDT | B | compra | nao | proximo | 3.87 | 0.80 | +0.80 | 0.0 | 2.568 | 1 | 2026-10-19 19:05 |
