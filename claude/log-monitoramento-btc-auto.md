# Log de Monitoramento Automatico -- Multi-Par (script gratuito, GitHub Actions)

> Gerado por script Python sem LLM (ver monitor/fetch_and_check.py). Fonte: OKX. Cobre os pares em PAIRS (configuracao no topo do script) -- BTC-USDT-SWAP e os demais adicionados na expansao de 07/09/2026. Leitura e MECANICA (regras objetivas da secao 4 do plano), sem a prosa qualitativa que o Claude gerava -- cole este log numa conversa do Claude se quiser a leitura interpretativa.

| Data/Hora (BRT) | Par | Close 1h | High/Low 1h | Close 4h | Swing 1h ref | ATR 1h | Funding | Zona ativa | Status checklist |
|---|---|---|---|---|---|---|---|---|---|
| 2026-10-11 16:06 | BTC-USDT-SWAP | 83634.7 | 83872.8/83518.9 | 83864.2 | sup 82907.1 (ha 8 candles) | 250.60 | -0.0009% | B/venda@83499.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-11 16:06 | ETH-USDT-SWAP | 2533.7 | 2541.1/2526.8 | 2534.4 | — | 11.04 | -0.0023% | — | sem_zona |
| 2026-10-11 16:06 | SOL-USDT-SWAP | 111.51 | 112.34/111.16 | 111.93 | — | 0.75286 | 0.0100% | — | sem_zona |
| 2026-10-11 16:06 | XRP-USDT-SWAP | 1.4083 | 1.4165/1.4050 | 1.4248 | res 1.4258 (ha 3 candles) | 0.00810 | 0.0043% | A/compra@1.4084 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-11 16:06 | DOGE-USDT-SWAP | 0.08670 | 0.08711/0.08643 | 0.08722 | res 0.08611 (ha 17 candles) | 0.00055 | 0.0008% | A/compra@0.08611 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-11 16:06 | ARB-USDT-SWAP | 0.19737 | 0.19868/0.19623 | 0.20064 | sup 0.19605 (ha 5 candles) | 0.00389 | 0.0094% | — | sem_zona |
| 2026-10-11 16:06 | WLD-USDT-SWAP | 0.56070 | 0.56590/0.55750 | 0.57920 | res 0.56900 (ha 17 candles) | 0.01002 | 0.0100% | — | sem_zona |
| 2026-10-11 16:06 | SUI-USDT-SWAP | 1.1214 | 1.1330/1.1166 | 1.1326 | — | 0.01109 | -0.0041% | B/compra@1.1380 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-11 16:06 | UNI-USDT-SWAP | 7.7300 | 7.8240/7.6940 | 7.7190 | res 7.6820 (ha 16 candles) | 0.09350 | -0.0036% | — | sem_zona |
| 2026-10-11 16:06 | LINK-USDT-SWAP | 13.29 | 13.42/13.24 | 13.35 | — | 0.10729 | 0.0051% | B/compra@13.23 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-11 17:06 | BTC-USDT-SWAP | 83625.2 | 83720.5/83606.6 | 83625.2 | — | 253.39 | 0.0000% | B/venda@83499.0 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-11 17:06 | ETH-USDT-SWAP | 2535.3 | 2537.7/2532.0 | 2535.3 | — | 11.04 | -0.0014% | — | sem_zona |
| 2026-10-11 17:06 | SOL-USDT-SWAP | 111.31 | 111.64/111.27 | 111.31 | — | 0.74643 | 0.0100% | — | sem_zona |
| 2026-10-11 17:06 | XRP-USDT-SWAP | 1.4096 | 1.4103/1.4073 | 1.4096 | res 1.4258 (ha 4 candles) | 0.00796 | 0.0025% | — | descartado_rr_baixo_setup_A |
| 2026-10-11 17:06 | DOGE-USDT-SWAP | 0.08684 | 0.08694/0.08665 | 0.08684 | res 0.08611 (ha 18 candles) | 0.00054 | 0.0010% | A/compra@0.08611 (0t/4c) | zona_mapeada_setup_A |
| 2026-10-11 17:06 | ARB-USDT-SWAP | 0.19909 | 0.19918/0.19695 | 0.19909 | sup 0.19605 (ha 6 candles) | 0.00375 | 0.0100% | — | sem_zona |
| 2026-10-11 17:06 | WLD-USDT-SWAP | 0.56490 | 0.56510/0.55540 | 0.56490 | res 0.58590 (ha 3 candles) | 0.00966 | 0.0100% | — | sem_zona |
| 2026-10-11 17:06 | SUI-USDT-SWAP | 1.1227 | 1.1244/1.1195 | 1.1227 | — | 0.01084 | -0.0031% | B/compra@1.1380 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-11 17:06 | UNI-USDT-SWAP | 7.7230 | 7.7480/7.7020 | 7.7230 | res 7.6820 (ha 17 candles) | 0.09057 | -0.0016% | — | sem_zona |
| 2026-10-11 17:06 | LINK-USDT-SWAP | 13.29 | 13.31/13.28 | 13.29 | res 13.24 (ha 29 candles) | 0.10457 | 0.0050% | B/compra@13.23 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-11 18:06 | BTC-USDT-SWAP | 83637.2 | 83698.8/83563.2 | 83625.2 | — | 249.74 | 0.0013% | B/venda@83499.0 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-11 18:06 | ETH-USDT-SWAP | 2536.8 | 2538.4/2531.9 | 2535.3 | — | 11.10 | -0.0012% | — | sem_zona |
| 2026-10-11 18:06 | SOL-USDT-SWAP | 111.28 | 111.44/110.94 | 111.31 | — | 0.73643 | 0.0100% | — | sem_zona |
| 2026-10-11 18:06 | XRP-USDT-SWAP | 1.4112 | 1.4114/1.4040 | 1.4096 | res 1.4258 (ha 5 candles) | 0.00805 | 0.0011% | — | sem_zona |
| 2026-10-11 18:06 | DOGE-USDT-SWAP | 0.08708 | 0.08708/0.08671 | 0.08684 | res 0.08765 (ha 3 candles) | 0.00054 | -0.0007% | A/compra@0.08611 (0t/5c) | zona_mapeada_setup_A |
| 2026-10-11 18:06 | ARB-USDT-SWAP | 0.19934 | 0.20036/0.19852 | 0.19909 | sup 0.19605 (ha 7 candles) | 0.00344 | 0.0100% | — | sem_zona |
| 2026-10-11 18:06 | WLD-USDT-SWAP | 0.55790 | 0.56530/0.55730 | 0.56490 | res 0.58590 (ha 4 candles) | 0.00975 | 0.0100% | B/compra@0.55290 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-11 18:06 | SUI-USDT-SWAP | 1.1259 | 1.1281/1.1196 | 1.1227 | — | 0.01083 | -0.0030% | B/compra@1.1380 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-11 18:06 | UNI-USDT-SWAP | 7.7400 | 7.7470/7.7020 | 7.7230 | res 7.8900 (ha 3 candles) | 0.08893 | 0.0009% | — | sem_zona |
| 2026-10-11 18:06 | LINK-USDT-SWAP | 13.34 | 13.34/13.25 | 13.29 | res 13.47 (ha 3 candles) | 0.10693 | 0.0051% | — | descartado_rr_baixo_setup_B |
| 2026-10-11 19:06 | BTC-USDT-SWAP | 83489.9 | 83643.1/83222.3 | 83625.2 | — | 262.31 | 0.0015% | B/venda@83499.0 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-11 19:06 | ETH-USDT-SWAP | 2528.5 | 2537.2/2513.4 | 2535.3 | — | 12.21 | -0.0014% | B/venda@2520.8 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-11 19:06 | SOL-USDT-SWAP | 110.69 | 111.30/109.81 | 111.31 | — | 0.80143 | 0.0082% | — | sem_zona |
| 2026-10-11 19:06 | XRP-USDT-SWAP | 1.4043 | 1.4116/1.3945 | 1.4096 | res 1.4258 (ha 6 candles) | 0.00886 | -0.0020% | — | sem_zona |
| 2026-10-11 19:06 | DOGE-USDT-SWAP | 0.08647 | 0.08715/0.08604 | 0.08684 | res 0.08765 (ha 4 candles) | 0.00059 | 0.0011% | A/compra@0.08611 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-11 19:06 | ARB-USDT-SWAP | 0.19912 | 0.19938/0.19545 | 0.19909 | sup 0.19605 (ha 8 candles) | 0.00349 | 0.0100% | — | sem_zona |
| 2026-10-11 19:06 | WLD-USDT-SWAP | 0.55010 | 0.55840/0.54360 | 0.56490 | res 0.58590 (ha 5 candles) | 0.01026 | 0.0100% | — | invalidado_setup_B |
| 2026-10-11 19:06 | SUI-USDT-SWAP | 1.1166 | 1.1263/1.1052 | 1.1227 | — | 0.01184 | -0.0004% | B/compra@1.1380 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-11 19:06 | UNI-USDT-SWAP | 7.6580 | 7.7420/7.5880 | 7.7230 | res 7.8900 (ha 4 candles) | 0.09407 | 0.0021% | — | sem_zona |
| 2026-10-11 19:06 | LINK-USDT-SWAP | 13.28 | 13.34/13.13 | 13.29 | res 13.47 (ha 4 candles) | 0.11586 | 0.0050% | B/compra@13.19 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-11 20:06 | BTC-USDT-SWAP | 83597.2 | 83644.9/83402.3 | 83625.2 | — | 269.92 | 0.0002% | — | invalidado_setup_B |
| 2026-10-11 20:06 | ETH-USDT-SWAP | 2532.5 | 2534.3/2525.8 | 2535.3 | — | 12.47 | -0.0020% | B/venda@2520.8 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-11 20:06 | SOL-USDT-SWAP | 111.04 | 111.30/110.44 | 111.31 | — | 0.84000 | 0.0074% | — | sem_zona |
| 2026-10-11 20:06 | XRP-USDT-SWAP | 1.4073 | 1.4098/1.4022 | 1.4096 | res 1.4258 (ha 7 candles) | 0.00913 | -0.0019% | — | sem_zona |
| 2026-10-11 20:06 | DOGE-USDT-SWAP | 0.08656 | 0.08676/0.08627 | 0.08684 | res 0.08765 (ha 5 candles) | 0.00061 | 0.0019% | A/compra@0.08611 (1t/1c) | zona_mapeada_setup_A |
| 2026-10-11 20:06 | ARB-USDT-SWAP | 0.19916 | 0.20010/0.19788 | 0.19909 | sup 0.19605 (ha 9 candles) | 0.00350 | 0.0100% | — | sem_zona |
| 2026-10-11 20:06 | WLD-USDT-SWAP | 0.55350 | 0.55400/0.54820 | 0.56490 | res 0.58590 (ha 6 candles) | 0.01024 | 0.0100% | — | sem_zona |
| 2026-10-11 20:06 | SUI-USDT-SWAP | 1.1232 | 1.1272/1.1135 | 1.1227 | — | 0.01240 | 0.0029% | B/compra@1.1380 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-11 20:06 | UNI-USDT-SWAP | 7.7500 | 7.7590/7.6390 | 7.7230 | res 7.8900 (ha 5 candles) | 0.09829 | 0.0023% | — | sem_zona |
| 2026-10-11 20:06 | LINK-USDT-SWAP | 13.31 | 13.33/13.24 | 13.29 | res 13.47 (ha 5 candles) | 0.11921 | 0.0049% | B/compra@13.19 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-11 21:06 | BTC-USDT-SWAP | 83716.0 | 83738.9/83597.2 | 83716.0 | — | 270.58 | -0.0013% | B/compra@83826.4 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-11 21:06 | ETH-USDT-SWAP | 2535.6 | 2537.3/2532.5 | 2535.6 | — | 12.30 | -0.0020% | B/venda@2520.8 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-11 21:06 | SOL-USDT-SWAP | 111.28 | 111.37/111.02 | 111.28 | — | 0.82643 | 0.0059% | — | sem_zona |
| 2026-10-11 21:06 | XRP-USDT-SWAP | 1.4096 | 1.4107/1.4072 | 1.4096 | res 1.4258 (ha 8 candles) | 0.00891 | -0.0015% | — | sem_zona |
| 2026-10-11 21:06 | DOGE-USDT-SWAP | 0.08673 | 0.08682/0.08656 | 0.08673 | res 0.08765 (ha 6 candles) | 0.00059 | 0.0023% | A/compra@0.08611 (1t/2c) | zona_mapeada_setup_A |
| 2026-10-11 21:06 | ARB-USDT-SWAP | 0.19941 | 0.20025/0.19841 | 0.19941 | — | 0.00300 | 0.0100% | B/compra@0.19834 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-11 21:06 | WLD-USDT-SWAP | 0.56000 | 0.56210/0.55330 | 0.56000 | res 0.58590 (ha 7 candles) | 0.01050 | 0.0100% | — | sem_zona |
| 2026-10-11 21:06 | SUI-USDT-SWAP | 1.1296 | 1.1324/1.1233 | 1.1296 | res 1.1413 (ha 7 candles) | 0.01256 | 0.0049% | B/compra@1.1380 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-11 21:06 | UNI-USDT-SWAP | 7.7650 | 7.7760/7.7150 | 7.7650 | res 7.8900 (ha 6 candles) | 0.09593 | 0.0051% | — | sem_zona |
| 2026-10-11 21:06 | LINK-USDT-SWAP | 13.34 | 13.35/13.31 | 13.34 | res 13.47 (ha 6 candles) | 0.11871 | 0.0029% | B/compra@13.19 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-11 22:06 | BTC-USDT-SWAP | 83923.5 | 83963.4/83666.1 | 83716.0 | — | 282.48 | -0.0020% | — | descartado_rr_baixo_setup_B |
| 2026-10-11 22:06 | ETH-USDT-SWAP | 2545.2 | 2548.7/2534.4 | 2535.6 | — | 12.89 | -0.0020% | B/venda@2520.8 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-11 22:06 | SOL-USDT-SWAP | 111.59 | 111.74/111.10 | 111.28 | — | 0.84571 | 0.0064% | B/venda@112.04 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-11 22:06 | XRP-USDT-SWAP | 1.4090 | 1.4133/1.4070 | 1.4096 | res 1.4258 (ha 9 candles) | 0.00900 | -0.0005% | — | sem_zona |
| 2026-10-11 22:06 | DOGE-USDT-SWAP | 0.08685 | 0.08693/0.08666 | 0.08673 | res 0.08715 (ha 3 candles) | 0.00059 | 0.0014% | A/compra@0.08611 (1t/3c) | zona_mapeada_setup_A |
| 2026-10-11 22:06 | ARB-USDT-SWAP | 0.19822 | 0.19975/0.19778 | 0.19941 | — | 0.00296 | 0.0100% | B/compra@0.19834 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-11 22:06 | WLD-USDT-SWAP | 0.55280 | 0.56060/0.54930 | 0.56000 | res 0.58590 (ha 8 candles) | 0.01096 | 0.0100% | — | sem_zona |
| 2026-10-11 22:06 | SUI-USDT-SWAP | 1.1258 | 1.1305/1.1206 | 1.1296 | res 1.1413 (ha 8 candles) | 0.01247 | 0.0052% | B/compra@1.1380 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-11 22:06 | UNI-USDT-SWAP | 7.7510 | 7.7830/7.7040 | 7.7650 | res 7.8900 (ha 7 candles) | 0.09693 | 0.0067% | B/compra@7.6800 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-11 22:06 | LINK-USDT-SWAP | 13.37 | 13.39/13.32 | 13.34 | res 13.47 (ha 7 candles) | 0.12071 | 0.0025% | B/compra@13.19 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-11 23:06 | BTC-USDT-SWAP | 83631.6 | 83999.9/83417.5 | 83716.0 | — | 309.46 | -0.0009% | — | sem_zona |
| 2026-10-11 23:06 | ETH-USDT-SWAP | 2541.2 | 2550.0/2532.4 | 2535.6 | — | 13.62 | -0.0015% | B/venda@2520.8 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-11 23:06 | SOL-USDT-SWAP | 111.57 | 111.98/110.84 | 111.28 | — | 0.89286 | 0.0072% | B/venda@112.04 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-11 23:06 | XRP-USDT-SWAP | 1.4040 | 1.4127/1.3997 | 1.4096 | res 1.4258 (ha 10 candles) | 0.00944 | 0.0018% | — | sem_zona |
| 2026-10-11 23:06 | DOGE-USDT-SWAP | 0.08661 | 0.08707/0.08627 | 0.08673 | res 0.08715 (ha 4 candles) | 0.00062 | -0.0004% | A/compra@0.08611 (1t/4c) | zona_mapeada_setup_A |
| 2026-10-11 23:06 | ARB-USDT-SWAP | 0.19650 | 0.19870/0.19508 | 0.19941 | — | 0.00282 | 0.0100% | — | invalidado_setup_B |
| 2026-10-11 23:06 | WLD-USDT-SWAP | 0.55100 | 0.55350/0.54770 | 0.56000 | res 0.58590 (ha 9 candles) | 0.01059 | 0.0100% | — | sem_zona |
| 2026-10-11 23:06 | SUI-USDT-SWAP | 1.1157 | 1.1321/1.1076 | 1.1296 | res 1.1413 (ha 9 candles) | 0.01343 | 0.0078% | — | zona_expirada_setup_B |
| 2026-10-11 23:06 | UNI-USDT-SWAP | 7.6790 | 7.7780/7.6330 | 7.7650 | res 7.8900 (ha 8 candles) | 0.10200 | 0.0051% | B/compra@7.6800 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-11 23:06 | LINK-USDT-SWAP | 13.36 | 13.45/13.28 | 13.34 | res 13.47 (ha 8 candles) | 0.12736 | 0.0037% | B/compra@13.19 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-12 00:06 | BTC-USDT-SWAP | 83797.9 | 83987.1/83579.9 | 83716.0 | — | 327.02 | -0.0009% | — | sem_zona |
| 2026-10-12 00:06 | ETH-USDT-SWAP | 2546.4 | 2564.0/2539.3 | 2535.6 | — | 14.95 | -0.0014% | B/venda@2520.8 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-12 00:06 | SOL-USDT-SWAP | 112.00 | 112.31/111.36 | 111.28 | — | 0.92857 | 0.0076% | B/venda@112.04 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-12 00:06 | XRP-USDT-SWAP | 1.4064 | 1.4127/1.4019 | 1.4096 | res 1.4258 (ha 11 candles) | 0.00994 | 0.0036% | — | sem_zona |
| 2026-10-12 00:06 | DOGE-USDT-SWAP | 0.08695 | 0.08736/0.08661 | 0.08673 | res 0.08715 (ha 5 candles) | 0.00065 | -0.0007% | A/compra@0.08611 (1t/5c) | zona_mapeada_setup_A |
| 2026-10-12 00:06 | ARB-USDT-SWAP | 0.19448 | 0.19778/0.19435 | 0.19941 | — | 0.00264 | 0.0100% | B/compra@0.19617 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-12 00:06 | WLD-USDT-SWAP | 0.55440 | 0.55880/0.55050 | 0.56000 | res 0.58590 (ha 10 candles) | 0.01074 | 0.0100% | — | sem_zona |
| 2026-10-12 00:06 | SUI-USDT-SWAP | 1.1173 | 1.1241/1.1111 | 1.1296 | res 1.1324 (ha 3 candles) | 0.01377 | 0.0100% | B/compra@1.1263 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-12 00:06 | UNI-USDT-SWAP | 7.6690 | 7.7390/7.6600 | 7.7650 | res 7.8900 (ha 9 candles) | 0.10457 | 0.0053% | B/compra@7.6800 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-12 00:06 | LINK-USDT-SWAP | 13.36 | 13.44/13.32 | 13.34 | res 13.47 (ha 9 candles) | 0.13086 | 0.0064% | B/compra@13.19 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-12 01:06 | BTC-USDT-SWAP | 83568.8 | 83798.0/83550.1 | 83568.8 | — | 339.34 | -0.0008% | — | sem_zona |
| 2026-10-12 01:06 | ETH-USDT-SWAP | 2545.5 | 2546.4/2540.2 | 2545.5 | — | 14.98 | -0.0003% | B/venda@2520.8 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-12 01:06 | SOL-USDT-SWAP | 111.66 | 112.00/111.53 | 111.66 | — | 0.94429 | 0.0089% | — | confirmado_calibracao_setup_B |
| 2026-10-12 01:06 | XRP-USDT-SWAP | 1.4053 | 1.4067/1.4031 | 1.4053 | res 1.4133 (ha 3 candles) | 0.00992 | 0.0038% | — | sem_zona |
| 2026-10-12 01:06 | DOGE-USDT-SWAP | 0.08682 | 0.08710/0.08675 | 0.08682 | res 0.08715 (ha 6 candles) | 0.00065 | -0.0015% | A/compra@0.08611 (1t/6c) | zona_mapeada_setup_A |
| 2026-10-12 01:06 | ARB-USDT-SWAP | 0.19436 | 0.19451/0.19328 | 0.19436 | — | 0.00258 | 0.0100% | B/compra@0.19617 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-12 01:06 | WLD-USDT-SWAP | 0.55490 | 0.55580/0.54960 | 0.55490 | res 0.58590 (ha 11 candles) | 0.01079 | 0.0100% | — | sem_zona |
| 2026-10-12 01:06 | SUI-USDT-SWAP | 1.1166 | 1.1189/1.1129 | 1.1166 | res 1.1324 (ha 4 candles) | 0.01381 | 0.0100% | B/compra@1.1263 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-12 01:06 | UNI-USDT-SWAP | 7.7250 | 7.7300/7.6430 | 7.7250 | res 7.7830 (ha 3 candles) | 0.10643 | 0.0031% | — | descartado_rr_baixo_setup_B |
| 2026-10-12 01:06 | LINK-USDT-SWAP | 13.35 | 13.37/13.32 | 13.35 | res 13.47 (ha 10 candles) | 0.12757 | 0.0066% | B/compra@13.19 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-12 02:06 | BTC-USDT-SWAP | 84100.1 | 84159.7/83450.8 | 83568.8 | — | 378.74 | -0.0003% | B/venda@84346.8 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-12 02:06 | ETH-USDT-SWAP | 2565.7 | 2568.8/2541.1 | 2545.5 | — | 16.44 | 0.0002% | B/venda@2520.8 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-12 02:06 | SOL-USDT-SWAP | 113.13 | 113.36/111.33 | 111.66 | — | 1.0514 | 0.0100% | — | sem_zona |
| 2026-10-12 02:06 | XRP-USDT-SWAP | 1.4186 | 1.4204/1.4029 | 1.4053 | res 1.4133 (ha 4 candles) | 0.01057 | 0.0049% | A/compra@1.4133 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-12 02:06 | DOGE-USDT-SWAP | 0.08793 | 0.08807/0.08666 | 0.08682 | res 0.08715 (ha 7 candles) | 0.00070 | -0.0011% | A/compra@0.08611 (1t/7c) | zona_mapeada_setup_A |
| 2026-10-12 02:06 | ARB-USDT-SWAP | 0.19699 | 0.19771/0.19366 | 0.19436 | — | 0.00268 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-10-12 02:06 | WLD-USDT-SWAP | 0.55940 | 0.56280/0.55180 | 0.55490 | res 0.58590 (ha 12 candles) | 0.01015 | 0.0100% | — | sem_zona |
| 2026-10-12 02:06 | SUI-USDT-SWAP | 1.1352 | 1.1397/1.1130 | 1.1166 | res 1.1324 (ha 5 candles) | 0.01481 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-10-12 02:06 | UNI-USDT-SWAP | 7.8070 | 7.8150/7.6830 | 7.7250 | res 7.7830 (ha 4 candles) | 0.10921 | 0.0036% | A/compra@7.7830 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-12 02:06 | LINK-USDT-SWAP | 13.46 | 13.48/13.31 | 13.35 | res 13.47 (ha 11 candles) | 0.12721 | 0.0077% | B/compra@13.19 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-12 03:06 | BTC-USDT-SWAP | 83969.5 | 84276.8/83755.6 | 83568.8 | — | 354.21 | 0.0001% | B/venda@84346.8 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-12 03:06 | ETH-USDT-SWAP | 2563.5 | 2571.9/2550.6 | 2545.5 | — | 15.49 | -0.0006% | — | zona_expirada_setup_B |
| 2026-10-12 03:06 | SOL-USDT-SWAP | 112.78 | 113.35/112.26 | 111.66 | — | 0.94500 | 0.0096% | — | sem_zona |
| 2026-10-12 03:06 | XRP-USDT-SWAP | 1.4129 | 1.4207/1.4077 | 1.4053 | res 1.4133 (ha 5 candles) | 0.00952 | 0.0047% | A/compra@1.4133 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-12 03:06 | DOGE-USDT-SWAP | 0.08761 | 0.08810/0.08726 | 0.08682 | res 0.08715 (ha 8 candles) | 0.00065 | -0.0006% | — | zona_expirada_setup_A |
| 2026-10-12 03:06 | ARB-USDT-SWAP | 0.19662 | 0.19859/0.19600 | 0.19436 | — | 0.00262 | 0.0100% | B/compra@0.19834 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-12 03:06 | WLD-USDT-SWAP | 0.55370 | 0.56080/0.55210 | 0.55490 | res 0.58590 (ha 13 candles) | 0.00927 | 0.0100% | B/compra@0.55290 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-12 03:06 | SUI-USDT-SWAP | 1.1268 | 1.1379/1.1239 | 1.1166 | res 1.1324 (ha 6 candles) | 0.01356 | 0.0069% | — | sem_zona |
| 2026-10-12 03:06 | UNI-USDT-SWAP | 7.7380 | 7.8320/7.7200 | 7.7250 | res 7.7830 (ha 5 candles) | 0.10471 | -0.0005% | — | invalidado_setup_A |
| 2026-10-12 03:06 | LINK-USDT-SWAP | 13.42 | 13.49/13.34 | 13.35 | res 13.47 (ha 12 candles) | 0.11693 | 0.0050% | — | zona_expirada_setup_B |
| 2026-10-12 04:06 | BTC-USDT-SWAP | 84182.0 | 84348.2/83720.0 | 83568.8 | — | 376.01 | 0.0010% | B/venda@84346.8 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-12 04:06 | ETH-USDT-SWAP | 2569.9 | 2576.8/2552.7 | 2545.5 | — | 15.38 | -0.0012% | — | sem_zona |
| 2026-10-12 04:06 | SOL-USDT-SWAP | 112.60 | 112.87/112.05 | 111.66 | — | 0.92429 | 0.0088% | — | sem_zona |
| 2026-10-12 04:06 | XRP-USDT-SWAP | 1.4137 | 1.4180/1.4056 | 1.4053 | res 1.4133 (ha 6 candles) | 0.00975 | 0.0048% | — | descartado_rr_baixo_setup_A |
| 2026-10-12 04:06 | DOGE-USDT-SWAP | 0.08754 | 0.08783/0.08710 | 0.08682 | res 0.08715 (ha 9 candles) | 0.00065 | 0.0002% | A/compra@0.08715 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-12 04:06 | ARB-USDT-SWAP | 0.19472 | 0.19670/0.19438 | 0.19436 | — | 0.00258 | 0.0100% | B/compra@0.19834 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-12 04:06 | WLD-USDT-SWAP | 0.54920 | 0.55400/0.54650 | 0.55490 | res 0.58590 (ha 14 candles) | 0.00881 | 0.0100% | — | invalidado_setup_B |
| 2026-10-12 04:06 | SUI-USDT-SWAP | 1.1306 | 1.1331/1.1199 | 1.1166 | res 1.1324 (ha 7 candles) | 0.01352 | 0.0033% | B/compra@1.1380 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-12 04:06 | UNI-USDT-SWAP | 7.6870 | 7.7470/7.6550 | 7.7250 | res 7.7830 (ha 6 candles) | 0.09700 | -0.0019% | B/compra@7.6800 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-12 04:06 | LINK-USDT-SWAP | 13.41 | 13.46/13.37 | 13.35 | res 13.47 (ha 13 candles) | 0.11521 | 0.0028% | — | sem_zona |
| 2026-10-12 05:06 | BTC-USDT-SWAP | 83962.2 | 84311.9/83929.6 | 83962.2 | — | 370.28 | 0.0026% | — | descartado_rr_baixo_setup_B |
| 2026-10-12 05:06 | ETH-USDT-SWAP | 2563.3 | 2578.4/2561.5 | 2563.3 | — | 15.45 | 0.0001% | — | sem_zona |
| 2026-10-12 05:06 | SOL-USDT-SWAP | 112.54 | 113.08/112.51 | 112.54 | — | 0.89000 | 0.0087% | — | sem_zona |
| 2026-10-12 05:06 | XRP-USDT-SWAP | 1.4119 | 1.4172/1.4111 | 1.4119 | res 1.4133 (ha 7 candles) | 0.00949 | 0.0036% | — | sem_zona |
| 2026-10-12 05:06 | DOGE-USDT-SWAP | 0.08779 | 0.08792/0.08742 | 0.08779 | res 0.08715 (ha 10 candles) | 0.00063 | 0.0030% | A/compra@0.08715 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-12 05:06 | ARB-USDT-SWAP | 0.19427 | 0.19527/0.19406 | 0.19427 | — | 0.00249 | 0.0099% | B/compra@0.19834 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-12 05:06 | WLD-USDT-SWAP | 0.55240 | 0.55310/0.54660 | 0.55240 | res 0.56280 (ha 3 candles) | 0.00863 | 0.0100% | — | sem_zona |
| 2026-10-12 05:06 | SUI-USDT-SWAP | 1.1286 | 1.1336/1.1276 | 1.1286 | res 1.1397 (ha 3 candles) | 0.01336 | 0.0017% | B/compra@1.1380 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-12 05:06 | UNI-USDT-SWAP | 7.6850 | 7.7230/7.6750 | 7.6850 | res 7.7830 (ha 7 candles) | 0.09500 | -0.0048% | B/compra@7.6800 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-12 05:06 | LINK-USDT-SWAP | 13.47 | 13.50/13.40 | 13.47 | res 13.47 (ha 14 candles) | 0.11171 | 0.0001% | B/compra@13.52 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-12 06:06 | BTC-USDT-SWAP | 83470.6 | 83962.1/83470.6 | 83962.2 | — | 380.11 | 0.0038% | B/venda@83499.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-12 06:06 | ETH-USDT-SWAP | 2551.4 | 2563.6/2550.7 | 2563.3 | — | 15.35 | 0.0019% | — | sem_zona |
| 2026-10-12 06:06 | SOL-USDT-SWAP | 111.68 | 112.57/111.63 | 112.54 | — | 0.87286 | 0.0098% | — | sem_zona |
| 2026-10-12 06:06 | XRP-USDT-SWAP | 1.4052 | 1.4119/1.4049 | 1.4119 | res 1.4207 (ha 3 candles) | 0.00916 | 0.0032% | — | sem_zona |
| 2026-10-12 06:06 | DOGE-USDT-SWAP | 0.08722 | 0.08780/0.08718 | 0.08779 | res 0.08810 (ha 3 candles) | 0.00063 | 0.0047% | A/compra@0.08715 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-12 06:06 | ARB-USDT-SWAP | 0.19428 | 0.19436/0.19283 | 0.19427 | — | 0.00243 | 0.0097% | B/compra@0.19834 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-12 06:06 | WLD-USDT-SWAP | 0.54920 | 0.55280/0.54690 | 0.55240 | res 0.56280 (ha 4 candles) | 0.00845 | 0.0100% | — | sem_zona |
| 2026-10-12 06:06 | SUI-USDT-SWAP | 1.1205 | 1.1287/1.1174 | 1.1286 | res 1.1397 (ha 4 candles) | 0.01300 | -0.0007% | B/compra@1.1380 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-12 06:06 | UNI-USDT-SWAP | 7.6490 | 7.6940/7.6160 | 7.6850 | res 7.8320 (ha 3 candles) | 0.09129 | -0.0045% | — | invalidado_setup_B |
| 2026-10-12 06:06 | LINK-USDT-SWAP | 13.35 | 13.47/13.33 | 13.47 | res 13.47 (ha 15 candles) | 0.10943 | -0.0013% | B/compra@13.52 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-12 07:06 | BTC-USDT-SWAP | 83521.7 | 83617.4/83275.0 | 83962.2 | — | 396.44 | 0.0060% | B/venda@83499.0 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-12 07:06 | ETH-USDT-SWAP | 2559.2 | 2559.2/2547.3 | 2563.3 | — | 15.80 | 0.0026% | — | sem_zona |
| 2026-10-12 07:06 | SOL-USDT-SWAP | 111.73 | 111.92/111.23 | 112.54 | — | 0.89571 | 0.0100% | — | sem_zona |
| 2026-10-12 07:06 | XRP-USDT-SWAP | 1.4053 | 1.4087/1.3997 | 1.4119 | res 1.4207 (ha 4 candles) | 0.00959 | 0.0018% | — | sem_zona |
| 2026-10-12 07:06 | DOGE-USDT-SWAP | 0.08715 | 0.08740/0.08674 | 0.08779 | res 0.08810 (ha 4 candles) | 0.00065 | 0.0062% | A/compra@0.08715 (2t/0c) | zona_mapeada_setup_A |
| 2026-10-12 07:06 | ARB-USDT-SWAP | 0.19458 | 0.19506/0.19351 | 0.19427 | — | 0.00238 | 0.0088% | B/compra@0.19834 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-12 07:06 | WLD-USDT-SWAP | 0.54970 | 0.55110/0.54620 | 0.55240 | res 0.56280 (ha 5 candles) | 0.00811 | 0.0100% | — | sem_zona |
| 2026-10-12 07:06 | SUI-USDT-SWAP | 1.1194 | 1.1249/1.1113 | 1.1286 | res 1.1397 (ha 5 candles) | 0.01362 | -0.0009% | B/compra@1.1380 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-12 07:06 | UNI-USDT-SWAP | 7.6130 | 7.6700/7.5580 | 7.6850 | res 7.8320 (ha 4 candles) | 0.09600 | -0.0008% | — | sem_zona |
| 2026-10-12 07:06 | LINK-USDT-SWAP | 13.37 | 13.37/13.29 | 13.47 | res 13.47 (ha 16 candles) | 0.11279 | -0.0013% | B/compra@13.52 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-12 08:06 | BTC-USDT-SWAP | 83470.0 | 83585.2/83400.0 | 83962.2 | — | 399.98 | 0.0069% | — | descartado_rr_baixo_setup_B |
| 2026-10-12 08:06 | ETH-USDT-SWAP | 2554.6 | 2559.6/2552.3 | 2563.3 | — | 15.86 | 0.0009% | — | sem_zona |
| 2026-10-12 08:06 | SOL-USDT-SWAP | 111.57 | 111.92/111.39 | 112.54 | — | 0.89786 | 0.0095% | — | sem_zona |
| 2026-10-12 08:06 | XRP-USDT-SWAP | 1.4044 | 1.4074/1.4003 | 1.4119 | res 1.4207 (ha 5 candles) | 0.00957 | 0.0010% | — | sem_zona |
| 2026-10-12 08:06 | DOGE-USDT-SWAP | 0.08729 | 0.08757/0.08686 | 0.08779 | res 0.08810 (ha 5 candles) | 0.00068 | 0.0074% | — | descartado_rr_baixo_setup_A |
| 2026-10-12 08:06 | ARB-USDT-SWAP | 0.19496 | 0.19618/0.19381 | 0.19427 | — | 0.00242 | 0.0060% | B/compra@0.19834 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-12 08:06 | WLD-USDT-SWAP | 0.54680 | 0.54970/0.54420 | 0.55240 | res 0.56280 (ha 6 candles) | 0.00793 | 0.0100% | — | sem_zona |
| 2026-10-12 08:06 | SUI-USDT-SWAP | 1.1168 | 1.1210/1.1136 | 1.1286 | res 1.1397 (ha 6 candles) | 0.01354 | -0.0006% | B/compra@1.1380 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-12 08:06 | UNI-USDT-SWAP | 7.6270 | 7.6460/7.5770 | 7.6850 | res 7.8320 (ha 5 candles) | 0.09771 | 0.0020% | — | sem_zona |
| 2026-10-12 08:06 | LINK-USDT-SWAP | 13.43 | 13.44/13.32 | 13.47 | res 13.50 (ha 3 candles) | 0.11550 | -0.0011% | B/compra@13.52 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-12 09:06 | BTC-USDT-SWAP | 83358.4 | 83472.0/83243.1 | 83358.4 | — | 386.27 | 0.0082% | B/compra@83123.1 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-12 09:06 | ETH-USDT-SWAP | 2545.1 | 2555.6/2538.8 | 2545.1 | — | 15.36 | 0.0011% | — | sem_zona |
| 2026-10-12 09:06 | SOL-USDT-SWAP | 110.96 | 111.58/110.59 | 110.96 | — | 0.86214 | 0.0095% | B/venda@110.74 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-12 09:06 | XRP-USDT-SWAP | 1.3983 | 1.4044/1.3941 | 1.3983 | res 1.4207 (ha 6 candles) | 0.00909 | 0.0009% | — | sem_zona |
| 2026-10-12 09:06 | DOGE-USDT-SWAP | 0.08709 | 0.08730/0.08655 | 0.08709 | res 0.08810 (ha 6 candles) | 0.00065 | 0.0088% | — | sem_zona |
| 2026-10-12 09:06 | ARB-USDT-SWAP | 0.19342 | 0.19505/0.19221 | 0.19342 | — | 0.00234 | 0.0049% | B/compra@0.19834 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-12 09:06 | WLD-USDT-SWAP | 0.53960 | 0.54690/0.53550 | 0.53960 | res 0.56280 (ha 7 candles) | 0.00769 | 0.0100% | — | sem_zona |
| 2026-10-12 09:06 | SUI-USDT-SWAP | 1.1028 | 1.1170/1.0968 | 1.1028 | res 1.1397 (ha 7 candles) | 0.01348 | -0.0014% | B/compra@1.1380 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-12 09:06 | UNI-USDT-SWAP | 7.5650 | 7.6300/7.5000 | 7.5650 | res 7.8320 (ha 6 candles) | 0.09600 | 0.0034% | — | sem_zona |
| 2026-10-12 09:06 | LINK-USDT-SWAP | 13.31 | 13.43/13.24 | 13.31 | res 13.50 (ha 4 candles) | 0.11393 | -0.0006% | B/compra@13.52 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-12 10:06 | BTC-USDT-SWAP | 82731.8 | 83367.0/82601.0 | 83358.4 | — | 423.66 | 0.0083% | — | invalidado_setup_B |
| 2026-10-12 10:06 | ETH-USDT-SWAP | 2530.5 | 2545.3/2516.7 | 2545.1 | — | 16.80 | 0.0015% | B/compra@2532.6 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-12 10:06 | SOL-USDT-SWAP | 110.21 | 111.04/109.94 | 110.96 | — | 0.87929 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-10-12 10:06 | XRP-USDT-SWAP | 1.3896 | 1.4023/1.3851 | 1.3983 | res 1.4207 (ha 7 candles) | 0.00977 | 0.0017% | — | sem_zona |
| 2026-10-12 10:06 | DOGE-USDT-SWAP | 0.08600 | 0.08739/0.08556 | 0.08709 | res 0.08810 (ha 7 candles) | 0.00075 | 0.0087% | — | sem_zona |
| 2026-10-12 10:06 | ARB-USDT-SWAP | 0.19152 | 0.19383/0.19025 | 0.19342 | — | 0.00244 | 0.0075% | B/compra@0.19834 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-12 10:06 | WLD-USDT-SWAP | 0.53700 | 0.54150/0.53290 | 0.53960 | res 0.56280 (ha 8 candles) | 0.00789 | 0.0100% | — | sem_zona |
| 2026-10-12 10:06 | SUI-USDT-SWAP | 1.0963 | 1.1082/1.0905 | 1.1028 | res 1.1397 (ha 8 candles) | 0.01376 | -0.0000% | B/compra@1.1380 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-12 10:06 | UNI-USDT-SWAP | 7.5210 | 7.5890/7.4720 | 7.5650 | res 7.8320 (ha 7 candles) | 0.09579 | 0.0059% | — | sem_zona |
| 2026-10-12 10:06 | LINK-USDT-SWAP | 13.19 | 13.33/13.14 | 13.31 | res 13.50 (ha 5 candles) | 0.12143 | 0.0000% | B/compra@13.52 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-12 11:06 | BTC-USDT-SWAP | 82926.9 | 83004.0/82419.0 | 83358.4 | — | 455.32 | 0.0076% | B/compra@82850.8 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-12 11:06 | ETH-USDT-SWAP | 2540.7 | 2544.2/2519.1 | 2545.1 | — | 18.25 | 0.0023% | — | descartado_rr_baixo_setup_B |
| 2026-10-12 11:06 | SOL-USDT-SWAP | 110.42 | 110.68/109.62 | 110.96 | — | 0.93000 | 0.0100% | — | sem_zona |
| 2026-10-12 11:06 | XRP-USDT-SWAP | 1.3904 | 1.3917/1.3809 | 1.3983 | res 1.4207 (ha 8 candles) | 0.01029 | 0.0033% | — | sem_zona |
| 2026-10-12 11:06 | DOGE-USDT-SWAP | 0.08596 | 0.08624/0.08561 | 0.08709 | res 0.08810 (ha 8 candles) | 0.00077 | 0.0091% | — | sem_zona |
| 2026-10-12 11:06 | ARB-USDT-SWAP | 0.19173 | 0.19258/0.19103 | 0.19342 | — | 0.00242 | 0.0085% | — | zona_expirada_setup_B |
| 2026-10-12 11:06 | WLD-USDT-SWAP | 0.53450 | 0.53950/0.53380 | 0.53960 | res 0.56280 (ha 9 candles) | 0.00766 | 0.0100% | — | sem_zona |
| 2026-10-12 11:06 | SUI-USDT-SWAP | 1.1024 | 1.1046/1.0912 | 1.1028 | res 1.1397 (ha 9 candles) | 0.01406 | 0.0022% | B/compra@1.1380 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-12 11:06 | UNI-USDT-SWAP | 7.5410 | 7.5750/7.5090 | 7.5650 | res 7.8320 (ha 8 candles) | 0.09614 | 0.0067% | — | sem_zona |
| 2026-10-12 11:06 | LINK-USDT-SWAP | 13.17 | 13.21/13.09 | 13.31 | res 13.50 (ha 6 candles) | 0.12736 | 0.0001% | B/compra@13.52 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-12 12:06 | BTC-USDT-SWAP | 82548.0 | 83085.0/82348.2 | 83358.4 | — | 486.71 | 0.0053% | — | invalidado_setup_B |
| 2026-10-12 12:06 | ETH-USDT-SWAP | 2522.7 | 2543.6/2512.0 | 2545.1 | — | 19.49 | 0.0012% | B/venda@2518.3 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-12 12:06 | SOL-USDT-SWAP | 108.71 | 110.57/108.28 | 110.96 | — | 1.0479 | 0.0071% | B/compra@108.37 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-12 12:06 | XRP-USDT-SWAP | 1.3727 | 1.3944/1.3684 | 1.3983 | res 1.4207 (ha 9 candles) | 0.01170 | 0.0022% | B/compra@1.3732 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-12 12:06 | DOGE-USDT-SWAP | 0.08496 | 0.08615/0.08453 | 0.08709 | res 0.08810 (ha 9 candles) | 0.00087 | 0.0074% | — | sem_zona |
| 2026-10-12 12:06 | ARB-USDT-SWAP | 0.18775 | 0.19225/0.18667 | 0.19342 | — | 0.00267 | 0.0098% | B/venda@0.18875 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-12 12:06 | WLD-USDT-SWAP | 0.52470 | 0.53600/0.51830 | 0.53960 | res 0.56280 (ha 10 candles) | 0.00812 | 0.0100% | B/compra@0.52640 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-12 12:06 | SUI-USDT-SWAP | 1.0856 | 1.1079/1.0773 | 1.1028 | res 1.1397 (ha 10 candles) | 0.01554 | 0.0018% | — | zona_expirada_setup_B |
| 2026-10-12 12:06 | UNI-USDT-SWAP | 7.4360 | 7.5590/7.3890 | 7.5650 | res 7.8320 (ha 9 candles) | 0.10264 | 0.0041% | — | sem_zona |
| 2026-10-12 12:06 | LINK-USDT-SWAP | 12.97 | 13.20/12.92 | 13.31 | res 13.50 (ha 7 candles) | 0.14150 | 0.0000% | B/compra@13.52 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-12 13:06 | BTC-USDT-SWAP | 82684.4 | 82763.6/82548.0 | 82684.4 | — | 460.51 | 0.0040% | B/compra@82501.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-12 13:06 | ETH-USDT-SWAP | 2528.9 | 2533.0/2522.2 | 2528.9 | — | 19.00 | -0.0004% | — | invalidado_setup_B |
| 2026-10-12 13:06 | SOL-USDT-SWAP | 108.84 | 109.19/108.67 | 108.84 | — | 1.0036 | 0.0031% | B/compra@108.37 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-12 13:06 | XRP-USDT-SWAP | 1.3766 | 1.3793/1.3728 | 1.3766 | res 1.4207 (ha 10 candles) | 0.01124 | 0.0033% | B/compra@1.3732 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-12 13:06 | DOGE-USDT-SWAP | 0.08496 | 0.08525/0.08484 | 0.08496 | res 0.08810 (ha 10 candles) | 0.00084 | 0.0065% | — | sem_zona |
| 2026-10-12 13:06 | ARB-USDT-SWAP | 0.18848 | 0.18984/0.18734 | 0.18848 | — | 0.00260 | 0.0100% | B/venda@0.18875 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-12 13:06 | WLD-USDT-SWAP | 0.52200 | 0.52760/0.52100 | 0.52200 | res 0.56280 (ha 11 candles) | 0.00818 | 0.0100% | — | invalidado_setup_B |
| 2026-10-12 13:06 | SUI-USDT-SWAP | 1.0870 | 1.0910/1.0843 | 1.0870 | res 1.1397 (ha 11 candles) | 0.01427 | 0.0049% | B/compra@1.0967 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-12 13:06 | UNI-USDT-SWAP | 7.4190 | 7.4880/7.4090 | 7.4190 | res 7.8320 (ha 10 candles) | 0.09793 | 0.0096% | — | sem_zona |
| 2026-10-12 13:06 | LINK-USDT-SWAP | 13.02 | 13.05/12.96 | 13.02 | res 13.50 (ha 8 candles) | 0.13529 | 0.0009% | — | zona_expirada_setup_B |
| 2026-10-12 14:06 | BTC-USDT-SWAP | 82471.0 | 82920.9/82446.7 | 82684.4 | — | 465.30 | 0.0024% | B/compra@82501.0 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-12 14:06 | ETH-USDT-SWAP | 2512.9 | 2533.9/2508.9 | 2528.9 | — | 19.02 | 0.0001% | — | sem_zona |
| 2026-10-12 14:06 | SOL-USDT-SWAP | 107.78 | 109.20/107.70 | 108.84 | — | 1.0429 | 0.0009% | — | invalidado_setup_B |
| 2026-10-12 14:06 | XRP-USDT-SWAP | 1.3584 | 1.3824/1.3559 | 1.3766 | res 1.4207 (ha 11 candles) | 0.01236 | 0.0040% | — | invalidado_setup_B |
| 2026-10-12 14:06 | DOGE-USDT-SWAP | 0.08436 | 0.08533/0.08427 | 0.08496 | res 0.08810 (ha 11 candles) | 0.00087 | 0.0060% | B/compra@0.08376 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-12 14:06 | ARB-USDT-SWAP | 0.18464 | 0.18978/0.18412 | 0.18848 | — | 0.00275 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-10-12 14:06 | WLD-USDT-SWAP | 0.51830 | 0.52490/0.51380 | 0.52200 | res 0.56280 (ha 12 candles) | 0.00838 | 0.0100% | — | sem_zona |
| 2026-10-12 14:06 | SUI-USDT-SWAP | 1.0677 | 1.0929/1.0637 | 1.0870 | res 1.1397 (ha 12 candles) | 0.01543 | 0.0072% | B/compra@1.0967 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-12 14:06 | UNI-USDT-SWAP | 7.3440 | 7.4730/7.3290 | 7.4190 | res 7.8320 (ha 11 candles) | 0.10257 | 0.0100% | — | sem_zona |
| 2026-10-12 14:06 | LINK-USDT-SWAP | 12.88 | 13.10/12.86 | 13.02 | res 13.50 (ha 9 candles) | 0.14429 | 0.0004% | — | sem_zona |
| 2026-10-12 15:06 | BTC-USDT-SWAP | 82465.4 | 82609.5/82330.1 | 82684.4 | — | 467.55 | 0.0029% | B/compra@82501.0 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-12 15:06 | ETH-USDT-SWAP | 2511.0 | 2517.9/2502.2 | 2528.9 | — | 19.69 | 0.0014% | — | sem_zona |
| 2026-10-12 15:06 | SOL-USDT-SWAP | 107.74 | 108.09/107.09 | 108.84 | — | 1.0807 | 0.0011% | — | sem_zona |
| 2026-10-12 15:06 | XRP-USDT-SWAP | 1.3619 | 1.3656/1.3562 | 1.3766 | res 1.4207 (ha 12 candles) | 0.01278 | 0.0065% | — | sem_zona |
| 2026-10-12 15:06 | DOGE-USDT-SWAP | 0.08484 | 0.08495/0.08434 | 0.08496 | res 0.08810 (ha 12 candles) | 0.00088 | 0.0051% | B/compra@0.08376 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-12 15:06 | ARB-USDT-SWAP | 0.18523 | 0.18593/0.18373 | 0.18848 | — | 0.00282 | 0.0100% | — | sem_zona |
| 2026-10-12 15:06 | WLD-USDT-SWAP | 0.52140 | 0.52330/0.51800 | 0.52200 | res 0.56280 (ha 13 candles) | 0.00831 | 0.0100% | — | sem_zona |
| 2026-10-12 15:06 | SUI-USDT-SWAP | 1.0698 | 1.0750/1.0647 | 1.0870 | res 1.1397 (ha 13 candles) | 0.01574 | 0.0100% | B/compra@1.0967 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-12 15:06 | UNI-USDT-SWAP | 7.3730 | 7.3950/7.3310 | 7.4190 | res 7.8320 (ha 12 candles) | 0.10093 | 0.0100% | — | sem_zona |
| 2026-10-12 15:06 | LINK-USDT-SWAP | 12.89 | 12.94/12.86 | 13.02 | res 13.50 (ha 10 candles) | 0.14650 | 0.0016% | — | sem_zona |
| 2026-10-12 16:06 | BTC-USDT-SWAP | 82420.0 | 82519.4/82250.0 | 82684.4 | — | 436.16 | 0.0039% | — | zona_expirada_setup_B |
| 2026-10-12 16:06 | ETH-USDT-SWAP | 2513.1 | 2514.0/2507.4 | 2528.9 | — | 18.18 | 0.0028% | — | sem_zona |
| 2026-10-12 16:06 | SOL-USDT-SWAP | 107.52 | 107.85/107.46 | 108.84 | — | 0.96357 | 0.0029% | — | sem_zona |
| 2026-10-12 16:06 | XRP-USDT-SWAP | 1.3590 | 1.3636/1.3560 | 1.3766 | res 1.4207 (ha 13 candles) | 0.01207 | 0.0061% | — | sem_zona |
| 2026-10-12 16:06 | DOGE-USDT-SWAP | 0.08483 | 0.08492/0.08460 | 0.08496 | res 0.08810 (ha 13 candles) | 0.00081 | 0.0044% | B/compra@0.08376 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-12 16:06 | ARB-USDT-SWAP | 0.18580 | 0.18594/0.18488 | 0.18848 | — | 0.00261 | 0.0100% | — | sem_zona |
| 2026-10-12 16:06 | WLD-USDT-SWAP | 0.51650 | 0.52250/0.51560 | 0.52200 | res 0.56280 (ha 14 candles) | 0.00802 | 0.0100% | B/compra@0.51080 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-12 16:06 | SUI-USDT-SWAP | 1.0656 | 1.0716/1.0626 | 1.0870 | res 1.1397 (ha 14 candles) | 0.01447 | 0.0100% | B/compra@1.0967 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-12 16:06 | UNI-USDT-SWAP | 7.3730 | 7.3850/7.3370 | 7.4190 | res 7.8320 (ha 13 candles) | 0.09493 | 0.0100% | — | sem_zona |
| 2026-10-12 16:06 | LINK-USDT-SWAP | 12.89 | 12.91/12.85 | 13.02 | res 13.50 (ha 11 candles) | 0.13907 | 0.0028% | — | sem_zona |
| 2026-10-12 17:06 | BTC-USDT-SWAP | 82823.2 | 82866.0/82307.7 | 82823.2 | res 84348.2 (ha 13 candles) | 438.81 | 0.0039% | B/compra@83123.1 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-12 17:06 | ETH-USDT-SWAP | 2520.3 | 2521.9/2506.7 | 2520.3 | res 2578.4 (ha 12 candles) | 17.75 | 0.0031% | — | sem_zona |
| 2026-10-12 17:06 | SOL-USDT-SWAP | 108.26 | 108.35/107.39 | 108.26 | res 113.36 (ha 15 candles) | 0.95429 | 0.0048% | — | sem_zona |
| 2026-10-12 17:06 | XRP-USDT-SWAP | 1.3644 | 1.3669/1.3534 | 1.3644 | res 1.4207 (ha 14 candles) | 0.01211 | 0.0047% | — | sem_zona |
| 2026-10-12 17:06 | DOGE-USDT-SWAP | 0.08519 | 0.08523/0.08455 | 0.08519 | res 0.08810 (ha 14 candles) | 0.00080 | 0.0045% | B/compra@0.08376 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-12 17:06 | ARB-USDT-SWAP | 0.18796 | 0.18839/0.18516 | 0.18796 | — | 0.00266 | 0.0100% | B/compra@0.18820 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-12 17:06 | WLD-USDT-SWAP | 0.51750 | 0.51900/0.51260 | 0.51750 | res 0.56280 (ha 15 candles) | 0.00786 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-10-12 17:06 | SUI-USDT-SWAP | 1.0718 | 1.0739/1.0613 | 1.0718 | res 1.1397 (ha 15 candles) | 0.01437 | 0.0100% | B/compra@1.0967 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-12 17:06 | UNI-USDT-SWAP | 7.3950 | 7.4290/7.3470 | 7.3950 | res 7.8320 (ha 14 candles) | 0.09279 | 0.0100% | B/compra@7.4520 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-12 17:06 | LINK-USDT-SWAP | 12.97 | 12.98/12.88 | 12.97 | res 13.50 (ha 12 candles) | 0.13607 | -0.0016% | — | sem_zona |
| 2026-10-12 18:06 | BTC-USDT-SWAP | 83053.5 | 83119.7/82819.3 | 82823.2 | res 84348.2 (ha 14 candles) | 415.39 | 0.0035% | — | descartado_rr_baixo_setup_B |
| 2026-10-12 18:06 | ETH-USDT-SWAP | 2518.0 | 2526.3/2517.8 | 2520.3 | res 2578.4 (ha 13 candles) | 16.64 | 0.0035% | — | sem_zona |
| 2026-10-12 18:06 | SOL-USDT-SWAP | 108.41 | 108.80/108.25 | 108.26 | res 113.36 (ha 16 candles) | 0.93500 | 0.0060% | — | sem_zona |
| 2026-10-12 18:06 | XRP-USDT-SWAP | 1.3664 | 1.3705/1.3639 | 1.3644 | res 1.4207 (ha 15 candles) | 0.01169 | 0.0022% | — | sem_zona |
| 2026-10-12 18:06 | DOGE-USDT-SWAP | 0.08519 | 0.08544/0.08516 | 0.08519 | res 0.08810 (ha 15 candles) | 0.00076 | 0.0046% | B/compra@0.08376 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-12 18:06 | ARB-USDT-SWAP | 0.18794 | 0.18925/0.18761 | 0.18796 | — | 0.00261 | 0.0100% | B/compra@0.18820 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-12 18:06 | WLD-USDT-SWAP | 0.51720 | 0.51990/0.51640 | 0.51750 | res 0.56280 (ha 16 candles) | 0.00757 | 0.0066% | — | sem_zona |
| 2026-10-12 18:06 | SUI-USDT-SWAP | 1.0732 | 1.0781/1.0715 | 1.0718 | res 1.1397 (ha 16 candles) | 0.01390 | 0.0100% | B/compra@1.0967 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-12 18:06 | UNI-USDT-SWAP | 7.3530 | 7.4200/7.3480 | 7.3950 | res 7.8320 (ha 15 candles) | 0.09136 | 0.0100% | B/compra@7.4520 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-12 18:06 | LINK-USDT-SWAP | 13.03 | 13.10/12.97 | 12.97 | res 13.50 (ha 13 candles) | 0.13871 | -0.0044% | — | sem_zona |
| 2026-10-12 19:06 | BTC-USDT-SWAP | 82534.0 | 83075.0/82400.4 | 82823.2 | res 84348.2 (ha 15 candles) | 436.27 | 0.0039% | B/compra@82850.8 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-12 19:06 | ETH-USDT-SWAP | 2489.7 | 2518.0/2481.7 | 2520.3 | res 2578.4 (ha 14 candles) | 18.03 | 0.0037% | — | sem_zona |
| 2026-10-12 19:06 | SOL-USDT-SWAP | 107.16 | 108.42/106.25 | 108.26 | res 113.36 (ha 17 candles) | 1.0493 | 0.0077% | — | sem_zona |
| 2026-10-12 19:06 | XRP-USDT-SWAP | 1.3514 | 1.3669/1.3414 | 1.3644 | res 1.4207 (ha 16 candles) | 0.01308 | -0.0004% | — | sem_zona |
| 2026-10-12 19:06 | DOGE-USDT-SWAP | 0.08372 | 0.08525/0.08275 | 0.08519 | res 0.08810 (ha 16 candles) | 0.00091 | 0.0042% | B/compra@0.08376 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-12 19:06 | ARB-USDT-SWAP | 0.18356 | 0.18813/0.18168 | 0.18796 | — | 0.00298 | 0.0093% | — | invalidado_setup_B |
| 2026-10-12 19:06 | WLD-USDT-SWAP | 0.50880 | 0.51780/0.50380 | 0.51750 | res 0.56280 (ha 17 candles) | 0.00811 | 0.0042% | B/compra@0.50770 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-12 19:06 | SUI-USDT-SWAP | 1.0508 | 1.0741/1.0420 | 1.0718 | res 1.1397 (ha 17 candles) | 0.01576 | 0.0100% | B/compra@1.0967 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-12 19:06 | UNI-USDT-SWAP | 7.2090 | 7.3590/7.1720 | 7.3950 | res 7.8320 (ha 16 candles) | 0.10129 | 0.0100% | B/compra@7.4520 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-12 19:06 | LINK-USDT-SWAP | 12.83 | 13.04/12.75 | 12.97 | res 13.50 (ha 14 candles) | 0.15221 | -0.0065% | — | sem_zona |
| 2026-10-12 20:06 | BTC-USDT-SWAP | 82111.1 | 82738.0/82038.1 | 82823.2 | res 84348.2 (ha 16 candles) | 451.15 | 0.0031% | B/compra@82850.8 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-12 20:06 | ETH-USDT-SWAP | 2465.1 | 2497.2/2463.3 | 2520.3 | res 2578.4 (ha 15 candles) | 19.53 | 0.0031% | B/compra@2473.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-12 20:06 | SOL-USDT-SWAP | 106.33 | 107.50/106.20 | 108.26 | res 113.36 (ha 18 candles) | 1.0750 | 0.0082% | B/compra@105.61 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-12 20:06 | XRP-USDT-SWAP | 1.3494 | 1.3566/1.3482 | 1.3644 | res 1.4207 (ha 17 candles) | 0.01318 | -0.0018% | — | sem_zona |
| 2026-10-12 20:06 | DOGE-USDT-SWAP | 0.08343 | 0.08419/0.08335 | 0.08519 | res 0.08810 (ha 17 candles) | 0.00092 | 0.0030% | — | invalidado_setup_B |
| 2026-10-12 20:06 | ARB-USDT-SWAP | 0.18224 | 0.18550/0.18212 | 0.18796 | — | 0.00311 | 0.0084% | — | sem_zona |
| 2026-10-12 20:06 | WLD-USDT-SWAP | 0.50480 | 0.51090/0.50410 | 0.51750 | res 0.56280 (ha 18 candles) | 0.00817 | 0.0057% | — | invalidado_setup_B |
| 2026-10-12 20:06 | SUI-USDT-SWAP | 1.0446 | 1.0562/1.0436 | 1.0718 | res 1.1397 (ha 18 candles) | 0.01586 | 0.0100% | B/compra@1.0967 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-12 20:06 | UNI-USDT-SWAP | 7.1480 | 7.2690/7.1410 | 7.3950 | res 7.8320 (ha 17 candles) | 0.10486 | 0.0100% | B/compra@7.4520 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-12 20:06 | LINK-USDT-SWAP | 12.79 | 12.90/12.77 | 12.97 | res 13.50 (ha 15 candles) | 0.15071 | -0.0074% | — | sem_zona |
| 2026-10-12 21:06 | BTC-USDT-SWAP | 81808.0 | 82225.0/81710.6 | 81808.0 | res 83119.7 (ha 3 candles) | 463.44 | 0.0024% | B/compra@82850.8 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-12 21:06 | ETH-USDT-SWAP | 2446.0 | 2470.1/2441.7 | 2446.0 | res 2526.3 (ha 3 candles) | 20.71 | 0.0015% | — | invalidado_setup_B |
| 2026-10-12 21:06 | SOL-USDT-SWAP | 105.71 | 106.58/105.33 | 105.71 | res 108.80 (ha 3 candles) | 1.1150 | 0.0096% | B/compra@105.61 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-12 21:06 | XRP-USDT-SWAP | 1.3413 | 1.3517/1.3368 | 1.3413 | res 1.3705 (ha 3 candles) | 0.01360 | -0.0026% | — | sem_zona |
| 2026-10-12 21:06 | DOGE-USDT-SWAP | 0.08220 | 0.08359/0.08201 | 0.08220 | res 0.08544 (ha 3 candles) | 0.00099 | 0.0059% | — | sem_zona |
| 2026-10-12 21:06 | ARB-USDT-SWAP | 0.17961 | 0.18278/0.17943 | 0.17961 | — | 0.00324 | 0.0096% | B/compra@0.17900 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-12 21:06 | WLD-USDT-SWAP | 0.49830 | 0.50670/0.49510 | 0.49830 | res 0.56280 (ha 19 candles) | 0.00865 | 0.0076% | — | sem_zona |
| 2026-10-12 21:06 | SUI-USDT-SWAP | 1.0282 | 1.0474/1.0237 | 1.0282 | res 1.0781 (ha 3 candles) | 0.01658 | 0.0100% | — | zona_expirada_setup_B |
| 2026-10-12 21:06 | UNI-USDT-SWAP | 6.9690 | 7.1720/6.9300 | 6.9690 | res 7.8320 (ha 18 candles) | 0.11414 | 0.0100% | B/compra@7.4520 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-12 21:06 | LINK-USDT-SWAP | 12.62 | 12.82/12.61 | 12.62 | res 13.10 (ha 3 candles) | 0.15979 | -0.0078% | — | sem_zona |
| 2026-10-12 22:05 | BTC-USDT-SWAP | 81403.4 | 81915.0/80961.3 | 81808.0 | res 83119.7 (ha 4 candles) | 518.33 | 0.0024% | B/compra@82850.8 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-12 22:05 | ETH-USDT-SWAP | 2420.8 | 2449.9/2407.5 | 2446.0 | res 2526.3 (ha 4 candles) | 23.22 | -0.0007% | B/compra@2405.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-12 22:05 | SOL-USDT-SWAP | 102.95 | 105.94/101.58 | 105.71 | res 108.80 (ha 4 candles) | 1.3886 | 0.0076% | — | invalidado_setup_B |
| 2026-10-12 22:05 | XRP-USDT-SWAP | 1.3200 | 1.3443/1.3102 | 1.3413 | res 1.3705 (ha 4 candles) | 0.01553 | -0.0039% | B/compra@1.3176 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-12 22:05 | DOGE-USDT-SWAP | 0.08099 | 0.08234/0.07996 | 0.08220 | res 0.08544 (ha 4 candles) | 0.00111 | 0.0062% | B/compra@0.08092 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-12 22:05 | ARB-USDT-SWAP | 0.17645 | 0.17991/0.17409 | 0.17961 | — | 0.00349 | 0.0094% | — | invalidado_setup_B |
| 2026-10-12 22:05 | WLD-USDT-SWAP | 0.48020 | 0.49950/0.47260 | 0.49830 | res 0.56280 (ha 20 candles) | 0.01018 | 0.0069% | B/compra@0.48010 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-12 22:05 | SUI-USDT-SWAP | 1.0069 | 1.0298/0.99300 | 1.0282 | res 1.0781 (ha 4 candles) | 0.01868 | 0.0100% | B/compra@0.99710 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-12 22:05 | UNI-USDT-SWAP | 6.8220 | 7.0010/6.7370 | 6.9690 | res 7.8320 (ha 19 candles) | 0.12807 | 0.0100% | B/compra@7.4520 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-12 22:05 | LINK-USDT-SWAP | 12.36 | 12.63/12.25 | 12.62 | res 13.10 (ha 4 candles) | 0.17821 | -0.0079% | — | sem_zona |
| 2026-10-12 23:05 | BTC-USDT-SWAP | 82405.2 | 82439.9/81392.8 | 81808.0 | res 83119.7 (ha 5 candles) | 576.77 | 0.0018% | B/compra@82850.8 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-12 23:05 | ETH-USDT-SWAP | 2463.1 | 2465.5/2420.8 | 2446.0 | res 2526.3 (ha 5 candles) | 25.22 | -0.0021% | B/compra@2405.0 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-12 23:05 | SOL-USDT-SWAP | 105.28 | 105.32/102.86 | 105.71 | res 108.80 (ha 5 candles) | 1.4936 | 0.0038% | — | sem_zona |
| 2026-10-12 23:05 | XRP-USDT-SWAP | 1.3528 | 1.3536/1.3196 | 1.3413 | res 1.3705 (ha 5 candles) | 0.01722 | -0.0053% | — | descartado_rr_baixo_setup_B |
| 2026-10-12 23:05 | DOGE-USDT-SWAP | 0.08288 | 0.08288/0.08096 | 0.08220 | res 0.08544 (ha 5 candles) | 0.00119 | 0.0043% | — | descartado_rr_baixo_setup_B |
| 2026-10-12 23:05 | ARB-USDT-SWAP | 0.18244 | 0.18254/0.17622 | 0.17961 | — | 0.00374 | 0.0069% | — | sem_zona |
| 2026-10-12 23:05 | WLD-USDT-SWAP | 0.49780 | 0.49800/0.47960 | 0.49830 | res 0.56280 (ha 21 candles) | 0.01068 | 0.0005% | — | descartado_rr_baixo_setup_B |
| 2026-10-12 23:05 | SUI-USDT-SWAP | 1.0338 | 1.0347/1.0057 | 1.0282 | res 1.0781 (ha 5 candles) | 0.01931 | 0.0086% | B/compra@0.99710 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-12 23:05 | UNI-USDT-SWAP | 7.0530 | 7.0620/6.8200 | 6.9690 | res 7.8320 (ha 20 candles) | 0.13607 | 0.0100% | B/compra@7.4520 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-12 23:05 | LINK-USDT-SWAP | 12.68 | 12.70/12.36 | 12.62 | res 13.10 (ha 5 candles) | 0.18936 | -0.0070% | — | sem_zona |
| 2026-10-13 00:05 | BTC-USDT-SWAP | 82890.8 | 83075.0/82383.3 | 81808.0 | res 83119.7 (ha 6 candles) | 571.46 | 0.0025% | — | descartado_rr_baixo_setup_B |
| 2026-10-13 00:05 | ETH-USDT-SWAP | 2490.0 | 2497.0/2461.6 | 2446.0 | res 2526.3 (ha 6 candles) | 25.69 | -0.0020% | B/compra@2405.0 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-13 00:05 | SOL-USDT-SWAP | 106.66 | 106.99/105.20 | 105.71 | res 108.80 (ha 6 candles) | 1.5429 | 0.0001% | — | sem_zona |
| 2026-10-13 00:05 | XRP-USDT-SWAP | 1.3644 | 1.3677/1.3522 | 1.3413 | res 1.3705 (ha 6 candles) | 0.01710 | -0.0058% | B/compra@1.3732 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-13 00:05 | DOGE-USDT-SWAP | 0.08362 | 0.08384/0.08277 | 0.08220 | res 0.08544 (ha 6 candles) | 0.00114 | 0.0040% | B/compra@0.08376 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-13 00:05 | ARB-USDT-SWAP | 0.18435 | 0.18468/0.18219 | 0.17961 | — | 0.00366 | 0.0014% | — | sem_zona |
| 2026-10-13 00:05 | WLD-USDT-SWAP | 0.50800 | 0.51000/0.49700 | 0.49830 | res 0.56280 (ha 22 candles) | 0.01099 | -0.0045% | B/compra@0.50770 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-13 00:05 | SUI-USDT-SWAP | 1.0426 | 1.0446/1.0321 | 1.0282 | res 1.0781 (ha 6 candles) | 0.01894 | 0.0011% | B/compra@0.99710 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-13 00:05 | UNI-USDT-SWAP | 7.1760 | 7.1980/7.0390 | 6.9690 | res 7.8320 (ha 21 candles) | 0.13907 | 0.0087% | B/compra@7.4520 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-13 00:05 | LINK-USDT-SWAP | 12.81 | 12.84/12.65 | 12.62 | res 13.10 (ha 6 candles) | 0.18850 | -0.0021% | B/compra@12.83 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-13 01:05 | BTC-USDT-SWAP | 83299.7 | 83590.3/82747.8 | 83299.7 | res 83119.7 (ha 7 candles) | 589.86 | 0.0042% | A/compra@83119.7 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-13 01:05 | ETH-USDT-SWAP | 2507.8 | 2513.7/2485.3 | 2507.8 | res 2526.3 (ha 7 candles) | 25.93 | -0.0005% | B/compra@2405.0 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-13 01:05 | SOL-USDT-SWAP | 107.41 | 107.92/106.38 | 107.41 | res 108.80 (ha 7 candles) | 1.5771 | -0.0030% | B/compra@108.37 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-13 01:05 | XRP-USDT-SWAP | 1.3673 | 1.3747/1.3595 | 1.3673 | res 1.3705 (ha 7 candles) | 0.01741 | -0.0074% | — | invalidado_setup_B |
| 2026-10-13 01:05 | DOGE-USDT-SWAP | 0.08437 | 0.08467/0.08346 | 0.08437 | res 0.08544 (ha 7 candles) | 0.00118 | 0.0042% | — | descartado_rr_baixo_setup_B |
| 2026-10-13 01:05 | ARB-USDT-SWAP | 0.18618 | 0.18703/0.18412 | 0.18618 | — | 0.00376 | -0.0036% | B/venda@0.18875 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-13 01:05 | WLD-USDT-SWAP | 0.51590 | 0.52020/0.50650 | 0.51590 | res 0.56280 (ha 23 candles) | 0.01156 | -0.0093% | — | descartado_rr_baixo_setup_B |
| 2026-10-13 01:05 | SUI-USDT-SWAP | 1.0495 | 1.0560/1.0401 | 1.0495 | res 1.0781 (ha 7 candles) | 0.01911 | -0.0046% | B/compra@0.99710 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-13 01:05 | UNI-USDT-SWAP | 7.2850 | 7.2980/7.1590 | 7.2850 | res 7.8320 (ha 22 candles) | 0.14429 | 0.0022% | — | zona_expirada_setup_B |
| 2026-10-13 01:05 | LINK-USDT-SWAP | 12.94 | 12.97/12.79 | 12.94 | res 13.10 (ha 7 candles) | 0.19300 | 0.0037% | — | descartado_rr_baixo_setup_B |
| 2026-10-13 02:05 | BTC-USDT-SWAP | 83420.3 | 83538.3/83213.4 | 83299.7 | res 83119.7 (ha 8 candles) | 560.44 | 0.0053% | — | descartado_rr_baixo_setup_A |
| 2026-10-13 02:05 | ETH-USDT-SWAP | 2516.7 | 2520.0/2505.7 | 2507.8 | res 2526.3 (ha 8 candles) | 24.69 | 0.0006% | B/compra@2405.0 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-13 02:05 | SOL-USDT-SWAP | 108.02 | 108.24/107.32 | 107.41 | res 108.80 (ha 8 candles) | 1.4793 | -0.0039% | — | descartado_rr_baixo_setup_B |
| 2026-10-13 02:05 | XRP-USDT-SWAP | 1.3679 | 1.3695/1.3641 | 1.3673 | res 1.3705 (ha 8 candles) | 0.01594 | -0.0068% | — | sem_zona |
| 2026-10-13 02:05 | DOGE-USDT-SWAP | 0.08461 | 0.08473/0.08427 | 0.08437 | res 0.08544 (ha 8 candles) | 0.00109 | 0.0066% | B/compra@0.08477 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-13 02:05 | ARB-USDT-SWAP | 0.18706 | 0.18754/0.18610 | 0.18618 | — | 0.00346 | -0.0042% | B/venda@0.18875 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-13 02:05 | WLD-USDT-SWAP | 0.52150 | 0.52380/0.51540 | 0.51590 | res 0.56280 (ha 24 candles) | 0.01090 | -0.0090% | B/compra@0.52640 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-13 02:05 | SUI-USDT-SWAP | 1.0617 | 1.0636/1.0487 | 1.0495 | res 1.0781 (ha 8 candles) | 0.01799 | -0.0069% | B/compra@0.99710 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-13 02:05 | UNI-USDT-SWAP | 7.3580 | 7.3710/7.2840 | 7.2850 | res 7.8320 (ha 23 candles) | 0.13836 | -0.0011% | — | sem_zona |
| 2026-10-13 02:05 | LINK-USDT-SWAP | 13.01 | 13.02/12.91 | 12.94 | res 13.10 (ha 8 candles) | 0.18157 | 0.0078% | — | sem_zona |
| 2026-10-13 03:05 | BTC-USDT-SWAP | 83641.3 | 83888.0/83347.6 | 83299.7 | res 83119.7 (ha 9 candles) | 583.64 | 0.0057% | B/compra@83826.4 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-13 03:05 | ETH-USDT-SWAP | 2530.4 | 2537.8/2511.9 | 2507.8 | res 2526.3 (ha 9 candles) | 25.77 | 0.0011% | B/compra@2405.0 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-13 03:05 | SOL-USDT-SWAP | 108.41 | 108.81/107.87 | 107.41 | res 108.80 (ha 9 candles) | 1.5093 | -0.0039% | B/compra@108.89 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-13 03:05 | XRP-USDT-SWAP | 1.3752 | 1.3760/1.3664 | 1.3673 | res 1.3705 (ha 9 candles) | 0.01616 | -0.0052% | B/compra@1.3866 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-13 03:05 | DOGE-USDT-SWAP | 0.08494 | 0.08511/0.08442 | 0.08437 | res 0.08544 (ha 9 candles) | 0.00111 | 0.0092% | — | descartado_rr_baixo_setup_B |
| 2026-10-13 03:05 | ARB-USDT-SWAP | 0.18907 | 0.18938/0.18691 | 0.18618 | — | 0.00346 | -0.0022% | B/venda@0.18875 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-13 03:05 | WLD-USDT-SWAP | 0.52260 | 0.52460/0.51730 | 0.51590 | res 0.56280 (ha 25 candles) | 0.01095 | -0.0061% | — | invalidado_setup_B |
| 2026-10-13 03:05 | SUI-USDT-SWAP | 1.0729 | 1.0756/1.0598 | 1.0495 | res 1.0781 (ha 9 candles) | 0.01864 | -0.0076% | B/compra@0.99710 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-13 03:05 | UNI-USDT-SWAP | 7.4360 | 7.4570/7.3390 | 7.2850 | res 7.8320 (ha 24 candles) | 0.14114 | -0.0044% | — | sem_zona |
| 2026-10-13 03:05 | LINK-USDT-SWAP | 13.17 | 13.19/12.98 | 12.94 | res 13.10 (ha 9 candles) | 0.18979 | 0.0088% | A/compra@13.10 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-13 04:05 | BTC-USDT-SWAP | 83733.6 | 83769.0/83529.4 | 83299.7 | res 83119.7 (ha 10 candles) | 566.88 | 0.0053% | — | descartado_rr_baixo_setup_B |
| 2026-10-13 04:05 | ETH-USDT-SWAP | 2533.1 | 2536.0/2525.4 | 2507.8 | res 2526.3 (ha 10 candles) | 24.73 | 0.0027% | B/compra@2405.0 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-13 04:05 | SOL-USDT-SWAP | 108.58 | 108.73/108.05 | 107.41 | res 108.80 (ha 10 candles) | 1.4507 | -0.0022% | — | descartado_rr_baixo_setup_B |
| 2026-10-13 04:05 | XRP-USDT-SWAP | 1.3770 | 1.3780/1.3715 | 1.3673 | res 1.3705 (ha 10 candles) | 0.01473 | -0.0026% | B/compra@1.3866 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-13 04:05 | DOGE-USDT-SWAP | 0.08506 | 0.08511/0.08460 | 0.08437 | res 0.08544 (ha 10 candles) | 0.00108 | 0.0100% | — | sem_zona |
| 2026-10-13 04:05 | ARB-USDT-SWAP | 0.19015 | 0.19060/0.18818 | 0.18618 | — | 0.00323 | 0.0004% | — | invalidado_setup_B |
| 2026-10-13 04:05 | WLD-USDT-SWAP | 0.52350 | 0.52390/0.51940 | 0.51590 | res 0.56280 (ha 26 candles) | 0.01048 | -0.0039% | — | sem_zona |
| 2026-10-13 04:05 | SUI-USDT-SWAP | 1.0732 | 1.0759/1.0681 | 1.0495 | res 1.0781 (ha 10 candles) | 0.01711 | -0.0063% | B/compra@0.99710 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-13 04:05 | UNI-USDT-SWAP | 7.4560 | 7.4980/7.3770 | 7.2850 | res 7.8320 (ha 25 candles) | 0.13950 | -0.0032% | — | sem_zona |
| 2026-10-13 04:05 | LINK-USDT-SWAP | 13.08 | 13.19/13.07 | 12.94 | res 13.10 (ha 10 candles) | 0.18107 | 0.0094% | A/compra@13.10 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-13 05:05 | BTC-USDT-SWAP | 83820.0 | 84037.5/83608.2 | 83820.0 | res 83119.7 (ha 11 candles) | 577.59 | 0.0039% | A/compra@83119.7 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-13 05:05 | ETH-USDT-SWAP | 2527.9 | 2537.5/2523.8 | 2527.9 | res 2526.3 (ha 11 candles) | 24.59 | 0.0027% | B/compra@2405.0 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-13 05:05 | SOL-USDT-SWAP | 108.52 | 109.05/107.92 | 108.52 | res 108.80 (ha 11 candles) | 1.4600 | -0.0003% | B/compra@108.37 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-13 05:05 | XRP-USDT-SWAP | 1.3771 | 1.3804/1.3715 | 1.3771 | res 1.3705 (ha 11 candles) | 0.01469 | -0.0005% | B/compra@1.3866 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-13 05:05 | DOGE-USDT-SWAP | 0.08491 | 0.08522/0.08460 | 0.08491 | res 0.08544 (ha 11 candles) | 0.00108 | 0.0100% | — | sem_zona |
| 2026-10-13 05:05 | ARB-USDT-SWAP | 0.18902 | 0.19033/0.18818 | 0.18902 | — | 0.00322 | 0.0034% | B/compra@0.18820 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-13 05:05 | WLD-USDT-SWAP | 0.51880 | 0.52360/0.51630 | 0.51880 | res 0.56280 (ha 27 candles) | 0.01062 | -0.0004% | — | sem_zona |
| 2026-10-13 05:05 | SUI-USDT-SWAP | 1.0702 | 1.0777/1.0645 | 1.0702 | res 1.0781 (ha 11 candles) | 0.01732 | -0.0048% | B/compra@0.99710 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-13 05:05 | UNI-USDT-SWAP | 7.4750 | 7.5290/7.4000 | 7.4750 | res 7.8320 (ha 26 candles) | 0.14414 | -0.0020% | — | sem_zona |
| 2026-10-13 05:05 | LINK-USDT-SWAP | 13.06 | 13.10/12.97 | 13.06 | res 13.10 (ha 11 candles) | 0.18450 | 0.0096% | A/compra@13.10 (2t/0c) | zona_mapeada_setup_A |
| 2026-10-13 06:05 | BTC-USDT-SWAP | 83548.0 | 84130.9/83537.9 | 83820.0 | res 83119.7 (ha 12 candles) | 600.70 | 0.0022% | A/compra@83119.7 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-13 06:05 | ETH-USDT-SWAP | 2516.9 | 2536.6/2516.9 | 2527.9 | res 2537.8 (ha 3 candles) | 25.52 | 0.0006% | — | zona_expirada_setup_B |
| 2026-10-13 06:05 | SOL-USDT-SWAP | 107.59 | 108.85/107.53 | 108.52 | res 108.80 (ha 12 candles) | 1.5264 | 0.0001% | — | invalidado_setup_B |
| 2026-10-13 06:05 | XRP-USDT-SWAP | 1.3723 | 1.3816/1.3723 | 1.3771 | res 1.3705 (ha 12 candles) | 0.01481 | -0.0015% | B/compra@1.3866 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-13 06:05 | DOGE-USDT-SWAP | 0.08433 | 0.08517/0.08432 | 0.08491 | res 0.08544 (ha 12 candles) | 0.00111 | 0.0088% | B/compra@0.08376 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-13 06:05 | ARB-USDT-SWAP | 0.18765 | 0.18971/0.18759 | 0.18902 | — | 0.00330 | 0.0070% | B/compra@0.18820 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-13 06:05 | WLD-USDT-SWAP | 0.51440 | 0.52060/0.51430 | 0.51880 | res 0.52460 (ha 3 candles) | 0.01058 | 0.0013% | B/compra@0.50770 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-13 06:05 | SUI-USDT-SWAP | 1.0626 | 1.0764/1.0624 | 1.0702 | res 1.0781 (ha 12 candles) | 0.01768 | -0.0033% | — | zona_expirada_setup_B |
| 2026-10-13 06:05 | UNI-USDT-SWAP | 7.4780 | 7.5230/7.4680 | 7.4750 | res 7.8320 (ha 27 candles) | 0.14464 | -0.0033% | — | sem_zona |
| 2026-10-13 06:05 | LINK-USDT-SWAP | 13.00 | 13.11/12.99 | 13.06 | res 13.10 (ha 12 candles) | 0.18821 | 0.0077% | — | invalidado_setup_A |
| 2026-10-13 07:05 | BTC-USDT-SWAP | 83593.8 | 83699.0/83319.2 | 83820.0 | res 83119.7 (ha 13 candles) | 587.95 | 0.0025% | A/compra@83119.7 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-13 07:05 | ETH-USDT-SWAP | 2513.5 | 2516.9/2503.1 | 2527.9 | res 2537.8 (ha 4 candles) | 25.42 | -0.0002% | B/compra@2496.2 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-13 07:05 | SOL-USDT-SWAP | 106.98 | 107.66/106.72 | 108.52 | res 108.80 (ha 13 candles) | 1.5250 | 0.0006% | — | sem_zona |
| 2026-10-13 07:05 | XRP-USDT-SWAP | 1.3609 | 1.3724/1.3591 | 1.3771 | res 1.3705 (ha 13 candles) | 0.01480 | -0.0020% | B/compra@1.3866 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-13 07:05 | DOGE-USDT-SWAP | 0.08385 | 0.08445/0.08363 | 0.08491 | res 0.08544 (ha 13 candles) | 0.00112 | 0.0064% | B/compra@0.08376 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-13 07:05 | ARB-USDT-SWAP | 0.18595 | 0.18777/0.18507 | 0.18902 | — | 0.00326 | 0.0100% | — | invalidado_setup_B |
| 2026-10-13 07:05 | WLD-USDT-SWAP | 0.50760 | 0.51610/0.50440 | 0.51880 | res 0.52460 (ha 4 candles) | 0.01096 | 0.0059% | B/compra@0.50770 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-13 07:05 | SUI-USDT-SWAP | 1.0510 | 1.0630/1.0475 | 1.0702 | res 1.0781 (ha 13 candles) | 0.01789 | 0.0030% | — | sem_zona |
| 2026-10-13 07:05 | UNI-USDT-SWAP | 7.4240 | 7.4970/7.4030 | 7.4750 | res 7.8320 (ha 28 candles) | 0.14550 | 0.0007% | — | sem_zona |
| 2026-10-13 07:05 | LINK-USDT-SWAP | 12.98 | 13.00/12.89 | 13.06 | res 13.19 (ha 3 candles) | 0.18829 | 0.0054% | — | sem_zona |
| 2026-10-13 08:05 | BTC-USDT-SWAP | 83315.4 | 83632.0/83188.1 | 83820.0 | res 83119.7 (ha 14 candles) | 598.20 | 0.0035% | A/compra@83119.7 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-13 08:05 | ETH-USDT-SWAP | 2497.8 | 2514.6/2489.9 | 2527.9 | res 2537.8 (ha 5 candles) | 26.58 | -0.0012% | B/compra@2496.2 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-13 08:05 | SOL-USDT-SWAP | 106.46 | 107.20/106.13 | 108.52 | res 109.05 (ha 3 candles) | 1.5621 | 0.0019% | B/compra@105.61 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-13 08:05 | XRP-USDT-SWAP | 1.3598 | 1.3659/1.3561 | 1.3771 | res 1.3705 (ha 14 candles) | 0.01503 | -0.0016% | B/compra@1.3866 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-13 08:05 | DOGE-USDT-SWAP | 0.08369 | 0.08405/0.08334 | 0.08491 | res 0.08522 (ha 3 candles) | 0.00115 | 0.0029% | B/compra@0.08376 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-13 08:05 | ARB-USDT-SWAP | 0.18450 | 0.18643/0.18401 | 0.18902 | — | 0.00332 | 0.0100% | — | sem_zona |
| 2026-10-13 08:05 | WLD-USDT-SWAP | 0.50420 | 0.51030/0.50170 | 0.51880 | res 0.52460 (ha 5 candles) | 0.01132 | 0.0089% | — | invalidado_setup_B |
| 2026-10-13 08:05 | SUI-USDT-SWAP | 1.0458 | 1.0539/1.0417 | 1.0702 | res 1.0777 (ha 3 candles) | 0.01829 | 0.0093% | — | sem_zona |
| 2026-10-13 08:05 | UNI-USDT-SWAP | 7.3430 | 7.4370/7.3040 | 7.4750 | res 7.5290 (ha 3 candles) | 0.14986 | 0.0079% | — | sem_zona |
| 2026-10-13 08:05 | LINK-USDT-SWAP | 12.87 | 12.99/12.81 | 13.06 | res 13.19 (ha 4 candles) | 0.19207 | 0.0020% | B/compra@12.83 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-13 09:05 | BTC-USDT-SWAP | 83326.8 | 83737.3/83112.2 | 83326.8 | res 84130.9 (ha 3 candles) | 594.66 | 0.0046% | A/compra@83119.7 (2t/0c) | zona_mapeada_setup_A |
| 2026-10-13 09:05 | ETH-USDT-SWAP | 2499.5 | 2524.5/2487.3 | 2499.5 | res 2537.8 (ha 6 candles) | 26.64 | -0.0011% | B/compra@2496.2 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-13 09:05 | SOL-USDT-SWAP | 106.12 | 107.46/105.57 | 106.12 | res 109.05 (ha 4 candles) | 1.5421 | 0.0016% | B/compra@105.61 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-13 09:05 | XRP-USDT-SWAP | 1.3570 | 1.3680/1.3485 | 1.3570 | res 1.3816 (ha 3 candles) | 0.01460 | -0.0017% | B/compra@1.3866 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-13 09:05 | DOGE-USDT-SWAP | 0.08348 | 0.08435/0.08293 | 0.08348 | res 0.08522 (ha 4 candles) | 0.00108 | -0.0012% | — | invalidado_setup_B |
| 2026-10-13 09:05 | ARB-USDT-SWAP | 0.18292 | 0.18614/0.18186 | 0.18292 | — | 0.00316 | 0.0100% | — | sem_zona |
| 2026-10-13 09:05 | WLD-USDT-SWAP | 0.50220 | 0.50990/0.49680 | 0.50220 | res 0.52460 (ha 6 candles) | 0.01126 | 0.0100% | — | sem_zona |
| 2026-10-13 09:05 | SUI-USDT-SWAP | 1.0349 | 1.0494/1.0287 | 1.0349 | res 1.0777 (ha 4 candles) | 0.01747 | 0.0100% | — | sem_zona |
| 2026-10-13 09:05 | UNI-USDT-SWAP | 7.2700 | 7.3990/7.2350 | 7.2700 | res 7.5290 (ha 4 candles) | 0.14821 | 0.0100% | B/compra@7.2270 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-13 09:05 | LINK-USDT-SWAP | 12.83 | 12.95/12.71 | 12.83 | res 13.19 (ha 5 candles) | 0.18836 | -0.0024% | B/compra@12.83 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-13 10:05 | BTC-USDT-SWAP | 83323.9 | 83453.6/83049.4 | 83326.8 | res 84130.9 (ha 4 candles) | 573.54 | 0.0054% | — | zona_expirada_setup_A |
| 2026-10-13 10:05 | ETH-USDT-SWAP | 2504.4 | 2506.1/2492.1 | 2499.5 | res 2537.8 (ha 7 candles) | 25.21 | -0.0014% | — | descartado_rr_baixo_setup_B |
| 2026-10-13 10:05 | SOL-USDT-SWAP | 106.61 | 106.72/105.65 | 106.12 | res 109.05 (ha 5 candles) | 1.5257 | 0.0005% | — | descartado_rr_baixo_setup_B |
| 2026-10-13 10:05 | XRP-USDT-SWAP | 1.3640 | 1.3655/1.3534 | 1.3570 | res 1.3816 (ha 4 candles) | 0.01486 | -0.0031% | B/compra@1.3866 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-13 10:05 | DOGE-USDT-SWAP | 0.08417 | 0.08418/0.08321 | 0.08348 | res 0.08522 (ha 5 candles) | 0.00109 | -0.0032% | B/compra@0.08477 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-13 10:05 | ARB-USDT-SWAP | 0.18505 | 0.18529/0.18189 | 0.18292 | — | 0.00316 | 0.0100% | — | sem_zona |
| 2026-10-13 10:05 | WLD-USDT-SWAP | 0.50530 | 0.50620/0.49610 | 0.50220 | res 0.52460 (ha 7 candles) | 0.01149 | 0.0066% | — | sem_zona |
| 2026-10-13 10:05 | SUI-USDT-SWAP | 1.0457 | 1.0465/1.0321 | 1.0349 | res 1.0777 (ha 5 candles) | 0.01760 | 0.0100% | — | sem_zona |
| 2026-10-13 10:05 | UNI-USDT-SWAP | 7.3340 | 7.3360/7.2180 | 7.2700 | res 7.5290 (ha 5 candles) | 0.14750 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-10-13 10:05 | LINK-USDT-SWAP | 12.94 | 12.96/12.76 | 12.83 | res 13.19 (ha 6 candles) | 0.19371 | -0.0046% | — | descartado_rr_baixo_setup_B |
| 2026-10-13 11:05 | BTC-USDT-SWAP | 83236.3 | 83666.0/83132.3 | 83326.8 | res 84130.9 (ha 5 candles) | 574.92 | 0.0059% | B/compra@82850.8 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-13 11:05 | ETH-USDT-SWAP | 2502.0 | 2521.1/2496.7 | 2499.5 | res 2537.8 (ha 8 candles) | 24.92 | -0.0011% | — | sem_zona |
| 2026-10-13 11:05 | SOL-USDT-SWAP | 106.71 | 107.48/106.07 | 106.12 | res 109.05 (ha 6 candles) | 1.5371 | -0.0007% | — | sem_zona |
| 2026-10-13 11:05 | XRP-USDT-SWAP | 1.3616 | 1.3708/1.3585 | 1.3570 | res 1.3816 (ha 5 candles) | 0.01468 | -0.0032% | — | zona_expirada_setup_B |
| 2026-10-13 11:05 | DOGE-USDT-SWAP | 0.08403 | 0.08474/0.08375 | 0.08348 | res 0.08522 (ha 6 candles) | 0.00104 | -0.0016% | — | invalidado_setup_B |
| 2026-10-13 11:05 | ARB-USDT-SWAP | 0.18359 | 0.18658/0.18334 | 0.18292 | — | 0.00316 | 0.0100% | — | sem_zona |
| 2026-10-13 11:05 | WLD-USDT-SWAP | 0.50080 | 0.50990/0.50020 | 0.50220 | res 0.52460 (ha 8 candles) | 0.01136 | 0.0027% | — | sem_zona |
| 2026-10-13 11:05 | SUI-USDT-SWAP | 1.0386 | 1.0534/1.0381 | 1.0349 | res 1.0777 (ha 6 candles) | 0.01700 | 0.0100% | — | sem_zona |
| 2026-10-13 11:05 | UNI-USDT-SWAP | 7.3520 | 7.4220/7.2750 | 7.2700 | res 7.5290 (ha 6 candles) | 0.14071 | 0.0100% | B/compra@7.4520 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-13 11:05 | LINK-USDT-SWAP | 12.87 | 13.04/12.86 | 12.83 | res 13.19 (ha 7 candles) | 0.19200 | -0.0040% | — | sem_zona |
| 2026-10-13 12:05 | BTC-USDT-SWAP | 83488.4 | 83830.0/83195.0 | 83326.8 | res 84130.9 (ha 6 candles) | 552.16 | 0.0054% | B/compra@82850.8 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-13 12:05 | ETH-USDT-SWAP | 2516.4 | 2527.7/2500.3 | 2499.5 | res 2537.8 (ha 9 candles) | 23.85 | -0.0005% | B/compra@2532.6 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-13 12:05 | SOL-USDT-SWAP | 107.49 | 108.61/106.63 | 106.12 | res 109.05 (ha 7 candles) | 1.3671 | -0.0003% | B/compra@108.37 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-13 12:05 | XRP-USDT-SWAP | 1.3730 | 1.3808/1.3606 | 1.3570 | res 1.3816 (ha 6 candles) | 0.01369 | -0.0021% | B/compra@1.3732 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-13 12:05 | DOGE-USDT-SWAP | 0.08453 | 0.08514/0.08394 | 0.08348 | res 0.08522 (ha 7 candles) | 0.00096 | -0.0000% | — | sem_zona |
| 2026-10-13 12:05 | ARB-USDT-SWAP | 0.18510 | 0.18765/0.18344 | 0.18292 | — | 0.00304 | 0.0100% | — | sem_zona |
| 2026-10-13 12:05 | WLD-USDT-SWAP | 0.50320 | 0.51150/0.50030 | 0.50220 | res 0.52460 (ha 9 candles) | 0.01024 | -0.0011% | — | sem_zona |
| 2026-10-13 12:05 | SUI-USDT-SWAP | 1.0467 | 1.0639/1.0365 | 1.0349 | res 1.0777 (ha 7 candles) | 0.01633 | 0.0053% | — | sem_zona |
| 2026-10-13 12:05 | UNI-USDT-SWAP | 7.5260 | 7.6480/7.3420 | 7.2700 | res 7.5290 (ha 7 candles) | 0.14371 | 0.0065% | — | descartado_rr_baixo_setup_B |
| 2026-10-13 12:05 | LINK-USDT-SWAP | 12.99 | 13.09/12.86 | 12.83 | res 13.19 (ha 8 candles) | 0.18164 | -0.0042% | — | sem_zona |
| 2026-10-13 13:05 | BTC-USDT-SWAP | 83392.4 | 83694.1/83171.7 | 83392.4 | — | 514.68 | 0.0050% | B/compra@82850.8 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-13 13:05 | ETH-USDT-SWAP | 2515.4 | 2522.1/2503.1 | 2515.4 | — | 22.00 | 0.0001% | B/compra@2532.6 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-13 13:05 | SOL-USDT-SWAP | 107.33 | 107.90/106.62 | 107.33 | — | 1.2829 | 0.0001% | B/compra@108.37 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-13 13:05 | XRP-USDT-SWAP | 1.3698 | 1.3772/1.3625 | 1.3698 | — | 0.01231 | -0.0019% | B/compra@1.3732 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-13 13:05 | DOGE-USDT-SWAP | 0.08416 | 0.08474/0.08377 | 0.08416 | — | 0.00089 | 0.0017% | B/compra@0.08376 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-13 13:05 | ARB-USDT-SWAP | 0.18464 | 0.18613/0.18366 | 0.18464 | res 0.19060 (ha 9 candles) | 0.00277 | 0.0100% | — | sem_zona |
| 2026-10-13 13:05 | WLD-USDT-SWAP | 0.50480 | 0.50800/0.50040 | 0.50480 | — | 0.00946 | -0.0062% | — | sem_zona |
| 2026-10-13 13:05 | SUI-USDT-SWAP | 1.0388 | 1.0512/1.0314 | 1.0388 | — | 0.01567 | -0.0002% | — | sem_zona |
| 2026-10-13 13:05 | UNI-USDT-SWAP | 7.5730 | 7.5860/7.4600 | 7.5730 | — | 0.13543 | 0.0048% | — | sem_zona |
| 2026-10-13 13:05 | LINK-USDT-SWAP | 12.89 | 13.02/12.82 | 12.89 | — | 0.17143 | -0.0041% | B/venda@12.96 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-13 14:05 | BTC-USDT-SWAP | 83340.0 | 83576.4/83340.0 | 83392.4 | — | 482.16 | 0.0046% | B/compra@82850.8 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-13 14:05 | ETH-USDT-SWAP | 2511.8 | 2522.2/2511.6 | 2515.4 | — | 20.24 | 0.0005% | B/compra@2532.6 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-13 14:05 | SOL-USDT-SWAP | 107.49 | 107.95/107.30 | 107.33 | — | 1.2014 | 0.0013% | B/compra@108.37 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-13 14:05 | XRP-USDT-SWAP | 1.3681 | 1.3771/1.3674 | 1.3698 | — | 0.01189 | -0.0005% | — | invalidado_setup_B |
| 2026-10-13 14:05 | DOGE-USDT-SWAP | 0.08448 | 0.08467/0.08414 | 0.08416 | — | 0.00085 | 0.0029% | B/compra@0.08376 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-13 14:05 | ARB-USDT-SWAP | 0.18674 | 0.18737/0.18460 | 0.18464 | res 0.19060 (ha 10 candles) | 0.00279 | 0.0100% | — | sem_zona |
| 2026-10-13 14:05 | WLD-USDT-SWAP | 0.51520 | 0.52020/0.50460 | 0.50480 | — | 0.00965 | -0.0099% | B/venda@0.52210 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-13 14:05 | SUI-USDT-SWAP | 1.0463 | 1.0504/1.0384 | 1.0388 | — | 0.01564 | -0.0061% | — | sem_zona |
| 2026-10-13 14:05 | UNI-USDT-SWAP | 7.5750 | 7.6260/7.5350 | 7.5730 | — | 0.13057 | 0.0023% | — | sem_zona |
| 2026-10-13 14:05 | LINK-USDT-SWAP | 12.92 | 12.97/12.89 | 12.89 | — | 0.16450 | -0.0030% | B/venda@12.96 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-13 15:05 | BTC-USDT-SWAP | 83067.6 | 83340.0/82907.7 | 83392.4 | — | 452.86 | 0.0049% | B/compra@82850.8 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-13 15:05 | ETH-USDT-SWAP | 2500.1 | 2511.8/2494.1 | 2515.4 | — | 19.48 | 0.0013% | B/compra@2532.6 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-13 15:05 | SOL-USDT-SWAP | 107.11 | 107.57/106.89 | 107.33 | — | 1.1400 | 0.0023% | B/compra@108.37 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-13 15:05 | XRP-USDT-SWAP | 1.3634 | 1.3707/1.3615 | 1.3698 | — | 0.01146 | -0.0003% | — | sem_zona |
| 2026-10-13 15:05 | DOGE-USDT-SWAP | 0.08401 | 0.08448/0.08388 | 0.08416 | — | 0.00081 | 0.0022% | B/compra@0.08376 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-13 15:05 | ARB-USDT-SWAP | 0.18724 | 0.18860/0.18581 | 0.18464 | res 0.19060 (ha 11 candles) | 0.00278 | 0.0073% | B/compra@0.18820 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-13 15:05 | WLD-USDT-SWAP | 0.51110 | 0.51540/0.50870 | 0.50480 | — | 0.00915 | -0.0122% | B/venda@0.52210 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-13 15:05 | SUI-USDT-SWAP | 1.0437 | 1.0508/1.0415 | 1.0388 | — | 0.01516 | -0.0069% | — | sem_zona |
| 2026-10-13 15:05 | UNI-USDT-SWAP | 7.5140 | 7.5880/7.4930 | 7.5730 | — | 0.12743 | 0.0012% | B/venda@7.4530 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-13 15:05 | LINK-USDT-SWAP | 12.88 | 12.94/12.85 | 12.89 | — | 0.15729 | -0.0014% | — | descartado_rr_baixo_setup_B |
