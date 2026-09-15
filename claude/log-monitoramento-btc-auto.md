# Log de Monitoramento Automatico -- Multi-Par (script gratuito, GitHub Actions)

> Gerado por script Python sem LLM (ver monitor/fetch_and_check.py). Fonte: OKX. Cobre os pares em PAIRS (configuracao no topo do script) -- BTC-USDT-SWAP e os demais adicionados na expansao de 07/09/2026. Leitura e MECANICA (regras objetivas da secao 4 do plano), sem a prosa qualitativa que o Claude gerava -- cole este log numa conversa do Claude se quiser a leitura interpretativa.

| Data/Hora (BRT) | Par | Close 1h | High/Low 1h | Close 4h | Swing 1h ref | ATR 1h | Funding | Zona ativa | Status checklist |
|---|---|---|---|---|---|---|---|---|---|
| 2026-09-13 19:05 | BTC-USDT-SWAP | 77275.0 | 77425.0/77270.6 | 77248.0 | sup 76434.8 (ha 10 candles) | 249.31 | 0.0078% | — | sem_zona |
| 2026-09-13 19:05 | ETH-USDT-SWAP | 2507.9 | 2515.5/2507.4 | 2504.9 | — | 15.68 | 0.0013% | B/venda@2523.0 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-13 19:05 | SOL-USDT-SWAP | 101.28 | 101.57/101.11 | 100.92 | — | 0.57429 | 0.0035% | — | sem_zona |
| 2026-09-13 19:05 | XRP-USDT-SWAP | 1.3567 | 1.3619/1.3562 | 1.3544 | sup 1.3313 (ha 8 candles) | 0.00856 | 0.0013% | — | sem_zona |
| 2026-09-13 19:05 | DOGE-USDT-SWAP | 0.08399 | 0.08443/0.08395 | 0.08413 | — | 0.00051 | 0.0075% | — | invalidado_setup_B |
| 2026-09-13 19:05 | ARB-USDT-SWAP | 0.13701 | 0.13859/0.13691 | 0.13758 | — | 0.00226 | 0.0011% | — | sem_zona |
| 2026-09-13 19:05 | WLD-USDT-SWAP | 0.38900 | 0.39070/0.38870 | 0.38770 | — | 0.00437 | -0.0019% | B/compra@0.38620 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-13 19:05 | SUI-USDT-SWAP | 0.71780 | 0.72160/0.71770 | 0.71810 | sup 0.70430 (ha 8 candles) | 0.00611 | 0.0094% | — | sem_zona |
| 2026-09-13 19:05 | UNI-USDT-SWAP | 6.2490 | 6.2990/6.2470 | 6.2360 | res 6.3840 (ha 4 candles) | 0.08400 | -0.0003% | — | sem_zona_posicao_aberta |
| 2026-09-13 19:05 | LINK-USDT-SWAP | 11.41 | 11.46/11.41 | 11.41 | sup 11.19 (ha 8 candles) | 0.08743 | -0.0107% | B/venda@11.52 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-13 20:05 | BTC-USDT-SWAP | 76679.3 | 77275.1/76628.9 | 77248.0 | sup 76434.8 (ha 11 candles) | 263.36 | 0.0059% | — | sem_zona |
| 2026-09-13 20:05 | ETH-USDT-SWAP | 2474.5 | 2507.9/2470.5 | 2504.9 | — | 15.97 | 0.0029% | B/venda@2523.0 (0t/2c) | zona_mapeada_setup_B |
| 2026-09-13 20:05 | SOL-USDT-SWAP | 99.67 | 101.28/99.25 | 100.92 | — | 0.64929 | 0.0010% | B/compra@100.15 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-13 20:05 | XRP-USDT-SWAP | 1.3367 | 1.3567/1.3330 | 1.3544 | sup 1.3313 (ha 9 candles) | 0.00919 | -0.0005% | — | sem_zona |
| 2026-09-13 20:05 | DOGE-USDT-SWAP | 0.08223 | 0.08398/0.08204 | 0.08413 | — | 0.00057 | 0.0080% | B/compra@0.08213 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-13 20:05 | ARB-USDT-SWAP | 0.13253 | 0.13702/0.13227 | 0.13758 | — | 0.00220 | 0.0026% | — | sem_zona |
| 2026-09-13 20:05 | WLD-USDT-SWAP | 0.37950 | 0.38890/0.37780 | 0.38770 | — | 0.00479 | -0.0043% | — | invalidado_setup_B |
| 2026-09-13 20:05 | SUI-USDT-SWAP | 0.69960 | 0.71780/0.69550 | 0.71810 | sup 0.70430 (ha 9 candles) | 0.00669 | 0.0023% | A/venda@0.70430 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-13 20:05 | UNI-USDT-SWAP | 6.1420 | 6.2490/6.0840 | 6.2360 | res 6.3840 (ha 5 candles) | 0.08307 | -0.0013% | — | sem_zona_posicao_aberta |
| 2026-09-13 20:05 | LINK-USDT-SWAP | 11.16 | 11.41/11.12 | 11.41 | sup 11.19 (ha 9 candles) | 0.09493 | -0.0075% | B/venda@11.52 (0t/2c) | zona_mapeada_setup_B |
| 2026-09-13 21:05 | BTC-USDT-SWAP | 76793.5 | 76836.8/76588.1 | 76793.5 | — | 255.41 | 0.0046% | B/compra@76916.6 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-13 21:05 | ETH-USDT-SWAP | 2475.7 | 2480.5/2468.8 | 2475.7 | — | 14.56 | 0.0039% | B/venda@2523.0 (0t/3c) | zona_mapeada_setup_B |
| 2026-09-13 21:05 | SOL-USDT-SWAP | 99.21 | 99.95/99.12 | 99.21 | — | 0.64929 | -0.0010% | B/compra@100.15 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-13 21:05 | XRP-USDT-SWAP | 1.3401 | 1.3438/1.3365 | 1.3401 | sup 1.3313 (ha 10 candles) | 0.00869 | -0.0011% | — | sem_zona |
| 2026-09-13 21:05 | DOGE-USDT-SWAP | 0.08235 | 0.08271/0.08211 | 0.08235 | — | 0.00057 | 0.0060% | B/compra@0.08213 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-13 21:05 | ARB-USDT-SWAP | 0.13290 | 0.13399/0.13244 | 0.13290 | — | 0.00211 | 0.0053% | — | sem_zona |
| 2026-09-13 21:05 | WLD-USDT-SWAP | 0.37840 | 0.38140/0.37710 | 0.37840 | — | 0.00476 | -0.0019% | B/venda@0.37490 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-13 21:05 | SUI-USDT-SWAP | 0.70120 | 0.70330/0.69720 | 0.70120 | sup 0.70430 (ha 10 candles) | 0.00663 | -0.0011% | A/venda@0.70430 (1t/0c) | zona_mapeada_setup_A |
| 2026-09-13 21:05 | UNI-USDT-SWAP | 6.1190 | 6.1790/6.1020 | 6.1190 | res 6.3840 (ha 6 candles) | 0.08129 | 0.0007% | — | sem_zona_posicao_aberta |
| 2026-09-13 21:05 | LINK-USDT-SWAP | 11.20 | 11.24/11.16 | 11.20 | sup 11.19 (ha 10 candles) | 0.09179 | -0.0062% | B/venda@11.52 (0t/3c) | zona_mapeada_setup_B |
| 2026-09-13 22:06 | BTC-USDT-SWAP | 76772.1 | 77064.2/76323.3 | 76793.5 | — | 294.97 | 0.0043% | — | invalidado_setup_B |
| 2026-09-13 22:06 | ETH-USDT-SWAP | 2483.2 | 2491.2/2462.4 | 2475.7 | — | 15.39 | 0.0048% | B/venda@2523.0 (0t/4c) | zona_mapeada_setup_B |
| 2026-09-13 22:06 | SOL-USDT-SWAP | 99.59 | 99.88/98.92 | 99.21 | — | 0.68214 | -0.0025% | B/compra@100.15 (0t/2c) | zona_mapeada_setup_B |
| 2026-09-13 22:06 | XRP-USDT-SWAP | 1.3465 | 1.3494/1.3333 | 1.3401 | sup 1.3313 (ha 11 candles) | 0.00930 | -0.0015% | — | sem_zona |
| 2026-09-13 22:06 | DOGE-USDT-SWAP | 0.08262 | 0.08283/0.08186 | 0.08235 | — | 0.00061 | 0.0030% | — | descartado_rr_baixo_setup_B |
| 2026-09-13 22:06 | ARB-USDT-SWAP | 0.13478 | 0.13528/0.13270 | 0.13290 | — | 0.00218 | 0.0067% | — | sem_zona |
| 2026-09-13 22:06 | WLD-USDT-SWAP | 0.37990 | 0.38230/0.37500 | 0.37840 | — | 0.00502 | 0.0027% | — | invalidado_setup_B |
| 2026-09-13 22:06 | SUI-USDT-SWAP | 0.70310 | 0.70630/0.69190 | 0.70120 | sup 0.70430 (ha 11 candles) | 0.00723 | -0.0059% | A/venda@0.70430 (2t/0c) | zona_mapeada_setup_A |
| 2026-09-13 22:06 | UNI-USDT-SWAP | 6.2010 | 6.2150/6.0870 | 6.1190 | res 6.3840 (ha 7 candles) | 0.08729 | 0.0035% | — | sem_zona_posicao_aberta |
| 2026-09-13 22:06 | LINK-USDT-SWAP | 11.26 | 11.29/11.10 | 11.20 | sup 11.19 (ha 11 candles) | 0.09921 | -0.0046% | B/venda@11.52 (0t/4c) | zona_mapeada_setup_B |
| 2026-09-13 23:05 | BTC-USDT-SWAP | 77078.9 | 77133.0/76602.8 | 76793.5 | — | 308.52 | 0.0049% | — | sem_zona |
| 2026-09-13 23:05 | ETH-USDT-SWAP | 2492.3 | 2496.4/2472.2 | 2475.7 | — | 16.00 | 0.0060% | B/venda@2523.0 (0t/5c) | zona_mapeada_setup_B |
| 2026-09-13 23:05 | SOL-USDT-SWAP | 100.12 | 100.18/99.11 | 99.21 | — | 0.73143 | -0.0024% | — | descartado_rr_baixo_setup_B |
| 2026-09-13 23:05 | XRP-USDT-SWAP | 1.3511 | 1.3529/1.3376 | 1.3401 | sup 1.3330 (ha 3 candles) | 0.01003 | -0.0007% | — | sem_zona |
| 2026-09-13 23:05 | DOGE-USDT-SWAP | 0.08306 | 0.08310/0.08228 | 0.08235 | — | 0.00064 | 0.0020% | — | sem_zona |
| 2026-09-13 23:05 | ARB-USDT-SWAP | 0.13595 | 0.13640/0.13358 | 0.13290 | — | 0.00225 | 0.0087% | — | sem_zona |
| 2026-09-13 23:05 | WLD-USDT-SWAP | 0.38340 | 0.38400/0.37800 | 0.37840 | — | 0.00518 | 0.0043% | B/venda@0.38450 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-13 23:05 | SUI-USDT-SWAP | 0.70820 | 0.70880/0.69840 | 0.70120 | sup 0.70430 (ha 12 candles) | 0.00769 | -0.0072% | — | invalidado_setup_A |
| 2026-09-13 23:05 | UNI-USDT-SWAP | 6.2360 | 6.2380/6.1360 | 6.1190 | res 6.3840 (ha 8 candles) | 0.08836 | 0.0058% | — | sem_zona_posicao_aberta |
| 2026-09-13 23:05 | LINK-USDT-SWAP | 11.31 | 11.32/11.19 | 11.20 | sup 11.19 (ha 12 candles) | 0.10550 | -0.0024% | B/venda@11.52 (0t/5c) | zona_mapeada_setup_B |
| 2026-09-14 00:05 | BTC-USDT-SWAP | 77573.7 | 77688.0/76982.5 | 76793.5 | — | 344.83 | 0.0054% | B/compra@77574.3 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 00:05 | ETH-USDT-SWAP | 2509.8 | 2512.5/2489.5 | 2475.7 | — | 17.00 | 0.0054% | B/venda@2523.0 (0t/6c) | zona_mapeada_setup_B |
| 2026-09-14 00:05 | SOL-USDT-SWAP | 100.94 | 101.04/99.90 | 99.21 | — | 0.79286 | -0.0005% | — | sem_zona |
| 2026-09-14 00:05 | XRP-USDT-SWAP | 1.3694 | 1.3731/1.3490 | 1.3401 | sup 1.3330 (ha 4 candles) | 0.01123 | 0.0023% | — | sem_zona |
| 2026-09-14 00:05 | DOGE-USDT-SWAP | 0.08404 | 0.08418/0.08297 | 0.08235 | — | 0.00071 | 0.0023% | B/venda@0.08394 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 00:05 | ARB-USDT-SWAP | 0.13934 | 0.14005/0.13555 | 0.13290 | — | 0.00245 | 0.0060% | — | sem_zona |
| 2026-09-14 00:05 | WLD-USDT-SWAP | 0.38610 | 0.38810/0.38250 | 0.37840 | — | 0.00544 | 0.0059% | — | invalidado_setup_B |
| 2026-09-14 00:05 | SUI-USDT-SWAP | 0.71370 | 0.71700/0.70610 | 0.70120 | sup 0.70430 (ha 13 candles) | 0.00824 | -0.0057% | — | sem_zona |
| 2026-09-14 00:05 | UNI-USDT-SWAP | 6.3350 | 6.3660/6.2230 | 6.1190 | res 6.3840 (ha 9 candles) | 0.09464 | 0.0100% | — | sem_zona_posicao_aberta |
| 2026-09-14 00:05 | LINK-USDT-SWAP | 11.36 | 11.39/11.29 | 11.20 | sup 11.19 (ha 13 candles) | 0.10671 | -0.0025% | B/venda@11.52 (0t/6c) | zona_mapeada_setup_B |
| 2026-09-14 01:05 | BTC-USDT-SWAP | 77562.7 | 77838.8/77461.1 | 77562.7 | — | 344.11 | 0.0054% | B/compra@77574.3 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-14 01:05 | ETH-USDT-SWAP | 2511.8 | 2518.9/2506.0 | 2511.8 | — | 16.27 | 0.0048% | B/venda@2523.0 (0t/7c) | zona_mapeada_setup_B |
| 2026-09-14 01:05 | SOL-USDT-SWAP | 100.93 | 101.29/100.72 | 100.93 | — | 0.77929 | 0.0000% | — | sem_zona |
| 2026-09-14 01:05 | XRP-USDT-SWAP | 1.3720 | 1.3803/1.3677 | 1.3720 | — | 0.01134 | 0.0038% | B/venda@1.3737 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 01:05 | DOGE-USDT-SWAP | 0.08387 | 0.08428/0.08370 | 0.08387 | — | 0.00070 | 0.0024% | — | descartado_rr_baixo_setup_B |
| 2026-09-14 01:05 | ARB-USDT-SWAP | 0.13859 | 0.14043/0.13839 | 0.13859 | — | 0.00242 | 0.0021% | — | sem_zona |
| 2026-09-14 01:05 | WLD-USDT-SWAP | 0.38640 | 0.38840/0.38460 | 0.38640 | — | 0.00530 | 0.0050% | B/venda@0.38910 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 01:05 | SUI-USDT-SWAP | 0.71610 | 0.71840/0.71320 | 0.71610 | sup 0.69190 (ha 3 candles) | 0.00794 | -0.0044% | — | sem_zona |
| 2026-09-14 01:05 | UNI-USDT-SWAP | 6.3910 | 6.4660/6.3190 | 6.3910 | res 6.3840 (ha 10 candles) | 0.09871 | 0.0100% | — | sem_zona_posicao_aberta |
| 2026-09-14 01:05 | LINK-USDT-SWAP | 11.37 | 11.44/11.34 | 11.37 | sup 11.10 (ha 3 candles) | 0.10536 | 0.0001% | B/venda@11.52 (0t/7c) | zona_mapeada_setup_B |
| 2026-09-14 02:05 | BTC-USDT-SWAP | 77643.8 | 77671.1/77488.6 | 77562.7 | — | 328.11 | 0.0060% | — | CONFIRMADO_setup_B |
| 2026-09-14 02:05 | ETH-USDT-SWAP | 2513.6 | 2517.1/2509.9 | 2511.8 | — | 15.56 | 0.0051% | — | zona_expirada_setup_B |
| 2026-09-14 02:05 | SOL-USDT-SWAP | 101.14 | 101.32/100.82 | 100.93 | — | 0.76214 | 0.0020% | B/compra@101.61 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 02:05 | XRP-USDT-SWAP | 1.3763 | 1.3798/1.3705 | 1.3720 | — | 0.01112 | 0.0062% | B/venda@1.3737 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-14 02:05 | DOGE-USDT-SWAP | 0.08400 | 0.08415/0.08379 | 0.08387 | — | 0.00069 | 0.0027% | B/compra@0.08450 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 02:05 | ARB-USDT-SWAP | 0.13732 | 0.13866/0.13712 | 0.13859 | — | 0.00231 | 0.0007% | B/compra@0.13729 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 02:05 | WLD-USDT-SWAP | 0.38450 | 0.38700/0.38400 | 0.38640 | — | 0.00505 | 0.0067% | B/venda@0.38910 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-14 02:05 | SUI-USDT-SWAP | 0.71780 | 0.72000/0.71490 | 0.71610 | sup 0.69190 (ha 4 candles) | 0.00794 | -0.0027% | — | sem_zona |
| 2026-09-14 02:05 | UNI-USDT-SWAP | 6.3820 | 6.4210/6.3550 | 6.3910 | res 6.3840 (ha 11 candles) | 0.09721 | 0.0100% | — | sem_zona_posicao_aberta |
| 2026-09-14 02:05 | LINK-USDT-SWAP | 11.39 | 11.41/11.36 | 11.37 | sup 11.10 (ha 4 candles) | 0.10607 | 0.0007% | — | zona_expirada_setup_B |
| 2026-09-14 03:05 | BTC-USDT-SWAP | 77574.9 | 77654.1/77443.0 | 77562.7 | — | 328.48 | 0.0060% | — | sem_zona |
| 2026-09-14 03:05 | ETH-USDT-SWAP | 2515.2 | 2515.2/2509.3 | 2511.8 | — | 15.22 | 0.0057% | — | sem_zona |
| 2026-09-14 03:05 | SOL-USDT-SWAP | 101.07 | 101.18/100.89 | 100.93 | — | 0.74714 | 0.0041% | B/compra@101.61 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-14 03:05 | XRP-USDT-SWAP | 1.3795 | 1.3808/1.3739 | 1.3720 | — | 0.01109 | 0.0078% | — | invalidado_setup_B |
| 2026-09-14 03:05 | DOGE-USDT-SWAP | 0.08421 | 0.08424/0.08393 | 0.08387 | — | 0.00069 | 0.0037% | B/compra@0.08450 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-14 03:05 | ARB-USDT-SWAP | 0.13675 | 0.13749/0.13650 | 0.13859 | — | 0.00225 | 0.0011% | B/compra@0.13729 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-14 03:05 | WLD-USDT-SWAP | 0.38350 | 0.38480/0.38240 | 0.38640 | — | 0.00484 | 0.0079% | B/venda@0.38910 (0t/2c) | zona_mapeada_setup_B |
| 2026-09-14 03:05 | SUI-USDT-SWAP | 0.71760 | 0.71820/0.71510 | 0.71610 | sup 0.69190 (ha 5 candles) | 0.00772 | -0.0001% | — | sem_zona |
| 2026-09-14 03:05 | UNI-USDT-SWAP | 6.3510 | 6.4100/6.3270 | 6.3910 | res 6.3840 (ha 12 candles) | 0.09721 | 0.0100% | — | sem_zona_posicao_aberta |
| 2026-09-14 03:05 | LINK-USDT-SWAP | 11.41 | 11.41/11.35 | 11.37 | sup 11.10 (ha 5 candles) | 0.10493 | 0.0019% | — | sem_zona |
| 2026-09-14 04:05 | BTC-USDT-SWAP | 77555.1 | 77869.2/77333.0 | 77562.7 | — | 350.14 | 0.0059% | — | sem_zona |
| 2026-09-14 04:05 | ETH-USDT-SWAP | 2513.4 | 2527.6/2506.2 | 2511.8 | — | 15.62 | 0.0045% | — | sem_zona |
| 2026-09-14 04:05 | SOL-USDT-SWAP | 101.50 | 101.97/101.04 | 100.93 | — | 0.75786 | 0.0053% | B/compra@101.61 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-14 04:05 | XRP-USDT-SWAP | 1.3858 | 1.3877/1.3738 | 1.3720 | — | 0.01149 | 0.0072% | B/compra@1.3804 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 04:05 | DOGE-USDT-SWAP | 0.08426 | 0.08455/0.08402 | 0.08387 | — | 0.00069 | 0.0026% | — | invalidado_setup_B |
| 2026-09-14 04:05 | ARB-USDT-SWAP | 0.13631 | 0.13874/0.13530 | 0.13859 | — | 0.00229 | -0.0006% | — | invalidado_setup_B |
| 2026-09-14 04:05 | WLD-USDT-SWAP | 0.38340 | 0.38730/0.38310 | 0.38640 | — | 0.00490 | 0.0056% | B/venda@0.38910 (0t/3c) | zona_mapeada_setup_B |
| 2026-09-14 04:05 | SUI-USDT-SWAP | 0.72310 | 0.72650/0.71730 | 0.71610 | sup 0.69190 (ha 6 candles) | 0.00799 | -0.0009% | — | sem_zona |
| 2026-09-14 04:05 | UNI-USDT-SWAP | 6.2980 | 6.3980/6.2510 | 6.3910 | res 6.4660 (ha 3 candles) | 0.10279 | 0.0081% | — | sem_zona_posicao_aberta |
| 2026-09-14 04:05 | LINK-USDT-SWAP | 11.41 | 11.46/11.38 | 11.37 | sup 11.10 (ha 6 candles) | 0.10400 | 0.0016% | — | sem_zona |
| 2026-09-14 05:05 | BTC-USDT-SWAP | 77854.9 | 77855.0/77487.7 | 77854.9 | — | 363.39 | 0.0056% | — | sem_zona |
| 2026-09-14 05:05 | ETH-USDT-SWAP | 2521.7 | 2525.8/2509.9 | 2521.7 | — | 16.01 | 0.0031% | B/venda@2530.5 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 05:05 | SOL-USDT-SWAP | 101.55 | 101.69/101.37 | 101.55 | — | 0.74929 | 0.0064% | B/compra@101.61 (2t/0c) | zona_mapeada_setup_B |
| 2026-09-14 05:05 | XRP-USDT-SWAP | 1.3900 | 1.3902/1.3837 | 1.3900 | — | 0.01151 | 0.0063% | B/compra@1.3804 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-14 05:05 | DOGE-USDT-SWAP | 0.08431 | 0.08440/0.08412 | 0.08431 | — | 0.00066 | 0.0026% | B/compra@0.08413 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 05:05 | ARB-USDT-SWAP | 0.13709 | 0.13755/0.13604 | 0.13709 | — | 0.00228 | -0.0047% | — | sem_zona |
| 2026-09-14 05:05 | WLD-USDT-SWAP | 0.38230 | 0.38490/0.38160 | 0.38230 | — | 0.00485 | 0.0046% | B/venda@0.38910 (0t/4c) | zona_mapeada_setup_B |
| 2026-09-14 05:05 | SUI-USDT-SWAP | 0.72400 | 0.72530/0.72060 | 0.72400 | sup 0.69190 (ha 7 candles) | 0.00799 | 0.0005% | — | sem_zona |
| 2026-09-14 05:05 | UNI-USDT-SWAP | 6.3480 | 6.3560/6.2850 | 6.3480 | res 6.4660 (ha 4 candles) | 0.10157 | 0.0053% | — | sem_zona_posicao_aberta |
| 2026-09-14 05:05 | LINK-USDT-SWAP | 11.40 | 11.43/11.37 | 11.40 | sup 11.10 (ha 7 candles) | 0.10300 | 0.0011% | — | sem_zona |
| 2026-09-14 06:05 | BTC-USDT-SWAP | 77707.4 | 77973.0/77619.5 | 77854.9 | — | 383.33 | 0.0047% | B/venda@77493.8 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 06:05 | ETH-USDT-SWAP | 2517.5 | 2532.6/2514.8 | 2521.7 | — | 16.91 | 0.0032% | — | descartado_rr_baixo_setup_B |
| 2026-09-14 06:05 | SOL-USDT-SWAP | 101.44 | 101.79/101.28 | 101.55 | — | 0.76214 | 0.0067% | — | zona_expirada_setup_B |
| 2026-09-14 06:05 | XRP-USDT-SWAP | 1.3846 | 1.3932/1.3834 | 1.3900 | — | 0.01175 | 0.0068% | B/compra@1.3804 (0t/2c) | zona_mapeada_setup_B |
| 2026-09-14 06:05 | DOGE-USDT-SWAP | 0.08411 | 0.08455/0.08401 | 0.08431 | — | 0.00068 | 0.0025% | B/compra@0.08413 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-14 06:05 | ARB-USDT-SWAP | 0.13598 | 0.13724/0.13569 | 0.13709 | — | 0.00228 | -0.0037% | — | sem_zona |
| 2026-09-14 06:05 | WLD-USDT-SWAP | 0.38290 | 0.38500/0.38040 | 0.38230 | — | 0.00507 | 0.0009% | B/venda@0.38910 (0t/5c) | zona_mapeada_setup_B |
| 2026-09-14 06:05 | SUI-USDT-SWAP | 0.72370 | 0.72880/0.71970 | 0.72400 | sup 0.69190 (ha 8 candles) | 0.00819 | -0.0025% | — | sem_zona |
| 2026-09-14 06:05 | UNI-USDT-SWAP | 6.2980 | 6.3670/6.2880 | 6.3480 | res 6.4660 (ha 5 candles) | 0.10343 | 0.0046% | — | sem_zona_posicao_aberta |
| 2026-09-14 06:05 | LINK-USDT-SWAP | 11.37 | 11.45/11.35 | 11.40 | sup 11.10 (ha 8 candles) | 0.10214 | 0.0001% | — | sem_zona |
| 2026-09-14 07:05 | BTC-USDT-SWAP | 78109.3 | 78345.0/77550.0 | 77854.9 | — | 425.35 | 0.0045% | — | invalidado_setup_B |
| 2026-09-14 07:05 | ETH-USDT-SWAP | 2522.8 | 2534.0/2510.1 | 2521.7 | — | 17.65 | 0.0034% | B/venda@2523.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 07:05 | SOL-USDT-SWAP | 101.90 | 102.31/101.17 | 101.55 | — | 0.80786 | 0.0082% | — | sem_zona |
| 2026-09-14 07:05 | XRP-USDT-SWAP | 1.4020 | 1.4094/1.3805 | 1.3900 | — | 0.01335 | 0.0075% | — | descartado_rr_baixo_setup_B |
| 2026-09-14 07:05 | DOGE-USDT-SWAP | 0.08439 | 0.08480/0.08377 | 0.08431 | — | 0.00071 | 0.0030% | — | descartado_rr_baixo_setup_B |
| 2026-09-14 07:05 | ARB-USDT-SWAP | 0.13640 | 0.13771/0.13477 | 0.13709 | — | 0.00234 | -0.0006% | — | sem_zona |
| 2026-09-14 07:05 | WLD-USDT-SWAP | 0.38530 | 0.38710/0.37960 | 0.38230 | — | 0.00488 | -0.0016% | B/venda@0.38910 (0t/6c) | zona_mapeada_setup_B |
| 2026-09-14 07:05 | SUI-USDT-SWAP | 0.72620 | 0.72990/0.72010 | 0.72400 | sup 0.69190 (ha 9 candles) | 0.00844 | -0.0033% | — | sem_zona |
| 2026-09-14 07:05 | UNI-USDT-SWAP | 6.3150 | 6.3720/6.2470 | 6.3480 | res 6.4660 (ha 6 candles) | 0.10350 | 0.0048% | — | sem_zona_posicao_aberta |
| 2026-09-14 07:05 | LINK-USDT-SWAP | 11.44 | 11.48/11.31 | 11.40 | sup 11.10 (ha 9 candles) | 0.10893 | 0.0009% | — | sem_zona |
| 2026-09-14 08:05 | BTC-USDT-SWAP | 77866.6 | 78135.8/77865.0 | 77854.9 | — | 437.14 | 0.0048% | — | sem_zona |
| 2026-09-14 08:05 | ETH-USDT-SWAP | 2512.2 | 2524.2/2512.2 | 2521.7 | — | 17.88 | 0.0046% | — | descartado_rr_baixo_setup_B |
| 2026-09-14 08:05 | SOL-USDT-SWAP | 101.73 | 101.97/101.64 | 101.55 | — | 0.79143 | 0.0075% | — | sem_zona |
| 2026-09-14 08:05 | XRP-USDT-SWAP | 1.3964 | 1.4080/1.3940 | 1.3900 | — | 0.01386 | 0.0087% | B/venda@1.3972 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 08:05 | DOGE-USDT-SWAP | 0.08432 | 0.08453/0.08419 | 0.08431 | — | 0.00071 | 0.0047% | B/compra@0.08450 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 08:05 | ARB-USDT-SWAP | 0.13526 | 0.13674/0.13513 | 0.13709 | — | 0.00239 | 0.0001% | — | sem_zona |
| 2026-09-14 08:05 | WLD-USDT-SWAP | 0.38410 | 0.38640/0.38310 | 0.38230 | — | 0.00489 | -0.0044% | B/venda@0.38910 (0t/7c) | zona_mapeada_setup_B |
| 2026-09-14 08:05 | SUI-USDT-SWAP | 0.72310 | 0.72760/0.72260 | 0.72400 | sup 0.69190 (ha 10 candles) | 0.00851 | -0.0009% | — | sem_zona |
| 2026-09-14 08:05 | UNI-USDT-SWAP | 6.3040 | 6.3360/6.2720 | 6.3480 | res 6.4660 (ha 7 candles) | 0.10350 | 0.0016% | — | sem_zona_posicao_aberta |
| 2026-09-14 08:05 | LINK-USDT-SWAP | 11.37 | 11.44/11.37 | 11.40 | sup 11.10 (ha 10 candles) | 0.10936 | 0.0022% | — | sem_zona |
| 2026-09-14 09:05 | BTC-USDT-SWAP | 77749.9 | 77897.7/77652.8 | 77749.9 | — | 443.61 | 0.0051% | — | sem_zona |
| 2026-09-14 09:05 | ETH-USDT-SWAP | 2508.2 | 2515.8/2503.8 | 2508.2 | — | 18.16 | 0.0064% | — | sem_zona |
| 2026-09-14 09:05 | SOL-USDT-SWAP | 101.32 | 101.86/101.25 | 101.32 | — | 0.80214 | 0.0085% | — | sem_zona |
| 2026-09-14 09:05 | XRP-USDT-SWAP | 1.3980 | 1.4059/1.3937 | 1.3980 | — | 0.01433 | 0.0100% | B/venda@1.3972 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-14 09:05 | DOGE-USDT-SWAP | 0.08408 | 0.08444/0.08397 | 0.08408 | — | 0.00071 | 0.0062% | — | invalidado_setup_B |
| 2026-09-14 09:05 | ARB-USDT-SWAP | 0.13485 | 0.13526/0.13421 | 0.13485 | sup 0.13227 (ha 13 candles) | 0.00235 | 0.0043% | — | sem_zona |
| 2026-09-14 09:05 | WLD-USDT-SWAP | 0.38500 | 0.38630/0.38220 | 0.38500 | — | 0.00504 | -0.0088% | — | zona_expirada_setup_B |
| 2026-09-14 09:05 | SUI-USDT-SWAP | 0.72380 | 0.72720/0.71830 | 0.72380 | sup 0.69190 (ha 11 candles) | 0.00887 | -0.0015% | — | sem_zona |
| 2026-09-14 09:05 | UNI-USDT-SWAP | 6.3030 | 6.3290/6.2690 | 6.3030 | res 6.4660 (ha 8 candles) | 0.10407 | 0.0015% | — | sem_zona_posicao_aberta |
| 2026-09-14 09:05 | LINK-USDT-SWAP | 11.38 | 11.41/11.35 | 11.38 | sup 11.10 (ha 11 candles) | 0.11036 | 0.0044% | — | sem_zona |
| 2026-09-14 10:05 | BTC-USDT-SWAP | 77666.7 | 78059.5/77577.0 | 77749.9 | — | 431.91 | 0.0052% | B/compra@77574.3 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 10:05 | ETH-USDT-SWAP | 2504.6 | 2517.8/2502.1 | 2508.2 | — | 16.61 | 0.0066% | — | sem_zona |
| 2026-09-14 10:05 | SOL-USDT-SWAP | 101.34 | 101.97/101.14 | 101.32 | — | 0.71643 | 0.0084% | — | sem_zona |
| 2026-09-14 10:05 | XRP-USDT-SWAP | 1.3945 | 1.4040/1.3918 | 1.3980 | — | 0.01351 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-09-14 10:05 | DOGE-USDT-SWAP | 0.08366 | 0.08440/0.08351 | 0.08408 | — | 0.00064 | 0.0056% | B/venda@0.08394 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 10:05 | ARB-USDT-SWAP | 0.13444 | 0.13635/0.13377 | 0.13485 | sup 0.13227 (ha 14 candles) | 0.00219 | 0.0086% | — | sem_zona |
| 2026-09-14 10:05 | WLD-USDT-SWAP | 0.38180 | 0.38750/0.38150 | 0.38500 | — | 0.00467 | -0.0108% | B/venda@0.38450 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 10:05 | SUI-USDT-SWAP | 0.72070 | 0.72770/0.71950 | 0.72380 | sup 0.69190 (ha 12 candles) | 0.00786 | -0.0059% | — | sem_zona |
| 2026-09-14 10:05 | UNI-USDT-SWAP | 6.2660 | 6.3370/6.2560 | 6.3030 | res 6.4660 (ha 9 candles) | 0.09807 | 0.0006% | — | sem_zona_posicao_aberta |
| 2026-09-14 10:05 | LINK-USDT-SWAP | 11.31 | 11.41/11.30 | 11.38 | sup 11.10 (ha 12 candles) | 0.09807 | 0.0047% | — | sem_zona |
| 2026-09-14 11:05 | BTC-USDT-SWAP | 78148.5 | 78472.6/77438.4 | 77749.9 | — | 488.02 | 0.0065% | — | descartado_rr_baixo_setup_B |
| 2026-09-14 11:05 | ETH-USDT-SWAP | 2499.5 | 2516.8/2486.9 | 2508.2 | — | 17.91 | 0.0067% | B/venda@2489.8 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 11:05 | SOL-USDT-SWAP | 101.31 | 101.87/100.61 | 101.32 | — | 0.74714 | 0.0095% | — | sem_zona |
| 2026-09-14 11:05 | XRP-USDT-SWAP | 1.3939 | 1.4026/1.3822 | 1.3980 | — | 0.01444 | 0.0100% | B/venda@1.4025 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 11:05 | DOGE-USDT-SWAP | 0.08367 | 0.08426/0.08307 | 0.08408 | — | 0.00068 | 0.0057% | B/venda@0.08394 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-14 11:05 | ARB-USDT-SWAP | 0.13436 | 0.13593/0.13284 | 0.13485 | sup 0.13227 (ha 15 candles) | 0.00230 | 0.0100% | — | sem_zona |
| 2026-09-14 11:05 | WLD-USDT-SWAP | 0.38250 | 0.38580/0.37840 | 0.38500 | — | 0.00489 | -0.0114% | B/venda@0.38450 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-14 11:05 | SUI-USDT-SWAP | 0.72130 | 0.72650/0.71450 | 0.72380 | sup 0.69190 (ha 13 candles) | 0.00829 | -0.0067% | — | sem_zona |
| 2026-09-14 11:05 | UNI-USDT-SWAP | 6.3600 | 6.4390/6.2090 | 6.3030 | res 6.4660 (ha 10 candles) | 0.10900 | 0.0047% | — | sem_zona_posicao_aberta |
| 2026-09-14 11:05 | LINK-USDT-SWAP | 11.34 | 11.43/11.24 | 11.38 | sup 11.10 (ha 13 candles) | 0.10507 | 0.0056% | — | sem_zona |
| 2026-09-14 12:06 | BTC-USDT-SWAP | 78486.4 | 78675.0/78132.3 | 77749.9 | — | 473.86 | 0.0056% | B/venda@78299.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 12:06 | ETH-USDT-SWAP | 2500.5 | 2515.2/2493.3 | 2508.2 | — | 17.42 | 0.0045% | — | invalidado_setup_B |
| 2026-09-14 12:06 | SOL-USDT-SWAP | 101.57 | 101.97/101.12 | 101.32 | — | 0.73929 | 0.0085% | — | sem_zona |
| 2026-09-14 12:06 | XRP-USDT-SWAP | 1.3993 | 1.4048/1.3934 | 1.3980 | — | 0.01411 | 0.0100% | B/venda@1.4025 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-14 12:06 | DOGE-USDT-SWAP | 0.08376 | 0.08425/0.08356 | 0.08408 | — | 0.00066 | 0.0048% | B/venda@0.08394 (2t/0c) | zona_mapeada_setup_B |
| 2026-09-14 12:06 | ARB-USDT-SWAP | 0.13499 | 0.13616/0.13427 | 0.13485 | sup 0.13227 (ha 16 candles) | 0.00225 | 0.0100% | — | sem_zona |
| 2026-09-14 12:06 | WLD-USDT-SWAP | 0.38110 | 0.38590/0.38060 | 0.38500 | — | 0.00475 | -0.0144% | — | descartado_rr_baixo_setup_B |
| 2026-09-14 12:06 | SUI-USDT-SWAP | 0.71940 | 0.72740/0.71720 | 0.72380 | sup 0.69190 (ha 14 candles) | 0.00799 | -0.0083% | — | sem_zona |
| 2026-09-14 12:06 | UNI-USDT-SWAP | 6.3390 | 6.3910/6.3150 | 6.3030 | res 6.4660 (ha 11 candles) | 0.10529 | 0.0056% | — | sem_zona_posicao_aberta |
| 2026-09-14 12:06 | LINK-USDT-SWAP | 11.40 | 11.44/11.34 | 11.38 | sup 11.10 (ha 14 candles) | 0.09893 | 0.0065% | — | sem_zona |
| 2026-09-14 13:05 | BTC-USDT-SWAP | 78536.7 | 78655.0/78266.7 | 78536.7 | sup 77333.0 (ha 9 candles) | 463.73 | 0.0046% | — | invalidado_setup_B |
| 2026-09-14 13:05 | ETH-USDT-SWAP | 2507.2 | 2512.0/2495.0 | 2507.2 | — | 16.90 | 0.0037% | — | sem_zona |
| 2026-09-14 13:05 | SOL-USDT-SWAP | 101.91 | 102.24/101.28 | 101.91 | res 102.31 (ha 6 candles) | 0.73143 | 0.0084% | — | sem_zona |
| 2026-09-14 13:05 | XRP-USDT-SWAP | 1.4026 | 1.4070/1.3916 | 1.4026 | — | 0.01411 | 0.0100% | B/venda@1.4025 (2t/0c) | zona_mapeada_setup_B |
| 2026-09-14 13:05 | DOGE-USDT-SWAP | 0.08401 | 0.08430/0.08354 | 0.08401 | sup 0.08186 (ha 15 candles) | 0.00066 | 0.0060% | — | zona_expirada_setup_B |
| 2026-09-14 13:05 | ARB-USDT-SWAP | 0.13557 | 0.13598/0.13406 | 0.13557 | sup 0.13227 (ha 17 candles) | 0.00219 | 0.0100% | — | sem_zona |
| 2026-09-14 13:05 | WLD-USDT-SWAP | 0.38350 | 0.38470/0.37900 | 0.38350 | sup 0.37960 (ha 6 candles) | 0.00473 | -0.0141% | — | sem_zona |
| 2026-09-14 13:05 | SUI-USDT-SWAP | 0.72400 | 0.72710/0.71620 | 0.72400 | sup 0.69190 (ha 15 candles) | 0.00802 | -0.0100% | — | sem_zona |
| 2026-09-14 13:05 | UNI-USDT-SWAP | 6.3670 | 6.3840/6.3120 | 6.3670 | — | 0.10314 | 0.0062% | — | sem_zona_posicao_aberta |
| 2026-09-14 13:05 | LINK-USDT-SWAP | 11.46 | 11.49/11.37 | 11.46 | sup 11.10 (ha 15 candles) | 0.09829 | 0.0096% | B/venda@11.52 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 14:05 | BTC-USDT-SWAP | 78730.7 | 78888.8/78384.7 | 78536.7 | sup 77438.4 (ha 3 candles) | 449.34 | 0.0055% | — | sem_zona |
| 2026-09-14 14:05 | ETH-USDT-SWAP | 2528.0 | 2537.5/2503.0 | 2507.2 | — | 17.72 | 0.0030% | B/venda@2523.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 14:05 | SOL-USDT-SWAP | 102.55 | 102.84/101.81 | 101.91 | res 102.31 (ha 7 candles) | 0.72357 | 0.0100% | A/compra@102.31 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-14 14:05 | XRP-USDT-SWAP | 1.4182 | 1.4220/1.4006 | 1.4026 | — | 0.01392 | 0.0100% | — | invalidado_setup_B |
| 2026-09-14 14:05 | DOGE-USDT-SWAP | 0.08441 | 0.08471/0.08384 | 0.08401 | sup 0.08307 (ha 3 candles) | 0.00063 | 0.0069% | — | sem_zona |
| 2026-09-14 14:05 | ARB-USDT-SWAP | 0.13666 | 0.13759/0.13516 | 0.13557 | sup 0.13284 (ha 3 candles) | 0.00204 | 0.0100% | — | sem_zona |
| 2026-09-14 14:05 | WLD-USDT-SWAP | 0.38570 | 0.38790/0.38250 | 0.38350 | sup 0.37840 (ha 3 candles) | 0.00471 | -0.0127% | B/venda@0.38910 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 14:05 | SUI-USDT-SWAP | 0.73110 | 0.73520/0.72270 | 0.72400 | sup 0.71450 (ha 3 candles) | 0.00814 | -0.0089% | — | sem_zona |
| 2026-09-14 14:05 | UNI-USDT-SWAP | 6.3930 | 6.4210/6.3350 | 6.3670 | — | 0.09907 | 0.0069% | — | sem_zona_posicao_aberta |
| 2026-09-14 14:05 | LINK-USDT-SWAP | 11.50 | 11.56/11.44 | 11.46 | sup 11.24 (ha 3 candles) | 0.10057 | 0.0100% | B/venda@11.52 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-14 15:05 | BTC-USDT-SWAP | 78916.3 | 79031.6/78675.4 | 78536.7 | sup 77438.4 (ha 4 candles) | 447.81 | 0.0065% | B/venda@79238.9 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 15:05 | ETH-USDT-SWAP | 2532.2 | 2534.5/2521.4 | 2507.2 | — | 17.74 | 0.0024% | — | invalidado_setup_B |
| 2026-09-14 15:05 | SOL-USDT-SWAP | 103.02 | 103.27/102.46 | 101.91 | res 102.31 (ha 8 candles) | 0.74071 | 0.0100% | — | descartado_rr_baixo_setup_A |
| 2026-09-14 15:05 | XRP-USDT-SWAP | 1.4340 | 1.4415/1.4160 | 1.4026 | — | 0.01484 | 0.0092% | B/venda@1.4323 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 15:05 | DOGE-USDT-SWAP | 0.08477 | 0.08494/0.08432 | 0.08401 | sup 0.08307 (ha 4 candles) | 0.00063 | 0.0070% | — | sem_zona |
| 2026-09-14 15:05 | ARB-USDT-SWAP | 0.14026 | 0.14161/0.13645 | 0.13557 | sup 0.13284 (ha 4 candles) | 0.00226 | 0.0100% | — | sem_zona |
| 2026-09-14 15:05 | WLD-USDT-SWAP | 0.39160 | 0.39280/0.38550 | 0.38350 | sup 0.37840 (ha 4 candles) | 0.00496 | -0.0118% | — | invalidado_setup_B |
| 2026-09-14 15:05 | SUI-USDT-SWAP | 0.73470 | 0.73630/0.72910 | 0.72400 | sup 0.71450 (ha 4 candles) | 0.00828 | -0.0057% | B/venda@0.73780 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 15:05 | UNI-USDT-SWAP | 6.4320 | 6.4650/6.3850 | 6.3670 | — | 0.09429 | 0.0088% | — | sem_zona_posicao_aberta |
| 2026-09-14 15:05 | LINK-USDT-SWAP | 11.61 | 11.64/11.49 | 11.46 | sup 11.24 (ha 4 candles) | 0.10414 | 0.0100% | — | invalidado_setup_B |
| 2026-09-14 16:05 | BTC-USDT-SWAP | 79188.0 | 79288.0/78801.1 | 78536.7 | sup 77438.4 (ha 5 candles) | 469.55 | 0.0060% | B/venda@79238.9 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-14 16:05 | ETH-USDT-SWAP | 2537.3 | 2543.6/2528.5 | 2507.2 | — | 18.30 | -0.0002% | B/venda@2546.5 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 16:05 | SOL-USDT-SWAP | 103.57 | 103.82/102.88 | 101.91 | res 102.31 (ha 9 candles) | 0.77214 | 0.0100% | — | sem_zona |
| 2026-09-14 16:05 | XRP-USDT-SWAP | 1.4765 | 1.4798/1.4295 | 1.4026 | — | 0.01777 | 0.0100% | — | invalidado_setup_B |
| 2026-09-14 16:05 | DOGE-USDT-SWAP | 0.08499 | 0.08530/0.08461 | 0.08401 | sup 0.08307 (ha 5 candles) | 0.00066 | 0.0080% | B/venda@0.08533 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 16:05 | ARB-USDT-SWAP | 0.14036 | 0.14133/0.13959 | 0.13557 | sup 0.13284 (ha 5 candles) | 0.00228 | 0.0100% | — | sem_zona |
| 2026-09-14 16:05 | WLD-USDT-SWAP | 0.39490 | 0.39520/0.39070 | 0.38350 | sup 0.37840 (ha 5 candles) | 0.00507 | -0.0130% | — | sem_zona |
| 2026-09-14 16:05 | SUI-USDT-SWAP | 0.74220 | 0.74490/0.73280 | 0.72400 | sup 0.71450 (ha 5 candles) | 0.00878 | -0.0037% | — | invalidado_setup_B |
| 2026-09-14 16:05 | UNI-USDT-SWAP | 6.6180 | 6.6330/6.4290 | 6.3670 | — | 0.10414 | 0.0100% | B/venda@6.5670 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 16:05 | LINK-USDT-SWAP | 11.70 | 11.71/11.58 | 11.46 | sup 11.24 (ha 5 candles) | 0.11014 | 0.0100% | B/venda@11.62 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 17:05 | BTC-USDT-SWAP | 78956.3 | 79200.0/78891.3 | 78956.3 | sup 77438.4 (ha 6 candles) | 476.52 | 0.0058% | — | descartado_rr_baixo_setup_B |
| 2026-09-14 17:05 | ETH-USDT-SWAP | 2538.6 | 2549.0/2532.9 | 2538.6 | — | 19.03 | -0.0009% | B/venda@2546.5 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-14 17:05 | SOL-USDT-SWAP | 103.21 | 103.56/102.85 | 103.21 | res 102.31 (ha 10 candles) | 0.80286 | 0.0100% | — | sem_zona |
| 2026-09-14 17:05 | XRP-USDT-SWAP | 1.4635 | 1.4773/1.4534 | 1.4635 | — | 0.01899 | 0.0100% | B/venda@1.4504 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 17:05 | DOGE-USDT-SWAP | 0.08467 | 0.08500/0.08454 | 0.08467 | sup 0.08307 (ha 6 candles) | 0.00067 | 0.0075% | B/venda@0.08533 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-14 17:05 | ARB-USDT-SWAP | 0.14014 | 0.14180/0.13998 | 0.14014 | sup 0.13284 (ha 6 candles) | 0.00234 | 0.0100% | — | sem_zona |
| 2026-09-14 17:05 | WLD-USDT-SWAP | 0.39020 | 0.39490/0.38940 | 0.39020 | sup 0.37840 (ha 6 candles) | 0.00529 | -0.0128% | — | sem_zona |
| 2026-09-14 17:05 | SUI-USDT-SWAP | 0.73510 | 0.74210/0.73370 | 0.73510 | sup 0.71450 (ha 6 candles) | 0.00916 | 0.0010% | B/venda@0.73050 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 17:05 | UNI-USDT-SWAP | 6.6880 | 6.7480/6.5810 | 6.6880 | — | 0.11014 | 0.0100% | — | invalidado_setup_B |
| 2026-09-14 17:05 | LINK-USDT-SWAP | 11.73 | 11.75/11.65 | 11.73 | sup 11.24 (ha 6 candles) | 0.11364 | 0.0100% | — | invalidado_setup_B |
| 2026-09-14 18:05 | BTC-USDT-SWAP | 79067.4 | 79569.0/78945.7 | 78956.3 | sup 77438.4 (ha 7 candles) | 482.74 | 0.0054% | B/venda@79387.8 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 18:05 | ETH-USDT-SWAP | 2569.9 | 2615.0/2538.6 | 2538.6 | — | 22.96 | 0.0029% | — | invalidado_setup_B |
| 2026-09-14 18:05 | SOL-USDT-SWAP | 103.95 | 104.78/103.16 | 103.21 | res 102.31 (ha 11 candles) | 0.85214 | 0.0100% | — | sem_zona |
| 2026-09-14 18:05 | XRP-USDT-SWAP | 1.4631 | 1.4914/1.4623 | 1.4635 | — | 0.02007 | 0.0100% | B/venda@1.4504 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-14 18:05 | DOGE-USDT-SWAP | 0.08512 | 0.08612/0.08466 | 0.08467 | sup 0.08307 (ha 7 candles) | 0.00073 | 0.0100% | B/venda@0.08533 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-14 18:05 | ARB-USDT-SWAP | 0.14071 | 0.14214/0.13997 | 0.14014 | sup 0.13284 (ha 7 candles) | 0.00225 | 0.0100% | — | sem_zona |
| 2026-09-14 18:05 | WLD-USDT-SWAP | 0.39370 | 0.39950/0.39020 | 0.39020 | sup 0.37840 (ha 7 candles) | 0.00566 | -0.0093% | — | sem_zona |
| 2026-09-14 18:05 | SUI-USDT-SWAP | 0.74080 | 0.74770/0.73490 | 0.73510 | sup 0.71450 (ha 7 candles) | 0.00942 | 0.0064% | B/venda@0.73050 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-14 18:05 | UNI-USDT-SWAP | 6.7180 | 6.7910/6.6680 | 6.6880 | — | 0.10843 | 0.0100% | B/compra@6.7120 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 18:05 | LINK-USDT-SWAP | 11.75 | 11.96/11.73 | 11.73 | sup 11.24 (ha 7 candles) | 0.12357 | 0.0086% | B/venda@11.83 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 19:05 | BTC-USDT-SWAP | 78728.2 | 79088.9/78710.0 | 78956.3 | sup 77438.4 (ha 8 candles) | 483.57 | 0.0044% | B/venda@79387.8 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-14 19:05 | ETH-USDT-SWAP | 2545.9 | 2571.1/2538.0 | 2538.6 | — | 24.20 | 0.0034% | B/venda@2536.9 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 19:05 | SOL-USDT-SWAP | 103.15 | 104.01/102.91 | 103.21 | res 102.31 (ha 12 candles) | 0.90786 | 0.0100% | — | sem_zona |
| 2026-09-14 19:05 | XRP-USDT-SWAP | 1.4425 | 1.4638/1.4412 | 1.4635 | — | 0.02122 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-09-14 19:05 | DOGE-USDT-SWAP | 0.08433 | 0.08514/0.08431 | 0.08467 | sup 0.08307 (ha 8 candles) | 0.00077 | 0.0100% | B/venda@0.08533 (1t/1c) | zona_mapeada_setup_B |
| 2026-09-14 19:05 | ARB-USDT-SWAP | 0.13598 | 0.14078/0.13590 | 0.14014 | sup 0.13284 (ha 8 candles) | 0.00249 | 0.0099% | — | sem_zona |
| 2026-09-14 19:05 | WLD-USDT-SWAP | 0.38780 | 0.39400/0.38720 | 0.39020 | sup 0.37840 (ha 8 candles) | 0.00591 | -0.0079% | B/venda@0.38450 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 19:05 | SUI-USDT-SWAP | 0.73040 | 0.74110/0.72980 | 0.73510 | sup 0.71450 (ha 8 candles) | 0.00989 | 0.0099% | — | descartado_rr_baixo_setup_B |
| 2026-09-14 19:05 | UNI-USDT-SWAP | 6.5510 | 6.7210/6.5460 | 6.6880 | — | 0.11586 | 0.0100% | — | invalidado_setup_B |
| 2026-09-14 19:05 | LINK-USDT-SWAP | 11.64 | 11.75/11.63 | 11.73 | sup 11.24 (ha 8 candles) | 0.12814 | 0.0045% | B/venda@11.83 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-14 20:05 | BTC-USDT-SWAP | 78516.1 | 78818.3/78460.7 | 78956.3 | sup 77438.4 (ha 9 candles) | 483.86 | 0.0034% | B/venda@79387.8 (0t/2c) | zona_mapeada_setup_B |
| 2026-09-14 20:05 | ETH-USDT-SWAP | 2532.2 | 2556.2/2530.9 | 2538.6 | — | 24.73 | 0.0051% | — | descartado_rr_baixo_setup_B |
| 2026-09-14 20:05 | SOL-USDT-SWAP | 102.84 | 103.53/102.75 | 103.21 | res 102.31 (ha 13 candles) | 0.92714 | 0.0100% | — | sem_zona |
| 2026-09-14 20:05 | XRP-USDT-SWAP | 1.4352 | 1.4530/1.4345 | 1.4635 | — | 0.02184 | 0.0100% | B/venda@1.4323 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 20:05 | DOGE-USDT-SWAP | 0.08403 | 0.08464/0.08393 | 0.08467 | sup 0.08307 (ha 9 candles) | 0.00079 | 0.0100% | B/venda@0.08533 (1t/2c) | zona_mapeada_setup_B |
| 2026-09-14 20:05 | ARB-USDT-SWAP | 0.13409 | 0.13609/0.13392 | 0.14014 | sup 0.13284 (ha 9 candles) | 0.00253 | 0.0078% | — | sem_zona |
| 2026-09-14 20:05 | WLD-USDT-SWAP | 0.38670 | 0.39010/0.38540 | 0.39020 | sup 0.37840 (ha 9 candles) | 0.00591 | -0.0057% | — | invalidado_setup_B |
| 2026-09-14 20:05 | SUI-USDT-SWAP | 0.72520 | 0.73330/0.72370 | 0.73510 | sup 0.71450 (ha 9 candles) | 0.00993 | 0.0100% | — | sem_zona |
| 2026-09-14 20:05 | UNI-USDT-SWAP | 6.5340 | 6.5820/6.5010 | 6.6880 | — | 0.11600 | 0.0100% | B/venda@6.5300 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 20:05 | LINK-USDT-SWAP | 11.56 | 11.69/11.56 | 11.73 | sup 11.24 (ha 9 candles) | 0.13043 | 0.0016% | B/venda@11.83 (0t/2c) | zona_mapeada_setup_B |
| 2026-09-14 21:05 | BTC-USDT-SWAP | 78158.4 | 78530.1/78093.0 | 78158.4 | sup 77438.4 (ha 10 candles) | 458.30 | 0.0028% | B/venda@79387.8 (0t/3c) | zona_mapeada_setup_B |
| 2026-09-14 21:05 | ETH-USDT-SWAP | 2514.2 | 2533.8/2512.0 | 2514.2 | — | 24.58 | 0.0057% | B/venda@2523.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 21:05 | SOL-USDT-SWAP | 102.50 | 102.96/102.38 | 102.50 | res 104.78 (ha 3 candles) | 0.88714 | 0.0100% | — | sem_zona |
| 2026-09-14 21:05 | XRP-USDT-SWAP | 1.4229 | 1.4374/1.4182 | 1.4229 | — | 0.02115 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-09-14 21:05 | DOGE-USDT-SWAP | 0.08360 | 0.08414/0.08355 | 0.08360 | sup 0.08307 (ha 10 candles) | 0.00075 | 0.0100% | B/venda@0.08533 (1t/3c) | zona_mapeada_setup_B |
| 2026-09-14 21:05 | ARB-USDT-SWAP | 0.13360 | 0.13491/0.13261 | 0.13360 | sup 0.13284 (ha 10 candles) | 0.00249 | 0.0068% | — | sem_zona |
| 2026-09-14 21:05 | WLD-USDT-SWAP | 0.38510 | 0.38740/0.38480 | 0.38510 | sup 0.37840 (ha 10 candles) | 0.00556 | -0.0060% | B/venda@0.38910 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 21:05 | SUI-USDT-SWAP | 0.72050 | 0.72650/0.71970 | 0.72050 | sup 0.71450 (ha 10 candles) | 0.00971 | 0.0100% | — | sem_zona |
| 2026-09-14 21:05 | UNI-USDT-SWAP | 6.5270 | 6.6070/6.5080 | 6.5270 | — | 0.11414 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-09-14 21:05 | LINK-USDT-SWAP | 11.51 | 11.58/11.49 | 11.51 | sup 11.24 (ha 10 candles) | 0.12479 | -0.0001% | B/venda@11.83 (0t/3c) | zona_mapeada_setup_B |
| 2026-09-14 22:05 | BTC-USDT-SWAP | 77928.8 | 78230.7/77905.9 | 78158.4 | sup 77438.4 (ha 11 candles) | 462.16 | 0.0041% | B/venda@79387.8 (0t/4c) | zona_mapeada_setup_B |
| 2026-09-14 22:05 | ETH-USDT-SWAP | 2514.8 | 2516.5/2505.1 | 2514.2 | — | 24.54 | 0.0053% | B/venda@2523.0 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-14 22:05 | SOL-USDT-SWAP | 102.40 | 102.81/102.33 | 102.50 | res 104.78 (ha 4 candles) | 0.89786 | 0.0100% | — | sem_zona |
| 2026-09-14 22:06 | XRP-USDT-SWAP | 1.4188 | 1.4270/1.4147 | 1.4229 | — | 0.02103 | 0.0100% | — | sem_zona |
| 2026-09-14 22:06 | DOGE-USDT-SWAP | 0.08369 | 0.08386/0.08350 | 0.08360 | sup 0.08307 (ha 11 candles) | 0.00076 | 0.0100% | B/venda@0.08533 (1t/4c) | zona_mapeada_setup_B |
| 2026-09-14 22:06 | ARB-USDT-SWAP | 0.13284 | 0.13400/0.13141 | 0.13360 | sup 0.13284 (ha 11 candles) | 0.00256 | 0.0069% | — | sem_zona |
| 2026-09-14 22:06 | WLD-USDT-SWAP | 0.38560 | 0.38740/0.38390 | 0.38510 | sup 0.37840 (ha 11 candles) | 0.00558 | -0.0108% | B/venda@0.38910 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-14 22:06 | SUI-USDT-SWAP | 0.71880 | 0.72200/0.71670 | 0.72050 | sup 0.71450 (ha 11 candles) | 0.00974 | 0.0100% | — | sem_zona |
| 2026-09-14 22:06 | UNI-USDT-SWAP | 6.6880 | 6.7080/6.5190 | 6.5270 | — | 0.12307 | 0.0055% | — | sem_zona |
| 2026-09-14 22:06 | LINK-USDT-SWAP | 11.56 | 11.57/11.50 | 11.51 | sup 11.24 (ha 11 candles) | 0.12486 | -0.0007% | B/venda@11.83 (0t/4c) | zona_mapeada_setup_B |
| 2026-09-14 23:05 | BTC-USDT-SWAP | 77876.1 | 78054.1/77710.1 | 78158.4 | sup 77438.4 (ha 12 candles) | 469.24 | 0.0058% | B/venda@79387.8 (0t/5c) | zona_mapeada_setup_B |
| 2026-09-14 23:05 | ETH-USDT-SWAP | 2514.2 | 2518.7/2506.8 | 2514.2 | — | 24.53 | 0.0043% | B/venda@2523.0 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-14 23:05 | SOL-USDT-SWAP | 102.21 | 102.55/102.10 | 102.50 | res 104.78 (ha 5 candles) | 0.88643 | 0.0084% | B/compra@101.61 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-14 23:05 | XRP-USDT-SWAP | 1.4216 | 1.4254/1.4147 | 1.4229 | — | 0.02092 | 0.0100% | — | sem_zona |
| 2026-09-14 23:05 | DOGE-USDT-SWAP | 0.08374 | 0.08393/0.08347 | 0.08360 | sup 0.08307 (ha 12 candles) | 0.00076 | 0.0100% | B/venda@0.08533 (1t/5c) | zona_mapeada_setup_B |
| 2026-09-14 23:05 | ARB-USDT-SWAP | 0.13454 | 0.13474/0.13254 | 0.13360 | sup 0.13284 (ha 12 candles) | 0.00264 | 0.0068% | — | sem_zona |
| 2026-09-14 23:05 | WLD-USDT-SWAP | 0.38240 | 0.38570/0.38200 | 0.38510 | sup 0.37840 (ha 12 candles) | 0.00555 | -0.0104% | B/venda@0.38910 (0t/2c) | zona_mapeada_setup_B |
| 2026-09-14 23:05 | SUI-USDT-SWAP | 0.71900 | 0.72130/0.71670 | 0.72050 | sup 0.71450 (ha 12 candles) | 0.00943 | 0.0100% | — | sem_zona |
| 2026-09-14 23:05 | UNI-USDT-SWAP | 6.6690 | 6.7380/6.6120 | 6.5270 | — | 0.12779 | -0.0032% | — | sem_zona |
| 2026-09-14 23:05 | LINK-USDT-SWAP | 11.59 | 11.61/11.54 | 11.51 | sup 11.24 (ha 12 candles) | 0.12507 | -0.0009% | B/venda@11.83 (0t/5c) | zona_mapeada_setup_B |
| 2026-09-15 00:05 | BTC-USDT-SWAP | 77873.7 | 77991.5/77750.0 | 78158.4 | sup 77438.4 (ha 13 candles) | 452.02 | 0.0059% | B/venda@79387.8 (0t/6c) | zona_mapeada_setup_B |
| 2026-09-15 00:05 | ETH-USDT-SWAP | 2511.3 | 2518.6/2508.1 | 2514.2 | — | 24.15 | 0.0035% | — | descartado_rr_baixo_setup_B |
| 2026-09-15 00:05 | SOL-USDT-SWAP | 101.94 | 102.35/101.93 | 102.50 | res 104.78 (ha 6 candles) | 0.85714 | 0.0074% | B/compra@101.61 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-15 00:05 | XRP-USDT-SWAP | 1.4229 | 1.4298/1.4214 | 1.4229 | — | 0.02065 | 0.0100% | — | sem_zona |
| 2026-09-15 00:05 | DOGE-USDT-SWAP | 0.08376 | 0.08387/0.08367 | 0.08360 | sup 0.08307 (ha 13 candles) | 0.00071 | 0.0097% | B/venda@0.08533 (1t/6c) | zona_mapeada_setup_B |
| 2026-09-15 00:05 | ARB-USDT-SWAP | 0.13400 | 0.13460/0.13328 | 0.13360 | sup 0.13284 (ha 13 candles) | 0.00255 | 0.0031% | — | sem_zona |
| 2026-09-15 00:05 | WLD-USDT-SWAP | 0.38100 | 0.38280/0.38030 | 0.38510 | sup 0.37840 (ha 13 candles) | 0.00530 | -0.0112% | B/venda@0.38910 (0t/3c) | zona_mapeada_setup_B |
| 2026-09-15 00:05 | SUI-USDT-SWAP | 0.72090 | 0.72270/0.71790 | 0.72050 | sup 0.71450 (ha 13 candles) | 0.00919 | 0.0100% | — | sem_zona |
| 2026-09-15 00:05 | UNI-USDT-SWAP | 6.6170 | 6.6930/6.5580 | 6.5270 | — | 0.13164 | -0.0057% | B/venda@6.5670 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-15 00:05 | LINK-USDT-SWAP | 11.55 | 11.63/11.55 | 11.51 | sup 11.49 (ha 3 candles) | 0.12243 | 0.0019% | B/venda@11.83 (0t/6c) | zona_mapeada_setup_B |
| 2026-09-15 01:05 | BTC-USDT-SWAP | 77650.1 | 77873.8/77609.0 | 77650.1 | sup 77438.4 (ha 14 candles) | 397.06 | 0.0059% | B/venda@79387.8 (0t/7c) | zona_mapeada_setup_B |
| 2026-09-15 01:05 | ETH-USDT-SWAP | 2497.7 | 2511.3/2493.4 | 2497.7 | — | 23.30 | 0.0019% | B/venda@2489.8 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-15 01:05 | SOL-USDT-SWAP | 101.50 | 101.94/101.20 | 101.50 | res 104.78 (ha 7 candles) | 0.82000 | 0.0064% | B/compra@101.61 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-15 01:05 | XRP-USDT-SWAP | 1.4153 | 1.4228/1.4110 | 1.4153 | — | 0.02004 | 0.0100% | — | sem_zona |
| 2026-09-15 01:05 | DOGE-USDT-SWAP | 0.08325 | 0.08376/0.08323 | 0.08325 | sup 0.08307 (ha 14 candles) | 0.00066 | 0.0083% | B/venda@0.08533 (1t/7c) | zona_mapeada_setup_B |
| 2026-09-15 01:05 | ARB-USDT-SWAP | 0.13296 | 0.13400/0.13234 | 0.13296 | sup 0.13141 (ha 3 candles) | 0.00245 | 0.0035% | — | sem_zona |
| 2026-09-15 01:05 | WLD-USDT-SWAP | 0.37800 | 0.38090/0.37670 | 0.37800 | sup 0.37840 (ha 14 candles) | 0.00508 | -0.0122% | B/venda@0.38910 (0t/4c) | zona_mapeada_setup_B |
| 2026-09-15 01:05 | SUI-USDT-SWAP | 0.71600 | 0.72090/0.71420 | 0.71600 | sup 0.71450 (ha 14 candles) | 0.00881 | 0.0100% | — | sem_zona |
| 2026-09-15 01:05 | UNI-USDT-SWAP | 6.5490 | 6.6180/6.4710 | 6.5490 | — | 0.12571 | -0.0049% | B/venda@6.5670 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-15 01:05 | LINK-USDT-SWAP | 11.50 | 11.56/11.45 | 11.50 | sup 11.49 (ha 4 candles) | 0.11671 | 0.0054% | B/venda@11.83 (0t/7c) | zona_mapeada_setup_B |
| 2026-09-15 01:05 | BTC-USDT-SWAP | 77650.1 | 77873.8/77609.0 | 77650.1 | sup 77438.4 (ha 14 candles) | 397.06 | 0.0059% | B/venda@79387.8 (0t/7c) | zona_mapeada_setup_B |
| 2026-09-15 01:05 | ETH-USDT-SWAP | 2497.7 | 2511.3/2493.4 | 2497.7 | — | 23.30 | 0.0019% | B/venda@2489.8 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-15 01:05 | SOL-USDT-SWAP | 101.50 | 101.94/101.20 | 101.50 | res 104.78 (ha 7 candles) | 0.82000 | 0.0064% | B/compra@101.61 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-15 01:05 | XRP-USDT-SWAP | 1.4153 | 1.4228/1.4110 | 1.4153 | — | 0.02004 | 0.0100% | — | sem_zona |
| 2026-09-15 01:05 | DOGE-USDT-SWAP | 0.08325 | 0.08376/0.08323 | 0.08325 | sup 0.08307 (ha 14 candles) | 0.00066 | 0.0083% | B/venda@0.08533 (1t/7c) | zona_mapeada_setup_B |
| 2026-09-15 01:05 | ARB-USDT-SWAP | 0.13296 | 0.13400/0.13234 | 0.13296 | sup 0.13141 (ha 3 candles) | 0.00245 | 0.0035% | — | sem_zona |
| 2026-09-15 01:05 | WLD-USDT-SWAP | 0.37800 | 0.38090/0.37670 | 0.37800 | sup 0.37840 (ha 14 candles) | 0.00508 | -0.0122% | B/venda@0.38910 (0t/4c) | zona_mapeada_setup_B |
| 2026-09-15 01:05 | SUI-USDT-SWAP | 0.71600 | 0.72090/0.71420 | 0.71600 | sup 0.71450 (ha 14 candles) | 0.00881 | 0.0100% | — | sem_zona |
| 2026-09-15 01:05 | UNI-USDT-SWAP | 6.5490 | 6.6180/6.4710 | 6.5490 | — | 0.12571 | -0.0049% | B/venda@6.5670 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-15 01:05 | LINK-USDT-SWAP | 11.50 | 11.56/11.45 | 11.50 | sup 11.49 (ha 4 candles) | 0.11671 | 0.0054% | B/venda@11.83 (0t/7c) | zona_mapeada_setup_B |
| 2026-09-15 02:05 | BTC-USDT-SWAP | 77540.0 | 77712.9/77505.1 | 77650.1 | sup 77438.4 (ha 15 candles) | 373.14 | 0.0072% | — | zona_expirada_setup_B |
| 2026-09-15 02:05 | ETH-USDT-SWAP | 2489.5 | 2499.4/2488.5 | 2497.7 | — | 22.51 | 0.0014% | — | descartado_rr_baixo_setup_B |
| 2026-09-15 02:05 | SOL-USDT-SWAP | 101.22 | 101.65/101.11 | 101.50 | res 104.78 (ha 8 candles) | 0.79786 | 0.0056% | — | invalidado_setup_B |
| 2026-09-15 02:05 | XRP-USDT-SWAP | 1.4130 | 1.4179/1.4067 | 1.4153 | — | 0.02003 | 0.0100% | — | sem_zona |
| 2026-09-15 02:05 | DOGE-USDT-SWAP | 0.08312 | 0.08338/0.08305 | 0.08325 | sup 0.08307 (ha 15 candles) | 0.00063 | 0.0059% | — | zona_expirada_setup_B |
| 2026-09-15 02:05 | ARB-USDT-SWAP | 0.13262 | 0.13339/0.13185 | 0.13296 | sup 0.13141 (ha 4 candles) | 0.00242 | 0.0052% | — | sem_zona |
| 2026-09-15 02:05 | WLD-USDT-SWAP | 0.37820 | 0.37950/0.37740 | 0.37800 | sup 0.37840 (ha 15 candles) | 0.00485 | -0.0124% | B/venda@0.38910 (0t/5c) | zona_mapeada_setup_B |
| 2026-09-15 02:05 | SUI-USDT-SWAP | 0.71230 | 0.71780/0.71060 | 0.71600 | sup 0.71450 (ha 15 candles) | 0.00859 | 0.0100% | A/venda@0.71450 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-15 02:05 | UNI-USDT-SWAP | 6.6250 | 6.6780/6.5420 | 6.5490 | — | 0.13000 | -0.0021% | — | invalidado_setup_B |
| 2026-09-15 02:05 | LINK-USDT-SWAP | 11.44 | 11.51/11.43 | 11.50 | sup 11.49 (ha 5 candles) | 0.11500 | 0.0059% | — | zona_expirada_setup_B |
| 2026-09-15 03:05 | BTC-USDT-SWAP | 77591.5 | 77635.8/77260.0 | 77650.1 | sup 77438.4 (ha 16 candles) | 372.25 | 0.0060% | B/venda@77493.8 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-15 03:05 | ETH-USDT-SWAP | 2495.1 | 2496.8/2476.2 | 2497.7 | — | 22.77 | 0.0003% | — | sem_zona |
| 2026-09-15 03:05 | SOL-USDT-SWAP | 101.26 | 101.35/100.52 | 101.50 | res 104.78 (ha 9 candles) | 0.78857 | 0.0030% | — | sem_zona |
| 2026-09-15 03:05 | XRP-USDT-SWAP | 1.4078 | 1.4132/1.3987 | 1.4153 | — | 0.01996 | 0.0100% | B/venda@1.3972 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-15 03:05 | DOGE-USDT-SWAP | 0.08313 | 0.08329/0.08263 | 0.08325 | sup 0.08307 (ha 16 candles) | 0.00063 | 0.0049% | — | sem_zona |
| 2026-09-15 03:05 | ARB-USDT-SWAP | 0.13423 | 0.13480/0.13122 | 0.13296 | sup 0.13141 (ha 5 candles) | 0.00254 | 0.0054% | — | sem_zona |
| 2026-09-15 03:05 | WLD-USDT-SWAP | 0.37560 | 0.37860/0.37370 | 0.37800 | sup 0.37840 (ha 16 candles) | 0.00479 | -0.0110% | B/venda@0.38910 (0t/6c) | zona_mapeada_setup_B |
| 2026-09-15 03:05 | SUI-USDT-SWAP | 0.71140 | 0.71280/0.70520 | 0.71600 | sup 0.71450 (ha 16 candles) | 0.00836 | 0.0100% | A/venda@0.71450 (1t/0c) | zona_mapeada_setup_A |
| 2026-09-15 03:05 | UNI-USDT-SWAP | 6.7200 | 6.7750/6.5750 | 6.5490 | — | 0.13914 | 0.0012% | B/compra@6.7120 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-15 03:05 | LINK-USDT-SWAP | 11.48 | 11.50/11.37 | 11.50 | sup 11.49 (ha 6 candles) | 0.11536 | 0.0062% | A/venda@11.49 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-15 04:05 | BTC-USDT-SWAP | 77245.3 | 77699.9/77142.7 | 77650.1 | sup 77438.4 (ha 17 candles) | 376.04 | 0.0046% | — | descartado_rr_baixo_setup_B |
| 2026-09-15 04:05 | ETH-USDT-SWAP | 2484.9 | 2500.4/2480.4 | 2497.7 | — | 21.73 | 0.0000% | — | sem_zona |
| 2026-09-15 04:05 | SOL-USDT-SWAP | 100.84 | 101.54/100.68 | 101.50 | res 104.78 (ha 10 candles) | 0.77643 | 0.0014% | — | sem_zona |
| 2026-09-15 04:05 | XRP-USDT-SWAP | 1.3991 | 1.4101/1.3952 | 1.4153 | — | 0.01950 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-09-15 04:05 | DOGE-USDT-SWAP | 0.08264 | 0.08326/0.08236 | 0.08325 | sup 0.08307 (ha 17 candles) | 0.00063 | 0.0024% | A/venda@0.08307 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-15 04:05 | ARB-USDT-SWAP | 0.13333 | 0.13475/0.13275 | 0.13296 | sup 0.13141 (ha 6 candles) | 0.00251 | 0.0051% | — | sem_zona |
| 2026-09-15 04:05 | WLD-USDT-SWAP | 0.37340 | 0.37620/0.37230 | 0.37800 | sup 0.37840 (ha 17 candles) | 0.00469 | -0.0099% | B/venda@0.38910 (0t/7c) | zona_mapeada_setup_B |
| 2026-09-15 04:05 | SUI-USDT-SWAP | 0.70810 | 0.71270/0.70570 | 0.71600 | sup 0.71450 (ha 17 candles) | 0.00796 | 0.0100% | — | descartado_rr_baixo_setup_A |
| 2026-09-15 04:05 | UNI-USDT-SWAP | 6.5930 | 6.7380/6.5680 | 6.5490 | — | 0.14514 | 0.0037% | — | invalidado_setup_B |
| 2026-09-15 04:05 | LINK-USDT-SWAP | 11.41 | 11.51/11.37 | 11.50 | sup 11.49 (ha 7 candles) | 0.11607 | 0.0056% | — | descartado_rr_baixo_setup_A |
| 2026-09-15 05:05 | BTC-USDT-SWAP | 76886.2 | 77277.5/76824.2 | 76886.2 | sup 77438.4 (ha 18 candles) | 382.98 | 0.0033% | — | sem_zona |
| 2026-09-15 05:05 | ETH-USDT-SWAP | 2472.9 | 2484.9/2467.1 | 2472.9 | — | 22.06 | -0.0001% | B/compra@2460.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-15 05:05 | SOL-USDT-SWAP | 100.38 | 101.00/100.28 | 100.38 | res 104.78 (ha 11 candles) | 0.77000 | -0.0011% | B/compra@100.15 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-15 05:05 | XRP-USDT-SWAP | 1.3935 | 1.4037/1.3913 | 1.3935 | — | 0.01856 | 0.0100% | B/compra@1.3804 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-15 05:05 | DOGE-USDT-SWAP | 0.08248 | 0.08292/0.08237 | 0.08248 | sup 0.08307 (ha 18 candles) | 0.00062 | 0.0004% | — | descartado_rr_baixo_setup_A |
| 2026-09-15 05:05 | ARB-USDT-SWAP | 0.13271 | 0.13383/0.13220 | 0.13271 | sup 0.13141 (ha 7 candles) | 0.00226 | 0.0068% | — | sem_zona |
| 2026-09-15 05:05 | WLD-USDT-SWAP | 0.37250 | 0.37560/0.37180 | 0.37250 | sup 0.37840 (ha 18 candles) | 0.00444 | -0.0065% | — | zona_expirada_setup_B |
| 2026-09-15 05:05 | SUI-USDT-SWAP | 0.70460 | 0.71050/0.70340 | 0.70460 | sup 0.71450 (ha 18 candles) | 0.00796 | 0.0100% | — | sem_zona |
| 2026-09-15 05:05 | UNI-USDT-SWAP | 6.5670 | 6.6680/6.5330 | 6.5670 | — | 0.14907 | 0.0045% | — | sem_zona |
| 2026-09-15 05:05 | LINK-USDT-SWAP | 11.33 | 11.43/11.32 | 11.33 | sup 11.49 (ha 8 candles) | 0.11357 | 0.0048% | — | sem_zona |
| 2026-09-15 06:05 | BTC-USDT-SWAP | 76968.3 | 76979.9/76666.0 | 76886.2 | sup 77438.4 (ha 19 candles) | 370.62 | 0.0049% | — | sem_zona |
| 2026-09-15 06:05 | ETH-USDT-SWAP | 2476.2 | 2476.5/2463.1 | 2472.9 | — | 21.94 | 0.0011% | — | descartado_rr_baixo_setup_B |
| 2026-09-15 06:05 | SOL-USDT-SWAP | 100.59 | 100.61/100.01 | 100.38 | res 104.78 (ha 12 candles) | 0.74571 | -0.0026% | — | descartado_rr_baixo_setup_B |
| 2026-09-15 06:05 | XRP-USDT-SWAP | 1.3973 | 1.3975/1.3853 | 1.3935 | — | 0.01584 | 0.0100% | B/compra@1.3804 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-15 06:05 | DOGE-USDT-SWAP | 0.08261 | 0.08264/0.08225 | 0.08248 | sup 0.08307 (ha 19 candles) | 0.00060 | -0.0001% | — | sem_zona |
| 2026-09-15 06:05 | ARB-USDT-SWAP | 0.13316 | 0.13345/0.13210 | 0.13271 | sup 0.13122 (ha 3 candles) | 0.00223 | 0.0091% | — | sem_zona |
| 2026-09-15 06:05 | WLD-USDT-SWAP | 0.37510 | 0.37520/0.37060 | 0.37250 | sup 0.37840 (ha 19 candles) | 0.00444 | -0.0058% | A/venda@0.37840 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-15 06:05 | SUI-USDT-SWAP | 0.70860 | 0.70880/0.70200 | 0.70460 | sup 0.71450 (ha 19 candles) | 0.00758 | 0.0100% | — | sem_zona |
| 2026-09-15 06:05 | UNI-USDT-SWAP | 6.6310 | 6.6330/6.5510 | 6.5670 | — | 0.14036 | 0.0083% | B/venda@6.5300 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-15 06:05 | LINK-USDT-SWAP | 11.40 | 11.40/11.29 | 11.33 | sup 11.49 (ha 9 candles) | 0.11171 | 0.0033% | — | sem_zona |
| 2026-09-15 07:05 | BTC-USDT-SWAP | 76950.8 | 77037.2/76837.0 | 76886.2 | sup 77438.4 (ha 20 candles) | 362.87 | 0.0069% | — | sem_zona |
| 2026-09-15 07:05 | ETH-USDT-SWAP | 2473.2 | 2479.4/2471.7 | 2472.9 | — | 21.35 | 0.0003% | — | sem_zona |
| 2026-09-15 07:05 | SOL-USDT-SWAP | 100.76 | 101.04/100.45 | 100.38 | res 104.78 (ha 13 candles) | 0.73643 | -0.0041% | — | sem_zona |
| 2026-09-15 07:05 | XRP-USDT-SWAP | 1.4017 | 1.4060/1.3951 | 1.3935 | — | 0.01491 | 0.0100% | B/compra@1.3804 (0t/2c) | zona_mapeada_setup_B |
| 2026-09-15 07:05 | DOGE-USDT-SWAP | 0.08259 | 0.08284/0.08250 | 0.08248 | sup 0.08307 (ha 20 candles) | 0.00059 | 0.0007% | — | sem_zona |
| 2026-09-15 07:05 | ARB-USDT-SWAP | 0.13419 | 0.13515/0.13290 | 0.13271 | sup 0.13122 (ha 4 candles) | 0.00226 | 0.0100% | — | sem_zona |
| 2026-09-15 07:05 | WLD-USDT-SWAP | 0.37380 | 0.37550/0.37350 | 0.37250 | sup 0.37840 (ha 20 candles) | 0.00419 | -0.0038% | A/venda@0.37840 (0t/1c) | zona_mapeada_setup_A |
| 2026-09-15 07:05 | SUI-USDT-SWAP | 0.71040 | 0.71350/0.70770 | 0.70460 | sup 0.71450 (ha 20 candles) | 0.00739 | 0.0100% | — | sem_zona |
| 2026-09-15 07:05 | UNI-USDT-SWAP | 6.6370 | 6.6740/6.4980 | 6.5670 | — | 0.14100 | 0.0064% | — | invalidado_setup_B |
| 2026-09-15 07:05 | LINK-USDT-SWAP | 11.38 | 11.42/11.36 | 11.33 | sup 11.49 (ha 10 candles) | 0.10836 | 0.0011% | — | sem_zona |
| 2026-09-15 08:05 | BTC-USDT-SWAP | 77024.9 | 77150.0/76844.0 | 76886.2 | sup 77438.4 (ha 21 candles) | 340.21 | 0.0084% | — | sem_zona |
| 2026-09-15 08:05 | ETH-USDT-SWAP | 2482.5 | 2485.8/2470.5 | 2472.9 | — | 16.99 | 0.0005% | — | sem_zona |
| 2026-09-15 08:05 | SOL-USDT-SWAP | 100.89 | 101.03/100.60 | 100.38 | res 104.78 (ha 14 candles) | 0.65143 | -0.0069% | — | sem_zona |
| 2026-09-15 08:05 | XRP-USDT-SWAP | 1.4018 | 1.4040/1.3967 | 1.3935 | — | 0.01336 | 0.0100% | B/compra@1.3804 (0t/3c) | zona_mapeada_setup_B |
| 2026-09-15 08:05 | DOGE-USDT-SWAP | 0.08274 | 0.08282/0.08251 | 0.08248 | sup 0.08307 (ha 21 candles) | 0.00051 | 0.0011% | — | sem_zona |
| 2026-09-15 08:05 | ARB-USDT-SWAP | 0.13571 | 0.13590/0.13402 | 0.13271 | sup 0.13122 (ha 5 candles) | 0.00224 | 0.0086% | — | sem_zona |
| 2026-09-15 08:05 | WLD-USDT-SWAP | 0.37400 | 0.37450/0.37210 | 0.37250 | sup 0.37840 (ha 21 candles) | 0.00370 | -0.0023% | A/venda@0.37840 (0t/2c) | zona_mapeada_setup_A |
| 2026-09-15 08:05 | SUI-USDT-SWAP | 0.71050 | 0.71260/0.70840 | 0.70460 | sup 0.71450 (ha 21 candles) | 0.00677 | 0.0100% | — | sem_zona |
| 2026-09-15 08:05 | UNI-USDT-SWAP | 6.7370 | 6.7370/6.6120 | 6.5670 | — | 0.14114 | 0.0063% | — | sem_zona |
| 2026-09-15 08:05 | LINK-USDT-SWAP | 11.38 | 11.39/11.35 | 11.33 | sup 11.49 (ha 11 candles) | 0.09529 | 0.0005% | — | sem_zona |
| 2026-09-15 09:05 | BTC-USDT-SWAP | 76889.1 | 77198.5/76800.0 | 76889.1 | — | 341.61 | 0.0084% | B/compra@76916.6 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-15 09:05 | ETH-USDT-SWAP | 2475.3 | 2487.2/2471.6 | 2475.3 | res 2615.0 (ha 15 candles) | 15.73 | 0.0007% | — | sem_zona |
| 2026-09-15 09:05 | SOL-USDT-SWAP | 100.77 | 100.95/100.34 | 100.77 | — | 0.61643 | -0.0090% | — | sem_zona |
| 2026-09-15 09:05 | XRP-USDT-SWAP | 1.4005 | 1.4028/1.3924 | 1.4005 | res 1.4914 (ha 15 candles) | 0.01249 | 0.0100% | B/compra@1.3804 (0t/4c) | zona_mapeada_setup_B |
| 2026-09-15 09:05 | DOGE-USDT-SWAP | 0.08248 | 0.08288/0.08223 | 0.08248 | — | 0.00050 | 0.0038% | B/compra@0.08213 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-15 09:05 | ARB-USDT-SWAP | 0.13717 | 0.13735/0.13446 | 0.13717 | sup 0.13122 (ha 6 candles) | 0.00210 | 0.0071% | — | sem_zona |
| 2026-09-15 09:05 | WLD-USDT-SWAP | 0.37410 | 0.37620/0.37010 | 0.37410 | sup 0.37840 (ha 22 candles) | 0.00365 | -0.0022% | A/venda@0.37840 (0t/3c) | zona_mapeada_setup_A |
| 2026-09-15 09:05 | SUI-USDT-SWAP | 0.70700 | 0.71270/0.70440 | 0.70700 | — | 0.00656 | 0.0071% | B/compra@0.70590 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-15 09:05 | UNI-USDT-SWAP | 6.6910 | 6.8310/6.6490 | 6.6910 | — | 0.14164 | 0.0076% | — | sem_zona |
| 2026-09-15 09:05 | LINK-USDT-SWAP | 11.38 | 11.40/11.32 | 11.38 | — | 0.09229 | -0.0018% | B/compra@11.44 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-15 10:05 | BTC-USDT-SWAP | 76915.5 | 77102.7/76813.2 | 76889.1 | — | 336.74 | 0.0082% | B/compra@76916.6 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-15 10:05 | ETH-USDT-SWAP | 2478.0 | 2485.0/2473.5 | 2475.3 | res 2615.0 (ha 16 candles) | 14.75 | 0.0010% | — | sem_zona |
| 2026-09-15 10:05 | SOL-USDT-SWAP | 100.92 | 101.16/100.74 | 100.77 | — | 0.59071 | -0.0094% | — | sem_zona |
| 2026-09-15 10:05 | XRP-USDT-SWAP | 1.4162 | 1.4214/1.3988 | 1.4005 | res 1.4914 (ha 16 candles) | 0.01278 | 0.0092% | B/compra@1.3804 (0t/5c) | zona_mapeada_setup_B |
| 2026-09-15 10:05 | DOGE-USDT-SWAP | 0.08277 | 0.08298/0.08242 | 0.08248 | — | 0.00049 | 0.0045% | B/compra@0.08213 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-15 10:05 | ARB-USDT-SWAP | 0.14076 | 0.14218/0.13602 | 0.13717 | sup 0.13122 (ha 7 candles) | 0.00238 | -0.0014% | — | sem_zona |
| 2026-09-15 10:05 | WLD-USDT-SWAP | 0.37560 | 0.37740/0.37380 | 0.37410 | sup 0.37840 (ha 23 candles) | 0.00357 | -0.0023% | A/venda@0.37840 (1t/0c) | zona_mapeada_setup_A |
| 2026-09-15 10:05 | SUI-USDT-SWAP | 0.71030 | 0.71300/0.70670 | 0.70700 | — | 0.00632 | 0.0039% | B/compra@0.70590 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-15 10:05 | UNI-USDT-SWAP | 6.7090 | 6.7940/6.6730 | 6.6910 | — | 0.14450 | 0.0063% | — | sem_zona |
| 2026-09-15 10:05 | LINK-USDT-SWAP | 11.41 | 11.45/11.36 | 11.38 | — | 0.08986 | -0.0022% | — | invalidado_setup_B |
| 2026-09-15 11:05 | BTC-USDT-SWAP | 76580.0 | 77098.0/76056.0 | 76889.1 | — | 379.95 | 0.0093% | — | invalidado_setup_B |
| 2026-09-15 11:05 | ETH-USDT-SWAP | 2452.8 | 2485.8/2430.3 | 2475.3 | res 2615.0 (ha 17 candles) | 17.16 | 0.0009% | B/compra@2442.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-15 11:05 | SOL-USDT-SWAP | 100.52 | 101.34/99.58 | 100.77 | — | 0.67500 | -0.0069% | — | sem_zona |
| 2026-09-15 11:05 | XRP-USDT-SWAP | 1.4144 | 1.4592/1.3946 | 1.4005 | res 1.4914 (ha 17 candles) | 0.01602 | 0.0084% | B/compra@1.3804 (0t/6c) | zona_mapeada_setup_B |
| 2026-09-15 11:05 | DOGE-USDT-SWAP | 0.08279 | 0.08337/0.08188 | 0.08248 | — | 0.00055 | 0.0025% | — | descartado_rr_baixo_setup_B |
| 2026-09-15 11:05 | ARB-USDT-SWAP | 0.14048 | 0.14392/0.13837 | 0.13717 | sup 0.13122 (ha 8 candles) | 0.00261 | -0.0029% | — | sem_zona |
| 2026-09-15 11:05 | WLD-USDT-SWAP | 0.37750 | 0.37880/0.37230 | 0.37410 | sup 0.37840 (ha 24 candles) | 0.00385 | 0.0028% | A/venda@0.37840 (2t/0c) | zona_mapeada_setup_A |
| 2026-09-15 11:05 | SUI-USDT-SWAP | 0.71030 | 0.71650/0.70240 | 0.70700 | — | 0.00684 | 0.0045% | B/compra@0.70590 (2t/0c) | zona_mapeada_setup_B |
| 2026-09-15 11:05 | UNI-USDT-SWAP | 6.4910 | 6.7370/6.4700 | 6.6910 | — | 0.15650 | 0.0051% | B/venda@6.3780 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-15 11:05 | LINK-USDT-SWAP | 11.38 | 11.53/11.30 | 11.38 | — | 0.09986 | 0.0031% | — | sem_zona |
| 2026-09-15 12:05 | BTC-USDT-SWAP | 75911.3 | 76661.8/75557.0 | 76889.1 | — | 435.66 | 0.0095% | B/compra@75866.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-15 12:05 | ETH-USDT-SWAP | 2406.7 | 2456.9/2387.0 | 2475.3 | res 2487.2 (ha 3 candles) | 21.33 | -0.0003% | — | invalidado_setup_B |
| 2026-09-15 12:05 | SOL-USDT-SWAP | 98.79 | 100.71/97.88 | 100.77 | — | 0.84286 | -0.0055% | B/compra@98.30 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-15 12:05 | XRP-USDT-SWAP | 1.3843 | 1.4164/1.3714 | 1.4005 | res 1.4914 (ha 18 candles) | 0.01836 | 0.0061% | B/compra@1.3804 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-15 12:05 | DOGE-USDT-SWAP | 0.08125 | 0.08292/0.08030 | 0.08248 | — | 0.00071 | 0.0014% | — | sem_zona |
| 2026-09-15 12:05 | ARB-USDT-SWAP | 0.13733 | 0.14073/0.13523 | 0.13717 | sup 0.13122 (ha 9 candles) | 0.00282 | -0.0077% | — | sem_zona |
| 2026-09-15 12:05 | WLD-USDT-SWAP | 0.36960 | 0.37830/0.36520 | 0.37410 | sup 0.37840 (ha 25 candles) | 0.00454 | -0.0005% | — | descartado_rr_baixo_setup_A |
| 2026-09-15 12:05 | SUI-USDT-SWAP | 0.69610 | 0.71180/0.68600 | 0.70700 | — | 0.00831 | 0.0020% | — | invalidado_setup_B |
| 2026-09-15 12:05 | UNI-USDT-SWAP | 6.2530 | 6.5200/6.1630 | 6.6910 | — | 0.16850 | 0.0021% | — | descartado_rr_baixo_setup_B |
| 2026-09-15 12:05 | LINK-USDT-SWAP | 11.18 | 11.41/11.03 | 11.38 | — | 0.12150 | 0.0055% | B/compra@11.22 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-15 13:05 | BTC-USDT-SWAP | 76474.0 | 76565.6/75792.1 | 76474.0 | — | 466.34 | 0.0081% | — | descartado_rr_baixo_setup_B |
| 2026-09-15 13:05 | ETH-USDT-SWAP | 2423.3 | 2431.5/2396.3 | 2423.3 | res 2487.2 (ha 4 candles) | 22.99 | -0.0007% | B/compra@2432.2 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-15 13:05 | SOL-USDT-SWAP | 99.32 | 99.71/98.49 | 99.32 | — | 0.89786 | -0.0037% | — | descartado_rr_baixo_setup_B |
| 2026-09-15 13:05 | XRP-USDT-SWAP | 1.3890 | 1.3972/1.3795 | 1.3890 | res 1.4914 (ha 19 candles) | 0.01886 | 0.0060% | B/compra@1.3804 (2t/0c) | zona_mapeada_setup_B |
| 2026-09-15 13:05 | DOGE-USDT-SWAP | 0.08164 | 0.08211/0.08106 | 0.08164 | — | 0.00076 | 0.0020% | — | sem_zona |
| 2026-09-15 13:05 | ARB-USDT-SWAP | 0.14895 | 0.15092/0.13707 | 0.14895 | sup 0.13122 (ha 10 candles) | 0.00365 | -0.0142% | B/venda@0.14674 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-15 13:05 | WLD-USDT-SWAP | 0.37140 | 0.37570/0.36870 | 0.37140 | sup 0.37840 (ha 26 candles) | 0.00477 | -0.0004% | B/venda@0.37490 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-15 13:05 | SUI-USDT-SWAP | 0.70140 | 0.70580/0.69480 | 0.70140 | — | 0.00876 | -0.0015% | B/compra@0.70270 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-15 13:05 | UNI-USDT-SWAP | 6.3250 | 6.3810/6.2380 | 6.3250 | — | 0.16971 | -0.0035% | — | sem_zona |
| 2026-09-15 13:05 | LINK-USDT-SWAP | 11.27 | 11.31/11.14 | 11.27 | — | 0.12850 | 0.0077% | — | descartado_rr_baixo_setup_B |
| 2026-09-15 14:05 | BTC-USDT-SWAP | 76353.5 | 76535.0/76225.7 | 76474.0 | — | 471.19 | 0.0072% | B/compra@76434.8 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-15 14:05 | ETH-USDT-SWAP | 2421.2 | 2424.8/2411.3 | 2423.3 | res 2487.2 (ha 5 candles) | 23.21 | -0.0010% | B/compra@2432.2 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-15 14:05 | SOL-USDT-SWAP | 99.04 | 99.40/98.83 | 99.32 | — | 0.90857 | -0.0026% | — | sem_zona |
| 2026-09-15 14:05 | XRP-USDT-SWAP | 1.3868 | 1.3924/1.3811 | 1.3890 | res 1.4592 (ha 3 candles) | 0.01906 | 0.0050% | — | zona_expirada_setup_B |
| 2026-09-15 14:05 | DOGE-USDT-SWAP | 0.08156 | 0.08180/0.08125 | 0.08164 | — | 0.00078 | 0.0048% | — | sem_zona |
| 2026-09-15 14:05 | ARB-USDT-SWAP | 0.14900 | 0.15616/0.14614 | 0.14895 | sup 0.13122 (ha 11 candles) | 0.00428 | -0.0160% | — | invalidado_setup_B |
| 2026-09-15 14:05 | WLD-USDT-SWAP | 0.37080 | 0.37280/0.36890 | 0.37140 | sup 0.37840 (ha 27 candles) | 0.00487 | 0.0012% | B/venda@0.37490 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-15 14:05 | SUI-USDT-SWAP | 0.70130 | 0.70390/0.69710 | 0.70140 | — | 0.00891 | -0.0040% | B/compra@0.70270 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-15 14:05 | UNI-USDT-SWAP | 6.4020 | 6.4540/6.3000 | 6.3250 | — | 0.17107 | -0.0051% | B/venda@6.5300 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-15 14:05 | LINK-USDT-SWAP | 11.26 | 11.30/11.19 | 11.27 | — | 0.13114 | 0.0097% | — | sem_zona |
| 2026-09-15 15:05 | BTC-USDT-SWAP | 76929.5 | 77324.9/76157.3 | 76474.0 | — | 535.67 | 0.0064% | — | descartado_rr_baixo_setup_B |
| 2026-09-15 15:05 | ETH-USDT-SWAP | 2440.1 | 2447.8/2411.5 | 2423.3 | res 2487.2 (ha 6 candles) | 24.52 | -0.0005% | — | descartado_rr_baixo_setup_B |
| 2026-09-15 15:05 | SOL-USDT-SWAP | 100.16 | 100.66/98.63 | 99.32 | — | 1.0007 | -0.0018% | B/compra@100.15 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-15 15:05 | XRP-USDT-SWAP | 1.4043 | 1.4126/1.3786 | 1.3890 | res 1.4592 (ha 4 candles) | 0.02064 | 0.0022% | B/compra@1.3907 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-15 15:05 | DOGE-USDT-SWAP | 0.08207 | 0.08250/0.08117 | 0.08164 | — | 0.00084 | 0.0077% | — | sem_zona |
| 2026-09-15 15:05 | ARB-USDT-SWAP | 0.15001 | 0.15328/0.14821 | 0.14895 | sup 0.13122 (ha 12 candles) | 0.00452 | -0.0136% | B/venda@0.15176 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-15 15:05 | WLD-USDT-SWAP | 0.37350 | 0.37650/0.36910 | 0.37140 | sup 0.36520 (ha 3 candles) | 0.00509 | -0.0011% | B/venda@0.37490 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-15 15:05 | SUI-USDT-SWAP | 0.70950 | 0.71160/0.69810 | 0.70140 | — | 0.00939 | -0.0039% | — | descartado_rr_baixo_setup_B |
| 2026-09-15 15:05 | UNI-USDT-SWAP | 6.4830 | 6.5730/6.3430 | 6.3250 | — | 0.17700 | -0.0053% | B/venda@6.5300 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-15 15:05 | LINK-USDT-SWAP | 11.31 | 11.41/11.19 | 11.27 | — | 0.13957 | 0.0100% | — | sem_zona |
| 2026-09-15 16:05 | BTC-USDT-SWAP | 75957.2 | 77183.3/74896.6 | 76474.0 | — | 684.16 | 0.0055% | B/compra@75866.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-15 16:05 | ETH-USDT-SWAP | 2401.7 | 2446.5/2356.2 | 2423.3 | res 2487.2 (ha 7 candles) | 30.19 | -0.0022% | B/compra@2404.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-15 16:05 | SOL-USDT-SWAP | 98.11 | 100.30/95.66 | 99.32 | — | 1.2936 | -0.0027% | — | invalidado_setup_B |
| 2026-09-15 16:05 | XRP-USDT-SWAP | 1.3246 | 1.4066/1.2877 | 1.3890 | res 1.4592 (ha 5 candles) | 0.02834 | 0.0049% | — | invalidado_setup_B |
| 2026-09-15 16:05 | DOGE-USDT-SWAP | 0.08077 | 0.08243/0.07835 | 0.08164 | — | 0.00111 | 0.0100% | B/compra@0.08001 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-15 16:05 | ARB-USDT-SWAP | 0.14540 | 0.15056/0.13944 | 0.14895 | sup 0.13122 (ha 13 candles) | 0.00520 | -0.0089% | B/venda@0.15176 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-15 16:05 | WLD-USDT-SWAP | 0.36730 | 0.37630/0.35520 | 0.37140 | sup 0.36520 (ha 4 candles) | 0.00645 | -0.0055% | B/venda@0.37490 (2t/0c) | zona_mapeada_setup_B |
| 2026-09-15 16:05 | SUI-USDT-SWAP | 0.69350 | 0.71100/0.67160 | 0.70140 | — | 0.01169 | -0.0026% | B/compra@0.69550 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-15 16:05 | UNI-USDT-SWAP | 6.3960 | 6.5270/6.1880 | 6.3250 | — | 0.19150 | -0.0029% | B/venda@6.5300 (2t/0c) | zona_mapeada_setup_B |
| 2026-09-15 16:05 | LINK-USDT-SWAP | 11.10 | 11.35/10.79 | 11.27 | — | 0.17386 | 0.0100% | B/compra@11.05 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-15 17:05 | BTC-USDT-SWAP | 76144.9 | 76277.0/75763.1 | 76144.9 | — | 694.03 | 0.0034% | — | CONFIRMADO_setup_B |
| 2026-09-15 17:05 | ETH-USDT-SWAP | 2415.5 | 2419.0/2396.2 | 2415.5 | res 2487.2 (ha 8 candles) | 30.36 | -0.0028% | — | CONFIRMADO_setup_B |
| 2026-09-15 17:05 | SOL-USDT-SWAP | 97.82 | 98.60/97.43 | 97.82 | — | 1.3179 | -0.0041% | B/compra@97.77 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-15 17:05 | XRP-USDT-SWAP | 1.2955 | 1.3294/1.2932 | 1.2955 | res 1.4592 (ha 6 candles) | 0.02989 | 0.0100% | B/compra@1.3151 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-15 17:05 | DOGE-USDT-SWAP | 0.08084 | 0.08120/0.08042 | 0.08084 | — | 0.00111 | 0.0100% | B/compra@0.08001 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-15 17:05 | ARB-USDT-SWAP | 0.14872 | 0.14965/0.14358 | 0.14872 | sup 0.13122 (ha 14 candles) | 0.00538 | -0.0042% | B/venda@0.15176 (0t/2c) | zona_mapeada_setup_B |
| 2026-09-15 17:05 | WLD-USDT-SWAP | 0.36770 | 0.36950/0.36410 | 0.36770 | sup 0.36520 (ha 5 candles) | 0.00649 | -0.0060% | B/venda@0.37490 (2t/1c) | zona_mapeada_setup_B |
| 2026-09-15 17:05 | SUI-USDT-SWAP | 0.69070 | 0.69680/0.68380 | 0.69070 | — | 0.01208 | -0.0028% | — | invalidado_setup_B |
| 2026-09-15 17:05 | UNI-USDT-SWAP | 6.4020 | 6.4350/6.3310 | 6.4020 | — | 0.18464 | -0.0026% | B/venda@6.5300 (2t/1c) | zona_mapeada_setup_B |
| 2026-09-15 17:05 | LINK-USDT-SWAP | 11.09 | 11.17/11.04 | 11.09 | — | 0.17400 | 0.0100% | B/compra@11.05 (1t/0c) | zona_mapeada_setup_B |
