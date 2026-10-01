# Log de Monitoramento Automatico -- Multi-Par (script gratuito, GitHub Actions)

> Gerado por script Python sem LLM (ver monitor/fetch_and_check.py). Fonte: OKX. Cobre os pares em PAIRS (configuracao no topo do script) -- BTC-USDT-SWAP e os demais adicionados na expansao de 07/09/2026. Leitura e MECANICA (regras objetivas da secao 4 do plano), sem a prosa qualitativa que o Claude gerava -- cole este log numa conversa do Claude se quiser a leitura interpretativa.

| Data/Hora (BRT) | Par | Close 1h | High/Low 1h | Close 4h | Swing 1h ref | ATR 1h | Funding | Zona ativa | Status checklist |
|---|---|---|---|---|---|---|---|---|---|
| 2026-09-29 00:06 | BTC-USDT-SWAP | 82937.0 | 83123.9/82856.8 | 83461.0 | — | 561.53 | 0.0028% | B/compra@82812.5 (2t/0c) | zona_mapeada_setup_B |
| 2026-09-29 00:06 | ETH-USDT-SWAP | 2656.6 | 2666.9/2650.7 | 2687.8 | — | 23.03 | 0.0066% | — | descartado_rr_baixo_setup_B |
| 2026-09-29 00:06 | SOL-USDT-SWAP | 116.90 | 117.25/116.35 | 118.83 | res 120.74 (ha 9 candles) | 1.4664 | -0.0000% | B/compra@119.76 (0t/3c) | zona_mapeada_setup_B |
| 2026-09-29 00:06 | XRP-USDT-SWAP | 1.4754 | 1.4808/1.4664 | 1.4962 | sup 1.4751 (ha 6 candles) | 0.02281 | 0.0036% | B/venda@1.4592 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-29 00:06 | DOGE-USDT-SWAP | 0.09225 | 0.09286/0.09175 | 0.09390 | — | 0.00142 | 0.0100% | B/venda@0.09138 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-29 00:06 | ARB-USDT-SWAP | 0.19443 | 0.19580/0.19194 | 0.20191 | res 0.20870 (ha 9 candles) | 0.00490 | 0.0100% | — | zona_expirada_setup_B |
| 2026-09-29 00:06 | WLD-USDT-SWAP | 0.46890 | 0.48270/0.46510 | 0.49120 | res 0.52040 (ha 14 candles) | 0.01350 | 0.0100% | — | sem_zona |
| 2026-09-29 00:06 | SUI-USDT-SWAP | 1.1114 | 1.1292/1.0967 | 1.1671 | res 1.1696 (ha 3 candles) | 0.02679 | 0.0100% | — | invalidado_setup_B |
| 2026-09-29 00:06 | UNI-USDT-SWAP | 8.5380 | 8.6440/8.4450 | 8.8010 | res 9.0900 (ha 14 candles) | 0.17586 | 0.0100% | B/compra@8.4900 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-29 00:06 | LINK-USDT-SWAP | 15.01 | 15.28/14.96 | 15.44 | sup 13.52 (ha 17 candles) | 0.40721 | 0.0095% | — | sem_zona |
| 2026-09-29 01:06 | BTC-USDT-SWAP | 83044.3 | 83188.8/82830.0 | 83044.3 | sup 83062.0 (ha 8 candles) | 549.91 | 0.0037% | — | zona_expirada_setup_B |
| 2026-09-29 01:06 | ETH-USDT-SWAP | 2664.3 | 2668.3/2654.0 | 2664.3 | — | 22.71 | 0.0070% | B/compra@2662.2 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-29 01:06 | SOL-USDT-SWAP | 117.80 | 117.99/116.84 | 117.80 | res 120.74 (ha 10 candles) | 1.4757 | 0.0018% | B/compra@119.76 (0t/4c) | zona_mapeada_setup_B |
| 2026-09-29 01:06 | XRP-USDT-SWAP | 1.4885 | 1.4914/1.4740 | 1.4885 | sup 1.4751 (ha 7 candles) | 0.02278 | 0.0053% | B/venda@1.4592 (0t/2c) | zona_mapeada_setup_B |
| 2026-09-29 01:06 | DOGE-USDT-SWAP | 0.09308 | 0.09336/0.09214 | 0.09308 | sup 0.09140 (ha 13 candles) | 0.00145 | 0.0100% | B/venda@0.09138 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-29 01:06 | ARB-USDT-SWAP | 0.19640 | 0.19805/0.19421 | 0.19640 | res 0.20870 (ha 10 candles) | 0.00489 | 0.0093% | B/compra@0.19575 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-29 01:06 | WLD-USDT-SWAP | 0.47410 | 0.47760/0.46770 | 0.47410 | res 0.49680 (ha 3 candles) | 0.01342 | 0.0100% | — | sem_zona |
| 2026-09-29 01:06 | SUI-USDT-SWAP | 1.1149 | 1.1271/1.1053 | 1.1149 | res 1.1696 (ha 4 candles) | 0.02696 | 0.0100% | — | sem_zona |
| 2026-09-29 01:06 | UNI-USDT-SWAP | 8.5800 | 8.6340/8.5260 | 8.5800 | res 8.8310 (ha 3 candles) | 0.17593 | 0.0100% | B/compra@8.4900 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-29 01:06 | LINK-USDT-SWAP | 14.86 | 15.10/14.79 | 14.86 | sup 13.52 (ha 18 candles) | 0.39764 | 0.0068% | — | sem_zona |
| 2026-09-29 02:06 | BTC-USDT-SWAP | 83171.9 | 83265.5/82999.8 | 83044.3 | sup 82726.0 (ha 3 candles) | 490.15 | 0.0041% | — | sem_zona |
| 2026-09-29 02:06 | ETH-USDT-SWAP | 2667.0 | 2672.8/2660.1 | 2664.3 | — | 20.79 | 0.0070% | B/compra@2662.2 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-29 02:06 | SOL-USDT-SWAP | 117.65 | 118.05/117.21 | 117.80 | res 120.74 (ha 11 candles) | 1.3550 | 0.0030% | B/compra@119.76 (0t/5c) | zona_mapeada_setup_B |
| 2026-09-29 02:06 | XRP-USDT-SWAP | 1.4851 | 1.4915/1.4789 | 1.4885 | sup 1.4647 (ha 3 candles) | 0.02029 | 0.0077% | B/venda@1.4592 (0t/3c) | zona_mapeada_setup_B |
| 2026-09-29 02:06 | DOGE-USDT-SWAP | 0.09304 | 0.09343/0.09265 | 0.09308 | sup 0.09140 (ha 14 candles) | 0.00132 | 0.0100% | B/venda@0.09138 (0t/2c) | zona_mapeada_setup_B |
| 2026-09-29 02:06 | ARB-USDT-SWAP | 0.19702 | 0.19889/0.19578 | 0.19640 | res 0.20870 (ha 11 candles) | 0.00452 | 0.0086% | B/compra@0.19575 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-29 02:06 | WLD-USDT-SWAP | 0.47490 | 0.48080/0.47170 | 0.47410 | res 0.49680 (ha 4 candles) | 0.01171 | 0.0100% | — | sem_zona |
| 2026-09-29 02:06 | SUI-USDT-SWAP | 1.1197 | 1.1263/1.1101 | 1.1149 | res 1.1696 (ha 5 candles) | 0.02554 | 0.0100% | — | sem_zona |
| 2026-09-29 02:06 | UNI-USDT-SWAP | 8.5690 | 8.6410/8.5120 | 8.5800 | res 8.8310 (ha 4 candles) | 0.16021 | 0.0100% | B/compra@8.4900 (2t/0c) | zona_mapeada_setup_B |
| 2026-09-29 02:06 | LINK-USDT-SWAP | 14.74 | 14.87/14.62 | 14.86 | sup 13.52 (ha 19 candles) | 0.36986 | 0.0066% | B/venda@14.48 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-29 03:06 | BTC-USDT-SWAP | 83399.9 | 83400.0/82933.0 | 83044.3 | sup 82726.0 (ha 4 candles) | 479.97 | 0.0044% | — | sem_zona |
| 2026-09-29 03:06 | ETH-USDT-SWAP | 2675.3 | 2676.9/2654.1 | 2664.3 | — | 20.50 | 0.0064% | — | descartado_rr_baixo_setup_B |
| 2026-09-29 03:06 | SOL-USDT-SWAP | 118.20 | 118.21/117.03 | 117.80 | res 120.74 (ha 12 candles) | 1.3400 | 0.0042% | B/compra@119.76 (0t/6c) | zona_mapeada_setup_B |
| 2026-09-29 03:06 | XRP-USDT-SWAP | 1.4933 | 1.4933/1.4735 | 1.4885 | sup 1.4647 (ha 4 candles) | 0.02007 | 0.0084% | B/venda@1.4592 (0t/4c) | zona_mapeada_setup_B |
| 2026-09-29 03:06 | DOGE-USDT-SWAP | 0.09381 | 0.09385/0.09257 | 0.09308 | sup 0.09175 (ha 3 candles) | 0.00130 | 0.0100% | B/venda@0.09138 (0t/3c) | zona_mapeada_setup_B |
| 2026-09-29 03:06 | ARB-USDT-SWAP | 0.19904 | 0.19970/0.19631 | 0.19640 | res 0.20870 (ha 12 candles) | 0.00451 | 0.0038% | — | confirmado_calibracao_setup_B |
| 2026-09-29 03:06 | WLD-USDT-SWAP | 0.48270 | 0.48400/0.47180 | 0.47410 | res 0.49680 (ha 5 candles) | 0.01189 | 0.0100% | — | sem_zona |
| 2026-09-29 03:06 | SUI-USDT-SWAP | 1.1221 | 1.1263/1.1082 | 1.1149 | res 1.1696 (ha 6 candles) | 0.02484 | 0.0100% | — | sem_zona |
| 2026-09-29 03:06 | UNI-USDT-SWAP | 8.6780 | 8.6960/8.5330 | 8.5800 | res 8.8310 (ha 5 candles) | 0.16000 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-09-29 03:06 | LINK-USDT-SWAP | 14.86 | 14.86/14.64 | 14.86 | sup 13.52 (ha 20 candles) | 0.35714 | 0.0026% | B/venda@14.48 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-29 04:06 | BTC-USDT-SWAP | 83965.1 | 83984.6/83380.2 | 83044.3 | sup 82726.0 (ha 5 candles) | 455.24 | 0.0032% | — | sem_zona |
| 2026-09-29 04:06 | ETH-USDT-SWAP | 2705.4 | 2708.0/2674.8 | 2664.3 | — | 20.86 | 0.0055% | B/venda@2696.9 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-29 04:06 | SOL-USDT-SWAP | 119.20 | 119.24/118.17 | 117.80 | res 120.74 (ha 13 candles) | 1.2636 | 0.0053% | B/compra@119.76 (0t/7c) | zona_mapeada_setup_B |
| 2026-09-29 04:06 | XRP-USDT-SWAP | 1.5052 | 1.5078/1.4930 | 1.4885 | sup 1.4647 (ha 5 candles) | 0.01889 | 0.0098% | B/venda@1.4592 (0t/5c) | zona_mapeada_setup_B |
| 2026-09-29 04:06 | DOGE-USDT-SWAP | 0.09472 | 0.09486/0.09379 | 0.09308 | sup 0.09175 (ha 4 candles) | 0.00122 | 0.0100% | B/venda@0.09138 (0t/4c) | zona_mapeada_setup_B |
| 2026-09-29 04:06 | ARB-USDT-SWAP | 0.20072 | 0.20180/0.19873 | 0.19640 | res 0.20870 (ha 13 candles) | 0.00432 | -0.0048% | — | sem_zona |
| 2026-09-29 04:06 | WLD-USDT-SWAP | 0.49240 | 0.49390/0.48150 | 0.47410 | res 0.49680 (ha 6 candles) | 0.01151 | 0.0100% | — | sem_zona |
| 2026-09-29 04:06 | SUI-USDT-SWAP | 1.1364 | 1.1388/1.1161 | 1.1149 | res 1.1696 (ha 7 candles) | 0.02403 | 0.0100% | — | sem_zona |
| 2026-09-29 04:06 | UNI-USDT-SWAP | 8.7730 | 8.7920/8.6690 | 8.5800 | res 8.8310 (ha 6 candles) | 0.15071 | 0.0100% | B/compra@8.7670 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-29 04:06 | LINK-USDT-SWAP | 14.98 | 15.05/14.84 | 14.86 | sup 13.52 (ha 21 candles) | 0.30886 | -0.0034% | B/venda@14.48 (0t/2c) | zona_mapeada_setup_B |
| 2026-09-29 05:06 | BTC-USDT-SWAP | 83944.5 | 84169.9/83822.1 | 83944.5 | sup 82726.0 (ha 6 candles) | 420.96 | 0.0026% | — | sem_zona |
| 2026-09-29 05:06 | ETH-USDT-SWAP | 2711.0 | 2718.3/2698.6 | 2711.0 | sup 2650.7 (ha 5 candles) | 19.43 | 0.0056% | — | invalidado_setup_B |
| 2026-09-29 05:06 | SOL-USDT-SWAP | 119.47 | 119.86/118.93 | 119.47 | — | 1.1707 | 0.0058% | B/compra@119.76 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-29 05:06 | XRP-USDT-SWAP | 1.5072 | 1.5110/1.5015 | 1.5072 | sup 1.4647 (ha 6 candles) | 0.01743 | 0.0097% | B/venda@1.4592 (0t/6c) | zona_mapeada_setup_B |
| 2026-09-29 05:06 | DOGE-USDT-SWAP | 0.09499 | 0.09523/0.09442 | 0.09499 | sup 0.09175 (ha 5 candles) | 0.00115 | 0.0100% | B/venda@0.09138 (0t/5c) | zona_mapeada_setup_B |
| 2026-09-29 05:06 | ARB-USDT-SWAP | 0.20374 | 0.20493/0.19978 | 0.20374 | res 0.20870 (ha 14 candles) | 0.00423 | -0.0113% | — | sem_zona |
| 2026-09-29 05:06 | WLD-USDT-SWAP | 0.50220 | 0.50660/0.49150 | 0.50220 | res 0.49680 (ha 7 candles) | 0.01159 | 0.0100% | A/compra@0.49680 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-29 05:06 | SUI-USDT-SWAP | 1.1526 | 1.1553/1.1327 | 1.1526 | res 1.1696 (ha 8 candles) | 0.02351 | 0.0100% | — | sem_zona |
| 2026-09-29 05:06 | UNI-USDT-SWAP | 8.9340 | 8.9960/8.7310 | 8.9340 | res 8.8310 (ha 7 candles) | 0.15414 | 0.0022% | — | descartado_rr_baixo_setup_B |
| 2026-09-29 05:06 | LINK-USDT-SWAP | 15.20 | 15.27/14.91 | 15.20 | sup 14.62 (ha 3 candles) | 0.30407 | -0.0039% | B/venda@14.48 (0t/3c) | zona_mapeada_setup_B |
| 2026-09-29 06:06 | BTC-USDT-SWAP | 83837.4 | 84338.2/83755.0 | 83944.5 | sup 82726.0 (ha 7 candles) | 444.16 | 0.0027% | — | sem_zona |
| 2026-09-29 06:06 | ETH-USDT-SWAP | 2707.8 | 2735.0/2704.4 | 2711.0 | sup 2650.7 (ha 6 candles) | 20.73 | 0.0055% | B/venda@2706.4 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-29 06:06 | SOL-USDT-SWAP | 119.12 | 119.95/118.83 | 119.47 | — | 1.1950 | 0.0055% | — | invalidado_setup_B |
| 2026-09-29 06:06 | XRP-USDT-SWAP | 1.5001 | 1.5137/1.4972 | 1.5072 | sup 1.4647 (ha 7 candles) | 0.01764 | 0.0100% | B/venda@1.4592 (0t/7c) | zona_mapeada_setup_B |
| 2026-09-29 06:06 | DOGE-USDT-SWAP | 0.09495 | 0.09547/0.09440 | 0.09499 | sup 0.09175 (ha 6 candles) | 0.00117 | 0.0100% | B/venda@0.09138 (0t/6c) | zona_mapeada_setup_B |
| 2026-09-29 06:06 | ARB-USDT-SWAP | 0.20464 | 0.20641/0.20287 | 0.20374 | res 0.20870 (ha 15 candles) | 0.00426 | -0.0185% | — | sem_zona |
| 2026-09-29 06:06 | WLD-USDT-SWAP | 0.49900 | 0.50610/0.49550 | 0.50220 | res 0.49680 (ha 8 candles) | 0.01179 | 0.0100% | A/compra@0.49680 (1t/0c) | zona_mapeada_setup_A |
| 2026-09-29 06:06 | SUI-USDT-SWAP | 1.1433 | 1.1598/1.1388 | 1.1526 | res 1.1696 (ha 9 candles) | 0.02404 | 0.0060% | — | sem_zona |
| 2026-09-29 06:06 | UNI-USDT-SWAP | 9.0030 | 9.3000/8.9120 | 8.9340 | res 8.8310 (ha 8 candles) | 0.17586 | -0.0049% | A/compra@8.8310 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-29 06:06 | LINK-USDT-SWAP | 15.30 | 15.33/15.07 | 15.20 | sup 14.62 (ha 4 candles) | 0.30300 | -0.0039% | B/venda@14.48 (0t/4c) | zona_mapeada_setup_B |
| 2026-09-29 07:06 | BTC-USDT-SWAP | 84206.3 | 84290.0/83729.0 | 83944.5 | sup 82726.0 (ha 8 candles) | 416.71 | 0.0022% | — | sem_zona |
| 2026-09-29 07:06 | ETH-USDT-SWAP | 2716.5 | 2721.1/2701.6 | 2711.0 | sup 2650.7 (ha 7 candles) | 19.56 | 0.0070% | — | invalidado_setup_B |
| 2026-09-29 07:06 | SOL-USDT-SWAP | 119.87 | 120.05/118.81 | 119.47 | — | 1.1371 | 0.0066% | B/venda@119.69 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-29 07:06 | XRP-USDT-SWAP | 1.5103 | 1.5140/1.4975 | 1.5072 | sup 1.4647 (ha 8 candles) | 0.01644 | 0.0100% | — | zona_expirada_setup_B |
| 2026-09-29 07:06 | DOGE-USDT-SWAP | 0.09550 | 0.09592/0.09470 | 0.09499 | sup 0.09175 (ha 7 candles) | 0.00111 | 0.0100% | B/venda@0.09138 (0t/7c) | zona_mapeada_setup_B |
| 2026-09-29 07:06 | ARB-USDT-SWAP | 0.20808 | 0.20870/0.20378 | 0.20374 | res 0.20870 (ha 16 candles) | 0.00407 | -0.0237% | B/compra@0.21025 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-29 07:06 | WLD-USDT-SWAP | 0.49900 | 0.50230/0.49730 | 0.50220 | res 0.49680 (ha 9 candles) | 0.01087 | 0.0100% | A/compra@0.49680 (2t/0c) | zona_mapeada_setup_A |
| 2026-09-29 07:06 | SUI-USDT-SWAP | 1.1670 | 1.1718/1.1402 | 1.1526 | res 1.1696 (ha 10 candles) | 0.02415 | 0.0015% | — | sem_zona |
| 2026-09-29 07:06 | UNI-USDT-SWAP | 9.0540 | 9.0870/8.9400 | 8.9340 | res 8.8310 (ha 9 candles) | 0.17243 | -0.0070% | A/compra@8.8310 (0t/1c) | zona_mapeada_setup_A |
| 2026-09-29 07:06 | LINK-USDT-SWAP | 15.45 | 15.48/15.24 | 15.20 | sup 14.62 (ha 5 candles) | 0.29600 | -0.0039% | B/venda@14.48 (0t/5c) | zona_mapeada_setup_B |
| 2026-09-29 08:06 | BTC-USDT-SWAP | 83988.3 | 84288.0/83942.2 | 83944.5 | sup 82726.0 (ha 9 candles) | 416.37 | 0.0007% | — | sem_zona |
| 2026-09-29 08:06 | ETH-USDT-SWAP | 2713.9 | 2719.4/2709.0 | 2711.0 | sup 2650.7 (ha 8 candles) | 19.16 | 0.0074% | B/venda@2724.2 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-29 08:06 | SOL-USDT-SWAP | 119.37 | 119.98/119.15 | 119.47 | — | 1.1286 | 0.0063% | — | descartado_rr_baixo_setup_B |
| 2026-09-29 08:06 | XRP-USDT-SWAP | 1.5076 | 1.5116/1.5020 | 1.5072 | sup 1.4647 (ha 9 candles) | 0.01571 | 0.0100% | — | sem_zona |
| 2026-09-29 08:06 | DOGE-USDT-SWAP | 0.09496 | 0.09559/0.09480 | 0.09499 | sup 0.09175 (ha 8 candles) | 0.00109 | 0.0097% | — | zona_expirada_setup_B |
| 2026-09-29 08:06 | ARB-USDT-SWAP | 0.20864 | 0.20962/0.20756 | 0.20374 | res 0.20870 (ha 17 candles) | 0.00397 | -0.0281% | — | invalidado_setup_B |
| 2026-09-29 08:06 | WLD-USDT-SWAP | 0.49900 | 0.49980/0.49430 | 0.50220 | res 0.50660 (ha 3 candles) | 0.01071 | 0.0100% | — | descartado_rr_baixo_setup_A |
| 2026-09-29 08:06 | SUI-USDT-SWAP | 1.1695 | 1.1739/1.1614 | 1.1526 | res 1.1696 (ha 11 candles) | 0.02359 | -0.0035% | — | sem_zona |
| 2026-09-29 08:06 | UNI-USDT-SWAP | 9.0410 | 9.0890/8.9890 | 8.9340 | res 8.8310 (ha 10 candles) | 0.17293 | -0.0096% | A/compra@8.8310 (0t/2c) | zona_mapeada_setup_A |
| 2026-09-29 08:06 | LINK-USDT-SWAP | 15.30 | 15.61/15.27 | 15.20 | sup 14.62 (ha 6 candles) | 0.29536 | -0.0025% | B/venda@14.48 (0t/6c) | zona_mapeada_setup_B |
| 2026-09-29 09:06 | BTC-USDT-SWAP | 84310.7 | 84464.8/83890.2 | 84310.7 | sup 82726.0 (ha 10 candles) | 425.74 | 0.0004% | — | sem_zona |
| 2026-09-29 09:06 | ETH-USDT-SWAP | 2731.0 | 2738.3/2713.8 | 2731.0 | sup 2650.7 (ha 9 candles) | 19.78 | 0.0080% | — | invalidado_setup_B |
| 2026-09-29 09:06 | SOL-USDT-SWAP | 120.07 | 120.37/119.16 | 120.07 | — | 1.1114 | 0.0058% | — | sem_zona |
| 2026-09-29 09:06 | XRP-USDT-SWAP | 1.5165 | 1.5203/1.5044 | 1.5165 | sup 1.4647 (ha 10 candles) | 0.01564 | 0.0100% | — | sem_zona |
| 2026-09-29 09:06 | DOGE-USDT-SWAP | 0.09570 | 0.09602/0.09482 | 0.09570 | sup 0.09175 (ha 9 candles) | 0.00109 | 0.0100% | — | sem_zona |
| 2026-09-29 09:06 | ARB-USDT-SWAP | 0.21362 | 0.21472/0.20817 | 0.21362 | res 0.20870 (ha 18 candles) | 0.00415 | -0.0309% | A/compra@0.20870 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-29 09:06 | WLD-USDT-SWAP | 0.50500 | 0.50720/0.49770 | 0.50500 | res 0.50660 (ha 4 candles) | 0.01074 | 0.0100% | B/compra@0.51080 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-29 09:06 | SUI-USDT-SWAP | 1.1802 | 1.1886/1.1630 | 1.1802 | res 1.1696 (ha 12 candles) | 0.02369 | -0.0042% | A/compra@1.1696 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-29 09:06 | UNI-USDT-SWAP | 9.1970 | 9.2560/9.0150 | 9.1970 | res 9.3000 (ha 3 candles) | 0.17864 | -0.0089% | A/compra@8.8310 (0t/3c) | zona_mapeada_setup_A |
| 2026-09-29 09:06 | LINK-USDT-SWAP | 15.34 | 15.45/15.28 | 15.34 | sup 14.62 (ha 7 candles) | 0.28486 | -0.0007% | B/venda@14.48 (0t/7c) | zona_mapeada_setup_B |
| 2026-09-29 10:06 | BTC-USDT-SWAP | 84288.2 | 84449.3/84089.0 | 84310.7 | sup 82726.0 (ha 11 candles) | 418.58 | 0.0004% | — | sem_zona |
| 2026-09-29 10:06 | ETH-USDT-SWAP | 2735.5 | 2748.5/2728.4 | 2731.0 | sup 2650.7 (ha 10 candles) | 19.75 | 0.0076% | B/venda@2742.9 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-29 10:06 | SOL-USDT-SWAP | 120.78 | 121.08/119.87 | 120.07 | — | 1.0936 | 0.0030% | — | sem_zona |
| 2026-09-29 10:06 | XRP-USDT-SWAP | 1.5466 | 1.5554/1.5114 | 1.5165 | sup 1.4647 (ha 11 candles) | 0.01759 | 0.0100% | B/venda@1.5458 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-29 10:06 | DOGE-USDT-SWAP | 0.09586 | 0.09635/0.09549 | 0.09570 | sup 0.09175 (ha 10 candles) | 0.00107 | 0.0100% | — | sem_zona |
| 2026-09-29 10:06 | ARB-USDT-SWAP | 0.21280 | 0.21614/0.21112 | 0.21362 | res 0.20870 (ha 19 candles) | 0.00421 | -0.0321% | A/compra@0.20870 (0t/1c) | zona_mapeada_setup_A |
| 2026-09-29 10:06 | WLD-USDT-SWAP | 0.50030 | 0.50850/0.49840 | 0.50500 | res 0.50660 (ha 5 candles) | 0.01079 | 0.0100% | — | invalidado_setup_B |
| 2026-09-29 10:06 | SUI-USDT-SWAP | 1.1751 | 1.1832/1.1704 | 1.1802 | res 1.1696 (ha 13 candles) | 0.02287 | -0.0058% | A/compra@1.1696 (1t/0c) | zona_mapeada_setup_A |
| 2026-09-29 10:06 | UNI-USDT-SWAP | 9.0700 | 9.2010/9.0230 | 9.1970 | res 9.3000 (ha 4 candles) | 0.18000 | -0.0093% | A/compra@8.8310 (0t/4c) | zona_mapeada_setup_A |
| 2026-09-29 10:06 | LINK-USDT-SWAP | 15.26 | 15.42/15.23 | 15.34 | sup 14.62 (ha 8 candles) | 0.27700 | 0.0013% | — | zona_expirada_setup_B |
| 2026-09-29 11:06 | BTC-USDT-SWAP | 84168.3 | 84544.9/83973.8 | 84310.7 | sup 82726.0 (ha 12 candles) | 445.58 | 0.0005% | — | sem_zona |
| 2026-09-29 11:06 | ETH-USDT-SWAP | 2725.8 | 2739.4/2719.6 | 2731.0 | sup 2650.7 (ha 11 candles) | 20.54 | 0.0062% | — | confirmado_calibracao_setup_B |
| 2026-09-29 11:06 | SOL-USDT-SWAP | 120.93 | 121.59/120.58 | 120.07 | — | 1.1329 | -0.0008% | — | sem_zona |
| 2026-09-29 11:06 | XRP-USDT-SWAP | 1.5477 | 1.5559/1.5383 | 1.5165 | sup 1.4647 (ha 12 candles) | 0.01820 | 0.0100% | B/venda@1.5458 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-29 11:06 | DOGE-USDT-SWAP | 0.09579 | 0.09630/0.09550 | 0.09570 | sup 0.09175 (ha 11 candles) | 0.00109 | 0.0100% | — | sem_zona |
| 2026-09-29 11:06 | ARB-USDT-SWAP | 0.21147 | 0.21370/0.21044 | 0.21362 | res 0.20870 (ha 20 candles) | 0.00432 | -0.0256% | A/compra@0.20870 (0t/2c) | zona_mapeada_setup_A |
| 2026-09-29 11:06 | WLD-USDT-SWAP | 0.49880 | 0.50210/0.49380 | 0.50500 | res 0.50660 (ha 6 candles) | 0.01088 | 0.0100% | — | sem_zona |
| 2026-09-29 11:06 | SUI-USDT-SWAP | 1.1619 | 1.1775/1.1537 | 1.1802 | res 1.1696 (ha 14 candles) | 0.02389 | -0.0044% | — | invalidado_setup_A |
| 2026-09-29 11:06 | UNI-USDT-SWAP | 9.0600 | 9.1060/8.9730 | 9.1970 | res 9.3000 (ha 5 candles) | 0.18293 | -0.0007% | A/compra@8.8310 (0t/5c) | zona_mapeada_setup_A |
| 2026-09-29 11:06 | LINK-USDT-SWAP | 15.13 | 15.35/15.11 | 15.34 | sup 14.62 (ha 9 candles) | 0.27471 | 0.0052% | — | sem_zona |
| 2026-09-29 12:06 | BTC-USDT-SWAP | 83717.6 | 84250.0/83643.3 | 84310.7 | sup 82726.0 (ha 13 candles) | 456.29 | 0.0018% | — | sem_zona |
| 2026-09-29 12:06 | ETH-USDT-SWAP | 2709.7 | 2731.0/2706.7 | 2731.0 | sup 2650.7 (ha 12 candles) | 20.94 | 0.0064% | B/venda@2724.2 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-29 12:06 | SOL-USDT-SWAP | 120.15 | 121.22/120.07 | 120.07 | — | 1.1393 | -0.0011% | — | sem_zona |
| 2026-09-29 12:06 | XRP-USDT-SWAP | 1.5450 | 1.5613/1.5407 | 1.5165 | sup 1.4647 (ha 13 candles) | 0.01851 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-09-29 12:06 | DOGE-USDT-SWAP | 0.09550 | 0.09606/0.09507 | 0.09570 | sup 0.09175 (ha 12 candles) | 0.00109 | 0.0100% | — | sem_zona |
| 2026-09-29 12:06 | ARB-USDT-SWAP | 0.21015 | 0.21207/0.20871 | 0.21362 | res 0.20870 (ha 21 candles) | 0.00434 | -0.0120% | A/compra@0.20870 (1t/0c) | zona_mapeada_setup_A |
| 2026-09-29 12:06 | WLD-USDT-SWAP | 0.51140 | 0.52210/0.49540 | 0.50500 | res 0.50660 (ha 7 candles) | 0.01209 | 0.0100% | A/compra@0.50660 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-29 12:06 | SUI-USDT-SWAP | 1.1637 | 1.1759/1.1503 | 1.1802 | res 1.1886 (ha 3 candles) | 0.02395 | 0.0007% | — | sem_zona |
| 2026-09-29 12:06 | UNI-USDT-SWAP | 8.9950 | 9.0720/8.9570 | 9.1970 | res 9.3000 (ha 6 candles) | 0.18307 | 0.0090% | A/compra@8.8310 (0t/6c) | zona_mapeada_setup_A |
| 2026-09-29 12:06 | LINK-USDT-SWAP | 15.10 | 15.18/14.98 | 15.34 | sup 14.62 (ha 10 candles) | 0.26257 | 0.0095% | — | sem_zona |
| 2026-09-29 13:06 | BTC-USDT-SWAP | 83049.8 | 83727.2/82877.3 | 83049.8 | sup 82726.0 (ha 14 candles) | 483.10 | 0.0036% | — | sem_zona |
| 2026-09-29 13:06 | ETH-USDT-SWAP | 2672.9 | 2710.8/2666.8 | 2672.9 | sup 2650.7 (ha 13 candles) | 22.28 | 0.0060% | B/venda@2724.2 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-29 13:06 | SOL-USDT-SWAP | 118.15 | 120.24/117.87 | 118.15 | sup 116.27 (ha 14 candles) | 1.1579 | -0.0015% | — | sem_zona |
| 2026-09-29 13:06 | XRP-USDT-SWAP | 1.5174 | 1.5452/1.5070 | 1.5174 | sup 1.4647 (ha 14 candles) | 0.01910 | 0.0100% | — | sem_zona |
| 2026-09-29 13:06 | DOGE-USDT-SWAP | 0.09369 | 0.09550/0.09322 | 0.09369 | sup 0.09175 (ha 13 candles) | 0.00111 | 0.0100% | — | sem_zona |
| 2026-09-29 13:06 | ARB-USDT-SWAP | 0.20566 | 0.21030/0.20362 | 0.20566 | — | 0.00413 | -0.0007% | — | invalidado_setup_A |
| 2026-09-29 13:06 | WLD-USDT-SWAP | 0.49610 | 0.51570/0.49070 | 0.49610 | — | 0.01264 | 0.0089% | — | invalidado_setup_A |
| 2026-09-29 13:06 | SUI-USDT-SWAP | 1.1377 | 1.1641/1.1297 | 1.1377 | — | 0.02294 | 0.0066% | B/compra@1.1273 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-29 13:06 | UNI-USDT-SWAP | 8.8590 | 8.9970/8.7840 | 8.8590 | — | 0.17871 | 0.0100% | A/compra@8.8310 (1t/0c) | zona_mapeada_setup_A |
| 2026-09-29 13:06 | LINK-USDT-SWAP | 14.79 | 15.10/14.71 | 14.79 | — | 0.26500 | 0.0100% | — | sem_zona |
| 2026-09-29 14:06 | BTC-USDT-SWAP | 83030.0 | 83274.9/82850.8 | 83049.8 | sup 82726.0 (ha 15 candles) | 494.31 | 0.0070% | — | sem_zona |
| 2026-09-29 14:06 | ETH-USDT-SWAP | 2674.8 | 2683.5/2667.0 | 2672.9 | sup 2650.7 (ha 14 candles) | 22.30 | 0.0071% | B/venda@2724.2 (0t/2c) | zona_mapeada_setup_B |
| 2026-09-29 14:06 | SOL-USDT-SWAP | 118.00 | 118.65/117.48 | 118.15 | sup 116.27 (ha 15 candles) | 1.1771 | -0.0019% | — | sem_zona |
| 2026-09-29 14:06 | XRP-USDT-SWAP | 1.4850 | 1.5232/1.4798 | 1.5174 | sup 1.4647 (ha 15 candles) | 0.02117 | 0.0100% | B/venda@1.4914 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-29 14:06 | DOGE-USDT-SWAP | 0.09329 | 0.09429/0.09280 | 0.09369 | sup 0.09175 (ha 14 candles) | 0.00113 | 0.0100% | — | sem_zona |
| 2026-09-29 14:06 | ARB-USDT-SWAP | 0.20468 | 0.20655/0.20326 | 0.20566 | — | 0.00409 | 0.0081% | — | sem_zona |
| 2026-09-29 14:06 | WLD-USDT-SWAP | 0.49100 | 0.50190/0.48460 | 0.49610 | — | 0.01262 | 0.0082% | — | sem_zona |
| 2026-09-29 14:06 | SUI-USDT-SWAP | 1.1364 | 1.1462/1.1275 | 1.1377 | — | 0.02196 | 0.0100% | B/compra@1.1273 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-29 14:06 | UNI-USDT-SWAP | 8.8010 | 8.9040/8.7470 | 8.8590 | — | 0.17571 | 0.0100% | A/compra@8.8310 (2t/0c) | zona_mapeada_setup_A |
| 2026-09-29 14:06 | LINK-USDT-SWAP | 14.70 | 14.88/14.64 | 14.79 | — | 0.25921 | 0.0100% | — | sem_zona |
| 2026-09-29 15:06 | BTC-USDT-SWAP | 83047.0 | 83195.0/82949.3 | 83049.8 | sup 82726.0 (ha 16 candles) | 486.24 | 0.0090% | — | sem_zona |
| 2026-09-29 15:06 | ETH-USDT-SWAP | 2672.5 | 2679.4/2668.3 | 2672.9 | sup 2650.7 (ha 15 candles) | 22.08 | 0.0073% | B/venda@2724.2 (0t/3c) | zona_mapeada_setup_B |
| 2026-09-29 15:06 | SOL-USDT-SWAP | 117.65 | 118.30/117.27 | 118.15 | sup 116.27 (ha 16 candles) | 1.1686 | -0.0022% | — | sem_zona |
| 2026-09-29 15:06 | XRP-USDT-SWAP | 1.4812 | 1.4899/1.4752 | 1.5174 | sup 1.4647 (ha 16 candles) | 0.02098 | 0.0078% | B/venda@1.4914 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-29 15:06 | DOGE-USDT-SWAP | 0.09320 | 0.09366/0.09268 | 0.09369 | sup 0.09175 (ha 15 candles) | 0.00112 | 0.0100% | — | sem_zona |
| 2026-09-29 15:06 | ARB-USDT-SWAP | 0.20431 | 0.20546/0.20269 | 0.20566 | — | 0.00401 | 0.0100% | — | sem_zona |
| 2026-09-29 15:06 | WLD-USDT-SWAP | 0.48530 | 0.49370/0.48270 | 0.49610 | — | 0.01270 | 0.0100% | B/venda@0.47950 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-29 15:06 | SUI-USDT-SWAP | 1.1325 | 1.1398/1.1259 | 1.1377 | — | 0.02139 | 0.0100% | B/compra@1.1273 (2t/0c) | zona_mapeada_setup_B |
| 2026-09-29 15:06 | UNI-USDT-SWAP | 8.8320 | 8.8700/8.7790 | 8.8590 | — | 0.17450 | 0.0100% | — | zona_expirada_setup_A |
| 2026-09-29 15:06 | LINK-USDT-SWAP | 14.54 | 14.75/14.48 | 14.79 | — | 0.25600 | 0.0100% | — | sem_zona |
| 2026-09-29 16:06 | BTC-USDT-SWAP | 83619.0 | 83677.8/83047.0 | 83049.8 | sup 82726.0 (ha 17 candles) | 512.31 | 0.0100% | — | sem_zona |
| 2026-09-29 16:06 | ETH-USDT-SWAP | 2694.4 | 2696.7/2672.5 | 2672.9 | sup 2666.8 (ha 3 candles) | 22.90 | 0.0074% | B/venda@2724.2 (0t/4c) | zona_mapeada_setup_B |
| 2026-09-29 16:06 | SOL-USDT-SWAP | 119.09 | 119.24/117.65 | 118.15 | sup 116.27 (ha 17 candles) | 1.2221 | -0.0026% | B/venda@119.69 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-29 16:06 | XRP-USDT-SWAP | 1.4990 | 1.5007/1.4812 | 1.5174 | sup 1.4647 (ha 17 candles) | 0.02147 | 0.0058% | — | invalidado_setup_B |
| 2026-09-29 16:06 | DOGE-USDT-SWAP | 0.09412 | 0.09430/0.09320 | 0.09369 | sup 0.09175 (ha 16 candles) | 0.00114 | 0.0100% | — | sem_zona |
| 2026-09-29 16:06 | ARB-USDT-SWAP | 0.20668 | 0.20885/0.20432 | 0.20566 | — | 0.00411 | 0.0100% | — | sem_zona |
| 2026-09-29 16:06 | WLD-USDT-SWAP | 0.49480 | 0.49790/0.48530 | 0.49610 | — | 0.01295 | 0.0100% | B/venda@0.47950 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-29 16:06 | SUI-USDT-SWAP | 1.1476 | 1.1523/1.1325 | 1.1377 | — | 0.02165 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-09-29 16:06 | UNI-USDT-SWAP | 8.9890 | 9.0180/8.8310 | 8.8590 | — | 0.17864 | 0.0100% | B/compra@9.0370 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-29 16:06 | LINK-USDT-SWAP | 14.57 | 14.68/14.55 | 14.79 | — | 0.24743 | 0.0084% | — | sem_zona |
| 2026-09-29 17:06 | BTC-USDT-SWAP | 83571.7 | 83666.0/83370.1 | 83571.7 | sup 82850.8 (ha 3 candles) | 500.09 | 0.0100% | — | sem_zona |
| 2026-09-29 17:06 | ETH-USDT-SWAP | 2688.9 | 2698.8/2684.9 | 2688.9 | sup 2666.8 (ha 4 candles) | 22.27 | 0.0068% | B/venda@2724.2 (0t/5c) | zona_mapeada_setup_B |
| 2026-09-29 17:06 | SOL-USDT-SWAP | 118.74 | 119.48/118.51 | 118.74 | sup 116.27 (ha 18 candles) | 1.2071 | -0.0022% | — | descartado_rr_baixo_setup_B |
| 2026-09-29 17:06 | XRP-USDT-SWAP | 1.4931 | 1.5032/1.4907 | 1.4931 | sup 1.4647 (ha 18 candles) | 0.02095 | 0.0046% | — | sem_zona |
| 2026-09-29 17:06 | DOGE-USDT-SWAP | 0.09362 | 0.09437/0.09347 | 0.09362 | sup 0.09175 (ha 17 candles) | 0.00111 | 0.0100% | — | sem_zona |
| 2026-09-29 17:06 | ARB-USDT-SWAP | 0.20508 | 0.20799/0.20496 | 0.20508 | — | 0.00409 | 0.0100% | — | sem_zona |
| 2026-09-29 17:06 | WLD-USDT-SWAP | 0.49320 | 0.50310/0.49240 | 0.49320 | — | 0.01284 | 0.0100% | B/venda@0.47950 (0t/2c) | zona_mapeada_setup_B |
| 2026-09-29 17:06 | SUI-USDT-SWAP | 1.1454 | 1.1577/1.1447 | 1.1454 | — | 0.02129 | 0.0100% | — | sem_zona |
| 2026-09-29 17:06 | UNI-USDT-SWAP | 8.9630 | 9.0490/8.9540 | 8.9630 | — | 0.17379 | 0.0100% | — | invalidado_setup_B |
| 2026-09-29 17:06 | LINK-USDT-SWAP | 14.63 | 14.68/14.57 | 14.63 | — | 0.23979 | 0.0064% | — | sem_zona |
| 2026-09-29 18:06 | BTC-USDT-SWAP | 83583.1 | 83641.3/83470.9 | 83571.7 | sup 82850.8 (ha 4 candles) | 469.09 | 0.0100% | — | sem_zona |
| 2026-09-29 18:06 | ETH-USDT-SWAP | 2688.1 | 2693.2/2685.4 | 2688.9 | sup 2666.8 (ha 5 candles) | 20.45 | 0.0065% | B/venda@2724.2 (0t/6c) | zona_mapeada_setup_B |
| 2026-09-29 18:06 | SOL-USDT-SWAP | 118.97 | 119.17/118.53 | 118.74 | sup 117.27 (ha 3 candles) | 1.1764 | -0.0036% | — | sem_zona |
| 2026-09-29 18:06 | XRP-USDT-SWAP | 1.4959 | 1.5003/1.4894 | 1.4931 | sup 1.4752 (ha 3 candles) | 0.02067 | 0.0023% | — | sem_zona |
| 2026-09-29 18:06 | DOGE-USDT-SWAP | 0.09399 | 0.09425/0.09340 | 0.09362 | sup 0.09268 (ha 3 candles) | 0.00110 | 0.0100% | — | sem_zona |
| 2026-09-29 18:06 | ARB-USDT-SWAP | 0.20736 | 0.20840/0.20417 | 0.20508 | — | 0.00417 | 0.0082% | B/compra@0.21025 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-29 18:06 | WLD-USDT-SWAP | 0.49450 | 0.49950/0.48930 | 0.49320 | — | 0.01269 | 0.0100% | B/venda@0.47950 (0t/3c) | zona_mapeada_setup_B |
| 2026-09-29 18:06 | SUI-USDT-SWAP | 1.1569 | 1.1620/1.1426 | 1.1454 | — | 0.02105 | 0.0100% | — | sem_zona |
| 2026-09-29 18:06 | UNI-USDT-SWAP | 8.9870 | 9.0150/8.9450 | 8.9630 | — | 0.17000 | 0.0100% | — | sem_zona |
| 2026-09-29 18:06 | LINK-USDT-SWAP | 14.70 | 14.73/14.59 | 14.63 | — | 0.23500 | 0.0060% | — | sem_zona |
| 2026-09-29 19:06 | BTC-USDT-SWAP | 83472.7 | 83583.1/83344.6 | 83571.7 | sup 82850.8 (ha 5 candles) | 461.29 | 0.0100% | — | sem_zona |
| 2026-09-29 19:06 | ETH-USDT-SWAP | 2678.4 | 2689.0/2676.0 | 2688.9 | sup 2666.8 (ha 6 candles) | 19.98 | 0.0078% | B/venda@2724.2 (0t/7c) | zona_mapeada_setup_B |
| 2026-09-29 19:06 | SOL-USDT-SWAP | 118.87 | 119.12/118.45 | 118.74 | sup 117.27 (ha 4 candles) | 1.1579 | -0.0050% | — | sem_zona |
| 2026-09-29 19:06 | XRP-USDT-SWAP | 1.4951 | 1.4980/1.4894 | 1.4931 | sup 1.4752 (ha 4 candles) | 0.02061 | 0.0019% | — | sem_zona |
| 2026-09-29 19:06 | DOGE-USDT-SWAP | 0.09408 | 0.09419/0.09365 | 0.09362 | sup 0.09268 (ha 4 candles) | 0.00108 | 0.0100% | — | sem_zona |
| 2026-09-29 19:06 | ARB-USDT-SWAP | 0.20638 | 0.20820/0.20499 | 0.20508 | — | 0.00403 | 0.0018% | B/compra@0.21025 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-29 19:06 | WLD-USDT-SWAP | 0.48920 | 0.49680/0.48670 | 0.49320 | — | 0.01233 | 0.0100% | B/venda@0.47950 (0t/4c) | zona_mapeada_setup_B |
| 2026-09-29 19:06 | SUI-USDT-SWAP | 1.1517 | 1.1590/1.1469 | 1.1454 | — | 0.02030 | 0.0100% | — | sem_zona |
| 2026-09-29 19:06 | UNI-USDT-SWAP | 8.9250 | 8.9960/8.9160 | 8.9630 | — | 0.15679 | 0.0100% | — | sem_zona |
| 2026-09-29 19:06 | LINK-USDT-SWAP | 14.70 | 14.75/14.61 | 14.63 | — | 0.21957 | 0.0071% | — | sem_zona |
| 2026-09-29 20:06 | BTC-USDT-SWAP | 83575.9 | 83694.6/83472.6 | 83571.7 | sup 82850.8 (ha 6 candles) | 435.49 | 0.0100% | — | sem_zona |
| 2026-09-29 20:06 | ETH-USDT-SWAP | 2680.7 | 2685.4/2673.5 | 2688.9 | sup 2666.8 (ha 7 candles) | 18.65 | 0.0074% | — | zona_expirada_setup_B |
| 2026-09-29 20:06 | SOL-USDT-SWAP | 119.05 | 119.54/118.79 | 118.74 | sup 117.27 (ha 5 candles) | 1.1314 | -0.0053% | — | sem_zona |
| 2026-09-29 20:06 | XRP-USDT-SWAP | 1.4931 | 1.4984/1.4909 | 1.4931 | sup 1.4752 (ha 5 candles) | 0.01996 | 0.0021% | — | sem_zona |
| 2026-09-29 20:06 | DOGE-USDT-SWAP | 0.09399 | 0.09445/0.09379 | 0.09362 | sup 0.09268 (ha 5 candles) | 0.00105 | 0.0100% | — | sem_zona |
| 2026-09-29 20:06 | ARB-USDT-SWAP | 0.20603 | 0.20803/0.20571 | 0.20508 | — | 0.00395 | -0.0005% | B/compra@0.21025 (0t/2c) | zona_mapeada_setup_B |
| 2026-09-29 20:06 | WLD-USDT-SWAP | 0.48790 | 0.49290/0.48650 | 0.49320 | — | 0.01203 | 0.0100% | B/venda@0.47950 (0t/5c) | zona_mapeada_setup_B |
| 2026-09-29 20:06 | SUI-USDT-SWAP | 1.1494 | 1.1546/1.1447 | 1.1454 | — | 0.01951 | 0.0100% | — | sem_zona |
| 2026-09-29 20:06 | UNI-USDT-SWAP | 8.9180 | 8.9720/8.9020 | 8.9630 | — | 0.13407 | 0.0100% | — | sem_zona |
| 2026-09-29 20:06 | LINK-USDT-SWAP | 14.68 | 14.74/14.66 | 14.63 | — | 0.20714 | 0.0100% | — | sem_zona |
| 2026-09-29 21:06 | BTC-USDT-SWAP | 83627.0 | 83816.7/83575.8 | 83627.0 | sup 82850.8 (ha 7 candles) | 412.62 | 0.0100% | — | sem_zona |
| 2026-09-29 21:06 | ETH-USDT-SWAP | 2676.8 | 2687.2/2674.6 | 2676.8 | sup 2666.8 (ha 8 candles) | 18.15 | 0.0057% | B/venda@2672.5 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-29 21:06 | SOL-USDT-SWAP | 119.08 | 119.61/118.80 | 119.08 | sup 117.27 (ha 6 candles) | 1.1007 | -0.0064% | — | sem_zona |
| 2026-09-29 21:06 | XRP-USDT-SWAP | 1.4898 | 1.4984/1.4874 | 1.4898 | sup 1.4752 (ha 6 candles) | 0.01957 | 0.0014% | — | sem_zona |
| 2026-09-29 21:06 | DOGE-USDT-SWAP | 0.09386 | 0.09445/0.09358 | 0.09386 | sup 0.09268 (ha 6 candles) | 0.00102 | 0.0100% | — | sem_zona |
| 2026-09-29 21:06 | ARB-USDT-SWAP | 0.20338 | 0.20727/0.20061 | 0.20338 | — | 0.00407 | -0.0022% | B/compra@0.21025 (0t/3c) | zona_mapeada_setup_B |
| 2026-09-29 21:06 | WLD-USDT-SWAP | 0.48340 | 0.49310/0.47690 | 0.48340 | — | 0.01283 | 0.0100% | — | invalidado_setup_B |
| 2026-09-29 21:06 | SUI-USDT-SWAP | 1.1519 | 1.1604/1.1436 | 1.1519 | sup 1.1259 (ha 6 candles) | 0.01845 | 0.0100% | — | sem_zona |
| 2026-09-29 21:06 | UNI-USDT-SWAP | 8.8850 | 8.9550/8.8160 | 8.8850 | sup 8.7470 (ha 7 candles) | 0.13350 | 0.0100% | — | sem_zona |
| 2026-09-29 21:06 | LINK-USDT-SWAP | 14.60 | 14.77/14.58 | 14.60 | — | 0.20343 | 0.0100% | B/venda@14.48 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-29 22:06 | BTC-USDT-SWAP | 83408.8 | 83696.1/83291.8 | 83627.0 | sup 82850.8 (ha 8 candles) | 416.80 | 0.0080% | — | sem_zona |
| 2026-09-29 22:06 | ETH-USDT-SWAP | 2671.7 | 2678.6/2666.4 | 2676.8 | sup 2666.8 (ha 9 candles) | 18.28 | 0.0059% | B/venda@2672.5 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-29 22:06 | SOL-USDT-SWAP | 118.89 | 119.23/118.39 | 119.08 | sup 117.27 (ha 7 candles) | 1.1014 | -0.0075% | — | sem_zona |
| 2026-09-29 22:06 | XRP-USDT-SWAP | 1.4915 | 1.4920/1.4848 | 1.4898 | sup 1.4752 (ha 7 candles) | 0.01940 | 0.0005% | — | sem_zona |
| 2026-09-29 22:06 | DOGE-USDT-SWAP | 0.09360 | 0.09395/0.09324 | 0.09386 | sup 0.09268 (ha 7 candles) | 0.00102 | 0.0100% | — | sem_zona |
| 2026-09-29 22:06 | ARB-USDT-SWAP | 0.20372 | 0.20505/0.20234 | 0.20338 | — | 0.00412 | -0.0019% | B/compra@0.21025 (0t/4c) | zona_mapeada_setup_B |
| 2026-09-29 22:06 | WLD-USDT-SWAP | 0.49020 | 0.49080/0.47940 | 0.48340 | — | 0.01325 | 0.0100% | — | sem_zona |
| 2026-09-29 22:06 | SUI-USDT-SWAP | 1.1464 | 1.1538/1.1409 | 1.1519 | sup 1.1259 (ha 7 candles) | 0.01848 | 0.0100% | — | sem_zona |
| 2026-09-29 22:06 | UNI-USDT-SWAP | 8.8380 | 8.9130/8.7750 | 8.8850 | sup 8.7470 (ha 8 candles) | 0.13621 | 0.0100% | — | sem_zona |
| 2026-09-29 22:06 | LINK-USDT-SWAP | 14.48 | 14.61/14.40 | 14.60 | — | 0.19407 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-09-29 23:06 | BTC-USDT-SWAP | 83404.4 | 83520.1/83294.2 | 83627.0 | sup 82850.8 (ha 9 candles) | 391.89 | 0.0059% | — | sem_zona |
| 2026-09-29 23:06 | ETH-USDT-SWAP | 2671.3 | 2676.3/2667.5 | 2676.8 | sup 2666.8 (ha 10 candles) | 17.16 | 0.0058% | B/venda@2672.5 (2t/0c) | zona_mapeada_setup_B |
| 2026-09-29 23:06 | SOL-USDT-SWAP | 119.35 | 119.59/118.75 | 119.08 | sup 117.27 (ha 8 candles) | 1.0750 | -0.0093% | B/venda@119.96 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-29 23:06 | XRP-USDT-SWAP | 1.4966 | 1.5000/1.4904 | 1.4898 | sup 1.4752 (ha 8 candles) | 0.01895 | 0.0011% | — | sem_zona |
| 2026-09-29 23:06 | DOGE-USDT-SWAP | 0.09393 | 0.09429/0.09351 | 0.09386 | sup 0.09268 (ha 8 candles) | 0.00099 | 0.0100% | — | sem_zona |
| 2026-09-29 23:06 | ARB-USDT-SWAP | 0.20422 | 0.20651/0.20336 | 0.20338 | — | 0.00387 | -0.0011% | B/compra@0.21025 (0t/5c) | zona_mapeada_setup_B |
| 2026-09-29 23:06 | WLD-USDT-SWAP | 0.49340 | 0.50120/0.48970 | 0.48340 | — | 0.01339 | 0.0100% | — | sem_zona |
| 2026-09-29 23:06 | SUI-USDT-SWAP | 1.1613 | 1.1773/1.1450 | 1.1519 | sup 1.1259 (ha 8 candles) | 0.01896 | 0.0100% | — | sem_zona |
| 2026-09-29 23:06 | UNI-USDT-SWAP | 8.8550 | 8.9280/8.8300 | 8.8850 | sup 8.7470 (ha 9 candles) | 0.12600 | 0.0100% | — | sem_zona |
| 2026-09-29 23:06 | LINK-USDT-SWAP | 14.42 | 14.53/14.42 | 14.60 | — | 0.18943 | 0.0100% | — | sem_zona |
| 2026-09-30 00:06 | BTC-USDT-SWAP | 83348.4 | 83585.8/83258.0 | 83627.0 | sup 82850.8 (ha 10 candles) | 389.57 | 0.0039% | — | sem_zona |
| 2026-09-30 00:06 | ETH-USDT-SWAP | 2673.4 | 2677.5/2664.3 | 2676.8 | sup 2666.8 (ha 11 candles) | 16.66 | 0.0057% | — | zona_expirada_setup_B |
| 2026-09-30 00:06 | SOL-USDT-SWAP | 119.62 | 120.06/119.11 | 119.08 | sup 117.27 (ha 9 candles) | 1.0564 | -0.0093% | B/venda@119.96 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-30 00:06 | XRP-USDT-SWAP | 1.5003 | 1.5040/1.4956 | 1.4898 | sup 1.4752 (ha 9 candles) | 0.01641 | 0.0021% | B/venda@1.4914 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-30 00:06 | DOGE-USDT-SWAP | 0.09387 | 0.09438/0.09363 | 0.09386 | sup 0.09268 (ha 9 candles) | 0.00098 | 0.0100% | — | sem_zona |
| 2026-09-30 00:06 | ARB-USDT-SWAP | 0.20343 | 0.20543/0.20278 | 0.20338 | — | 0.00370 | 0.0011% | B/compra@0.21025 (0t/6c) | zona_mapeada_setup_B |
| 2026-09-30 00:06 | WLD-USDT-SWAP | 0.49070 | 0.50000/0.48820 | 0.48340 | — | 0.01351 | 0.0100% | — | sem_zona |
| 2026-09-30 00:06 | SUI-USDT-SWAP | 1.1615 | 1.1673/1.1541 | 1.1519 | sup 1.1259 (ha 9 candles) | 0.01899 | 0.0100% | — | sem_zona |
| 2026-09-30 00:06 | UNI-USDT-SWAP | 8.8180 | 8.8960/8.7890 | 8.8850 | sup 8.7470 (ha 10 candles) | 0.12093 | 0.0100% | — | sem_zona |
| 2026-09-30 00:06 | LINK-USDT-SWAP | 14.49 | 14.51/14.37 | 14.60 | — | 0.18550 | 0.0094% | — | sem_zona |
| 2026-09-30 01:06 | BTC-USDT-SWAP | 83272.8 | 83391.1/83132.6 | 83272.8 | — | 367.24 | 0.0035% | B/compra@83118.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-30 01:06 | ETH-USDT-SWAP | 2670.5 | 2675.3/2666.8 | 2670.5 | — | 15.85 | 0.0060% | B/compra@2662.2 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-30 01:06 | SOL-USDT-SWAP | 119.07 | 119.84/118.85 | 119.07 | — | 1.0550 | -0.0081% | — | descartado_rr_baixo_setup_B |
| 2026-09-30 01:06 | XRP-USDT-SWAP | 1.4927 | 1.5013/1.4897 | 1.4927 | — | 0.01598 | 0.0028% | — | descartado_rr_baixo_setup_B |
| 2026-09-30 01:06 | DOGE-USDT-SWAP | 0.09334 | 0.09396/0.09303 | 0.09334 | — | 0.00099 | 0.0100% | — | sem_zona |
| 2026-09-30 01:06 | ARB-USDT-SWAP | 0.20184 | 0.20379/0.20139 | 0.20184 | sup 0.20061 (ha 4 candles) | 0.00364 | 0.0047% | B/compra@0.21025 (0t/7c) | zona_mapeada_setup_B |
| 2026-09-30 01:06 | WLD-USDT-SWAP | 0.48910 | 0.49170/0.48520 | 0.48910 | sup 0.47690 (ha 4 candles) | 0.01339 | 0.0100% | — | sem_zona |
| 2026-09-30 01:06 | SUI-USDT-SWAP | 1.1471 | 1.1633/1.1457 | 1.1471 | sup 1.1409 (ha 3 candles) | 0.01854 | 0.0100% | — | sem_zona |
| 2026-09-30 01:06 | UNI-USDT-SWAP | 8.7740 | 8.8260/8.7210 | 8.7740 | sup 8.7470 (ha 11 candles) | 0.11893 | 0.0100% | — | sem_zona |
| 2026-09-30 01:06 | LINK-USDT-SWAP | 14.37 | 14.49/14.32 | 14.37 | — | 0.18050 | 0.0100% | — | sem_zona |
| 2026-09-30 02:06 | BTC-USDT-SWAP | 83174.8 | 83393.4/83170.0 | 83272.8 | — | 339.86 | 0.0036% | B/compra@83118.0 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-30 02:06 | ETH-USDT-SWAP | 2669.0 | 2675.7/2669.0 | 2670.5 | — | 14.59 | 0.0059% | B/compra@2662.2 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-30 02:06 | SOL-USDT-SWAP | 118.72 | 119.68/118.66 | 119.07 | — | 1.0457 | -0.0069% | — | sem_zona |
| 2026-09-30 02:06 | XRP-USDT-SWAP | 1.4928 | 1.4990/1.4918 | 1.4927 | — | 0.01502 | 0.0042% | B/compra@1.5004 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-30 02:06 | DOGE-USDT-SWAP | 0.09336 | 0.09391/0.09330 | 0.09334 | — | 0.00096 | 0.0100% | — | sem_zona |
| 2026-09-30 02:06 | ARB-USDT-SWAP | 0.20136 | 0.20320/0.20135 | 0.20184 | sup 0.20061 (ha 5 candles) | 0.00354 | 0.0064% | — | zona_expirada_setup_B |
| 2026-09-30 02:06 | WLD-USDT-SWAP | 0.49510 | 0.49840/0.48840 | 0.48910 | sup 0.47690 (ha 5 candles) | 0.01219 | 0.0100% | — | sem_zona |
| 2026-09-30 02:06 | SUI-USDT-SWAP | 1.1542 | 1.1627/1.1469 | 1.1471 | sup 1.1409 (ha 4 candles) | 0.01784 | 0.0100% | — | sem_zona |
| 2026-09-30 02:06 | UNI-USDT-SWAP | 8.8290 | 8.8760/8.7700 | 8.7740 | sup 8.7470 (ha 12 candles) | 0.11829 | 0.0100% | — | sem_zona |
| 2026-09-30 02:06 | LINK-USDT-SWAP | 14.35 | 14.44/14.34 | 14.37 | — | 0.17393 | 0.0100% | — | sem_zona |
| 2026-09-30 03:06 | BTC-USDT-SWAP | 83350.0 | 83487.9/83149.9 | 83272.8 | — | 303.30 | 0.0035% | B/compra@83118.0 (2t/0c) | zona_mapeada_setup_B |
| 2026-09-30 03:06 | ETH-USDT-SWAP | 2674.1 | 2679.9/2666.1 | 2670.5 | — | 12.43 | 0.0065% | B/compra@2662.2 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-30 03:06 | SOL-USDT-SWAP | 119.04 | 119.60/118.43 | 119.07 | — | 0.96000 | -0.0031% | B/venda@119.69 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-30 03:06 | XRP-USDT-SWAP | 1.5027 | 1.5048/1.4926 | 1.4927 | — | 0.01316 | 0.0035% | — | descartado_rr_baixo_setup_B |
| 2026-09-30 03:06 | DOGE-USDT-SWAP | 0.09392 | 0.09412/0.09327 | 0.09334 | — | 0.00086 | 0.0100% | — | sem_zona |
| 2026-09-30 03:06 | ARB-USDT-SWAP | 0.20288 | 0.20363/0.20114 | 0.20184 | sup 0.20061 (ha 6 candles) | 0.00324 | 0.0080% | — | sem_zona |
| 2026-09-30 03:06 | WLD-USDT-SWAP | 0.50010 | 0.50670/0.49260 | 0.48910 | sup 0.47690 (ha 6 candles) | 0.01141 | 0.0100% | — | sem_zona |
| 2026-09-30 03:06 | SUI-USDT-SWAP | 1.1624 | 1.1670/1.1502 | 1.1471 | sup 1.1409 (ha 5 candles) | 0.01659 | 0.0100% | — | sem_zona |
| 2026-09-30 03:06 | UNI-USDT-SWAP | 8.8590 | 8.8890/8.8050 | 8.7740 | sup 8.7470 (ha 13 candles) | 0.10907 | 0.0100% | — | sem_zona |
| 2026-09-30 03:06 | LINK-USDT-SWAP | 14.42 | 14.45/14.33 | 14.37 | — | 0.15386 | 0.0100% | — | sem_zona |
| 2026-09-30 04:06 | BTC-USDT-SWAP | 83012.2 | 83397.2/82935.0 | 83272.8 | — | 306.02 | 0.0043% | — | invalidado_setup_B |
| 2026-09-30 04:06 | ETH-USDT-SWAP | 2661.0 | 2675.8/2656.6 | 2670.5 | — | 12.63 | 0.0075% | B/compra@2662.2 (2t/0c) | zona_mapeada_setup_B |
| 2026-09-30 04:06 | SOL-USDT-SWAP | 118.05 | 119.18/118.00 | 119.07 | — | 0.96071 | -0.0010% | B/venda@119.69 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-30 04:06 | XRP-USDT-SWAP | 1.4921 | 1.5061/1.4906 | 1.4927 | — | 0.01117 | 0.0017% | — | sem_zona |
| 2026-09-30 04:06 | DOGE-USDT-SWAP | 0.09298 | 0.09411/0.09283 | 0.09334 | — | 0.00084 | 0.0100% | — | sem_zona |
| 2026-09-30 04:06 | ARB-USDT-SWAP | 0.20105 | 0.20374/0.20053 | 0.20184 | sup 0.20061 (ha 7 candles) | 0.00323 | 0.0093% | — | sem_zona |
| 2026-09-30 04:06 | WLD-USDT-SWAP | 0.49520 | 0.50380/0.49380 | 0.48910 | sup 0.47690 (ha 7 candles) | 0.01089 | 0.0100% | — | sem_zona |
| 2026-09-30 04:06 | SUI-USDT-SWAP | 1.1575 | 1.1724/1.1570 | 1.1471 | sup 1.1409 (ha 6 candles) | 0.01635 | 0.0068% | — | sem_zona |
| 2026-09-30 04:06 | UNI-USDT-SWAP | 8.7470 | 8.8720/8.7240 | 8.7740 | sup 8.7210 (ha 3 candles) | 0.10843 | 0.0100% | — | sem_zona |
| 2026-09-30 04:06 | LINK-USDT-SWAP | 14.29 | 14.45/14.28 | 14.37 | — | 0.14864 | 0.0100% | B/venda@14.21 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-30 05:06 | BTC-USDT-SWAP | 83248.4 | 83429.0/82918.9 | 83248.4 | res 83816.7 (ha 8 candles) | 324.91 | 0.0031% | B/compra@83439.3 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-30 05:06 | ETH-USDT-SWAP | 2673.4 | 2676.8/2659.3 | 2673.4 | — | 13.09 | 0.0058% | — | descartado_rr_baixo_setup_B |
| 2026-09-30 05:06 | SOL-USDT-SWAP | 118.41 | 118.89/117.81 | 118.41 | — | 0.96429 | 0.0002% | B/venda@119.69 (0t/2c) | zona_mapeada_setup_B |
| 2026-09-30 05:06 | XRP-USDT-SWAP | 1.4998 | 1.5037/1.4885 | 1.4998 | — | 0.01121 | 0.0022% | — | sem_zona |
| 2026-09-30 05:06 | DOGE-USDT-SWAP | 0.09375 | 0.09407/0.09288 | 0.09375 | — | 0.00086 | 0.0100% | — | sem_zona |
| 2026-09-30 05:06 | ARB-USDT-SWAP | 0.20285 | 0.20369/0.20086 | 0.20285 | sup 0.20061 (ha 8 candles) | 0.00323 | 0.0100% | — | sem_zona |
| 2026-09-30 05:06 | WLD-USDT-SWAP | 0.50150 | 0.50330/0.49260 | 0.50150 | sup 0.47690 (ha 8 candles) | 0.01087 | 0.0096% | — | sem_zona |
| 2026-09-30 05:06 | SUI-USDT-SWAP | 1.1652 | 1.1728/1.1490 | 1.1652 | sup 1.1409 (ha 7 candles) | 0.01706 | 0.0030% | — | sem_zona |
| 2026-09-30 05:06 | UNI-USDT-SWAP | 8.8190 | 8.8610/8.7380 | 8.8190 | sup 8.7210 (ha 4 candles) | 0.11071 | 0.0100% | — | sem_zona |
| 2026-09-30 05:06 | LINK-USDT-SWAP | 14.30 | 14.35/14.25 | 14.30 | — | 0.13607 | 0.0100% | B/venda@14.21 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-30 06:06 | BTC-USDT-SWAP | 83029.2 | 83299.0/82983.0 | 83248.4 | res 83816.7 (ha 9 candles) | 302.42 | 0.0030% | B/compra@83439.3 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-30 06:06 | ETH-USDT-SWAP | 2670.0 | 2673.5/2663.5 | 2673.4 | — | 12.07 | 0.0054% | — | sem_zona |
| 2026-09-30 06:06 | SOL-USDT-SWAP | 118.17 | 118.47/117.75 | 118.41 | — | 0.90214 | 0.0020% | B/venda@119.69 (0t/3c) | zona_mapeada_setup_B |
| 2026-09-30 06:06 | XRP-USDT-SWAP | 1.4966 | 1.5010/1.4915 | 1.4998 | — | 0.01049 | 0.0024% | — | sem_zona |
| 2026-09-30 06:06 | DOGE-USDT-SWAP | 0.09358 | 0.09380/0.09327 | 0.09375 | — | 0.00082 | 0.0100% | — | sem_zona |
| 2026-09-30 06:06 | ARB-USDT-SWAP | 0.20377 | 0.20457/0.20172 | 0.20285 | sup 0.20061 (ha 9 candles) | 0.00311 | 0.0097% | — | sem_zona |
| 2026-09-30 06:06 | WLD-USDT-SWAP | 0.51430 | 0.51940/0.49490 | 0.50150 | sup 0.47690 (ha 9 candles) | 0.01172 | 0.0100% | — | sem_zona |
| 2026-09-30 06:06 | SUI-USDT-SWAP | 1.1575 | 1.1677/1.1511 | 1.1652 | sup 1.1409 (ha 8 candles) | 0.01683 | 0.0009% | — | sem_zona |
| 2026-09-30 06:06 | UNI-USDT-SWAP | 8.8010 | 8.8430/8.7610 | 8.8190 | sup 8.7210 (ha 5 candles) | 0.10321 | 0.0100% | — | sem_zona |
| 2026-09-30 06:06 | LINK-USDT-SWAP | 14.29 | 14.31/14.19 | 14.30 | — | 0.13521 | 0.0100% | — | invalidado_setup_B |
| 2026-09-30 07:06 | BTC-USDT-SWAP | 83597.6 | 83786.8/83019.4 | 83248.4 | res 83816.7 (ha 10 candles) | 336.10 | 0.0039% | — | descartado_rr_baixo_setup_B |
| 2026-09-30 07:06 | ETH-USDT-SWAP | 2687.6 | 2699.7/2669.5 | 2673.4 | — | 13.23 | 0.0057% | B/venda@2696.9 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-30 07:06 | SOL-USDT-SWAP | 119.29 | 119.79/118.13 | 118.41 | — | 0.95143 | 0.0051% | B/venda@119.69 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-30 07:06 | XRP-USDT-SWAP | 1.5097 | 1.5156/1.4960 | 1.4998 | — | 0.01100 | 0.0060% | — | sem_zona |
| 2026-09-30 07:06 | DOGE-USDT-SWAP | 0.09424 | 0.09468/0.09353 | 0.09375 | — | 0.00084 | 0.0100% | — | sem_zona |
| 2026-09-30 07:06 | ARB-USDT-SWAP | 0.20321 | 0.20672/0.20307 | 0.20285 | sup 0.20053 (ha 3 candles) | 0.00316 | 0.0063% | — | sem_zona |
| 2026-09-30 07:06 | WLD-USDT-SWAP | 0.51310 | 0.52290/0.51110 | 0.50150 | sup 0.47690 (ha 10 candles) | 0.01180 | 0.0100% | — | sem_zona |
| 2026-09-30 07:06 | SUI-USDT-SWAP | 1.1597 | 1.1763/1.1556 | 1.1652 | sup 1.1409 (ha 9 candles) | 0.01738 | 0.0008% | — | sem_zona |
| 2026-09-30 07:06 | UNI-USDT-SWAP | 8.8260 | 8.9050/8.7990 | 8.8190 | sup 8.7210 (ha 6 candles) | 0.10400 | 0.0100% | — | sem_zona |
| 2026-09-30 07:06 | LINK-USDT-SWAP | 14.36 | 14.45/14.28 | 14.30 | — | 0.14000 | 0.0100% | — | sem_zona |
| 2026-09-30 08:06 | BTC-USDT-SWAP | 83873.4 | 83921.2/83597.6 | 83248.4 | res 83816.7 (ha 11 candles) | 347.04 | 0.0038% | A/compra@83816.7 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-30 08:06 | ETH-USDT-SWAP | 2694.2 | 2696.8/2686.7 | 2673.4 | — | 13.40 | 0.0054% | B/venda@2696.9 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-30 08:06 | SOL-USDT-SWAP | 119.81 | 119.87/119.20 | 118.41 | — | 0.95357 | 0.0078% | B/venda@119.69 (2t/0c) | zona_mapeada_setup_B |
| 2026-09-30 08:06 | XRP-USDT-SWAP | 1.5121 | 1.5146/1.5060 | 1.4998 | — | 0.01084 | 0.0085% | — | sem_zona |
| 2026-09-30 08:06 | DOGE-USDT-SWAP | 0.09535 | 0.09541/0.09419 | 0.09375 | — | 0.00086 | 0.0100% | B/compra@0.09519 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-30 08:06 | ARB-USDT-SWAP | 0.20393 | 0.20518/0.20261 | 0.20285 | sup 0.20053 (ha 4 candles) | 0.00304 | 0.0015% | — | sem_zona |
| 2026-09-30 08:06 | WLD-USDT-SWAP | 0.51300 | 0.51790/0.51100 | 0.50150 | sup 0.47690 (ha 11 candles) | 0.01156 | 0.0100% | — | sem_zona |
| 2026-09-30 08:06 | SUI-USDT-SWAP | 1.1561 | 1.1658/1.1549 | 1.1652 | sup 1.1409 (ha 10 candles) | 0.01677 | -0.0014% | — | sem_zona |
| 2026-09-30 08:06 | UNI-USDT-SWAP | 8.8900 | 8.9280/8.8070 | 8.8190 | sup 8.7210 (ha 7 candles) | 0.10764 | 0.0100% | — | sem_zona |
| 2026-09-30 08:06 | LINK-USDT-SWAP | 14.40 | 14.45/14.35 | 14.30 | — | 0.13736 | 0.0100% | B/venda@14.48 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-30 09:06 | BTC-USDT-SWAP | 83879.2 | 83944.0/83650.5 | 83879.2 | res 83816.7 (ha 12 candles) | 350.97 | 0.0034% | — | descartado_rr_baixo_setup_A |
| 2026-09-30 09:06 | ETH-USDT-SWAP | 2696.4 | 2699.0/2683.6 | 2696.4 | — | 13.57 | 0.0056% | B/venda@2696.9 (2t/0c) | zona_mapeada_setup_B |
| 2026-09-30 09:06 | SOL-USDT-SWAP | 119.46 | 119.82/119.13 | 119.46 | — | 0.95500 | 0.0098% | — | zona_expirada_setup_B |
| 2026-09-30 09:06 | XRP-USDT-SWAP | 1.5153 | 1.5197/1.5063 | 1.5153 | — | 0.01118 | 0.0100% | — | sem_zona |
| 2026-09-30 09:06 | DOGE-USDT-SWAP | 0.09579 | 0.09661/0.09494 | 0.09579 | — | 0.00094 | 0.0100% | B/compra@0.09519 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-30 09:06 | ARB-USDT-SWAP | 0.20385 | 0.20438/0.20277 | 0.20385 | sup 0.20053 (ha 5 candles) | 0.00292 | -0.0054% | — | sem_zona |
| 2026-09-30 09:06 | WLD-USDT-SWAP | 0.54220 | 0.54320/0.50820 | 0.54220 | — | 0.01334 | 0.0076% | B/venda@0.55180 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-30 09:06 | SUI-USDT-SWAP | 1.1501 | 1.1588/1.1457 | 1.1501 | sup 1.1409 (ha 11 candles) | 0.01684 | -0.0019% | — | sem_zona |
| 2026-09-30 09:06 | UNI-USDT-SWAP | 8.9000 | 8.9210/8.8250 | 8.9000 | sup 8.7210 (ha 8 candles) | 0.10879 | 0.0100% | — | sem_zona |
| 2026-09-30 09:06 | LINK-USDT-SWAP | 14.44 | 14.44/14.30 | 14.44 | — | 0.13686 | 0.0100% | B/venda@14.48 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-30 10:06 | BTC-USDT-SWAP | 85254.3 | 85490.6/83713.4 | 83879.2 | res 83816.7 (ha 13 candles) | 462.06 | 0.0047% | B/compra@85070.2 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-30 10:06 | ETH-USDT-SWAP | 2729.8 | 2737.9/2690.8 | 2696.4 | — | 16.08 | 0.0066% | — | invalidado_setup_B |
| 2026-09-30 10:06 | SOL-USDT-SWAP | 121.86 | 122.49/119.35 | 119.46 | — | 1.1257 | 0.0100% | — | sem_zona |
| 2026-09-30 10:06 | XRP-USDT-SWAP | 1.5339 | 1.5402/1.5059 | 1.5153 | — | 0.01309 | 0.0100% | — | sem_zona |
| 2026-09-30 10:06 | DOGE-USDT-SWAP | 0.09727 | 0.09778/0.09548 | 0.09579 | — | 0.00106 | 0.0100% | B/compra@0.09519 (1t/1c) | zona_mapeada_setup_B |
| 2026-09-30 10:06 | ARB-USDT-SWAP | 0.20870 | 0.21010/0.20293 | 0.20385 | sup 0.20053 (ha 6 candles) | 0.00327 | -0.0104% | — | sem_zona |
| 2026-09-30 10:06 | WLD-USDT-SWAP | 0.54470 | 0.55200/0.52860 | 0.54220 | — | 0.01456 | 0.0100% | B/venda@0.55180 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-30 10:06 | SUI-USDT-SWAP | 1.1877 | 1.1928/1.1380 | 1.1501 | sup 1.1409 (ha 12 candles) | 0.02005 | -0.0005% | — | sem_zona |
| 2026-09-30 10:06 | UNI-USDT-SWAP | 9.1820 | 9.1970/8.8250 | 8.9000 | sup 8.7210 (ha 9 candles) | 0.13036 | 0.0100% | — | sem_zona |
| 2026-09-30 10:06 | LINK-USDT-SWAP | 14.72 | 14.81/14.37 | 14.44 | — | 0.16257 | 0.0100% | — | invalidado_setup_B |
| 2026-09-30 11:06 | BTC-USDT-SWAP | 84599.6 | 85639.0/83976.1 | 83879.2 | res 83816.7 (ha 14 candles) | 563.63 | 0.0053% | — | invalidado_setup_B |
| 2026-09-30 11:06 | ETH-USDT-SWAP | 2708.8 | 2737.5/2688.0 | 2696.4 | — | 18.72 | 0.0073% | B/venda@2720.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-30 11:06 | SOL-USDT-SWAP | 120.97 | 122.77/119.71 | 119.46 | — | 1.2864 | 0.0100% | B/venda@120.74 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-30 11:06 | XRP-USDT-SWAP | 1.5195 | 1.5440/1.5067 | 1.5153 | — | 0.01497 | 0.0100% | — | sem_zona |
| 2026-09-30 11:06 | DOGE-USDT-SWAP | 0.09622 | 0.09813/0.09551 | 0.09579 | — | 0.00118 | 0.0100% | B/compra@0.09519 (1t/2c) | zona_mapeada_setup_B |
| 2026-09-30 11:06 | ARB-USDT-SWAP | 0.20776 | 0.21221/0.20451 | 0.20385 | sup 0.20053 (ha 7 candles) | 0.00335 | -0.0159% | — | sem_zona |
| 2026-09-30 11:06 | WLD-USDT-SWAP | 0.55070 | 0.57120/0.54170 | 0.54220 | — | 0.01551 | 0.0100% | B/venda@0.55180 (2t/0c) | zona_mapeada_setup_B |
| 2026-09-30 11:06 | SUI-USDT-SWAP | 1.1802 | 1.2112/1.1648 | 1.1501 | sup 1.1409 (ha 13 candles) | 0.02216 | -0.0013% | — | sem_zona |
| 2026-09-30 11:06 | UNI-USDT-SWAP | 8.9840 | 9.1840/8.8930 | 8.9000 | sup 8.7210 (ha 10 candles) | 0.14121 | 0.0100% | — | sem_zona |
| 2026-09-30 11:06 | LINK-USDT-SWAP | 14.55 | 14.77/14.36 | 14.44 | — | 0.17814 | 0.0100% | — | sem_zona |
| 2026-09-30 12:06 | BTC-USDT-SWAP | 83757.5 | 84600.0/83309.9 | 83879.2 | res 83816.7 (ha 15 candles) | 626.90 | 0.0046% | B/compra@83764.7 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-30 12:06 | ETH-USDT-SWAP | 2676.7 | 2712.7/2666.6 | 2696.4 | — | 21.14 | 0.0058% | B/venda@2720.0 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-30 12:06 | SOL-USDT-SWAP | 118.74 | 121.29/118.38 | 119.46 | — | 1.4343 | 0.0082% | — | descartado_rr_baixo_setup_B |
| 2026-09-30 12:06 | XRP-USDT-SWAP | 1.4963 | 1.5218/1.4903 | 1.5153 | — | 0.01671 | 0.0100% | B/venda@1.4914 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-30 12:06 | DOGE-USDT-SWAP | 0.09472 | 0.09654/0.09418 | 0.09579 | — | 0.00130 | 0.0100% | — | invalidado_setup_B |
| 2026-09-30 12:06 | ARB-USDT-SWAP | 0.20190 | 0.20865/0.20097 | 0.20385 | sup 0.20053 (ha 8 candles) | 0.00370 | -0.0170% | — | sem_zona |
| 2026-09-30 12:06 | WLD-USDT-SWAP | 0.53960 | 0.55180/0.53320 | 0.54220 | — | 0.01602 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-09-30 12:06 | SUI-USDT-SWAP | 1.1598 | 1.1896/1.1460 | 1.1501 | sup 1.1409 (ha 14 candles) | 0.02436 | -0.0035% | — | sem_zona |
| 2026-09-30 12:06 | UNI-USDT-SWAP | 8.8320 | 9.0230/8.7400 | 8.9000 | sup 8.7210 (ha 11 candles) | 0.15157 | 0.0100% | — | sem_zona |
| 2026-09-30 12:06 | LINK-USDT-SWAP | 14.20 | 14.60/14.04 | 14.44 | — | 0.20329 | 0.0096% | B/venda@14.21 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-30 13:06 | BTC-USDT-SWAP | 84097.1 | 84258.0/83637.5 | 84097.1 | res 83816.7 (ha 16 candles) | 655.09 | 0.0035% | — | descartado_rr_baixo_setup_B |
| 2026-09-30 13:06 | ETH-USDT-SWAP | 2682.0 | 2688.0/2670.2 | 2682.0 | — | 21.78 | 0.0034% | B/venda@2720.0 (0t/2c) | zona_mapeada_setup_B |
| 2026-09-30 13:06 | SOL-USDT-SWAP | 119.25 | 119.48/117.83 | 119.25 | — | 1.4921 | 0.0038% | B/venda@119.69 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-30 13:06 | XRP-USDT-SWAP | 1.5045 | 1.5086/1.4885 | 1.5045 | — | 0.01746 | 0.0075% | — | invalidado_setup_B |
| 2026-09-30 13:06 | DOGE-USDT-SWAP | 0.09533 | 0.09560/0.09409 | 0.09533 | — | 0.00136 | 0.0100% | B/venda@0.09542 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-30 13:06 | ARB-USDT-SWAP | 0.20475 | 0.20525/0.19917 | 0.20475 | sup 0.20053 (ha 9 candles) | 0.00391 | -0.0199% | — | sem_zona |
| 2026-09-30 13:06 | WLD-USDT-SWAP | 0.53520 | 0.54230/0.52380 | 0.53520 | — | 0.01652 | 0.0100% | — | sem_zona |
| 2026-09-30 13:06 | SUI-USDT-SWAP | 1.1850 | 1.1854/1.1471 | 1.1850 | sup 1.1380 (ha 3 candles) | 0.02479 | -0.0005% | — | sem_zona |
| 2026-09-30 13:06 | UNI-USDT-SWAP | 9.0100 | 9.0250/8.8000 | 9.0100 | — | 0.16064 | 0.0100% | B/compra@9.0370 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-30 13:06 | LINK-USDT-SWAP | 14.24 | 14.30/14.11 | 14.24 | — | 0.20879 | 0.0073% | B/venda@14.21 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-30 14:06 | BTC-USDT-SWAP | 84316.4 | 84444.0/84088.0 | 84097.1 | res 85639.0 (ha 3 candles) | 657.10 | 0.0025% | — | sem_zona |
| 2026-09-30 14:06 | ETH-USDT-SWAP | 2694.5 | 2695.0/2680.6 | 2682.0 | — | 21.87 | 0.0020% | B/venda@2720.0 (0t/3c) | zona_mapeada_setup_B |
| 2026-09-30 14:06 | SOL-USDT-SWAP | 120.29 | 120.38/119.14 | 119.25 | — | 1.5129 | 0.0022% | — | invalidado_setup_B |
| 2026-09-30 14:06 | XRP-USDT-SWAP | 1.5112 | 1.5136/1.5040 | 1.5045 | — | 0.01754 | 0.0073% | B/compra@1.5004 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-30 14:06 | DOGE-USDT-SWAP | 0.09522 | 0.09575/0.09480 | 0.09533 | — | 0.00137 | 0.0100% | B/venda@0.09542 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-30 14:06 | ARB-USDT-SWAP | 0.20615 | 0.20703/0.20382 | 0.20475 | sup 0.20053 (ha 10 candles) | 0.00395 | -0.0177% | — | sem_zona |
| 2026-09-30 14:06 | WLD-USDT-SWAP | 0.54530 | 0.54690/0.53510 | 0.53520 | — | 0.01652 | 0.0100% | — | sem_zona |
| 2026-09-30 14:06 | SUI-USDT-SWAP | 1.1955 | 1.2072/1.1804 | 1.1850 | sup 1.1380 (ha 4 candles) | 0.02576 | 0.0037% | — | sem_zona |
| 2026-09-30 14:06 | UNI-USDT-SWAP | 9.0060 | 9.0420/8.9240 | 9.0100 | — | 0.16143 | 0.0100% | B/compra@9.0370 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-30 14:06 | LINK-USDT-SWAP | 14.44 | 14.48/14.21 | 14.24 | — | 0.21843 | 0.0066% | — | invalidado_setup_B |
| 2026-09-30 14:22 | BTC-USDT-SWAP | 84316.4 | 84444.0/84088.0 | 84097.1 | res 85639.0 (ha 3 candles) | 657.10 | 0.0021% | — | sem_zona |
| 2026-09-30 14:22 | ETH-USDT-SWAP | 2694.5 | 2695.0/2680.6 | 2682.0 | — | 21.87 | 0.0020% | B/venda@2720.0 (0t/3c) | zona_mapeada_setup_B |
| 2026-09-30 14:22 | SOL-USDT-SWAP | 120.29 | 120.38/119.14 | 119.25 | — | 1.5129 | 0.0019% | — | invalidado_setup_B |
| 2026-09-30 14:22 | XRP-USDT-SWAP | 1.5112 | 1.5136/1.5040 | 1.5045 | — | 0.01754 | 0.0072% | B/compra@1.5004 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-30 14:22 | DOGE-USDT-SWAP | 0.09522 | 0.09575/0.09480 | 0.09533 | — | 0.00137 | 0.0100% | B/venda@0.09542 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-30 14:22 | ARB-USDT-SWAP | 0.20615 | 0.20703/0.20382 | 0.20475 | sup 0.20053 (ha 10 candles) | 0.00395 | -0.0164% | — | sem_zona |
| 2026-09-30 14:22 | WLD-USDT-SWAP | 0.54530 | 0.54690/0.53510 | 0.53520 | — | 0.01652 | 0.0100% | — | sem_zona |
| 2026-09-30 14:22 | SUI-USDT-SWAP | 1.1955 | 1.2072/1.1804 | 1.1850 | sup 1.1380 (ha 4 candles) | 0.02576 | 0.0045% | — | sem_zona |
| 2026-09-30 14:22 | UNI-USDT-SWAP | 9.0060 | 9.0420/8.9240 | 9.0100 | — | 0.16143 | 0.0100% | B/compra@9.0370 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-30 14:22 | LINK-USDT-SWAP | 14.44 | 14.48/14.21 | 14.24 | — | 0.21843 | 0.0063% | — | invalidado_setup_B |
| 2026-09-30 14:42 | BTC-USDT-SWAP | 84316.4 | 84444.0/84088.0 | 84097.1 | res 85639.0 (ha 3 candles) | 657.10 | 0.0018% | — | sem_zona |
| 2026-09-30 14:42 | ETH-USDT-SWAP | 2694.5 | 2695.0/2680.6 | 2682.0 | — | 21.87 | 0.0023% | B/venda@2720.0 (0t/3c) | zona_mapeada_setup_B |
| 2026-09-30 14:42 | SOL-USDT-SWAP | 120.29 | 120.38/119.14 | 119.25 | — | 1.5129 | 0.0010% | — | invalidado_setup_B |
| 2026-09-30 14:42 | XRP-USDT-SWAP | 1.5112 | 1.5136/1.5040 | 1.5045 | — | 0.01754 | 0.0070% | B/compra@1.5004 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-30 14:42 | DOGE-USDT-SWAP | 0.09522 | 0.09575/0.09480 | 0.09533 | — | 0.00137 | 0.0100% | B/venda@0.09542 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-30 14:42 | ARB-USDT-SWAP | 0.20615 | 0.20703/0.20382 | 0.20475 | sup 0.20053 (ha 10 candles) | 0.00395 | -0.0144% | — | sem_zona |
| 2026-09-30 14:42 | WLD-USDT-SWAP | 0.54530 | 0.54690/0.53510 | 0.53520 | — | 0.01652 | 0.0100% | — | sem_zona |
| 2026-09-30 14:42 | SUI-USDT-SWAP | 1.1955 | 1.2072/1.1804 | 1.1850 | sup 1.1380 (ha 4 candles) | 0.02576 | 0.0053% | — | sem_zona |
| 2026-09-30 14:42 | UNI-USDT-SWAP | 9.0060 | 9.0420/8.9240 | 9.0100 | — | 0.16143 | 0.0100% | B/compra@9.0370 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-30 14:42 | LINK-USDT-SWAP | 14.44 | 14.48/14.21 | 14.24 | — | 0.21843 | 0.0059% | — | invalidado_setup_B |
| 2026-09-30 15:06 | BTC-USDT-SWAP | 83988.4 | 84388.0/83841.4 | 84097.1 | res 85639.0 (ha 4 candles) | 677.68 | 0.0019% | — | sem_zona |
| 2026-09-30 15:06 | ETH-USDT-SWAP | 2681.3 | 2696.7/2674.1 | 2682.0 | — | 22.88 | 0.0021% | B/venda@2720.0 (0t/4c) | zona_mapeada_setup_B |
| 2026-09-30 15:06 | SOL-USDT-SWAP | 119.12 | 120.53/118.78 | 119.25 | — | 1.5671 | 0.0001% | B/compra@119.76 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-30 15:06 | XRP-USDT-SWAP | 1.4986 | 1.5135/1.4957 | 1.5045 | — | 0.01799 | 0.0068% | B/compra@1.5004 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-30 15:06 | DOGE-USDT-SWAP | 0.09438 | 0.09548/0.09418 | 0.09533 | — | 0.00140 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-09-30 15:06 | ARB-USDT-SWAP | 0.20408 | 0.20624/0.20327 | 0.20475 | sup 0.20053 (ha 11 candles) | 0.00399 | -0.0119% | — | sem_zona |
| 2026-09-30 15:06 | WLD-USDT-SWAP | 0.53340 | 0.54820/0.53040 | 0.53520 | — | 0.01733 | 0.0100% | — | sem_zona |
| 2026-09-30 15:06 | SUI-USDT-SWAP | 1.1730 | 1.2004/1.1695 | 1.1850 | sup 1.1380 (ha 5 candles) | 0.02671 | 0.0057% | — | sem_zona |
| 2026-09-30 15:06 | UNI-USDT-SWAP | 8.8560 | 9.0100/8.8310 | 9.0100 | — | 0.16671 | 0.0100% | — | invalidado_setup_B |
| 2026-09-30 15:06 | LINK-USDT-SWAP | 14.37 | 14.45/14.31 | 14.24 | — | 0.21579 | 0.0060% | B/venda@14.48 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-30 16:06 | BTC-USDT-SWAP | 83912.6 | 84042.0/83750.8 | 84097.1 | res 85639.0 (ha 5 candles) | 682.52 | 0.0023% | B/compra@83439.3 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-30 16:06 | ETH-USDT-SWAP | 2677.8 | 2683.4/2672.4 | 2682.0 | — | 23.19 | 0.0021% | B/venda@2720.0 (0t/5c) | zona_mapeada_setup_B |
| 2026-09-30 16:06 | SOL-USDT-SWAP | 118.63 | 119.28/118.16 | 119.25 | — | 1.5743 | -0.0027% | B/compra@119.76 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-30 16:06 | XRP-USDT-SWAP | 1.4948 | 1.5003/1.4886 | 1.5045 | — | 0.01831 | 0.0059% | — | invalidado_setup_B |
| 2026-09-30 16:06 | DOGE-USDT-SWAP | 0.09412 | 0.09452/0.09365 | 0.09533 | — | 0.00141 | 0.0089% | — | sem_zona |
| 2026-09-30 16:06 | ARB-USDT-SWAP | 0.20332 | 0.20469/0.20229 | 0.20475 | sup 0.19917 (ha 3 candles) | 0.00403 | -0.0070% | — | sem_zona |
| 2026-09-30 16:06 | WLD-USDT-SWAP | 0.53060 | 0.53470/0.52240 | 0.53520 | — | 0.01749 | 0.0100% | — | sem_zona |
| 2026-09-30 16:06 | SUI-USDT-SWAP | 1.1612 | 1.1764/1.1539 | 1.1850 | sup 1.1380 (ha 6 candles) | 0.02719 | 0.0029% | — | sem_zona |
| 2026-09-30 16:06 | UNI-USDT-SWAP | 8.8570 | 8.8730/8.8080 | 9.0100 | — | 0.16379 | 0.0100% | B/compra@8.7670 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-30 16:06 | LINK-USDT-SWAP | 14.34 | 14.39/14.29 | 14.24 | — | 0.21621 | 0.0052% | B/venda@14.48 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-30 17:06 | BTC-USDT-SWAP | 83564.6 | 83930.0/83465.3 | 83564.6 | res 85639.0 (ha 6 candles) | 691.57 | 0.0030% | B/compra@83439.3 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-30 17:06 | ETH-USDT-SWAP | 2668.3 | 2679.6/2666.0 | 2668.3 | res 2737.9 (ha 7 candles) | 23.17 | 0.0014% | B/venda@2720.0 (0t/6c) | zona_mapeada_setup_B |
| 2026-09-30 17:06 | SOL-USDT-SWAP | 117.16 | 118.72/116.93 | 117.16 | — | 1.6186 | -0.0067% | B/compra@119.76 (0t/2c) | zona_mapeada_setup_B |
| 2026-09-30 17:06 | XRP-USDT-SWAP | 1.4884 | 1.4965/1.4841 | 1.4884 | — | 0.01832 | 0.0031% | — | sem_zona |
| 2026-09-30 17:06 | DOGE-USDT-SWAP | 0.09398 | 0.09438/0.09351 | 0.09398 | — | 0.00142 | 0.0073% | — | sem_zona |
| 2026-09-30 17:06 | ARB-USDT-SWAP | 0.20189 | 0.20411/0.20127 | 0.20189 | sup 0.19917 (ha 4 candles) | 0.00405 | -0.0005% | — | sem_zona |
| 2026-09-30 17:06 | WLD-USDT-SWAP | 0.53100 | 0.53440/0.52730 | 0.53100 | — | 0.01699 | 0.0100% | — | sem_zona |
| 2026-09-30 17:06 | SUI-USDT-SWAP | 1.1468 | 1.1643/1.1422 | 1.1468 | sup 1.1380 (ha 7 candles) | 0.02756 | -0.0004% | — | sem_zona |
| 2026-09-30 17:06 | UNI-USDT-SWAP | 8.8310 | 8.9280/8.8090 | 8.8310 | — | 0.16629 | 0.0100% | B/compra@8.7670 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-30 17:06 | LINK-USDT-SWAP | 14.23 | 14.37/14.20 | 14.23 | — | 0.22021 | 0.0046% | B/venda@14.48 (0t/2c) | zona_mapeada_setup_B |
| 2026-09-30 18:06 | BTC-USDT-SWAP | 83634.1 | 83735.5/83496.0 | 83564.6 | res 85639.0 (ha 7 candles) | 675.66 | 0.0037% | B/compra@83439.3 (2t/0c) | zona_mapeada_setup_B |
| 2026-09-30 18:06 | ETH-USDT-SWAP | 2681.1 | 2681.5/2667.2 | 2668.3 | res 2737.9 (ha 8 candles) | 22.82 | 0.0004% | B/venda@2720.0 (0t/7c) | zona_mapeada_setup_B |
| 2026-09-30 18:06 | SOL-USDT-SWAP | 117.96 | 118.11/117.12 | 117.16 | — | 1.6050 | -0.0092% | B/compra@119.76 (0t/3c) | zona_mapeada_setup_B |
| 2026-09-30 18:06 | XRP-USDT-SWAP | 1.4909 | 1.4960/1.4857 | 1.4884 | — | 0.01795 | 0.0008% | — | sem_zona |
| 2026-09-30 18:06 | DOGE-USDT-SWAP | 0.09436 | 0.09468/0.09393 | 0.09398 | — | 0.00138 | 0.0042% | — | sem_zona |
| 2026-09-30 18:06 | ARB-USDT-SWAP | 0.20445 | 0.20530/0.20140 | 0.20189 | sup 0.19917 (ha 5 candles) | 0.00410 | 0.0029% | — | sem_zona |
| 2026-09-30 18:06 | WLD-USDT-SWAP | 0.53510 | 0.54000/0.52990 | 0.53100 | — | 0.01700 | 0.0100% | — | sem_zona |
| 2026-09-30 18:06 | SUI-USDT-SWAP | 1.1627 | 1.1686/1.1466 | 1.1468 | sup 1.1380 (ha 8 candles) | 0.02804 | -0.0026% | — | sem_zona |
| 2026-09-30 18:06 | UNI-USDT-SWAP | 8.8480 | 8.9190/8.8100 | 8.8310 | — | 0.16350 | 0.0100% | B/compra@8.7670 (0t/2c) | zona_mapeada_setup_B |
| 2026-09-30 18:06 | LINK-USDT-SWAP | 14.30 | 14.35/14.20 | 14.23 | — | 0.21900 | 0.0062% | B/venda@14.48 (0t/3c) | zona_mapeada_setup_B |
| 2026-09-30 19:06 | BTC-USDT-SWAP | 83716.7 | 83791.7/83634.1 | 83564.6 | res 85639.0 (ha 8 candles) | 650.49 | 0.0041% | B/compra@83439.3 (2t/1c) | zona_mapeada_setup_B |
| 2026-09-30 19:06 | ETH-USDT-SWAP | 2683.2 | 2684.7/2680.5 | 2668.3 | res 2737.9 (ha 9 candles) | 21.88 | -0.0001% | — | zona_expirada_setup_B |
| 2026-09-30 19:06 | SOL-USDT-SWAP | 118.00 | 118.22/117.73 | 117.16 | — | 1.5629 | -0.0078% | B/compra@119.76 (0t/4c) | zona_mapeada_setup_B |
| 2026-09-30 19:06 | XRP-USDT-SWAP | 1.4882 | 1.4933/1.4853 | 1.4884 | — | 0.01744 | -0.0012% | — | sem_zona |
| 2026-09-30 19:06 | DOGE-USDT-SWAP | 0.09424 | 0.09459/0.09410 | 0.09398 | — | 0.00133 | 0.0033% | — | sem_zona |
| 2026-09-30 19:06 | ARB-USDT-SWAP | 0.20250 | 0.20544/0.20220 | 0.20189 | sup 0.19917 (ha 6 candles) | 0.00413 | 0.0052% | — | sem_zona |
| 2026-09-30 19:06 | WLD-USDT-SWAP | 0.53380 | 0.53940/0.53030 | 0.53100 | — | 0.01689 | 0.0100% | — | sem_zona |
| 2026-09-30 19:06 | SUI-USDT-SWAP | 1.1583 | 1.1675/1.1540 | 1.1468 | sup 1.1380 (ha 9 candles) | 0.02730 | 0.0001% | — | sem_zona |
| 2026-09-30 19:06 | UNI-USDT-SWAP | 8.8030 | 8.8850/8.7700 | 8.8310 | — | 0.16293 | 0.0100% | B/compra@8.7670 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-30 19:06 | LINK-USDT-SWAP | 14.35 | 14.35/14.30 | 14.23 | — | 0.21636 | 0.0067% | B/venda@14.48 (0t/4c) | zona_mapeada_setup_B |
| 2026-09-30 20:06 | BTC-USDT-SWAP | 83644.2 | 83815.1/83533.0 | 83564.6 | res 85639.0 (ha 9 candles) | 648.06 | 0.0050% | — | zona_expirada_setup_B |
| 2026-09-30 20:06 | ETH-USDT-SWAP | 2685.7 | 2691.9/2677.0 | 2668.3 | res 2737.9 (ha 10 candles) | 22.22 | 0.0007% | — | sem_zona |
| 2026-09-30 20:06 | SOL-USDT-SWAP | 118.07 | 118.48/117.54 | 117.16 | — | 1.5786 | -0.0076% | B/compra@119.76 (0t/5c) | zona_mapeada_setup_B |
| 2026-09-30 20:06 | XRP-USDT-SWAP | 1.4885 | 1.4940/1.4841 | 1.4884 | — | 0.01746 | -0.0004% | — | sem_zona |
| 2026-09-30 20:06 | DOGE-USDT-SWAP | 0.09443 | 0.09478/0.09390 | 0.09398 | — | 0.00135 | 0.0053% | B/compra@0.09519 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-30 20:06 | ARB-USDT-SWAP | 0.20325 | 0.20439/0.20095 | 0.20189 | sup 0.19917 (ha 7 candles) | 0.00418 | 0.0058% | — | sem_zona |
| 2026-09-30 20:06 | WLD-USDT-SWAP | 0.53880 | 0.54150/0.52600 | 0.53100 | — | 0.01624 | 0.0100% | — | sem_zona |
| 2026-09-30 20:06 | SUI-USDT-SWAP | 1.1641 | 1.1764/1.1491 | 1.1468 | sup 1.1422 (ha 3 candles) | 0.02806 | 0.0051% | — | sem_zona |
| 2026-09-30 20:06 | UNI-USDT-SWAP | 8.8730 | 8.9050/8.7550 | 8.8310 | — | 0.16779 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-09-30 20:06 | LINK-USDT-SWAP | 14.37 | 14.42/14.26 | 14.23 | — | 0.21914 | 0.0091% | B/venda@14.48 (0t/5c) | zona_mapeada_setup_B |
| 2026-09-30 21:06 | BTC-USDT-SWAP | 83579.9 | 83800.0/83480.0 | 83579.9 | res 85639.0 (ha 10 candles) | 616.11 | 0.0054% | B/compra@83764.7 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-30 21:06 | ETH-USDT-SWAP | 2684.7 | 2693.3/2683.3 | 2684.7 | res 2737.9 (ha 11 candles) | 20.78 | 0.0018% | — | sem_zona |
| 2026-09-30 21:06 | SOL-USDT-SWAP | 118.06 | 118.48/117.93 | 118.06 | — | 1.4993 | -0.0063% | B/compra@119.76 (0t/6c) | zona_mapeada_setup_B |
| 2026-09-30 21:06 | XRP-USDT-SWAP | 1.4891 | 1.4934/1.4848 | 1.4891 | — | 0.01668 | -0.0006% | — | sem_zona |
| 2026-09-30 21:06 | DOGE-USDT-SWAP | 0.09450 | 0.09479/0.09432 | 0.09450 | — | 0.00130 | 0.0057% | B/compra@0.09519 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-30 21:06 | ARB-USDT-SWAP | 0.20281 | 0.20436/0.20255 | 0.20281 | sup 0.19917 (ha 8 candles) | 0.00404 | 0.0042% | — | sem_zona |
| 2026-09-30 21:06 | WLD-USDT-SWAP | 0.53510 | 0.54410/0.53360 | 0.53510 | — | 0.01615 | 0.0100% | — | sem_zona |
| 2026-09-30 21:06 | SUI-USDT-SWAP | 1.1637 | 1.1719/1.1616 | 1.1637 | sup 1.1422 (ha 4 candles) | 0.02732 | 0.0060% | — | sem_zona |
| 2026-09-30 21:06 | UNI-USDT-SWAP | 8.8740 | 8.9220/8.8590 | 8.8740 | — | 0.16471 | 0.0100% | — | sem_zona |
| 2026-09-30 21:06 | LINK-USDT-SWAP | 14.36 | 14.43/14.35 | 14.36 | — | 0.21250 | 0.0084% | — | descartado_rr_baixo_setup_B |
