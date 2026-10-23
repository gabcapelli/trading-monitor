# Calibracao — registro mecanico de sinais (atualizado 2026-10-23 17:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 93 | 93 | 25 (27%) | -0.04R (-0.000R/sinal) |
| Descartados por R:R baixo | 426 | 425 | 274 (64%) | -5.09R (-0.012R/sinal) |
| TODOS | 519 | 518 | 299 (58%) | -5.13R (-0.010R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=299, mediana 0.35R, maximo 0.99R, 8% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=219, mediana 0.39R, 22% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SOL/USDT | B | venda | nao | proximo | 3.02 | 1.96 | +1.96 | 0.0 | 2.875 | 2 | 2026-10-23 15:06 |
| ETH/USDT | B | compra | nao | proximo | 0.16 | 0.16 | -1.00 | 1.88 | 0.18 | 1 | 2026-10-23 11:06 |
| SUI/USDT | B | compra | nao | proximo | 0.40 | 0.40 | -1.00 | 2.395 | 0.147 | 1 | 2026-10-23 11:06 |
| ETH/USDT | B | compra | nao | proximo | 0.83 | 0.01 | +0.01 | 0.719 | 0.135 | 1 | 2026-10-23 09:15 |
| XRP/USDT | B | compra | nao | proximo | 1.68 | 0.20 | +0.20 | 0.822 | 0.218 | 1 | 2026-10-23 09:15 |
| SUI/USDT | B | compra | nao | proximo | 0.83 | 0.09 | +0.09 | 0.314 | 0.404 | 1 | 2026-10-23 09:15 |
| DOGE/USDT | B | venda | nao | proximo | 3.46 | 1.11 | +1.11 | 0.895 | 1.691 | 4 | 2026-10-23 08:06 |
| WLD/USDT | B | venda | nao | proximo | 0.21 | 0.21 | +0.21 | 0.253 | 0.262 | 1 | 2026-10-23 07:06 |
| DOGE/USDT | B | compra | nao | proximo | 0.06 | 0.06 | +0.06 | 0.361 | 0.722 | 1 | 2026-10-23 03:06 |
| UNI/USDT | B | compra | nao | proximo | 6.93 | 1.37 | -1.00 | 1.064 | 1.157 | 6 | 2026-10-23 03:06 |
| ETH/USDT | B | compra | nao | proximo | 0.07 | 0.06 | -1.00 | 1.291 | 0.066 | 12 | 2026-10-23 00:06 |
| UNI/USDT | B | compra | nao | proximo | 0.11 | 0.11 | +0.11 | 0.409 | 0.277 | 1 | 2026-10-23 00:06 |
| WLD/USDT | B | compra | nao | proximo | 2.64 | 0.92 | +0.92 | 0.303 | 2.109 | 2 | 2026-10-22 21:06 |
| UNI/USDT | B | compra | sim | proximo | 4.12 | 4.12 | +4.12 | 0.676 | 4.734 | 4 | 2026-10-22 21:06 |
| ARB/USDT | B | compra | nao | proximo | 3.40 | 0.52 | -1.00 | 1.368 | 0.103 | 1 | 2026-10-22 17:06 |
| BTC/USDT | B | compra | nao | proximo | 9.30 | 0.85 | +0.85 | 0.691 | 1.052 | 7 | 2026-10-22 16:06 |
| SOL/USDT | B | compra | nao | proximo | 2.98 | 1.33 | -1.00 | 1.046 | 0.568 | 2 | 2026-10-22 16:06 |
| DOGE/USDT | B | compra | sim | proximo | 2.56 | 2.24 | +2.24 | 0.764 | 2.255 | 8 | 2026-10-22 16:06 |
| UNI/USDT | B | compra | sim | proximo | 2.23 | 2.23 | +2.23 | 0.677 | 2.59 | 9 | 2026-10-22 16:06 |
| ETH/USDT | B | compra | nao | proximo | 6.20 | 0.38 | +0.38 | 0.558 | 0.388 | 1 | 2026-10-22 11:06 |
| SUI/USDT | B | compra | nao | proximo | 7.22 | 0.65 | -1.00 | 1.784 | 0.29 | 2 | 2026-10-22 11:06 |
| UNI/USDT | B | compra | nao | proximo | 5.85 | 0.46 | -1.00 | 1.345 | 0.364 | 2 | 2026-10-22 11:06 |
| SOL/USDT | B | compra | nao | proximo | 5.26 | 0.03 | +0.03 | 0.075 | 0.495 | 1 | 2026-10-22 07:06 |
| ARB/USDT | B | compra | nao | proximo | 10.42 | 1.03 | +1.03 | 0.071 | 1.606 | 1 | 2026-10-22 07:06 |
| UNI/USDT | B | compra | nao | proximo | 6.78 | 1.27 | -1.00 | 1.975 | 1.179 | 7 | 2026-10-22 07:06 |
