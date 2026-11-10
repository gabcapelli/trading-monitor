# Calibracao — registro mecanico de sinais (atualizado 2026-11-10 13:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 112 | 112 | 31 (28%) | +5.90R (+0.053R/sinal) |
| Descartados por R:R baixo | 626 | 625 | 394 (63%) | -29.14R (-0.047R/sinal) |
| TODOS | 738 | 737 | 425 (58%) | -23.24R (-0.032R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=425, mediana 0.33R, maximo 0.99R, 7% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=312, mediana 0.38R, 20% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ARB/USDT | B | venda | nao | proximo | 0.27 | 0.00 | aberto | — | — | — | 2026-11-10 13:06 |
| BTC/USDT | A | venda | nao | proximo | 0.01 | 0.01 | +0.01 | 0.621 | 0.132 | 1 | 2026-11-10 11:06 |
| LINK/USDT | A | venda | nao | proximo | 0.72 | 0.72 | +0.72 | 0.962 | 1.186 | 2 | 2026-11-10 11:06 |
| UNI/USDT | B | compra | nao | proximo | 2.41 | 0.15 | -1.00 | 2.518 | 0.929 | 1 | 2026-11-10 10:06 |
| ETH/USDT | A | venda | nao | proximo | 0.52 | 0.52 | -1.00 | 1.157 | 4.037 | 3 | 2026-11-10 08:06 |
| XRP/USDT | A | venda | nao | proximo | 0.55 | 0.03 | +0.03 | 0.345 | 0.751 | 1 | 2026-11-10 08:06 |
| ARB/USDT | B | venda | nao | proximo | 1.01 | 1.01 | +1.01 | 0.0 | 2.697 | 1 | 2026-11-10 04:06 |
| SUI/USDT | B | compra | nao | proximo | 3.89 | 1.64 | -1.00 | 1.431 | 0.927 | 5 | 2026-11-10 02:06 |
| UNI/USDT | B | compra | nao | proximo | 3.03 | 0.82 | +0.82 | 0.035 | 2.12 | 1 | 2026-11-10 02:06 |
| SUI/USDT | A | venda | nao | proximo | 6.12 | 0.05 | +0.05 | 0.21 | 0.684 | 1 | 2026-11-09 23:06 |
| UNI/USDT | B | compra | nao | proximo | 1.46 | 0.35 | +0.35 | 0.066 | 0.837 | 1 | 2026-11-09 22:06 |
| UNI/USDT | A | compra | nao | proximo | 1.89 | 0.21 | +0.21 | 0.656 | 0.4 | 2 | 2026-11-09 17:06 |
| UNI/USDT | B | compra | nao | proximo | 0.11 | 0.06 | +0.06 | 0.391 | 1.062 | 1 | 2026-11-09 15:06 |
| UNI/USDT | B | compra | nao | proximo | 0.03 | 0.03 | -1.00 | 1.073 | 0.034 | 1 | 2026-11-09 13:06 |
| UNI/USDT | B | compra | nao | proximo | 1.78 | 1.74 | +1.74 | 0.312 | 1.892 | 7 | 2026-11-09 06:06 |
| LINK/USDT | B | compra | nao | proximo | 0.82 | 0.82 | +0.82 | 0.317 | 1.117 | 4 | 2026-11-09 06:06 |
| XRP/USDT | A | venda | nao | proximo | — | — | -1.00 | 1.407 | 0.095 | 1 | 2026-11-09 05:06 |
| LINK/USDT | B | compra | sim | proximo | 3.00 | 3.00 | -1.00 | 1.342 | 0.37 | 1 | 2026-11-09 00:06 |
| BTC/USDT | B | compra | nao | proximo | 1.18 | 0.85 | -1.00 | 1.138 | 0.443 | 5 | 2026-11-08 22:06 |
| UNI/USDT | B | compra | nao | proximo | 0.47 | 0.22 | +0.22 | 0.292 | 0.235 | 2 | 2026-11-08 22:06 |
| LINK/USDT | B | compra | nao | proximo | 1.22 | 1.22 | -1.00 | 1.203 | 0.375 | 6 | 2026-11-08 22:06 |
| LINK/USDT | B | compra | sim | proximo | 2.71 | 2.71 | -1.00 | 1.019 | 1.636 | 9 | 2026-11-08 20:06 |
| BTC/USDT | B | compra | nao | proximo | 1.09 | 0.23 | -1.00 | 11.005 | 0.007 | 3 | 2026-11-08 16:06 |
| LINK/USDT | B | compra | sim | proximo | 4.19 | 4.19 | -1.00 | 13.491 | 2.223 | 4 | 2026-11-08 15:06 |
| ARB/USDT | B | venda | nao | proximo | 1.45 | 1.45 | -1.00 | 1.083 | 0.0 | 1 | 2026-11-08 10:06 |
