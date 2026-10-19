# Calibracao — registro mecanico de sinais (atualizado 2026-10-19 09:05 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 85 | 85 | 21 (25%) | -6.84R (-0.080R/sinal) |
| Descartados por R:R baixo | 367 | 365 | 238 (65%) | +1.17R (+0.003R/sinal) |
| TODOS | 452 | 450 | 259 (58%) | -5.67R (-0.013R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=259, mediana 0.35R, maximo 0.99R, 8% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=191, mediana 0.42R, 22% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| UNI/USDT | B | venda | nao | proximo | 11.44 | 0.36 | +0.36 | 0.571 | 0.438 | 1 | 2026-10-19 06:05 |
| BTC/USDT | B | venda | nao | proximo | 4.15 | 1.57 | aberto | 0.757 | 1.22 | — | 2026-10-19 05:05 |
| ETH/USDT | B | venda | nao | proximo | 5.46 | 0.36 | +0.36 | 0.867 | 0.823 | 3 | 2026-10-19 05:05 |
| XRP/USDT | B | compra | nao | proximo | 0.53 | 0.53 | +0.53 | 0.257 | 1.349 | 2 | 2026-10-19 03:05 |
| LINK/USDT | B | compra | nao | proximo | 1.11 | 1.11 | -1.00 | 1.626 | 1.103 | 5 | 2026-10-19 03:05 |
| SOL/USDT | B | venda | nao | proximo | 12.27 | 1.69 | -1.00 | 1.922 | 0.379 | 1 | 2026-10-19 01:05 |
| LINK/USDT | B | compra | nao | proximo | 1.87 | 1.70 | -1.00 | 1.371 | 0.805 | 9 | 2026-10-18 23:05 |
| LINK/USDT | B | compra | nao | proximo | 0.34 | 0.34 | +0.34 | 0.301 | 0.969 | 1 | 2026-10-18 21:05 |
| BTC/USDT | B | compra | sim | proximo | 3.90 | 2.16 | +2.16 | 0.154 | 2.542 | 2 | 2026-10-18 18:05 |
| ARB/USDT | B | compra | nao | proximo | 2.51 | 1.84 | -1.00 | 3.071 | 0.654 | 3 | 2026-10-18 14:05 |
| BTC/USDT | B | compra | sim | proximo | 5.51 | 2.62 | -1.00 | 1.851 | 0.539 | 4 | 2026-10-18 13:05 |
| SOL/USDT | A | venda | nao | proximo | 0.91 | 0.49 | +0.49 | 0.397 | 1.715 | 5 | 2026-10-18 12:05 |
| UNI/USDT | A | venda | nao | proximo | 0.35 | 0.15 | +0.15 | 0.278 | 0.692 | 1 | 2026-10-18 12:05 |
| WLD/USDT | B | venda | nao | proximo | 2.05 | 0.71 | +0.71 | 0.172 | 0.729 | 1 | 2026-10-18 08:05 |
| LINK/USDT | B | compra | nao | proximo | 0.42 | 0.42 | -1.00 | 2.295 | 0.133 | 4 | 2026-10-18 07:05 |
| ARB/USDT | B | compra | nao | proximo | 3.94 | 0.73 | +0.73 | 0.62 | 0.745 | 3 | 2026-10-17 20:06 |
| DOGE/USDT | B | compra | sim | proximo | 2.16 | 2.16 | -1.00 | 8.863 | 1.151 | 2 | 2026-10-17 17:06 |
| LINK/USDT | B | compra | sim | proximo | 5.74 | 5.40 | -1.00 | 6.017 | 0.982 | 2 | 2026-10-17 17:06 |
| LINK/USDT | B | compra | sim | proximo | 3.60 | 3.45 | -1.00 | 1.707 | 1.453 | 4 | 2026-10-17 15:06 |
| SUI/USDT | B | compra | nao | proximo | 1.36 | 1.36 | -1.00 | 1.945 | 0.221 | 2 | 2026-10-17 08:06 |
| ARB/USDT | B | venda | nao | proximo | 8.57 | 1.90 | +1.90 | 0.655 | 2.059 | 4 | 2026-10-17 07:06 |
| WLD/USDT | B | venda | nao | proximo | 4.00 | 1.99 | +1.99 | 0.398 | 2.982 | 7 | 2026-10-17 03:06 |
| ARB/USDT | B | compra | nao | proximo | 6.13 | 0.14 | +0.14 | 0.31 | 1.011 | 1 | 2026-10-17 01:06 |
| UNI/USDT | B | compra | nao | proximo | 0.15 | 0.03 | +0.03 | 0.5 | 0.272 | 1 | 2026-10-17 01:06 |
| ARB/USDT | B | venda | nao | proximo | 0.20 | 0.20 | +0.20 | 0.215 | 0.426 | 1 | 2026-10-16 22:06 |
