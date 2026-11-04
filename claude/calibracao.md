# Calibracao — registro mecanico de sinais (atualizado 2026-11-03 23:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 102 | 102 | 27 (26%) | -2.57R (-0.025R/sinal) |
| Descartados por R:R baixo | 553 | 549 | 346 (63%) | -24.37R (-0.044R/sinal) |
| TODOS | 655 | 651 | 373 (57%) | -26.94R (-0.041R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=373, mediana 0.32R, maximo 0.99R, 7% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=278, mediana 0.39R, 21% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ETH/USDT | B | venda | nao | proximo | 1.39 | 0.58 | aberto | — | — | — | 2026-11-03 23:06 |
| XRP/USDT | B | venda | nao | proximo | 0.83 | 0.61 | aberto | — | — | — | 2026-11-03 23:06 |
| UNI/USDT | B | venda | nao | proximo | 2.30 | 0.26 | aberto | — | — | — | 2026-11-03 23:06 |
| ETH/USDT | B | compra | nao | proximo | 1.43 | 1.06 | -1.00 | 1.391 | 0.713 | 3 | 2026-11-03 18:06 |
| XRP/USDT | B | compra | nao | proximo | 1.64 | 1.64 | -1.00 | 3.641 | 1.255 | 4 | 2026-11-03 18:06 |
| BTC/USDT | B | compra | nao | proximo | 0.37 | 0.04 | +0.04 | 0.291 | 0.181 | 1 | 2026-11-03 14:06 |
| DOGE/USDT | B | compra | nao | proximo | 1.40 | 1.40 | -1.00 | 3.145 | 1.273 | 10 | 2026-11-03 12:06 |
| SUI/USDT | B | compra | nao | proximo | 1.14 | 0.73 | -1.00 | 1.993 | 0.648 | 10 | 2026-11-03 12:06 |
| LINK/USDT | B | compra | nao | proximo | 1.25 | 0.19 | -1.00 | 1.403 | 0.104 | 2 | 2026-11-03 11:06 |
| DOGE/USDT | B | compra | nao | proximo | 0.63 | 0.63 | -1.00 | 1.447 | 0.57 | 12 | 2026-11-03 10:06 |
| ARB/USDT | B | compra | nao | proximo | 0.87 | 0.44 | -1.00 | 1.044 | 0.169 | 3 | 2026-11-03 10:06 |
| SUI/USDT | A | compra | nao | proximo | 0.04 | 0.04 | +0.04 | 0.455 | 0.485 | 1 | 2026-11-03 10:06 |
| BTC/USDT | B | compra | nao | proximo | 3.06 | 1.56 | -1.00 | 1.264 | 0.502 | 3 | 2026-11-03 01:06 |
| ETH/USDT | B | compra | nao | proximo | 1.26 | 1.26 | -1.00 | 2.741 | 0.84 | 1 | 2026-11-02 12:06 |
| LINK/USDT | B | compra | nao | proximo | 1.47 | 1.47 | -1.00 | 2.387 | 0.809 | 1 | 2026-11-02 12:06 |
| LINK/USDT | B | compra | nao | proximo | 4.09 | 0.17 | +0.17 | 0.119 | 2.414 | 1 | 2026-11-02 09:06 |
| ETH/USDT | B | compra | nao | proximo | 1.47 | 1.47 | -1.00 | 1.021 | 0.253 | 3 | 2026-11-02 06:06 |
| UNI/USDT | B | venda | nao | proximo | 1.21 | 1.21 | -1.00 | 1.543 | 0.325 | 3 | 2026-11-02 04:06 |
| UNI/USDT | B | venda | nao | proximo | 3.55 | 1.65 | +1.65 | 0.461 | 1.952 | 2 | 2026-11-02 02:06 |
| ARB/USDT | B | compra | nao | proximo | 1.58 | 0.50 | -1.00 | 2.448 | 0.466 | 3 | 2026-11-02 01:06 |
| ETH/USDT | B | compra | sim | proximo | 10.89 | 5.01 | -1.00 | 1.058 | 3.072 | 3 | 2026-11-02 00:06 |
| UNI/USDT | B | venda | nao | proximo | 1.62 | 0.16 | -1.00 | 1.386 | 0.082 | 1 | 2026-11-01 22:06 |
| SOL/USDT | B | compra | nao | proximo | 1.50 | 1.50 | +1.50 | 0.775 | 1.495 | 4 | 2026-11-01 21:06 |
| ARB/USDT | B | compra | nao | proximo | 1.79 | 0.16 | +0.16 | 0.424 | 0.379 | 1 | 2026-11-01 18:06 |
| UNI/USDT | B | venda | nao | proximo | 2.01 | 1.33 | -1.00 | 1.442 | 1.21 | 6 | 2026-11-01 15:06 |
