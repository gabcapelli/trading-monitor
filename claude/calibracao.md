# Calibracao — registro mecanico de sinais (atualizado 2026-09-23 10:05 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 52 | 52 | 10 (19%) | -17.53R (-0.337R/sinal) |
| Descartados por R:R baixo | 133 | 130 | 82 (63%) | -4.76R (-0.037R/sinal) |
| TODOS | 185 | 182 | 92 (51%) | -22.30R (-0.123R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=92, mediana 0.38R, maximo 0.98R, 12% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=90, mediana 0.36R, 24% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| XRP/USDT | A | compra | nao | proximo | — | — | -1.00 | 1.914 | 0.069 | 2 | 2026-09-23 04:05 |
| DOGE/USDT | A | compra | nao | proximo | 0.81 | 0.81 | -1.00 | 1.457 | 0.286 | 6 | 2026-09-23 00:05 |
| XRP/USDT | A | compra | nao | proximo | 1.87 | 0.13 | +0.13 | 0.177 | 0.61 | 1 | 2026-09-22 20:05 |
| SOL/USDT | A | compra | sim | proximo | 3.88 | 2.17 | +2.17 | 0.955 | 2.487 | 2 | 2026-09-22 19:05 |
| BTC/USDT | A | compra | sim | proximo | 2.44 | 2.44 | -1.00 | 1.075 | 0.598 | 6 | 2026-09-22 14:05 |
| ETH/USDT | A | compra | sim | proximo | 2.19 | 2.19 | -1.00 | 1.972 | 0.045 | 1 | 2026-09-22 11:05 |
| ARB/USDT | B | venda | sim | proximo | 2.66 | 2.66 | +2.66 | 0.473 | 2.723 | 15 | 2026-09-21 21:05 |
| SOL/USDT | A | compra | nao | proximo | — | — | -1.00 | 1.293 | 0.563 | 1 | 2026-09-21 20:05 |
| ETH/USDT | A | compra | nao | proximo | — | — | -1.00 | 1.44 | 2.173 | 9 | 2026-09-21 16:05 |
| LINK/USDT | A | compra | nao | proximo | 1.18 | 1.18 | +1.18 | 0.263 | 1.993 | 2 | 2026-09-21 16:05 |
| ETH/USDT | A | compra | nao | proximo | — | — | aberto | 0.99 | 5.501 | — | 2026-09-21 09:05 |
| ARB/USDT | B | venda | nao | proximo | 1.79 | 1.79 | -1.00 | 2.032 | 0.221 | 1 | 2026-09-21 09:05 |
| WLD/USDT | A | compra | nao | proximo | 0.16 | 0.16 | -1.00 | 1.457 | 0.585 | 1 | 2026-09-21 06:05 |
| SUI/USDT | A | compra | nao | proximo | — | — | aberto | 0.349 | 5.082 | — | 2026-09-21 05:05 |
| DOGE/USDT | B | compra | nao | proximo | 0.87 | 0.87 | +0.87 | 0.302 | 4.182 | 2 | 2026-09-21 04:05 |
| SUI/USDT | A | compra | nao | proximo | — | — | aberto | 0.778 | 4.781 | — | 2026-09-21 01:05 |
| ETH/USDT | A | compra | nao | proximo | 0.56 | 0.12 | +0.12 | 0.198 | 0.582 | 1 | 2026-09-21 00:05 |
| WLD/USDT | B | venda | nao | proximo | 1.03 | 0.41 | -1.00 | 1.036 | 0.304 | 4 | 2026-09-20 23:05 |
| DOGE/USDT | B | compra | nao | proximo | 1.70 | 0.11 | +0.11 | 0.934 | 0.687 | 1 | 2026-09-20 22:05 |
| LINK/USDT | B | venda | nao | proximo | 3.09 | 0.08 | +0.08 | 0.476 | 0.377 | 1 | 2026-09-20 15:05 |
| WLD/USDT | B | venda | nao | proximo | 0.51 | 0.51 | -1.00 | 1.012 | 0.118 | 1 | 2026-09-20 06:05 |
| LINK/USDT | B | compra | nao | proximo | 2.22 | 0.11 | +0.11 | 0.156 | 0.374 | 1 | 2026-09-19 20:05 |
| WLD/USDT | A | compra | sim | proximo | 2.69 | 2.69 | -1.00 | 2.688 | 0.616 | 2 | 2026-09-19 17:05 |
| XRP/USDT | B | venda | nao | proximo | 0.95 | 0.95 | +0.95 | 0.426 | 1.348 | 4 | 2026-09-19 15:05 |
| BTC/USDT | A | compra | nao | proximo | — | — | -1.00 | 1.005 | 0.039 | 1 | 2026-09-19 14:05 |
