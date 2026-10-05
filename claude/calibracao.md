# Calibracao — registro mecanico de sinais (atualizado 2026-10-05 14:05 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 71 | 70 | 18 (26%) | -3.28R (-0.047R/sinal) |
| Descartados por R:R baixo | 264 | 262 | 171 (65%) | +0.50R (+0.002R/sinal) |
| TODOS | 335 | 332 | 189 (57%) | -2.78R (-0.008R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=189, mediana 0.35R, maximo 0.98R, 8% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=143, mediana 0.41R, 22% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| LINK/USDT | B | compra | sim | proximo | 4.57 | 3.14 | aberto | — | — | — | 2026-10-05 14:05 |
| SOL/USDT | B | venda | nao | proximo | 0.36 | 0.36 | +0.36 | 0.656 | 0.894 | 1 | 2026-10-05 13:05 |
| ETH/USDT | B | venda | nao | proximo | 0.34 | 0.16 | +0.16 | 0.071 | 0.309 | 1 | 2026-10-05 12:05 |
| DOGE/USDT | B | venda | nao | proximo | 1.06 | 0.44 | aberto | 0.2 | 0.429 | — | 2026-10-05 12:05 |
| ARB/USDT | B | venda | nao | proximo | 0.39 | 0.07 | +0.07 | 0.365 | 0.14 | 2 | 2026-10-05 12:05 |
| UNI/USDT | B | compra | nao | proximo | 1.44 | 0.46 | -1.00 | 1.781 | 0.48 | 1 | 2026-10-05 11:05 |
| ETH/USDT | B | venda | nao | proximo | 1.59 | 1.11 | -1.00 | 1.409 | 0.001 | 1 | 2026-10-05 10:05 |
| SOL/USDT | B | venda | nao | proximo | 0.80 | 0.80 | -1.00 | 1.187 | 0.331 | 1 | 2026-10-05 10:05 |
| DOGE/USDT | B | venda | nao | proximo | 1.23 | 0.11 | -1.00 | 1.199 | 2.264 | 2 | 2026-10-05 10:05 |
| ETH/USDT | B | compra | nao | proximo | 3.05 | 0.60 | +0.60 | 0.939 | 0.977 | 1 | 2026-10-05 08:05 |
| LINK/USDT | B | venda | nao | proximo | 1.06 | 0.02 | +0.02 | 0.301 | 0.237 | 1 | 2026-10-05 06:05 |
| BTC/USDT | A | compra | sim | proximo | 3.10 | 2.91 | -1.00 | 1.49 | 2.405 | 10 | 2026-10-05 03:05 |
| XRP/USDT | B | compra | nao | proximo | 2.76 | 0.28 | +0.28 | 0.0 | 1.532 | 1 | 2026-10-05 03:05 |
| DOGE/USDT | B | compra | nao | proximo | 4.72 | 0.39 | +0.39 | 0.0 | 2.033 | 1 | 2026-10-05 03:05 |
| UNI/USDT | A | compra | nao | proximo | 1.95 | 0.50 | +0.50 | 0.859 | 1.081 | 2 | 2026-10-04 22:05 |
| SUI/USDT | B | venda | nao | proximo | 1.85 | 1.80 | -1.00 | 1.302 | 0.013 | 1 | 2026-10-04 19:05 |
| LINK/USDT | B | venda | nao | proximo | 1.18 | 0.91 | -1.00 | 2.124 | 0.251 | 3 | 2026-10-04 17:05 |
| XRP/USDT | B | compra | nao | proximo | 2.02 | 0.53 | +0.53 | 0.026 | 1.996 | 1 | 2026-10-04 16:05 |
| ETH/USDT | B | venda | sim | proximo | 2.54 | 2.54 | -1.00 | 1.152 | 0.642 | 3 | 2026-10-04 15:05 |
| BTC/USDT | B | compra | nao | proximo | 0.68 | 0.68 | +0.68 | 0.241 | 1.03 | 1 | 2026-10-04 12:05 |
| SOL/USDT | A | compra | nao | proximo | 2.11 | 1.33 | -1.00 | 1.063 | 0.469 | 5 | 2026-10-04 12:05 |
| LINK/USDT | B | compra | nao | proximo | 0.02 | 0.02 | +0.02 | 0.365 | 0.584 | 1 | 2026-10-04 12:05 |
| ETH/USDT | B | venda | nao | proximo | 1.95 | 0.73 | -1.00 | 1.083 | 0.432 | 3 | 2026-10-04 10:05 |
| ARB/USDT | B | compra | nao | proximo | 3.45 | 1.95 | +1.95 | 0.535 | 2.021 | 5 | 2026-10-04 10:05 |
| LINK/USDT | B | compra | nao | proximo | 1.48 | 0.36 | +0.36 | 0.462 | 0.473 | 1 | 2026-10-04 10:05 |
