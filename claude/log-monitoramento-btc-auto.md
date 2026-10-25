# Log de Monitoramento Automatico -- Multi-Par (script gratuito, GitHub Actions)

> Gerado por script Python sem LLM (ver monitor/fetch_and_check.py). Fonte: OKX. Cobre os pares em PAIRS (configuracao no topo do script) -- BTC-USDT-SWAP e os demais adicionados na expansao de 07/09/2026. Leitura e MECANICA (regras objetivas da secao 4 do plano), sem a prosa qualitativa que o Claude gerava -- cole este log numa conversa do Claude se quiser a leitura interpretativa.

| Data/Hora (BRT) | Par | Close 1h | High/Low 1h | Close 4h | Swing 1h ref | ATR 1h | Funding | Zona ativa | Status checklist |
|---|---|---|---|---|---|---|---|---|---|
| 2026-10-23 14:06 | BTC-USDT-SWAP | 81684.1 | 81819.9/81455.4 | 81651.1 | — | 379.72 | 0.0076% | — | sem_zona |
| 2026-10-23 14:06 | ETH-USDT-SWAP | 2405.9 | 2413.0/2397.5 | 2406.5 | — | 15.93 | 0.0058% | — | sem_zona |
| 2026-10-23 14:06 | SOL-USDT-SWAP | 104.61 | 104.97/104.27 | 104.73 | — | 0.72571 | 0.0066% | B/venda@104.76 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-23 14:06 | XRP-USDT-SWAP | 1.3095 | 1.3159/1.3064 | 1.3126 | res 1.3300 (ha 9 candles) | 0.00925 | 0.0100% | B/compra@1.3102 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-23 14:06 | DOGE-USDT-SWAP | 0.07990 | 0.08033/0.07982 | 0.08015 | — | 0.00063 | 0.0067% | B/compra@0.07996 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-23 14:06 | ARB-USDT-SWAP | 0.17927 | 0.18032/0.17792 | 0.17988 | sup 0.17743 (ha 17 candles) | 0.00258 | -0.0003% | — | sem_zona |
| 2026-10-23 14:06 | WLD-USDT-SWAP | 0.53060 | 0.53430/0.52670 | 0.53200 | — | 0.00936 | 0.0090% | B/venda@0.53940 (2t/2c) | zona_mapeada_setup_B |
| 2026-10-23 14:06 | SUI-USDT-SWAP | 0.98940 | 0.99490/0.98570 | 0.99200 | — | 0.01018 | 0.0033% | — | invalidado_setup_B |
| 2026-10-23 14:06 | UNI-USDT-SWAP | 7.1450 | 7.1990/7.1040 | 7.1420 | sup 6.9690 (ha 17 candles) | 0.09186 | 0.0041% | — | sem_zona |
| 2026-10-23 14:06 | LINK-USDT-SWAP | 12.03 | 12.09/11.99 | 12.05 | sup 11.77 (ha 24 candles) | 0.10014 | 0.0100% | B/compra@12.15 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-23 15:06 | BTC-USDT-SWAP | 81616.1 | 81815.3/81541.0 | 81651.1 | — | 374.71 | 0.0093% | — | sem_zona |
| 2026-10-23 15:06 | ETH-USDT-SWAP | 2408.3 | 2412.9/2403.8 | 2406.5 | — | 15.82 | 0.0049% | — | sem_zona |
| 2026-10-23 15:06 | SOL-USDT-SWAP | 104.48 | 104.76/104.31 | 104.73 | — | 0.71357 | 0.0075% | — | descartado_rr_baixo_setup_B |
| 2026-10-23 15:06 | XRP-USDT-SWAP | 1.3104 | 1.3132/1.3077 | 1.3126 | res 1.3238 (ha 3 candles) | 0.00912 | 0.0100% | B/compra@1.3102 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-23 15:06 | DOGE-USDT-SWAP | 0.07988 | 0.08005/0.07974 | 0.08015 | — | 0.00062 | 0.0087% | B/compra@0.07996 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-23 15:06 | ARB-USDT-SWAP | 0.18072 | 0.18106/0.17881 | 0.17988 | sup 0.17568 (ha 3 candles) | 0.00246 | -0.0013% | — | sem_zona |
| 2026-10-23 15:06 | WLD-USDT-SWAP | 0.53280 | 0.53340/0.52840 | 0.53200 | — | 0.00911 | 0.0068% | B/venda@0.53940 (2t/3c) | zona_mapeada_setup_B |
| 2026-10-23 15:06 | SUI-USDT-SWAP | 0.99050 | 0.99240/0.98660 | 0.99200 | — | 0.01006 | 0.0031% | B/compra@0.99710 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-23 15:06 | UNI-USDT-SWAP | 7.1660 | 7.1780/7.1260 | 7.1420 | sup 6.9910 (ha 3 candles) | 0.08779 | 0.0048% | — | sem_zona |
| 2026-10-23 15:06 | LINK-USDT-SWAP | 12.04 | 12.07/12.02 | 12.05 | sup 11.85 (ha 3 candles) | 0.09914 | 0.0100% | B/compra@12.15 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-23 15:28 | BTC-USDT-SWAP | 81616.1 | 81815.3/81541.0 | 81651.1 | — | 374.71 | 0.0100% | — | sem_zona |
| 2026-10-23 15:28 | ETH-USDT-SWAP | 2408.3 | 2412.9/2403.8 | 2406.5 | — | 15.82 | 0.0042% | — | sem_zona |
| 2026-10-23 15:28 | SOL-USDT-SWAP | 104.48 | 104.76/104.31 | 104.73 | — | 0.71357 | 0.0078% | — | descartado_rr_baixo_setup_B |
| 2026-10-23 15:28 | XRP-USDT-SWAP | 1.3104 | 1.3132/1.3077 | 1.3126 | res 1.3238 (ha 3 candles) | 0.00912 | 0.0100% | B/compra@1.3102 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-23 15:28 | DOGE-USDT-SWAP | 0.07988 | 0.08005/0.07974 | 0.08015 | — | 0.00062 | 0.0094% | B/compra@0.07996 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-23 15:28 | ARB-USDT-SWAP | 0.18072 | 0.18106/0.17881 | 0.17988 | sup 0.17568 (ha 3 candles) | 0.00246 | 0.0001% | — | sem_zona |
| 2026-10-23 15:28 | WLD-USDT-SWAP | 0.53280 | 0.53340/0.52840 | 0.53200 | — | 0.00911 | 0.0062% | B/venda@0.53940 (2t/3c) | zona_mapeada_setup_B |
| 2026-10-23 15:28 | SUI-USDT-SWAP | 0.99050 | 0.99240/0.98660 | 0.99200 | — | 0.01006 | 0.0041% | B/compra@0.99710 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-23 15:28 | UNI-USDT-SWAP | 7.1660 | 7.1780/7.1260 | 7.1420 | sup 6.9910 (ha 3 candles) | 0.08779 | 0.0059% | — | sem_zona |
| 2026-10-23 15:28 | LINK-USDT-SWAP | 12.04 | 12.07/12.02 | 12.05 | sup 11.85 (ha 3 candles) | 0.09914 | 0.0100% | B/compra@12.15 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-23 16:06 | BTC-USDT-SWAP | 81413.3 | 81637.5/81385.1 | 81651.1 | — | 367.28 | 0.0100% | B/compra@81166.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-23 16:06 | ETH-USDT-SWAP | 2401.1 | 2409.0/2398.5 | 2406.5 | — | 15.19 | 0.0033% | B/compra@2391.7 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-23 16:06 | SOL-USDT-SWAP | 104.03 | 104.47/103.98 | 104.73 | — | 0.71571 | 0.0086% | — | sem_zona |
| 2026-10-23 16:06 | XRP-USDT-SWAP | 1.3088 | 1.3130/1.3073 | 1.3126 | res 1.3238 (ha 4 candles) | 0.00916 | 0.0100% | — | zona_expirada_setup_B |
| 2026-10-23 16:06 | DOGE-USDT-SWAP | 0.07948 | 0.07987/0.07937 | 0.08015 | — | 0.00064 | 0.0100% | — | invalidado_setup_B |
| 2026-10-23 16:06 | ARB-USDT-SWAP | 0.17977 | 0.18222/0.17942 | 0.17988 | sup 0.17568 (ha 4 candles) | 0.00246 | 0.0005% | — | sem_zona |
| 2026-10-23 16:06 | WLD-USDT-SWAP | 0.52830 | 0.53510/0.52780 | 0.53200 | — | 0.00881 | 0.0037% | B/venda@0.53940 (2t/4c) | zona_mapeada_setup_B |
| 2026-10-23 16:06 | SUI-USDT-SWAP | 0.98250 | 0.99150/0.98230 | 0.99200 | — | 0.01027 | 0.0058% | B/compra@0.99710 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-23 16:06 | UNI-USDT-SWAP | 7.1180 | 7.1890/7.1150 | 7.1420 | sup 6.9910 (ha 4 candles) | 0.08871 | 0.0082% | — | sem_zona |
| 2026-10-23 16:06 | LINK-USDT-SWAP | 11.98 | 12.05/11.97 | 12.05 | sup 11.85 (ha 4 candles) | 0.09964 | 0.0100% | B/compra@12.15 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-23 17:06 | BTC-USDT-SWAP | 81260.5 | 81444.8/81222.2 | 81260.5 | — | 361.84 | 0.0100% | B/compra@81166.0 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-23 17:06 | ETH-USDT-SWAP | 2393.5 | 2401.6/2392.2 | 2393.5 | — | 14.92 | 0.0030% | B/compra@2391.7 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-23 17:06 | SOL-USDT-SWAP | 103.52 | 104.16/103.47 | 103.52 | — | 0.72214 | 0.0081% | — | sem_zona |
| 2026-10-23 17:06 | XRP-USDT-SWAP | 1.3028 | 1.3091/1.2992 | 1.3028 | — | 0.00912 | 0.0100% | — | sem_zona |
| 2026-10-23 17:06 | DOGE-USDT-SWAP | 0.07910 | 0.07953/0.07891 | 0.07910 | — | 0.00063 | 0.0100% | B/compra@0.07929 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-23 17:06 | ARB-USDT-SWAP | 0.17749 | 0.17987/0.17721 | 0.17749 | sup 0.17568 (ha 5 candles) | 0.00252 | -0.0017% | — | sem_zona |
| 2026-10-23 17:06 | WLD-USDT-SWAP | 0.51900 | 0.52850/0.51600 | 0.51900 | — | 0.00906 | 0.0034% | B/venda@0.53940 (2t/5c) | zona_mapeada_setup_B |
| 2026-10-23 17:06 | SUI-USDT-SWAP | 0.97320 | 0.98300/0.97080 | 0.97320 | sup 0.97440 (ha 5 candles) | 0.01037 | 0.0061% | B/compra@0.99710 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-23 17:06 | UNI-USDT-SWAP | 7.0590 | 7.1230/7.0480 | 7.0590 | sup 6.9910 (ha 5 candles) | 0.08736 | 0.0067% | — | sem_zona |
| 2026-10-23 17:06 | LINK-USDT-SWAP | 11.91 | 11.98/11.89 | 11.91 | sup 11.85 (ha 5 candles) | 0.10014 | 0.0100% | — | zona_expirada_setup_B |
| 2026-10-23 18:06 | BTC-USDT-SWAP | 81377.8 | 81471.8/81240.1 | 81260.5 | — | 361.59 | 0.0100% | B/compra@81166.0 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-23 18:06 | ETH-USDT-SWAP | 2400.5 | 2403.6/2392.1 | 2393.5 | — | 14.86 | 0.0027% | — | descartado_rr_baixo_setup_B |
| 2026-10-23 18:06 | SOL-USDT-SWAP | 103.87 | 104.04/103.35 | 103.52 | — | 0.73571 | 0.0072% | B/compra@103.48 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-23 18:06 | XRP-USDT-SWAP | 1.3077 | 1.3105/1.3016 | 1.3028 | — | 0.00919 | 0.0100% | — | sem_zona |
| 2026-10-23 18:06 | DOGE-USDT-SWAP | 0.07924 | 0.07938/0.07896 | 0.07910 | — | 0.00063 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-10-23 18:06 | ARB-USDT-SWAP | 0.17815 | 0.17896/0.17626 | 0.17749 | sup 0.17568 (ha 6 candles) | 0.00260 | -0.0006% | — | sem_zona |
| 2026-10-23 18:06 | WLD-USDT-SWAP | 0.51380 | 0.51930/0.51360 | 0.51900 | — | 0.00881 | 0.0053% | B/venda@0.53940 (2t/6c) | zona_mapeada_setup_B |
| 2026-10-23 18:06 | SUI-USDT-SWAP | 0.97810 | 0.98030/0.97170 | 0.97320 | sup 0.97440 (ha 6 candles) | 0.01031 | 0.0055% | B/compra@0.99710 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-23 18:06 | UNI-USDT-SWAP | 7.1140 | 7.1200/7.0340 | 7.0590 | sup 6.9910 (ha 6 candles) | 0.08629 | 0.0057% | — | sem_zona |
| 2026-10-23 18:06 | LINK-USDT-SWAP | 11.93 | 11.97/11.88 | 11.91 | sup 11.85 (ha 6 candles) | 0.10014 | 0.0055% | — | sem_zona |
| 2026-10-23 19:06 | BTC-USDT-SWAP | 81342.2 | 81470.0/81293.9 | 81260.5 | — | 348.37 | 0.0100% | B/compra@81166.0 (2t/1c) | zona_mapeada_setup_B |
| 2026-10-23 19:06 | ETH-USDT-SWAP | 2398.8 | 2404.8/2395.6 | 2393.5 | — | 14.75 | 0.0037% | B/compra@2407.5 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-23 19:06 | SOL-USDT-SWAP | 103.60 | 104.07/103.47 | 103.52 | — | 0.74071 | 0.0080% | B/compra@103.48 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-23 19:06 | XRP-USDT-SWAP | 1.3057 | 1.3097/1.3040 | 1.3028 | — | 0.00897 | 0.0100% | — | sem_zona |
| 2026-10-23 19:06 | DOGE-USDT-SWAP | 0.07929 | 0.07953/0.07909 | 0.07910 | — | 0.00063 | 0.0100% | — | sem_zona |
| 2026-10-23 19:06 | ARB-USDT-SWAP | 0.17783 | 0.17901/0.17726 | 0.17749 | sup 0.17568 (ha 7 candles) | 0.00262 | 0.0031% | — | sem_zona |
| 2026-10-23 19:06 | WLD-USDT-SWAP | 0.50840 | 0.51570/0.50760 | 0.51900 | — | 0.00861 | 0.0045% | B/venda@0.53940 (2t/7c) | zona_mapeada_setup_B |
| 2026-10-23 19:06 | SUI-USDT-SWAP | 0.97370 | 0.98060/0.97270 | 0.97320 | sup 0.97440 (ha 7 candles) | 0.01034 | 0.0053% | B/compra@0.99710 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-23 19:06 | UNI-USDT-SWAP | 7.0680 | 7.1350/7.0580 | 7.0590 | sup 6.9910 (ha 7 candles) | 0.08643 | 0.0070% | — | sem_zona |
| 2026-10-23 19:06 | LINK-USDT-SWAP | 11.90 | 11.96/11.88 | 11.91 | sup 11.85 (ha 7 candles) | 0.10014 | 0.0034% | — | sem_zona |
| 2026-10-23 20:06 | BTC-USDT-SWAP | 80790.5 | 81412.6/80520.0 | 81260.5 | — | 385.53 | 0.0100% | — | invalidado_setup_B |
| 2026-10-23 20:06 | ETH-USDT-SWAP | 2366.0 | 2402.2/2350.1 | 2393.5 | — | 17.46 | 0.0029% | B/compra@2407.5 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-23 20:06 | SOL-USDT-SWAP | 102.27 | 103.81/101.64 | 103.52 | — | 0.85071 | 0.0053% | — | invalidado_setup_B |
| 2026-10-23 20:06 | XRP-USDT-SWAP | 1.2890 | 1.3088/1.2807 | 1.3028 | — | 0.01044 | 0.0082% | B/compra@1.2856 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-23 20:06 | DOGE-USDT-SWAP | 0.07792 | 0.07944/0.07734 | 0.07910 | — | 0.00073 | 0.0065% | B/compra@0.07842 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-23 20:06 | ARB-USDT-SWAP | 0.17133 | 0.17882/0.16979 | 0.17749 | sup 0.17568 (ha 8 candles) | 0.00317 | 0.0018% | A/venda@0.17568 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-23 20:06 | WLD-USDT-SWAP | 0.47670 | 0.51220/0.47260 | 0.51900 | — | 0.01095 | 0.0032% | — | zona_expirada_setup_B |
| 2026-10-23 20:06 | SUI-USDT-SWAP | 0.94870 | 0.97740/0.93870 | 0.97320 | sup 0.97440 (ha 8 candles) | 0.01252 | 0.0020% | B/compra@0.99710 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-23 20:06 | UNI-USDT-SWAP | 6.8540 | 7.1080/6.7930 | 7.0590 | sup 6.9910 (ha 8 candles) | 0.10557 | 0.0026% | A/venda@6.9910 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-23 20:06 | LINK-USDT-SWAP | 11.68 | 11.95/11.59 | 11.91 | sup 11.85 (ha 8 candles) | 0.12143 | -0.0024% | A/venda@11.85 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-23 21:06 | BTC-USDT-SWAP | 81149.9 | 81160.0/80456.6 | 81149.9 | — | 415.29 | 0.0100% | B/compra@80961.3 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-23 21:06 | ETH-USDT-SWAP | 2386.5 | 2387.6/2356.2 | 2386.5 | — | 18.49 | 0.0019% | B/compra@2407.5 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-23 21:06 | SOL-USDT-SWAP | 102.80 | 102.92/101.75 | 102.80 | — | 0.87714 | 0.0038% | B/compra@102.38 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-23 21:06 | XRP-USDT-SWAP | 1.2945 | 1.2958/1.2820 | 1.2945 | — | 0.01071 | 0.0052% | — | descartado_rr_baixo_setup_B |
| 2026-10-23 21:06 | DOGE-USDT-SWAP | 0.07858 | 0.07867/0.07739 | 0.07858 | sup 0.07889 (ha 9 candles) | 0.00077 | 0.0023% | — | invalidado_tendencia_virou_setup_B |
| 2026-10-23 21:06 | ARB-USDT-SWAP | 0.17170 | 0.17307/0.16980 | 0.17170 | sup 0.17568 (ha 9 candles) | 0.00320 | 0.0030% | A/venda@0.17568 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-23 21:06 | WLD-USDT-SWAP | 0.48200 | 0.48430/0.47540 | 0.48200 | — | 0.01049 | -0.0026% | B/compra@0.47770 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-23 21:06 | SUI-USDT-SWAP | 0.95990 | 0.96130/0.94200 | 0.95990 | sup 0.97440 (ha 9 candles) | 0.01314 | -0.0028% | B/compra@0.99710 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-23 21:06 | UNI-USDT-SWAP | 6.9640 | 6.9670/6.8120 | 6.9640 | sup 6.9910 (ha 9 candles) | 0.10964 | 0.0018% | A/venda@6.9910 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-23 21:06 | LINK-USDT-SWAP | 11.82 | 11.83/11.63 | 11.82 | sup 11.85 (ha 9 candles) | 0.12507 | -0.0041% | A/venda@11.85 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-23 22:06 | BTC-USDT-SWAP | 80571.3 | 81175.7/80559.8 | 81149.9 | — | 442.15 | 0.0076% | — | invalidado_setup_B |
| 2026-10-23 22:06 | ETH-USDT-SWAP | 2373.2 | 2387.7/2368.4 | 2386.5 | — | 19.05 | 0.0018% | B/compra@2407.5 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-23 22:06 | SOL-USDT-SWAP | 102.23 | 102.83/101.93 | 102.80 | — | 0.90857 | 0.0046% | B/compra@102.38 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-23 22:06 | XRP-USDT-SWAP | 1.2861 | 1.2948/1.2823 | 1.2945 | — | 0.01111 | 0.0022% | B/compra@1.2886 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-23 22:06 | DOGE-USDT-SWAP | 0.07834 | 0.07865/0.07805 | 0.07858 | sup 0.07889 (ha 10 candles) | 0.00077 | 0.0001% | A/venda@0.07889 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-23 22:06 | ARB-USDT-SWAP | 0.16896 | 0.17172/0.16712 | 0.17170 | sup 0.17568 (ha 10 candles) | 0.00339 | 0.0054% | A/venda@0.17568 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-23 22:06 | WLD-USDT-SWAP | 0.47360 | 0.48190/0.47060 | 0.48200 | — | 0.01090 | -0.0038% | — | invalidado_setup_B |
| 2026-10-23 22:06 | SUI-USDT-SWAP | 0.95310 | 0.96250/0.94940 | 0.95990 | sup 0.97440 (ha 10 candles) | 0.01353 | -0.0056% | B/compra@0.99710 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-23 22:06 | UNI-USDT-SWAP | 6.8880 | 6.9760/6.8590 | 6.9640 | sup 6.9910 (ha 10 candles) | 0.11336 | 0.0039% | — | descartado_rr_baixo_setup_A |
| 2026-10-23 22:06 | LINK-USDT-SWAP | 11.74 | 11.84/11.71 | 11.82 | sup 11.85 (ha 10 candles) | 0.12907 | -0.0030% | — | descartado_rr_baixo_setup_A |
| 2026-10-23 23:06 | BTC-USDT-SWAP | 80884.2 | 80927.1/80571.2 | 81149.9 | — | 452.27 | 0.0052% | B/compra@81166.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-23 23:06 | ETH-USDT-SWAP | 2381.0 | 2382.7/2371.2 | 2386.5 | — | 18.82 | 0.0033% | B/compra@2407.5 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-23 23:06 | SOL-USDT-SWAP | 102.55 | 102.68/102.13 | 102.80 | — | 0.88500 | 0.0075% | — | confirmado_calibracao_setup_B |
| 2026-10-23 23:06 | XRP-USDT-SWAP | 1.2908 | 1.2927/1.2854 | 1.2945 | — | 0.01104 | 0.0010% | — | descartado_rr_baixo_setup_B |
| 2026-10-23 23:06 | DOGE-USDT-SWAP | 0.07878 | 0.07884/0.07834 | 0.07858 | sup 0.07734 (ha 3 candles) | 0.00074 | 0.0006% | A/venda@0.07889 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-23 23:06 | ARB-USDT-SWAP | 0.17056 | 0.17090/0.16838 | 0.17170 | sup 0.17568 (ha 11 candles) | 0.00343 | 0.0040% | A/venda@0.17568 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-23 23:06 | WLD-USDT-SWAP | 0.47600 | 0.47820/0.47260 | 0.48200 | — | 0.01065 | -0.0019% | B/compra@0.47260 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-23 23:06 | SUI-USDT-SWAP | 0.96180 | 0.96310/0.95320 | 0.95990 | sup 0.93870 (ha 3 candles) | 0.01337 | -0.0059% | — | zona_expirada_setup_B |
| 2026-10-23 23:06 | UNI-USDT-SWAP | 6.9710 | 6.9780/6.8870 | 6.9640 | sup 6.7930 (ha 3 candles) | 0.11357 | 0.0056% | — | sem_zona |
| 2026-10-23 23:06 | LINK-USDT-SWAP | 11.83 | 11.84/11.74 | 11.82 | sup 11.59 (ha 3 candles) | 0.12871 | -0.0029% | — | sem_zona |
| 2026-10-24 00:06 | BTC-USDT-SWAP | 80959.9 | 80962.0/80801.0 | 81149.9 | — | 436.62 | 0.0038% | B/compra@81166.0 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-24 00:06 | ETH-USDT-SWAP | 2383.9 | 2384.2/2377.8 | 2386.5 | — | 18.48 | 0.0059% | B/compra@2407.5 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-24 00:06 | SOL-USDT-SWAP | 102.72 | 102.73/102.39 | 102.80 | — | 0.86786 | 0.0100% | — | sem_zona |
| 2026-10-24 00:06 | XRP-USDT-SWAP | 1.2927 | 1.2934/1.2896 | 1.2945 | — | 0.01086 | 0.0012% | B/compra@1.2856 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-24 00:06 | DOGE-USDT-SWAP | 0.07891 | 0.07902/0.07874 | 0.07858 | sup 0.07734 (ha 4 candles) | 0.00073 | 0.0016% | A/venda@0.07889 (2t/0c) | zona_mapeada_setup_A |
| 2026-10-24 00:06 | ARB-USDT-SWAP | 0.17198 | 0.17222/0.17014 | 0.17170 | sup 0.17568 (ha 12 candles) | 0.00343 | 0.0030% | A/venda@0.17568 (0t/4c) | zona_mapeada_setup_A |
| 2026-10-24 00:06 | WLD-USDT-SWAP | 0.48170 | 0.48240/0.47510 | 0.48200 | — | 0.01067 | -0.0026% | — | confirmado_calibracao_setup_B |
| 2026-10-24 00:06 | SUI-USDT-SWAP | 0.96410 | 0.96470/0.95990 | 0.95990 | sup 0.93870 (ha 4 candles) | 0.01314 | -0.0046% | — | sem_zona |
| 2026-10-24 00:06 | UNI-USDT-SWAP | 6.9960 | 7.0180/6.9660 | 6.9640 | sup 6.7930 (ha 4 candles) | 0.11314 | 0.0072% | — | sem_zona |
| 2026-10-24 00:06 | LINK-USDT-SWAP | 11.87 | 11.87/11.82 | 11.82 | sup 11.59 (ha 4 candles) | 0.12686 | -0.0003% | — | sem_zona |
| 2026-10-24 01:06 | BTC-USDT-SWAP | 80930.6 | 81060.0/80814.9 | 80930.6 | sup 80456.6 (ha 4 candles) | 420.73 | 0.0025% | — | invalidado_setup_B |
| 2026-10-24 01:06 | ETH-USDT-SWAP | 2381.6 | 2389.7/2378.5 | 2381.6 | sup 2350.1 (ha 5 candles) | 17.79 | 0.0067% | B/compra@2407.5 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-24 01:06 | SOL-USDT-SWAP | 102.61 | 103.09/102.45 | 102.61 | sup 101.64 (ha 5 candles) | 0.83929 | 0.0100% | — | sem_zona |
| 2026-10-24 01:06 | XRP-USDT-SWAP | 1.2906 | 1.2957/1.2881 | 1.2906 | — | 0.01075 | 0.0024% | B/compra@1.2856 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-24 01:06 | DOGE-USDT-SWAP | 0.07878 | 0.07906/0.07856 | 0.07878 | sup 0.07734 (ha 5 candles) | 0.00072 | 0.0015% | — | zona_expirada_setup_A |
| 2026-10-24 01:06 | ARB-USDT-SWAP | 0.17172 | 0.17288/0.17085 | 0.17172 | sup 0.16712 (ha 3 candles) | 0.00332 | 0.0013% | A/venda@0.17568 (0t/5c) | zona_mapeada_setup_A |
| 2026-10-24 01:06 | WLD-USDT-SWAP | 0.47960 | 0.48420/0.47800 | 0.47960 | — | 0.01059 | -0.0027% | B/compra@0.47770 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-24 01:06 | SUI-USDT-SWAP | 0.96230 | 0.96870/0.95980 | 0.96230 | sup 0.93870 (ha 5 candles) | 0.01302 | -0.0035% | — | sem_zona |
| 2026-10-24 01:06 | UNI-USDT-SWAP | 6.9650 | 7.0290/6.9430 | 6.9650 | sup 6.7930 (ha 5 candles) | 0.11129 | 0.0087% | — | sem_zona |
| 2026-10-24 01:06 | LINK-USDT-SWAP | 11.86 | 11.91/11.83 | 11.86 | sup 11.59 (ha 5 candles) | 0.12429 | 0.0037% | — | sem_zona |
| 2026-10-24 02:06 | BTC-USDT-SWAP | 80854.0 | 81061.4/80802.0 | 80930.6 | sup 80456.6 (ha 5 candles) | 369.97 | 0.0027% | — | sem_zona |
| 2026-10-24 02:06 | ETH-USDT-SWAP | 2381.9 | 2385.3/2378.9 | 2381.6 | sup 2350.1 (ha 6 candles) | 15.41 | 0.0083% | B/compra@2407.5 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-24 02:06 | SOL-USDT-SWAP | 102.65 | 102.83/102.49 | 102.61 | sup 101.64 (ha 6 candles) | 0.73643 | 0.0100% | — | sem_zona |
| 2026-10-24 02:06 | XRP-USDT-SWAP | 1.2918 | 1.2939/1.2896 | 1.2906 | — | 0.00946 | 0.0043% | B/compra@1.2856 (1t/1c) | zona_mapeada_setup_B |
| 2026-10-24 02:06 | DOGE-USDT-SWAP | 0.07875 | 0.07899/0.07870 | 0.07878 | sup 0.07734 (ha 6 candles) | 0.00063 | 0.0035% | — | sem_zona |
| 2026-10-24 02:06 | ARB-USDT-SWAP | 0.17148 | 0.17240/0.17091 | 0.17172 | sup 0.16712 (ha 4 candles) | 0.00298 | -0.0001% | A/venda@0.17568 (0t/6c) | zona_mapeada_setup_A |
| 2026-10-24 02:06 | WLD-USDT-SWAP | 0.48050 | 0.48290/0.47820 | 0.47960 | — | 0.00972 | -0.0003% | B/compra@0.47770 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-24 02:06 | SUI-USDT-SWAP | 0.96230 | 0.96610/0.96040 | 0.96230 | sup 0.93870 (ha 6 candles) | 0.01158 | 0.0018% | — | sem_zona |
| 2026-10-24 02:06 | UNI-USDT-SWAP | 6.9850 | 7.0230/6.9570 | 6.9650 | sup 6.7930 (ha 6 candles) | 0.10150 | 0.0097% | — | sem_zona |
| 2026-10-24 02:06 | LINK-USDT-SWAP | 11.86 | 11.88/11.82 | 11.86 | sup 11.59 (ha 6 candles) | 0.11064 | 0.0074% | — | sem_zona |
| 2026-10-24 03:06 | BTC-USDT-SWAP | 80734.0 | 80854.0/80672.7 | 80930.6 | sup 80456.6 (ha 6 candles) | 352.59 | 0.0032% | — | sem_zona |
| 2026-10-24 03:06 | ETH-USDT-SWAP | 2377.2 | 2381.9/2374.5 | 2381.6 | sup 2350.1 (ha 7 candles) | 15.07 | 0.0095% | — | zona_expirada_setup_B |
| 2026-10-24 03:06 | SOL-USDT-SWAP | 102.30 | 102.66/102.16 | 102.61 | sup 101.64 (ha 7 candles) | 0.73143 | 0.0100% | — | sem_zona |
| 2026-10-24 03:06 | XRP-USDT-SWAP | 1.2877 | 1.2920/1.2868 | 1.2906 | — | 0.00913 | 0.0049% | B/compra@1.2856 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-24 03:06 | DOGE-USDT-SWAP | 0.07837 | 0.07875/0.07828 | 0.07878 | sup 0.07734 (ha 7 candles) | 0.00063 | 0.0050% | — | sem_zona |
| 2026-10-24 03:06 | ARB-USDT-SWAP | 0.17087 | 0.17158/0.17033 | 0.17172 | sup 0.16712 (ha 5 candles) | 0.00292 | 0.0011% | A/venda@0.17568 (0t/7c) | zona_mapeada_setup_A |
| 2026-10-24 03:06 | WLD-USDT-SWAP | 0.47730 | 0.48120/0.47480 | 0.47960 | — | 0.00974 | 0.0042% | B/compra@0.47770 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-24 03:06 | SUI-USDT-SWAP | 0.95880 | 0.96240/0.95580 | 0.96230 | sup 0.93870 (ha 7 candles) | 0.01143 | 0.0051% | — | sem_zona |
| 2026-10-24 03:06 | UNI-USDT-SWAP | 6.9320 | 6.9880/6.9170 | 6.9650 | sup 6.7930 (ha 7 candles) | 0.10086 | 0.0100% | — | sem_zona |
| 2026-10-24 03:06 | LINK-USDT-SWAP | 11.80 | 11.86/11.79 | 11.86 | sup 11.59 (ha 7 candles) | 0.11014 | 0.0098% | — | sem_zona |
| 2026-10-24 04:06 | BTC-USDT-SWAP | 80748.2 | 80797.4/80650.5 | 80930.6 | sup 80456.6 (ha 7 candles) | 337.04 | 0.0039% | — | sem_zona |
| 2026-10-24 04:06 | ETH-USDT-SWAP | 2377.8 | 2379.8/2373.4 | 2381.6 | sup 2350.1 (ha 8 candles) | 14.42 | 0.0099% | — | sem_zona |
| 2026-10-24 04:06 | SOL-USDT-SWAP | 102.12 | 102.38/101.98 | 102.61 | sup 101.64 (ha 8 candles) | 0.71000 | 0.0100% | — | sem_zona |
| 2026-10-24 04:06 | XRP-USDT-SWAP | 1.2886 | 1.2894/1.2859 | 1.2906 | — | 0.00870 | 0.0048% | — | descartado_rr_baixo_setup_B |
| 2026-10-24 04:06 | DOGE-USDT-SWAP | 0.07823 | 0.07840/0.07816 | 0.07878 | sup 0.07734 (ha 8 candles) | 0.00061 | 0.0063% | — | sem_zona |
| 2026-10-24 04:06 | ARB-USDT-SWAP | 0.17026 | 0.17096/0.16966 | 0.17172 | sup 0.16712 (ha 6 candles) | 0.00284 | 0.0028% | — | zona_expirada_setup_A |
| 2026-10-24 04:06 | WLD-USDT-SWAP | 0.47430 | 0.47780/0.47410 | 0.47960 | — | 0.00946 | 0.0073% | — | invalidado_setup_B |
| 2026-10-24 04:06 | SUI-USDT-SWAP | 0.95700 | 0.95980/0.95480 | 0.96230 | sup 0.93870 (ha 8 candles) | 0.01113 | 0.0091% | — | sem_zona |
| 2026-10-24 04:06 | UNI-USDT-SWAP | 6.9100 | 6.9390/6.8970 | 6.9650 | sup 6.7930 (ha 8 candles) | 0.09707 | 0.0095% | — | sem_zona |
| 2026-10-24 04:06 | LINK-USDT-SWAP | 11.79 | 11.82/11.78 | 11.86 | sup 11.59 (ha 8 candles) | 0.10586 | 0.0100% | — | sem_zona |
| 2026-10-24 05:06 | BTC-USDT-SWAP | 80699.9 | 80888.5/80666.9 | 80699.9 | sup 80456.6 (ha 8 candles) | 333.28 | 0.0052% | — | sem_zona |
| 2026-10-24 05:06 | ETH-USDT-SWAP | 2373.9 | 2383.3/2372.2 | 2373.9 | sup 2350.1 (ha 9 candles) | 14.56 | 0.0091% | — | sem_zona |
| 2026-10-24 05:06 | SOL-USDT-SWAP | 101.87 | 102.40/101.76 | 101.87 | sup 101.64 (ha 9 candles) | 0.72357 | 0.0100% | — | sem_zona |
| 2026-10-24 05:06 | XRP-USDT-SWAP | 1.2845 | 1.2917/1.2832 | 1.2845 | — | 0.00891 | 0.0028% | B/compra@1.2886 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-24 05:06 | DOGE-USDT-SWAP | 0.07777 | 0.07843/0.07755 | 0.07777 | sup 0.07734 (ha 9 candles) | 0.00065 | 0.0040% | — | sem_zona |
| 2026-10-24 05:06 | ARB-USDT-SWAP | 0.16847 | 0.17092/0.16828 | 0.16847 | sup 0.16712 (ha 7 candles) | 0.00287 | 0.0025% | — | sem_zona |
| 2026-10-24 05:06 | WLD-USDT-SWAP | 0.47230 | 0.47710/0.46720 | 0.47230 | — | 0.00981 | 0.0074% | B/compra@0.47260 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-24 05:06 | SUI-USDT-SWAP | 0.94860 | 0.96090/0.94780 | 0.94860 | sup 0.93870 (ha 9 candles) | 0.01165 | 0.0096% | — | sem_zona |
| 2026-10-24 05:06 | UNI-USDT-SWAP | 6.8480 | 6.9380/6.8370 | 6.8480 | sup 6.7930 (ha 9 candles) | 0.10057 | 0.0073% | — | sem_zona |
| 2026-10-24 05:06 | LINK-USDT-SWAP | 11.71 | 11.82/11.70 | 11.71 | sup 11.59 (ha 9 candles) | 0.11071 | 0.0099% | — | sem_zona |
| 2026-10-24 06:06 | BTC-USDT-SWAP | 80680.2 | 80790.0/80593.8 | 80699.9 | sup 80456.6 (ha 9 candles) | 329.26 | 0.0069% | — | sem_zona |
| 2026-10-24 06:06 | ETH-USDT-SWAP | 2368.3 | 2375.8/2366.0 | 2373.9 | sup 2350.1 (ha 10 candles) | 14.51 | 0.0097% | — | sem_zona |
| 2026-10-24 06:06 | SOL-USDT-SWAP | 101.92 | 102.16/101.71 | 101.87 | sup 101.64 (ha 10 candles) | 0.72000 | 0.0100% | — | sem_zona |
| 2026-10-24 06:06 | XRP-USDT-SWAP | 1.2801 | 1.2856/1.2783 | 1.2845 | — | 0.00903 | 0.0011% | B/compra@1.2886 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-24 06:06 | DOGE-USDT-SWAP | 0.07753 | 0.07789/0.07742 | 0.07777 | sup 0.07734 (ha 10 candles) | 0.00065 | 0.0053% | — | sem_zona |
| 2026-10-24 06:06 | ARB-USDT-SWAP | 0.16899 | 0.16950/0.16813 | 0.16847 | sup 0.16712 (ha 8 candles) | 0.00276 | 0.0043% | — | sem_zona |
| 2026-10-24 06:06 | WLD-USDT-SWAP | 0.46860 | 0.47450/0.46600 | 0.47230 | — | 0.00989 | 0.0095% | — | invalidado_setup_B |
| 2026-10-24 06:06 | SUI-USDT-SWAP | 0.94670 | 0.95070/0.94500 | 0.94860 | sup 0.93870 (ha 10 candles) | 0.01140 | 0.0100% | — | sem_zona |
| 2026-10-24 06:06 | UNI-USDT-SWAP | 6.8380 | 6.8700/6.8220 | 6.8480 | sup 6.7930 (ha 10 candles) | 0.09871 | 0.0063% | — | sem_zona |
| 2026-10-24 06:06 | LINK-USDT-SWAP | 11.64 | 11.73/11.62 | 11.71 | sup 11.59 (ha 10 candles) | 0.11207 | 0.0100% | — | sem_zona |
| 2026-10-24 07:06 | BTC-USDT-SWAP | 80593.8 | 80680.3/80390.5 | 80699.9 | sup 80456.6 (ha 10 candles) | 334.06 | 0.0083% | — | sem_zona |
| 2026-10-24 07:06 | ETH-USDT-SWAP | 2366.5 | 2368.5/2356.1 | 2373.9 | sup 2350.1 (ha 11 candles) | 14.72 | 0.0100% | — | sem_zona |
| 2026-10-24 07:06 | SOL-USDT-SWAP | 101.36 | 101.94/101.08 | 101.87 | sup 101.64 (ha 11 candles) | 0.73214 | 0.0100% | A/venda@101.64 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-24 07:06 | XRP-USDT-SWAP | 1.2762 | 1.2809/1.2725 | 1.2845 | — | 0.00892 | -0.0006% | B/compra@1.2886 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-24 07:06 | DOGE-USDT-SWAP | 0.07725 | 0.07757/0.07682 | 0.07777 | sup 0.07734 (ha 11 candles) | 0.00066 | 0.0043% | A/venda@0.07734 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-24 07:06 | ARB-USDT-SWAP | 0.16910 | 0.16940/0.16814 | 0.16847 | sup 0.16712 (ha 9 candles) | 0.00266 | 0.0056% | — | sem_zona |
| 2026-10-24 07:06 | WLD-USDT-SWAP | 0.46760 | 0.46890/0.46390 | 0.47230 | — | 0.00936 | 0.0100% | B/compra@0.46070 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-24 07:06 | SUI-USDT-SWAP | 0.94370 | 0.94720/0.93880 | 0.94860 | sup 0.93870 (ha 11 candles) | 0.01113 | 0.0100% | — | sem_zona |
| 2026-10-24 07:06 | UNI-USDT-SWAP | 6.8350 | 6.8450/6.7820 | 6.8480 | sup 6.7930 (ha 11 candles) | 0.09786 | 0.0039% | — | sem_zona |
| 2026-10-24 07:06 | LINK-USDT-SWAP | 11.56 | 11.63/11.52 | 11.71 | sup 11.59 (ha 11 candles) | 0.11379 | 0.0081% | A/venda@11.59 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-24 08:06 | BTC-USDT-SWAP | 80638.8 | 80712.2/80488.0 | 80699.9 | sup 80456.6 (ha 11 candles) | 333.53 | 0.0099% | — | sem_zona |
| 2026-10-24 08:06 | ETH-USDT-SWAP | 2369.0 | 2372.7/2363.1 | 2373.9 | sup 2350.1 (ha 12 candles) | 14.58 | 0.0100% | — | sem_zona |
| 2026-10-24 08:06 | SOL-USDT-SWAP | 101.68 | 101.82/101.30 | 101.87 | sup 101.64 (ha 12 candles) | 0.72000 | 0.0100% | A/venda@101.64 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-24 08:06 | XRP-USDT-SWAP | 1.2813 | 1.2827/1.2749 | 1.2845 | — | 0.00884 | -0.0005% | B/compra@1.2886 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-24 08:06 | DOGE-USDT-SWAP | 0.07756 | 0.07757/0.07714 | 0.07777 | sup 0.07734 (ha 12 candles) | 0.00066 | 0.0038% | — | invalidado_setup_A |
| 2026-10-24 08:06 | ARB-USDT-SWAP | 0.16876 | 0.16943/0.16813 | 0.16847 | sup 0.16712 (ha 10 candles) | 0.00256 | 0.0048% | — | sem_zona |
| 2026-10-24 08:06 | WLD-USDT-SWAP | 0.46980 | 0.47110/0.46550 | 0.47230 | — | 0.00935 | 0.0046% | B/compra@0.46070 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-24 08:06 | SUI-USDT-SWAP | 0.94720 | 0.94870/0.94210 | 0.94860 | sup 0.93870 (ha 12 candles) | 0.01099 | 0.0100% | — | sem_zona |
| 2026-10-24 08:06 | UNI-USDT-SWAP | 6.8670 | 6.8800/6.8230 | 6.8480 | sup 6.7930 (ha 12 candles) | 0.09579 | 0.0034% | — | sem_zona |
| 2026-10-24 08:06 | LINK-USDT-SWAP | 11.61 | 11.62/11.54 | 11.71 | sup 11.59 (ha 12 candles) | 0.11393 | 0.0057% | A/venda@11.59 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-24 09:06 | BTC-USDT-SWAP | 80563.3 | 80684.8/80541.2 | 80563.3 | sup 80456.6 (ha 12 candles) | 331.21 | 0.0100% | — | sem_zona |
| 2026-10-24 09:06 | ETH-USDT-SWAP | 2364.6 | 2371.5/2363.9 | 2364.6 | sup 2350.1 (ha 13 candles) | 14.47 | 0.0100% | — | sem_zona |
| 2026-10-24 09:06 | SOL-USDT-SWAP | 101.48 | 101.71/101.24 | 101.48 | sup 101.64 (ha 13 candles) | 0.71071 | 0.0100% | A/venda@101.64 (2t/0c) | zona_mapeada_setup_A |
| 2026-10-24 09:06 | XRP-USDT-SWAP | 1.2808 | 1.2827/1.2775 | 1.2808 | — | 0.00881 | -0.0010% | B/compra@1.2886 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-24 09:06 | DOGE-USDT-SWAP | 0.07755 | 0.07765/0.07734 | 0.07755 | sup 0.07734 (ha 13 candles) | 0.00065 | 0.0031% | — | sem_zona |
| 2026-10-24 09:06 | ARB-USDT-SWAP | 0.16893 | 0.16911/0.16838 | 0.16893 | sup 0.16813 (ha 3 candles) | 0.00249 | 0.0033% | — | sem_zona |
| 2026-10-24 09:06 | WLD-USDT-SWAP | 0.47210 | 0.47270/0.46820 | 0.47210 | — | 0.00909 | -0.0016% | B/compra@0.46070 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-24 09:06 | SUI-USDT-SWAP | 0.94760 | 0.94870/0.94470 | 0.94760 | sup 0.93870 (ha 13 candles) | 0.01071 | 0.0100% | — | sem_zona |
| 2026-10-24 09:06 | UNI-USDT-SWAP | 6.8100 | 6.8810/6.8040 | 6.8100 | sup 6.7930 (ha 13 candles) | 0.09579 | 0.0047% | — | sem_zona |
| 2026-10-24 09:06 | LINK-USDT-SWAP | 11.60 | 11.63/11.59 | 11.60 | sup 11.59 (ha 13 candles) | 0.11079 | 0.0040% | — | descartado_rr_baixo_setup_A |
| 2026-10-24 10:06 | BTC-USDT-SWAP | 80737.6 | 80813.0/80516.0 | 80563.3 | sup 80390.5 (ha 3 candles) | 288.66 | 0.0100% | — | sem_zona |
| 2026-10-24 10:06 | ETH-USDT-SWAP | 2368.2 | 2372.3/2362.3 | 2364.6 | sup 2356.1 (ha 3 candles) | 11.46 | 0.0100% | — | sem_zona |
| 2026-10-24 10:06 | SOL-USDT-SWAP | 101.54 | 101.69/101.27 | 101.48 | sup 101.08 (ha 3 candles) | 0.58571 | 0.0084% | — | zona_expirada_setup_A |
| 2026-10-24 10:06 | XRP-USDT-SWAP | 1.2841 | 1.2869/1.2786 | 1.2808 | — | 0.00739 | -0.0025% | — | invalidado_setup_B |
| 2026-10-24 10:06 | DOGE-USDT-SWAP | 0.07752 | 0.07773/0.07727 | 0.07755 | sup 0.07682 (ha 3 candles) | 0.00053 | -0.0010% | — | sem_zona |
| 2026-10-24 10:06 | ARB-USDT-SWAP | 0.17070 | 0.17148/0.16846 | 0.16893 | sup 0.16813 (ha 4 candles) | 0.00206 | 0.0016% | — | sem_zona |
| 2026-10-24 10:06 | WLD-USDT-SWAP | 0.47040 | 0.47380/0.46930 | 0.47210 | — | 0.00659 | -0.0082% | B/compra@0.46070 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-24 10:06 | SUI-USDT-SWAP | 0.94760 | 0.95230/0.94610 | 0.94760 | sup 0.93880 (ha 3 candles) | 0.00839 | 0.0087% | — | sem_zona |
| 2026-10-24 10:06 | UNI-USDT-SWAP | 6.8210 | 6.8520/6.7900 | 6.8100 | sup 6.7820 (ha 3 candles) | 0.07771 | 0.0051% | — | sem_zona |
| 2026-10-24 10:06 | LINK-USDT-SWAP | 11.62 | 11.64/11.57 | 11.60 | sup 11.52 (ha 3 candles) | 0.08986 | 0.0024% | — | sem_zona |
| 2026-10-24 11:06 | BTC-USDT-SWAP | 80670.2 | 80817.8/80623.0 | 80563.3 | sup 80390.5 (ha 4 candles) | 252.34 | 0.0100% | — | sem_zona |
| 2026-10-24 11:06 | ETH-USDT-SWAP | 2367.3 | 2371.9/2364.0 | 2364.6 | sup 2356.1 (ha 4 candles) | 9.7829 | 0.0092% | — | sem_zona |
| 2026-10-24 11:06 | SOL-USDT-SWAP | 101.37 | 101.75/101.18 | 101.48 | sup 101.08 (ha 4 candles) | 0.54286 | 0.0062% | — | sem_zona |
| 2026-10-24 11:06 | XRP-USDT-SWAP | 1.2832 | 1.2873/1.2806 | 1.2808 | — | 0.00689 | -0.0035% | B/compra@1.2856 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-24 11:06 | DOGE-USDT-SWAP | 0.07749 | 0.07768/0.07727 | 0.07755 | sup 0.07682 (ha 4 candles) | 0.00047 | -0.0036% | — | sem_zona |
| 2026-10-24 11:06 | ARB-USDT-SWAP | 0.16882 | 0.17129/0.16881 | 0.16893 | sup 0.16813 (ha 3 candles) | 0.00200 | -0.0012% | — | sem_zona |
| 2026-10-24 11:06 | WLD-USDT-SWAP | 0.46660 | 0.47160/0.46380 | 0.47210 | — | 0.00651 | -0.0111% | B/compra@0.46070 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-24 11:06 | SUI-USDT-SWAP | 0.94420 | 0.95040/0.94180 | 0.94760 | sup 0.93880 (ha 4 candles) | 0.00762 | 0.0063% | — | sem_zona |
| 2026-10-24 11:06 | UNI-USDT-SWAP | 6.8480 | 6.8560/6.8050 | 6.8100 | sup 6.7820 (ha 4 candles) | 0.07029 | 0.0043% | — | sem_zona |
| 2026-10-24 11:06 | LINK-USDT-SWAP | 11.58 | 11.65/11.57 | 11.60 | sup 11.52 (ha 4 candles) | 0.08186 | 0.0028% | — | sem_zona |
| 2026-10-24 12:06 | BTC-USDT-SWAP | 80168.7 | 80730.2/79758.0 | 80563.3 | sup 80390.5 (ha 5 candles) | 277.79 | 0.0079% | A/venda@80390.5 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-24 12:06 | ETH-USDT-SWAP | 2341.2 | 2369.1/2326.8 | 2364.6 | sup 2356.1 (ha 5 candles) | 11.43 | 0.0061% | A/venda@2356.1 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-24 12:06 | SOL-USDT-SWAP | 100.33 | 101.45/99.58 | 101.48 | sup 101.08 (ha 5 candles) | 0.61214 | 0.0020% | A/venda@101.08 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-24 12:06 | XRP-USDT-SWAP | 1.2732 | 1.2854/1.2644 | 1.2808 | — | 0.00749 | -0.0028% | — | invalidado_setup_B |
| 2026-10-24 12:06 | DOGE-USDT-SWAP | 0.07615 | 0.07760/0.07546 | 0.07755 | sup 0.07682 (ha 5 candles) | 0.00058 | -0.0025% | A/venda@0.07682 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-24 12:06 | ARB-USDT-SWAP | 0.16714 | 0.16902/0.16433 | 0.16893 | sup 0.16813 (ha 4 candles) | 0.00201 | -0.0017% | A/venda@0.16813 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-24 12:06 | WLD-USDT-SWAP | 0.46350 | 0.47000/0.45720 | 0.47210 | — | 0.00661 | -0.0108% | B/compra@0.46070 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-24 12:06 | SUI-USDT-SWAP | 0.92760 | 0.94570/0.91440 | 0.94760 | sup 0.93880 (ha 5 candles) | 0.00892 | 0.0037% | A/venda@0.93880 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-24 12:06 | UNI-USDT-SWAP | 6.6980 | 6.8600/6.5990 | 6.8100 | sup 6.7820 (ha 5 candles) | 0.08057 | 0.0032% | A/venda@6.7820 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-24 12:06 | LINK-USDT-SWAP | 11.46 | 11.61/11.35 | 11.60 | sup 11.52 (ha 5 candles) | 0.09086 | 0.0021% | A/venda@11.52 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-24 13:06 | BTC-USDT-SWAP | 79755.1 | 80194.4/79168.0 | 79755.1 | sup 80390.5 (ha 6 candles) | 325.68 | 0.0044% | A/venda@80390.5 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-24 13:06 | ETH-USDT-SWAP | 2304.7 | 2342.4/2281.0 | 2304.7 | sup 2356.1 (ha 6 candles) | 14.99 | 0.0018% | A/venda@2356.1 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-24 13:06 | SOL-USDT-SWAP | 99.73 | 100.43/98.54 | 99.73 | sup 101.08 (ha 6 candles) | 0.70786 | -0.0009% | A/venda@101.08 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-24 13:06 | XRP-USDT-SWAP | 1.2676 | 1.2745/1.2539 | 1.2676 | — | 0.00844 | -0.0035% | B/compra@1.2692 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-24 13:06 | DOGE-USDT-SWAP | 0.07565 | 0.07620/0.07469 | 0.07565 | sup 0.07682 (ha 6 candles) | 0.00065 | -0.0034% | A/venda@0.07682 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-24 13:06 | ARB-USDT-SWAP | 0.16571 | 0.16739/0.16332 | 0.16571 | sup 0.16813 (ha 5 candles) | 0.00212 | -0.0008% | A/venda@0.16813 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-24 13:06 | WLD-USDT-SWAP | 0.46190 | 0.46480/0.45790 | 0.46190 | — | 0.00670 | -0.0097% | B/compra@0.46070 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-24 13:06 | SUI-USDT-SWAP | 0.92490 | 0.92900/0.91080 | 0.92490 | sup 0.93880 (ha 6 candles) | 0.00951 | 0.0013% | A/venda@0.93880 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-24 13:06 | UNI-USDT-SWAP | 6.6020 | 6.7060/6.5130 | 6.6020 | sup 6.7820 (ha 6 candles) | 0.08786 | 0.0000% | A/venda@6.7820 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-24 13:06 | LINK-USDT-SWAP | 11.38 | 11.47/11.23 | 11.38 | sup 11.52 (ha 6 candles) | 0.10121 | -0.0005% | A/venda@11.52 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-24 14:06 | BTC-USDT-SWAP | 80175.1 | 80266.4/79526.9 | 79755.1 | sup 80390.5 (ha 7 candles) | 367.00 | 0.0019% | A/venda@80390.5 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-24 14:06 | ETH-USDT-SWAP | 2317.0 | 2320.4/2293.0 | 2304.7 | sup 2356.1 (ha 7 candles) | 16.48 | -0.0006% | A/venda@2356.1 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-24 14:06 | SOL-USDT-SWAP | 100.44 | 100.62/99.42 | 99.73 | sup 101.08 (ha 7 candles) | 0.76929 | -0.0020% | A/venda@101.08 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-24 14:06 | XRP-USDT-SWAP | 1.2764 | 1.2774/1.2624 | 1.2676 | — | 0.00924 | -0.0031% | — | descartado_rr_baixo_setup_B |
| 2026-10-24 14:06 | DOGE-USDT-SWAP | 0.07643 | 0.07648/0.07546 | 0.07565 | sup 0.07682 (ha 7 candles) | 0.00071 | -0.0025% | A/venda@0.07682 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-24 14:06 | ARB-USDT-SWAP | 0.16595 | 0.16649/0.16366 | 0.16571 | sup 0.16813 (ha 6 candles) | 0.00218 | 0.0031% | A/venda@0.16813 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-24 14:06 | WLD-USDT-SWAP | 0.46460 | 0.46710/0.45780 | 0.46190 | — | 0.00684 | -0.0101% | — | descartado_rr_baixo_setup_B |
| 2026-10-24 14:06 | SUI-USDT-SWAP | 0.92980 | 0.93200/0.91800 | 0.92490 | sup 0.93880 (ha 7 candles) | 0.01016 | -0.0002% | A/venda@0.93880 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-24 14:06 | UNI-USDT-SWAP | 6.6620 | 6.6700/6.5450 | 6.6020 | sup 6.7820 (ha 7 candles) | 0.09307 | -0.0013% | A/venda@6.7820 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-24 14:06 | LINK-USDT-SWAP | 11.46 | 11.47/11.31 | 11.38 | sup 11.52 (ha 7 candles) | 0.10893 | -0.0015% | A/venda@11.52 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-24 15:06 | BTC-USDT-SWAP | 80233.5 | 80280.4/80065.0 | 79755.1 | sup 80390.5 (ha 8 candles) | 364.88 | 0.0004% | A/venda@80390.5 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-24 15:06 | ETH-USDT-SWAP | 2321.8 | 2325.9/2313.1 | 2304.7 | sup 2356.1 (ha 8 candles) | 16.60 | -0.0021% | A/venda@2356.1 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-24 15:06 | SOL-USDT-SWAP | 100.45 | 100.53/100.04 | 99.73 | sup 101.08 (ha 8 candles) | 0.75857 | -0.0015% | A/venda@101.08 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-24 15:06 | XRP-USDT-SWAP | 1.2758 | 1.2789/1.2727 | 1.2676 | — | 0.00914 | -0.0023% | B/compra@1.2826 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-24 15:06 | DOGE-USDT-SWAP | 0.07646 | 0.07654/0.07615 | 0.07565 | sup 0.07682 (ha 8 candles) | 0.00070 | -0.0004% | A/venda@0.07682 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-24 15:06 | ARB-USDT-SWAP | 0.16545 | 0.16600/0.16378 | 0.16571 | sup 0.16813 (ha 7 candles) | 0.00219 | 0.0056% | A/venda@0.16813 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-24 15:06 | WLD-USDT-SWAP | 0.45830 | 0.46470/0.45710 | 0.46190 | — | 0.00694 | -0.0108% | B/compra@0.45610 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-24 15:06 | SUI-USDT-SWAP | 0.92380 | 0.93000/0.91980 | 0.92490 | sup 0.93880 (ha 8 candles) | 0.01026 | 0.0018% | A/venda@0.93880 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-24 15:06 | UNI-USDT-SWAP | 6.6650 | 6.6890/6.6230 | 6.6020 | sup 6.7820 (ha 8 candles) | 0.09164 | -0.0034% | A/venda@6.7820 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-24 15:06 | LINK-USDT-SWAP | 11.42 | 11.46/11.39 | 11.38 | sup 11.52 (ha 8 candles) | 0.10893 | 0.0001% | A/venda@11.52 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-24 16:06 | BTC-USDT-SWAP | 80502.5 | 80600.0/80209.0 | 79755.1 | sup 79168.0 (ha 3 candles) | 374.28 | -0.0002% | — | invalidado_setup_A |
| 2026-10-24 16:06 | ETH-USDT-SWAP | 2336.8 | 2341.7/2321.2 | 2304.7 | sup 2281.0 (ha 3 candles) | 17.61 | -0.0033% | A/venda@2356.1 (0t/4c) | zona_mapeada_setup_A |
| 2026-10-24 16:06 | SOL-USDT-SWAP | 101.26 | 101.42/100.42 | 99.73 | sup 98.54 (ha 3 candles) | 0.80571 | -0.0006% | — | invalidado_setup_A |
| 2026-10-24 16:06 | XRP-USDT-SWAP | 1.2861 | 1.2884/1.2747 | 1.2676 | — | 0.00981 | -0.0018% | — | descartado_rr_baixo_setup_B |
| 2026-10-24 16:06 | DOGE-USDT-SWAP | 0.07705 | 0.07720/0.07637 | 0.07565 | sup 0.07469 (ha 3 candles) | 0.00074 | 0.0021% | — | invalidado_setup_A |
| 2026-10-24 16:06 | ARB-USDT-SWAP | 0.16816 | 0.16860/0.16525 | 0.16571 | sup 0.16332 (ha 3 candles) | 0.00232 | 0.0072% | A/venda@0.16813 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-24 16:06 | WLD-USDT-SWAP | 0.46680 | 0.46820/0.45800 | 0.46190 | — | 0.00734 | -0.0121% | B/compra@0.45610 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-24 16:06 | SUI-USDT-SWAP | 0.93580 | 0.93790/0.92230 | 0.92490 | sup 0.91080 (ha 3 candles) | 0.01096 | 0.0006% | A/venda@0.93880 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-24 16:06 | UNI-USDT-SWAP | 6.7580 | 6.7790/6.6640 | 6.6020 | sup 6.5130 (ha 3 candles) | 0.09514 | -0.0034% | A/venda@6.7820 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-24 16:06 | LINK-USDT-SWAP | 11.53 | 11.56/11.41 | 11.38 | sup 11.23 (ha 3 candles) | 0.11479 | 0.0009% | A/venda@11.52 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-24 17:06 | BTC-USDT-SWAP | 80443.8 | 80576.7/80443.7 | 80443.8 | sup 79168.0 (ha 4 candles) | 370.83 | -0.0000% | — | sem_zona |
| 2026-10-24 17:06 | ETH-USDT-SWAP | 2338.4 | 2340.8/2334.4 | 2338.4 | sup 2281.0 (ha 4 candles) | 17.55 | -0.0040% | A/venda@2356.1 (0t/5c) | zona_mapeada_setup_A |
| 2026-10-24 17:06 | SOL-USDT-SWAP | 101.10 | 101.32/101.00 | 101.10 | sup 98.54 (ha 4 candles) | 0.79286 | 0.0010% | — | sem_zona |
| 2026-10-24 17:06 | XRP-USDT-SWAP | 1.2882 | 1.2906/1.2847 | 1.2882 | — | 0.00986 | -0.0015% | B/compra@1.2943 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-24 17:06 | DOGE-USDT-SWAP | 0.07707 | 0.07718/0.07691 | 0.07707 | sup 0.07469 (ha 4 candles) | 0.00072 | 0.0015% | — | sem_zona |
| 2026-10-24 17:06 | ARB-USDT-SWAP | 0.16735 | 0.16818/0.16678 | 0.16735 | sup 0.16332 (ha 4 candles) | 0.00233 | 0.0059% | A/venda@0.16813 (2t/0c) | zona_mapeada_setup_A |
| 2026-10-24 17:06 | WLD-USDT-SWAP | 0.46390 | 0.46670/0.46250 | 0.46390 | — | 0.00719 | -0.0121% | B/compra@0.45610 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-24 17:06 | SUI-USDT-SWAP | 0.93500 | 0.93730/0.93320 | 0.93500 | sup 0.91080 (ha 4 candles) | 0.01079 | -0.0013% | A/venda@0.93880 (2t/0c) | zona_mapeada_setup_A |
| 2026-10-24 17:06 | UNI-USDT-SWAP | 6.7690 | 6.7800/6.7470 | 6.7690 | sup 6.5130 (ha 4 candles) | 0.09243 | -0.0014% | A/venda@6.7820 (2t/0c) | zona_mapeada_setup_A |
| 2026-10-24 17:06 | LINK-USDT-SWAP | 11.54 | 11.55/11.51 | 11.54 | sup 11.23 (ha 4 candles) | 0.11200 | 0.0015% | A/venda@11.52 (2t/0c) | zona_mapeada_setup_A |
| 2026-10-24 18:06 | BTC-USDT-SWAP | 80480.5 | 80588.0/80443.8 | 80443.8 | sup 79168.0 (ha 5 candles) | 370.64 | 0.0002% | — | sem_zona |
| 2026-10-24 18:06 | ETH-USDT-SWAP | 2346.0 | 2349.0/2338.4 | 2338.4 | sup 2281.0 (ha 5 candles) | 17.85 | -0.0028% | A/venda@2356.1 (0t/6c) | zona_mapeada_setup_A |
| 2026-10-24 18:06 | SOL-USDT-SWAP | 101.54 | 101.65/101.11 | 101.10 | sup 98.54 (ha 5 candles) | 0.80357 | 0.0032% | — | sem_zona |
| 2026-10-24 18:06 | XRP-USDT-SWAP | 1.2908 | 1.2944/1.2882 | 1.2882 | — | 0.01006 | -0.0005% | — | invalidado_setup_B |
| 2026-10-24 18:06 | DOGE-USDT-SWAP | 0.07724 | 0.07747/0.07706 | 0.07707 | sup 0.07469 (ha 5 candles) | 0.00073 | -0.0004% | — | sem_zona |
| 2026-10-24 18:06 | ARB-USDT-SWAP | 0.16759 | 0.16886/0.16734 | 0.16735 | sup 0.16332 (ha 5 candles) | 0.00235 | 0.0032% | — | zona_expirada_setup_A |
| 2026-10-24 18:06 | WLD-USDT-SWAP | 0.46620 | 0.46980/0.46400 | 0.46390 | — | 0.00734 | -0.0140% | B/compra@0.45610 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-24 18:06 | SUI-USDT-SWAP | 0.93660 | 0.94060/0.93500 | 0.93500 | sup 0.91080 (ha 5 candles) | 0.01083 | -0.0029% | — | zona_expirada_setup_A |
| 2026-10-24 18:06 | UNI-USDT-SWAP | 6.8000 | 6.8270/6.7700 | 6.7690 | sup 6.5130 (ha 5 candles) | 0.09357 | 0.0003% | — | zona_expirada_setup_A |
| 2026-10-24 18:06 | LINK-USDT-SWAP | 11.57 | 11.61/11.54 | 11.54 | sup 11.23 (ha 5 candles) | 0.11414 | 0.0027% | — | invalidado_setup_A |
| 2026-10-24 19:06 | BTC-USDT-SWAP | 80380.9 | 80484.7/80260.0 | 80443.8 | sup 79168.0 (ha 6 candles) | 370.86 | 0.0010% | — | sem_zona |
| 2026-10-24 19:06 | ETH-USDT-SWAP | 2339.1 | 2346.3/2333.0 | 2338.4 | sup 2281.0 (ha 6 candles) | 18.00 | -0.0015% | A/venda@2356.1 (0t/7c) | zona_mapeada_setup_A |
| 2026-10-24 19:06 | SOL-USDT-SWAP | 101.33 | 101.55/101.05 | 101.10 | sup 98.54 (ha 6 candles) | 0.79357 | 0.0052% | — | sem_zona |
| 2026-10-24 19:06 | XRP-USDT-SWAP | 1.2920 | 1.2942/1.2888 | 1.2882 | — | 0.00984 | 0.0013% | B/compra@1.2856 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-24 19:06 | DOGE-USDT-SWAP | 0.07709 | 0.07726/0.07691 | 0.07707 | sup 0.07469 (ha 6 candles) | 0.00070 | -0.0008% | — | sem_zona |
| 2026-10-24 19:06 | ARB-USDT-SWAP | 0.16653 | 0.16761/0.16640 | 0.16735 | sup 0.16332 (ha 6 candles) | 0.00225 | 0.0040% | — | sem_zona |
| 2026-10-24 19:06 | WLD-USDT-SWAP | 0.46330 | 0.46650/0.46200 | 0.46390 | — | 0.00696 | -0.0116% | B/compra@0.45610 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-24 19:06 | SUI-USDT-SWAP | 0.92840 | 0.93690/0.92790 | 0.93500 | sup 0.91080 (ha 6 candles) | 0.01054 | -0.0029% | — | sem_zona |
| 2026-10-24 19:06 | UNI-USDT-SWAP | 6.7670 | 6.8050/6.7550 | 6.7690 | sup 6.5130 (ha 6 candles) | 0.08993 | 0.0036% | — | sem_zona |
| 2026-10-24 19:06 | LINK-USDT-SWAP | 11.52 | 11.57/11.49 | 11.54 | sup 11.23 (ha 6 candles) | 0.11136 | 0.0063% | — | sem_zona |
| 2026-10-24 20:06 | BTC-USDT-SWAP | 80563.3 | 80616.6/80380.9 | 80443.8 | sup 79168.0 (ha 7 candles) | 373.68 | 0.0016% | — | sem_zona |
| 2026-10-24 20:06 | ETH-USDT-SWAP | 2345.5 | 2345.5/2339.0 | 2338.4 | sup 2281.0 (ha 7 candles) | 17.76 | 0.0006% | — | zona_expirada_setup_A |
| 2026-10-24 20:06 | SOL-USDT-SWAP | 101.56 | 101.70/101.33 | 101.10 | sup 98.54 (ha 7 candles) | 0.78786 | 0.0058% | — | sem_zona |
| 2026-10-24 20:06 | XRP-USDT-SWAP | 1.2933 | 1.2955/1.2899 | 1.2882 | — | 0.00971 | 0.0033% | B/compra@1.2856 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-24 20:06 | DOGE-USDT-SWAP | 0.07734 | 0.07737/0.07708 | 0.07707 | sup 0.07469 (ha 7 candles) | 0.00068 | -0.0021% | — | sem_zona |
| 2026-10-24 20:06 | ARB-USDT-SWAP | 0.16751 | 0.16774/0.16640 | 0.16735 | sup 0.16332 (ha 7 candles) | 0.00224 | 0.0008% | — | sem_zona |
| 2026-10-24 20:06 | WLD-USDT-SWAP | 0.46450 | 0.46490/0.45830 | 0.46390 | — | 0.00682 | -0.0068% | B/compra@0.45610 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-24 20:06 | SUI-USDT-SWAP | 0.93230 | 0.93240/0.92820 | 0.93500 | sup 0.91080 (ha 7 candles) | 0.01043 | -0.0023% | — | sem_zona |
| 2026-10-24 20:06 | UNI-USDT-SWAP | 6.8170 | 6.8250/6.7640 | 6.7690 | sup 6.5130 (ha 7 candles) | 0.09086 | 0.0046% | — | sem_zona |
| 2026-10-24 20:06 | LINK-USDT-SWAP | 11.56 | 11.57/11.52 | 11.54 | sup 11.23 (ha 7 candles) | 0.10779 | 0.0079% | — | sem_zona |
| 2026-10-24 21:06 | BTC-USDT-SWAP | 80850.0 | 80897.6/80498.6 | 80850.0 | sup 79168.0 (ha 8 candles) | 381.48 | 0.0023% | — | sem_zona |
| 2026-10-24 21:06 | ETH-USDT-SWAP | 2357.4 | 2361.0/2341.7 | 2357.4 | sup 2281.0 (ha 8 candles) | 18.26 | 0.0013% | — | sem_zona |
| 2026-10-24 21:06 | SOL-USDT-SWAP | 102.30 | 102.52/101.50 | 102.30 | sup 98.54 (ha 8 candles) | 0.79929 | 0.0041% | — | sem_zona |
| 2026-10-24 21:06 | XRP-USDT-SWAP | 1.2988 | 1.3009/1.2910 | 1.2988 | — | 0.00982 | 0.0053% | B/compra@1.2856 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-24 21:06 | DOGE-USDT-SWAP | 0.07763 | 0.07777/0.07715 | 0.07763 | sup 0.07469 (ha 8 candles) | 0.00067 | -0.0026% | — | sem_zona |
| 2026-10-24 21:06 | ARB-USDT-SWAP | 0.16914 | 0.16986/0.16717 | 0.16914 | sup 0.16332 (ha 8 candles) | 0.00235 | -0.0023% | — | sem_zona |
| 2026-10-24 21:06 | WLD-USDT-SWAP | 0.46860 | 0.46980/0.46360 | 0.46860 | — | 0.00691 | -0.0077% | B/compra@0.45610 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-24 21:06 | SUI-USDT-SWAP | 0.93810 | 0.94120/0.93150 | 0.93810 | sup 0.91080 (ha 8 candles) | 0.01052 | -0.0011% | — | sem_zona |
| 2026-10-24 21:06 | UNI-USDT-SWAP | 6.8610 | 6.8930/6.8110 | 6.8610 | sup 6.5130 (ha 8 candles) | 0.09221 | 0.0050% | — | sem_zona |
| 2026-10-24 21:06 | LINK-USDT-SWAP | 11.62 | 11.65/11.55 | 11.62 | sup 11.23 (ha 8 candles) | 0.10636 | 0.0080% | — | sem_zona |
| 2026-10-24 22:06 | BTC-USDT-SWAP | 80844.4 | 80879.9/80732.6 | 80850.0 | sup 79168.0 (ha 9 candles) | 375.99 | 0.0032% | — | sem_zona |
| 2026-10-24 22:06 | ETH-USDT-SWAP | 2359.3 | 2362.7/2354.0 | 2357.4 | sup 2281.0 (ha 9 candles) | 18.19 | 0.0013% | — | sem_zona |
| 2026-10-24 22:06 | SOL-USDT-SWAP | 102.40 | 102.55/102.14 | 102.30 | sup 98.54 (ha 9 candles) | 0.79143 | 0.0016% | — | sem_zona |
| 2026-10-24 22:06 | XRP-USDT-SWAP | 1.3043 | 1.3059/1.2977 | 1.2988 | — | 0.00985 | 0.0049% | B/compra@1.2856 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-24 22:06 | DOGE-USDT-SWAP | 0.07783 | 0.07803/0.07754 | 0.07763 | sup 0.07469 (ha 9 candles) | 0.00068 | -0.0033% | — | sem_zona |
| 2026-10-24 22:06 | ARB-USDT-SWAP | 0.17068 | 0.17079/0.16892 | 0.16914 | sup 0.16332 (ha 9 candles) | 0.00239 | -0.0052% | — | sem_zona |
| 2026-10-24 22:06 | WLD-USDT-SWAP | 0.47000 | 0.47220/0.46660 | 0.46860 | — | 0.00691 | -0.0087% | B/compra@0.45610 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-24 22:06 | SUI-USDT-SWAP | 0.94010 | 0.94230/0.93640 | 0.93810 | sup 0.91080 (ha 9 candles) | 0.01047 | -0.0038% | — | sem_zona |
| 2026-10-24 22:06 | UNI-USDT-SWAP | 6.8710 | 6.8950/6.8510 | 6.8610 | sup 6.5130 (ha 9 candles) | 0.09129 | 0.0048% | — | sem_zona |
| 2026-10-24 22:06 | LINK-USDT-SWAP | 11.63 | 11.64/11.60 | 11.62 | sup 11.23 (ha 9 candles) | 0.10364 | 0.0089% | — | sem_zona |
| 2026-10-24 23:06 | BTC-USDT-SWAP | 80872.6 | 80895.2/80745.4 | 80850.0 | sup 79168.0 (ha 10 candles) | 376.43 | 0.0041% | — | sem_zona |
| 2026-10-24 23:06 | ETH-USDT-SWAP | 2363.5 | 2364.2/2354.9 | 2357.4 | sup 2281.0 (ha 10 candles) | 18.32 | 0.0013% | — | sem_zona |
| 2026-10-24 23:06 | SOL-USDT-SWAP | 102.43 | 102.54/102.11 | 102.30 | sup 98.54 (ha 10 candles) | 0.78857 | -0.0004% | — | sem_zona |
| 2026-10-24 23:06 | XRP-USDT-SWAP | 1.3067 | 1.3067/1.2997 | 1.2988 | — | 0.00998 | 0.0037% | B/compra@1.2856 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-24 23:06 | DOGE-USDT-SWAP | 0.07787 | 0.07796/0.07765 | 0.07763 | sup 0.07469 (ha 10 candles) | 0.00068 | -0.0033% | — | sem_zona |
| 2026-10-24 23:06 | ARB-USDT-SWAP | 0.16990 | 0.17072/0.16953 | 0.16914 | sup 0.16640 (ha 3 candles) | 0.00242 | -0.0088% | — | sem_zona |
| 2026-10-24 23:06 | WLD-USDT-SWAP | 0.46860 | 0.47270/0.46700 | 0.46860 | — | 0.00699 | -0.0102% | — | zona_expirada_setup_B |
| 2026-10-24 23:06 | SUI-USDT-SWAP | 0.93910 | 0.94010/0.93660 | 0.93810 | sup 0.91080 (ha 10 candles) | 0.01044 | -0.0030% | — | sem_zona |
| 2026-10-24 23:06 | UNI-USDT-SWAP | 6.8400 | 6.8750/6.8260 | 6.8610 | sup 6.5130 (ha 10 candles) | 0.08929 | 0.0064% | — | sem_zona |
| 2026-10-24 23:06 | LINK-USDT-SWAP | 11.62 | 11.63/11.59 | 11.62 | sup 11.23 (ha 10 candles) | 0.10364 | 0.0100% | — | sem_zona |
| 2026-10-25 00:06 | BTC-USDT-SWAP | 80880.1 | 80978.0/80778.0 | 80850.0 | sup 79168.0 (ha 11 candles) | 369.50 | 0.0060% | — | sem_zona |
| 2026-10-25 00:06 | ETH-USDT-SWAP | 2364.5 | 2371.0/2359.6 | 2357.4 | sup 2281.0 (ha 11 candles) | 18.41 | 0.0015% | — | sem_zona |
| 2026-10-25 00:06 | SOL-USDT-SWAP | 102.37 | 102.59/102.21 | 102.30 | sup 98.54 (ha 11 candles) | 0.78571 | -0.0031% | — | sem_zona |
| 2026-10-25 00:06 | XRP-USDT-SWAP | 1.3108 | 1.3125/1.3040 | 1.2988 | — | 0.00999 | 0.0031% | B/compra@1.2856 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-25 00:06 | DOGE-USDT-SWAP | 0.07771 | 0.07797/0.07767 | 0.07763 | sup 0.07469 (ha 11 candles) | 0.00067 | -0.0039% | — | sem_zona |
| 2026-10-25 00:06 | ARB-USDT-SWAP | 0.16848 | 0.17016/0.16848 | 0.16914 | sup 0.16640 (ha 4 candles) | 0.00232 | -0.0103% | — | sem_zona |
| 2026-10-25 00:06 | WLD-USDT-SWAP | 0.46620 | 0.47140/0.46580 | 0.46860 | — | 0.00707 | -0.0105% | — | sem_zona |
| 2026-10-25 00:06 | SUI-USDT-SWAP | 0.93510 | 0.94080/0.93430 | 0.93810 | sup 0.91080 (ha 11 candles) | 0.01046 | -0.0027% | — | sem_zona |
| 2026-10-25 00:06 | UNI-USDT-SWAP | 6.8170 | 6.8610/6.8090 | 6.8610 | sup 6.5130 (ha 11 candles) | 0.08857 | 0.0024% | — | sem_zona |
| 2026-10-25 00:06 | LINK-USDT-SWAP | 11.58 | 11.63/11.58 | 11.62 | sup 11.23 (ha 11 candles) | 0.10243 | 0.0100% | — | sem_zona |
| 2026-10-25 01:06 | BTC-USDT-SWAP | 80826.6 | 81008.0/80819.0 | 80826.6 | sup 79168.0 (ha 12 candles) | 369.09 | 0.0076% | — | sem_zona |
| 2026-10-25 01:06 | ETH-USDT-SWAP | 2361.6 | 2368.4/2360.7 | 2361.6 | sup 2281.0 (ha 12 candles) | 18.40 | 0.0010% | — | sem_zona |
| 2026-10-25 01:06 | SOL-USDT-SWAP | 102.37 | 102.67/102.29 | 102.37 | sup 98.54 (ha 12 candles) | 0.77214 | -0.0055% | — | sem_zona |
| 2026-10-25 01:06 | XRP-USDT-SWAP | 1.3104 | 1.3125/1.3082 | 1.3104 | sup 1.2539 (ha 12 candles) | 0.00982 | 0.0028% | B/compra@1.2856 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-25 01:06 | DOGE-USDT-SWAP | 0.07782 | 0.07790/0.07763 | 0.07782 | sup 0.07469 (ha 12 candles) | 0.00066 | -0.0051% | — | sem_zona |
| 2026-10-25 01:06 | ARB-USDT-SWAP | 0.16791 | 0.16887/0.16778 | 0.16791 | sup 0.16640 (ha 5 candles) | 0.00223 | -0.0076% | — | sem_zona |
| 2026-10-25 01:06 | WLD-USDT-SWAP | 0.46870 | 0.47170/0.46570 | 0.46870 | — | 0.00694 | -0.0116% | B/compra@0.47260 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-25 01:06 | SUI-USDT-SWAP | 0.93650 | 0.93950/0.93420 | 0.93650 | sup 0.91080 (ha 12 candles) | 0.01022 | -0.0038% | — | sem_zona |
| 2026-10-25 01:06 | UNI-USDT-SWAP | 6.8200 | 6.8430/6.8010 | 6.8200 | sup 6.5130 (ha 12 candles) | 0.08793 | -0.0002% | — | sem_zona |
| 2026-10-25 01:06 | LINK-USDT-SWAP | 11.58 | 11.62/11.57 | 11.58 | sup 11.23 (ha 12 candles) | 0.09950 | 0.0100% | — | sem_zona |
| 2026-10-25 02:06 | BTC-USDT-SWAP | 80896.3 | 80925.9/80786.1 | 80826.6 | sup 79168.0 (ha 13 candles) | 309.63 | 0.0082% | — | sem_zona |
| 2026-10-25 02:06 | ETH-USDT-SWAP | 2367.1 | 2368.6/2361.1 | 2361.6 | sup 2281.0 (ha 13 candles) | 15.91 | 0.0010% | — | sem_zona |
| 2026-10-25 02:06 | SOL-USDT-SWAP | 102.56 | 102.72/102.30 | 102.37 | sup 98.54 (ha 13 candles) | 0.66857 | -0.0061% | — | sem_zona |
| 2026-10-25 02:06 | XRP-USDT-SWAP | 1.3132 | 1.3153/1.3082 | 1.3104 | sup 1.2539 (ha 13 candles) | 0.00883 | 0.0029% | B/compra@1.2856 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-25 02:06 | DOGE-USDT-SWAP | 0.07788 | 0.07799/0.07778 | 0.07782 | sup 0.07469 (ha 13 candles) | 0.00052 | -0.0057% | — | sem_zona |
| 2026-10-25 02:06 | ARB-USDT-SWAP | 0.16754 | 0.16831/0.16741 | 0.16791 | sup 0.16640 (ha 6 candles) | 0.00195 | -0.0029% | — | sem_zona |
| 2026-10-25 02:06 | WLD-USDT-SWAP | 0.46920 | 0.47090/0.46740 | 0.46870 | — | 0.00628 | -0.0117% | — | invalidado_setup_B |
| 2026-10-25 02:06 | SUI-USDT-SWAP | 0.93190 | 0.93690/0.93180 | 0.93650 | sup 0.91080 (ha 13 candles) | 0.00835 | -0.0010% | — | sem_zona |
| 2026-10-25 02:06 | UNI-USDT-SWAP | 6.8220 | 6.8300/6.7960 | 6.8200 | sup 6.5130 (ha 13 candles) | 0.07171 | 0.0009% | — | sem_zona |
| 2026-10-25 02:06 | LINK-USDT-SWAP | 11.58 | 11.60/11.57 | 11.58 | sup 11.23 (ha 13 candles) | 0.08264 | 0.0100% | — | sem_zona |
| 2026-10-25 03:06 | BTC-USDT-SWAP | 80578.7 | 80896.7/80459.6 | 80826.6 | sup 79168.0 (ha 14 candles) | 267.54 | 0.0082% | — | sem_zona |
| 2026-10-25 03:06 | ETH-USDT-SWAP | 2352.3 | 2367.7/2345.9 | 2361.6 | sup 2281.0 (ha 14 candles) | 13.08 | 0.0001% | — | sem_zona |
| 2026-10-25 03:06 | SOL-USDT-SWAP | 101.91 | 102.58/101.68 | 102.37 | sup 98.54 (ha 14 candles) | 0.59786 | -0.0056% | — | sem_zona |
| 2026-10-25 03:06 | XRP-USDT-SWAP | 1.3000 | 1.3135/1.2982 | 1.3104 | sup 1.2539 (ha 14 candles) | 0.00845 | 0.0028% | — | zona_expirada_setup_B |
| 2026-10-25 03:06 | DOGE-USDT-SWAP | 0.07705 | 0.07790/0.07686 | 0.07782 | sup 0.07469 (ha 14 candles) | 0.00049 | -0.0068% | — | sem_zona |
| 2026-10-25 03:06 | ARB-USDT-SWAP | 0.16673 | 0.16776/0.16615 | 0.16791 | sup 0.16640 (ha 7 candles) | 0.00178 | -0.0012% | — | sem_zona |
| 2026-10-25 03:06 | WLD-USDT-SWAP | 0.46580 | 0.47030/0.46450 | 0.46870 | — | 0.00620 | -0.0091% | — | sem_zona |
| 2026-10-25 03:06 | SUI-USDT-SWAP | 0.91980 | 0.93210/0.91620 | 0.93650 | sup 0.91080 (ha 14 candles) | 0.00819 | 0.0023% | — | sem_zona |
| 2026-10-25 03:06 | UNI-USDT-SWAP | 6.7790 | 6.8410/6.7550 | 6.8200 | sup 6.5130 (ha 14 candles) | 0.06407 | 0.0013% | — | sem_zona |
| 2026-10-25 03:06 | LINK-USDT-SWAP | 11.44 | 11.58/11.42 | 11.58 | sup 11.23 (ha 14 candles) | 0.07707 | 0.0099% | — | sem_zona |
| 2026-10-25 04:06 | BTC-USDT-SWAP | 80467.3 | 80648.6/80391.7 | 80826.6 | sup 79168.0 (ha 15 candles) | 233.06 | 0.0090% | — | sem_zona |
| 2026-10-25 04:06 | ETH-USDT-SWAP | 2339.9 | 2353.2/2335.0 | 2361.6 | sup 2281.0 (ha 15 candles) | 12.43 | 0.0009% | — | sem_zona |
| 2026-10-25 04:06 | SOL-USDT-SWAP | 101.27 | 101.95/101.17 | 102.37 | sup 98.54 (ha 15 candles) | 0.56786 | -0.0039% | — | sem_zona |
| 2026-10-25 04:06 | XRP-USDT-SWAP | 1.2943 | 1.3025/1.2935 | 1.3104 | sup 1.2539 (ha 15 candles) | 0.00802 | 0.0041% | — | sem_zona |
| 2026-10-25 04:06 | DOGE-USDT-SWAP | 0.07667 | 0.07709/0.07651 | 0.07782 | sup 0.07469 (ha 15 candles) | 0.00045 | -0.0061% | — | sem_zona |
| 2026-10-25 04:06 | ARB-USDT-SWAP | 0.16544 | 0.16680/0.16485 | 0.16791 | sup 0.16640 (ha 8 candles) | 0.00172 | 0.0022% | A/venda@0.16640 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-25 04:06 | WLD-USDT-SWAP | 0.46310 | 0.46630/0.46010 | 0.46870 | — | 0.00598 | -0.0066% | B/compra@0.46070 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-25 04:06 | SUI-USDT-SWAP | 0.91500 | 0.92190/0.91210 | 0.93650 | sup 0.91080 (ha 15 candles) | 0.00789 | 0.0051% | — | sem_zona |
| 2026-10-25 04:06 | UNI-USDT-SWAP | 6.7260 | 6.7860/6.7090 | 6.8200 | sup 6.5130 (ha 15 candles) | 0.06064 | 0.0034% | — | sem_zona |
| 2026-10-25 04:06 | LINK-USDT-SWAP | 11.36 | 11.45/11.33 | 11.58 | sup 11.23 (ha 15 candles) | 0.07436 | 0.0094% | — | sem_zona |
| 2026-10-25 05:06 | BTC-USDT-SWAP | 80648.0 | 80690.5/80467.3 | 80648.0 | sup 79168.0 (ha 16 candles) | 233.62 | 0.0094% | — | sem_zona |
| 2026-10-25 05:06 | ETH-USDT-SWAP | 2347.1 | 2349.9/2339.9 | 2347.1 | sup 2281.0 (ha 16 candles) | 12.23 | 0.0013% | — | sem_zona |
| 2026-10-25 05:06 | SOL-USDT-SWAP | 101.60 | 101.83/101.26 | 101.60 | sup 98.54 (ha 16 candles) | 0.57357 | -0.0021% | — | sem_zona |
| 2026-10-25 05:06 | XRP-USDT-SWAP | 1.3014 | 1.3047/1.2942 | 1.3014 | sup 1.2539 (ha 16 candles) | 0.00833 | 0.0058% | — | sem_zona |
| 2026-10-25 05:06 | DOGE-USDT-SWAP | 0.07692 | 0.07709/0.07664 | 0.07692 | sup 0.07469 (ha 16 candles) | 0.00046 | -0.0049% | — | sem_zona |
| 2026-10-25 05:06 | ARB-USDT-SWAP | 0.16638 | 0.16680/0.16524 | 0.16638 | sup 0.16640 (ha 9 candles) | 0.00167 | 0.0031% | A/venda@0.16640 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-25 05:06 | WLD-USDT-SWAP | 0.46560 | 0.46650/0.46190 | 0.46560 | — | 0.00576 | -0.0038% | — | descartado_rr_baixo_setup_B |
| 2026-10-25 05:06 | SUI-USDT-SWAP | 0.91830 | 0.92110/0.91380 | 0.91830 | sup 0.91080 (ha 16 candles) | 0.00768 | 0.0066% | — | sem_zona |
| 2026-10-25 05:06 | UNI-USDT-SWAP | 6.7720 | 6.7920/6.7160 | 6.7720 | sup 6.5130 (ha 16 candles) | 0.06136 | 0.0013% | — | sem_zona |
| 2026-10-25 05:06 | LINK-USDT-SWAP | 11.40 | 11.42/11.35 | 11.40 | sup 11.23 (ha 16 candles) | 0.07364 | 0.0084% | — | sem_zona |
| 2026-10-25 06:06 | BTC-USDT-SWAP | 80373.0 | 80671.3/80331.8 | 80648.0 | sup 79168.0 (ha 17 candles) | 229.94 | 0.0091% | — | sem_zona |
| 2026-10-25 06:06 | ETH-USDT-SWAP | 2334.2 | 2347.6/2331.1 | 2347.1 | sup 2281.0 (ha 17 candles) | 11.94 | 0.0020% | — | sem_zona |
| 2026-10-25 06:06 | SOL-USDT-SWAP | 100.78 | 101.61/100.62 | 101.60 | sup 98.54 (ha 17 candles) | 0.57286 | -0.0011% | — | sem_zona |
| 2026-10-25 06:06 | XRP-USDT-SWAP | 1.2946 | 1.3028/1.2918 | 1.3014 | sup 1.2539 (ha 17 candles) | 0.00814 | 0.0064% | — | sem_zona |
| 2026-10-25 06:06 | DOGE-USDT-SWAP | 0.07628 | 0.07694/0.07617 | 0.07692 | sup 0.07469 (ha 17 candles) | 0.00045 | -0.0033% | — | sem_zona |
| 2026-10-25 06:06 | ARB-USDT-SWAP | 0.16389 | 0.16654/0.16314 | 0.16638 | sup 0.16640 (ha 10 candles) | 0.00167 | 0.0033% | — | descartado_rr_baixo_setup_A |
| 2026-10-25 06:06 | WLD-USDT-SWAP | 0.44200 | 0.46570/0.43160 | 0.46560 | — | 0.00747 | 0.0005% | — | sem_zona |
| 2026-10-25 06:06 | SUI-USDT-SWAP | 0.90960 | 0.92010/0.90770 | 0.91830 | sup 0.91080 (ha 17 candles) | 0.00745 | 0.0063% | A/venda@0.91080 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-25 06:06 | UNI-USDT-SWAP | 6.6800 | 6.7750/6.6670 | 6.7720 | sup 6.5130 (ha 17 candles) | 0.06086 | -0.0004% | — | sem_zona |
| 2026-10-25 06:06 | LINK-USDT-SWAP | 11.32 | 11.41/11.29 | 11.40 | sup 11.23 (ha 17 candles) | 0.07157 | 0.0070% | — | sem_zona |
| 2026-10-25 07:06 | BTC-USDT-SWAP | 80300.1 | 80424.9/80050.0 | 80648.0 | sup 79168.0 (ha 18 candles) | 247.22 | 0.0100% | — | sem_zona |
| 2026-10-25 07:06 | ETH-USDT-SWAP | 2326.7 | 2336.0/2316.0 | 2347.1 | sup 2281.0 (ha 18 candles) | 12.91 | 0.0036% | — | sem_zona |
| 2026-10-25 07:06 | SOL-USDT-SWAP | 100.84 | 100.96/100.28 | 101.60 | sup 98.54 (ha 18 candles) | 0.59857 | 0.0015% | — | sem_zona |
| 2026-10-25 07:06 | XRP-USDT-SWAP | 1.2937 | 1.2968/1.2884 | 1.3014 | sup 1.2539 (ha 18 candles) | 0.00831 | 0.0076% | — | sem_zona |
| 2026-10-25 07:06 | DOGE-USDT-SWAP | 0.07648 | 0.07651/0.07591 | 0.07692 | sup 0.07469 (ha 18 candles) | 0.00048 | 0.0003% | — | sem_zona |
| 2026-10-25 07:06 | ARB-USDT-SWAP | 0.16461 | 0.16474/0.16304 | 0.16638 | sup 0.16640 (ha 11 candles) | 0.00169 | 0.0054% | — | sem_zona |
| 2026-10-25 07:06 | WLD-USDT-SWAP | 0.44680 | 0.44800/0.43690 | 0.46560 | — | 0.00796 | 0.0018% | — | sem_zona |
| 2026-10-25 07:06 | SUI-USDT-SWAP | 0.91180 | 0.91280/0.90340 | 0.91830 | sup 0.91080 (ha 18 candles) | 0.00783 | 0.0064% | A/venda@0.91080 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-25 07:06 | UNI-USDT-SWAP | 6.7000 | 6.7050/6.6380 | 6.7720 | sup 6.5130 (ha 18 candles) | 0.06329 | 0.0014% | — | sem_zona |
| 2026-10-25 07:06 | LINK-USDT-SWAP | 11.32 | 11.34/11.25 | 11.40 | sup 11.23 (ha 18 candles) | 0.07529 | 0.0051% | — | sem_zona |
| 2026-10-25 08:06 | BTC-USDT-SWAP | 80240.0 | 80392.7/80176.1 | 80648.0 | sup 79168.0 (ha 19 candles) | 252.39 | 0.0100% | — | sem_zona |
| 2026-10-25 08:06 | ETH-USDT-SWAP | 2325.5 | 2331.3/2321.4 | 2347.1 | sup 2281.0 (ha 19 candles) | 12.86 | 0.0044% | — | sem_zona |
| 2026-10-25 08:06 | SOL-USDT-SWAP | 100.68 | 100.93/100.51 | 101.60 | sup 98.54 (ha 19 candles) | 0.58929 | 0.0023% | — | sem_zona |
| 2026-10-25 08:06 | XRP-USDT-SWAP | 1.2920 | 1.2957/1.2894 | 1.3014 | sup 1.2539 (ha 19 candles) | 0.00832 | 0.0076% | — | sem_zona |
| 2026-10-25 08:06 | DOGE-USDT-SWAP | 0.07640 | 0.07664/0.07632 | 0.07692 | sup 0.07469 (ha 19 candles) | 0.00047 | 0.0009% | — | sem_zona |
| 2026-10-25 08:06 | ARB-USDT-SWAP | 0.16424 | 0.16487/0.16399 | 0.16638 | sup 0.16640 (ha 12 candles) | 0.00165 | 0.0066% | — | sem_zona |
| 2026-10-25 08:06 | WLD-USDT-SWAP | 0.44390 | 0.44720/0.44100 | 0.46560 | — | 0.00798 | 0.0058% | — | sem_zona |
| 2026-10-25 08:06 | SUI-USDT-SWAP | 0.90950 | 0.91320/0.90750 | 0.91830 | sup 0.91080 (ha 19 candles) | 0.00784 | 0.0065% | — | descartado_rr_baixo_setup_A |
| 2026-10-25 08:06 | UNI-USDT-SWAP | 6.6680 | 6.7120/6.6580 | 6.7720 | sup 6.5130 (ha 19 candles) | 0.06300 | 0.0023% | — | sem_zona |
| 2026-10-25 08:06 | LINK-USDT-SWAP | 11.31 | 11.33/11.29 | 11.40 | sup 11.23 (ha 19 candles) | 0.07343 | 0.0025% | — | sem_zona |
| 2026-10-25 09:06 | BTC-USDT-SWAP | 80543.3 | 80611.5/80240.0 | 80543.3 | sup 79168.0 (ha 20 candles) | 262.88 | 0.0100% | — | sem_zona |
| 2026-10-25 09:06 | ETH-USDT-SWAP | 2338.7 | 2343.0/2324.5 | 2338.7 | sup 2281.0 (ha 20 candles) | 13.23 | 0.0056% | — | sem_zona |
| 2026-10-25 09:06 | SOL-USDT-SWAP | 101.27 | 101.33/100.61 | 101.27 | sup 98.54 (ha 20 candles) | 0.60500 | 0.0034% | — | sem_zona |
| 2026-10-25 09:06 | XRP-USDT-SWAP | 1.2993 | 1.3018/1.2910 | 1.2993 | sup 1.2539 (ha 20 candles) | 0.00871 | 0.0081% | — | sem_zona |
| 2026-10-25 09:06 | DOGE-USDT-SWAP | 0.07674 | 0.07684/0.07638 | 0.07674 | sup 0.07469 (ha 20 candles) | 0.00048 | 0.0028% | — | sem_zona |
| 2026-10-25 09:06 | ARB-USDT-SWAP | 0.16621 | 0.16631/0.16382 | 0.16621 | sup 0.16640 (ha 13 candles) | 0.00174 | 0.0073% | — | sem_zona |
| 2026-10-25 09:06 | WLD-USDT-SWAP | 0.45320 | 0.45600/0.44250 | 0.45320 | — | 0.00862 | 0.0057% | B/compra@0.45610 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-25 09:06 | SUI-USDT-SWAP | 0.91900 | 0.92060/0.90920 | 0.91900 | sup 0.91080 (ha 20 candles) | 0.00801 | 0.0046% | — | sem_zona |
| 2026-10-25 09:06 | UNI-USDT-SWAP | 6.7560 | 6.7690/6.6620 | 6.7560 | sup 6.5130 (ha 20 candles) | 0.06707 | 0.0006% | — | sem_zona |
| 2026-10-25 09:06 | LINK-USDT-SWAP | 11.40 | 11.42/11.31 | 11.40 | sup 11.23 (ha 20 candles) | 0.07507 | 0.0007% | — | sem_zona |
| 2026-10-25 10:06 | BTC-USDT-SWAP | 80412.7 | 80543.4/80282.6 | 80543.3 | sup 80050.0 (ha 3 candles) | 264.67 | 0.0099% | — | sem_zona |
| 2026-10-25 10:06 | ETH-USDT-SWAP | 2333.9 | 2338.8/2326.5 | 2338.7 | sup 2316.0 (ha 3 candles) | 13.64 | 0.0057% | — | sem_zona |
| 2026-10-25 10:06 | SOL-USDT-SWAP | 100.98 | 101.28/100.64 | 101.27 | sup 100.28 (ha 3 candles) | 0.62429 | 0.0061% | — | sem_zona |
| 2026-10-25 10:06 | XRP-USDT-SWAP | 1.2962 | 1.3000/1.2933 | 1.2993 | sup 1.2884 (ha 3 candles) | 0.00879 | 0.0079% | — | sem_zona |
| 2026-10-25 10:06 | DOGE-USDT-SWAP | 0.07663 | 0.07675/0.07638 | 0.07674 | sup 0.07591 (ha 3 candles) | 0.00049 | 0.0034% | — | sem_zona |
| 2026-10-25 10:06 | ARB-USDT-SWAP | 0.16560 | 0.16634/0.16455 | 0.16621 | sup 0.16304 (ha 3 candles) | 0.00177 | 0.0050% | — | sem_zona |
| 2026-10-25 10:06 | WLD-USDT-SWAP | 0.45000 | 0.45450/0.44540 | 0.45320 | — | 0.00880 | 0.0040% | — | invalidado_setup_B |
| 2026-10-25 10:06 | SUI-USDT-SWAP | 0.91700 | 0.92020/0.91370 | 0.91900 | sup 0.90340 (ha 3 candles) | 0.00817 | -0.0000% | — | sem_zona |
| 2026-10-25 10:06 | UNI-USDT-SWAP | 6.7120 | 6.7620/6.6890 | 6.7560 | sup 6.6380 (ha 3 candles) | 0.06793 | 0.0003% | — | sem_zona |
| 2026-10-25 10:06 | LINK-USDT-SWAP | 11.38 | 11.40/11.33 | 11.40 | sup 11.25 (ha 3 candles) | 0.07679 | -0.0002% | — | sem_zona |
| 2026-10-25 11:07 | BTC-USDT-SWAP | 80344.5 | 80430.5/80199.0 | 80543.3 | sup 80050.0 (ha 4 candles) | 252.71 | 0.0085% | — | sem_zona |
| 2026-10-25 11:07 | ETH-USDT-SWAP | 2333.2 | 2338.7/2325.3 | 2338.7 | sup 2316.0 (ha 4 candles) | 13.22 | 0.0047% | — | sem_zona |
| 2026-10-25 11:07 | SOL-USDT-SWAP | 100.71 | 101.16/100.68 | 101.27 | sup 100.28 (ha 4 candles) | 0.58571 | 0.0074% | — | sem_zona |
| 2026-10-25 11:07 | XRP-USDT-SWAP | 1.2959 | 1.2994/1.2934 | 1.2993 | sup 1.2884 (ha 4 candles) | 0.00851 | 0.0079% | — | sem_zona |
| 2026-10-25 11:07 | DOGE-USDT-SWAP | 0.07672 | 0.07697/0.07652 | 0.07674 | sup 0.07591 (ha 4 candles) | 0.00047 | 0.0018% | — | sem_zona |
| 2026-10-25 11:07 | ARB-USDT-SWAP | 0.16534 | 0.16618/0.16464 | 0.16621 | sup 0.16304 (ha 4 candles) | 0.00169 | 0.0047% | — | sem_zona |
| 2026-10-25 11:07 | WLD-USDT-SWAP | 0.44920 | 0.45220/0.44780 | 0.45320 | — | 0.00867 | 0.0048% | — | sem_zona |
| 2026-10-25 11:07 | SUI-USDT-SWAP | 0.91150 | 0.91920/0.91130 | 0.91900 | sup 0.90340 (ha 4 candles) | 0.00804 | 0.0007% | — | sem_zona |
| 2026-10-25 11:07 | UNI-USDT-SWAP | 6.7220 | 6.7580/6.7000 | 6.7560 | sup 6.6380 (ha 4 candles) | 0.06621 | -0.0010% | — | sem_zona |
| 2026-10-25 11:07 | LINK-USDT-SWAP | 11.37 | 11.41/11.35 | 11.40 | sup 11.25 (ha 4 candles) | 0.07457 | -0.0006% | — | sem_zona |
| 2026-10-25 12:06 | BTC-USDT-SWAP | 80611.9 | 80620.0/80260.0 | 80543.3 | sup 80050.0 (ha 5 candles) | 267.90 | 0.0078% | — | sem_zona |
| 2026-10-25 12:06 | ETH-USDT-SWAP | 2342.7 | 2344.0/2329.4 | 2338.7 | sup 2316.0 (ha 5 candles) | 13.64 | 0.0045% | — | sem_zona |
| 2026-10-25 12:06 | SOL-USDT-SWAP | 101.32 | 101.34/100.56 | 101.27 | sup 100.28 (ha 5 candles) | 0.61214 | 0.0081% | — | sem_zona |
| 2026-10-25 12:06 | XRP-USDT-SWAP | 1.2982 | 1.2994/1.2913 | 1.2993 | sup 1.2884 (ha 5 candles) | 0.00850 | 0.0069% | — | sem_zona |
| 2026-10-25 12:06 | DOGE-USDT-SWAP | 0.07707 | 0.07713/0.07650 | 0.07674 | sup 0.07591 (ha 5 candles) | 0.00048 | 0.0003% | — | sem_zona |
| 2026-10-25 12:06 | ARB-USDT-SWAP | 0.16737 | 0.16747/0.16496 | 0.16621 | sup 0.16304 (ha 5 candles) | 0.00174 | 0.0041% | — | sem_zona |
| 2026-10-25 12:06 | WLD-USDT-SWAP | 0.45190 | 0.45380/0.44610 | 0.45320 | — | 0.00882 | 0.0042% | — | sem_zona |
| 2026-10-25 12:06 | SUI-USDT-SWAP | 0.91390 | 0.91420/0.90720 | 0.91900 | sup 0.90340 (ha 5 candles) | 0.00812 | 0.0021% | — | sem_zona |
| 2026-10-25 12:06 | UNI-USDT-SWAP | 6.7890 | 6.7920/6.7100 | 6.7560 | sup 6.6380 (ha 5 candles) | 0.06893 | -0.0007% | — | sem_zona |
| 2026-10-25 12:06 | LINK-USDT-SWAP | 11.40 | 11.41/11.32 | 11.40 | sup 11.25 (ha 5 candles) | 0.07764 | 0.0009% | — | sem_zona |
