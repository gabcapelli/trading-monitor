# Calibracao — registro mecanico de sinais (atualizado 2026-10-26 09:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 95 | 95 | 25 (26%) | -2.04R (-0.021R/sinal) |
| Descartados por R:R baixo | 448 | 448 | 279 (62%) | -20.98R (-0.047R/sinal) |
| TODOS | 543 | 543 | 304 (56%) | -23.02R (-0.042R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=304, mediana 0.34R, maximo 0.99R, 8% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=239, mediana 0.38R, 21% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SOL/USDT | B | compra | nao | proximo | 0.67 | 0.67 | -1.00 | 1.108 | 0.262 | 4 | 2026-10-26 02:06 |
| UNI/USDT | B | compra | nao | proximo | 0.98 | 0.93 | +0.93 | 0.209 | 1.671 | 4 | 2026-10-26 02:06 |
| XRP/USDT | A | venda | nao | proximo | 1.74 | 0.34 | -1.00 | 1.218 | 0.038 | 2 | 2026-10-26 01:06 |
| ETH/USDT | A | venda | nao | proximo | 1.26 | 1.26 | -1.00 | 1.031 | 0.675 | 2 | 2026-10-26 00:06 |
| SOL/USDT | B | compra | nao | proximo | 1.47 | 1.47 | -1.00 | 2.317 | 0.277 | 1 | 2026-10-25 22:06 |
| DOGE/USDT | B | compra | nao | proximo | 1.53 | 1.53 | -1.00 | 2.457 | 0.243 | 1 | 2026-10-25 22:06 |
| UNI/USDT | B | compra | nao | proximo | 1.39 | 1.39 | -1.00 | 2.312 | 0.182 | 1 | 2026-10-25 22:06 |
| WLD/USDT | B | compra | nao | proximo | 1.53 | 1.16 | -1.00 | 1.517 | 0.468 | 5 | 2026-10-25 14:06 |
| SUI/USDT | A | venda | nao | proximo | — | — | -1.00 | 2.476 | 0.067 | 1 | 2026-10-25 08:06 |
| ARB/USDT | A | venda | nao | proximo | 0.20 | 0.20 | +0.20 | 0.302 | 0.302 | 1 | 2026-10-25 06:06 |
| WLD/USDT | B | compra | nao | proximo | 1.66 | 0.98 | -1.00 | 7.951 | 0.023 | 1 | 2026-10-25 05:06 |
| XRP/USDT | B | compra | nao | proximo | 0.10 | 0.10 | +0.10 | 0.113 | 0.363 | 1 | 2026-10-24 16:06 |
| XRP/USDT | B | compra | nao | proximo | 0.73 | 0.73 | +0.73 | 0.248 | 0.804 | 2 | 2026-10-24 14:06 |
| WLD/USDT | B | compra | nao | proximo | 1.23 | 1.23 | -1.00 | 1.002 | 0.013 | 1 | 2026-10-24 14:06 |
| LINK/USDT | A | venda | nao | proximo | 0.27 | 0.27 | -1.00 | 1.148 | 0.549 | 1 | 2026-10-24 09:06 |
| XRP/USDT | B | compra | nao | proximo | 1.99 | 1.99 | -1.00 | 1.513 | 0.868 | 1 | 2026-10-24 04:06 |
| WLD/USDT | B | compra | sim | proximo | 6.96 | 2.20 | -1.00 | 1.891 | 0.326 | 5 | 2026-10-24 00:06 |
| SOL/USDT | B | compra | sim | proximo | 5.21 | 3.46 | -1.00 | 1.121 | 1.062 | 5 | 2026-10-23 23:06 |
| XRP/USDT | B | compra | nao | proximo | 5.07 | 1.95 | -1.00 | 1.169 | 0.753 | 6 | 2026-10-23 23:06 |
| UNI/USDT | A | venda | nao | proximo | 0.05 | 0.05 | -1.00 | 1.309 | 0.01 | 2 | 2026-10-23 22:06 |
| LINK/USDT | A | venda | nao | proximo | 2.10 | 0.40 | -1.00 | 1.158 | 0.0 | 2 | 2026-10-23 22:06 |
| XRP/USDT | B | compra | nao | proximo | 2.16 | 0.66 | -1.00 | 1.194 | 0.088 | 9 | 2026-10-23 21:06 |
| ETH/USDT | B | compra | nao | proximo | 1.68 | 0.15 | +0.15 | 0.495 | 0.436 | 1 | 2026-10-23 18:06 |
| DOGE/USDT | B | compra | nao | proximo | 4.09 | 1.31 | -1.00 | 5.544 | 0.846 | 2 | 2026-10-23 18:06 |
| SOL/USDT | B | venda | nao | proximo | 3.02 | 1.96 | +1.96 | 0.0 | 2.875 | 2 | 2026-10-23 15:06 |
