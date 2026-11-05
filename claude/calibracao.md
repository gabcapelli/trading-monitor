# Calibracao — registro mecanico de sinais (atualizado 2026-11-05 00:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 103 | 103 | 27 (26%) | -3.57R (-0.035R/sinal) |
| Descartados por R:R baixo | 567 | 565 | 358 (63%) | -23.21R (-0.041R/sinal) |
| TODOS | 670 | 668 | 385 (58%) | -26.78R (-0.040R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=385, mediana 0.32R, maximo 0.99R, 7% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=283, mediana 0.39R, 20% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ARB/USDT | B | compra | nao | proximo | 2.01 | 0.20 | aberto | — | — | — | 2026-11-05 00:06 |
| XRP/USDT | B | compra | nao | proximo | 0.57 | 0.57 | aberto | 0.284 | 0.221 | — | 2026-11-04 23:06 |
| SOL/USDT | B | venda | nao | proximo | 2.22 | 0.07 | -1.00 | 1.152 | 0.419 | 1 | 2026-11-04 21:06 |
| ARB/USDT | B | compra | nao | proximo | 3.22 | 0.05 | +0.05 | 0.29 | 0.19 | 1 | 2026-11-04 18:06 |
| UNI/USDT | A | compra | nao | proximo | 1.93 | 1.93 | +1.93 | 0.636 | 2.211 | 2 | 2026-11-04 18:06 |
| LINK/USDT | B | venda | nao | proximo | 1.62 | 0.23 | -1.00 | 1.337 | 0.118 | 3 | 2026-11-04 17:06 |
| BTC/USDT | B | venda | sim | proximo | 5.57 | 5.57 | -1.00 | 1.478 | 0.99 | 4 | 2026-11-04 16:06 |
| SOL/USDT | B | venda | nao | proximo | 2.84 | 0.15 | +0.15 | 0.348 | 0.531 | 1 | 2026-11-04 15:06 |
| LINK/USDT | B | venda | nao | proximo | 4.45 | 0.61 | +0.61 | 0.506 | 0.876 | 1 | 2026-11-04 15:06 |
| BTC/USDT | B | venda | nao | proximo | 8.92 | 1.81 | -1.00 | 3.921 | 1.506 | 3 | 2026-11-04 09:06 |
| UNI/USDT | A | compra | nao | proximo | 0.29 | 0.29 | +0.29 | 0.089 | 0.519 | 1 | 2026-11-04 05:06 |
| XRP/USDT | B | compra | nao | proximo | 1.49 | 0.01 | +0.01 | 0.088 | 0.737 | 1 | 2026-11-04 01:06 |
| SUI/USDT | B | compra | nao | proximo | 1.74 | 0.37 | +0.37 | 0.064 | 0.839 | 1 | 2026-11-04 01:06 |
| UNI/USDT | B | compra | nao | proximo | 1.18 | 0.22 | +0.22 | 0.092 | 0.876 | 1 | 2026-11-04 01:06 |
| ARB/USDT | A | venda | nao | proximo | 1.10 | 0.08 | +0.08 | 0.205 | 0.643 | 1 | 2026-11-04 00:06 |
| ETH/USDT | B | venda | nao | proximo | 1.39 | 0.58 | +0.58 | 0.446 | 1.21 | 1 | 2026-11-03 23:06 |
| XRP/USDT | B | venda | nao | proximo | 0.83 | 0.61 | +0.61 | 0.732 | 1.112 | 2 | 2026-11-03 23:06 |
| UNI/USDT | B | venda | nao | proximo | 2.30 | 0.26 | +0.26 | 0.469 | 0.655 | 1 | 2026-11-03 23:06 |
| ETH/USDT | B | compra | nao | proximo | 1.43 | 1.06 | -1.00 | 1.391 | 0.713 | 3 | 2026-11-03 18:06 |
| XRP/USDT | B | compra | nao | proximo | 1.64 | 1.64 | -1.00 | 3.641 | 1.255 | 4 | 2026-11-03 18:06 |
| BTC/USDT | B | compra | nao | proximo | 0.37 | 0.04 | +0.04 | 0.291 | 0.181 | 1 | 2026-11-03 14:06 |
| DOGE/USDT | B | compra | nao | proximo | 1.40 | 1.40 | -1.00 | 3.145 | 1.273 | 10 | 2026-11-03 12:06 |
| SUI/USDT | B | compra | nao | proximo | 1.14 | 0.73 | -1.00 | 1.993 | 0.648 | 10 | 2026-11-03 12:06 |
| LINK/USDT | B | compra | nao | proximo | 1.25 | 0.19 | -1.00 | 1.403 | 0.104 | 2 | 2026-11-03 11:06 |
| DOGE/USDT | B | compra | nao | proximo | 0.63 | 0.63 | -1.00 | 1.447 | 0.57 | 12 | 2026-11-03 10:06 |
