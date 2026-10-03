# Calibracao — registro mecanico de sinais (atualizado 2026-10-03 06:05 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 67 | 65 | 15 (23%) | -10.56R (-0.162R/sinal) |
| Descartados por R:R baixo | 229 | 226 | 146 (65%) | -3.32R (-0.015R/sinal) |
| TODOS | 296 | 291 | 161 (55%) | -13.88R (-0.048R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=161, mediana 0.35R, maximo 0.98R, 7% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=130, mediana 0.39R, 22% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ARB/USDT | B | compra | nao | proximo | 0.90 | 0.90 | aberto | 0.699 | 0.349 | — | 2026-10-03 03:05 |
| LINK/USDT | B | compra | nao | proximo | 4.02 | 1.25 | aberto | 0.665 | 0.926 | — | 2026-10-03 03:05 |
| DOGE/USDT | A | venda | nao | proximo | 4.75 | 0.03 | +0.03 | 0.381 | 0.281 | 1 | 2026-10-02 23:05 |
| SUI/USDT | B | venda | nao | proximo | 2.44 | 0.05 | +0.05 | 0.331 | 0.32 | 1 | 2026-10-02 23:05 |
| UNI/USDT | B | compra | nao | proximo | 0.76 | 0.15 | +0.15 | 0.29 | 0.527 | 1 | 2026-10-02 22:05 |
| LINK/USDT | B | compra | sim | proximo | 4.63 | 2.13 | aberto | 0.235 | 1.846 | — | 2026-10-02 22:05 |
| SUI/USDT | B | compra | nao | proximo | 2.80 | 0.67 | +0.67 | 0.073 | 1.801 | 1 | 2026-10-02 21:05 |
| UNI/USDT | B | compra | nao | proximo | 3.72 | 0.38 | +0.38 | 0.429 | 0.848 | 1 | 2026-10-02 19:05 |
| LINK/USDT | B | compra | sim | proximo | 5.53 | 3.33 | aberto | 0.227 | 3.075 | — | 2026-10-02 19:05 |
| UNI/USDT | B | compra | nao | proximo | 3.68 | 0.92 | +0.92 | 0.165 | 1.305 | 3 | 2026-10-02 17:05 |
| DOGE/USDT | B | venda | nao | proximo | 2.81 | 1.90 | +1.90 | 0.304 | 7.136 | 2 | 2026-10-02 14:05 |
| LINK/USDT | B | venda | nao | proximo | 0.16 | 0.16 | +0.16 | 0.478 | 0.858 | 1 | 2026-10-02 14:05 |
| UNI/USDT | B | compra | nao | proximo | 2.05 | 0.13 | +0.13 | 0.423 | 0.498 | 1 | 2026-10-02 13:05 |
| ETH/USDT | B | venda | sim | proximo | 2.05 | 2.05 | +2.05 | 0.238 | 2.099 | 3 | 2026-10-02 11:05 |
| SOL/USDT | B | venda | nao | proximo | 3.20 | 0.55 | +0.55 | 0.274 | 1.365 | 1 | 2026-10-02 11:05 |
| XRP/USDT | B | venda | nao | proximo | 2.36 | 1.21 | +1.21 | 0.289 | 1.47 | 1 | 2026-10-02 11:05 |
| DOGE/USDT | B | venda | nao | proximo | 2.80 | 0.35 | +0.35 | 0.353 | 1.477 | 1 | 2026-10-02 11:05 |
| UNI/USDT | B | venda | nao | proximo | 1.21 | 1.11 | +1.11 | 0.375 | 3.05 | 5 | 2026-10-02 11:05 |
| LINK/USDT | B | venda | nao | proximo | 0.65 | 0.65 | +0.65 | 0.442 | 1.421 | 1 | 2026-10-02 11:05 |
| DOGE/USDT | B | venda | nao | proximo | 6.02 | 0.59 | -1.00 | 1.97 | 0.675 | 1 | 2026-10-02 09:05 |
| ETH/USDT | B | venda | sim | proximo | 6.38 | 6.38 | -1.00 | 2.315 | 1.308 | 3 | 2026-10-02 07:05 |
| DOGE/USDT | B | venda | nao | proximo | 6.23 | 0.33 | +0.33 | 0.179 | 0.976 | 1 | 2026-10-02 07:05 |
| DOGE/USDT | B | venda | nao | proximo | 2.60 | 0.55 | -1.00 | 2.009 | 0.421 | 3 | 2026-10-02 03:05 |
| WLD/USDT | B | compra | nao | proximo | 1.11 | 0.30 | +0.30 | 0.355 | 1.072 | 2 | 2026-10-02 02:05 |
| UNI/USDT | B | compra | nao | proximo | 0.07 | 0.07 | +0.07 | 0.624 | 0.078 | 1 | 2026-10-02 02:05 |
