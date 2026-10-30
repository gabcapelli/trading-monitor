# Log de Monitoramento Automatico -- Multi-Par (script gratuito, GitHub Actions)

> Gerado por script Python sem LLM (ver monitor/fetch_and_check.py). Fonte: OKX. Cobre os pares em PAIRS (configuracao no topo do script) -- BTC-USDT-SWAP e os demais adicionados na expansao de 07/09/2026. Leitura e MECANICA (regras objetivas da secao 4 do plano), sem a prosa qualitativa que o Claude gerava -- cole este log numa conversa do Claude se quiser a leitura interpretativa.

| Data/Hora (BRT) | Par | Close 1h | High/Low 1h | Close 4h | Swing 1h ref | ATR 1h | Funding | Zona ativa | Status checklist |
|---|---|---|---|---|---|---|---|---|---|
| 2026-10-28 05:06 | BTC-USDT-SWAP | 81058.2 | 81059.9/80845.0 | 81058.2 | — | 271.46 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-10-28 05:06 | ETH-USDT-SWAP | 2360.2 | 2360.5/2351.0 | 2360.2 | — | 11.07 | 0.0098% | B/compra@2358.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-28 05:06 | SOL-USDT-SWAP | 102.28 | 102.29/101.88 | 102.28 | sup 101.00 (ha 6 candles) | 0.50714 | 0.0052% | — | sem_zona |
| 2026-10-28 05:06 | XRP-USDT-SWAP | 1.3286 | 1.3289/1.3232 | 1.3286 | — | 0.00811 | 0.0100% | — | invalidado_setup_B |
| 2026-10-28 05:06 | DOGE-USDT-SWAP | 0.08003 | 0.08005/0.07962 | 0.08003 | res 0.08028 (ha 4 candles) | 0.00047 | 0.0100% | B/compra@0.07929 (2t/3c) | zona_mapeada_setup_B |
| 2026-10-28 05:06 | ARB-USDT-SWAP | 0.16866 | 0.16892/0.16765 | 0.16866 | — | 0.00190 | -0.0026% | — | sem_zona |
| 2026-10-28 05:06 | WLD-USDT-SWAP | 0.43560 | 0.43580/0.43110 | 0.43560 | — | 0.00524 | -0.0128% | — | sem_zona |
| 2026-10-28 05:06 | SUI-USDT-SWAP | 0.93870 | 0.93870/0.93160 | 0.93870 | — | 0.00714 | 0.0087% | — | descartado_rr_baixo_setup_B |
| 2026-10-28 05:06 | UNI-USDT-SWAP | 7.1800 | 7.1850/7.1240 | 7.1800 | res 7.2280 (ha 3 candles) | 0.06436 | -0.0058% | — | descartado_rr_baixo_setup_A |
| 2026-10-28 05:06 | LINK-USDT-SWAP | 11.78 | 11.78/11.70 | 11.78 | — | 0.08650 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-10-28 06:06 | BTC-USDT-SWAP | 81450.9 | 81786.9/81055.2 | 81058.2 | — | 303.80 | 0.0100% | — | sem_zona |
| 2026-10-28 06:06 | ETH-USDT-SWAP | 2371.2 | 2387.3/2360.1 | 2360.2 | — | 12.50 | 0.0097% | B/compra@2358.0 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-28 06:06 | SOL-USDT-SWAP | 102.61 | 103.66/102.21 | 102.28 | sup 101.00 (ha 7 candles) | 0.57286 | 0.0071% | B/venda@102.69 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-28 06:06 | XRP-USDT-SWAP | 1.3311 | 1.3396/1.3283 | 1.3286 | — | 0.00820 | 0.0100% | B/venda@1.3300 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-28 06:06 | DOGE-USDT-SWAP | 0.08015 | 0.08044/0.07995 | 0.08003 | res 0.08028 (ha 5 candles) | 0.00048 | 0.0100% | B/compra@0.07929 (2t/4c) | zona_mapeada_setup_B |
| 2026-10-28 06:06 | ARB-USDT-SWAP | 0.16905 | 0.17052/0.16821 | 0.16866 | — | 0.00197 | -0.0070% | — | sem_zona |
| 2026-10-28 06:06 | WLD-USDT-SWAP | 0.43630 | 0.44220/0.43440 | 0.43560 | — | 0.00542 | -0.0121% | — | sem_zona |
| 2026-10-28 06:06 | SUI-USDT-SWAP | 0.93990 | 0.94790/0.93710 | 0.93870 | — | 0.00739 | 0.0082% | B/compra@0.93640 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-28 06:06 | UNI-USDT-SWAP | 7.1760 | 7.2720/7.1750 | 7.1800 | res 7.2280 (ha 4 candles) | 0.06871 | -0.0010% | — | sem_zona |
| 2026-10-28 06:06 | LINK-USDT-SWAP | 11.81 | 11.89/11.76 | 11.78 | — | 0.09093 | 0.0100% | B/compra@11.83 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-28 07:06 | BTC-USDT-SWAP | 81519.3 | 81525.2/81320.5 | 81058.2 | — | 301.72 | 0.0100% | — | sem_zona |
| 2026-10-28 07:06 | ETH-USDT-SWAP | 2372.6 | 2372.8/2365.0 | 2360.2 | — | 12.16 | 0.0100% | B/compra@2358.0 (1t/1c) | zona_mapeada_setup_B |
| 2026-10-28 07:06 | SOL-USDT-SWAP | 102.92 | 102.94/102.42 | 102.28 | sup 101.00 (ha 8 candles) | 0.57786 | 0.0096% | — | invalidado_setup_B |
| 2026-10-28 07:06 | XRP-USDT-SWAP | 1.3314 | 1.3335/1.3273 | 1.3286 | — | 0.00821 | 0.0100% | B/venda@1.3300 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-28 07:06 | DOGE-USDT-SWAP | 0.08048 | 0.08061/0.08003 | 0.08003 | res 0.08028 (ha 6 candles) | 0.00050 | 0.0100% | B/compra@0.07929 (2t/5c) | zona_mapeada_setup_B |
| 2026-10-28 07:06 | ARB-USDT-SWAP | 0.16978 | 0.16995/0.16851 | 0.16866 | — | 0.00196 | -0.0051% | B/compra@0.16922 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-28 07:06 | WLD-USDT-SWAP | 0.43820 | 0.43920/0.43440 | 0.43560 | — | 0.00538 | -0.0112% | — | sem_zona |
| 2026-10-28 07:06 | SUI-USDT-SWAP | 0.94480 | 0.94530/0.93840 | 0.93870 | — | 0.00748 | 0.0058% | B/compra@0.93640 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-28 07:06 | UNI-USDT-SWAP | 7.1990 | 7.1990/7.1490 | 7.1800 | res 7.2280 (ha 5 candles) | 0.06871 | 0.0029% | — | sem_zona |
| 2026-10-28 07:06 | LINK-USDT-SWAP | 11.87 | 11.88/11.78 | 11.78 | — | 0.09257 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-10-28 08:06 | BTC-USDT-SWAP | 81463.9 | 81569.0/81413.7 | 81058.2 | — | 299.13 | 0.0100% | — | sem_zona |
| 2026-10-28 08:06 | ETH-USDT-SWAP | 2367.9 | 2374.4/2367.1 | 2360.2 | — | 12.05 | 0.0100% | B/compra@2358.0 (1t/2c) | zona_mapeada_setup_B |
| 2026-10-28 08:06 | SOL-USDT-SWAP | 102.90 | 103.19/102.86 | 102.28 | sup 101.00 (ha 9 candles) | 0.57286 | 0.0100% | — | sem_zona |
| 2026-10-28 08:06 | XRP-USDT-SWAP | 1.3282 | 1.3324/1.3280 | 1.3286 | — | 0.00802 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-10-28 08:06 | DOGE-USDT-SWAP | 0.08025 | 0.08058/0.08010 | 0.08003 | res 0.08028 (ha 7 candles) | 0.00051 | 0.0100% | B/compra@0.07929 (2t/6c) | zona_mapeada_setup_B |
| 2026-10-28 08:06 | ARB-USDT-SWAP | 0.16905 | 0.17026/0.16891 | 0.16866 | — | 0.00196 | -0.0052% | B/compra@0.16922 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-28 08:06 | WLD-USDT-SWAP | 0.43800 | 0.43940/0.43600 | 0.43560 | — | 0.00539 | -0.0085% | — | sem_zona |
| 2026-10-28 08:06 | SUI-USDT-SWAP | 0.94270 | 0.94560/0.94100 | 0.93870 | — | 0.00746 | 0.0043% | B/compra@0.93640 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-28 08:06 | UNI-USDT-SWAP | 7.1780 | 7.2080/7.1560 | 7.1800 | res 7.2280 (ha 6 candles) | 0.06986 | 0.0064% | — | sem_zona |
| 2026-10-28 08:06 | LINK-USDT-SWAP | 11.82 | 11.88/11.79 | 11.78 | — | 0.09514 | 0.0100% | B/compra@11.77 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-28 09:06 | BTC-USDT-SWAP | 81293.9 | 81464.0/81267.8 | 81293.9 | — | 265.84 | 0.0100% | B/compra@81166.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-28 09:06 | ETH-USDT-SWAP | 2360.6 | 2367.9/2358.0 | 2360.6 | — | 10.96 | 0.0100% | B/compra@2358.0 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-28 09:06 | SOL-USDT-SWAP | 102.68 | 102.94/102.54 | 102.68 | sup 101.00 (ha 10 candles) | 0.53143 | 0.0100% | — | sem_zona |
| 2026-10-28 09:06 | XRP-USDT-SWAP | 1.3244 | 1.3282/1.3243 | 1.3244 | — | 0.00736 | 0.0100% | B/venda@1.3212 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-28 09:06 | DOGE-USDT-SWAP | 0.08012 | 0.08035/0.07999 | 0.08012 | res 0.08028 (ha 8 candles) | 0.00049 | 0.0100% | B/compra@0.07929 (2t/7c) | zona_mapeada_setup_B |
| 2026-10-28 09:06 | ARB-USDT-SWAP | 0.16820 | 0.16904/0.16756 | 0.16820 | — | 0.00181 | -0.0039% | — | invalidado_setup_B |
| 2026-10-28 09:06 | WLD-USDT-SWAP | 0.43590 | 0.43840/0.43360 | 0.43590 | sup 0.43110 (ha 4 candles) | 0.00485 | -0.0056% | — | sem_zona |
| 2026-10-28 09:06 | SUI-USDT-SWAP | 0.93920 | 0.94270/0.93870 | 0.93920 | — | 0.00671 | 0.0031% | B/compra@0.93640 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-28 09:06 | UNI-USDT-SWAP | 7.1400 | 7.1900/7.1350 | 7.1400 | res 7.2720 (ha 3 candles) | 0.06543 | 0.0070% | B/compra@7.0920 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-28 09:06 | LINK-USDT-SWAP | 11.77 | 11.82/11.75 | 11.77 | — | 0.08900 | 0.0100% | B/compra@11.77 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-28 10:06 | BTC-USDT-SWAP | 80700.0 | 81305.6/80652.9 | 81293.9 | — | 296.36 | 0.0091% | — | invalidado_setup_B |
| 2026-10-28 10:06 | ETH-USDT-SWAP | 2338.8 | 2361.5/2334.0 | 2360.6 | — | 12.29 | 0.0094% | — | invalidado_setup_B |
| 2026-10-28 10:06 | SOL-USDT-SWAP | 101.50 | 102.72/101.34 | 102.68 | sup 101.00 (ha 11 candles) | 0.60643 | 0.0100% | — | sem_zona |
| 2026-10-28 10:06 | XRP-USDT-SWAP | 1.3160 | 1.3248/1.3126 | 1.3244 | — | 0.00787 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-10-28 10:06 | DOGE-USDT-SWAP | 0.07925 | 0.08012/0.07912 | 0.08012 | res 0.08061 (ha 3 candles) | 0.00054 | 0.0100% | — | zona_expirada_setup_B |
| 2026-10-28 10:06 | ARB-USDT-SWAP | 0.16447 | 0.16822/0.16419 | 0.16820 | — | 0.00196 | -0.0064% | B/compra@0.16304 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-28 10:06 | WLD-USDT-SWAP | 0.42800 | 0.43610/0.42500 | 0.43590 | sup 0.43110 (ha 5 candles) | 0.00536 | -0.0030% | A/venda@0.43110 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-28 10:06 | SUI-USDT-SWAP | 0.92420 | 0.93930/0.92260 | 0.93920 | — | 0.00755 | 0.0031% | — | invalidado_setup_B |
| 2026-10-28 10:06 | UNI-USDT-SWAP | 7.0230 | 7.1400/7.0010 | 7.1400 | res 7.2720 (ha 4 candles) | 0.07243 | 0.0077% | — | invalidado_setup_B |
| 2026-10-28 10:06 | LINK-USDT-SWAP | 11.60 | 11.77/11.57 | 11.77 | — | 0.09943 | 0.0100% | — | invalidado_setup_B |
| 2026-10-28 11:06 | BTC-USDT-SWAP | 80702.1 | 80888.0/80350.0 | 81293.9 | — | 316.98 | 0.0063% | B/venda@80822.6 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-28 11:06 | ETH-USDT-SWAP | 2335.3 | 2345.9/2321.3 | 2360.6 | — | 13.49 | 0.0078% | B/venda@2344.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-28 11:06 | SOL-USDT-SWAP | 101.11 | 101.72/100.67 | 102.68 | sup 101.00 (ha 12 candles) | 0.65643 | 0.0100% | — | sem_zona |
| 2026-10-28 11:06 | XRP-USDT-SWAP | 1.3189 | 1.3223/1.3132 | 1.3244 | — | 0.00789 | 0.0100% | B/venda@1.3153 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-28 11:06 | DOGE-USDT-SWAP | 0.07902 | 0.07939/0.07857 | 0.08012 | res 0.08061 (ha 4 candles) | 0.00056 | 0.0100% | — | sem_zona |
| 2026-10-28 11:06 | ARB-USDT-SWAP | 0.16485 | 0.16595/0.16373 | 0.16820 | — | 0.00200 | -0.0095% | B/compra@0.16304 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-28 11:06 | WLD-USDT-SWAP | 0.42880 | 0.43290/0.42630 | 0.43590 | sup 0.43110 (ha 6 candles) | 0.00549 | -0.0035% | A/venda@0.43110 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-28 11:06 | SUI-USDT-SWAP | 0.92310 | 0.92960/0.91840 | 0.93920 | — | 0.00786 | -0.0000% | — | sem_zona |
| 2026-10-28 11:06 | UNI-USDT-SWAP | 7.0210 | 7.0670/6.9830 | 7.1400 | res 7.2720 (ha 5 candles) | 0.07507 | 0.0067% | B/compra@6.9810 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-28 11:06 | LINK-USDT-SWAP | 11.55 | 11.70/11.51 | 11.77 | — | 0.10836 | 0.0100% | B/venda@11.62 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-28 12:06 | BTC-USDT-SWAP | 80570.2 | 80839.2/80420.0 | 81293.9 | — | 330.69 | 0.0061% | — | descartado_rr_baixo_setup_B |
| 2026-10-28 12:06 | ETH-USDT-SWAP | 2332.5 | 2340.8/2325.3 | 2360.6 | — | 14.17 | 0.0072% | B/venda@2344.0 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-28 12:06 | SOL-USDT-SWAP | 100.88 | 101.28/100.39 | 102.68 | sup 101.00 (ha 13 candles) | 0.70571 | 0.0087% | A/venda@101.00 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-28 12:06 | XRP-USDT-SWAP | 1.3128 | 1.3212/1.3090 | 1.3244 | — | 0.00840 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-10-28 12:06 | DOGE-USDT-SWAP | 0.07916 | 0.07924/0.07854 | 0.08012 | res 0.08061 (ha 5 candles) | 0.00058 | 0.0100% | — | sem_zona |
| 2026-10-28 12:06 | ARB-USDT-SWAP | 0.16529 | 0.16530/0.16325 | 0.16820 | — | 0.00199 | -0.0087% | — | descartado_rr_baixo_setup_B |
| 2026-10-28 12:06 | WLD-USDT-SWAP | 0.42930 | 0.42990/0.42510 | 0.43590 | sup 0.43110 (ha 7 candles) | 0.00558 | -0.0006% | A/venda@0.43110 (2t/0c) | zona_mapeada_setup_A |
| 2026-10-28 12:06 | SUI-USDT-SWAP | 0.92340 | 0.92570/0.91640 | 0.93920 | — | 0.00829 | -0.0011% | — | sem_zona |
| 2026-10-28 12:06 | UNI-USDT-SWAP | 7.0340 | 7.0460/6.9660 | 7.1400 | res 7.2720 (ha 6 candles) | 0.07643 | 0.0051% | — | descartado_rr_baixo_setup_B |
| 2026-10-28 12:06 | LINK-USDT-SWAP | 11.55 | 11.59/11.47 | 11.77 | — | 0.11321 | 0.0100% | B/venda@11.62 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-28 13:06 | BTC-USDT-SWAP | 80520.1 | 80735.6/80465.5 | 80520.1 | — | 322.46 | 0.0067% | B/compra@80621.4 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-28 13:06 | ETH-USDT-SWAP | 2334.0 | 2339.9/2329.7 | 2334.0 | — | 13.56 | 0.0072% | B/venda@2344.0 (1t/1c) | zona_mapeada_setup_B |
| 2026-10-28 13:06 | SOL-USDT-SWAP | 101.02 | 101.25/100.81 | 101.02 | sup 101.00 (ha 14 candles) | 0.68357 | 0.0086% | A/venda@101.00 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-28 13:06 | XRP-USDT-SWAP | 1.3114 | 1.3160/1.3101 | 1.3114 | res 1.3396 (ha 7 candles) | 0.00783 | 0.0100% | B/compra@1.3102 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-28 13:06 | DOGE-USDT-SWAP | 0.07929 | 0.07943/0.07911 | 0.07929 | res 0.08061 (ha 6 candles) | 0.00056 | 0.0100% | — | sem_zona |
| 2026-10-28 13:06 | ARB-USDT-SWAP | 0.16779 | 0.16788/0.16530 | 0.16779 | — | 0.00202 | -0.0030% | B/compra@0.16922 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-28 13:06 | WLD-USDT-SWAP | 0.43260 | 0.43520/0.42940 | 0.43260 | sup 0.42500 (ha 3 candles) | 0.00567 | 0.0046% | — | invalidado_setup_A |
| 2026-10-28 13:06 | SUI-USDT-SWAP | 0.92710 | 0.92880/0.92340 | 0.92710 | — | 0.00794 | -0.0015% | B/venda@0.93080 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-28 13:06 | UNI-USDT-SWAP | 7.0860 | 7.0880/7.0350 | 7.0860 | res 7.2720 (ha 7 candles) | 0.07414 | 0.0057% | B/compra@7.0920 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-28 13:06 | LINK-USDT-SWAP | 11.56 | 11.59/11.53 | 11.56 | — | 0.10993 | 0.0100% | B/venda@11.62 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-28 14:06 | BTC-USDT-SWAP | 80588.1 | 80721.2/80361.3 | 80520.1 | — | 327.19 | 0.0075% | — | descartado_rr_baixo_setup_B |
| 2026-10-28 14:06 | ETH-USDT-SWAP | 2334.5 | 2340.8/2325.7 | 2334.0 | — | 13.41 | 0.0076% | B/venda@2344.0 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-28 14:06 | SOL-USDT-SWAP | 101.17 | 101.38/100.66 | 101.02 | sup 101.00 (ha 15 candles) | 0.69714 | 0.0090% | A/venda@101.00 (2t/0c) | zona_mapeada_setup_A |
| 2026-10-28 14:06 | XRP-USDT-SWAP | 1.3141 | 1.3167/1.3073 | 1.3114 | res 1.3396 (ha 8 candles) | 0.00770 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-10-28 14:06 | DOGE-USDT-SWAP | 0.07909 | 0.07935/0.07876 | 0.07929 | res 0.08061 (ha 7 candles) | 0.00057 | 0.0100% | — | sem_zona |
| 2026-10-28 14:06 | ARB-USDT-SWAP | 0.16559 | 0.16778/0.16444 | 0.16779 | — | 0.00214 | -0.0031% | B/compra@0.16922 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-28 14:06 | WLD-USDT-SWAP | 0.42460 | 0.43330/0.41700 | 0.43260 | sup 0.42500 (ha 4 candles) | 0.00655 | 0.0084% | A/venda@0.42500 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-28 14:06 | SUI-USDT-SWAP | 0.92460 | 0.92810/0.91830 | 0.92710 | — | 0.00804 | -0.0019% | B/venda@0.93080 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-28 14:06 | UNI-USDT-SWAP | 7.0800 | 7.1050/7.0270 | 7.0860 | res 7.2720 (ha 8 candles) | 0.07486 | 0.0069% | B/compra@7.0920 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-28 14:06 | LINK-USDT-SWAP | 11.52 | 11.58/11.46 | 11.56 | — | 0.10871 | 0.0100% | B/venda@11.62 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-28 15:06 | BTC-USDT-SWAP | 80824.2 | 80948.0/80432.8 | 80520.1 | — | 341.06 | 0.0089% | B/venda@81008.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-28 15:06 | ETH-USDT-SWAP | 2344.0 | 2347.6/2330.1 | 2334.0 | — | 13.78 | 0.0080% | — | zona_expirada_setup_B |
| 2026-10-28 15:06 | SOL-USDT-SWAP | 101.62 | 101.81/100.86 | 101.02 | sup 100.39 (ha 3 candles) | 0.70286 | 0.0099% | — | invalidado_setup_A |
| 2026-10-28 15:06 | XRP-USDT-SWAP | 1.3167 | 1.3206/1.3111 | 1.3114 | res 1.3396 (ha 9 candles) | 0.00760 | 0.0100% | — | sem_zona |
| 2026-10-28 15:06 | DOGE-USDT-SWAP | 0.07920 | 0.07939/0.07875 | 0.07929 | res 0.08061 (ha 8 candles) | 0.00054 | 0.0100% | — | sem_zona |
| 2026-10-28 15:06 | ARB-USDT-SWAP | 0.16630 | 0.16711/0.16465 | 0.16779 | — | 0.00217 | -0.0032% | B/compra@0.16922 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-28 15:06 | WLD-USDT-SWAP | 0.42470 | 0.42760/0.42160 | 0.43260 | sup 0.42500 (ha 5 candles) | 0.00652 | 0.0100% | A/venda@0.42500 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-28 15:06 | SUI-USDT-SWAP | 0.92470 | 0.92880/0.91940 | 0.92710 | — | 0.00812 | -0.0014% | B/venda@0.93080 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-28 15:06 | UNI-USDT-SWAP | 7.0750 | 7.0900/7.0280 | 7.0860 | res 7.2720 (ha 9 candles) | 0.07586 | 0.0084% | B/compra@7.0920 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-28 15:06 | LINK-USDT-SWAP | 11.54 | 11.58/11.46 | 11.56 | — | 0.10557 | 0.0100% | B/venda@11.62 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-28 16:06 | BTC-USDT-SWAP | 80985.0 | 81299.0/80646.2 | 80520.1 | — | 371.74 | 0.0100% | B/venda@81008.0 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-28 16:06 | ETH-USDT-SWAP | 2353.9 | 2368.7/2338.2 | 2334.0 | — | 15.33 | 0.0100% | B/compra@2350.1 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-28 16:06 | SOL-USDT-SWAP | 102.10 | 102.53/101.12 | 101.02 | sup 100.39 (ha 4 candles) | 0.76500 | 0.0100% | — | sem_zona |
| 2026-10-28 16:06 | XRP-USDT-SWAP | 1.3264 | 1.3319/1.3139 | 1.3114 | res 1.3396 (ha 10 candles) | 0.00826 | 0.0100% | — | sem_zona |
| 2026-10-28 16:06 | DOGE-USDT-SWAP | 0.07953 | 0.07980/0.07887 | 0.07929 | res 0.08061 (ha 9 candles) | 0.00058 | 0.0100% | B/compra@0.07996 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-28 16:06 | ARB-USDT-SWAP | 0.17159 | 0.17215/0.16579 | 0.16779 | — | 0.00246 | 0.0018% | — | descartado_rr_baixo_setup_B |
| 2026-10-28 16:06 | WLD-USDT-SWAP | 0.43680 | 0.43930/0.42380 | 0.43260 | sup 0.42500 (ha 6 candles) | 0.00724 | 0.0100% | — | invalidado_setup_A |
| 2026-10-28 16:06 | SUI-USDT-SWAP | 0.93840 | 0.94230/0.92290 | 0.92710 | — | 0.00905 | -0.0017% | — | invalidado_setup_B |
| 2026-10-28 16:06 | UNI-USDT-SWAP | 7.2050 | 7.2210/7.0550 | 7.0860 | res 7.2720 (ha 10 candles) | 0.07857 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-10-28 16:06 | LINK-USDT-SWAP | 11.68 | 11.76/11.52 | 11.56 | — | 0.11721 | 0.0100% | — | invalidado_setup_B |
| 2026-10-28 17:06 | BTC-USDT-SWAP | 81553.6 | 81599.9/80943.8 | 81553.6 | — | 410.61 | 0.0100% | — | invalidado_setup_B |
| 2026-10-28 17:06 | ETH-USDT-SWAP | 2370.6 | 2371.0/2352.0 | 2370.6 | — | 16.32 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-10-28 17:06 | SOL-USDT-SWAP | 103.00 | 103.01/101.89 | 103.00 | sup 100.39 (ha 5 candles) | 0.82143 | 0.0100% | B/venda@102.69 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-28 17:06 | XRP-USDT-SWAP | 1.3351 | 1.3353/1.3232 | 1.3351 | res 1.3396 (ha 11 candles) | 0.00882 | 0.0100% | — | sem_zona |
| 2026-10-28 17:06 | DOGE-USDT-SWAP | 0.08018 | 0.08019/0.07946 | 0.08018 | res 0.08061 (ha 10 candles) | 0.00061 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-10-28 17:06 | ARB-USDT-SWAP | 0.17451 | 0.17461/0.17127 | 0.17451 | — | 0.00258 | 0.0073% | B/venda@0.17358 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-28 17:06 | WLD-USDT-SWAP | 0.44250 | 0.44380/0.43420 | 0.44250 | sup 0.41700 (ha 3 candles) | 0.00759 | 0.0100% | — | sem_zona |
| 2026-10-28 17:06 | SUI-USDT-SWAP | 0.95090 | 0.95110/0.93660 | 0.95090 | — | 0.00967 | -0.0012% | B/compra@0.95220 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-28 17:06 | UNI-USDT-SWAP | 7.2410 | 7.2430/7.1710 | 7.2410 | res 7.2720 (ha 11 candles) | 0.08021 | 0.0100% | — | sem_zona |
| 2026-10-28 17:06 | LINK-USDT-SWAP | 11.86 | 11.86/11.67 | 11.86 | — | 0.12629 | 0.0100% | B/compra@11.83 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-28 18:06 | BTC-USDT-SWAP | 81303.9 | 81768.0/80960.0 | 81553.6 | — | 455.34 | 0.0100% | B/compra@81166.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-28 18:06 | ETH-USDT-SWAP | 2360.0 | 2391.2/2347.0 | 2370.6 | — | 18.97 | 0.0100% | B/compra@2358.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-28 18:06 | SOL-USDT-SWAP | 102.49 | 103.83/101.83 | 103.00 | sup 100.39 (ha 6 candles) | 0.93357 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-10-28 18:06 | XRP-USDT-SWAP | 1.3310 | 1.3438/1.3248 | 1.3351 | res 1.3396 (ha 12 candles) | 0.00992 | 0.0100% | — | sem_zona |
| 2026-10-28 18:06 | DOGE-USDT-SWAP | 0.08024 | 0.08087/0.07961 | 0.08018 | res 0.08061 (ha 11 candles) | 0.00067 | 0.0100% | — | sem_zona |
| 2026-10-28 18:06 | ARB-USDT-SWAP | 0.17565 | 0.17855/0.17330 | 0.17451 | — | 0.00282 | 0.0100% | — | invalidado_setup_B |
| 2026-10-28 18:06 | WLD-USDT-SWAP | 0.44190 | 0.45280/0.43450 | 0.44250 | sup 0.41700 (ha 4 candles) | 0.00854 | 0.0100% | — | sem_zona |
| 2026-10-28 18:06 | SUI-USDT-SWAP | 0.94880 | 0.96560/0.93780 | 0.95090 | — | 0.01121 | -0.0009% | — | invalidado_setup_B |
| 2026-10-28 18:06 | UNI-USDT-SWAP | 7.2440 | 7.3390/7.1510 | 7.2410 | res 7.2720 (ha 12 candles) | 0.08843 | 0.0100% | — | sem_zona |
| 2026-10-28 18:06 | LINK-USDT-SWAP | 11.83 | 12.00/11.71 | 11.86 | — | 0.14171 | 0.0100% | B/compra@11.83 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-28 19:06 | BTC-USDT-SWAP | 81328.1 | 81428.6/81107.9 | 81553.6 | — | 462.90 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-10-28 19:06 | ETH-USDT-SWAP | 2363.7 | 2370.8/2354.1 | 2370.6 | — | 19.48 | 0.0100% | B/compra@2358.0 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-28 19:06 | SOL-USDT-SWAP | 102.71 | 102.94/102.13 | 103.00 | sup 100.39 (ha 7 candles) | 0.96214 | 0.0100% | — | sem_zona |
| 2026-10-28 19:06 | XRP-USDT-SWAP | 1.3319 | 1.3338/1.3254 | 1.3351 | res 1.3396 (ha 13 candles) | 0.01011 | 0.0100% | — | sem_zona |
| 2026-10-28 19:06 | DOGE-USDT-SWAP | 0.08022 | 0.08047/0.07989 | 0.08018 | res 0.08061 (ha 12 candles) | 0.00068 | 0.0100% | — | sem_zona |
| 2026-10-28 19:06 | ARB-USDT-SWAP | 0.17559 | 0.17785/0.17425 | 0.17451 | — | 0.00299 | 0.0100% | B/compra@0.17743 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-28 19:06 | WLD-USDT-SWAP | 0.44070 | 0.44540/0.43690 | 0.44250 | sup 0.41700 (ha 5 candles) | 0.00881 | 0.0100% | — | sem_zona |
| 2026-10-28 19:06 | SUI-USDT-SWAP | 0.95070 | 0.95460/0.94310 | 0.95090 | — | 0.01152 | 0.0005% | B/compra@0.95790 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-28 19:06 | UNI-USDT-SWAP | 7.3020 | 7.3530/7.2270 | 7.2410 | res 7.2720 (ha 13 candles) | 0.09307 | 0.0100% | A/compra@7.2720 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-28 19:06 | LINK-USDT-SWAP | 11.87 | 11.90/11.77 | 11.86 | — | 0.14571 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-10-28 20:06 | BTC-USDT-SWAP | 81242.6 | 81407.7/81101.9 | 81553.6 | — | 432.48 | 0.0100% | B/compra@80961.3 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-28 20:06 | ETH-USDT-SWAP | 2359.2 | 2366.7/2354.2 | 2370.6 | — | 18.44 | 0.0100% | B/compra@2358.0 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-28 20:06 | SOL-USDT-SWAP | 102.48 | 102.76/102.20 | 103.00 | sup 100.39 (ha 8 candles) | 0.89857 | 0.0100% | — | sem_zona |
| 2026-10-28 20:06 | XRP-USDT-SWAP | 1.3269 | 1.3318/1.3247 | 1.3351 | res 1.3396 (ha 14 candles) | 0.00982 | 0.0100% | — | sem_zona |
| 2026-10-28 20:06 | DOGE-USDT-SWAP | 0.07980 | 0.08023/0.07973 | 0.08018 | res 0.08061 (ha 13 candles) | 0.00068 | 0.0100% | — | sem_zona |
| 2026-10-28 20:06 | ARB-USDT-SWAP | 0.17312 | 0.17557/0.17292 | 0.17451 | — | 0.00301 | 0.0100% | B/compra@0.17743 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-28 20:06 | WLD-USDT-SWAP | 0.43780 | 0.44070/0.43690 | 0.44250 | sup 0.41700 (ha 6 candles) | 0.00853 | 0.0100% | — | sem_zona |
| 2026-10-28 20:06 | SUI-USDT-SWAP | 0.94450 | 0.95060/0.94340 | 0.95090 | — | 0.01127 | 0.0020% | B/compra@0.95790 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-28 20:06 | UNI-USDT-SWAP | 7.2430 | 7.3010/7.2320 | 7.2410 | res 7.2720 (ha 14 candles) | 0.09114 | 0.0100% | — | invalidado_setup_A |
| 2026-10-28 20:06 | LINK-USDT-SWAP | 11.81 | 11.87/11.79 | 11.86 | — | 0.14200 | 0.0100% | B/compra@11.77 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-28 21:06 | BTC-USDT-SWAP | 81309.9 | 81333.0/81121.0 | 81309.9 | res 81768.0 (ha 3 candles) | 433.00 | 0.0100% | B/compra@80961.3 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-28 21:06 | ETH-USDT-SWAP | 2358.6 | 2361.5/2353.6 | 2358.6 | — | 18.44 | 0.0098% | — | zona_expirada_setup_B |
| 2026-10-28 21:06 | SOL-USDT-SWAP | 102.37 | 102.51/102.22 | 102.37 | sup 100.39 (ha 9 candles) | 0.88214 | 0.0100% | — | sem_zona |
| 2026-10-28 21:06 | XRP-USDT-SWAP | 1.3253 | 1.3283/1.3240 | 1.3253 | res 1.3438 (ha 3 candles) | 0.00969 | 0.0100% | — | sem_zona |
| 2026-10-28 21:06 | DOGE-USDT-SWAP | 0.07972 | 0.07990/0.07956 | 0.07972 | res 0.08087 (ha 3 candles) | 0.00066 | 0.0100% | B/compra@0.07929 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-28 21:06 | ARB-USDT-SWAP | 0.17209 | 0.17312/0.17140 | 0.17209 | — | 0.00303 | 0.0100% | B/compra@0.17743 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-28 21:06 | WLD-USDT-SWAP | 0.43760 | 0.43890/0.43510 | 0.43760 | sup 0.41700 (ha 7 candles) | 0.00846 | 0.0100% | — | sem_zona |
| 2026-10-28 21:06 | SUI-USDT-SWAP | 0.94270 | 0.94520/0.94010 | 0.94270 | — | 0.01114 | 0.0036% | B/compra@0.95790 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-28 21:06 | UNI-USDT-SWAP | 7.2470 | 7.2510/7.2020 | 7.2470 | res 7.2720 (ha 15 candles) | 0.09107 | 0.0100% | — | sem_zona |
| 2026-10-28 21:06 | LINK-USDT-SWAP | 11.81 | 11.83/11.77 | 11.81 | — | 0.13929 | 0.0100% | B/compra@11.77 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-28 22:06 | BTC-USDT-SWAP | 81062.4 | 81349.6/81062.4 | 81309.9 | res 81768.0 (ha 4 candles) | 442.42 | 0.0100% | B/compra@80961.3 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-28 22:06 | ETH-USDT-SWAP | 2353.6 | 2360.5/2353.2 | 2358.6 | — | 18.45 | 0.0089% | B/compra@2350.1 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-28 22:06 | SOL-USDT-SWAP | 101.80 | 102.50/101.78 | 102.37 | sup 100.39 (ha 10 candles) | 0.91000 | 0.0100% | — | sem_zona |
| 2026-10-28 22:06 | XRP-USDT-SWAP | 1.3205 | 1.3264/1.3204 | 1.3253 | res 1.3438 (ha 4 candles) | 0.00980 | 0.0100% | — | sem_zona |
| 2026-10-28 22:06 | DOGE-USDT-SWAP | 0.07944 | 0.07987/0.07944 | 0.07972 | res 0.08087 (ha 4 candles) | 0.00066 | 0.0100% | B/compra@0.07929 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-28 22:06 | ARB-USDT-SWAP | 0.17098 | 0.17283/0.17096 | 0.17209 | — | 0.00307 | 0.0100% | B/compra@0.17743 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-28 22:06 | WLD-USDT-SWAP | 0.43370 | 0.43880/0.43350 | 0.43760 | sup 0.41700 (ha 8 candles) | 0.00859 | 0.0100% | — | sem_zona |
| 2026-10-28 22:06 | SUI-USDT-SWAP | 0.93830 | 0.94630/0.93830 | 0.94270 | — | 0.01139 | 0.0036% | B/compra@0.95790 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-28 22:06 | UNI-USDT-SWAP | 7.2290 | 7.3010/7.2270 | 7.2470 | res 7.3530 (ha 3 candles) | 0.09264 | 0.0100% | — | sem_zona |
| 2026-10-28 22:06 | LINK-USDT-SWAP | 11.75 | 11.84/11.75 | 11.81 | — | 0.13914 | 0.0100% | B/compra@11.77 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-28 23:06 | BTC-USDT-SWAP | 79978.9 | 81069.6/79902.7 | 81309.9 | res 81768.0 (ha 5 candles) | 511.76 | 0.0085% | — | invalidado_setup_B |
| 2026-10-28 23:06 | ETH-USDT-SWAP | 2313.2 | 2353.6/2310.7 | 2358.6 | — | 20.80 | 0.0076% | — | invalidado_setup_B |
| 2026-10-28 23:06 | SOL-USDT-SWAP | 99.81 | 101.81/99.69 | 102.37 | sup 100.39 (ha 11 candles) | 1.0329 | 0.0100% | A/venda@100.39 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-28 23:06 | XRP-USDT-SWAP | 1.2975 | 1.3206/1.2959 | 1.3253 | res 1.3438 (ha 5 candles) | 0.01129 | 0.0100% | B/compra@1.2943 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-28 23:06 | DOGE-USDT-SWAP | 0.07802 | 0.07953/0.07790 | 0.07972 | res 0.08087 (ha 5 candles) | 0.00075 | 0.0086% | — | invalidado_setup_B |
| 2026-10-28 23:06 | ARB-USDT-SWAP | 0.16592 | 0.17125/0.16551 | 0.17209 | — | 0.00338 | 0.0100% | B/compra@0.17743 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-28 23:06 | WLD-USDT-SWAP | 0.42020 | 0.43390/0.41930 | 0.43760 | sup 0.41700 (ha 9 candles) | 0.00929 | 0.0100% | — | sem_zona |
| 2026-10-28 23:06 | SUI-USDT-SWAP | 0.91240 | 0.93890/0.91040 | 0.94270 | — | 0.01314 | 0.0006% | B/compra@0.95790 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-28 23:06 | UNI-USDT-SWAP | 7.0390 | 7.2600/7.0240 | 7.2470 | res 7.3530 (ha 4 candles) | 0.10557 | 0.0100% | B/compra@7.0920 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-28 23:06 | LINK-USDT-SWAP | 11.46 | 11.76/11.42 | 11.81 | — | 0.15807 | 0.0065% | — | invalidado_setup_B |
| 2026-10-29 00:06 | BTC-USDT-SWAP | 79932.9 | 80148.0/79666.0 | 81309.9 | res 81768.0 (ha 6 candles) | 499.56 | 0.0062% | B/compra@79725.3 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-29 00:06 | ETH-USDT-SWAP | 2311.1 | 2317.4/2292.2 | 2358.6 | — | 20.64 | 0.0061% | B/compra@2315.3 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-29 00:06 | SOL-USDT-SWAP | 100.03 | 100.12/99.17 | 102.37 | sup 100.39 (ha 12 candles) | 1.0021 | 0.0080% | A/venda@100.39 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-29 00:06 | XRP-USDT-SWAP | 1.2957 | 1.3024/1.2879 | 1.3253 | res 1.3438 (ha 6 candles) | 0.01145 | 0.0100% | B/compra@1.2943 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-29 00:06 | DOGE-USDT-SWAP | 0.07795 | 0.07828/0.07737 | 0.07972 | res 0.08087 (ha 6 candles) | 0.00074 | 0.0036% | B/compra@0.07780 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-29 00:06 | ARB-USDT-SWAP | 0.16509 | 0.16637/0.16395 | 0.17209 | — | 0.00326 | 0.0038% | B/compra@0.17743 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-29 00:06 | WLD-USDT-SWAP | 0.41540 | 0.42180/0.41250 | 0.43760 | sup 0.41700 (ha 10 candles) | 0.00916 | 0.0100% | A/venda@0.41700 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-29 00:06 | SUI-USDT-SWAP | 0.90970 | 0.91560/0.89790 | 0.94270 | — | 0.01321 | -0.0034% | B/compra@0.95790 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-29 00:06 | UNI-USDT-SWAP | 6.9980 | 7.0780/6.9080 | 7.2470 | res 7.3530 (ha 5 candles) | 0.10779 | 0.0100% | — | invalidado_setup_B |
| 2026-10-29 00:06 | LINK-USDT-SWAP | 11.40 | 11.49/11.28 | 11.81 | — | 0.15921 | -0.0009% | B/compra@11.52 (0t/0c) | zona_mapeada_setup_B |
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
