# Sinais -- atualizado 2026-09-10 23:05 BRT

> Gerado a partir de `claude/trade_journal.db` a cada execucao. **Edite as colunas Status (candidato/entrado/descartado), Resultado (R) e Conta 30? (sim/nao) direto neste arquivo** -- a proxima execucao le suas mudancas e aplica ao banco antes de reescrever o arquivo, entao suas edicoes nunca se perdem. NAO edite a ordem ou os nomes das colunas, so os valores dessas tres. Resultado (R) de um trade 'entrado' pode ser preenchido automaticamente pelo script quando o stop ou o alvo sugerido forem tocados numa candle de 1h -- edite manualmente so se voce operou com stop/alvo diferentes dos sugeridos (sua edicao sempre tem prioridade). Conta 30? nasce 'sim' -- mude para 'nao' se este trade nao deve contar para o gate de validacao (ex.: duplicata de um lote correlacionado). Preco de entrada / Stop / Alvo / R:R aqui sao SUGESTOES MECANICAS SIMPLES (preco de entrada = fechamento do candle 1h de confirmacao; stop = extremo da varredura + buffer de ATR; alvo = pivo 1h oposto mais recente) -- validar no grafico antes de usar, nao substituem o checklist da secao 4 do plano. So aparecem aqui sinais que ja passaram no filtro de R:R minimo (2) do plano.

| ID | Par | Setup | Direcao | Preco entrada | Stop sugerido | Alvo sugerido | R:R sugerido | Tend. 4h | Status | Resultado (R) | Conta 30? | Criado em |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 32 | SUI/USDT | B | compra | 0.73260 | 0.72556 | 0.77040 | 5.37 | lateral | candidato | — | sim | 2026-09-10 22:05 |
| 31 | DOGE/USDT | B | venda | 0.08403 | 0.08433 | 0.08256 | 4.95 | baixa | candidato | — | sim | 2026-09-10 19:05 |
| 30 | XRP/USDT | B | compra | 1.3597 | 1.3503 | 1.4388 | 8.40 | lateral | candidato | — | sim | 2026-09-10 15:05 |
| 29 | ETH/USDT | B | compra | 2442.4 | 2423.6 | 2483.7 | 2.20 | lateral | entrado | — | sim | 2026-09-10 12:05 |
| 28 | XRP/USDT | B | compra | 1.3635 | 1.3467 | 1.4388 | 4.48 | lateral | entrado | -1.00 | sim | 2026-09-10 11:06 |
| 27 | LINK/USDT | B | venda | 11.78 | 11.87 | 11.58 | 2.11 | lateral | entrado | -1.00 | sim | 2026-09-10 05:06 |
| 26 | SOL/USDT | B | compra | 102.05 | 101.44 | 104.78 | 4.48 | lateral | entrado | -1.00 | sim | 2026-09-10 03:05 |
| 25 | LINK/USDT | B | venda | 11.81 | 11.89 | 11.58 | 2.89 | lateral | entrado | -1.00 | sim | 2026-09-10 01:05 |
| 24 | BTC/USDT | B | venda | 78297.4 | 78567.7 | 77710.0 | 2.17 | baixa | entrado | 2.17 | sim | 2026-09-10 01:05 |
| 23 | XRP/USDT | B | compra | 1.3914 | 1.3783 | 1.4388 | 3.61 | lateral | entrado | -1.00 | sim | 2026-09-10 00:05 |
| 22 | ETH/USDT | A | venda | 2463.7 | 2472.6 | 2440.4 | 2.63 | baixa | entrado | -1.00 | sim | 2026-09-09 22:05 |
| 21 | SUI/USDT | B | compra | 0.78540 | 0.77524 | 0.82940 | 4.33 | lateral | entrado | -1.00 | nao | 2026-09-09 18:05 |
| 20 | XRP/USDT | B | compra | 1.4028 | 1.3921 | 1.4388 | 3.36 | alta | entrado | -1.00 | nao | 2026-09-09 18:05 |
| 19 | SOL/USDT | B | compra | 102.50 | 101.66 | 104.78 | 2.70 | lateral | entrado | -1.00 | sim | 2026-09-09 18:05 |
| 18 | ETH/USDT | B | compra | 2470.6 | 2449.7 | 2520.4 | 2.38 | lateral | entrado | -1.00 | sim | 2026-09-09 18:05 |
| 17 | XRP/USDT | B | venda | 1.4225 | 1.4355 | 1.3830 | 3.05 | alta | entrado | -1.00 | sim | 2026-09-08 17:05 |
| 16 | DOGE/USDT | B | venda | 0.09000 | 0.09092 | 0.08784 | 2.34 | lateral | descartado | — | sim | 2026-09-08 15:05 |
| 15 | UNI/USDT | B | compra | 6.9280 | 6.8065 | 7.1920 | 2.17 | baixa | entrado | -1.00 | sim | 2026-09-08 13:05 |
| 14 | ETH/USDT | B | compra | 2484.6 | 2454.2 | 2499.4 | 0.49 | alta | descartado | — | sim | 2026-09-08 12:05 |
| 13 | BTC/USDT | B | venda | 77941.9 | 78554.3 | 77436.2 | 0.83 | lateral | descartado | — | sim | 2026-09-08 11:06 |
| 12 | SUI/USDT | B | venda | 0.80990 | 0.82385 | 0.80880 | 0.08 | alta | descartado | — | sim | 2026-09-08 09:05 |
| 11 | DOGE/USDT | B | venda | 0.08951 | 0.09028 | 0.08876 | 0.97 | lateral | descartado | — | sim | 2026-09-08 09:05 |
| 10 | XRP/USDT | B | venda | 1.3971 | 1.4042 | 1.3804 | 2.36 | lateral | entrado | -1.00 | sim | 2026-09-08 08:05 |
| 9 | ETH/USDT | B | venda | 2480.2 | 2500.8 | 2461.5 | 0.91 | alta | descartado | — | sim | 2026-09-08 08:05 |
| 8 | XRP/USDT | B | compra | 1.3894 | 1.3820 | 1.4067 | 2.35 | lateral | entrado | 2.35 | sim | 2026-09-08 06:05 |
| 7 | DOGE/USDT | B | venda | 0.08960 | 0.09009 | 0.08854 | 2.17 | lateral | entrado | -1.00 | sim | 2026-09-08 02:05 |
| 6 | SOL/USDT | B | venda | 102.93 | 103.47 | 102.85 | 0.15 | alta | descartado | — | sim | 2026-09-08 02:05 |
| 5 | XRP/USDT | B | venda | 1.3962 | 1.4012 | 1.3739 | 4.50 | lateral | entrado | -1.00 | sim | 2026-09-07 19:49 |
| 4 | ETH/USDT | B | venda | 2490.0 | 2497.4 | 2463.6 | 3.57 | alta | entrado | -1.00 | sim | 2026-09-07 19:49 |
| 3 | BTC/USDT | B | venda | 79120.0 | 79267.0 | 78619.6 | 3.41 | alta | entrado | -1.00 | sim | 2026-09-07 19:49 |
| 2 | XRP/USDT | B | venda | — | — | — | — | lateral | descartado | — | sim | 2026-09-07 19:06 |
| 1 | ETH/USDT | B | venda | — | — | — | — | alta | descartado | — | sim | 2026-09-07 19:06 |
