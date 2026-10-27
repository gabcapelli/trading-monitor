# Calibracao — registro mecanico de sinais (atualizado 2026-10-27 12:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 97 | 97 | 25 (26%) | -4.04R (-0.042R/sinal) |
| Descartados por R:R baixo | 464 | 464 | 292 (63%) | -20.30R (-0.044R/sinal) |
| TODOS | 561 | 561 | 317 (57%) | -24.34R (-0.043R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=317, mediana 0.34R, maximo 0.99R, 8% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=244, mediana 0.36R, 21% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| DOGE/USDT | B | compra | nao | proximo | 0.22 | 0.21 | +0.21 | 0.783 | 0.211 | 2 | 2026-10-27 10:06 |
| XRP/USDT | B | compra | nao | proximo | 0.81 | 0.31 | +0.31 | 0.146 | 0.446 | 1 | 2026-10-27 08:06 |
| DOGE/USDT | B | compra | nao | proximo | 0.97 | 0.18 | +0.18 | 0.178 | 0.246 | 1 | 2026-10-27 08:06 |
| UNI/USDT | B | compra | nao | proximo | 0.55 | 0.31 | +0.31 | 0.246 | 0.382 | 1 | 2026-10-27 08:06 |
| LINK/USDT | B | compra | nao | proximo | 0.53 | 0.47 | +0.47 | 0.435 | 0.716 | 2 | 2026-10-27 08:06 |
| BTC/USDT | B | compra | sim | proximo | 2.88 | 2.88 | -1.00 | 1.16 | 0.119 | 1 | 2026-10-27 06:06 |
| ETH/USDT | B | compra | nao | proximo | 1.77 | 1.77 | -1.00 | 1.35 | 0.081 | 1 | 2026-10-27 03:06 |
| UNI/USDT | B | compra | nao | proximo | 1.76 | 0.04 | +0.04 | 0.744 | 0.117 | 1 | 2026-10-27 03:06 |
| DOGE/USDT | B | venda | nao | proximo | 3.63 | 1.19 | +1.19 | 0.183 | 2.043 | 2 | 2026-10-26 23:06 |
| XRP/USDT | B | compra | nao | proximo | 0.08 | 0.08 | +0.08 | 0.024 | 0.194 | 1 | 2026-10-26 21:06 |
| DOGE/USDT | B | compra | nao | proximo | 0.52 | 0.01 | +0.01 | 0.033 | 0.289 | 1 | 2026-10-26 21:06 |
| BTC/USDT | B | compra | nao | proximo | 2.71 | 1.72 | -1.00 | 1.345 | 0.336 | 2 | 2026-10-26 19:06 |
| XRP/USDT | B | compra | nao | proximo | 1.89 | 0.37 | +0.37 | 0.633 | 0.422 | 1 | 2026-10-26 19:06 |
| DOGE/USDT | B | compra | nao | proximo | 2.16 | 0.37 | +0.37 | 0.51 | 0.394 | 1 | 2026-10-26 19:06 |
| SOL/USDT | A | venda | nao | proximo | 1.00 | 1.00 | -1.00 | 1.632 | 0.423 | 1 | 2026-10-26 18:06 |
| ETH/USDT | B | compra | sim | proximo | 3.07 | 2.33 | -1.00 | 1.477 | 0.158 | 1 | 2026-10-26 17:06 |
| DOGE/USDT | B | compra | nao | proximo | 0.10 | 0.10 | +0.10 | 0.179 | 0.26 | 1 | 2026-10-26 12:06 |
| UNI/USDT | B | compra | nao | proximo | 0.05 | 0.05 | +0.05 | 0.08 | 0.511 | 1 | 2026-10-26 12:06 |
| SOL/USDT | B | compra | nao | proximo | 0.67 | 0.67 | -1.00 | 1.108 | 0.262 | 4 | 2026-10-26 02:06 |
| UNI/USDT | B | compra | nao | proximo | 0.98 | 0.93 | +0.93 | 0.209 | 1.671 | 4 | 2026-10-26 02:06 |
| XRP/USDT | A | venda | nao | proximo | 1.74 | 0.34 | -1.00 | 1.218 | 0.038 | 2 | 2026-10-26 01:06 |
| ETH/USDT | A | venda | nao | proximo | 1.26 | 1.26 | -1.00 | 1.031 | 0.675 | 2 | 2026-10-26 00:06 |
| SOL/USDT | B | compra | nao | proximo | 1.47 | 1.47 | -1.00 | 2.317 | 0.277 | 1 | 2026-10-25 22:06 |
| DOGE/USDT | B | compra | nao | proximo | 1.53 | 1.53 | -1.00 | 2.457 | 0.243 | 1 | 2026-10-25 22:06 |
| UNI/USDT | B | compra | nao | proximo | 1.39 | 1.39 | -1.00 | 2.312 | 0.182 | 1 | 2026-10-25 22:06 |
