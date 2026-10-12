# Calibracao — registro mecanico de sinais (atualizado 2026-10-12 15:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 75 | 75 | 20 (27%) | +0.00R (+0.000R/sinal) |
| Descartados por R:R baixo | 305 | 303 | 197 (65%) | +0.69R (+0.002R/sinal) |
| TODOS | 380 | 378 | 217 (57%) | +0.70R (+0.002R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=217, mediana 0.35R, maximo 0.99R, 8% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=161, mediana 0.36R, 21% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ARB/USDT | B | venda | nao | proximo | 0.33 | 0.32 | aberto | 0.238 | 0.168 | — | 2026-10-12 14:06 |
| ETH/USDT | B | compra | nao | proximo | 1.62 | 0.57 | -1.00 | 1.227 | 0.126 | 1 | 2026-10-12 11:06 |
| SOL/USDT | B | venda | nao | proximo | 0.44 | 0.44 | +0.44 | 0.512 | 0.643 | 1 | 2026-10-12 10:06 |
| BTC/USDT | B | venda | nao | proximo | 1.60 | 1.60 | +1.60 | 0.013 | 5.599 | 2 | 2026-10-12 08:06 |
| DOGE/USDT | A | compra | nao | proximo | 1.63 | 0.72 | -1.00 | 1.486 | 0.02 | 1 | 2026-10-12 08:06 |
| BTC/USDT | B | venda | nao | proximo | 1.91 | 1.20 | +1.20 | 0.0 | 1.271 | 1 | 2026-10-12 05:06 |
| XRP/USDT | A | compra | nao | proximo | 1.33 | 0.42 | -1.00 | 1.543 | 0.386 | 3 | 2026-10-12 04:06 |
| ARB/USDT | B | compra | nao | proximo | 0.94 | 0.26 | +0.26 | 0.275 | 0.445 | 1 | 2026-10-12 02:06 |
| SUI/USDT | B | compra | nao | proximo | 0.26 | 0.18 | -1.00 | 1.009 | 0.114 | 5 | 2026-10-12 02:06 |
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
