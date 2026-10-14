# Calibracao — registro mecanico de sinais (atualizado 2026-10-14 06:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 77 | 77 | 20 (26%) | -2.00R (-0.026R/sinal) |
| Descartados por R:R baixo | 331 | 328 | 215 (66%) | +2.83R (+0.009R/sinal) |
| TODOS | 408 | 405 | 235 (58%) | +0.83R (+0.002R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=235, mediana 0.35R, maximo 0.99R, 8% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=170, mediana 0.39R, 21% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| WLD/USDT | B | compra | nao | proximo | 1.97 | 1.97 | aberto | 0.55 | 1.757 | — | 2026-10-14 04:06 |
| ETH/USDT | B | venda | nao | proximo | 1.57 | 0.98 | +0.98 | 0.417 | 1.294 | 2 | 2026-10-14 01:06 |
| ARB/USDT | B | compra | sim | proximo | 2.47 | 2.47 | -1.00 | 1.573 | 0.967 | 4 | 2026-10-13 23:06 |
| ARB/USDT | A | compra | sim | proximo | 2.28 | 2.28 | -1.00 | 1.165 | 1.785 | 6 | 2026-10-13 21:06 |
| DOGE/USDT | B | compra | nao | proximo | 1.74 | 1.74 | -1.00 | 1.354 | 0.387 | 3 | 2026-10-13 18:05 |
| WLD/USDT | B | venda | nao | proximo | 2.97 | 1.35 | +1.35 | 0.621 | 1.449 | 9 | 2026-10-13 18:05 |
| DOGE/USDT | B | compra | nao | proximo | 1.03 | 1.03 | +1.03 | 0.539 | 1.079 | 6 | 2026-10-13 16:05 |
| ARB/USDT | B | compra | nao | proximo | 0.77 | 0.14 | +0.14 | 0.249 | 0.993 | 1 | 2026-10-13 16:05 |
| LINK/USDT | B | venda | nao | proximo | 2.14 | 0.18 | -1.00 | 1.082 | 0.104 | 1 | 2026-10-13 15:05 |
| UNI/USDT | B | compra | nao | proximo | 0.02 | 0.02 | +0.02 | 0.333 | 0.302 | 1 | 2026-10-13 12:05 |
| ETH/USDT | B | compra | nao | proximo | 2.26 | 0.52 | +0.52 | 0.519 | 1.129 | 1 | 2026-10-13 10:05 |
| SOL/USDT | B | compra | nao | proximo | 2.19 | 1.97 | aberto | 0.485 | 1.825 | — | 2026-10-13 10:05 |
| UNI/USDT | B | compra | nao | proximo | 1.49 | 0.34 | +0.34 | 0.451 | 0.673 | 1 | 2026-10-13 10:05 |
| LINK/USDT | B | compra | nao | proximo | 1.22 | 0.11 | +0.11 | 0.426 | 0.497 | 1 | 2026-10-13 10:05 |
| BTC/USDT | B | compra | nao | proximo | 2.36 | 1.70 | -1.00 | 1.588 | 1.523 | 3 | 2026-10-13 04:05 |
| SOL/USDT | B | compra | nao | proximo | 0.33 | 0.33 | +0.33 | 0.978 | 0.696 | 1 | 2026-10-13 04:05 |
| DOGE/USDT | B | compra | nao | proximo | 0.79 | 0.79 | -1.00 | 2.075 | 0.443 | 4 | 2026-10-13 03:05 |
| BTC/USDT | A | compra | nao | proximo | 3.53 | 0.26 | +0.26 | 0.276 | 1.779 | 1 | 2026-10-13 02:05 |
| SOL/USDT | B | compra | nao | proximo | 0.92 | 0.92 | +0.92 | 0.177 | 0.932 | 1 | 2026-10-13 02:05 |
| DOGE/USDT | B | compra | nao | proximo | 1.04 | 1.04 | -1.00 | 1.002 | 0.827 | 7 | 2026-10-13 01:05 |
| WLD/USDT | B | compra | nao | proximo | 4.44 | 0.62 | +0.62 | 0.047 | 0.748 | 1 | 2026-10-13 01:05 |
| LINK/USDT | B | compra | nao | proximo | 0.93 | 0.16 | +0.16 | 0.168 | 0.493 | 1 | 2026-10-13 01:05 |
| BTC/USDT | B | compra | nao | proximo | 0.41 | 0.03 | +0.03 | 0.253 | 1.239 | 1 | 2026-10-13 00:05 |
| XRP/USDT | B | compra | nao | proximo | 0.51 | 0.51 | +0.51 | 0.017 | 0.627 | 2 | 2026-10-12 23:05 |
| DOGE/USDT | B | compra | nao | proximo | 1.26 | 1.26 | +1.26 | 0.054 | 1.349 | 31 | 2026-10-12 23:05 |
