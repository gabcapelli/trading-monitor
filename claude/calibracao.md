# Calibracao — registro mecanico de sinais (atualizado 2026-09-16 19:05 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 40 | 39 | 4 (10%) | -25.93R (-0.665R/sinal) |
| Descartados por R:R baixo | 81 | 80 | 54 (68%) | +2.86R (+0.036R/sinal) |
| TODOS | 121 | 119 | 58 (49%) | -23.07R (-0.194R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=58, mediana 0.38R, maximo 0.98R, 10% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=61, mediana 0.27R, 26% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| LINK/USDT | B | compra | sim | proximo | 3.73 | 3.73 | aberto | 0.907 | 0.053 | — | 2026-09-16 18:05 |
| DOGE/USDT | B | compra | nao | proximo | 0.25 | 0.25 | +0.25 | 0.106 | 0.312 | 1 | 2026-09-16 17:05 |
| SUI/USDT | B | compra | nao | proximo | 0.54 | 0.37 | +0.37 | 0.094 | 0.62 | 1 | 2026-09-16 17:05 |
| UNI/USDT | B | compra | nao | proximo | 1.38 | 0.19 | +0.19 | 0.346 | 0.846 | 1 | 2026-09-16 13:05 |
| XRP/USDT | A | venda | nao | proximo | 0.27 | 0.27 | +0.27 | 0.728 | 0.615 | 1 | 2026-09-16 12:05 |
| BTC/USDT | B | compra | sim | proximo | 2.74 | 2.43 | -1.00 | 1.119 | 0.145 | 1 | 2026-09-16 09:05 |
| LINK/USDT | B | compra | sim | proximo | 6.22 | 6.22 | -1.00 | 1.578 | 0.046 | 1 | 2026-09-16 09:05 |
| DOGE/USDT | B | compra | nao | proximo | 1.85 | 1.85 | -1.00 | 2.219 | 0.914 | 2 | 2026-09-16 08:05 |
| BTC/USDT | B | compra | nao | proximo | 0.37 | 0.37 | -1.00 | 1.164 | 0.267 | 1 | 2026-09-16 04:05 |
| SOL/USDT | B | compra | sim | proximo | 6.56 | 4.51 | -1.00 | 1.674 | 0.246 | 2 | 2026-09-16 04:05 |
| ARB/USDT | B | venda | nao | proximo | 3.84 | 0.58 | -1.00 | 1.046 | 0.28 | 3 | 2026-09-15 22:05 |
| SOL/USDT | B | compra | sim | proximo | 4.29 | 3.03 | -1.00 | 1.05 | 1.181 | 19 | 2026-09-15 20:05 |
| LINK/USDT | B | compra | sim | proximo | 5.09 | 5.09 | -1.00 | 1.295 | 0.893 | 3 | 2026-09-15 20:05 |
| BTC/USDT | B | compra | sim | proximo | 2.34 | 2.34 | -1.00 | 1.303 | 0.141 | 1 | 2026-09-15 17:05 |
| ETH/USDT | B | compra | sim | proximo | 3.21 | 2.63 | -1.00 | 1.001 | 0.11 | 1 | 2026-09-15 17:05 |
| BTC/USDT | B | compra | nao | proximo | 0.33 | 0.33 | -1.00 | 2.462 | 0.307 | 1 | 2026-09-15 15:05 |
| ETH/USDT | B | compra | nao | proximo | 1.52 | 1.10 | -1.00 | 2.705 | 0.206 | 1 | 2026-09-15 15:05 |
| SUI/USDT | B | compra | nao | proximo | 0.57 | 0.32 | -1.00 | 3.071 | 0.122 | 1 | 2026-09-15 15:05 |
| BTC/USDT | B | compra | nao | proximo | 0.99 | 0.99 | +0.99 | 0.435 | 1.168 | 2 | 2026-09-15 13:05 |
| SOL/USDT | B | compra | nao | proximo | 5.94 | 0.84 | +0.84 | 0.75 | 1.457 | 2 | 2026-09-15 13:05 |
| LINK/USDT | B | compra | nao | proximo | 2.50 | 1.45 | -1.00 | 3.358 | 1.001 | 3 | 2026-09-15 13:05 |
| WLD/USDT | A | venda | nao | proximo | — | — | aberto | 0.754 | 1.573 | — | 2026-09-15 12:05 |
| UNI/USDT | B | venda | nao | proximo | 0.16 | 0.02 | +0.02 | 0.451 | 0.053 | 1 | 2026-09-15 12:05 |
| DOGE/USDT | B | compra | nao | proximo | 3.45 | 1.45 | -1.00 | 2.58 | 0.135 | 1 | 2026-09-15 11:05 |
| ETH/USDT | B | compra | nao | proximo | 9.09 | 0.49 | +0.49 | 0.374 | 0.633 | 2 | 2026-09-15 06:05 |
