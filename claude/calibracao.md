# Calibracao — registro mecanico de sinais (atualizado 2026-11-19 15:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 125 | 125 | 38 (30%) | +17.76R (+0.142R/sinal) |
| Descartados por R:R baixo | 665 | 660 | 422 (64%) | -23.25R (-0.035R/sinal) |
| TODOS | 790 | 785 | 460 (59%) | -5.49R (-0.007R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=460, mediana 0.32R, maximo 0.99R, 7% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=325, mediana 0.37R, 20% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
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
| LINK/USDT | B | venda | nao | proximo | 2.39 | 1.91 | +1.91 | 0.221 | 4.015 | 1 | 2026-11-17 12:06 |
| ARB/USDT | A | venda | sim | proximo | 2.74 | 2.74 | -1.00 | 2.726 | 0.049 | 1 | 2026-11-15 23:06 |
| BTC/USDT | A | venda | nao | proximo | — | — | -1.00 | 1.516 | 1.197 | 6 | 2026-11-15 01:06 |
| ARB/USDT | A | venda | nao | proximo | — | — | aberto | 0.739 | 2.578 | — | 2026-11-14 14:06 |
| SUI/USDT | A | venda | nao | proximo | — | — | aberto | 0.163 | 3.503 | — | 2026-11-14 12:06 |
| WLD/USDT | A | venda | nao | proximo | — | — | aberto | 0.215 | 7.436 | — | 2026-11-14 10:06 |
| ARB/USDT | A | venda | nao | proximo | 0.86 | 0.86 | +0.86 | 0.026 | 1.183 | 1 | 2026-11-14 04:06 |
| ETH/USDT | A | venda | nao | proximo | — | — | -1.00 | 1.053 | 0.183 | 6 | 2026-11-14 01:06 |
| SUI/USDT | A | venda | nao | proximo | 0.69 | 0.69 | +0.69 | 0.989 | 1.093 | 10 | 2026-11-14 01:06 |
| UNI/USDT | A | venda | nao | proximo | — | — | aberto | 0.882 | 7.768 | — | 2026-11-14 01:06 |
| SUI/USDT | A | venda | nao | proximo | 0.48 | 0.48 | +0.48 | 0.069 | 3.083 | 1 | 2026-11-13 23:06 |
| XRP/USDT | A | venda | sim | proximo | 2.04 | 2.04 | +2.04 | 0.204 | 4.289 | 2 | 2026-11-13 22:06 |
