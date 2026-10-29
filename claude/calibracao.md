# Calibracao — registro mecanico de sinais (atualizado 2026-10-29 05:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 98 | 98 | 26 (27%) | -1.78R (-0.018R/sinal) |
| Descartados por R:R baixo | 502 | 502 | 322 (64%) | -17.19R (-0.034R/sinal) |
| TODOS | 600 | 600 | 348 (58%) | -18.98R (-0.032R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=348, mediana 0.33R, maximo 0.99R, 7% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=252, mediana 0.36R, 21% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SOL/USDT | A | venda | nao | proximo | 1.62 | 0.14 | +0.14 | 0.154 | 0.733 | 1 | 2026-10-29 04:06 |
| BTC/USDT | B | compra | nao | proximo | 3.00 | 0.27 | +0.27 | 0.074 | 0.519 | 1 | 2026-10-29 02:06 |
| DOGE/USDT | B | compra | nao | proximo | 2.98 | 0.45 | +0.45 | 0.0 | 0.836 | 1 | 2026-10-29 02:06 |
| UNI/USDT | B | compra | nao | proximo | 3.15 | 0.66 | +0.66 | 0.0 | 1.039 | 1 | 2026-10-29 02:06 |
| BTC/USDT | B | compra | nao | proximo | 1.72 | 0.78 | -1.00 | 5.349 | 0.299 | 4 | 2026-10-28 19:06 |
| LINK/USDT | B | compra | nao | proximo | 0.16 | 0.16 | -1.00 | 1.03 | 0.0 | 3 | 2026-10-28 19:06 |
| SOL/USDT | B | venda | nao | proximo | 1.47 | 0.59 | +0.59 | 0.314 | 1.953 | 5 | 2026-10-28 18:06 |
| ETH/USDT | B | compra | nao | proximo | 0.83 | 0.02 | -1.00 | 1.167 | 1.02 | 1 | 2026-10-28 17:06 |
| DOGE/USDT | B | compra | nao | proximo | 0.55 | 0.13 | +0.13 | 0.73 | 0.884 | 1 | 2026-10-28 17:06 |
| ARB/USDT | B | compra | nao | proximo | 0.22 | 0.21 | +0.21 | 0.053 | 0.5 | 1 | 2026-10-28 16:06 |
| UNI/USDT | B | compra | nao | proximo | 0.42 | 0.02 | +0.02 | 0.215 | 0.241 | 1 | 2026-10-28 16:06 |
| BTC/USDT | B | compra | nao | proximo | 4.62 | 0.05 | +0.05 | 0.598 | 1.387 | 1 | 2026-10-28 14:06 |
| XRP/USDT | B | compra | nao | proximo | 3.37 | 0.16 | +0.16 | 0.396 | 0.859 | 1 | 2026-10-28 14:06 |
| BTC/USDT | B | venda | nao | proximo | 3.62 | 0.38 | +0.38 | 0.548 | 0.692 | 2 | 2026-10-28 12:06 |
| XRP/USDT | B | venda | nao | proximo | 2.41 | 1.22 | -1.00 | 2.067 | 0.595 | 4 | 2026-10-28 12:06 |
| ARB/USDT | B | compra | nao | proximo | 2.34 | 1.52 | +1.52 | 0.38 | 3.064 | 4 | 2026-10-28 12:06 |
| UNI/USDT | B | compra | nao | proximo | 3.15 | 0.01 | +0.01 | 0.0 | 0.714 | 1 | 2026-10-28 12:06 |
| XRP/USDT | B | venda | nao | proximo | 2.66 | 1.51 | -1.00 | 1.658 | 0.907 | 6 | 2026-10-28 10:06 |
| XRP/USDT | B | venda | nao | proximo | 1.00 | 1.00 | +1.00 | 0.0 | 3.119 | 2 | 2026-10-28 08:06 |
| LINK/USDT | B | compra | nao | proximo | 0.38 | 0.38 | -1.00 | 1.203 | 0.098 | 2 | 2026-10-28 07:06 |
| BTC/USDT | B | compra | nao | proximo | 0.59 | 0.01 | +0.01 | 0.012 | 3.032 | 1 | 2026-10-28 05:06 |
| SUI/USDT | B | compra | nao | proximo | 0.79 | 0.46 | +0.46 | 0.205 | 1.177 | 1 | 2026-10-28 05:06 |
| UNI/USDT | A | compra | nao | proximo | 0.77 | 0.13 | +0.13 | 0.08 | 1.474 | 1 | 2026-10-28 05:06 |
| LINK/USDT | B | compra | nao | proximo | 0.58 | 0.58 | +0.58 | 0.218 | 1.343 | 1 | 2026-10-28 05:06 |
| BTC/USDT | B | compra | nao | proximo | 0.57 | 0.57 | -1.00 | 1.142 | 0.008 | 3 | 2026-10-28 01:06 |
