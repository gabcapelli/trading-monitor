# Calibracao — registro mecanico de sinais (atualizado 2026-10-25 14:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 95 | 95 | 25 (26%) | -2.04R (-0.021R/sinal) |
| Descartados por R:R baixo | 441 | 440 | 278 (63%) | -14.91R (-0.034R/sinal) |
| TODOS | 536 | 535 | 303 (57%) | -16.95R (-0.032R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=303, mediana 0.34R, maximo 0.99R, 8% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=232, mediana 0.39R, 22% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| WLD/USDT | B | compra | nao | proximo | 1.53 | 1.16 | aberto | — | — | — | 2026-10-25 14:06 |
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
| ETH/USDT | B | compra | nao | proximo | 0.16 | 0.16 | -1.00 | 1.88 | 0.18 | 1 | 2026-10-23 11:06 |
| SUI/USDT | B | compra | nao | proximo | 0.40 | 0.40 | -1.00 | 2.395 | 0.147 | 1 | 2026-10-23 11:06 |
| ETH/USDT | B | compra | nao | proximo | 0.83 | 0.01 | +0.01 | 0.719 | 0.135 | 1 | 2026-10-23 09:15 |
| XRP/USDT | B | compra | nao | proximo | 1.68 | 0.20 | +0.20 | 0.822 | 0.218 | 1 | 2026-10-23 09:15 |
| SUI/USDT | B | compra | nao | proximo | 0.83 | 0.09 | +0.09 | 0.314 | 0.404 | 1 | 2026-10-23 09:15 |
| DOGE/USDT | B | venda | nao | proximo | 3.46 | 1.11 | +1.11 | 0.895 | 1.691 | 4 | 2026-10-23 08:06 |
| WLD/USDT | B | venda | nao | proximo | 0.21 | 0.21 | +0.21 | 0.253 | 0.262 | 1 | 2026-10-23 07:06 |
