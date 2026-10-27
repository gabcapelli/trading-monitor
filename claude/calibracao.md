# Calibracao — registro mecanico de sinais (atualizado 2026-10-26 22:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 96 | 96 | 25 (26%) | -3.04R (-0.032R/sinal) |
| Descartados por R:R baixo | 456 | 456 | 285 (62%) | -22.00R (-0.048R/sinal) |
| TODOS | 552 | 552 | 310 (56%) | -25.04R (-0.045R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=310, mediana 0.34R, maximo 0.99R, 8% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=242, mediana 0.38R, 21% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| XRP/USDT | B | compra | nao | proximo | 0.08 | 0.08 | +0.08 | 0.024 | 0.194 | 1 | 2026-10-26 21:06 |
| DOGE/USDT | B | compra | nao | proximo | 0.52 | 0.01 | +0.01 | 0.033 | 0.289 | 1 | 2026-10-26 21:06 |
| BTC/USDT | B | compra | nao | proximo | 2.71 | 1.72 | -1.00 | 1.345 | 0.336 | 2 | 2026-10-26 19:06 |
| XRP/USDT | B | compra | nao | proximo | 1.89 | 0.37 | +0.37 | 0.633 | 0.422 | 1 | 2026-10-26 19:06 |
| DOGE/USDT | B | compra | nao | proximo | 2.16 | 0.37 | +0.37 | 0.51 | 0.394 | 1 | 2026-10-26 19:06 |
| SOL/USDT | A | venda | nao | proximo | 1.00 | 1.00 | -1.00 | 1.632 | 0.423 | 1 | 2026-10-26 18:06 |
| ETH/USDT | B | compra | sim | proximo | 3.07 | 2.33 | -1.00 | 1.477 | 0.158 | 1 | 2026-10-26 17:06 |
| DOGE/USDT | B | compra | nao | proximo | 0.10 | 0.10 | +0.10 | 0.179 | 0.26 | 1 | 2026-10-26 12:06 |
| UNI/USDT | B | compra | nao | proximo | 0.05 | 0.05 | +0.05 | 0.08 | 0.511 | 1 | 2026-10-26 12:06 |
| SOL/USDT | B | compra | nao | proximo | 0.67 | 0.67 | -1.00 | 1.108 | 0.262 | 4 | 2026-10-26 02:06 |
| UNI/USDT | B | compra | nao | proximo | 0.98 | 0.93 | +0.93 | 0.209 | 1.671 | 4 | 2026-10-26 02:06 |
| XRP/USDT | A | venda | nao | proximo | 1.74 | 0.34 | -1.00 | 1.218 | 0.038 | 2 | 2026-10-26 01:06 |
| ETH/USDT | A | venda | nao | proximo | 1.26 | 1.26 | -1.00 | 1.031 | 0.675 | 2 | 2026-10-26 00:06 |
| SOL/USDT | B | compra | nao | proximo | 1.47 | 1.47 | -1.00 | 2.317 | 0.277 | 1 | 2026-10-25 22:06 |
| DOGE/USDT | B | compra | nao | proximo | 1.53 | 1.53 | -1.00 | 2.457 | 0.243 | 1 | 2026-10-25 22:06 |
| UNI/USDT | B | compra | nao | proximo | 1.39 | 1.39 | -1.00 | 2.312 | 0.182 | 1 | 2026-10-25 22:06 |
| WLD/USDT | B | compra | nao | proximo | 1.53 | 1.16 | -1.00 | 1.517 | 0.468 | 5 | 2026-10-25 14:06 |
| SUI/USDT | A | venda | nao | proximo | — | — | -1.00 | 2.476 | 0.067 | 1 | 2026-10-25 08:06 |
| ARB/USDT | A | venda | nao | proximo | 0.20 | 0.20 | +0.20 | 0.302 | 0.302 | 1 | 2026-10-25 06:06 |
| WLD/USDT | B | compra | nao | proximo | 1.66 | 0.98 | -1.00 | 7.951 | 0.023 | 1 | 2026-10-25 05:06 |
| XRP/USDT | B | compra | nao | proximo | 0.10 | 0.10 | +0.10 | 0.113 | 0.363 | 1 | 2026-10-24 16:06 |
| XRP/USDT | B | compra | nao | proximo | 0.73 | 0.73 | +0.73 | 0.248 | 0.804 | 2 | 2026-10-24 14:06 |
| WLD/USDT | B | compra | nao | proximo | 1.23 | 1.23 | -1.00 | 1.002 | 0.013 | 1 | 2026-10-24 14:06 |
| LINK/USDT | A | venda | nao | proximo | 0.27 | 0.27 | -1.00 | 1.148 | 0.549 | 1 | 2026-10-24 09:06 |
| XRP/USDT | B | compra | nao | proximo | 1.99 | 1.99 | -1.00 | 1.513 | 0.868 | 1 | 2026-10-24 04:06 |
