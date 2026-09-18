# Calibracao — registro mecanico de sinais (atualizado 2026-09-17 21:05 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 44 | 43 | 6 (14%) | -22.83R (-0.531R/sinal) |
| Descartados por R:R baixo | 99 | 94 | 61 (65%) | -0.32R (-0.003R/sinal) |
| TODOS | 143 | 137 | 67 (49%) | -23.15R (-0.169R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=67, mediana 0.38R, maximo 0.98R, 10% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=70, mediana 0.34R, 26% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| BTC/USDT | B | compra | nao | proximo | 3.52 | 0.73 | aberto | 0.173 | 0.421 | — | 2026-09-17 20:05 |
| WLD/USDT | B | compra | nao | proximo | 0.85 | 0.85 | +0.85 | 0.188 | 1.042 | 1 | 2026-09-17 20:05 |
| ARB/USDT | B | venda | nao | proximo | 1.92 | 1.77 | aberto | 0.649 | 0.363 | — | 2026-09-17 19:05 |
| ARB/USDT | B | venda | sim | proximo | 2.47 | 2.29 | aberto | 0.804 | 0.681 | — | 2026-09-17 17:05 |
| DOGE/USDT | B | compra | nao | proximo | 1.88 | 1.88 | -1.00 | 1.181 | 0.277 | 2 | 2026-09-17 14:05 |
| BTC/USDT | B | compra | nao | proximo | 0.70 | 0.70 | aberto | 0.959 | 0.339 | — | 2026-09-17 13:05 |
| SUI/USDT | A | compra | nao | proximo | 1.23 | 1.23 | aberto | 0.38 | 0.794 | — | 2026-09-17 13:05 |
| LINK/USDT | B | compra | nao | proximo | 0.24 | 0.24 | +0.24 | 0.425 | 0.328 | 2 | 2026-09-17 13:05 |
| UNI/USDT | B | venda | nao | proximo | 1.82 | 1.82 | -1.00 | 2.083 | 0.75 | 2 | 2026-09-17 12:05 |
| ETH/USDT | B | compra | nao | proximo | 0.81 | 0.81 | aberto | 0.787 | 0.674 | — | 2026-09-17 11:05 |
| ARB/USDT | B | compra | nao | proximo | 2.86 | 1.79 | +1.79 | 0.766 | 2.124 | 2 | 2026-09-17 11:05 |
| BTC/USDT | B | compra | nao | proximo | 0.85 | 0.28 | +0.28 | 0.226 | 1.993 | 1 | 2026-09-17 09:05 |
| UNI/USDT | B | venda | nao | proximo | 1.23 | 1.23 | -1.00 | 2.169 | 0.633 | 4 | 2026-09-17 07:05 |
| SOL/USDT | B | compra | nao | proximo | 1.98 | 1.98 | -1.00 | 1.538 | 1.0 | 2 | 2026-09-17 06:05 |
| WLD/USDT | B | compra | nao | proximo | 0.38 | 0.38 | -1.00 | 1.326 | 0.341 | 1 | 2026-09-17 06:05 |
| UNI/USDT | B | venda | sim | proximo | 6.48 | 2.02 | -1.00 | 1.02 | 0.778 | 2 | 2026-09-17 03:05 |
| LINK/USDT | B | compra | sim | proximo | 2.46 | 2.46 | +2.46 | 0.433 | 2.614 | 10 | 2026-09-17 02:05 |
| UNI/USDT | B | compra | nao | proximo | 0.43 | 0.07 | +0.07 | 0.442 | 0.929 | 1 | 2026-09-17 01:05 |
| BTC/USDT | B | compra | nao | proximo | 0.49 | 0.49 | +0.49 | 0.509 | 0.523 | 2 | 2026-09-17 00:05 |
| LINK/USDT | B | compra | sim | proximo | 2.64 | 2.64 | +2.64 | 0.823 | 2.795 | 12 | 2026-09-17 00:05 |
| WLD/USDT | B | venda | nao | proximo | 3.76 | 1.59 | -1.00 | 1.122 | 0.421 | 1 | 2026-09-16 22:05 |
| UNI/USDT | A | compra | nao | proximo | 0.37 | 0.09 | +0.09 | 0.211 | 0.229 | 1 | 2026-09-16 21:05 |
| LINK/USDT | B | compra | sim | proximo | 3.73 | 3.73 | -1.00 | 1.286 | 0.053 | 2 | 2026-09-16 18:05 |
| DOGE/USDT | B | compra | nao | proximo | 0.25 | 0.25 | +0.25 | 0.106 | 0.312 | 1 | 2026-09-16 17:05 |
| SUI/USDT | B | compra | nao | proximo | 0.54 | 0.37 | +0.37 | 0.094 | 0.62 | 1 | 2026-09-16 17:05 |
