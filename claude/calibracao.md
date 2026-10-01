# Calibracao — registro mecanico de sinais (atualizado 2026-10-01 12:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 62 | 62 | 14 (23%) | -10.61R (-0.171R/sinal) |
| Descartados por R:R baixo | 198 | 196 | 120 (61%) | -11.01R (-0.056R/sinal) |
| TODOS | 260 | 258 | 134 (52%) | -21.62R (-0.084R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=134, mediana 0.35R, maximo 0.98R, 9% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=124, mediana 0.35R, 23% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ETH/USDT | B | venda | nao | proximo | 0.95 | 0.45 | aberto | — | — | — | 2026-10-01 12:06 |
| BTC/USDT | B | compra | nao | proximo | 0.89 | 0.38 | +0.38 | 0.726 | 0.757 | 1 | 2026-10-01 11:06 |
| ETH/USDT | B | venda | nao | proximo | 0.91 | 0.49 | +0.49 | 0.61 | 0.538 | 2 | 2026-10-01 10:06 |
| LINK/USDT | B | venda | nao | proximo | 1.34 | 0.54 | +0.54 | 0.548 | 0.714 | 1 | 2026-10-01 10:06 |
| BTC/USDT | B | compra | nao | proximo | 0.71 | 0.27 | +0.27 | 0.871 | 0.593 | 4 | 2026-10-01 08:06 |
| BTC/USDT | B | compra | nao | proximo | 4.78 | 0.65 | +0.65 | 0.02 | 0.756 | 1 | 2026-10-01 06:06 |
| UNI/USDT | B | compra | nao | proximo | 0.60 | 0.11 | +0.11 | 0.176 | 0.319 | 1 | 2026-10-01 06:06 |
| ETH/USDT | B | venda | sim | proximo | 4.56 | 4.01 | +4.01 | 0.713 | 4.916 | 1 | 2026-10-01 04:06 |
| SOL/USDT | B | venda | nao | proximo | 3.08 | 1.65 | +1.65 | 0.335 | 4.126 | 1 | 2026-10-01 04:06 |
| LINK/USDT | B | venda | sim | proximo | 2.99 | 2.99 | +2.99 | 0.574 | 3.924 | 1 | 2026-10-01 04:06 |
| LINK/USDT | B | venda | nao | proximo | 1.73 | 1.73 | -1.00 | 1.062 | 0.564 | 2 | 2026-09-30 21:06 |
| UNI/USDT | B | compra | nao | proximo | 2.40 | 1.31 | -1.00 | 1.143 | 1.269 | 10 | 2026-09-30 20:06 |
| DOGE/USDT | B | venda | nao | proximo | 1.25 | 1.25 | -1.00 | 1.121 | 0.702 | 10 | 2026-09-30 15:06 |
| BTC/USDT | B | compra | nao | proximo | 0.85 | 0.01 | +0.01 | 0.017 | 0.661 | 1 | 2026-09-30 13:06 |
| SOL/USDT | B | venda | nao | proximo | 0.37 | 0.13 | +0.13 | 0.275 | 0.338 | 1 | 2026-09-30 12:06 |
| WLD/USDT | B | venda | nao | proximo | 4.54 | 1.79 | +1.79 | 0.623 | 1.804 | 18 | 2026-09-30 12:06 |
| BTC/USDT | A | compra | nao | proximo | 2.52 | 0.84 | +0.84 | 0.629 | 6.108 | 1 | 2026-09-30 09:06 |
| BTC/USDT | B | compra | nao | proximo | 0.36 | 0.36 | +0.36 | 0.0 | 0.529 | 1 | 2026-09-30 07:06 |
| ETH/USDT | B | compra | nao | proximo | 1.66 | 1.39 | +1.39 | 0.645 | 1.716 | 2 | 2026-09-30 05:06 |
| XRP/USDT | B | compra | nao | proximo | 5.13 | 0.08 | -1.00 | 1.06 | 0.298 | 1 | 2026-09-30 03:06 |
| SOL/USDT | B | venda | nao | proximo | 0.78 | 0.78 | +0.78 | 0.697 | 1.222 | 3 | 2026-09-30 01:06 |
| XRP/USDT | B | venda | nao | proximo | 0.77 | 0.77 | -1.00 | 1.187 | 0.088 | 2 | 2026-09-30 01:06 |
| LINK/USDT | B | venda | nao | proximo | 0.02 | 0.02 | +0.02 | 0.335 | 0.453 | 1 | 2026-09-29 22:06 |
| SOL/USDT | B | venda | nao | proximo | 2.87 | 0.73 | -1.00 | 1.011 | 0.337 | 4 | 2026-09-29 17:06 |
| SUI/USDT | B | compra | nao | proximo | 2.37 | 0.75 | +0.75 | 0.29 | 0.834 | 2 | 2026-09-29 16:06 |
