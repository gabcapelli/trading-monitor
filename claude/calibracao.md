# Calibracao — registro mecanico de sinais (atualizado 2026-09-10 18:36 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 22 | 21 | 2 (10%) | -14.48R (-0.689R/sinal) |
| Descartados por R:R baixo | 6 | 6 | 5 (83%) | +1.59R (+0.265R/sinal) |
| TODOS | 28 | 27 | 7 (26%) | -12.89R (-0.477R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=7, mediana 0.43R, maximo 0.98R, 43% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=20, mediana 0.36R, 30% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|
| XRP/USDT | B | compra | sim | 8.40 | 4.46 | -1.00 | 1.38 | 0.042 | 1 | 2026-09-10 15:05 |
| ETH/USDT | B | compra | sim | 2.20 | 1.04 | aberto | 0.607 | 1.698 | — | 2026-09-10 12:05 |
| XRP/USDT | B | compra | sim | 4.48 | 2.27 | -1.00 | 1.285 | 0.268 | 3 | 2026-09-10 11:06 |
| LINK/USDT | B | venda | sim | 2.11 | 0.72 | -1.00 | 1.099 | 0.359 | 4 | 2026-09-10 05:06 |
| SOL/USDT | B | compra | sim | 4.48 | 0.13 | -1.00 | 1.165 | 0.082 | 1 | 2026-09-10 03:05 |
| BTC/USDT | B | venda | sim | 2.17 | 0.24 | +2.17 | 0.821 | 2.43 | 8 | 2026-09-10 01:05 |
| LINK/USDT | B | venda | sim | 2.89 | 1.23 | -1.00 | 1.017 | 0.565 | 3 | 2026-09-10 01:05 |
| XRP/USDT | B | compra | sim | 3.61 | 0.79 | -1.00 | 1.159 | 0.206 | 5 | 2026-09-10 00:05 |
| ETH/USDT | A | venda | sim | 2.63 | 0.02 | -1.00 | 1.639 | 1.158 | 1 | 2026-09-09 22:05 |
| ETH/USDT | B | compra | sim | 2.38 | 0.69 | -1.00 | 1.367 | 0.032 | 2 | 2026-09-09 18:05 |
| SOL/USDT | B | compra | sim | 2.70 | 1.85 | -1.00 | 2.784 | 0.059 | 2 | 2026-09-09 18:05 |
| XRP/USDT | B | compra | sim | 3.36 | 0.36 | -1.00 | 1.119 | 0.009 | 1 | 2026-09-09 18:05 |
| SUI/USDT | B | compra | sim | 4.33 | 0.82 | -1.00 | 1.516 | 0.03 | 1 | 2026-09-09 18:05 |
| XRP/USDT | B | venda | sim | 3.05 | 1.23 | -1.00 | 1.119 | 1.011 | 9 | 2026-09-08 17:05 |
| DOGE/USDT | B | venda | sim | 2.34 | 0.42 | -1.00 | 1.071 | 0.919 | 7 | 2026-09-08 15:05 |
| UNI/USDT | B | compra | sim | 2.17 | 0.40 | -1.00 | 1.358 | 0.049 | 3 | 2026-09-08 13:05 |
| ETH/USDT | B | compra | nao | 0.49 | 0.01 | +0.49 | 0.187 | 0.529 | 1 | 2026-09-08 12:05 |
| BTC/USDT | B | venda | nao | 0.83 | — | -1.00 | 1.072 | 0.192 | 1 | 2026-09-08 11:06 |
| DOGE/USDT | B | venda | nao | 0.97 | 0.45 | +0.97 | 0.026 | 1.439 | 1 | 2026-09-08 09:05 |
| SUI/USDT | B | venda | nao | 0.08 | 0.08 | +0.08 | 0.43 | 0.401 | 1 | 2026-09-08 09:05 |
| ETH/USDT | B | venda | nao | 0.91 | 0.32 | +0.91 | 0.068 | 1.923 | 3 | 2026-09-08 08:05 |
| XRP/USDT | B | venda | sim | 2.36 | 0.56 | -1.00 | 1.538 | 1.99 | 3 | 2026-09-08 08:05 |
| XRP/USDT | B | compra | sim | 2.35 | 1.67 | +2.35 | 0.869 | 2.526 | 5 | 2026-09-08 06:05 |
| SOL/USDT | B | venda | nao | 0.15 | 0.15 | +0.15 | 0.978 | 0.221 | 1 | 2026-09-08 02:05 |
| DOGE/USDT | B | venda | sim | 2.17 | 0.90 | -1.00 | 1.289 | 0.654 | 1 | 2026-09-08 02:05 |
