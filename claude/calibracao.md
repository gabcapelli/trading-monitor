# Calibracao — registro mecanico de sinais (atualizado 2026-11-25 22:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 136 | 136 | 42 (31%) | +21.94R (+0.161R/sinal) |
| Descartados por R:R baixo | 711 | 706 | 448 (63%) | -31.26R (-0.044R/sinal) |
| TODOS | 847 | 842 | 490 (58%) | -9.32R (-0.011R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=490, mediana 0.33R, maximo 0.99R, 8% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=352, mediana 0.39R, 19% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ETH/USDT | A | compra | nao | proximo | 1.68 | 0.26 | +0.26 | 0.902 | 1.426 | 1 | 2026-11-25 20:06 |
| ARB/USDT | A | compra | nao | proximo | 0.74 | 0.74 | +0.74 | 0.269 | 1.196 | 1 | 2026-11-25 20:06 |
| WLD/USDT | B | venda | nao | proximo | 5.11 | 1.19 | -1.00 | 1.495 | 0.536 | 3 | 2026-11-25 19:06 |
| SUI/USDT | B | venda | nao | proximo | 9.10 | 1.27 | -1.00 | 3.841 | 0.441 | 3 | 2026-11-25 19:06 |
| ARB/USDT | B | compra | nao | proximo | 4.50 | 1.70 | +1.70 | 0.519 | 3.046 | 4 | 2026-11-25 18:06 |
| DOGE/USDT | B | compra | nao | proximo | 0.67 | 0.51 | +0.51 | 0.203 | 2.167 | 1 | 2026-11-25 16:06 |
| BTC/USDT | B | compra | nao | proximo | 0.40 | 0.40 | +0.40 | 0.101 | 0.407 | 1 | 2026-11-25 15:06 |
| XRP/USDT | B | compra | nao | proximo | 0.12 | 0.12 | +0.12 | 0.12 | 0.315 | 1 | 2026-11-25 15:06 |
| LINK/USDT | B | compra | nao | proximo | 1.29 | 0.15 | +0.15 | 0.186 | 2.049 | 1 | 2026-11-25 14:06 |
| XRP/USDT | B | compra | nao | proximo | 1.36 | 0.80 | +0.80 | 0.694 | 1.376 | 3 | 2026-11-25 12:06 |
| LINK/USDT | B | compra | nao | proximo | 0.85 | 0.04 | +0.04 | 0.456 | 0.476 | 1 | 2026-11-25 12:06 |
| ETH/USDT | B | compra | nao | proximo | 3.04 | 0.72 | -1.00 | 1.856 | 0.54 | 1 | 2026-11-25 10:06 |
| SOL/USDT | B | compra | sim | proximo | 4.10 | 3.19 | -1.00 | 2.215 | 0.295 | 1 | 2026-11-25 10:06 |
| LINK/USDT | B | compra | nao | proximo | 2.92 | 0.28 | -1.00 | 1.928 | 0.506 | 1 | 2026-11-25 10:06 |
| BTC/USDT | B | compra | nao | proximo | 0.91 | 0.91 | -1.00 | 1.299 | 0.021 | 3 | 2026-11-25 06:06 |
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
