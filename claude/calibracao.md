# Calibracao — registro mecanico de sinais (atualizado 2026-09-15 14:05 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 32 | 32 | 4 (12%) | -18.93R (-0.591R/sinal) |
| Descartados por R:R baixo | 71 | 67 | 48 (72%) | +6.95R (+0.104R/sinal) |
| TODOS | 103 | 99 | 52 (53%) | -11.98R (-0.121R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=52, mediana 0.38R, maximo 0.98R, 12% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=47, mediana 0.36R, 30% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| BTC/USDT | B | compra | nao | proximo | 0.99 | 0.99 | aberto | 0.341 | 0.084 | — | 2026-09-15 13:05 |
| SOL/USDT | B | compra | nao | proximo | 5.94 | 0.84 | aberto | 0.533 | 0.087 | — | 2026-09-15 13:05 |
| LINK/USDT | B | compra | nao | proximo | 2.50 | 1.45 | aberto | 0.549 | 0.222 | — | 2026-09-15 13:05 |
| WLD/USDT | A | venda | nao | proximo | — | — | aberto | 0.666 | 0.098 | — | 2026-09-15 12:05 |
| UNI/USDT | B | venda | nao | proximo | 0.16 | 0.02 | +0.02 | 0.451 | 0.053 | 1 | 2026-09-15 12:05 |
| DOGE/USDT | B | compra | nao | proximo | 3.45 | 1.45 | -1.00 | 2.58 | 0.135 | 1 | 2026-09-15 11:05 |
| ETH/USDT | B | compra | nao | proximo | 9.09 | 0.49 | +0.49 | 0.374 | 0.633 | 2 | 2026-09-15 06:05 |
| SOL/USDT | B | compra | nao | proximo | 6.40 | 1.36 | -1.00 | 1.543 | 1.146 | 5 | 2026-09-15 06:05 |
| DOGE/USDT | A | venda | nao | proximo | 1.23 | 0.70 | -1.00 | 1.772 | 1.194 | 6 | 2026-09-15 05:05 |
| BTC/USDT | B | venda | nao | proximo | 1.87 | 0.09 | +0.09 | 0.065 | 0.856 | 1 | 2026-09-15 04:05 |
| XRP/USDT | B | venda | nao | proximo | 1.31 | 1.31 | -1.00 | 1.722 | 1.066 | 6 | 2026-09-15 04:05 |
| SUI/USDT | A | venda | nao | proximo | 3.00 | 0.41 | +0.41 | 0.445 | 0.871 | 1 | 2026-09-15 04:05 |
| LINK/USDT | A | venda | nao | proximo | 1.55 | 0.20 | +0.20 | 0.223 | 0.827 | 1 | 2026-09-15 04:05 |
| ETH/USDT | B | venda | nao | proximo | 0.22 | 0.22 | +0.22 | 0.597 | 1.098 | 1 | 2026-09-15 02:05 |
| ETH/USDT | B | venda | nao | proximo | 2.53 | 0.40 | +0.40 | 0.001 | 1.859 | 1 | 2026-09-15 00:05 |
| XRP/USDT | B | venda | nao | proximo | 2.45 | 0.42 | +0.42 | 0.247 | 0.494 | 1 | 2026-09-14 21:05 |
| UNI/USDT | B | venda | nao | proximo | 3.48 | 0.57 | -1.00 | 1.98 | 0.088 | 1 | 2026-09-14 21:05 |
| ETH/USDT | B | venda | nao | proximo | 1.72 | 0.70 | +0.70 | 0.057 | 0.767 | 1 | 2026-09-14 20:05 |
| XRP/USDT | B | venda | nao | proximo | 2.57 | 1.14 | +1.14 | 0.448 | 1.187 | 3 | 2026-09-14 19:05 |
| SUI/USDT | B | venda | nao | proximo | 1.36 | 0.56 | +0.56 | 0.248 | 0.573 | 1 | 2026-09-14 19:05 |
| BTC/USDT | B | venda | nao | proximo | 5.21 | 0.86 | -1.00 | 2.103 | 0.036 | 1 | 2026-09-14 17:05 |
| SOL/USDT | A | compra | nao | proximo | 0.11 | 0.11 | +0.11 | 0.221 | 1.262 | 1 | 2026-09-14 15:05 |
| WLD/USDT | B | venda | nao | proximo | 0.28 | 0.28 | +0.28 | 0.682 | 0.398 | 1 | 2026-09-14 12:06 |
| BTC/USDT | B | compra | nao | proximo | 0.26 | 0.26 | +0.26 | 0.021 | 0.694 | 1 | 2026-09-14 11:05 |
| XRP/USDT | B | venda | nao | proximo | 5.67 | 1.06 | +1.06 | 0.746 | 1.134 | 1 | 2026-09-14 10:05 |
