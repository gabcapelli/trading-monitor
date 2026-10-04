# Calibracao — registro mecanico de sinais (atualizado 2026-10-04 08:05 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 68 | 67 | 17 (25%) | -5.10R (-0.076R/sinal) |
| Descartados por R:R baixo | 242 | 240 | 158 (66%) | +3.59R (+0.015R/sinal) |
| TODOS | 310 | 307 | 175 (57%) | -1.51R (-0.005R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=175, mediana 0.35R, maximo 0.98R, 7% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=132, mediana 0.39R, 22% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| BTC/USDT | A | compra | nao | proximo | 10.84 | 0.27 | +0.27 | 0.054 | 1.1 | 1 | 2026-10-04 07:05 |
| ETH/USDT | B | venda | nao | proximo | 2.64 | 1.35 | aberto | 0.798 | 0.305 | — | 2026-10-04 06:05 |
| BTC/USDT | B | compra | nao | proximo | 11.05 | 0.87 | +0.87 | 0.36 | 1.137 | 2 | 2026-10-04 05:05 |
| DOGE/USDT | B | compra | nao | proximo | 0.04 | 0.04 | +0.04 | 0.684 | 0.129 | 1 | 2026-10-04 05:05 |
| UNI/USDT | B | compra | nao | proximo | 1.14 | 0.35 | +0.35 | 0.52 | 0.47 | 1 | 2026-10-04 05:05 |
| ETH/USDT | B | venda | nao | proximo | 3.24 | 0.87 | -1.00 | 1.193 | 0.35 | 3 | 2026-10-04 00:05 |
| SOL/USDT | A | compra | nao | proximo | 6.57 | 0.80 | +0.80 | 0.51 | 1.975 | 1 | 2026-10-04 00:05 |
| SUI/USDT | B | venda | nao | proximo | 2.06 | 1.48 | +1.48 | 0.698 | 1.571 | 10 | 2026-10-03 21:05 |
| UNI/USDT | B | compra | nao | proximo | 5.66 | 0.22 | +0.22 | 0.342 | 0.524 | 1 | 2026-10-03 20:05 |
| ARB/USDT | B | compra | nao | proximo | 2.35 | 1.45 | +1.45 | 0.565 | 2.838 | 5 | 2026-10-03 17:05 |
| BTC/USDT | A | compra | nao | proximo | 21.73 | 1.33 | +1.33 | 0.679 | 1.365 | 2 | 2026-10-03 13:06 |
| SUI/USDT | B | venda | nao | proximo | 3.35 | 1.11 | +1.11 | 0.157 | 1.518 | 4 | 2026-10-03 10:05 |
| UNI/USDT | B | venda | sim | proximo | 6.95 | 3.82 | aberto | 0.114 | 3.12 | — | 2026-10-03 08:05 |
| ARB/USDT | B | compra | nao | proximo | 1.14 | 0.10 | +0.10 | 0.254 | 0.178 | 1 | 2026-10-03 07:05 |
| ARB/USDT | B | compra | nao | proximo | 0.90 | 0.90 | +0.90 | 0.699 | 2.22 | 4 | 2026-10-03 03:05 |
| LINK/USDT | B | compra | nao | proximo | 4.02 | 1.25 | -1.00 | 1.027 | 0.926 | 6 | 2026-10-03 03:05 |
| DOGE/USDT | A | venda | nao | proximo | 4.75 | 0.03 | +0.03 | 0.381 | 0.281 | 1 | 2026-10-02 23:05 |
| SUI/USDT | B | venda | nao | proximo | 2.44 | 0.05 | +0.05 | 0.331 | 0.32 | 1 | 2026-10-02 23:05 |
| UNI/USDT | B | compra | nao | proximo | 0.76 | 0.15 | +0.15 | 0.29 | 0.527 | 1 | 2026-10-02 22:05 |
| LINK/USDT | B | compra | sim | proximo | 4.63 | 2.13 | +2.13 | 0.802 | 2.285 | 22 | 2026-10-02 22:05 |
| SUI/USDT | B | compra | nao | proximo | 2.80 | 0.67 | +0.67 | 0.073 | 1.801 | 1 | 2026-10-02 21:05 |
| UNI/USDT | B | compra | nao | proximo | 3.72 | 0.38 | +0.38 | 0.429 | 0.848 | 1 | 2026-10-02 19:05 |
| LINK/USDT | B | compra | sim | proximo | 5.53 | 3.33 | +3.33 | 0.227 | 3.462 | 25 | 2026-10-02 19:05 |
| UNI/USDT | B | compra | nao | proximo | 3.68 | 0.92 | +0.92 | 0.165 | 1.305 | 3 | 2026-10-02 17:05 |
| DOGE/USDT | B | venda | nao | proximo | 2.81 | 1.90 | +1.90 | 0.304 | 7.136 | 2 | 2026-10-02 14:05 |
