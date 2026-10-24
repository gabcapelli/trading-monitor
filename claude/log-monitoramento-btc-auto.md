# Log de Monitoramento Automatico -- Multi-Par (script gratuito, GitHub Actions)

> Gerado por script Python sem LLM (ver monitor/fetch_and_check.py). Fonte: OKX. Cobre os pares em PAIRS (configuracao no topo do script) -- BTC-USDT-SWAP e os demais adicionados na expansao de 07/09/2026. Leitura e MECANICA (regras objetivas da secao 4 do plano), sem a prosa qualitativa que o Claude gerava -- cole este log numa conversa do Claude se quiser a leitura interpretativa.

| Data/Hora (BRT) | Par | Close 1h | High/Low 1h | Close 4h | Swing 1h ref | ATR 1h | Funding | Zona ativa | Status checklist |
|---|---|---|---|---|---|---|---|---|---|
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
| 2026-10-23 03:06 | BTC-USDT-SWAP | 81807.9 | 81857.0/81558.3 | 81857.0 | res 81535.9 (ha 8 candles) | 401.41 | 0.0082% | A/compra@81535.9 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-23 03:06 | ETH-USDT-SWAP | 2403.2 | 2406.5/2393.3 | 2409.9 | res 2416.7 (ha 3 candles) | 18.15 | 0.0087% | B/compra@2391.7 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-23 03:06 | SOL-USDT-SWAP | 104.41 | 104.56/103.97 | 104.19 | res 104.84 (ha 3 candles) | 0.81429 | 0.0100% | B/compra@103.48 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-23 03:06 | XRP-USDT-SWAP | 1.3256 | 1.3288/1.3183 | 1.3213 | res 1.3985 (ha 35 candles) | 0.01021 | 0.0099% | — | sem_zona |
| 2026-10-23 03:06 | DOGE-USDT-SWAP | 0.07983 | 0.08009/0.07942 | 0.07961 | res 0.07986 (ha 16 candles) | 0.00061 | 0.0088% | — | descartado_rr_baixo_setup_B |
| 2026-10-23 03:06 | ARB-USDT-SWAP | 0.18286 | 0.18469/0.18285 | 0.18516 | — | 0.00292 | -0.0046% | B/compra@0.17662 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-23 03:06 | WLD-USDT-SWAP | 0.55160 | 0.55250/0.54340 | 0.55280 | res 0.56230 (ha 4 candles) | 0.01281 | 0.0081% | — | sem_zona |
| 2026-10-23 03:06 | SUI-USDT-SWAP | 0.99660 | 1.0008/0.99010 | 0.99240 | res 1.0560 (ha 35 candles) | 0.00962 | -0.0026% | — | invalidado_setup_B |
| 2026-10-23 03:06 | UNI-USDT-SWAP | 7.2090 | 7.2370/7.1430 | 7.1740 | — | 0.09193 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-10-23 03:06 | LINK-USDT-SWAP | 12.20 | 12.22/12.13 | 12.19 | res 12.28 (ha 3 candles) | 0.11779 | 0.0100% | A/compra@12.01 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-23 04:43 | BTC-USDT-SWAP | 81857.8 | 81950.7/81715.6 | 81857.0 | res 82010.8 (ha 3 candles) | 359.03 | 0.0081% | A/compra@81535.9 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-23 04:43 | ETH-USDT-SWAP | 2408.8 | 2411.8/2399.5 | 2409.9 | res 2416.7 (ha 4 candles) | 15.90 | 0.0081% | B/compra@2391.7 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-23 04:43 | SOL-USDT-SWAP | 104.67 | 104.72/104.22 | 104.19 | res 104.84 (ha 4 candles) | 0.71000 | 0.0075% | B/compra@103.48 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-23 04:44 | XRP-USDT-SWAP | 1.3291 | 1.3300/1.3220 | 1.3213 | res 1.3985 (ha 36 candles) | 0.00934 | 0.0085% | — | sem_zona |
| 2026-10-23 04:44 | DOGE-USDT-SWAP | 0.08008 | 0.08017/0.07966 | 0.07961 | res 0.07986 (ha 17 candles) | 0.00053 | 0.0100% | — | sem_zona |
| 2026-10-23 04:44 | ARB-USDT-SWAP | 0.18280 | 0.18359/0.18200 | 0.18516 | — | 0.00266 | -0.0031% | — | zona_expirada_setup_B |
| 2026-10-23 04:44 | WLD-USDT-SWAP | 0.55510 | 0.55880/0.54960 | 0.55280 | res 0.56230 (ha 5 candles) | 0.01258 | 0.0086% | — | sem_zona |
| 2026-10-23 04:44 | SUI-USDT-SWAP | 1.0003 | 1.0029/0.99350 | 0.99240 | res 1.0560 (ha 36 candles) | 0.00904 | -0.0019% | B/compra@0.99710 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-23 04:44 | UNI-USDT-SWAP | 7.2510 | 7.2570/7.1560 | 7.1740 | — | 0.08479 | 0.0100% | — | sem_zona |
| 2026-10-23 04:44 | LINK-USDT-SWAP | 12.24 | 12.26/12.17 | 12.19 | res 12.28 (ha 4 candles) | 0.10679 | 0.0100% | A/compra@12.01 (0t/4c) | zona_mapeada_setup_A |
| 2026-10-23 05:06 | BTC-USDT-SWAP | 81546.3 | 81881.8/81520.6 | 81546.3 | — | 362.88 | 0.0075% | A/compra@81535.9 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-23 05:06 | ETH-USDT-SWAP | 2399.9 | 2409.5/2398.8 | 2399.9 | — | 15.68 | 0.0066% | B/compra@2391.7 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-23 05:06 | SOL-USDT-SWAP | 104.26 | 104.72/104.19 | 104.26 | — | 0.69214 | 0.0067% | B/compra@103.48 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-23 05:06 | XRP-USDT-SWAP | 1.3220 | 1.3300/1.3213 | 1.3220 | res 1.3985 (ha 37 candles) | 0.00926 | 0.0087% | — | sem_zona |
| 2026-10-23 05:06 | DOGE-USDT-SWAP | 0.07983 | 0.08011/0.07976 | 0.07983 | — | 0.00053 | 0.0100% | B/venda@0.08009 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-23 05:06 | ARB-USDT-SWAP | 0.18193 | 0.18297/0.18157 | 0.18193 | — | 0.00258 | -0.0018% | — | sem_zona |
| 2026-10-23 05:06 | WLD-USDT-SWAP | 0.54610 | 0.55540/0.54460 | 0.54610 | — | 0.01298 | 0.0078% | B/venda@0.53940 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-23 05:06 | SUI-USDT-SWAP | 0.99400 | 1.0008/0.99330 | 0.99400 | — | 0.00905 | -0.0016% | — | invalidado_setup_B |
| 2026-10-23 05:06 | UNI-USDT-SWAP | 7.2400 | 7.2960/7.2210 | 7.2400 | sup 6.9690 (ha 8 candles) | 0.08407 | 0.0098% | — | sem_zona |
| 2026-10-23 05:06 | LINK-USDT-SWAP | 12.16 | 12.24/12.16 | 12.16 | — | 0.10571 | 0.0100% | A/compra@12.01 (0t/5c) | zona_mapeada_setup_A |
| 2026-10-23 06:06 | BTC-USDT-SWAP | 81722.0 | 81887.0/81514.6 | 81546.3 | — | 362.35 | 0.0074% | A/compra@81535.9 (2t/0c) | zona_mapeada_setup_A |
| 2026-10-23 06:06 | ETH-USDT-SWAP | 2405.2 | 2412.6/2398.5 | 2399.9 | — | 15.82 | 0.0038% | B/compra@2391.7 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-23 06:06 | SOL-USDT-SWAP | 104.59 | 104.85/104.22 | 104.26 | — | 0.68429 | 0.0050% | B/compra@103.48 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-23 06:06 | XRP-USDT-SWAP | 1.3256 | 1.3288/1.3213 | 1.3220 | res 1.3985 (ha 38 candles) | 0.00919 | 0.0095% | — | sem_zona |
| 2026-10-23 06:06 | DOGE-USDT-SWAP | 0.08041 | 0.08064/0.07982 | 0.07983 | — | 0.00054 | 0.0100% | — | invalidado_setup_B |
| 2026-10-23 06:06 | ARB-USDT-SWAP | 0.18161 | 0.18241/0.18104 | 0.18193 | — | 0.00252 | -0.0022% | — | sem_zona |
| 2026-10-23 06:06 | WLD-USDT-SWAP | 0.54810 | 0.55200/0.54510 | 0.54610 | — | 0.01074 | 0.0066% | B/venda@0.53940 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-23 06:06 | SUI-USDT-SWAP | 0.99800 | 1.0010/0.99280 | 0.99400 | — | 0.00912 | -0.0002% | B/compra@1.0002 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-23 06:06 | UNI-USDT-SWAP | 7.2250 | 7.2640/7.2170 | 7.2400 | sup 6.9690 (ha 9 candles) | 0.08221 | 0.0059% | — | sem_zona |
| 2026-10-23 06:06 | LINK-USDT-SWAP | 12.19 | 12.22/12.16 | 12.16 | — | 0.10336 | 0.0100% | A/compra@12.01 (0t/6c) | zona_mapeada_setup_A |
| 2026-10-23 07:06 | BTC-USDT-SWAP | 81640.1 | 81796.4/81509.7 | 81546.3 | — | 363.21 | 0.0086% | — | zona_expirada_setup_A |
| 2026-10-23 07:06 | ETH-USDT-SWAP | 2397.5 | 2407.0/2390.0 | 2399.9 | — | 15.95 | 0.0030% | B/compra@2391.7 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-23 07:06 | SOL-USDT-SWAP | 104.16 | 104.62/103.82 | 104.26 | — | 0.69143 | 0.0039% | B/compra@103.48 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-23 07:06 | XRP-USDT-SWAP | 1.3187 | 1.3263/1.3163 | 1.3220 | res 1.3300 (ha 3 candles) | 0.00916 | 0.0089% | B/compra@1.3176 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-23 07:06 | DOGE-USDT-SWAP | 0.07998 | 0.08049/0.07986 | 0.07983 | — | 0.00054 | 0.0087% | B/venda@0.08025 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-23 07:06 | ARB-USDT-SWAP | 0.18025 | 0.18215/0.17928 | 0.18193 | — | 0.00257 | -0.0017% | — | sem_zona |
| 2026-10-23 07:06 | WLD-USDT-SWAP | 0.53940 | 0.54940/0.53410 | 0.54610 | — | 0.01065 | 0.0083% | — | descartado_rr_baixo_setup_B |
| 2026-10-23 07:06 | SUI-USDT-SWAP | 0.99110 | 0.99850/0.98790 | 0.99400 | — | 0.00926 | 0.0020% | — | invalidado_setup_B |
| 2026-10-23 07:06 | UNI-USDT-SWAP | 7.1720 | 7.2370/7.1390 | 7.2400 | sup 6.9690 (ha 10 candles) | 0.08414 | 0.0043% | — | sem_zona |
| 2026-10-23 07:06 | LINK-USDT-SWAP | 12.09 | 12.20/12.05 | 12.16 | — | 0.10743 | 0.0100% | A/compra@12.01 (0t/7c) | zona_mapeada_setup_A |
| 2026-10-23 08:06 | BTC-USDT-SWAP | 81663.9 | 81820.0/81580.1 | 81546.3 | — | 357.89 | 0.0096% | — | sem_zona |
| 2026-10-23 08:06 | ETH-USDT-SWAP | 2396.7 | 2405.5/2394.0 | 2399.9 | — | 16.00 | 0.0027% | B/compra@2391.7 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-23 08:06 | SOL-USDT-SWAP | 104.02 | 104.44/103.98 | 104.26 | — | 0.67071 | 0.0039% | B/compra@103.48 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-23 08:06 | XRP-USDT-SWAP | 1.3187 | 1.3240/1.3170 | 1.3220 | res 1.3300 (ha 3 candles) | 0.00877 | 0.0092% | B/compra@1.3176 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-23 08:06 | DOGE-USDT-SWAP | 0.07993 | 0.08049/0.07982 | 0.07983 | — | 0.00055 | 0.0074% | — | descartado_rr_baixo_setup_B |
| 2026-10-23 08:06 | ARB-USDT-SWAP | 0.17994 | 0.18162/0.17976 | 0.18193 | — | 0.00253 | -0.0018% | — | sem_zona |
| 2026-10-23 08:06 | WLD-USDT-SWAP | 0.53770 | 0.54220/0.53650 | 0.54610 | — | 0.00988 | 0.0100% | B/venda@0.53360 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-23 08:06 | SUI-USDT-SWAP | 0.98760 | 0.99470/0.98700 | 0.99400 | — | 0.00919 | 0.0049% | B/compra@0.99300 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-23 08:06 | UNI-USDT-SWAP | 7.1650 | 7.2190/7.1540 | 7.2400 | sup 6.9690 (ha 11 candles) | 0.08393 | 0.0051% | — | sem_zona |
| 2026-10-23 08:06 | LINK-USDT-SWAP | 12.05 | 12.12/12.05 | 12.16 | — | 0.10443 | 0.0100% | — | zona_expirada_setup_A |
| 2026-10-23 09:15 | BTC-USDT-SWAP | 81701.1 | 81752.7/81538.5 | 81701.1 | — | 350.22 | 0.0100% | — | sem_zona |
| 2026-10-23 09:15 | ETH-USDT-SWAP | 2401.8 | 2405.0/2390.3 | 2401.8 | — | 15.48 | 0.0032% | — | descartado_rr_baixo_setup_B |
| 2026-10-23 09:15 | SOL-USDT-SWAP | 104.47 | 104.64/103.76 | 104.47 | — | 0.67643 | 0.0036% | B/compra@103.48 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-23 09:15 | XRP-USDT-SWAP | 1.3200 | 1.3232/1.3149 | 1.3200 | res 1.3300 (ha 4 candles) | 0.00858 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-10-23 09:15 | DOGE-USDT-SWAP | 0.08022 | 0.08043/0.07961 | 0.08022 | — | 0.00056 | 0.0065% | B/venda@0.08009 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-23 09:15 | ARB-USDT-SWAP | 0.18035 | 0.18109/0.17911 | 0.18035 | sup 0.17743 (ha 12 candles) | 0.00242 | -0.0016% | — | sem_zona |
| 2026-10-23 09:15 | WLD-USDT-SWAP | 0.54170 | 0.54410/0.53500 | 0.54170 | — | 0.00994 | 0.0100% | — | invalidado_setup_B |
| 2026-10-23 09:15 | SUI-USDT-SWAP | 0.99370 | 0.99570/0.98350 | 0.99370 | — | 0.00944 | 0.0061% | — | descartado_rr_baixo_setup_B |
| 2026-10-23 09:15 | UNI-USDT-SWAP | 7.1920 | 7.2170/7.1290 | 7.1920 | sup 6.9690 (ha 12 candles) | 0.08457 | 0.0058% | — | sem_zona |
| 2026-10-23 09:15 | LINK-USDT-SWAP | 12.09 | 12.11/12.01 | 12.09 | — | 0.10464 | 0.0100% | B/compra@12.15 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-23 10:06 | BTC-USDT-SWAP | 81703.4 | 81800.0/81419.9 | 81701.1 | — | 359.88 | 0.0100% | — | sem_zona |
| 2026-10-23 10:06 | ETH-USDT-SWAP | 2402.4 | 2403.6/2392.4 | 2401.8 | — | 15.28 | 0.0041% | B/compra@2407.5 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-23 10:06 | SOL-USDT-SWAP | 104.41 | 104.72/104.14 | 104.47 | — | 0.67214 | 0.0033% | — | zona_expirada_setup_B |
| 2026-10-23 10:06 | XRP-USDT-SWAP | 1.3169 | 1.3213/1.3151 | 1.3200 | res 1.3300 (ha 5 candles) | 0.00866 | 0.0100% | — | sem_zona |
| 2026-10-23 10:06 | DOGE-USDT-SWAP | 0.08019 | 0.08040/0.07993 | 0.08022 | — | 0.00057 | 0.0052% | B/venda@0.08009 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-23 10:06 | ARB-USDT-SWAP | 0.18039 | 0.18130/0.17926 | 0.18035 | sup 0.17743 (ha 13 candles) | 0.00232 | 0.0001% | — | sem_zona |
| 2026-10-23 10:06 | WLD-USDT-SWAP | 0.53660 | 0.54200/0.53500 | 0.54170 | — | 0.00963 | 0.0100% | B/venda@0.53940 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-23 10:06 | SUI-USDT-SWAP | 0.99650 | 0.99820/0.99020 | 0.99370 | — | 0.00939 | 0.0060% | B/compra@1.0002 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-23 10:06 | UNI-USDT-SWAP | 7.1750 | 7.2150/7.1570 | 7.1920 | sup 6.9690 (ha 13 candles) | 0.08471 | 0.0072% | — | sem_zona |
| 2026-10-23 10:06 | LINK-USDT-SWAP | 12.06 | 12.11/12.04 | 12.09 | — | 0.10364 | 0.0100% | B/compra@12.15 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-23 11:06 | BTC-USDT-SWAP | 81960.8 | 82047.6/81580.0 | 81701.1 | — | 380.39 | 0.0097% | — | sem_zona |
| 2026-10-23 11:06 | ETH-USDT-SWAP | 2413.5 | 2416.7/2395.9 | 2401.8 | — | 16.15 | 0.0047% | — | descartado_rr_baixo_setup_B |
| 2026-10-23 11:06 | SOL-USDT-SWAP | 104.98 | 105.20/104.16 | 104.47 | — | 0.71214 | 0.0033% | B/venda@104.76 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-23 11:06 | XRP-USDT-SWAP | 1.3214 | 1.3223/1.3131 | 1.3200 | res 1.3300 (ha 6 candles) | 0.00901 | 0.0100% | — | sem_zona |
| 2026-10-23 11:06 | DOGE-USDT-SWAP | 0.08037 | 0.08048/0.07989 | 0.08022 | — | 0.00059 | 0.0027% | — | invalidado_setup_B |
| 2026-10-23 11:06 | ARB-USDT-SWAP | 0.18157 | 0.18228/0.17869 | 0.18035 | sup 0.17743 (ha 14 candles) | 0.00246 | -0.0021% | — | sem_zona |
| 2026-10-23 11:06 | WLD-USDT-SWAP | 0.53740 | 0.53790/0.53050 | 0.54170 | — | 0.00967 | 0.0100% | B/venda@0.53940 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-23 11:06 | SUI-USDT-SWAP | 0.99880 | 1.0002/0.98960 | 0.99370 | — | 0.00989 | 0.0036% | — | descartado_rr_baixo_setup_B |
| 2026-10-23 11:06 | UNI-USDT-SWAP | 7.1520 | 7.1840/7.0720 | 7.1920 | sup 6.9690 (ha 14 candles) | 0.08986 | 0.0069% | — | sem_zona |
| 2026-10-23 11:06 | LINK-USDT-SWAP | 12.07 | 12.09/11.98 | 12.09 | — | 0.10729 | 0.0100% | B/compra@12.15 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-23 12:06 | BTC-USDT-SWAP | 81743.0 | 82020.0/81050.0 | 81701.1 | — | 419.09 | 0.0080% | — | sem_zona |
| 2026-10-23 12:06 | ETH-USDT-SWAP | 2407.9 | 2417.0/2377.3 | 2401.8 | — | 18.00 | 0.0048% | — | sem_zona |
| 2026-10-23 12:06 | SOL-USDT-SWAP | 104.74 | 105.20/103.42 | 104.47 | — | 0.79000 | 0.0044% | B/venda@104.76 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-23 12:06 | XRP-USDT-SWAP | 1.3140 | 1.3238/1.3015 | 1.3200 | res 1.3300 (ha 7 candles) | 0.01001 | 0.0100% | B/compra@1.3102 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-23 12:06 | DOGE-USDT-SWAP | 0.07999 | 0.08047/0.07889 | 0.08022 | — | 0.00067 | 0.0041% | B/compra@0.07996 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-23 12:06 | ARB-USDT-SWAP | 0.17939 | 0.18204/0.17568 | 0.18035 | sup 0.17743 (ha 15 candles) | 0.00274 | -0.0009% | — | sem_zona |
| 2026-10-23 12:06 | WLD-USDT-SWAP | 0.53230 | 0.54160/0.52480 | 0.54170 | — | 0.01021 | 0.0100% | B/venda@0.53940 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-23 12:06 | SUI-USDT-SWAP | 0.98990 | 1.0003/0.97440 | 0.99370 | — | 0.01113 | 0.0026% | B/compra@0.99300 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-23 12:06 | UNI-USDT-SWAP | 7.1140 | 7.1940/6.9910 | 7.1920 | sup 6.9690 (ha 15 candles) | 0.10043 | 0.0070% | — | sem_zona |
| 2026-10-23 12:06 | LINK-USDT-SWAP | 12.03 | 12.10/11.85 | 12.09 | — | 0.11986 | 0.0100% | B/compra@12.15 (0t/3c) | zona_mapeada_setup_B |
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
