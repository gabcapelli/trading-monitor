# Calibracao — registro mecanico de sinais (atualizado 2026-09-11 10:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 26 | 26 | 3 (12%) | -16.28R (-0.626R/sinal) |
| Descartados por R:R baixo | 12 | 11 | 9 (82%) | +2.26R (+0.206R/sinal) |
| TODOS | 38 | 37 | 12 (32%) | -14.02R (-0.379R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=12, mediana 0.43R, maximo 0.98R, 25% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=25, mediana 0.64R, 40% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SUI/USDT | B | compra | nao | proximo | 0.08 | 0.08 | aberto | — | — | — | 2026-09-11 10:06 |
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
| XRP/USDT | B | compra | sim | recente | 4.48 | 2.27 | -1.00 | 1.285 | 0.268 | 3 | 2026-09-10 11:06 |
| LINK/USDT | B | venda | sim | recente | 2.11 | 0.72 | -1.00 | 1.099 | 0.359 | 4 | 2026-09-10 05:06 |
| SOL/USDT | B | compra | sim | recente | 4.48 | 0.13 | -1.00 | 1.165 | 0.082 | 1 | 2026-09-10 03:05 |
| BTC/USDT | B | venda | sim | recente | 2.17 | 0.24 | +2.17 | 0.821 | 2.43 | 8 | 2026-09-10 01:05 |
| LINK/USDT | B | venda | sim | recente | 2.89 | 1.23 | -1.00 | 1.017 | 0.565 | 3 | 2026-09-10 01:05 |
| XRP/USDT | B | compra | sim | recente | 3.61 | 0.79 | -1.00 | 1.159 | 0.206 | 5 | 2026-09-10 00:05 |
| ETH/USDT | A | venda | sim | recente | 2.63 | 0.02 | -1.00 | 1.639 | 1.158 | 1 | 2026-09-09 22:05 |
| ETH/USDT | B | compra | sim | recente | 2.38 | 0.69 | -1.00 | 1.367 | 0.032 | 2 | 2026-09-09 18:05 |
| SOL/USDT | B | compra | sim | recente | 2.70 | 1.85 | -1.00 | 2.784 | 0.059 | 2 | 2026-09-09 18:05 |
| XRP/USDT | B | compra | sim | recente | 3.36 | 0.36 | -1.00 | 1.119 | 0.009 | 1 | 2026-09-09 18:05 |
| SUI/USDT | B | compra | sim | recente | 4.33 | 0.82 | -1.00 | 1.516 | 0.03 | 1 | 2026-09-09 18:05 |
| XRP/USDT | B | venda | sim | recente | 3.05 | 1.23 | -1.00 | 1.119 | 1.011 | 9 | 2026-09-08 17:05 |
| DOGE/USDT | B | venda | sim | recente | 2.34 | 0.42 | -1.00 | 1.071 | 0.919 | 7 | 2026-09-08 15:05 |
