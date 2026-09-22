# Log de Monitoramento Automatico -- Multi-Par (script gratuito, GitHub Actions)

> Gerado por script Python sem LLM (ver monitor/fetch_and_check.py). Fonte: OKX. Cobre os pares em PAIRS (configuracao no topo do script) -- BTC-USDT-SWAP e os demais adicionados na expansao de 07/09/2026. Leitura e MECANICA (regras objetivas da secao 4 do plano), sem a prosa qualitativa que o Claude gerava -- cole este log numa conversa do Claude se quiser a leitura interpretativa.

| Data/Hora (BRT) | Par | Close 1h | High/Low 1h | Close 4h | Swing 1h ref | ATR 1h | Funding | Zona ativa | Status checklist |
|---|---|---|---|---|---|---|---|---|---|
| 2026-09-20 19:05 | BTC-USDT-SWAP | 80900.5 | 81053.5/80541.3 | 81154.0 | res 81485.9 (ha 5 candles) | 328.82 | 0.0097% | — | sem_zona |
| 2026-09-20 19:05 | ETH-USDT-SWAP | 2630.0 | 2634.8/2607.0 | 2632.2 | res 2649.0 (ha 4 candles) | 19.23 | 0.0043% | A/compra@2586.2 (0t/6c) | zona_mapeada_setup_A |
| 2026-09-20 19:05 | SOL-USDT-SWAP | 109.84 | 110.09/109.01 | 110.39 | res 108.83 (ha 9 candles) | 0.97857 | 0.0100% | A/compra@108.83 (1t/0c) | zona_mapeada_setup_A |
| 2026-09-20 19:05 | XRP-USDT-SWAP | 1.4018 | 1.4059/1.3909 | 1.4086 | res 1.4169 (ha 5 candles) | 0.01276 | 0.0100% | B/compra@1.3739 (0t/7c) | zona_mapeada_setup_B |
| 2026-09-20 19:05 | DOGE-USDT-SWAP | 0.08688 | 0.08735/0.08607 | 0.08734 | res 0.08780 (ha 4 candles) | 0.00086 | 0.0100% | — | invalidado_setup_B |
| 2026-09-20 19:05 | ARB-USDT-SWAP | 0.21774 | 0.21795/0.20886 | 0.21084 | — | 0.00624 | -0.0032% | — | sem_zona |
| 2026-09-20 19:05 | WLD-USDT-SWAP | 0.43650 | 0.43850/0.42880 | 0.43600 | — | 0.01022 | 0.0087% | — | invalidado_setup_B |
| 2026-09-20 19:05 | SUI-USDT-SWAP | 0.88460 | 0.89090/0.86930 | 0.88030 | res 0.92020 (ha 4 candles) | 0.02173 | 0.0100% | A/compra@0.83220 (0t/6c) | zona_mapeada_setup_A |
| 2026-09-20 19:05 | UNI-USDT-SWAP | 8.8150 | 8.8260/8.5880 | 8.7330 | res 8.9760 (ha 5 candles) | 0.15186 | 0.0001% | — | sem_zona |
| 2026-09-20 19:05 | LINK-USDT-SWAP | 12.45 | 12.50/12.32 | 12.53 | — | 0.15136 | 0.0100% | — | sem_zona |
| 2026-09-20 20:05 | BTC-USDT-SWAP | 81183.7 | 81273.4/80734.6 | 81154.0 | res 81485.9 (ha 6 candles) | 346.91 | 0.0096% | — | sem_zona |
| 2026-09-20 20:05 | ETH-USDT-SWAP | 2638.1 | 2647.0/2622.9 | 2632.2 | res 2649.0 (ha 5 candles) | 19.92 | 0.0048% | A/compra@2586.2 (0t/7c) | zona_mapeada_setup_A |
| 2026-09-20 20:05 | SOL-USDT-SWAP | 110.96 | 111.02/109.56 | 110.39 | res 108.83 (ha 10 candles) | 1.0057 | 0.0100% | A/compra@108.83 (1t/1c) | zona_mapeada_setup_A |
| 2026-09-20 20:05 | XRP-USDT-SWAP | 1.4093 | 1.4125/1.3970 | 1.4086 | res 1.4169 (ha 6 candles) | 0.01316 | 0.0100% | — | zona_expirada_setup_B |
| 2026-09-20 20:05 | DOGE-USDT-SWAP | 0.08744 | 0.08758/0.08661 | 0.08734 | res 0.08780 (ha 5 candles) | 0.00088 | 0.0100% | B/compra@0.08784 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-20 20:05 | ARB-USDT-SWAP | 0.21739 | 0.22494/0.21659 | 0.21084 | — | 0.00636 | -0.0010% | — | sem_zona |
| 2026-09-20 20:05 | WLD-USDT-SWAP | 0.43820 | 0.44060/0.43520 | 0.43600 | — | 0.00994 | 0.0086% | — | sem_zona |
| 2026-09-20 20:05 | SUI-USDT-SWAP | 0.89490 | 0.90440/0.88030 | 0.88030 | res 0.92020 (ha 5 candles) | 0.02255 | 0.0100% | A/compra@0.83220 (0t/7c) | zona_mapeada_setup_A |
| 2026-09-20 20:05 | UNI-USDT-SWAP | 8.7530 | 8.9880/8.7460 | 8.7330 | res 8.9760 (ha 6 candles) | 0.16036 | 0.0006% | — | sem_zona |
| 2026-09-20 20:05 | LINK-USDT-SWAP | 12.50 | 12.55/12.39 | 12.53 | — | 0.15364 | 0.0100% | — | sem_zona |
| 2026-09-20 21:05 | BTC-USDT-SWAP | 81144.3 | 81301.5/81092.5 | 81144.3 | res 81485.9 (ha 7 candles) | 337.74 | 0.0092% | — | sem_zona |
| 2026-09-20 21:05 | ETH-USDT-SWAP | 2643.4 | 2647.9/2630.7 | 2643.4 | res 2649.0 (ha 6 candles) | 20.22 | 0.0037% | — | zona_expirada_setup_A |
| 2026-09-20 21:05 | SOL-USDT-SWAP | 111.12 | 111.42/110.50 | 111.12 | res 108.83 (ha 11 candles) | 1.0157 | 0.0100% | A/compra@108.83 (1t/2c) | zona_mapeada_setup_A |
| 2026-09-20 21:05 | XRP-USDT-SWAP | 1.4101 | 1.4159/1.4071 | 1.4101 | res 1.4169 (ha 7 candles) | 0.01284 | 0.0100% | — | sem_zona |
| 2026-09-20 21:05 | DOGE-USDT-SWAP | 0.08727 | 0.08752/0.08710 | 0.08727 | — | 0.00086 | 0.0100% | B/compra@0.08784 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-20 21:05 | ARB-USDT-SWAP | 0.21764 | 0.22139/0.21584 | 0.21764 | — | 0.00651 | 0.0001% | — | sem_zona |
| 2026-09-20 21:05 | WLD-USDT-SWAP | 0.43520 | 0.43820/0.43450 | 0.43520 | — | 0.00952 | 0.0059% | — | sem_zona |
| 2026-09-20 21:05 | SUI-USDT-SWAP | 0.89680 | 0.90190/0.88680 | 0.89680 | res 0.92020 (ha 6 candles) | 0.02230 | 0.0100% | — | zona_expirada_setup_A |
| 2026-09-20 21:05 | UNI-USDT-SWAP | 8.7240 | 8.7840/8.6080 | 8.7240 | res 8.9760 (ha 7 candles) | 0.16400 | 0.0018% | — | sem_zona |
| 2026-09-20 21:05 | LINK-USDT-SWAP | 12.52 | 12.53/12.45 | 12.52 | res 12.61 (ha 6 candles) | 0.14857 | 0.0100% | — | sem_zona |
| 2026-09-20 22:05 | BTC-USDT-SWAP | 81573.3 | 81823.5/81130.2 | 81144.3 | res 81485.9 (ha 8 candles) | 372.29 | 0.0097% | A/compra@81485.9 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-20 22:05 | ETH-USDT-SWAP | 2688.0 | 2709.9/2642.3 | 2643.4 | res 2649.0 (ha 7 candles) | 24.27 | 0.0065% | A/compra@2649.0 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-20 22:05 | SOL-USDT-SWAP | 112.27 | 112.89/111.10 | 111.12 | res 108.83 (ha 12 candles) | 1.1050 | 0.0100% | A/compra@108.83 (1t/3c) | zona_mapeada_setup_A |
| 2026-09-20 22:05 | XRP-USDT-SWAP | 1.4255 | 1.4329/1.4096 | 1.4101 | res 1.4169 (ha 8 candles) | 0.01372 | 0.0100% | A/compra@1.4169 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-20 22:05 | DOGE-USDT-SWAP | 0.08870 | 0.08896/0.08722 | 0.08727 | — | 0.00093 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-09-20 22:05 | ARB-USDT-SWAP | 0.22065 | 0.22279/0.21636 | 0.21764 | — | 0.00655 | -0.0007% | — | sem_zona |
| 2026-09-20 22:05 | WLD-USDT-SWAP | 0.44220 | 0.44600/0.43500 | 0.43520 | — | 0.00978 | 0.0051% | B/venda@0.44750 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-20 22:05 | SUI-USDT-SWAP | 0.93120 | 0.94900/0.89520 | 0.89680 | res 0.92020 (ha 7 candles) | 0.02524 | 0.0100% | A/compra@0.92020 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-20 22:05 | UNI-USDT-SWAP | 8.8800 | 8.9220/8.6780 | 8.7240 | res 8.9760 (ha 8 candles) | 0.17536 | 0.0055% | — | sem_zona |
| 2026-09-20 22:05 | LINK-USDT-SWAP | 12.71 | 12.79/12.50 | 12.52 | res 12.61 (ha 7 candles) | 0.16279 | 0.0100% | A/compra@12.61 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-20 23:05 | BTC-USDT-SWAP | 80970.9 | 82088.0/80822.4 | 81144.3 | res 81485.9 (ha 9 candles) | 444.97 | 0.0100% | — | invalidado_setup_A |
| 2026-09-20 23:05 | ETH-USDT-SWAP | 2648.2 | 2700.7/2642.1 | 2643.4 | res 2649.0 (ha 8 candles) | 27.46 | 0.0081% | A/compra@2649.0 (1t/0c) | zona_mapeada_setup_A |
| 2026-09-20 23:05 | SOL-USDT-SWAP | 110.92 | 113.44/110.66 | 111.12 | res 108.83 (ha 13 candles) | 1.2486 | 0.0100% | A/compra@108.83 (1t/4c) | zona_mapeada_setup_A |
| 2026-09-20 23:05 | XRP-USDT-SWAP | 1.4077 | 1.4387/1.4032 | 1.4101 | res 1.4169 (ha 9 candles) | 0.01574 | 0.0100% | — | invalidado_setup_A |
| 2026-09-20 23:05 | DOGE-USDT-SWAP | 0.08747 | 0.08978/0.08723 | 0.08727 | — | 0.00107 | 0.0100% | B/venda@0.08827 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-20 23:05 | ARB-USDT-SWAP | 0.21313 | 0.22066/0.21243 | 0.21764 | — | 0.00686 | -0.0062% | — | sem_zona |
| 2026-09-20 23:05 | WLD-USDT-SWAP | 0.43110 | 0.44550/0.43040 | 0.43520 | — | 0.01043 | 0.0046% | — | descartado_rr_baixo_setup_B |
| 2026-09-20 23:05 | SUI-USDT-SWAP | 0.92240 | 0.95440/0.91750 | 0.89680 | res 0.92020 (ha 8 candles) | 0.02714 | 0.0100% | A/compra@0.92020 (1t/0c) | zona_mapeada_setup_A |
| 2026-09-20 23:05 | UNI-USDT-SWAP | 8.5680 | 8.8920/8.5410 | 8.7240 | res 8.9880 (ha 3 candles) | 0.19186 | 0.0031% | — | sem_zona |
| 2026-09-20 23:05 | LINK-USDT-SWAP | 12.47 | 12.80/12.44 | 12.52 | res 12.61 (ha 8 candles) | 0.18057 | 0.0100% | — | invalidado_setup_A |
| 2026-09-21 00:05 | BTC-USDT-SWAP | 81297.5 | 81484.3/80923.8 | 81144.3 | res 81485.9 (ha 10 candles) | 470.33 | 0.0100% | — | sem_zona |
| 2026-09-21 00:05 | ETH-USDT-SWAP | 2660.9 | 2668.7/2642.9 | 2643.4 | res 2649.0 (ha 9 candles) | 28.49 | 0.0083% | — | descartado_rr_baixo_setup_A |
| 2026-09-21 00:05 | SOL-USDT-SWAP | 111.18 | 111.96/110.65 | 111.12 | res 108.83 (ha 14 candles) | 1.2886 | 0.0100% | A/compra@108.83 (1t/5c) | zona_mapeada_setup_A |
| 2026-09-21 00:05 | XRP-USDT-SWAP | 1.4153 | 1.4211/1.4045 | 1.4101 | res 1.4169 (ha 10 candles) | 0.01619 | 0.0100% | — | sem_zona |
| 2026-09-21 00:05 | DOGE-USDT-SWAP | 0.08805 | 0.08844/0.08717 | 0.08727 | — | 0.00111 | 0.0100% | B/venda@0.08827 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-21 00:05 | ARB-USDT-SWAP | 0.21735 | 0.21898/0.20904 | 0.21764 | — | 0.00725 | -0.0059% | — | sem_zona |
| 2026-09-21 00:05 | WLD-USDT-SWAP | 0.43920 | 0.44140/0.42640 | 0.43520 | — | 0.01101 | 0.0066% | — | sem_zona |
| 2026-09-21 00:05 | SUI-USDT-SWAP | 0.92570 | 0.94150/0.91340 | 0.89680 | res 0.92020 (ha 9 candles) | 0.02809 | 0.0100% | A/compra@0.92020 (2t/0c) | zona_mapeada_setup_A |
| 2026-09-21 00:05 | UNI-USDT-SWAP | 8.7140 | 8.7750/8.5470 | 8.7240 | res 8.9880 (ha 4 candles) | 0.19643 | 0.0058% | — | sem_zona |
| 2026-09-21 00:05 | LINK-USDT-SWAP | 12.58 | 12.64/12.45 | 12.52 | res 12.61 (ha 9 candles) | 0.18721 | 0.0100% | — | sem_zona |
| 2026-09-21 01:05 | BTC-USDT-SWAP | 81409.9 | 81563.8/81220.0 | 81409.9 | res 81485.9 (ha 11 candles) | 477.02 | 0.0100% | — | sem_zona |
| 2026-09-21 01:05 | ETH-USDT-SWAP | 2664.9 | 2673.0/2656.8 | 2664.9 | res 2709.9 (ha 3 candles) | 28.94 | 0.0080% | — | sem_zona |
| 2026-09-21 01:05 | SOL-USDT-SWAP | 111.51 | 111.88/111.12 | 111.51 | res 108.83 (ha 15 candles) | 1.2957 | 0.0100% | A/compra@108.83 (1t/6c) | zona_mapeada_setup_A |
| 2026-09-21 01:05 | XRP-USDT-SWAP | 1.4225 | 1.4257/1.4149 | 1.4225 | res 1.4169 (ha 11 candles) | 0.01637 | 0.0100% | — | sem_zona |
| 2026-09-21 01:05 | DOGE-USDT-SWAP | 0.08844 | 0.08876/0.08804 | 0.08844 | — | 0.00113 | 0.0100% | B/venda@0.08827 (2t/0c) | zona_mapeada_setup_B |
| 2026-09-21 01:05 | ARB-USDT-SWAP | 0.22127 | 0.22657/0.21694 | 0.22127 | — | 0.00762 | -0.0100% | — | sem_zona |
| 2026-09-21 01:05 | WLD-USDT-SWAP | 0.44170 | 0.44410/0.43870 | 0.44170 | — | 0.01091 | 0.0100% | — | sem_zona |
| 2026-09-21 01:05 | SUI-USDT-SWAP | 0.94930 | 0.95170/0.92460 | 0.94930 | res 0.92020 (ha 10 candles) | 0.02929 | 0.0100% | — | descartado_rr_baixo_setup_A |
| 2026-09-21 01:05 | UNI-USDT-SWAP | 8.7530 | 8.8200/8.6950 | 8.7530 | res 8.9880 (ha 5 candles) | 0.19343 | 0.0100% | — | sem_zona |
| 2026-09-21 01:05 | LINK-USDT-SWAP | 12.68 | 12.70/12.58 | 12.68 | res 12.61 (ha 10 candles) | 0.18893 | 0.0100% | — | sem_zona |
| 2026-09-21 02:05 | BTC-USDT-SWAP | 81367.2 | 81487.6/81205.9 | 81409.9 | res 82088.0 (ha 3 candles) | 469.93 | 0.0100% | — | sem_zona |
| 2026-09-21 02:05 | ETH-USDT-SWAP | 2662.7 | 2669.3/2652.0 | 2664.9 | res 2709.9 (ha 4 candles) | 29.06 | 0.0080% | — | sem_zona |
| 2026-09-21 02:05 | SOL-USDT-SWAP | 111.41 | 111.77/110.98 | 111.51 | res 113.44 (ha 3 candles) | 1.2993 | 0.0100% | A/compra@108.83 (1t/7c) | zona_mapeada_setup_A |
| 2026-09-21 02:06 | XRP-USDT-SWAP | 1.4186 | 1.4235/1.4130 | 1.4225 | res 1.4387 (ha 3 candles) | 0.01641 | 0.0100% | — | sem_zona |
| 2026-09-21 02:06 | DOGE-USDT-SWAP | 0.08829 | 0.08861/0.08777 | 0.08844 | — | 0.00115 | 0.0100% | — | zona_expirada_setup_B |
| 2026-09-21 02:06 | ARB-USDT-SWAP | 0.21527 | 0.22198/0.21498 | 0.22127 | — | 0.00718 | -0.0109% | — | sem_zona |
| 2026-09-21 02:06 | WLD-USDT-SWAP | 0.44070 | 0.44290/0.43550 | 0.44170 | — | 0.01102 | 0.0100% | — | sem_zona |
| 2026-09-21 02:06 | SUI-USDT-SWAP | 0.93320 | 0.95340/0.93230 | 0.94930 | res 0.95440 (ha 3 candles) | 0.02999 | 0.0100% | — | sem_zona |
| 2026-09-21 02:06 | UNI-USDT-SWAP | 8.7570 | 8.8500/8.6680 | 8.7530 | res 8.9880 (ha 6 candles) | 0.19600 | 0.0100% | — | sem_zona |
| 2026-09-21 02:06 | LINK-USDT-SWAP | 12.63 | 12.71/12.57 | 12.68 | res 12.80 (ha 3 candles) | 0.18921 | 0.0100% | — | sem_zona |
| 2026-09-21 03:05 | BTC-USDT-SWAP | 81529.5 | 81767.2/81275.9 | 81409.9 | res 82088.0 (ha 4 candles) | 482.38 | 0.0100% | — | sem_zona |
| 2026-09-21 03:05 | ETH-USDT-SWAP | 2664.2 | 2675.0/2657.5 | 2664.9 | res 2709.9 (ha 5 candles) | 28.13 | 0.0074% | — | sem_zona |
| 2026-09-21 03:05 | SOL-USDT-SWAP | 111.72 | 112.19/111.23 | 111.51 | res 113.44 (ha 4 candles) | 1.3114 | 0.0100% | — | zona_expirada_setup_A |
| 2026-09-21 03:05 | XRP-USDT-SWAP | 1.4301 | 1.4380/1.4152 | 1.4225 | res 1.4387 (ha 4 candles) | 0.01716 | 0.0100% | — | sem_zona |
| 2026-09-21 03:05 | DOGE-USDT-SWAP | 0.08834 | 0.08909/0.08802 | 0.08844 | — | 0.00117 | 0.0100% | B/compra@0.08845 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-21 03:05 | ARB-USDT-SWAP | 0.21475 | 0.21617/0.21311 | 0.22127 | — | 0.00678 | -0.0104% | — | sem_zona |
| 2026-09-21 03:05 | WLD-USDT-SWAP | 0.44370 | 0.44710/0.43780 | 0.44170 | — | 0.01071 | 0.0100% | — | sem_zona |
| 2026-09-21 03:05 | SUI-USDT-SWAP | 0.93750 | 0.95070/0.92780 | 0.94930 | res 0.95440 (ha 4 candles) | 0.02986 | 0.0100% | — | sem_zona |
| 2026-09-21 03:05 | UNI-USDT-SWAP | 8.6380 | 8.8050/8.5800 | 8.7530 | res 8.9880 (ha 7 candles) | 0.20079 | 0.0100% | — | sem_zona |
| 2026-09-21 03:05 | LINK-USDT-SWAP | 12.54 | 12.65/12.54 | 12.68 | res 12.80 (ha 4 candles) | 0.18007 | 0.0100% | — | sem_zona |
| 2026-09-21 04:05 | BTC-USDT-SWAP | 81611.7 | 81862.5/81358.0 | 81409.9 | res 82088.0 (ha 5 candles) | 466.63 | 0.0100% | — | sem_zona |
| 2026-09-21 04:05 | ETH-USDT-SWAP | 2662.0 | 2677.8/2653.0 | 2664.9 | res 2709.9 (ha 6 candles) | 26.85 | 0.0067% | — | sem_zona |
| 2026-09-21 04:05 | SOL-USDT-SWAP | 112.15 | 112.56/111.47 | 111.51 | res 113.44 (ha 5 candles) | 1.2321 | 0.0100% | — | sem_zona |
| 2026-09-21 04:05 | XRP-USDT-SWAP | 1.4361 | 1.4418/1.4245 | 1.4225 | res 1.4387 (ha 5 candles) | 0.01624 | 0.0100% | — | sem_zona |
| 2026-09-21 04:05 | DOGE-USDT-SWAP | 0.08903 | 0.08943/0.08828 | 0.08844 | — | 0.00111 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-09-21 04:05 | ARB-USDT-SWAP | 0.21428 | 0.21641/0.21272 | 0.22127 | — | 0.00631 | -0.0080% | — | sem_zona |
| 2026-09-21 04:05 | WLD-USDT-SWAP | 0.45220 | 0.45400/0.44140 | 0.44170 | — | 0.00989 | 0.0100% | — | sem_zona |
| 2026-09-21 04:05 | SUI-USDT-SWAP | 0.96120 | 0.97770/0.93530 | 0.94930 | res 0.95440 (ha 5 candles) | 0.02761 | 0.0100% | A/compra@0.95440 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-21 04:05 | UNI-USDT-SWAP | 8.6320 | 8.6830/8.5810 | 8.7530 | res 8.9880 (ha 8 candles) | 0.18679 | 0.0095% | — | sem_zona |
| 2026-09-21 04:05 | LINK-USDT-SWAP | 12.54 | 12.61/12.47 | 12.68 | res 12.80 (ha 5 candles) | 0.17136 | 0.0100% | — | sem_zona |
| 2026-09-21 05:05 | BTC-USDT-SWAP | 81700.0 | 81700.0/81432.2 | 81700.0 | res 82088.0 (ha 6 candles) | 457.06 | 0.0100% | — | sem_zona |
| 2026-09-21 05:05 | ETH-USDT-SWAP | 2660.8 | 2664.7/2645.0 | 2660.8 | res 2709.9 (ha 7 candles) | 25.90 | 0.0082% | — | sem_zona |
| 2026-09-21 05:05 | SOL-USDT-SWAP | 112.08 | 112.35/111.34 | 112.08 | res 113.44 (ha 6 candles) | 1.2286 | 0.0100% | — | sem_zona |
| 2026-09-21 05:05 | XRP-USDT-SWAP | 1.4384 | 1.4465/1.4296 | 1.4384 | res 1.4387 (ha 6 candles) | 0.01633 | 0.0100% | — | sem_zona |
| 2026-09-21 05:05 | DOGE-USDT-SWAP | 0.08972 | 0.08975/0.08877 | 0.08972 | — | 0.00110 | 0.0100% | — | sem_zona |
| 2026-09-21 05:05 | ARB-USDT-SWAP | 0.21333 | 0.21476/0.21139 | 0.21333 | — | 0.00615 | -0.0069% | — | sem_zona |
| 2026-09-21 05:05 | WLD-USDT-SWAP | 0.44800 | 0.45360/0.44340 | 0.44800 | res 0.44600 (ha 7 candles) | 0.00929 | 0.0100% | A/compra@0.44600 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-21 05:05 | SUI-USDT-SWAP | 0.96620 | 0.96880/0.94620 | 0.96620 | res 0.95440 (ha 6 candles) | 0.02669 | 0.0100% | — | descartado_rr_baixo_setup_A |
| 2026-09-21 05:05 | UNI-USDT-SWAP | 8.6280 | 8.6440/8.4900 | 8.6280 | res 8.9880 (ha 9 candles) | 0.18971 | 0.0072% | — | sem_zona |
| 2026-09-21 05:05 | LINK-USDT-SWAP | 12.56 | 12.58/12.47 | 12.56 | res 12.80 (ha 6 candles) | 0.16200 | 0.0100% | — | sem_zona |
| 2026-09-21 06:05 | BTC-USDT-SWAP | 83718.0 | 84234.1/81699.9 | 81700.0 | res 82088.0 (ha 7 candles) | 616.04 | 0.0100% | A/compra@82088.0 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-21 06:05 | ETH-USDT-SWAP | 2695.0 | 2714.0/2659.9 | 2660.8 | res 2709.9 (ha 8 candles) | 28.40 | 0.0084% | — | sem_zona |
| 2026-09-21 06:05 | SOL-USDT-SWAP | 115.26 | 116.38/112.03 | 112.08 | res 113.44 (ha 7 candles) | 1.4571 | 0.0100% | A/compra@113.44 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-21 06:05 | XRP-USDT-SWAP | 1.4762 | 1.4875/1.4378 | 1.4384 | res 1.4387 (ha 7 candles) | 0.01886 | 0.0100% | A/compra@1.4387 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-21 06:05 | DOGE-USDT-SWAP | 0.09186 | 0.09263/0.08965 | 0.08972 | — | 0.00125 | 0.0100% | B/venda@0.09156 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-21 06:05 | ARB-USDT-SWAP | 0.21703 | 0.21808/0.21236 | 0.21333 | — | 0.00615 | -0.0104% | — | sem_zona |
| 2026-09-21 06:05 | WLD-USDT-SWAP | 0.45260 | 0.45450/0.44480 | 0.44800 | res 0.44600 (ha 8 candles) | 0.00919 | 0.0097% | — | descartado_rr_baixo_setup_A |
| 2026-09-21 06:05 | SUI-USDT-SWAP | 0.99450 | 0.99970/0.95830 | 0.96620 | res 0.95440 (ha 7 candles) | 0.02766 | 0.0100% | — | sem_zona |
| 2026-09-21 06:05 | UNI-USDT-SWAP | 8.8220 | 8.8750/8.6200 | 8.6280 | res 8.9880 (ha 10 candles) | 0.19543 | 0.0074% | — | sem_zona |
| 2026-09-21 06:05 | LINK-USDT-SWAP | 12.82 | 12.86/12.55 | 12.56 | res 12.80 (ha 7 candles) | 0.17379 | 0.0100% | A/compra@12.80 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-21 07:05 | BTC-USDT-SWAP | 84625.9 | 85332.9/83657.8 | 81700.0 | res 82088.0 (ha 8 candles) | 716.39 | 0.0100% | A/compra@82088.0 (0t/1c) | zona_mapeada_setup_A |
| 2026-09-21 07:05 | ETH-USDT-SWAP | 2719.6 | 2748.4/2690.8 | 2660.8 | res 2709.9 (ha 9 candles) | 31.56 | 0.0084% | A/compra@2709.9 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-21 07:05 | SOL-USDT-SWAP | 115.87 | 116.83/114.89 | 112.08 | res 113.44 (ha 8 candles) | 1.4871 | 0.0100% | A/compra@113.44 (0t/1c) | zona_mapeada_setup_A |
| 2026-09-21 07:05 | XRP-USDT-SWAP | 1.4746 | 1.4869/1.4699 | 1.4384 | res 1.4387 (ha 8 candles) | 0.01911 | 0.0100% | A/compra@1.4387 (0t/1c) | zona_mapeada_setup_A |
| 2026-09-21 07:05 | DOGE-USDT-SWAP | 0.09211 | 0.09484/0.09115 | 0.08972 | — | 0.00144 | 0.0100% | — | invalidado_setup_B |
| 2026-09-21 07:05 | ARB-USDT-SWAP | 0.21824 | 0.22227/0.21644 | 0.21333 | — | 0.00632 | -0.0137% | — | sem_zona |
| 2026-09-21 07:05 | WLD-USDT-SWAP | 0.44150 | 0.45770/0.43990 | 0.44800 | res 0.44600 (ha 9 candles) | 0.00988 | 0.0021% | — | sem_zona |
| 2026-09-21 07:05 | SUI-USDT-SWAP | 0.98400 | 1.0212/0.98000 | 0.96620 | res 0.95440 (ha 8 candles) | 0.02968 | 0.0100% | — | sem_zona |
| 2026-09-21 07:05 | UNI-USDT-SWAP | 8.9730 | 9.2950/8.7540 | 8.6280 | res 8.9880 (ha 11 candles) | 0.22729 | 0.0053% | — | sem_zona |
| 2026-09-21 07:05 | LINK-USDT-SWAP | 12.94 | 13.13/12.78 | 12.56 | res 12.80 (ha 8 candles) | 0.18714 | 0.0100% | A/compra@12.80 (1t/0c) | zona_mapeada_setup_A |
| 2026-09-21 08:05 | BTC-USDT-SWAP | 84404.4 | 84794.1/84102.6 | 81700.0 | res 82088.0 (ha 9 candles) | 754.95 | 0.0100% | A/compra@82088.0 (0t/2c) | zona_mapeada_setup_A |
| 2026-09-21 08:05 | ETH-USDT-SWAP | 2714.6 | 2725.7/2706.0 | 2660.8 | res 2709.9 (ha 10 candles) | 32.00 | 0.0089% | A/compra@2709.9 (1t/0c) | zona_mapeada_setup_A |
| 2026-09-21 08:05 | SOL-USDT-SWAP | 115.97 | 116.08/115.42 | 112.08 | res 113.44 (ha 9 candles) | 1.4929 | 0.0100% | A/compra@113.44 (0t/2c) | zona_mapeada_setup_A |
| 2026-09-21 08:05 | XRP-USDT-SWAP | 1.4906 | 1.4946/1.4690 | 1.4384 | res 1.4387 (ha 9 candles) | 0.02038 | 0.0100% | A/compra@1.4387 (0t/2c) | zona_mapeada_setup_A |
| 2026-09-21 08:05 | DOGE-USDT-SWAP | 0.09291 | 0.09291/0.09171 | 0.08972 | — | 0.00149 | 0.0100% | — | sem_zona |
| 2026-09-21 08:05 | ARB-USDT-SWAP | 0.23197 | 0.23358/0.21766 | 0.21333 | — | 0.00727 | -0.0128% | B/venda@0.23014 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-21 08:05 | WLD-USDT-SWAP | 0.44890 | 0.44920/0.44030 | 0.44800 | res 0.44600 (ha 10 candles) | 0.01009 | -0.0005% | — | sem_zona |
| 2026-09-21 08:05 | SUI-USDT-SWAP | 1.0019 | 1.0053/0.97650 | 0.96620 | res 0.95440 (ha 9 candles) | 0.03051 | 0.0100% | — | sem_zona |
| 2026-09-21 08:05 | UNI-USDT-SWAP | 9.0060 | 9.0350/8.8610 | 8.6280 | res 8.9880 (ha 12 candles) | 0.23121 | 0.0015% | A/compra@8.9880 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-21 08:05 | LINK-USDT-SWAP | 13.04 | 13.05/12.91 | 12.56 | res 12.80 (ha 9 candles) | 0.19171 | 0.0100% | A/compra@12.80 (1t/1c) | zona_mapeada_setup_A |
| 2026-09-21 09:05 | BTC-USDT-SWAP | 84848.7 | 84881.6/84354.9 | 84848.7 | res 82088.0 (ha 10 candles) | 755.99 | 0.0100% | A/compra@82088.0 (0t/3c) | zona_mapeada_setup_A |
| 2026-09-21 09:05 | ETH-USDT-SWAP | 2724.0 | 2729.9/2712.0 | 2724.0 | res 2709.9 (ha 11 candles) | 31.29 | 0.0060% | — | descartado_rr_baixo_setup_A |
| 2026-09-21 09:05 | SOL-USDT-SWAP | 116.76 | 117.15/115.78 | 116.76 | res 113.44 (ha 10 candles) | 1.5136 | 0.0100% | A/compra@113.44 (0t/3c) | zona_mapeada_setup_A |
| 2026-09-21 09:05 | XRP-USDT-SWAP | 1.4856 | 1.4979/1.4840 | 1.4856 | res 1.4387 (ha 10 candles) | 0.02030 | 0.0100% | A/compra@1.4387 (0t/3c) | zona_mapeada_setup_A |
| 2026-09-21 09:05 | DOGE-USDT-SWAP | 0.09332 | 0.09375/0.09274 | 0.09332 | — | 0.00147 | 0.0100% | — | sem_zona |
| 2026-09-21 09:05 | ARB-USDT-SWAP | 0.22796 | 0.23647/0.22713 | 0.22796 | — | 0.00729 | -0.0121% | — | descartado_rr_baixo_setup_B |
| 2026-09-21 09:05 | WLD-USDT-SWAP | 0.44870 | 0.45340/0.44780 | 0.44870 | res 0.44600 (ha 11 candles) | 0.00979 | -0.0021% | — | sem_zona |
| 2026-09-21 09:05 | SUI-USDT-SWAP | 1.0150 | 1.0344/0.99890 | 1.0150 | res 0.95440 (ha 10 candles) | 0.03150 | 0.0100% | — | sem_zona |
| 2026-09-21 09:05 | UNI-USDT-SWAP | 8.9230 | 9.0440/8.8940 | 8.9230 | res 8.9880 (ha 13 candles) | 0.22493 | 0.0006% | — | invalidado_setup_A |
| 2026-09-21 09:05 | LINK-USDT-SWAP | 13.04 | 13.14/13.01 | 13.04 | res 12.80 (ha 10 candles) | 0.18779 | 0.0100% | A/compra@12.80 (1t/2c) | zona_mapeada_setup_A |
| 2026-09-21 10:05 | BTC-USDT-SWAP | 85273.0 | 85479.8/84771.5 | 84848.7 | res 82088.0 (ha 11 candles) | 768.09 | 0.0080% | A/compra@82088.0 (0t/4c) | zona_mapeada_setup_A |
| 2026-09-21 10:05 | ETH-USDT-SWAP | 2733.7 | 2739.6/2717.0 | 2724.0 | res 2748.4 (ha 3 candles) | 31.18 | 0.0035% | — | sem_zona |
| 2026-09-21 10:05 | SOL-USDT-SWAP | 116.74 | 117.08/116.12 | 116.76 | res 113.44 (ha 11 candles) | 1.4779 | 0.0100% | A/compra@113.44 (0t/4c) | zona_mapeada_setup_A |
| 2026-09-21 10:05 | XRP-USDT-SWAP | 1.4872 | 1.4960/1.4834 | 1.4856 | res 1.4387 (ha 11 candles) | 0.02009 | 0.0100% | A/compra@1.4387 (0t/4c) | zona_mapeada_setup_A |
| 2026-09-21 10:05 | DOGE-USDT-SWAP | 0.09344 | 0.09393/0.09292 | 0.09332 | — | 0.00147 | 0.0100% | — | sem_zona |
| 2026-09-21 10:05 | ARB-USDT-SWAP | 0.24454 | 0.24673/0.22592 | 0.22796 | — | 0.00818 | -0.0056% | — | sem_zona |
| 2026-09-21 10:05 | WLD-USDT-SWAP | 0.45200 | 0.45320/0.44680 | 0.44870 | res 0.45770 (ha 3 candles) | 0.00986 | -0.0021% | — | sem_zona |
| 2026-09-21 10:05 | SUI-USDT-SWAP | 1.0368 | 1.0438/1.0138 | 1.0150 | res 0.95440 (ha 11 candles) | 0.03192 | 0.0100% | — | sem_zona |
| 2026-09-21 10:05 | UNI-USDT-SWAP | 9.0350 | 9.0390/8.7520 | 8.9230 | res 9.2950 (ha 3 candles) | 0.22814 | 0.0007% | — | sem_zona |
| 2026-09-21 10:05 | LINK-USDT-SWAP | 13.12 | 13.14/13.01 | 13.04 | res 12.80 (ha 11 candles) | 0.18586 | 0.0100% | A/compra@12.80 (1t/3c) | zona_mapeada_setup_A |
| 2026-09-21 11:05 | BTC-USDT-SWAP | 85424.5 | 85830.9/84733.4 | 84848.7 | res 82088.0 (ha 12 candles) | 831.56 | 0.0059% | A/compra@82088.0 (0t/5c) | zona_mapeada_setup_A |
| 2026-09-21 11:05 | ETH-USDT-SWAP | 2731.1 | 2745.0/2716.3 | 2724.0 | res 2748.4 (ha 4 candles) | 32.00 | 0.0018% | — | sem_zona |
| 2026-09-21 11:05 | SOL-USDT-SWAP | 117.98 | 118.35/116.60 | 116.76 | res 113.44 (ha 12 candles) | 1.5371 | 0.0076% | A/compra@113.44 (0t/5c) | zona_mapeada_setup_A |
| 2026-09-21 11:05 | XRP-USDT-SWAP | 1.4898 | 1.4977/1.4713 | 1.4856 | res 1.4387 (ha 12 candles) | 0.02135 | 0.0100% | A/compra@1.4387 (0t/5c) | zona_mapeada_setup_A |
| 2026-09-21 11:05 | DOGE-USDT-SWAP | 0.09325 | 0.09438/0.09241 | 0.09332 | — | 0.00158 | 0.0100% | — | sem_zona |
| 2026-09-21 11:05 | ARB-USDT-SWAP | 0.23863 | 0.24769/0.23630 | 0.22796 | — | 0.00860 | -0.0012% | — | sem_zona |
| 2026-09-21 11:05 | WLD-USDT-SWAP | 0.44710 | 0.45540/0.44240 | 0.44870 | res 0.45770 (ha 4 candles) | 0.01053 | -0.0005% | — | sem_zona |
| 2026-09-21 11:05 | SUI-USDT-SWAP | 1.0373 | 1.0567/1.0284 | 1.0150 | res 0.95440 (ha 12 candles) | 0.03286 | 0.0100% | — | sem_zona |
| 2026-09-21 11:05 | UNI-USDT-SWAP | 8.8800 | 9.0550/8.8340 | 8.9230 | res 9.2950 (ha 4 candles) | 0.23136 | 0.0012% | — | sem_zona |
| 2026-09-21 11:05 | LINK-USDT-SWAP | 13.03 | 13.17/12.90 | 13.04 | res 12.80 (ha 12 candles) | 0.19914 | 0.0100% | A/compra@12.80 (1t/4c) | zona_mapeada_setup_A |
| 2026-09-21 12:05 | BTC-USDT-SWAP | 85800.0 | 86095.0/85000.2 | 84848.7 | res 82088.0 (ha 13 candles) | 860.24 | 0.0035% | A/compra@82088.0 (0t/6c) | zona_mapeada_setup_A |
| 2026-09-21 12:05 | ETH-USDT-SWAP | 2735.2 | 2756.8/2710.0 | 2724.0 | res 2748.4 (ha 5 candles) | 30.51 | 0.0017% | — | sem_zona |
| 2026-09-21 12:05 | SOL-USDT-SWAP | 117.97 | 118.89/117.29 | 116.76 | res 113.44 (ha 13 candles) | 1.5236 | 0.0037% | A/compra@113.44 (0t/6c) | zona_mapeada_setup_A |
| 2026-09-21 12:05 | XRP-USDT-SWAP | 1.4969 | 1.5069/1.4747 | 1.4856 | res 1.4387 (ha 13 candles) | 0.02199 | 0.0100% | A/compra@1.4387 (0t/6c) | zona_mapeada_setup_A |
| 2026-09-21 12:05 | DOGE-USDT-SWAP | 0.09493 | 0.09524/0.09215 | 0.09332 | — | 0.00168 | 0.0100% | B/venda@0.09529 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-21 12:05 | ARB-USDT-SWAP | 0.23513 | 0.23947/0.23218 | 0.22796 | — | 0.00866 | 0.0036% | — | sem_zona |
| 2026-09-21 12:05 | WLD-USDT-SWAP | 0.44190 | 0.44730/0.43610 | 0.44870 | res 0.45770 (ha 5 candles) | 0.01054 | -0.0014% | — | sem_zona |
| 2026-09-21 12:05 | SUI-USDT-SWAP | 1.0331 | 1.0564/1.0178 | 1.0150 | res 0.95440 (ha 13 candles) | 0.03178 | 0.0100% | — | sem_zona |
| 2026-09-21 12:05 | UNI-USDT-SWAP | 8.8330 | 8.9640/8.7000 | 8.9230 | res 9.2950 (ha 5 candles) | 0.23279 | -0.0010% | — | sem_zona |
| 2026-09-21 12:05 | LINK-USDT-SWAP | 12.99 | 13.06/12.86 | 13.04 | res 12.80 (ha 13 candles) | 0.19357 | 0.0090% | A/compra@12.80 (1t/5c) | zona_mapeada_setup_A |
| 2026-09-21 13:05 | BTC-USDT-SWAP | 85887.6 | 86319.6/85753.2 | 85887.6 | res 82088.0 (ha 14 candles) | 810.29 | 0.0019% | A/compra@82088.0 (0t/7c) | zona_mapeada_setup_A |
| 2026-09-21 13:05 | ETH-USDT-SWAP | 2754.0 | 2764.8/2727.0 | 2754.0 | res 2748.4 (ha 6 candles) | 29.02 | 0.0011% | A/compra@2748.4 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-21 13:05 | SOL-USDT-SWAP | 117.87 | 119.10/117.29 | 117.87 | res 113.44 (ha 14 candles) | 1.4543 | 0.0022% | A/compra@113.44 (0t/7c) | zona_mapeada_setup_A |
| 2026-09-21 13:05 | XRP-USDT-SWAP | 1.4948 | 1.5089/1.4839 | 1.4948 | res 1.4387 (ha 14 candles) | 0.02124 | 0.0100% | A/compra@1.4387 (0t/7c) | zona_mapeada_setup_A |
| 2026-09-21 13:05 | DOGE-USDT-SWAP | 0.09729 | 0.09817/0.09480 | 0.09729 | — | 0.00174 | 0.0100% | — | invalidado_setup_B |
| 2026-09-21 13:05 | ARB-USDT-SWAP | 0.23115 | 0.23822/0.22731 | 0.23115 | — | 0.00885 | 0.0019% | — | sem_zona |
| 2026-09-21 13:05 | WLD-USDT-SWAP | 0.44080 | 0.44600/0.43370 | 0.44080 | res 0.45770 (ha 6 candles) | 0.01034 | -0.0009% | — | sem_zona |
| 2026-09-21 13:05 | SUI-USDT-SWAP | 1.0181 | 1.0427/1.0050 | 1.0181 | res 0.95440 (ha 14 candles) | 0.03184 | 0.0100% | A/compra@0.95440 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-21 13:05 | UNI-USDT-SWAP | 8.8310 | 8.9930/8.7060 | 8.8310 | res 9.2950 (ha 6 candles) | 0.22821 | -0.0035% | — | sem_zona |
| 2026-09-21 13:05 | LINK-USDT-SWAP | 13.01 | 13.10/12.88 | 13.01 | res 12.80 (ha 14 candles) | 0.18364 | 0.0018% | A/compra@12.80 (1t/6c) | zona_mapeada_setup_A |
| 2026-09-21 14:05 | BTC-USDT-SWAP | 85916.6 | 86077.1/85551.9 | 85887.6 | res 82088.0 (ha 15 candles) | 807.77 | 0.0012% | — | zona_expirada_setup_A |
| 2026-09-21 14:05 | ETH-USDT-SWAP | 2753.3 | 2768.6/2741.4 | 2754.0 | res 2748.4 (ha 7 candles) | 29.12 | 0.0013% | A/compra@2748.4 (1t/0c) | zona_mapeada_setup_A |
| 2026-09-21 14:05 | SOL-USDT-SWAP | 117.45 | 118.27/116.70 | 117.87 | res 113.44 (ha 15 candles) | 1.4729 | 0.0006% | — | zona_expirada_setup_A |
| 2026-09-21 14:05 | XRP-USDT-SWAP | 1.4884 | 1.5037/1.4801 | 1.4948 | res 1.4387 (ha 15 candles) | 0.02174 | 0.0100% | — | zona_expirada_setup_A |
| 2026-09-21 14:05 | DOGE-USDT-SWAP | 0.09662 | 0.09790/0.09516 | 0.09729 | — | 0.00184 | 0.0100% | — | sem_zona |
| 2026-09-21 14:05 | ARB-USDT-SWAP | 0.22640 | 0.23546/0.22430 | 0.23115 | — | 0.00894 | -0.0001% | — | sem_zona |
| 2026-09-21 14:05 | WLD-USDT-SWAP | 0.43860 | 0.44470/0.43740 | 0.44080 | res 0.45540 (ha 3 candles) | 0.00979 | -0.0022% | — | sem_zona |
| 2026-09-21 14:05 | SUI-USDT-SWAP | 1.0141 | 1.0435/1.0138 | 1.0181 | res 1.0567 (ha 3 candles) | 0.03195 | 0.0100% | A/compra@0.95440 (0t/1c) | zona_mapeada_setup_A |
| 2026-09-21 14:05 | UNI-USDT-SWAP | 8.9070 | 8.9930/8.8210 | 8.8310 | res 9.0550 (ha 3 candles) | 0.22421 | -0.0015% | — | sem_zona |
| 2026-09-21 14:05 | LINK-USDT-SWAP | 12.98 | 13.08/12.89 | 13.01 | res 13.17 (ha 3 candles) | 0.18321 | -0.0038% | A/compra@12.80 (1t/7c) | zona_mapeada_setup_A |
| 2026-09-21 15:05 | BTC-USDT-SWAP | 85858.5 | 86073.4/85638.0 | 85887.6 | res 82088.0 (ha 16 candles) | 814.31 | 0.0019% | — | sem_zona |
| 2026-09-21 15:05 | ETH-USDT-SWAP | 2741.8 | 2756.8/2733.8 | 2754.0 | res 2748.4 (ha 8 candles) | 29.61 | 0.0013% | A/compra@2748.4 (2t/0c) | zona_mapeada_setup_A |
| 2026-09-21 15:05 | SOL-USDT-SWAP | 117.15 | 117.86/116.61 | 117.87 | res 113.44 (ha 16 candles) | 1.5079 | 0.0026% | — | sem_zona |
| 2026-09-21 15:05 | XRP-USDT-SWAP | 1.4951 | 1.4994/1.4870 | 1.4948 | res 1.4387 (ha 16 candles) | 0.02185 | 0.0100% | — | sem_zona |
| 2026-09-21 15:05 | DOGE-USDT-SWAP | 0.09737 | 0.09906/0.09646 | 0.09729 | — | 0.00198 | 0.0100% | — | sem_zona |
| 2026-09-21 15:05 | ARB-USDT-SWAP | 0.22493 | 0.22830/0.22317 | 0.23115 | — | 0.00862 | 0.0018% | — | sem_zona |
| 2026-09-21 15:05 | WLD-USDT-SWAP | 0.43070 | 0.43980/0.42730 | 0.44080 | res 0.45540 (ha 4 candles) | 0.01030 | -0.0022% | — | sem_zona |
| 2026-09-21 15:05 | SUI-USDT-SWAP | 0.99540 | 1.0237/0.99040 | 1.0181 | res 1.0567 (ha 4 candles) | 0.03239 | 0.0100% | A/compra@0.95440 (0t/2c) | zona_mapeada_setup_A |
| 2026-09-21 15:05 | UNI-USDT-SWAP | 8.7760 | 8.9600/8.7450 | 8.8310 | res 9.0550 (ha 4 candles) | 0.23064 | -0.0010% | — | sem_zona |
| 2026-09-21 15:05 | LINK-USDT-SWAP | 12.81 | 13.00/12.74 | 13.01 | res 13.17 (ha 4 candles) | 0.19329 | -0.0033% | A/compra@12.80 (2t/0c) | zona_mapeada_setup_A |
| 2026-09-21 16:05 | BTC-USDT-SWAP | 86035.2 | 86048.1/85757.8 | 85887.6 | res 86319.6 (ha 3 candles) | 814.93 | 0.0039% | — | sem_zona |
| 2026-09-21 16:05 | ETH-USDT-SWAP | 2756.8 | 2756.8/2736.6 | 2754.0 | res 2748.4 (ha 9 candles) | 29.81 | 0.0018% | — | descartado_rr_baixo_setup_A |
| 2026-09-21 16:05 | SOL-USDT-SWAP | 117.68 | 117.83/116.81 | 117.87 | res 119.10 (ha 3 candles) | 1.5243 | 0.0059% | — | sem_zona |
| 2026-09-21 16:05 | XRP-USDT-SWAP | 1.5091 | 1.5147/1.4914 | 1.4948 | res 1.4387 (ha 17 candles) | 0.02276 | 0.0100% | — | sem_zona |
| 2026-09-21 16:05 | DOGE-USDT-SWAP | 0.09966 | 0.09999/0.09692 | 0.09729 | — | 0.00214 | 0.0100% | — | sem_zona |
| 2026-09-21 16:05 | ARB-USDT-SWAP | 0.22628 | 0.22744/0.22381 | 0.23115 | — | 0.00837 | 0.0028% | — | sem_zona |
| 2026-09-21 16:05 | WLD-USDT-SWAP | 0.43440 | 0.43570/0.42890 | 0.44080 | res 0.45540 (ha 5 candles) | 0.01026 | -0.0022% | — | sem_zona |
| 2026-09-21 16:05 | SUI-USDT-SWAP | 1.0123 | 1.0124/0.99460 | 1.0181 | res 1.0567 (ha 5 candles) | 0.03216 | 0.0100% | A/compra@0.95440 (0t/3c) | zona_mapeada_setup_A |
| 2026-09-21 16:05 | UNI-USDT-SWAP | 8.7420 | 8.8640/8.6640 | 8.8310 | res 9.0550 (ha 5 candles) | 0.23193 | -0.0026% | — | sem_zona |
| 2026-09-21 16:05 | LINK-USDT-SWAP | 12.95 | 12.96/12.78 | 13.01 | res 13.17 (ha 5 candles) | 0.19650 | 0.0000% | — | descartado_rr_baixo_setup_A |
| 2026-09-21 17:05 | BTC-USDT-SWAP | 86451.6 | 86887.9/85939.3 | 86451.6 | res 86319.6 (ha 4 candles) | 847.59 | 0.0037% | A/compra@86319.6 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-21 17:05 | ETH-USDT-SWAP | 2760.4 | 2775.0/2753.7 | 2760.4 | res 2748.4 (ha 10 candles) | 30.09 | 0.0012% | — | sem_zona |
| 2026-09-21 17:05 | SOL-USDT-SWAP | 118.31 | 118.43/117.22 | 118.31 | res 119.10 (ha 4 candles) | 1.5421 | 0.0091% | — | sem_zona |
| 2026-09-21 17:05 | XRP-USDT-SWAP | 1.5071 | 1.5096/1.4966 | 1.5071 | res 1.4387 (ha 18 candles) | 0.02206 | 0.0100% | — | sem_zona |
| 2026-09-21 17:05 | DOGE-USDT-SWAP | 0.09853 | 0.10007/0.09751 | 0.09853 | — | 0.00224 | 0.0100% | — | sem_zona |
| 2026-09-21 17:05 | ARB-USDT-SWAP | 0.22774 | 0.22948/0.22553 | 0.22774 | — | 0.00844 | -0.0036% | B/venda@0.23014 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-21 17:05 | WLD-USDT-SWAP | 0.43920 | 0.43950/0.43220 | 0.43920 | res 0.45540 (ha 6 candles) | 0.01011 | -0.0034% | — | sem_zona |
| 2026-09-21 17:05 | SUI-USDT-SWAP | 1.0364 | 1.0378/1.0064 | 1.0364 | res 1.0567 (ha 6 candles) | 0.03276 | 0.0100% | A/compra@0.95440 (0t/4c) | zona_mapeada_setup_A |
| 2026-09-21 17:05 | UNI-USDT-SWAP | 8.8130 | 8.8260/8.7170 | 8.8130 | res 9.0550 (ha 6 candles) | 0.22364 | 0.0003% | — | sem_zona |
| 2026-09-21 17:05 | LINK-USDT-SWAP | 13.03 | 13.06/12.90 | 13.03 | res 13.17 (ha 6 candles) | 0.19936 | 0.0054% | — | sem_zona |
| 2026-09-21 18:05 | BTC-USDT-SWAP | 86965.2 | 87374.3/86451.7 | 86451.6 | res 86319.6 (ha 5 candles) | 877.46 | 0.0056% | A/compra@86319.6 (1t/0c) | zona_mapeada_setup_A |
| 2026-09-21 18:05 | ETH-USDT-SWAP | 2782.9 | 2807.0/2760.4 | 2760.4 | res 2748.4 (ha 11 candles) | 31.64 | 0.0022% | — | sem_zona |
| 2026-09-21 18:05 | SOL-USDT-SWAP | 119.16 | 119.47/118.15 | 118.31 | res 119.10 (ha 5 candles) | 1.5586 | 0.0100% | A/compra@119.10 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-21 18:05 | XRP-USDT-SWAP | 1.5330 | 1.5373/1.5029 | 1.5071 | res 1.4387 (ha 19 candles) | 0.02329 | 0.0100% | — | sem_zona |
| 2026-09-21 18:05 | DOGE-USDT-SWAP | 0.10018 | 0.10119/0.09840 | 0.09853 | — | 0.00236 | 0.0100% | — | sem_zona |
| 2026-09-21 18:05 | ARB-USDT-SWAP | 0.22213 | 0.22789/0.22115 | 0.22774 | — | 0.00866 | -0.0065% | B/venda@0.23014 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-21 18:05 | WLD-USDT-SWAP | 0.46340 | 0.46650/0.43900 | 0.43920 | res 0.45540 (ha 7 candles) | 0.01118 | 0.0035% | A/compra@0.45540 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-21 18:05 | SUI-USDT-SWAP | 1.0199 | 1.0382/1.0162 | 1.0364 | res 1.0567 (ha 7 candles) | 0.03131 | 0.0100% | A/compra@0.95440 (0t/5c) | zona_mapeada_setup_A |
| 2026-09-21 18:05 | UNI-USDT-SWAP | 8.8200 | 8.8760/8.7250 | 8.8130 | res 9.0550 (ha 7 candles) | 0.22714 | 0.0011% | — | sem_zona |
| 2026-09-21 18:05 | LINK-USDT-SWAP | 13.16 | 13.32/13.02 | 13.03 | res 13.17 (ha 7 candles) | 0.21021 | 0.0100% | — | sem_zona |
| 2026-09-21 19:05 | BTC-USDT-SWAP | 86551.1 | 86965.2/86518.8 | 86451.6 | res 86319.6 (ha 6 candles) | 890.22 | 0.0100% | A/compra@86319.6 (2t/0c) | zona_mapeada_setup_A |
| 2026-09-21 19:05 | ETH-USDT-SWAP | 2767.2 | 2782.9/2762.3 | 2760.4 | res 2748.4 (ha 12 candles) | 31.71 | 0.0022% | — | sem_zona |
| 2026-09-21 19:05 | SOL-USDT-SWAP | 119.06 | 119.96/118.59 | 118.31 | res 119.10 (ha 6 candles) | 1.5843 | 0.0100% | A/compra@119.10 (1t/0c) | zona_mapeada_setup_A |
| 2026-09-21 19:05 | XRP-USDT-SWAP | 1.5495 | 1.5554/1.5176 | 1.5071 | res 1.4387 (ha 20 candles) | 0.02478 | 0.0100% | — | sem_zona |
| 2026-09-21 19:05 | DOGE-USDT-SWAP | 0.09928 | 0.10021/0.09806 | 0.09853 | — | 0.00245 | 0.0100% | — | sem_zona |
| 2026-09-21 19:05 | ARB-USDT-SWAP | 0.22142 | 0.22532/0.22030 | 0.22774 | — | 0.00877 | -0.0109% | B/venda@0.23014 (0t/2c) | zona_mapeada_setup_B |
| 2026-09-21 19:05 | WLD-USDT-SWAP | 0.45120 | 0.46530/0.45030 | 0.43920 | res 0.45540 (ha 8 candles) | 0.01152 | 0.0100% | — | invalidado_setup_A |
| 2026-09-21 19:05 | SUI-USDT-SWAP | 1.0174 | 1.0205/1.0116 | 1.0364 | res 1.0567 (ha 8 candles) | 0.03033 | 0.0100% | A/compra@0.95440 (0t/6c) | zona_mapeada_setup_A |
| 2026-09-21 19:05 | UNI-USDT-SWAP | 8.7730 | 8.9590/8.7520 | 8.8130 | res 9.0550 (ha 8 candles) | 0.23093 | 0.0034% | — | sem_zona |
| 2026-09-21 19:05 | LINK-USDT-SWAP | 13.11 | 13.20/13.04 | 13.03 | res 13.17 (ha 8 candles) | 0.21386 | 0.0100% | — | sem_zona |
| 2026-09-21 20:05 | BTC-USDT-SWAP | 86422.4 | 86728.1/86263.2 | 86451.6 | res 86319.6 (ha 7 candles) | 742.41 | 0.0100% | — | zona_expirada_setup_A |
| 2026-09-21 20:05 | ETH-USDT-SWAP | 2777.7 | 2782.9/2766.7 | 2760.4 | res 2748.4 (ha 13 candles) | 29.00 | 0.0020% | — | sem_zona |
| 2026-09-21 20:05 | SOL-USDT-SWAP | 119.43 | 119.80/118.73 | 118.31 | res 119.10 (ha 7 candles) | 1.3500 | 0.0100% | — | descartado_rr_baixo_setup_A |
| 2026-09-21 20:05 | XRP-USDT-SWAP | 1.5555 | 1.5745/1.5450 | 1.5071 | res 1.4387 (ha 21 candles) | 0.02334 | 0.0100% | — | sem_zona |
| 2026-09-21 20:05 | DOGE-USDT-SWAP | 0.10031 | 0.10194/0.09929 | 0.09853 | — | 0.00242 | 0.0100% | — | sem_zona |
| 2026-09-21 20:05 | ARB-USDT-SWAP | 0.22565 | 0.22609/0.22142 | 0.22774 | — | 0.00870 | -0.0103% | B/venda@0.23014 (0t/3c) | zona_mapeada_setup_B |
| 2026-09-21 20:05 | WLD-USDT-SWAP | 0.46060 | 0.46260/0.45130 | 0.43920 | res 0.45540 (ha 9 candles) | 0.01164 | 0.0100% | — | sem_zona |
| 2026-09-21 20:05 | SUI-USDT-SWAP | 1.0271 | 1.0317/1.0174 | 1.0364 | res 1.0567 (ha 9 candles) | 0.02839 | 0.0100% | A/compra@0.95440 (0t/7c) | zona_mapeada_setup_A |
| 2026-09-21 20:05 | UNI-USDT-SWAP | 8.9820 | 8.9870/8.7460 | 8.8130 | res 9.0550 (ha 9 candles) | 0.22993 | 0.0074% | — | sem_zona |
| 2026-09-21 20:05 | LINK-USDT-SWAP | 13.22 | 13.22/13.10 | 13.03 | res 13.17 (ha 9 candles) | 0.20064 | 0.0100% | A/compra@13.17 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-21 21:05 | BTC-USDT-SWAP | 86589.1 | 86677.8/86340.0 | 86589.1 | res 87374.3 (ha 3 candles) | 646.89 | 0.0100% | — | sem_zona |
| 2026-09-21 21:05 | ETH-USDT-SWAP | 2774.6 | 2787.5/2765.0 | 2774.6 | res 2807.0 (ha 3 candles) | 26.49 | 0.0020% | — | sem_zona |
| 2026-09-21 21:05 | SOL-USDT-SWAP | 118.87 | 119.90/118.35 | 118.87 | res 119.10 (ha 8 candles) | 1.3221 | 0.0100% | — | sem_zona |
| 2026-09-21 21:05 | XRP-USDT-SWAP | 1.5360 | 1.5691/1.5252 | 1.5360 | res 1.4387 (ha 22 candles) | 0.02526 | 0.0100% | — | sem_zona |
| 2026-09-21 21:05 | DOGE-USDT-SWAP | 0.09987 | 0.10218/0.09888 | 0.09987 | — | 0.00239 | 0.0100% | — | sem_zona |
| 2026-09-21 21:05 | ARB-USDT-SWAP | 0.22559 | 0.23007/0.22474 | 0.22559 | — | 0.00866 | -0.0120% | — | CONFIRMADO_setup_B |
| 2026-09-21 21:05 | WLD-USDT-SWAP | 0.45800 | 0.46540/0.45540 | 0.45800 | res 0.46650 (ha 3 candles) | 0.01109 | 0.0100% | — | sem_zona |
| 2026-09-21 21:05 | SUI-USDT-SWAP | 1.0423 | 1.0470/1.0260 | 1.0423 | res 1.0567 (ha 10 candles) | 0.02695 | 0.0100% | — | zona_expirada_setup_A |
| 2026-09-21 21:05 | UNI-USDT-SWAP | 8.9880 | 9.1670/8.9380 | 8.9880 | — | 0.20764 | 0.0088% | — | sem_zona |
| 2026-09-21 21:05 | LINK-USDT-SWAP | 13.18 | 13.26/13.09 | 13.18 | res 13.32 (ha 3 candles) | 0.18829 | 0.0100% | A/compra@13.17 (1t/0c) | zona_mapeada_setup_A |
| 2026-09-21 22:05 | BTC-USDT-SWAP | 85875.7 | 86602.7/85827.9 | 86589.1 | res 87374.3 (ha 4 candles) | 652.84 | 0.0100% | — | sem_zona |
| 2026-09-21 22:05 | ETH-USDT-SWAP | 2753.7 | 2776.8/2751.2 | 2774.6 | res 2807.0 (ha 4 candles) | 26.92 | 0.0034% | — | sem_zona |
| 2026-09-21 22:05 | SOL-USDT-SWAP | 118.30 | 119.44/118.02 | 118.87 | res 119.96 (ha 3 candles) | 1.3764 | 0.0100% | — | sem_zona |
| 2026-09-21 22:05 | XRP-USDT-SWAP | 1.5216 | 1.5406/1.5182 | 1.5360 | res 1.4387 (ha 23 candles) | 0.02503 | 0.0100% | A/compra@1.4387 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-21 22:05 | DOGE-USDT-SWAP | 0.09942 | 0.10169/0.09915 | 0.09987 | — | 0.00249 | 0.0100% | — | sem_zona |
| 2026-09-21 22:05 | ARB-USDT-SWAP | 0.22370 | 0.22812/0.22246 | 0.22559 | — | 0.00793 | -0.0107% | B/venda@0.21927 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-21 22:05 | WLD-USDT-SWAP | 0.46960 | 0.47750/0.45610 | 0.45800 | res 0.46650 (ha 4 candles) | 0.01198 | 0.0100% | A/compra@0.46650 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-21 22:05 | SUI-USDT-SWAP | 1.0508 | 1.0814/1.0350 | 1.0423 | res 1.0567 (ha 11 candles) | 0.02821 | 0.0100% | — | sem_zona |
| 2026-09-21 22:05 | UNI-USDT-SWAP | 9.0770 | 9.3120/8.9660 | 8.9880 | — | 0.21993 | 0.0100% | — | sem_zona |
| 2026-09-21 22:05 | LINK-USDT-SWAP | 13.07 | 13.23/13.05 | 13.18 | res 13.32 (ha 4 candles) | 0.19071 | 0.0100% | — | invalidado_setup_A |
| 2026-09-21 23:05 | BTC-USDT-SWAP | 85594.4 | 85950.0/85360.8 | 86589.1 | res 87374.3 (ha 5 candles) | 657.31 | 0.0100% | — | sem_zona |
| 2026-09-21 23:05 | ETH-USDT-SWAP | 2747.7 | 2756.0/2735.2 | 2774.6 | res 2807.0 (ha 5 candles) | 27.13 | 0.0055% | — | sem_zona |
| 2026-09-21 23:05 | SOL-USDT-SWAP | 117.56 | 118.41/116.88 | 118.87 | res 119.96 (ha 4 candles) | 1.3879 | 0.0100% | — | sem_zona |
| 2026-09-21 23:05 | XRP-USDT-SWAP | 1.5122 | 1.5231/1.5041 | 1.5360 | res 1.5745 (ha 3 candles) | 0.02539 | 0.0100% | A/compra@1.4387 (0t/1c) | zona_mapeada_setup_A |
| 2026-09-21 23:05 | DOGE-USDT-SWAP | 0.09978 | 0.10053/0.09781 | 0.09987 | — | 0.00261 | 0.0100% | — | sem_zona |
| 2026-09-21 23:05 | ARB-USDT-SWAP | 0.22291 | 0.22386/0.21868 | 0.22559 | — | 0.00763 | -0.0138% | — | invalidado_setup_B |
| 2026-09-21 23:05 | WLD-USDT-SWAP | 0.46590 | 0.47340/0.45770 | 0.45800 | res 0.46650 (ha 5 candles) | 0.01270 | 0.0100% | A/compra@0.46650 (1t/0c) | zona_mapeada_setup_A |
| 2026-09-21 23:05 | SUI-USDT-SWAP | 1.0378 | 1.0576/1.0263 | 1.0423 | res 1.0567 (ha 12 candles) | 0.02791 | 0.0100% | — | sem_zona |
| 2026-09-21 23:05 | UNI-USDT-SWAP | 9.1720 | 9.1970/8.9150 | 8.9880 | — | 0.22936 | 0.0100% | — | sem_zona |
| 2026-09-21 23:05 | LINK-USDT-SWAP | 13.04 | 13.08/12.86 | 13.18 | res 13.32 (ha 5 candles) | 0.19800 | 0.0100% | — | sem_zona |
| 2026-09-22 00:05 | BTC-USDT-SWAP | 85690.0 | 85857.7/85362.5 | 86589.1 | res 87374.3 (ha 6 candles) | 642.09 | 0.0100% | — | sem_zona |
| 2026-09-22 00:05 | ETH-USDT-SWAP | 2739.0 | 2749.5/2735.6 | 2774.6 | res 2807.0 (ha 6 candles) | 26.51 | 0.0069% | — | sem_zona |
| 2026-09-22 00:05 | SOL-USDT-SWAP | 116.89 | 118.07/116.37 | 118.87 | res 119.96 (ha 5 candles) | 1.4407 | 0.0100% | — | sem_zona |
| 2026-09-22 00:05 | XRP-USDT-SWAP | 1.5153 | 1.5268/1.5077 | 1.5360 | res 1.5745 (ha 4 candles) | 0.02586 | 0.0100% | A/compra@1.4387 (0t/2c) | zona_mapeada_setup_A |
| 2026-09-22 00:05 | DOGE-USDT-SWAP | 0.09892 | 0.10080/0.09874 | 0.09987 | — | 0.00269 | 0.0100% | — | sem_zona |
| 2026-09-22 00:05 | ARB-USDT-SWAP | 0.22047 | 0.22423/0.22008 | 0.22559 | — | 0.00644 | -0.0142% | — | sem_zona |
| 2026-09-22 00:05 | WLD-USDT-SWAP | 0.45620 | 0.46850/0.45470 | 0.45800 | res 0.46650 (ha 6 candles) | 0.01323 | 0.0100% | — | invalidado_setup_A |
| 2026-09-22 00:05 | SUI-USDT-SWAP | 1.0441 | 1.0661/1.0342 | 1.0423 | res 1.0567 (ha 13 candles) | 0.02804 | 0.0100% | — | sem_zona |
| 2026-09-22 00:05 | UNI-USDT-SWAP | 9.1360 | 9.3260/9.0260 | 8.9880 | — | 0.23029 | 0.0100% | — | sem_zona |
| 2026-09-22 00:05 | LINK-USDT-SWAP | 12.94 | 13.08/12.91 | 13.18 | res 13.32 (ha 6 candles) | 0.20107 | 0.0100% | — | sem_zona |
| 2026-09-22 01:05 | BTC-USDT-SWAP | 85669.4 | 85730.0/85276.2 | 85669.4 | res 87374.3 (ha 7 candles) | 596.11 | 0.0100% | — | sem_zona |
| 2026-09-22 01:05 | ETH-USDT-SWAP | 2738.5 | 2744.0/2723.5 | 2738.5 | res 2807.0 (ha 7 candles) | 25.93 | 0.0075% | — | sem_zona |
| 2026-09-22 01:05 | SOL-USDT-SWAP | 116.76 | 117.03/116.26 | 116.76 | res 119.96 (ha 6 candles) | 1.3707 | 0.0100% | — | sem_zona |
| 2026-09-22 01:05 | XRP-USDT-SWAP | 1.5160 | 1.5222/1.5100 | 1.5160 | res 1.5745 (ha 5 candles) | 0.02484 | 0.0100% | A/compra@1.4387 (0t/3c) | zona_mapeada_setup_A |
| 2026-09-22 01:05 | DOGE-USDT-SWAP | 0.10193 | 0.10229/0.09849 | 0.10193 | — | 0.00282 | 0.0100% | — | sem_zona |
| 2026-09-22 01:05 | ARB-USDT-SWAP | 0.22021 | 0.22183/0.21754 | 0.22021 | res 0.23007 (ha 4 candles) | 0.00594 | -0.0116% | — | sem_zona |
| 2026-09-22 01:05 | WLD-USDT-SWAP | 0.45740 | 0.46200/0.45340 | 0.45740 | res 0.47750 (ha 3 candles) | 0.01291 | 0.0100% | — | sem_zona |
| 2026-09-22 01:05 | SUI-USDT-SWAP | 1.0368 | 1.0502/1.0313 | 1.0368 | res 1.0814 (ha 3 candles) | 0.02737 | 0.0100% | — | sem_zona |
| 2026-09-22 01:05 | UNI-USDT-SWAP | 9.0810 | 9.1590/8.9540 | 9.0810 | — | 0.22914 | 0.0100% | — | sem_zona |
| 2026-09-22 01:05 | LINK-USDT-SWAP | 13.00 | 13.00/12.86 | 13.00 | res 13.32 (ha 7 candles) | 0.19243 | 0.0100% | — | sem_zona |
| 2026-09-22 02:05 | BTC-USDT-SWAP | 85432.8 | 85710.0/85399.9 | 85669.4 | res 87374.3 (ha 8 candles) | 540.06 | 0.0100% | — | sem_zona |
| 2026-09-22 02:05 | ETH-USDT-SWAP | 2728.6 | 2742.4/2725.2 | 2738.5 | res 2807.0 (ha 8 candles) | 23.82 | 0.0084% | — | sem_zona |
| 2026-09-22 02:05 | SOL-USDT-SWAP | 116.34 | 117.10/116.19 | 116.76 | res 119.96 (ha 7 candles) | 1.3214 | 0.0100% | — | sem_zona |
| 2026-09-22 02:05 | XRP-USDT-SWAP | 1.5117 | 1.5265/1.5086 | 1.5160 | res 1.5745 (ha 6 candles) | 0.02382 | 0.0100% | A/compra@1.4387 (0t/4c) | zona_mapeada_setup_A |
| 2026-09-22 02:05 | DOGE-USDT-SWAP | 0.09994 | 0.10598/0.09952 | 0.10193 | — | 0.00306 | 0.0100% | — | sem_zona |
| 2026-09-22 02:05 | ARB-USDT-SWAP | 0.21823 | 0.22045/0.21620 | 0.22021 | res 0.23007 (ha 5 candles) | 0.00572 | -0.0093% | — | sem_zona |
| 2026-09-22 02:05 | WLD-USDT-SWAP | 0.44900 | 0.46200/0.44610 | 0.45740 | res 0.47750 (ha 4 candles) | 0.01325 | 0.0100% | — | sem_zona |
| 2026-09-22 02:05 | SUI-USDT-SWAP | 1.0200 | 1.0403/1.0148 | 1.0368 | res 1.0814 (ha 4 candles) | 0.02644 | 0.0100% | — | sem_zona |
| 2026-09-22 02:05 | UNI-USDT-SWAP | 8.8420 | 9.1040/8.8170 | 9.0810 | — | 0.23079 | 0.0100% | — | sem_zona |
| 2026-09-22 02:05 | LINK-USDT-SWAP | 12.90 | 13.06/12.88 | 13.00 | res 13.32 (ha 8 candles) | 0.19079 | 0.0100% | — | sem_zona |
| 2026-09-22 03:05 | BTC-USDT-SWAP | 85381.5 | 85577.4/85070.2 | 85669.4 | res 87374.3 (ha 9 candles) | 535.83 | 0.0100% | — | sem_zona |
| 2026-09-22 03:05 | ETH-USDT-SWAP | 2732.0 | 2738.3/2714.6 | 2738.5 | res 2807.0 (ha 9 candles) | 22.82 | 0.0094% | — | sem_zona |
| 2026-09-22 03:05 | SOL-USDT-SWAP | 116.79 | 117.15/115.52 | 116.76 | res 119.96 (ha 8 candles) | 1.3086 | 0.0100% | — | sem_zona |
| 2026-09-22 03:05 | XRP-USDT-SWAP | 1.5136 | 1.5179/1.4932 | 1.5160 | res 1.5745 (ha 7 candles) | 0.02380 | 0.0100% | A/compra@1.4387 (0t/5c) | zona_mapeada_setup_A |
| 2026-09-22 03:05 | DOGE-USDT-SWAP | 0.10008 | 0.10034/0.09838 | 0.10193 | — | 0.00296 | 0.0100% | — | sem_zona |
| 2026-09-22 03:05 | ARB-USDT-SWAP | 0.22150 | 0.22291/0.21625 | 0.22021 | res 0.23007 (ha 6 candles) | 0.00542 | -0.0070% | — | sem_zona |
| 2026-09-22 03:05 | WLD-USDT-SWAP | 0.45430 | 0.45840/0.44660 | 0.45740 | res 0.47750 (ha 5 candles) | 0.01321 | 0.0100% | — | sem_zona |
| 2026-09-22 03:05 | SUI-USDT-SWAP | 1.0200 | 1.0251/0.99800 | 1.0368 | res 1.0814 (ha 5 candles) | 0.02568 | 0.0100% | — | sem_zona |
| 2026-09-22 03:05 | UNI-USDT-SWAP | 8.9870 | 9.0520/8.8010 | 9.0810 | — | 0.22821 | 0.0100% | — | sem_zona |
| 2026-09-22 03:05 | LINK-USDT-SWAP | 12.94 | 12.98/12.80 | 13.00 | res 13.32 (ha 9 candles) | 0.18829 | 0.0100% | — | sem_zona |
| 2026-09-22 04:05 | BTC-USDT-SWAP | 85357.2 | 85560.0/85224.2 | 85669.4 | res 87374.3 (ha 10 candles) | 522.30 | 0.0100% | — | sem_zona |
| 2026-09-22 04:05 | ETH-USDT-SWAP | 2729.2 | 2735.2/2723.5 | 2738.5 | res 2807.0 (ha 10 candles) | 21.71 | 0.0078% | — | sem_zona |
| 2026-09-22 04:05 | SOL-USDT-SWAP | 116.48 | 117.01/116.33 | 116.76 | res 119.96 (ha 9 candles) | 1.2450 | 0.0100% | — | sem_zona |
| 2026-09-22 04:05 | XRP-USDT-SWAP | 1.5190 | 1.5260/1.5115 | 1.5160 | res 1.5745 (ha 8 candles) | 0.02315 | 0.0100% | A/compra@1.4387 (0t/6c) | zona_mapeada_setup_A |
| 2026-09-22 04:05 | DOGE-USDT-SWAP | 0.09976 | 0.10060/0.09943 | 0.10193 | — | 0.00285 | 0.0100% | — | sem_zona |
| 2026-09-22 04:05 | ARB-USDT-SWAP | 0.21856 | 0.22196/0.21851 | 0.22021 | res 0.23007 (ha 7 candles) | 0.00486 | -0.0088% | — | sem_zona |
| 2026-09-22 04:05 | WLD-USDT-SWAP | 0.45210 | 0.45710/0.45040 | 0.45740 | res 0.47750 (ha 6 candles) | 0.01317 | 0.0100% | — | sem_zona |
| 2026-09-22 04:05 | SUI-USDT-SWAP | 1.0167 | 1.0240/1.0086 | 1.0368 | res 1.0814 (ha 6 candles) | 0.02466 | 0.0100% | — | sem_zona |
| 2026-09-22 04:05 | UNI-USDT-SWAP | 8.8590 | 9.0110/8.8440 | 9.0810 | — | 0.22786 | 0.0100% | — | sem_zona |
| 2026-09-22 04:05 | LINK-USDT-SWAP | 12.91 | 12.97/12.85 | 13.00 | res 13.32 (ha 10 candles) | 0.18371 | 0.0100% | — | sem_zona |
| 2026-09-22 05:05 | BTC-USDT-SWAP | 85334.7 | 85475.7/85142.5 | 85334.7 | res 87374.3 (ha 11 candles) | 515.00 | 0.0100% | — | sem_zona |
| 2026-09-22 05:05 | ETH-USDT-SWAP | 2725.5 | 2733.5/2721.5 | 2725.5 | res 2807.0 (ha 11 candles) | 20.92 | 0.0079% | — | sem_zona |
| 2026-09-22 05:05 | SOL-USDT-SWAP | 116.27 | 116.80/115.96 | 116.27 | res 119.96 (ha 10 candles) | 1.2157 | 0.0100% | — | sem_zona |
| 2026-09-22 05:05 | XRP-USDT-SWAP | 1.5183 | 1.5255/1.5102 | 1.5183 | res 1.5745 (ha 9 candles) | 0.02336 | 0.0100% | A/compra@1.4387 (0t/7c) | zona_mapeada_setup_A |
| 2026-09-22 05:05 | DOGE-USDT-SWAP | 0.09884 | 0.09998/0.09874 | 0.09884 | — | 0.00275 | 0.0100% | — | sem_zona |
| 2026-09-22 05:05 | ARB-USDT-SWAP | 0.21875 | 0.21964/0.21678 | 0.21875 | res 0.23007 (ha 8 candles) | 0.00470 | -0.0070% | — | sem_zona |
| 2026-09-22 05:05 | WLD-USDT-SWAP | 0.45190 | 0.45650/0.44790 | 0.45190 | res 0.47750 (ha 7 candles) | 0.01289 | 0.0100% | — | sem_zona |
| 2026-09-22 05:05 | SUI-USDT-SWAP | 1.0132 | 1.0215/1.0075 | 1.0132 | res 1.0814 (ha 7 candles) | 0.02328 | 0.0100% | — | sem_zona |
| 2026-09-22 05:05 | UNI-USDT-SWAP | 8.9210 | 8.9380/8.8110 | 8.9210 | — | 0.22157 | 0.0100% | — | sem_zona |
| 2026-09-22 05:05 | LINK-USDT-SWAP | 12.90 | 12.94/12.82 | 12.90 | res 13.32 (ha 11 candles) | 0.17343 | 0.0100% | — | sem_zona |
| 2026-09-22 06:05 | BTC-USDT-SWAP | 86168.1 | 86342.5/85290.7 | 85334.7 | res 87374.3 (ha 12 candles) | 569.39 | 0.0100% | — | sem_zona |
| 2026-09-22 06:05 | ETH-USDT-SWAP | 2747.5 | 2755.0/2720.4 | 2725.5 | res 2807.0 (ha 12 candles) | 21.95 | 0.0067% | — | sem_zona |
| 2026-09-22 06:05 | SOL-USDT-SWAP | 117.44 | 118.00/115.74 | 116.27 | res 119.96 (ha 11 candles) | 1.3043 | 0.0100% | — | sem_zona |
| 2026-09-22 06:05 | XRP-USDT-SWAP | 1.5462 | 1.5539/1.5139 | 1.5183 | res 1.5745 (ha 10 candles) | 0.02455 | 0.0100% | — | zona_expirada_setup_A |
| 2026-09-22 06:05 | DOGE-USDT-SWAP | 0.09954 | 0.09976/0.09758 | 0.09884 | — | 0.00269 | 0.0100% | — | sem_zona |
| 2026-09-22 06:05 | ARB-USDT-SWAP | 0.22068 | 0.22317/0.21813 | 0.21875 | res 0.23007 (ha 9 candles) | 0.00480 | -0.0119% | — | sem_zona |
| 2026-09-22 06:05 | WLD-USDT-SWAP | 0.45490 | 0.45640/0.44670 | 0.45190 | res 0.47750 (ha 8 candles) | 0.01310 | 0.0100% | — | sem_zona |
| 2026-09-22 06:05 | SUI-USDT-SWAP | 1.0243 | 1.0287/1.0085 | 1.0132 | res 1.0814 (ha 8 candles) | 0.02345 | 0.0100% | — | sem_zona |
| 2026-09-22 06:05 | UNI-USDT-SWAP | 8.9340 | 9.0620/8.8500 | 8.9210 | — | 0.22243 | 0.0100% | — | sem_zona |
| 2026-09-22 06:05 | LINK-USDT-SWAP | 13.03 | 13.07/12.81 | 12.90 | res 13.32 (ha 12 candles) | 0.17929 | 0.0100% | — | sem_zona |
| 2026-09-22 07:05 | BTC-USDT-SWAP | 86228.0 | 86255.0/85623.0 | 85334.7 | res 87374.3 (ha 13 candles) | 546.78 | 0.0100% | — | sem_zona |
| 2026-09-22 07:05 | ETH-USDT-SWAP | 2749.6 | 2753.7/2728.6 | 2725.5 | res 2807.0 (ha 13 candles) | 22.22 | 0.0068% | — | sem_zona |
| 2026-09-22 07:05 | SOL-USDT-SWAP | 117.43 | 117.55/116.61 | 116.27 | res 119.96 (ha 12 candles) | 1.2850 | 0.0100% | — | sem_zona |
| 2026-09-22 07:05 | XRP-USDT-SWAP | 1.5412 | 1.5475/1.5262 | 1.5183 | res 1.5745 (ha 11 candles) | 0.02514 | 0.0100% | — | sem_zona |
| 2026-09-22 07:05 | DOGE-USDT-SWAP | 0.09877 | 0.09959/0.09818 | 0.09884 | — | 0.00260 | 0.0100% | — | sem_zona |
| 2026-09-22 07:05 | ARB-USDT-SWAP | 0.21891 | 0.22079/0.21720 | 0.21875 | res 0.23007 (ha 10 candles) | 0.00478 | -0.0142% | — | sem_zona |
| 2026-09-22 07:05 | WLD-USDT-SWAP | 0.44900 | 0.45580/0.44590 | 0.45190 | res 0.47750 (ha 9 candles) | 0.01329 | 0.0100% | — | sem_zona |
| 2026-09-22 07:05 | SUI-USDT-SWAP | 1.0216 | 1.0242/1.0094 | 1.0132 | res 1.0814 (ha 9 candles) | 0.02227 | 0.0100% | — | sem_zona |
| 2026-09-22 07:05 | UNI-USDT-SWAP | 8.8580 | 8.9340/8.7220 | 8.9210 | — | 0.22979 | 0.0100% | — | sem_zona |
| 2026-09-22 07:05 | LINK-USDT-SWAP | 13.00 | 13.03/12.87 | 12.90 | res 13.32 (ha 13 candles) | 0.17900 | 0.0100% | — | sem_zona |
| 2026-09-22 08:05 | BTC-USDT-SWAP | 85874.3 | 86238.4/85710.0 | 85334.7 | res 87374.3 (ha 14 candles) | 518.61 | 0.0100% | — | sem_zona |
| 2026-09-22 08:05 | ETH-USDT-SWAP | 2741.1 | 2751.0/2734.0 | 2725.5 | res 2807.0 (ha 14 candles) | 20.11 | 0.0072% | — | sem_zona |
| 2026-09-22 08:05 | SOL-USDT-SWAP | 116.78 | 117.43/116.33 | 116.27 | res 119.96 (ha 13 candles) | 1.2693 | 0.0100% | — | sem_zona |
| 2026-09-22 08:05 | XRP-USDT-SWAP | 1.5314 | 1.5413/1.5185 | 1.5183 | res 1.5745 (ha 12 candles) | 0.02431 | 0.0100% | — | sem_zona |
| 2026-09-22 08:05 | DOGE-USDT-SWAP | 0.09779 | 0.09879/0.09731 | 0.09884 | — | 0.00251 | 0.0100% | — | sem_zona |
| 2026-09-22 08:05 | ARB-USDT-SWAP | 0.21751 | 0.21897/0.21423 | 0.21875 | res 0.23007 (ha 11 candles) | 0.00463 | -0.0167% | — | sem_zona |
| 2026-09-22 08:05 | WLD-USDT-SWAP | 0.44790 | 0.44910/0.44070 | 0.45190 | res 0.47750 (ha 10 candles) | 0.01192 | 0.0100% | — | sem_zona |
| 2026-09-22 08:05 | SUI-USDT-SWAP | 1.0093 | 1.0216/1.0022 | 1.0132 | res 1.0814 (ha 10 candles) | 0.02209 | 0.0100% | — | sem_zona |
| 2026-09-22 08:05 | UNI-USDT-SWAP | 8.7460 | 8.8570/8.7070 | 8.9210 | — | 0.22979 | 0.0086% | — | sem_zona |
| 2026-09-22 08:05 | LINK-USDT-SWAP | 12.90 | 13.01/12.86 | 12.90 | res 13.32 (ha 14 candles) | 0.16836 | 0.0100% | — | sem_zona |
| 2026-09-22 09:05 | BTC-USDT-SWAP | 85963.0 | 86110.9/85737.8 | 85963.0 | res 86342.5 (ha 3 candles) | 513.38 | 0.0100% | — | sem_zona |
| 2026-09-22 09:05 | ETH-USDT-SWAP | 2741.2 | 2746.7/2733.6 | 2741.2 | res 2755.0 (ha 3 candles) | 19.58 | 0.0080% | — | sem_zona |
| 2026-09-22 09:05 | SOL-USDT-SWAP | 117.26 | 117.46/116.33 | 117.26 | res 118.00 (ha 3 candles) | 1.2521 | 0.0100% | — | sem_zona |
| 2026-09-22 09:05 | XRP-USDT-SWAP | 1.5372 | 1.5453/1.5209 | 1.5372 | res 1.5539 (ha 3 candles) | 0.02336 | 0.0100% | — | sem_zona |
| 2026-09-22 09:05 | DOGE-USDT-SWAP | 0.09790 | 0.09828/0.09712 | 0.09790 | — | 0.00244 | 0.0100% | — | sem_zona |
| 2026-09-22 09:05 | ARB-USDT-SWAP | 0.21775 | 0.21817/0.21502 | 0.21775 | res 0.22317 (ha 3 candles) | 0.00450 | -0.0208% | — | sem_zona |
| 2026-09-22 09:05 | WLD-USDT-SWAP | 0.44790 | 0.45060/0.44410 | 0.44790 | res 0.47750 (ha 11 candles) | 0.01131 | 0.0054% | — | sem_zona |
| 2026-09-22 09:05 | SUI-USDT-SWAP | 1.0141 | 1.0211/1.0028 | 1.0141 | res 1.0287 (ha 3 candles) | 0.02276 | 0.0100% | — | sem_zona |
| 2026-09-22 09:05 | UNI-USDT-SWAP | 8.7000 | 8.7680/8.6720 | 8.7000 | — | 0.22186 | 0.0100% | — | sem_zona |
| 2026-09-22 09:05 | LINK-USDT-SWAP | 12.94 | 12.98/12.84 | 12.94 | res 13.07 (ha 3 candles) | 0.16736 | 0.0100% | — | sem_zona |
| 2026-09-22 10:05 | BTC-USDT-SWAP | 85999.2 | 86184.9/85755.0 | 85963.0 | res 86342.5 (ha 4 candles) | 510.88 | 0.0100% | — | sem_zona |
| 2026-09-22 10:05 | ETH-USDT-SWAP | 2755.8 | 2757.0/2735.1 | 2741.2 | res 2755.0 (ha 4 candles) | 19.98 | 0.0085% | A/compra@2755.0 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-22 10:05 | SOL-USDT-SWAP | 117.42 | 117.70/116.80 | 117.26 | res 118.00 (ha 4 candles) | 1.2400 | 0.0083% | — | sem_zona |
| 2026-09-22 10:05 | XRP-USDT-SWAP | 1.5424 | 1.5461/1.5290 | 1.5372 | res 1.5539 (ha 4 candles) | 0.02247 | 0.0100% | — | sem_zona |
| 2026-09-22 10:05 | DOGE-USDT-SWAP | 0.09988 | 0.09995/0.09751 | 0.09790 | — | 0.00242 | 0.0100% | — | sem_zona |
| 2026-09-22 10:05 | ARB-USDT-SWAP | 0.22136 | 0.22175/0.21648 | 0.21775 | res 0.22317 (ha 4 candles) | 0.00454 | -0.0224% | — | sem_zona |
| 2026-09-22 10:05 | WLD-USDT-SWAP | 0.45620 | 0.45710/0.44550 | 0.44790 | res 0.47750 (ha 12 candles) | 0.01133 | 0.0034% | — | sem_zona |
| 2026-09-22 10:05 | SUI-USDT-SWAP | 1.0255 | 1.0273/1.0086 | 1.0141 | res 1.0287 (ha 4 candles) | 0.02307 | 0.0100% | — | sem_zona |
| 2026-09-22 10:05 | UNI-USDT-SWAP | 9.7090 | 9.7300/8.6820 | 8.7000 | — | 0.27950 | 0.0100% | — | sem_zona |
| 2026-09-22 10:05 | LINK-USDT-SWAP | 13.00 | 13.00/12.81 | 12.94 | res 13.07 (ha 4 candles) | 0.17214 | 0.0100% | — | sem_zona |
| 2026-09-22 11:05 | BTC-USDT-SWAP | 86320.9 | 86341.6/85518.4 | 85963.0 | res 86342.5 (ha 5 candles) | 545.55 | 0.0100% | — | sem_zona |
| 2026-09-22 11:05 | ETH-USDT-SWAP | 2758.0 | 2764.0/2737.7 | 2741.2 | res 2755.0 (ha 5 candles) | 20.25 | 0.0078% | — | CONFIRMADO_setup_A |
| 2026-09-22 11:05 | SOL-USDT-SWAP | 117.92 | 117.95/116.75 | 117.26 | res 118.00 (ha 5 candles) | 1.2150 | 0.0047% | — | sem_zona |
| 2026-09-22 11:05 | XRP-USDT-SWAP | 1.5885 | 1.5972/1.5374 | 1.5372 | res 1.5539 (ha 5 candles) | 0.02361 | 0.0100% | A/compra@1.5539 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-22 11:05 | DOGE-USDT-SWAP | 0.10094 | 0.10106/0.09937 | 0.09790 | — | 0.00231 | 0.0100% | — | sem_zona |
| 2026-09-22 11:05 | ARB-USDT-SWAP | 0.21689 | 0.22258/0.21515 | 0.21775 | res 0.22317 (ha 5 candles) | 0.00469 | -0.0214% | — | sem_zona |
| 2026-09-22 11:05 | WLD-USDT-SWAP | 0.45990 | 0.46290/0.45210 | 0.44790 | res 0.47750 (ha 13 candles) | 0.01139 | 0.0054% | — | sem_zona |
| 2026-09-22 11:05 | SUI-USDT-SWAP | 1.0182 | 1.0308/1.0077 | 1.0141 | res 1.0287 (ha 5 candles) | 0.02322 | 0.0100% | — | sem_zona |
| 2026-09-22 11:05 | UNI-USDT-SWAP | 9.0420 | 9.7410/8.9610 | 8.7000 | — | 0.31886 | 0.0100% | — | sem_zona |
| 2026-09-22 11:05 | LINK-USDT-SWAP | 13.12 | 13.29/12.93 | 12.94 | res 13.07 (ha 5 candles) | 0.18550 | 0.0100% | A/compra@13.07 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-22 12:05 | BTC-USDT-SWAP | 86206.8 | 86442.9/85406.0 | 85963.0 | res 86342.5 (ha 6 candles) | 564.27 | 0.0082% | — | sem_zona |
| 2026-09-22 12:05 | ETH-USDT-SWAP | 2741.3 | 2759.0/2714.0 | 2741.2 | res 2755.0 (ha 6 candles) | 21.63 | 0.0069% | — | sem_zona |
| 2026-09-22 12:05 | SOL-USDT-SWAP | 116.82 | 117.93/115.83 | 117.26 | res 118.00 (ha 6 candles) | 1.2636 | 0.0015% | — | sem_zona |
| 2026-09-22 12:05 | XRP-USDT-SWAP | 1.5642 | 1.5900/1.5328 | 1.5372 | res 1.5539 (ha 6 candles) | 0.02609 | 0.0100% | A/compra@1.5539 (1t/0c) | zona_mapeada_setup_A |
| 2026-09-22 12:05 | DOGE-USDT-SWAP | 0.09998 | 0.10113/0.09841 | 0.09790 | — | 0.00232 | 0.0100% | — | sem_zona |
| 2026-09-22 12:05 | ARB-USDT-SWAP | 0.21388 | 0.21694/0.21103 | 0.21775 | res 0.22317 (ha 6 candles) | 0.00471 | -0.0190% | — | sem_zona |
| 2026-09-22 12:05 | WLD-USDT-SWAP | 0.45030 | 0.46000/0.44370 | 0.44790 | res 0.47750 (ha 14 candles) | 0.01102 | 0.0047% | — | sem_zona |
| 2026-09-22 12:05 | SUI-USDT-SWAP | 1.0006 | 1.0181/0.98610 | 1.0141 | res 1.0287 (ha 6 candles) | 0.02220 | 0.0100% | — | sem_zona |
| 2026-09-22 12:05 | UNI-USDT-SWAP | 8.9630 | 9.0530/8.7830 | 8.7000 | — | 0.31343 | 0.0100% | — | sem_zona |
| 2026-09-22 12:05 | LINK-USDT-SWAP | 12.94 | 13.12/12.74 | 12.94 | res 13.07 (ha 6 candles) | 0.19957 | 0.0100% | — | invalidado_setup_A |
| 2026-09-22 13:05 | BTC-USDT-SWAP | 86369.9 | 86736.6/86070.8 | 86369.9 | res 86342.5 (ha 7 candles) | 569.74 | 0.0052% | A/compra@86342.5 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-22 13:05 | ETH-USDT-SWAP | 2742.8 | 2755.0/2735.4 | 2742.8 | res 2755.0 (ha 7 candles) | 21.55 | 0.0056% | — | sem_zona |
| 2026-09-22 13:05 | SOL-USDT-SWAP | 117.31 | 117.87/116.71 | 117.31 | res 118.00 (ha 7 candles) | 1.2371 | -0.0001% | — | sem_zona |
| 2026-09-22 13:05 | XRP-USDT-SWAP | 1.5716 | 1.5861/1.5629 | 1.5716 | res 1.5539 (ha 7 candles) | 0.02639 | 0.0100% | A/compra@1.5539 (1t/1c) | zona_mapeada_setup_A |
| 2026-09-22 13:05 | DOGE-USDT-SWAP | 0.09998 | 0.10052/0.09927 | 0.09998 | — | 0.00222 | 0.0100% | — | sem_zona |
| 2026-09-22 13:05 | ARB-USDT-SWAP | 0.21401 | 0.21543/0.21325 | 0.21401 | res 0.22317 (ha 7 candles) | 0.00450 | -0.0176% | — | sem_zona |
| 2026-09-22 13:05 | WLD-USDT-SWAP | 0.45290 | 0.45760/0.44980 | 0.45290 | res 0.47750 (ha 15 candles) | 0.01046 | 0.0086% | — | sem_zona |
| 2026-09-22 13:05 | SUI-USDT-SWAP | 1.0065 | 1.0155/1.0004 | 1.0065 | res 1.0287 (ha 7 candles) | 0.02104 | 0.0100% | — | sem_zona |
| 2026-09-22 13:05 | UNI-USDT-SWAP | 9.1730 | 9.3800/8.9280 | 9.1730 | — | 0.32557 | 0.0100% | — | sem_zona |
| 2026-09-22 13:05 | LINK-USDT-SWAP | 13.04 | 13.11/12.93 | 13.04 | res 13.07 (ha 7 candles) | 0.19607 | 0.0100% | — | sem_zona |
| 2026-09-22 14:05 | BTC-USDT-SWAP | 86375.1 | 86547.6/86022.9 | 86369.9 | res 86342.5 (ha 8 candles) | 571.85 | 0.0033% | — | CONFIRMADO_setup_A |
| 2026-09-22 14:05 | ETH-USDT-SWAP | 2744.6 | 2749.7/2728.0 | 2742.8 | res 2764.0 (ha 3 candles) | 22.10 | 0.0046% | — | sem_zona |
| 2026-09-22 14:05 | SOL-USDT-SWAP | 117.40 | 117.76/116.64 | 117.31 | res 117.95 (ha 3 candles) | 1.1957 | 0.0002% | — | sem_zona |
| 2026-09-22 14:05 | XRP-USDT-SWAP | 1.5628 | 1.5769/1.5471 | 1.5716 | res 1.5972 (ha 3 candles) | 0.02716 | 0.0100% | A/compra@1.5539 (2t/0c) | zona_mapeada_setup_A |
| 2026-09-22 14:05 | DOGE-USDT-SWAP | 0.09946 | 0.10017/0.09862 | 0.09998 | — | 0.00218 | 0.0100% | — | sem_zona |
| 2026-09-22 14:05 | ARB-USDT-SWAP | 0.21480 | 0.21556/0.21225 | 0.21401 | res 0.22258 (ha 3 candles) | 0.00444 | -0.0118% | — | sem_zona |
| 2026-09-22 14:05 | WLD-USDT-SWAP | 0.45400 | 0.45410/0.44670 | 0.45290 | res 0.46290 (ha 3 candles) | 0.01000 | 0.0100% | — | sem_zona |
| 2026-09-22 14:05 | SUI-USDT-SWAP | 1.0015 | 1.0080/0.99490 | 1.0065 | res 1.0308 (ha 3 candles) | 0.01970 | 0.0100% | — | sem_zona |
| 2026-09-22 14:05 | UNI-USDT-SWAP | 9.2010 | 9.2580/9.0570 | 9.1730 | — | 0.31850 | 0.0089% | — | sem_zona |
| 2026-09-22 14:05 | LINK-USDT-SWAP | 13.00 | 13.04/12.89 | 13.04 | res 13.29 (ha 3 candles) | 0.19500 | 0.0100% | — | sem_zona |
| 2026-09-22 15:05 | BTC-USDT-SWAP | 86537.5 | 86620.0/86204.2 | 86369.9 | res 86342.5 (ha 9 candles) | 569.14 | 0.0018% | — | sem_zona |
| 2026-09-22 15:05 | ETH-USDT-SWAP | 2752.4 | 2759.0/2742.3 | 2742.8 | res 2764.0 (ha 4 candles) | 21.83 | 0.0050% | — | sem_zona |
| 2026-09-22 15:05 | SOL-USDT-SWAP | 117.91 | 118.14/117.26 | 117.31 | res 117.95 (ha 4 candles) | 1.2036 | 0.0022% | — | sem_zona |
| 2026-09-22 15:05 | XRP-USDT-SWAP | 1.5711 | 1.5755/1.5612 | 1.5716 | res 1.5972 (ha 4 candles) | 0.02731 | 0.0100% | A/compra@1.5539 (2t/1c) | zona_mapeada_setup_A |
| 2026-09-22 15:05 | DOGE-USDT-SWAP | 0.09968 | 0.10005/0.09926 | 0.09998 | — | 0.00196 | 0.0100% | — | sem_zona |
| 2026-09-22 15:05 | ARB-USDT-SWAP | 0.21653 | 0.21778/0.21460 | 0.21401 | res 0.22258 (ha 4 candles) | 0.00436 | -0.0108% | — | sem_zona |
| 2026-09-22 15:05 | WLD-USDT-SWAP | 0.45670 | 0.45920/0.45290 | 0.45290 | res 0.46290 (ha 4 candles) | 0.00984 | 0.0100% | — | sem_zona |
| 2026-09-22 15:05 | SUI-USDT-SWAP | 1.0068 | 1.0095/1.0006 | 1.0065 | res 1.0308 (ha 4 candles) | 0.01899 | 0.0100% | — | sem_zona |
| 2026-09-22 15:05 | UNI-USDT-SWAP | 9.1380 | 9.2210/9.0960 | 9.1730 | — | 0.31279 | 0.0051% | — | sem_zona |
| 2026-09-22 15:05 | LINK-USDT-SWAP | 13.01 | 13.04/12.96 | 13.04 | res 13.29 (ha 4 candles) | 0.19057 | 0.0100% | — | sem_zona |
| 2026-09-22 16:05 | BTC-USDT-SWAP | 86417.3 | 86615.1/86210.0 | 86369.9 | res 86736.6 (ha 3 candles) | 575.92 | 0.0018% | — | sem_zona |
| 2026-09-22 16:05 | ETH-USDT-SWAP | 2751.2 | 2755.5/2741.6 | 2742.8 | res 2764.0 (ha 5 candles) | 21.60 | 0.0049% | — | sem_zona |
| 2026-09-22 16:05 | SOL-USDT-SWAP | 118.08 | 118.42/117.57 | 117.31 | res 117.95 (ha 5 candles) | 1.1993 | 0.0033% | A/compra@117.95 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-22 16:05 | XRP-USDT-SWAP | 1.5812 | 1.5867/1.5673 | 1.5716 | res 1.5972 (ha 5 candles) | 0.02741 | 0.0100% | A/compra@1.5539 (2t/2c) | zona_mapeada_setup_A |
| 2026-09-22 16:05 | DOGE-USDT-SWAP | 0.09990 | 0.10010/0.09919 | 0.09998 | — | 0.00157 | 0.0100% | — | sem_zona |
| 2026-09-22 16:05 | ARB-USDT-SWAP | 0.21644 | 0.21787/0.21594 | 0.21401 | res 0.22258 (ha 5 candles) | 0.00419 | -0.0129% | — | sem_zona |
| 2026-09-22 16:05 | WLD-USDT-SWAP | 0.45530 | 0.46260/0.45500 | 0.45290 | res 0.46290 (ha 5 candles) | 0.00924 | 0.0100% | — | sem_zona |
| 2026-09-22 16:05 | SUI-USDT-SWAP | 1.0065 | 1.0111/1.0024 | 1.0065 | res 1.0308 (ha 5 candles) | 0.01779 | 0.0100% | — | sem_zona |
| 2026-09-22 16:05 | UNI-USDT-SWAP | 9.1360 | 9.2550/9.1320 | 9.1730 | — | 0.30107 | 0.0014% | — | sem_zona |
| 2026-09-22 16:05 | LINK-USDT-SWAP | 13.00 | 13.05/12.97 | 13.04 | res 13.29 (ha 5 candles) | 0.18357 | 0.0100% | — | sem_zona |
| 2026-09-22 17:05 | BTC-USDT-SWAP | 86152.3 | 86540.0/86106.2 | 86152.3 | res 86736.6 (ha 4 candles) | 570.68 | 0.0002% | — | sem_zona |
| 2026-09-22 17:05 | ETH-USDT-SWAP | 2750.2 | 2762.5/2743.3 | 2750.2 | res 2764.0 (ha 6 candles) | 21.27 | 0.0037% | — | sem_zona |
| 2026-09-22 17:05 | SOL-USDT-SWAP | 118.20 | 118.66/117.70 | 118.20 | res 117.95 (ha 6 candles) | 1.1514 | 0.0023% | A/compra@117.95 (1t/0c) | zona_mapeada_setup_A |
| 2026-09-22 17:05 | XRP-USDT-SWAP | 1.5874 | 1.6098/1.5720 | 1.5874 | res 1.5972 (ha 6 candles) | 0.02835 | 0.0100% | A/compra@1.5539 (2t/3c) | zona_mapeada_setup_A |
| 2026-09-22 17:05 | DOGE-USDT-SWAP | 0.09998 | 0.10055/0.09950 | 0.09998 | — | 0.00150 | 0.0100% | — | sem_zona |
| 2026-09-22 17:05 | ARB-USDT-SWAP | 0.21817 | 0.21836/0.21557 | 0.21817 | res 0.22258 (ha 6 candles) | 0.00392 | -0.0093% | — | sem_zona |
| 2026-09-22 17:05 | WLD-USDT-SWAP | 0.46250 | 0.46370/0.45420 | 0.46250 | res 0.46290 (ha 6 candles) | 0.00908 | 0.0100% | — | sem_zona |
| 2026-09-22 17:05 | SUI-USDT-SWAP | 1.0045 | 1.0150/1.0010 | 1.0045 | res 1.0308 (ha 6 candles) | 0.01685 | 0.0100% | — | sem_zona |
| 2026-09-22 17:05 | UNI-USDT-SWAP | 9.2220 | 9.3360/9.1360 | 9.2220 | — | 0.29743 | 0.0024% | — | sem_zona |
| 2026-09-22 17:05 | LINK-USDT-SWAP | 13.00 | 13.10/12.93 | 13.00 | res 13.29 (ha 6 candles) | 0.18264 | 0.0100% | — | sem_zona |
| 2026-09-22 18:05 | BTC-USDT-SWAP | 86230.3 | 86339.1/86082.4 | 86152.3 | res 86736.6 (ha 5 candles) | 565.03 | -0.0005% | — | sem_zona |
| 2026-09-22 18:05 | ETH-USDT-SWAP | 2750.5 | 2757.3/2746.1 | 2750.2 | res 2764.0 (ha 7 candles) | 21.24 | 0.0033% | — | sem_zona |
| 2026-09-22 18:05 | SOL-USDT-SWAP | 117.90 | 118.30/117.73 | 118.20 | res 117.95 (ha 7 candles) | 1.1436 | 0.0030% | A/compra@117.95 (2t/0c) | zona_mapeada_setup_A |
| 2026-09-22 18:05 | XRP-USDT-SWAP | 1.5714 | 1.5913/1.5641 | 1.5874 | res 1.5972 (ha 7 candles) | 0.02926 | 0.0100% | A/compra@1.5539 (2t/4c) | zona_mapeada_setup_A |
| 2026-09-22 18:05 | DOGE-USDT-SWAP | 0.10008 | 0.10059/0.09941 | 0.09998 | — | 0.00150 | 0.0100% | — | sem_zona |
| 2026-09-22 18:05 | ARB-USDT-SWAP | 0.21870 | 0.21928/0.21659 | 0.21817 | res 0.22258 (ha 7 candles) | 0.00386 | -0.0112% | — | sem_zona |
| 2026-09-22 18:05 | WLD-USDT-SWAP | 0.46420 | 0.46920/0.46090 | 0.46250 | res 0.46290 (ha 7 candles) | 0.00919 | 0.0100% | A/compra@0.46290 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-22 18:05 | SUI-USDT-SWAP | 1.0079 | 1.0118/1.0001 | 1.0045 | res 1.0308 (ha 7 candles) | 0.01659 | 0.0100% | — | sem_zona |
| 2026-09-22 18:05 | UNI-USDT-SWAP | 9.4670 | 9.4780/9.2120 | 9.2220 | — | 0.30450 | 0.0032% | B/venda@9.4950 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-22 18:05 | LINK-USDT-SWAP | 12.95 | 13.01/12.93 | 13.00 | res 13.29 (ha 7 candles) | 0.17957 | 0.0100% | — | sem_zona |
