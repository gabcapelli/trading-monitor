# Calibracao — registro mecanico de sinais (atualizado 2026-10-20 19:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 87 | 87 | 21 (24%) | -8.84R (-0.102R/sinal) |
| Descartados por R:R baixo | 385 | 384 | 253 (66%) | +5.37R (+0.014R/sinal) |
| TODOS | 472 | 471 | 274 (58%) | -3.47R (-0.007R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=274, mediana 0.34R, maximo 0.99R, 8% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=197, mediana 0.42R, 23% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
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
| ETH/USDT | B | compra | sim | proximo | 5.13 | 2.70 | -1.00 | 3.452 | 1.927 | 5 | 2026-10-19 18:05 |
| SOL/USDT | B | venda | nao | proximo | 2.80 | 0.44 | +0.44 | 0.615 | 0.551 | 1 | 2026-10-19 11:05 |
| LINK/USDT | B | compra | nao | proximo | 1.43 | 0.13 | -1.00 | 1.316 | 0.331 | 1 | 2026-10-19 10:05 |
| UNI/USDT | B | venda | nao | proximo | 11.44 | 0.36 | +0.36 | 0.571 | 0.438 | 1 | 2026-10-19 06:05 |
| BTC/USDT | B | venda | nao | proximo | 4.15 | 1.57 | +1.57 | 0.757 | 1.949 | 7 | 2026-10-19 05:05 |
| ETH/USDT | B | venda | nao | proximo | 5.46 | 0.36 | +0.36 | 0.867 | 0.823 | 3 | 2026-10-19 05:05 |
| XRP/USDT | B | compra | nao | proximo | 0.53 | 0.53 | +0.53 | 0.257 | 1.349 | 2 | 2026-10-19 03:05 |
| LINK/USDT | B | compra | nao | proximo | 1.11 | 1.11 | -1.00 | 1.626 | 1.103 | 5 | 2026-10-19 03:05 |
