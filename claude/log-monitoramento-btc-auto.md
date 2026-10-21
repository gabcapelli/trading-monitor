# Log de Monitoramento Automatico -- Multi-Par (script gratuito, GitHub Actions)

> Gerado por script Python sem LLM (ver monitor/fetch_and_check.py). Fonte: OKX. Cobre os pares em PAIRS (configuracao no topo do script) -- BTC-USDT-SWAP e os demais adicionados na expansao de 07/09/2026. Leitura e MECANICA (regras objetivas da secao 4 do plano), sem a prosa qualitativa que o Claude gerava -- cole este log numa conversa do Claude se quiser a leitura interpretativa.

| Data/Hora (BRT) | Par | Close 1h | High/Low 1h | Close 4h | Swing 1h ref | ATR 1h | Funding | Zona ativa | Status checklist |
|---|---|---|---|---|---|---|---|---|---|
| 2026-10-19 17:05 | BTC-USDT-SWAP | 81839.9 | 82053.6/81758.0 | 81839.9 | — | 456.71 | 0.0100% | — | sem_zona |
| 2026-10-19 17:05 | ETH-USDT-SWAP | 2394.0 | 2403.9/2389.7 | 2394.0 | — | 19.17 | 0.0091% | B/compra@2391.7 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 17:05 | SOL-USDT-SWAP | 103.99 | 104.43/103.73 | 103.99 | — | 0.88643 | 0.0091% | — | sem_zona |
| 2026-10-19 17:05 | XRP-USDT-SWAP | 1.3003 | 1.3048/1.2972 | 1.3003 | sup 1.2925 (ha 5 candles) | 0.01017 | 0.0100% | B/compra@1.3102 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-19 17:05 | DOGE-USDT-SWAP | 0.07916 | 0.07941/0.07901 | 0.07916 | sup 0.07854 (ha 5 candles) | 0.00068 | 0.0098% | — | sem_zona |
| 2026-10-19 17:05 | ARB-USDT-SWAP | 0.19200 | 0.19397/0.19181 | 0.19200 | — | 0.00341 | 0.0100% | — | sem_zona |
| 2026-10-19 17:05 | WLD-USDT-SWAP | 0.50650 | 0.51240/0.50550 | 0.50650 | sup 0.49330 (ha 9 candles) | 0.01064 | 0.0100% | — | sem_zona |
| 2026-10-19 17:05 | SUI-USDT-SWAP | 0.98390 | 0.98900/0.98260 | 0.98390 | sup 0.97920 (ha 5 candles) | 0.01195 | 0.0100% | — | sem_zona |
| 2026-10-19 17:05 | UNI-USDT-SWAP | 7.1910 | 7.2400/7.1770 | 7.1910 | — | 0.09557 | 0.0099% | B/compra@7.2270 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 17:05 | LINK-USDT-SWAP | 11.87 | 11.95/11.86 | 11.87 | sup 11.86 (ha 5 candles) | 0.11771 | 0.0100% | A/venda@12.08 (0t/4c) | zona_mapeada_setup_A |
| 2026-10-19 18:05 | BTC-USDT-SWAP | 81983.2 | 82055.6/81807.0 | 81839.9 | — | 456.55 | 0.0095% | — | sem_zona |
| 2026-10-19 18:05 | ETH-USDT-SWAP | 2400.0 | 2402.7/2392.9 | 2394.0 | — | 19.29 | 0.0085% | — | confirmado_calibracao_setup_B |
| 2026-10-19 18:05 | SOL-USDT-SWAP | 104.50 | 104.75/103.91 | 103.99 | — | 0.91786 | 0.0078% | B/venda@104.76 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 18:05 | XRP-USDT-SWAP | 1.3009 | 1.3052/1.2991 | 1.3003 | sup 1.2925 (ha 6 candles) | 0.01032 | 0.0100% | B/compra@1.3102 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-19 18:05 | DOGE-USDT-SWAP | 0.07930 | 0.07952/0.07915 | 0.07916 | sup 0.07854 (ha 6 candles) | 0.00069 | 0.0089% | — | sem_zona |
| 2026-10-19 18:05 | ARB-USDT-SWAP | 0.19228 | 0.19322/0.19159 | 0.19200 | — | 0.00315 | 0.0100% | — | sem_zona |
| 2026-10-19 18:05 | WLD-USDT-SWAP | 0.51060 | 0.51800/0.50650 | 0.50650 | sup 0.49330 (ha 10 candles) | 0.01111 | 0.0100% | — | sem_zona |
| 2026-10-19 18:05 | SUI-USDT-SWAP | 0.98580 | 0.99100/0.98230 | 0.98390 | sup 0.97920 (ha 6 candles) | 0.01228 | 0.0100% | — | sem_zona |
| 2026-10-19 18:05 | UNI-USDT-SWAP | 7.2130 | 7.2310/7.1870 | 7.1910 | — | 0.09450 | 0.0100% | B/compra@7.2270 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-19 18:05 | LINK-USDT-SWAP | 11.91 | 11.94/11.87 | 11.87 | sup 11.86 (ha 6 candles) | 0.11686 | 0.0100% | A/venda@12.08 (0t/5c) | zona_mapeada_setup_A |
| 2026-10-19 19:05 | BTC-USDT-SWAP | 82010.0 | 82185.0/81972.6 | 81839.9 | — | 435.26 | 0.0089% | — | sem_zona |
| 2026-10-19 19:05 | ETH-USDT-SWAP | 2401.7 | 2409.4/2399.7 | 2394.0 | — | 18.72 | 0.0076% | B/compra@2407.5 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 19:05 | SOL-USDT-SWAP | 104.69 | 104.91/104.49 | 103.99 | — | 0.90143 | 0.0060% | B/venda@104.76 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-19 19:05 | XRP-USDT-SWAP | 1.3028 | 1.3059/1.3009 | 1.3003 | sup 1.2925 (ha 7 candles) | 0.01007 | 0.0100% | B/compra@1.3102 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-19 19:05 | DOGE-USDT-SWAP | 0.07948 | 0.07959/0.07930 | 0.07916 | sup 0.07870 (ha 3 candles) | 0.00067 | 0.0090% | — | sem_zona |
| 2026-10-19 19:05 | ARB-USDT-SWAP | 0.19608 | 0.20277/0.19215 | 0.19200 | — | 0.00368 | 0.0100% | B/compra@0.19734 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 19:05 | WLD-USDT-SWAP | 0.51660 | 0.51790/0.51070 | 0.50650 | sup 0.50120 (ha 3 candles) | 0.01056 | 0.0100% | B/venda@0.51160 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 19:05 | SUI-USDT-SWAP | 0.98940 | 0.99170/0.98590 | 0.98390 | sup 0.98020 (ha 3 candles) | 0.01210 | 0.0100% | — | sem_zona |
| 2026-10-19 19:05 | UNI-USDT-SWAP | 7.2490 | 7.2710/7.2130 | 7.1910 | — | 0.09171 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-10-19 19:05 | LINK-USDT-SWAP | 11.95 | 11.96/11.90 | 11.87 | sup 11.83 (ha 3 candles) | 0.11543 | 0.0100% | A/venda@12.08 (0t/6c) | zona_mapeada_setup_A |
| 2026-10-19 20:05 | BTC-USDT-SWAP | 82018.9 | 82243.4/82000.4 | 81839.9 | — | 424.76 | 0.0084% | — | sem_zona |
| 2026-10-19 20:05 | ETH-USDT-SWAP | 2405.9 | 2417.3/2401.7 | 2394.0 | — | 18.89 | 0.0075% | B/compra@2407.5 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-19 20:05 | SOL-USDT-SWAP | 105.12 | 105.64/104.70 | 103.99 | — | 0.93000 | 0.0055% | — | invalidado_setup_B |
| 2026-10-19 20:05 | XRP-USDT-SWAP | 1.3045 | 1.3108/1.3029 | 1.3003 | sup 1.2925 (ha 8 candles) | 0.01016 | 0.0100% | — | invalidado_setup_B |
| 2026-10-19 20:05 | DOGE-USDT-SWAP | 0.07967 | 0.08009/0.07949 | 0.07916 | sup 0.07870 (ha 4 candles) | 0.00068 | 0.0086% | — | sem_zona |
| 2026-10-19 20:05 | ARB-USDT-SWAP | 0.19703 | 0.20070/0.19551 | 0.19200 | — | 0.00386 | 0.0100% | B/compra@0.19734 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-19 20:05 | WLD-USDT-SWAP | 0.52840 | 0.53550/0.51650 | 0.50650 | sup 0.50120 (ha 4 candles) | 0.01126 | 0.0100% | B/venda@0.51160 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-19 20:05 | SUI-USDT-SWAP | 0.99850 | 1.0073/0.98950 | 0.98390 | sup 0.98020 (ha 4 candles) | 0.01279 | 0.0100% | — | sem_zona |
| 2026-10-19 20:05 | UNI-USDT-SWAP | 7.2960 | 7.3650/7.2500 | 7.1910 | — | 0.09550 | 0.0100% | B/venda@7.3540 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 20:05 | LINK-USDT-SWAP | 12.03 | 12.07/11.95 | 11.87 | sup 11.83 (ha 4 candles) | 0.12021 | 0.0100% | A/venda@12.08 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-19 21:06 | BTC-USDT-SWAP | 81909.6 | 82082.0/81895.0 | 81909.6 | — | 412.03 | 0.0084% | — | sem_zona |
| 2026-10-19 21:06 | ETH-USDT-SWAP | 2407.1 | 2411.1/2403.7 | 2407.1 | — | 18.40 | 0.0076% | B/compra@2407.5 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-19 21:06 | SOL-USDT-SWAP | 105.03 | 105.25/104.89 | 105.03 | — | 0.91786 | 0.0053% | B/venda@105.22 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 21:06 | XRP-USDT-SWAP | 1.3036 | 1.3059/1.3029 | 1.3036 | sup 1.2925 (ha 9 candles) | 0.01001 | 0.0100% | — | sem_zona |
| 2026-10-19 21:06 | DOGE-USDT-SWAP | 0.07970 | 0.07980/0.07951 | 0.07970 | sup 0.07870 (ha 5 candles) | 0.00068 | 0.0075% | — | sem_zona |
| 2026-10-19 21:06 | ARB-USDT-SWAP | 0.19708 | 0.19816/0.19660 | 0.19708 | — | 0.00381 | 0.0088% | B/compra@0.19734 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-19 21:06 | WLD-USDT-SWAP | 0.53320 | 0.53730/0.52580 | 0.53320 | sup 0.50120 (ha 5 candles) | 0.01161 | 0.0100% | B/venda@0.51160 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-19 21:06 | SUI-USDT-SWAP | 0.99850 | 1.0014/0.99540 | 0.99850 | sup 0.98020 (ha 5 candles) | 0.01264 | 0.0100% | — | sem_zona |
| 2026-10-19 21:06 | UNI-USDT-SWAP | 7.3120 | 7.3450/7.2720 | 7.3120 | — | 0.09693 | 0.0068% | B/venda@7.3540 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-19 21:06 | LINK-USDT-SWAP | 12.05 | 12.07/12.00 | 12.05 | sup 11.83 (ha 5 candles) | 0.12121 | 0.0100% | A/venda@12.08 (2t/0c) | zona_mapeada_setup_A |
| 2026-10-19 22:06 | BTC-USDT-SWAP | 81696.9 | 81984.9/81411.6 | 81909.6 | — | 396.56 | 0.0097% | — | sem_zona |
| 2026-10-19 22:06 | ETH-USDT-SWAP | 2400.7 | 2409.4/2391.1 | 2407.1 | — | 17.98 | 0.0077% | — | invalidado_setup_B |
| 2026-10-19 22:06 | SOL-USDT-SWAP | 104.71 | 105.12/104.26 | 105.03 | — | 0.89286 | 0.0052% | B/venda@105.22 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-19 22:06 | XRP-USDT-SWAP | 1.2977 | 1.3048/1.2954 | 1.3036 | sup 1.2925 (ha 10 candles) | 0.00959 | 0.0100% | — | sem_zona |
| 2026-10-19 22:06 | DOGE-USDT-SWAP | 0.07930 | 0.07978/0.07919 | 0.07970 | sup 0.07870 (ha 6 candles) | 0.00064 | 0.0084% | — | sem_zona |
| 2026-10-19 22:06 | ARB-USDT-SWAP | 0.19861 | 0.19929/0.19468 | 0.19708 | — | 0.00391 | 0.0058% | — | descartado_rr_baixo_setup_B |
| 2026-10-19 22:06 | WLD-USDT-SWAP | 0.53320 | 0.53930/0.52770 | 0.53320 | sup 0.50120 (ha 6 candles) | 0.01150 | 0.0100% | B/venda@0.51160 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-19 22:06 | SUI-USDT-SWAP | 0.99490 | 0.99990/0.99010 | 0.99850 | sup 0.98020 (ha 6 candles) | 0.01219 | 0.0100% | — | sem_zona |
| 2026-10-19 22:06 | UNI-USDT-SWAP | 7.2880 | 7.3250/7.2420 | 7.3120 | — | 0.09579 | 0.0056% | B/venda@7.3540 (1t/1c) | zona_mapeada_setup_B |
| 2026-10-19 22:06 | LINK-USDT-SWAP | 11.99 | 12.06/11.95 | 12.05 | sup 11.83 (ha 6 candles) | 0.11943 | 0.0100% | — | descartado_rr_baixo_setup_A |
| 2026-10-19 23:06 | BTC-USDT-SWAP | 81773.0 | 81824.9/81166.0 | 81909.6 | — | 423.21 | 0.0100% | — | sem_zona |
| 2026-10-19 23:06 | ETH-USDT-SWAP | 2398.3 | 2401.4/2369.0 | 2407.1 | — | 19.28 | 0.0069% | B/compra@2391.7 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 23:06 | SOL-USDT-SWAP | 104.83 | 104.92/103.61 | 105.03 | — | 0.94214 | 0.0063% | B/venda@105.22 (1t/1c) | zona_mapeada_setup_B |
| 2026-10-19 23:06 | XRP-USDT-SWAP | 1.3011 | 1.3028/1.2856 | 1.3036 | sup 1.2925 (ha 11 candles) | 0.01030 | 0.0100% | — | sem_zona |
| 2026-10-19 23:06 | DOGE-USDT-SWAP | 0.07932 | 0.07946/0.07842 | 0.07970 | sup 0.07870 (ha 7 candles) | 0.00068 | 0.0090% | — | sem_zona |
| 2026-10-19 23:06 | ARB-USDT-SWAP | 0.19913 | 0.20023/0.19465 | 0.19708 | — | 0.00417 | -0.0024% | B/compra@0.19938 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 23:06 | WLD-USDT-SWAP | 0.53290 | 0.54170/0.52210 | 0.53320 | sup 0.50120 (ha 7 candles) | 0.01254 | 0.0100% | B/venda@0.51160 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-19 23:06 | SUI-USDT-SWAP | 0.99110 | 0.99500/0.97530 | 0.99850 | sup 0.98020 (ha 7 candles) | 0.01302 | 0.0098% | — | sem_zona |
| 2026-10-19 23:06 | UNI-USDT-SWAP | 7.2760 | 7.3110/7.1800 | 7.3120 | — | 0.09993 | 0.0071% | B/venda@7.3540 (1t/2c) | zona_mapeada_setup_B |
| 2026-10-19 23:06 | LINK-USDT-SWAP | 11.97 | 12.00/11.83 | 12.05 | sup 11.83 (ha 7 candles) | 0.12521 | 0.0100% | — | sem_zona |
| 2026-10-20 00:06 | BTC-USDT-SWAP | 81765.2 | 81932.1/81503.0 | 81909.6 | — | 427.75 | 0.0100% | — | sem_zona |
| 2026-10-20 00:06 | ETH-USDT-SWAP | 2399.8 | 2406.7/2387.3 | 2407.1 | — | 19.89 | 0.0058% | — | descartado_rr_baixo_setup_B |
| 2026-10-20 00:06 | SOL-USDT-SWAP | 105.10 | 105.42/104.29 | 105.03 | — | 0.95643 | 0.0074% | B/venda@105.22 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-20 00:06 | XRP-USDT-SWAP | 1.3033 | 1.3061/1.2960 | 1.3036 | sup 1.2925 (ha 12 candles) | 0.01029 | 0.0100% | — | sem_zona |
| 2026-10-20 00:06 | DOGE-USDT-SWAP | 0.07951 | 0.07975/0.07898 | 0.07970 | sup 0.07870 (ha 8 candles) | 0.00067 | 0.0100% | — | sem_zona |
| 2026-10-20 00:06 | ARB-USDT-SWAP | 0.20127 | 0.20429/0.19778 | 0.19708 | — | 0.00430 | -0.0109% | B/compra@0.19938 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-20 00:06 | WLD-USDT-SWAP | 0.53870 | 0.54270/0.53100 | 0.53320 | sup 0.50120 (ha 8 candles) | 0.01214 | 0.0100% | B/venda@0.51160 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-20 00:06 | SUI-USDT-SWAP | 0.99760 | 1.0024/0.98440 | 0.99850 | sup 0.98020 (ha 8 candles) | 0.01350 | 0.0100% | — | sem_zona |
| 2026-10-20 00:06 | UNI-USDT-SWAP | 7.2680 | 7.3120/7.2230 | 7.3120 | — | 0.10007 | 0.0100% | B/venda@7.3540 (1t/3c) | zona_mapeada_setup_B |
| 2026-10-20 00:06 | LINK-USDT-SWAP | 12.03 | 12.07/11.92 | 12.05 | sup 11.83 (ha 8 candles) | 0.12686 | 0.0100% | — | sem_zona |
| 2026-10-20 01:06 | BTC-USDT-SWAP | 82098.8 | 82099.0/81741.9 | 82098.8 | — | 401.90 | 0.0100% | B/venda@82267.7 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 01:06 | ETH-USDT-SWAP | 2414.0 | 2414.8/2398.9 | 2414.0 | — | 18.59 | 0.0059% | B/compra@2407.5 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 01:06 | SOL-USDT-SWAP | 105.28 | 105.35/104.82 | 105.28 | res 105.64 (ha 5 candles) | 0.88857 | 0.0074% | — | zona_expirada_setup_B |
| 2026-10-20 01:06 | XRP-USDT-SWAP | 1.3060 | 1.3066/1.2996 | 1.3060 | sup 1.2925 (ha 13 candles) | 0.00970 | 0.0100% | — | sem_zona |
| 2026-10-20 01:06 | DOGE-USDT-SWAP | 0.07980 | 0.07980/0.07936 | 0.07980 | sup 0.07870 (ha 9 candles) | 0.00064 | 0.0100% | — | sem_zona |
| 2026-10-20 01:06 | ARB-USDT-SWAP | 0.20212 | 0.20249/0.19812 | 0.20212 | — | 0.00432 | -0.0166% | — | descartado_rr_baixo_setup_B |
| 2026-10-20 01:06 | WLD-USDT-SWAP | 0.54390 | 0.54890/0.53750 | 0.54390 | sup 0.50120 (ha 9 candles) | 0.01220 | 0.0100% | B/venda@0.51160 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-20 01:06 | SUI-USDT-SWAP | 1.0026 | 1.0026/0.99260 | 1.0026 | sup 0.98020 (ha 9 candles) | 0.01308 | 0.0100% | — | sem_zona |
| 2026-10-20 01:06 | UNI-USDT-SWAP | 7.3110 | 7.3110/7.2460 | 7.3110 | — | 0.09343 | 0.0100% | B/venda@7.3540 (1t/4c) | zona_mapeada_setup_B |
| 2026-10-20 01:06 | LINK-USDT-SWAP | 12.10 | 12.11/11.99 | 12.10 | sup 11.83 (ha 9 candles) | 0.12243 | 0.0100% | — | sem_zona |
| 2026-10-20 02:06 | BTC-USDT-SWAP | 82058.3 | 82240.0/82010.0 | 82098.8 | — | 359.46 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-10-20 02:06 | ETH-USDT-SWAP | 2411.6 | 2416.8/2408.8 | 2414.0 | — | 16.32 | 0.0053% | B/compra@2407.5 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-20 02:06 | SOL-USDT-SWAP | 105.18 | 105.47/105.08 | 105.28 | res 105.64 (ha 6 candles) | 0.80000 | 0.0067% | B/compra@105.61 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 02:06 | XRP-USDT-SWAP | 1.3044 | 1.3077/1.3031 | 1.3060 | sup 1.2856 (ha 3 candles) | 0.00854 | 0.0100% | — | sem_zona |
| 2026-10-20 02:06 | DOGE-USDT-SWAP | 0.07957 | 0.07987/0.07952 | 0.07980 | sup 0.07842 (ha 3 candles) | 0.00055 | 0.0100% | — | sem_zona |
| 2026-10-20 02:06 | ARB-USDT-SWAP | 0.19951 | 0.20219/0.19833 | 0.20212 | — | 0.00413 | -0.0180% | B/venda@0.20232 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 02:06 | WLD-USDT-SWAP | 0.54240 | 0.55390/0.54020 | 0.54390 | sup 0.50120 (ha 10 candles) | 0.01220 | 0.0100% | B/venda@0.51160 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-20 02:06 | SUI-USDT-SWAP | 0.99880 | 1.0061/0.99760 | 1.0026 | sup 0.97530 (ha 3 candles) | 0.01171 | 0.0099% | — | sem_zona |
| 2026-10-20 02:06 | UNI-USDT-SWAP | 7.2920 | 7.3410/7.2680 | 7.3110 | — | 0.08307 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-10-20 02:06 | LINK-USDT-SWAP | 12.04 | 12.11/12.04 | 12.10 | sup 11.83 (ha 3 candles) | 0.10900 | 0.0074% | — | sem_zona |
| 2026-10-20 03:06 | BTC-USDT-SWAP | 81677.8 | 82078.3/81671.8 | 82098.8 | — | 343.36 | 0.0096% | — | sem_zona |
| 2026-10-20 03:06 | ETH-USDT-SWAP | 2395.6 | 2412.8/2395.6 | 2414.0 | — | 15.52 | 0.0044% | — | invalidado_setup_B |
| 2026-10-20 03:06 | SOL-USDT-SWAP | 104.48 | 105.22/104.44 | 105.28 | res 105.64 (ha 7 candles) | 0.77000 | 0.0059% | B/compra@105.61 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-20 03:06 | XRP-USDT-SWAP | 1.3012 | 1.3065/1.3006 | 1.3060 | sup 1.2856 (ha 4 candles) | 0.00792 | 0.0100% | — | sem_zona |
| 2026-10-20 03:06 | DOGE-USDT-SWAP | 0.07923 | 0.07973/0.07919 | 0.07980 | sup 0.07842 (ha 4 candles) | 0.00053 | 0.0100% | — | sem_zona |
| 2026-10-20 03:06 | ARB-USDT-SWAP | 0.19783 | 0.20055/0.19749 | 0.20212 | — | 0.00405 | -0.0175% | B/venda@0.20232 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-20 03:06 | WLD-USDT-SWAP | 0.53650 | 0.54590/0.53450 | 0.54390 | sup 0.50120 (ha 11 candles) | 0.01222 | 0.0100% | — | zona_expirada_setup_B |
| 2026-10-20 03:06 | SUI-USDT-SWAP | 0.99120 | 1.0009/0.99060 | 1.0026 | sup 0.97530 (ha 4 candles) | 0.01088 | 0.0089% | — | sem_zona |
| 2026-10-20 03:06 | UNI-USDT-SWAP | 7.1960 | 7.2970/7.1960 | 7.3110 | — | 0.08321 | 0.0082% | B/compra@7.2270 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 03:06 | LINK-USDT-SWAP | 11.97 | 12.07/11.97 | 12.10 | sup 11.83 (ha 4 candles) | 0.10457 | 0.0046% | — | sem_zona |
| 2026-10-20 04:06 | BTC-USDT-SWAP | 81771.3 | 81844.6/81580.3 | 82098.8 | — | 335.85 | 0.0081% | — | sem_zona |
| 2026-10-20 04:06 | ETH-USDT-SWAP | 2397.5 | 2401.3/2390.3 | 2414.0 | — | 14.99 | 0.0054% | B/compra@2391.7 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 04:06 | SOL-USDT-SWAP | 104.63 | 104.87/104.16 | 105.28 | res 105.64 (ha 8 candles) | 0.76000 | 0.0065% | B/compra@105.61 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-20 04:06 | XRP-USDT-SWAP | 1.3008 | 1.3044/1.2989 | 1.3060 | sup 1.2856 (ha 5 candles) | 0.00755 | 0.0100% | — | sem_zona |
| 2026-10-20 04:06 | DOGE-USDT-SWAP | 0.07934 | 0.07948/0.07900 | 0.07980 | sup 0.07842 (ha 5 candles) | 0.00052 | 0.0100% | — | sem_zona |
| 2026-10-20 04:06 | ARB-USDT-SWAP | 0.19697 | 0.19941/0.19663 | 0.20212 | — | 0.00407 | -0.0128% | B/venda@0.20232 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-20 04:06 | WLD-USDT-SWAP | 0.54290 | 0.54560/0.53370 | 0.54390 | sup 0.50120 (ha 12 candles) | 0.01225 | 0.0100% | B/venda@0.53940 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 04:06 | SUI-USDT-SWAP | 0.99460 | 0.99880/0.98770 | 1.0026 | sup 0.97530 (ha 5 candles) | 0.01092 | 0.0096% | — | sem_zona |
| 2026-10-20 04:06 | UNI-USDT-SWAP | 7.1870 | 7.2250/7.1150 | 7.3110 | — | 0.08393 | 0.0076% | — | invalidado_setup_B |
| 2026-10-20 04:06 | LINK-USDT-SWAP | 12.00 | 12.04/11.94 | 12.10 | sup 11.83 (ha 5 candles) | 0.10407 | 0.0045% | — | sem_zona |
| 2026-10-20 05:06 | BTC-USDT-SWAP | 81514.6 | 81813.3/81420.0 | 81514.6 | — | 347.26 | 0.0046% | — | sem_zona |
| 2026-10-20 05:06 | ETH-USDT-SWAP | 2389.8 | 2398.5/2385.6 | 2389.8 | — | 15.03 | 0.0040% | B/compra@2391.7 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-20 05:06 | SOL-USDT-SWAP | 104.36 | 104.73/104.21 | 104.36 | res 105.47 (ha 3 candles) | 0.73857 | 0.0045% | B/compra@105.61 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-20 05:06 | XRP-USDT-SWAP | 1.2966 | 1.3023/1.2950 | 1.2966 | sup 1.2856 (ha 6 candles) | 0.00760 | 0.0077% | — | sem_zona |
| 2026-10-20 05:06 | DOGE-USDT-SWAP | 0.07923 | 0.07944/0.07910 | 0.07923 | sup 0.07842 (ha 6 candles) | 0.00051 | 0.0100% | — | sem_zona |
| 2026-10-20 05:06 | ARB-USDT-SWAP | 0.19311 | 0.19746/0.19211 | 0.19311 | — | 0.00427 | -0.0050% | B/venda@0.20232 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-20 05:06 | WLD-USDT-SWAP | 0.53950 | 0.54520/0.53660 | 0.53950 | sup 0.50120 (ha 13 candles) | 0.01236 | 0.0100% | — | confirmado_calibracao_setup_B |
| 2026-10-20 05:06 | SUI-USDT-SWAP | 0.99070 | 0.99650/0.98840 | 0.99070 | sup 0.97530 (ha 6 candles) | 0.01084 | 0.0088% | — | sem_zona |
| 2026-10-20 05:06 | UNI-USDT-SWAP | 7.1800 | 7.2070/7.1550 | 7.1800 | — | 0.08150 | 0.0078% | — | sem_zona |
| 2026-10-20 05:06 | LINK-USDT-SWAP | 11.96 | 12.02/11.94 | 11.96 | sup 11.83 (ha 6 candles) | 0.10086 | 0.0037% | — | sem_zona |
| 2026-10-20 06:06 | BTC-USDT-SWAP | 81499.9 | 81597.0/81323.3 | 81514.6 | — | 340.91 | 0.0025% | — | sem_zona |
| 2026-10-20 06:06 | ETH-USDT-SWAP | 2384.2 | 2391.3/2377.0 | 2389.8 | — | 14.73 | 0.0030% | — | invalidado_setup_B |
| 2026-10-20 06:06 | SOL-USDT-SWAP | 104.08 | 104.45/103.77 | 104.36 | res 105.47 (ha 4 candles) | 0.72714 | 0.0041% | B/compra@105.61 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-20 06:06 | XRP-USDT-SWAP | 1.2939 | 1.2996/1.2915 | 1.2966 | sup 1.2856 (ha 7 candles) | 0.00749 | 0.0040% | — | sem_zona |
| 2026-10-20 06:06 | DOGE-USDT-SWAP | 0.07897 | 0.07928/0.07874 | 0.07923 | sup 0.07842 (ha 7 candles) | 0.00050 | 0.0100% | — | sem_zona |
| 2026-10-20 06:06 | ARB-USDT-SWAP | 0.19007 | 0.19311/0.18888 | 0.19311 | — | 0.00439 | 0.0019% | B/venda@0.20232 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-20 06:06 | WLD-USDT-SWAP | 0.53650 | 0.54000/0.53410 | 0.53950 | sup 0.50120 (ha 14 candles) | 0.01157 | 0.0100% | B/venda@0.53360 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 06:06 | SUI-USDT-SWAP | 0.98700 | 0.99190/0.98280 | 0.99070 | sup 0.97530 (ha 7 candles) | 0.01068 | 0.0091% | — | sem_zona |
| 2026-10-20 06:06 | UNI-USDT-SWAP | 7.1420 | 7.1850/7.0930 | 7.1800 | — | 0.08214 | 0.0080% | B/compra@7.0890 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 06:06 | LINK-USDT-SWAP | 11.93 | 11.96/11.89 | 11.96 | sup 11.83 (ha 7 candles) | 0.09771 | 0.0044% | — | sem_zona |
| 2026-10-20 07:06 | BTC-USDT-SWAP | 81457.8 | 81581.9/81288.0 | 81514.6 | — | 340.79 | 0.0015% | — | sem_zona |
| 2026-10-20 07:06 | ETH-USDT-SWAP | 2383.1 | 2387.8/2375.4 | 2389.8 | — | 14.60 | 0.0014% | — | sem_zona |
| 2026-10-20 07:06 | SOL-USDT-SWAP | 104.00 | 104.29/103.74 | 104.36 | res 105.47 (ha 5 candles) | 0.71643 | 0.0045% | B/compra@105.61 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-20 07:06 | XRP-USDT-SWAP | 1.2931 | 1.2961/1.2895 | 1.2966 | sup 1.2856 (ha 8 candles) | 0.00741 | 0.0032% | — | sem_zona |
| 2026-10-20 07:06 | DOGE-USDT-SWAP | 0.07900 | 0.07910/0.07873 | 0.07923 | sup 0.07842 (ha 8 candles) | 0.00050 | 0.0100% | — | sem_zona |
| 2026-10-20 07:06 | ARB-USDT-SWAP | 0.18953 | 0.19067/0.18888 | 0.19311 | — | 0.00437 | 0.0087% | B/venda@0.20232 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-20 07:06 | WLD-USDT-SWAP | 0.53420 | 0.53830/0.52950 | 0.53950 | sup 0.50120 (ha 15 candles) | 0.01171 | 0.0100% | B/venda@0.53360 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-20 07:06 | SUI-USDT-SWAP | 0.98850 | 0.98910/0.98250 | 0.99070 | sup 0.97530 (ha 8 candles) | 0.01069 | 0.0100% | — | sem_zona |
| 2026-10-20 07:06 | UNI-USDT-SWAP | 7.1240 | 7.1600/7.0920 | 7.1800 | — | 0.08250 | 0.0082% | B/compra@7.0890 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-20 07:06 | LINK-USDT-SWAP | 11.93 | 11.95/11.88 | 11.96 | sup 11.83 (ha 8 candles) | 0.09621 | 0.0066% | — | sem_zona |
| 2026-10-20 08:06 | BTC-USDT-SWAP | 81517.6 | 81620.5/81440.7 | 81514.6 | — | 335.88 | 0.0007% | — | sem_zona |
| 2026-10-20 08:06 | ETH-USDT-SWAP | 2385.9 | 2389.9/2381.5 | 2389.8 | — | 14.50 | 0.0009% | — | sem_zona |
| 2026-10-20 08:06 | SOL-USDT-SWAP | 104.22 | 104.25/103.80 | 104.36 | res 105.47 (ha 6 candles) | 0.68857 | 0.0045% | B/compra@105.61 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-20 08:06 | XRP-USDT-SWAP | 1.2941 | 1.2957/1.2906 | 1.2966 | sup 1.2856 (ha 9 candles) | 0.00734 | 0.0044% | — | sem_zona |
| 2026-10-20 08:06 | DOGE-USDT-SWAP | 0.07902 | 0.07913/0.07884 | 0.07923 | sup 0.07842 (ha 9 candles) | 0.00050 | 0.0100% | — | sem_zona |
| 2026-10-20 08:06 | ARB-USDT-SWAP | 0.18982 | 0.19002/0.18866 | 0.19311 | — | 0.00435 | 0.0098% | B/venda@0.20232 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-20 08:06 | WLD-USDT-SWAP | 0.54120 | 0.54230/0.52970 | 0.53950 | sup 0.50120 (ha 16 candles) | 0.01179 | 0.0100% | — | invalidado_setup_B |
| 2026-10-20 08:06 | SUI-USDT-SWAP | 0.99210 | 0.99220/0.98560 | 0.99070 | sup 0.97530 (ha 9 candles) | 0.01054 | 0.0090% | — | sem_zona |
| 2026-10-20 08:06 | UNI-USDT-SWAP | 7.1450 | 7.1550/7.1090 | 7.1800 | — | 0.08264 | 0.0089% | — | descartado_rr_baixo_setup_B |
| 2026-10-20 08:06 | LINK-USDT-SWAP | 11.93 | 11.95/11.90 | 11.96 | sup 11.83 (ha 9 candles) | 0.09479 | 0.0078% | — | sem_zona |
| 2026-10-20 09:06 | BTC-USDT-SWAP | 81468.0 | 81624.5/81410.0 | 81468.0 | — | 336.03 | 0.0012% | — | sem_zona |
| 2026-10-20 09:06 | ETH-USDT-SWAP | 2383.5 | 2390.8/2381.5 | 2383.5 | — | 14.47 | 0.0012% | — | sem_zona |
| 2026-10-20 09:06 | SOL-USDT-SWAP | 104.05 | 104.41/103.94 | 104.05 | res 105.47 (ha 7 candles) | 0.69214 | 0.0045% | B/compra@105.61 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-20 09:06 | XRP-USDT-SWAP | 1.2966 | 1.3020/1.2929 | 1.2966 | sup 1.2856 (ha 10 candles) | 0.00764 | 0.0052% | — | sem_zona |
| 2026-10-20 09:06 | DOGE-USDT-SWAP | 0.07903 | 0.07936/0.07895 | 0.07903 | sup 0.07842 (ha 10 candles) | 0.00050 | 0.0100% | — | sem_zona |
| 2026-10-20 09:06 | ARB-USDT-SWAP | 0.18934 | 0.19034/0.18825 | 0.18934 | — | 0.00374 | 0.0100% | B/venda@0.20232 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-20 09:06 | WLD-USDT-SWAP | 0.54300 | 0.54480/0.53670 | 0.54300 | sup 0.50120 (ha 17 candles) | 0.01184 | 0.0100% | B/venda@0.53940 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 09:06 | SUI-USDT-SWAP | 0.99100 | 0.99580/0.98870 | 0.99100 | sup 0.97530 (ha 10 candles) | 0.01063 | 0.0081% | — | sem_zona |
| 2026-10-20 09:06 | UNI-USDT-SWAP | 7.1270 | 7.1700/7.1040 | 7.1270 | — | 0.08321 | 0.0093% | — | sem_zona |
| 2026-10-20 09:06 | LINK-USDT-SWAP | 11.94 | 11.99/11.91 | 11.94 | sup 11.83 (ha 10 candles) | 0.09629 | 0.0092% | — | sem_zona |
| 2026-10-20 10:06 | BTC-USDT-SWAP | 81577.9 | 81743.8/81300.0 | 81468.0 | — | 350.37 | 0.0019% | — | sem_zona |
| 2026-10-20 10:06 | ETH-USDT-SWAP | 2395.4 | 2403.3/2380.4 | 2383.5 | — | 14.99 | 0.0023% | B/compra@2405.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 10:06 | SOL-USDT-SWAP | 104.44 | 104.86/103.95 | 104.05 | res 105.47 (ha 8 candles) | 0.68929 | 0.0051% | — | zona_expirada_setup_B |
| 2026-10-20 10:06 | XRP-USDT-SWAP | 1.2996 | 1.3033/1.2946 | 1.2966 | sup 1.2895 (ha 3 candles) | 0.00769 | 0.0060% | — | sem_zona |
| 2026-10-20 10:06 | DOGE-USDT-SWAP | 0.07925 | 0.07960/0.07897 | 0.07903 | sup 0.07873 (ha 3 candles) | 0.00051 | 0.0100% | — | sem_zona |
| 2026-10-20 10:06 | ARB-USDT-SWAP | 0.18859 | 0.19010/0.18774 | 0.18934 | — | 0.00354 | 0.0078% | — | zona_expirada_setup_B |
| 2026-10-20 10:06 | WLD-USDT-SWAP | 0.55240 | 0.55870/0.54210 | 0.54300 | sup 0.52950 (ha 3 candles) | 0.01167 | 0.0100% | — | invalidado_setup_B |
| 2026-10-20 10:06 | SUI-USDT-SWAP | 0.99700 | 1.0024/0.98910 | 0.99100 | sup 0.98250 (ha 3 candles) | 0.01030 | 0.0088% | — | sem_zona |
| 2026-10-20 10:06 | UNI-USDT-SWAP | 7.1450 | 7.1990/7.1150 | 7.1270 | — | 0.08093 | 0.0076% | — | sem_zona |
| 2026-10-20 10:06 | LINK-USDT-SWAP | 11.98 | 12.04/11.94 | 11.94 | sup 11.88 (ha 3 candles) | 0.09471 | 0.0100% | — | sem_zona |
| 2026-10-20 11:07 | BTC-USDT-SWAP | 82124.3 | 82149.0/81273.0 | 81468.0 | — | 399.59 | 0.0036% | B/venda@82267.7 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 11:07 | ETH-USDT-SWAP | 2410.7 | 2412.9/2382.1 | 2383.5 | — | 16.66 | 0.0033% | — | descartado_rr_baixo_setup_B |
| 2026-10-20 11:07 | SOL-USDT-SWAP | 105.21 | 105.24/103.79 | 104.05 | res 105.47 (ha 9 candles) | 0.76714 | 0.0056% | — | sem_zona |
| 2026-10-20 11:07 | XRP-USDT-SWAP | 1.3095 | 1.3100/1.2950 | 1.2966 | sup 1.2895 (ha 4 candles) | 0.00854 | 0.0066% | — | sem_zona |
| 2026-10-20 11:07 | DOGE-USDT-SWAP | 0.08008 | 0.08011/0.07899 | 0.07903 | sup 0.07873 (ha 4 candles) | 0.00057 | 0.0088% | — | sem_zona |
| 2026-10-20 11:07 | ARB-USDT-SWAP | 0.19210 | 0.19222/0.18728 | 0.18934 | — | 0.00378 | 0.0020% | — | sem_zona |
| 2026-10-20 11:07 | WLD-USDT-SWAP | 0.55690 | 0.55790/0.54790 | 0.54300 | sup 0.52950 (ha 4 candles) | 0.01156 | 0.0100% | — | sem_zona |
| 2026-10-20 11:07 | SUI-USDT-SWAP | 1.0126 | 1.0135/0.98930 | 0.99100 | sup 0.98250 (ha 4 candles) | 0.01160 | 0.0098% | — | sem_zona |
| 2026-10-20 11:07 | UNI-USDT-SWAP | 7.2800 | 7.2810/7.0960 | 7.1270 | — | 0.08893 | 0.0081% | B/compra@7.2270 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 11:07 | LINK-USDT-SWAP | 12.09 | 12.10/11.92 | 11.94 | sup 11.88 (ha 4 candles) | 0.10236 | 0.0100% | — | sem_zona |
| 2026-10-20 12:06 | BTC-USDT-SWAP | 83231.6 | 83436.9/82066.5 | 81468.0 | — | 456.52 | 0.0051% | — | invalidado_setup_B |
| 2026-10-20 12:06 | ETH-USDT-SWAP | 2471.2 | 2477.8/2408.0 | 2383.5 | — | 20.34 | 0.0046% | B/compra@2473.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 12:06 | SOL-USDT-SWAP | 107.70 | 108.24/105.14 | 104.05 | res 105.47 (ha 10 candles) | 0.92714 | 0.0055% | B/compra@108.37 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 12:06 | XRP-USDT-SWAP | 1.3430 | 1.3457/1.3091 | 1.2966 | sup 1.2895 (ha 5 candles) | 0.01049 | 0.0075% | B/venda@1.3469 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 12:06 | DOGE-USDT-SWAP | 0.08186 | 0.08200/0.08005 | 0.07903 | sup 0.07873 (ha 5 candles) | 0.00066 | 0.0080% | — | sem_zona |
| 2026-10-20 12:06 | ARB-USDT-SWAP | 0.19655 | 0.19880/0.19181 | 0.18934 | — | 0.00395 | -0.0007% | B/venda@0.19508 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 12:06 | WLD-USDT-SWAP | 0.57690 | 0.58560/0.55350 | 0.54300 | sup 0.52950 (ha 5 candles) | 0.01303 | 0.0100% | B/venda@0.58590 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 12:06 | SUI-USDT-SWAP | 1.0403 | 1.0437/1.0124 | 0.99100 | sup 0.98250 (ha 5 candles) | 0.01314 | 0.0100% | — | sem_zona |
| 2026-10-20 12:06 | UNI-USDT-SWAP | 7.5260 | 7.5680/7.2650 | 7.1270 | — | 0.10464 | 0.0091% | B/compra@7.2270 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-20 12:06 | LINK-USDT-SWAP | 12.42 | 12.47/12.09 | 11.94 | sup 11.88 (ha 5 candles) | 0.12136 | 0.0100% | — | sem_zona |
| 2026-10-20 13:06 | BTC-USDT-SWAP | 82577.3 | 83273.6/82152.5 | 82577.3 | res 82240.0 (ha 11 candles) | 489.54 | 0.0053% | A/compra@82240.0 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-20 13:06 | ETH-USDT-SWAP | 2440.1 | 2472.0/2425.5 | 2440.1 | res 2416.8 (ha 11 candles) | 21.34 | 0.0059% | — | invalidado_setup_B |
| 2026-10-20 13:06 | SOL-USDT-SWAP | 105.79 | 107.87/104.91 | 105.79 | res 105.47 (ha 11 candles) | 1.0450 | 0.0040% | B/compra@108.37 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-20 13:06 | XRP-USDT-SWAP | 1.3213 | 1.3438/1.3089 | 1.3213 | — | 0.01175 | 0.0060% | B/venda@1.3469 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-20 13:06 | DOGE-USDT-SWAP | 0.08055 | 0.08191/0.07983 | 0.08055 | — | 0.00074 | 0.0087% | B/compra@0.08092 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 13:06 | ARB-USDT-SWAP | 0.18898 | 0.19658/0.18612 | 0.18898 | — | 0.00430 | -0.0043% | — | descartado_rr_baixo_setup_B |
| 2026-10-20 13:06 | WLD-USDT-SWAP | 0.56290 | 0.57710/0.55910 | 0.56290 | sup 0.52950 (ha 6 candles) | 0.01291 | 0.0100% | B/venda@0.58590 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-20 13:06 | SUI-USDT-SWAP | 1.0119 | 1.0409/0.99730 | 1.0119 | — | 0.01484 | 0.0100% | — | sem_zona |
| 2026-10-20 13:06 | UNI-USDT-SWAP | 7.2680 | 7.5310/7.1880 | 7.2680 | — | 0.11979 | 0.0043% | B/compra@7.2270 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-20 13:06 | LINK-USDT-SWAP | 12.19 | 12.42/12.07 | 12.19 | — | 0.13479 | 0.0082% | B/compra@12.15 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 14:09 | BTC-USDT-SWAP | 82734.5 | 82803.7/82312.0 | 82577.3 | res 82240.0 (ha 12 candles) | 494.01 | 0.0056% | — | descartado_rr_baixo_setup_A |
| 2026-10-20 14:09 | ETH-USDT-SWAP | 2450.7 | 2455.8/2431.1 | 2440.1 | res 2416.8 (ha 12 candles) | 21.72 | 0.0070% | A/compra@2416.8 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-20 14:09 | SOL-USDT-SWAP | 106.43 | 106.73/105.24 | 105.79 | res 105.47 (ha 12 candles) | 1.0707 | 0.0027% | B/compra@108.37 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-20 14:09 | XRP-USDT-SWAP | 1.3275 | 1.3302/1.3158 | 1.3213 | — | 0.01206 | 0.0053% | B/venda@1.3469 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-20 14:09 | DOGE-USDT-SWAP | 0.08119 | 0.08129/0.08030 | 0.08055 | — | 0.00075 | 0.0078% | — | descartado_rr_baixo_setup_B |
| 2026-10-20 14:09 | ARB-USDT-SWAP | 0.18930 | 0.19029/0.18642 | 0.18898 | — | 0.00411 | -0.0100% | B/venda@0.18875 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 14:09 | WLD-USDT-SWAP | 0.56760 | 0.57150/0.55610 | 0.56290 | sup 0.52950 (ha 7 candles) | 0.01318 | 0.0100% | B/venda@0.58590 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-20 14:09 | SUI-USDT-SWAP | 1.0188 | 1.0224/1.0062 | 1.0119 | — | 0.01471 | 0.0100% | — | sem_zona |
| 2026-10-20 14:09 | UNI-USDT-SWAP | 7.3720 | 7.3910/7.2160 | 7.2680 | — | 0.12593 | -0.0007% | — | descartado_rr_baixo_setup_B |
| 2026-10-20 14:09 | LINK-USDT-SWAP | 12.27 | 12.30/12.15 | 12.19 | — | 0.13521 | 0.0035% | — | descartado_rr_baixo_setup_B |
| 2026-10-20 15:06 | BTC-USDT-SWAP | 82779.0 | 82899.0/82640.4 | 82577.3 | res 83436.9 (ha 3 candles) | 486.97 | 0.0052% | B/compra@82907.7 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 15:06 | ETH-USDT-SWAP | 2449.5 | 2454.1/2443.2 | 2440.1 | res 2477.8 (ha 3 candles) | 21.37 | 0.0067% | A/compra@2416.8 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-20 15:06 | SOL-USDT-SWAP | 106.71 | 106.76/106.20 | 105.79 | res 108.24 (ha 3 candles) | 1.0729 | 0.0020% | B/compra@108.37 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-20 15:06 | XRP-USDT-SWAP | 1.3293 | 1.3315/1.3249 | 1.3213 | — | 0.01203 | 0.0039% | B/venda@1.3469 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-20 15:06 | DOGE-USDT-SWAP | 0.08131 | 0.08139/0.08096 | 0.08055 | — | 0.00075 | 0.0074% | — | sem_zona |
| 2026-10-20 15:06 | ARB-USDT-SWAP | 0.18901 | 0.18958/0.18721 | 0.18898 | — | 0.00397 | -0.0127% | B/venda@0.18875 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-20 15:06 | WLD-USDT-SWAP | 0.57640 | 0.58030/0.56330 | 0.56290 | sup 0.52950 (ha 8 candles) | 0.01358 | 0.0100% | B/venda@0.58590 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-20 15:06 | SUI-USDT-SWAP | 1.0221 | 1.0233/1.0141 | 1.0119 | — | 0.01466 | 0.0100% | — | sem_zona |
| 2026-10-20 15:06 | UNI-USDT-SWAP | 7.4260 | 7.4600/7.3450 | 7.2680 | — | 0.12950 | 0.0008% | B/venda@7.3520 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 15:06 | LINK-USDT-SWAP | 12.24 | 12.28/12.19 | 12.19 | — | 0.13279 | 0.0026% | B/compra@12.25 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 16:06 | BTC-USDT-SWAP | 82503.1 | 82788.0/82428.8 | 82577.3 | res 83436.9 (ha 4 candles) | 496.20 | 0.0056% | — | invalidado_setup_B |
| 2026-10-20 16:06 | ETH-USDT-SWAP | 2437.4 | 2450.1/2434.0 | 2440.1 | res 2477.8 (ha 4 candles) | 21.94 | 0.0068% | A/compra@2416.8 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-20 16:06 | SOL-USDT-SWAP | 105.93 | 106.76/105.67 | 105.79 | res 108.24 (ha 4 candles) | 1.1229 | 0.0018% | B/compra@108.37 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-20 16:06 | XRP-USDT-SWAP | 1.3236 | 1.3301/1.3180 | 1.3213 | — | 0.01256 | 0.0036% | B/venda@1.3469 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-20 16:06 | DOGE-USDT-SWAP | 0.08125 | 0.08134/0.08094 | 0.08055 | — | 0.00076 | 0.0100% | — | sem_zona |
| 2026-10-20 16:06 | ARB-USDT-SWAP | 0.19069 | 0.19218/0.18880 | 0.18898 | — | 0.00393 | -0.0119% | — | invalidado_setup_B |
| 2026-10-20 16:06 | WLD-USDT-SWAP | 0.57970 | 0.58510/0.57360 | 0.56290 | sup 0.52950 (ha 9 candles) | 0.01342 | 0.0100% | B/venda@0.58590 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-20 16:06 | SUI-USDT-SWAP | 1.0155 | 1.0226/1.0110 | 1.0119 | — | 0.01488 | 0.0100% | — | sem_zona |
| 2026-10-20 16:06 | UNI-USDT-SWAP | 7.3630 | 7.4470/7.3430 | 7.2680 | — | 0.13171 | 0.0053% | — | descartado_rr_baixo_setup_B |
| 2026-10-20 16:06 | LINK-USDT-SWAP | 12.18 | 12.24/12.13 | 12.19 | — | 0.13593 | 0.0033% | — | invalidado_setup_B |
| 2026-10-20 17:06 | BTC-USDT-SWAP | 82575.0 | 82635.3/82360.0 | 82575.0 | res 83436.9 (ha 5 candles) | 486.83 | 0.0072% | B/compra@82752.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 17:06 | ETH-USDT-SWAP | 2437.0 | 2441.0/2424.3 | 2437.0 | res 2477.8 (ha 5 candles) | 21.90 | 0.0073% | A/compra@2416.8 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-20 17:06 | SOL-USDT-SWAP | 106.03 | 106.23/105.21 | 106.03 | res 108.24 (ha 5 candles) | 1.1400 | 0.0010% | B/compra@108.37 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-20 17:06 | XRP-USDT-SWAP | 1.3285 | 1.3298/1.3162 | 1.3285 | — | 0.01311 | 0.0029% | B/venda@1.3469 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-20 17:06 | DOGE-USDT-SWAP | 0.08153 | 0.08168/0.08094 | 0.08153 | — | 0.00077 | 0.0100% | — | sem_zona |
| 2026-10-20 17:06 | ARB-USDT-SWAP | 0.18890 | 0.19078/0.18764 | 0.18890 | — | 0.00394 | -0.0067% | — | sem_zona |
| 2026-10-20 17:06 | WLD-USDT-SWAP | 0.58190 | 0.58420/0.57610 | 0.58190 | sup 0.52950 (ha 10 candles) | 0.01319 | 0.0100% | B/venda@0.58590 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-20 17:06 | SUI-USDT-SWAP | 1.0227 | 1.0232/1.0078 | 1.0227 | — | 0.01524 | 0.0100% | — | sem_zona |
| 2026-10-20 17:06 | UNI-USDT-SWAP | 7.3220 | 7.3700/7.2580 | 7.3220 | — | 0.13250 | 0.0059% | — | sem_zona |
| 2026-10-20 17:06 | LINK-USDT-SWAP | 12.21 | 12.21/12.10 | 12.21 | — | 0.13743 | 0.0048% | B/venda@12.26 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 18:06 | BTC-USDT-SWAP | 82812.2 | 82817.0/82486.4 | 82575.0 | res 83436.9 (ha 6 candles) | 491.56 | 0.0071% | — | descartado_rr_baixo_setup_B |
| 2026-10-20 18:06 | ETH-USDT-SWAP | 2448.0 | 2448.7/2433.2 | 2437.0 | res 2477.8 (ha 6 candles) | 22.22 | 0.0081% | A/compra@2416.8 (0t/4c) | zona_mapeada_setup_A |
| 2026-10-20 18:06 | SOL-USDT-SWAP | 106.69 | 106.75/105.86 | 106.03 | res 108.24 (ha 6 candles) | 1.1529 | 0.0025% | B/compra@108.37 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-20 18:06 | XRP-USDT-SWAP | 1.3341 | 1.3353/1.3257 | 1.3285 | — | 0.01341 | 0.0021% | B/venda@1.3469 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-20 18:06 | DOGE-USDT-SWAP | 0.08193 | 0.08200/0.08141 | 0.08153 | — | 0.00078 | 0.0100% | — | sem_zona |
| 2026-10-20 18:06 | ARB-USDT-SWAP | 0.19044 | 0.19070/0.18799 | 0.18890 | — | 0.00393 | -0.0038% | — | sem_zona |
| 2026-10-20 18:06 | WLD-USDT-SWAP | 0.58790 | 0.59620/0.57930 | 0.58190 | sup 0.52950 (ha 11 candles) | 0.01354 | 0.0100% | — | zona_expirada_setup_B |
| 2026-10-20 18:06 | SUI-USDT-SWAP | 1.0315 | 1.0333/1.0188 | 1.0227 | — | 0.01549 | 0.0092% | — | sem_zona |
| 2026-10-20 18:06 | UNI-USDT-SWAP | 7.4450 | 7.4580/7.2960 | 7.3220 | — | 0.13621 | 0.0061% | B/venda@7.4530 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 18:06 | LINK-USDT-SWAP | 12.31 | 12.31/12.19 | 12.21 | — | 0.13914 | 0.0061% | — | invalidado_setup_B |
| 2026-10-20 19:06 | BTC-USDT-SWAP | 82931.5 | 82984.5/82779.8 | 82575.0 | res 83436.9 (ha 7 candles) | 478.09 | 0.0070% | B/compra@82907.7 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 19:06 | ETH-USDT-SWAP | 2456.4 | 2459.9/2446.9 | 2437.0 | res 2477.8 (ha 7 candles) | 22.23 | 0.0091% | A/compra@2416.8 (0t/5c) | zona_mapeada_setup_A |
| 2026-10-20 19:06 | SOL-USDT-SWAP | 106.71 | 107.02/106.46 | 106.03 | res 108.24 (ha 7 candles) | 1.1557 | 0.0047% | B/compra@108.37 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-20 19:06 | XRP-USDT-SWAP | 1.3318 | 1.3363/1.3300 | 1.3285 | — | 0.01334 | 0.0028% | B/venda@1.3469 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-20 19:06 | DOGE-USDT-SWAP | 0.08179 | 0.08197/0.08165 | 0.08153 | — | 0.00078 | 0.0100% | — | sem_zona |
| 2026-10-20 19:06 | ARB-USDT-SWAP | 0.18913 | 0.19187/0.18904 | 0.18890 | — | 0.00375 | -0.0038% | — | sem_zona |
| 2026-10-20 19:06 | WLD-USDT-SWAP | 0.59250 | 0.59450/0.58250 | 0.58190 | sup 0.52950 (ha 12 candles) | 0.01379 | 0.0100% | B/venda@0.59040 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 19:06 | SUI-USDT-SWAP | 1.0296 | 1.0333/1.0272 | 1.0227 | — | 0.01534 | 0.0100% | — | sem_zona |
| 2026-10-20 19:06 | UNI-USDT-SWAP | 7.4860 | 7.5080/7.4400 | 7.3220 | — | 0.13736 | 0.0056% | B/venda@7.4530 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-20 19:06 | LINK-USDT-SWAP | 12.29 | 12.33/12.27 | 12.21 | — | 0.13800 | 0.0068% | — | sem_zona |
| 2026-10-20 20:06 | BTC-USDT-SWAP | 83055.9 | 83148.4/82905.8 | 82575.0 | res 83436.9 (ha 8 candles) | 475.87 | 0.0064% | — | descartado_rr_baixo_setup_B |
| 2026-10-20 20:06 | ETH-USDT-SWAP | 2455.0 | 2464.5/2453.6 | 2437.0 | res 2477.8 (ha 8 candles) | 21.98 | 0.0095% | A/compra@2416.8 (0t/6c) | zona_mapeada_setup_A |
| 2026-10-20 20:06 | SOL-USDT-SWAP | 106.81 | 107.17/106.63 | 106.03 | res 108.24 (ha 8 candles) | 1.1457 | 0.0065% | — | zona_expirada_setup_B |
| 2026-10-20 20:06 | XRP-USDT-SWAP | 1.3376 | 1.3441/1.3313 | 1.3285 | — | 0.01367 | 0.0036% | — | zona_expirada_setup_B |
| 2026-10-20 20:06 | DOGE-USDT-SWAP | 0.08205 | 0.08225/0.08171 | 0.08153 | — | 0.00078 | 0.0100% | — | sem_zona |
| 2026-10-20 20:06 | ARB-USDT-SWAP | 0.18816 | 0.19075/0.18806 | 0.18890 | — | 0.00364 | -0.0074% | — | sem_zona |
| 2026-10-20 20:06 | WLD-USDT-SWAP | 0.58880 | 0.59460/0.58750 | 0.58190 | sup 0.52950 (ha 13 candles) | 0.01387 | 0.0100% | — | confirmado_calibracao_setup_B |
| 2026-10-20 20:06 | SUI-USDT-SWAP | 1.0310 | 1.0355/1.0285 | 1.0227 | — | 0.01519 | 0.0100% | — | sem_zona |
| 2026-10-20 20:06 | UNI-USDT-SWAP | 7.4770 | 7.5800/7.4740 | 7.3220 | — | 0.13836 | 0.0081% | — | descartado_rr_baixo_setup_B |
| 2026-10-20 20:06 | LINK-USDT-SWAP | 12.31 | 12.35/12.29 | 12.21 | — | 0.13657 | 0.0071% | — | sem_zona |
| 2026-10-20 21:06 | BTC-USDT-SWAP | 82984.5 | 83056.0/82838.6 | 82984.5 | res 83436.9 (ha 9 candles) | 470.41 | 0.0054% | B/compra@82752.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 21:06 | ETH-USDT-SWAP | 2448.1 | 2455.0/2444.5 | 2448.1 | res 2477.8 (ha 9 candles) | 21.85 | 0.0097% | A/compra@2416.8 (0t/7c) | zona_mapeada_setup_A |
| 2026-10-20 21:06 | SOL-USDT-SWAP | 106.47 | 106.83/106.26 | 106.47 | res 108.24 (ha 9 candles) | 1.1471 | 0.0073% | B/compra@105.61 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 21:06 | XRP-USDT-SWAP | 1.3353 | 1.3376/1.3329 | 1.3353 | — | 0.01354 | 0.0060% | — | sem_zona |
| 2026-10-20 21:06 | DOGE-USDT-SWAP | 0.08183 | 0.08205/0.08171 | 0.08183 | — | 0.00077 | 0.0100% | — | sem_zona |
| 2026-10-20 21:06 | ARB-USDT-SWAP | 0.18748 | 0.18816/0.18636 | 0.18748 | — | 0.00364 | -0.0081% | — | sem_zona |
| 2026-10-20 21:06 | WLD-USDT-SWAP | 0.58710 | 0.59140/0.58570 | 0.58710 | sup 0.52950 (ha 14 candles) | 0.01365 | 0.0100% | B/venda@0.58590 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 21:06 | SUI-USDT-SWAP | 1.0298 | 1.0317/1.0274 | 1.0298 | — | 0.01503 | 0.0100% | — | sem_zona |
| 2026-10-20 21:06 | UNI-USDT-SWAP | 7.4400 | 7.4800/7.4260 | 7.4400 | res 7.5680 (ha 9 candles) | 0.13736 | 0.0087% | B/compra@7.4520 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 21:06 | LINK-USDT-SWAP | 12.32 | 12.34/12.27 | 12.32 | — | 0.13657 | 0.0063% | — | sem_zona |
| 2026-10-20 22:06 | BTC-USDT-SWAP | 82985.4 | 83188.8/82830.0 | 82984.5 | res 83436.9 (ha 10 candles) | 483.19 | 0.0044% | B/compra@82752.0 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-20 22:06 | ETH-USDT-SWAP | 2452.1 | 2458.0/2442.7 | 2448.1 | res 2477.8 (ha 10 candles) | 22.34 | 0.0100% | — | zona_expirada_setup_A |
| 2026-10-20 22:06 | SOL-USDT-SWAP | 106.57 | 106.94/106.21 | 106.47 | res 108.24 (ha 10 candles) | 1.1671 | 0.0070% | B/compra@105.61 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-20 22:06 | XRP-USDT-SWAP | 1.3366 | 1.3404/1.3330 | 1.3353 | — | 0.01370 | 0.0088% | — | sem_zona |
| 2026-10-20 22:06 | DOGE-USDT-SWAP | 0.08207 | 0.08232/0.08165 | 0.08183 | — | 0.00080 | 0.0100% | — | sem_zona |
| 2026-10-20 22:06 | ARB-USDT-SWAP | 0.18840 | 0.18955/0.18677 | 0.18748 | — | 0.00374 | -0.0116% | — | sem_zona |
| 2026-10-20 22:06 | WLD-USDT-SWAP | 0.58220 | 0.59000/0.57960 | 0.58710 | sup 0.52950 (ha 15 candles) | 0.01349 | 0.0100% | — | confirmado_calibracao_setup_B |
| 2026-10-20 22:06 | SUI-USDT-SWAP | 1.0348 | 1.0407/1.0278 | 1.0298 | — | 0.01548 | 0.0100% | — | sem_zona |
| 2026-10-20 22:06 | UNI-USDT-SWAP | 7.5990 | 7.6990/7.4160 | 7.4400 | res 7.5680 (ha 10 candles) | 0.15429 | 0.0034% | — | descartado_rr_baixo_setup_B |
| 2026-10-20 22:06 | LINK-USDT-SWAP | 12.37 | 12.40/12.29 | 12.32 | — | 0.14121 | 0.0048% | — | sem_zona |
| 2026-10-20 23:06 | BTC-USDT-SWAP | 82958.5 | 83187.4/82734.1 | 82984.5 | res 83436.9 (ha 11 candles) | 500.25 | 0.0039% | B/compra@82752.0 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-20 23:06 | ETH-USDT-SWAP | 2454.7 | 2464.5/2441.3 | 2448.1 | res 2477.8 (ha 11 candles) | 23.34 | 0.0099% | — | sem_zona |
| 2026-10-20 23:06 | SOL-USDT-SWAP | 106.65 | 107.09/106.17 | 106.47 | res 107.17 (ha 3 candles) | 1.1993 | 0.0069% | B/compra@105.61 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-20 23:06 | XRP-USDT-SWAP | 1.3383 | 1.3427/1.3326 | 1.3353 | — | 0.01377 | 0.0100% | — | sem_zona |
| 2026-10-20 23:06 | DOGE-USDT-SWAP | 0.08206 | 0.08230/0.08173 | 0.08183 | — | 0.00081 | 0.0100% | — | sem_zona |
| 2026-10-20 23:06 | ARB-USDT-SWAP | 0.19368 | 0.19682/0.18758 | 0.18748 | — | 0.00425 | -0.0081% | B/venda@0.19508 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 23:06 | WLD-USDT-SWAP | 0.58510 | 0.59320/0.57920 | 0.58710 | sup 0.52950 (ha 16 candles) | 0.01391 | 0.0100% | B/venda@0.57610 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 23:06 | SUI-USDT-SWAP | 1.0330 | 1.0408/1.0283 | 1.0298 | — | 0.01586 | 0.0100% | — | sem_zona |
| 2026-10-20 23:06 | UNI-USDT-SWAP | 7.6310 | 7.7850/7.5070 | 7.4400 | res 7.5680 (ha 11 candles) | 0.16943 | -0.0026% | A/compra@7.5680 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-20 23:06 | LINK-USDT-SWAP | 12.40 | 12.46/12.32 | 12.32 | — | 0.14564 | 0.0040% | — | sem_zona |
| 2026-10-21 00:06 | BTC-USDT-SWAP | 82767.9 | 82994.9/82684.5 | 82984.5 | res 83436.9 (ha 12 candles) | 490.72 | 0.0032% | — | zona_expirada_setup_B |
| 2026-10-21 00:06 | ETH-USDT-SWAP | 2447.6 | 2456.2/2445.5 | 2448.1 | res 2477.8 (ha 12 candles) | 22.47 | 0.0094% | — | sem_zona |
| 2026-10-21 00:06 | SOL-USDT-SWAP | 106.24 | 106.72/106.00 | 106.47 | res 107.17 (ha 4 candles) | 1.1857 | 0.0076% | B/compra@105.61 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-21 00:06 | XRP-USDT-SWAP | 1.3344 | 1.3390/1.3312 | 1.3353 | — | 0.01371 | 0.0100% | — | sem_zona |
| 2026-10-21 00:06 | DOGE-USDT-SWAP | 0.08183 | 0.08214/0.08152 | 0.08183 | — | 0.00081 | 0.0100% | — | sem_zona |
| 2026-10-21 00:06 | ARB-USDT-SWAP | 0.19184 | 0.19380/0.19120 | 0.18748 | — | 0.00427 | -0.0050% | B/venda@0.19508 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-21 00:06 | WLD-USDT-SWAP | 0.59140 | 0.59370/0.58310 | 0.58710 | sup 0.52950 (ha 17 candles) | 0.01349 | 0.0100% | B/venda@0.57610 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-21 00:06 | SUI-USDT-SWAP | 1.0290 | 1.0344/1.0239 | 1.0298 | — | 0.01566 | 0.0100% | — | sem_zona |
| 2026-10-21 00:06 | UNI-USDT-SWAP | 7.6200 | 7.6720/7.5490 | 7.4400 | res 7.5680 (ha 12 candles) | 0.17221 | -0.0064% | A/compra@7.5680 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-21 00:06 | LINK-USDT-SWAP | 12.35 | 12.41/12.32 | 12.32 | — | 0.14536 | 0.0017% | B/compra@12.25 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-21 01:06 | BTC-USDT-SWAP | 82694.5 | 82835.7/82690.8 | 82694.5 | res 83188.8 (ha 3 candles) | 438.50 | 0.0030% | B/compra@82907.7 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-21 01:06 | ETH-USDT-SWAP | 2443.3 | 2451.0/2443.2 | 2443.3 | res 2477.8 (ha 13 candles) | 20.83 | 0.0093% | — | sem_zona |
| 2026-10-21 01:06 | SOL-USDT-SWAP | 105.78 | 106.26/105.78 | 105.78 | res 107.17 (ha 5 candles) | 1.1164 | 0.0075% | B/compra@105.61 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-21 01:06 | XRP-USDT-SWAP | 1.3316 | 1.3345/1.3311 | 1.3316 | res 1.3441 (ha 5 candles) | 0.01288 | 0.0100% | — | sem_zona |
| 2026-10-21 01:06 | DOGE-USDT-SWAP | 0.08146 | 0.08182/0.08146 | 0.08146 | — | 0.00076 | 0.0100% | B/compra@0.08092 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-21 01:06 | ARB-USDT-SWAP | 0.19082 | 0.19186/0.18921 | 0.19082 | res 0.19880 (ha 13 candles) | 0.00411 | -0.0044% | B/venda@0.19508 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-21 01:06 | WLD-USDT-SWAP | 0.59090 | 0.59330/0.58570 | 0.59090 | sup 0.52950 (ha 18 candles) | 0.01331 | 0.0100% | B/venda@0.57610 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-21 01:06 | SUI-USDT-SWAP | 1.0256 | 1.0289/1.0230 | 1.0256 | res 1.0437 (ha 13 candles) | 0.01436 | 0.0100% | — | sem_zona |
| 2026-10-21 01:06 | UNI-USDT-SWAP | 7.5370 | 7.6240/7.5360 | 7.5370 | res 7.5680 (ha 13 candles) | 0.16529 | -0.0087% | A/compra@7.5680 (2t/0c) | zona_mapeada_setup_A |
| 2026-10-21 01:06 | LINK-USDT-SWAP | 12.32 | 12.36/12.32 | 12.32 | res 12.47 (ha 13 candles) | 0.13557 | -0.0009% | B/compra@12.25 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-21 02:06 | BTC-USDT-SWAP | 82773.6 | 82865.0/82694.5 | 82694.5 | res 83188.8 (ha 4 candles) | 352.79 | 0.0035% | — | invalidado_setup_B |
| 2026-10-21 02:06 | ETH-USDT-SWAP | 2444.1 | 2446.8/2441.1 | 2443.3 | res 2464.5 (ha 3 candles) | 16.25 | 0.0088% | — | sem_zona |
| 2026-10-21 02:06 | SOL-USDT-SWAP | 105.83 | 105.98/105.64 | 105.78 | res 107.17 (ha 6 candles) | 0.91929 | 0.0069% | B/compra@105.61 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-21 02:06 | XRP-USDT-SWAP | 1.3329 | 1.3339/1.3308 | 1.3316 | res 1.3441 (ha 6 candles) | 0.01049 | 0.0100% | — | sem_zona |
| 2026-10-21 02:06 | DOGE-USDT-SWAP | 0.08154 | 0.08166/0.08138 | 0.08146 | — | 0.00064 | 0.0100% | B/compra@0.08092 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-21 02:06 | ARB-USDT-SWAP | 0.19043 | 0.19257/0.19041 | 0.19082 | res 0.19682 (ha 3 candles) | 0.00376 | -0.0053% | B/venda@0.19508 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-21 02:06 | WLD-USDT-SWAP | 0.58980 | 0.59870/0.58810 | 0.59090 | sup 0.57920 (ha 3 candles) | 0.01178 | 0.0100% | B/venda@0.57610 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-21 02:06 | SUI-USDT-SWAP | 1.0238 | 1.0282/1.0226 | 1.0256 | res 1.0408 (ha 3 candles) | 0.01253 | 0.0100% | — | sem_zona |
| 2026-10-21 02:06 | UNI-USDT-SWAP | 7.4830 | 7.5600/7.4790 | 7.5370 | res 7.7850 (ha 3 candles) | 0.14943 | -0.0055% | — | invalidado_setup_A |
| 2026-10-21 02:06 | LINK-USDT-SWAP | 12.33 | 12.36/12.31 | 12.32 | res 12.46 (ha 3 candles) | 0.11164 | -0.0028% | B/compra@12.25 (0t/2c) | zona_mapeada_setup_B |
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
