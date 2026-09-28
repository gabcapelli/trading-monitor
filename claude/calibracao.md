# Calibracao — registro mecanico de sinais (atualizado 2026-09-28 14:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 58 | 58 | 10 (17%) | -23.53R (-0.406R/sinal) |
| Descartados por R:R baixo | 165 | 163 | 98 (60%) | -14.49R (-0.089R/sinal) |
| TODOS | 223 | 221 | 108 (49%) | -38.02R (-0.172R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=108, mediana 0.37R, maximo 0.98R, 10% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=113, mediana 0.36R, 23% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| BTC/USDT | B | compra | nao | proximo | 2.66 | 1.25 | +1.25 | 0.19 | 1.351 | 1 | 2026-09-28 13:06 |
| UNI/USDT | B | compra | nao | proximo | 1.61 | 1.61 | aberto | 0.33 | 1.244 | — | 2026-09-28 13:06 |
| LINK/USDT | B | venda | nao | proximo | 1.16 | 0.35 | -1.00 | 1.894 | 0.221 | 2 | 2026-09-28 12:06 |
| BTC/USDT | B | compra | nao | proximo | 3.69 | 1.34 | -1.00 | 2.968 | 0.0 | 1 | 2026-09-28 11:06 |
| BTC/USDT | B | compra | sim | proximo | 10.54 | 5.73 | -1.00 | 3.077 | 4.079 | 3 | 2026-09-28 09:07 |
| SOL/USDT | B | compra | sim | proximo | 3.94 | 2.14 | -1.00 | 2.096 | 0.227 | 1 | 2026-09-28 02:06 |
| ARB/USDT | B | compra | nao | proximo | 5.00 | 1.46 | -1.00 | 1.08 | 0.249 | 1 | 2026-09-28 02:06 |
| SOL/USDT | A | compra | nao | proximo | 5.49 | 0.19 | +0.19 | 0.084 | 0.993 | 1 | 2026-09-27 13:06 |
| BTC/USDT | A | compra | nao | proximo | 0.85 | 0.05 | +0.05 | 0.372 | 0.456 | 1 | 2026-09-27 07:06 |
| ARB/USDT | A | compra | nao | proximo | 0.01 | 0.01 | +0.01 | 0.504 | 0.012 | 1 | 2026-09-27 07:06 |
| DOGE/USDT | B | compra | nao | proximo | 0.43 | 0.06 | +0.06 | 0.352 | 0.264 | 1 | 2026-09-27 05:06 |
| BTC/USDT | A | compra | nao | proximo | 3.53 | 0.59 | +0.59 | 0.789 | 0.854 | 4 | 2026-09-26 23:06 |
| ARB/USDT | B | venda | nao | proximo | 1.41 | 0.47 | +0.47 | 0.185 | 1.218 | 2 | 2026-09-26 16:06 |
| ARB/USDT | B | venda | nao | proximo | 1.98 | 1.17 | +1.17 | 0.046 | 1.82 | 4 | 2026-09-26 14:06 |
| LINK/USDT | A | compra | nao | proximo | — | — | -1.00 | 1.156 | 1.657 | 5 | 2026-09-26 11:06 |
| DOGE/USDT | B | compra | nao | proximo | 3.00 | 1.85 | -1.00 | 1.898 | 0.415 | 2 | 2026-09-26 05:06 |
| LINK/USDT | A | compra | nao | proximo | 0.96 | 0.96 | -1.00 | 1.381 | 0.949 | 2 | 2026-09-26 05:06 |
| WLD/USDT | B | venda | nao | proximo | 2.00 | 1.63 | -1.00 | 2.032 | 0.173 | 1 | 2026-09-25 19:05 |
| DOGE/USDT | B | compra | nao | proximo | 1.21 | 1.21 | -1.00 | 1.116 | 0.655 | 2 | 2026-09-25 17:05 |
| XRP/USDT | A | compra | nao | proximo | 2.49 | 0.34 | -1.00 | 1.07 | 0.194 | 1 | 2026-09-25 12:05 |
| WLD/USDT | B | venda | nao | proximo | 5.27 | 0.12 | -1.00 | 2.456 | 0.024 | 1 | 2026-09-25 08:05 |
| ETH/USDT | B | venda | nao | proximo | 0.10 | 0.10 | +0.10 | 0.171 | 0.167 | 1 | 2026-09-25 00:05 |
| ARB/USDT | B | venda | nao | proximo | 0.03 | 0.03 | +0.03 | 0.391 | 0.068 | 1 | 2026-09-25 00:05 |
| SUI/USDT | B | venda | nao | proximo | 0.27 | 0.14 | -1.00 | 1.275 | 0.06 | 7 | 2026-09-25 00:05 |
| WLD/USDT | B | venda | nao | proximo | 0.30 | 0.30 | +0.30 | 0.582 | 1.074 | 1 | 2026-09-24 23:05 |
