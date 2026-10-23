# Calibracao — registro mecanico de sinais (atualizado 2026-10-23 06:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 93 | 93 | 25 (27%) | -0.04R (-0.000R/sinal) |
| Descartados por R:R baixo | 418 | 415 | 268 (65%) | -4.66R (-0.011R/sinal) |
| TODOS | 511 | 508 | 293 (58%) | -4.70R (-0.009R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=293, mediana 0.35R, maximo 0.99R, 8% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=215, mediana 0.39R, 22% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| DOGE/USDT | B | compra | nao | proximo | 0.06 | 0.06 | +0.06 | 0.361 | 0.722 | 1 | 2026-10-23 03:06 |
| UNI/USDT | B | compra | nao | proximo | 6.93 | 1.37 | aberto | 0.705 | 1.157 | — | 2026-10-23 03:06 |
| ETH/USDT | B | compra | nao | proximo | 0.07 | 0.06 | aberto | 0.838 | 0.041 | — | 2026-10-23 00:06 |
| UNI/USDT | B | compra | nao | proximo | 0.11 | 0.11 | +0.11 | 0.409 | 0.277 | 1 | 2026-10-23 00:06 |
| WLD/USDT | B | compra | nao | proximo | 2.64 | 0.92 | +0.92 | 0.303 | 2.109 | 2 | 2026-10-22 21:06 |
| UNI/USDT | B | compra | sim | proximo | 4.12 | 4.12 | +4.12 | 0.676 | 4.734 | 4 | 2026-10-22 21:06 |
| ARB/USDT | B | compra | nao | proximo | 3.40 | 0.52 | -1.00 | 1.368 | 0.103 | 1 | 2026-10-22 17:06 |
| BTC/USDT | B | compra | nao | proximo | 9.30 | 0.85 | +0.85 | 0.691 | 1.052 | 7 | 2026-10-22 16:06 |
| SOL/USDT | B | compra | nao | proximo | 2.98 | 1.33 | -1.00 | 1.046 | 0.568 | 2 | 2026-10-22 16:06 |
| DOGE/USDT | B | compra | sim | proximo | 2.56 | 2.24 | +2.24 | 0.764 | 2.255 | 8 | 2026-10-22 16:06 |
| UNI/USDT | B | compra | sim | proximo | 2.23 | 2.23 | +2.23 | 0.677 | 2.59 | 9 | 2026-10-22 16:06 |
| ETH/USDT | B | compra | nao | proximo | 6.20 | 0.38 | +0.38 | 0.558 | 0.388 | 1 | 2026-10-22 11:06 |
| SUI/USDT | B | compra | nao | proximo | 7.22 | 0.65 | -1.00 | 1.784 | 0.29 | 2 | 2026-10-22 11:06 |
| UNI/USDT | B | compra | nao | proximo | 5.85 | 0.46 | -1.00 | 1.345 | 0.364 | 2 | 2026-10-22 11:06 |
| SOL/USDT | B | compra | nao | proximo | 5.26 | 0.03 | +0.03 | 0.075 | 0.495 | 1 | 2026-10-22 07:06 |
| ARB/USDT | B | compra | nao | proximo | 10.42 | 1.03 | +1.03 | 0.071 | 1.606 | 1 | 2026-10-22 07:06 |
| UNI/USDT | B | compra | nao | proximo | 6.78 | 1.27 | -1.00 | 1.975 | 1.179 | 7 | 2026-10-22 07:06 |
| LINK/USDT | B | compra | nao | proximo | 9.83 | 0.30 | +0.30 | 0.117 | 0.572 | 1 | 2026-10-22 07:06 |
| WLD/USDT | B | compra | nao | proximo | 6.96 | 0.76 | +0.76 | 0.539 | 1.412 | 1 | 2026-10-22 06:06 |
| UNI/USDT | B | compra | nao | proximo | 8.52 | 1.05 | -1.00 | 1.107 | 0.098 | 1 | 2026-10-22 05:06 |
| LINK/USDT | B | compra | nao | proximo | 8.66 | 1.05 | -1.00 | 2.628 | 0.0 | 1 | 2026-10-22 05:06 |
| SOL/USDT | B | compra | nao | proximo | 7.38 | 0.16 | -1.00 | 1.839 | 0.184 | 1 | 2026-10-22 02:06 |
| SUI/USDT | B | compra | nao | proximo | 8.24 | 0.11 | -1.00 | 1.79 | 0.358 | 1 | 2026-10-22 02:06 |
| BTC/USDT | B | compra | nao | proximo | 6.58 | 0.83 | -1.00 | 1.558 | 0.223 | 3 | 2026-10-22 01:06 |
| WLD/USDT | B | venda | nao | proximo | 0.47 | 0.47 | +0.47 | 0.209 | 1.269 | 3 | 2026-10-21 23:06 |
