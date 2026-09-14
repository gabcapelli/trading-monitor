# Calibracao — registro mecanico de sinais (atualizado 2026-09-14 09:05 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 32 | 31 | 4 (13%) | -17.93R (-0.578R/sinal) |
| Descartados por R:R baixo | 46 | 44 | 32 (73%) | +6.59R (+0.150R/sinal) |
| TODOS | 78 | 75 | 36 (48%) | -11.33R (-0.151R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=36, mediana 0.38R, maximo 0.98R, 14% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=39, mediana 0.36R, 26% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ETH/USDT | B | venda | nao | proximo | 3.62 | 0.35 | +0.35 | 0.262 | 0.614 | 1 | 2026-09-14 08:05 |
| XRP/USDT | B | compra | nao | proximo | 1.33 | 0.99 | aberto | 0.363 | 0.263 | — | 2026-09-14 07:05 |
| DOGE/USDT | B | compra | nao | proximo | 0.33 | 0.26 | aberto | 0.608 | 0.203 | — | 2026-09-14 07:05 |
| ETH/USDT | B | venda | nao | proximo | 3.28 | 0.22 | +0.22 | 0.983 | 0.442 | 1 | 2026-09-14 06:05 |
| BTC/USDT | B | compra | sim | proximo | 11.94 | 4.66 | -1.00 | 1.068 | 0.055 | 1 | 2026-09-14 02:05 |
| DOGE/USDT | B | venda | nao | proximo | 4.19 | 0.77 | -1.00 | 1.416 | 0.167 | 3 | 2026-09-14 01:05 |
| SOL/USDT | B | compra | nao | proximo | 1.34 | 0.12 | +0.12 | 0.203 | 0.849 | 1 | 2026-09-13 23:05 |
| DOGE/USDT | B | compra | nao | proximo | 2.44 | 1.91 | +1.91 | 0.414 | 2.022 | 3 | 2026-09-13 22:06 |
| ARB/USDT | B | compra | sim | proximo | 3.57 | 3.57 | -1.00 | 1.311 | 0.673 | 1 | 2026-09-13 18:05 |
| XRP/USDT | A | venda | nao | proximo | 4.07 | 1.60 | -1.00 | 1.197 | 0.0 | 1 | 2026-09-13 17:05 |
| LINK/USDT | A | venda | nao | proximo | 3.06 | 0.28 | +0.28 | 0.928 | 3.919 | 3 | 2026-09-13 17:05 |
| SUI/USDT | A | venda | nao | proximo | 1.09 | 0.72 | -1.00 | 1.507 | 0.0 | 2 | 2026-09-13 13:05 |
| SOL/USDT | B | compra | nao | proximo | 3.23 | 0.07 | +0.07 | 0.0 | 1.061 | 1 | 2026-09-13 11:05 |
| WLD/USDT | B | venda | nao | proximo | 0.70 | 0.70 | -1.00 | 1.366 | 0.445 | 3 | 2026-09-13 08:05 |
| XRP/USDT | A | venda | sim | proximo | 2.35 | 2.35 | +2.35 | 0.336 | 2.61 | 1 | 2026-09-13 05:05 |
| LINK/USDT | A | venda | nao | proximo | 4.63 | 0.82 | +0.82 | 0.55 | 3.527 | 1 | 2026-09-13 05:05 |
| ETH/USDT | B | venda | nao | proximo | 1.45 | 1.45 | -1.00 | 1.033 | 0.003 | 1 | 2026-09-13 02:05 |
| SOL/USDT | B | compra | nao | proximo | 2.48 | 1.75 | -1.00 | 2.682 | 0.772 | 2 | 2026-09-13 02:05 |
| LINK/USDT | B | venda | nao | proximo | 1.51 | 0.48 | +0.48 | 0.695 | 1.299 | 1 | 2026-09-13 00:05 |
| LINK/USDT | B | venda | nao | proximo | 0.47 | 0.21 | -1.00 | 1.051 | 0.097 | 4 | 2026-09-12 20:05 |
| SUI/USDT | A | venda | nao | proximo | 0.29 | 0.29 | -1.00 | 1.221 | 0.212 | 1 | 2026-09-12 19:05 |
| XRP/USDT | A | venda | sim | proximo | 6.82 | 6.82 | -1.00 | 1.584 | 0.041 | 1 | 2026-09-12 17:05 |
| DOGE/USDT | B | compra | nao | proximo | 2.43 | 1.68 | -1.00 | 1.006 | 0.796 | 3 | 2026-09-12 17:05 |
| LINK/USDT | A | venda | nao | proximo | 0.54 | 0.13 | -1.00 | 1.008 | 0.228 | 1 | 2026-09-12 17:05 |
| UNI/USDT | B | venda | sim | proximo | 6.19 | 6.03 | -1.00 | 1.152 | 0.634 | 2 | 2026-09-12 16:05 |
