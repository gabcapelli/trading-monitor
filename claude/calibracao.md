# Calibracao — registro mecanico de sinais (atualizado 2026-11-02 05:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 102 | 102 | 27 (26%) | -2.57R (-0.025R/sinal) |
| Descartados por R:R baixo | 536 | 534 | 343 (64%) | -12.62R (-0.024R/sinal) |
| TODOS | 638 | 636 | 370 (58%) | -15.19R (-0.024R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=370, mediana 0.33R, maximo 0.99R, 7% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=266, mediana 0.38R, 21% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| UNI/USDT | B | venda | nao | proximo | 1.21 | 1.21 | aberto | 0.534 | 0.325 | — | 2026-11-02 04:06 |
| UNI/USDT | B | venda | nao | proximo | 3.55 | 1.65 | +1.65 | 0.461 | 1.952 | 2 | 2026-11-02 02:06 |
| ARB/USDT | B | compra | nao | proximo | 1.58 | 0.50 | -1.00 | 2.448 | 0.466 | 3 | 2026-11-02 01:06 |
| ETH/USDT | B | compra | sim | proximo | 10.89 | 5.01 | -1.00 | 1.058 | 3.072 | 3 | 2026-11-02 00:06 |
| UNI/USDT | B | venda | nao | proximo | 1.62 | 0.16 | -1.00 | 1.386 | 0.082 | 1 | 2026-11-01 22:06 |
| SOL/USDT | B | compra | nao | proximo | 1.50 | 1.50 | +1.50 | 0.775 | 1.495 | 4 | 2026-11-01 21:06 |
| ARB/USDT | B | compra | nao | proximo | 1.79 | 0.16 | +0.16 | 0.424 | 0.379 | 1 | 2026-11-01 18:06 |
| UNI/USDT | B | venda | nao | proximo | 2.01 | 1.33 | -1.00 | 1.442 | 1.21 | 6 | 2026-11-01 15:06 |
| SUI/USDT | B | compra | nao | proximo | 1.50 | 0.63 | -1.00 | 1.847 | 0.087 | 2 | 2026-11-01 14:06 |
| ARB/USDT | B | compra | nao | proximo | 0.15 | 0.15 | -1.00 | 1.049 | 0.034 | 2 | 2026-11-01 13:06 |
| UNI/USDT | B | venda | nao | proximo | 0.78 | 0.78 | +0.78 | 0.055 | 1.034 | 2 | 2026-11-01 13:06 |
| UNI/USDT | B | venda | sim | proximo | 3.27 | 2.47 | -1.00 | 2.159 | 0.735 | 2 | 2026-11-01 09:06 |
| UNI/USDT | B | venda | sim | proximo | 3.59 | 2.81 | -1.00 | 1.759 | 1.094 | 4 | 2026-11-01 07:06 |
| DOGE/USDT | B | compra | nao | proximo | 0.81 | 0.33 | -1.00 | 1.346 | 0.03 | 1 | 2026-11-01 06:06 |
| ARB/USDT | B | compra | nao | proximo | 1.44 | 0.19 | +0.19 | 0.128 | 1.556 | 1 | 2026-11-01 00:06 |
| LINK/USDT | B | venda | nao | proximo | 0.40 | 0.40 | +0.40 | 0.512 | 0.418 | 2 | 2026-11-01 00:06 |
| SUI/USDT | B | compra | nao | proximo | 1.04 | 0.89 | +0.89 | 0.384 | 1.114 | 8 | 2026-10-31 19:06 |
| ARB/USDT | B | compra | nao | proximo | 2.88 | 0.24 | +0.24 | 0.784 | 0.824 | 1 | 2026-10-31 18:06 |
| UNI/USDT | B | compra | nao | proximo | 0.95 | 0.83 | +0.83 | 0.497 | 1.153 | 1 | 2026-10-31 12:06 |
| UNI/USDT | B | compra | nao | proximo | 0.91 | 0.82 | +0.82 | 0.494 | 1.065 | 3 | 2026-10-31 10:06 |
| LINK/USDT | B | venda | nao | proximo | 2.38 | 0.49 | -1.00 | 1.398 | 0.146 | 1 | 2026-10-31 09:06 |
| SUI/USDT | B | compra | nao | proximo | 3.53 | 1.67 | +1.67 | 0.796 | 1.837 | 7 | 2026-10-31 06:06 |
| WLD/USDT | A | venda | nao | proximo | 1.66 | 1.11 | +1.11 | 0.392 | 1.115 | 4 | 2026-10-31 05:06 |
| LINK/USDT | B | venda | nao | proximo | 4.96 | 0.59 | +0.59 | 0.062 | 0.662 | 1 | 2026-10-31 00:06 |
| DOGE/USDT | B | compra | nao | proximo | 1.53 | 0.58 | +0.58 | 0.129 | 0.991 | 1 | 2026-10-30 21:06 |
