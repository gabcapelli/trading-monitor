# Calibracao — registro mecanico de sinais (atualizado 2026-11-06 08:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 107 | 107 | 30 (28%) | +6.80R (+0.064R/sinal) |
| Descartados por R:R baixo | 586 | 584 | 370 (63%) | -24.87R (-0.043R/sinal) |
| TODOS | 693 | 691 | 400 (58%) | -18.07R (-0.026R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=400, mediana 0.33R, maximo 0.99R, 7% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=291, mediana 0.38R, 20% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| DOGE/USDT | B | compra | nao | proximo | 0.11 | 0.11 | aberto | 0.301 | 0.079 | — | 2026-11-06 07:06 |
| UNI/USDT | B | compra | nao | proximo | 0.52 | 0.52 | +0.52 | 0.601 | 0.897 | 1 | 2026-11-06 04:06 |
| UNI/USDT | B | venda | nao | proximo | 2.46 | 0.46 | +0.46 | 0.186 | 0.646 | 1 | 2026-11-06 02:06 |
| SOL/USDT | B | compra | nao | proximo | 0.09 | 0.09 | -1.00 | 1.206 | 0.164 | 1 | 2026-11-06 00:06 |
| UNI/USDT | B | compra | nao | proximo | 8.95 | 0.56 | -1.00 | 1.405 | 0.205 | 3 | 2026-11-06 00:06 |
| ARB/USDT | B | compra | nao | proximo | 0.53 | 0.41 | +0.41 | 0.264 | 0.811 | 1 | 2026-11-05 23:06 |
| BTC/USDT | B | compra | nao | proximo | 4.75 | 1.26 | aberto | 0.804 | 0.354 | — | 2026-11-05 21:06 |
| UNI/USDT | B | compra | sim | proximo | 8.97 | 2.06 | +2.06 | 0.018 | 2.306 | 8 | 2026-11-05 21:06 |
| DOGE/USDT | B | compra | nao | proximo | 4.52 | 2.00 | -1.00 | 1.161 | 0.266 | 3 | 2026-11-05 17:06 |
| SUI/USDT | B | compra | nao | proximo | 5.39 | 1.46 | -1.00 | 1.339 | 0.182 | 2 | 2026-11-05 17:06 |
| UNI/USDT | B | compra | sim | proximo | 11.54 | 2.18 | -1.00 | 1.206 | 0.482 | 2 | 2026-11-05 15:06 |
| SUI/USDT | B | venda | nao | proximo | 0.88 | 0.27 | +0.27 | 0.024 | 1.474 | 1 | 2026-11-05 12:06 |
| ETH/USDT | B | venda | sim | proximo | 7.08 | 7.08 | +7.08 | 0.276 | 13.766 | 2 | 2026-11-05 11:06 |
| SOL/USDT | B | venda | nao | proximo | 0.81 | 0.03 | +0.03 | 0.239 | 0.12 | 1 | 2026-11-05 10:06 |
| SUI/USDT | B | venda | nao | proximo | 0.94 | 0.90 | +0.90 | 0.345 | 2.171 | 2 | 2026-11-05 10:06 |
| SOL/USDT | B | venda | sim | proximo | 2.23 | 2.23 | +2.23 | 0.495 | 3.894 | 2 | 2026-11-05 08:06 |
| LINK/USDT | B | venda | nao | proximo | 1.11 | 1.10 | +1.10 | 0.381 | 2.567 | 2 | 2026-11-05 08:06 |
| ARB/USDT | B | compra | nao | proximo | 0.18 | 0.08 | -1.00 | 1.68 | 0.077 | 4 | 2026-11-05 06:06 |
| ARB/USDT | B | compra | nao | proximo | 0.60 | 0.09 | +0.09 | 0.631 | 0.204 | 1 | 2026-11-05 04:06 |
| ETH/USDT | B | venda | nao | proximo | 1.00 | 1.00 | -1.00 | 1.169 | 0.105 | 1 | 2026-11-05 03:06 |
| SOL/USDT | B | venda | nao | proximo | 2.05 | 0.27 | -1.00 | 1.038 | 0.173 | 2 | 2026-11-05 03:06 |
| ARB/USDT | B | compra | nao | proximo | 1.56 | 0.05 | +0.05 | 0.925 | 0.167 | 1 | 2026-11-05 02:06 |
| SOL/USDT | B | venda | nao | proximo | 2.00 | 0.73 | +0.73 | 0.847 | 1.426 | 9 | 2026-11-05 01:06 |
| ARB/USDT | B | compra | nao | proximo | 2.01 | 0.20 | +0.20 | 0.326 | 1.446 | 1 | 2026-11-05 00:06 |
| XRP/USDT | B | compra | nao | proximo | 0.57 | 0.57 | +0.57 | 0.284 | 0.664 | 2 | 2026-11-04 23:06 |
