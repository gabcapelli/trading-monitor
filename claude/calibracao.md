# Calibracao — registro mecanico de sinais (atualizado 2026-09-15 00:05 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 32 | 32 | 4 (12%) | -18.93R (-0.591R/sinal) |
| Descartados por R:R baixo | 57 | 56 | 41 (73%) | +9.11R (+0.163R/sinal) |
| TODOS | 89 | 88 | 45 (51%) | -9.81R (-0.112R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=45, mediana 0.38R, maximo 0.98R, 13% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=43, mediana 0.27R, 26% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ETH/USDT | B | venda | nao | proximo | 2.53 | 0.40 | aberto | — | — | — | 2026-09-15 00:05 |
| XRP/USDT | B | venda | nao | proximo | 2.45 | 0.42 | +0.42 | 0.247 | 0.494 | 1 | 2026-09-14 21:05 |
| UNI/USDT | B | venda | nao | proximo | 3.48 | 0.57 | -1.00 | 1.98 | 0.088 | 1 | 2026-09-14 21:05 |
| ETH/USDT | B | venda | nao | proximo | 1.72 | 0.70 | +0.70 | 0.057 | 0.767 | 1 | 2026-09-14 20:05 |
| XRP/USDT | B | venda | nao | proximo | 2.57 | 1.14 | +1.14 | 0.448 | 1.187 | 3 | 2026-09-14 19:05 |
| SUI/USDT | B | venda | nao | proximo | 1.36 | 0.56 | +0.56 | 0.248 | 0.573 | 1 | 2026-09-14 19:05 |
| BTC/USDT | B | venda | nao | proximo | 5.21 | 0.86 | -1.00 | 2.103 | 0.036 | 1 | 2026-09-14 17:05 |
| SOL/USDT | A | compra | nao | proximo | 0.11 | 0.11 | +0.11 | 0.221 | 1.262 | 1 | 2026-09-14 15:05 |
| WLD/USDT | B | venda | nao | proximo | 0.28 | 0.28 | +0.28 | 0.682 | 0.398 | 1 | 2026-09-14 12:06 |
| BTC/USDT | B | compra | nao | proximo | 0.26 | 0.26 | +0.26 | 0.021 | 0.694 | 1 | 2026-09-14 11:05 |
| XRP/USDT | B | venda | nao | proximo | 5.67 | 1.06 | +1.06 | 0.746 | 1.134 | 1 | 2026-09-14 10:05 |
| ETH/USDT | B | venda | nao | proximo | 3.62 | 0.35 | +0.35 | 0.262 | 0.614 | 1 | 2026-09-14 08:05 |
| XRP/USDT | B | compra | nao | proximo | 1.33 | 0.99 | +0.99 | 0.867 | 1.73 | 8 | 2026-09-14 07:05 |
| DOGE/USDT | B | compra | nao | proximo | 0.33 | 0.26 | -1.00 | 1.273 | 0.203 | 3 | 2026-09-14 07:05 |
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
