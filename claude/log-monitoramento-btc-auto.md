# Log de Monitoramento Automatico -- Multi-Par (script gratuito, GitHub Actions)

> Gerado por script Python sem LLM (ver monitor/fetch_and_check.py). Fonte: OKX. Cobre os pares em PAIRS (configuracao no topo do script) -- BTC-USDT-SWAP e os demais adicionados na expansao de 07/09/2026. Leitura e MECANICA (regras objetivas da secao 4 do plano), sem a prosa qualitativa que o Claude gerava -- cole este log numa conversa do Claude se quiser a leitura interpretativa.

| Data/Hora (BRT) | Par | Close 1h | High/Low 1h | Close 4h | Swing 1h ref | ATR 1h | Funding | Zona ativa | Status checklist |
|---|---|---|---|---|---|---|---|---|---|
| 2026-11-03 16:06 | BTC-USDT-SWAP | 77559.9 | 77888.8/77534.0 | 77656.5 | — | 390.50 | 0.0100% | — | sem_zona |
| 2026-11-03 16:06 | ETH-USDT-SWAP | 2292.2 | 2303.5/2291.7 | 2298.5 | — | 15.40 | 0.0100% | — | invalidado_setup_B |
| 2026-11-03 16:06 | SOL-USDT-SWAP | 93.39 | 93.89/93.29 | 93.70 | sup 91.21 (ha 12 candles) | 0.73786 | -0.0007% | — | sem_zona |
| 2026-11-03 16:06 | XRP-USDT-SWAP | 1.2801 | 1.2866/1.2798 | 1.2802 | — | 0.00934 | 0.0100% | B/compra@1.2723 (0t/2c) | zona_mapeada_setup_B |
| 2026-11-03 16:06 | DOGE-USDT-SWAP | 0.07519 | 0.07546/0.07515 | 0.07548 | — | 0.00050 | 0.0100% | — | sem_zona |
| 2026-11-03 16:06 | ARB-USDT-SWAP | 0.15782 | 0.15918/0.15753 | 0.15987 | sup 0.15125 (ha 15 candles) | 0.00205 | 0.0090% | — | sem_zona |
| 2026-11-03 16:06 | WLD-USDT-SWAP | 0.37160 | 0.37330/0.36900 | 0.37200 | — | 0.00451 | 0.0016% | — | sem_zona |
| 2026-11-03 16:06 | SUI-USDT-SWAP | 0.89600 | 0.90090/0.89550 | 0.89790 | res 0.90100 (ha 3 candles) | 0.00857 | 0.0100% | A/compra@0.87990 (0t/3c) | zona_mapeada_setup_A |
| 2026-11-03 16:06 | UNI-USDT-SWAP | 7.2470 | 7.3540/7.2270 | 7.3510 | — | 0.10600 | 0.0100% | B/venda@7.4110 (2t/3c) | zona_mapeada_setup_B |
| 2026-11-03 16:06 | LINK-USDT-SWAP | 11.10 | 11.18/11.09 | 11.15 | — | 0.09786 | 0.0100% | — | sem_zona |
| 2026-11-03 17:06 | BTC-USDT-SWAP | 77588.1 | 77642.0/77490.6 | 77588.1 | sup 76360.0 (ha 13 candles) | 374.41 | 0.0100% | — | sem_zona |
| 2026-11-03 17:06 | ETH-USDT-SWAP | 2286.1 | 2293.0/2283.3 | 2286.1 | — | 15.35 | 0.0100% | B/compra@2292.2 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-03 17:06 | SOL-USDT-SWAP | 93.24 | 93.45/93.11 | 93.24 | sup 91.21 (ha 13 candles) | 0.71286 | 0.0008% | — | sem_zona |
| 2026-11-03 17:06 | XRP-USDT-SWAP | 1.2771 | 1.2801/1.2751 | 1.2771 | — | 0.00939 | 0.0100% | B/compra@1.2723 (0t/3c) | zona_mapeada_setup_B |
| 2026-11-03 17:06 | DOGE-USDT-SWAP | 0.07510 | 0.07526/0.07498 | 0.07510 | — | 0.00050 | 0.0100% | — | sem_zona |
| 2026-11-03 17:06 | ARB-USDT-SWAP | 0.15774 | 0.15812/0.15730 | 0.15774 | sup 0.15125 (ha 16 candles) | 0.00203 | 0.0086% | — | sem_zona |
| 2026-11-03 17:06 | WLD-USDT-SWAP | 0.37040 | 0.37240/0.36960 | 0.37040 | — | 0.00447 | 0.0064% | — | sem_zona |
| 2026-11-03 17:06 | SUI-USDT-SWAP | 0.89540 | 0.89730/0.89290 | 0.89540 | — | 0.00849 | 0.0100% | A/compra@0.87990 (0t/4c) | zona_mapeada_setup_A |
| 2026-11-03 17:06 | UNI-USDT-SWAP | 7.2240 | 7.2520/7.1910 | 7.2240 | — | 0.10564 | 0.0100% | B/venda@7.4110 (2t/4c) | zona_mapeada_setup_B |
| 2026-11-03 17:06 | LINK-USDT-SWAP | 11.05 | 11.11/11.04 | 11.05 | — | 0.09757 | 0.0100% | — | sem_zona |
| 2026-11-03 18:06 | BTC-USDT-SWAP | 77838.4 | 77927.3/77570.3 | 77588.1 | sup 76360.0 (ha 14 candles) | 367.81 | 0.0100% | — | sem_zona |
| 2026-11-03 18:06 | ETH-USDT-SWAP | 2290.0 | 2292.2/2278.9 | 2286.1 | — | 15.21 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-11-03 18:06 | SOL-USDT-SWAP | 93.53 | 93.62/93.07 | 93.24 | sup 91.21 (ha 14 candles) | 0.69571 | 0.0039% | — | sem_zona |
| 2026-11-03 18:06 | XRP-USDT-SWAP | 1.2791 | 1.2799/1.2728 | 1.2771 | — | 0.00950 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-11-03 18:06 | DOGE-USDT-SWAP | 0.07524 | 0.07528/0.07494 | 0.07510 | — | 0.00049 | 0.0100% | — | sem_zona |
| 2026-11-03 18:06 | ARB-USDT-SWAP | 0.15733 | 0.15794/0.15681 | 0.15774 | sup 0.15125 (ha 17 candles) | 0.00204 | 0.0075% | — | sem_zona |
| 2026-11-03 18:06 | WLD-USDT-SWAP | 0.37060 | 0.37090/0.36820 | 0.37040 | — | 0.00432 | 0.0096% | — | sem_zona |
| 2026-11-03 18:06 | SUI-USDT-SWAP | 0.89650 | 0.89710/0.89280 | 0.89540 | — | 0.00827 | 0.0100% | A/compra@0.87990 (0t/5c) | zona_mapeada_setup_A |
| 2026-11-03 18:06 | UNI-USDT-SWAP | 7.2330 | 7.2630/7.2060 | 7.2240 | — | 0.10479 | 0.0100% | B/venda@7.4110 (2t/5c) | zona_mapeada_setup_B |
| 2026-11-03 18:06 | LINK-USDT-SWAP | 11.10 | 11.10/11.03 | 11.05 | — | 0.09729 | 0.0100% | — | sem_zona |
| 2026-11-03 19:06 | BTC-USDT-SWAP | 77876.9 | 78049.4/77789.3 | 77588.1 | sup 76360.0 (ha 15 candles) | 352.62 | 0.0100% | — | sem_zona |
| 2026-11-03 19:06 | ETH-USDT-SWAP | 2293.6 | 2299.0/2288.6 | 2286.1 | — | 14.74 | 0.0100% | B/compra@2296.4 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-03 19:06 | SOL-USDT-SWAP | 93.66 | 93.91/93.44 | 93.24 | sup 91.21 (ha 15 candles) | 0.66643 | 0.0060% | — | sem_zona |
| 2026-11-03 19:06 | XRP-USDT-SWAP | 1.2819 | 1.2882/1.2786 | 1.2771 | — | 0.00967 | 0.0100% | B/compra@1.2856 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-03 19:06 | DOGE-USDT-SWAP | 0.07556 | 0.07569/0.07520 | 0.07510 | — | 0.00048 | 0.0091% | B/compra@0.07592 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-03 19:06 | ARB-USDT-SWAP | 0.15794 | 0.15842/0.15703 | 0.15774 | sup 0.15125 (ha 18 candles) | 0.00203 | 0.0046% | — | sem_zona |
| 2026-11-03 19:06 | WLD-USDT-SWAP | 0.37490 | 0.37750/0.36970 | 0.37040 | — | 0.00464 | 0.0093% | — | sem_zona |
| 2026-11-03 19:06 | SUI-USDT-SWAP | 0.90010 | 0.90360/0.89530 | 0.89540 | — | 0.00821 | 0.0100% | A/compra@0.87990 (0t/6c) | zona_mapeada_setup_A |
| 2026-11-03 19:06 | UNI-USDT-SWAP | 7.1630 | 7.2350/7.1600 | 7.2240 | — | 0.10000 | 0.0100% | B/venda@7.4110 (2t/6c) | zona_mapeada_setup_B |
| 2026-11-03 19:06 | LINK-USDT-SWAP | 11.14 | 11.18/11.09 | 11.05 | — | 0.09614 | 0.0100% | — | sem_zona |
| 2026-11-03 20:06 | BTC-USDT-SWAP | 77863.3 | 77881.4/77685.7 | 77588.1 | sup 76360.0 (ha 16 candles) | 341.94 | 0.0100% | — | sem_zona |
| 2026-11-03 20:06 | ETH-USDT-SWAP | 2292.3 | 2294.3/2286.8 | 2286.1 | — | 14.45 | 0.0100% | — | invalidado_setup_B |
| 2026-11-03 20:06 | SOL-USDT-SWAP | 93.49 | 93.68/93.26 | 93.24 | sup 91.21 (ha 16 candles) | 0.65071 | 0.0084% | — | sem_zona |
| 2026-11-03 20:06 | XRP-USDT-SWAP | 1.2808 | 1.2823/1.2772 | 1.2771 | — | 0.00969 | 0.0100% | B/compra@1.2856 (0t/1c) | zona_mapeada_setup_B |
| 2026-11-03 20:06 | DOGE-USDT-SWAP | 0.07553 | 0.07558/0.07526 | 0.07510 | — | 0.00047 | 0.0079% | B/compra@0.07592 (0t/1c) | zona_mapeada_setup_B |
| 2026-11-03 20:06 | ARB-USDT-SWAP | 0.15868 | 0.15874/0.15739 | 0.15774 | sup 0.15125 (ha 19 candles) | 0.00203 | 0.0027% | — | sem_zona |
| 2026-11-03 20:06 | WLD-USDT-SWAP | 0.37690 | 0.37730/0.37360 | 0.37040 | — | 0.00468 | 0.0099% | — | sem_zona |
| 2026-11-03 20:06 | SUI-USDT-SWAP | 0.89980 | 0.90040/0.89510 | 0.89540 | — | 0.00817 | 0.0100% | A/compra@0.87990 (0t/7c) | zona_mapeada_setup_A |
| 2026-11-03 20:06 | UNI-USDT-SWAP | 7.2150 | 7.2200/7.1340 | 7.2240 | — | 0.09786 | 0.0100% | B/venda@7.4110 (2t/7c) | zona_mapeada_setup_B |
| 2026-11-03 20:06 | LINK-USDT-SWAP | 11.11 | 11.15/11.07 | 11.05 | — | 0.09671 | 0.0100% | — | sem_zona |
| 2026-11-03 21:06 | BTC-USDT-SWAP | 77439.4 | 77974.7/77400.0 | 77439.4 | sup 76360.0 (ha 17 candles) | 350.89 | 0.0100% | — | sem_zona |
| 2026-11-03 21:06 | ETH-USDT-SWAP | 2274.0 | 2293.7/2272.4 | 2274.0 | — | 15.03 | 0.0100% | B/venda@2277.5 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-03 21:06 | SOL-USDT-SWAP | 92.79 | 93.65/92.72 | 92.79 | sup 91.21 (ha 17 candles) | 0.67429 | 0.0100% | — | sem_zona |
| 2026-11-03 21:06 | XRP-USDT-SWAP | 1.2763 | 1.2839/1.2754 | 1.2763 | — | 0.01003 | 0.0100% | — | invalidado_setup_B |
| 2026-11-03 21:06 | DOGE-USDT-SWAP | 0.07517 | 0.07565/0.07513 | 0.07517 | — | 0.00048 | 0.0063% | B/compra@0.07592 (0t/2c) | zona_mapeada_setup_B |
| 2026-11-03 21:06 | ARB-USDT-SWAP | 0.15790 | 0.15966/0.15780 | 0.15790 | sup 0.15681 (ha 3 candles) | 0.00199 | 0.0037% | — | sem_zona |
| 2026-11-03 21:06 | WLD-USDT-SWAP | 0.37700 | 0.38080/0.37500 | 0.37700 | sup 0.36620 (ha 7 candles) | 0.00480 | 0.0100% | — | sem_zona |
| 2026-11-03 21:06 | SUI-USDT-SWAP | 0.89350 | 0.90220/0.89280 | 0.89350 | — | 0.00824 | 0.0100% | — | zona_expirada_setup_A |
| 2026-11-03 21:06 | UNI-USDT-SWAP | 7.2220 | 7.3070/7.2130 | 7.2220 | — | 0.09557 | 0.0100% | — | zona_expirada_setup_B |
| 2026-11-03 21:06 | LINK-USDT-SWAP | 11.02 | 11.15/11.02 | 11.02 | — | 0.10229 | 0.0100% | — | sem_zona |
| 2026-11-03 22:06 | BTC-USDT-SWAP | 77221.3 | 77530.1/76827.0 | 77439.4 | sup 76360.0 (ha 18 candles) | 388.38 | 0.0100% | — | sem_zona |
| 2026-11-03 22:06 | ETH-USDT-SWAP | 2273.6 | 2280.3/2258.0 | 2274.0 | — | 15.97 | 0.0100% | B/venda@2277.5 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-03 22:06 | SOL-USDT-SWAP | 92.45 | 92.97/91.57 | 92.79 | sup 91.21 (ha 18 candles) | 0.74857 | 0.0100% | — | sem_zona |
| 2026-11-03 22:06 | XRP-USDT-SWAP | 1.2610 | 1.2783/1.2527 | 1.2763 | — | 0.01163 | 0.0100% | B/venda@1.2640 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-03 22:06 | DOGE-USDT-SWAP | 0.07460 | 0.07527/0.07392 | 0.07517 | — | 0.00055 | 0.0046% | B/compra@0.07592 (0t/3c) | zona_mapeada_setup_B |
| 2026-11-03 22:06 | ARB-USDT-SWAP | 0.15629 | 0.15838/0.15478 | 0.15790 | sup 0.15681 (ha 4 candles) | 0.00215 | 0.0030% | A/venda@0.15681 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-03 22:06 | WLD-USDT-SWAP | 0.37350 | 0.37870/0.36920 | 0.37700 | sup 0.36620 (ha 8 candles) | 0.00526 | 0.0100% | — | sem_zona |
| 2026-11-03 22:06 | SUI-USDT-SWAP | 0.88670 | 0.89600/0.87670 | 0.89350 | — | 0.00915 | 0.0100% | B/compra@0.88510 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-03 22:06 | UNI-USDT-SWAP | 7.1790 | 7.2540/7.1160 | 7.2220 | — | 0.10200 | 0.0100% | B/venda@7.2270 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-03 22:06 | LINK-USDT-SWAP | 10.92 | 11.04/10.82 | 11.02 | — | 0.11343 | 0.0100% | — | sem_zona |
| 2026-11-03 23:06 | BTC-USDT-SWAP | 77010.9 | 77315.4/76785.0 | 77439.4 | sup 76360.0 (ha 19 candles) | 411.21 | 0.0100% | — | sem_zona |
| 2026-11-03 23:06 | ETH-USDT-SWAP | 2263.1 | 2278.0/2258.2 | 2274.0 | — | 16.61 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-11-03 23:06 | SOL-USDT-SWAP | 91.95 | 92.61/91.60 | 92.79 | sup 91.21 (ha 19 candles) | 0.79143 | 0.0100% | — | sem_zona |
| 2026-11-03 23:06 | XRP-USDT-SWAP | 1.2529 | 1.2622/1.2476 | 1.2763 | — | 0.01217 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-11-03 23:06 | DOGE-USDT-SWAP | 0.07401 | 0.07469/0.07369 | 0.07517 | — | 0.00059 | 0.0018% | B/compra@0.07592 (0t/4c) | zona_mapeada_setup_B |
| 2026-11-03 23:06 | ARB-USDT-SWAP | 0.15585 | 0.15674/0.15442 | 0.15790 | sup 0.15681 (ha 5 candles) | 0.00204 | 0.0028% | A/venda@0.15681 (1t/0c) | zona_mapeada_setup_A |
| 2026-11-03 23:06 | WLD-USDT-SWAP | 0.37060 | 0.37480/0.36690 | 0.37700 | sup 0.36620 (ha 9 candles) | 0.00545 | 0.0100% | — | sem_zona |
| 2026-11-03 23:06 | SUI-USDT-SWAP | 0.87940 | 0.88850/0.87460 | 0.89350 | — | 0.00946 | 0.0100% | — | invalidado_setup_B |
| 2026-11-03 23:06 | UNI-USDT-SWAP | 7.0890 | 7.2020/7.0500 | 7.2220 | — | 0.10629 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-11-03 23:06 | LINK-USDT-SWAP | 10.85 | 10.95/10.79 | 11.02 | — | 0.12000 | 0.0100% | — | sem_zona |
| 2026-11-04 00:06 | BTC-USDT-SWAP | 76131.5 | 77189.0/76115.3 | 77439.4 | sup 76360.0 (ha 20 candles) | 451.10 | 0.0100% | A/venda@76360.0 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-04 00:06 | ETH-USDT-SWAP | 2243.7 | 2270.5/2243.1 | 2274.0 | — | 16.94 | 0.0100% | B/compra@2246.2 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-04 00:06 | SOL-USDT-SWAP | 90.82 | 92.27/90.80 | 92.79 | sup 91.21 (ha 20 candles) | 0.82214 | 0.0100% | A/venda@91.21 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-04 00:06 | XRP-USDT-SWAP | 1.2482 | 1.2557/1.2482 | 1.2763 | — | 0.01044 | 0.0100% | B/compra@1.2413 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-04 00:06 | DOGE-USDT-SWAP | 0.07309 | 0.07429/0.07306 | 0.07517 | — | 0.00061 | 0.0005% | B/compra@0.07592 (0t/5c) | zona_mapeada_setup_B |
| 2026-11-04 00:06 | ARB-USDT-SWAP | 0.15441 | 0.15709/0.15434 | 0.15790 | sup 0.15681 (ha 6 candles) | 0.00199 | 0.0032% | — | descartado_rr_baixo_setup_A |
| 2026-11-04 00:06 | WLD-USDT-SWAP | 0.36670 | 0.37320/0.36650 | 0.37700 | sup 0.36620 (ha 10 candles) | 0.00549 | 0.0100% | — | sem_zona |
| 2026-11-04 00:06 | SUI-USDT-SWAP | 0.86740 | 0.88380/0.86670 | 0.89350 | — | 0.00949 | 0.0100% | B/compra@0.87440 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-04 00:06 | UNI-USDT-SWAP | 7.0120 | 7.1470/7.0080 | 7.2220 | — | 0.10629 | 0.0100% | B/compra@6.9410 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-04 00:06 | LINK-USDT-SWAP | 10.73 | 10.90/10.72 | 11.02 | — | 0.12136 | 0.0100% | — | sem_zona |
| 2026-11-04 01:06 | BTC-USDT-SWAP | 76450.2 | 76547.0/75690.1 | 76450.2 | sup 76360.0 (ha 21 candles) | 471.46 | 0.0100% | A/venda@76360.0 (1t/0c) | zona_mapeada_setup_A |
| 2026-11-04 01:06 | ETH-USDT-SWAP | 2248.5 | 2250.0/2225.0 | 2248.5 | sup 2240.1 (ha 21 candles) | 16.54 | 0.0100% | — | invalidado_tendencia_virou_setup_B |
| 2026-11-04 01:06 | SOL-USDT-SWAP | 91.01 | 91.20/89.78 | 91.01 | sup 91.21 (ha 21 candles) | 0.83357 | 0.0065% | A/venda@91.21 (1t/0c) | zona_mapeada_setup_A |
| 2026-11-04 01:06 | XRP-USDT-SWAP | 1.2594 | 1.2606/1.2412 | 1.2594 | — | 0.01068 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-11-04 01:06 | DOGE-USDT-SWAP | 0.07334 | 0.07346/0.07223 | 0.07334 | — | 0.00064 | 0.0001% | B/compra@0.07592 (0t/6c) | zona_mapeada_setup_B |
| 2026-11-04 01:06 | ARB-USDT-SWAP | 0.15444 | 0.15500/0.15256 | 0.15444 | sup 0.15681 (ha 7 candles) | 0.00194 | 0.0034% | — | sem_zona |
| 2026-11-04 01:06 | WLD-USDT-SWAP | 0.36810 | 0.36830/0.36130 | 0.36810 | sup 0.36620 (ha 11 candles) | 0.00546 | 0.0072% | — | sem_zona |
| 2026-11-04 01:06 | SUI-USDT-SWAP | 0.87350 | 0.87420/0.85720 | 0.87350 | — | 0.00981 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-11-04 01:06 | UNI-USDT-SWAP | 7.1010 | 7.1180/6.9370 | 7.1010 | res 7.3070 (ha 4 candles) | 0.10629 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-11-04 01:06 | LINK-USDT-SWAP | 10.77 | 10.78/10.62 | 10.77 | sup 11.00 (ha 21 candles) | 0.12021 | 0.0100% | A/venda@11.00 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-04 02:06 | BTC-USDT-SWAP | 77345.7 | 77577.8/76389.1 | 76450.2 | sup 76360.0 (ha 22 candles) | 528.82 | 0.0100% | — | invalidado_setup_A |
| 2026-11-04 02:06 | ETH-USDT-SWAP | 2279.1 | 2285.8/2246.7 | 2248.5 | sup 2240.1 (ha 22 candles) | 18.07 | 0.0091% | — | sem_zona |
| 2026-11-04 02:06 | SOL-USDT-SWAP | 92.28 | 92.54/90.91 | 91.01 | sup 91.21 (ha 22 candles) | 0.89143 | 0.0048% | — | invalidado_setup_A |
| 2026-11-04 02:06 | XRP-USDT-SWAP | 1.2706 | 1.2736/1.2577 | 1.2594 | — | 0.01092 | 0.0100% | B/compra@1.2723 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-04 02:06 | DOGE-USDT-SWAP | 0.07421 | 0.07441/0.07326 | 0.07334 | — | 0.00069 | 0.0005% | B/compra@0.07592 (0t/7c) | zona_mapeada_setup_B |
| 2026-11-04 02:06 | ARB-USDT-SWAP | 0.15766 | 0.15832/0.15426 | 0.15444 | sup 0.15681 (ha 8 candles) | 0.00207 | 0.0001% | — | sem_zona |
| 2026-11-04 02:06 | WLD-USDT-SWAP | 0.37560 | 0.37680/0.36740 | 0.36810 | sup 0.36620 (ha 12 candles) | 0.00582 | 0.0039% | — | sem_zona |
| 2026-11-04 02:06 | SUI-USDT-SWAP | 0.88590 | 0.88800/0.87240 | 0.87350 | — | 0.01019 | 0.0100% | B/compra@0.88510 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-04 02:06 | UNI-USDT-SWAP | 7.1950 | 7.2540/7.0850 | 7.1010 | res 7.3070 (ha 5 candles) | 0.11179 | 0.0100% | — | sem_zona |
| 2026-11-04 02:06 | LINK-USDT-SWAP | 10.95 | 10.98/10.76 | 10.77 | sup 11.00 (ha 22 candles) | 0.12786 | 0.0100% | A/venda@11.00 (1t/0c) | zona_mapeada_setup_A |
| 2026-11-04 03:06 | BTC-USDT-SWAP | 77716.6 | 78170.2/77232.4 | 76450.2 | sup 76360.0 (ha 23 candles) | 554.48 | 0.0100% | — | sem_zona |
| 2026-11-04 03:06 | ETH-USDT-SWAP | 2292.0 | 2307.1/2275.7 | 2248.5 | sup 2240.1 (ha 23 candles) | 18.78 | 0.0083% | — | sem_zona |
| 2026-11-04 03:06 | SOL-USDT-SWAP | 92.71 | 93.32/92.03 | 91.01 | sup 91.21 (ha 23 candles) | 0.91357 | 0.0060% | — | sem_zona |
| 2026-11-04 03:06 | XRP-USDT-SWAP | 1.2760 | 1.2831/1.2686 | 1.2594 | — | 0.01112 | 0.0100% | B/compra@1.2723 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-04 03:06 | DOGE-USDT-SWAP | 0.07467 | 0.07508/0.07406 | 0.07334 | — | 0.00072 | 0.0028% | — | zona_expirada_setup_B |
| 2026-11-04 03:06 | ARB-USDT-SWAP | 0.15961 | 0.16091/0.15700 | 0.15444 | sup 0.15681 (ha 9 candles) | 0.00222 | 0.0008% | — | sem_zona |
| 2026-11-04 03:06 | WLD-USDT-SWAP | 0.38280 | 0.38610/0.37260 | 0.36810 | sup 0.36620 (ha 13 candles) | 0.00645 | 0.0025% | — | sem_zona |
| 2026-11-04 03:06 | SUI-USDT-SWAP | 0.89130 | 0.89810/0.88250 | 0.87350 | — | 0.01068 | 0.0100% | B/compra@0.88510 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-04 03:06 | UNI-USDT-SWAP | 7.2960 | 7.3570/7.1750 | 7.1010 | res 7.3070 (ha 6 candles) | 0.11550 | 0.0100% | — | sem_zona |
| 2026-11-04 03:06 | LINK-USDT-SWAP | 11.01 | 11.09/10.90 | 10.77 | sup 11.00 (ha 23 candles) | 0.13143 | 0.0100% | A/venda@11.00 (2t/0c) | zona_mapeada_setup_A |
| 2026-11-04 04:06 | BTC-USDT-SWAP | 77965.0 | 78045.2/77716.6 | 76450.2 | sup 75690.1 (ha 3 candles) | 550.19 | 0.0100% | — | sem_zona |
| 2026-11-04 04:06 | ETH-USDT-SWAP | 2296.7 | 2300.0/2287.4 | 2248.5 | sup 2225.0 (ha 3 candles) | 18.51 | 0.0076% | — | sem_zona |
| 2026-11-04 04:06 | SOL-USDT-SWAP | 92.99 | 93.16/92.59 | 91.01 | sup 89.78 (ha 3 candles) | 0.89429 | 0.0079% | — | sem_zona |
| 2026-11-04 04:06 | XRP-USDT-SWAP | 1.2749 | 1.2779/1.2727 | 1.2594 | — | 0.01091 | 0.0100% | B/compra@1.2723 (2t/0c) | zona_mapeada_setup_B |
| 2026-11-04 04:06 | DOGE-USDT-SWAP | 0.07476 | 0.07489/0.07448 | 0.07334 | — | 0.00071 | 0.0061% | B/compra@0.07457 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-04 04:06 | ARB-USDT-SWAP | 0.16006 | 0.16096/0.15915 | 0.15444 | sup 0.15256 (ha 3 candles) | 0.00222 | 0.0000% | — | sem_zona |
| 2026-11-04 04:06 | WLD-USDT-SWAP | 0.38280 | 0.38650/0.38150 | 0.36810 | sup 0.36130 (ha 3 candles) | 0.00636 | -0.0000% | — | sem_zona |
| 2026-11-04 04:06 | SUI-USDT-SWAP | 0.89680 | 0.89930/0.88840 | 0.87350 | — | 0.01082 | 0.0100% | B/compra@0.88510 (1t/1c) | zona_mapeada_setup_B |
| 2026-11-04 04:06 | UNI-USDT-SWAP | 7.3690 | 7.4020/7.2810 | 7.1010 | res 7.3070 (ha 7 candles) | 0.11836 | 0.0100% | A/compra@7.3070 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-04 04:06 | LINK-USDT-SWAP | 11.06 | 11.08/10.98 | 10.77 | sup 10.62 (ha 3 candles) | 0.13000 | 0.0099% | — | invalidado_setup_A |
| 2026-11-04 05:06 | BTC-USDT-SWAP | 78105.3 | 78345.6/77858.0 | 78105.3 | sup 75690.1 (ha 4 candles) | 571.46 | 0.0089% | — | sem_zona |
| 2026-11-04 05:06 | ETH-USDT-SWAP | 2302.6 | 2313.0/2294.0 | 2302.6 | sup 2225.0 (ha 4 candles) | 19.33 | 0.0068% | — | sem_zona |
| 2026-11-04 05:06 | SOL-USDT-SWAP | 93.01 | 93.40/92.71 | 93.01 | sup 89.78 (ha 4 candles) | 0.91357 | 0.0100% | — | sem_zona |
| 2026-11-04 05:06 | XRP-USDT-SWAP | 1.2729 | 1.2789/1.2716 | 1.2729 | — | 0.01086 | 0.0100% | — | zona_expirada_setup_B |
| 2026-11-04 05:06 | DOGE-USDT-SWAP | 0.07483 | 0.07513/0.07452 | 0.07483 | — | 0.00073 | 0.0076% | B/compra@0.07457 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-04 05:06 | ARB-USDT-SWAP | 0.15983 | 0.16121/0.15890 | 0.15983 | sup 0.15256 (ha 4 candles) | 0.00224 | 0.0021% | — | sem_zona |
| 2026-11-04 05:06 | WLD-USDT-SWAP | 0.39240 | 0.39670/0.38110 | 0.39240 | sup 0.36130 (ha 4 candles) | 0.00726 | 0.0002% | — | sem_zona |
| 2026-11-04 05:06 | SUI-USDT-SWAP | 0.90270 | 0.90730/0.89380 | 0.90270 | — | 0.01143 | 0.0100% | B/compra@0.88510 (1t/2c) | zona_mapeada_setup_B |
| 2026-11-04 05:06 | UNI-USDT-SWAP | 7.4730 | 7.5510/7.3280 | 7.4730 | res 7.3070 (ha 8 candles) | 0.12893 | 0.0100% | — | descartado_rr_baixo_setup_A |
| 2026-11-04 05:06 | LINK-USDT-SWAP | 11.12 | 11.17/11.02 | 11.12 | sup 10.62 (ha 4 candles) | 0.13650 | 0.0085% | — | sem_zona |
| 2026-11-04 06:06 | BTC-USDT-SWAP | 78461.9 | 78490.0/78105.4 | 78105.3 | sup 75690.1 (ha 5 candles) | 573.60 | 0.0089% | B/venda@78831.1 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-04 06:06 | ETH-USDT-SWAP | 2322.4 | 2328.8/2302.5 | 2302.6 | sup 2225.0 (ha 5 candles) | 20.37 | 0.0078% | B/venda@2318.1 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-04 06:06 | SOL-USDT-SWAP | 93.25 | 93.59/93.00 | 93.01 | sup 89.78 (ha 5 candles) | 0.91286 | 0.0100% | — | sem_zona |
| 2026-11-04 06:06 | XRP-USDT-SWAP | 1.2800 | 1.2837/1.2730 | 1.2729 | — | 0.01115 | 0.0100% | B/compra@1.2856 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-04 06:06 | DOGE-USDT-SWAP | 0.07519 | 0.07546/0.07481 | 0.07483 | — | 0.00076 | 0.0094% | B/compra@0.07457 (1t/1c) | zona_mapeada_setup_B |
| 2026-11-04 06:06 | ARB-USDT-SWAP | 0.16202 | 0.16234/0.15979 | 0.15983 | sup 0.15256 (ha 5 candles) | 0.00231 | 0.0026% | — | sem_zona |
| 2026-11-04 06:06 | WLD-USDT-SWAP | 0.39420 | 0.39630/0.39140 | 0.39240 | sup 0.36130 (ha 5 candles) | 0.00731 | -0.0011% | — | sem_zona |
| 2026-11-04 06:06 | SUI-USDT-SWAP | 0.91450 | 0.91820/0.90250 | 0.90270 | — | 0.01216 | 0.0100% | B/compra@0.88510 (1t/3c) | zona_mapeada_setup_B |
| 2026-11-04 06:06 | UNI-USDT-SWAP | 7.4820 | 7.5550/7.4590 | 7.4730 | res 7.3070 (ha 9 candles) | 0.12671 | 0.0100% | — | sem_zona |
| 2026-11-04 06:06 | LINK-USDT-SWAP | 11.17 | 11.24/11.12 | 11.12 | sup 10.62 (ha 5 candles) | 0.13893 | 0.0080% | — | sem_zona |
| 2026-11-04 08:06 | BTC-USDT-SWAP | 78569.6 | 78688.0/78345.0 | 78105.3 | sup 75690.1 (ha 7 candles) | 581.18 | 0.0076% | B/venda@78831.1 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-04 08:06 | ETH-USDT-SWAP | 2327.4 | 2334.7/2320.0 | 2302.6 | sup 2225.0 (ha 7 candles) | 20.44 | 0.0087% | — | invalidado_setup_B |
| 2026-11-04 08:06 | SOL-USDT-SWAP | 93.58 | 93.82/93.02 | 93.01 | sup 89.78 (ha 7 candles) | 0.93786 | 0.0100% | — | sem_zona |
| 2026-11-04 08:06 | XRP-USDT-SWAP | 1.2910 | 1.2983/1.2810 | 1.2729 | — | 0.01206 | 0.0100% | B/compra@1.2856 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-04 08:06 | DOGE-USDT-SWAP | 0.07523 | 0.07546/0.07507 | 0.07483 | — | 0.00076 | 0.0100% | B/compra@0.07457 (1t/3c) | zona_mapeada_setup_B |
| 2026-11-04 08:06 | ARB-USDT-SWAP | 0.16368 | 0.16393/0.16231 | 0.15983 | sup 0.15256 (ha 7 candles) | 0.00243 | 0.0091% | — | sem_zona |
| 2026-11-04 08:06 | WLD-USDT-SWAP | 0.39080 | 0.39100/0.38730 | 0.39240 | sup 0.36130 (ha 7 candles) | 0.00761 | 0.0037% | — | sem_zona |
| 2026-11-04 08:06 | SUI-USDT-SWAP | 0.91550 | 0.91940/0.90940 | 0.90270 | — | 0.01281 | 0.0100% | B/compra@0.88510 (1t/5c) | zona_mapeada_setup_B |
| 2026-11-04 08:06 | UNI-USDT-SWAP | 7.4630 | 7.5070/7.4300 | 7.4730 | res 7.3070 (ha 11 candles) | 0.12836 | 0.0100% | — | sem_zona |
| 2026-11-04 08:06 | LINK-USDT-SWAP | 11.18 | 11.21/11.10 | 11.12 | sup 10.62 (ha 7 candles) | 0.14300 | 0.0052% | — | sem_zona |
| 2026-11-04 09:06 | BTC-USDT-SWAP | 78440.5 | 78690.8/78425.0 | 78440.5 | sup 75690.1 (ha 8 candles) | 581.59 | 0.0070% | — | descartado_rr_baixo_setup_B |
| 2026-11-04 09:06 | ETH-USDT-SWAP | 2326.8 | 2338.9/2325.2 | 2326.8 | sup 2225.0 (ha 8 candles) | 20.68 | 0.0069% | — | sem_zona |
| 2026-11-04 09:06 | SOL-USDT-SWAP | 93.56 | 94.15/93.44 | 93.56 | sup 89.78 (ha 8 candles) | 0.95500 | 0.0100% | — | sem_zona |
| 2026-11-04 09:06 | XRP-USDT-SWAP | 1.2877 | 1.2957/1.2871 | 1.2877 | — | 0.01199 | 0.0100% | B/compra@1.2856 (2t/0c) | zona_mapeada_setup_B |
| 2026-11-04 09:06 | DOGE-USDT-SWAP | 0.07525 | 0.07559/0.07508 | 0.07525 | sup 0.07223 (ha 8 candles) | 0.00077 | 0.0100% | B/compra@0.07457 (1t/4c) | zona_mapeada_setup_B |
| 2026-11-04 09:06 | ARB-USDT-SWAP | 0.16340 | 0.16565/0.16321 | 0.16340 | sup 0.15256 (ha 8 candles) | 0.00251 | 0.0100% | — | sem_zona |
| 2026-11-04 09:06 | WLD-USDT-SWAP | 0.38680 | 0.39320/0.38650 | 0.38680 | sup 0.36130 (ha 8 candles) | 0.00754 | 0.0031% | — | sem_zona |
| 2026-11-04 09:06 | SUI-USDT-SWAP | 0.91010 | 0.91720/0.90960 | 0.91010 | — | 0.01276 | 0.0100% | B/compra@0.88510 (1t/6c) | zona_mapeada_setup_B |
| 2026-11-04 09:06 | UNI-USDT-SWAP | 7.4370 | 7.5230/7.4360 | 7.4370 | res 7.5550 (ha 3 candles) | 0.12921 | 0.0100% | — | sem_zona |
| 2026-11-04 09:06 | LINK-USDT-SWAP | 11.16 | 11.22/11.15 | 11.16 | sup 10.62 (ha 8 candles) | 0.14100 | 0.0048% | — | sem_zona |
| 2026-11-04 10:06 | BTC-USDT-SWAP | 78261.5 | 78466.3/77976.0 | 78440.5 | sup 75690.1 (ha 9 candles) | 602.63 | 0.0087% | — | sem_zona |
| 2026-11-04 10:06 | ETH-USDT-SWAP | 2312.7 | 2328.5/2308.5 | 2326.8 | sup 2225.0 (ha 9 candles) | 21.57 | 0.0052% | — | sem_zona |
| 2026-11-04 10:06 | SOL-USDT-SWAP | 92.56 | 93.63/92.42 | 93.56 | sup 89.78 (ha 9 candles) | 1.0114 | 0.0100% | — | sem_zona |
| 2026-11-04 10:06 | XRP-USDT-SWAP | 1.2775 | 1.2885/1.2754 | 1.2877 | — | 0.01256 | 0.0100% | — | invalidado_setup_B |
| 2026-11-04 10:06 | DOGE-USDT-SWAP | 0.07450 | 0.07531/0.07433 | 0.07525 | sup 0.07223 (ha 9 candles) | 0.00081 | 0.0100% | B/compra@0.07457 (2t/0c) | zona_mapeada_setup_B |
| 2026-11-04 10:06 | ARB-USDT-SWAP | 0.16126 | 0.16375/0.16095 | 0.16340 | sup 0.15256 (ha 9 candles) | 0.00261 | 0.0100% | — | sem_zona |
| 2026-11-04 10:06 | WLD-USDT-SWAP | 0.37700 | 0.38670/0.37610 | 0.38680 | sup 0.36130 (ha 9 candles) | 0.00804 | 0.0058% | — | sem_zona |
| 2026-11-04 10:06 | SUI-USDT-SWAP | 0.90110 | 0.91100/0.89740 | 0.91010 | — | 0.01335 | 0.0100% | B/compra@0.88510 (1t/7c) | zona_mapeada_setup_B |
| 2026-11-04 10:06 | UNI-USDT-SWAP | 7.3350 | 7.4680/7.3100 | 7.4370 | res 7.5550 (ha 4 candles) | 0.13436 | 0.0100% | — | sem_zona |
| 2026-11-04 10:06 | LINK-USDT-SWAP | 11.08 | 11.17/11.04 | 11.16 | sup 10.62 (ha 9 candles) | 0.14457 | 0.0040% | — | sem_zona |
| 2026-11-04 11:06 | BTC-USDT-SWAP | 78339.0 | 78515.5/78255.9 | 78440.5 | sup 75690.1 (ha 10 candles) | 580.12 | 0.0096% | — | sem_zona |
| 2026-11-04 11:06 | ETH-USDT-SWAP | 2318.1 | 2321.0/2312.7 | 2326.8 | sup 2225.0 (ha 10 candles) | 20.64 | 0.0040% | — | sem_zona |
| 2026-11-04 11:06 | SOL-USDT-SWAP | 92.92 | 93.07/92.51 | 93.56 | sup 89.78 (ha 10 candles) | 0.98500 | 0.0100% | — | sem_zona |
| 2026-11-04 11:06 | XRP-USDT-SWAP | 1.2815 | 1.2847/1.2773 | 1.2877 | — | 0.01249 | 0.0100% | B/compra@1.2723 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-04 11:06 | DOGE-USDT-SWAP | 0.07479 | 0.07489/0.07450 | 0.07525 | sup 0.07223 (ha 10 candles) | 0.00080 | 0.0087% | — | invalidado_tendencia_virou_setup_B |
| 2026-11-04 11:06 | ARB-USDT-SWAP | 0.16106 | 0.16224/0.16057 | 0.16340 | sup 0.15256 (ha 10 candles) | 0.00260 | 0.0100% | — | sem_zona |
| 2026-11-04 11:06 | WLD-USDT-SWAP | 0.38010 | 0.38320/0.37670 | 0.38680 | sup 0.36130 (ha 10 candles) | 0.00809 | 0.0051% | — | sem_zona |
| 2026-11-04 11:06 | SUI-USDT-SWAP | 0.90440 | 0.90590/0.89970 | 0.91010 | — | 0.01312 | 0.0100% | — | zona_expirada_setup_B |
| 2026-11-04 11:06 | UNI-USDT-SWAP | 7.3190 | 7.3730/7.3020 | 7.4370 | res 7.5550 (ha 5 candles) | 0.13271 | 0.0100% | — | sem_zona |
| 2026-11-04 11:06 | LINK-USDT-SWAP | 11.15 | 11.18/11.08 | 11.16 | sup 10.62 (ha 10 candles) | 0.14236 | 0.0029% | — | sem_zona |
| 2026-11-04 12:06 | BTC-USDT-SWAP | 79302.0 | 79650.0/78164.6 | 78440.5 | sup 75690.1 (ha 11 candles) | 636.00 | 0.0091% | — | sem_zona |
| 2026-11-04 12:06 | ETH-USDT-SWAP | 2378.2 | 2388.0/2311.6 | 2326.8 | sup 2225.0 (ha 11 candles) | 24.51 | 0.0067% | B/venda@2378.8 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-04 12:06 | SOL-USDT-SWAP | 95.15 | 95.64/92.57 | 93.56 | sup 89.78 (ha 11 candles) | 1.1043 | 0.0100% | B/venda@95.89 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-04 12:06 | XRP-USDT-SWAP | 1.3164 | 1.3179/1.2785 | 1.2877 | — | 0.01347 | 0.0100% | B/compra@1.2723 (0t/1c) | zona_mapeada_setup_B |
| 2026-11-04 12:06 | DOGE-USDT-SWAP | 0.07662 | 0.07696/0.07454 | 0.07525 | sup 0.07223 (ha 11 candles) | 0.00088 | 0.0078% | B/venda@0.07630 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-04 12:06 | ARB-USDT-SWAP | 0.16653 | 0.16745/0.15989 | 0.16340 | sup 0.15256 (ha 11 candles) | 0.00288 | 0.0100% | B/venda@0.16676 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-04 12:06 | WLD-USDT-SWAP | 0.39030 | 0.39170/0.37740 | 0.38680 | sup 0.36130 (ha 11 candles) | 0.00843 | 0.0032% | — | sem_zona |
| 2026-11-04 12:06 | SUI-USDT-SWAP | 0.93120 | 0.93870/0.89960 | 0.91010 | — | 0.01454 | 0.0100% | B/venda@0.93080 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-04 12:06 | UNI-USDT-SWAP | 7.5450 | 7.5500/7.2520 | 7.4370 | res 7.5550 (ha 6 candles) | 0.14414 | 0.0100% | — | sem_zona |
| 2026-11-04 12:06 | LINK-USDT-SWAP | 11.54 | 11.57/11.08 | 11.16 | sup 10.62 (ha 11 candles) | 0.16164 | 0.0065% | B/venda@11.62 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-04 13:06 | BTC-USDT-SWAP | 80273.5 | 81199.9/79270.0 | 80273.5 | sup 77976.0 (ha 3 candles) | 735.96 | 0.0100% | B/venda@80822.6 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-04 13:06 | ETH-USDT-SWAP | 2425.8 | 2451.1/2377.3 | 2425.8 | sup 2308.5 (ha 3 candles) | 28.37 | 0.0100% | — | invalidado_setup_B |
| 2026-11-04 13:06 | SOL-USDT-SWAP | 96.65 | 98.13/95.10 | 96.65 | sup 92.42 (ha 3 candles) | 1.2486 | 0.0100% | — | invalidado_setup_B |
| 2026-11-04 13:06 | XRP-USDT-SWAP | 1.3155 | 1.3421/1.3128 | 1.3155 | res 1.2983 (ha 5 candles) | 0.01452 | 0.0100% | B/compra@1.2723 (0t/2c) | zona_mapeada_setup_B |
| 2026-11-04 13:06 | DOGE-USDT-SWAP | 0.07729 | 0.07834/0.07662 | 0.07729 | sup 0.07433 (ha 3 candles) | 0.00093 | 0.0096% | B/venda@0.07630 (0t/1c) | zona_mapeada_setup_B |
| 2026-11-04 13:06 | ARB-USDT-SWAP | 0.16840 | 0.17245/0.16642 | 0.16840 | — | 0.00314 | 0.0100% | — | invalidado_setup_B |
| 2026-11-04 13:06 | WLD-USDT-SWAP | 0.39220 | 0.40180/0.38970 | 0.39220 | sup 0.37610 (ha 3 candles) | 0.00873 | -0.0004% | — | sem_zona |
| 2026-11-04 13:06 | SUI-USDT-SWAP | 0.94290 | 0.95700/0.93010 | 0.94290 | — | 0.01546 | 0.0100% | — | invalidado_setup_B |
| 2026-11-04 13:06 | UNI-USDT-SWAP | 7.6710 | 7.7580/7.5320 | 7.6710 | res 7.5550 (ha 7 candles) | 0.14943 | 0.0100% | A/compra@7.5550 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-04 13:06 | LINK-USDT-SWAP | 11.60 | 11.79/11.54 | 11.60 | sup 11.04 (ha 3 candles) | 0.16864 | 0.0098% | B/venda@11.62 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-04 14:06 | BTC-USDT-SWAP | 80491.2 | 80700.0/80267.9 | 80273.5 | sup 77976.0 (ha 4 candles) | 690.14 | 0.0087% | B/venda@80822.6 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-04 14:06 | ETH-USDT-SWAP | 2434.2 | 2446.1/2425.8 | 2425.8 | sup 2308.5 (ha 4 candles) | 27.86 | 0.0100% | B/venda@2417.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-04 14:06 | SOL-USDT-SWAP | 96.63 | 97.28/96.38 | 96.65 | sup 92.42 (ha 4 candles) | 1.2079 | 0.0100% | B/venda@96.94 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-04 14:06 | XRP-USDT-SWAP | 1.3148 | 1.3212/1.3083 | 1.3155 | res 1.2983 (ha 6 candles) | 0.01491 | 0.0100% | B/compra@1.2723 (0t/3c) | zona_mapeada_setup_B |
| 2026-11-04 14:06 | DOGE-USDT-SWAP | 0.07755 | 0.07784/0.07711 | 0.07729 | sup 0.07433 (ha 4 candles) | 0.00090 | 0.0100% | B/venda@0.07630 (0t/2c) | zona_mapeada_setup_B |
| 2026-11-04 14:06 | ARB-USDT-SWAP | 0.16668 | 0.16976/0.16628 | 0.16840 | — | 0.00320 | 0.0100% | B/compra@0.16447 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-04 14:06 | WLD-USDT-SWAP | 0.39120 | 0.39540/0.38840 | 0.39220 | sup 0.37610 (ha 4 candles) | 0.00875 | -0.0036% | — | sem_zona |
| 2026-11-04 14:06 | SUI-USDT-SWAP | 0.94470 | 0.95020/0.93850 | 0.94290 | — | 0.01508 | 0.0100% | B/compra@0.93870 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-04 14:06 | UNI-USDT-SWAP | 7.7030 | 7.7860/7.6310 | 7.6710 | res 7.5550 (ha 8 candles) | 0.15057 | 0.0100% | A/compra@7.5550 (0t/1c) | zona_mapeada_setup_A |
| 2026-11-04 14:06 | LINK-USDT-SWAP | 11.63 | 11.71/11.56 | 11.60 | sup 11.04 (ha 4 candles) | 0.16729 | 0.0100% | B/venda@11.62 (2t/0c) | zona_mapeada_setup_B |
| 2026-11-04 15:06 | BTC-USDT-SWAP | 80392.9 | 80533.2/80182.0 | 80273.5 | sup 77976.0 (ha 5 candles) | 654.01 | 0.0085% | B/venda@80822.6 (1t/1c) | zona_mapeada_setup_B |
| 2026-11-04 15:06 | ETH-USDT-SWAP | 2424.0 | 2435.0/2419.0 | 2425.8 | sup 2308.5 (ha 5 candles) | 27.22 | 0.0100% | — | invalidado_setup_B |
| 2026-11-04 15:06 | SOL-USDT-SWAP | 95.68 | 96.71/95.46 | 96.65 | sup 92.42 (ha 5 candles) | 1.1957 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-11-04 15:06 | XRP-USDT-SWAP | 1.3107 | 1.3148/1.3060 | 1.3155 | res 1.2983 (ha 7 candles) | 0.01415 | 0.0100% | B/compra@1.2723 (0t/4c) | zona_mapeada_setup_B |
| 2026-11-04 15:06 | DOGE-USDT-SWAP | 0.07672 | 0.07759/0.07643 | 0.07729 | sup 0.07433 (ha 5 candles) | 0.00089 | 0.0091% | — | invalidado_setup_B |
| 2026-11-04 15:06 | ARB-USDT-SWAP | 0.16456 | 0.16683/0.16321 | 0.16840 | — | 0.00328 | 0.0069% | B/compra@0.16447 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-04 15:06 | WLD-USDT-SWAP | 0.37990 | 0.39310/0.36670 | 0.39220 | sup 0.37610 (ha 5 candles) | 0.01014 | -0.0101% | — | sem_zona |
| 2026-11-04 15:06 | SUI-USDT-SWAP | 0.93590 | 0.94580/0.92900 | 0.94290 | — | 0.01506 | 0.0100% | B/compra@0.93870 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-04 15:06 | UNI-USDT-SWAP | 7.6550 | 7.7060/7.5670 | 7.6710 | res 7.5550 (ha 9 candles) | 0.14757 | 0.0100% | A/compra@7.5550 (1t/0c) | zona_mapeada_setup_A |
| 2026-11-04 15:06 | LINK-USDT-SWAP | 11.54 | 11.63/11.48 | 11.60 | sup 11.04 (ha 5 candles) | 0.16686 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-11-04 16:06 | BTC-USDT-SWAP | 80319.4 | 80680.0/80261.1 | 80273.5 | sup 77976.0 (ha 6 candles) | 599.03 | 0.0075% | — | confirmado_calibracao_setup_B |
| 2026-11-04 16:06 | ETH-USDT-SWAP | 2422.4 | 2436.2/2419.0 | 2425.8 | sup 2308.5 (ha 6 candles) | 25.65 | 0.0100% | — | sem_zona |
| 2026-11-04 16:06 | SOL-USDT-SWAP | 95.22 | 96.08/95.07 | 96.65 | sup 92.42 (ha 6 candles) | 1.1514 | 0.0100% | B/venda@95.89 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-04 16:06 | XRP-USDT-SWAP | 1.3056 | 1.3172/1.3032 | 1.3155 | res 1.3421 (ha 3 candles) | 0.01401 | 0.0100% | B/compra@1.2723 (0t/5c) | zona_mapeada_setup_B |
| 2026-11-04 16:06 | DOGE-USDT-SWAP | 0.07665 | 0.07716/0.07646 | 0.07729 | sup 0.07433 (ha 6 candles) | 0.00086 | 0.0088% | — | sem_zona |
| 2026-11-04 16:06 | ARB-USDT-SWAP | 0.16252 | 0.16598/0.16200 | 0.16840 | — | 0.00327 | 0.0001% | — | invalidado_setup_B |
| 2026-11-04 16:06 | WLD-USDT-SWAP | 0.37700 | 0.38390/0.37520 | 0.39220 | sup 0.37610 (ha 6 candles) | 0.01009 | -0.0150% | — | sem_zona |
| 2026-11-04 16:06 | SUI-USDT-SWAP | 0.92940 | 0.94130/0.92750 | 0.94290 | — | 0.01494 | 0.0100% | — | invalidado_setup_B |
| 2026-11-04 16:06 | UNI-USDT-SWAP | 7.6220 | 7.7210/7.6150 | 7.6710 | res 7.5550 (ha 10 candles) | 0.14307 | 0.0100% | A/compra@7.5550 (1t/1c) | zona_mapeada_setup_A |
| 2026-11-04 16:06 | LINK-USDT-SWAP | 11.48 | 11.59/11.44 | 11.60 | sup 11.04 (ha 6 candles) | 0.16171 | 0.0088% | B/venda@11.55 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-04 17:06 | BTC-USDT-SWAP | 79951.6 | 80374.6/79903.1 | 79951.6 | sup 77976.0 (ha 7 candles) | 565.72 | 0.0081% | — | sem_zona |
| 2026-11-04 17:06 | ETH-USDT-SWAP | 2405.2 | 2428.1/2404.3 | 2405.2 | sup 2308.5 (ha 7 candles) | 25.10 | 0.0100% | B/venda@2391.2 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-04 17:06 | SOL-USDT-SWAP | 94.47 | 95.51/94.40 | 94.47 | sup 92.42 (ha 7 candles) | 1.1386 | 0.0100% | B/venda@95.89 (0t/1c) | zona_mapeada_setup_B |
| 2026-11-04 17:06 | XRP-USDT-SWAP | 1.2989 | 1.3077/1.2977 | 1.2989 | res 1.3421 (ha 4 candles) | 0.01369 | 0.0100% | B/compra@1.2723 (0t/6c) | zona_mapeada_setup_B |
| 2026-11-04 17:06 | DOGE-USDT-SWAP | 0.07645 | 0.07691/0.07625 | 0.07645 | sup 0.07433 (ha 7 candles) | 0.00083 | 0.0100% | — | sem_zona |
| 2026-11-04 17:06 | ARB-USDT-SWAP | 0.16082 | 0.16276/0.16060 | 0.16082 | — | 0.00315 | -0.0048% | B/compra@0.15961 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-04 17:06 | WLD-USDT-SWAP | 0.37350 | 0.37880/0.37290 | 0.37350 | sup 0.37610 (ha 7 candles) | 0.00954 | -0.0185% | A/venda@0.37610 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-04 17:06 | SUI-USDT-SWAP | 0.92090 | 0.93200/0.91980 | 0.92090 | — | 0.01469 | 0.0100% | B/venda@0.91360 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-04 17:06 | UNI-USDT-SWAP | 7.5450 | 7.6520/7.5370 | 7.5450 | res 7.7860 (ha 3 candles) | 0.13829 | 0.0100% | A/compra@7.5550 (2t/0c) | zona_mapeada_setup_A |
| 2026-11-04 17:06 | LINK-USDT-SWAP | 11.35 | 11.52/11.33 | 11.35 | sup 11.04 (ha 7 candles) | 0.16171 | 0.0081% | — | descartado_rr_baixo_setup_B |
| 2026-11-04 18:06 | BTC-USDT-SWAP | 80105.0 | 80329.8/79914.9 | 79951.6 | sup 77976.0 (ha 8 candles) | 571.89 | 0.0085% | — | sem_zona |
| 2026-11-04 18:06 | ETH-USDT-SWAP | 2420.2 | 2423.1/2404.0 | 2405.2 | sup 2308.5 (ha 8 candles) | 25.56 | 0.0100% | B/venda@2391.2 (0t/1c) | zona_mapeada_setup_B |
| 2026-11-04 18:06 | SOL-USDT-SWAP | 94.81 | 95.12/94.28 | 94.47 | sup 92.42 (ha 8 candles) | 1.1579 | 0.0100% | B/venda@95.89 (0t/2c) | zona_mapeada_setup_B |
| 2026-11-04 18:06 | XRP-USDT-SWAP | 1.3035 | 1.3073/1.2967 | 1.2989 | res 1.3421 (ha 5 candles) | 0.01408 | 0.0100% | B/compra@1.2723 (0t/7c) | zona_mapeada_setup_B |
| 2026-11-04 18:06 | DOGE-USDT-SWAP | 0.07675 | 0.07704/0.07630 | 0.07645 | sup 0.07433 (ha 8 candles) | 0.00086 | 0.0100% | — | sem_zona |
| 2026-11-04 18:06 | ARB-USDT-SWAP | 0.16281 | 0.16356/0.16014 | 0.16082 | — | 0.00326 | -0.0052% | — | descartado_rr_baixo_setup_B |
| 2026-11-04 18:06 | WLD-USDT-SWAP | 0.37630 | 0.37830/0.37070 | 0.37350 | sup 0.36670 (ha 3 candles) | 0.00973 | -0.0232% | A/venda@0.37610 (1t/0c) | zona_mapeada_setup_A |
| 2026-11-04 18:06 | SUI-USDT-SWAP | 0.92480 | 0.92760/0.91580 | 0.92090 | — | 0.01476 | 0.0100% | — | invalidado_setup_B |
| 2026-11-04 18:06 | UNI-USDT-SWAP | 7.6070 | 7.6310/7.5280 | 7.5450 | res 7.7860 (ha 4 candles) | 0.13700 | 0.0100% | — | descartado_rr_baixo_setup_A |
| 2026-11-04 18:06 | LINK-USDT-SWAP | 11.42 | 11.45/11.32 | 11.35 | sup 11.04 (ha 8 candles) | 0.16336 | 0.0079% | — | sem_zona |
| 2026-11-04 19:06 | BTC-USDT-SWAP | 80201.4 | 80292.6/80054.8 | 79951.6 | sup 77976.0 (ha 9 candles) | 554.04 | 0.0085% | — | sem_zona |
| 2026-11-04 19:06 | ETH-USDT-SWAP | 2417.2 | 2427.0/2414.4 | 2405.2 | sup 2308.5 (ha 9 candles) | 25.11 | 0.0097% | B/venda@2391.2 (0t/2c) | zona_mapeada_setup_B |
| 2026-11-04 19:06 | SOL-USDT-SWAP | 94.75 | 95.02/94.47 | 94.47 | sup 92.42 (ha 9 candles) | 1.1479 | 0.0100% | B/venda@95.89 (0t/3c) | zona_mapeada_setup_B |
| 2026-11-04 19:06 | XRP-USDT-SWAP | 1.3037 | 1.3052/1.3010 | 1.2989 | res 1.3421 (ha 6 candles) | 0.01386 | 0.0100% | — | zona_expirada_setup_B |
| 2026-11-04 19:06 | DOGE-USDT-SWAP | 0.07679 | 0.07690/0.07652 | 0.07645 | sup 0.07433 (ha 9 candles) | 0.00084 | 0.0100% | — | sem_zona |
| 2026-11-04 19:06 | ARB-USDT-SWAP | 0.16259 | 0.16338/0.16194 | 0.16082 | — | 0.00320 | -0.0074% | B/compra@0.16224 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-04 19:06 | WLD-USDT-SWAP | 0.37750 | 0.37850/0.37450 | 0.37350 | sup 0.36670 (ha 4 candles) | 0.00890 | -0.0242% | A/venda@0.37610 (2t/0c) | zona_mapeada_setup_A |
| 2026-11-04 19:06 | SUI-USDT-SWAP | 0.92130 | 0.92700/0.91690 | 0.92090 | — | 0.01451 | 0.0100% | B/venda@0.93080 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-04 19:06 | UNI-USDT-SWAP | 7.6370 | 7.6460/7.5480 | 7.5450 | res 7.7860 (ha 5 candles) | 0.12807 | 0.0100% | — | sem_zona |
| 2026-11-04 19:06 | LINK-USDT-SWAP | 11.42 | 11.47/11.36 | 11.35 | sup 11.04 (ha 9 candles) | 0.16007 | 0.0083% | — | sem_zona |
| 2026-11-04 20:06 | BTC-USDT-SWAP | 80688.8 | 80941.0/80189.8 | 79951.6 | sup 79903.1 (ha 3 candles) | 580.22 | 0.0083% | B/venda@81008.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-04 20:06 | ETH-USDT-SWAP | 2435.3 | 2444.4/2416.4 | 2405.2 | sup 2308.5 (ha 10 candles) | 25.22 | 0.0083% | B/venda@2391.2 (0t/3c) | zona_mapeada_setup_B |
| 2026-11-04 20:06 | SOL-USDT-SWAP | 95.95 | 96.24/94.72 | 94.47 | sup 92.42 (ha 10 candles) | 1.2143 | 0.0093% | B/venda@95.89 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-04 20:06 | XRP-USDT-SWAP | 1.3114 | 1.3150/1.3031 | 1.2989 | res 1.3421 (ha 7 candles) | 0.01394 | 0.0100% | — | sem_zona |
| 2026-11-04 20:06 | DOGE-USDT-SWAP | 0.07749 | 0.07771/0.07676 | 0.07645 | sup 0.07625 (ha 3 candles) | 0.00086 | 0.0100% | B/venda@0.07803 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-04 20:06 | ARB-USDT-SWAP | 0.16414 | 0.16605/0.16228 | 0.16082 | — | 0.00329 | -0.0092% | B/compra@0.16224 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-04 20:06 | WLD-USDT-SWAP | 0.38090 | 0.38390/0.37720 | 0.37350 | sup 0.36670 (ha 5 candles) | 0.00903 | -0.0204% | — | invalidado_setup_A |
| 2026-11-04 20:06 | SUI-USDT-SWAP | 0.93760 | 0.94080/0.92000 | 0.92090 | — | 0.01488 | 0.0100% | — | invalidado_setup_B |
| 2026-11-04 20:06 | UNI-USDT-SWAP | 7.7940 | 7.8120/7.6310 | 7.5450 | res 7.7860 (ha 6 candles) | 0.13414 | 0.0100% | A/compra@7.7860 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-04 20:06 | LINK-USDT-SWAP | 11.55 | 11.60/11.41 | 11.35 | sup 11.04 (ha 10 candles) | 0.16414 | 0.0100% | B/venda@11.62 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-04 21:06 | BTC-USDT-SWAP | 80466.1 | 80709.7/80343.3 | 80466.1 | sup 79903.1 (ha 4 candles) | 587.00 | 0.0075% | B/venda@81008.0 (0t/1c) | zona_mapeada_setup_B |
| 2026-11-04 21:06 | ETH-USDT-SWAP | 2423.4 | 2435.3/2422.7 | 2423.4 | sup 2404.0 (ha 3 candles) | 25.45 | 0.0073% | B/venda@2391.2 (0t/4c) | zona_mapeada_setup_B |
| 2026-11-04 21:06 | SOL-USDT-SWAP | 95.55 | 96.00/95.32 | 95.55 | sup 94.28 (ha 3 candles) | 1.2314 | 0.0076% | — | descartado_rr_baixo_setup_B |
| 2026-11-04 21:06 | XRP-USDT-SWAP | 1.3050 | 1.3114/1.3041 | 1.3050 | res 1.3421 (ha 8 candles) | 0.01391 | 0.0100% | — | sem_zona |
| 2026-11-04 21:06 | DOGE-USDT-SWAP | 0.07704 | 0.07749/0.07699 | 0.07704 | sup 0.07625 (ha 4 candles) | 0.00087 | 0.0100% | B/venda@0.07803 (0t/1c) | zona_mapeada_setup_B |
| 2026-11-04 21:06 | ARB-USDT-SWAP | 0.16230 | 0.16414/0.16224 | 0.16230 | — | 0.00328 | -0.0128% | B/compra@0.16224 (2t/0c) | zona_mapeada_setup_B |
| 2026-11-04 21:06 | WLD-USDT-SWAP | 0.37470 | 0.38100/0.37420 | 0.37470 | sup 0.36670 (ha 6 candles) | 0.00908 | -0.0199% | — | sem_zona |
| 2026-11-04 21:06 | SUI-USDT-SWAP | 0.92860 | 0.93870/0.92830 | 0.92860 | — | 0.01507 | 0.0100% | — | sem_zona |
| 2026-11-04 21:06 | UNI-USDT-SWAP | 7.6250 | 7.8190/7.6220 | 7.6250 | res 7.7860 (ha 7 candles) | 0.14364 | 0.0100% | — | invalidado_setup_A |
| 2026-11-04 21:06 | LINK-USDT-SWAP | 11.44 | 11.55/11.44 | 11.44 | sup 11.32 (ha 3 candles) | 0.16629 | 0.0100% | B/venda@11.62 (0t/1c) | zona_mapeada_setup_B |
| 2026-11-04 22:06 | BTC-USDT-SWAP | 80517.4 | 80820.2/80450.0 | 80466.1 | sup 79903.1 (ha 5 candles) | 588.94 | 0.0075% | B/venda@81008.0 (0t/2c) | zona_mapeada_setup_B |
| 2026-11-04 22:06 | ETH-USDT-SWAP | 2420.0 | 2431.6/2418.2 | 2423.4 | sup 2404.0 (ha 4 candles) | 25.36 | 0.0067% | B/venda@2391.2 (0t/5c) | zona_mapeada_setup_B |
| 2026-11-04 22:06 | SOL-USDT-SWAP | 95.68 | 96.21/95.31 | 95.55 | sup 94.28 (ha 4 candles) | 1.2386 | 0.0072% | — | sem_zona |
| 2026-11-04 22:06 | XRP-USDT-SWAP | 1.3026 | 1.3094/1.3026 | 1.3050 | res 1.3421 (ha 9 candles) | 0.01316 | 0.0100% | B/compra@1.2943 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-04 22:06 | DOGE-USDT-SWAP | 0.07691 | 0.07721/0.07688 | 0.07704 | sup 0.07625 (ha 5 candles) | 0.00087 | 0.0100% | B/venda@0.07803 (0t/2c) | zona_mapeada_setup_B |
| 2026-11-04 22:06 | ARB-USDT-SWAP | 0.16265 | 0.16363/0.16136 | 0.16230 | — | 0.00332 | -0.0131% | — | zona_expirada_setup_B |
| 2026-11-04 22:06 | WLD-USDT-SWAP | 0.37620 | 0.38100/0.37350 | 0.37470 | sup 0.36670 (ha 7 candles) | 0.00935 | -0.0229% | — | sem_zona |
| 2026-11-04 22:06 | SUI-USDT-SWAP | 0.92970 | 0.93570/0.92630 | 0.92860 | — | 0.01503 | 0.0084% | — | sem_zona |
| 2026-11-04 22:06 | UNI-USDT-SWAP | 7.6660 | 7.7490/7.6140 | 7.6250 | res 7.7860 (ha 8 candles) | 0.14779 | 0.0100% | — | sem_zona |
| 2026-11-04 22:06 | LINK-USDT-SWAP | 11.39 | 11.50/11.39 | 11.44 | sup 11.32 (ha 4 candles) | 0.16579 | 0.0100% | B/venda@11.62 (0t/2c) | zona_mapeada_setup_B |
| 2026-11-04 23:06 | BTC-USDT-SWAP | 80645.8 | 80886.4/80215.0 | 80466.1 | sup 79903.1 (ha 6 candles) | 617.91 | 0.0077% | B/venda@81008.0 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-04 23:06 | ETH-USDT-SWAP | 2428.6 | 2434.9/2406.1 | 2423.4 | sup 2404.0 (ha 5 candles) | 26.43 | 0.0056% | B/venda@2391.2 (0t/6c) | zona_mapeada_setup_B |
| 2026-11-04 23:06 | SOL-USDT-SWAP | 95.99 | 96.40/95.08 | 95.55 | sup 94.28 (ha 5 candles) | 1.2821 | 0.0046% | B/venda@96.94 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-04 23:06 | XRP-USDT-SWAP | 1.3078 | 1.3107/1.2965 | 1.3050 | res 1.3150 (ha 3 candles) | 0.01356 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-11-04 23:06 | DOGE-USDT-SWAP | 0.07705 | 0.07729/0.07647 | 0.07704 | sup 0.07625 (ha 6 candles) | 0.00089 | 0.0100% | B/venda@0.07803 (0t/3c) | zona_mapeada_setup_B |
| 2026-11-04 23:06 | ARB-USDT-SWAP | 0.16304 | 0.16432/0.16131 | 0.16230 | — | 0.00336 | -0.0138% | B/compra@0.16325 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-04 23:06 | WLD-USDT-SWAP | 0.37430 | 0.37850/0.37070 | 0.37470 | sup 0.36670 (ha 8 candles) | 0.00943 | -0.0239% | — | sem_zona |
| 2026-11-04 23:06 | SUI-USDT-SWAP | 0.92850 | 0.93470/0.92100 | 0.92860 | — | 0.01546 | 0.0054% | — | sem_zona |
| 2026-11-04 23:06 | UNI-USDT-SWAP | 7.6310 | 7.6870/7.5980 | 7.6250 | res 7.7860 (ha 9 candles) | 0.14793 | 0.0100% | — | sem_zona |
| 2026-11-04 23:06 | LINK-USDT-SWAP | 11.44 | 11.49/11.32 | 11.44 | sup 11.32 (ha 5 candles) | 0.17293 | 0.0100% | B/venda@11.62 (0t/3c) | zona_mapeada_setup_B |
| 2026-11-05 00:06 | BTC-USDT-SWAP | 80541.2 | 80832.9/80521.7 | 80466.1 | sup 79903.1 (ha 7 candles) | 605.12 | 0.0097% | B/venda@81008.0 (1t/1c) | zona_mapeada_setup_B |
| 2026-11-05 00:06 | ETH-USDT-SWAP | 2428.4 | 2434.8/2423.5 | 2423.4 | sup 2404.0 (ha 6 candles) | 25.82 | 0.0052% | B/venda@2391.2 (0t/7c) | zona_mapeada_setup_B |
| 2026-11-05 00:06 | SOL-USDT-SWAP | 96.33 | 96.60/95.85 | 95.55 | sup 94.28 (ha 6 candles) | 1.2493 | 0.0026% | B/venda@96.94 (0t/1c) | zona_mapeada_setup_B |
| 2026-11-05 00:06 | XRP-USDT-SWAP | 1.3064 | 1.3106/1.3042 | 1.3050 | res 1.3150 (ha 4 candles) | 0.01309 | 0.0100% | — | sem_zona |
| 2026-11-05 00:06 | DOGE-USDT-SWAP | 0.07714 | 0.07730/0.07694 | 0.07704 | sup 0.07625 (ha 7 candles) | 0.00085 | 0.0100% | B/venda@0.07803 (0t/4c) | zona_mapeada_setup_B |
| 2026-11-05 00:06 | ARB-USDT-SWAP | 0.16364 | 0.16420/0.16277 | 0.16230 | — | 0.00327 | -0.0122% | — | descartado_rr_baixo_setup_B |
| 2026-11-05 00:06 | WLD-USDT-SWAP | 0.37830 | 0.37970/0.37290 | 0.37470 | sup 0.36670 (ha 9 candles) | 0.00915 | -0.0219% | — | sem_zona |
| 2026-11-05 00:06 | SUI-USDT-SWAP | 0.92870 | 0.93180/0.92550 | 0.92860 | — | 0.01494 | 0.0030% | B/compra@0.93870 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-05 00:06 | UNI-USDT-SWAP | 7.6530 | 7.6930/7.6230 | 7.6250 | res 7.8190 (ha 3 candles) | 0.14164 | 0.0100% | — | sem_zona |
| 2026-11-05 00:06 | LINK-USDT-SWAP | 11.48 | 11.51/11.42 | 11.44 | sup 11.32 (ha 6 candles) | 0.17036 | 0.0093% | B/venda@11.62 (0t/4c) | zona_mapeada_setup_B |
| 2026-11-05 01:06 | BTC-USDT-SWAP | 80517.9 | 80810.0/80499.0 | 80517.9 | — | 608.79 | 0.0100% | B/venda@81008.0 (1t/2c) | zona_mapeada_setup_B |
| 2026-11-05 01:06 | ETH-USDT-SWAP | 2423.5 | 2435.9/2423.0 | 2423.5 | — | 26.14 | 0.0046% | — | zona_expirada_setup_B |
| 2026-11-05 01:06 | SOL-USDT-SWAP | 96.22 | 97.06/96.12 | 96.22 | — | 1.2764 | 0.0012% | — | descartado_rr_baixo_setup_B |
| 2026-11-05 01:06 | XRP-USDT-SWAP | 1.3090 | 1.3162/1.3054 | 1.3090 | res 1.3150 (ha 5 candles) | 0.01333 | 0.0100% | — | sem_zona |
| 2026-11-05 01:06 | DOGE-USDT-SWAP | 0.07691 | 0.07744/0.07690 | 0.07691 | — | 0.00086 | 0.0100% | B/venda@0.07803 (0t/5c) | zona_mapeada_setup_B |
| 2026-11-05 01:06 | ARB-USDT-SWAP | 0.16351 | 0.16537/0.16325 | 0.16351 | res 0.16605 (ha 5 candles) | 0.00330 | -0.0121% | B/compra@0.16224 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-05 01:06 | WLD-USDT-SWAP | 0.37460 | 0.38050/0.37460 | 0.37460 | sup 0.36670 (ha 10 candles) | 0.00911 | -0.0202% | — | sem_zona |
| 2026-11-05 01:06 | SUI-USDT-SWAP | 0.93100 | 0.93920/0.92660 | 0.93100 | — | 0.01540 | 0.0006% | — | invalidado_setup_B |
| 2026-11-05 01:06 | UNI-USDT-SWAP | 7.7080 | 7.8170/7.6320 | 7.7080 | res 7.8190 (ha 4 candles) | 0.14979 | 0.0100% | — | sem_zona |
| 2026-11-05 01:06 | LINK-USDT-SWAP | 11.54 | 11.64/11.45 | 11.54 | — | 0.17736 | 0.0093% | B/venda@11.62 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-05 02:06 | BTC-USDT-SWAP | 80488.3 | 80709.0/80335.6 | 80517.9 | — | 529.36 | 0.0100% | B/venda@81008.0 (1t/3c) | zona_mapeada_setup_B |
| 2026-11-05 02:06 | ETH-USDT-SWAP | 2423.6 | 2431.4/2417.3 | 2423.5 | — | 21.69 | 0.0049% | B/venda@2417.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-05 02:06 | SOL-USDT-SWAP | 96.00 | 96.50/95.83 | 96.22 | — | 1.1050 | 0.0019% | B/venda@95.89 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-05 02:06 | XRP-USDT-SWAP | 1.3083 | 1.3139/1.3044 | 1.3090 | res 1.3150 (ha 6 candles) | 0.01119 | 0.0100% | — | sem_zona |
| 2026-11-05 02:06 | DOGE-USDT-SWAP | 0.07682 | 0.07714/0.07665 | 0.07691 | — | 0.00072 | 0.0100% | B/venda@0.07803 (0t/6c) | zona_mapeada_setup_B |
| 2026-11-05 02:06 | ARB-USDT-SWAP | 0.16381 | 0.16439/0.16266 | 0.16351 | res 0.16605 (ha 6 candles) | 0.00288 | -0.0130% | — | descartado_rr_baixo_setup_B |
| 2026-11-05 02:06 | WLD-USDT-SWAP | 0.37430 | 0.37700/0.37210 | 0.37460 | sup 0.37070 (ha 3 candles) | 0.00844 | -0.0202% | — | sem_zona |
| 2026-11-05 02:06 | SUI-USDT-SWAP | 0.92890 | 0.93410/0.92630 | 0.93100 | — | 0.01316 | 0.0007% | — | sem_zona |
| 2026-11-05 02:06 | UNI-USDT-SWAP | 7.6660 | 7.7520/7.6530 | 7.7080 | res 7.8190 (ha 5 candles) | 0.13557 | 0.0100% | — | sem_zona |
| 2026-11-05 02:06 | LINK-USDT-SWAP | 11.56 | 11.61/11.50 | 11.54 | — | 0.15064 | 0.0095% | B/venda@11.62 (2t/0c) | zona_mapeada_setup_B |
| 2026-11-05 03:06 | BTC-USDT-SWAP | 80371.0 | 80587.3/80353.0 | 80517.9 | — | 408.25 | 0.0100% | B/venda@81008.0 (1t/4c) | zona_mapeada_setup_B |
| 2026-11-05 03:06 | ETH-USDT-SWAP | 2418.0 | 2428.2/2418.0 | 2423.5 | — | 17.15 | 0.0047% | — | descartado_rr_baixo_setup_B |
| 2026-11-05 03:06 | SOL-USDT-SWAP | 95.70 | 96.30/95.63 | 96.22 | — | 0.93643 | 0.0027% | — | descartado_rr_baixo_setup_B |
| 2026-11-05 03:06 | XRP-USDT-SWAP | 1.3059 | 1.3122/1.3049 | 1.3090 | res 1.3150 (ha 7 candles) | 0.00962 | 0.0100% | — | sem_zona |
| 2026-11-05 03:06 | DOGE-USDT-SWAP | 0.07645 | 0.07683/0.07634 | 0.07691 | — | 0.00063 | 0.0100% | B/venda@0.07803 (0t/7c) | zona_mapeada_setup_B |
| 2026-11-05 03:06 | ARB-USDT-SWAP | 0.16297 | 0.16405/0.16248 | 0.16351 | res 0.16605 (ha 7 candles) | 0.00256 | -0.0126% | B/compra@0.16325 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-05 03:06 | WLD-USDT-SWAP | 0.37350 | 0.37620/0.37160 | 0.37460 | sup 0.37070 (ha 4 candles) | 0.00790 | -0.0212% | — | sem_zona |
| 2026-11-05 03:06 | SUI-USDT-SWAP | 0.92120 | 0.92960/0.92050 | 0.93100 | — | 0.01189 | 0.0027% | B/venda@0.91360 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-05 03:06 | UNI-USDT-SWAP | 7.5610 | 7.6670/7.5570 | 7.7080 | res 7.8190 (ha 6 candles) | 0.12729 | 0.0100% | — | sem_zona |
| 2026-11-05 03:06 | LINK-USDT-SWAP | 11.50 | 11.58/11.50 | 11.54 | — | 0.13814 | 0.0090% | B/venda@11.62 (2t/1c) | zona_mapeada_setup_B |
| 2026-11-05 04:06 | BTC-USDT-SWAP | 80624.8 | 80684.4/80346.0 | 80517.9 | — | 401.56 | 0.0100% | B/venda@81008.0 (1t/5c) | zona_mapeada_setup_B |
| 2026-11-05 04:06 | ETH-USDT-SWAP | 2429.0 | 2432.0/2416.8 | 2423.5 | — | 16.79 | 0.0044% | — | sem_zona |
| 2026-11-05 04:06 | SOL-USDT-SWAP | 96.18 | 96.30/95.58 | 96.22 | — | 0.92357 | 0.0018% | — | sem_zona |
| 2026-11-05 04:06 | XRP-USDT-SWAP | 1.3107 | 1.3116/1.3048 | 1.3090 | res 1.3162 (ha 3 candles) | 0.00919 | 0.0100% | — | sem_zona |
| 2026-11-05 04:06 | DOGE-USDT-SWAP | 0.07656 | 0.07672/0.07633 | 0.07691 | — | 0.00061 | 0.0100% | — | zona_expirada_setup_B |
| 2026-11-05 04:06 | ARB-USDT-SWAP | 0.16410 | 0.16466/0.16224 | 0.16351 | res 0.16537 (ha 3 candles) | 0.00249 | -0.0105% | — | descartado_rr_baixo_setup_B |
| 2026-11-05 04:06 | WLD-USDT-SWAP | 0.37660 | 0.37870/0.37280 | 0.37460 | sup 0.37070 (ha 5 candles) | 0.00782 | -0.0207% | — | sem_zona |
| 2026-11-05 04:06 | SUI-USDT-SWAP | 0.92560 | 0.92800/0.91920 | 0.93100 | — | 0.01169 | 0.0037% | B/venda@0.91360 (0t/1c) | zona_mapeada_setup_B |
| 2026-11-05 04:06 | UNI-USDT-SWAP | 7.6630 | 7.6960/7.5420 | 7.7080 | res 7.8170 (ha 3 candles) | 0.12721 | 0.0100% | — | sem_zona |
| 2026-11-05 04:06 | LINK-USDT-SWAP | 11.53 | 11.58/11.47 | 11.54 | — | 0.13443 | 0.0094% | B/venda@11.62 (2t/2c) | zona_mapeada_setup_B |
| 2026-11-05 05:06 | BTC-USDT-SWAP | 80363.7 | 80755.5/80291.9 | 80363.7 | — | 409.59 | 0.0100% | B/venda@81008.0 (1t/6c) | zona_mapeada_setup_B |
| 2026-11-05 05:06 | ETH-USDT-SWAP | 2416.0 | 2433.9/2411.5 | 2416.0 | — | 17.25 | 0.0079% | — | sem_zona |
| 2026-11-05 05:06 | SOL-USDT-SWAP | 95.84 | 96.42/95.66 | 95.84 | — | 0.88857 | 0.0018% | — | sem_zona |
| 2026-11-05 05:06 | XRP-USDT-SWAP | 1.3137 | 1.3148/1.3079 | 1.3137 | res 1.3162 (ha 4 candles) | 0.00905 | 0.0100% | — | sem_zona |
| 2026-11-05 05:06 | DOGE-USDT-SWAP | 0.07640 | 0.07669/0.07623 | 0.07640 | — | 0.00056 | 0.0100% | B/venda@0.07630 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-05 05:06 | ARB-USDT-SWAP | 0.16306 | 0.16453/0.16277 | 0.16306 | res 0.16537 (ha 4 candles) | 0.00236 | -0.0084% | B/compra@0.16224 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-05 05:06 | WLD-USDT-SWAP | 0.37460 | 0.37810/0.37310 | 0.37460 | — | 0.00629 | -0.0214% | — | sem_zona |
| 2026-11-05 05:06 | SUI-USDT-SWAP | 0.92120 | 0.92840/0.91900 | 0.92120 | — | 0.01116 | 0.0047% | B/venda@0.91360 (0t/2c) | zona_mapeada_setup_B |
| 2026-11-05 05:06 | UNI-USDT-SWAP | 7.5850 | 7.6880/7.5710 | 7.5850 | res 7.8170 (ha 4 candles) | 0.12564 | 0.0100% | — | sem_zona |
| 2026-11-05 05:06 | LINK-USDT-SWAP | 11.53 | 11.58/11.47 | 11.53 | — | 0.13121 | 0.0096% | B/venda@11.62 (2t/3c) | zona_mapeada_setup_B |
| 2026-11-05 06:06 | BTC-USDT-SWAP | 80499.9 | 80624.4/80353.1 | 80363.7 | — | 399.04 | 0.0100% | B/venda@81008.0 (1t/7c) | zona_mapeada_setup_B |
| 2026-11-05 06:06 | ETH-USDT-SWAP | 2420.0 | 2426.6/2415.4 | 2416.0 | — | 16.82 | 0.0100% | — | sem_zona |
| 2026-11-05 06:06 | SOL-USDT-SWAP | 96.76 | 97.04/95.72 | 95.84 | — | 0.91071 | 0.0032% | B/venda@96.94 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-05 06:06 | XRP-USDT-SWAP | 1.3244 | 1.3268/1.3128 | 1.3137 | res 1.3162 (ha 5 candles) | 0.00905 | 0.0100% | A/compra@1.3162 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-05 06:06 | DOGE-USDT-SWAP | 0.07707 | 0.07709/0.07632 | 0.07640 | — | 0.00056 | 0.0100% | — | invalidado_setup_B |
| 2026-11-05 06:06 | ARB-USDT-SWAP | 0.16552 | 0.16555/0.16277 | 0.16306 | res 0.16537 (ha 5 candles) | 0.00227 | -0.0079% | — | descartado_rr_baixo_setup_B |
| 2026-11-05 06:06 | WLD-USDT-SWAP | 0.38020 | 0.38220/0.37360 | 0.37460 | — | 0.00629 | -0.0184% | — | sem_zona |
| 2026-11-05 06:06 | SUI-USDT-SWAP | 0.93230 | 0.93310/0.91990 | 0.92120 | — | 0.01111 | 0.0089% | B/venda@0.91360 (0t/3c) | zona_mapeada_setup_B |
| 2026-11-05 06:06 | UNI-USDT-SWAP | 7.6330 | 7.6580/7.5700 | 7.5850 | res 7.8170 (ha 5 candles) | 0.12436 | 0.0100% | — | sem_zona |
| 2026-11-05 06:06 | LINK-USDT-SWAP | 11.62 | 11.65/11.51 | 11.53 | — | 0.13014 | 0.0100% | — | zona_expirada_setup_B |
| 2026-11-05 07:06 | BTC-USDT-SWAP | 80444.9 | 80499.9/80262.5 | 80363.7 | — | 382.32 | 0.0100% | — | zona_expirada_setup_B |
| 2026-11-05 07:06 | ETH-USDT-SWAP | 2419.8 | 2420.5/2411.8 | 2416.0 | — | 15.75 | 0.0100% | — | sem_zona |
| 2026-11-05 07:06 | SOL-USDT-SWAP | 96.82 | 96.86/96.36 | 95.84 | — | 0.86714 | 0.0050% | B/venda@96.94 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-05 07:06 | XRP-USDT-SWAP | 1.3199 | 1.3248/1.3138 | 1.3137 | res 1.3162 (ha 6 candles) | 0.00912 | 0.0100% | A/compra@1.3162 (1t/0c) | zona_mapeada_setup_A |
| 2026-11-05 07:06 | DOGE-USDT-SWAP | 0.07707 | 0.07714/0.07676 | 0.07640 | — | 0.00054 | 0.0100% | B/compra@0.07737 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-05 07:06 | ARB-USDT-SWAP | 0.16522 | 0.16575/0.16458 | 0.16306 | res 0.16537 (ha 6 candles) | 0.00220 | -0.0045% | B/compra@0.16447 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-05 07:06 | WLD-USDT-SWAP | 0.37800 | 0.38030/0.37590 | 0.37460 | — | 0.00618 | -0.0142% | — | sem_zona |
| 2026-11-05 07:06 | SUI-USDT-SWAP | 0.93130 | 0.93390/0.92670 | 0.92120 | — | 0.01076 | 0.0100% | B/venda@0.91360 (0t/4c) | zona_mapeada_setup_B |
| 2026-11-05 07:06 | UNI-USDT-SWAP | 7.5870 | 7.6360/7.5600 | 7.5850 | res 7.8170 (ha 6 candles) | 0.12157 | 0.0100% | — | sem_zona |
| 2026-11-05 07:06 | LINK-USDT-SWAP | 11.60 | 11.63/11.52 | 11.53 | — | 0.12479 | 0.0100% | B/venda@11.55 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-05 08:06 | BTC-USDT-SWAP | 80284.8 | 80519.3/80234.8 | 80363.7 | — | 373.01 | 0.0100% | — | sem_zona |
| 2026-11-05 08:06 | ETH-USDT-SWAP | 2418.2 | 2421.0/2414.7 | 2416.0 | — | 14.84 | 0.0100% | — | sem_zona |
| 2026-11-05 08:06 | SOL-USDT-SWAP | 96.57 | 96.93/96.43 | 95.84 | — | 0.84286 | 0.0061% | — | confirmado_calibracao_setup_B |
| 2026-11-05 08:06 | XRP-USDT-SWAP | 1.3183 | 1.3208/1.3163 | 1.3137 | res 1.3162 (ha 7 candles) | 0.00869 | 0.0100% | A/compra@1.3162 (2t/0c) | zona_mapeada_setup_A |
| 2026-11-05 08:06 | DOGE-USDT-SWAP | 0.07683 | 0.07713/0.07681 | 0.07640 | — | 0.00051 | 0.0100% | B/compra@0.07737 (0t/1c) | zona_mapeada_setup_B |
| 2026-11-05 08:06 | ARB-USDT-SWAP | 0.16351 | 0.16523/0.16329 | 0.16306 | res 0.16537 (ha 7 candles) | 0.00209 | -0.0026% | — | invalidado_setup_B |
| 2026-11-05 08:06 | WLD-USDT-SWAP | 0.37420 | 0.37830/0.37290 | 0.37460 | — | 0.00602 | -0.0140% | — | sem_zona |
| 2026-11-05 08:06 | SUI-USDT-SWAP | 0.92280 | 0.93140/0.92200 | 0.92120 | — | 0.01059 | 0.0100% | B/venda@0.91360 (0t/5c) | zona_mapeada_setup_B |
| 2026-11-05 08:06 | UNI-USDT-SWAP | 7.4560 | 7.5880/7.4510 | 7.5850 | res 7.8170 (ha 7 candles) | 0.12400 | 0.0100% | — | sem_zona |
| 2026-11-05 08:06 | LINK-USDT-SWAP | 11.54 | 11.60/11.52 | 11.53 | — | 0.12186 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-11-05 09:06 | BTC-USDT-SWAP | 80389.3 | 80412.0/80234.6 | 80389.3 | — | 368.69 | 0.0100% | — | sem_zona |
| 2026-11-05 09:06 | ETH-USDT-SWAP | 2420.6 | 2423.4/2416.2 | 2420.6 | — | 14.45 | 0.0100% | — | sem_zona |
| 2026-11-05 09:06 | SOL-USDT-SWAP | 96.48 | 96.79/96.40 | 96.48 | — | 0.83143 | 0.0075% | B/venda@95.89 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-05 09:06 | XRP-USDT-SWAP | 1.3183 | 1.3215/1.3165 | 1.3183 | res 1.3268 (ha 3 candles) | 0.00874 | 0.0100% | — | zona_expirada_setup_A |
| 2026-11-05 09:06 | DOGE-USDT-SWAP | 0.07685 | 0.07697/0.07672 | 0.07685 | — | 0.00050 | 0.0100% | B/compra@0.07737 (0t/2c) | zona_mapeada_setup_B |
| 2026-11-05 09:06 | ARB-USDT-SWAP | 0.16350 | 0.16398/0.16323 | 0.16350 | res 0.16537 (ha 8 candles) | 0.00204 | -0.0011% | B/compra@0.16224 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-05 09:06 | WLD-USDT-SWAP | 0.37480 | 0.37580/0.37340 | 0.37480 | — | 0.00591 | -0.0135% | — | sem_zona |
| 2026-11-05 09:06 | SUI-USDT-SWAP | 0.92390 | 0.92680/0.92210 | 0.92390 | — | 0.01020 | 0.0100% | B/venda@0.91360 (0t/6c) | zona_mapeada_setup_B |
| 2026-11-05 09:06 | UNI-USDT-SWAP | 7.4260 | 7.4770/7.3720 | 7.4260 | res 7.8170 (ha 8 candles) | 0.12450 | 0.0100% | — | sem_zona |
| 2026-11-05 09:06 | LINK-USDT-SWAP | 11.54 | 11.57/11.52 | 11.54 | — | 0.11786 | 0.0100% | — | sem_zona |
| 2026-11-05 10:06 | BTC-USDT-SWAP | 79670.8 | 80389.3/79521.3 | 80389.3 | — | 377.04 | 0.0100% | B/compra@79666.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-05 10:06 | ETH-USDT-SWAP | 2393.2 | 2420.6/2386.1 | 2420.6 | — | 14.93 | 0.0100% | B/venda@2391.2 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-05 10:06 | SOL-USDT-SWAP | 95.30 | 96.47/94.84 | 96.48 | — | 0.84000 | 0.0072% | — | descartado_rr_baixo_setup_B |
| 2026-11-05 10:06 | XRP-USDT-SWAP | 1.3046 | 1.3182/1.2997 | 1.3183 | res 1.3268 (ha 4 candles) | 0.00922 | 0.0100% | — | sem_zona |
| 2026-11-05 10:06 | DOGE-USDT-SWAP | 0.07590 | 0.07685/0.07564 | 0.07685 | — | 0.00052 | 0.0100% | B/compra@0.07737 (0t/3c) | zona_mapeada_setup_B |
| 2026-11-05 10:06 | ARB-USDT-SWAP | 0.16170 | 0.16345/0.16052 | 0.16350 | res 0.16575 (ha 3 candles) | 0.00199 | 0.0010% | — | invalidado_setup_B |
| 2026-11-05 10:06 | WLD-USDT-SWAP | 0.37040 | 0.37480/0.36780 | 0.37480 | — | 0.00593 | -0.0100% | — | sem_zona |
| 2026-11-05 10:06 | SUI-USDT-SWAP | 0.91070 | 0.92390/0.90770 | 0.92390 | — | 0.00987 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-11-05 10:06 | UNI-USDT-SWAP | 7.3080 | 7.4260/7.2830 | 7.4260 | res 7.8170 (ha 9 candles) | 0.12179 | 0.0100% | — | sem_zona |
| 2026-11-05 10:06 | LINK-USDT-SWAP | 11.44 | 11.55/11.37 | 11.54 | — | 0.11786 | 0.0100% | — | sem_zona |
| 2026-11-05 11:06 | BTC-USDT-SWAP | 79656.9 | 79873.9/79537.2 | 80389.3 | — | 374.91 | 0.0100% | B/compra@79666.0 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-05 11:06 | ETH-USDT-SWAP | 2387.3 | 2397.0/2384.4 | 2420.6 | — | 14.93 | 0.0100% | — | confirmado_calibracao_setup_B |
| 2026-11-05 11:06 | SOL-USDT-SWAP | 95.33 | 95.60/95.15 | 96.48 | — | 0.82357 | 0.0060% | B/compra@95.13 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-05 11:06 | XRP-USDT-SWAP | 1.3066 | 1.3106/1.3037 | 1.3183 | res 1.3268 (ha 5 candles) | 0.00919 | 0.0100% | — | sem_zona |
| 2026-11-05 11:06 | DOGE-USDT-SWAP | 0.07593 | 0.07609/0.07576 | 0.07685 | — | 0.00051 | 0.0100% | B/compra@0.07737 (0t/4c) | zona_mapeada_setup_B |
| 2026-11-05 11:06 | ARB-USDT-SWAP | 0.16277 | 0.16284/0.16157 | 0.16350 | res 0.16575 (ha 4 candles) | 0.00194 | 0.0015% | B/compra@0.16325 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-05 11:06 | WLD-USDT-SWAP | 0.36780 | 0.37260/0.36620 | 0.37480 | — | 0.00590 | -0.0102% | — | sem_zona |
| 2026-11-05 11:06 | SUI-USDT-SWAP | 0.91100 | 0.91560/0.90960 | 0.92390 | — | 0.00956 | 0.0100% | B/venda@0.90860 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-05 11:06 | UNI-USDT-SWAP | 7.3020 | 7.3340/7.2630 | 7.4260 | res 7.8170 (ha 10 candles) | 0.11279 | 0.0100% | — | sem_zona |
| 2026-11-05 11:06 | LINK-USDT-SWAP | 11.43 | 11.47/11.39 | 11.54 | — | 0.11500 | 0.0100% | — | sem_zona |
| 2026-11-05 12:06 | BTC-USDT-SWAP | 78279.8 | 79725.1/78038.2 | 80389.3 | — | 468.96 | 0.0100% | — | invalidado_setup_B |
| 2026-11-05 12:06 | ETH-USDT-SWAP | 2343.2 | 2390.4/2333.5 | 2420.6 | — | 18.04 | 0.0100% | B/venda@2344.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-05 12:06 | SOL-USDT-SWAP | 92.95 | 95.50/92.54 | 96.48 | — | 0.97071 | 0.0046% | — | invalidado_setup_B |
| 2026-11-05 12:06 | XRP-USDT-SWAP | 1.2800 | 1.3083/1.2747 | 1.3183 | res 1.3268 (ha 6 candles) | 0.01111 | 0.0100% | B/compra@1.2723 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-05 12:06 | DOGE-USDT-SWAP | 0.07422 | 0.07600/0.07388 | 0.07685 | — | 0.00064 | 0.0100% | B/compra@0.07737 (0t/5c) | zona_mapeada_setup_B |
| 2026-11-05 12:06 | ARB-USDT-SWAP | 0.15863 | 0.16314/0.15773 | 0.16350 | res 0.16575 (ha 5 candles) | 0.00217 | 0.0027% | — | invalidado_setup_B |
| 2026-11-05 12:06 | WLD-USDT-SWAP | 0.35800 | 0.36840/0.35540 | 0.37480 | — | 0.00629 | -0.0108% | B/compra@0.35940 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-05 12:06 | SUI-USDT-SWAP | 0.88340 | 0.91200/0.87990 | 0.92390 | — | 0.01118 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-11-05 12:06 | UNI-USDT-SWAP | 7.1650 | 7.3300/7.1040 | 7.4260 | res 7.8170 (ha 11 candles) | 0.11929 | 0.0100% | — | sem_zona |
| 2026-11-05 12:06 | LINK-USDT-SWAP | 11.14 | 11.46/11.09 | 11.54 | — | 0.13379 | 0.0100% | B/compra@11.23 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-05 14:06 | BTC-USDT-SWAP | 76350.0 | 76980.0/75605.8 | 76000.0 | — | 694.71 | 0.0100% | B/compra@76360.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-05 14:06 | ETH-USDT-SWAP | 2264.3 | 2285.5/2238.3 | 2251.0 | — | 26.34 | 0.0100% | B/venda@2344.0 (0t/2c) | zona_mapeada_setup_B |
| 2026-11-05 14:06 | SOL-USDT-SWAP | 90.28 | 91.54/89.66 | 90.15 | — | 1.2307 | -0.0030% | B/compra@90.79 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-05 14:06 | XRP-USDT-SWAP | 1.2427 | 1.2591/1.2398 | 1.2445 | res 1.3268 (ha 8 candles) | 0.01411 | 0.0059% | B/compra@1.2723 (0t/2c) | zona_mapeada_setup_B |
| 2026-11-05 14:06 | DOGE-USDT-SWAP | 0.07199 | 0.07285/0.07143 | 0.07176 | — | 0.00088 | -0.0018% | B/compra@0.07737 (0t/7c) | zona_mapeada_setup_B |
| 2026-11-05 14:06 | ARB-USDT-SWAP | 0.15472 | 0.15709/0.15154 | 0.15223 | res 0.16575 (ha 7 candles) | 0.00288 | -0.0096% | — | sem_zona |
| 2026-11-05 14:06 | WLD-USDT-SWAP | 0.34290 | 0.34970/0.33940 | 0.34070 | — | 0.00776 | -0.0276% | B/compra@0.35940 (0t/2c) | zona_mapeada_setup_B |
| 2026-11-05 14:06 | SUI-USDT-SWAP | 0.85300 | 0.87090/0.84780 | 0.85270 | — | 0.01458 | -0.0045% | B/compra@0.85890 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-05 14:06 | UNI-USDT-SWAP | 6.8230 | 6.9600/6.7190 | 6.7770 | res 7.8170 (ha 13 candles) | 0.16593 | 0.0100% | B/compra@6.8050 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-05 14:06 | LINK-USDT-SWAP | 10.79 | 10.93/10.66 | 10.71 | — | 0.17850 | 0.0093% | B/compra@11.23 (0t/2c) | zona_mapeada_setup_B |
| 2026-11-05 15:06 | BTC-USDT-SWAP | 75904.1 | 76353.7/75771.4 | 76000.0 | — | 714.09 | 0.0100% | — | invalidado_setup_B |
| 2026-11-05 15:06 | ETH-USDT-SWAP | 2253.7 | 2265.6/2246.2 | 2251.0 | — | 26.80 | 0.0027% | B/venda@2344.0 (0t/3c) | zona_mapeada_setup_B |
| 2026-11-05 15:06 | SOL-USDT-SWAP | 89.14 | 90.35/88.87 | 90.15 | — | 1.2693 | -0.0033% | B/compra@90.79 (0t/1c) | zona_mapeada_setup_B |
| 2026-11-05 15:06 | XRP-USDT-SWAP | 1.2342 | 1.2445/1.2312 | 1.2445 | res 1.3268 (ha 9 candles) | 0.01429 | -0.0010% | B/compra@1.2723 (0t/3c) | zona_mapeada_setup_B |
| 2026-11-05 15:06 | DOGE-USDT-SWAP | 0.07147 | 0.07202/0.07135 | 0.07176 | — | 0.00089 | -0.0055% | — | zona_expirada_setup_B |
| 2026-11-05 15:06 | ARB-USDT-SWAP | 0.15524 | 0.15628/0.15342 | 0.15223 | res 0.16575 (ha 8 candles) | 0.00293 | -0.0140% | — | sem_zona |
| 2026-11-05 15:06 | WLD-USDT-SWAP | 0.33930 | 0.34280/0.33650 | 0.34070 | — | 0.00780 | -0.0318% | B/compra@0.35940 (0t/3c) | zona_mapeada_setup_B |
| 2026-11-05 15:06 | SUI-USDT-SWAP | 0.84370 | 0.85350/0.84210 | 0.85270 | — | 0.01449 | -0.0080% | B/compra@0.85890 (0t/1c) | zona_mapeada_setup_B |
| 2026-11-05 15:06 | UNI-USDT-SWAP | 6.8600 | 6.8850/6.7930 | 6.7770 | res 7.8170 (ha 14 candles) | 0.15929 | 0.0100% | — | confirmado_calibracao_setup_B |
| 2026-11-05 15:06 | LINK-USDT-SWAP | 10.66 | 10.79/10.63 | 10.71 | — | 0.17593 | 0.0023% | B/compra@11.23 (0t/3c) | zona_mapeada_setup_B |
| 2026-11-05 16:06 | BTC-USDT-SWAP | 76052.5 | 76238.4/75638.7 | 76000.0 | — | 730.26 | 0.0100% | — | sem_zona |
| 2026-11-05 16:06 | ETH-USDT-SWAP | 2250.7 | 2259.3/2241.0 | 2251.0 | — | 27.10 | -0.0036% | B/venda@2344.0 (0t/4c) | zona_mapeada_setup_B |
| 2026-11-05 16:06 | SOL-USDT-SWAP | 89.58 | 89.87/88.70 | 90.15 | — | 1.3050 | -0.0047% | B/compra@90.79 (0t/2c) | zona_mapeada_setup_B |
| 2026-11-05 16:06 | XRP-USDT-SWAP | 1.2336 | 1.2363/1.2278 | 1.2445 | res 1.3268 (ha 10 candles) | 0.01421 | -0.0037% | B/compra@1.2723 (0t/4c) | zona_mapeada_setup_B |
| 2026-11-05 16:06 | DOGE-USDT-SWAP | 0.07188 | 0.07205/0.07104 | 0.07176 | — | 0.00092 | -0.0062% | B/compra@0.07204 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-05 16:06 | ARB-USDT-SWAP | 0.15723 | 0.15812/0.15456 | 0.15223 | res 0.16575 (ha 9 candles) | 0.00306 | -0.0143% | — | sem_zona |
| 2026-11-05 16:06 | WLD-USDT-SWAP | 0.34320 | 0.34410/0.33610 | 0.34070 | — | 0.00802 | -0.0368% | B/compra@0.35940 (0t/4c) | zona_mapeada_setup_B |
| 2026-11-05 16:06 | SUI-USDT-SWAP | 0.85100 | 0.85260/0.83970 | 0.85270 | — | 0.01486 | -0.0103% | B/compra@0.85890 (0t/2c) | zona_mapeada_setup_B |
| 2026-11-05 16:06 | UNI-USDT-SWAP | 6.8090 | 6.8630/6.8040 | 6.7770 | res 7.8170 (ha 15 candles) | 0.15643 | 0.0100% | B/compra@6.9080 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-05 16:06 | LINK-USDT-SWAP | 10.73 | 10.75/10.62 | 10.71 | — | 0.17736 | 0.0006% | B/compra@11.23 (0t/4c) | zona_mapeada_setup_B |
| 2026-11-05 17:06 | BTC-USDT-SWAP | 76322.1 | 76530.0/75837.0 | 76322.1 | — | 763.02 | 0.0099% | — | sem_zona |
| 2026-11-05 17:06 | ETH-USDT-SWAP | 2260.6 | 2268.3/2243.2 | 2260.6 | — | 28.16 | -0.0074% | B/venda@2344.0 (0t/5c) | zona_mapeada_setup_B |
| 2026-11-05 17:06 | SOL-USDT-SWAP | 90.05 | 90.21/89.21 | 90.05 | — | 1.3286 | -0.0059% | B/compra@90.79 (0t/3c) | zona_mapeada_setup_B |
| 2026-11-05 17:06 | XRP-USDT-SWAP | 1.2434 | 1.2449/1.2282 | 1.2434 | res 1.3268 (ha 11 candles) | 0.01489 | -0.0047% | B/compra@1.2723 (0t/5c) | zona_mapeada_setup_B |
| 2026-11-05 17:06 | DOGE-USDT-SWAP | 0.07255 | 0.07269/0.07163 | 0.07255 | — | 0.00096 | -0.0034% | — | descartado_rr_baixo_setup_B |
| 2026-11-05 17:06 | ARB-USDT-SWAP | 0.15906 | 0.15992/0.15659 | 0.15906 | res 0.16575 (ha 10 candles) | 0.00319 | -0.0127% | B/compra@0.15961 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-05 17:06 | WLD-USDT-SWAP | 0.34400 | 0.34690/0.34100 | 0.34400 | — | 0.00811 | -0.0428% | B/compra@0.35940 (0t/5c) | zona_mapeada_setup_B |
| 2026-11-05 17:06 | SUI-USDT-SWAP | 0.85980 | 0.86470/0.84760 | 0.85980 | — | 0.01543 | -0.0110% | — | descartado_rr_baixo_setup_B |
| 2026-11-05 17:06 | UNI-USDT-SWAP | 6.8450 | 6.9000/6.7600 | 6.8450 | res 7.8170 (ha 16 candles) | 0.15857 | 0.0070% | — | invalidado_setup_B |
| 2026-11-05 17:06 | LINK-USDT-SWAP | 10.85 | 10.88/10.69 | 10.85 | — | 0.18529 | -0.0002% | B/compra@11.23 (0t/5c) | zona_mapeada_setup_B |
