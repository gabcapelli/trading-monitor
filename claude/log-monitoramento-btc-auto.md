# Log de Monitoramento Automatico -- Multi-Par (script gratuito, GitHub Actions)

> Gerado por script Python sem LLM (ver monitor/fetch_and_check.py). Fonte: OKX. Cobre os pares em PAIRS (configuracao no topo do script) -- BTC-USDT-SWAP e os demais adicionados na expansao de 07/09/2026. Leitura e MECANICA (regras objetivas da secao 4 do plano), sem a prosa qualitativa que o Claude gerava -- cole este log numa conversa do Claude se quiser a leitura interpretativa.

| Data/Hora (BRT) | Par | Close 1h | High/Low 1h | Close 4h | Swing 1h ref | ATR 1h | Funding | Zona ativa | Status checklist |
|---|---|---|---|---|---|---|---|---|---|
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
