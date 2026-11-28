# Calibracao — registro mecanico de sinais (atualizado 2026-11-28 09:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 141 | 141 | 44 (31%) | +25.64R (+0.182R/sinal) |
| Descartados por R:R baixo | 736 | 729 | 461 (63%) | -35.81R (-0.049R/sinal) |
| TODOS | 877 | 870 | 505 (58%) | -10.17R (-0.012R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=505, mediana 0.33R, maximo 0.99R, 8% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=365, mediana 0.38R, 19% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ETH/USDT | B | compra | sim | proximo | 3.53 | 3.53 | -1.00 | 1.955 | 0.27 | 1 | 2026-11-28 07:06 |
| SOL/USDT | B | compra | nao | proximo | 2.70 | 0.03 | -1.00 | 2.132 | 0.219 | 1 | 2026-11-28 04:06 |
| UNI/USDT | B | compra | nao | proximo | 3.85 | 0.80 | aberto | 0.602 | 0.549 | — | 2026-11-28 04:06 |
| XRP/USDT | B | compra | nao | proximo | 0.89 | 0.89 | -1.00 | 1.996 | 0.521 | 2 | 2026-11-28 01:06 |
| DOGE/USDT | B | compra | nao | proximo | 0.92 | 0.92 | -1.00 | 1.09 | 0.223 | 1 | 2026-11-28 01:06 |
| XRP/USDT | B | compra | nao | proximo | 0.05 | 0.05 | +0.05 | 0.724 | 0.256 | 1 | 2026-11-27 23:06 |
| DOGE/USDT | B | compra | nao | proximo | 0.25 | 0.25 | +0.25 | 0.959 | 0.329 | 1 | 2026-11-27 23:06 |
| SOL/USDT | B | venda | nao | proximo | 6.65 | 0.57 | +0.57 | 0.498 | 1.992 | 2 | 2026-11-27 18:06 |
| SOL/USDT | B | compra | nao | proximo | 2.16 | 0.70 | -1.00 | 1.336 | 0.473 | 12 | 2026-11-27 15:06 |
| DOGE/USDT | B | compra | nao | proximo | 1.58 | 1.58 | -1.00 | 1.738 | 0.311 | 12 | 2026-11-27 15:06 |
| ARB/USDT | B | venda | nao | proximo | 1.99 | 1.73 | +1.73 | 0.848 | 1.949 | 12 | 2026-11-27 14:06 |
| ETH/USDT | B | compra | nao | proximo | 2.02 | 0.40 | aberto | 0.801 | 0.374 | — | 2026-11-27 13:06 |
| WLD/USDT | B | compra | nao | proximo | 1.72 | 0.06 | +0.06 | 0.105 | 0.359 | 1 | 2026-11-27 13:06 |
| SOL/USDT | B | venda | nao | proximo | 0.03 | 0.03 | +0.03 | 0.533 | 0.313 | 1 | 2026-11-27 12:06 |
| XRP/USDT | B | venda | sim | proximo | 5.19 | 4.30 | +4.30 | 0.272 | 5.868 | 3 | 2026-11-27 09:06 |
| XRP/USDT | B | venda | sim | proximo | 2.90 | 2.40 | +2.40 | 0.803 | 3.272 | 6 | 2026-11-27 06:06 |
| SUI/USDT | B | venda | nao | proximo | 3.14 | 0.53 | +0.53 | 0.05 | 0.701 | 1 | 2026-11-26 20:06 |
| WLD/USDT | B | compra | nao | proximo | 1.78 | 1.09 | -1.00 | 2.118 | 0.615 | 2 | 2026-11-26 18:06 |
| ARB/USDT | B | venda | nao | proximo | 2.99 | 0.54 | -1.00 | 1.088 | 0.211 | 2 | 2026-11-26 17:06 |
| XRP/USDT | B | compra | sim | proximo | 2.62 | 2.13 | -1.00 | 1.741 | 1.448 | 7 | 2026-11-26 14:06 |
| BTC/USDT | B | venda | nao | proximo | 1.31 | 0.74 | +0.74 | 0.0 | 2.979 | 1 | 2026-11-26 12:06 |
| LINK/USDT | B | venda | nao | proximo | 0.43 | 0.43 | +0.43 | 0.159 | 1.403 | 1 | 2026-11-26 12:06 |
| BTC/USDT | B | compra | nao | proximo | 1.61 | 1.06 | -1.00 | 2.956 | 1.021 | 4 | 2026-11-26 09:06 |
| WLD/USDT | B | compra | nao | proximo | 0.31 | 0.10 | +0.10 | 0.524 | 0.454 | 1 | 2026-11-26 09:06 |
| WLD/USDT | B | venda | nao | proximo | 0.50 | 0.50 | -1.00 | 1.06 | 0.076 | 2 | 2026-11-26 04:06 |
