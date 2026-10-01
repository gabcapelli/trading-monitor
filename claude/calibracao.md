# Calibracao — registro mecanico de sinais (atualizado 2026-10-01 01:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 60 | 60 | 12 (20%) | -17.61R (-0.294R/sinal) |
| Descartados por R:R baixo | 190 | 187 | 112 (60%) | -15.90R (-0.085R/sinal) |
| TODOS | 250 | 247 | 124 (50%) | -33.52R (-0.136R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=124, mediana 0.35R, maximo 0.98R, 9% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=123, mediana 0.34R, 22% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| LINK/USDT | B | venda | nao | proximo | 1.73 | 1.73 | -1.00 | 1.062 | 0.564 | 2 | 2026-09-30 21:06 |
| UNI/USDT | B | compra | nao | proximo | 2.40 | 1.31 | aberto | 0.638 | 0.364 | — | 2026-09-30 20:06 |
| DOGE/USDT | B | venda | nao | proximo | 1.25 | 1.25 | -1.00 | 1.121 | 0.702 | 10 | 2026-09-30 15:06 |
| BTC/USDT | B | compra | nao | proximo | 0.85 | 0.01 | +0.01 | 0.017 | 0.661 | 1 | 2026-09-30 13:06 |
| SOL/USDT | B | venda | nao | proximo | 0.37 | 0.13 | +0.13 | 0.275 | 0.338 | 1 | 2026-09-30 12:06 |
| WLD/USDT | B | venda | nao | proximo | 4.54 | 1.79 | aberto | 0.623 | 1.246 | — | 2026-09-30 12:06 |
| BTC/USDT | A | compra | nao | proximo | 2.52 | 0.84 | +0.84 | 0.629 | 6.108 | 1 | 2026-09-30 09:06 |
| BTC/USDT | B | compra | nao | proximo | 0.36 | 0.36 | +0.36 | 0.0 | 0.529 | 1 | 2026-09-30 07:06 |
| ETH/USDT | B | compra | nao | proximo | 1.66 | 1.39 | +1.39 | 0.645 | 1.716 | 2 | 2026-09-30 05:06 |
| XRP/USDT | B | compra | nao | proximo | 5.13 | 0.08 | -1.00 | 1.06 | 0.298 | 1 | 2026-09-30 03:06 |
| SOL/USDT | B | venda | nao | proximo | 0.78 | 0.78 | +0.78 | 0.697 | 1.222 | 3 | 2026-09-30 01:06 |
| XRP/USDT | B | venda | nao | proximo | 0.77 | 0.77 | -1.00 | 1.187 | 0.088 | 2 | 2026-09-30 01:06 |
| LINK/USDT | B | venda | nao | proximo | 0.02 | 0.02 | +0.02 | 0.335 | 0.453 | 1 | 2026-09-29 22:06 |
| SOL/USDT | B | venda | nao | proximo | 2.87 | 0.73 | -1.00 | 1.011 | 0.337 | 4 | 2026-09-29 17:06 |
| SUI/USDT | B | compra | nao | proximo | 2.37 | 0.75 | +0.75 | 0.29 | 0.834 | 2 | 2026-09-29 16:06 |
| XRP/USDT | B | venda | nao | proximo | 4.42 | 0.48 | +0.48 | 0.011 | 2.093 | 1 | 2026-09-29 12:06 |
| ETH/USDT | B | venda | sim | proximo | 4.82 | 2.88 | +2.88 | 0.33 | 3.786 | 2 | 2026-09-29 11:06 |
| SOL/USDT | B | venda | nao | proximo | 4.29 | 1.74 | -1.00 | 1.383 | 0.291 | 1 | 2026-09-29 08:06 |
| WLD/USDT | A | compra | nao | proximo | 1.32 | 1.32 | +1.32 | 0.225 | 1.421 | 1 | 2026-09-29 08:06 |
| UNI/USDT | B | compra | nao | proximo | 0.71 | 0.71 | +0.71 | 0.101 | 1.676 | 1 | 2026-09-29 05:06 |
| ETH/USDT | B | compra | nao | proximo | 0.84 | 0.84 | +0.84 | 0.021 | 1.409 | 1 | 2026-09-29 03:06 |
| ARB/USDT | B | compra | sim | proximo | 3.04 | 3.04 | +3.04 | 0.097 | 3.037 | 4 | 2026-09-29 03:06 |
| UNI/USDT | B | compra | nao | proximo | 0.95 | 0.95 | +0.95 | 0.056 | 1.975 | 2 | 2026-09-29 03:06 |
| ETH/USDT | B | venda | nao | proximo | 0.53 | 0.53 | -1.00 | 1.291 | 0.206 | 2 | 2026-09-29 00:06 |
| ETH/USDT | B | venda | nao | proximo | 0.62 | 0.01 | +0.01 | 0.207 | 0.998 | 1 | 2026-09-28 22:06 |
