# Calibracao — registro mecanico de sinais (atualizado 2026-11-21 23:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 129 | 129 | 40 (31%) | +20.67R (+0.160R/sinal) |
| Descartados por R:R baixo | 673 | 667 | 425 (64%) | -25.34R (-0.038R/sinal) |
| TODOS | 802 | 796 | 465 (58%) | -4.67R (-0.006R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=465, mediana 0.32R, maximo 0.99R, 7% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=331, mediana 0.37R, 20% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SOL/USDT | B | compra | nao | proximo | 1.59 | 0.86 | aberto | 0.406 | 0.209 | — | 2026-11-21 11:06 |
| ARB/USDT | A | venda | sim | proximo | 2.16 | 2.16 | -1.00 | 2.165 | 0.042 | 1 | 2026-11-21 10:06 |
| SOL/USDT | B | compra | nao | proximo | 1.50 | 1.50 | +1.50 | 0.157 | 1.683 | 3 | 2026-11-21 07:06 |
| WLD/USDT | A | venda | nao | proximo | — | — | -1.00 | 1.07 | 0.555 | 8 | 2026-11-21 01:06 |
| SOL/USDT | B | compra | nao | proximo | 2.17 | 1.43 | -1.00 | 1.6 | 0.266 | 6 | 2026-11-20 19:06 |
| ARB/USDT | A | venda | sim | proximo | 2.77 | 2.77 | +2.77 | 0.088 | 5.026 | 7 | 2026-11-20 06:06 |
| SOL/USDT | B | venda | nao | proximo | 0.04 | 0.04 | +0.04 | 0.885 | 0.288 | 1 | 2026-11-20 02:06 |
| UNI/USDT | A | venda | sim | proximo | 2.14 | 2.14 | +2.14 | 0.884 | 4.463 | 12 | 2026-11-20 01:06 |
| XRP/USDT | B | compra | nao | proximo | 2.79 | 0.37 | +0.37 | 0.706 | 0.448 | 1 | 2026-11-20 00:06 |
| DOGE/USDT | B | compra | nao | proximo | 2.03 | 1.29 | -1.00 | 1.02 | 0.143 | 2 | 2026-11-20 00:06 |
| WLD/USDT | B | compra | sim | proximo | 4.90 | 3.62 | -1.00 | 1.789 | 0.817 | 11 | 2026-11-20 00:06 |
| LINK/USDT | B | compra | nao | proximo | 4.06 | 1.84 | -1.00 | 3.158 | 1.127 | 2 | 2026-11-19 21:06 |
| DOGE/USDT | A | compra | nao | proximo | 0.14 | 0.14 | +0.14 | 0.218 | 0.233 | 1 | 2026-11-19 10:06 |
| XRP/USDT | A | compra | nao | proximo | 2.04 | 0.62 | +0.62 | 0.473 | 0.843 | 5 | 2026-11-19 04:06 |
| WLD/USDT | B | compra | nao | proximo | 0.04 | 0.04 | +0.04 | 0.112 | 0.356 | 1 | 2026-11-19 01:06 |
| LINK/USDT | B | compra | nao | proximo | 0.08 | 0.08 | +0.08 | 0.094 | 0.346 | 1 | 2026-11-19 01:06 |
| DOGE/USDT | B | compra | nao | proximo | 1.15 | 0.44 | +0.44 | 0.721 | 0.791 | 5 | 2026-11-18 21:06 |
| BTC/USDT | A | venda | nao | proximo | 2.12 | 0.13 | +0.13 | 0.516 | 3.021 | 1 | 2026-11-18 11:06 |
| ETH/USDT | A | venda | nao | proximo | 3.31 | 0.28 | +0.28 | 0.656 | 2.948 | 1 | 2026-11-18 11:06 |
| ARB/USDT | A | venda | nao | proximo | 0.49 | 0.49 | +0.49 | 0.339 | 1.329 | 1 | 2026-11-18 11:06 |
| XRP/USDT | B | compra | sim | proximo | 4.94 | 4.94 | -1.00 | 1.106 | 0.637 | 1 | 2026-11-18 07:06 |
| DOGE/USDT | B | venda | sim | proximo | 5.11 | 2.60 | +2.60 | 0.306 | 2.817 | 15 | 2026-11-17 22:06 |
| SUI/USDT | B | venda | sim | proximo | 4.53 | 2.39 | +2.39 | 0.478 | 3.06 | 14 | 2026-11-17 22:06 |
| UNI/USDT | B | venda | nao | proximo | 0.92 | 0.59 | +0.59 | 0.013 | 0.652 | 1 | 2026-11-17 22:06 |
| XRP/USDT | B | venda | sim | proximo | 2.64 | 2.24 | +2.24 | 0.317 | 3.579 | 1 | 2026-11-17 12:06 |
