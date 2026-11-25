# Calibracao — registro mecanico de sinais (atualizado 2026-11-25 08:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 135 | 135 | 42 (31%) | +22.94R (+0.170R/sinal) |
| Descartados por R:R baixo | 698 | 692 | 439 (63%) | -30.97R (-0.045R/sinal) |
| TODOS | 833 | 827 | 481 (58%) | -8.03R (-0.010R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=481, mediana 0.33R, maximo 0.99R, 7% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=346, mediana 0.38R, 19% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| BTC/USDT | B | compra | nao | proximo | 0.91 | 0.91 | aberto | 0.858 | 0.021 | — | 2026-11-25 06:06 |
| ETH/USDT | B | compra | nao | proximo | 1.40 | 1.40 | -1.00 | 1.851 | 0.165 | 4 | 2026-11-25 01:06 |
| SOL/USDT | B | compra | nao | proximo | 0.84 | 0.31 | -1.00 | 1.09 | 0.098 | 2 | 2026-11-25 01:06 |
| ARB/USDT | B | compra | sim | proximo | 4.68 | 2.45 | -1.00 | 1.257 | 0.605 | 6 | 2026-11-25 01:06 |
| WLD/USDT | B | compra | nao | proximo | 1.05 | 1.05 | -1.00 | 1.526 | 0.54 | 4 | 2026-11-25 01:06 |
| SUI/USDT | B | compra | nao | proximo | 0.95 | 0.82 | -1.00 | 1.328 | 0.517 | 4 | 2026-11-25 01:06 |
| XRP/USDT | B | compra | nao | proximo | 1.28 | 0.01 | +0.01 | 0.39 | 0.755 | 1 | 2026-11-25 00:06 |
| SOL/USDT | B | compra | nao | proximo | 4.13 | 1.16 | -1.00 | 1.713 | 0.184 | 3 | 2026-11-24 20:06 |
| SOL/USDT | B | compra | nao | proximo | 4.17 | 0.05 | +0.05 | 0.376 | 0.322 | 1 | 2026-11-24 15:06 |
| ARB/USDT | B | compra | nao | proximo | 2.85 | 0.98 | -1.00 | 1.073 | 0.39 | 2 | 2026-11-24 15:06 |
| SOL/USDT | B | compra | nao | proximo | 1.73 | 0.10 | -1.00 | 1.269 | 0.087 | 2 | 2026-11-24 09:06 |
| XRP/USDT | B | compra | nao | proximo | 7.16 | 1.25 | -1.00 | 1.028 | 0.052 | 1 | 2026-11-24 03:06 |
| DOGE/USDT | B | compra | nao | proximo | 4.65 | 1.85 | -1.00 | 1.017 | 0.961 | 7 | 2026-11-24 01:06 |
| LINK/USDT | B | compra | nao | proximo | 3.25 | 0.27 | +0.27 | 0.112 | 0.528 | 1 | 2026-11-24 01:06 |
| SOL/USDT | B | venda | nao | proximo | 0.77 | 0.66 | +0.66 | 0.866 | 0.682 | 8 | 2026-11-24 00:06 |
| SUI/USDT | B | compra | sim | proximo | 6.36 | 2.99 | -1.00 | 1.027 | 0.931 | 3 | 2026-11-23 21:06 |
| SOL/USDT | B | venda | nao | proximo | 1.72 | 0.40 | +0.40 | 0.594 | 1.04 | 1 | 2026-11-23 16:06 |
| SOL/USDT | B | venda | sim | proximo | 2.80 | 2.02 | +2.02 | 0.182 | 2.398 | 4 | 2026-11-23 13:06 |
| LINK/USDT | B | venda | nao | proximo | 2.05 | 0.55 | +0.55 | 0.348 | 0.913 | 3 | 2026-11-23 12:06 |
| ETH/USDT | B | compra | nao | proximo | 0.08 | 0.08 | +0.08 | 0.413 | 0.377 | 1 | 2026-11-23 11:06 |
| XRP/USDT | B | compra | nao | proximo | 0.18 | 0.06 | +0.06 | 0.275 | 0.734 | 1 | 2026-11-23 11:06 |
| LINK/USDT | B | compra | nao | proximo | 1.32 | 1.32 | +1.32 | 0.331 | 1.546 | 1 | 2026-11-23 08:06 |
| UNI/USDT | B | venda | nao | proximo | 2.30 | 0.41 | +0.41 | 0.696 | 0.58 | 3 | 2026-11-23 07:06 |
| XRP/USDT | B | compra | sim | proximo | 4.81 | 4.25 | +4.25 | 0.79 | 7.346 | 5 | 2026-11-23 06:06 |
| SUI/USDT | A | compra | nao | proximo | 0.46 | 0.46 | +0.46 | 0.675 | 0.82 | 1 | 2026-11-23 05:06 |
