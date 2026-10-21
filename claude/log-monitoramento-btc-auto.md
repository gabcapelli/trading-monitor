# Log de Monitoramento Automatico -- Multi-Par (script gratuito, GitHub Actions)

> Gerado por script Python sem LLM (ver monitor/fetch_and_check.py). Fonte: OKX. Cobre os pares em PAIRS (configuracao no topo do script) -- BTC-USDT-SWAP e os demais adicionados na expansao de 07/09/2026. Leitura e MECANICA (regras objetivas da secao 4 do plano), sem a prosa qualitativa que o Claude gerava -- cole este log numa conversa do Claude se quiser a leitura interpretativa.

| Data/Hora (BRT) | Par | Close 1h | High/Low 1h | Close 4h | Swing 1h ref | ATR 1h | Funding | Zona ativa | Status checklist |
|---|---|---|---|---|---|---|---|---|---|
| 2026-10-19 00:05 | BTC-USDT-SWAP | 82677.0 | 82777.0/82306.9 | 82069.5 | sup 80621.4 (ha 6 candles) | 400.34 | 0.0050% | B/compra@80961.3 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-19 00:05 | ETH-USDT-SWAP | 2425.7 | 2437.8/2415.1 | 2409.4 | sup 2328.0 (ha 7 candles) | 22.33 | 0.0099% | — | sem_zona |
| 2026-10-19 00:05 | SOL-USDT-SWAP | 105.44 | 105.86/104.76 | 104.06 | sup 100.34 (ha 7 candles) | 1.0486 | 0.0029% | B/venda@105.22 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-19 00:05 | XRP-USDT-SWAP | 1.3123 | 1.3161/1.3062 | 1.3064 | — | 0.01213 | 0.0064% | — | invalidado_setup_B |
| 2026-10-19 00:05 | DOGE-USDT-SWAP | 0.08001 | 0.08025/0.07946 | 0.07941 | sup 0.07603 (ha 7 candles) | 0.00091 | 0.0025% | — | sem_zona |
| 2026-10-19 00:05 | ARB-USDT-SWAP | 0.19220 | 0.19300/0.18883 | 0.18691 | res 0.18141 (ha 9 candles) | 0.00328 | -0.0006% | B/compra@0.17409 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-19 00:05 | WLD-USDT-SWAP | 0.49230 | 0.49510/0.48590 | 0.48870 | sup 0.45610 (ha 6 candles) | 0.00994 | 0.0051% | — | sem_zona |
| 2026-10-19 00:05 | SUI-USDT-SWAP | 1.0071 | 1.0109/0.99640 | 0.99630 | sup 0.93640 (ha 7 candles) | 0.01392 | 0.0001% | — | sem_zona |
| 2026-10-19 00:05 | UNI-USDT-SWAP | 7.2910 | 7.3250/7.2210 | 7.1950 | sup 6.8030 (ha 7 candles) | 0.11336 | 0.0083% | B/venda@7.3540 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 00:05 | LINK-USDT-SWAP | 12.21 | 12.26/12.13 | 12.03 | — | 0.13521 | -0.0015% | B/compra@12.25 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 01:05 | BTC-USDT-SWAP | 82475.8 | 82688.0/82429.6 | 82475.8 | sup 80621.4 (ha 7 candles) | 371.05 | 0.0038% | B/compra@80961.3 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-19 01:05 | ETH-USDT-SWAP | 2423.2 | 2428.6/2420.3 | 2423.2 | sup 2328.0 (ha 8 candles) | 20.43 | 0.0091% | — | sem_zona |
| 2026-10-19 01:05 | SOL-USDT-SWAP | 105.19 | 105.49/105.07 | 105.19 | sup 100.34 (ha 8 candles) | 0.95357 | 0.0018% | — | descartado_rr_baixo_setup_B |
| 2026-10-19 01:05 | XRP-USDT-SWAP | 1.3096 | 1.3130/1.3082 | 1.3096 | — | 0.01101 | 0.0066% | B/compra@1.3102 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 01:05 | DOGE-USDT-SWAP | 0.07961 | 0.08003/0.07954 | 0.07961 | sup 0.07603 (ha 8 candles) | 0.00082 | 0.0003% | — | sem_zona |
| 2026-10-19 01:05 | ARB-USDT-SWAP | 0.19274 | 0.19275/0.18987 | 0.19274 | res 0.18141 (ha 10 candles) | 0.00319 | -0.0014% | — | zona_expirada_setup_B |
| 2026-10-19 01:05 | WLD-USDT-SWAP | 0.49150 | 0.49340/0.48940 | 0.49150 | sup 0.45610 (ha 7 candles) | 0.00895 | 0.0086% | — | sem_zona |
| 2026-10-19 01:05 | SUI-USDT-SWAP | 1.0008 | 1.0076/0.99930 | 1.0008 | sup 0.93640 (ha 8 candles) | 0.01309 | -0.0011% | — | sem_zona |
| 2026-10-19 01:05 | UNI-USDT-SWAP | 7.2930 | 7.3240/7.2680 | 7.2930 | sup 6.8030 (ha 8 candles) | 0.10500 | 0.0048% | B/venda@7.3540 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-19 01:05 | LINK-USDT-SWAP | 12.17 | 12.22/12.17 | 12.17 | — | 0.12300 | 0.0011% | — | invalidado_setup_B |
| 2026-10-19 02:05 | BTC-USDT-SWAP | 82740.6 | 82846.5/82438.6 | 82475.8 | sup 80621.4 (ha 8 candles) | 362.45 | 0.0034% | B/compra@80961.3 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-19 02:05 | ETH-USDT-SWAP | 2427.9 | 2432.6/2419.1 | 2423.2 | sup 2328.0 (ha 9 candles) | 19.22 | 0.0088% | B/venda@2441.4 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 02:05 | SOL-USDT-SWAP | 105.63 | 105.95/105.04 | 105.19 | sup 100.34 (ha 9 candles) | 0.93429 | 0.0027% | — | sem_zona |
| 2026-10-19 02:05 | XRP-USDT-SWAP | 1.3125 | 1.3159/1.3086 | 1.3096 | — | 0.01069 | 0.0071% | B/compra@1.3102 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-19 02:05 | DOGE-USDT-SWAP | 0.07962 | 0.07996/0.07936 | 0.07961 | sup 0.07603 (ha 9 candles) | 0.00080 | 0.0026% | — | sem_zona |
| 2026-10-19 02:05 | ARB-USDT-SWAP | 0.19271 | 0.19431/0.19155 | 0.19274 | res 0.18141 (ha 11 candles) | 0.00317 | 0.0004% | A/compra@0.18141 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-19 02:05 | WLD-USDT-SWAP | 0.49450 | 0.49660/0.48920 | 0.49150 | sup 0.45610 (ha 8 candles) | 0.00870 | 0.0100% | — | sem_zona |
| 2026-10-19 02:05 | SUI-USDT-SWAP | 1.0071 | 1.0116/0.99720 | 1.0008 | sup 0.93640 (ha 9 candles) | 0.01293 | -0.0001% | — | sem_zona |
| 2026-10-19 02:05 | UNI-USDT-SWAP | 7.3670 | 7.4190/7.2760 | 7.2930 | sup 6.8030 (ha 9 candles) | 0.10443 | 0.0033% | B/venda@7.3540 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-19 02:06 | LINK-USDT-SWAP | 12.16 | 12.18/12.10 | 12.17 | — | 0.11886 | 0.0039% | B/compra@12.15 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 03:05 | BTC-USDT-SWAP | 82725.6 | 82749.8/82500.2 | 82475.8 | sup 80621.4 (ha 9 candles) | 361.85 | 0.0037% | — | zona_expirada_setup_B |
| 2026-10-19 03:05 | ETH-USDT-SWAP | 2430.6 | 2430.6/2420.2 | 2423.2 | sup 2328.0 (ha 10 candles) | 19.01 | 0.0089% | B/venda@2441.4 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-19 03:05 | SOL-USDT-SWAP | 105.64 | 105.79/105.19 | 105.19 | sup 100.34 (ha 10 candles) | 0.92071 | 0.0024% | — | sem_zona |
| 2026-10-19 03:05 | XRP-USDT-SWAP | 1.3128 | 1.3128/1.3076 | 1.3096 | — | 0.01028 | 0.0065% | — | descartado_rr_baixo_setup_B |
| 2026-10-19 03:05 | DOGE-USDT-SWAP | 0.07967 | 0.07967/0.07925 | 0.07961 | sup 0.07603 (ha 10 candles) | 0.00076 | 0.0055% | — | sem_zona |
| 2026-10-19 03:05 | ARB-USDT-SWAP | 0.19352 | 0.19421/0.19167 | 0.19274 | res 0.18141 (ha 12 candles) | 0.00320 | 0.0023% | A/compra@0.18141 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-19 03:05 | WLD-USDT-SWAP | 0.49560 | 0.49760/0.49050 | 0.49150 | sup 0.45610 (ha 9 candles) | 0.00860 | 0.0100% | — | sem_zona |
| 2026-10-19 03:05 | SUI-USDT-SWAP | 1.0095 | 1.0117/1.0006 | 1.0008 | sup 0.93640 (ha 10 candles) | 0.01294 | 0.0021% | — | sem_zona |
| 2026-10-19 03:05 | UNI-USDT-SWAP | 7.3860 | 7.4190/7.3290 | 7.2930 | sup 6.8030 (ha 10 candles) | 0.10214 | 0.0035% | — | invalidado_setup_B |
| 2026-10-19 03:05 | LINK-USDT-SWAP | 12.16 | 12.18/12.08 | 12.17 | — | 0.11771 | 0.0077% | — | descartado_rr_baixo_setup_B |
| 2026-10-19 04:05 | BTC-USDT-SWAP | 82808.5 | 82897.1/82646.2 | 82475.8 | sup 80621.4 (ha 10 candles) | 361.76 | 0.0044% | B/venda@82898.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 04:05 | ETH-USDT-SWAP | 2429.4 | 2435.6/2427.6 | 2423.2 | sup 2328.0 (ha 11 candles) | 18.30 | 0.0076% | B/venda@2441.4 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-19 04:05 | SOL-USDT-SWAP | 105.69 | 105.87/105.47 | 105.19 | sup 100.34 (ha 11 candles) | 0.91786 | 0.0023% | — | sem_zona |
| 2026-10-19 04:05 | XRP-USDT-SWAP | 1.3139 | 1.3152/1.3112 | 1.3096 | — | 0.01020 | 0.0066% | B/compra@1.3176 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 04:05 | DOGE-USDT-SWAP | 0.07980 | 0.07984/0.07953 | 0.07961 | sup 0.07603 (ha 11 candles) | 0.00074 | 0.0086% | — | sem_zona |
| 2026-10-19 04:05 | ARB-USDT-SWAP | 0.19549 | 0.19872/0.19338 | 0.19274 | res 0.18141 (ha 13 candles) | 0.00346 | 0.0015% | A/compra@0.18141 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-19 04:05 | WLD-USDT-SWAP | 0.49580 | 0.49870/0.49370 | 0.49150 | sup 0.45610 (ha 10 candles) | 0.00865 | 0.0083% | — | sem_zona |
| 2026-10-19 04:05 | SUI-USDT-SWAP | 1.0088 | 1.0115/1.0074 | 1.0008 | sup 0.93640 (ha 11 candles) | 0.01272 | 0.0035% | — | sem_zona |
| 2026-10-19 04:05 | UNI-USDT-SWAP | 7.3880 | 7.4050/7.3460 | 7.2930 | sup 6.8030 (ha 11 candles) | 0.10243 | 0.0039% | B/venda@7.4530 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 04:05 | LINK-USDT-SWAP | 12.20 | 12.21/12.13 | 12.17 | — | 0.11929 | 0.0097% | B/compra@12.25 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 05:05 | BTC-USDT-SWAP | 82690.5 | 83149.8/82639.3 | 82690.5 | sup 80621.4 (ha 11 candles) | 387.26 | 0.0061% | — | descartado_rr_baixo_setup_B |
| 2026-10-19 05:05 | ETH-USDT-SWAP | 2429.3 | 2446.0/2428.3 | 2429.3 | sup 2328.0 (ha 12 candles) | 18.80 | 0.0063% | — | descartado_rr_baixo_setup_B |
| 2026-10-19 05:05 | SOL-USDT-SWAP | 105.59 | 106.18/105.53 | 105.59 | sup 100.34 (ha 12 candles) | 0.92071 | 0.0029% | — | sem_zona |
| 2026-10-19 05:05 | XRP-USDT-SWAP | 1.3129 | 1.3212/1.3127 | 1.3129 | — | 0.01034 | 0.0062% | — | invalidado_setup_B |
| 2026-10-19 05:05 | DOGE-USDT-SWAP | 0.07973 | 0.08016/0.07969 | 0.07973 | sup 0.07603 (ha 12 candles) | 0.00074 | 0.0097% | — | sem_zona |
| 2026-10-19 05:05 | ARB-USDT-SWAP | 0.19800 | 0.19868/0.19544 | 0.19800 | — | 0.00353 | 0.0020% | A/compra@0.18141 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-19 05:05 | WLD-USDT-SWAP | 0.50740 | 0.51050/0.49550 | 0.50740 | sup 0.45610 (ha 11 candles) | 0.00912 | 0.0081% | B/venda@0.51160 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 05:05 | SUI-USDT-SWAP | 1.0119 | 1.0171/1.0087 | 1.0119 | sup 0.93640 (ha 12 candles) | 0.01283 | 0.0026% | — | sem_zona |
| 2026-10-19 05:05 | UNI-USDT-SWAP | 7.4370 | 7.4830/7.3860 | 7.4370 | sup 6.8030 (ha 12 candles) | 0.10443 | -0.0004% | B/venda@7.4530 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-19 05:05 | LINK-USDT-SWAP | 12.19 | 12.26/12.18 | 12.19 | — | 0.11986 | 0.0077% | — | invalidado_setup_B |
| 2026-10-19 06:05 | BTC-USDT-SWAP | 82788.1 | 82940.0/82550.0 | 82690.5 | sup 80621.4 (ha 12 candles) | 400.95 | 0.0084% | B/venda@82624.9 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 06:05 | ETH-USDT-SWAP | 2434.3 | 2439.0/2425.8 | 2429.3 | sup 2328.0 (ha 13 candles) | 18.89 | 0.0055% | — | sem_zona |
| 2026-10-19 06:05 | SOL-USDT-SWAP | 105.63 | 105.93/105.38 | 105.59 | sup 100.34 (ha 13 candles) | 0.92786 | 0.0036% | — | sem_zona |
| 2026-10-19 06:05 | XRP-USDT-SWAP | 1.3139 | 1.3165/1.3098 | 1.3129 | — | 0.01046 | 0.0057% | B/compra@1.3102 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 06:05 | DOGE-USDT-SWAP | 0.07973 | 0.07992/0.07943 | 0.07973 | sup 0.07925 (ha 3 candles) | 0.00075 | 0.0100% | — | sem_zona |
| 2026-10-19 06:05 | ARB-USDT-SWAP | 0.19838 | 0.20020/0.19764 | 0.19800 | — | 0.00362 | 0.0002% | A/compra@0.18141 (0t/4c) | zona_mapeada_setup_A |
| 2026-10-19 06:05 | WLD-USDT-SWAP | 0.50620 | 0.51140/0.50230 | 0.50740 | sup 0.45610 (ha 12 candles) | 0.00924 | 0.0100% | B/venda@0.51160 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-19 06:05 | SUI-USDT-SWAP | 1.0067 | 1.0138/1.0055 | 1.0119 | sup 0.93640 (ha 13 candles) | 0.01303 | 0.0049% | — | sem_zona |
| 2026-10-19 06:05 | UNI-USDT-SWAP | 7.4040 | 7.4460/7.3830 | 7.4370 | sup 6.8030 (ha 13 candles) | 0.10543 | -0.0007% | — | descartado_rr_baixo_setup_B |
| 2026-10-19 06:05 | LINK-USDT-SWAP | 12.16 | 12.21/12.15 | 12.19 | — | 0.12000 | 0.0091% | B/compra@12.15 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 07:05 | BTC-USDT-SWAP | 82733.0 | 83067.4/82702.2 | 82690.5 | sup 80621.4 (ha 13 candles) | 398.14 | 0.0099% | — | invalidado_setup_B |
| 2026-10-19 07:05 | ETH-USDT-SWAP | 2436.1 | 2445.4/2431.0 | 2429.3 | sup 2328.0 (ha 14 candles) | 16.99 | 0.0046% | — | sem_zona |
| 2026-10-19 07:05 | SOL-USDT-SWAP | 105.41 | 105.91/105.38 | 105.59 | sup 100.34 (ha 14 candles) | 0.82500 | 0.0035% | — | sem_zona |
| 2026-10-19 07:05 | XRP-USDT-SWAP | 1.3125 | 1.3170/1.3118 | 1.3129 | — | 0.00930 | 0.0052% | B/compra@1.3102 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-19 07:05 | DOGE-USDT-SWAP | 0.07969 | 0.07999/0.07960 | 0.07973 | sup 0.07925 (ha 4 candles) | 0.00065 | 0.0100% | — | sem_zona |
| 2026-10-19 07:05 | ARB-USDT-SWAP | 0.19755 | 0.19965/0.19728 | 0.19800 | — | 0.00344 | 0.0017% | A/compra@0.18141 (0t/5c) | zona_mapeada_setup_A |
| 2026-10-19 07:05 | WLD-USDT-SWAP | 0.50270 | 0.50890/0.50220 | 0.50740 | sup 0.45610 (ha 13 candles) | 0.00891 | 0.0100% | B/venda@0.51160 (1t/1c) | zona_mapeada_setup_B |
| 2026-10-19 07:05 | SUI-USDT-SWAP | 1.0049 | 1.0121/1.0041 | 1.0119 | sup 0.93640 (ha 14 candles) | 0.01175 | 0.0073% | — | sem_zona |
| 2026-10-19 07:05 | UNI-USDT-SWAP | 7.3920 | 7.4340/7.3810 | 7.4370 | sup 6.8030 (ha 14 candles) | 0.09757 | -0.0004% | B/venda@7.3540 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 07:05 | LINK-USDT-SWAP | 12.13 | 12.19/12.13 | 12.19 | — | 0.10571 | 0.0099% | B/compra@12.15 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-19 08:05 | BTC-USDT-SWAP | 82390.6 | 82872.8/82083.0 | 82690.5 | sup 80621.4 (ha 14 candles) | 429.69 | 0.0100% | — | sem_zona |
| 2026-10-19 08:05 | ETH-USDT-SWAP | 2425.3 | 2438.1/2414.0 | 2429.3 | sup 2328.0 (ha 15 candles) | 17.25 | 0.0053% | — | sem_zona |
| 2026-10-19 08:05 | SOL-USDT-SWAP | 104.93 | 105.59/104.38 | 105.59 | sup 100.34 (ha 15 candles) | 0.84786 | 0.0050% | — | sem_zona |
| 2026-10-19 08:05 | XRP-USDT-SWAP | 1.3041 | 1.3138/1.2985 | 1.3129 | — | 0.00985 | 0.0039% | — | invalidado_setup_B |
| 2026-10-19 08:05 | DOGE-USDT-SWAP | 0.07919 | 0.07978/0.07874 | 0.07973 | sup 0.07925 (ha 5 candles) | 0.00069 | 0.0097% | A/venda@0.07925 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-19 08:05 | ARB-USDT-SWAP | 0.19615 | 0.19813/0.19500 | 0.19800 | — | 0.00352 | 0.0069% | A/compra@0.18141 (0t/6c) | zona_mapeada_setup_A |
| 2026-10-19 08:05 | WLD-USDT-SWAP | 0.49880 | 0.50640/0.49330 | 0.50740 | sup 0.45610 (ha 14 candles) | 0.00904 | 0.0100% | B/venda@0.51160 (1t/2c) | zona_mapeada_setup_B |
| 2026-10-19 08:05 | SUI-USDT-SWAP | 0.99870 | 1.0072/0.99100 | 1.0119 | sup 0.93640 (ha 15 candles) | 0.01236 | 0.0094% | — | sem_zona |
| 2026-10-19 08:05 | UNI-USDT-SWAP | 7.3650 | 7.3990/7.3000 | 7.4370 | sup 6.8030 (ha 15 candles) | 0.10000 | 0.0028% | B/venda@7.3540 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-19 08:05 | LINK-USDT-SWAP | 12.07 | 12.16/12.02 | 12.19 | — | 0.10850 | 0.0099% | — | invalidado_setup_B |
| 2026-10-19 09:05 | BTC-USDT-SWAP | 82331.9 | 82390.6/82104.8 | 82331.9 | sup 80621.4 (ha 15 candles) | 426.32 | 0.0100% | — | sem_zona |
| 2026-10-19 09:05 | ETH-USDT-SWAP | 2418.9 | 2425.3/2411.0 | 2418.9 | sup 2328.0 (ha 16 candles) | 16.69 | 0.0061% | — | sem_zona |
| 2026-10-19 09:05 | SOL-USDT-SWAP | 104.64 | 104.93/104.31 | 104.64 | sup 100.34 (ha 16 candles) | 0.81357 | 0.0068% | B/venda@105.22 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 09:05 | XRP-USDT-SWAP | 1.3028 | 1.3046/1.2974 | 1.3028 | — | 0.00948 | 0.0027% | — | sem_zona |
| 2026-10-19 09:05 | DOGE-USDT-SWAP | 0.07910 | 0.07920/0.07868 | 0.07910 | sup 0.07925 (ha 6 candles) | 0.00064 | 0.0086% | A/venda@0.07925 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-19 09:05 | ARB-USDT-SWAP | 0.19529 | 0.19633/0.19440 | 0.19529 | — | 0.00342 | 0.0086% | A/compra@0.18141 (0t/7c) | zona_mapeada_setup_A |
| 2026-10-19 09:05 | WLD-USDT-SWAP | 0.49810 | 0.50060/0.49560 | 0.49810 | sup 0.45610 (ha 15 candles) | 0.00884 | 0.0100% | B/venda@0.51160 (1t/3c) | zona_mapeada_setup_B |
| 2026-10-19 09:05 | SUI-USDT-SWAP | 0.99550 | 0.99860/0.99070 | 0.99550 | sup 0.93640 (ha 16 candles) | 0.01194 | 0.0100% | — | sem_zona |
| 2026-10-19 09:05 | UNI-USDT-SWAP | 7.3420 | 7.3810/7.3080 | 7.3420 | sup 6.8030 (ha 16 candles) | 0.09700 | 0.0062% | B/venda@7.3540 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-19 09:05 | LINK-USDT-SWAP | 12.02 | 12.07/11.98 | 12.02 | — | 0.10464 | 0.0100% | B/compra@12.06 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 10:05 | BTC-USDT-SWAP | 82568.8 | 82665.6/82300.0 | 82331.9 | sup 80621.4 (ha 16 candles) | 407.71 | 0.0100% | — | sem_zona |
| 2026-10-19 10:05 | ETH-USDT-SWAP | 2422.8 | 2428.4/2417.5 | 2418.9 | sup 2328.0 (ha 17 candles) | 15.44 | 0.0063% | — | sem_zona |
| 2026-10-19 10:05 | SOL-USDT-SWAP | 105.25 | 105.50/104.57 | 104.64 | sup 100.34 (ha 17 candles) | 0.74714 | 0.0085% | B/venda@105.22 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-19 10:05 | XRP-USDT-SWAP | 1.3101 | 1.3119/1.3016 | 1.3028 | — | 0.00822 | 0.0015% | — | sem_zona |
| 2026-10-19 10:05 | DOGE-USDT-SWAP | 0.07977 | 0.07989/0.07903 | 0.07910 | sup 0.07925 (ha 7 candles) | 0.00059 | 0.0043% | — | invalidado_setup_A |
| 2026-10-19 10:05 | ARB-USDT-SWAP | 0.19750 | 0.19988/0.19511 | 0.19529 | — | 0.00339 | 0.0047% | — | zona_expirada_setup_A |
| 2026-10-19 10:05 | WLD-USDT-SWAP | 0.50670 | 0.51480/0.49750 | 0.49810 | sup 0.45610 (ha 16 candles) | 0.00888 | 0.0100% | B/venda@0.51160 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-19 10:05 | SUI-USDT-SWAP | 1.0045 | 1.0056/0.99430 | 0.99550 | sup 0.93640 (ha 17 candles) | 0.01075 | 0.0100% | — | sem_zona |
| 2026-10-19 10:05 | UNI-USDT-SWAP | 7.3800 | 7.4190/7.3320 | 7.3420 | sup 6.8030 (ha 17 candles) | 0.08714 | 0.0086% | — | invalidado_setup_B |
| 2026-10-19 10:05 | LINK-USDT-SWAP | 12.11 | 12.13/12.01 | 12.02 | — | 0.09636 | 0.0093% | — | descartado_rr_baixo_setup_B |
| 2026-10-19 11:05 | BTC-USDT-SWAP | 82089.0 | 82733.4/82014.4 | 82331.9 | sup 80621.4 (ha 17 candles) | 421.61 | 0.0100% | — | sem_zona |
| 2026-10-19 11:05 | ETH-USDT-SWAP | 2399.4 | 2429.0/2395.0 | 2418.9 | sup 2328.0 (ha 18 candles) | 15.95 | 0.0063% | — | sem_zona |
| 2026-10-19 11:05 | SOL-USDT-SWAP | 104.25 | 105.57/104.09 | 104.64 | sup 100.34 (ha 18 candles) | 0.78571 | 0.0097% | — | descartado_rr_baixo_setup_B |
| 2026-10-19 11:05 | XRP-USDT-SWAP | 1.3011 | 1.3146/1.2994 | 1.3028 | — | 0.00834 | 0.0002% | — | sem_zona |
| 2026-10-19 11:05 | DOGE-USDT-SWAP | 0.07912 | 0.07997/0.07901 | 0.07910 | sup 0.07925 (ha 8 candles) | 0.00061 | 0.0023% | — | sem_zona |
| 2026-10-19 11:05 | ARB-USDT-SWAP | 0.19558 | 0.19910/0.19501 | 0.19529 | — | 0.00340 | 0.0046% | B/venda@0.19508 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 11:05 | WLD-USDT-SWAP | 0.50980 | 0.51620/0.50560 | 0.49810 | sup 0.49330 (ha 3 candles) | 0.00891 | 0.0100% | — | zona_expirada_setup_B |
| 2026-10-19 11:05 | SUI-USDT-SWAP | 0.99350 | 1.0082/0.99230 | 0.99550 | sup 0.93640 (ha 18 candles) | 0.01079 | 0.0100% | — | sem_zona |
| 2026-10-19 11:05 | UNI-USDT-SWAP | 7.2810 | 7.4240/7.2660 | 7.3420 | sup 6.8030 (ha 18 candles) | 0.09286 | 0.0092% | — | sem_zona |
| 2026-10-19 11:05 | LINK-USDT-SWAP | 11.98 | 12.14/11.96 | 12.02 | — | 0.10064 | 0.0085% | — | sem_zona |
| 2026-10-19 12:05 | BTC-USDT-SWAP | 82264.0 | 82544.2/81720.0 | 82331.9 | sup 80621.4 (ha 18 candles) | 441.15 | 0.0100% | — | sem_zona |
| 2026-10-19 12:05 | ETH-USDT-SWAP | 2410.4 | 2423.9/2384.0 | 2418.9 | sup 2328.0 (ha 19 candles) | 17.62 | 0.0062% | — | sem_zona |
| 2026-10-19 12:05 | SOL-USDT-SWAP | 104.66 | 105.11/103.48 | 104.64 | sup 100.34 (ha 19 candles) | 0.84071 | 0.0100% | — | sem_zona |
| 2026-10-19 12:05 | XRP-USDT-SWAP | 1.3049 | 1.3134/1.2925 | 1.3028 | — | 0.00921 | 0.0020% | — | sem_zona |
| 2026-10-19 12:05 | DOGE-USDT-SWAP | 0.07952 | 0.08006/0.07854 | 0.07910 | sup 0.07925 (ha 9 candles) | 0.00067 | -0.0002% | — | sem_zona |
| 2026-10-19 12:05 | ARB-USDT-SWAP | 0.19766 | 0.19955/0.19308 | 0.19529 | — | 0.00364 | 0.0060% | — | invalidado_setup_B |
| 2026-10-19 12:05 | WLD-USDT-SWAP | 0.50830 | 0.51160/0.49790 | 0.49810 | sup 0.49330 (ha 4 candles) | 0.00939 | 0.0100% | — | sem_zona |
| 2026-10-19 12:05 | SUI-USDT-SWAP | 0.99970 | 1.0068/0.97920 | 0.99550 | sup 0.93640 (ha 19 candles) | 0.01166 | 0.0100% | — | sem_zona |
| 2026-10-19 12:05 | UNI-USDT-SWAP | 7.3420 | 7.3970/7.1790 | 7.3420 | sup 6.8030 (ha 19 candles) | 0.10093 | 0.0076% | — | sem_zona |
| 2026-10-19 12:05 | LINK-USDT-SWAP | 12.04 | 12.12/11.86 | 12.02 | — | 0.10921 | 0.0072% | — | sem_zona |
| 2026-10-19 13:05 | BTC-USDT-SWAP | 81912.4 | 82506.8/81875.0 | 81912.4 | sup 80621.4 (ha 19 candles) | 465.63 | 0.0100% | — | sem_zona |
| 2026-10-19 13:05 | ETH-USDT-SWAP | 2393.3 | 2421.0/2392.6 | 2393.3 | sup 2328.0 (ha 20 candles) | 18.55 | 0.0074% | — | sem_zona |
| 2026-10-19 13:05 | SOL-USDT-SWAP | 104.08 | 105.25/104.05 | 104.08 | sup 100.34 (ha 20 candles) | 0.87357 | 0.0089% | — | sem_zona |
| 2026-10-19 13:05 | XRP-USDT-SWAP | 1.2979 | 1.3109/1.2964 | 1.2979 | — | 0.00964 | 0.0046% | — | sem_zona |
| 2026-10-19 13:05 | DOGE-USDT-SWAP | 0.07903 | 0.07980/0.07898 | 0.07903 | sup 0.07925 (ha 10 candles) | 0.00069 | 0.0019% | — | sem_zona |
| 2026-10-19 13:05 | ARB-USDT-SWAP | 0.19565 | 0.19940/0.19526 | 0.19565 | — | 0.00360 | 0.0066% | B/compra@0.19834 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 13:05 | WLD-USDT-SWAP | 0.50630 | 0.51530/0.50420 | 0.50630 | sup 0.49330 (ha 5 candles) | 0.00959 | 0.0100% | — | sem_zona |
| 2026-10-19 13:05 | SUI-USDT-SWAP | 0.99120 | 1.0110/0.98900 | 0.99120 | sup 0.93640 (ha 20 candles) | 0.01272 | 0.0100% | — | sem_zona |
| 2026-10-19 13:05 | UNI-USDT-SWAP | 7.2880 | 7.3820/7.2830 | 7.2880 | sup 6.8030 (ha 20 candles) | 0.09993 | 0.0071% | — | sem_zona |
| 2026-10-19 13:05 | LINK-USDT-SWAP | 11.95 | 12.10/11.94 | 11.95 | sup 12.08 (ha 10 candles) | 0.11286 | 0.0073% | A/venda@12.08 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-19 14:05 | BTC-USDT-SWAP | 81948.2 | 82051.5/81682.0 | 81912.4 | sup 80621.4 (ha 20 candles) | 458.44 | 0.0100% | — | sem_zona |
| 2026-10-19 14:05 | ETH-USDT-SWAP | 2401.5 | 2404.9/2386.5 | 2393.3 | sup 2328.0 (ha 21 candles) | 18.24 | 0.0088% | — | sem_zona |
| 2026-10-19 14:05 | SOL-USDT-SWAP | 104.37 | 104.72/103.87 | 104.08 | sup 100.34 (ha 21 candles) | 0.85571 | 0.0090% | — | sem_zona |
| 2026-10-19 14:05 | XRP-USDT-SWAP | 1.3013 | 1.3052/1.2945 | 1.2979 | — | 0.00970 | 0.0071% | — | sem_zona |
| 2026-10-19 14:05 | DOGE-USDT-SWAP | 0.07926 | 0.07949/0.07887 | 0.07903 | sup 0.07925 (ha 11 candles) | 0.00068 | 0.0069% | — | sem_zona |
| 2026-10-19 14:05 | ARB-USDT-SWAP | 0.19565 | 0.19784/0.19524 | 0.19565 | — | 0.00349 | 0.0100% | — | invalidado_setup_B |
| 2026-10-19 14:05 | WLD-USDT-SWAP | 0.50990 | 0.51580/0.50430 | 0.50630 | sup 0.49330 (ha 6 candles) | 0.00976 | 0.0100% | — | sem_zona |
| 2026-10-19 14:05 | SUI-USDT-SWAP | 0.99100 | 0.99830/0.98780 | 0.99120 | sup 0.93640 (ha 21 candles) | 0.01244 | 0.0100% | — | sem_zona |
| 2026-10-19 14:05 | UNI-USDT-SWAP | 7.3110 | 7.3560/7.2560 | 7.2880 | sup 6.8030 (ha 21 candles) | 0.09964 | 0.0053% | — | sem_zona |
| 2026-10-19 14:05 | LINK-USDT-SWAP | 11.97 | 12.02/11.91 | 11.95 | sup 12.08 (ha 11 candles) | 0.11071 | 0.0100% | A/venda@12.08 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-19 15:05 | BTC-USDT-SWAP | 81894.1 | 82033.5/81800.0 | 81912.4 | sup 80621.4 (ha 21 candles) | 456.66 | 0.0100% | — | sem_zona |
| 2026-10-19 15:05 | ETH-USDT-SWAP | 2397.2 | 2404.8/2392.4 | 2393.3 | sup 2384.0 (ha 3 candles) | 18.54 | 0.0092% | — | sem_zona |
| 2026-10-19 15:05 | SOL-USDT-SWAP | 104.01 | 104.63/103.81 | 104.08 | sup 103.48 (ha 3 candles) | 0.88429 | 0.0088% | — | sem_zona |
| 2026-10-19 15:05 | XRP-USDT-SWAP | 1.3001 | 1.3044/1.2978 | 1.2979 | — | 0.00983 | 0.0100% | — | sem_zona |
| 2026-10-19 15:05 | DOGE-USDT-SWAP | 0.07904 | 0.07943/0.07893 | 0.07903 | sup 0.07854 (ha 3 candles) | 0.00068 | 0.0100% | — | sem_zona |
| 2026-10-19 15:05 | ARB-USDT-SWAP | 0.19362 | 0.19592/0.19339 | 0.19565 | — | 0.00346 | 0.0100% | — | sem_zona |
| 2026-10-19 15:05 | WLD-USDT-SWAP | 0.51150 | 0.51420/0.50710 | 0.50630 | sup 0.49330 (ha 7 candles) | 0.00998 | 0.0100% | — | sem_zona |
| 2026-10-19 15:05 | SUI-USDT-SWAP | 0.98630 | 0.99350/0.98420 | 0.99120 | sup 0.97920 (ha 3 candles) | 0.01251 | 0.0100% | — | sem_zona |
| 2026-10-19 15:05 | UNI-USDT-SWAP | 7.2510 | 7.3320/7.2460 | 7.2880 | sup 7.1790 (ha 3 candles) | 0.10179 | 0.0061% | — | sem_zona |
| 2026-10-19 15:05 | LINK-USDT-SWAP | 11.90 | 12.00/11.88 | 11.95 | sup 11.86 (ha 3 candles) | 0.11564 | 0.0100% | A/venda@12.08 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-19 16:05 | BTC-USDT-SWAP | 81928.8 | 82121.9/81759.3 | 81912.4 | sup 80621.4 (ha 22 candles) | 453.43 | 0.0099% | — | sem_zona |
| 2026-10-19 16:05 | ETH-USDT-SWAP | 2400.2 | 2407.6/2389.1 | 2393.3 | sup 2384.0 (ha 4 candles) | 18.90 | 0.0090% | — | sem_zona |
| 2026-10-19 16:05 | SOL-USDT-SWAP | 103.94 | 104.44/103.60 | 104.08 | sup 103.48 (ha 4 candles) | 0.87929 | 0.0088% | — | sem_zona |
| 2026-10-19 16:05 | XRP-USDT-SWAP | 1.3028 | 1.3054/1.2957 | 1.2979 | — | 0.01000 | 0.0100% | B/compra@1.3102 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 16:05 | DOGE-USDT-SWAP | 0.07925 | 0.07935/0.07870 | 0.07903 | sup 0.07854 (ha 4 candles) | 0.00068 | 0.0100% | — | sem_zona |
| 2026-10-19 16:05 | ARB-USDT-SWAP | 0.19391 | 0.19514/0.19267 | 0.19565 | — | 0.00344 | 0.0100% | — | sem_zona |
| 2026-10-19 16:05 | WLD-USDT-SWAP | 0.50710 | 0.51810/0.50120 | 0.50630 | sup 0.49330 (ha 8 candles) | 0.01066 | 0.0100% | — | sem_zona |
| 2026-10-19 16:05 | SUI-USDT-SWAP | 0.98770 | 0.99150/0.98020 | 0.99120 | sup 0.97920 (ha 4 candles) | 0.01229 | 0.0100% | — | sem_zona |
| 2026-10-19 16:05 | UNI-USDT-SWAP | 7.2400 | 7.2850/7.2020 | 7.2880 | sup 7.1790 (ha 4 candles) | 0.09750 | 0.0086% | — | sem_zona |
| 2026-10-19 16:05 | LINK-USDT-SWAP | 11.90 | 11.95/11.83 | 11.95 | sup 11.86 (ha 4 candles) | 0.11843 | 0.0100% | A/venda@12.08 (0t/3c) | zona_mapeada_setup_A |
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
