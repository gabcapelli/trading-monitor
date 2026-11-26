# Log de Monitoramento Automatico -- Multi-Par (script gratuito, GitHub Actions)

> Gerado por script Python sem LLM (ver monitor/fetch_and_check.py). Fonte: OKX. Cobre os pares em PAIRS (configuracao no topo do script) -- BTC-USDT-SWAP e os demais adicionados na expansao de 07/09/2026. Leitura e MECANICA (regras objetivas da secao 4 do plano), sem a prosa qualitativa que o Claude gerava -- cole este log numa conversa do Claude se quiser a leitura interpretativa.

| Data/Hora (BRT) | Par | Close 1h | High/Low 1h | Close 4h | Swing 1h ref | ATR 1h | Funding | Zona ativa | Status checklist |
|---|---|---|---|---|---|---|---|---|---|
| 2026-11-24 17:06 | BTC-USDT-SWAP | 59656.4 | 60053.7/59641.2 | 59656.4 | res 60666.0 (ha 5 candles) | 608.96 | 0.0095% | — | sem_zona |
| 2026-11-24 17:06 | ETH-USDT-SWAP | 1673.0 | 1684.6/1672.8 | 1673.0 | res 1707.7 (ha 7 candles) | 18.13 | 0.0085% | — | sem_zona |
| 2026-11-24 17:06 | SOL-USDT-SWAP | 68.97 | 69.56/68.96 | 68.97 | res 72.65 (ha 18 candles) | 0.84071 | -0.0022% | B/compra@69.87 (0t/1c) | zona_mapeada_setup_B |
| 2026-11-24 17:06 | XRP-USDT-SWAP | 0.91710 | 0.92360/0.91710 | 0.91710 | res 0.96090 (ha 14 candles) | 0.01035 | 0.0030% | B/compra@0.91250 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-24 17:06 | DOGE-USDT-SWAP | 0.05511 | 0.05543/0.05508 | 0.05511 | res 0.05692 (ha 14 candles) | 0.00061 | 0.0003% | — | sem_zona |
| 2026-11-24 17:06 | ARB-USDT-SWAP | 0.10994 | 0.11171/0.10988 | 0.10994 | res 0.11781 (ha 14 candles) | 0.00187 | 0.0023% | — | sem_zona |
| 2026-11-24 17:06 | WLD-USDT-SWAP | 0.23290 | 0.23580/0.23280 | 0.23290 | res 0.24570 (ha 13 candles) | 0.00404 | -0.0331% | B/compra@0.23040 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-24 17:06 | SUI-USDT-SWAP | 0.64250 | 0.64830/0.64220 | 0.64250 | res 0.67960 (ha 14 candles) | 0.00891 | -0.0019% | B/compra@0.63330 (0t/4c) | zona_mapeada_setup_B |
| 2026-11-24 17:06 | UNI-USDT-SWAP | 4.6950 | 4.7520/4.6910 | 4.6950 | res 4.9330 (ha 14 candles) | 0.06943 | 0.0100% | — | sem_zona |
| 2026-11-24 17:06 | LINK-USDT-SWAP | 8.8160 | 8.8990/8.8150 | 8.8160 | res 9.1430 (ha 14 candles) | 0.10743 | -0.0070% | — | invalidado_setup_B |
| 2026-11-24 18:06 | BTC-USDT-SWAP | 59747.1 | 59888.8/59445.9 | 59656.4 | res 60666.0 (ha 6 candles) | 619.49 | 0.0096% | — | sem_zona |
| 2026-11-24 18:06 | ETH-USDT-SWAP | 1675.4 | 1681.7/1666.2 | 1673.0 | res 1707.7 (ha 8 candles) | 18.60 | 0.0089% | — | sem_zona |
| 2026-11-24 18:06 | SOL-USDT-SWAP | 69.28 | 69.52/68.86 | 68.97 | res 72.65 (ha 19 candles) | 0.84571 | -0.0011% | B/compra@69.87 (0t/2c) | zona_mapeada_setup_B |
| 2026-11-24 18:06 | XRP-USDT-SWAP | 0.91930 | 0.92300/0.91540 | 0.91710 | res 0.96090 (ha 15 candles) | 0.01015 | 0.0040% | B/compra@0.91250 (0t/1c) | zona_mapeada_setup_B |
| 2026-11-24 18:06 | DOGE-USDT-SWAP | 0.05527 | 0.05545/0.05493 | 0.05511 | res 0.05692 (ha 15 candles) | 0.00062 | 0.0012% | — | sem_zona |
| 2026-11-24 18:06 | ARB-USDT-SWAP | 0.11064 | 0.11142/0.10964 | 0.10994 | res 0.11781 (ha 15 candles) | 0.00184 | 0.0041% | — | sem_zona |
| 2026-11-24 18:06 | WLD-USDT-SWAP | 0.23470 | 0.23590/0.23190 | 0.23290 | res 0.24570 (ha 14 candles) | 0.00412 | -0.0263% | B/compra@0.23040 (0t/1c) | zona_mapeada_setup_B |
| 2026-11-24 18:06 | SUI-USDT-SWAP | 0.64410 | 0.64670/0.63920 | 0.64250 | res 0.67960 (ha 15 candles) | 0.00899 | -0.0010% | B/compra@0.63330 (0t/5c) | zona_mapeada_setup_B |
| 2026-11-24 18:06 | UNI-USDT-SWAP | 4.7080 | 4.7340/4.6800 | 4.6950 | res 4.9330 (ha 15 candles) | 0.06900 | 0.0100% | — | sem_zona |
| 2026-11-24 18:06 | LINK-USDT-SWAP | 8.8300 | 8.8680/8.7890 | 8.8160 | res 9.1430 (ha 15 candles) | 0.10864 | -0.0028% | — | sem_zona |
| 2026-11-24 19:06 | BTC-USDT-SWAP | 59863.4 | 59949.3/59675.2 | 59656.4 | res 60666.0 (ha 7 candles) | 618.05 | 0.0081% | — | sem_zona |
| 2026-11-24 19:06 | ETH-USDT-SWAP | 1680.0 | 1682.2/1672.2 | 1673.0 | res 1707.7 (ha 9 candles) | 18.61 | 0.0090% | — | sem_zona |
| 2026-11-24 19:06 | SOL-USDT-SWAP | 69.41 | 69.55/69.15 | 68.97 | res 72.65 (ha 20 candles) | 0.84214 | 0.0011% | B/compra@69.87 (0t/3c) | zona_mapeada_setup_B |
| 2026-11-24 19:06 | XRP-USDT-SWAP | 0.92250 | 0.92320/0.91830 | 0.91710 | res 0.92770 (ha 3 candles) | 0.00991 | 0.0056% | B/compra@0.91250 (0t/2c) | zona_mapeada_setup_B |
| 2026-11-24 19:06 | DOGE-USDT-SWAP | 0.05534 | 0.05539/0.05513 | 0.05511 | res 0.05553 (ha 3 candles) | 0.00061 | 0.0034% | — | sem_zona |
| 2026-11-24 19:06 | ARB-USDT-SWAP | 0.11061 | 0.11102/0.11015 | 0.10994 | res 0.11781 (ha 16 candles) | 0.00183 | 0.0037% | — | sem_zona |
| 2026-11-24 19:06 | WLD-USDT-SWAP | 0.23440 | 0.23530/0.23340 | 0.23290 | res 0.23780 (ha 3 candles) | 0.00404 | -0.0194% | B/compra@0.23040 (0t/2c) | zona_mapeada_setup_B |
| 2026-11-24 19:06 | SUI-USDT-SWAP | 0.64510 | 0.64620/0.64270 | 0.64250 | res 0.65320 (ha 3 candles) | 0.00873 | -0.0006% | B/compra@0.63330 (0t/6c) | zona_mapeada_setup_B |
| 2026-11-24 19:06 | UNI-USDT-SWAP | 4.7130 | 4.7150/4.6850 | 4.6950 | res 4.7630 (ha 3 candles) | 0.06621 | 0.0100% | — | sem_zona |
| 2026-11-24 19:06 | LINK-USDT-SWAP | 8.8280 | 8.8400/8.7930 | 8.8160 | res 8.9310 (ha 3 candles) | 0.10679 | -0.0001% | — | sem_zona |
| 2026-11-24 20:06 | BTC-USDT-SWAP | 59959.3 | 60072.6/59842.8 | 59656.4 | res 60666.0 (ha 8 candles) | 598.19 | 0.0067% | B/compra@60339.6 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-24 20:06 | ETH-USDT-SWAP | 1684.8 | 1687.8/1679.2 | 1673.0 | res 1707.7 (ha 10 candles) | 18.16 | 0.0086% | — | sem_zona |
| 2026-11-24 20:06 | SOL-USDT-SWAP | 69.95 | 70.04/69.38 | 68.97 | res 72.65 (ha 21 candles) | 0.83714 | 0.0034% | — | descartado_rr_baixo_setup_B |
| 2026-11-24 20:06 | XRP-USDT-SWAP | 0.92550 | 0.92630/0.92170 | 0.91710 | res 0.92770 (ha 4 candles) | 0.00952 | 0.0058% | B/compra@0.91250 (0t/3c) | zona_mapeada_setup_B |
| 2026-11-24 20:06 | DOGE-USDT-SWAP | 0.05537 | 0.05551/0.05530 | 0.05511 | res 0.05553 (ha 4 candles) | 0.00059 | 0.0080% | — | sem_zona |
| 2026-11-24 20:06 | ARB-USDT-SWAP | 0.11027 | 0.11095/0.11027 | 0.10994 | res 0.11781 (ha 17 candles) | 0.00178 | -0.0001% | — | sem_zona |
| 2026-11-24 20:06 | WLD-USDT-SWAP | 0.23550 | 0.23610/0.23400 | 0.23290 | res 0.23780 (ha 4 candles) | 0.00396 | -0.0156% | B/compra@0.23040 (0t/3c) | zona_mapeada_setup_B |
| 2026-11-24 20:06 | SUI-USDT-SWAP | 0.64910 | 0.65040/0.64480 | 0.64250 | res 0.65320 (ha 4 candles) | 0.00864 | -0.0017% | B/compra@0.63330 (0t/7c) | zona_mapeada_setup_B |
| 2026-11-24 20:06 | UNI-USDT-SWAP | 4.7270 | 4.7400/4.7110 | 4.6950 | res 4.7630 (ha 4 candles) | 0.06379 | 0.0100% | — | sem_zona |
| 2026-11-24 20:06 | LINK-USDT-SWAP | 8.8590 | 8.8780/8.8220 | 8.8160 | res 8.9310 (ha 4 candles) | 0.10371 | 0.0019% | B/compra@8.9300 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-24 21:06 | BTC-USDT-SWAP | 59796.8 | 60040.0/59735.3 | 59796.8 | res 60666.0 (ha 9 candles) | 582.96 | 0.0054% | B/compra@60339.6 (0t/1c) | zona_mapeada_setup_B |
| 2026-11-24 21:06 | ETH-USDT-SWAP | 1679.3 | 1685.3/1676.9 | 1679.3 | res 1707.7 (ha 11 candles) | 17.42 | 0.0080% | — | sem_zona |
| 2026-11-24 21:06 | SOL-USDT-SWAP | 69.65 | 70.07/69.62 | 69.65 | res 72.65 (ha 22 candles) | 0.82571 | 0.0055% | — | sem_zona |
| 2026-11-24 21:06 | XRP-USDT-SWAP | 0.92440 | 0.92720/0.92220 | 0.92440 | res 0.92770 (ha 5 candles) | 0.00927 | 0.0060% | B/compra@0.91250 (0t/4c) | zona_mapeada_setup_B |
| 2026-11-24 21:06 | DOGE-USDT-SWAP | 0.05528 | 0.05546/0.05512 | 0.05528 | res 0.05553 (ha 5 candles) | 0.00057 | 0.0097% | B/compra@0.05534 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-24 21:06 | ARB-USDT-SWAP | 0.11032 | 0.11046/0.10941 | 0.11032 | res 0.11781 (ha 18 candles) | 0.00177 | -0.0006% | — | sem_zona |
| 2026-11-24 21:06 | WLD-USDT-SWAP | 0.23560 | 0.23640/0.23430 | 0.23560 | res 0.23780 (ha 5 candles) | 0.00384 | -0.0188% | B/compra@0.23040 (0t/4c) | zona_mapeada_setup_B |
| 2026-11-24 21:06 | SUI-USDT-SWAP | 0.64810 | 0.65040/0.64600 | 0.64810 | res 0.65320 (ha 5 candles) | 0.00844 | -0.0021% | — | zona_expirada_setup_B |
| 2026-11-24 21:06 | UNI-USDT-SWAP | 4.7160 | 4.7460/4.7060 | 4.7160 | res 4.7630 (ha 5 candles) | 0.06207 | 0.0100% | — | sem_zona |
| 2026-11-24 21:06 | LINK-USDT-SWAP | 8.8480 | 8.8820/8.8260 | 8.8480 | res 8.9310 (ha 5 candles) | 0.10171 | 0.0037% | B/compra@8.9300 (0t/1c) | zona_mapeada_setup_B |
| 2026-11-24 22:06 | BTC-USDT-SWAP | 59629.1 | 59801.1/59415.1 | 59796.8 | res 60666.0 (ha 10 candles) | 560.73 | 0.0041% | B/compra@60339.6 (0t/2c) | zona_mapeada_setup_B |
| 2026-11-24 22:06 | ETH-USDT-SWAP | 1672.8 | 1679.4/1666.9 | 1679.3 | res 1707.7 (ha 12 candles) | 17.12 | 0.0086% | — | sem_zona |
| 2026-11-24 22:06 | SOL-USDT-SWAP | 69.61 | 69.88/69.40 | 69.65 | res 72.65 (ha 23 candles) | 0.79286 | 0.0078% | — | sem_zona |
| 2026-11-24 22:06 | XRP-USDT-SWAP | 0.92150 | 0.92490/0.92030 | 0.92440 | res 0.92770 (ha 6 candles) | 0.00886 | 0.0051% | B/compra@0.91250 (0t/5c) | zona_mapeada_setup_B |
| 2026-11-24 22:06 | DOGE-USDT-SWAP | 0.05508 | 0.05531/0.05496 | 0.05528 | res 0.05553 (ha 6 candles) | 0.00056 | 0.0088% | — | invalidado_setup_B |
| 2026-11-24 22:06 | ARB-USDT-SWAP | 0.11047 | 0.11060/0.10964 | 0.11032 | res 0.11781 (ha 19 candles) | 0.00174 | -0.0030% | — | sem_zona |
| 2026-11-24 22:06 | WLD-USDT-SWAP | 0.23310 | 0.23600/0.23290 | 0.23560 | res 0.23780 (ha 6 candles) | 0.00385 | -0.0230% | B/compra@0.23040 (0t/5c) | zona_mapeada_setup_B |
| 2026-11-24 22:06 | SUI-USDT-SWAP | 0.64480 | 0.64880/0.64370 | 0.64810 | res 0.65320 (ha 6 candles) | 0.00819 | -0.0056% | B/compra@0.64030 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-24 22:06 | UNI-USDT-SWAP | 4.7070 | 4.7310/4.6860 | 4.7160 | res 4.7630 (ha 6 candles) | 0.06143 | 0.0078% | — | sem_zona |
| 2026-11-24 22:06 | LINK-USDT-SWAP | 8.8070 | 8.8520/8.7870 | 8.8480 | res 8.9310 (ha 6 candles) | 0.09900 | 0.0039% | B/compra@8.9300 (0t/2c) | zona_mapeada_setup_B |
| 2026-11-24 23:06 | BTC-USDT-SWAP | 59238.9 | 59732.1/59030.2 | 59796.8 | res 60072.6 (ha 3 candles) | 543.63 | 0.0038% | B/compra@60339.6 (0t/3c) | zona_mapeada_setup_B |
| 2026-11-24 23:06 | ETH-USDT-SWAP | 1657.5 | 1674.5/1652.5 | 1679.3 | res 1687.8 (ha 3 candles) | 16.80 | 0.0082% | B/compra@1647.1 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-24 23:06 | SOL-USDT-SWAP | 69.00 | 69.65/68.83 | 69.65 | res 72.65 (ha 24 candles) | 0.77429 | 0.0100% | B/compra@68.68 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-24 23:06 | XRP-USDT-SWAP | 0.91330 | 0.92270/0.91130 | 0.92440 | res 0.92770 (ha 7 candles) | 0.00890 | 0.0048% | B/compra@0.91250 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-24 23:06 | DOGE-USDT-SWAP | 0.05466 | 0.05512/0.05448 | 0.05528 | res 0.05551 (ha 3 candles) | 0.00055 | 0.0076% | B/compra@0.05432 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-24 23:06 | ARB-USDT-SWAP | 0.10906 | 0.11056/0.10893 | 0.11032 | res 0.11781 (ha 20 candles) | 0.00175 | -0.0023% | B/compra@0.11011 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-24 23:06 | WLD-USDT-SWAP | 0.23230 | 0.23380/0.23130 | 0.23560 | res 0.23780 (ha 7 candles) | 0.00372 | -0.0210% | B/compra@0.23040 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-24 23:06 | SUI-USDT-SWAP | 0.64170 | 0.64600/0.63940 | 0.64810 | res 0.65040 (ha 3 candles) | 0.00808 | -0.0073% | B/compra@0.64030 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-24 23:06 | UNI-USDT-SWAP | 4.6050 | 4.7110/4.5940 | 4.7160 | res 4.7630 (ha 7 candles) | 0.06471 | 0.0078% | B/compra@4.6280 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-24 23:06 | LINK-USDT-SWAP | 8.7440 | 8.8120/8.7170 | 8.8480 | res 8.9310 (ha 7 candles) | 0.09650 | 0.0057% | B/compra@8.9300 (0t/3c) | zona_mapeada_setup_B |
| 2026-11-25 00:06 | BTC-USDT-SWAP | 59209.7 | 59338.2/58913.9 | 59796.8 | res 60072.6 (ha 4 candles) | 538.96 | 0.0033% | B/compra@60339.6 (0t/4c) | zona_mapeada_setup_B |
| 2026-11-25 00:06 | ETH-USDT-SWAP | 1655.3 | 1661.8/1650.2 | 1679.3 | res 1687.8 (ha 4 candles) | 16.62 | 0.0075% | B/compra@1647.1 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-25 00:06 | SOL-USDT-SWAP | 68.78 | 69.03/68.41 | 69.65 | res 70.07 (ha 3 candles) | 0.78143 | 0.0100% | B/compra@68.68 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-25 00:06 | XRP-USDT-SWAP | 0.91740 | 0.91870/0.91060 | 0.92440 | res 0.92720 (ha 3 candles) | 0.00886 | 0.0016% | — | descartado_rr_baixo_setup_B |
| 2026-11-25 00:06 | DOGE-USDT-SWAP | 0.05463 | 0.05471/0.05435 | 0.05528 | res 0.05551 (ha 4 candles) | 0.00054 | 0.0060% | B/compra@0.05432 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-25 00:06 | ARB-USDT-SWAP | 0.10888 | 0.10906/0.10836 | 0.11032 | res 0.11781 (ha 21 candles) | 0.00162 | -0.0013% | B/compra@0.11011 (0t/1c) | zona_mapeada_setup_B |
| 2026-11-25 00:06 | WLD-USDT-SWAP | 0.23160 | 0.23280/0.23110 | 0.23560 | res 0.23640 (ha 3 candles) | 0.00355 | -0.0226% | B/compra@0.23040 (2t/0c) | zona_mapeada_setup_B |
| 2026-11-25 00:06 | SUI-USDT-SWAP | 0.64040 | 0.64210/0.63840 | 0.64810 | res 0.65040 (ha 3 candles) | 0.00777 | -0.0093% | B/compra@0.64030 (2t/0c) | zona_mapeada_setup_B |
| 2026-11-25 00:06 | UNI-USDT-SWAP | 4.5950 | 4.6230/4.5740 | 4.7160 | res 4.7460 (ha 3 candles) | 0.06386 | 0.0068% | — | invalidado_setup_B |
| 2026-11-25 00:06 | LINK-USDT-SWAP | 8.7430 | 8.7580/8.7020 | 8.8480 | res 8.8820 (ha 3 candles) | 0.09379 | 0.0046% | B/compra@8.9300 (0t/4c) | zona_mapeada_setup_B |
| 2026-11-25 01:06 | BTC-USDT-SWAP | 59391.2 | 59639.5/59000.1 | 59391.2 | res 60072.6 (ha 5 candles) | 524.31 | 0.0037% | B/compra@60339.6 (0t/5c) | zona_mapeada_setup_B |
| 2026-11-25 01:06 | ETH-USDT-SWAP | 1663.7 | 1670.6/1648.0 | 1663.7 | res 1687.8 (ha 5 candles) | 16.33 | 0.0068% | — | descartado_rr_baixo_setup_B |
| 2026-11-25 01:06 | SOL-USDT-SWAP | 69.30 | 69.63/68.46 | 69.30 | res 70.07 (ha 4 candles) | 0.77286 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-11-25 01:06 | XRP-USDT-SWAP | 0.92040 | 0.92320/0.91440 | 0.92040 | res 0.92720 (ha 4 candles) | 0.00851 | 0.0001% | — | sem_zona |
| 2026-11-25 01:06 | DOGE-USDT-SWAP | 0.05461 | 0.05505/0.05436 | 0.05461 | res 0.05551 (ha 5 candles) | 0.00052 | 0.0066% | B/compra@0.05432 (2t/0c) | zona_mapeada_setup_B |
| 2026-11-25 01:06 | ARB-USDT-SWAP | 0.10991 | 0.11027/0.10838 | 0.10991 | res 0.11781 (ha 22 candles) | 0.00156 | 0.0026% | — | confirmado_calibracao_setup_B |
| 2026-11-25 01:06 | WLD-USDT-SWAP | 0.23310 | 0.23380/0.23030 | 0.23310 | res 0.23640 (ha 4 candles) | 0.00346 | -0.0238% | — | descartado_rr_baixo_setup_B |
| 2026-11-25 01:06 | SUI-USDT-SWAP | 0.64360 | 0.64660/0.63720 | 0.64360 | — | 0.00754 | -0.0109% | — | descartado_rr_baixo_setup_B |
| 2026-11-25 01:06 | UNI-USDT-SWAP | 4.6050 | 4.6380/4.5690 | 4.6050 | res 4.7460 (ha 4 candles) | 0.06250 | 0.0080% | B/compra@4.6100 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-25 01:06 | LINK-USDT-SWAP | 8.8050 | 8.8210/8.7090 | 8.8050 | res 8.8820 (ha 4 candles) | 0.09064 | 0.0049% | B/compra@8.9300 (0t/5c) | zona_mapeada_setup_B |
| 2026-11-25 02:06 | BTC-USDT-SWAP | 59196.9 | 59391.2/58917.5 | 59391.2 | res 60072.6 (ha 6 candles) | 507.13 | 0.0052% | B/compra@60339.6 (0t/6c) | zona_mapeada_setup_B |
| 2026-11-25 02:06 | ETH-USDT-SWAP | 1659.9 | 1666.5/1652.6 | 1663.7 | res 1687.8 (ha 6 candles) | 15.63 | 0.0057% | — | sem_zona |
| 2026-11-25 02:06 | SOL-USDT-SWAP | 68.74 | 69.39/68.48 | 69.30 | res 70.07 (ha 5 candles) | 0.75714 | 0.0100% | — | sem_zona |
| 2026-11-25 02:06 | XRP-USDT-SWAP | 0.91830 | 0.92300/0.91510 | 0.92040 | res 0.92720 (ha 5 candles) | 0.00828 | -0.0010% | — | sem_zona |
| 2026-11-25 02:06 | DOGE-USDT-SWAP | 0.05460 | 0.05480/0.05434 | 0.05461 | res 0.05551 (ha 6 candles) | 0.00050 | 0.0078% | — | zona_expirada_setup_B |
| 2026-11-25 02:06 | ARB-USDT-SWAP | 0.10975 | 0.11038/0.10907 | 0.10991 | res 0.11781 (ha 23 candles) | 0.00149 | 0.0068% | — | sem_zona |
| 2026-11-25 02:06 | WLD-USDT-SWAP | 0.23270 | 0.23410/0.23140 | 0.23310 | res 0.23640 (ha 5 candles) | 0.00337 | -0.0231% | — | sem_zona |
| 2026-11-25 02:06 | SUI-USDT-SWAP | 0.64240 | 0.64640/0.63960 | 0.64360 | — | 0.00729 | -0.0101% | — | sem_zona |
| 2026-11-25 02:06 | UNI-USDT-SWAP | 4.6060 | 4.6280/4.5810 | 4.6050 | res 4.7460 (ha 5 candles) | 0.06021 | 0.0097% | B/compra@4.6100 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-25 02:06 | LINK-USDT-SWAP | 8.7760 | 8.8250/8.7400 | 8.8050 | res 8.8820 (ha 5 candles) | 0.08757 | 0.0064% | B/compra@8.9300 (0t/6c) | zona_mapeada_setup_B |
| 2026-11-25 03:06 | BTC-USDT-SWAP | 59134.7 | 59289.2/58957.3 | 59391.2 | res 60072.6 (ha 7 candles) | 464.10 | 0.0066% | B/compra@60339.6 (0t/7c) | zona_mapeada_setup_B |
| 2026-11-25 03:06 | ETH-USDT-SWAP | 1656.7 | 1662.7/1652.2 | 1663.7 | res 1687.8 (ha 7 candles) | 14.24 | 0.0059% | — | sem_zona |
| 2026-11-25 03:06 | SOL-USDT-SWAP | 68.70 | 68.88/68.30 | 69.30 | res 70.07 (ha 6 candles) | 0.69143 | 0.0100% | — | sem_zona |
| 2026-11-25 03:06 | XRP-USDT-SWAP | 0.91670 | 0.92040/0.91430 | 0.92040 | res 0.92720 (ha 6 candles) | 0.00767 | 0.0000% | — | sem_zona |
| 2026-11-25 03:06 | DOGE-USDT-SWAP | 0.05470 | 0.05479/0.05449 | 0.05461 | res 0.05551 (ha 7 candles) | 0.00044 | 0.0085% | — | sem_zona |
| 2026-11-25 03:06 | ARB-USDT-SWAP | 0.10975 | 0.11016/0.10925 | 0.10991 | res 0.11781 (ha 24 candles) | 0.00133 | 0.0087% | — | sem_zona |
| 2026-11-25 03:06 | WLD-USDT-SWAP | 0.23320 | 0.23390/0.23180 | 0.23310 | res 0.23640 (ha 6 candles) | 0.00303 | -0.0223% | — | sem_zona |
| 2026-11-25 03:06 | SUI-USDT-SWAP | 0.64290 | 0.64490/0.64060 | 0.64360 | — | 0.00644 | -0.0079% | — | sem_zona |
| 2026-11-25 03:06 | UNI-USDT-SWAP | 4.6120 | 4.6280/4.5910 | 4.6050 | res 4.7460 (ha 6 candles) | 0.05436 | 0.0100% | B/compra@4.6100 (2t/0c) | zona_mapeada_setup_B |
| 2026-11-25 03:06 | LINK-USDT-SWAP | 8.7530 | 8.7930/8.7320 | 8.8050 | res 8.8820 (ha 6 candles) | 0.07893 | 0.0077% | B/compra@8.9300 (0t/7c) | zona_mapeada_setup_B |
| 2026-11-25 04:06 | BTC-USDT-SWAP | 59205.8 | 59331.1/58967.6 | 59391.2 | res 60072.6 (ha 8 candles) | 451.24 | 0.0067% | — | zona_expirada_setup_B |
| 2026-11-25 04:06 | ETH-USDT-SWAP | 1659.4 | 1663.2/1652.5 | 1663.7 | res 1687.8 (ha 8 candles) | 13.72 | 0.0057% | — | sem_zona |
| 2026-11-25 04:06 | SOL-USDT-SWAP | 68.80 | 68.98/68.45 | 69.30 | res 70.07 (ha 7 candles) | 0.66643 | 0.0100% | — | sem_zona |
| 2026-11-25 04:06 | XRP-USDT-SWAP | 0.91940 | 0.92130/0.91460 | 0.92040 | res 0.92720 (ha 7 candles) | 0.00750 | 0.0012% | — | sem_zona |
| 2026-11-25 04:06 | DOGE-USDT-SWAP | 0.05486 | 0.05499/0.05460 | 0.05461 | res 0.05551 (ha 8 candles) | 0.00043 | 0.0086% | — | sem_zona |
| 2026-11-25 04:06 | ARB-USDT-SWAP | 0.11047 | 0.11093/0.10934 | 0.10991 | res 0.11781 (ha 25 candles) | 0.00135 | 0.0086% | — | sem_zona |
| 2026-11-25 04:06 | WLD-USDT-SWAP | 0.23310 | 0.23480/0.23240 | 0.23310 | res 0.23640 (ha 7 candles) | 0.00286 | -0.0201% | — | sem_zona |
| 2026-11-25 04:06 | SUI-USDT-SWAP | 0.64470 | 0.64730/0.64150 | 0.64360 | — | 0.00636 | -0.0039% | — | sem_zona |
| 2026-11-25 04:06 | UNI-USDT-SWAP | 4.5980 | 4.6280/4.5810 | 4.6050 | res 4.7460 (ha 7 candles) | 0.05379 | 0.0100% | — | zona_expirada_setup_B |
| 2026-11-25 04:06 | LINK-USDT-SWAP | 8.7610 | 8.7910/8.7240 | 8.8050 | res 8.8820 (ha 7 candles) | 0.07657 | 0.0092% | — | zona_expirada_setup_B |
| 2026-11-25 05:06 | BTC-USDT-SWAP | 58710.8 | 59392.8/58588.9 | 58710.8 | res 60072.6 (ha 9 candles) | 443.61 | 0.0061% | B/compra@58731.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-25 05:06 | ETH-USDT-SWAP | 1640.2 | 1664.5/1631.7 | 1640.2 | res 1687.8 (ha 9 candles) | 14.41 | 0.0038% | — | sem_zona |
| 2026-11-25 05:06 | SOL-USDT-SWAP | 67.77 | 68.99/67.66 | 67.77 | res 70.07 (ha 8 candles) | 0.69500 | 0.0075% | B/compra@67.33 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-25 05:06 | XRP-USDT-SWAP | 0.91400 | 0.92280/0.90910 | 0.91400 | — | 0.00741 | 0.0016% | — | sem_zona |
| 2026-11-25 05:06 | DOGE-USDT-SWAP | 0.05426 | 0.05497/0.05397 | 0.05426 | res 0.05551 (ha 9 candles) | 0.00044 | 0.0076% | — | sem_zona |
| 2026-11-25 05:06 | ARB-USDT-SWAP | 0.10962 | 0.11071/0.10875 | 0.10962 | res 0.11781 (ha 26 candles) | 0.00132 | 0.0100% | — | sem_zona |
| 2026-11-25 05:06 | WLD-USDT-SWAP | 0.23070 | 0.23340/0.22830 | 0.23070 | — | 0.00289 | -0.0189% | B/venda@0.23190 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-25 05:06 | SUI-USDT-SWAP | 0.64010 | 0.64650/0.63410 | 0.64010 | — | 0.00633 | -0.0038% | — | sem_zona |
| 2026-11-25 05:06 | UNI-USDT-SWAP | 4.5510 | 4.6140/4.5090 | 4.5510 | res 4.7460 (ha 8 candles) | 0.05464 | 0.0100% | B/compra@4.5520 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-25 05:06 | LINK-USDT-SWAP | 8.7040 | 8.7860/8.6550 | 8.7040 | res 8.8250 (ha 3 candles) | 0.07514 | 0.0078% | B/compra@8.7100 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-25 06:06 | BTC-USDT-SWAP | 59393.9 | 59459.0/58690.8 | 58710.8 | res 60072.6 (ha 10 candles) | 468.34 | 0.0040% | — | descartado_rr_baixo_setup_B |
| 2026-11-25 06:06 | ETH-USDT-SWAP | 1652.3 | 1656.0/1637.1 | 1640.2 | res 1687.8 (ha 10 candles) | 14.99 | 0.0007% | — | sem_zona |
| 2026-11-25 06:06 | SOL-USDT-SWAP | 68.08 | 68.47/67.67 | 67.77 | res 70.07 (ha 9 candles) | 0.71500 | 0.0042% | B/compra@67.33 (0t/1c) | zona_mapeada_setup_B |
| 2026-11-25 06:06 | XRP-USDT-SWAP | 0.92190 | 0.92690/0.91410 | 0.91400 | — | 0.00777 | 0.0012% | — | sem_zona |
| 2026-11-25 06:06 | DOGE-USDT-SWAP | 0.05449 | 0.05473/0.05424 | 0.05426 | res 0.05551 (ha 10 candles) | 0.00045 | 0.0059% | — | sem_zona |
| 2026-11-25 06:06 | ARB-USDT-SWAP | 0.10966 | 0.11016/0.10923 | 0.10962 | res 0.11781 (ha 27 candles) | 0.00129 | 0.0100% | — | sem_zona |
| 2026-11-25 06:06 | WLD-USDT-SWAP | 0.23140 | 0.23240/0.23010 | 0.23070 | — | 0.00275 | -0.0216% | B/venda@0.23190 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-25 06:06 | SUI-USDT-SWAP | 0.64390 | 0.64650/0.63960 | 0.64010 | — | 0.00629 | -0.0087% | — | sem_zona |
| 2026-11-25 06:06 | UNI-USDT-SWAP | 4.5510 | 4.5820/4.5290 | 4.5510 | res 4.7460 (ha 9 candles) | 0.05593 | 0.0100% | B/compra@4.5520 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-25 06:06 | LINK-USDT-SWAP | 8.7510 | 8.7900/8.6970 | 8.7040 | res 8.8250 (ha 4 candles) | 0.07764 | 0.0052% | B/compra@8.7100 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-25 07:06 | BTC-USDT-SWAP | 59066.0 | 59409.9/58767.9 | 58710.8 | res 60072.6 (ha 11 candles) | 484.74 | 0.0045% | — | sem_zona |
| 2026-11-25 07:06 | ETH-USDT-SWAP | 1644.4 | 1652.6/1633.5 | 1640.2 | res 1687.8 (ha 11 candles) | 15.52 | -0.0007% | — | sem_zona |
| 2026-11-25 07:06 | SOL-USDT-SWAP | 67.67 | 68.08/67.28 | 67.77 | res 70.07 (ha 10 candles) | 0.72929 | 0.0009% | B/compra@67.33 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-25 07:06 | XRP-USDT-SWAP | 0.91550 | 0.92220/0.91170 | 0.91400 | — | 0.00806 | 0.0003% | — | sem_zona |
| 2026-11-25 07:06 | DOGE-USDT-SWAP | 0.05402 | 0.05450/0.05373 | 0.05426 | res 0.05551 (ha 11 candles) | 0.00048 | 0.0050% | B/compra@0.05373 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-25 07:06 | ARB-USDT-SWAP | 0.10847 | 0.10965/0.10779 | 0.10962 | res 0.11093 (ha 3 candles) | 0.00130 | 0.0100% | — | sem_zona |
| 2026-11-25 07:06 | WLD-USDT-SWAP | 0.22930 | 0.23150/0.22770 | 0.23070 | — | 0.00281 | -0.0237% | B/venda@0.23190 (2t/0c) | zona_mapeada_setup_B |
| 2026-11-25 07:06 | SUI-USDT-SWAP | 0.63780 | 0.64420/0.63370 | 0.64010 | — | 0.00661 | -0.0110% | B/compra@0.63330 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-25 07:06 | UNI-USDT-SWAP | 4.5160 | 4.5520/4.4860 | 4.5510 | res 4.7460 (ha 10 candles) | 0.05629 | 0.0100% | — | invalidado_setup_B |
| 2026-11-25 07:06 | LINK-USDT-SWAP | 8.6620 | 8.7530/8.6100 | 8.7040 | res 8.8250 (ha 5 candles) | 0.08186 | 0.0074% | — | invalidado_setup_B |
| 2026-11-25 08:06 | BTC-USDT-SWAP | 58881.2 | 59176.0/58750.6 | 58710.8 | res 60072.6 (ha 12 candles) | 483.49 | 0.0069% | — | sem_zona |
| 2026-11-25 08:06 | ETH-USDT-SWAP | 1647.7 | 1648.5/1640.9 | 1640.2 | res 1687.8 (ha 12 candles) | 14.96 | -0.0013% | — | sem_zona |
| 2026-11-25 08:06 | SOL-USDT-SWAP | 67.78 | 67.83/67.52 | 67.77 | res 70.07 (ha 11 candles) | 0.70429 | -0.0017% | B/compra@67.33 (1t/1c) | zona_mapeada_setup_B |
| 2026-11-25 08:06 | XRP-USDT-SWAP | 0.91260 | 0.91730/0.91070 | 0.91400 | — | 0.00799 | -0.0003% | B/compra@0.91250 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-25 08:06 | DOGE-USDT-SWAP | 0.05401 | 0.05411/0.05385 | 0.05426 | res 0.05551 (ha 12 candles) | 0.00047 | 0.0032% | B/compra@0.05373 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-25 08:06 | ARB-USDT-SWAP | 0.10775 | 0.10866/0.10725 | 0.10962 | res 0.11093 (ha 4 candles) | 0.00127 | 0.0087% | — | sem_zona |
| 2026-11-25 08:06 | WLD-USDT-SWAP | 0.22860 | 0.23020/0.22760 | 0.23070 | — | 0.00271 | -0.0256% | B/venda@0.23190 (2t/1c) | zona_mapeada_setup_B |
| 2026-11-25 08:06 | SUI-USDT-SWAP | 0.63550 | 0.63900/0.63320 | 0.64010 | — | 0.00649 | -0.0123% | B/compra@0.63330 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-25 08:06 | UNI-USDT-SWAP | 4.5110 | 4.5230/4.4930 | 4.5510 | res 4.7460 (ha 11 candles) | 0.05457 | 0.0097% | — | sem_zona |
| 2026-11-25 08:06 | LINK-USDT-SWAP | 8.6460 | 8.6760/8.6260 | 8.7040 | res 8.8250 (ha 6 candles) | 0.07979 | 0.0100% | — | sem_zona |
| 2026-11-25 09:06 | BTC-USDT-SWAP | 58610.4 | 58899.1/58420.1 | 58610.4 | res 59459.0 (ha 3 candles) | 498.12 | 0.0076% | — | sem_zona |
| 2026-11-25 09:06 | ETH-USDT-SWAP | 1638.0 | 1649.0/1634.2 | 1638.0 | res 1687.8 (ha 13 candles) | 15.30 | -0.0011% | B/compra@1647.1 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-25 09:06 | SOL-USDT-SWAP | 67.51 | 67.85/67.23 | 67.51 | res 70.07 (ha 12 candles) | 0.72000 | -0.0039% | B/compra@67.33 (2t/0c) | zona_mapeada_setup_B |
| 2026-11-25 09:06 | XRP-USDT-SWAP | 0.90830 | 0.91280/0.90390 | 0.90830 | — | 0.00827 | -0.0019% | — | invalidado_setup_B |
| 2026-11-25 09:06 | DOGE-USDT-SWAP | 0.05362 | 0.05404/0.05354 | 0.05362 | res 0.05551 (ha 13 candles) | 0.00048 | 0.0021% | B/compra@0.05373 (2t/0c) | zona_mapeada_setup_B |
| 2026-11-25 09:06 | ARB-USDT-SWAP | 0.10751 | 0.10794/0.10713 | 0.10751 | res 0.11093 (ha 5 candles) | 0.00126 | 0.0100% | — | sem_zona |
| 2026-11-25 09:06 | WLD-USDT-SWAP | 0.22840 | 0.22980/0.22740 | 0.22840 | — | 0.00274 | -0.0266% | B/venda@0.23190 (2t/2c) | zona_mapeada_setup_B |
| 2026-11-25 09:06 | SUI-USDT-SWAP | 0.62870 | 0.63630/0.62750 | 0.62870 | — | 0.00686 | -0.0135% | — | invalidado_setup_B |
| 2026-11-25 09:06 | UNI-USDT-SWAP | 4.5010 | 4.5350/4.4940 | 4.5010 | res 4.7460 (ha 12 candles) | 0.05536 | 0.0065% | — | sem_zona |
| 2026-11-25 09:06 | LINK-USDT-SWAP | 8.5970 | 8.6550/8.5740 | 8.5970 | res 8.8250 (ha 7 candles) | 0.08221 | 0.0100% | B/compra@8.5670 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-25 10:06 | BTC-USDT-SWAP | 58725.1 | 58762.8/58437.5 | 58610.4 | res 59459.0 (ha 4 candles) | 504.94 | 0.0070% | — | sem_zona |
| 2026-11-25 10:06 | ETH-USDT-SWAP | 1647.3 | 1648.7/1635.5 | 1638.0 | res 1687.8 (ha 14 candles) | 15.62 | -0.0004% | — | descartado_rr_baixo_setup_B |
| 2026-11-25 10:06 | SOL-USDT-SWAP | 67.85 | 67.99/67.38 | 67.51 | res 70.07 (ha 13 candles) | 0.71643 | -0.0059% | — | confirmado_calibracao_setup_B |
| 2026-11-25 10:06 | XRP-USDT-SWAP | 0.90760 | 0.91170/0.90550 | 0.90830 | — | 0.00839 | -0.0024% | — | sem_zona |
| 2026-11-25 10:06 | DOGE-USDT-SWAP | 0.05364 | 0.05386/0.05348 | 0.05362 | res 0.05551 (ha 14 candles) | 0.00049 | -0.0002% | — | zona_expirada_setup_B |
| 2026-11-25 10:06 | ARB-USDT-SWAP | 0.10781 | 0.10833/0.10730 | 0.10751 | res 0.11093 (ha 6 candles) | 0.00129 | 0.0100% | — | sem_zona |
| 2026-11-25 10:06 | WLD-USDT-SWAP | 0.22750 | 0.23010/0.22650 | 0.22840 | — | 0.00285 | -0.0277% | B/venda@0.23190 (2t/3c) | zona_mapeada_setup_B |
| 2026-11-25 10:06 | SUI-USDT-SWAP | 0.62960 | 0.63230/0.62680 | 0.62870 | — | 0.00686 | -0.0127% | — | sem_zona |
| 2026-11-25 10:06 | UNI-USDT-SWAP | 4.5000 | 4.5280/4.4830 | 4.5010 | res 4.7460 (ha 13 candles) | 0.05650 | 0.0039% | — | sem_zona |
| 2026-11-25 10:06 | LINK-USDT-SWAP | 8.6400 | 8.6500/8.5850 | 8.5970 | res 8.8250 (ha 8 candles) | 0.08286 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-11-25 11:06 | BTC-USDT-SWAP | 58051.1 | 58896.4/57923.1 | 58610.4 | res 59459.0 (ha 5 candles) | 552.70 | 0.0060% | — | sem_zona |
| 2026-11-25 11:06 | ETH-USDT-SWAP | 1631.3 | 1654.5/1622.6 | 1638.0 | res 1687.8 (ha 15 candles) | 17.30 | 0.0016% | — | sem_zona |
| 2026-11-25 11:06 | SOL-USDT-SWAP | 66.82 | 68.01/66.65 | 67.51 | res 70.07 (ha 14 candles) | 0.78143 | -0.0065% | — | sem_zona |
| 2026-11-25 11:06 | XRP-USDT-SWAP | 0.89410 | 0.90940/0.89220 | 0.90830 | — | 0.00926 | -0.0034% | B/compra@0.89220 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-25 11:06 | DOGE-USDT-SWAP | 0.05288 | 0.05376/0.05269 | 0.05362 | res 0.05551 (ha 15 candles) | 0.00055 | -0.0017% | — | sem_zona |
| 2026-11-25 11:06 | ARB-USDT-SWAP | 0.10631 | 0.10810/0.10597 | 0.10751 | res 0.11093 (ha 7 candles) | 0.00137 | 0.0089% | — | sem_zona |
| 2026-11-25 11:06 | WLD-USDT-SWAP | 0.22460 | 0.22860/0.22380 | 0.22840 | — | 0.00304 | -0.0280% | B/venda@0.23190 (2t/4c) | zona_mapeada_setup_B |
| 2026-11-25 11:06 | SUI-USDT-SWAP | 0.61920 | 0.63000/0.61770 | 0.62870 | — | 0.00742 | -0.0136% | — | sem_zona |
| 2026-11-25 11:06 | UNI-USDT-SWAP | 4.4470 | 4.5210/4.4290 | 4.5010 | res 4.7460 (ha 14 candles) | 0.06021 | 0.0035% | — | sem_zona |
| 2026-11-25 11:06 | LINK-USDT-SWAP | 8.5460 | 8.6720/8.5180 | 8.5970 | res 8.8250 (ha 9 candles) | 0.08986 | 0.0093% | B/compra@8.4880 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-25 12:06 | BTC-USDT-SWAP | 58208.7 | 58430.0/57257.8 | 58610.4 | res 59459.0 (ha 6 candles) | 608.86 | 0.0044% | — | sem_zona |
| 2026-11-25 12:06 | ETH-USDT-SWAP | 1645.4 | 1647.7/1607.7 | 1638.0 | res 1687.8 (ha 16 candles) | 19.26 | 0.0037% | — | sem_zona |
| 2026-11-25 12:06 | SOL-USDT-SWAP | 67.35 | 67.48/65.78 | 67.51 | res 70.07 (ha 15 candles) | 0.86857 | -0.0059% | — | sem_zona |
| 2026-11-25 12:06 | XRP-USDT-SWAP | 0.90410 | 0.90560/0.88840 | 0.90830 | — | 0.01016 | -0.0017% | — | descartado_rr_baixo_setup_B |
| 2026-11-25 12:06 | DOGE-USDT-SWAP | 0.05329 | 0.05330/0.05215 | 0.05362 | res 0.05551 (ha 16 candles) | 0.00060 | -0.0042% | — | sem_zona |
| 2026-11-25 12:06 | ARB-USDT-SWAP | 0.10746 | 0.10746/0.10457 | 0.10751 | res 0.11093 (ha 8 candles) | 0.00150 | 0.0093% | — | sem_zona |
| 2026-11-25 12:06 | WLD-USDT-SWAP | 0.22710 | 0.22710/0.22170 | 0.22840 | — | 0.00321 | -0.0256% | B/venda@0.23190 (2t/5c) | zona_mapeada_setup_B |
| 2026-11-25 12:06 | SUI-USDT-SWAP | 0.62660 | 0.62670/0.61360 | 0.62870 | — | 0.00799 | -0.0157% | — | sem_zona |
| 2026-11-25 12:06 | UNI-USDT-SWAP | 4.4710 | 4.4720/4.3610 | 4.5010 | res 4.7460 (ha 15 candles) | 0.06493 | 0.0024% | — | sem_zona |
| 2026-11-25 12:06 | LINK-USDT-SWAP | 8.6490 | 8.6550/8.4530 | 8.5970 | res 8.8250 (ha 10 candles) | 0.09964 | 0.0073% | — | descartado_rr_baixo_setup_B |
| 2026-11-25 13:06 | BTC-USDT-SWAP | 58315.5 | 58710.6/57655.0 | 58315.5 | res 59459.0 (ha 7 candles) | 634.12 | 0.0040% | — | sem_zona |
| 2026-11-25 13:06 | ETH-USDT-SWAP | 1648.0 | 1671.7/1623.5 | 1648.0 | res 1687.8 (ha 17 candles) | 21.13 | 0.0048% | — | sem_zona |
| 2026-11-25 13:06 | SOL-USDT-SWAP | 67.68 | 68.06/66.56 | 67.68 | res 70.07 (ha 16 candles) | 0.91714 | -0.0062% | — | sem_zona |
| 2026-11-25 13:06 | XRP-USDT-SWAP | 0.90230 | 0.91370/0.89250 | 0.90230 | — | 0.01086 | 0.0008% | — | sem_zona |
| 2026-11-25 13:06 | DOGE-USDT-SWAP | 0.05335 | 0.05389/0.05280 | 0.05335 | res 0.05551 (ha 17 candles) | 0.00064 | -0.0041% | — | sem_zona |
| 2026-11-25 13:06 | ARB-USDT-SWAP | 0.10674 | 0.10890/0.10604 | 0.10674 | res 0.11093 (ha 9 candles) | 0.00159 | 0.0072% | — | sem_zona |
| 2026-11-25 13:06 | WLD-USDT-SWAP | 0.22750 | 0.22990/0.22390 | 0.22750 | — | 0.00346 | -0.0276% | B/venda@0.23190 (2t/6c) | zona_mapeada_setup_B |
| 2026-11-25 13:06 | SUI-USDT-SWAP | 0.62590 | 0.63380/0.61780 | 0.62590 | — | 0.00866 | -0.0153% | — | sem_zona |
| 2026-11-25 13:06 | UNI-USDT-SWAP | 4.4760 | 4.5340/4.4190 | 4.4760 | res 4.7460 (ha 16 candles) | 0.06479 | 0.0031% | — | sem_zona |
| 2026-11-25 13:06 | LINK-USDT-SWAP | 8.6370 | 8.7470/8.5550 | 8.6370 | res 8.8250 (ha 11 candles) | 0.10657 | 0.0039% | B/compra@8.7100 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-25 14:06 | BTC-USDT-SWAP | 58589.4 | 58987.5/58074.1 | 58315.5 | res 59459.0 (ha 8 candles) | 669.06 | 0.0058% | B/compra@58731.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-25 14:06 | ETH-USDT-SWAP | 1644.7 | 1661.7/1629.1 | 1648.0 | res 1687.8 (ha 18 candles) | 22.63 | 0.0056% | — | sem_zona |
| 2026-11-25 14:06 | SOL-USDT-SWAP | 67.82 | 68.38/67.18 | 67.68 | res 70.07 (ha 17 candles) | 0.95857 | -0.0058% | — | sem_zona |
| 2026-11-25 14:06 | XRP-USDT-SWAP | 0.90610 | 0.90830/0.89770 | 0.90230 | — | 0.01104 | 0.0022% | B/compra@0.91250 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-25 14:06 | DOGE-USDT-SWAP | 0.05356 | 0.05377/0.05307 | 0.05335 | res 0.05551 (ha 18 candles) | 0.00066 | -0.0040% | — | sem_zona |
| 2026-11-25 14:06 | ARB-USDT-SWAP | 0.10755 | 0.10766/0.10598 | 0.10674 | res 0.11093 (ha 10 candles) | 0.00166 | 0.0059% | — | sem_zona |
| 2026-11-25 14:06 | WLD-USDT-SWAP | 0.23120 | 0.23180/0.22660 | 0.22750 | — | 0.00371 | -0.0292% | — | zona_expirada_setup_B |
| 2026-11-25 14:06 | SUI-USDT-SWAP | 0.63190 | 0.63260/0.62370 | 0.62590 | — | 0.00904 | -0.0165% | — | sem_zona |
| 2026-11-25 14:06 | UNI-USDT-SWAP | 4.4950 | 4.5130/4.4520 | 4.4760 | res 4.7460 (ha 17 candles) | 0.06564 | 0.0043% | — | sem_zona |
| 2026-11-25 14:06 | LINK-USDT-SWAP | 8.6930 | 8.7080/8.6020 | 8.6370 | res 8.8250 (ha 12 candles) | 0.11014 | -0.0012% | — | descartado_rr_baixo_setup_B |
| 2026-11-25 15:06 | BTC-USDT-SWAP | 59582.9 | 59936.3/58433.0 | 58315.5 | res 59459.0 (ha 9 candles) | 730.76 | 0.0075% | — | descartado_rr_baixo_setup_B |
| 2026-11-25 15:06 | ETH-USDT-SWAP | 1678.3 | 1686.5/1641.2 | 1648.0 | res 1687.8 (ha 19 candles) | 24.25 | 0.0056% | — | sem_zona |
| 2026-11-25 15:06 | SOL-USDT-SWAP | 69.40 | 69.69/67.64 | 67.68 | res 70.07 (ha 18 candles) | 1.0214 | -0.0061% | B/compra@68.68 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-25 15:06 | XRP-USDT-SWAP | 0.92440 | 0.92710/0.90400 | 0.90230 | — | 0.01206 | 0.0046% | — | descartado_rr_baixo_setup_B |
| 2026-11-25 15:06 | DOGE-USDT-SWAP | 0.05488 | 0.05510/0.05343 | 0.05335 | res 0.05551 (ha 19 candles) | 0.00073 | -0.0034% | B/compra@0.05534 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-25 15:06 | ARB-USDT-SWAP | 0.11036 | 0.11098/0.10734 | 0.10674 | res 0.11093 (ha 11 candles) | 0.00179 | 0.0092% | B/compra@0.11022 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-25 15:06 | WLD-USDT-SWAP | 0.23720 | 0.23890/0.23080 | 0.22750 | — | 0.00404 | -0.0267% | — | sem_zona |
| 2026-11-25 15:06 | SUI-USDT-SWAP | 0.64790 | 0.65170/0.63050 | 0.62590 | — | 0.00988 | -0.0154% | B/venda@0.65460 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-25 15:06 | UNI-USDT-SWAP | 4.6490 | 4.6850/4.4820 | 4.4760 | res 4.7460 (ha 18 candles) | 0.07521 | 0.0069% | B/compra@4.6280 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-25 15:06 | LINK-USDT-SWAP | 8.8660 | 8.9020/8.6740 | 8.6370 | res 8.8250 (ha 13 candles) | 0.11843 | -0.0033% | A/compra@8.8250 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-25 16:06 | BTC-USDT-SWAP | 59700.0 | 60080.9/59459.4 | 58315.5 | res 59459.0 (ha 10 candles) | 741.32 | 0.0084% | A/compra@59459.0 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-25 16:06 | ETH-USDT-SWAP | 1679.7 | 1695.9/1675.0 | 1648.0 | res 1687.8 (ha 20 candles) | 24.75 | 0.0062% | — | sem_zona |
| 2026-11-25 16:06 | SOL-USDT-SWAP | 69.73 | 70.13/69.19 | 67.68 | res 70.07 (ha 19 candles) | 1.0236 | -0.0064% | B/compra@68.68 (0t/1c) | zona_mapeada_setup_B |
| 2026-11-25 16:06 | XRP-USDT-SWAP | 0.92830 | 0.93120/0.92180 | 0.90230 | — | 0.01216 | 0.0054% | — | sem_zona |
| 2026-11-25 16:06 | DOGE-USDT-SWAP | 0.05518 | 0.05531/0.05476 | 0.05335 | res 0.05551 (ha 20 candles) | 0.00074 | -0.0034% | — | descartado_rr_baixo_setup_B |
| 2026-11-25 16:06 | ARB-USDT-SWAP | 0.11071 | 0.11156/0.10990 | 0.10674 | res 0.11093 (ha 12 candles) | 0.00181 | 0.0043% | B/compra@0.11022 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-25 16:06 | WLD-USDT-SWAP | 0.23740 | 0.23930/0.23540 | 0.22750 | — | 0.00412 | -0.0292% | — | sem_zona |
| 2026-11-25 16:06 | SUI-USDT-SWAP | 0.65490 | 0.65780/0.64680 | 0.62590 | — | 0.01018 | -0.0159% | B/venda@0.65460 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-25 16:06 | UNI-USDT-SWAP | 4.6580 | 4.7050/4.6350 | 4.4760 | res 4.7460 (ha 19 candles) | 0.07686 | 0.0096% | B/compra@4.6280 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-25 16:06 | LINK-USDT-SWAP | 8.9750 | 9.0440/8.8580 | 8.6370 | res 8.8250 (ha 14 candles) | 0.12564 | -0.0036% | A/compra@8.8250 (0t/1c) | zona_mapeada_setup_A |
| 2026-11-25 17:06 | BTC-USDT-SWAP | 59856.2 | 60388.0/59670.0 | 59856.2 | res 59459.0 (ha 11 candles) | 768.90 | 0.0092% | A/compra@59459.0 (0t/1c) | zona_mapeada_setup_A |
| 2026-11-25 17:06 | ETH-USDT-SWAP | 1683.7 | 1698.4/1678.7 | 1683.7 | res 1687.8 (ha 21 candles) | 25.41 | 0.0069% | — | sem_zona |
| 2026-11-25 17:06 | SOL-USDT-SWAP | 70.29 | 71.07/69.66 | 70.29 | res 70.07 (ha 20 candles) | 1.0829 | -0.0041% | B/compra@68.68 (0t/2c) | zona_mapeada_setup_B |
| 2026-11-25 17:06 | XRP-USDT-SWAP | 0.93870 | 0.94690/0.92770 | 0.93870 | — | 0.01310 | 0.0057% | B/venda@0.93840 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-25 17:06 | DOGE-USDT-SWAP | 0.05575 | 0.05625/0.05508 | 0.05575 | res 0.05551 (ha 21 candles) | 0.00080 | -0.0011% | — | sem_zona |
| 2026-11-25 17:06 | ARB-USDT-SWAP | 0.11092 | 0.11279/0.11055 | 0.11092 | res 0.11093 (ha 13 candles) | 0.00191 | 0.0030% | B/compra@0.11022 (2t/0c) | zona_mapeada_setup_B |
| 2026-11-25 17:06 | WLD-USDT-SWAP | 0.23910 | 0.24290/0.23720 | 0.23910 | — | 0.00438 | -0.0263% | B/venda@0.24120 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-25 17:06 | SUI-USDT-SWAP | 0.66190 | 0.66900/0.65420 | 0.66190 | — | 0.01093 | -0.0129% | — | invalidado_setup_B |
| 2026-11-25 17:06 | UNI-USDT-SWAP | 4.7200 | 4.7660/4.6480 | 4.7200 | res 4.7460 (ha 20 candles) | 0.08264 | 0.0100% | B/compra@4.6280 (1t/1c) | zona_mapeada_setup_B |
| 2026-11-25 17:06 | LINK-USDT-SWAP | 9.0750 | 9.1300/8.9700 | 9.0750 | res 8.8250 (ha 15 candles) | 0.13271 | -0.0006% | A/compra@8.8250 (0t/2c) | zona_mapeada_setup_A |
| 2026-11-25 18:06 | BTC-USDT-SWAP | 60246.0 | 60365.9/59766.8 | 59856.2 | res 59459.0 (ha 12 candles) | 785.73 | 0.0100% | A/compra@59459.0 (0t/2c) | zona_mapeada_setup_A |
| 2026-11-25 18:06 | ETH-USDT-SWAP | 1689.5 | 1691.6/1678.3 | 1683.7 | res 1687.8 (ha 22 candles) | 25.59 | 0.0085% | A/compra@1687.8 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-25 18:06 | SOL-USDT-SWAP | 70.59 | 70.66/70.06 | 70.29 | res 70.07 (ha 21 candles) | 1.0879 | -0.0007% | B/compra@68.68 (0t/3c) | zona_mapeada_setup_B |
| 2026-11-25 18:06 | XRP-USDT-SWAP | 0.94180 | 0.94210/0.93390 | 0.93870 | — | 0.01321 | 0.0071% | — | invalidado_setup_B |
| 2026-11-25 18:06 | DOGE-USDT-SWAP | 0.05596 | 0.05604/0.05553 | 0.05575 | res 0.05551 (ha 22 candles) | 0.00081 | 0.0023% | — | sem_zona |
| 2026-11-25 18:06 | ARB-USDT-SWAP | 0.11174 | 0.11196/0.11058 | 0.11092 | res 0.11093 (ha 14 candles) | 0.00189 | 0.0013% | — | descartado_rr_baixo_setup_B |
| 2026-11-25 18:06 | WLD-USDT-SWAP | 0.24140 | 0.24260/0.23830 | 0.23910 | — | 0.00451 | -0.0221% | B/venda@0.24120 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-25 18:06 | SUI-USDT-SWAP | 0.66460 | 0.66540/0.65930 | 0.66190 | — | 0.01095 | -0.0063% | B/venda@0.66830 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-25 18:06 | UNI-USDT-SWAP | 4.7560 | 4.7590/4.7110 | 4.7200 | res 4.7460 (ha 21 candles) | 0.08271 | 0.0100% | B/compra@4.6280 (1t/2c) | zona_mapeada_setup_B |
| 2026-11-25 18:06 | LINK-USDT-SWAP | 9.1120 | 9.1250/9.0500 | 9.0750 | res 8.8250 (ha 16 candles) | 0.13329 | 0.0049% | A/compra@8.8250 (0t/3c) | zona_mapeada_setup_A |
| 2026-11-25 19:06 | BTC-USDT-SWAP | 60214.0 | 60489.7/60140.0 | 59856.2 | res 59459.0 (ha 13 candles) | 753.29 | 0.0100% | A/compra@59459.0 (0t/3c) | zona_mapeada_setup_A |
| 2026-11-25 19:06 | ETH-USDT-SWAP | 1685.4 | 1693.7/1685.3 | 1683.7 | res 1687.8 (ha 23 candles) | 23.84 | 0.0084% | A/compra@1687.8 (1t/0c) | zona_mapeada_setup_A |
| 2026-11-25 19:06 | SOL-USDT-SWAP | 70.60 | 70.95/70.36 | 70.29 | res 70.07 (ha 22 candles) | 1.0350 | 0.0014% | B/compra@68.68 (0t/4c) | zona_mapeada_setup_B |
| 2026-11-25 19:06 | XRP-USDT-SWAP | 0.94070 | 0.94840/0.94050 | 0.93870 | — | 0.01279 | 0.0068% | B/compra@0.94500 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-25 19:06 | DOGE-USDT-SWAP | 0.05590 | 0.05637/0.05586 | 0.05575 | res 0.05551 (ha 23 candles) | 0.00077 | 0.0036% | — | sem_zona |
| 2026-11-25 19:06 | ARB-USDT-SWAP | 0.11159 | 0.11225/0.11104 | 0.11092 | res 0.11093 (ha 15 candles) | 0.00184 | -0.0017% | A/compra@0.11093 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-25 19:06 | WLD-USDT-SWAP | 0.23980 | 0.24290/0.23880 | 0.23910 | — | 0.00444 | -0.0185% | — | descartado_rr_baixo_setup_B |
| 2026-11-25 19:06 | SUI-USDT-SWAP | 0.66310 | 0.66750/0.66270 | 0.66190 | — | 0.01041 | -0.0024% | — | descartado_rr_baixo_setup_B |
| 2026-11-25 19:06 | UNI-USDT-SWAP | 4.7380 | 4.7710/4.7270 | 4.7200 | res 4.7460 (ha 22 candles) | 0.07836 | 0.0100% | B/compra@4.6280 (1t/3c) | zona_mapeada_setup_B |
| 2026-11-25 19:06 | LINK-USDT-SWAP | 9.0600 | 9.1330/9.0560 | 9.0750 | res 8.8250 (ha 17 candles) | 0.12943 | 0.0078% | A/compra@8.8250 (0t/4c) | zona_mapeada_setup_A |
| 2026-11-25 20:06 | BTC-USDT-SWAP | 60091.5 | 60244.5/60020.0 | 59856.2 | res 59459.0 (ha 14 candles) | 714.45 | 0.0100% | A/compra@59459.0 (0t/4c) | zona_mapeada_setup_A |
| 2026-11-25 20:06 | ETH-USDT-SWAP | 1686.0 | 1688.3/1680.9 | 1683.7 | res 1698.4 (ha 3 candles) | 23.02 | 0.0078% | — | descartado_rr_baixo_setup_A |
| 2026-11-25 20:06 | SOL-USDT-SWAP | 70.53 | 70.63/70.34 | 70.29 | res 71.07 (ha 3 candles) | 0.99857 | 0.0043% | B/compra@68.68 (0t/5c) | zona_mapeada_setup_B |
| 2026-11-25 20:06 | XRP-USDT-SWAP | 0.93660 | 0.94070/0.93530 | 0.93870 | — | 0.01226 | 0.0069% | B/compra@0.94500 (0t/1c) | zona_mapeada_setup_B |
| 2026-11-25 20:06 | DOGE-USDT-SWAP | 0.05591 | 0.05598/0.05575 | 0.05575 | res 0.05551 (ha 24 candles) | 0.00075 | 0.0068% | — | sem_zona |
| 2026-11-25 20:06 | ARB-USDT-SWAP | 0.11205 | 0.11214/0.11123 | 0.11092 | res 0.11279 (ha 3 candles) | 0.00184 | -0.0012% | — | descartado_rr_baixo_setup_A |
| 2026-11-25 20:06 | WLD-USDT-SWAP | 0.23890 | 0.23990/0.23850 | 0.23910 | — | 0.00438 | -0.0127% | — | sem_zona |
| 2026-11-25 20:06 | SUI-USDT-SWAP | 0.66320 | 0.66440/0.66140 | 0.66190 | — | 0.01013 | 0.0025% | — | sem_zona |
| 2026-11-25 20:06 | UNI-USDT-SWAP | 4.7120 | 4.7390/4.7110 | 4.7200 | res 4.7460 (ha 23 candles) | 0.07657 | 0.0100% | B/compra@4.6280 (1t/4c) | zona_mapeada_setup_B |
| 2026-11-25 20:06 | LINK-USDT-SWAP | 9.0290 | 9.0690/9.0150 | 9.0750 | res 8.8250 (ha 18 candles) | 0.12664 | 0.0100% | A/compra@8.8250 (0t/5c) | zona_mapeada_setup_A |
| 2026-11-25 21:06 | BTC-USDT-SWAP | 60432.7 | 60544.3/59911.5 | 60432.7 | res 59459.0 (ha 15 candles) | 713.79 | 0.0100% | A/compra@59459.0 (0t/5c) | zona_mapeada_setup_A |
| 2026-11-25 21:06 | ETH-USDT-SWAP | 1691.8 | 1696.5/1679.3 | 1691.8 | res 1698.4 (ha 4 candles) | 22.87 | 0.0065% | — | sem_zona |
| 2026-11-25 21:06 | SOL-USDT-SWAP | 70.45 | 70.62/70.20 | 70.45 | res 71.07 (ha 4 candles) | 0.97143 | 0.0071% | B/compra@68.68 (0t/6c) | zona_mapeada_setup_B |
| 2026-11-25 21:06 | XRP-USDT-SWAP | 0.93730 | 0.93820/0.93210 | 0.93730 | — | 0.01194 | 0.0054% | B/compra@0.94500 (0t/2c) | zona_mapeada_setup_B |
| 2026-11-25 21:06 | DOGE-USDT-SWAP | 0.05601 | 0.05603/0.05570 | 0.05601 | res 0.05551 (ha 25 candles) | 0.00072 | 0.0074% | — | sem_zona |
| 2026-11-25 21:06 | ARB-USDT-SWAP | 0.11306 | 0.11325/0.11178 | 0.11306 | res 0.11279 (ha 4 candles) | 0.00181 | 0.0029% | A/compra@0.11279 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-25 21:06 | WLD-USDT-SWAP | 0.23980 | 0.24040/0.23790 | 0.23980 | — | 0.00429 | -0.0077% | B/compra@0.24230 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-25 21:06 | SUI-USDT-SWAP | 0.66710 | 0.66810/0.66070 | 0.66710 | — | 0.00991 | 0.0057% | — | sem_zona |
| 2026-11-25 21:06 | UNI-USDT-SWAP | 4.7440 | 4.7450/4.6860 | 4.7440 | res 4.7460 (ha 24 candles) | 0.07607 | 0.0100% | B/compra@4.6280 (1t/5c) | zona_mapeada_setup_B |
| 2026-11-25 21:06 | LINK-USDT-SWAP | 9.0500 | 9.0640/8.9910 | 9.0500 | res 8.8250 (ha 19 candles) | 0.12164 | 0.0100% | A/compra@8.8250 (0t/6c) | zona_mapeada_setup_A |
| 2026-11-25 22:06 | BTC-USDT-SWAP | 60503.9 | 61620.0/60341.9 | 60432.7 | res 59459.0 (ha 16 candles) | 774.70 | 0.0100% | A/compra@59459.0 (0t/6c) | zona_mapeada_setup_A |
| 2026-11-25 22:06 | ETH-USDT-SWAP | 1696.8 | 1729.7/1689.5 | 1691.8 | res 1698.4 (ha 5 candles) | 25.20 | 0.0072% | B/compra@1709.1 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-25 22:06 | SOL-USDT-SWAP | 70.81 | 71.90/70.36 | 70.45 | res 71.07 (ha 5 candles) | 1.0593 | 0.0096% | B/compra@68.68 (0t/7c) | zona_mapeada_setup_B |
| 2026-11-25 22:06 | XRP-USDT-SWAP | 0.94000 | 0.95320/0.93600 | 0.93730 | — | 0.01270 | 0.0043% | — | invalidado_setup_B |
| 2026-11-25 22:06 | DOGE-USDT-SWAP | 0.05638 | 0.05718/0.05596 | 0.05601 | res 0.05551 (ha 26 candles) | 0.00079 | 0.0062% | — | sem_zona |
| 2026-11-25 22:06 | ARB-USDT-SWAP | 0.11354 | 0.11585/0.11297 | 0.11306 | res 0.11279 (ha 5 candles) | 0.00191 | 0.0063% | A/compra@0.11279 (1t/0c) | zona_mapeada_setup_A |
| 2026-11-25 22:06 | WLD-USDT-SWAP | 0.24100 | 0.24510/0.23940 | 0.23980 | — | 0.00451 | -0.0079% | — | invalidado_setup_B |
| 2026-11-25 22:06 | SUI-USDT-SWAP | 0.67170 | 0.68400/0.66640 | 0.66710 | — | 0.01075 | 0.0091% | B/compra@0.67470 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-25 22:06 | UNI-USDT-SWAP | 4.7230 | 4.8530/4.7150 | 4.7440 | res 4.7460 (ha 25 candles) | 0.08379 | 0.0100% | B/compra@4.6280 (1t/6c) | zona_mapeada_setup_B |
| 2026-11-25 22:06 | LINK-USDT-SWAP | 9.0980 | 9.2370/9.0430 | 9.0500 | res 8.8250 (ha 20 candles) | 0.13193 | 0.0073% | A/compra@8.8250 (0t/7c) | zona_mapeada_setup_A |
| 2026-11-25 23:06 | BTC-USDT-SWAP | 60847.0 | 60959.6/60438.7 | 60432.7 | res 59459.0 (ha 17 candles) | 777.69 | 0.0100% | A/compra@59459.0 (0t/7c) | zona_mapeada_setup_A |
| 2026-11-25 23:06 | ETH-USDT-SWAP | 1702.0 | 1706.4/1694.4 | 1691.8 | res 1698.4 (ha 6 candles) | 25.00 | 0.0083% | — | invalidado_setup_B |
| 2026-11-25 23:06 | SOL-USDT-SWAP | 71.10 | 71.19/70.67 | 70.45 | res 71.07 (ha 6 candles) | 1.0521 | 0.0100% | — | zona_expirada_setup_B |
| 2026-11-25 23:06 | XRP-USDT-SWAP | 0.95180 | 0.95210/0.93850 | 0.93730 | — | 0.01304 | 0.0038% | B/compra@0.95390 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-25 23:06 | DOGE-USDT-SWAP | 0.05669 | 0.05677/0.05628 | 0.05601 | res 0.05551 (ha 27 candles) | 0.00079 | 0.0043% | — | sem_zona |
| 2026-11-25 23:06 | ARB-USDT-SWAP | 0.11388 | 0.11413/0.11300 | 0.11306 | res 0.11279 (ha 6 candles) | 0.00194 | 0.0078% | — | descartado_rr_baixo_setup_A |
| 2026-11-25 23:06 | WLD-USDT-SWAP | 0.24320 | 0.24370/0.24050 | 0.23980 | — | 0.00456 | -0.0116% | — | sem_zona |
| 2026-11-25 23:06 | SUI-USDT-SWAP | 0.67560 | 0.67640/0.67020 | 0.66710 | — | 0.01056 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-11-25 23:06 | UNI-USDT-SWAP | 4.7680 | 4.7790/4.7170 | 4.7440 | res 4.7460 (ha 26 candles) | 0.08529 | 0.0100% | B/compra@4.6280 (1t/7c) | zona_mapeada_setup_B |
| 2026-11-25 23:06 | LINK-USDT-SWAP | 9.1900 | 9.2050/9.0840 | 9.0500 | res 8.8250 (ha 21 candles) | 0.13479 | 0.0044% | — | zona_expirada_setup_A |
| 2026-11-26 00:06 | BTC-USDT-SWAP | 60684.4 | 61088.5/60584.2 | 60432.7 | res 59459.0 (ha 18 candles) | 790.48 | 0.0097% | — | zona_expirada_setup_A |
| 2026-11-26 00:06 | ETH-USDT-SWAP | 1697.9 | 1708.5/1694.5 | 1691.8 | res 1698.4 (ha 7 candles) | 25.06 | 0.0087% | — | sem_zona |
| 2026-11-26 00:06 | SOL-USDT-SWAP | 71.13 | 71.55/70.96 | 70.45 | res 71.07 (ha 7 candles) | 1.0507 | 0.0100% | A/compra@71.07 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-26 00:06 | XRP-USDT-SWAP | 0.95510 | 0.96030/0.95090 | 0.93730 | — | 0.01326 | 0.0019% | B/compra@0.95390 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-26 00:06 | DOGE-USDT-SWAP | 0.05669 | 0.05696/0.05656 | 0.05601 | res 0.05551 (ha 28 candles) | 0.00079 | 0.0024% | A/compra@0.05551 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-26 00:06 | ARB-USDT-SWAP | 0.11411 | 0.11488/0.11348 | 0.11306 | res 0.11279 (ha 7 candles) | 0.00196 | 0.0083% | — | sem_zona |
| 2026-11-26 00:06 | WLD-USDT-SWAP | 0.24380 | 0.24630/0.24280 | 0.23980 | — | 0.00456 | -0.0159% | — | sem_zona |
| 2026-11-26 00:06 | SUI-USDT-SWAP | 0.67240 | 0.68090/0.67180 | 0.66710 | — | 0.01082 | 0.0100% | — | sem_zona |
| 2026-11-26 00:06 | UNI-USDT-SWAP | 4.7590 | 4.8120/4.7510 | 4.7440 | res 4.7460 (ha 27 candles) | 0.08643 | 0.0090% | — | zona_expirada_setup_B |
| 2026-11-26 00:06 | LINK-USDT-SWAP | 9.1470 | 9.2420/9.1300 | 9.0500 | res 8.8250 (ha 22 candles) | 0.13814 | 0.0009% | — | sem_zona |
| 2026-11-26 01:06 | BTC-USDT-SWAP | 60754.5 | 60922.1/60609.0 | 60754.5 | — | 743.32 | 0.0087% | B/venda@60970.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-26 01:06 | ETH-USDT-SWAP | 1697.3 | 1701.7/1692.2 | 1697.3 | — | 23.46 | 0.0099% | — | sem_zona |
| 2026-11-26 01:06 | SOL-USDT-SWAP | 70.99 | 71.27/70.90 | 70.99 | — | 0.98000 | 0.0100% | A/compra@71.07 (1t/0c) | zona_mapeada_setup_A |
| 2026-11-26 01:06 | XRP-USDT-SWAP | 0.95700 | 0.96010/0.95420 | 0.95700 | — | 0.01246 | 0.0002% | B/compra@0.95390 (2t/0c) | zona_mapeada_setup_B |
| 2026-11-26 01:06 | DOGE-USDT-SWAP | 0.05684 | 0.05695/0.05658 | 0.05684 | — | 0.00074 | -0.0000% | A/compra@0.05551 (0t/1c) | zona_mapeada_setup_A |
| 2026-11-26 01:06 | ARB-USDT-SWAP | 0.11398 | 0.11443/0.11379 | 0.11398 | — | 0.00186 | 0.0078% | B/venda@0.11436 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-26 01:06 | WLD-USDT-SWAP | 0.24290 | 0.24430/0.24280 | 0.24290 | — | 0.00432 | -0.0190% | — | sem_zona |
| 2026-11-26 01:06 | SUI-USDT-SWAP | 0.67290 | 0.67550/0.67030 | 0.67290 | — | 0.01031 | 0.0084% | — | sem_zona |
| 2026-11-26 01:06 | UNI-USDT-SWAP | 4.7620 | 4.7880/4.7530 | 4.7620 | — | 0.08236 | 0.0078% | B/venda@4.7890 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-26 01:06 | LINK-USDT-SWAP | 9.1920 | 9.2220/9.1350 | 9.1920 | — | 0.13336 | 0.0006% | B/venda@9.2750 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-26 02:06 | BTC-USDT-SWAP | 60948.2 | 61119.8/60734.1 | 60754.5 | — | 687.14 | 0.0084% | B/venda@60970.0 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-26 02:06 | ETH-USDT-SWAP | 1701.8 | 1706.8/1697.0 | 1697.3 | — | 21.31 | 0.0095% | B/venda@1716.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-26 02:06 | SOL-USDT-SWAP | 71.10 | 71.28/70.98 | 70.99 | — | 0.88000 | 0.0100% | A/compra@71.07 (2t/0c) | zona_mapeada_setup_A |
| 2026-11-26 02:06 | XRP-USDT-SWAP | 0.95760 | 0.96110/0.95610 | 0.95700 | — | 0.01159 | -0.0006% | — | zona_expirada_setup_B |
| 2026-11-26 02:06 | DOGE-USDT-SWAP | 0.05682 | 0.05706/0.05675 | 0.05684 | — | 0.00068 | -0.0015% | A/compra@0.05551 (0t/2c) | zona_mapeada_setup_A |
| 2026-11-26 02:06 | ARB-USDT-SWAP | 0.11459 | 0.11515/0.11391 | 0.11398 | — | 0.00174 | 0.0050% | B/venda@0.11436 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-26 02:06 | WLD-USDT-SWAP | 0.24320 | 0.24410/0.24270 | 0.24290 | — | 0.00404 | -0.0199% | — | sem_zona |
| 2026-11-26 02:06 | SUI-USDT-SWAP | 0.67110 | 0.67470/0.67030 | 0.67290 | — | 0.00969 | 0.0072% | — | sem_zona |
| 2026-11-26 02:06 | UNI-USDT-SWAP | 4.7630 | 4.7810/4.7580 | 4.7620 | — | 0.07607 | 0.0055% | B/venda@4.7890 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-26 02:06 | LINK-USDT-SWAP | 9.2330 | 9.2510/9.1900 | 9.1920 | — | 0.12329 | 0.0017% | B/venda@9.2750 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-26 03:06 | BTC-USDT-SWAP | 60787.6 | 61046.3/60750.0 | 60754.5 | — | 632.91 | 0.0079% | — | descartado_rr_baixo_setup_B |
| 2026-11-26 03:06 | ETH-USDT-SWAP | 1694.0 | 1703.3/1692.5 | 1697.3 | — | 18.64 | 0.0091% | B/venda@1716.0 (0t/1c) | zona_mapeada_setup_B |
| 2026-11-26 03:06 | SOL-USDT-SWAP | 70.91 | 71.37/70.86 | 70.99 | — | 0.80929 | 0.0100% | — | zona_expirada_setup_A |
| 2026-11-26 03:06 | XRP-USDT-SWAP | 0.95870 | 0.96340/0.95750 | 0.95700 | — | 0.01049 | -0.0004% | — | sem_zona |
| 2026-11-26 03:06 | DOGE-USDT-SWAP | 0.05669 | 0.05693/0.05666 | 0.05684 | — | 0.00062 | 0.0002% | A/compra@0.05551 (0t/3c) | zona_mapeada_setup_A |
| 2026-11-26 03:06 | ARB-USDT-SWAP | 0.11502 | 0.11566/0.11429 | 0.11398 | — | 0.00163 | 0.0052% | — | invalidado_setup_B |
| 2026-11-26 03:06 | WLD-USDT-SWAP | 0.24340 | 0.24380/0.24260 | 0.24290 | — | 0.00369 | -0.0191% | B/venda@0.24120 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-26 03:06 | SUI-USDT-SWAP | 0.67140 | 0.67370/0.66970 | 0.67290 | — | 0.00884 | 0.0065% | B/venda@0.66830 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-26 03:06 | UNI-USDT-SWAP | 4.7250 | 4.7680/4.7120 | 4.7620 | — | 0.07186 | 0.0051% | B/venda@4.7890 (1t/1c) | zona_mapeada_setup_B |
| 2026-11-26 03:06 | LINK-USDT-SWAP | 9.2190 | 9.2580/9.2130 | 9.1920 | — | 0.11279 | 0.0033% | — | confirmado_calibracao_setup_B |
| 2026-11-26 04:06 | BTC-USDT-SWAP | 60526.5 | 60796.7/60343.0 | 60754.5 | — | 600.07 | 0.0060% | B/compra@60339.6 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-26 04:06 | ETH-USDT-SWAP | 1686.8 | 1694.3/1681.6 | 1697.3 | — | 17.22 | 0.0085% | B/venda@1716.0 (0t/2c) | zona_mapeada_setup_B |
| 2026-11-26 04:06 | SOL-USDT-SWAP | 70.64 | 70.96/70.49 | 70.99 | — | 0.75714 | 0.0100% | B/venda@71.07 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-26 04:06 | XRP-USDT-SWAP | 0.94960 | 0.95890/0.94880 | 0.95700 | — | 0.01046 | 0.0010% | B/compra@0.94500 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-26 04:06 | DOGE-USDT-SWAP | 0.05630 | 0.05670/0.05625 | 0.05684 | — | 0.00061 | 0.0032% | A/compra@0.05551 (0t/4c) | zona_mapeada_setup_A |
| 2026-11-26 04:06 | ARB-USDT-SWAP | 0.11419 | 0.11526/0.11399 | 0.11398 | — | 0.00160 | 0.0066% | — | sem_zona |
| 2026-11-26 04:06 | WLD-USDT-SWAP | 0.23990 | 0.24350/0.23930 | 0.24290 | — | 0.00362 | -0.0155% | — | descartado_rr_baixo_setup_B |
| 2026-11-26 04:06 | SUI-USDT-SWAP | 0.66620 | 0.67220/0.66490 | 0.67290 | — | 0.00872 | 0.0063% | — | descartado_rr_baixo_setup_B |
| 2026-11-26 04:06 | UNI-USDT-SWAP | 4.6810 | 4.7260/4.6650 | 4.7620 | — | 0.07186 | 0.0067% | B/venda@4.7890 (1t/2c) | zona_mapeada_setup_B |
| 2026-11-26 04:06 | LINK-USDT-SWAP | 9.1570 | 9.2210/9.1400 | 9.1920 | — | 0.11100 | 0.0090% | — | sem_zona |
| 2026-11-26 05:06 | BTC-USDT-SWAP | 60500.6 | 60645.0/60380.0 | 60500.6 | — | 511.62 | 0.0070% | B/compra@60339.6 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-26 05:06 | ETH-USDT-SWAP | 1688.8 | 1693.6/1685.3 | 1688.8 | — | 14.58 | 0.0073% | B/venda@1716.0 (0t/3c) | zona_mapeada_setup_B |
| 2026-11-26 05:06 | SOL-USDT-SWAP | 70.80 | 71.10/70.60 | 70.80 | — | 0.64643 | 0.0100% | B/venda@71.07 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-26 05:06 | XRP-USDT-SWAP | 0.95260 | 0.95460/0.94860 | 0.95260 | — | 0.00924 | 0.0032% | B/compra@0.94500 (0t/1c) | zona_mapeada_setup_B |
| 2026-11-26 05:06 | DOGE-USDT-SWAP | 0.05647 | 0.05659/0.05627 | 0.05647 | — | 0.00051 | 0.0043% | A/compra@0.05551 (0t/5c) | zona_mapeada_setup_A |
| 2026-11-26 05:06 | ARB-USDT-SWAP | 0.11441 | 0.11482/0.11393 | 0.11441 | — | 0.00141 | 0.0079% | — | sem_zona |
| 2026-11-26 05:06 | WLD-USDT-SWAP | 0.24130 | 0.24180/0.23960 | 0.24130 | — | 0.00320 | -0.0081% | — | sem_zona |
| 2026-11-26 05:06 | SUI-USDT-SWAP | 0.66950 | 0.67040/0.66540 | 0.66950 | — | 0.00756 | 0.0075% | — | sem_zona |
| 2026-11-26 05:06 | UNI-USDT-SWAP | 4.7170 | 4.7180/4.6740 | 4.7170 | — | 0.06050 | 0.0089% | B/venda@4.7890 (1t/3c) | zona_mapeada_setup_B |
| 2026-11-26 05:06 | LINK-USDT-SWAP | 9.1560 | 9.1820/9.1380 | 9.1560 | — | 0.09786 | 0.0100% | — | sem_zona |
| 2026-11-26 06:06 | BTC-USDT-SWAP | 60886.6 | 61040.0/60500.6 | 60500.6 | — | 505.76 | 0.0081% | B/compra@60339.6 (1t/1c) | zona_mapeada_setup_B |
| 2026-11-26 06:06 | ETH-USDT-SWAP | 1700.5 | 1702.6/1686.3 | 1688.8 | — | 14.25 | 0.0067% | B/venda@1716.0 (0t/4c) | zona_mapeada_setup_B |
| 2026-11-26 06:06 | SOL-USDT-SWAP | 71.07 | 71.33/70.78 | 70.80 | — | 0.61857 | 0.0100% | B/venda@71.07 (2t/0c) | zona_mapeada_setup_B |
| 2026-11-26 06:06 | XRP-USDT-SWAP | 0.95660 | 0.95970/0.95120 | 0.95260 | — | 0.00917 | 0.0042% | B/compra@0.94500 (0t/2c) | zona_mapeada_setup_B |
| 2026-11-26 06:06 | DOGE-USDT-SWAP | 0.05670 | 0.05690/0.05641 | 0.05647 | — | 0.00051 | 0.0055% | A/compra@0.05551 (0t/6c) | zona_mapeada_setup_A |
| 2026-11-26 06:06 | ARB-USDT-SWAP | 0.11551 | 0.11639/0.11420 | 0.11441 | — | 0.00144 | 0.0100% | — | sem_zona |
| 2026-11-26 06:06 | WLD-USDT-SWAP | 0.24350 | 0.24410/0.24100 | 0.24130 | — | 0.00314 | -0.0088% | B/compra@0.24230 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-26 06:06 | SUI-USDT-SWAP | 0.67010 | 0.67420/0.66820 | 0.66950 | — | 0.00721 | 0.0075% | — | sem_zona |
| 2026-11-26 06:06 | UNI-USDT-SWAP | 4.7520 | 4.7680/4.7130 | 4.7170 | — | 0.05943 | 0.0100% | B/venda@4.7890 (1t/4c) | zona_mapeada_setup_B |
| 2026-11-26 06:06 | LINK-USDT-SWAP | 9.2500 | 9.2730/9.1390 | 9.1560 | — | 0.09414 | 0.0100% | — | sem_zona |
| 2026-11-26 07:06 | BTC-USDT-SWAP | 60913.0 | 60967.6/60724.4 | 60500.6 | — | 471.84 | 0.0089% | B/compra@60339.6 (1t/2c) | zona_mapeada_setup_B |
| 2026-11-26 07:06 | ETH-USDT-SWAP | 1703.0 | 1706.0/1697.4 | 1688.8 | — | 13.45 | 0.0060% | B/venda@1716.0 (0t/5c) | zona_mapeada_setup_B |
| 2026-11-26 07:06 | SOL-USDT-SWAP | 71.09 | 71.25/70.86 | 70.80 | — | 0.54571 | 0.0100% | — | zona_expirada_setup_B |
| 2026-11-26 07:06 | XRP-USDT-SWAP | 0.95390 | 0.95660/0.95070 | 0.95260 | — | 0.00822 | 0.0054% | B/compra@0.94500 (0t/3c) | zona_mapeada_setup_B |
| 2026-11-26 07:06 | DOGE-USDT-SWAP | 0.05673 | 0.05681/0.05656 | 0.05647 | — | 0.00044 | 0.0067% | A/compra@0.05551 (0t/7c) | zona_mapeada_setup_A |
| 2026-11-26 07:06 | ARB-USDT-SWAP | 0.11526 | 0.11557/0.11475 | 0.11441 | — | 0.00134 | 0.0083% | — | sem_zona |
| 2026-11-26 07:06 | WLD-USDT-SWAP | 0.24320 | 0.24350/0.24160 | 0.24130 | — | 0.00287 | -0.0042% | B/compra@0.24230 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-26 07:06 | SUI-USDT-SWAP | 0.66870 | 0.67030/0.66760 | 0.66950 | — | 0.00634 | 0.0100% | — | sem_zona |
| 2026-11-26 07:06 | UNI-USDT-SWAP | 4.7420 | 4.7590/4.7350 | 4.7170 | — | 0.05271 | 0.0100% | B/venda@4.7890 (1t/5c) | zona_mapeada_setup_B |
| 2026-11-26 07:06 | LINK-USDT-SWAP | 9.2510 | 9.2710/9.2200 | 9.1560 | — | 0.08636 | 0.0100% | — | sem_zona |
| 2026-11-26 08:06 | BTC-USDT-SWAP | 60484.6 | 60985.0/60435.2 | 60500.6 | — | 468.32 | 0.0080% | B/compra@60339.6 (2t/0c) | zona_mapeada_setup_B |
| 2026-11-26 08:06 | ETH-USDT-SWAP | 1694.3 | 1704.4/1692.2 | 1688.8 | — | 13.37 | 0.0059% | B/venda@1716.0 (0t/6c) | zona_mapeada_setup_B |
| 2026-11-26 08:06 | SOL-USDT-SWAP | 70.54 | 71.16/70.50 | 70.80 | — | 0.55000 | 0.0100% | — | sem_zona |
| 2026-11-26 08:06 | XRP-USDT-SWAP | 0.94960 | 0.95460/0.94700 | 0.95260 | — | 0.00818 | 0.0067% | B/compra@0.94500 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-26 08:06 | DOGE-USDT-SWAP | 0.05655 | 0.05675/0.05650 | 0.05647 | — | 0.00042 | 0.0100% | — | zona_expirada_setup_A |
| 2026-11-26 08:06 | ARB-USDT-SWAP | 0.11417 | 0.11525/0.11387 | 0.11441 | — | 0.00134 | 0.0059% | — | sem_zona |
| 2026-11-26 08:06 | WLD-USDT-SWAP | 0.24330 | 0.24490/0.24250 | 0.24130 | — | 0.00274 | -0.0049% | B/compra@0.24230 (2t/0c) | zona_mapeada_setup_B |
| 2026-11-26 08:06 | SUI-USDT-SWAP | 0.66580 | 0.66980/0.66430 | 0.66950 | — | 0.00630 | 0.0100% | — | sem_zona |
| 2026-11-26 08:06 | UNI-USDT-SWAP | 4.7220 | 4.7580/4.7110 | 4.7170 | — | 0.05264 | 0.0100% | B/venda@4.7890 (1t/6c) | zona_mapeada_setup_B |
| 2026-11-26 08:06 | LINK-USDT-SWAP | 9.1980 | 9.2650/9.1780 | 9.1560 | — | 0.08721 | 0.0100% | — | sem_zona |
| 2026-11-26 09:06 | BTC-USDT-SWAP | 60684.5 | 60763.2/60461.1 | 60684.5 | — | 464.92 | 0.0063% | — | descartado_rr_baixo_setup_B |
| 2026-11-26 09:06 | ETH-USDT-SWAP | 1699.7 | 1701.5/1692.6 | 1699.7 | — | 13.41 | 0.0064% | B/venda@1716.0 (0t/7c) | zona_mapeada_setup_B |
| 2026-11-26 09:06 | SOL-USDT-SWAP | 70.84 | 70.89/70.42 | 70.84 | — | 0.54143 | 0.0100% | — | sem_zona |
| 2026-11-26 09:06 | XRP-USDT-SWAP | 0.95200 | 0.95370/0.94880 | 0.95200 | — | 0.00796 | 0.0080% | B/compra@0.94500 (1t/1c) | zona_mapeada_setup_B |
| 2026-11-26 09:06 | DOGE-USDT-SWAP | 0.05684 | 0.05687/0.05648 | 0.05684 | — | 0.00041 | 0.0100% | — | sem_zona |
| 2026-11-26 09:06 | ARB-USDT-SWAP | 0.11466 | 0.11493/0.11400 | 0.11466 | — | 0.00132 | 0.0051% | — | sem_zona |
| 2026-11-26 09:06 | WLD-USDT-SWAP | 0.24540 | 0.24560/0.24280 | 0.24540 | — | 0.00264 | -0.0056% | — | descartado_rr_baixo_setup_B |
| 2026-11-26 09:06 | SUI-USDT-SWAP | 0.66930 | 0.66990/0.66510 | 0.66930 | — | 0.00630 | 0.0100% | — | sem_zona |
| 2026-11-26 09:06 | UNI-USDT-SWAP | 4.7270 | 4.7370/4.7120 | 4.7270 | — | 0.05129 | 0.0100% | B/venda@4.7890 (1t/7c) | zona_mapeada_setup_B |
| 2026-11-26 09:06 | LINK-USDT-SWAP | 9.2260 | 9.2570/9.1830 | 9.2260 | — | 0.08700 | 0.0100% | — | sem_zona |
| 2026-11-26 10:06 | BTC-USDT-SWAP | 60801.4 | 60960.1/60562.6 | 60684.5 | — | 477.28 | 0.0056% | — | sem_zona |
| 2026-11-26 10:06 | ETH-USDT-SWAP | 1705.7 | 1711.9/1698.8 | 1699.7 | — | 13.82 | 0.0074% | B/venda@1716.0 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-26 10:06 | SOL-USDT-SWAP | 70.93 | 71.22/70.64 | 70.84 | — | 0.56214 | 0.0100% | — | sem_zona |
| 2026-11-26 10:06 | XRP-USDT-SWAP | 0.95060 | 0.95600/0.94820 | 0.95200 | — | 0.00814 | 0.0088% | B/compra@0.94500 (1t/2c) | zona_mapeada_setup_B |
| 2026-11-26 10:06 | DOGE-USDT-SWAP | 0.05676 | 0.05711/0.05665 | 0.05684 | — | 0.00043 | 0.0100% | — | sem_zona |
| 2026-11-26 10:06 | ARB-USDT-SWAP | 0.11369 | 0.11531/0.11364 | 0.11466 | — | 0.00138 | 0.0018% | — | sem_zona |
| 2026-11-26 10:06 | WLD-USDT-SWAP | 0.24420 | 0.24670/0.24390 | 0.24540 | — | 0.00274 | -0.0066% | — | sem_zona |
| 2026-11-26 10:06 | SUI-USDT-SWAP | 0.66700 | 0.67320/0.66660 | 0.66930 | — | 0.00656 | 0.0100% | — | sem_zona |
| 2026-11-26 10:06 | UNI-USDT-SWAP | 4.7280 | 4.7530/4.7090 | 4.7270 | — | 0.05243 | 0.0100% | — | zona_expirada_setup_B |
| 2026-11-26 10:06 | LINK-USDT-SWAP | 9.2420 | 9.2630/9.2080 | 9.2260 | — | 0.08707 | 0.0100% | — | sem_zona |
| 2026-11-26 11:06 | BTC-USDT-SWAP | 60850.2 | 60925.0/60759.4 | 60684.5 | — | 443.91 | 0.0048% | B/venda@60970.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-26 11:06 | ETH-USDT-SWAP | 1703.6 | 1708.0/1701.5 | 1699.7 | — | 13.06 | 0.0075% | B/venda@1716.0 (1t/1c) | zona_mapeada_setup_B |
| 2026-11-26 11:06 | SOL-USDT-SWAP | 71.19 | 71.23/70.83 | 70.84 | — | 0.56071 | 0.0100% | B/compra@71.00 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-26 11:06 | XRP-USDT-SWAP | 0.95120 | 0.95250/0.94810 | 0.95200 | — | 0.00801 | 0.0092% | B/compra@0.94500 (1t/3c) | zona_mapeada_setup_B |
| 2026-11-26 11:06 | DOGE-USDT-SWAP | 0.05690 | 0.05694/0.05668 | 0.05684 | — | 0.00042 | 0.0100% | — | sem_zona |
| 2026-11-26 11:06 | ARB-USDT-SWAP | 0.11326 | 0.11369/0.11251 | 0.11466 | — | 0.00136 | 0.0007% | — | sem_zona |
| 2026-11-26 11:06 | WLD-USDT-SWAP | 0.24500 | 0.24570/0.24370 | 0.24540 | — | 0.00271 | -0.0058% | — | sem_zona |
| 2026-11-26 11:06 | SUI-USDT-SWAP | 0.66730 | 0.66900/0.66500 | 0.66930 | — | 0.00631 | 0.0100% | — | sem_zona |
| 2026-11-26 11:06 | UNI-USDT-SWAP | 4.7230 | 4.7330/4.7150 | 4.7270 | — | 0.04950 | 0.0100% | — | sem_zona |
| 2026-11-26 11:06 | LINK-USDT-SWAP | 9.2470 | 9.2560/9.2200 | 9.2260 | — | 0.08443 | 0.0100% | B/venda@9.2750 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-26 12:06 | BTC-USDT-SWAP | 60702.3 | 60938.9/60674.0 | 60684.5 | — | 371.54 | 0.0048% | — | descartado_rr_baixo_setup_B |
| 2026-11-26 12:06 | ETH-USDT-SWAP | 1697.2 | 1707.1/1695.5 | 1699.7 | — | 11.02 | 0.0079% | B/venda@1716.0 (1t/2c) | zona_mapeada_setup_B |
| 2026-11-26 12:06 | SOL-USDT-SWAP | 71.01 | 71.55/70.96 | 70.84 | — | 0.49286 | 0.0100% | B/compra@71.00 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-26 12:06 | XRP-USDT-SWAP | 0.94870 | 0.95420/0.94860 | 0.95200 | — | 0.00719 | 0.0095% | B/compra@0.94500 (1t/4c) | zona_mapeada_setup_B |
| 2026-11-26 12:06 | DOGE-USDT-SWAP | 0.05672 | 0.05727/0.05671 | 0.05684 | — | 0.00038 | 0.0100% | — | sem_zona |
| 2026-11-26 12:06 | ARB-USDT-SWAP | 0.11204 | 0.11366/0.11201 | 0.11466 | — | 0.00127 | -0.0002% | — | sem_zona |
| 2026-11-26 12:06 | WLD-USDT-SWAP | 0.24290 | 0.24610/0.24250 | 0.24540 | — | 0.00256 | -0.0101% | B/venda@0.24120 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-26 12:06 | SUI-USDT-SWAP | 0.66110 | 0.66950/0.66080 | 0.66930 | — | 0.00568 | 0.0100% | — | sem_zona |
| 2026-11-26 12:06 | UNI-USDT-SWAP | 4.6390 | 4.7360/4.6310 | 4.7270 | — | 0.04714 | 0.0100% | B/compra@4.6280 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-26 12:06 | LINK-USDT-SWAP | 9.1840 | 9.2830/9.1630 | 9.2260 | — | 0.07914 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-11-26 13:06 | BTC-USDT-SWAP | 60597.9 | 60702.3/59886.8 | 60597.9 | sup 60343.0 (ha 9 candles) | 392.58 | 0.0046% | — | sem_zona |
| 2026-11-26 13:06 | ETH-USDT-SWAP | 1691.8 | 1697.2/1666.7 | 1691.8 | sup 1681.6 (ha 9 candles) | 12.34 | 0.0061% | B/venda@1716.0 (1t/3c) | zona_mapeada_setup_B |
| 2026-11-26 13:06 | SOL-USDT-SWAP | 71.02 | 71.21/69.74 | 71.02 | sup 70.42 (ha 4 candles) | 0.56071 | 0.0100% | — | invalidado_tendencia_virou_setup_B |
| 2026-11-26 13:06 | XRP-USDT-SWAP | 0.94730 | 0.94870/0.93310 | 0.94730 | — | 0.00733 | 0.0100% | B/compra@0.94500 (2t/0c) | zona_mapeada_setup_B |
| 2026-11-26 13:06 | DOGE-USDT-SWAP | 0.05661 | 0.05673/0.05578 | 0.05661 | — | 0.00041 | 0.0100% | — | sem_zona |
| 2026-11-26 13:06 | ARB-USDT-SWAP | 0.11221 | 0.11231/0.10986 | 0.11221 | — | 0.00136 | 0.0027% | — | sem_zona |
| 2026-11-26 13:06 | WLD-USDT-SWAP | 0.24290 | 0.24330/0.23820 | 0.24290 | — | 0.00269 | -0.0131% | — | invalidado_setup_B |
| 2026-11-26 13:06 | SUI-USDT-SWAP | 0.66300 | 0.66460/0.64930 | 0.66300 | sup 0.66430 (ha 5 candles) | 0.00633 | 0.0100% | A/venda@0.66430 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-26 13:06 | UNI-USDT-SWAP | 4.6200 | 4.6390/4.5360 | 4.6200 | sup 4.6650 (ha 9 candles) | 0.05007 | 0.0088% | B/compra@4.6280 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-26 13:06 | LINK-USDT-SWAP | 9.1840 | 9.2010/9.0340 | 9.1840 | — | 0.08243 | 0.0098% | — | sem_zona |
| 2026-11-26 14:06 | BTC-USDT-SWAP | 60498.1 | 60835.0/60315.2 | 60597.9 | sup 60343.0 (ha 10 candles) | 393.69 | 0.0051% | — | sem_zona |
| 2026-11-26 14:06 | ETH-USDT-SWAP | 1691.3 | 1698.0/1682.2 | 1691.8 | sup 1681.6 (ha 10 candles) | 12.47 | 0.0059% | B/venda@1716.0 (1t/4c) | zona_mapeada_setup_B |
| 2026-11-26 14:06 | SOL-USDT-SWAP | 70.96 | 71.20/70.49 | 71.02 | sup 70.42 (ha 5 candles) | 0.56929 | 0.0100% | — | sem_zona |
| 2026-11-26 14:06 | XRP-USDT-SWAP | 0.95000 | 0.95210/0.94560 | 0.94730 | — | 0.00712 | 0.0100% | — | confirmado_calibracao_setup_B |
| 2026-11-26 14:06 | DOGE-USDT-SWAP | 0.05667 | 0.05683/0.05639 | 0.05661 | — | 0.00041 | 0.0100% | — | sem_zona |
| 2026-11-26 14:06 | ARB-USDT-SWAP | 0.11301 | 0.11311/0.11219 | 0.11221 | — | 0.00133 | 0.0060% | — | sem_zona |
| 2026-11-26 14:06 | WLD-USDT-SWAP | 0.24240 | 0.24390/0.24130 | 0.24290 | — | 0.00263 | -0.0154% | — | sem_zona |
| 2026-11-26 14:06 | SUI-USDT-SWAP | 0.66540 | 0.66620/0.66120 | 0.66300 | sup 0.66430 (ha 6 candles) | 0.00604 | 0.0100% | A/venda@0.66430 (1t/0c) | zona_mapeada_setup_A |
| 2026-11-26 14:06 | UNI-USDT-SWAP | 4.6050 | 4.6560/4.5900 | 4.6200 | sup 4.6650 (ha 10 candles) | 0.05043 | 0.0082% | — | invalidado_setup_B |
| 2026-11-26 14:06 | LINK-USDT-SWAP | 9.1910 | 9.2100/9.1430 | 9.1840 | — | 0.07921 | 0.0082% | — | sem_zona |
| 2026-11-26 15:06 | BTC-USDT-SWAP | 60504.7 | 60634.0/60380.9 | 60597.9 | sup 60343.0 (ha 11 candles) | 389.40 | 0.0052% | — | sem_zona |
| 2026-11-26 15:06 | ETH-USDT-SWAP | 1693.4 | 1695.5/1689.4 | 1691.8 | sup 1681.6 (ha 11 candles) | 12.23 | 0.0051% | B/venda@1716.0 (1t/5c) | zona_mapeada_setup_B |
| 2026-11-26 15:06 | SOL-USDT-SWAP | 71.06 | 71.14/70.78 | 71.02 | sup 70.42 (ha 6 candles) | 0.56857 | 0.0100% | B/venda@71.07 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-26 15:06 | XRP-USDT-SWAP | 0.95150 | 0.95250/0.94710 | 0.94730 | — | 0.00709 | 0.0100% | B/compra@0.95390 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-26 15:06 | DOGE-USDT-SWAP | 0.05685 | 0.05685/0.05658 | 0.05661 | — | 0.00040 | 0.0100% | — | sem_zona |
| 2026-11-26 15:06 | ARB-USDT-SWAP | 0.11313 | 0.11360/0.11275 | 0.11221 | — | 0.00134 | 0.0079% | — | sem_zona |
| 2026-11-26 15:06 | WLD-USDT-SWAP | 0.24190 | 0.24300/0.24120 | 0.24290 | — | 0.00265 | -0.0147% | — | sem_zona |
| 2026-11-26 15:06 | SUI-USDT-SWAP | 0.66680 | 0.66770/0.66440 | 0.66300 | sup 0.66430 (ha 7 candles) | 0.00590 | 0.0100% | — | invalidado_setup_A |
| 2026-11-26 15:06 | UNI-USDT-SWAP | 4.6070 | 4.6270/4.5580 | 4.6200 | sup 4.6650 (ha 11 candles) | 0.05286 | 0.0080% | A/venda@4.6650 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-26 15:06 | LINK-USDT-SWAP | 9.2150 | 9.2190/9.1720 | 9.1840 | — | 0.07636 | 0.0063% | — | sem_zona |
| 2026-11-26 16:06 | BTC-USDT-SWAP | 60446.6 | 60743.6/60355.5 | 60597.9 | sup 59886.8 (ha 3 candles) | 389.57 | 0.0042% | — | sem_zona |
| 2026-11-26 16:06 | ETH-USDT-SWAP | 1699.5 | 1703.7/1691.0 | 1691.8 | sup 1666.7 (ha 3 candles) | 12.44 | 0.0048% | B/venda@1716.0 (1t/6c) | zona_mapeada_setup_B |
| 2026-11-26 16:06 | SOL-USDT-SWAP | 71.27 | 71.51/70.98 | 71.02 | sup 69.74 (ha 3 candles) | 0.58500 | 0.0100% | — | invalidado_setup_B |
| 2026-11-26 16:06 | XRP-USDT-SWAP | 0.95330 | 0.95740/0.95140 | 0.94730 | — | 0.00716 | 0.0100% | B/compra@0.95390 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-26 16:06 | DOGE-USDT-SWAP | 0.05691 | 0.05715/0.05680 | 0.05661 | — | 0.00041 | 0.0100% | — | sem_zona |
| 2026-11-26 16:06 | ARB-USDT-SWAP | 0.11393 | 0.11405/0.11289 | 0.11221 | — | 0.00134 | 0.0078% | B/venda@0.11436 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-26 16:06 | WLD-USDT-SWAP | 0.24330 | 0.24490/0.24180 | 0.24290 | — | 0.00277 | -0.0121% | — | sem_zona |
| 2026-11-26 16:06 | SUI-USDT-SWAP | 0.67060 | 0.67270/0.66640 | 0.66300 | sup 0.64930 (ha 3 candles) | 0.00604 | 0.0100% | B/venda@0.66830 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-26 16:06 | UNI-USDT-SWAP | 4.6550 | 4.6710/4.6070 | 4.6200 | sup 4.5360 (ha 3 candles) | 0.05579 | 0.0071% | A/venda@4.6650 (1t/0c) | zona_mapeada_setup_A |
| 2026-11-26 16:06 | LINK-USDT-SWAP | 9.2660 | 9.2820/9.2140 | 9.1840 | — | 0.07686 | 0.0024% | — | sem_zona |
