# Calibracao — registro mecanico de sinais (atualizado 2026-09-12 00:05 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 26 | 26 | 3 (12%) | -16.28R (-0.626R/sinal) |
| Descartados por R:R baixo | 25 | 22 | 20 (91%) | +6.17R (+0.280R/sinal) |
| TODOS | 51 | 48 | 23 (48%) | -10.11R (-0.211R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=23, mediana 0.38R, maximo 0.98R, 13% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=25, mediana 0.64R, 40% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ETH/USDT | B | venda | nao | proximo | 4.43 | 1.96 | aberto | 0.463 | 1.154 | — | 2026-09-11 18:06 |
| ETH/USDT | B | venda | nao | proximo | 2.96 | 1.42 | aberto | 0.318 | 0.915 | — | 2026-09-11 16:06 |
| DOGE/USDT | B | venda | nao | proximo | 2.52 | 0.28 | +0.28 | 0.063 | 1.327 | 1 | 2026-09-11 15:06 |
| LINK/USDT | B | venda | nao | proximo | 3.75 | 0.93 | +0.93 | 0.151 | 1.533 | 1 | 2026-09-11 15:06 |
| XRP/USDT | B | venda | nao | proximo | 1.76 | 0.95 | aberto | 0.302 | 0.853 | — | 2026-09-11 13:06 |
| DOGE/USDT | B | venda | nao | proximo | 1.40 | 0.16 | +0.16 | 0.478 | 0.742 | 3 | 2026-09-11 13:06 |
| ARB/USDT | B | venda | nao | proximo | 0.91 | 0.69 | +0.69 | 0.377 | 0.708 | 3 | 2026-09-11 13:06 |
| SOL/USDT | B | venda | nao | proximo | 1.75 | 0.05 | +0.05 | 0.13 | 0.768 | 1 | 2026-09-11 12:06 |
| SUI/USDT | B | venda | nao | proximo | 1.39 | 0.94 | +0.94 | 0.447 | 0.949 | 1 | 2026-09-11 12:06 |
| UNI/USDT | B | venda | nao | proximo | 1.76 | 0.54 | +0.54 | 0.346 | 0.93 | 1 | 2026-09-11 12:06 |
| LINK/USDT | B | venda | nao | proximo | 1.81 | 0.03 | +0.03 | 0.28 | 0.993 | 1 | 2026-09-11 12:06 |
| XRP/USDT | B | compra | nao | proximo | 0.38 | 0.15 | +0.15 | 0.467 | 0.274 | 1 | 2026-09-11 11:06 |
| WLD/USDT | A | compra | nao | proximo | 1.82 | 0.04 | +0.04 | 0.376 | 0.231 | 1 | 2026-09-11 11:06 |
| SUI/USDT | B | compra | nao | proximo | 0.08 | 0.08 | +0.08 | 0.409 | 0.653 | 1 | 2026-09-11 10:06 |
| UNI/USDT | B | venda | nao | proximo | 0.25 | 0.05 | +0.05 | 0.354 | 0.362 | 1 | 2026-09-11 08:06 |
| LINK/USDT | B | venda | nao | proximo | 0.50 | 0.50 | +0.50 | 0.426 | 0.939 | 1 | 2026-09-11 07:06 |
| DOGE/USDT | B | venda | sim | proximo | 2.30 | 2.30 | -1.00 | 3.913 | 3.775 | 5 | 2026-09-11 05:06 |
| LINK/USDT | B | venda | nao | proximo | 1.59 | 0.42 | +0.42 | 0.507 | 0.64 | 1 | 2026-09-11 04:05 |
| SUI/USDT | B | compra | sim | proximo | 6.15 | 6.15 | -1.00 | 1.643 | 1.023 | 6 | 2026-09-11 01:05 |
| SUI/USDT | B | compra | sim | proximo | 5.71 | 5.37 | -1.00 | 1.023 | 1.364 | 10 | 2026-09-10 22:05 |
| LINK/USDT | B | venda | nao | proximo | — | — | -1.00 | 1.188 | 0.64 | 5 | 2026-09-10 21:05 |
| UNI/USDT | B | venda | nao | proximo | 3.29 | 0.70 | +0.70 | 0.244 | 0.831 | 1 | 2026-09-10 20:05 |
| DOGE/USDT | B | venda | sim | recente | 4.95 | 4.95 | -1.00 | 4.85 | 6.399 | 15 | 2026-09-10 19:05 |
| XRP/USDT | B | compra | sim | recente | 8.40 | 4.46 | -1.00 | 1.38 | 0.042 | 1 | 2026-09-10 15:05 |
| ETH/USDT | B | compra | sim | recente | 2.20 | 1.04 | +2.20 | 0.607 | 2.206 | 18 | 2026-09-10 12:05 |
