# Calibracao — registro mecanico de sinais (atualizado 2026-10-20 06:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 87 | 86 | 21 (24%) | -7.84R (-0.091R/sinal) |
| Descartados por R:R baixo | 376 | 375 | 245 (65%) | +2.54R (+0.007R/sinal) |
| TODOS | 463 | 461 | 266 (58%) | -5.30R (-0.011R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=266, mediana 0.35R, maximo 0.99R, 8% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=195, mediana 0.42R, 23% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| WLD/USDT | B | venda | sim | proximo | 5.52 | 5.52 | aberto | 0.072 | 0.779 | — | 2026-10-20 05:06 |
| BTC/USDT | B | venda | nao | proximo | 4.10 | 0.69 | +0.69 | 0.092 | 1.776 | 1 | 2026-10-20 02:06 |
| UNI/USDT | B | venda | nao | proximo | 1.95 | 0.37 | +0.37 | 0.087 | 1.675 | 1 | 2026-10-20 02:06 |
| ARB/USDT | B | compra | nao | proximo | 0.15 | 0.05 | -1.00 | 1.045 | 0.016 | 2 | 2026-10-20 01:06 |
| ETH/USDT | B | compra | nao | proximo | 1.20 | 1.20 | -1.00 | 1.569 | 1.168 | 6 | 2026-10-20 00:06 |
| ARB/USDT | B | compra | nao | proximo | 0.96 | 0.29 | +0.29 | 0.916 | 0.375 | 1 | 2026-10-19 22:06 |
| LINK/USDT | A | venda | nao | proximo | 1.73 | 0.22 | +0.22 | 0.125 | 1.785 | 1 | 2026-10-19 22:06 |
| UNI/USDT | B | compra | nao | proximo | 3.87 | 0.80 | +0.80 | 0.0 | 2.568 | 1 | 2026-10-19 19:05 |
| ETH/USDT | B | compra | sim | proximo | 5.13 | 2.70 | -1.00 | 3.452 | 1.927 | 5 | 2026-10-19 18:05 |
| SOL/USDT | B | venda | nao | proximo | 2.80 | 0.44 | +0.44 | 0.615 | 0.551 | 1 | 2026-10-19 11:05 |
| LINK/USDT | B | compra | nao | proximo | 1.43 | 0.13 | -1.00 | 1.316 | 0.331 | 1 | 2026-10-19 10:05 |
| UNI/USDT | B | venda | nao | proximo | 11.44 | 0.36 | +0.36 | 0.571 | 0.438 | 1 | 2026-10-19 06:05 |
| BTC/USDT | B | venda | nao | proximo | 4.15 | 1.57 | +1.57 | 0.757 | 1.949 | 7 | 2026-10-19 05:05 |
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
