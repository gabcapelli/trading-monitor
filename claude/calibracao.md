# Calibracao — registro mecanico de sinais (atualizado 2026-09-18 18:05 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 47 | 47 | 8 (17%) | -19.36R (-0.412R/sinal) |
| Descartados por R:R baixo | 109 | 107 | 73 (68%) | +5.57R (+0.052R/sinal) |
| TODOS | 156 | 154 | 81 (53%) | -13.78R (-0.090R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=81, mediana 0.38R, maximo 0.98R, 11% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=73, mediana 0.36R, 25% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| LINK/USDT | B | compra | nao | proximo | — | — | aberto | 0.294 | 0.203 | — | 2026-09-18 17:05 |
| WLD/USDT | B | venda | nao | proximo | 1.80 | 0.83 | aberto | 0.373 | 0.176 | — | 2026-09-18 14:05 |
| LINK/USDT | B | venda | sim | proximo | 3.86 | 3.86 | -1.00 | 2.165 | 0.598 | 4 | 2026-09-18 13:05 |
| XRP/USDT | B | compra | nao | proximo | 2.25 | 0.02 | +0.02 | 0.014 | 0.945 | 1 | 2026-09-18 11:05 |
| BTC/USDT | B | compra | sim | proximo | 8.85 | 3.42 | +3.42 | 0.15 | 3.916 | 3 | 2026-09-18 04:05 |
| BTC/USDT | A | compra | sim | proximo | 5.17 | 2.05 | +2.05 | 0.416 | 2.332 | 5 | 2026-09-18 02:05 |
| DOGE/USDT | B | compra | nao | proximo | 1.84 | 0.13 | +0.13 | 0.547 | 0.194 | 1 | 2026-09-18 02:05 |
| ETH/USDT | B | compra | nao | proximo | 1.72 | 1.72 | +1.72 | 0.093 | 1.868 | 1 | 2026-09-18 00:05 |
| LINK/USDT | B | compra | nao | proximo | 0.33 | 0.28 | +0.28 | 0.129 | 2.082 | 1 | 2026-09-18 00:05 |
| DOGE/USDT | B | compra | nao | proximo | 0.20 | 0.20 | +0.20 | 0.233 | 0.933 | 1 | 2026-09-17 23:05 |
| BTC/USDT | B | compra | nao | proximo | 1.65 | 0.52 | +0.52 | 0.204 | 0.563 | 1 | 2026-09-17 22:05 |
| ETH/USDT | B | compra | nao | proximo | 2.56 | 0.54 | +0.54 | 0.212 | 0.869 | 1 | 2026-09-17 22:05 |
| WLD/USDT | B | compra | nao | proximo | 1.57 | 0.03 | +0.03 | 0.065 | 1.51 | 1 | 2026-09-17 22:05 |
| BTC/USDT | B | compra | nao | proximo | 3.52 | 0.73 | +0.73 | 0.66 | 0.806 | 2 | 2026-09-17 20:05 |
| WLD/USDT | B | compra | nao | proximo | 0.85 | 0.85 | +0.85 | 0.188 | 1.042 | 1 | 2026-09-17 20:05 |
| ARB/USDT | B | venda | nao | proximo | 1.92 | 1.77 | -1.00 | 1.406 | 0.363 | 3 | 2026-09-17 19:05 |
| ARB/USDT | B | venda | sim | proximo | 2.47 | 2.29 | -1.00 | 1.345 | 0.681 | 5 | 2026-09-17 17:05 |
| DOGE/USDT | B | compra | nao | proximo | 1.88 | 1.88 | -1.00 | 1.181 | 0.277 | 2 | 2026-09-17 14:05 |
| BTC/USDT | B | compra | nao | proximo | 0.70 | 0.70 | +0.70 | 0.959 | 1.49 | 12 | 2026-09-17 13:05 |
| SUI/USDT | A | compra | nao | proximo | 1.23 | 1.23 | +1.23 | 0.38 | 1.733 | 9 | 2026-09-17 13:05 |
| LINK/USDT | B | compra | nao | proximo | 0.24 | 0.24 | +0.24 | 0.425 | 0.328 | 2 | 2026-09-17 13:05 |
| UNI/USDT | B | venda | nao | proximo | 1.82 | 1.82 | -1.00 | 2.083 | 0.75 | 2 | 2026-09-17 12:05 |
| ETH/USDT | B | compra | nao | proximo | 0.81 | 0.81 | +0.81 | 0.811 | 0.971 | 16 | 2026-09-17 11:05 |
| ARB/USDT | B | compra | nao | proximo | 2.86 | 1.79 | +1.79 | 0.766 | 2.124 | 2 | 2026-09-17 11:05 |
| BTC/USDT | B | compra | nao | proximo | 0.85 | 0.28 | +0.28 | 0.226 | 1.993 | 1 | 2026-09-17 09:05 |
