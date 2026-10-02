# Calibracao — registro mecanico de sinais (atualizado 2026-10-02 10:05 BRT)

> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preco (OHLC de 1h contra stop/alvo sugeridos).
>
> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' enviesa o dado pela sua propria selecao — que e justamente a variavel que se quer isolar pra calibrar parametro. Os descartes sao os contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores ou vencedores.
>
> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer parametros com historico de verdade, use `python monitor/replay.py --varrer stop_buffer` (ou `alvo`, ou `min_rr`).

Regra de alvo em vigor agora: **proximo** (coluna `Regra` abaixo mostra qual decidiu cada sinal -- ver CHANGELOG v6).

| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |
|---|---|---|---|---|
| Aceitos (R:R >= 2) | 64 | 64 | 14 (22%) | -12.61R (-0.197R/sinal) |
| Descartados por R:R baixo | 213 | 212 | 132 (62%) | -11.58R (-0.055R/sinal) |
| TODOS | 277 | 276 | 146 (53%) | -24.19R (-0.088R/sinal) |

**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) — n=146, mediana 0.35R, maximo 0.98R, 8% acima de 0.8R.

> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra apertar o stop.

**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) — n=130, mediana 0.39R, 22% chegaram a 1R a favor.

> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, o problema esta no ALVO/saida, nao na entrada. Se a mediana for baixa, o problema esta na entrada e mexer no alvo nao resolve.

## Ultimos 25 sinais mecanicos

| Par | Setup | Direcao | Aceito | Regra | R:R (recente) | R:R (proximo) | Resultado | MAE | MFE | Candles | Quando |
|---|---|---|---|---|---|---|---|---|---|---|---|
| DOGE/USDT | B | venda | nao | proximo | 6.02 | 0.59 | -1.00 | 1.97 | 0.675 | 1 | 2026-10-02 09:05 |
| ETH/USDT | B | venda | sim | proximo | 6.38 | 6.38 | -1.00 | 2.315 | 1.308 | 3 | 2026-10-02 07:05 |
| DOGE/USDT | B | venda | nao | proximo | 6.23 | 0.33 | +0.33 | 0.179 | 0.976 | 1 | 2026-10-02 07:05 |
| DOGE/USDT | B | venda | nao | proximo | 2.60 | 0.55 | -1.00 | 2.009 | 0.421 | 3 | 2026-10-02 03:05 |
| WLD/USDT | B | compra | nao | proximo | 1.11 | 0.30 | +0.30 | 0.355 | 1.072 | 2 | 2026-10-02 02:05 |
| UNI/USDT | B | compra | nao | proximo | 0.07 | 0.07 | +0.07 | 0.624 | 0.078 | 1 | 2026-10-02 02:05 |
| ETH/USDT | B | venda | sim | proximo | 2.91 | 2.91 | -1.00 | 2.783 | 0.492 | 1 | 2026-10-02 01:05 |
| SOL/USDT | A | compra | nao | proximo | 3.36 | 0.05 | +0.05 | 0.184 | 1.505 | 1 | 2026-10-02 00:05 |
| WLD/USDT | A | compra | nao | proximo | 3.27 | 0.31 | +0.31 | 0.161 | 0.483 | 1 | 2026-10-01 23:05 |
| BTC/USDT | A | compra | nao | proximo | 2.00 | 0.38 | +0.38 | 0.407 | 0.594 | 1 | 2026-10-01 20:05 |
| ETH/USDT | B | venda | nao | proximo | 2.48 | 1.61 | -1.00 | 1.108 | 0.979 | 4 | 2026-10-01 18:05 |
| LINK/USDT | B | venda | nao | proximo | 1.58 | 0.86 | +0.86 | 0.111 | 1.229 | 1 | 2026-10-01 18:05 |
| SUI/USDT | A | compra | nao | proximo | 0.09 | 0.04 | +0.04 | 0.387 | 0.168 | 1 | 2026-10-01 17:05 |
| ETH/USDT | B | venda | nao | proximo | 1.64 | 1.11 | -1.00 | 1.121 | 0.725 | 7 | 2026-10-01 16:05 |
| UNI/USDT | B | compra | nao | proximo | 0.97 | 0.10 | +0.10 | 0.487 | 0.309 | 1 | 2026-10-01 15:05 |
| BTC/USDT | B | compra | nao | proximo | 0.58 | 0.03 | +0.03 | 0.286 | 1.129 | 1 | 2026-10-01 13:05 |
| SUI/USDT | B | compra | nao | proximo | 1.18 | 0.52 | +0.52 | 0.189 | 0.792 | 1 | 2026-10-01 13:05 |
| ETH/USDT | B | venda | nao | proximo | 0.95 | 0.45 | +0.45 | 0.321 | 0.944 | 1 | 2026-10-01 12:06 |
| BTC/USDT | B | compra | nao | proximo | 0.89 | 0.38 | +0.38 | 0.726 | 0.757 | 1 | 2026-10-01 11:06 |
| ETH/USDT | B | venda | nao | proximo | 0.91 | 0.49 | +0.49 | 0.61 | 0.538 | 2 | 2026-10-01 10:06 |
| LINK/USDT | B | venda | nao | proximo | 1.34 | 0.54 | +0.54 | 0.548 | 0.714 | 1 | 2026-10-01 10:06 |
| BTC/USDT | B | compra | nao | proximo | 0.71 | 0.27 | +0.27 | 0.871 | 0.593 | 4 | 2026-10-01 08:06 |
| BTC/USDT | B | compra | nao | proximo | 4.78 | 0.65 | +0.65 | 0.02 | 0.756 | 1 | 2026-10-01 06:06 |
| UNI/USDT | B | compra | nao | proximo | 0.60 | 0.11 | +0.11 | 0.176 | 0.319 | 1 | 2026-10-01 06:06 |
| ETH/USDT | B | venda | sim | proximo | 4.56 | 4.01 | +4.01 | 0.713 | 4.916 | 1 | 2026-10-01 04:06 |
