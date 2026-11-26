# Calibracao — registro mecanico de sinais (atualizado 2026-11-26 20:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 138 | 137 | 42 (31%) | +20.94R (+0.153R/sinal) |
| Descartados por R:R baixo | 723 | 717 | 454 (63%) | -34.03R (-0.047R/sinal) |
| TODOS | 861 | 854 | 496 (58%) | -13.09R (-0.015R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=496, mediana 0.33R, maximo 0.99R, 7% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=358, mediana 0.39R, 19% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SUI/USDT | B | venda | nao | proximo | 3.14 | 0.53 | aberto | — | — | — | 2026-11-26 20:06 |
| WLD/USDT | B | compra | nao | proximo | 1.78 | 1.09 | -1.00 | 2.118 | 0.615 | 2 | 2026-11-26 18:06 |
| ARB/USDT | B | venda | nao | proximo | 2.99 | 0.54 | -1.00 | 1.088 | 0.211 | 2 | 2026-11-26 17:06 |
| XRP/USDT | B | compra | sim | proximo | 2.62 | 2.13 | aberto | 0.959 | 1.448 | — | 2026-11-26 14:06 |
| BTC/USDT | B | venda | nao | proximo | 1.31 | 0.74 | +0.74 | 0.0 | 2.979 | 1 | 2026-11-26 12:06 |
| LINK/USDT | B | venda | nao | proximo | 0.43 | 0.43 | +0.43 | 0.159 | 1.403 | 1 | 2026-11-26 12:06 |
| BTC/USDT | B | compra | nao | proximo | 1.61 | 1.06 | -1.00 | 2.956 | 1.021 | 4 | 2026-11-26 09:06 |
| WLD/USDT | B | compra | nao | proximo | 0.31 | 0.10 | +0.10 | 0.524 | 0.454 | 1 | 2026-11-26 09:06 |
| WLD/USDT | B | venda | nao | proximo | 0.50 | 0.50 | -1.00 | 1.06 | 0.076 | 2 | 2026-11-26 04:06 |
| SUI/USDT | B | venda | nao | proximo | 7.65 | 0.23 | -1.00 | 1.164 | 0.116 | 2 | 2026-11-26 04:06 |
| BTC/USDT | B | venda | nao | proximo | 10.96 | 0.19 | +0.19 | 0.028 | 1.381 | 1 | 2026-11-26 03:06 |
| LINK/USDT | B | venda | sim | proximo | 4.53 | 4.53 | -1.00 | 1.074 | 1.611 | 3 | 2026-11-26 03:06 |
| ARB/USDT | A | compra | nao | proximo | 3.66 | 0.15 | +0.15 | 0.373 | 0.931 | 1 | 2026-11-25 23:06 |
| SUI/USDT | B | compra | nao | proximo | 0.62 | 0.62 | +0.62 | 0.589 | 0.821 | 1 | 2026-11-25 23:06 |
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
