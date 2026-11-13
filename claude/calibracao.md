# Calibracao — registro mecanico de sinais (atualizado 2026-11-13 07:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 119 | 118 | 34 (29%) | +11.49R (+0.097R/sinal) |
| Descartados por R:R baixo | 645 | 644 | 408 (63%) | -29.51R (-0.046R/sinal) |
| TODOS | 764 | 762 | 442 (58%) | -18.02R (-0.024R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=442, mediana 0.32R, maximo 0.99R, 7% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=320, mediana 0.38R, 20% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SUI/USDT | B | compra | nao | proximo | 1.50 | 1.50 | aberto | — | — | — | 2026-11-13 07:06 |
| DOGE/USDT | A | venda | sim | proximo | 2.19 | 2.19 | aberto | 0.666 | 0.348 | — | 2026-11-13 05:06 |
| LINK/USDT | A | venda | nao | proximo | — | — | -1.00 | 1.896 | 0.353 | 2 | 2026-11-13 02:06 |
| SOL/USDT | A | venda | nao | proximo | — | — | -1.00 | 1.095 | 0.229 | 4 | 2026-11-13 01:06 |
| SUI/USDT | B | compra | sim | proximo | 2.94 | 2.94 | -1.00 | 1.113 | 0.609 | 1 | 2026-11-12 21:06 |
| SOL/USDT | A | venda | nao | proximo | 0.06 | 0.06 | +0.06 | 0.284 | 2.509 | 1 | 2026-11-12 10:06 |
| DOGE/USDT | A | venda | nao | proximo | 0.15 | 0.15 | +0.15 | 0.212 | 4.076 | 1 | 2026-11-12 10:06 |
| WLD/USDT | A | venda | nao | proximo | 0.18 | 0.18 | +0.18 | 0.613 | 1.354 | 1 | 2026-11-12 10:06 |
| BTC/USDT | A | venda | nao | proximo | 0.41 | 0.41 | +0.41 | 0.352 | 1.309 | 2 | 2026-11-12 09:06 |
| ARB/USDT | A | venda | nao | proximo | — | — | -1.00 | 1.904 | 4.302 | 10 | 2026-11-12 06:06 |
| XRP/USDT | A | venda | nao | proximo | 0.56 | 0.56 | +0.56 | 0.029 | 1.001 | 1 | 2026-11-12 02:06 |
| DOGE/USDT | A | venda | nao | proximo | 2.77 | 0.80 | +0.80 | 0.319 | 0.799 | 1 | 2026-11-12 01:06 |
| ARB/USDT | A | venda | nao | proximo | 0.27 | 0.27 | +0.27 | 0.333 | 1.481 | 1 | 2026-11-11 19:06 |
| SUI/USDT | A | compra | nao | proximo | 3.38 | 1.05 | -1.00 | 1.367 | 0.336 | 1 | 2026-11-11 18:06 |
| ARB/USDT | B | venda | nao | proximo | 0.56 | 0.56 | +0.56 | 0.118 | 0.901 | 4 | 2026-11-11 15:06 |
| SUI/USDT | B | compra | nao | proximo | 0.18 | 0.18 | +0.18 | 0.106 | 0.339 | 1 | 2026-11-11 13:06 |
| SUI/USDT | B | compra | nao | proximo | 0.28 | 0.28 | +0.28 | 0.824 | 0.309 | 1 | 2026-11-11 11:06 |
| SUI/USDT | B | compra | nao | proximo | 0.54 | 0.54 | -1.00 | 1.068 | 0.093 | 1 | 2026-11-11 09:06 |
| SUI/USDT | B | compra | nao | proximo | 1.00 | 1.00 | +1.00 | 0.323 | 1.029 | 5 | 2026-11-11 07:06 |
| ARB/USDT | B | compra | sim | proximo | 4.69 | 3.16 | -1.00 | 1.468 | 1.801 | 14 | 2026-11-11 05:06 |
| ARB/USDT | B | venda | nao | proximo | 3.72 | 0.04 | +0.04 | 0.143 | 2.06 | 1 | 2026-11-11 03:06 |
| ARB/USDT | B | venda | nao | proximo | 3.60 | 0.13 | +0.13 | 0.158 | 0.942 | 1 | 2026-11-11 01:06 |
| ARB/USDT | B | compra | sim | proximo | 3.57 | 2.83 | +2.83 | 0.005 | 2.888 | 4 | 2026-11-10 19:06 |
| UNI/USDT | B | compra | sim | proximo | 5.57 | 3.37 | -1.00 | 1.312 | 0.737 | 4 | 2026-11-10 17:06 |
| WLD/USDT | B | compra | sim | proximo | 2.74 | 2.74 | +2.74 | 0.537 | 3.15 | 22 | 2026-11-10 15:06 |
