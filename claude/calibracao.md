# Calibracao — registro mecanico de sinais (atualizado 2026-10-12 03:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 75 | 75 | 20 (27%) | +0.00R (+0.000R/sinal) |
| Descartados por R:R baixo | 298 | 296 | 194 (66%) | +1.47R (+0.005R/sinal) |
| TODOS | 373 | 371 | 214 (58%) | +1.47R (+0.004R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=214, mediana 0.35R, maximo 0.99R, 8% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=157, mediana 0.39R, 22% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ARB/USDT | B | compra | nao | proximo | 0.94 | 0.26 | +0.26 | 0.275 | 0.445 | 1 | 2026-10-12 02:06 |
| SUI/USDT | B | compra | nao | proximo | 0.26 | 0.18 | aberto | 0.477 | 0.114 | — | 2026-10-12 02:06 |
| SOL/USDT | B | venda | sim | proximo | 4.26 | 4.26 | -1.00 | 3.913 | 0.76 | 1 | 2026-10-12 01:06 |
| UNI/USDT | B | compra | nao | proximo | 0.63 | 0.63 | +0.63 | 0.453 | 0.971 | 1 | 2026-10-12 01:06 |
| BTC/USDT | B | compra | nao | proximo | 0.89 | 0.89 | -1.00 | 1.771 | 0.267 | 1 | 2026-10-11 22:06 |
| LINK/USDT | B | compra | nao | proximo | 1.46 | 1.46 | -1.00 | 2.175 | 0.042 | 1 | 2026-10-11 18:06 |
| XRP/USDT | A | compra | nao | proximo | 5.23 | 0.19 | -1.00 | 1.809 | 0.581 | 1 | 2026-10-11 17:06 |
| ETH/USDT | B | compra | nao | proximo | 1.27 | 1.27 | -1.00 | 1.025 | 0.156 | 2 | 2026-10-11 14:06 |
| SUI/USDT | B | compra | nao | proximo | 0.26 | 0.26 | -1.00 | 1.924 | 0.143 | 2 | 2026-10-11 14:06 |
| UNI/USDT | A | compra | nao | proximo | 0.80 | 0.80 | -1.00 | 1.455 | 0.109 | 5 | 2026-10-11 14:06 |
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
