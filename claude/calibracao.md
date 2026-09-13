# Calibracao — registro mecanico de sinais (atualizado 2026-09-13 12:05 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 30 | 29 | 4 (14%) | -15.93R (-0.549R/sinal) |
| Descartados por R:R baixo | 36 | 36 | 27 (75%) | +6.72R (+0.187R/sinal) |
| TODOS | 66 | 65 | 31 (48%) | -9.21R (-0.142R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=31, mediana 0.38R, maximo 0.98R, 10% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=34, mediana 0.56R, 29% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SOL/USDT | B | compra | nao | proximo | 3.23 | 0.07 | +0.07 | 0.0 | 1.061 | 1 | 2026-09-13 11:05 |
| WLD/USDT | B | venda | nao | proximo | 0.70 | 0.70 | -1.00 | 1.366 | 0.445 | 3 | 2026-09-13 08:05 |
| XRP/USDT | A | venda | sim | proximo | 2.35 | 2.35 | +2.35 | 0.336 | 2.61 | 1 | 2026-09-13 05:05 |
| LINK/USDT | A | venda | nao | proximo | 4.63 | 0.82 | +0.82 | 0.55 | 3.527 | 1 | 2026-09-13 05:05 |
| ETH/USDT | B | venda | nao | proximo | 1.45 | 1.45 | -1.00 | 1.033 | 0.003 | 1 | 2026-09-13 02:05 |
| SOL/USDT | B | compra | nao | proximo | 2.48 | 1.75 | -1.00 | 2.682 | 0.772 | 2 | 2026-09-13 02:05 |
| LINK/USDT | B | venda | nao | proximo | 1.51 | 0.48 | +0.48 | 0.695 | 1.299 | 1 | 2026-09-13 00:05 |
| LINK/USDT | B | venda | nao | proximo | 0.47 | 0.21 | -1.00 | 1.051 | 0.097 | 4 | 2026-09-12 20:05 |
| SUI/USDT | A | venda | nao | proximo | 0.29 | 0.29 | -1.00 | 1.221 | 0.212 | 1 | 2026-09-12 19:05 |
| XRP/USDT | A | venda | sim | proximo | 6.82 | 6.82 | -1.00 | 1.584 | 0.041 | 1 | 2026-09-12 17:05 |
| DOGE/USDT | B | compra | nao | proximo | 2.43 | 1.68 | -1.00 | 1.006 | 0.796 | 3 | 2026-09-12 17:05 |
| LINK/USDT | A | venda | nao | proximo | 0.54 | 0.13 | -1.00 | 1.008 | 0.228 | 1 | 2026-09-12 17:05 |
| UNI/USDT | B | venda | sim | proximo | 6.19 | 6.03 | -1.00 | 1.152 | 0.634 | 2 | 2026-09-12 16:05 |
| UNI/USDT | B | venda | sim | proximo | 2.29 | 2.24 | aberto | 0.594 | 1.276 | — | 2026-09-12 14:05 |
| SOL/USDT | B | compra | nao | proximo | 4.25 | 1.84 | +1.84 | 0.369 | 2.156 | 7 | 2026-09-12 03:05 |
| ETH/USDT | B | venda | nao | proximo | 4.43 | 1.96 | +1.96 | 0.779 | 1.968 | 36 | 2026-09-11 18:06 |
| ETH/USDT | B | venda | nao | proximo | 2.96 | 1.42 | +1.42 | 0.318 | 1.423 | 38 | 2026-09-11 16:06 |
| DOGE/USDT | B | venda | nao | proximo | 2.52 | 0.28 | +0.28 | 0.063 | 1.327 | 1 | 2026-09-11 15:06 |
| LINK/USDT | B | venda | nao | proximo | 3.75 | 0.93 | +0.93 | 0.151 | 1.533 | 1 | 2026-09-11 15:06 |
| XRP/USDT | B | venda | nao | proximo | 1.76 | 0.95 | +0.95 | 0.302 | 1.08 | 42 | 2026-09-11 13:06 |
| DOGE/USDT | B | venda | nao | proximo | 1.40 | 0.16 | +0.16 | 0.478 | 0.742 | 3 | 2026-09-11 13:06 |
| ARB/USDT | B | venda | nao | proximo | 0.91 | 0.69 | +0.69 | 0.377 | 0.708 | 3 | 2026-09-11 13:06 |
| SOL/USDT | B | venda | nao | proximo | 1.75 | 0.05 | +0.05 | 0.13 | 0.768 | 1 | 2026-09-11 12:06 |
| SUI/USDT | B | venda | nao | proximo | 1.39 | 0.94 | +0.94 | 0.447 | 0.949 | 1 | 2026-09-11 12:06 |
| UNI/USDT | B | venda | nao | proximo | 1.76 | 0.54 | +0.54 | 0.346 | 0.93 | 1 | 2026-09-11 12:06 |
