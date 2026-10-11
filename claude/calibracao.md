# Calibracao — registro mecanico de sinais (atualizado 2026-10-11 14:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 74 | 74 | 20 (27%) | +1.00R (+0.014R/sinal) |
| Descartados por R:R baixo | 292 | 288 | 192 (67%) | +6.58R (+0.023R/sinal) |
| TODOS | 366 | 362 | 212 (59%) | +7.58R (+0.021R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=212, mediana 0.35R, maximo 0.99R, 8% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=150, mediana 0.42R, 23% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ETH/USDT | B | compra | nao | proximo | 1.27 | 1.27 | aberto | — | — | — | 2026-10-11 14:06 |
| SUI/USDT | B | compra | nao | proximo | 0.26 | 0.26 | aberto | — | — | — | 2026-10-11 14:06 |
| UNI/USDT | A | compra | nao | proximo | 0.80 | 0.80 | aberto | — | — | — | 2026-10-11 14:06 |
| SUI/USDT | B | compra | nao | proximo | 1.76 | 1.76 | +1.76 | 0.396 | 2.305 | 1 | 2026-10-11 12:06 |
| WLD/USDT | B | compra | nao | proximo | 1.69 | 1.48 | +1.48 | 0.75 | 2.661 | 2 | 2026-10-11 10:06 |
| SUI/USDT | B | compra | sim | proximo | 4.23 | 4.23 | +4.23 | 0.791 | 5.246 | 3 | 2026-10-11 10:06 |
| WLD/USDT | B | venda | nao | proximo | 1.72 | 0.31 | +0.31 | 0.132 | 0.924 | 1 | 2026-10-11 07:06 |
| SUI/USDT | B | compra | nao | proximo | 1.74 | 1.74 | -1.00 | 1.104 | 0.239 | 6 | 2026-10-11 02:06 |
| WLD/USDT | B | compra | nao | proximo | 0.41 | 0.41 | -1.00 | 1.877 | 0.289 | 2 | 2026-10-10 23:06 |
| LINK/USDT | B | venda | nao | proximo | 2.24 | 0.90 | -1.00 | 1.853 | 0.293 | 1 | 2026-10-10 22:06 |
| WLD/USDT | B | venda | nao | proximo | 2.30 | 0.13 | +0.13 | 0.723 | 0.562 | 1 | 2026-10-10 21:06 |
| WLD/USDT | B | venda | nao | proximo | 4.59 | 0.01 | +0.01 | 0.143 | 0.271 | 1 | 2026-10-10 05:06 |
| SOL/USDT | A | venda | nao | proximo | 0.68 | 0.68 | -1.00 | 1.262 | 1.293 | 1 | 2026-10-09 19:05 |
| BTC/USDT | B | compra | nao | proximo | 0.85 | 0.85 | +0.85 | 0.488 | 2.598 | 8 | 2026-10-09 01:05 |
| ETH/USDT | B | venda | nao | proximo | 0.49 | 0.10 | +0.10 | 0.237 | 0.229 | 1 | 2026-10-06 13:05 |
| ARB/USDT | B | compra | nao | proximo | 2.22 | 0.03 | +0.03 | 0.476 | 0.43 | 1 | 2026-10-06 12:05 |
| WLD/USDT | B | venda | nao | proximo | 1.59 | 0.21 | +0.21 | 0.529 | 0.987 | 1 | 2026-10-06 11:05 |
| ETH/USDT | B | compra | nao | proximo | 0.59 | 0.59 | -1.00 | 1.119 | 0.775 | 2 | 2026-10-06 10:05 |
| XRP/USDT | B | compra | nao | proximo | 0.26 | 0.24 | +0.24 | 0.435 | 1.176 | 1 | 2026-10-06 08:05 |
| UNI/USDT | B | compra | nao | proximo | 5.34 | 1.25 | +1.25 | 0.736 | 1.316 | 3 | 2026-10-06 05:05 |
| LINK/USDT | B | compra | nao | proximo | 0.24 | 0.24 | +0.24 | 0.036 | 0.455 | 1 | 2026-10-06 05:05 |
| BTC/USDT | B | venda | nao | proximo | 1.99 | 0.41 | +0.41 | 0.0 | 1.429 | 1 | 2026-10-06 03:05 |
| SOL/USDT | B | venda | nao | proximo | 1.49 | 0.52 | +0.52 | 0.178 | 0.988 | 1 | 2026-10-06 03:05 |
| LINK/USDT | B | compra | sim | proximo | 2.35 | 2.35 | -1.00 | 1.104 | 0.544 | 2 | 2026-10-06 02:05 |
| DOGE/USDT | B | venda | nao | proximo | 1.75 | 0.37 | +0.37 | 0.175 | 0.686 | 1 | 2026-10-05 23:05 |
