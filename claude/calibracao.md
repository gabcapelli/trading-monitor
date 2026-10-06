# Calibracao — registro mecanico de sinais (atualizado 2026-10-06 09:05 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 73 | 73 | 19 (26%) | -3.23R (-0.044R/sinal) |
| Descartados por R:R baixo | 275 | 273 | 182 (67%) | +6.24R (+0.023R/sinal) |
| TODOS | 348 | 346 | 201 (58%) | +3.01R (+0.009R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=201, mediana 0.35R, maximo 0.99R, 8% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=145, mediana 0.42R, 23% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| XRP/USDT | B | compra | nao | proximo | 0.26 | 0.24 | +0.24 | 0.435 | 1.176 | 1 | 2026-10-06 08:05 |
| UNI/USDT | B | compra | nao | proximo | 5.34 | 1.25 | +1.25 | 0.736 | 1.316 | 3 | 2026-10-06 05:05 |
| LINK/USDT | B | compra | nao | proximo | 0.24 | 0.24 | +0.24 | 0.036 | 0.455 | 1 | 2026-10-06 05:05 |
| BTC/USDT | B | venda | nao | proximo | 1.99 | 0.41 | +0.41 | 0.0 | 1.429 | 1 | 2026-10-06 03:05 |
| SOL/USDT | B | venda | nao | proximo | 1.49 | 0.52 | +0.52 | 0.178 | 0.988 | 1 | 2026-10-06 03:05 |
| LINK/USDT | B | compra | sim | proximo | 2.35 | 2.35 | -1.00 | 1.104 | 0.544 | 2 | 2026-10-06 02:05 |
| DOGE/USDT | B | venda | nao | proximo | 1.75 | 0.37 | +0.37 | 0.175 | 0.686 | 1 | 2026-10-05 23:05 |
| ARB/USDT | B | venda | nao | proximo | 1.40 | 0.67 | +0.67 | 0.349 | 0.715 | 2 | 2026-10-05 22:05 |
| WLD/USDT | B | venda | nao | proximo | 2.62 | 0.11 | +0.11 | 0.55 | 0.577 | 1 | 2026-10-05 22:05 |
| SUI/USDT | B | venda | nao | proximo | 2.42 | 0.98 | +0.98 | 0.451 | 1.236 | 2 | 2026-10-05 22:05 |
| ETH/USDT | B | venda | sim | proximo | 4.53 | 2.05 | +2.05 | 0.988 | 2.891 | 5 | 2026-10-05 20:05 |
| DOGE/USDT | B | venda | nao | proximo | 3.52 | 0.19 | +0.19 | 0.224 | 0.503 | 1 | 2026-10-05 20:05 |
| DOGE/USDT | B | compra | nao | proximo | 1.27 | 0.76 | +0.76 | 0.108 | 0.765 | 3 | 2026-10-05 17:34 |
| LINK/USDT | B | compra | sim | proximo | 4.57 | 3.14 | -1.00 | 1.103 | 1.48 | 11 | 2026-10-05 14:05 |
| SOL/USDT | B | venda | nao | proximo | 0.36 | 0.36 | +0.36 | 0.656 | 0.894 | 1 | 2026-10-05 13:05 |
| ETH/USDT | B | venda | nao | proximo | 0.34 | 0.16 | +0.16 | 0.071 | 0.309 | 1 | 2026-10-05 12:05 |
| DOGE/USDT | B | venda | nao | proximo | 1.06 | 0.44 | aberto | 0.744 | 0.429 | — | 2026-10-05 12:05 |
| ARB/USDT | B | venda | nao | proximo | 0.39 | 0.07 | +0.07 | 0.365 | 0.14 | 2 | 2026-10-05 12:05 |
| UNI/USDT | B | compra | nao | proximo | 1.44 | 0.46 | -1.00 | 1.781 | 0.48 | 1 | 2026-10-05 11:05 |
| ETH/USDT | B | venda | nao | proximo | 1.59 | 1.11 | -1.00 | 1.409 | 0.001 | 1 | 2026-10-05 10:05 |
| SOL/USDT | B | venda | nao | proximo | 0.80 | 0.80 | -1.00 | 1.187 | 0.331 | 1 | 2026-10-05 10:05 |
| DOGE/USDT | B | venda | nao | proximo | 1.23 | 0.11 | -1.00 | 1.199 | 2.264 | 2 | 2026-10-05 10:05 |
| ETH/USDT | B | compra | nao | proximo | 3.05 | 0.60 | +0.60 | 0.939 | 0.977 | 1 | 2026-10-05 08:05 |
| LINK/USDT | B | venda | nao | proximo | 1.06 | 0.02 | +0.02 | 0.301 | 0.237 | 1 | 2026-10-05 06:05 |
| BTC/USDT | A | compra | sim | proximo | 3.10 | 2.91 | -1.00 | 1.49 | 2.405 | 10 | 2026-10-05 03:05 |
