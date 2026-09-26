# Calibracao — registro mecanico de sinais (atualizado 2026-09-25 21:05 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 56 | 56 | 10 (18%) | -21.53R (-0.385R/sinal) |
| Descartados por R:R baixo | 150 | 149 | 90 (60%) | -12.28R (-0.082R/sinal) |
| TODOS | 206 | 205 | 100 (49%) | -33.81R (-0.165R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=100, mediana 0.38R, maximo 0.98R, 11% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=105, mediana 0.36R, 23% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| WLD/USDT | B | venda | nao | proximo | 2.00 | 1.63 | -1.00 | 2.032 | 0.173 | 1 | 2026-09-25 19:05 |
| DOGE/USDT | B | compra | nao | proximo | 1.21 | 1.21 | -1.00 | 1.116 | 0.655 | 2 | 2026-09-25 17:05 |
| XRP/USDT | A | compra | nao | proximo | 2.49 | 0.34 | -1.00 | 1.07 | 0.194 | 1 | 2026-09-25 12:05 |
| WLD/USDT | B | venda | nao | proximo | 5.27 | 0.12 | -1.00 | 2.456 | 0.024 | 1 | 2026-09-25 08:05 |
| ETH/USDT | B | venda | nao | proximo | 0.10 | 0.10 | +0.10 | 0.171 | 0.167 | 1 | 2026-09-25 00:05 |
| ARB/USDT | B | venda | nao | proximo | 0.03 | 0.03 | +0.03 | 0.391 | 0.068 | 1 | 2026-09-25 00:05 |
| SUI/USDT | B | venda | nao | proximo | 0.27 | 0.14 | -1.00 | 1.275 | 0.06 | 7 | 2026-09-25 00:05 |
| WLD/USDT | B | venda | nao | proximo | 0.30 | 0.30 | +0.30 | 0.582 | 1.074 | 1 | 2026-09-24 23:05 |
| LINK/USDT | B | venda | sim | proximo | 11.12 | 2.95 | -1.00 | 1.495 | 0.275 | 2 | 2026-09-24 20:05 |
| XRP/USDT | A | compra | nao | proximo | 5.35 | 0.78 | +0.78 | 0.621 | 1.068 | 6 | 2026-09-24 16:05 |
| WLD/USDT | B | compra | nao | proximo | 1.29 | 1.29 | +1.29 | 0.0 | 2.657 | 1 | 2026-09-24 10:05 |
| LINK/USDT | B | venda | nao | proximo | 0.31 | 0.02 | -1.00 | 1.166 | 0.184 | 1 | 2026-09-24 09:05 |
| ARB/USDT | B | compra | nao | proximo | 3.15 | 0.68 | +0.68 | 0.606 | 2.71 | 3 | 2026-09-24 08:05 |
| ETH/USDT | B | venda | nao | proximo | 0.22 | 0.22 | +0.22 | 0.179 | 1.503 | 1 | 2026-09-24 06:05 |
| WLD/USDT | A | compra | sim | proximo | 9.41 | 3.87 | -1.00 | 2.653 | 0.385 | 2 | 2026-09-24 04:05 |
| LINK/USDT | B | venda | nao | proximo | 0.43 | 0.23 | -1.00 | 1.427 | 0.703 | 1 | 2026-09-23 23:05 |
| ETH/USDT | B | venda | sim | proximo | 3.35 | 2.28 | -1.00 | 2.552 | 0.304 | 2 | 2026-09-23 18:05 |
| SOL/USDT | B | venda | nao | proximo | 1.45 | 1.45 | -1.00 | 1.976 | 0.221 | 2 | 2026-09-23 18:05 |
| WLD/USDT | B | compra | sim | proximo | 9.15 | 4.59 | -1.00 | 1.479 | 0.722 | 7 | 2026-09-23 17:05 |
| LINK/USDT | B | compra | nao | proximo | 9.39 | 1.40 | -1.00 | 1.179 | 0.927 | 7 | 2026-09-23 17:05 |
| LINK/USDT | B | venda | nao | proximo | 0.90 | 0.09 | +0.09 | 0.134 | 0.359 | 1 | 2026-09-23 12:05 |
| XRP/USDT | A | compra | nao | proximo | — | — | -1.00 | 1.914 | 0.069 | 2 | 2026-09-23 04:05 |
| DOGE/USDT | A | compra | nao | proximo | 0.81 | 0.81 | -1.00 | 1.457 | 0.286 | 6 | 2026-09-23 00:05 |
| XRP/USDT | A | compra | nao | proximo | 1.87 | 0.13 | +0.13 | 0.177 | 0.61 | 1 | 2026-09-22 20:05 |
| SOL/USDT | A | compra | sim | proximo | 3.88 | 2.17 | +2.17 | 0.955 | 2.487 | 2 | 2026-09-22 19:05 |
