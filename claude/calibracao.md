# Calibracao — registro mecanico de sinais (atualizado 2026-10-18 16:06 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 84 | 83 | 20 (24%) | -8.00R (-0.096R/sinal) |
| Descartados por R:R baixo | 359 | 356 | 233 (65%) | +3.10R (+0.009R/sinal) |
| TODOS | 443 | 439 | 253 (58%) | -4.90R (-0.011R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=253, mediana 0.35R, maximo 0.99R, 8% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=186, mediana 0.42R, 22% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ARB/USDT | B | compra | nao | proximo | 2.51 | 1.84 | aberto | 0.83 | 0.654 | — | 2026-10-18 14:05 |
| BTC/USDT | B | compra | sim | proximo | 5.51 | 2.62 | aberto | 0.767 | 0.539 | — | 2026-10-18 13:05 |
| SOL/USDT | A | venda | nao | proximo | 0.91 | 0.49 | aberto | 0.397 | 0.397 | — | 2026-10-18 12:05 |
| UNI/USDT | A | venda | nao | proximo | 0.35 | 0.15 | +0.15 | 0.278 | 0.692 | 1 | 2026-10-18 12:05 |
| WLD/USDT | B | venda | nao | proximo | 2.05 | 0.71 | +0.71 | 0.172 | 0.729 | 1 | 2026-10-18 08:05 |
| LINK/USDT | B | compra | nao | proximo | 0.42 | 0.42 | -1.00 | 2.295 | 0.133 | 4 | 2026-10-18 07:05 |
| ARB/USDT | B | compra | nao | proximo | 3.94 | 0.73 | +0.73 | 0.62 | 0.745 | 3 | 2026-10-17 20:06 |
| DOGE/USDT | B | compra | sim | proximo | 2.16 | 2.16 | -1.00 | 8.863 | 1.151 | 2 | 2026-10-17 17:06 |
| LINK/USDT | B | compra | sim | proximo | 5.74 | 5.40 | -1.00 | 6.017 | 0.982 | 2 | 2026-10-17 17:06 |
| LINK/USDT | B | compra | sim | proximo | 3.60 | 3.45 | -1.00 | 1.707 | 1.453 | 4 | 2026-10-17 15:06 |
| SUI/USDT | B | compra | nao | proximo | 1.36 | 1.36 | -1.00 | 1.945 | 0.221 | 2 | 2026-10-17 08:06 |
| ARB/USDT | B | venda | nao | proximo | 8.57 | 1.90 | +1.90 | 0.655 | 2.059 | 4 | 2026-10-17 07:06 |
| WLD/USDT | B | venda | nao | proximo | 4.00 | 1.99 | +1.99 | 0.398 | 2.982 | 7 | 2026-10-17 03:06 |
| ARB/USDT | B | compra | nao | proximo | 6.13 | 0.14 | +0.14 | 0.31 | 1.011 | 1 | 2026-10-17 01:06 |
| UNI/USDT | B | compra | nao | proximo | 0.15 | 0.03 | +0.03 | 0.5 | 0.272 | 1 | 2026-10-17 01:06 |
| ARB/USDT | B | venda | nao | proximo | 0.20 | 0.20 | +0.20 | 0.215 | 0.426 | 1 | 2026-10-16 22:06 |
| LINK/USDT | A | venda | nao | proximo | 3.98 | 0.03 | +0.03 | 0.692 | 0.546 | 1 | 2026-10-16 16:06 |
| WLD/USDT | B | venda | nao | proximo | 2.50 | 1.03 | +1.03 | 0.032 | 1.503 | 1 | 2026-10-16 12:06 |
| WLD/USDT | B | venda | nao | proximo | 2.34 | 1.24 | +1.24 | 0.34 | 1.595 | 3 | 2026-10-16 10:06 |
| UNI/USDT | B | venda | nao | proximo | 1.20 | 0.21 | +0.21 | 0.321 | 0.313 | 1 | 2026-10-16 10:06 |
| UNI/USDT | B | compra | nao | proximo | 1.04 | 0.72 | +0.72 | 0.0 | 0.964 | 1 | 2026-10-16 02:06 |
| ARB/USDT | B | venda | sim | proximo | 5.71 | 2.10 | -1.00 | 1.214 | 0.731 | 4 | 2026-10-15 23:06 |
| UNI/USDT | B | venda | nao | proximo | 5.43 | 0.76 | +0.76 | 0.892 | 1.3 | 2 | 2026-10-15 23:06 |
| XRP/USDT | B | compra | nao | proximo | 2.26 | 1.63 | -1.00 | 1.605 | 0.737 | 24 | 2026-10-15 13:06 |
| BTC/USDT | B | compra | nao | proximo | 0.03 | 0.03 | +0.03 | 0.07 | 0.429 | 1 | 2026-10-15 12:06 |
