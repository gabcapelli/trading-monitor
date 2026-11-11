# Calibracao — registro mecanico de sinais (atualizado 2026-11-11 16:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 117 | 116 | 34 (29%) | +13.49R (+0.116R/sinal) |
| Descartados por R:R baixo | 633 | 632 | 400 (63%) | -28.50R (-0.045R/sinal) |
| TODOS | 750 | 748 | 434 (58%) | -15.01R (-0.020R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=434, mediana 0.32R, maximo 0.99R, 7% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=314, mediana 0.38R, 20% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ARB/USDT | B | venda | nao | proximo | 0.56 | 0.56 | aberto | 0.118 | 0.249 | — | 2026-11-11 15:06 |
| SUI/USDT | B | compra | nao | proximo | 0.18 | 0.18 | +0.18 | 0.106 | 0.339 | 1 | 2026-11-11 13:06 |
| SUI/USDT | B | compra | nao | proximo | 0.28 | 0.28 | +0.28 | 0.824 | 0.309 | 1 | 2026-11-11 11:06 |
| SUI/USDT | B | compra | nao | proximo | 0.54 | 0.54 | -1.00 | 1.068 | 0.093 | 1 | 2026-11-11 09:06 |
| SUI/USDT | B | compra | nao | proximo | 1.00 | 1.00 | +1.00 | 0.323 | 1.029 | 5 | 2026-11-11 07:06 |
| ARB/USDT | B | compra | sim | proximo | 4.69 | 3.16 | aberto | 0.496 | 1.801 | — | 2026-11-11 05:06 |
| ARB/USDT | B | venda | nao | proximo | 3.72 | 0.04 | +0.04 | 0.143 | 2.06 | 1 | 2026-11-11 03:06 |
| ARB/USDT | B | venda | nao | proximo | 3.60 | 0.13 | +0.13 | 0.158 | 0.942 | 1 | 2026-11-11 01:06 |
| ARB/USDT | B | compra | sim | proximo | 3.57 | 2.83 | +2.83 | 0.005 | 2.888 | 4 | 2026-11-10 19:06 |
| UNI/USDT | B | compra | sim | proximo | 5.57 | 3.37 | -1.00 | 1.312 | 0.737 | 4 | 2026-11-10 17:06 |
| WLD/USDT | B | compra | sim | proximo | 2.74 | 2.74 | +2.74 | 0.537 | 3.15 | 22 | 2026-11-10 15:06 |
| SUI/USDT | B | compra | sim | proximo | 3.78 | 3.02 | +3.02 | 0.269 | 3.558 | 22 | 2026-11-10 15:06 |
| ARB/USDT | B | venda | nao | proximo | 0.27 | 0.00 | +0.00 | 0.151 | 0.799 | 1 | 2026-11-10 13:06 |
| BTC/USDT | A | venda | nao | proximo | 0.01 | 0.01 | +0.01 | 0.621 | 0.132 | 1 | 2026-11-10 11:06 |
| LINK/USDT | A | venda | nao | proximo | 0.72 | 0.72 | +0.72 | 0.962 | 1.186 | 2 | 2026-11-10 11:06 |
| UNI/USDT | B | compra | nao | proximo | 2.41 | 0.15 | -1.00 | 2.518 | 0.929 | 1 | 2026-11-10 10:06 |
| ETH/USDT | A | venda | nao | proximo | 0.52 | 0.52 | -1.00 | 1.157 | 4.037 | 3 | 2026-11-10 08:06 |
| XRP/USDT | A | venda | nao | proximo | 0.55 | 0.03 | +0.03 | 0.345 | 0.751 | 1 | 2026-11-10 08:06 |
| ARB/USDT | B | venda | nao | proximo | 1.01 | 1.01 | +1.01 | 0.0 | 2.697 | 1 | 2026-11-10 04:06 |
| SUI/USDT | B | compra | nao | proximo | 3.89 | 1.64 | -1.00 | 1.431 | 0.927 | 5 | 2026-11-10 02:06 |
| UNI/USDT | B | compra | nao | proximo | 3.03 | 0.82 | +0.82 | 0.035 | 2.12 | 1 | 2026-11-10 02:06 |
| SUI/USDT | A | venda | nao | proximo | 6.12 | 0.05 | +0.05 | 0.21 | 0.684 | 1 | 2026-11-09 23:06 |
| UNI/USDT | B | compra | nao | proximo | 1.46 | 0.35 | +0.35 | 0.066 | 0.837 | 1 | 2026-11-09 22:06 |
| UNI/USDT | A | compra | nao | proximo | 1.89 | 0.21 | +0.21 | 0.656 | 0.4 | 2 | 2026-11-09 17:06 |
| UNI/USDT | B | compra | nao | proximo | 0.11 | 0.06 | +0.06 | 0.391 | 1.062 | 1 | 2026-11-09 15:06 |
