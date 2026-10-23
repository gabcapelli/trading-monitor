# Log de Monitoramento Automatico -- Multi-Par (script gratuito, GitHub Actions)

> Gerado por script Python sem LLM (ver monitor/fetch_and_check.py). Fonte: OKX. Cobre os pares em PAIRS (configuracao no topo do script) -- BTC-USDT-SWAP e os demais adicionados na expansao de 07/09/2026. Leitura e MECANICA (regras objetivas da secao 4 do plano), sem a prosa qualitativa que o Claude gerava -- cole este log numa conversa do Claude se quiser a leitura interpretativa.

| Data/Hora (BRT) | Par | Close 1h | High/Low 1h | Close 4h | Swing 1h ref | ATR 1h | Funding | Zona ativa | Status checklist |
|---|---|---|---|---|---|---|---|---|---|
| 2026-10-21 03:06 | BTC-USDT-SWAP | 82640.1 | 82932.6/82587.5 | 82694.5 | res 83188.8 (ha 5 candles) | 297.36 | 0.0046% | B/compra@82752.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-21 03:06 | ETH-USDT-SWAP | 2437.9 | 2450.6/2436.6 | 2443.3 | res 2464.5 (ha 4 candles) | 13.94 | 0.0077% | — | sem_zona |
| 2026-10-21 03:06 | SOL-USDT-SWAP | 105.64 | 106.15/105.54 | 105.78 | res 107.17 (ha 7 candles) | 0.75143 | 0.0052% | — | zona_expirada_setup_B |
| 2026-10-21 03:06 | XRP-USDT-SWAP | 1.3331 | 1.3383/1.3322 | 1.3316 | res 1.3441 (ha 7 candles) | 0.00843 | 0.0099% | — | sem_zona |
| 2026-10-21 03:06 | DOGE-USDT-SWAP | 0.08133 | 0.08180/0.08131 | 0.08146 | — | 0.00053 | 0.0100% | B/compra@0.08092 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-21 03:06 | ARB-USDT-SWAP | 0.18765 | 0.19146/0.18731 | 0.19082 | res 0.19682 (ha 4 candles) | 0.00331 | -0.0085% | B/venda@0.19508 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-21 03:06 | WLD-USDT-SWAP | 0.58420 | 0.59180/0.58210 | 0.59090 | sup 0.57920 (ha 4 candles) | 0.01119 | 0.0100% | B/venda@0.57610 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-21 03:06 | SUI-USDT-SWAP | 1.0185 | 1.0278/1.0173 | 1.0256 | res 1.0408 (ha 4 candles) | 0.01016 | 0.0100% | — | sem_zona |
| 2026-10-21 03:06 | UNI-USDT-SWAP | 7.4190 | 7.5100/7.4170 | 7.5370 | res 7.7850 (ha 4 candles) | 0.13157 | -0.0019% | B/compra@7.4520 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-21 03:06 | LINK-USDT-SWAP | 12.28 | 12.37/12.27 | 12.32 | res 12.46 (ha 4 candles) | 0.09336 | -0.0028% | B/compra@12.25 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-21 04:06 | BTC-USDT-SWAP | 82767.3 | 82888.0/82605.5 | 82694.5 | res 83188.8 (ha 6 candles) | 282.42 | 0.0062% | B/compra@82752.0 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-21 04:06 | ETH-USDT-SWAP | 2439.0 | 2446.6/2435.5 | 2443.3 | res 2464.5 (ha 5 candles) | 12.96 | 0.0068% | — | sem_zona |
| 2026-10-21 04:06 | SOL-USDT-SWAP | 105.95 | 106.24/105.57 | 105.78 | res 107.17 (ha 8 candles) | 0.69286 | 0.0039% | — | sem_zona |
| 2026-10-21 04:06 | XRP-USDT-SWAP | 1.3332 | 1.3377/1.3319 | 1.3316 | res 1.3441 (ha 8 candles) | 0.00781 | 0.0098% | — | sem_zona |
| 2026-10-21 04:06 | DOGE-USDT-SWAP | 0.08148 | 0.08171/0.08119 | 0.08146 | — | 0.00049 | 0.0100% | B/compra@0.08092 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-21 04:06 | ARB-USDT-SWAP | 0.18956 | 0.18975/0.18742 | 0.19082 | res 0.19682 (ha 5 candles) | 0.00320 | -0.0086% | B/venda@0.19508 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-21 04:06 | WLD-USDT-SWAP | 0.58010 | 0.58570/0.57860 | 0.59090 | sup 0.57920 (ha 5 candles) | 0.01059 | 0.0100% | — | invalidado_setup_B |
| 2026-10-21 04:06 | SUI-USDT-SWAP | 1.0227 | 1.0250/1.0167 | 1.0256 | res 1.0408 (ha 5 candles) | 0.00960 | 0.0100% | — | sem_zona |
| 2026-10-21 04:06 | UNI-USDT-SWAP | 7.4610 | 7.4910/7.3900 | 7.5370 | res 7.7850 (ha 5 candles) | 0.12629 | 0.0018% | — | descartado_rr_baixo_setup_B |
| 2026-10-21 04:06 | LINK-USDT-SWAP | 12.30 | 12.35/12.26 | 12.32 | res 12.46 (ha 5 candles) | 0.08886 | -0.0010% | B/compra@12.25 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-21 05:06 | BTC-USDT-SWAP | 83114.0 | 83238.8/82725.8 | 83114.0 | res 83188.8 (ha 7 candles) | 300.59 | 0.0075% | — | descartado_rr_baixo_setup_B |
| 2026-10-21 05:06 | ETH-USDT-SWAP | 2455.5 | 2458.7/2438.2 | 2455.5 | res 2464.5 (ha 6 candles) | 13.65 | 0.0075% | — | sem_zona |
| 2026-10-21 05:06 | SOL-USDT-SWAP | 106.77 | 106.95/105.90 | 106.77 | res 107.17 (ha 9 candles) | 0.72786 | 0.0041% | — | sem_zona |
| 2026-10-21 05:06 | XRP-USDT-SWAP | 1.3459 | 1.3494/1.3325 | 1.3459 | res 1.3441 (ha 9 candles) | 0.00855 | 0.0100% | A/compra@1.3441 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-21 05:06 | DOGE-USDT-SWAP | 0.08206 | 0.08224/0.08142 | 0.08206 | — | 0.00052 | 0.0100% | B/compra@0.08092 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-21 05:06 | ARB-USDT-SWAP | 0.19060 | 0.19240/0.18928 | 0.19060 | res 0.19682 (ha 6 candles) | 0.00326 | -0.0098% | B/venda@0.19508 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-21 05:06 | WLD-USDT-SWAP | 0.58350 | 0.58790/0.57910 | 0.58350 | sup 0.57920 (ha 6 candles) | 0.01001 | 0.0100% | B/venda@0.58590 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-21 05:06 | SUI-USDT-SWAP | 1.0344 | 1.0379/1.0214 | 1.0344 | res 1.0408 (ha 6 candles) | 0.01012 | 0.0100% | — | sem_zona |
| 2026-10-21 05:06 | UNI-USDT-SWAP | 7.5470 | 7.5870/7.4470 | 7.5470 | res 7.7850 (ha 6 candles) | 0.12807 | 0.0050% | — | sem_zona |
| 2026-10-21 05:06 | LINK-USDT-SWAP | 12.41 | 12.44/12.29 | 12.41 | res 12.46 (ha 6 candles) | 0.09350 | -0.0003% | B/compra@12.25 (2t/1c) | zona_mapeada_setup_B |
| 2026-10-21 06:06 | BTC-USDT-SWAP | 83205.2 | 83681.8/83056.0 | 83114.0 | res 83188.8 (ha 8 candles) | 319.64 | 0.0076% | A/compra@83188.8 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-21 06:06 | ETH-USDT-SWAP | 2452.7 | 2466.5/2449.6 | 2455.5 | res 2464.5 (ha 7 candles) | 13.70 | 0.0075% | — | sem_zona |
| 2026-10-21 06:06 | SOL-USDT-SWAP | 106.55 | 107.23/106.42 | 106.77 | res 107.17 (ha 10 candles) | 0.70786 | 0.0040% | — | sem_zona |
| 2026-10-21 06:06 | XRP-USDT-SWAP | 1.3473 | 1.3544/1.3420 | 1.3459 | res 1.3441 (ha 10 candles) | 0.00857 | 0.0089% | A/compra@1.3441 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-21 06:06 | DOGE-USDT-SWAP | 0.08180 | 0.08226/0.08178 | 0.08206 | — | 0.00053 | 0.0100% | B/compra@0.08092 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-21 06:06 | ARB-USDT-SWAP | 0.18919 | 0.19143/0.18903 | 0.19060 | res 0.19682 (ha 7 candles) | 0.00319 | -0.0130% | B/venda@0.19508 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-21 06:06 | WLD-USDT-SWAP | 0.58440 | 0.58680/0.58100 | 0.58350 | sup 0.57920 (ha 7 candles) | 0.00960 | 0.0100% | B/venda@0.58590 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-21 06:06 | SUI-USDT-SWAP | 1.0291 | 1.0371/1.0286 | 1.0344 | res 1.0408 (ha 7 candles) | 0.00990 | 0.0090% | — | sem_zona |
| 2026-10-21 06:06 | UNI-USDT-SWAP | 7.4950 | 7.5900/7.4940 | 7.5470 | res 7.7850 (ha 7 candles) | 0.12750 | 0.0059% | — | sem_zona |
| 2026-10-21 06:06 | LINK-USDT-SWAP | 12.36 | 12.43/12.35 | 12.41 | res 12.46 (ha 7 candles) | 0.09136 | 0.0014% | B/compra@12.25 (2t/2c) | zona_mapeada_setup_B |
| 2026-10-21 07:06 | BTC-USDT-SWAP | 83397.9 | 83622.0/83183.3 | 83114.0 | res 83188.8 (ha 9 candles) | 331.31 | 0.0075% | A/compra@83188.8 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-21 07:06 | ETH-USDT-SWAP | 2455.3 | 2465.5/2451.7 | 2455.5 | res 2464.5 (ha 8 candles) | 13.50 | 0.0073% | — | sem_zona |
| 2026-10-21 07:06 | SOL-USDT-SWAP | 106.58 | 107.07/106.51 | 106.77 | res 107.17 (ha 11 candles) | 0.67500 | 0.0040% | — | sem_zona |
| 2026-10-21 07:06 | XRP-USDT-SWAP | 1.3556 | 1.3683/1.3472 | 1.3459 | res 1.3441 (ha 11 candles) | 0.00911 | 0.0060% | A/compra@1.3441 (1t/1c) | zona_mapeada_setup_A |
| 2026-10-21 07:06 | DOGE-USDT-SWAP | 0.08187 | 0.08226/0.08173 | 0.08206 | — | 0.00051 | 0.0100% | B/compra@0.08092 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-21 07:06 | ARB-USDT-SWAP | 0.18939 | 0.19084/0.18844 | 0.19060 | res 0.19682 (ha 8 candles) | 0.00313 | -0.0182% | — | zona_expirada_setup_B |
| 2026-10-21 07:06 | WLD-USDT-SWAP | 0.58120 | 0.58650/0.57940 | 0.58350 | sup 0.57860 (ha 3 candles) | 0.00953 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-10-21 07:06 | SUI-USDT-SWAP | 1.0296 | 1.0353/1.0280 | 1.0344 | res 1.0408 (ha 8 candles) | 0.00932 | 0.0068% | — | sem_zona |
| 2026-10-21 07:06 | UNI-USDT-SWAP | 7.4980 | 7.5620/7.4820 | 7.5470 | res 7.7850 (ha 8 candles) | 0.12521 | 0.0041% | — | sem_zona |
| 2026-10-21 07:06 | LINK-USDT-SWAP | 12.34 | 12.42/12.34 | 12.41 | res 12.46 (ha 8 candles) | 0.08900 | 0.0028% | B/compra@12.25 (2t/3c) | zona_mapeada_setup_B |
| 2026-10-21 08:06 | BTC-USDT-SWAP | 83355.6 | 83449.8/83211.0 | 83114.0 | res 83188.8 (ha 10 candles) | 324.75 | 0.0072% | A/compra@83188.8 (2t/0c) | zona_mapeada_setup_A |
| 2026-10-21 08:06 | ETH-USDT-SWAP | 2456.0 | 2458.6/2445.0 | 2455.5 | res 2464.5 (ha 9 candles) | 13.37 | 0.0080% | — | sem_zona |
| 2026-10-21 08:06 | SOL-USDT-SWAP | 106.56 | 106.68/105.92 | 106.77 | res 107.17 (ha 12 candles) | 0.66571 | 0.0023% | — | sem_zona |
| 2026-10-21 08:06 | XRP-USDT-SWAP | 1.3573 | 1.3613/1.3503 | 1.3459 | res 1.3441 (ha 12 candles) | 0.00921 | 0.0031% | A/compra@1.3441 (1t/2c) | zona_mapeada_setup_A |
| 2026-10-21 08:06 | DOGE-USDT-SWAP | 0.08195 | 0.08203/0.08153 | 0.08206 | — | 0.00050 | 0.0100% | B/compra@0.08092 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-21 08:06 | ARB-USDT-SWAP | 0.19188 | 0.19222/0.18853 | 0.19060 | res 0.19682 (ha 9 candles) | 0.00320 | -0.0180% | — | sem_zona |
| 2026-10-21 08:06 | WLD-USDT-SWAP | 0.58170 | 0.58520/0.57530 | 0.58350 | sup 0.57860 (ha 4 candles) | 0.00903 | 0.0100% | B/venda@0.57610 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-21 08:06 | SUI-USDT-SWAP | 1.0298 | 1.0313/1.0220 | 1.0344 | res 1.0379 (ha 3 candles) | 0.00895 | 0.0047% | — | sem_zona |
| 2026-10-21 08:06 | UNI-USDT-SWAP | 7.4560 | 7.5020/7.3740 | 7.5470 | res 7.7850 (ha 9 candles) | 0.12279 | -0.0011% | — | sem_zona |
| 2026-10-21 08:06 | LINK-USDT-SWAP | 12.34 | 12.35/12.28 | 12.41 | res 12.44 (ha 3 candles) | 0.08564 | 0.0046% | — | zona_expirada_setup_B |
| 2026-10-21 09:06 | BTC-USDT-SWAP | 83456.7 | 83559.7/83328.9 | 83456.7 | res 83681.8 (ha 3 candles) | 326.61 | 0.0055% | A/compra@83188.8 (2t/1c) | zona_mapeada_setup_A |
| 2026-10-21 09:06 | ETH-USDT-SWAP | 2468.1 | 2473.0/2456.0 | 2468.1 | res 2464.5 (ha 10 candles) | 13.65 | 0.0071% | A/compra@2464.5 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-21 09:06 | SOL-USDT-SWAP | 106.81 | 107.03/106.56 | 106.81 | res 107.23 (ha 3 candles) | 0.65929 | 0.0016% | — | sem_zona |
| 2026-10-21 09:06 | XRP-USDT-SWAP | 1.3551 | 1.3609/1.3544 | 1.3551 | res 1.3441 (ha 13 candles) | 0.00922 | 0.0009% | A/compra@1.3441 (1t/3c) | zona_mapeada_setup_A |
| 2026-10-21 09:06 | DOGE-USDT-SWAP | 0.08203 | 0.08216/0.08193 | 0.08203 | — | 0.00050 | 0.0084% | — | zona_expirada_setup_B |
| 2026-10-21 09:06 | ARB-USDT-SWAP | 0.19238 | 0.19392/0.19109 | 0.19238 | res 0.19682 (ha 10 candles) | 0.00320 | -0.0140% | — | sem_zona |
| 2026-10-21 09:06 | WLD-USDT-SWAP | 0.59350 | 0.59420/0.58080 | 0.59350 | sup 0.57860 (ha 5 candles) | 0.00913 | 0.0100% | B/venda@0.57610 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-21 09:06 | SUI-USDT-SWAP | 1.0331 | 1.0363/1.0297 | 1.0331 | res 1.0379 (ha 4 candles) | 0.00899 | 0.0050% | — | sem_zona |
| 2026-10-21 09:06 | UNI-USDT-SWAP | 7.4990 | 7.5260/7.4560 | 7.4990 | res 7.5900 (ha 3 candles) | 0.12293 | -0.0049% | — | sem_zona |
| 2026-10-21 09:06 | LINK-USDT-SWAP | 12.38 | 12.42/12.34 | 12.38 | res 12.44 (ha 4 candles) | 0.08729 | 0.0043% | — | sem_zona |
| 2026-10-21 10:06 | BTC-USDT-SWAP | 83462.1 | 83613.7/83411.8 | 83456.7 | res 83681.8 (ha 4 candles) | 323.71 | 0.0036% | A/compra@83188.8 (2t/2c) | zona_mapeada_setup_A |
| 2026-10-21 10:06 | ETH-USDT-SWAP | 2467.9 | 2471.7/2464.2 | 2468.1 | res 2464.5 (ha 11 candles) | 13.42 | 0.0066% | A/compra@2464.5 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-21 10:06 | SOL-USDT-SWAP | 106.95 | 107.07/106.75 | 106.81 | res 107.23 (ha 4 candles) | 0.64357 | 0.0002% | — | sem_zona |
| 2026-10-21 10:06 | XRP-USDT-SWAP | 1.3570 | 1.3594/1.3538 | 1.3551 | res 1.3683 (ha 3 candles) | 0.00871 | -0.0002% | A/compra@1.3441 (1t/4c) | zona_mapeada_setup_A |
| 2026-10-21 10:06 | DOGE-USDT-SWAP | 0.08212 | 0.08212/0.08189 | 0.08203 | — | 0.00047 | 0.0063% | — | sem_zona |
| 2026-10-21 10:06 | ARB-USDT-SWAP | 0.19235 | 0.19283/0.19064 | 0.19238 | res 0.19682 (ha 11 candles) | 0.00317 | -0.0122% | — | sem_zona |
| 2026-10-21 10:06 | WLD-USDT-SWAP | 0.59380 | 0.59650/0.58890 | 0.59350 | sup 0.57860 (ha 6 candles) | 0.00916 | 0.0100% | B/venda@0.57610 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-21 10:06 | SUI-USDT-SWAP | 1.0353 | 1.0381/1.0321 | 1.0331 | res 1.0379 (ha 5 candles) | 0.00891 | 0.0064% | — | sem_zona |
| 2026-10-21 10:06 | UNI-USDT-SWAP | 7.4830 | 7.5160/7.4620 | 7.4990 | res 7.5900 (ha 4 candles) | 0.11921 | -0.0064% | — | sem_zona |
| 2026-10-21 10:06 | LINK-USDT-SWAP | 12.42 | 12.42/12.37 | 12.38 | res 12.44 (ha 5 candles) | 0.08671 | 0.0022% | — | sem_zona |
| 2026-10-21 11:06 | BTC-USDT-SWAP | 83784.1 | 83947.5/83233.0 | 83456.7 | res 83681.8 (ha 5 candles) | 359.21 | 0.0021% | — | descartado_rr_baixo_setup_A |
| 2026-10-21 11:06 | ETH-USDT-SWAP | 2472.1 | 2497.8/2456.6 | 2468.1 | res 2464.5 (ha 12 candles) | 15.60 | 0.0066% | A/compra@2464.5 (2t/0c) | zona_mapeada_setup_A |
| 2026-10-21 11:06 | SOL-USDT-SWAP | 106.71 | 107.72/106.18 | 106.81 | res 107.23 (ha 5 candles) | 0.71286 | 0.0006% | — | sem_zona |
| 2026-10-21 11:06 | XRP-USDT-SWAP | 1.3574 | 1.3662/1.3518 | 1.3551 | res 1.3683 (ha 4 candles) | 0.00940 | -0.0012% | A/compra@1.3441 (1t/5c) | zona_mapeada_setup_A |
| 2026-10-21 11:06 | DOGE-USDT-SWAP | 0.08211 | 0.08266/0.08175 | 0.08203 | — | 0.00052 | 0.0038% | — | sem_zona |
| 2026-10-21 11:06 | ARB-USDT-SWAP | 0.19189 | 0.19489/0.19118 | 0.19238 | res 0.19682 (ha 12 candles) | 0.00330 | -0.0091% | — | sem_zona |
| 2026-10-21 11:06 | WLD-USDT-SWAP | 0.57570 | 0.59560/0.57310 | 0.59350 | sup 0.57860 (ha 7 candles) | 0.01036 | 0.0089% | — | confirmado_calibracao_setup_B |
| 2026-10-21 11:06 | SUI-USDT-SWAP | 1.0295 | 1.0434/1.0260 | 1.0331 | res 1.0379 (ha 6 candles) | 0.00985 | 0.0075% | — | sem_zona |
| 2026-10-21 11:06 | UNI-USDT-SWAP | 7.4330 | 7.5720/7.3590 | 7.4990 | res 7.5900 (ha 5 candles) | 0.13057 | -0.0060% | — | sem_zona |
| 2026-10-21 11:06 | LINK-USDT-SWAP | 12.37 | 12.53/12.32 | 12.38 | res 12.44 (ha 6 candles) | 0.09636 | -0.0026% | — | sem_zona |
| 2026-10-21 12:06 | BTC-USDT-SWAP | 84545.9 | 84735.2/83571.2 | 83456.7 | res 83681.8 (ha 6 candles) | 416.73 | 0.0029% | A/compra@83681.8 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-21 12:06 | ETH-USDT-SWAP | 2495.7 | 2503.0/2462.8 | 2468.1 | res 2464.5 (ha 13 candles) | 17.38 | 0.0052% | — | descartado_rr_baixo_setup_A |
| 2026-10-21 12:06 | SOL-USDT-SWAP | 107.64 | 108.03/106.23 | 106.81 | res 107.23 (ha 6 candles) | 0.78929 | 0.0007% | A/compra@107.23 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-21 12:06 | XRP-USDT-SWAP | 1.3827 | 1.3877/1.3540 | 1.3551 | res 1.3683 (ha 5 candles) | 0.01128 | 0.0003% | A/compra@1.3441 (1t/6c) | zona_mapeada_setup_A |
| 2026-10-21 12:06 | DOGE-USDT-SWAP | 0.08312 | 0.08339/0.08179 | 0.08203 | — | 0.00058 | 0.0029% | B/venda@0.08286 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-21 12:06 | ARB-USDT-SWAP | 0.19394 | 0.19443/0.19025 | 0.19238 | res 0.19682 (ha 13 candles) | 0.00340 | -0.0040% | — | sem_zona |
| 2026-10-21 12:06 | WLD-USDT-SWAP | 0.57750 | 0.57940/0.56530 | 0.59350 | sup 0.57860 (ha 8 candles) | 0.01063 | 0.0062% | — | sem_zona |
| 2026-10-21 12:06 | SUI-USDT-SWAP | 1.0435 | 1.0463/1.0222 | 1.0331 | res 1.0379 (ha 7 candles) | 0.01065 | 0.0088% | A/compra@1.0379 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-21 12:06 | UNI-USDT-SWAP | 7.5340 | 7.5480/7.3750 | 7.4990 | res 7.5900 (ha 6 candles) | 0.12271 | -0.0060% | B/compra@7.4520 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-21 12:06 | LINK-USDT-SWAP | 12.54 | 12.57/12.31 | 12.38 | res 12.44 (ha 7 candles) | 0.10621 | -0.0048% | A/compra@12.44 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-21 13:06 | BTC-USDT-SWAP | 84502.1 | 84799.9/84339.2 | 84502.1 | res 83681.8 (ha 7 candles) | 417.26 | 0.0035% | A/compra@83681.8 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-21 13:06 | ETH-USDT-SWAP | 2511.2 | 2514.5/2495.0 | 2511.2 | res 2464.5 (ha 14 candles) | 17.12 | 0.0029% | — | sem_zona |
| 2026-10-21 13:06 | SOL-USDT-SWAP | 108.44 | 108.88/107.50 | 108.44 | res 107.23 (ha 7 candles) | 0.82214 | 0.0021% | A/compra@107.23 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-21 13:06 | XRP-USDT-SWAP | 1.3803 | 1.3864/1.3725 | 1.3803 | res 1.3683 (ha 6 candles) | 0.01155 | 0.0020% | A/compra@1.3441 (1t/7c) | zona_mapeada_setup_A |
| 2026-10-21 13:06 | DOGE-USDT-SWAP | 0.08344 | 0.08377/0.08298 | 0.08344 | — | 0.00060 | 0.0030% | — | invalidado_setup_B |
| 2026-10-21 13:06 | ARB-USDT-SWAP | 0.19661 | 0.19849/0.19366 | 0.19661 | res 0.19682 (ha 14 candles) | 0.00309 | 0.0019% | B/compra@0.19834 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-21 13:06 | WLD-USDT-SWAP | 0.57360 | 0.57880/0.56960 | 0.57360 | sup 0.57860 (ha 9 candles) | 0.01029 | 0.0065% | — | sem_zona |
| 2026-10-21 13:06 | SUI-USDT-SWAP | 1.0491 | 1.0507/1.0391 | 1.0491 | res 1.0379 (ha 8 candles) | 0.01059 | 0.0054% | — | descartado_rr_baixo_setup_A |
| 2026-10-21 13:06 | UNI-USDT-SWAP | 7.6170 | 7.6610/7.5310 | 7.6170 | res 7.5900 (ha 7 candles) | 0.11214 | -0.0053% | B/compra@7.4520 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-21 13:06 | LINK-USDT-SWAP | 12.69 | 12.70/12.53 | 12.69 | res 12.44 (ha 8 candles) | 0.10829 | -0.0071% | A/compra@12.44 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-21 14:06 | BTC-USDT-SWAP | 84508.2 | 84876.0/84449.9 | 84502.1 | res 83681.8 (ha 8 candles) | 425.52 | 0.0040% | A/compra@83681.8 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-21 14:06 | ETH-USDT-SWAP | 2508.5 | 2527.6/2502.6 | 2511.2 | res 2464.5 (ha 15 candles) | 18.14 | 0.0020% | B/compra@2496.2 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-21 14:06 | SOL-USDT-SWAP | 108.26 | 108.83/108.11 | 108.44 | res 107.23 (ha 8 candles) | 0.82214 | 0.0053% | A/compra@107.23 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-21 14:06 | XRP-USDT-SWAP | 1.3800 | 1.3857/1.3760 | 1.3803 | res 1.3683 (ha 7 candles) | 0.01169 | 0.0028% | — | zona_expirada_setup_A |
| 2026-10-21 14:06 | DOGE-USDT-SWAP | 0.08326 | 0.08365/0.08309 | 0.08344 | — | 0.00059 | 0.0068% | — | sem_zona |
| 2026-10-21 14:06 | ARB-USDT-SWAP | 0.19422 | 0.19680/0.19411 | 0.19661 | res 0.19682 (ha 15 candles) | 0.00309 | 0.0057% | B/compra@0.19834 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-21 14:06 | WLD-USDT-SWAP | 0.57070 | 0.57690/0.57020 | 0.57360 | sup 0.57860 (ha 10 candles) | 0.01001 | 0.0100% | — | sem_zona |
| 2026-10-21 14:06 | SUI-USDT-SWAP | 1.0434 | 1.0521/1.0429 | 1.0491 | res 1.0379 (ha 9 candles) | 0.01049 | 0.0012% | — | sem_zona |
| 2026-10-21 14:06 | UNI-USDT-SWAP | 7.5600 | 7.6370/7.5530 | 7.6170 | res 7.5900 (ha 8 candles) | 0.10936 | -0.0043% | B/compra@7.4520 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-21 14:06 | LINK-USDT-SWAP | 12.63 | 12.76/12.63 | 12.69 | res 12.44 (ha 9 candles) | 0.11071 | -0.0094% | A/compra@12.44 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-21 15:06 | BTC-USDT-SWAP | 84639.9 | 84670.6/84346.6 | 84502.1 | res 83681.8 (ha 9 candles) | 438.31 | 0.0041% | A/compra@83681.8 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-21 15:06 | ETH-USDT-SWAP | 2513.7 | 2518.5/2502.1 | 2511.2 | res 2464.5 (ha 16 candles) | 18.75 | 0.0009% | B/compra@2496.2 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-21 15:06 | SOL-USDT-SWAP | 108.52 | 108.72/107.88 | 108.44 | res 107.23 (ha 9 candles) | 0.84786 | 0.0067% | A/compra@107.23 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-21 15:06 | XRP-USDT-SWAP | 1.3877 | 1.3882/1.3759 | 1.3803 | res 1.3683 (ha 8 candles) | 0.01232 | 0.0040% | A/compra@1.3683 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-21 15:06 | DOGE-USDT-SWAP | 0.08327 | 0.08342/0.08301 | 0.08344 | — | 0.00060 | 0.0093% | — | sem_zona |
| 2026-10-21 15:06 | ARB-USDT-SWAP | 0.19498 | 0.19660/0.19315 | 0.19661 | res 0.19682 (ha 16 candles) | 0.00315 | 0.0079% | B/compra@0.19834 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-21 15:06 | WLD-USDT-SWAP | 0.57240 | 0.57430/0.56970 | 0.57360 | sup 0.56530 (ha 3 candles) | 0.00979 | 0.0100% | — | sem_zona |
| 2026-10-21 15:06 | SUI-USDT-SWAP | 1.0452 | 1.0500/1.0410 | 1.0491 | res 1.0379 (ha 10 candles) | 0.01071 | 0.0003% | — | sem_zona |
| 2026-10-21 15:06 | UNI-USDT-SWAP | 7.6000 | 7.6590/7.5350 | 7.6170 | res 7.5900 (ha 9 candles) | 0.11193 | -0.0036% | B/compra@7.4520 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-21 15:06 | LINK-USDT-SWAP | 12.67 | 12.74/12.60 | 12.69 | res 12.44 (ha 10 candles) | 0.11721 | -0.0099% | A/compra@12.44 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-21 16:06 | BTC-USDT-SWAP | 84380.4 | 84833.7/84355.0 | 84502.1 | res 83681.8 (ha 10 candles) | 460.33 | 0.0033% | A/compra@83681.8 (0t/4c) | zona_mapeada_setup_A |
| 2026-10-21 16:06 | ETH-USDT-SWAP | 2496.2 | 2519.7/2494.0 | 2511.2 | res 2464.5 (ha 17 candles) | 20.18 | -0.0005% | B/compra@2496.2 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-21 16:06 | SOL-USDT-SWAP | 108.03 | 109.17/107.98 | 108.44 | res 107.23 (ha 10 candles) | 0.90857 | 0.0076% | A/compra@107.23 (0t/4c) | zona_mapeada_setup_A |
| 2026-10-21 16:06 | XRP-USDT-SWAP | 1.3870 | 1.3985/1.3852 | 1.3803 | res 1.3683 (ha 9 candles) | 0.01305 | 0.0048% | A/compra@1.3683 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-21 16:06 | DOGE-USDT-SWAP | 0.08289 | 0.08379/0.08280 | 0.08344 | — | 0.00065 | 0.0100% | — | sem_zona |
| 2026-10-21 16:06 | ARB-USDT-SWAP | 0.19466 | 0.19814/0.19429 | 0.19661 | res 0.19849 (ha 3 candles) | 0.00327 | 0.0096% | — | invalidado_setup_B |
| 2026-10-21 16:06 | WLD-USDT-SWAP | 0.57020 | 0.57730/0.56840 | 0.57360 | sup 0.56530 (ha 4 candles) | 0.00967 | 0.0100% | — | sem_zona |
| 2026-10-21 16:06 | SUI-USDT-SWAP | 1.0421 | 1.0560/1.0406 | 1.0491 | res 1.0379 (ha 11 candles) | 0.01141 | -0.0009% | — | sem_zona |
| 2026-10-21 16:06 | UNI-USDT-SWAP | 7.6100 | 7.7300/7.5930 | 7.6170 | res 7.5900 (ha 10 candles) | 0.11593 | 0.0010% | B/compra@7.4520 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-21 16:06 | LINK-USDT-SWAP | 12.68 | 12.80/12.66 | 12.69 | res 12.44 (ha 11 candles) | 0.12357 | -0.0095% | A/compra@12.44 (0t/4c) | zona_mapeada_setup_A |
| 2026-10-21 17:06 | BTC-USDT-SWAP | 84437.0 | 84558.0/84133.3 | 84437.0 | res 84876.0 (ha 3 candles) | 466.01 | 0.0001% | A/compra@83681.8 (0t/5c) | zona_mapeada_setup_A |
| 2026-10-21 17:06 | ETH-USDT-SWAP | 2493.3 | 2499.1/2482.5 | 2493.3 | res 2527.6 (ha 3 candles) | 20.36 | 0.0001% | B/compra@2496.2 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-21 17:06 | SOL-USDT-SWAP | 108.24 | 108.40/107.32 | 108.24 | res 107.23 (ha 11 candles) | 0.94214 | 0.0092% | — | descartado_rr_baixo_setup_A |
| 2026-10-21 17:06 | XRP-USDT-SWAP | 1.3882 | 1.3933/1.3775 | 1.3882 | res 1.3683 (ha 10 candles) | 0.01374 | 0.0064% | A/compra@1.3683 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-21 17:06 | DOGE-USDT-SWAP | 0.08291 | 0.08318/0.08260 | 0.08291 | — | 0.00065 | 0.0100% | — | sem_zona |
| 2026-10-21 17:06 | ARB-USDT-SWAP | 0.19555 | 0.19715/0.19266 | 0.19555 | res 0.19849 (ha 4 candles) | 0.00330 | 0.0100% | — | sem_zona |
| 2026-10-21 17:06 | WLD-USDT-SWAP | 0.56930 | 0.57220/0.56550 | 0.56930 | — | 0.00946 | 0.0100% | — | sem_zona |
| 2026-10-21 17:06 | SUI-USDT-SWAP | 1.0420 | 1.0437/1.0337 | 1.0420 | res 1.0379 (ha 12 candles) | 0.01137 | -0.0010% | — | sem_zona |
| 2026-10-21 17:06 | UNI-USDT-SWAP | 7.5910 | 7.6360/7.5110 | 7.5910 | res 7.5900 (ha 11 candles) | 0.11821 | 0.0041% | B/compra@7.4520 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-21 17:06 | LINK-USDT-SWAP | 12.68 | 12.70/12.60 | 12.68 | res 12.44 (ha 12 candles) | 0.12371 | -0.0097% | A/compra@12.44 (0t/5c) | zona_mapeada_setup_A |
| 2026-10-21 18:06 | BTC-USDT-SWAP | 84636.0 | 84804.2/84384.0 | 84437.0 | res 84876.0 (ha 4 candles) | 475.85 | -0.0019% | A/compra@83681.8 (0t/6c) | zona_mapeada_setup_A |
| 2026-10-21 18:06 | ETH-USDT-SWAP | 2491.5 | 2497.8/2489.0 | 2493.3 | res 2527.6 (ha 4 candles) | 20.20 | 0.0007% | — | invalidado_setup_B |
| 2026-10-21 18:06 | SOL-USDT-SWAP | 107.99 | 108.47/107.90 | 108.24 | res 107.23 (ha 12 candles) | 0.93500 | 0.0085% | B/compra@108.37 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-21 18:06 | XRP-USDT-SWAP | 1.3844 | 1.3922/1.3832 | 1.3882 | res 1.3683 (ha 11 candles) | 0.01397 | 0.0059% | A/compra@1.3683 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-21 18:06 | DOGE-USDT-SWAP | 0.08291 | 0.08315/0.08279 | 0.08291 | — | 0.00064 | 0.0100% | — | sem_zona |
| 2026-10-21 18:06 | ARB-USDT-SWAP | 0.19496 | 0.19698/0.19406 | 0.19555 | res 0.19849 (ha 5 candles) | 0.00334 | 0.0100% | — | sem_zona |
| 2026-10-21 18:06 | WLD-USDT-SWAP | 0.57410 | 0.57520/0.56840 | 0.56930 | — | 0.00944 | 0.0100% | — | sem_zona |
| 2026-10-21 18:06 | SUI-USDT-SWAP | 1.0431 | 1.0487/1.0393 | 1.0420 | res 1.0379 (ha 13 candles) | 0.01145 | -0.0029% | — | sem_zona |
| 2026-10-21 18:06 | UNI-USDT-SWAP | 7.5900 | 7.6260/7.5420 | 7.5910 | res 7.5900 (ha 12 candles) | 0.11700 | 0.0028% | B/compra@7.4520 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-21 18:06 | LINK-USDT-SWAP | 12.66 | 12.73/12.63 | 12.68 | res 12.44 (ha 13 candles) | 0.12400 | -0.0097% | A/compra@12.44 (0t/6c) | zona_mapeada_setup_A |
| 2026-10-21 19:06 | BTC-USDT-SWAP | 84803.9 | 84803.9/84590.9 | 84437.0 | res 84876.0 (ha 5 candles) | 454.42 | -0.0038% | A/compra@83681.8 (0t/7c) | zona_mapeada_setup_A |
| 2026-10-21 19:06 | ETH-USDT-SWAP | 2498.4 | 2500.9/2489.8 | 2493.3 | res 2527.6 (ha 5 candles) | 19.52 | 0.0017% | — | sem_zona |
| 2026-10-21 19:06 | SOL-USDT-SWAP | 108.24 | 108.40/107.83 | 108.24 | res 109.17 (ha 3 candles) | 0.90071 | 0.0080% | — | descartado_rr_baixo_setup_B |
| 2026-10-21 19:06 | XRP-USDT-SWAP | 1.3824 | 1.3864/1.3803 | 1.3882 | res 1.3985 (ha 3 candles) | 0.01320 | 0.0068% | A/compra@1.3683 (0t/4c) | zona_mapeada_setup_A |
| 2026-10-21 19:06 | DOGE-USDT-SWAP | 0.08284 | 0.08310/0.08270 | 0.08291 | — | 0.00061 | 0.0100% | — | sem_zona |
| 2026-10-21 19:06 | ARB-USDT-SWAP | 0.19350 | 0.19558/0.19310 | 0.19555 | res 0.19849 (ha 6 candles) | 0.00329 | 0.0100% | — | sem_zona |
| 2026-10-21 19:06 | WLD-USDT-SWAP | 0.57560 | 0.57710/0.57370 | 0.56930 | — | 0.00905 | 0.0100% | B/venda@0.57610 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-21 19:06 | SUI-USDT-SWAP | 1.0454 | 1.0489/1.0413 | 1.0420 | res 1.0560 (ha 3 candles) | 0.01081 | -0.0029% | — | sem_zona |
| 2026-10-21 19:06 | UNI-USDT-SWAP | 7.6140 | 7.6530/7.5700 | 7.5910 | res 7.7300 (ha 3 candles) | 0.11293 | 0.0022% | B/compra@7.4520 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-21 19:06 | LINK-USDT-SWAP | 12.67 | 12.71/12.64 | 12.68 | res 12.80 (ha 3 candles) | 0.11821 | -0.0088% | A/compra@12.44 (0t/7c) | zona_mapeada_setup_A |
| 2026-10-21 20:06 | BTC-USDT-SWAP | 84400.1 | 84803.9/84400.0 | 84437.0 | res 84876.0 (ha 6 candles) | 438.57 | -0.0045% | — | zona_expirada_setup_A |
| 2026-10-21 20:06 | ETH-USDT-SWAP | 2483.2 | 2498.4/2482.2 | 2493.3 | res 2527.6 (ha 6 candles) | 19.47 | 0.0026% | B/compra@2473.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-21 20:06 | SOL-USDT-SWAP | 107.38 | 108.25/107.33 | 108.24 | res 109.17 (ha 4 candles) | 0.90857 | 0.0057% | — | sem_zona |
| 2026-10-21 20:06 | XRP-USDT-SWAP | 1.3709 | 1.3830/1.3708 | 1.3882 | res 1.3985 (ha 4 candles) | 0.01319 | 0.0076% | A/compra@1.3683 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-21 20:06 | DOGE-USDT-SWAP | 0.08223 | 0.08284/0.08217 | 0.08291 | — | 0.00063 | 0.0100% | — | sem_zona |
| 2026-10-21 20:06 | ARB-USDT-SWAP | 0.19097 | 0.19361/0.19063 | 0.19555 | res 0.19849 (ha 7 candles) | 0.00334 | 0.0100% | — | sem_zona |
| 2026-10-21 20:06 | WLD-USDT-SWAP | 0.57850 | 0.57880/0.57280 | 0.56930 | — | 0.00906 | 0.0100% | — | invalidado_setup_B |
| 2026-10-21 20:06 | SUI-USDT-SWAP | 1.0337 | 1.0453/1.0321 | 1.0420 | res 1.0560 (ha 4 candles) | 0.01116 | 0.0001% | — | sem_zona |
| 2026-10-21 20:06 | UNI-USDT-SWAP | 7.4990 | 7.6190/7.4960 | 7.5910 | res 7.7300 (ha 4 candles) | 0.11486 | -0.0014% | — | zona_expirada_setup_B |
| 2026-10-21 20:06 | LINK-USDT-SWAP | 12.57 | 12.68/12.56 | 12.68 | res 12.80 (ha 4 candles) | 0.12143 | -0.0057% | — | zona_expirada_setup_A |
| 2026-10-21 21:06 | BTC-USDT-SWAP | 84049.9 | 84460.3/84010.2 | 84049.9 | res 84876.0 (ha 7 candles) | 439.39 | -0.0047% | — | sem_zona |
| 2026-10-21 21:06 | ETH-USDT-SWAP | 2473.0 | 2485.4/2469.0 | 2473.0 | res 2527.6 (ha 7 candles) | 19.66 | 0.0038% | B/compra@2473.0 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-21 21:06 | SOL-USDT-SWAP | 106.91 | 107.48/106.65 | 106.91 | res 109.17 (ha 5 candles) | 0.92786 | 0.0038% | — | sem_zona |
| 2026-10-21 21:06 | XRP-USDT-SWAP | 1.3649 | 1.3717/1.3612 | 1.3649 | res 1.3985 (ha 5 candles) | 0.01243 | 0.0092% | — | invalidado_setup_A |
| 2026-10-21 21:06 | DOGE-USDT-SWAP | 0.08193 | 0.08229/0.08173 | 0.08193 | — | 0.00063 | 0.0100% | — | sem_zona |
| 2026-10-21 21:06 | ARB-USDT-SWAP | 0.18787 | 0.19123/0.18754 | 0.18787 | res 0.19849 (ha 8 candles) | 0.00343 | 0.0054% | — | sem_zona |
| 2026-10-21 21:06 | WLD-USDT-SWAP | 0.58340 | 0.58440/0.57810 | 0.58340 | — | 0.00901 | 0.0024% | B/venda@0.58590 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-21 21:06 | SUI-USDT-SWAP | 1.0285 | 1.0346/1.0259 | 1.0285 | res 1.0560 (ha 5 candles) | 0.01126 | 0.0004% | — | sem_zona |
| 2026-10-21 21:06 | UNI-USDT-SWAP | 7.4480 | 7.5100/7.4180 | 7.4480 | res 7.7300 (ha 5 candles) | 0.11571 | -0.0035% | — | sem_zona |
| 2026-10-21 21:06 | LINK-USDT-SWAP | 12.50 | 12.58/12.48 | 12.50 | res 12.80 (ha 5 candles) | 0.12300 | -0.0016% | — | sem_zona |
| 2026-10-21 22:06 | BTC-USDT-SWAP | 84151.5 | 84307.6/84038.8 | 84049.9 | res 84876.0 (ha 8 candles) | 441.53 | -0.0058% | — | sem_zona |
| 2026-10-21 22:06 | ETH-USDT-SWAP | 2472.7 | 2481.4/2472.1 | 2473.0 | res 2527.6 (ha 8 candles) | 19.35 | 0.0047% | B/compra@2473.0 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-21 22:06 | SOL-USDT-SWAP | 107.16 | 107.44/106.91 | 106.91 | res 109.17 (ha 6 candles) | 0.91143 | 0.0030% | — | sem_zona |
| 2026-10-21 22:06 | XRP-USDT-SWAP | 1.3627 | 1.3692/1.3626 | 1.3649 | res 1.3985 (ha 6 candles) | 0.01211 | 0.0100% | — | sem_zona |
| 2026-10-21 22:06 | DOGE-USDT-SWAP | 0.08184 | 0.08215/0.08184 | 0.08193 | — | 0.00061 | 0.0100% | — | sem_zona |
| 2026-10-21 22:06 | ARB-USDT-SWAP | 0.19045 | 0.19065/0.18733 | 0.18787 | res 0.19849 (ha 9 candles) | 0.00340 | -0.0031% | — | sem_zona |
| 2026-10-21 22:06 | WLD-USDT-SWAP | 0.58370 | 0.58920/0.58040 | 0.58340 | — | 0.00893 | -0.0058% | B/venda@0.58590 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-21 22:06 | SUI-USDT-SWAP | 1.0315 | 1.0350/1.0274 | 1.0285 | res 1.0560 (ha 6 candles) | 0.01114 | -0.0022% | — | sem_zona |
| 2026-10-21 22:06 | UNI-USDT-SWAP | 7.5260 | 7.5530/7.4480 | 7.4480 | res 7.7300 (ha 6 candles) | 0.11407 | -0.0067% | — | sem_zona |
| 2026-10-21 22:06 | LINK-USDT-SWAP | 12.56 | 12.59/12.48 | 12.50 | res 12.80 (ha 6 candles) | 0.12507 | -0.0010% | — | sem_zona |
| 2026-10-21 23:06 | BTC-USDT-SWAP | 83370.5 | 84320.0/83363.9 | 84049.9 | res 84876.0 (ha 9 candles) | 493.34 | -0.0050% | — | sem_zona |
| 2026-10-21 23:06 | ETH-USDT-SWAP | 2450.8 | 2478.5/2447.0 | 2473.0 | res 2527.6 (ha 9 candles) | 20.39 | 0.0058% | — | invalidado_setup_B |
| 2026-10-21 23:06 | SOL-USDT-SWAP | 106.12 | 107.39/105.83 | 106.91 | res 109.17 (ha 7 candles) | 0.98929 | 0.0019% | B/compra@105.61 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-21 23:06 | XRP-USDT-SWAP | 1.3508 | 1.3660/1.3467 | 1.3649 | res 1.3985 (ha 7 candles) | 0.01303 | 0.0098% | — | sem_zona |
| 2026-10-21 23:06 | DOGE-USDT-SWAP | 0.08112 | 0.08213/0.08084 | 0.08193 | — | 0.00069 | 0.0100% | B/compra@0.08092 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-21 23:06 | ARB-USDT-SWAP | 0.18861 | 0.19340/0.18821 | 0.18787 | res 0.19849 (ha 10 candles) | 0.00357 | -0.0074% | — | sem_zona |
| 2026-10-21 23:06 | WLD-USDT-SWAP | 0.57310 | 0.58840/0.56920 | 0.58340 | — | 0.00934 | -0.0081% | — | descartado_rr_baixo_setup_B |
| 2026-10-21 23:06 | SUI-USDT-SWAP | 1.0161 | 1.0362/1.0124 | 1.0285 | res 1.0560 (ha 7 candles) | 0.01236 | -0.0046% | — | sem_zona |
| 2026-10-21 23:06 | UNI-USDT-SWAP | 7.4100 | 7.5930/7.4010 | 7.4480 | res 7.7300 (ha 7 candles) | 0.12279 | -0.0089% | — | sem_zona |
| 2026-10-21 23:06 | LINK-USDT-SWAP | 12.42 | 12.61/12.38 | 12.50 | res 12.80 (ha 7 candles) | 0.13536 | 0.0013% | — | sem_zona |
| 2026-10-22 00:06 | BTC-USDT-SWAP | 82896.0 | 83447.8/82757.1 | 84049.9 | res 84876.0 (ha 10 candles) | 528.25 | -0.0006% | B/compra@82907.7 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 00:06 | ETH-USDT-SWAP | 2441.2 | 2453.0/2436.0 | 2473.0 | res 2527.6 (ha 10 candles) | 21.06 | 0.0070% | — | sem_zona |
| 2026-10-22 00:06 | SOL-USDT-SWAP | 105.47 | 106.21/105.19 | 106.91 | res 109.17 (ha 8 candles) | 1.0393 | 0.0008% | B/compra@105.61 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-22 00:06 | XRP-USDT-SWAP | 1.3456 | 1.3525/1.3425 | 1.3649 | res 1.3985 (ha 8 candles) | 0.01334 | 0.0077% | — | sem_zona |
| 2026-10-22 00:06 | DOGE-USDT-SWAP | 0.08039 | 0.08117/0.08003 | 0.08193 | — | 0.00075 | 0.0100% | — | invalidado_setup_B |
| 2026-10-22 00:06 | ARB-USDT-SWAP | 0.18550 | 0.18893/0.18409 | 0.18787 | res 0.19849 (ha 11 candles) | 0.00376 | -0.0128% | — | sem_zona |
| 2026-10-22 00:06 | WLD-USDT-SWAP | 0.57300 | 0.57630/0.56650 | 0.58340 | — | 0.00950 | -0.0017% | B/venda@0.57610 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 00:06 | SUI-USDT-SWAP | 1.0078 | 1.0171/1.0033 | 1.0285 | res 1.0560 (ha 8 candles) | 0.01292 | -0.0059% | B/compra@1.0002 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 00:06 | UNI-USDT-SWAP | 7.2850 | 7.4220/7.2530 | 7.4480 | res 7.7300 (ha 8 candles) | 0.13100 | -0.0078% | B/compra@7.2270 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 00:06 | LINK-USDT-SWAP | 12.32 | 12.45/12.29 | 12.50 | res 12.80 (ha 8 candles) | 0.14343 | 0.0020% | B/compra@12.25 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 01:06 | BTC-USDT-SWAP | 82900.1 | 83001.7/82650.0 | 82900.1 | res 84876.0 (ha 11 candles) | 502.34 | 0.0046% | — | descartado_rr_baixo_setup_B |
| 2026-10-22 01:06 | ETH-USDT-SWAP | 2443.8 | 2444.8/2433.0 | 2443.8 | res 2527.6 (ha 11 candles) | 18.96 | 0.0079% | — | sem_zona |
| 2026-10-22 01:06 | SOL-USDT-SWAP | 105.47 | 105.74/104.93 | 105.47 | res 109.17 (ha 9 candles) | 0.98714 | 0.0008% | B/compra@105.61 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-22 01:06 | XRP-USDT-SWAP | 1.3448 | 1.3478/1.3362 | 1.3448 | res 1.3985 (ha 9 candles) | 0.01314 | 0.0054% | — | sem_zona |
| 2026-10-22 01:06 | DOGE-USDT-SWAP | 0.08033 | 0.08054/0.07992 | 0.08033 | — | 0.00073 | 0.0100% | B/venda@0.08009 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 01:06 | ARB-USDT-SWAP | 0.18582 | 0.18612/0.18435 | 0.18582 | — | 0.00362 | -0.0154% | — | sem_zona |
| 2026-10-22 01:06 | WLD-USDT-SWAP | 0.57150 | 0.57650/0.56660 | 0.57150 | res 0.58920 (ha 3 candles) | 0.00860 | 0.0033% | B/venda@0.57610 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-22 01:06 | SUI-USDT-SWAP | 1.0053 | 1.0112/0.99800 | 1.0053 | res 1.0560 (ha 9 candles) | 0.01262 | -0.0070% | B/compra@1.0002 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-22 01:06 | UNI-USDT-SWAP | 7.2390 | 7.3150/7.1770 | 7.2390 | res 7.7300 (ha 9 candles) | 0.12564 | -0.0030% | B/compra@7.2270 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-22 01:06 | LINK-USDT-SWAP | 12.26 | 12.35/12.18 | 12.26 | res 12.80 (ha 9 candles) | 0.14143 | 0.0054% | B/compra@12.25 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-22 02:06 | BTC-USDT-SWAP | 82889.8 | 82955.0/82667.9 | 82900.1 | res 84876.0 (ha 12 candles) | 439.70 | 0.0078% | B/compra@82752.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 02:06 | ETH-USDT-SWAP | 2446.4 | 2446.5/2438.2 | 2443.8 | res 2527.6 (ha 12 candles) | 16.68 | 0.0084% | — | sem_zona |
| 2026-10-22 02:06 | SOL-USDT-SWAP | 105.56 | 105.65/105.16 | 105.47 | res 109.17 (ha 10 candles) | 0.89357 | 0.0010% | — | descartado_rr_baixo_setup_B |
| 2026-10-22 02:06 | XRP-USDT-SWAP | 1.3480 | 1.3480/1.3422 | 1.3448 | res 1.3985 (ha 10 candles) | 0.01115 | 0.0039% | — | sem_zona |
| 2026-10-22 02:06 | DOGE-USDT-SWAP | 0.08020 | 0.08049/0.07994 | 0.08033 | — | 0.00066 | 0.0083% | B/venda@0.08009 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-22 02:06 | ARB-USDT-SWAP | 0.18424 | 0.18652/0.18354 | 0.18582 | — | 0.00353 | -0.0182% | — | sem_zona |
| 2026-10-22 02:06 | WLD-USDT-SWAP | 0.55770 | 0.57480/0.55250 | 0.57150 | res 0.58920 (ha 4 candles) | 0.00919 | 0.0100% | — | invalidado_tendencia_virou_setup_B |
| 2026-10-22 02:06 | SUI-USDT-SWAP | 1.0054 | 1.0080/1.0004 | 1.0053 | res 1.0560 (ha 10 candles) | 0.01144 | -0.0067% | — | descartado_rr_baixo_setup_B |
| 2026-10-22 02:06 | UNI-USDT-SWAP | 7.2270 | 7.2630/7.1920 | 7.2390 | res 7.7300 (ha 10 candles) | 0.11836 | -0.0010% | B/compra@7.2270 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-22 02:06 | LINK-USDT-SWAP | 12.26 | 12.29/12.20 | 12.26 | res 12.80 (ha 10 candles) | 0.12986 | 0.0073% | B/compra@12.25 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-22 03:06 | BTC-USDT-SWAP | 82788.0 | 82967.1/82621.4 | 82900.1 | res 84876.0 (ha 13 candles) | 431.49 | 0.0100% | B/compra@82752.0 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-22 03:06 | ETH-USDT-SWAP | 2437.8 | 2447.3/2430.0 | 2443.8 | res 2527.6 (ha 13 candles) | 16.52 | 0.0087% | — | sem_zona |
| 2026-10-22 03:06 | SOL-USDT-SWAP | 105.01 | 105.65/104.66 | 105.47 | res 109.17 (ha 11 candles) | 0.86571 | 0.0019% | — | sem_zona |
| 2026-10-22 03:06 | XRP-USDT-SWAP | 1.3438 | 1.3511/1.3393 | 1.3448 | res 1.3985 (ha 11 candles) | 0.01100 | 0.0031% | — | sem_zona |
| 2026-10-22 03:06 | DOGE-USDT-SWAP | 0.07986 | 0.08031/0.07954 | 0.08033 | — | 0.00066 | 0.0067% | B/venda@0.08009 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-22 03:06 | ARB-USDT-SWAP | 0.18134 | 0.18458/0.18083 | 0.18582 | — | 0.00346 | -0.0192% | B/compra@0.17900 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 03:06 | WLD-USDT-SWAP | 0.54520 | 0.55880/0.54400 | 0.57150 | res 0.58920 (ha 5 candles) | 0.00959 | 0.0100% | B/compra@0.54010 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 03:06 | SUI-USDT-SWAP | 0.99870 | 1.0076/0.99440 | 1.0053 | res 1.0560 (ha 11 candles) | 0.01156 | -0.0045% | B/compra@0.99300 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 03:06 | UNI-USDT-SWAP | 7.1290 | 7.2420/7.1100 | 7.2390 | res 7.7300 (ha 11 candles) | 0.11850 | -0.0008% | — | invalidado_setup_B |
| 2026-10-22 03:06 | LINK-USDT-SWAP | 12.20 | 12.28/12.15 | 12.26 | res 12.80 (ha 11 candles) | 0.12657 | 0.0065% | — | invalidado_setup_B |
| 2026-10-22 04:06 | BTC-USDT-SWAP | 82465.5 | 82856.3/82432.1 | 82900.1 | res 84876.0 (ha 14 candles) | 431.35 | 0.0100% | — | invalidado_setup_B |
| 2026-10-22 04:06 | ETH-USDT-SWAP | 2432.5 | 2441.8/2427.3 | 2443.8 | res 2527.6 (ha 14 candles) | 15.77 | 0.0090% | — | sem_zona |
| 2026-10-22 04:06 | SOL-USDT-SWAP | 104.56 | 105.16/104.39 | 105.47 | res 109.17 (ha 12 candles) | 0.86929 | 0.0033% | — | sem_zona |
| 2026-10-22 04:06 | XRP-USDT-SWAP | 1.3414 | 1.3491/1.3382 | 1.3448 | res 1.3985 (ha 12 candles) | 0.01109 | 0.0038% | — | sem_zona |
| 2026-10-22 04:06 | DOGE-USDT-SWAP | 0.07973 | 0.07999/0.07955 | 0.08033 | — | 0.00065 | 0.0062% | — | zona_expirada_setup_B |
| 2026-10-22 04:06 | ARB-USDT-SWAP | 0.18161 | 0.18198/0.18044 | 0.18582 | — | 0.00337 | -0.0176% | B/compra@0.17900 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-22 04:06 | WLD-USDT-SWAP | 0.54380 | 0.54900/0.54110 | 0.57150 | res 0.58920 (ha 6 candles) | 0.00967 | 0.0100% | B/compra@0.54010 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-22 04:06 | SUI-USDT-SWAP | 0.99670 | 1.0012/0.99400 | 1.0053 | res 1.0560 (ha 12 candles) | 0.01141 | -0.0022% | B/compra@0.99300 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-22 04:06 | UNI-USDT-SWAP | 7.1220 | 7.1420/7.0720 | 7.2390 | res 7.7300 (ha 12 candles) | 0.11750 | 0.0003% | B/compra@7.0920 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 04:06 | LINK-USDT-SWAP | 12.18 | 12.23/12.15 | 12.26 | res 12.80 (ha 12 candles) | 0.12264 | 0.0044% | B/compra@12.15 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 05:06 | BTC-USDT-SWAP | 82202.0 | 82499.7/82088.0 | 82202.0 | res 84876.0 (ha 15 candles) | 437.61 | 0.0100% | — | sem_zona |
| 2026-10-22 05:06 | ETH-USDT-SWAP | 2428.6 | 2434.5/2425.0 | 2428.6 | res 2527.6 (ha 15 candles) | 15.28 | 0.0067% | — | sem_zona |
| 2026-10-22 05:06 | SOL-USDT-SWAP | 104.37 | 104.63/104.15 | 104.37 | res 109.17 (ha 13 candles) | 0.84357 | 0.0026% | — | sem_zona |
| 2026-10-22 05:06 | XRP-USDT-SWAP | 1.3392 | 1.3423/1.3361 | 1.3392 | res 1.3985 (ha 13 candles) | 0.01065 | 0.0038% | — | sem_zona |
| 2026-10-22 05:06 | DOGE-USDT-SWAP | 0.07959 | 0.07979/0.07941 | 0.07959 | res 0.08379 (ha 13 candles) | 0.00065 | 0.0051% | B/compra@0.07929 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 05:06 | ARB-USDT-SWAP | 0.18070 | 0.18187/0.18002 | 0.18070 | — | 0.00326 | -0.0171% | B/compra@0.17900 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-22 05:06 | WLD-USDT-SWAP | 0.54010 | 0.54430/0.53780 | 0.54010 | res 0.58920 (ha 7 candles) | 0.00981 | 0.0100% | B/compra@0.54010 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-22 05:06 | SUI-USDT-SWAP | 0.99230 | 0.99780/0.99030 | 0.99230 | res 1.0560 (ha 13 candles) | 0.01131 | -0.0011% | B/compra@0.99300 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-22 05:06 | UNI-USDT-SWAP | 7.1220 | 7.1290/7.0620 | 7.1220 | — | 0.11343 | -0.0012% | — | descartado_rr_baixo_setup_B |
| 2026-10-22 05:06 | LINK-USDT-SWAP | 12.19 | 12.20/12.13 | 12.19 | res 12.80 (ha 13 candles) | 0.11779 | 0.0025% | — | descartado_rr_baixo_setup_B |
| 2026-10-22 06:06 | BTC-USDT-SWAP | 81816.3 | 82242.7/81805.1 | 82202.0 | res 84876.0 (ha 16 candles) | 434.68 | 0.0099% | — | sem_zona |
| 2026-10-22 06:06 | ETH-USDT-SWAP | 2407.5 | 2429.3/2402.3 | 2428.6 | res 2527.6 (ha 16 candles) | 15.37 | 0.0049% | B/compra@2407.5 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 06:06 | SOL-USDT-SWAP | 103.77 | 104.38/103.54 | 104.37 | res 109.17 (ha 14 candles) | 0.81857 | 0.0035% | B/compra@103.48 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 06:06 | XRP-USDT-SWAP | 1.3270 | 1.3394/1.3245 | 1.3392 | res 1.3985 (ha 14 candles) | 0.01076 | 0.0034% | — | sem_zona |
| 2026-10-22 06:06 | DOGE-USDT-SWAP | 0.07898 | 0.07958/0.07880 | 0.07959 | res 0.08379 (ha 14 candles) | 0.00063 | 0.0055% | — | invalidado_setup_B |
| 2026-10-22 06:06 | ARB-USDT-SWAP | 0.17923 | 0.18098/0.17832 | 0.18070 | — | 0.00318 | -0.0158% | B/compra@0.17900 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-22 06:06 | WLD-USDT-SWAP | 0.54140 | 0.54290/0.53550 | 0.54010 | res 0.58920 (ha 8 candles) | 0.00970 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-10-22 06:06 | SUI-USDT-SWAP | 0.98220 | 0.99220/0.98080 | 0.99230 | res 1.0560 (ha 14 candles) | 0.01103 | -0.0028% | — | invalidado_setup_B |
| 2026-10-22 06:06 | UNI-USDT-SWAP | 7.0450 | 7.1290/7.0430 | 7.1220 | — | 0.10979 | -0.0009% | B/compra@6.9810 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 06:06 | LINK-USDT-SWAP | 12.03 | 12.19/12.00 | 12.19 | res 12.80 (ha 14 candles) | 0.12143 | 0.0014% | B/compra@12.06 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 07:06 | BTC-USDT-SWAP | 81918.4 | 81925.3/81588.9 | 82202.0 | res 84876.0 (ha 17 candles) | 428.37 | 0.0075% | — | sem_zona |
| 2026-10-22 07:06 | ETH-USDT-SWAP | 2407.0 | 2408.0/2393.3 | 2428.6 | res 2527.6 (ha 17 candles) | 15.23 | 0.0024% | B/compra@2407.5 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-22 07:06 | SOL-USDT-SWAP | 104.28 | 104.28/103.43 | 104.37 | res 109.17 (ha 15 candles) | 0.80214 | 0.0026% | — | descartado_rr_baixo_setup_B |
| 2026-10-22 07:06 | XRP-USDT-SWAP | 1.3290 | 1.3297/1.3241 | 1.3392 | res 1.3985 (ha 15 candles) | 0.01004 | 0.0042% | — | sem_zona |
| 2026-10-22 07:06 | DOGE-USDT-SWAP | 0.07920 | 0.07921/0.07866 | 0.07959 | res 0.08379 (ha 15 candles) | 0.00063 | 0.0020% | — | sem_zona |
| 2026-10-22 07:06 | ARB-USDT-SWAP | 0.17953 | 0.17986/0.17801 | 0.18070 | — | 0.00299 | -0.0169% | — | descartado_rr_baixo_setup_B |
| 2026-10-22 07:06 | WLD-USDT-SWAP | 0.54970 | 0.55110/0.53770 | 0.54010 | res 0.58920 (ha 9 candles) | 0.01018 | 0.0100% | — | sem_zona |
| 2026-10-22 07:06 | SUI-USDT-SWAP | 0.98590 | 0.98590/0.97720 | 0.99230 | res 1.0560 (ha 15 candles) | 0.01094 | -0.0039% | — | sem_zona |
| 2026-10-22 07:06 | UNI-USDT-SWAP | 7.0740 | 7.0770/6.9880 | 7.1220 | — | 0.10721 | 0.0017% | — | descartado_rr_baixo_setup_B |
| 2026-10-22 07:06 | LINK-USDT-SWAP | 12.04 | 12.05/11.98 | 12.19 | res 12.80 (ha 15 candles) | 0.11943 | -0.0017% | — | descartado_rr_baixo_setup_B |
| 2026-10-22 08:06 | BTC-USDT-SWAP | 82004.2 | 82154.3/81891.6 | 82202.0 | res 84876.0 (ha 18 candles) | 417.12 | 0.0060% | — | sem_zona |
| 2026-10-22 08:06 | ETH-USDT-SWAP | 2405.0 | 2412.6/2402.3 | 2428.6 | res 2527.6 (ha 18 candles) | 15.34 | 0.0010% | B/compra@2407.5 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-22 08:06 | SOL-USDT-SWAP | 104.50 | 104.74/104.21 | 104.37 | res 109.17 (ha 16 candles) | 0.79929 | 0.0007% | — | sem_zona |
| 2026-10-22 08:06 | XRP-USDT-SWAP | 1.3290 | 1.3338/1.3277 | 1.3392 | res 1.3985 (ha 16 candles) | 0.00983 | 0.0041% | — | sem_zona |
| 2026-10-22 08:06 | DOGE-USDT-SWAP | 0.07918 | 0.07943/0.07906 | 0.07959 | res 0.08379 (ha 16 candles) | 0.00063 | -0.0012% | — | sem_zona |
| 2026-10-22 08:06 | ARB-USDT-SWAP | 0.18219 | 0.18245/0.17940 | 0.18070 | — | 0.00300 | -0.0221% | — | sem_zona |
| 2026-10-22 08:06 | WLD-USDT-SWAP | 0.55220 | 0.55290/0.54620 | 0.54010 | res 0.58920 (ha 10 candles) | 0.01017 | 0.0100% | — | sem_zona |
| 2026-10-22 08:06 | SUI-USDT-SWAP | 0.98610 | 0.99040/0.98410 | 0.99230 | res 1.0560 (ha 16 candles) | 0.01071 | -0.0049% | — | sem_zona |
| 2026-10-22 08:06 | UNI-USDT-SWAP | 7.1050 | 7.1140/7.0700 | 7.1220 | — | 0.10436 | 0.0017% | B/compra@7.0920 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 08:06 | LINK-USDT-SWAP | 12.05 | 12.09/12.04 | 12.19 | res 12.80 (ha 16 candles) | 0.11636 | -0.0036% | — | sem_zona |
| 2026-10-22 09:06 | BTC-USDT-SWAP | 81712.1 | 82004.2/81708.2 | 81712.1 | res 84876.0 (ha 19 candles) | 423.05 | 0.0050% | — | sem_zona |
| 2026-10-22 09:06 | ETH-USDT-SWAP | 2399.2 | 2405.8/2397.6 | 2399.2 | res 2527.6 (ha 19 candles) | 15.13 | 0.0005% | — | invalidado_setup_B |
| 2026-10-22 09:06 | SOL-USDT-SWAP | 104.40 | 104.70/104.37 | 104.40 | res 109.17 (ha 17 candles) | 0.78214 | 0.0009% | — | sem_zona |
| 2026-10-22 09:06 | XRP-USDT-SWAP | 1.3255 | 1.3306/1.3249 | 1.3255 | res 1.3985 (ha 17 candles) | 0.00980 | 0.0047% | — | sem_zona |
| 2026-10-22 09:06 | DOGE-USDT-SWAP | 0.07927 | 0.07938/0.07914 | 0.07927 | res 0.08379 (ha 17 candles) | 0.00062 | -0.0038% | — | sem_zona |
| 2026-10-22 09:06 | ARB-USDT-SWAP | 0.18377 | 0.18521/0.18201 | 0.18377 | — | 0.00305 | -0.0251% | — | sem_zona |
| 2026-10-22 09:06 | WLD-USDT-SWAP | 0.54590 | 0.55250/0.54540 | 0.54590 | res 0.58920 (ha 11 candles) | 0.01044 | 0.0100% | — | sem_zona |
| 2026-10-22 09:06 | SUI-USDT-SWAP | 0.98620 | 0.99100/0.98470 | 0.98620 | res 1.0560 (ha 17 candles) | 0.01062 | -0.0066% | — | sem_zona |
| 2026-10-22 09:06 | UNI-USDT-SWAP | 7.0790 | 7.1230/7.0720 | 7.0790 | — | 0.10207 | 0.0027% | B/compra@7.0920 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-22 09:06 | LINK-USDT-SWAP | 12.04 | 12.10/12.02 | 12.04 | res 12.80 (ha 17 candles) | 0.11686 | -0.0039% | — | sem_zona |
| 2026-10-22 10:06 | BTC-USDT-SWAP | 81665.0 | 81880.0/81588.0 | 81712.1 | res 84876.0 (ha 20 candles) | 415.06 | 0.0057% | — | sem_zona |
| 2026-10-22 10:06 | ETH-USDT-SWAP | 2399.8 | 2405.9/2397.4 | 2399.2 | res 2527.6 (ha 20 candles) | 14.59 | 0.0013% | B/compra@2391.7 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 10:06 | SOL-USDT-SWAP | 104.37 | 104.55/104.12 | 104.40 | res 109.17 (ha 18 candles) | 0.74714 | 0.0026% | — | sem_zona |
| 2026-10-22 10:06 | XRP-USDT-SWAP | 1.3242 | 1.3285/1.3210 | 1.3255 | res 1.3985 (ha 18 candles) | 0.00946 | 0.0048% | B/compra@1.3176 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 10:06 | DOGE-USDT-SWAP | 0.07936 | 0.07952/0.07911 | 0.07927 | res 0.08379 (ha 18 candles) | 0.00060 | -0.0036% | — | sem_zona |
| 2026-10-22 10:06 | ARB-USDT-SWAP | 0.18448 | 0.18573/0.18237 | 0.18377 | — | 0.00307 | -0.0218% | B/compra@0.18612 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 10:06 | WLD-USDT-SWAP | 0.53880 | 0.54770/0.53640 | 0.54590 | res 0.58920 (ha 12 candles) | 0.01081 | 0.0055% | — | sem_zona |
| 2026-10-22 10:06 | SUI-USDT-SWAP | 0.98280 | 0.98800/0.98120 | 0.98620 | res 1.0560 (ha 18 candles) | 0.01016 | -0.0063% | B/compra@0.97530 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 10:06 | UNI-USDT-SWAP | 7.0730 | 7.1160/7.0610 | 7.0790 | — | 0.09721 | 0.0065% | B/compra@7.0920 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-22 10:06 | LINK-USDT-SWAP | 12.03 | 12.07/12.00 | 12.04 | res 12.80 (ha 18 candles) | 0.11286 | -0.0028% | — | sem_zona |
| 2026-10-22 11:06 | BTC-USDT-SWAP | 81677.5 | 82061.9/81335.8 | 81712.1 | res 84876.0 (ha 21 candles) | 434.77 | 0.0072% | — | sem_zona |
| 2026-10-22 11:06 | ETH-USDT-SWAP | 2409.5 | 2417.3/2392.0 | 2399.2 | res 2527.6 (ha 21 candles) | 15.22 | 0.0027% | — | descartado_rr_baixo_setup_B |
| 2026-10-22 11:06 | SOL-USDT-SWAP | 105.02 | 105.24/104.08 | 104.40 | res 109.17 (ha 19 candles) | 0.77071 | 0.0039% | — | sem_zona |
| 2026-10-22 11:06 | XRP-USDT-SWAP | 1.3271 | 1.3329/1.3184 | 1.3255 | res 1.3985 (ha 19 candles) | 0.00975 | 0.0039% | B/compra@1.3176 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-22 11:06 | DOGE-USDT-SWAP | 0.07974 | 0.07986/0.07914 | 0.07927 | res 0.08379 (ha 19 candles) | 0.00061 | -0.0042% | B/compra@0.07996 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 11:06 | ARB-USDT-SWAP | 0.18520 | 0.18617/0.18345 | 0.18377 | — | 0.00301 | -0.0161% | — | invalidado_setup_B |
| 2026-10-22 11:06 | WLD-USDT-SWAP | 0.54760 | 0.54990/0.53680 | 0.54590 | res 0.55290 (ha 3 candles) | 0.01130 | 0.0015% | — | sem_zona |
| 2026-10-22 11:06 | SUI-USDT-SWAP | 0.98640 | 0.98990/0.97780 | 0.98620 | res 1.0560 (ha 19 candles) | 0.01040 | -0.0065% | — | descartado_rr_baixo_setup_B |
| 2026-10-22 11:06 | UNI-USDT-SWAP | 7.1520 | 7.1760/7.0630 | 7.0790 | — | 0.09871 | 0.0045% | — | descartado_rr_baixo_setup_B |
| 2026-10-22 11:06 | LINK-USDT-SWAP | 12.07 | 12.11/11.99 | 12.04 | res 12.80 (ha 19 candles) | 0.11371 | -0.0023% | B/compra@12.15 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 12:06 | BTC-USDT-SWAP | 81840.1 | 81907.3/81545.9 | 81712.1 | res 84876.0 (ha 22 candles) | 441.39 | 0.0079% | — | sem_zona |
| 2026-10-22 12:06 | ETH-USDT-SWAP | 2412.0 | 2416.9/2398.9 | 2399.2 | res 2527.6 (ha 22 candles) | 15.84 | 0.0038% | B/compra@2407.5 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 12:06 | SOL-USDT-SWAP | 104.64 | 105.23/104.21 | 104.40 | res 109.17 (ha 20 candles) | 0.80571 | 0.0030% | — | sem_zona |
| 2026-10-22 12:06 | XRP-USDT-SWAP | 1.3236 | 1.3284/1.3200 | 1.3255 | res 1.3985 (ha 20 candles) | 0.00988 | 0.0037% | B/compra@1.3176 (1t/1c) | zona_mapeada_setup_B |
| 2026-10-22 12:06 | DOGE-USDT-SWAP | 0.07938 | 0.07984/0.07919 | 0.07927 | res 0.08379 (ha 20 candles) | 0.00064 | -0.0035% | — | invalidado_setup_B |
| 2026-10-22 12:06 | ARB-USDT-SWAP | 0.18393 | 0.18588/0.18314 | 0.18377 | — | 0.00296 | -0.0125% | — | sem_zona |
| 2026-10-22 12:06 | WLD-USDT-SWAP | 0.54690 | 0.55060/0.54280 | 0.54590 | res 0.55290 (ha 4 candles) | 0.01123 | -0.0025% | — | sem_zona |
| 2026-10-22 12:06 | SUI-USDT-SWAP | 0.98220 | 0.98920/0.97870 | 0.98620 | res 1.0560 (ha 20 candles) | 0.01061 | -0.0078% | — | sem_zona |
| 2026-10-22 12:06 | UNI-USDT-SWAP | 7.1330 | 7.1880/7.0830 | 7.0790 | — | 0.09871 | 0.0009% | — | sem_zona |
| 2026-10-22 12:06 | LINK-USDT-SWAP | 12.04 | 12.09/12.00 | 12.04 | res 12.80 (ha 20 candles) | 0.11293 | -0.0016% | B/compra@12.15 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-22 13:06 | BTC-USDT-SWAP | 81649.9 | 81855.0/81257.4 | 81649.9 | res 84876.0 (ha 23 candles) | 415.78 | 0.0080% | — | sem_zona |
| 2026-10-22 13:06 | ETH-USDT-SWAP | 2397.6 | 2413.6/2384.0 | 2397.6 | res 2527.6 (ha 23 candles) | 15.71 | 0.0044% | — | invalidado_setup_B |
| 2026-10-22 13:06 | SOL-USDT-SWAP | 104.57 | 104.74/103.88 | 104.57 | res 109.17 (ha 21 candles) | 0.75571 | 0.0037% | — | sem_zona |
| 2026-10-22 13:06 | XRP-USDT-SWAP | 1.3216 | 1.3254/1.3139 | 1.3216 | res 1.3985 (ha 21 candles) | 0.00932 | 0.0042% | B/compra@1.3176 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-22 13:06 | DOGE-USDT-SWAP | 0.07917 | 0.07947/0.07852 | 0.07917 | res 0.08379 (ha 21 candles) | 0.00061 | -0.0021% | B/compra@0.07929 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 13:06 | ARB-USDT-SWAP | 0.18363 | 0.18451/0.18158 | 0.18363 | — | 0.00280 | -0.0078% | — | sem_zona |
| 2026-10-22 13:06 | WLD-USDT-SWAP | 0.53210 | 0.54820/0.52510 | 0.53210 | res 0.55290 (ha 5 candles) | 0.01151 | 0.0004% | — | sem_zona |
| 2026-10-22 13:06 | SUI-USDT-SWAP | 0.97910 | 0.98410/0.96920 | 0.97910 | res 1.0560 (ha 21 candles) | 0.00997 | -0.0082% | — | sem_zona |
| 2026-10-22 13:06 | UNI-USDT-SWAP | 7.0670 | 7.1490/7.0190 | 7.0670 | — | 0.09429 | -0.0020% | — | sem_zona |
| 2026-10-22 13:06 | LINK-USDT-SWAP | 11.98 | 12.05/11.91 | 11.98 | res 12.80 (ha 21 candles) | 0.10693 | -0.0007% | B/compra@12.15 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-22 14:06 | BTC-USDT-SWAP | 81241.6 | 81728.5/80900.0 | 81649.9 | res 84876.0 (ha 24 candles) | 425.62 | 0.0086% | B/compra@81166.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 14:06 | ETH-USDT-SWAP | 2379.5 | 2401.8/2358.0 | 2397.6 | res 2417.3 (ha 3 candles) | 17.62 | 0.0039% | B/compra@2369.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 14:06 | SOL-USDT-SWAP | 103.76 | 104.89/102.93 | 104.57 | res 105.24 (ha 3 candles) | 0.82286 | 0.0040% | — | sem_zona |
| 2026-10-22 14:06 | XRP-USDT-SWAP | 1.3171 | 1.3257/1.3055 | 1.3216 | res 1.3985 (ha 22 candles) | 0.01005 | 0.0053% | — | zona_expirada_setup_B |
| 2026-10-22 14:06 | DOGE-USDT-SWAP | 0.07852 | 0.07939/0.07780 | 0.07917 | res 0.07986 (ha 3 candles) | 0.00065 | -0.0029% | — | invalidado_setup_B |
| 2026-10-22 14:06 | ARB-USDT-SWAP | 0.18139 | 0.18444/0.17911 | 0.18363 | — | 0.00284 | -0.0061% | — | sem_zona |
| 2026-10-22 14:06 | WLD-USDT-SWAP | 0.52810 | 0.53470/0.52230 | 0.53210 | res 0.55290 (ha 6 candles) | 0.01169 | 0.0035% | — | sem_zona |
| 2026-10-22 14:06 | SUI-USDT-SWAP | 0.97530 | 0.98290/0.96540 | 0.97910 | res 1.0560 (ha 22 candles) | 0.01024 | -0.0102% | — | sem_zona |
| 2026-10-22 14:06 | UNI-USDT-SWAP | 6.9590 | 7.0840/6.8830 | 7.0670 | — | 0.09657 | -0.0047% | B/compra@6.9810 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 14:06 | LINK-USDT-SWAP | 11.86 | 12.01/11.77 | 11.98 | res 12.11 (ha 3 candles) | 0.11243 | -0.0026% | B/compra@12.15 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-22 15:06 | BTC-USDT-SWAP | 81175.4 | 81423.2/81115.9 | 81649.9 | res 84876.0 (ha 25 candles) | 422.45 | 0.0086% | B/compra@81166.0 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-22 15:06 | ETH-USDT-SWAP | 2378.6 | 2387.4/2373.6 | 2397.6 | res 2417.3 (ha 4 candles) | 17.77 | 0.0022% | B/compra@2369.0 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-22 15:06 | SOL-USDT-SWAP | 103.56 | 104.00/103.22 | 104.57 | res 105.24 (ha 4 candles) | 0.82071 | 0.0028% | B/compra@103.48 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 15:06 | XRP-USDT-SWAP | 1.3088 | 1.3176/1.3078 | 1.3216 | res 1.3985 (ha 23 candles) | 0.00992 | 0.0053% | B/compra@1.3102 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 15:06 | DOGE-USDT-SWAP | 0.07827 | 0.07864/0.07821 | 0.07917 | res 0.07986 (ha 4 candles) | 0.00063 | -0.0012% | B/compra@0.07842 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 15:06 | ARB-USDT-SWAP | 0.18147 | 0.18294/0.18050 | 0.18363 | — | 0.00289 | -0.0062% | — | sem_zona |
| 2026-10-22 15:06 | WLD-USDT-SWAP | 0.52650 | 0.53040/0.52520 | 0.53210 | res 0.55290 (ha 7 candles) | 0.01136 | 0.0091% | — | sem_zona |
| 2026-10-22 15:06 | SUI-USDT-SWAP | 0.97500 | 0.97950/0.97210 | 0.97910 | res 1.0560 (ha 23 candles) | 0.00982 | -0.0132% | — | sem_zona |
| 2026-10-22 15:06 | UNI-USDT-SWAP | 6.9760 | 7.0130/6.9280 | 7.0670 | — | 0.09279 | -0.0073% | B/compra@6.9810 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-22 15:06 | LINK-USDT-SWAP | 11.89 | 11.94/11.84 | 11.98 | res 12.11 (ha 4 candles) | 0.10671 | -0.0037% | B/compra@12.15 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-22 16:06 | BTC-USDT-SWAP | 81350.0 | 81393.4/81013.6 | 81649.9 | res 84876.0 (ha 26 candles) | 429.07 | 0.0094% | — | descartado_rr_baixo_setup_B |
| 2026-10-22 16:06 | ETH-USDT-SWAP | 2383.6 | 2385.7/2373.6 | 2397.6 | res 2417.3 (ha 5 candles) | 18.04 | 0.0016% | B/compra@2369.0 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-22 16:06 | SOL-USDT-SWAP | 103.56 | 103.82/103.08 | 104.57 | res 105.24 (ha 5 candles) | 0.83857 | 0.0034% | — | descartado_rr_baixo_setup_B |
| 2026-10-22 16:06 | XRP-USDT-SWAP | 1.3076 | 1.3104/1.3020 | 1.3216 | res 1.3985 (ha 24 candles) | 0.01011 | 0.0068% | — | invalidado_setup_B |
| 2026-10-22 16:06 | DOGE-USDT-SWAP | 0.07852 | 0.07863/0.07806 | 0.07917 | res 0.07986 (ha 5 candles) | 0.00063 | 0.0010% | — | confirmado_calibracao_setup_B |
| 2026-10-22 16:06 | ARB-USDT-SWAP | 0.18036 | 0.18156/0.17936 | 0.18363 | — | 0.00283 | -0.0073% | B/compra@0.17900 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 16:06 | WLD-USDT-SWAP | 0.55820 | 0.56390/0.52560 | 0.53210 | res 0.55290 (ha 8 candles) | 0.01250 | 0.0100% | A/compra@0.55290 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-22 16:06 | SUI-USDT-SWAP | 0.97760 | 0.97840/0.97120 | 0.97910 | res 1.0560 (ha 24 candles) | 0.00979 | -0.0132% | — | sem_zona |
| 2026-10-22 16:06 | UNI-USDT-SWAP | 7.0200 | 7.0270/6.9540 | 7.0670 | — | 0.09293 | -0.0108% | — | confirmado_calibracao_setup_B |
| 2026-10-22 16:06 | LINK-USDT-SWAP | 11.94 | 11.94/11.85 | 11.98 | res 12.11 (ha 5 candles) | 0.10707 | -0.0033% | B/compra@12.15 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-22 17:06 | BTC-USDT-SWAP | 81467.3 | 81520.5/81245.9 | 81467.3 | res 84876.0 (ha 27 candles) | 423.99 | 0.0094% | — | sem_zona |
| 2026-10-22 17:06 | ETH-USDT-SWAP | 2385.8 | 2392.7/2377.5 | 2385.8 | res 2417.3 (ha 6 candles) | 17.90 | 0.0016% | B/compra@2369.0 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-22 17:06 | SOL-USDT-SWAP | 103.58 | 103.88/103.18 | 103.58 | res 105.24 (ha 6 candles) | 0.81786 | 0.0041% | — | sem_zona |
| 2026-10-22 17:06 | XRP-USDT-SWAP | 1.3048 | 1.3136/1.3032 | 1.3048 | res 1.3985 (ha 25 candles) | 0.01001 | 0.0090% | — | sem_zona |
| 2026-10-22 17:06 | DOGE-USDT-SWAP | 0.07866 | 0.07899/0.07836 | 0.07866 | res 0.07986 (ha 6 candles) | 0.00062 | 0.0027% | — | sem_zona |
| 2026-10-22 17:06 | ARB-USDT-SWAP | 0.18055 | 0.18142/0.17917 | 0.18055 | — | 0.00272 | -0.0110% | — | descartado_rr_baixo_setup_B |
| 2026-10-22 17:06 | WLD-USDT-SWAP | 0.55380 | 0.56650/0.55000 | 0.55380 | res 0.55290 (ha 9 candles) | 0.01262 | 0.0100% | A/compra@0.55290 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-22 17:06 | SUI-USDT-SWAP | 0.97560 | 0.98150/0.97280 | 0.97560 | res 1.0560 (ha 25 candles) | 0.00947 | -0.0112% | — | sem_zona |
| 2026-10-22 17:06 | UNI-USDT-SWAP | 7.0330 | 7.0650/6.9940 | 7.0330 | — | 0.08857 | -0.0123% | B/compra@7.0920 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 17:06 | LINK-USDT-SWAP | 11.95 | 12.01/11.92 | 11.95 | res 12.11 (ha 6 candles) | 0.10450 | -0.0031% | B/compra@12.15 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-22 18:06 | BTC-USDT-SWAP | 81239.6 | 81474.5/81160.0 | 81467.3 | res 84876.0 (ha 28 candles) | 416.16 | 0.0091% | B/compra@80961.3 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 18:06 | ETH-USDT-SWAP | 2381.9 | 2387.3/2376.5 | 2385.8 | res 2417.3 (ha 7 candles) | 17.63 | 0.0018% | B/compra@2369.0 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-22 18:06 | SOL-USDT-SWAP | 103.32 | 103.72/102.97 | 103.58 | res 105.24 (ha 7 candles) | 0.81643 | 0.0045% | — | sem_zona |
| 2026-10-22 18:06 | XRP-USDT-SWAP | 1.3003 | 1.3068/1.2943 | 1.3048 | res 1.3985 (ha 26 candles) | 0.01012 | 0.0085% | — | sem_zona |
| 2026-10-22 18:06 | DOGE-USDT-SWAP | 0.07833 | 0.07873/0.07812 | 0.07866 | res 0.07986 (ha 7 candles) | 0.00064 | 0.0045% | — | sem_zona |
| 2026-10-22 18:06 | ARB-USDT-SWAP | 0.17930 | 0.18072/0.17829 | 0.18055 | — | 0.00279 | -0.0120% | — | sem_zona |
| 2026-10-22 18:06 | WLD-USDT-SWAP | 0.54410 | 0.55660/0.54010 | 0.55380 | res 0.55290 (ha 10 candles) | 0.01324 | 0.0100% | — | invalidado_setup_A |
| 2026-10-22 18:06 | SUI-USDT-SWAP | 0.97170 | 0.97630/0.96770 | 0.97560 | res 1.0560 (ha 26 candles) | 0.00957 | -0.0080% | — | sem_zona |
| 2026-10-22 18:06 | UNI-USDT-SWAP | 6.9990 | 7.0450/6.9770 | 7.0330 | — | 0.08843 | -0.0104% | B/compra@7.0920 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-22 18:06 | LINK-USDT-SWAP | 11.90 | 11.98/11.86 | 11.95 | res 12.11 (ha 7 candles) | 0.10764 | -0.0045% | B/compra@12.15 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-22 19:06 | BTC-USDT-SWAP | 81442.5 | 81535.9/81214.4 | 81467.3 | res 84876.0 (ha 29 candles) | 409.71 | 0.0081% | B/compra@80961.3 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-22 19:06 | ETH-USDT-SWAP | 2392.5 | 2401.9/2380.0 | 2385.8 | res 2417.3 (ha 8 candles) | 18.52 | 0.0036% | B/compra@2369.0 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-22 19:06 | SOL-USDT-SWAP | 103.66 | 104.04/103.24 | 103.58 | res 105.24 (ha 8 candles) | 0.83929 | 0.0057% | — | sem_zona |
| 2026-10-22 19:06 | XRP-USDT-SWAP | 1.3079 | 1.3110/1.3000 | 1.3048 | res 1.3985 (ha 27 candles) | 0.01046 | 0.0092% | — | sem_zona |
| 2026-10-22 19:06 | DOGE-USDT-SWAP | 0.07882 | 0.07896/0.07831 | 0.07866 | res 0.07986 (ha 8 candles) | 0.00065 | 0.0040% | B/compra@0.07929 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 19:06 | ARB-USDT-SWAP | 0.18060 | 0.18257/0.17903 | 0.18055 | — | 0.00291 | -0.0133% | — | sem_zona |
| 2026-10-22 19:06 | WLD-USDT-SWAP | 0.54470 | 0.54970/0.54150 | 0.55380 | res 0.55290 (ha 11 candles) | 0.01336 | 0.0100% | B/compra@0.54010 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 19:06 | SUI-USDT-SWAP | 0.97660 | 0.97990/0.97120 | 0.97560 | res 1.0560 (ha 27 candles) | 0.00966 | -0.0054% | B/compra@0.97530 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 19:06 | UNI-USDT-SWAP | 7.0280 | 7.0760/6.9970 | 7.0330 | — | 0.08929 | -0.0060% | — | invalidado_setup_B |
| 2026-10-22 19:06 | LINK-USDT-SWAP | 11.95 | 12.00/11.90 | 11.95 | res 12.11 (ha 8 candles) | 0.10986 | -0.0037% | — | zona_expirada_setup_B |
| 2026-10-22 20:06 | BTC-USDT-SWAP | 81309.7 | 81511.8/81266.9 | 81467.3 | res 84876.0 (ha 30 candles) | 395.95 | 0.0069% | B/compra@80961.3 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-22 20:06 | ETH-USDT-SWAP | 2384.3 | 2396.7/2382.7 | 2385.8 | res 2417.3 (ha 9 candles) | 17.59 | 0.0051% | B/compra@2369.0 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-22 20:06 | SOL-USDT-SWAP | 103.32 | 103.86/103.22 | 103.58 | res 105.24 (ha 9 candles) | 0.82500 | 0.0076% | — | sem_zona |
| 2026-10-22 20:06 | XRP-USDT-SWAP | 1.3065 | 1.3105/1.3054 | 1.3048 | res 1.3985 (ha 28 candles) | 0.00976 | 0.0089% | — | sem_zona |
| 2026-10-22 20:06 | DOGE-USDT-SWAP | 0.07860 | 0.07895/0.07855 | 0.07866 | res 0.07986 (ha 9 candles) | 0.00063 | 0.0033% | B/compra@0.07929 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-22 20:06 | ARB-USDT-SWAP | 0.17882 | 0.18176/0.17843 | 0.18055 | — | 0.00296 | -0.0131% | B/compra@0.17662 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 20:06 | WLD-USDT-SWAP | 0.54100 | 0.54850/0.53710 | 0.55380 | res 0.56650 (ha 3 candles) | 0.01364 | 0.0093% | B/compra@0.54010 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-22 20:06 | SUI-USDT-SWAP | 0.97240 | 0.98010/0.97140 | 0.97560 | res 1.0560 (ha 28 candles) | 0.00946 | -0.0036% | — | invalidado_setup_B |
| 2026-10-22 20:06 | UNI-USDT-SWAP | 7.0030 | 7.0530/6.9970 | 7.0330 | — | 0.08714 | -0.0037% | B/compra@6.9810 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 20:06 | LINK-USDT-SWAP | 11.91 | 11.99/11.90 | 11.95 | res 12.01 (ha 3 candles) | 0.10279 | -0.0031% | — | sem_zona |
| 2026-10-22 21:06 | BTC-USDT-SWAP | 81380.9 | 81399.9/81219.4 | 81380.9 | res 84876.0 (ha 31 candles) | 384.81 | 0.0069% | B/compra@80961.3 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-22 21:06 | ETH-USDT-SWAP | 2388.3 | 2388.8/2380.2 | 2388.3 | res 2417.3 (ha 10 candles) | 17.16 | 0.0065% | B/compra@2369.0 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-22 21:06 | SOL-USDT-SWAP | 103.61 | 103.68/103.20 | 103.61 | res 105.24 (ha 10 candles) | 0.79857 | 0.0093% | — | sem_zona |
| 2026-10-22 21:06 | XRP-USDT-SWAP | 1.3087 | 1.3094/1.3051 | 1.3087 | res 1.3985 (ha 29 candles) | 0.00967 | 0.0091% | — | sem_zona |
| 2026-10-22 21:06 | DOGE-USDT-SWAP | 0.07878 | 0.07881/0.07850 | 0.07878 | res 0.07986 (ha 10 candles) | 0.00061 | 0.0022% | B/compra@0.07929 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-22 21:06 | ARB-USDT-SWAP | 0.17899 | 0.17912/0.17743 | 0.17899 | — | 0.00294 | -0.0122% | B/compra@0.17662 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-22 21:06 | WLD-USDT-SWAP | 0.54560 | 0.54580/0.53900 | 0.54560 | res 0.56650 (ha 4 candles) | 0.01317 | 0.0080% | — | descartado_rr_baixo_setup_B |
| 2026-10-22 21:06 | SUI-USDT-SWAP | 0.97170 | 0.97430/0.97060 | 0.97170 | res 1.0560 (ha 29 candles) | 0.00910 | -0.0009% | — | sem_zona |
| 2026-10-22 21:06 | UNI-USDT-SWAP | 7.0050 | 7.0090/6.9690 | 7.0050 | — | 0.08364 | -0.0012% | — | confirmado_calibracao_setup_B |
| 2026-10-22 21:06 | LINK-USDT-SWAP | 11.95 | 11.96/11.90 | 11.95 | res 12.01 (ha 4 candles) | 0.10186 | -0.0032% | — | sem_zona |
| 2026-10-22 22:06 | BTC-USDT-SWAP | 81427.6 | 81516.1/81088.0 | 81380.9 | res 81535.9 (ha 3 candles) | 396.63 | 0.0073% | B/compra@80961.3 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-22 22:06 | ETH-USDT-SWAP | 2394.2 | 2396.4/2382.5 | 2388.3 | res 2401.9 (ha 3 candles) | 17.42 | 0.0082% | — | zona_expirada_setup_B |
| 2026-10-22 22:06 | SOL-USDT-SWAP | 104.02 | 104.11/103.42 | 103.61 | res 105.24 (ha 11 candles) | 0.81000 | 0.0100% | — | sem_zona |
| 2026-10-22 22:06 | XRP-USDT-SWAP | 1.3121 | 1.3140/1.3058 | 1.3087 | res 1.3985 (ha 30 candles) | 0.00982 | 0.0094% | B/compra@1.3176 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 22:06 | DOGE-USDT-SWAP | 0.07903 | 0.07907/0.07867 | 0.07878 | res 0.07986 (ha 11 candles) | 0.00061 | 0.0032% | B/compra@0.07929 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-22 22:06 | ARB-USDT-SWAP | 0.18025 | 0.18107/0.17867 | 0.17899 | — | 0.00290 | -0.0128% | B/compra@0.17662 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-22 22:06 | WLD-USDT-SWAP | 0.54970 | 0.55240/0.54320 | 0.54560 | res 0.56650 (ha 5 candles) | 0.01335 | 0.0055% | — | sem_zona |
| 2026-10-22 22:06 | SUI-USDT-SWAP | 0.97680 | 0.97800/0.96950 | 0.97170 | res 1.0560 (ha 30 candles) | 0.00926 | 0.0022% | — | sem_zona |
| 2026-10-22 22:06 | UNI-USDT-SWAP | 7.0230 | 7.0350/6.9800 | 7.0050 | — | 0.08443 | 0.0010% | — | sem_zona |
| 2026-10-22 22:06 | LINK-USDT-SWAP | 12.00 | 12.00/11.93 | 11.95 | res 12.01 (ha 5 candles) | 0.10350 | -0.0020% | B/compra@12.06 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 23:06 | BTC-USDT-SWAP | 81311.4 | 81749.0/81166.6 | 81380.9 | res 81535.9 (ha 4 candles) | 417.09 | 0.0079% | B/compra@80961.3 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-22 23:06 | ETH-USDT-SWAP | 2391.5 | 2407.9/2380.2 | 2388.3 | res 2401.9 (ha 4 candles) | 18.81 | 0.0081% | B/compra@2391.7 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 23:06 | SOL-USDT-SWAP | 103.99 | 104.67/103.53 | 103.61 | res 105.24 (ha 12 candles) | 0.86786 | 0.0100% | — | sem_zona |
| 2026-10-22 23:06 | XRP-USDT-SWAP | 1.3120 | 1.3213/1.3066 | 1.3087 | res 1.3985 (ha 31 candles) | 0.01046 | 0.0100% | — | invalidado_setup_B |
| 2026-10-22 23:06 | DOGE-USDT-SWAP | 0.07907 | 0.07958/0.07874 | 0.07878 | res 0.07986 (ha 12 candles) | 0.00065 | 0.0037% | — | invalidado_setup_B |
| 2026-10-22 23:06 | ARB-USDT-SWAP | 0.18021 | 0.18209/0.17902 | 0.17899 | — | 0.00289 | -0.0109% | B/compra@0.17662 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-22 23:06 | WLD-USDT-SWAP | 0.55500 | 0.56230/0.54530 | 0.54560 | res 0.56650 (ha 6 candles) | 0.01406 | 0.0020% | — | sem_zona |
| 2026-10-22 23:06 | SUI-USDT-SWAP | 0.97980 | 0.98830/0.97340 | 0.97170 | res 1.0560 (ha 31 candles) | 0.00987 | 0.0034% | — | sem_zona |
| 2026-10-22 23:06 | UNI-USDT-SWAP | 7.0420 | 7.1080/6.9750 | 7.0050 | — | 0.09029 | 0.0039% | B/compra@7.0920 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-22 23:06 | LINK-USDT-SWAP | 12.02 | 12.14/11.96 | 11.95 | res 12.01 (ha 6 candles) | 0.11114 | -0.0004% | — | invalidado_setup_B |
| 2026-10-23 00:06 | BTC-USDT-SWAP | 81930.1 | 81970.0/81212.0 | 81380.9 | res 81535.9 (ha 5 candles) | 450.37 | 0.0081% | B/compra@80961.3 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-23 00:06 | ETH-USDT-SWAP | 2415.1 | 2416.7/2387.8 | 2388.3 | res 2401.9 (ha 5 candles) | 20.26 | 0.0073% | — | descartado_rr_baixo_setup_B |
| 2026-10-23 00:06 | SOL-USDT-SWAP | 104.57 | 104.84/103.81 | 103.61 | res 105.24 (ha 13 candles) | 0.91071 | 0.0100% | — | sem_zona |
| 2026-10-23 00:06 | XRP-USDT-SWAP | 1.3226 | 1.3251/1.3097 | 1.3087 | res 1.3985 (ha 32 candles) | 0.01103 | 0.0100% | — | sem_zona |
| 2026-10-23 00:06 | DOGE-USDT-SWAP | 0.07965 | 0.07970/0.07892 | 0.07878 | res 0.07986 (ha 13 candles) | 0.00068 | 0.0053% | B/compra@0.07996 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-23 00:06 | ARB-USDT-SWAP | 0.18251 | 0.18344/0.17983 | 0.17899 | — | 0.00291 | -0.0119% | B/compra@0.17662 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-23 00:06 | WLD-USDT-SWAP | 0.55810 | 0.56100/0.55220 | 0.54560 | res 0.56650 (ha 7 candles) | 0.01388 | 0.0015% | — | sem_zona |
| 2026-10-23 00:06 | SUI-USDT-SWAP | 0.99380 | 0.99460/0.97830 | 0.97170 | res 1.0560 (ha 32 candles) | 0.01055 | 0.0016% | B/compra@1.0002 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-23 00:06 | UNI-USDT-SWAP | 7.1710 | 7.1840/7.0220 | 7.0050 | — | 0.09793 | 0.0061% | — | descartado_rr_baixo_setup_B |
| 2026-10-23 00:06 | LINK-USDT-SWAP | 12.23 | 12.28/12.00 | 11.95 | res 12.01 (ha 7 candles) | 0.12571 | 0.0021% | A/compra@12.01 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-23 01:38 | BTC-USDT-SWAP | 81857.0 | 82010.8/81666.4 | 81857.0 | res 81535.9 (ha 6 candles) | 423.11 | 0.0072% | B/compra@80961.3 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-23 01:38 | ETH-USDT-SWAP | 2409.9 | 2416.3/2405.6 | 2409.9 | res 2401.9 (ha 6 candles) | 19.22 | 0.0080% | A/compra@2401.9 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-23 01:39 | SOL-USDT-SWAP | 104.19 | 104.60/103.98 | 104.19 | res 105.24 (ha 14 candles) | 0.87214 | 0.0100% | — | sem_zona |
| 2026-10-23 01:39 | XRP-USDT-SWAP | 1.3213 | 1.3235/1.3162 | 1.3213 | res 1.3985 (ha 33 candles) | 0.01051 | 0.0100% | — | sem_zona |
| 2026-10-23 01:39 | DOGE-USDT-SWAP | 0.07961 | 0.07975/0.07941 | 0.07961 | res 0.07986 (ha 14 candles) | 0.00065 | 0.0079% | B/compra@0.07996 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-23 01:39 | ARB-USDT-SWAP | 0.18516 | 0.18567/0.18174 | 0.18516 | — | 0.00299 | -0.0075% | B/compra@0.17662 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-23 01:39 | WLD-USDT-SWAP | 0.55280 | 0.56000/0.55150 | 0.55280 | res 0.56650 (ha 8 candles) | 0.01355 | 0.0050% | — | sem_zona |
| 2026-10-23 01:39 | SUI-USDT-SWAP | 0.99240 | 0.99550/0.98810 | 0.99240 | res 1.0560 (ha 33 candles) | 0.01021 | -0.0019% | B/compra@1.0002 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-23 01:39 | UNI-USDT-SWAP | 7.1740 | 7.2150/7.1060 | 7.1740 | — | 0.09764 | 0.0095% | B/compra@7.2270 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-23 01:39 | LINK-USDT-SWAP | 12.19 | 12.23/12.16 | 12.19 | res 12.01 (ha 8 candles) | 0.12257 | 0.0087% | A/compra@12.01 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-23 02:25 | BTC-USDT-SWAP | 81558.2 | 81857.0/81500.5 | 81857.0 | res 81535.9 (ha 7 candles) | 422.76 | 0.0076% | — | zona_expirada_setup_B |
| 2026-10-23 02:25 | ETH-USDT-SWAP | 2393.3 | 2409.9/2390.6 | 2409.9 | res 2401.9 (ha 7 candles) | 19.32 | 0.0085% | — | invalidado_setup_A |
| 2026-10-23 02:26 | SOL-USDT-SWAP | 103.96 | 104.26/103.79 | 104.19 | res 105.24 (ha 15 candles) | 0.83286 | 0.0100% | B/compra@103.48 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-23 02:26 | XRP-USDT-SWAP | 1.3183 | 1.3216/1.3165 | 1.3213 | res 1.3985 (ha 34 candles) | 0.01028 | 0.0100% | — | sem_zona |
| 2026-10-23 02:26 | DOGE-USDT-SWAP | 0.07942 | 0.07964/0.07933 | 0.07961 | res 0.07986 (ha 15 candles) | 0.00063 | 0.0088% | B/compra@0.07996 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-23 02:26 | ARB-USDT-SWAP | 0.18306 | 0.18549/0.18260 | 0.18516 | — | 0.00300 | -0.0055% | B/compra@0.17662 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-23 02:26 | WLD-USDT-SWAP | 0.54670 | 0.55580/0.54440 | 0.55280 | res 0.56230 (ha 3 candles) | 0.01381 | 0.0068% | — | sem_zona |
| 2026-10-23 02:26 | SUI-USDT-SWAP | 0.99000 | 0.99370/0.98740 | 0.99240 | res 1.0560 (ha 34 candles) | 0.00991 | -0.0021% | B/compra@1.0002 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-23 02:26 | UNI-USDT-SWAP | 7.1430 | 7.1820/7.1210 | 7.1740 | — | 0.09450 | 0.0100% | B/compra@7.2270 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-23 02:26 | LINK-USDT-SWAP | 12.14 | 12.20/12.12 | 12.19 | res 12.01 (ha 9 candles) | 0.12164 | 0.0100% | A/compra@12.01 (0t/2c) | zona_mapeada_setup_A |
