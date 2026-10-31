# Log de Monitoramento Automatico -- Multi-Par (script gratuito, GitHub Actions)

> Gerado por script Python sem LLM (ver monitor/fetch_and_check.py). Fonte: OKX. Cobre os pares em PAIRS (configuracao no topo do script) -- BTC-USDT-SWAP e os demais adicionados na expansao de 07/09/2026. Leitura e MECANICA (regras objetivas da secao 4 do plano), sem a prosa qualitativa que o Claude gerava -- cole este log numa conversa do Claude se quiser a leitura interpretativa.

| Data/Hora (BRT) | Par | Close 1h | High/Low 1h | Close 4h | Swing 1h ref | ATR 1h | Funding | Zona ativa | Status checklist |
|---|---|---|---|---|---|---|---|---|---|
| 2026-10-29 01:06 | BTC-USDT-SWAP | 79813.1 | 79997.5/79710.9 | 79813.1 | res 81768.0 (ha 7 candles) | 481.61 | 0.0041% | B/compra@79725.3 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-29 01:06 | ETH-USDT-SWAP | 2307.9 | 2313.0/2301.5 | 2307.9 | — | 19.70 | 0.0041% | — | invalidado_setup_B |
| 2026-10-29 01:06 | SOL-USDT-SWAP | 99.63 | 100.13/99.44 | 99.63 | sup 100.39 (ha 13 candles) | 0.97643 | 0.0043% | A/venda@100.39 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-29 01:06 | XRP-USDT-SWAP | 1.2896 | 1.2983/1.2877 | 1.2896 | res 1.3438 (ha 7 candles) | 0.01156 | 0.0100% | — | invalidado_setup_B |
| 2026-10-29 01:06 | DOGE-USDT-SWAP | 0.07778 | 0.07812/0.07751 | 0.07778 | res 0.08087 (ha 7 candles) | 0.00073 | 0.0010% | B/compra@0.07780 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-29 01:06 | ARB-USDT-SWAP | 0.16519 | 0.16601/0.16344 | 0.16519 | sup 0.16325 (ha 13 candles) | 0.00329 | -0.0050% | B/compra@0.17743 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-29 01:06 | WLD-USDT-SWAP | 0.41460 | 0.41720/0.41080 | 0.41460 | sup 0.41700 (ha 11 candles) | 0.00915 | 0.0100% | A/venda@0.41700 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-29 01:06 | SUI-USDT-SWAP | 0.90420 | 0.91170/0.89870 | 0.90420 | — | 0.01334 | -0.0049% | B/compra@0.95790 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-29 01:06 | UNI-USDT-SWAP | 6.9810 | 7.0310/6.9350 | 6.9810 | res 7.3530 (ha 6 candles) | 0.10864 | 0.0100% | B/compra@6.9410 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-29 01:06 | LINK-USDT-SWAP | 11.39 | 11.43/11.30 | 11.39 | — | 0.15436 | -0.0050% | B/compra@11.52 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-29 02:06 | BTC-USDT-SWAP | 80217.8 | 80282.0/79750.0 | 79813.1 | res 81768.0 (ha 8 candles) | 489.66 | 0.0038% | — | descartado_rr_baixo_setup_B |
| 2026-10-29 02:06 | ETH-USDT-SWAP | 2320.5 | 2323.9/2304.0 | 2307.9 | — | 20.02 | 0.0040% | B/compra@2328.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-29 02:06 | SOL-USDT-SWAP | 100.11 | 100.26/99.40 | 99.63 | sup 100.39 (ha 14 candles) | 0.97429 | 0.0031% | A/venda@100.39 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-29 02:06 | XRP-USDT-SWAP | 1.2964 | 1.2980/1.2856 | 1.2896 | res 1.3438 (ha 8 candles) | 0.01157 | 0.0100% | B/compra@1.2886 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-29 02:06 | DOGE-USDT-SWAP | 0.07827 | 0.07831/0.07747 | 0.07778 | res 0.08087 (ha 8 candles) | 0.00074 | -0.0000% | — | descartado_rr_baixo_setup_B |
| 2026-10-29 02:06 | ARB-USDT-SWAP | 0.16558 | 0.16595/0.16436 | 0.16519 | sup 0.16325 (ha 14 candles) | 0.00325 | -0.0070% | B/compra@0.17743 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-29 02:06 | WLD-USDT-SWAP | 0.41650 | 0.41760/0.41300 | 0.41460 | sup 0.41700 (ha 12 candles) | 0.00914 | 0.0100% | A/venda@0.41700 (2t/0c) | zona_mapeada_setup_A |
| 2026-10-29 02:06 | SUI-USDT-SWAP | 0.91080 | 0.91240/0.90110 | 0.90420 | — | 0.01348 | -0.0036% | B/compra@0.95790 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-29 02:06 | UNI-USDT-SWAP | 7.0350 | 7.0550/6.9450 | 6.9810 | res 7.3530 (ha 7 candles) | 0.11079 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-10-29 02:06 | LINK-USDT-SWAP | 11.46 | 11.48/11.35 | 11.39 | — | 0.15607 | -0.0030% | — | invalidado_setup_B |
| 2026-10-29 03:06 | BTC-USDT-SWAP | 80196.5 | 80485.8/80179.5 | 79813.1 | res 81768.0 (ha 9 candles) | 492.25 | 0.0037% | — | sem_zona |
| 2026-10-29 03:06 | ETH-USDT-SWAP | 2322.2 | 2335.0/2320.3 | 2307.9 | — | 20.34 | 0.0044% | — | invalidado_setup_B |
| 2026-10-29 03:06 | SOL-USDT-SWAP | 100.25 | 100.78/100.11 | 99.63 | sup 99.17 (ha 3 candles) | 0.99071 | 0.0028% | A/venda@100.39 (2t/0c) | zona_mapeada_setup_A |
| 2026-10-29 03:06 | XRP-USDT-SWAP | 1.2986 | 1.3040/1.2962 | 1.2896 | res 1.3438 (ha 9 candles) | 0.01171 | 0.0100% | B/compra@1.2886 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-29 03:06 | DOGE-USDT-SWAP | 0.07856 | 0.07900/0.07827 | 0.07778 | res 0.08087 (ha 9 candles) | 0.00077 | -0.0005% | B/compra@0.07842 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-29 03:06 | ARB-USDT-SWAP | 0.16643 | 0.16868/0.16553 | 0.16519 | sup 0.16325 (ha 15 candles) | 0.00329 | -0.0048% | — | zona_expirada_setup_B |
| 2026-10-29 03:06 | WLD-USDT-SWAP | 0.41930 | 0.42300/0.41650 | 0.41460 | sup 0.41700 (ha 13 candles) | 0.00918 | 0.0100% | — | invalidado_setup_A |
| 2026-10-29 03:06 | SUI-USDT-SWAP | 0.91570 | 0.92210/0.91060 | 0.90420 | — | 0.01391 | -0.0020% | — | zona_expirada_setup_B |
| 2026-10-29 03:06 | UNI-USDT-SWAP | 7.0640 | 7.1400/7.0350 | 6.9810 | res 7.3530 (ha 8 candles) | 0.11443 | 0.0100% | B/compra@7.0920 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-29 03:06 | LINK-USDT-SWAP | 11.52 | 11.61/11.46 | 11.39 | — | 0.16257 | -0.0005% | B/venda@11.62 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-29 04:06 | BTC-USDT-SWAP | 79931.8 | 80244.9/79857.2 | 79813.1 | res 81768.0 (ha 10 candles) | 494.24 | 0.0039% | — | sem_zona |
| 2026-10-29 04:06 | ETH-USDT-SWAP | 2312.7 | 2324.6/2309.3 | 2307.9 | — | 20.36 | 0.0053% | B/compra@2315.3 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-29 04:06 | SOL-USDT-SWAP | 100.01 | 100.43/99.81 | 99.63 | sup 99.17 (ha 4 candles) | 0.98357 | 0.0027% | — | descartado_rr_baixo_setup_A |
| 2026-10-29 04:06 | XRP-USDT-SWAP | 1.2935 | 1.3002/1.2916 | 1.2896 | res 1.3438 (ha 10 candles) | 0.01165 | 0.0100% | B/compra@1.2886 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-29 04:06 | DOGE-USDT-SWAP | 0.07800 | 0.07873/0.07793 | 0.07778 | res 0.08087 (ha 10 candles) | 0.00078 | -0.0003% | — | invalidado_setup_B |
| 2026-10-29 04:06 | ARB-USDT-SWAP | 0.16430 | 0.16703/0.16424 | 0.16519 | sup 0.16344 (ha 3 candles) | 0.00325 | -0.0080% | — | sem_zona |
| 2026-10-29 04:06 | WLD-USDT-SWAP | 0.41270 | 0.41990/0.41150 | 0.41460 | sup 0.41080 (ha 3 candles) | 0.00861 | 0.0100% | — | sem_zona |
| 2026-10-29 04:06 | SUI-USDT-SWAP | 0.90820 | 0.91820/0.90680 | 0.90420 | — | 0.01403 | -0.0024% | B/compra@0.90000 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-29 04:06 | UNI-USDT-SWAP | 7.0030 | 7.0850/6.9990 | 6.9810 | res 7.3530 (ha 9 candles) | 0.11500 | 0.0089% | — | invalidado_setup_B |
| 2026-10-29 04:06 | LINK-USDT-SWAP | 11.43 | 11.53/11.41 | 11.39 | — | 0.16293 | 0.0015% | B/venda@11.62 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-29 05:06 | BTC-USDT-SWAP | 79820.1 | 79950.0/79790.0 | 79820.1 | res 81768.0 (ha 11 candles) | 468.86 | 0.0034% | B/compra@79477.9 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-29 05:06 | ETH-USDT-SWAP | 2309.2 | 2314.0/2304.1 | 2309.2 | — | 19.81 | 0.0061% | — | invalidado_setup_B |
| 2026-10-29 05:06 | SOL-USDT-SWAP | 99.70 | 100.09/99.63 | 99.70 | sup 99.17 (ha 5 candles) | 0.94857 | 0.0013% | — | sem_zona |
| 2026-10-29 05:06 | XRP-USDT-SWAP | 1.2881 | 1.2949/1.2878 | 1.2881 | res 1.3438 (ha 11 candles) | 0.01148 | 0.0086% | B/compra@1.2886 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-29 05:06 | DOGE-USDT-SWAP | 0.07767 | 0.07806/0.07763 | 0.07767 | res 0.08087 (ha 11 candles) | 0.00077 | -0.0005% | B/compra@0.07780 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-29 05:06 | ARB-USDT-SWAP | 0.16299 | 0.16444/0.16224 | 0.16299 | sup 0.16344 (ha 4 candles) | 0.00323 | -0.0127% | A/venda@0.16344 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-29 05:06 | WLD-USDT-SWAP | 0.41230 | 0.41310/0.40860 | 0.41230 | sup 0.41080 (ha 4 candles) | 0.00851 | 0.0100% | — | sem_zona |
| 2026-10-29 05:06 | SUI-USDT-SWAP | 0.90640 | 0.90950/0.90100 | 0.90640 | — | 0.01396 | -0.0028% | B/compra@0.90000 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-29 05:06 | UNI-USDT-SWAP | 6.9910 | 7.0110/6.9660 | 6.9910 | res 7.3530 (ha 10 candles) | 0.11379 | 0.0045% | B/compra@6.9410 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-29 05:06 | LINK-USDT-SWAP | 11.36 | 11.44/11.35 | 11.36 | — | 0.16021 | 0.0012% | B/venda@11.62 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-29 06:06 | BTC-USDT-SWAP | 80030.2 | 80115.7/79805.3 | 79820.1 | res 80485.8 (ha 3 candles) | 444.41 | 0.0034% | B/compra@79477.9 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-29 06:06 | ETH-USDT-SWAP | 2318.4 | 2322.0/2309.0 | 2309.2 | — | 18.57 | 0.0057% | B/compra@2328.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-29 06:06 | SOL-USDT-SWAP | 100.18 | 100.30/99.70 | 99.70 | sup 99.17 (ha 6 candles) | 0.89071 | 0.0018% | — | sem_zona |
| 2026-10-29 06:06 | XRP-USDT-SWAP | 1.2908 | 1.2938/1.2868 | 1.2881 | res 1.3040 (ha 3 candles) | 0.01069 | 0.0100% | B/compra@1.2886 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-29 06:06 | DOGE-USDT-SWAP | 0.07803 | 0.07813/0.07760 | 0.07767 | res 0.07900 (ha 3 candles) | 0.00074 | 0.0018% | — | descartado_rr_baixo_setup_B |
| 2026-10-29 06:06 | ARB-USDT-SWAP | 0.16415 | 0.16485/0.16292 | 0.16299 | sup 0.16344 (ha 5 candles) | 0.00292 | -0.0130% | A/venda@0.16344 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-29 06:06 | WLD-USDT-SWAP | 0.41670 | 0.41780/0.41210 | 0.41230 | sup 0.41080 (ha 5 candles) | 0.00781 | 0.0100% | — | sem_zona |
| 2026-10-29 06:06 | SUI-USDT-SWAP | 0.91120 | 0.91300/0.90500 | 0.90640 | — | 0.01315 | -0.0038% | B/compra@0.90000 (1t/1c) | zona_mapeada_setup_B |
| 2026-10-29 06:06 | UNI-USDT-SWAP | 7.0150 | 7.0590/6.9750 | 6.9910 | res 7.1400 (ha 3 candles) | 0.10793 | 0.0026% | B/compra@6.9410 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-29 06:06 | LINK-USDT-SWAP | 11.47 | 11.48/11.36 | 11.36 | — | 0.15150 | 0.0049% | B/venda@11.62 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-29 07:06 | BTC-USDT-SWAP | 80171.8 | 80308.0/80004.0 | 79820.1 | res 80485.8 (ha 4 candles) | 419.26 | 0.0037% | B/compra@79477.9 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-29 07:06 | ETH-USDT-SWAP | 2320.4 | 2326.8/2315.5 | 2309.2 | — | 18.02 | 0.0049% | — | invalidado_setup_B |
| 2026-10-29 07:06 | SOL-USDT-SWAP | 100.22 | 100.60/99.99 | 99.70 | sup 99.17 (ha 7 candles) | 0.85429 | 0.0019% | — | sem_zona |
| 2026-10-29 07:06 | XRP-USDT-SWAP | 1.2922 | 1.2960/1.2888 | 1.2881 | res 1.3040 (ha 4 candles) | 0.01034 | 0.0100% | — | zona_expirada_setup_B |
| 2026-10-29 07:06 | DOGE-USDT-SWAP | 0.07821 | 0.07838/0.07801 | 0.07767 | res 0.07900 (ha 4 candles) | 0.00071 | 0.0037% | B/compra@0.07842 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-29 07:06 | ARB-USDT-SWAP | 0.16512 | 0.16586/0.16405 | 0.16299 | sup 0.16344 (ha 6 candles) | 0.00281 | -0.0129% | — | invalidado_setup_A |
| 2026-10-29 07:06 | WLD-USDT-SWAP | 0.41810 | 0.42130/0.41620 | 0.41230 | sup 0.41080 (ha 6 candles) | 0.00749 | 0.0100% | — | sem_zona |
| 2026-10-29 07:06 | SUI-USDT-SWAP | 0.91560 | 0.91850/0.91010 | 0.90640 | — | 0.01271 | -0.0032% | B/compra@0.90000 (1t/2c) | zona_mapeada_setup_B |
| 2026-10-29 07:06 | UNI-USDT-SWAP | 7.0480 | 7.0950/7.0070 | 6.9910 | res 7.1400 (ha 4 candles) | 0.10907 | 0.0032% | B/compra@6.9410 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-29 07:06 | LINK-USDT-SWAP | 11.51 | 11.54/11.46 | 11.36 | — | 0.14393 | 0.0100% | B/venda@11.62 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-29 08:06 | BTC-USDT-SWAP | 80258.1 | 80346.5/80075.5 | 79820.1 | res 80485.8 (ha 5 candles) | 380.90 | 0.0051% | B/compra@79477.9 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-29 08:06 | ETH-USDT-SWAP | 2327.8 | 2329.8/2316.1 | 2309.2 | — | 15.84 | 0.0046% | — | sem_zona |
| 2026-10-29 08:06 | SOL-USDT-SWAP | 100.59 | 100.78/100.00 | 99.70 | sup 99.17 (ha 8 candles) | 0.76714 | 0.0038% | — | sem_zona |
| 2026-10-29 08:06 | XRP-USDT-SWAP | 1.2940 | 1.2966/1.2870 | 1.2881 | res 1.3040 (ha 5 candles) | 0.00967 | 0.0100% | B/compra@1.2943 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-29 08:06 | DOGE-USDT-SWAP | 0.07857 | 0.07866/0.07786 | 0.07767 | res 0.07900 (ha 5 candles) | 0.00068 | 0.0049% | — | descartado_rr_baixo_setup_B |
| 2026-10-29 08:06 | ARB-USDT-SWAP | 0.16853 | 0.16962/0.16496 | 0.16299 | sup 0.16224 (ha 3 candles) | 0.00277 | -0.0074% | — | sem_zona |
| 2026-10-29 08:06 | WLD-USDT-SWAP | 0.42370 | 0.42620/0.41650 | 0.41230 | sup 0.40860 (ha 3 candles) | 0.00687 | 0.0097% | — | sem_zona |
| 2026-10-29 08:06 | SUI-USDT-SWAP | 0.92540 | 0.92820/0.91240 | 0.90640 | — | 0.01186 | -0.0010% | B/compra@0.90000 (1t/3c) | zona_mapeada_setup_B |
| 2026-10-29 08:06 | UNI-USDT-SWAP | 7.1530 | 7.1820/7.0130 | 6.9910 | res 7.1400 (ha 5 candles) | 0.10771 | 0.0035% | B/compra@6.9410 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-29 08:06 | LINK-USDT-SWAP | 11.59 | 11.61/11.47 | 11.36 | — | 0.13307 | 0.0100% | B/venda@11.62 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-29 09:06 | BTC-USDT-SWAP | 80133.3 | 80280.0/80088.4 | 80133.3 | res 80485.8 (ha 6 candles) | 371.68 | 0.0073% | B/compra@79477.9 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-29 09:06 | ETH-USDT-SWAP | 2324.2 | 2327.8/2321.6 | 2324.2 | res 2335.0 (ha 6 candles) | 15.09 | 0.0047% | B/compra@2315.3 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-29 09:06 | SOL-USDT-SWAP | 100.32 | 100.63/100.30 | 100.32 | — | 0.73286 | 0.0045% | B/compra@99.83 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-29 09:06 | XRP-USDT-SWAP | 1.2911 | 1.2943/1.2895 | 1.2911 | — | 0.00941 | 0.0100% | — | invalidado_setup_B |
| 2026-10-29 09:06 | DOGE-USDT-SWAP | 0.07862 | 0.07876/0.07844 | 0.07862 | res 0.07900 (ha 6 candles) | 0.00066 | 0.0074% | — | sem_zona |
| 2026-10-29 09:06 | ARB-USDT-SWAP | 0.16790 | 0.16918/0.16690 | 0.16790 | — | 0.00267 | -0.0041% | B/compra@0.16922 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-29 09:06 | WLD-USDT-SWAP | 0.42000 | 0.42450/0.41920 | 0.42000 | — | 0.00664 | 0.0100% | B/compra@0.42450 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-29 09:06 | SUI-USDT-SWAP | 0.92180 | 0.92660/0.92080 | 0.92180 | res 0.92210 (ha 6 candles) | 0.01145 | 0.0023% | B/compra@0.90000 (1t/4c) | zona_mapeada_setup_B |
| 2026-10-29 09:06 | UNI-USDT-SWAP | 7.1810 | 7.2400/7.1270 | 7.1810 | res 7.1400 (ha 6 candles) | 0.10679 | 0.0093% | B/compra@6.9410 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-29 09:06 | LINK-USDT-SWAP | 11.62 | 11.64/11.57 | 11.62 | — | 0.12907 | 0.0100% | B/venda@11.62 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-29 10:06 | BTC-USDT-SWAP | 80024.4 | 80245.2/79973.8 | 80133.3 | res 80485.8 (ha 7 candles) | 369.22 | 0.0082% | B/compra@79477.9 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-29 10:06 | ETH-USDT-SWAP | 2322.0 | 2328.6/2316.6 | 2324.2 | res 2335.0 (ha 7 candles) | 15.05 | 0.0047% | B/compra@2315.3 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-29 10:06 | SOL-USDT-SWAP | 100.49 | 100.71/100.07 | 100.32 | — | 0.73857 | 0.0041% | B/compra@99.83 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-29 10:06 | XRP-USDT-SWAP | 1.2889 | 1.2934/1.2859 | 1.2911 | — | 0.00944 | 0.0100% | B/compra@1.2856 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-29 10:06 | DOGE-USDT-SWAP | 0.07895 | 0.07906/0.07843 | 0.07862 | res 0.07900 (ha 7 candles) | 0.00067 | 0.0100% | B/compra@0.07929 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-29 10:06 | ARB-USDT-SWAP | 0.17097 | 0.17103/0.16737 | 0.16790 | — | 0.00274 | 0.0030% | — | descartado_rr_baixo_setup_B |
| 2026-10-29 10:06 | WLD-USDT-SWAP | 0.42160 | 0.42170/0.41680 | 0.42000 | — | 0.00672 | 0.0100% | B/compra@0.42450 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-29 10:06 | SUI-USDT-SWAP | 0.92510 | 0.92650/0.91660 | 0.92180 | res 0.92210 (ha 7 candles) | 0.01164 | 0.0047% | B/compra@0.90000 (1t/5c) | zona_mapeada_setup_B |
| 2026-10-29 10:06 | UNI-USDT-SWAP | 7.2130 | 7.2400/7.1460 | 7.1810 | res 7.1400 (ha 7 candles) | 0.10850 | 0.0100% | B/compra@6.9410 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-29 10:06 | LINK-USDT-SWAP | 11.63 | 11.66/11.56 | 11.62 | — | 0.13050 | 0.0100% | — | zona_expirada_setup_B |
| 2026-10-29 11:06 | BTC-USDT-SWAP | 80272.7 | 80388.7/79860.0 | 80133.3 | res 80485.8 (ha 8 candles) | 391.84 | 0.0089% | B/compra@79477.9 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-29 11:06 | ETH-USDT-SWAP | 2326.1 | 2331.3/2312.2 | 2324.2 | res 2335.0 (ha 8 candles) | 15.85 | 0.0049% | — | descartado_rr_baixo_setup_B |
| 2026-10-29 11:06 | SOL-USDT-SWAP | 100.61 | 100.91/100.08 | 100.32 | — | 0.77714 | 0.0040% | B/compra@99.83 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-29 11:06 | XRP-USDT-SWAP | 1.2904 | 1.2950/1.2855 | 1.2911 | — | 0.00981 | 0.0100% | B/compra@1.2856 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-29 11:06 | DOGE-USDT-SWAP | 0.07915 | 0.07936/0.07871 | 0.07862 | res 0.07900 (ha 8 candles) | 0.00069 | 0.0100% | — | confirmado_calibracao_setup_B |
| 2026-10-29 11:06 | ARB-USDT-SWAP | 0.16989 | 0.17212/0.16843 | 0.16790 | — | 0.00288 | 0.0086% | — | sem_zona |
| 2026-10-29 11:06 | WLD-USDT-SWAP | 0.42120 | 0.42440/0.41780 | 0.42000 | — | 0.00692 | 0.0085% | — | invalidado_setup_B |
| 2026-10-29 11:06 | SUI-USDT-SWAP | 0.93080 | 0.93400/0.92270 | 0.92180 | res 0.92210 (ha 8 candles) | 0.01208 | 0.0082% | B/compra@0.90000 (1t/6c) | zona_mapeada_setup_B |
| 2026-10-29 11:06 | UNI-USDT-SWAP | 7.1840 | 7.2690/7.1230 | 7.1810 | res 7.1400 (ha 8 candles) | 0.11543 | 0.0100% | B/compra@6.9410 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-29 11:06 | LINK-USDT-SWAP | 11.64 | 11.70/11.57 | 11.62 | — | 0.13521 | 0.0100% | B/venda@11.55 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-29 12:06 | BTC-USDT-SWAP | 81146.2 | 81525.0/80234.2 | 80133.3 | res 80485.8 (ha 9 candles) | 463.53 | 0.0100% | B/compra@79477.9 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-29 12:06 | ETH-USDT-SWAP | 2343.6 | 2352.7/2321.6 | 2324.2 | res 2335.0 (ha 9 candles) | 17.55 | 0.0051% | A/compra@2335.0 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-29 12:06 | SOL-USDT-SWAP | 101.73 | 102.18/100.50 | 100.32 | — | 0.84571 | 0.0060% | B/compra@99.83 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-29 12:06 | XRP-USDT-SWAP | 1.3023 | 1.3079/1.2891 | 1.2911 | — | 0.01072 | 0.0100% | B/compra@1.2856 (1t/1c) | zona_mapeada_setup_B |
| 2026-10-29 12:06 | DOGE-USDT-SWAP | 0.07985 | 0.08046/0.07901 | 0.07862 | res 0.07900 (ha 9 candles) | 0.00076 | 0.0100% | A/compra@0.07900 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-29 12:06 | ARB-USDT-SWAP | 0.17180 | 0.17367/0.16944 | 0.16790 | — | 0.00305 | 0.0100% | B/venda@0.17358 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-29 12:06 | WLD-USDT-SWAP | 0.42550 | 0.43230/0.42000 | 0.42000 | — | 0.00742 | 0.0049% | — | sem_zona |
| 2026-10-29 12:06 | SUI-USDT-SWAP | 0.94160 | 0.95210/0.92950 | 0.92180 | res 0.92210 (ha 9 candles) | 0.01312 | 0.0082% | B/compra@0.90000 (1t/7c) | zona_mapeada_setup_B |
| 2026-10-29 12:06 | UNI-USDT-SWAP | 7.2740 | 7.3320/7.1740 | 7.1810 | res 7.1400 (ha 9 candles) | 0.12143 | 0.0100% | B/compra@6.9410 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-29 12:06 | LINK-USDT-SWAP | 11.79 | 11.84/11.62 | 11.62 | — | 0.14443 | 0.0100% | B/venda@11.55 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-29 13:06 | BTC-USDT-SWAP | 81744.1 | 81883.0/81146.1 | 81744.1 | res 80485.8 (ha 10 candles) | 432.81 | 0.0097% | — | zona_expirada_setup_B |
| 2026-10-29 13:06 | ETH-USDT-SWAP | 2368.0 | 2372.3/2343.6 | 2368.0 | — | 16.53 | 0.0064% | A/compra@2335.0 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-29 13:06 | SOL-USDT-SWAP | 102.66 | 102.70/101.68 | 102.66 | res 100.78 (ha 10 candles) | 0.76714 | 0.0077% | B/compra@99.83 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-29 13:06 | XRP-USDT-SWAP | 1.3097 | 1.3123/1.3015 | 1.3097 | — | 0.00973 | 0.0100% | B/compra@1.2856 (1t/2c) | zona_mapeada_setup_B |
| 2026-10-29 13:06 | DOGE-USDT-SWAP | 0.08062 | 0.08069/0.07972 | 0.08062 | res 0.07900 (ha 10 candles) | 0.00072 | 0.0100% | A/compra@0.07900 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-29 13:06 | ARB-USDT-SWAP | 0.17445 | 0.17493/0.17108 | 0.17445 | — | 0.00292 | 0.0100% | — | invalidado_setup_B |
| 2026-10-29 13:06 | WLD-USDT-SWAP | 0.43690 | 0.43830/0.42500 | 0.43690 | — | 0.00733 | 0.0022% | B/compra@0.43160 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-29 13:06 | SUI-USDT-SWAP | 0.95360 | 0.95440/0.94020 | 0.95360 | — | 0.01210 | 0.0100% | — | zona_expirada_setup_B |
| 2026-10-29 13:06 | UNI-USDT-SWAP | 7.3950 | 7.4220/7.2590 | 7.3950 | — | 0.11621 | 0.0100% | — | zona_expirada_setup_B |
| 2026-10-29 13:06 | LINK-USDT-SWAP | 11.96 | 11.97/11.78 | 11.96 | res 11.61 (ha 10 candles) | 0.13386 | 0.0100% | B/venda@11.55 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-29 14:06 | BTC-USDT-SWAP | 81240.0 | 81944.4/81153.8 | 81744.1 | res 80485.8 (ha 11 candles) | 454.86 | 0.0100% | A/compra@80485.8 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-29 14:06 | ETH-USDT-SWAP | 2352.2 | 2378.8/2350.3 | 2368.0 | — | 16.77 | 0.0087% | A/compra@2335.0 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-29 14:06 | SOL-USDT-SWAP | 101.86 | 103.17/101.73 | 102.66 | res 100.78 (ha 11 candles) | 0.80214 | 0.0100% | B/compra@99.83 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-29 14:06 | XRP-USDT-SWAP | 1.2991 | 1.3179/1.2974 | 1.3097 | — | 0.01016 | 0.0100% | B/compra@1.2856 (1t/3c) | zona_mapeada_setup_B |
| 2026-10-29 14:06 | DOGE-USDT-SWAP | 0.08009 | 0.08146/0.07990 | 0.08062 | res 0.07900 (ha 11 candles) | 0.00076 | 0.0100% | A/compra@0.07900 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-29 14:06 | ARB-USDT-SWAP | 0.17235 | 0.17596/0.17132 | 0.17445 | — | 0.00307 | 0.0100% | — | sem_zona |
| 2026-10-29 14:06 | WLD-USDT-SWAP | 0.43350 | 0.44370/0.43200 | 0.43690 | — | 0.00750 | 0.0044% | B/compra@0.43160 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-29 14:06 | SUI-USDT-SWAP | 0.94730 | 0.96150/0.94220 | 0.95360 | — | 0.01221 | 0.0100% | B/compra@0.93870 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-29 14:06 | UNI-USDT-SWAP | 7.3700 | 7.5190/7.3500 | 7.3950 | — | 0.11614 | 0.0100% | B/venda@7.2960 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-29 14:06 | LINK-USDT-SWAP | 11.86 | 12.01/11.82 | 11.96 | res 11.61 (ha 11 candles) | 0.13257 | 0.0100% | B/venda@11.55 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-29 15:06 | BTC-USDT-SWAP | 80870.1 | 81240.1/80650.2 | 81744.1 | res 80485.8 (ha 12 candles) | 476.52 | 0.0100% | A/compra@80485.8 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-29 15:06 | ETH-USDT-SWAP | 2340.5 | 2354.2/2330.7 | 2368.0 | — | 17.62 | 0.0100% | A/compra@2335.0 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-29 15:06 | SOL-USDT-SWAP | 101.04 | 101.93/100.70 | 102.66 | res 100.78 (ha 12 candles) | 0.84071 | 0.0100% | B/compra@99.83 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-29 15:06 | XRP-USDT-SWAP | 1.2928 | 1.3003/1.2871 | 1.3097 | — | 0.01034 | 0.0100% | B/compra@1.2856 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-29 15:06 | DOGE-USDT-SWAP | 0.07957 | 0.08020/0.07917 | 0.08062 | res 0.07900 (ha 12 candles) | 0.00079 | 0.0100% | A/compra@0.07900 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-29 15:06 | ARB-USDT-SWAP | 0.16956 | 0.17270/0.16811 | 0.17445 | — | 0.00322 | 0.0100% | — | sem_zona |
| 2026-10-29 15:06 | WLD-USDT-SWAP | 0.42360 | 0.43380/0.41830 | 0.43690 | — | 0.00815 | 0.0100% | — | invalidado_setup_B |
| 2026-10-29 15:06 | SUI-USDT-SWAP | 0.93590 | 0.94780/0.92790 | 0.95360 | — | 0.01271 | 0.0100% | B/compra@0.93870 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-29 15:06 | UNI-USDT-SWAP | 7.2630 | 7.3790/7.2040 | 7.3950 | — | 0.12179 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-10-29 15:06 | LINK-USDT-SWAP | 11.74 | 11.87/11.66 | 11.96 | res 11.61 (ha 12 candles) | 0.13843 | 0.0100% | B/venda@11.55 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-29 16:06 | BTC-USDT-SWAP | 80833.4 | 80929.2/80558.6 | 81744.1 | res 80485.8 (ha 13 candles) | 464.99 | 0.0100% | A/compra@80485.8 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-29 16:06 | ETH-USDT-SWAP | 2330.3 | 2342.2/2323.3 | 2368.0 | — | 17.55 | 0.0100% | — | invalidado_setup_A |
| 2026-10-29 16:06 | SOL-USDT-SWAP | 100.55 | 101.18/100.28 | 102.66 | res 100.78 (ha 13 candles) | 0.84357 | 0.0100% | B/compra@99.83 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-29 16:06 | XRP-USDT-SWAP | 1.2857 | 1.2946/1.2781 | 1.3097 | — | 0.01064 | 0.0100% | — | zona_expirada_setup_B |
| 2026-10-29 16:06 | DOGE-USDT-SWAP | 0.07930 | 0.07967/0.07896 | 0.08062 | res 0.07900 (ha 13 candles) | 0.00078 | 0.0100% | A/compra@0.07900 (2t/0c) | zona_mapeada_setup_A |
| 2026-10-29 16:06 | ARB-USDT-SWAP | 0.16863 | 0.17037/0.16732 | 0.17445 | — | 0.00332 | 0.0100% | — | sem_zona |
| 2026-10-29 16:06 | WLD-USDT-SWAP | 0.41890 | 0.42430/0.41630 | 0.43690 | — | 0.00839 | 0.0100% | B/compra@0.42450 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-29 16:06 | SUI-USDT-SWAP | 0.93120 | 0.93730/0.92500 | 0.95360 | — | 0.01278 | 0.0100% | — | invalidado_setup_B |
| 2026-10-29 16:06 | UNI-USDT-SWAP | 7.1830 | 7.2800/7.1530 | 7.3950 | — | 0.12300 | 0.0100% | B/venda@7.2080 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-29 16:06 | LINK-USDT-SWAP | 11.68 | 11.76/11.63 | 11.96 | res 11.61 (ha 13 candles) | 0.13829 | 0.0100% | B/venda@11.55 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-29 17:06 | BTC-USDT-SWAP | 80823.8 | 80928.6/80740.0 | 80823.8 | res 81944.4 (ha 3 candles) | 456.59 | 0.0100% | A/compra@80485.8 (1t/1c) | zona_mapeada_setup_A |
| 2026-10-29 17:06 | ETH-USDT-SWAP | 2336.1 | 2338.7/2325.6 | 2336.1 | — | 17.44 | 0.0100% | B/venda@2344.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-29 17:06 | SOL-USDT-SWAP | 99.77 | 100.61/99.76 | 99.77 | res 103.17 (ha 3 candles) | 0.85643 | 0.0100% | B/compra@99.83 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-29 17:06 | XRP-USDT-SWAP | 1.2816 | 1.2873/1.2802 | 1.2816 | — | 0.01059 | 0.0100% | B/compra@1.2886 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-29 17:06 | DOGE-USDT-SWAP | 0.07925 | 0.07947/0.07898 | 0.07925 | res 0.08146 (ha 3 candles) | 0.00077 | 0.0100% | — | zona_expirada_setup_A |
| 2026-10-29 17:06 | ARB-USDT-SWAP | 0.16820 | 0.16924/0.16781 | 0.16820 | — | 0.00320 | 0.0100% | — | sem_zona |
| 2026-10-29 17:06 | WLD-USDT-SWAP | 0.41780 | 0.41960/0.41580 | 0.41780 | — | 0.00820 | 0.0100% | B/compra@0.42450 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-29 17:06 | SUI-USDT-SWAP | 0.92920 | 0.93380/0.92730 | 0.92920 | — | 0.01242 | 0.0100% | B/venda@0.93080 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-29 17:06 | UNI-USDT-SWAP | 7.1700 | 7.1940/7.1470 | 7.1700 | — | 0.11886 | 0.0100% | B/venda@7.2080 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-29 17:06 | LINK-USDT-SWAP | 11.69 | 11.73/11.63 | 11.69 | res 12.01 (ha 3 candles) | 0.13500 | 0.0100% | B/venda@11.55 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-29 18:06 | BTC-USDT-SWAP | 78808.0 | 80826.1/78233.0 | 80823.8 | res 81944.4 (ha 4 candles) | 614.11 | 0.0100% | — | invalidado_setup_A |
| 2026-10-29 18:06 | ETH-USDT-SWAP | 2256.5 | 2336.2/2231.0 | 2336.1 | — | 23.86 | 0.0090% | B/venda@2344.0 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-29 18:06 | SOL-USDT-SWAP | 96.12 | 99.90/94.83 | 99.77 | res 103.17 (ha 4 candles) | 1.1743 | 0.0093% | — | invalidado_setup_B |
| 2026-10-29 18:06 | XRP-USDT-SWAP | 1.2375 | 1.2824/1.2210 | 1.2816 | — | 0.01436 | 0.0061% | B/compra@1.2886 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-29 18:06 | DOGE-USDT-SWAP | 0.07531 | 0.07930/0.07420 | 0.07925 | res 0.08146 (ha 4 candles) | 0.00107 | 0.0100% | B/compra@0.07592 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-29 18:06 | ARB-USDT-SWAP | 0.15335 | 0.16837/0.15086 | 0.16820 | — | 0.00425 | 0.0086% | — | sem_zona |
| 2026-10-29 18:06 | WLD-USDT-SWAP | 0.38850 | 0.41810/0.37710 | 0.41780 | — | 0.01053 | 0.0100% | B/compra@0.42450 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-29 18:06 | SUI-USDT-SWAP | 0.87370 | 0.93010/0.85750 | 0.92920 | — | 0.01679 | 0.0099% | — | descartado_rr_baixo_setup_B |
| 2026-10-29 18:06 | UNI-USDT-SWAP | 6.6010 | 7.1750/6.4790 | 7.1700 | — | 0.16243 | 0.0035% | B/venda@7.2080 (1t/1c) | zona_mapeada_setup_B |
| 2026-10-29 18:06 | LINK-USDT-SWAP | 10.99 | 11.69/10.88 | 11.69 | res 12.01 (ha 4 candles) | 0.18436 | 0.0100% | — | invalidado_tendencia_virou_setup_B |
| 2026-10-29 19:06 | BTC-USDT-SWAP | 79002.0 | 79765.5/78533.2 | 80823.8 | res 81944.4 (ha 5 candles) | 690.71 | 0.0100% | B/compra@79477.9 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-29 19:06 | ETH-USDT-SWAP | 2272.3 | 2293.6/2245.1 | 2336.1 | — | 26.62 | 0.0040% | B/venda@2344.0 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-29 19:06 | SOL-USDT-SWAP | 97.50 | 98.06/95.35 | 99.77 | res 103.17 (ha 5 candles) | 1.3350 | 0.0056% | — | sem_zona |
| 2026-10-29 19:06 | XRP-USDT-SWAP | 1.2539 | 1.2640/1.2334 | 1.2816 | — | 0.01604 | 0.0011% | B/compra@1.2886 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-29 19:06 | DOGE-USDT-SWAP | 0.07609 | 0.07697/0.07491 | 0.07925 | res 0.08146 (ha 5 candles) | 0.00119 | 0.0078% | B/compra@0.07592 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-29 19:06 | ARB-USDT-SWAP | 0.15557 | 0.16030/0.15276 | 0.16820 | — | 0.00463 | 0.0017% | — | sem_zona |
| 2026-10-29 19:06 | WLD-USDT-SWAP | 0.39080 | 0.39990/0.38710 | 0.41780 | — | 0.01112 | 0.0100% | B/compra@0.42450 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-29 19:06 | SUI-USDT-SWAP | 0.88200 | 0.89970/0.86950 | 0.92920 | — | 0.01834 | 0.0005% | — | sem_zona |
| 2026-10-29 19:06 | UNI-USDT-SWAP | 6.3630 | 6.8180/6.3510 | 7.1700 | — | 0.19257 | -0.0025% | B/venda@7.2080 (1t/2c) | zona_mapeada_setup_B |
| 2026-10-29 19:06 | LINK-USDT-SWAP | 11.04 | 11.29/10.95 | 11.69 | res 12.01 (ha 5 candles) | 0.20307 | 0.0100% | — | sem_zona |
| 2026-10-29 20:06 | BTC-USDT-SWAP | 78984.4 | 79247.0/78607.2 | 80823.8 | res 81944.4 (ha 6 candles) | 714.24 | 0.0100% | B/compra@79477.9 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-29 20:06 | ETH-USDT-SWAP | 2273.4 | 2284.0/2251.1 | 2336.1 | — | 28.04 | 0.0003% | B/venda@2344.0 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-29 20:06 | SOL-USDT-SWAP | 97.01 | 97.80/96.48 | 99.77 | res 103.17 (ha 6 candles) | 1.3864 | 0.0051% | — | sem_zona |
| 2026-10-29 20:06 | XRP-USDT-SWAP | 1.2452 | 1.2589/1.2425 | 1.2816 | — | 0.01671 | 0.0012% | B/compra@1.2886 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-29 20:06 | DOGE-USDT-SWAP | 0.07612 | 0.07660/0.07544 | 0.07925 | res 0.08146 (ha 6 candles) | 0.00124 | 0.0023% | B/compra@0.07592 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-29 20:06 | ARB-USDT-SWAP | 0.15431 | 0.15659/0.15274 | 0.16820 | — | 0.00477 | -0.0028% | — | sem_zona |
| 2026-10-29 20:06 | WLD-USDT-SWAP | 0.38810 | 0.39550/0.38280 | 0.41780 | — | 0.01162 | 0.0100% | B/compra@0.42450 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-29 20:06 | SUI-USDT-SWAP | 0.88120 | 0.88950/0.87230 | 0.92920 | — | 0.01900 | -0.0045% | — | sem_zona |
| 2026-10-29 20:06 | UNI-USDT-SWAP | 6.4270 | 6.5980/6.2510 | 7.1700 | — | 0.21136 | 0.0040% | B/venda@7.2080 (1t/3c) | zona_mapeada_setup_B |
| 2026-10-29 20:06 | LINK-USDT-SWAP | 10.75 | 11.05/10.71 | 11.69 | res 12.01 (ha 6 candles) | 0.21893 | 0.0083% | — | sem_zona |
| 2026-10-29 21:06 | BTC-USDT-SWAP | 77966.9 | 79000.0/77896.4 | 77966.9 | res 81944.4 (ha 7 candles) | 771.35 | 0.0100% | B/compra@79477.9 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-29 21:06 | ETH-USDT-SWAP | 2252.5 | 2273.5/2247.5 | 2252.5 | — | 29.09 | -0.0030% | B/venda@2344.0 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-29 21:06 | SOL-USDT-SWAP | 95.58 | 97.07/95.52 | 95.58 | res 103.17 (ha 7 candles) | 1.4536 | 0.0029% | — | sem_zona |
| 2026-10-29 21:06 | XRP-USDT-SWAP | 1.2368 | 1.2482/1.2340 | 1.2368 | — | 0.01721 | -0.0005% | B/compra@1.2886 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-29 21:06 | DOGE-USDT-SWAP | 0.07522 | 0.07627/0.07506 | 0.07522 | res 0.08146 (ha 7 candles) | 0.00130 | -0.0009% | — | invalidado_setup_B |
| 2026-10-29 21:06 | ARB-USDT-SWAP | 0.15419 | 0.15585/0.15282 | 0.15419 | — | 0.00486 | -0.0045% | — | sem_zona |
| 2026-10-29 21:06 | WLD-USDT-SWAP | 0.38180 | 0.38970/0.38160 | 0.38180 | — | 0.01184 | 0.0100% | B/compra@0.42450 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-29 21:06 | SUI-USDT-SWAP | 0.86890 | 0.88390/0.86720 | 0.86890 | — | 0.01959 | -0.0049% | — | sem_zona |
| 2026-10-29 21:06 | UNI-USDT-SWAP | 6.4650 | 6.5140/6.3390 | 6.4650 | — | 0.21757 | 0.0084% | B/venda@7.2080 (1t/4c) | zona_mapeada_setup_B |
| 2026-10-29 21:06 | LINK-USDT-SWAP | 10.61 | 10.75/10.53 | 10.61 | res 12.01 (ha 7 candles) | 0.22921 | 0.0046% | — | sem_zona |
| 2026-10-29 22:06 | BTC-USDT-SWAP | 77229.6 | 78258.0/76738.8 | 77966.9 | res 81944.4 (ha 8 candles) | 860.51 | 0.0100% | B/compra@79477.9 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-29 22:06 | ETH-USDT-SWAP | 2221.6 | 2256.9/2196.2 | 2252.5 | — | 32.45 | -0.0050% | B/venda@2344.0 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-29 22:06 | SOL-USDT-SWAP | 94.77 | 95.70/92.26 | 95.58 | res 103.17 (ha 8 candles) | 1.6436 | -0.0022% | — | sem_zona |
| 2026-10-29 22:06 | XRP-USDT-SWAP | 1.2239 | 1.2397/1.2001 | 1.2368 | — | 0.01935 | -0.0045% | B/compra@1.2886 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-29 22:06 | DOGE-USDT-SWAP | 0.07429 | 0.07545/0.07204 | 0.07522 | res 0.08146 (ha 8 candles) | 0.00148 | -0.0025% | B/compra@0.07469 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-29 22:06 | ARB-USDT-SWAP | 0.15542 | 0.15547/0.14771 | 0.15419 | — | 0.00508 | -0.0059% | — | sem_zona |
| 2026-10-29 22:06 | WLD-USDT-SWAP | 0.37470 | 0.38270/0.35940 | 0.38180 | — | 0.01281 | 0.0100% | B/compra@0.42450 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-29 22:06 | SUI-USDT-SWAP | 0.85480 | 0.87370/0.82620 | 0.86890 | — | 0.02186 | -0.0101% | — | sem_zona |
| 2026-10-29 22:06 | UNI-USDT-SWAP | 6.5170 | 6.5180/6.2540 | 6.4650 | — | 0.22436 | 0.0098% | B/venda@7.2080 (1t/5c) | zona_mapeada_setup_B |
| 2026-10-29 22:06 | LINK-USDT-SWAP | 10.50 | 10.65/10.24 | 10.61 | res 12.01 (ha 8 candles) | 0.24800 | 0.0010% | — | sem_zona |
| 2026-10-29 23:06 | BTC-USDT-SWAP | 76823.8 | 77361.6/76622.9 | 77966.9 | res 81944.4 (ha 9 candles) | 899.59 | 0.0100% | B/compra@79477.9 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-29 23:06 | ETH-USDT-SWAP | 2194.7 | 2227.4/2171.5 | 2252.5 | — | 36.00 | -0.0067% | B/venda@2344.0 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-29 23:06 | SOL-USDT-SWAP | 93.92 | 94.92/93.04 | 95.58 | res 103.17 (ha 9 candles) | 1.7543 | -0.0068% | — | sem_zona |
| 2026-10-29 23:06 | XRP-USDT-SWAP | 1.2097 | 1.2251/1.1987 | 1.2368 | — | 0.02089 | -0.0043% | B/compra@1.2886 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-29 23:06 | DOGE-USDT-SWAP | 0.07400 | 0.07463/0.07331 | 0.07522 | res 0.08146 (ha 9 candles) | 0.00155 | -0.0028% | — | invalidado_setup_B |
| 2026-10-29 23:06 | ARB-USDT-SWAP | 0.15325 | 0.15569/0.15201 | 0.15419 | — | 0.00518 | -0.0045% | — | sem_zona |
| 2026-10-29 23:06 | WLD-USDT-SWAP | 0.37290 | 0.37710/0.36840 | 0.38180 | — | 0.01305 | 0.0100% | B/compra@0.42450 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-29 23:06 | SUI-USDT-SWAP | 0.85540 | 0.86380/0.84550 | 0.86890 | — | 0.02275 | -0.0113% | — | sem_zona |
| 2026-10-29 23:06 | UNI-USDT-SWAP | 6.5510 | 6.5760/6.4120 | 6.4650 | — | 0.22800 | 0.0100% | B/venda@7.2080 (1t/6c) | zona_mapeada_setup_B |
| 2026-10-29 23:06 | LINK-USDT-SWAP | 10.52 | 10.65/10.41 | 10.61 | res 12.01 (ha 9 candles) | 0.25950 | 0.0024% | — | sem_zona |
| 2026-10-30 00:06 | BTC-USDT-SWAP | 77394.2 | 77544.4/76472.0 | 77966.9 | res 81944.4 (ha 10 candles) | 956.80 | 0.0100% | B/compra@79477.9 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-30 00:06 | ETH-USDT-SWAP | 2209.4 | 2218.6/2180.0 | 2252.5 | — | 37.90 | -0.0083% | B/venda@2344.0 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-30 00:06 | SOL-USDT-SWAP | 95.33 | 95.42/93.42 | 95.58 | res 103.17 (ha 10 candles) | 1.8514 | -0.0144% | — | sem_zona |
| 2026-10-30 00:06 | XRP-USDT-SWAP | 1.2202 | 1.2257/1.2057 | 1.2368 | — | 0.02179 | -0.0070% | B/compra@1.2886 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-30 00:06 | DOGE-USDT-SWAP | 0.07494 | 0.07522/0.07357 | 0.07522 | res 0.08146 (ha 10 candles) | 0.00163 | -0.0048% | B/compra@0.07592 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-30 00:06 | ARB-USDT-SWAP | 0.15600 | 0.15633/0.15257 | 0.15419 | — | 0.00519 | -0.0012% | — | sem_zona |
| 2026-10-30 00:06 | WLD-USDT-SWAP | 0.37990 | 0.38120/0.37000 | 0.38180 | — | 0.01350 | 0.0077% | — | zona_expirada_setup_B |
| 2026-10-30 00:06 | SUI-USDT-SWAP | 0.86590 | 0.87010/0.84810 | 0.86890 | — | 0.02361 | -0.0117% | — | sem_zona |
| 2026-10-30 00:06 | UNI-USDT-SWAP | 6.6120 | 6.6740/6.4790 | 6.4650 | — | 0.23521 | 0.0032% | B/venda@7.2080 (1t/7c) | zona_mapeada_setup_B |
| 2026-10-30 00:06 | LINK-USDT-SWAP | 10.71 | 10.73/10.47 | 10.61 | res 12.01 (ha 10 candles) | 0.27143 | 0.0004% | — | sem_zona |
| 2026-10-30 01:06 | BTC-USDT-SWAP | 78200.1 | 78224.0/77281.0 | 78200.1 | res 81944.4 (ha 11 candles) | 986.39 | 0.0100% | B/compra@79477.9 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-30 01:06 | ETH-USDT-SWAP | 2236.4 | 2238.0/2208.3 | 2236.4 | — | 38.66 | -0.0087% | — | zona_expirada_setup_B |
| 2026-10-30 01:06 | SOL-USDT-SWAP | 97.12 | 97.17/95.27 | 97.12 | res 103.17 (ha 11 candles) | 1.9279 | -0.0220% | B/compra@98.54 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-30 01:06 | XRP-USDT-SWAP | 1.2460 | 1.2481/1.2195 | 1.2460 | — | 0.02315 | -0.0114% | — | zona_expirada_setup_B |
| 2026-10-30 01:06 | DOGE-USDT-SWAP | 0.07603 | 0.07611/0.07491 | 0.07603 | res 0.08146 (ha 11 candles) | 0.00167 | -0.0063% | — | descartado_rr_baixo_setup_B |
| 2026-10-30 01:06 | ARB-USDT-SWAP | 0.15798 | 0.15847/0.15530 | 0.15798 | — | 0.00515 | -0.0006% | — | sem_zona |
| 2026-10-30 01:06 | WLD-USDT-SWAP | 0.38720 | 0.38840/0.37940 | 0.38720 | — | 0.01367 | -0.0122% | — | sem_zona |
| 2026-10-30 01:06 | SUI-USDT-SWAP | 0.88370 | 0.88640/0.86550 | 0.88370 | — | 0.02430 | -0.0129% | B/compra@0.90000 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-30 01:06 | UNI-USDT-SWAP | 6.7250 | 6.7600/6.5910 | 6.7250 | — | 0.23686 | -0.0002% | — | zona_expirada_setup_B |
| 2026-10-30 01:06 | LINK-USDT-SWAP | 10.95 | 10.97/10.70 | 10.95 | res 12.01 (ha 11 candles) | 0.28143 | -0.0027% | — | sem_zona |
| 2026-10-30 02:06 | BTC-USDT-SWAP | 78225.1 | 78420.0/77883.3 | 78200.1 | res 81944.4 (ha 12 candles) | 932.53 | 0.0100% | B/compra@79477.9 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-30 02:06 | ETH-USDT-SWAP | 2242.4 | 2246.7/2223.8 | 2236.4 | — | 38.08 | -0.0092% | — | sem_zona |
| 2026-10-30 02:06 | SOL-USDT-SWAP | 97.16 | 97.57/96.66 | 97.12 | res 103.17 (ha 12 candles) | 1.8729 | -0.0270% | B/compra@98.54 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-30 02:06 | XRP-USDT-SWAP | 1.2533 | 1.2559/1.2413 | 1.2460 | — | 0.02285 | -0.0126% | B/compra@1.2539 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-30 02:06 | DOGE-USDT-SWAP | 0.07609 | 0.07634/0.07554 | 0.07603 | res 0.08146 (ha 12 candles) | 0.00162 | -0.0066% | B/compra@0.07661 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-30 02:06 | ARB-USDT-SWAP | 0.16371 | 0.16385/0.15761 | 0.15798 | — | 0.00529 | 0.0002% | B/compra@0.16447 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-30 02:06 | WLD-USDT-SWAP | 0.39150 | 0.39280/0.38380 | 0.38720 | — | 0.01344 | -0.0321% | — | sem_zona |
| 2026-10-30 02:06 | SUI-USDT-SWAP | 0.89420 | 0.89630/0.87750 | 0.88370 | — | 0.02403 | -0.0097% | — | descartado_rr_baixo_setup_B |
| 2026-10-30 02:06 | UNI-USDT-SWAP | 6.7950 | 6.8180/6.6680 | 6.7250 | — | 0.23629 | 0.0009% | B/venda@6.8950 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-30 02:06 | LINK-USDT-SWAP | 11.05 | 11.08/10.90 | 10.95 | res 12.01 (ha 12 candles) | 0.27929 | -0.0068% | B/compra@11.22 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-30 03:06 | BTC-USDT-SWAP | 78504.2 | 78737.7/78191.5 | 78200.1 | res 81944.4 (ha 13 candles) | 918.91 | 0.0100% | — | zona_expirada_setup_B |
| 2026-10-30 03:06 | ETH-USDT-SWAP | 2237.9 | 2253.0/2237.0 | 2236.4 | — | 37.17 | -0.0078% | — | sem_zona |
| 2026-10-30 03:06 | SOL-USDT-SWAP | 97.87 | 98.50/97.12 | 97.12 | res 103.17 (ha 13 candles) | 1.8986 | -0.0291% | — | invalidado_setup_B |
| 2026-10-30 03:06 | XRP-USDT-SWAP | 1.2559 | 1.2617/1.2522 | 1.2460 | — | 0.02276 | -0.0128% | B/compra@1.2539 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-30 03:06 | DOGE-USDT-SWAP | 0.07610 | 0.07659/0.07602 | 0.07603 | res 0.08146 (ha 13 candles) | 0.00159 | -0.0037% | — | invalidado_setup_B |
| 2026-10-30 03:06 | ARB-USDT-SWAP | 0.16391 | 0.16648/0.16355 | 0.15798 | — | 0.00523 | 0.0083% | B/compra@0.16447 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-30 03:06 | WLD-USDT-SWAP | 0.39540 | 0.39980/0.39130 | 0.38720 | — | 0.01309 | -0.0495% | — | sem_zona |
| 2026-10-30 03:06 | SUI-USDT-SWAP | 0.89010 | 0.90450/0.88980 | 0.88370 | — | 0.02406 | -0.0029% | — | sem_zona |
| 2026-10-30 03:06 | UNI-USDT-SWAP | 6.7460 | 6.8800/6.7440 | 6.7250 | — | 0.23436 | 0.0023% | — | descartado_rr_baixo_setup_B |
| 2026-10-30 03:06 | LINK-USDT-SWAP | 11.05 | 11.15/11.04 | 10.95 | res 12.01 (ha 13 candles) | 0.27379 | -0.0068% | — | invalidado_setup_B |
| 2026-10-30 04:06 | BTC-USDT-SWAP | 78603.7 | 78767.0/78350.9 | 78200.1 | res 81944.4 (ha 14 candles) | 892.16 | 0.0086% | B/compra@79168.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-30 04:06 | ETH-USDT-SWAP | 2252.7 | 2258.1/2233.9 | 2236.4 | — | 36.86 | -0.0073% | — | sem_zona |
| 2026-10-30 04:06 | SOL-USDT-SWAP | 98.22 | 98.49/97.67 | 97.12 | res 103.17 (ha 14 candles) | 1.8543 | -0.0285% | B/compra@99.11 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-30 04:06 | XRP-USDT-SWAP | 1.2664 | 1.2736/1.2540 | 1.2460 | — | 0.02269 | -0.0146% | — | descartado_rr_baixo_setup_B |
| 2026-10-30 04:06 | DOGE-USDT-SWAP | 0.07643 | 0.07681/0.07602 | 0.07603 | res 0.08146 (ha 14 candles) | 0.00154 | -0.0010% | B/compra@0.07592 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-30 04:06 | ARB-USDT-SWAP | 0.16460 | 0.16661/0.16300 | 0.15798 | — | 0.00515 | 0.0100% | B/compra@0.16447 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-30 04:06 | WLD-USDT-SWAP | 0.39650 | 0.40120/0.39490 | 0.38720 | — | 0.01271 | -0.0562% | — | sem_zona |
| 2026-10-30 04:06 | SUI-USDT-SWAP | 0.89550 | 0.90200/0.88680 | 0.88370 | — | 0.02377 | 0.0012% | B/compra@0.91080 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-30 04:06 | UNI-USDT-SWAP | 6.8150 | 6.8760/6.7250 | 6.7250 | — | 0.23307 | 0.0022% | B/compra@6.9410 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-30 04:06 | LINK-USDT-SWAP | 11.12 | 11.18/11.02 | 10.95 | res 12.01 (ha 14 candles) | 0.27093 | -0.0069% | — | sem_zona |
| 2026-10-30 05:06 | BTC-USDT-SWAP | 78138.6 | 78610.0/78009.4 | 78138.6 | res 81944.4 (ha 15 candles) | 892.92 | 0.0053% | B/compra@79168.0 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-30 05:06 | ETH-USDT-SWAP | 2235.8 | 2253.9/2226.8 | 2235.8 | sup 2171.5 (ha 6 candles) | 37.11 | -0.0079% | — | sem_zona |
| 2026-10-30 05:06 | SOL-USDT-SWAP | 97.26 | 98.22/96.91 | 97.26 | — | 1.8600 | -0.0252% | B/compra@99.11 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-30 05:06 | XRP-USDT-SWAP | 1.2501 | 1.2667/1.2478 | 1.2501 | — | 0.02310 | -0.0156% | — | sem_zona |
| 2026-10-30 05:06 | DOGE-USDT-SWAP | 0.07560 | 0.07644/0.07545 | 0.07560 | res 0.08146 (ha 15 candles) | 0.00153 | -0.0001% | B/compra@0.07592 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-30 05:06 | ARB-USDT-SWAP | 0.16485 | 0.16562/0.16328 | 0.16485 | sup 0.14771 (ha 7 candles) | 0.00499 | 0.0100% | — | invalidado_tendencia_virou_setup_B |
| 2026-10-30 05:06 | WLD-USDT-SWAP | 0.39240 | 0.39670/0.38950 | 0.39240 | sup 0.35940 (ha 7 candles) | 0.01211 | -0.0484% | — | sem_zona |
| 2026-10-30 05:06 | SUI-USDT-SWAP | 0.88490 | 0.89680/0.88130 | 0.88490 | sup 0.82620 (ha 7 candles) | 0.02346 | 0.0005% | B/compra@0.91080 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-30 05:06 | UNI-USDT-SWAP | 6.6920 | 6.8230/6.6620 | 6.6920 | — | 0.23207 | 0.0063% | B/compra@6.9410 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-30 05:06 | LINK-USDT-SWAP | 11.04 | 11.14/11.00 | 11.04 | res 12.01 (ha 15 candles) | 0.26650 | -0.0066% | — | sem_zona |
| 2026-10-30 06:06 | BTC-USDT-SWAP | 77993.9 | 78215.3/77860.0 | 78138.6 | res 81944.4 (ha 16 candles) | 891.83 | 0.0055% | B/compra@79168.0 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-30 06:06 | ETH-USDT-SWAP | 2228.0 | 2236.8/2222.9 | 2235.8 | sup 2171.5 (ha 7 candles) | 36.76 | -0.0056% | — | sem_zona |
| 2026-10-30 06:06 | SOL-USDT-SWAP | 97.31 | 97.54/96.82 | 97.26 | — | 1.8471 | -0.0227% | B/compra@99.11 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-30 06:06 | XRP-USDT-SWAP | 1.2557 | 1.2581/1.2474 | 1.2501 | — | 0.02269 | -0.0154% | B/compra@1.2723 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-30 06:06 | DOGE-USDT-SWAP | 0.07560 | 0.07607/0.07532 | 0.07560 | res 0.08146 (ha 16 candles) | 0.00154 | -0.0004% | B/compra@0.07592 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-30 06:06 | ARB-USDT-SWAP | 0.16291 | 0.16568/0.16228 | 0.16485 | sup 0.14771 (ha 8 candles) | 0.00502 | 0.0100% | — | sem_zona |
| 2026-10-30 06:06 | WLD-USDT-SWAP | 0.39630 | 0.39730/0.39070 | 0.39240 | sup 0.35940 (ha 8 candles) | 0.01201 | -0.0449% | — | sem_zona |
| 2026-10-30 06:06 | SUI-USDT-SWAP | 0.88270 | 0.88780/0.87970 | 0.88490 | sup 0.82620 (ha 8 candles) | 0.02316 | -0.0019% | B/compra@0.91080 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-30 06:06 | UNI-USDT-SWAP | 6.7350 | 6.7430/6.6550 | 6.6920 | — | 0.22929 | 0.0089% | B/compra@6.9410 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-30 06:06 | LINK-USDT-SWAP | 11.01 | 11.11/10.99 | 11.04 | res 12.01 (ha 16 candles) | 0.26550 | -0.0039% | — | sem_zona |
| 2026-10-30 07:06 | BTC-USDT-SWAP | 77645.2 | 78010.0/77510.0 | 78138.6 | res 78767.0 (ha 3 candles) | 914.07 | 0.0068% | B/compra@79168.0 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-30 07:06 | ETH-USDT-SWAP | 2228.6 | 2231.3/2220.0 | 2235.8 | sup 2171.5 (ha 8 candles) | 36.62 | -0.0021% | — | sem_zona |
| 2026-10-30 07:06 | SOL-USDT-SWAP | 96.80 | 97.42/96.62 | 97.26 | — | 1.8436 | -0.0145% | B/compra@99.11 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-30 07:06 | XRP-USDT-SWAP | 1.2530 | 1.2624/1.2508 | 1.2501 | — | 0.02301 | -0.0143% | B/compra@1.2723 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-30 07:06 | DOGE-USDT-SWAP | 0.07548 | 0.07576/0.07522 | 0.07560 | res 0.07681 (ha 3 candles) | 0.00154 | 0.0025% | — | invalidado_setup_B |
| 2026-10-30 07:06 | ARB-USDT-SWAP | 0.16210 | 0.16314/0.16120 | 0.16485 | sup 0.14771 (ha 9 candles) | 0.00505 | 0.0100% | — | sem_zona |
| 2026-10-30 07:06 | WLD-USDT-SWAP | 0.40270 | 0.40340/0.39440 | 0.39240 | sup 0.35940 (ha 9 candles) | 0.01239 | -0.0386% | — | sem_zona |
| 2026-10-30 07:06 | SUI-USDT-SWAP | 0.88570 | 0.88630/0.87880 | 0.88490 | sup 0.82620 (ha 9 candles) | 0.02323 | 0.0030% | B/compra@0.91080 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-30 07:06 | UNI-USDT-SWAP | 6.7840 | 6.7870/6.6670 | 6.6920 | — | 0.23450 | 0.0100% | B/compra@6.9410 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-30 07:06 | LINK-USDT-SWAP | 11.04 | 11.04/10.95 | 11.04 | res 11.18 (ha 3 candles) | 0.26486 | 0.0019% | — | sem_zona |
| 2026-10-30 08:06 | BTC-USDT-SWAP | 77797.3 | 77799.8/77302.5 | 78138.6 | res 78767.0 (ha 4 candles) | 764.37 | 0.0100% | B/compra@79168.0 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-30 08:06 | ETH-USDT-SWAP | 2248.6 | 2249.6/2220.4 | 2235.8 | sup 2171.5 (ha 9 candles) | 31.20 | 0.0016% | — | sem_zona |
| 2026-10-30 08:06 | SOL-USDT-SWAP | 97.27 | 97.31/96.24 | 97.26 | — | 1.5579 | -0.0041% | B/compra@99.11 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-30 08:06 | XRP-USDT-SWAP | 1.2580 | 1.2594/1.2435 | 1.2501 | — | 0.01976 | -0.0100% | B/compra@1.2723 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-30 08:06 | DOGE-USDT-SWAP | 0.07610 | 0.07611/0.07518 | 0.07560 | res 0.07681 (ha 4 candles) | 0.00124 | 0.0049% | B/compra@0.07661 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-30 08:06 | ARB-USDT-SWAP | 0.16402 | 0.16427/0.16124 | 0.16485 | sup 0.14771 (ha 10 candles) | 0.00402 | 0.0100% | — | sem_zona |
| 2026-10-30 08:06 | WLD-USDT-SWAP | 0.40600 | 0.40670/0.39780 | 0.39240 | sup 0.35940 (ha 10 candles) | 0.01009 | -0.0301% | — | sem_zona |
| 2026-10-30 08:06 | SUI-USDT-SWAP | 0.89470 | 0.89490/0.88120 | 0.88490 | sup 0.82620 (ha 10 candles) | 0.01902 | 0.0056% | B/compra@0.91080 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-30 08:06 | UNI-USDT-SWAP | 6.8510 | 6.8550/6.7360 | 6.6920 | — | 0.19329 | 0.0100% | B/compra@6.9410 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-30 08:06 | LINK-USDT-SWAP | 11.13 | 11.14/10.98 | 11.04 | res 11.18 (ha 4 candles) | 0.21821 | 0.0076% | — | sem_zona |
| 2026-10-30 09:06 | BTC-USDT-SWAP | 77343.7 | 77834.3/77188.0 | 77343.7 | res 78767.0 (ha 5 candles) | 722.51 | 0.0100% | B/compra@79168.0 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-30 09:06 | ETH-USDT-SWAP | 2235.3 | 2252.7/2228.8 | 2235.3 | sup 2171.5 (ha 10 candles) | 29.43 | 0.0016% | — | sem_zona |
| 2026-10-30 09:06 | SOL-USDT-SWAP | 96.51 | 97.35/96.25 | 96.51 | — | 1.4429 | 0.0036% | B/compra@99.11 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-30 09:06 | XRP-USDT-SWAP | 1.2456 | 1.2602/1.2447 | 1.2456 | — | 0.01868 | -0.0063% | B/compra@1.2723 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-30 09:06 | DOGE-USDT-SWAP | 0.07575 | 0.07619/0.07552 | 0.07575 | res 0.07681 (ha 5 candles) | 0.00114 | 0.0063% | B/compra@0.07661 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-30 09:06 | ARB-USDT-SWAP | 0.16425 | 0.16455/0.16272 | 0.16425 | sup 0.14771 (ha 11 candles) | 0.00361 | 0.0100% | — | sem_zona |
| 2026-10-30 09:06 | WLD-USDT-SWAP | 0.40260 | 0.40760/0.40190 | 0.40260 | sup 0.35940 (ha 11 candles) | 0.00959 | -0.0226% | — | sem_zona |
| 2026-10-30 09:06 | SUI-USDT-SWAP | 0.88530 | 0.89630/0.88280 | 0.88530 | sup 0.82620 (ha 11 candles) | 0.01783 | 0.0072% | B/compra@0.91080 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-30 09:06 | UNI-USDT-SWAP | 6.8700 | 6.9580/6.8430 | 6.8700 | — | 0.16814 | 0.0100% | — | invalidado_setup_B |
| 2026-10-30 09:06 | LINK-USDT-SWAP | 11.07 | 11.17/11.03 | 11.07 | res 11.18 (ha 5 candles) | 0.20329 | 0.0100% | — | sem_zona |
| 2026-10-30 10:06 | BTC-USDT-SWAP | 77436.0 | 77568.3/77241.6 | 77343.7 | res 78767.0 (ha 6 candles) | 700.15 | 0.0100% | B/compra@79168.0 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-30 10:06 | ETH-USDT-SWAP | 2233.8 | 2240.5/2227.2 | 2235.3 | sup 2220.0 (ha 3 candles) | 28.03 | 0.0021% | — | sem_zona |
| 2026-10-30 10:06 | SOL-USDT-SWAP | 96.82 | 96.84/96.36 | 96.51 | — | 1.3829 | 0.0090% | B/compra@99.11 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-30 10:06 | XRP-USDT-SWAP | 1.2477 | 1.2498/1.2431 | 1.2456 | — | 0.01799 | -0.0056% | B/compra@1.2723 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-30 10:06 | DOGE-USDT-SWAP | 0.07592 | 0.07602/0.07567 | 0.07575 | res 0.07681 (ha 6 candles) | 0.00108 | 0.0074% | B/compra@0.07661 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-30 10:06 | ARB-USDT-SWAP | 0.16497 | 0.16603/0.16390 | 0.16425 | sup 0.16120 (ha 3 candles) | 0.00349 | 0.0100% | — | sem_zona |
| 2026-10-30 10:06 | WLD-USDT-SWAP | 0.40540 | 0.40540/0.39950 | 0.40260 | sup 0.35940 (ha 12 candles) | 0.00910 | -0.0123% | — | sem_zona |
| 2026-10-30 10:06 | SUI-USDT-SWAP | 0.88660 | 0.88920/0.88360 | 0.88530 | sup 0.87880 (ha 3 candles) | 0.01700 | 0.0073% | B/compra@0.91080 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-30 10:06 | UNI-USDT-SWAP | 6.9350 | 6.9790/6.8620 | 6.8700 | — | 0.15171 | 0.0100% | B/compra@6.8830 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-30 10:06 | LINK-USDT-SWAP | 11.08 | 11.13/11.04 | 11.07 | res 11.18 (ha 6 candles) | 0.18571 | 0.0100% | — | sem_zona |
| 2026-10-30 11:06 | BTC-USDT-SWAP | 77130.1 | 77436.0/76567.0 | 77343.7 | res 78767.0 (ha 7 candles) | 683.39 | 0.0100% | B/compra@79168.0 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-30 11:06 | ETH-USDT-SWAP | 2224.6 | 2234.9/2205.8 | 2235.3 | sup 2220.0 (ha 4 candles) | 28.26 | 0.0029% | — | sem_zona |
| 2026-10-30 11:06 | SOL-USDT-SWAP | 95.25 | 96.82/94.51 | 96.51 | — | 1.4371 | 0.0100% | B/compra@99.11 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-30 11:06 | XRP-USDT-SWAP | 1.2425 | 1.2483/1.2327 | 1.2456 | — | 0.01809 | -0.0046% | B/compra@1.2723 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-30 11:06 | DOGE-USDT-SWAP | 0.07547 | 0.07595/0.07487 | 0.07575 | res 0.07681 (ha 7 candles) | 0.00107 | 0.0086% | B/compra@0.07661 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-30 11:06 | ARB-USDT-SWAP | 0.16352 | 0.16514/0.16155 | 0.16425 | sup 0.16120 (ha 4 candles) | 0.00353 | 0.0100% | — | sem_zona |
| 2026-10-30 11:06 | WLD-USDT-SWAP | 0.39900 | 0.40550/0.39400 | 0.40260 | sup 0.35940 (ha 13 candles) | 0.00934 | -0.0074% | — | sem_zona |
| 2026-10-30 11:06 | SUI-USDT-SWAP | 0.88350 | 0.88730/0.87630 | 0.88530 | sup 0.87880 (ha 4 candles) | 0.01659 | 0.0055% | B/compra@0.91080 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-30 11:06 | UNI-USDT-SWAP | 6.8610 | 6.9500/6.7780 | 6.8700 | — | 0.15150 | 0.0100% | B/compra@6.8830 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-30 11:06 | LINK-USDT-SWAP | 11.00 | 11.08/10.91 | 11.07 | res 11.18 (ha 7 candles) | 0.18207 | 0.0100% | — | sem_zona |
| 2026-10-30 12:06 | BTC-USDT-SWAP | 77199.6 | 77284.8/76627.4 | 77343.7 | res 78767.0 (ha 8 candles) | 621.84 | 0.0100% | — | zona_expirada_setup_B |
| 2026-10-30 12:06 | ETH-USDT-SWAP | 2236.3 | 2238.6/2213.0 | 2235.3 | sup 2220.0 (ha 5 candles) | 25.75 | 0.0026% | — | sem_zona |
| 2026-10-30 12:06 | SOL-USDT-SWAP | 94.49 | 95.29/93.85 | 96.51 | — | 1.2943 | 0.0100% | — | zona_expirada_setup_B |
| 2026-10-30 12:06 | XRP-USDT-SWAP | 1.2428 | 1.2449/1.2280 | 1.2456 | — | 0.01646 | -0.0036% | B/compra@1.2723 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-30 12:06 | DOGE-USDT-SWAP | 0.07568 | 0.07583/0.07479 | 0.07575 | res 0.07619 (ha 3 candles) | 0.00091 | 0.0089% | B/compra@0.07661 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-30 12:06 | ARB-USDT-SWAP | 0.16355 | 0.16435/0.16163 | 0.16425 | sup 0.16120 (ha 5 candles) | 0.00317 | 0.0100% | — | sem_zona |
| 2026-10-30 12:06 | WLD-USDT-SWAP | 0.40340 | 0.40830/0.39660 | 0.40260 | sup 0.35940 (ha 14 candles) | 0.00851 | -0.0111% | — | sem_zona |
| 2026-10-30 12:06 | SUI-USDT-SWAP | 0.89070 | 0.89410/0.87530 | 0.88530 | sup 0.87880 (ha 5 candles) | 0.01454 | 0.0042% | — | zona_expirada_setup_B |
| 2026-10-30 12:06 | UNI-USDT-SWAP | 6.9470 | 6.9560/6.7910 | 6.8700 | — | 0.14443 | 0.0087% | — | descartado_rr_baixo_setup_B |
| 2026-10-30 12:06 | LINK-USDT-SWAP | 11.12 | 11.13/10.89 | 11.07 | res 11.17 (ha 3 candles) | 0.17057 | 0.0074% | B/compra@11.22 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-30 13:06 | BTC-USDT-SWAP | 77570.1 | 78070.0/77181.8 | 77570.1 | — | 632.51 | 0.0100% | — | sem_zona |
| 2026-10-30 13:06 | ETH-USDT-SWAP | 2225.5 | 2261.6/2219.6 | 2225.5 | sup 2220.0 (ha 6 candles) | 24.76 | -0.0001% | — | sem_zona |
| 2026-10-30 13:06 | SOL-USDT-SWAP | 94.80 | 95.82/94.04 | 94.80 | sup 92.26 (ha 15 candles) | 1.2871 | 0.0100% | — | sem_zona |
| 2026-10-30 13:06 | XRP-USDT-SWAP | 1.2537 | 1.2615/1.2416 | 1.2537 | sup 1.1987 (ha 14 candles) | 0.01600 | -0.0115% | B/compra@1.2723 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-30 13:06 | DOGE-USDT-SWAP | 0.07582 | 0.07663/0.07546 | 0.07582 | — | 0.00089 | 0.0073% | — | invalidado_setup_B |
| 2026-10-30 13:06 | ARB-USDT-SWAP | 0.16208 | 0.16596/0.16080 | 0.16208 | sup 0.16120 (ha 6 candles) | 0.00327 | 0.0100% | — | sem_zona |
| 2026-10-30 13:06 | WLD-USDT-SWAP | 0.41140 | 0.41370/0.40330 | 0.41140 | sup 0.35940 (ha 15 candles) | 0.00864 | -0.0200% | — | sem_zona |
| 2026-10-30 13:06 | SUI-USDT-SWAP | 0.88870 | 0.90820/0.88080 | 0.88870 | sup 0.87880 (ha 6 candles) | 0.01519 | -0.0010% | — | sem_zona |
| 2026-10-30 13:06 | UNI-USDT-SWAP | 6.9420 | 7.1430/6.8930 | 6.9420 | — | 0.15057 | 0.0068% | B/venda@6.8950 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-30 13:06 | LINK-USDT-SWAP | 11.05 | 11.28/11.00 | 11.05 | — | 0.17393 | 0.0010% | — | invalidado_setup_B |
| 2026-10-30 14:06 | BTC-USDT-SWAP | 77302.8 | 77646.0/77066.7 | 77570.1 | — | 597.29 | 0.0100% | — | sem_zona |
| 2026-10-30 14:06 | ETH-USDT-SWAP | 2231.7 | 2237.9/2215.6 | 2225.5 | sup 2205.8 (ha 3 candles) | 23.60 | -0.0042% | — | sem_zona |
| 2026-10-30 14:06 | SOL-USDT-SWAP | 94.88 | 95.35/94.31 | 94.80 | sup 92.26 (ha 16 candles) | 1.2186 | 0.0071% | — | sem_zona |
| 2026-10-30 14:06 | XRP-USDT-SWAP | 1.2453 | 1.2538/1.2426 | 1.2537 | sup 1.1987 (ha 15 candles) | 0.01537 | -0.0146% | — | zona_expirada_setup_B |
| 2026-10-30 14:06 | DOGE-USDT-SWAP | 0.07556 | 0.07603/0.07535 | 0.07582 | — | 0.00083 | 0.0080% | B/compra@0.07592 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-30 14:06 | ARB-USDT-SWAP | 0.16216 | 0.16381/0.16130 | 0.16208 | sup 0.16120 (ha 7 candles) | 0.00319 | 0.0079% | — | sem_zona |
| 2026-10-30 14:06 | WLD-USDT-SWAP | 0.41340 | 0.41460/0.40800 | 0.41140 | sup 0.39400 (ha 3 candles) | 0.00831 | -0.0505% | — | sem_zona |
| 2026-10-30 14:06 | SUI-USDT-SWAP | 0.89060 | 0.89800/0.88400 | 0.88870 | sup 0.87880 (ha 7 candles) | 0.01462 | -0.0061% | — | sem_zona |
| 2026-10-30 14:06 | UNI-USDT-SWAP | 6.9710 | 7.0410/6.8880 | 6.9420 | — | 0.14757 | 0.0087% | — | invalidado_setup_B |
| 2026-10-30 14:06 | LINK-USDT-SWAP | 11.19 | 11.21/11.01 | 11.05 | — | 0.16979 | -0.0046% | — | sem_zona |
| 2026-10-30 15:06 | BTC-USDT-SWAP | 77135.1 | 77446.2/77056.0 | 77570.1 | — | 557.81 | 0.0100% | — | sem_zona |
| 2026-10-30 15:06 | ETH-USDT-SWAP | 2242.4 | 2246.5/2231.1 | 2225.5 | sup 2205.8 (ha 4 candles) | 22.58 | -0.0055% | — | sem_zona |
| 2026-10-30 15:06 | SOL-USDT-SWAP | 94.39 | 95.13/94.10 | 94.80 | sup 93.85 (ha 3 candles) | 1.1564 | 0.0039% | — | sem_zona |
| 2026-10-30 15:06 | XRP-USDT-SWAP | 1.2442 | 1.2513/1.2423 | 1.2537 | sup 1.2280 (ha 3 candles) | 0.01397 | -0.0167% | — | sem_zona |
| 2026-10-30 15:06 | DOGE-USDT-SWAP | 0.07535 | 0.07599/0.07524 | 0.07582 | — | 0.00079 | 0.0079% | — | invalidado_setup_B |
| 2026-10-30 15:06 | ARB-USDT-SWAP | 0.16300 | 0.16409/0.16211 | 0.16208 | sup 0.16120 (ha 8 candles) | 0.00310 | 0.0086% | — | sem_zona |
| 2026-10-30 15:06 | WLD-USDT-SWAP | 0.41400 | 0.41630/0.40840 | 0.41140 | sup 0.39400 (ha 4 candles) | 0.00823 | -0.1111% | — | sem_zona |
| 2026-10-30 15:06 | SUI-USDT-SWAP | 0.88770 | 0.89430/0.88440 | 0.88870 | sup 0.87530 (ha 3 candles) | 0.01384 | -0.0086% | — | sem_zona |
| 2026-10-30 15:06 | UNI-USDT-SWAP | 6.9530 | 7.0130/6.9180 | 6.9420 | — | 0.14229 | 0.0086% | B/compra@6.9410 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-30 15:06 | LINK-USDT-SWAP | 11.18 | 11.25/11.15 | 11.05 | — | 0.15807 | -0.0092% | B/compra@11.26 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-30 16:06 | BTC-USDT-SWAP | 76598.1 | 77159.8/76260.0 | 77570.1 | — | 583.74 | 0.0100% | — | sem_zona |
| 2026-10-30 16:06 | ETH-USDT-SWAP | 2230.3 | 2245.2/2217.0 | 2225.5 | sup 2205.8 (ha 5 candles) | 22.96 | -0.0081% | — | sem_zona |
| 2026-10-30 16:06 | SOL-USDT-SWAP | 94.18 | 94.56/93.52 | 94.80 | sup 93.85 (ha 4 candles) | 1.1657 | 0.0024% | — | sem_zona |
| 2026-10-30 16:06 | XRP-USDT-SWAP | 1.2398 | 1.2446/1.2327 | 1.2537 | sup 1.2280 (ha 4 candles) | 0.01378 | -0.0179% | — | sem_zona |
| 2026-10-30 16:06 | DOGE-USDT-SWAP | 0.07483 | 0.07546/0.07440 | 0.07582 | — | 0.00081 | 0.0067% | B/compra@0.07469 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-30 16:06 | ARB-USDT-SWAP | 0.16129 | 0.16388/0.16026 | 0.16208 | sup 0.16120 (ha 9 candles) | 0.00291 | 0.0082% | — | sem_zona |
| 2026-10-30 16:06 | WLD-USDT-SWAP | 0.40290 | 0.41790/0.39940 | 0.41140 | sup 0.39400 (ha 5 candles) | 0.00891 | -0.1027% | — | sem_zona |
| 2026-10-30 16:06 | SUI-USDT-SWAP | 0.88080 | 0.89020/0.87440 | 0.88870 | sup 0.87530 (ha 4 candles) | 0.01362 | -0.0102% | — | sem_zona |
| 2026-10-30 16:06 | UNI-USDT-SWAP | 6.9040 | 6.9610/6.8380 | 6.9420 | — | 0.14036 | 0.0100% | — | invalidado_setup_B |
| 2026-10-30 16:06 | LINK-USDT-SWAP | 11.15 | 11.21/11.07 | 11.05 | — | 0.15557 | -0.0138% | B/compra@11.26 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-30 17:06 | BTC-USDT-SWAP | 76876.2 | 76993.9/76300.0 | 76876.2 | — | 594.29 | 0.0100% | — | sem_zona |
| 2026-10-30 17:06 | ETH-USDT-SWAP | 2237.7 | 2241.4/2220.6 | 2237.7 | sup 2205.8 (ha 6 candles) | 23.31 | -0.0108% | — | sem_zona |
| 2026-10-30 17:06 | SOL-USDT-SWAP | 94.68 | 94.88/94.00 | 94.68 | sup 93.85 (ha 5 candles) | 1.1300 | -0.0013% | — | sem_zona |
| 2026-10-30 17:06 | XRP-USDT-SWAP | 1.2496 | 1.2507/1.2371 | 1.2496 | sup 1.2280 (ha 5 candles) | 0.01407 | -0.0195% | — | sem_zona |
| 2026-10-30 17:06 | DOGE-USDT-SWAP | 0.07537 | 0.07547/0.07451 | 0.07537 | — | 0.00084 | 0.0072% | — | descartado_rr_baixo_setup_B |
| 2026-10-30 17:06 | ARB-USDT-SWAP | 0.16328 | 0.16351/0.16086 | 0.16328 | sup 0.16120 (ha 10 candles) | 0.00289 | 0.0090% | — | sem_zona |
| 2026-10-30 17:06 | WLD-USDT-SWAP | 0.40720 | 0.40910/0.40210 | 0.40720 | sup 0.39400 (ha 6 candles) | 0.00880 | -0.0792% | — | sem_zona |
| 2026-10-30 17:06 | SUI-USDT-SWAP | 0.89140 | 0.89270/0.87800 | 0.89140 | sup 0.87530 (ha 5 candles) | 0.01362 | -0.0095% | — | sem_zona |
| 2026-10-30 17:06 | UNI-USDT-SWAP | 6.9500 | 6.9780/6.8700 | 6.9500 | — | 0.13836 | 0.0100% | B/compra@6.8830 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-30 17:06 | LINK-USDT-SWAP | 11.12 | 11.19/11.09 | 11.12 | — | 0.15450 | -0.0145% | B/compra@11.26 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-30 18:06 | BTC-USDT-SWAP | 76870.2 | 77125.1/76745.7 | 76876.2 | — | 591.67 | 0.0100% | — | sem_zona |
| 2026-10-30 18:06 | ETH-USDT-SWAP | 2237.5 | 2245.0/2234.4 | 2237.7 | sup 2205.8 (ha 7 candles) | 22.33 | -0.0132% | — | sem_zona |
| 2026-10-30 18:06 | SOL-USDT-SWAP | 95.14 | 95.18/94.61 | 94.68 | sup 93.85 (ha 6 candles) | 1.1121 | -0.0052% | — | sem_zona |
| 2026-10-30 18:06 | XRP-USDT-SWAP | 1.2496 | 1.2517/1.2463 | 1.2496 | sup 1.2280 (ha 6 candles) | 0.01306 | -0.0196% | — | sem_zona |
| 2026-10-30 18:06 | DOGE-USDT-SWAP | 0.07542 | 0.07559/0.07513 | 0.07537 | — | 0.00082 | 0.0073% | B/compra@0.07592 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-30 18:06 | ARB-USDT-SWAP | 0.16214 | 0.16430/0.16081 | 0.16328 | sup 0.16120 (ha 11 candles) | 0.00288 | 0.0084% | — | sem_zona |
| 2026-10-30 18:06 | WLD-USDT-SWAP | 0.40450 | 0.40960/0.39940 | 0.40720 | sup 0.39400 (ha 7 candles) | 0.00908 | -0.0564% | — | sem_zona |
| 2026-10-30 18:06 | SUI-USDT-SWAP | 0.89060 | 0.89570/0.88220 | 0.89140 | sup 0.87530 (ha 6 candles) | 0.01350 | -0.0068% | — | sem_zona |
| 2026-10-30 18:06 | UNI-USDT-SWAP | 6.9270 | 7.0040/6.8810 | 6.9500 | — | 0.13636 | 0.0100% | B/compra@6.8830 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-30 18:06 | LINK-USDT-SWAP | 11.18 | 11.19/11.07 | 11.12 | — | 0.15236 | -0.0161% | B/compra@11.26 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-30 19:06 | BTC-USDT-SWAP | 76656.1 | 77000.0/76543.0 | 76876.2 | — | 581.41 | 0.0100% | — | sem_zona |
| 2026-10-30 19:06 | ETH-USDT-SWAP | 2236.7 | 2244.5/2233.1 | 2237.7 | sup 2205.8 (ha 8 candles) | 21.21 | -0.0128% | — | sem_zona |
| 2026-10-30 19:06 | SOL-USDT-SWAP | 95.32 | 95.58/95.00 | 94.68 | sup 93.52 (ha 3 candles) | 1.0600 | -0.0069% | — | sem_zona |
| 2026-10-30 19:06 | XRP-USDT-SWAP | 1.2503 | 1.2529/1.2474 | 1.2496 | sup 1.2327 (ha 3 candles) | 0.01210 | -0.0151% | — | sem_zona |
| 2026-10-30 19:06 | DOGE-USDT-SWAP | 0.07529 | 0.07562/0.07524 | 0.07537 | — | 0.00077 | 0.0072% | B/compra@0.07592 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-30 19:06 | ARB-USDT-SWAP | 0.16120 | 0.16267/0.16089 | 0.16328 | sup 0.16026 (ha 3 candles) | 0.00285 | 0.0071% | — | sem_zona |
| 2026-10-30 19:06 | WLD-USDT-SWAP | 0.40410 | 0.40720/0.40220 | 0.40720 | sup 0.39940 (ha 3 candles) | 0.00892 | -0.0334% | — | sem_zona |
| 2026-10-30 19:06 | SUI-USDT-SWAP | 0.89370 | 0.89920/0.88790 | 0.89140 | sup 0.87440 (ha 3 candles) | 0.01320 | -0.0036% | — | sem_zona |
| 2026-10-30 19:06 | UNI-USDT-SWAP | 6.9490 | 6.9890/6.9060 | 6.9500 | — | 0.13079 | 0.0100% | B/compra@6.8830 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-30 19:06 | LINK-USDT-SWAP | 11.22 | 11.27/11.17 | 11.12 | — | 0.14929 | -0.0117% | — | invalidado_setup_B |
| 2026-10-30 20:06 | BTC-USDT-SWAP | 76891.3 | 76950.0/76657.1 | 76876.2 | — | 577.03 | 0.0100% | — | sem_zona |
| 2026-10-30 20:06 | ETH-USDT-SWAP | 2234.4 | 2242.8/2231.3 | 2237.7 | sup 2205.8 (ha 9 candles) | 21.04 | -0.0104% | — | sem_zona |
| 2026-10-30 20:06 | SOL-USDT-SWAP | 95.78 | 95.93/95.30 | 94.68 | sup 93.52 (ha 4 candles) | 1.0536 | -0.0083% | — | sem_zona |
| 2026-10-30 20:06 | XRP-USDT-SWAP | 1.2522 | 1.2543/1.2489 | 1.2496 | sup 1.2327 (ha 4 candles) | 0.01172 | -0.0095% | — | sem_zona |
| 2026-10-30 20:06 | DOGE-USDT-SWAP | 0.07558 | 0.07569/0.07527 | 0.07537 | — | 0.00075 | 0.0081% | B/compra@0.07592 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-30 20:06 | ARB-USDT-SWAP | 0.16146 | 0.16228/0.16116 | 0.16328 | sup 0.16026 (ha 4 candles) | 0.00268 | 0.0040% | — | sem_zona |
| 2026-10-30 20:06 | WLD-USDT-SWAP | 0.40640 | 0.40680/0.40330 | 0.40720 | sup 0.39940 (ha 4 candles) | 0.00870 | -0.0117% | — | sem_zona |
| 2026-10-30 20:06 | SUI-USDT-SWAP | 0.89940 | 0.90300/0.89380 | 0.89140 | sup 0.87440 (ha 4 candles) | 0.01329 | -0.0018% | — | sem_zona |
| 2026-10-30 20:06 | UNI-USDT-SWAP | 6.9780 | 7.0080/6.9500 | 6.9500 | — | 0.12871 | 0.0100% | B/compra@6.8830 (2t/1c) | zona_mapeada_setup_B |
| 2026-10-30 20:06 | LINK-USDT-SWAP | 11.34 | 11.39/11.22 | 11.12 | — | 0.15279 | -0.0072% | — | sem_zona |
| 2026-10-30 21:06 | BTC-USDT-SWAP | 77286.8 | 77321.7/76850.0 | 77286.8 | — | 575.01 | 0.0100% | — | sem_zona |
| 2026-10-30 21:06 | ETH-USDT-SWAP | 2243.4 | 2246.5/2233.6 | 2243.4 | sup 2205.8 (ha 10 candles) | 21.15 | -0.0080% | — | sem_zona |
| 2026-10-30 21:06 | SOL-USDT-SWAP | 96.27 | 96.30/95.72 | 96.27 | sup 93.52 (ha 5 candles) | 1.0379 | -0.0083% | — | sem_zona |
| 2026-10-30 21:06 | XRP-USDT-SWAP | 1.2556 | 1.2560/1.2508 | 1.2556 | sup 1.2327 (ha 5 candles) | 0.01126 | -0.0052% | — | sem_zona |
| 2026-10-30 21:06 | DOGE-USDT-SWAP | 0.07592 | 0.07598/0.07553 | 0.07592 | — | 0.00074 | 0.0096% | — | descartado_rr_baixo_setup_B |
| 2026-10-30 21:06 | ARB-USDT-SWAP | 0.16288 | 0.16345/0.16129 | 0.16288 | sup 0.16026 (ha 5 candles) | 0.00270 | 0.0002% | — | sem_zona |
| 2026-10-30 21:06 | WLD-USDT-SWAP | 0.40680 | 0.41060/0.40620 | 0.40680 | sup 0.39940 (ha 3 candles) | 0.00837 | 0.0035% | — | sem_zona |
| 2026-10-30 21:06 | SUI-USDT-SWAP | 0.90440 | 0.90760/0.89820 | 0.90440 | sup 0.87440 (ha 5 candles) | 0.01342 | 0.0001% | — | sem_zona |
| 2026-10-30 21:06 | UNI-USDT-SWAP | 7.1440 | 7.1930/6.9780 | 7.1440 | — | 0.13550 | 0.0100% | B/compra@6.8830 (2t/2c) | zona_mapeada_setup_B |
| 2026-10-30 21:06 | LINK-USDT-SWAP | 11.44 | 11.45/11.30 | 11.44 | — | 0.15621 | -0.0027% | B/venda@11.55 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-30 22:06 | BTC-USDT-SWAP | 77493.7 | 77500.0/77197.4 | 77286.8 | — | 561.10 | 0.0099% | — | sem_zona |
| 2026-10-30 22:06 | ETH-USDT-SWAP | 2247.4 | 2249.6/2242.6 | 2243.4 | sup 2205.8 (ha 11 candles) | 19.56 | -0.0076% | — | sem_zona |
| 2026-10-30 22:06 | SOL-USDT-SWAP | 96.66 | 96.77/96.13 | 96.27 | sup 93.52 (ha 6 candles) | 1.0071 | -0.0087% | — | sem_zona |
| 2026-10-30 22:06 | XRP-USDT-SWAP | 1.2591 | 1.2605/1.2551 | 1.2556 | sup 1.2327 (ha 6 candles) | 0.01051 | -0.0039% | — | sem_zona |
| 2026-10-30 22:06 | DOGE-USDT-SWAP | 0.07618 | 0.07638/0.07586 | 0.07592 | — | 0.00071 | 0.0091% | B/compra@0.07661 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-30 22:06 | ARB-USDT-SWAP | 0.16516 | 0.16580/0.16272 | 0.16288 | sup 0.16026 (ha 6 candles) | 0.00270 | -0.0024% | — | sem_zona |
| 2026-10-30 22:06 | WLD-USDT-SWAP | 0.40560 | 0.40920/0.40540 | 0.40680 | sup 0.39940 (ha 4 candles) | 0.00801 | 0.0061% | — | sem_zona |
| 2026-10-30 22:06 | SUI-USDT-SWAP | 0.91130 | 0.91360/0.90370 | 0.90440 | sup 0.87440 (ha 6 candles) | 0.01315 | -0.0010% | — | sem_zona |
| 2026-10-30 22:06 | UNI-USDT-SWAP | 7.1270 | 7.2270/7.1170 | 7.1440 | — | 0.13486 | 0.0089% | B/compra@6.8830 (2t/3c) | zona_mapeada_setup_B |
| 2026-10-30 22:06 | LINK-USDT-SWAP | 11.64 | 11.73/11.44 | 11.44 | — | 0.16557 | 0.0017% | — | invalidado_setup_B |
| 2026-10-30 23:06 | BTC-USDT-SWAP | 77336.2 | 77586.4/77305.2 | 77286.8 | — | 535.02 | 0.0093% | — | sem_zona |
| 2026-10-30 23:06 | ETH-USDT-SWAP | 2242.3 | 2251.2/2241.1 | 2243.4 | sup 2205.8 (ha 12 candles) | 18.58 | -0.0083% | — | sem_zona |
| 2026-10-30 23:06 | SOL-USDT-SWAP | 96.58 | 96.94/96.41 | 96.27 | sup 93.52 (ha 7 candles) | 0.96643 | -0.0120% | — | sem_zona |
| 2026-10-30 23:06 | XRP-USDT-SWAP | 1.2542 | 1.2611/1.2540 | 1.2556 | sup 1.2327 (ha 7 candles) | 0.00991 | -0.0022% | — | sem_zona |
| 2026-10-30 23:06 | DOGE-USDT-SWAP | 0.07594 | 0.07637/0.07592 | 0.07592 | — | 0.00070 | 0.0090% | B/compra@0.07661 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-30 23:06 | ARB-USDT-SWAP | 0.16290 | 0.16601/0.16284 | 0.16288 | sup 0.16026 (ha 7 candles) | 0.00280 | -0.0047% | — | sem_zona |
| 2026-10-30 23:06 | WLD-USDT-SWAP | 0.40050 | 0.40710/0.40010 | 0.40680 | sup 0.39940 (ha 5 candles) | 0.00810 | 0.0063% | — | sem_zona |
| 2026-10-30 23:06 | SUI-USDT-SWAP | 0.90270 | 0.91310/0.90140 | 0.90440 | sup 0.87440 (ha 7 candles) | 0.01302 | -0.0021% | — | sem_zona |
| 2026-10-30 23:06 | UNI-USDT-SWAP | 7.0350 | 7.1590/7.0200 | 7.1440 | — | 0.13657 | 0.0100% | B/compra@6.8830 (2t/4c) | zona_mapeada_setup_B |
| 2026-10-30 23:06 | LINK-USDT-SWAP | 11.60 | 11.70/11.54 | 11.44 | — | 0.16693 | 0.0009% | B/venda@11.62 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-31 00:06 | BTC-USDT-SWAP | 77383.6 | 77457.0/77254.9 | 77286.8 | — | 526.12 | 0.0100% | — | sem_zona |
| 2026-10-31 00:06 | ETH-USDT-SWAP | 2244.4 | 2246.6/2240.4 | 2243.4 | sup 2205.8 (ha 13 candles) | 18.07 | -0.0078% | — | sem_zona |
| 2026-10-31 00:06 | SOL-USDT-SWAP | 96.70 | 96.90/96.35 | 96.27 | sup 93.52 (ha 8 candles) | 0.97143 | -0.0149% | — | sem_zona |
| 2026-10-31 00:06 | XRP-USDT-SWAP | 1.2558 | 1.2569/1.2520 | 1.2556 | sup 1.2327 (ha 8 candles) | 0.00979 | -0.0014% | — | sem_zona |
| 2026-10-31 00:06 | DOGE-USDT-SWAP | 0.07580 | 0.07601/0.07570 | 0.07592 | — | 0.00069 | 0.0099% | B/compra@0.07661 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-31 00:06 | ARB-USDT-SWAP | 0.16221 | 0.16294/0.16162 | 0.16288 | sup 0.16026 (ha 8 candles) | 0.00274 | -0.0032% | — | sem_zona |
| 2026-10-31 00:06 | WLD-USDT-SWAP | 0.40210 | 0.40250/0.39820 | 0.40680 | sup 0.39940 (ha 6 candles) | 0.00799 | -0.0017% | — | sem_zona |
| 2026-10-31 00:06 | SUI-USDT-SWAP | 0.90440 | 0.90680/0.89940 | 0.90440 | sup 0.87440 (ha 8 candles) | 0.01315 | -0.0047% | — | sem_zona |
| 2026-10-31 00:06 | UNI-USDT-SWAP | 7.0330 | 7.0650/7.0020 | 7.1440 | — | 0.13271 | 0.0100% | B/compra@6.8830 (2t/5c) | zona_mapeada_setup_B |
| 2026-10-31 00:06 | LINK-USDT-SWAP | 11.54 | 11.65/11.53 | 11.44 | — | 0.16871 | -0.0033% | — | descartado_rr_baixo_setup_B |
