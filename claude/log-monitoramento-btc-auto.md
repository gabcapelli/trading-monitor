# Log de Monitoramento Automatico -- Multi-Par (script gratuito, GitHub Actions)

> Gerado por script Python sem LLM (ver monitor/fetch_and_check.py). Fonte: OKX. Cobre os pares em PAIRS (configuracao no topo do script) -- BTC-USDT-SWAP e os demais adicionados na expansao de 07/09/2026. Leitura e MECANICA (regras objetivas da secao 4 do plano), sem a prosa qualitativa que o Claude gerava -- cole este log numa conversa do Claude se quiser a leitura interpretativa.

| Data/Hora (BRT) | Par | Close 1h | High/Low 1h | Close 4h | Swing 1h ref | ATR 1h | Funding | Zona ativa | Status checklist |
|---|---|---|---|---|---|---|---|---|---|
| 2026-10-06 05:05 | BTC-USDT-SWAP | 85525.6 | 85596.0/85230.0 | 85525.6 | — | 292.94 | 0.0042% | B/venda@85137.5 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-06 05:05 | ETH-USDT-SWAP | 2706.4 | 2709.0/2694.4 | 2706.4 | — | 9.6386 | 0.0034% | B/venda@2706.4 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-06 05:05 | SOL-USDT-SWAP | 120.14 | 120.25/119.64 | 120.14 | — | 0.56714 | -0.0000% | — | invalidado_setup_B |
| 2026-10-06 05:05 | XRP-USDT-SWAP | 1.4992 | 1.5011/1.4941 | 1.4992 | — | 0.00716 | 0.0086% | B/compra@1.5004 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-06 05:05 | DOGE-USDT-SWAP | 0.09464 | 0.09473/0.09423 | 0.09464 | — | 0.00050 | 0.0100% | — | sem_zona |
| 2026-10-06 05:05 | ARB-USDT-SWAP | 0.20271 | 0.20306/0.20053 | 0.20271 | — | 0.00265 | -0.0061% | — | sem_zona |
| 2026-10-06 05:05 | WLD-USDT-SWAP | 0.56310 | 0.56390/0.55590 | 0.56310 | — | 0.00818 | 0.0094% | — | sem_zona |
| 2026-10-06 05:05 | SUI-USDT-SWAP | 1.1931 | 1.1946/1.1852 | 1.1931 | — | 0.01315 | -0.0055% | B/venda@1.2112 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-06 05:05 | UNI-USDT-SWAP | 8.8420 | 8.8530/8.7870 | 8.8420 | — | 0.08843 | 0.0096% | — | descartado_rr_baixo_setup_B |
| 2026-10-06 05:05 | LINK-USDT-SWAP | 13.93 | 13.96/13.80 | 13.93 | — | 0.07521 | 0.0091% | — | descartado_rr_baixo_setup_B |
| 2026-10-06 06:05 | BTC-USDT-SWAP | 85982.9 | 86017.0/85511.2 | 85525.6 | — | 307.06 | 0.0033% | B/venda@85137.5 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-06 06:05 | ETH-USDT-SWAP | 2715.4 | 2715.4/2706.4 | 2706.4 | — | 9.8250 | 0.0017% | — | invalidado_setup_B |
| 2026-10-06 06:05 | SOL-USDT-SWAP | 120.47 | 120.78/120.12 | 120.14 | — | 0.59000 | 0.0006% | B/venda@120.74 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-06 06:05 | XRP-USDT-SWAP | 1.5032 | 1.5061/1.4990 | 1.4992 | — | 0.00724 | 0.0078% | B/compra@1.5004 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-06 06:05 | DOGE-USDT-SWAP | 0.09489 | 0.09495/0.09462 | 0.09464 | — | 0.00050 | 0.0100% | B/compra@0.09519 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-06 06:05 | ARB-USDT-SWAP | 0.20250 | 0.20369/0.20238 | 0.20271 | — | 0.00245 | -0.0073% | — | sem_zona |
| 2026-10-06 06:05 | WLD-USDT-SWAP | 0.56250 | 0.56520/0.56180 | 0.56310 | — | 0.00788 | 0.0076% | — | sem_zona |
| 2026-10-06 06:05 | SUI-USDT-SWAP | 1.2019 | 1.2060/1.1922 | 1.1931 | — | 0.01379 | -0.0072% | B/venda@1.2112 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-06 06:05 | UNI-USDT-SWAP | 8.8630 | 8.8820/8.8400 | 8.8420 | — | 0.07921 | 0.0065% | — | sem_zona |
| 2026-10-06 06:05 | LINK-USDT-SWAP | 13.97 | 14.00/13.93 | 13.93 | — | 0.07621 | 0.0096% | — | sem_zona |
| 2026-10-06 07:05 | BTC-USDT-SWAP | 85954.6 | 86221.4/85601.0 | 85525.6 | — | 332.89 | 0.0031% | B/venda@85137.5 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-06 07:05 | ETH-USDT-SWAP | 2709.1 | 2720.0/2692.3 | 2706.4 | — | 11.32 | 0.0018% | B/compra@2714.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-06 07:05 | SOL-USDT-SWAP | 119.49 | 120.61/118.73 | 120.14 | — | 0.69357 | 0.0002% | B/venda@120.74 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-06 07:05 | XRP-USDT-SWAP | 1.5027 | 1.5103/1.4946 | 1.4992 | — | 0.00784 | 0.0070% | B/compra@1.5004 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-06 07:05 | DOGE-USDT-SWAP | 0.09493 | 0.09526/0.09432 | 0.09464 | — | 0.00051 | 0.0100% | — | invalidado_setup_B |
| 2026-10-06 07:05 | ARB-USDT-SWAP | 0.20112 | 0.20296/0.19834 | 0.20271 | — | 0.00252 | -0.0096% | — | sem_zona |
| 2026-10-06 07:05 | WLD-USDT-SWAP | 0.56190 | 0.56540/0.55340 | 0.56310 | — | 0.00830 | 0.0062% | — | sem_zona |
| 2026-10-06 07:05 | SUI-USDT-SWAP | 1.1921 | 1.2042/1.1828 | 1.1931 | — | 0.01422 | -0.0082% | — | zona_expirada_setup_B |
| 2026-10-06 07:05 | UNI-USDT-SWAP | 8.8580 | 8.8850/8.7950 | 8.8420 | — | 0.07929 | 0.0043% | — | sem_zona |
| 2026-10-06 07:05 | LINK-USDT-SWAP | 13.95 | 14.01/13.88 | 13.93 | — | 0.08050 | 0.0088% | — | sem_zona |
| 2026-10-06 08:05 | BTC-USDT-SWAP | 86123.5 | 86232.7/85918.1 | 85525.6 | — | 339.30 | 0.0031% | B/venda@85137.5 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-06 08:05 | ETH-USDT-SWAP | 2712.6 | 2716.6/2707.4 | 2706.4 | — | 11.32 | 0.0016% | B/compra@2714.0 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-06 08:05 | SOL-USDT-SWAP | 120.20 | 120.52/119.40 | 120.14 | — | 0.73643 | 0.0003% | B/venda@120.74 (1t/1c) | zona_mapeada_setup_B |
| 2026-10-06 08:05 | XRP-USDT-SWAP | 1.5075 | 1.5100/1.5021 | 1.4992 | — | 0.00806 | 0.0081% | — | descartado_rr_baixo_setup_B |
| 2026-10-06 08:05 | DOGE-USDT-SWAP | 0.09537 | 0.09547/0.09485 | 0.09464 | — | 0.00051 | 0.0100% | B/venda@0.09542 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-06 08:05 | ARB-USDT-SWAP | 0.20239 | 0.20298/0.20075 | 0.20271 | — | 0.00241 | -0.0081% | — | sem_zona |
| 2026-10-06 08:05 | WLD-USDT-SWAP | 0.56430 | 0.56780/0.56000 | 0.56310 | — | 0.00829 | 0.0062% | — | sem_zona |
| 2026-10-06 08:05 | SUI-USDT-SWAP | 1.1962 | 1.2019/1.1898 | 1.1931 | — | 0.01272 | -0.0070% | B/venda@1.1886 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-06 08:05 | UNI-USDT-SWAP | 8.8730 | 8.9260/8.8510 | 8.8420 | — | 0.07821 | 0.0036% | — | sem_zona |
| 2026-10-06 08:05 | LINK-USDT-SWAP | 14.02 | 14.07/13.95 | 13.93 | — | 0.08507 | 0.0097% | B/compra@14.04 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-06 09:05 | BTC-USDT-SWAP | 86208.4 | 86369.4/86035.4 | 86208.4 | — | 342.69 | 0.0040% | B/venda@85137.5 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-06 09:05 | ETH-USDT-SWAP | 2713.0 | 2716.6/2708.3 | 2713.0 | — | 11.34 | 0.0021% | B/compra@2714.0 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-06 09:05 | SOL-USDT-SWAP | 120.27 | 120.38/119.89 | 120.27 | — | 0.75000 | 0.0014% | B/venda@120.74 (1t/2c) | zona_mapeada_setup_B |
| 2026-10-06 09:05 | XRP-USDT-SWAP | 1.5126 | 1.5148/1.5048 | 1.5126 | — | 0.00840 | 0.0100% | — | sem_zona |
| 2026-10-06 09:05 | DOGE-USDT-SWAP | 0.09572 | 0.09578/0.09526 | 0.09572 | — | 0.00053 | 0.0100% | — | invalidado_setup_B |
| 2026-10-06 09:05 | ARB-USDT-SWAP | 0.20142 | 0.20255/0.20084 | 0.20142 | res 0.21098 (ha 14 candles) | 0.00234 | -0.0041% | — | sem_zona |
| 2026-10-06 09:05 | WLD-USDT-SWAP | 0.56640 | 0.56650/0.55940 | 0.56640 | — | 0.00780 | 0.0085% | B/venda@0.57120 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-06 09:05 | SUI-USDT-SWAP | 1.2045 | 1.2053/1.1930 | 1.2045 | — | 0.01286 | -0.0027% | B/venda@1.1886 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-06 09:05 | UNI-USDT-SWAP | 8.8960 | 8.9070/8.8360 | 8.8960 | — | 0.08029 | 0.0055% | B/compra@8.9360 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-06 09:05 | LINK-USDT-SWAP | 14.06 | 14.09/14.01 | 14.06 | — | 0.08793 | 0.0096% | B/compra@14.04 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-06 10:05 | BTC-USDT-SWAP | 86177.6 | 86380.0/86073.9 | 86208.4 | — | 352.20 | 0.0049% | B/venda@85137.5 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-06 10:05 | ETH-USDT-SWAP | 2714.4 | 2717.3/2705.9 | 2713.0 | — | 11.57 | 0.0028% | — | descartado_rr_baixo_setup_B |
| 2026-10-06 10:05 | SOL-USDT-SWAP | 120.36 | 120.58/119.99 | 120.27 | — | 0.73429 | 0.0018% | B/venda@120.74 (1t/3c) | zona_mapeada_setup_B |
| 2026-10-06 10:05 | XRP-USDT-SWAP | 1.5113 | 1.5146/1.5071 | 1.5126 | — | 0.00842 | 0.0100% | — | sem_zona |
| 2026-10-06 10:05 | DOGE-USDT-SWAP | 0.09549 | 0.09578/0.09529 | 0.09572 | — | 0.00053 | 0.0100% | — | sem_zona |
| 2026-10-06 10:05 | ARB-USDT-SWAP | 0.20058 | 0.20177/0.20018 | 0.20142 | res 0.21098 (ha 15 candles) | 0.00224 | -0.0038% | B/compra@0.19917 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-06 10:05 | WLD-USDT-SWAP | 0.56520 | 0.56750/0.56180 | 0.56640 | — | 0.00770 | 0.0100% | B/venda@0.57120 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-06 10:05 | SUI-USDT-SWAP | 1.1936 | 1.2058/1.1921 | 1.2045 | — | 0.01284 | 0.0023% | B/venda@1.1886 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-06 10:05 | UNI-USDT-SWAP | 8.8890 | 8.9030/8.8270 | 8.8960 | — | 0.07921 | 0.0084% | B/compra@8.9360 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-06 10:05 | LINK-USDT-SWAP | 14.01 | 14.07/13.96 | 14.06 | — | 0.09050 | 0.0080% | — | invalidado_setup_B |
| 2026-10-06 11:05 | BTC-USDT-SWAP | 86278.8 | 86449.5/85924.1 | 86208.4 | — | 364.10 | 0.0053% | B/venda@85137.5 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-06 11:05 | ETH-USDT-SWAP | 2713.4 | 2719.8/2708.0 | 2713.0 | — | 11.72 | 0.0027% | B/venda@2721.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-06 11:05 | SOL-USDT-SWAP | 120.83 | 121.12/120.09 | 120.27 | — | 0.75214 | 0.0019% | B/venda@120.74 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-06 11:05 | XRP-USDT-SWAP | 1.5141 | 1.5170/1.5061 | 1.5126 | — | 0.00877 | 0.0100% | — | sem_zona |
| 2026-10-06 11:05 | DOGE-USDT-SWAP | 0.09599 | 0.09620/0.09518 | 0.09572 | — | 0.00057 | 0.0100% | B/venda@0.09608 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-06 11:05 | ARB-USDT-SWAP | 0.20039 | 0.20205/0.19968 | 0.20142 | res 0.21098 (ha 16 candles) | 0.00229 | -0.0053% | B/compra@0.19917 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-06 11:05 | WLD-USDT-SWAP | 0.56450 | 0.57070/0.56310 | 0.56640 | — | 0.00790 | 0.0090% | — | descartado_rr_baixo_setup_B |
| 2026-10-06 11:05 | SUI-USDT-SWAP | 1.1949 | 1.2035/1.1880 | 1.2045 | — | 0.01305 | 0.0049% | — | invalidado_setup_B |
| 2026-10-06 11:05 | UNI-USDT-SWAP | 8.8660 | 8.9380/8.8590 | 8.8960 | — | 0.08164 | 0.0100% | — | invalidado_setup_B |
| 2026-10-06 11:05 | LINK-USDT-SWAP | 13.99 | 14.05/13.96 | 14.06 | — | 0.09143 | 0.0065% | — | sem_zona |
| 2026-10-06 12:05 | BTC-USDT-SWAP | 86561.4 | 86587.5/85912.9 | 86208.4 | — | 396.70 | 0.0047% | — | zona_expirada_setup_B |
| 2026-10-06 12:05 | ETH-USDT-SWAP | 2720.8 | 2721.8/2703.6 | 2713.0 | — | 12.42 | 0.0022% | B/venda@2721.0 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-06 12:05 | SOL-USDT-SWAP | 121.68 | 121.72/120.52 | 120.27 | — | 0.81071 | 0.0020% | — | invalidado_setup_B |
| 2026-10-06 12:05 | XRP-USDT-SWAP | 1.5221 | 1.5226/1.5094 | 1.5126 | — | 0.00929 | 0.0100% | — | sem_zona |
| 2026-10-06 12:05 | DOGE-USDT-SWAP | 0.09624 | 0.09630/0.09547 | 0.09572 | — | 0.00060 | 0.0100% | — | invalidado_setup_B |
| 2026-10-06 12:05 | ARB-USDT-SWAP | 0.20267 | 0.20294/0.19916 | 0.20142 | res 0.21098 (ha 17 candles) | 0.00232 | -0.0079% | — | descartado_rr_baixo_setup_B |
| 2026-10-06 12:05 | WLD-USDT-SWAP | 0.56620 | 0.56820/0.55760 | 0.56640 | — | 0.00804 | 0.0084% | — | sem_zona |
| 2026-10-06 12:05 | SUI-USDT-SWAP | 1.1983 | 1.1996/1.1880 | 1.2045 | — | 0.01285 | 0.0051% | — | sem_zona |
| 2026-10-06 12:05 | UNI-USDT-SWAP | 8.8480 | 8.8840/8.7970 | 8.8960 | — | 0.08164 | 0.0100% | B/compra@8.8530 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-06 12:05 | LINK-USDT-SWAP | 14.08 | 14.08/13.93 | 14.06 | — | 0.09800 | 0.0048% | B/compra@14.13 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-06 13:05 | BTC-USDT-SWAP | 85681.6 | 86656.0/85681.6 | 85681.6 | — | 427.89 | 0.0034% | B/venda@85639.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-06 13:05 | ETH-USDT-SWAP | 2700.7 | 2724.4/2700.0 | 2700.7 | — | 12.92 | 0.0019% | — | descartado_rr_baixo_setup_B |
| 2026-10-06 13:05 | SOL-USDT-SWAP | 120.44 | 121.95/120.42 | 120.44 | — | 0.86214 | 0.0021% | B/venda@119.96 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-06 13:05 | XRP-USDT-SWAP | 1.5019 | 1.5236/1.5013 | 1.5019 | — | 0.00991 | 0.0100% | — | sem_zona |
| 2026-10-06 13:05 | DOGE-USDT-SWAP | 0.09533 | 0.09634/0.09529 | 0.09533 | — | 0.00062 | 0.0100% | B/venda@0.09542 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-06 13:05 | ARB-USDT-SWAP | 0.20123 | 0.20428/0.20089 | 0.20123 | res 0.21098 (ha 18 candles) | 0.00237 | -0.0042% | — | sem_zona |
| 2026-10-06 13:05 | WLD-USDT-SWAP | 0.55430 | 0.56750/0.55110 | 0.55430 | — | 0.00861 | 0.0072% | B/venda@0.55180 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-06 13:05 | SUI-USDT-SWAP | 1.1855 | 1.2004/1.1848 | 1.1855 | — | 0.01266 | 0.0019% | — | sem_zona |
| 2026-10-06 13:05 | UNI-USDT-SWAP | 8.6650 | 8.8630/8.6610 | 8.6650 | — | 0.08614 | 0.0100% | — | invalidado_setup_B |
| 2026-10-06 13:05 | LINK-USDT-SWAP | 13.94 | 14.12/13.93 | 13.94 | — | 0.10143 | 0.0031% | — | invalidado_setup_B |
| 2026-10-08 12:05 | BTC-USDT-SWAP | 82659.9 | 82748.1/82090.9 | 82463.9 | — | 535.84 | 0.0070% | — | zona_expirada_setup_B |
| 2026-10-08 12:05 | ETH-USDT-SWAP | 2530.3 | 2535.8/2516.3 | 2536.4 | sup 2542.8 (ha 10 candles) | 20.06 | 0.0050% | A/venda@2542.8 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-08 12:05 | SOL-USDT-SWAP | 112.44 | 112.76/112.08 | 113.12 | sup 114.09 (ha 10 candles) | 1.0193 | 0.0009% | — | zona_expirada_setup_B |
| 2026-10-08 12:05 | XRP-USDT-SWAP | 1.4039 | 1.4082/1.3976 | 1.3970 | — | 0.01332 | 0.0024% | — | sem_zona |
| 2026-10-08 12:05 | DOGE-USDT-SWAP | 0.08708 | 0.08751/0.08687 | 0.08712 | sup 0.08502 (ha 10 candles) | 0.00098 | 0.0096% | — | zona_expirada_setup_B |
| 2026-10-08 12:05 | ARB-USDT-SWAP | 0.18227 | 0.18439/0.18151 | 0.18412 | sup 0.18036 (ha 10 candles) | 0.00291 | 0.0055% | — | sem_zona |
| 2026-10-08 12:05 | WLD-USDT-SWAP | 0.51170 | 0.51730/0.50970 | 0.51780 | sup 0.50780 (ha 10 candles) | 0.01031 | 0.0100% | — | zona_expirada_setup_B |
| 2026-10-08 12:05 | SUI-USDT-SWAP | 1.0988 | 1.1071/1.0942 | 1.1162 | sup 1.1157 (ha 10 candles) | 0.01731 | 0.0077% | A/venda@1.1157 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-08 12:05 | UNI-USDT-SWAP | 7.6170 | 7.6610/7.5350 | 7.7180 | sup 7.6830 (ha 8 candles) | 0.12186 | 0.0100% | A/venda@7.6830 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-08 12:05 | LINK-USDT-SWAP | 12.96 | 13.03/12.92 | 13.00 | sup 12.93 (ha 10 candles) | 0.13329 | 0.0034% | — | sem_zona |
| 2026-10-08 13:05 | BTC-USDT-SWAP | 80991.9 | 82659.9/80910.4 | 80991.9 | — | 630.25 | 0.0062% | — | sem_zona |
| 2026-10-08 13:05 | ETH-USDT-SWAP | 2434.3 | 2530.4/2428.0 | 2434.3 | sup 2542.8 (ha 11 candles) | 26.50 | 0.0034% | A/venda@2542.8 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-08 13:05 | SOL-USDT-SWAP | 108.50 | 112.45/108.00 | 108.50 | sup 114.09 (ha 11 candles) | 1.2807 | -0.0021% | A/venda@114.09 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-08 13:05 | XRP-USDT-SWAP | 1.3453 | 1.4051/1.3400 | 1.3453 | — | 0.01736 | -0.0029% | — | sem_zona |
| 2026-10-08 13:05 | DOGE-USDT-SWAP | 0.08262 | 0.08714/0.08183 | 0.08262 | sup 0.08502 (ha 11 candles) | 0.00130 | 0.0054% | A/venda@0.08502 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-08 13:05 | ARB-USDT-SWAP | 0.16605 | 0.18234/0.16142 | 0.16605 | sup 0.18036 (ha 11 candles) | 0.00424 | 0.0063% | A/venda@0.18036 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-08 13:05 | WLD-USDT-SWAP | 0.47780 | 0.51210/0.47380 | 0.47780 | sup 0.50780 (ha 11 candles) | 0.01238 | 0.0100% | A/venda@0.50780 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-08 13:05 | SUI-USDT-SWAP | 1.0260 | 1.0999/1.0201 | 1.0260 | sup 1.1157 (ha 11 candles) | 0.02179 | 0.0081% | A/venda@1.1157 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-08 13:05 | UNI-USDT-SWAP | 7.3180 | 7.6200/7.1830 | 7.3180 | sup 7.6830 (ha 9 candles) | 0.14479 | 0.0100% | A/venda@7.6830 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-08 13:05 | LINK-USDT-SWAP | 12.35 | 12.96/12.30 | 12.35 | sup 12.93 (ha 11 candles) | 0.17300 | -0.0015% | A/venda@12.93 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-08 14:06 | BTC-USDT-SWAP | 80908.4 | 81413.9/80721.6 | 80991.9 | — | 650.78 | 0.0050% | — | sem_zona |
| 2026-10-08 14:06 | ETH-USDT-SWAP | 2415.4 | 2440.8/2408.0 | 2434.3 | sup 2542.8 (ha 12 candles) | 27.91 | 0.0031% | A/venda@2542.8 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-08 14:06 | SOL-USDT-SWAP | 107.64 | 109.08/107.51 | 108.50 | sup 114.09 (ha 12 candles) | 1.3371 | -0.0024% | A/venda@114.09 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-08 14:06 | XRP-USDT-SWAP | 1.3431 | 1.3615/1.3359 | 1.3453 | — | 0.01861 | -0.0041% | — | sem_zona |
| 2026-10-08 14:06 | DOGE-USDT-SWAP | 0.08217 | 0.08362/0.08202 | 0.08262 | sup 0.08502 (ha 12 candles) | 0.00138 | 0.0014% | A/venda@0.08502 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-08 14:06 | ARB-USDT-SWAP | 0.16633 | 0.16914/0.16518 | 0.16605 | sup 0.18036 (ha 12 candles) | 0.00440 | 0.0059% | A/venda@0.18036 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-08 14:06 | WLD-USDT-SWAP | 0.46950 | 0.48380/0.46750 | 0.47780 | sup 0.50780 (ha 12 candles) | 0.01309 | 0.0100% | A/venda@0.50780 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-08 14:06 | SUI-USDT-SWAP | 1.0242 | 1.0464/1.0183 | 1.0260 | sup 1.1157 (ha 12 candles) | 0.02239 | 0.0056% | A/venda@1.1157 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-08 14:06 | UNI-USDT-SWAP | 7.1450 | 7.3750/7.1260 | 7.3180 | sup 7.6830 (ha 10 candles) | 0.15600 | 0.0100% | A/venda@7.6830 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-08 14:06 | LINK-USDT-SWAP | 12.34 | 12.52/12.29 | 12.35 | sup 12.93 (ha 12 candles) | 0.18264 | -0.0055% | A/venda@12.93 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-08 15:05 | BTC-USDT-SWAP | 80718.0 | 80987.0/80351.0 | 80991.9 | — | 655.04 | 0.0053% | — | sem_zona |
| 2026-10-08 15:05 | ETH-USDT-SWAP | 2417.1 | 2426.4/2405.0 | 2434.3 | sup 2542.8 (ha 13 candles) | 28.21 | 0.0019% | A/venda@2542.8 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-08 15:05 | SOL-USDT-SWAP | 106.32 | 107.86/105.61 | 108.50 | sup 114.09 (ha 13 candles) | 1.4350 | -0.0023% | A/venda@114.09 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-08 15:05 | XRP-USDT-SWAP | 1.3262 | 1.3459/1.3176 | 1.3453 | — | 0.01973 | -0.0019% | — | sem_zona |
| 2026-10-08 15:05 | DOGE-USDT-SWAP | 0.08147 | 0.08235/0.08092 | 0.08262 | sup 0.08502 (ha 13 candles) | 0.00144 | -0.0034% | A/venda@0.08502 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-08 15:05 | ARB-USDT-SWAP | 0.16381 | 0.16662/0.16210 | 0.16605 | sup 0.18036 (ha 13 candles) | 0.00452 | 0.0050% | A/venda@0.18036 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-08 15:05 | WLD-USDT-SWAP | 0.46130 | 0.47070/0.45880 | 0.47780 | sup 0.50780 (ha 13 candles) | 0.01347 | 0.0091% | A/venda@0.50780 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-08 15:05 | SUI-USDT-SWAP | 1.0024 | 1.0276/0.99710 | 1.0260 | sup 1.1157 (ha 13 candles) | 0.02362 | 0.0045% | A/venda@1.1157 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-08 15:05 | UNI-USDT-SWAP | 7.0480 | 7.1820/6.9870 | 7.3180 | sup 7.6830 (ha 11 candles) | 0.16371 | 0.0100% | A/venda@7.6830 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-08 15:05 | LINK-USDT-SWAP | 12.18 | 12.37/12.06 | 12.35 | sup 12.93 (ha 13 candles) | 0.19457 | -0.0095% | A/venda@12.93 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-08 16:05 | BTC-USDT-SWAP | 81460.1 | 81525.7/80500.0 | 80991.9 | — | 675.94 | 0.0040% | — | sem_zona |
| 2026-10-08 16:05 | ETH-USDT-SWAP | 2445.5 | 2447.7/2411.3 | 2434.3 | sup 2542.8 (ha 14 candles) | 28.50 | -0.0024% | A/venda@2542.8 (0t/4c) | zona_mapeada_setup_A |
| 2026-10-08 16:05 | SOL-USDT-SWAP | 108.02 | 108.21/105.96 | 108.50 | sup 114.09 (ha 14 candles) | 1.4793 | -0.0025% | A/venda@114.09 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-08 16:05 | XRP-USDT-SWAP | 1.3591 | 1.3628/1.3239 | 1.3453 | — | 0.02033 | -0.0025% | — | sem_zona |
| 2026-10-08 16:05 | DOGE-USDT-SWAP | 0.08300 | 0.08306/0.08137 | 0.08262 | sup 0.08502 (ha 14 candles) | 0.00130 | -0.0080% | A/venda@0.08502 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-08 16:05 | ARB-USDT-SWAP | 0.16842 | 0.16925/0.16320 | 0.16605 | sup 0.16142 (ha 3 candles) | 0.00457 | 0.0039% | A/venda@0.18036 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-08 16:05 | WLD-USDT-SWAP | 0.47250 | 0.47380/0.45860 | 0.47780 | sup 0.50780 (ha 14 candles) | 0.01369 | 0.0054% | A/venda@0.50780 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-08 16:05 | SUI-USDT-SWAP | 1.0263 | 1.0300/1.0002 | 1.0260 | sup 1.1157 (ha 14 candles) | 0.02433 | -0.0029% | A/venda@1.1157 (0t/4c) | zona_mapeada_setup_A |
| 2026-10-08 16:05 | UNI-USDT-SWAP | 7.1950 | 7.2170/7.0270 | 7.3180 | sup 7.6830 (ha 12 candles) | 0.16750 | 0.0100% | A/venda@7.6830 (0t/4c) | zona_mapeada_setup_A |
| 2026-10-08 16:05 | LINK-USDT-SWAP | 12.38 | 12.42/12.13 | 12.35 | sup 12.93 (ha 14 candles) | 0.19807 | -0.0113% | A/venda@12.93 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-08 17:05 | BTC-USDT-SWAP | 81744.7 | 81816.5/81385.9 | 81744.7 | — | 673.61 | 0.0026% | — | sem_zona |
| 2026-10-08 17:05 | ETH-USDT-SWAP | 2463.2 | 2464.6/2441.8 | 2463.2 | sup 2542.8 (ha 15 candles) | 29.02 | -0.0062% | A/venda@2542.8 (0t/5c) | zona_mapeada_setup_A |
| 2026-10-08 17:05 | SOL-USDT-SWAP | 109.10 | 109.39/107.99 | 109.10 | sup 114.09 (ha 15 candles) | 1.5136 | -0.0048% | A/venda@114.09 (0t/4c) | zona_mapeada_setup_A |
| 2026-10-08 17:05 | XRP-USDT-SWAP | 1.3718 | 1.3764/1.3588 | 1.3718 | — | 0.02059 | -0.0067% | — | sem_zona |
| 2026-10-08 17:05 | DOGE-USDT-SWAP | 0.08371 | 0.08386/0.08299 | 0.08371 | sup 0.08502 (ha 15 candles) | 0.00129 | -0.0127% | A/venda@0.08502 (0t/4c) | zona_mapeada_setup_A |
| 2026-10-08 17:05 | ARB-USDT-SWAP | 0.17107 | 0.17163/0.16842 | 0.17107 | sup 0.16142 (ha 4 candles) | 0.00459 | -0.0027% | A/venda@0.18036 (0t/4c) | zona_mapeada_setup_A |
| 2026-10-08 17:05 | WLD-USDT-SWAP | 0.47930 | 0.48180/0.47140 | 0.47930 | sup 0.50780 (ha 15 candles) | 0.01360 | -0.0025% | A/venda@0.50780 (0t/4c) | zona_mapeada_setup_A |
| 2026-10-08 17:05 | SUI-USDT-SWAP | 1.0388 | 1.0470/1.0259 | 1.0388 | sup 1.1157 (ha 15 candles) | 0.02468 | -0.0130% | A/venda@1.1157 (0t/5c) | zona_mapeada_setup_A |
| 2026-10-08 17:05 | UNI-USDT-SWAP | 7.2530 | 7.2760/7.1840 | 7.2530 | sup 7.6830 (ha 13 candles) | 0.16214 | 0.0100% | A/venda@7.6830 (0t/5c) | zona_mapeada_setup_A |
| 2026-10-08 17:05 | LINK-USDT-SWAP | 12.51 | 12.54/12.37 | 12.51 | sup 12.93 (ha 15 candles) | 0.19971 | -0.0149% | A/venda@12.93 (0t/4c) | zona_mapeada_setup_A |
| 2026-10-08 18:05 | BTC-USDT-SWAP | 81769.3 | 81859.8/81661.0 | 81744.7 | — | 655.44 | 0.0017% | — | sem_zona |
| 2026-10-08 18:05 | ETH-USDT-SWAP | 2473.5 | 2476.7/2463.0 | 2463.2 | sup 2405.0 (ha 3 candles) | 28.77 | -0.0078% | A/venda@2542.8 (0t/6c) | zona_mapeada_setup_A |
| 2026-10-08 18:05 | SOL-USDT-SWAP | 109.81 | 109.88/108.94 | 109.10 | sup 105.61 (ha 3 candles) | 1.5064 | -0.0075% | A/venda@114.09 (0t/5c) | zona_mapeada_setup_A |
| 2026-10-08 18:05 | XRP-USDT-SWAP | 1.3771 | 1.3789/1.3719 | 1.3718 | — | 0.02011 | -0.0092% | — | sem_zona |
| 2026-10-08 18:05 | DOGE-USDT-SWAP | 0.08421 | 0.08439/0.08370 | 0.08371 | sup 0.08092 (ha 3 candles) | 0.00129 | -0.0153% | A/venda@0.08502 (0t/5c) | zona_mapeada_setup_A |
| 2026-10-08 18:05 | ARB-USDT-SWAP | 0.17280 | 0.17336/0.17106 | 0.17107 | sup 0.16142 (ha 5 candles) | 0.00455 | -0.0074% | A/venda@0.18036 (0t/5c) | zona_mapeada_setup_A |
| 2026-10-08 18:05 | WLD-USDT-SWAP | 0.48310 | 0.48430/0.47940 | 0.47930 | sup 0.50780 (ha 16 candles) | 0.01310 | -0.0062% | A/venda@0.50780 (0t/5c) | zona_mapeada_setup_A |
| 2026-10-08 18:05 | SUI-USDT-SWAP | 1.0532 | 1.0557/1.0388 | 1.0388 | sup 0.99710 (ha 3 candles) | 0.02467 | -0.0186% | A/venda@1.1157 (0t/6c) | zona_mapeada_setup_A |
| 2026-10-08 18:05 | UNI-USDT-SWAP | 7.3520 | 7.3560/7.2520 | 7.2530 | sup 6.9870 (ha 3 candles) | 0.16193 | 0.0078% | A/venda@7.6830 (0t/6c) | zona_mapeada_setup_A |
| 2026-10-08 18:05 | LINK-USDT-SWAP | 12.66 | 12.68/12.50 | 12.51 | sup 12.06 (ha 3 candles) | 0.20279 | -0.0169% | A/venda@12.93 (0t/5c) | zona_mapeada_setup_A |
| 2026-10-08 19:05 | BTC-USDT-SWAP | 81669.9 | 81769.3/81560.8 | 81744.7 | — | 628.49 | 0.0023% | — | sem_zona |
| 2026-10-08 19:05 | ETH-USDT-SWAP | 2478.5 | 2483.1/2467.0 | 2463.2 | sup 2405.0 (ha 4 candles) | 28.68 | -0.0064% | A/venda@2542.8 (0t/7c) | zona_mapeada_setup_A |
| 2026-10-08 19:05 | SOL-USDT-SWAP | 110.58 | 110.81/109.44 | 109.10 | sup 105.61 (ha 4 candles) | 1.5393 | -0.0079% | A/venda@114.09 (0t/6c) | zona_mapeada_setup_A |
| 2026-10-08 19:05 | XRP-USDT-SWAP | 1.3764 | 1.3836/1.3725 | 1.3718 | — | 0.01984 | -0.0072% | — | sem_zona |
| 2026-10-08 19:05 | DOGE-USDT-SWAP | 0.08432 | 0.08441/0.08397 | 0.08371 | sup 0.08092 (ha 4 candles) | 0.00126 | -0.0129% | A/venda@0.08502 (0t/6c) | zona_mapeada_setup_A |
| 2026-10-08 19:05 | ARB-USDT-SWAP | 0.17312 | 0.17339/0.17185 | 0.17107 | sup 0.16142 (ha 6 candles) | 0.00443 | -0.0080% | A/venda@0.18036 (0t/6c) | zona_mapeada_setup_A |
| 2026-10-08 19:05 | WLD-USDT-SWAP | 0.48080 | 0.48350/0.47810 | 0.47930 | sup 0.45860 (ha 3 candles) | 0.01266 | -0.0072% | A/venda@0.50780 (0t/6c) | zona_mapeada_setup_A |
| 2026-10-08 19:05 | SUI-USDT-SWAP | 1.0487 | 1.0545/1.0440 | 1.0388 | sup 0.99710 (ha 4 candles) | 0.02424 | -0.0180% | A/venda@1.1157 (0t/7c) | zona_mapeada_setup_A |
| 2026-10-08 19:05 | UNI-USDT-SWAP | 7.3580 | 7.3790/7.3010 | 7.2530 | sup 6.9870 (ha 4 candles) | 0.15743 | 0.0027% | A/venda@7.6830 (0t/7c) | zona_mapeada_setup_A |
| 2026-10-08 19:05 | LINK-USDT-SWAP | 12.73 | 12.73/12.62 | 12.51 | sup 12.06 (ha 4 candles) | 0.20229 | -0.0167% | A/venda@12.93 (0t/6c) | zona_mapeada_setup_A |
| 2026-10-08 20:05 | BTC-USDT-SWAP | 81863.4 | 81905.0/81645.0 | 81744.7 | — | 627.94 | 0.0033% | — | sem_zona |
| 2026-10-08 20:05 | ETH-USDT-SWAP | 2475.0 | 2481.2/2470.3 | 2463.2 | sup 2405.0 (ha 5 candles) | 28.58 | -0.0055% | — | zona_expirada_setup_A |
| 2026-10-08 20:05 | SOL-USDT-SWAP | 110.29 | 110.79/110.04 | 109.10 | sup 105.61 (ha 5 candles) | 1.5607 | -0.0071% | A/venda@114.09 (0t/7c) | zona_mapeada_setup_A |
| 2026-10-08 20:05 | XRP-USDT-SWAP | 1.3820 | 1.3833/1.3762 | 1.3718 | — | 0.01973 | -0.0051% | — | sem_zona |
| 2026-10-08 20:05 | DOGE-USDT-SWAP | 0.08444 | 0.08458/0.08426 | 0.08371 | sup 0.08092 (ha 5 candles) | 0.00125 | -0.0089% | A/venda@0.08502 (0t/7c) | zona_mapeada_setup_A |
| 2026-10-08 20:05 | ARB-USDT-SWAP | 0.17368 | 0.17456/0.17302 | 0.17107 | sup 0.16142 (ha 7 candles) | 0.00441 | -0.0087% | A/venda@0.18036 (0t/7c) | zona_mapeada_setup_A |
| 2026-10-08 20:05 | WLD-USDT-SWAP | 0.48040 | 0.48310/0.48020 | 0.47930 | sup 0.45860 (ha 4 candles) | 0.01246 | -0.0093% | A/venda@0.50780 (0t/7c) | zona_mapeada_setup_A |
| 2026-10-08 20:05 | SUI-USDT-SWAP | 1.0497 | 1.0544/1.0474 | 1.0388 | sup 0.99710 (ha 5 candles) | 0.02379 | -0.0181% | — | zona_expirada_setup_A |
| 2026-10-08 20:05 | UNI-USDT-SWAP | 7.3330 | 7.3780/7.3260 | 7.2530 | sup 6.9870 (ha 5 candles) | 0.15643 | -0.0005% | — | zona_expirada_setup_A |
| 2026-10-08 20:05 | LINK-USDT-SWAP | 12.76 | 12.79/12.71 | 12.51 | sup 12.06 (ha 5 candles) | 0.20271 | -0.0154% | A/venda@12.93 (0t/7c) | zona_mapeada_setup_A |
| 2026-10-08 21:05 | BTC-USDT-SWAP | 81714.9 | 81899.0/81656.6 | 81714.9 | — | 619.94 | 0.0028% | — | sem_zona |
| 2026-10-08 21:05 | ETH-USDT-SWAP | 2473.7 | 2483.0/2470.7 | 2473.7 | sup 2405.0 (ha 6 candles) | 28.42 | -0.0050% | — | sem_zona |
| 2026-10-08 21:05 | SOL-USDT-SWAP | 109.55 | 110.42/109.37 | 109.55 | sup 105.61 (ha 6 candles) | 1.5864 | -0.0081% | — | zona_expirada_setup_A |
| 2026-10-08 21:05 | XRP-USDT-SWAP | 1.3797 | 1.3871/1.3778 | 1.3797 | — | 0.01968 | -0.0053% | — | sem_zona |
| 2026-10-08 21:05 | DOGE-USDT-SWAP | 0.08401 | 0.08468/0.08394 | 0.08401 | sup 0.08092 (ha 6 candles) | 0.00125 | -0.0042% | — | zona_expirada_setup_A |
| 2026-10-08 21:05 | ARB-USDT-SWAP | 0.17256 | 0.17436/0.17229 | 0.17256 | sup 0.16142 (ha 8 candles) | 0.00431 | -0.0070% | — | zona_expirada_setup_A |
| 2026-10-08 21:05 | WLD-USDT-SWAP | 0.47950 | 0.48220/0.47930 | 0.47950 | sup 0.45860 (ha 5 candles) | 0.01179 | -0.0099% | — | zona_expirada_setup_A |
| 2026-10-08 21:05 | SUI-USDT-SWAP | 1.0402 | 1.0536/1.0384 | 1.0402 | sup 0.99710 (ha 6 candles) | 0.02361 | -0.0160% | B/venda@1.0374 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-08 21:05 | UNI-USDT-SWAP | 7.1180 | 7.3780/7.0030 | 7.1180 | sup 6.9870 (ha 6 candles) | 0.17579 | -0.0029% | — | sem_zona |
| 2026-10-08 21:05 | LINK-USDT-SWAP | 12.70 | 12.80/12.68 | 12.70 | sup 12.06 (ha 6 candles) | 0.20200 | -0.0123% | — | zona_expirada_setup_A |
| 2026-10-08 22:05 | BTC-USDT-SWAP | 81769.9 | 81868.0/81664.0 | 81714.9 | — | 592.75 | 0.0032% | — | sem_zona |
| 2026-10-08 22:05 | ETH-USDT-SWAP | 2476.7 | 2482.3/2472.7 | 2473.7 | sup 2405.0 (ha 7 candles) | 27.61 | -0.0050% | — | sem_zona |
| 2026-10-08 22:05 | SOL-USDT-SWAP | 109.26 | 109.75/108.75 | 109.55 | sup 105.61 (ha 7 candles) | 1.5736 | -0.0052% | — | sem_zona |
| 2026-10-08 22:05 | XRP-USDT-SWAP | 1.3870 | 1.3894/1.3796 | 1.3797 | — | 0.01914 | -0.0072% | — | sem_zona |
| 2026-10-08 22:05 | DOGE-USDT-SWAP | 0.08424 | 0.08439/0.08384 | 0.08401 | sup 0.08092 (ha 7 candles) | 0.00121 | 0.0003% | — | sem_zona |
| 2026-10-08 22:05 | ARB-USDT-SWAP | 0.17188 | 0.17371/0.17172 | 0.17256 | sup 0.16142 (ha 9 candles) | 0.00421 | -0.0057% | — | sem_zona |
| 2026-10-08 22:05 | WLD-USDT-SWAP | 0.48270 | 0.48720/0.47940 | 0.47950 | sup 0.45860 (ha 6 candles) | 0.01099 | -0.0084% | B/venda@0.47950 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-08 22:05 | SUI-USDT-SWAP | 1.0433 | 1.0469/1.0387 | 1.0402 | sup 0.99710 (ha 7 candles) | 0.02295 | -0.0108% | B/venda@1.0374 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-08 22:05 | UNI-USDT-SWAP | 7.1860 | 7.2140/7.1030 | 7.1180 | sup 6.9870 (ha 7 candles) | 0.17479 | 0.0033% | — | sem_zona |
| 2026-10-08 22:05 | LINK-USDT-SWAP | 12.70 | 12.76/12.66 | 12.70 | sup 12.06 (ha 7 candles) | 0.19900 | -0.0095% | — | sem_zona |
| 2026-10-08 23:06 | BTC-USDT-SWAP | 81942.9 | 81964.9/81569.2 | 81714.9 | — | 589.86 | 0.0033% | — | sem_zona |
| 2026-10-08 23:06 | ETH-USDT-SWAP | 2480.9 | 2485.7/2468.6 | 2473.7 | sup 2405.0 (ha 8 candles) | 27.03 | -0.0046% | — | sem_zona |
| 2026-10-08 23:06 | SOL-USDT-SWAP | 109.40 | 109.59/108.75 | 109.55 | sup 105.61 (ha 8 candles) | 1.5379 | -0.0002% | — | sem_zona |
| 2026-10-08 23:06 | XRP-USDT-SWAP | 1.3892 | 1.3943/1.3829 | 1.3797 | — | 0.01927 | -0.0083% | — | sem_zona |
| 2026-10-08 23:06 | DOGE-USDT-SWAP | 0.08470 | 0.08491/0.08409 | 0.08401 | sup 0.08092 (ha 8 candles) | 0.00122 | 0.0037% | — | sem_zona |
| 2026-10-08 23:06 | ARB-USDT-SWAP | 0.17366 | 0.17458/0.17172 | 0.17256 | sup 0.16142 (ha 10 candles) | 0.00427 | -0.0050% | — | sem_zona |
| 2026-10-08 23:06 | WLD-USDT-SWAP | 0.48910 | 0.49070/0.48110 | 0.47950 | sup 0.45860 (ha 7 candles) | 0.01122 | -0.0074% | — | invalidado_setup_B |
| 2026-10-08 23:06 | SUI-USDT-SWAP | 1.0533 | 1.0577/1.0423 | 1.0402 | sup 0.99710 (ha 8 candles) | 0.02306 | -0.0061% | — | invalidado_setup_B |
| 2026-10-08 23:06 | UNI-USDT-SWAP | 7.2970 | 7.3260/7.1740 | 7.1180 | sup 6.9870 (ha 8 candles) | 0.18057 | 0.0070% | — | sem_zona |
| 2026-10-08 23:06 | LINK-USDT-SWAP | 12.80 | 12.82/12.69 | 12.70 | sup 12.06 (ha 8 candles) | 0.20050 | -0.0064% | — | sem_zona |
| 2026-10-09 00:05 | BTC-USDT-SWAP | 82079.0 | 82340.9/81871.0 | 81714.9 | — | 576.46 | 0.0050% | B/compra@82501.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-09 00:05 | ETH-USDT-SWAP | 2488.2 | 2499.0/2476.4 | 2473.7 | sup 2405.0 (ha 9 candles) | 26.88 | -0.0042% | — | sem_zona |
| 2026-10-09 00:06 | SOL-USDT-SWAP | 110.24 | 110.87/109.38 | 109.55 | sup 105.61 (ha 9 candles) | 1.5543 | 0.0018% | — | sem_zona |
| 2026-10-09 00:06 | XRP-USDT-SWAP | 1.3911 | 1.3980/1.3835 | 1.3797 | — | 0.01954 | -0.0093% | — | sem_zona |
| 2026-10-09 00:06 | DOGE-USDT-SWAP | 0.08471 | 0.08517/0.08432 | 0.08401 | sup 0.08092 (ha 9 candles) | 0.00122 | 0.0040% | — | sem_zona |
| 2026-10-09 00:06 | ARB-USDT-SWAP | 0.17501 | 0.17581/0.17286 | 0.17256 | sup 0.16142 (ha 11 candles) | 0.00429 | -0.0060% | — | sem_zona |
| 2026-10-09 00:06 | WLD-USDT-SWAP | 0.48780 | 0.49080/0.48320 | 0.47950 | sup 0.45860 (ha 8 candles) | 0.01111 | -0.0060% | — | sem_zona |
| 2026-10-09 00:06 | SUI-USDT-SWAP | 1.0499 | 1.0575/1.0432 | 1.0402 | sup 1.0384 (ha 3 candles) | 0.02231 | -0.0014% | — | sem_zona |
| 2026-10-09 00:06 | UNI-USDT-SWAP | 7.3250 | 7.3700/7.2530 | 7.1180 | sup 7.0030 (ha 3 candles) | 0.17379 | 0.0061% | — | sem_zona |
| 2026-10-09 00:06 | LINK-USDT-SWAP | 12.77 | 12.84/12.72 | 12.70 | sup 12.06 (ha 9 candles) | 0.19879 | -0.0037% | — | sem_zona |
| 2026-10-09 01:05 | BTC-USDT-SWAP | 82382.8 | 82398.6/82007.2 | 82382.8 | — | 540.14 | 0.0058% | — | descartado_rr_baixo_setup_B |
| 2026-10-09 01:05 | ETH-USDT-SWAP | 2491.9 | 2492.5/2483.2 | 2491.9 | sup 2405.0 (ha 10 candles) | 24.77 | -0.0061% | — | sem_zona |
| 2026-10-09 01:05 | SOL-USDT-SWAP | 110.36 | 110.42/109.81 | 110.36 | sup 108.75 (ha 3 candles) | 1.4750 | 0.0006% | — | sem_zona |
| 2026-10-09 01:05 | XRP-USDT-SWAP | 1.3946 | 1.3951/1.3897 | 1.3946 | — | 0.01870 | -0.0114% | — | sem_zona |
| 2026-10-09 01:05 | DOGE-USDT-SWAP | 0.08499 | 0.08504/0.08462 | 0.08499 | sup 0.08384 (ha 3 candles) | 0.00117 | 0.0015% | — | sem_zona |
| 2026-10-09 01:05 | ARB-USDT-SWAP | 0.17678 | 0.17719/0.17469 | 0.17678 | sup 0.17172 (ha 3 candles) | 0.00423 | -0.0075% | — | sem_zona |
| 2026-10-09 01:05 | WLD-USDT-SWAP | 0.49090 | 0.49380/0.48690 | 0.49090 | sup 0.45860 (ha 9 candles) | 0.01056 | -0.0058% | — | sem_zona |
| 2026-10-09 01:05 | SUI-USDT-SWAP | 1.0556 | 1.0582/1.0477 | 1.0556 | sup 1.0384 (ha 4 candles) | 0.02144 | -0.0012% | — | sem_zona |
| 2026-10-09 01:05 | UNI-USDT-SWAP | 7.3640 | 7.3650/7.3000 | 7.3640 | sup 7.0030 (ha 4 candles) | 0.16736 | 0.0050% | — | sem_zona |
| 2026-10-09 01:05 | LINK-USDT-SWAP | 12.85 | 12.85/12.76 | 12.85 | sup 12.06 (ha 10 candles) | 0.19200 | -0.0023% | — | sem_zona |
| 2026-10-09 02:05 | BTC-USDT-SWAP | 82206.3 | 82486.0/82173.3 | 82382.8 | — | 515.54 | 0.0057% | — | sem_zona |
| 2026-10-09 02:05 | ETH-USDT-SWAP | 2485.9 | 2494.5/2482.2 | 2491.9 | sup 2468.6 (ha 3 candles) | 24.25 | -0.0076% | — | sem_zona |
| 2026-10-09 02:05 | SOL-USDT-SWAP | 109.83 | 110.64/109.62 | 110.36 | sup 108.75 (ha 3 candles) | 1.4993 | -0.0004% | — | sem_zona |
| 2026-10-09 02:05 | XRP-USDT-SWAP | 1.3912 | 1.3972/1.3899 | 1.3946 | — | 0.01846 | -0.0127% | — | sem_zona |
| 2026-10-09 02:05 | DOGE-USDT-SWAP | 0.08479 | 0.08513/0.08469 | 0.08499 | sup 0.08384 (ha 4 candles) | 0.00116 | -0.0025% | — | sem_zona |
| 2026-10-09 02:05 | ARB-USDT-SWAP | 0.17667 | 0.17747/0.17628 | 0.17678 | sup 0.17172 (ha 3 candles) | 0.00411 | -0.0089% | — | sem_zona |
| 2026-10-09 02:05 | WLD-USDT-SWAP | 0.49040 | 0.49370/0.48940 | 0.49090 | sup 0.45860 (ha 10 candles) | 0.01032 | -0.0051% | — | sem_zona |
| 2026-10-09 02:05 | SUI-USDT-SWAP | 1.0514 | 1.0575/1.0481 | 1.0556 | sup 1.0384 (ha 5 candles) | 0.02119 | -0.0018% | — | sem_zona |
| 2026-10-09 02:05 | UNI-USDT-SWAP | 7.3210 | 7.4000/7.3070 | 7.3640 | sup 7.0030 (ha 5 candles) | 0.16500 | 0.0032% | — | sem_zona |
| 2026-10-09 02:05 | LINK-USDT-SWAP | 12.81 | 12.88/12.81 | 12.85 | sup 12.06 (ha 11 candles) | 0.18929 | -0.0015% | — | sem_zona |
| 2026-10-09 03:05 | BTC-USDT-SWAP | 82316.3 | 82580.0/82191.0 | 82382.8 | — | 418.36 | 0.0053% | — | sem_zona |
| 2026-10-09 03:05 | ETH-USDT-SWAP | 2489.4 | 2498.4/2484.6 | 2491.9 | sup 2468.6 (ha 4 candles) | 17.92 | -0.0077% | — | sem_zona |
| 2026-10-09 03:05 | SOL-USDT-SWAP | 110.23 | 110.72/109.79 | 110.36 | sup 108.75 (ha 4 candles) | 1.2479 | -0.0013% | — | sem_zona |
| 2026-10-09 03:05 | XRP-USDT-SWAP | 1.3959 | 1.4013/1.3907 | 1.3946 | — | 0.01457 | -0.0102% | — | sem_zona |
| 2026-10-09 03:05 | DOGE-USDT-SWAP | 0.08515 | 0.08546/0.08477 | 0.08499 | sup 0.08384 (ha 5 candles) | 0.00083 | -0.0052% | — | sem_zona |
| 2026-10-09 03:05 | ARB-USDT-SWAP | 0.17773 | 0.17935/0.17656 | 0.17678 | sup 0.17172 (ha 4 candles) | 0.00282 | -0.0111% | — | sem_zona |
| 2026-10-09 03:05 | WLD-USDT-SWAP | 0.49580 | 0.49920/0.49010 | 0.49090 | sup 0.45860 (ha 11 candles) | 0.00824 | -0.0033% | — | sem_zona |
| 2026-10-09 03:05 | SUI-USDT-SWAP | 1.0653 | 1.0720/1.0515 | 1.0556 | sup 1.0384 (ha 6 candles) | 0.01696 | -0.0034% | — | sem_zona |
| 2026-10-09 03:05 | UNI-USDT-SWAP | 7.3680 | 7.4530/7.3150 | 7.3640 | sup 7.0030 (ha 6 candles) | 0.14364 | 0.0045% | — | sem_zona |
| 2026-10-09 03:05 | LINK-USDT-SWAP | 12.85 | 12.92/12.81 | 12.85 | sup 12.06 (ha 12 candles) | 0.14957 | 0.0003% | — | sem_zona |
| 2026-10-09 04:05 | BTC-USDT-SWAP | 82524.1 | 82625.0/82316.0 | 82382.8 | — | 390.98 | 0.0041% | B/compra@82812.5 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-09 04:05 | ETH-USDT-SWAP | 2498.0 | 2501.5/2489.4 | 2491.9 | sup 2468.6 (ha 5 candles) | 16.44 | -0.0080% | — | sem_zona |
| 2026-10-09 04:05 | SOL-USDT-SWAP | 110.57 | 110.78/110.22 | 110.36 | sup 108.75 (ha 5 candles) | 1.1757 | -0.0030% | — | sem_zona |
| 2026-10-09 04:05 | XRP-USDT-SWAP | 1.3995 | 1.4028/1.3954 | 1.3946 | — | 0.01327 | -0.0092% | — | sem_zona |
| 2026-10-09 04:05 | DOGE-USDT-SWAP | 0.08538 | 0.08553/0.08515 | 0.08499 | sup 0.08384 (ha 6 candles) | 0.00074 | -0.0081% | — | sem_zona |
| 2026-10-09 04:05 | ARB-USDT-SWAP | 0.17813 | 0.17886/0.17761 | 0.17678 | sup 0.17172 (ha 5 candles) | 0.00263 | -0.0135% | — | sem_zona |
| 2026-10-09 04:05 | WLD-USDT-SWAP | 0.49510 | 0.49820/0.49440 | 0.49090 | sup 0.45860 (ha 12 candles) | 0.00734 | -0.0010% | — | sem_zona |
| 2026-10-09 04:05 | SUI-USDT-SWAP | 1.0660 | 1.0719/1.0647 | 1.0556 | sup 1.0384 (ha 7 candles) | 0.01547 | -0.0057% | — | sem_zona |
| 2026-10-09 04:05 | UNI-USDT-SWAP | 7.4320 | 7.4430/7.3640 | 7.3640 | sup 7.0030 (ha 7 candles) | 0.13150 | 0.0026% | — | sem_zona |
| 2026-10-09 04:05 | LINK-USDT-SWAP | 12.89 | 12.91/12.85 | 12.85 | sup 12.06 (ha 13 candles) | 0.13750 | -0.0005% | — | sem_zona |
| 2026-10-09 05:05 | BTC-USDT-SWAP | 82607.7 | 82610.0/82440.0 | 82607.7 | sup 81569.2 (ha 6 candles) | 357.69 | 0.0003% | B/compra@82812.5 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-09 05:05 | ETH-USDT-SWAP | 2502.8 | 2504.6/2495.0 | 2502.8 | sup 2468.6 (ha 6 candles) | 15.60 | -0.0086% | — | sem_zona |
| 2026-10-09 05:05 | SOL-USDT-SWAP | 110.61 | 110.67/110.13 | 110.61 | sup 108.75 (ha 6 candles) | 1.0536 | -0.0057% | — | sem_zona |
| 2026-10-09 05:05 | XRP-USDT-SWAP | 1.4032 | 1.4043/1.3973 | 1.4032 | sup 1.3176 (ha 14 candles) | 0.01175 | -0.0084% | — | sem_zona |
| 2026-10-09 05:05 | DOGE-USDT-SWAP | 0.08535 | 0.08544/0.08518 | 0.08535 | sup 0.08384 (ha 7 candles) | 0.00065 | -0.0079% | — | sem_zona |
| 2026-10-09 05:05 | ARB-USDT-SWAP | 0.17933 | 0.17976/0.17755 | 0.17933 | sup 0.17172 (ha 6 candles) | 0.00246 | -0.0138% | — | sem_zona |
| 2026-10-09 05:05 | WLD-USDT-SWAP | 0.50180 | 0.50280/0.49330 | 0.50180 | sup 0.45860 (ha 13 candles) | 0.00717 | -0.0009% | — | sem_zona |
| 2026-10-09 05:05 | SUI-USDT-SWAP | 1.0754 | 1.0763/1.0620 | 1.0754 | sup 1.0384 (ha 8 candles) | 0.01431 | -0.0062% | — | sem_zona |
| 2026-10-09 05:05 | UNI-USDT-SWAP | 7.4330 | 7.4520/7.3800 | 7.4330 | sup 7.0030 (ha 8 candles) | 0.12271 | -0.0009% | — | sem_zona |
| 2026-10-09 05:05 | LINK-USDT-SWAP | 12.94 | 12.96/12.86 | 12.94 | sup 12.06 (ha 14 candles) | 0.12300 | -0.0002% | — | sem_zona |
| 2026-10-09 06:05 | BTC-USDT-SWAP | 82656.5 | 82713.3/82470.0 | 82607.7 | sup 81569.2 (ha 7 candles) | 301.81 | -0.0015% | B/compra@82812.5 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-09 06:05 | ETH-USDT-SWAP | 2503.8 | 2506.6/2495.8 | 2502.8 | sup 2468.6 (ha 7 candles) | 13.78 | -0.0096% | — | sem_zona |
| 2026-10-09 06:05 | SOL-USDT-SWAP | 110.54 | 110.77/109.94 | 110.61 | sup 108.75 (ha 7 candles) | 0.95214 | -0.0067% | — | sem_zona |
| 2026-10-09 06:05 | XRP-USDT-SWAP | 1.4035 | 1.4061/1.3978 | 1.4032 | sup 1.3176 (ha 15 candles) | 0.00956 | -0.0079% | — | sem_zona |
| 2026-10-09 06:05 | DOGE-USDT-SWAP | 0.08519 | 0.08541/0.08499 | 0.08535 | sup 0.08384 (ha 8 candles) | 0.00056 | -0.0050% | — | sem_zona |
| 2026-10-09 06:05 | ARB-USDT-SWAP | 0.17952 | 0.17982/0.17826 | 0.17933 | sup 0.17172 (ha 7 candles) | 0.00214 | -0.0174% | — | sem_zona |
| 2026-10-09 06:05 | WLD-USDT-SWAP | 0.49870 | 0.50260/0.49670 | 0.50180 | sup 0.45860 (ha 14 candles) | 0.00651 | 0.0035% | — | sem_zona |
| 2026-10-09 06:05 | SUI-USDT-SWAP | 1.0722 | 1.0783/1.0685 | 1.0754 | sup 1.0384 (ha 9 candles) | 0.01289 | -0.0078% | — | sem_zona |
| 2026-10-09 06:05 | UNI-USDT-SWAP | 7.4150 | 7.4330/7.3730 | 7.4330 | sup 7.0030 (ha 9 candles) | 0.11343 | -0.0026% | — | sem_zona |
| 2026-10-09 06:05 | LINK-USDT-SWAP | 12.88 | 12.95/12.84 | 12.94 | sup 12.06 (ha 15 candles) | 0.11050 | -0.0008% | — | sem_zona |
| 2026-10-09 07:06 | BTC-USDT-SWAP | 82611.0 | 82656.5/82505.3 | 82607.7 | sup 81569.2 (ha 8 candles) | 281.85 | -0.0025% | B/compra@82812.5 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-09 07:06 | ETH-USDT-SWAP | 2501.0 | 2508.0/2500.2 | 2502.8 | sup 2468.6 (ha 8 candles) | 12.70 | -0.0089% | — | sem_zona |
| 2026-10-09 07:06 | SOL-USDT-SWAP | 110.36 | 110.63/110.25 | 110.61 | sup 108.75 (ha 8 candles) | 0.87929 | -0.0060% | — | sem_zona |
| 2026-10-09 07:06 | XRP-USDT-SWAP | 1.4002 | 1.4036/1.3977 | 1.4032 | sup 1.3176 (ha 16 candles) | 0.00873 | -0.0055% | — | sem_zona |
| 2026-10-09 07:06 | DOGE-USDT-SWAP | 0.08506 | 0.08520/0.08484 | 0.08535 | sup 0.08384 (ha 9 candles) | 0.00053 | -0.0022% | — | sem_zona |
| 2026-10-09 07:06 | ARB-USDT-SWAP | 0.17909 | 0.17968/0.17870 | 0.17933 | sup 0.17172 (ha 8 candles) | 0.00198 | -0.0187% | — | sem_zona |
| 2026-10-09 07:06 | WLD-USDT-SWAP | 0.49680 | 0.49880/0.49540 | 0.50180 | sup 0.45860 (ha 15 candles) | 0.00601 | 0.0066% | — | sem_zona |
| 2026-10-09 07:06 | SUI-USDT-SWAP | 1.0700 | 1.0723/1.0661 | 1.0754 | sup 1.0384 (ha 10 candles) | 0.01182 | -0.0068% | — | sem_zona |
| 2026-10-09 07:06 | UNI-USDT-SWAP | 7.3860 | 7.4160/7.3580 | 7.4330 | sup 7.0030 (ha 10 candles) | 0.11100 | -0.0008% | — | sem_zona |
| 2026-10-09 07:06 | LINK-USDT-SWAP | 12.90 | 12.91/12.86 | 12.94 | sup 12.06 (ha 16 candles) | 0.10164 | -0.0016% | — | sem_zona |
| 2026-10-09 08:05 | BTC-USDT-SWAP | 82521.0 | 82683.0/82353.1 | 82607.7 | sup 81569.2 (ha 9 candles) | 291.21 | -0.0031% | B/compra@82812.5 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-09 08:05 | ETH-USDT-SWAP | 2491.6 | 2502.4/2486.1 | 2502.8 | sup 2468.6 (ha 9 candles) | 12.88 | -0.0078% | — | sem_zona |
| 2026-10-09 08:05 | SOL-USDT-SWAP | 109.69 | 110.51/109.32 | 110.61 | sup 108.75 (ha 9 candles) | 0.89714 | -0.0047% | — | sem_zona |
| 2026-10-09 08:05 | XRP-USDT-SWAP | 1.3854 | 1.4015/1.3801 | 1.4032 | sup 1.3176 (ha 17 candles) | 0.00975 | -0.0017% | — | sem_zona |
| 2026-10-09 08:05 | DOGE-USDT-SWAP | 0.08427 | 0.08507/0.08401 | 0.08535 | sup 0.08384 (ha 10 candles) | 0.00055 | -0.0002% | — | sem_zona |
| 2026-10-09 08:05 | ARB-USDT-SWAP | 0.17752 | 0.17959/0.17616 | 0.17933 | sup 0.17172 (ha 9 candles) | 0.00206 | -0.0167% | — | sem_zona |
| 2026-10-09 08:05 | WLD-USDT-SWAP | 0.49210 | 0.49740/0.48830 | 0.50180 | sup 0.45860 (ha 16 candles) | 0.00630 | 0.0099% | — | sem_zona |
| 2026-10-09 08:05 | SUI-USDT-SWAP | 1.0584 | 1.0717/1.0501 | 1.0754 | sup 1.0384 (ha 11 candles) | 0.01216 | -0.0029% | — | sem_zona |
| 2026-10-09 08:05 | UNI-USDT-SWAP | 7.3300 | 7.3960/7.3070 | 7.4330 | sup 7.0030 (ha 11 candles) | 0.10993 | 0.0020% | — | sem_zona |
| 2026-10-09 08:05 | LINK-USDT-SWAP | 12.78 | 12.90/12.72 | 12.94 | sup 12.06 (ha 17 candles) | 0.10229 | -0.0015% | — | sem_zona |
| 2026-10-09 09:05 | BTC-USDT-SWAP | 83207.9 | 83499.0/82420.0 | 83207.9 | sup 81569.2 (ha 10 candles) | 353.39 | -0.0025% | — | invalidado_tendencia_virou_setup_B |
| 2026-10-09 09:05 | ETH-USDT-SWAP | 2505.1 | 2520.8/2488.0 | 2505.1 | sup 2468.6 (ha 10 candles) | 14.08 | -0.0056% | — | sem_zona |
| 2026-10-09 09:05 | SOL-USDT-SWAP | 111.23 | 112.04/109.47 | 111.23 | sup 108.75 (ha 10 candles) | 0.98286 | -0.0029% | — | sem_zona |
| 2026-10-09 09:05 | XRP-USDT-SWAP | 1.4010 | 1.4067/1.3824 | 1.4010 | sup 1.3176 (ha 18 candles) | 0.01069 | 0.0004% | — | sem_zona |
| 2026-10-09 09:05 | DOGE-USDT-SWAP | 0.08497 | 0.08557/0.08403 | 0.08497 | sup 0.08384 (ha 11 candles) | 0.00063 | 0.0007% | — | sem_zona |
| 2026-10-09 09:05 | ARB-USDT-SWAP | 0.17931 | 0.18161/0.17715 | 0.17931 | sup 0.17172 (ha 10 candles) | 0.00227 | -0.0162% | — | sem_zona |
| 2026-10-09 09:05 | WLD-USDT-SWAP | 0.49640 | 0.50220/0.48990 | 0.49640 | sup 0.45860 (ha 17 candles) | 0.00679 | 0.0061% | — | sem_zona |
| 2026-10-09 09:05 | SUI-USDT-SWAP | 1.0705 | 1.0791/1.0552 | 1.0705 | sup 1.0384 (ha 12 candles) | 0.01311 | -0.0000% | — | sem_zona |
| 2026-10-09 09:05 | UNI-USDT-SWAP | 7.3800 | 7.4460/7.2840 | 7.3800 | sup 7.0030 (ha 12 candles) | 0.11593 | 0.0061% | — | sem_zona |
| 2026-10-09 09:05 | LINK-USDT-SWAP | 12.91 | 12.95/12.74 | 12.91 | sup 12.06 (ha 18 candles) | 0.10943 | -0.0010% | — | sem_zona |
| 2026-10-09 10:07 | BTC-USDT-SWAP | 82995.6 | 83386.5/82872.7 | 83207.9 | sup 81569.2 (ha 11 candles) | 371.52 | -0.0006% | — | sem_zona |
| 2026-10-09 10:07 | ETH-USDT-SWAP | 2496.9 | 2509.7/2491.4 | 2505.1 | sup 2468.6 (ha 11 candles) | 14.60 | -0.0046% | — | sem_zona |
| 2026-10-09 10:07 | SOL-USDT-SWAP | 110.40 | 111.32/110.11 | 111.23 | sup 108.75 (ha 11 candles) | 1.0157 | -0.0027% | — | sem_zona |
| 2026-10-09 10:07 | XRP-USDT-SWAP | 1.3902 | 1.4024/1.3861 | 1.4010 | sup 1.3176 (ha 19 candles) | 0.01135 | 0.0004% | — | sem_zona |
| 2026-10-09 10:07 | DOGE-USDT-SWAP | 0.08473 | 0.08519/0.08447 | 0.08497 | sup 0.08384 (ha 12 candles) | 0.00066 | -0.0009% | — | sem_zona |
| 2026-10-09 10:07 | ARB-USDT-SWAP | 0.17979 | 0.18017/0.17840 | 0.17931 | sup 0.17172 (ha 11 candles) | 0.00229 | -0.0139% | — | sem_zona |
| 2026-10-09 10:07 | WLD-USDT-SWAP | 0.49410 | 0.49840/0.49190 | 0.49640 | sup 0.45860 (ha 18 candles) | 0.00705 | 0.0005% | — | sem_zona |
| 2026-10-09 10:07 | SUI-USDT-SWAP | 1.0621 | 1.0746/1.0587 | 1.0705 | sup 1.0384 (ha 13 candles) | 0.01375 | -0.0001% | — | sem_zona |
| 2026-10-09 10:07 | UNI-USDT-SWAP | 7.3510 | 7.4000/7.3130 | 7.3800 | sup 7.0030 (ha 13 candles) | 0.11843 | 0.0077% | — | sem_zona |
| 2026-10-09 10:07 | LINK-USDT-SWAP | 12.81 | 12.93/12.75 | 12.91 | sup 12.06 (ha 19 candles) | 0.11629 | -0.0034% | — | sem_zona |
| 2026-10-09 11:07 | BTC-USDT-SWAP | 82587.4 | 83142.7/82449.3 | 83207.9 | sup 82353.1 (ha 3 candles) | 403.74 | 0.0010% | — | sem_zona |
| 2026-10-09 11:07 | ETH-USDT-SWAP | 2482.7 | 2502.3/2475.2 | 2505.1 | sup 2468.6 (ha 12 candles) | 15.66 | -0.0033% | — | sem_zona |
| 2026-10-09 11:07 | SOL-USDT-SWAP | 109.53 | 110.63/109.10 | 111.23 | sup 108.75 (ha 12 candles) | 1.0500 | -0.0012% | — | sem_zona |
| 2026-10-09 11:07 | XRP-USDT-SWAP | 1.3794 | 1.3922/1.3763 | 1.4010 | sup 1.3176 (ha 20 candles) | 0.01182 | 0.0016% | — | sem_zona |
| 2026-10-09 11:07 | DOGE-USDT-SWAP | 0.08443 | 0.08492/0.08415 | 0.08497 | sup 0.08401 (ha 3 candles) | 0.00066 | -0.0018% | — | sem_zona |
| 2026-10-09 11:07 | ARB-USDT-SWAP | 0.17824 | 0.18094/0.17820 | 0.17931 | sup 0.17616 (ha 3 candles) | 0.00233 | -0.0120% | — | sem_zona |
| 2026-10-09 11:07 | WLD-USDT-SWAP | 0.48960 | 0.49610/0.48740 | 0.49640 | sup 0.45860 (ha 19 candles) | 0.00746 | 0.0027% | — | sem_zona |
| 2026-10-09 11:07 | SUI-USDT-SWAP | 1.0565 | 1.0659/1.0508 | 1.0705 | sup 1.0501 (ha 3 candles) | 0.01374 | 0.0011% | — | sem_zona |
| 2026-10-09 11:07 | UNI-USDT-SWAP | 7.2890 | 7.3910/7.2760 | 7.3800 | sup 7.0030 (ha 14 candles) | 0.09986 | 0.0095% | — | sem_zona |
| 2026-10-09 11:07 | LINK-USDT-SWAP | 12.75 | 12.84/12.72 | 12.91 | sup 12.72 (ha 3 candles) | 0.11621 | -0.0042% | — | sem_zona |
| 2026-10-09 12:05 | BTC-USDT-SWAP | 83000.0 | 83289.4/82423.0 | 83207.9 | sup 82353.1 (ha 4 candles) | 451.05 | 0.0021% | — | sem_zona |
| 2026-10-09 12:05 | ETH-USDT-SWAP | 2489.8 | 2502.1/2476.7 | 2505.1 | sup 2468.6 (ha 13 candles) | 16.80 | -0.0023% | — | sem_zona |
| 2026-10-09 12:05 | SOL-USDT-SWAP | 110.02 | 110.79/109.09 | 111.23 | sup 108.75 (ha 13 candles) | 1.1000 | 0.0000% | — | sem_zona |
| 2026-10-09 12:05 | XRP-USDT-SWAP | 1.3831 | 1.3917/1.3732 | 1.4010 | sup 1.3176 (ha 21 candles) | 0.01244 | 0.0035% | — | sem_zona |
| 2026-10-09 12:05 | DOGE-USDT-SWAP | 0.08459 | 0.08507/0.08376 | 0.08497 | sup 0.08401 (ha 4 candles) | 0.00072 | -0.0028% | — | sem_zona |
| 2026-10-09 12:05 | ARB-USDT-SWAP | 0.17974 | 0.18056/0.17720 | 0.17931 | sup 0.17616 (ha 4 candles) | 0.00243 | -0.0089% | — | sem_zona |
| 2026-10-09 12:05 | WLD-USDT-SWAP | 0.49210 | 0.49390/0.48590 | 0.49640 | sup 0.45860 (ha 20 candles) | 0.00748 | 0.0033% | — | sem_zona |
| 2026-10-09 12:05 | SUI-USDT-SWAP | 1.0572 | 1.0637/1.0480 | 1.0705 | sup 1.0501 (ha 4 candles) | 0.01428 | 0.0024% | — | sem_zona |
| 2026-10-09 12:05 | UNI-USDT-SWAP | 7.3780 | 7.4070/7.2550 | 7.3800 | sup 7.0030 (ha 15 candles) | 0.10279 | 0.0100% | — | sem_zona |
| 2026-10-09 12:05 | LINK-USDT-SWAP | 12.80 | 12.88/12.68 | 12.91 | sup 12.72 (ha 4 candles) | 0.12307 | -0.0039% | — | sem_zona |
| 2026-10-09 13:07 | BTC-USDT-SWAP | 82833.9 | 83044.8/82771.0 | 82833.9 | sup 82353.1 (ha 5 candles) | 442.34 | 0.0029% | — | sem_zona |
| 2026-10-09 13:07 | ETH-USDT-SWAP | 2487.6 | 2493.2/2483.4 | 2487.6 | sup 2468.6 (ha 14 candles) | 16.27 | -0.0020% | — | sem_zona |
| 2026-10-09 13:07 | SOL-USDT-SWAP | 109.64 | 110.06/109.32 | 109.64 | sup 108.75 (ha 14 candles) | 1.0929 | 0.0008% | — | sem_zona |
| 2026-10-09 13:07 | XRP-USDT-SWAP | 1.3816 | 1.3842/1.3775 | 1.3816 | sup 1.3176 (ha 22 candles) | 0.01211 | 0.0037% | — | sem_zona |
| 2026-10-09 13:07 | DOGE-USDT-SWAP | 0.08459 | 0.08468/0.08422 | 0.08459 | sup 0.08401 (ha 5 candles) | 0.00069 | -0.0014% | — | sem_zona |
| 2026-10-09 13:07 | ARB-USDT-SWAP | 0.18077 | 0.18105/0.17831 | 0.18077 | sup 0.17616 (ha 5 candles) | 0.00242 | -0.0079% | — | sem_zona |
| 2026-10-09 13:07 | WLD-USDT-SWAP | 0.49250 | 0.49320/0.48710 | 0.49250 | sup 0.45860 (ha 21 candles) | 0.00723 | 0.0043% | — | sem_zona |
| 2026-10-09 13:07 | SUI-USDT-SWAP | 1.0571 | 1.0614/1.0507 | 1.0571 | sup 1.0501 (ha 5 candles) | 0.01394 | 0.0024% | — | sem_zona |
| 2026-10-09 13:07 | UNI-USDT-SWAP | 7.3600 | 7.3850/7.3110 | 7.3600 | sup 7.0030 (ha 16 candles) | 0.09721 | 0.0097% | — | sem_zona |
| 2026-10-09 13:07 | LINK-USDT-SWAP | 12.81 | 12.82/12.73 | 12.81 | sup 12.72 (ha 5 candles) | 0.12107 | -0.0037% | — | sem_zona |
| 2026-10-09 14:05 | BTC-USDT-SWAP | 82707.8 | 82979.5/82670.0 | 82833.9 | sup 82353.1 (ha 6 candles) | 430.89 | 0.0032% | — | sem_zona |
| 2026-10-09 14:05 | ETH-USDT-SWAP | 2490.1 | 2498.1/2485.6 | 2487.6 | sup 2475.2 (ha 3 candles) | 15.56 | -0.0017% | — | sem_zona |
| 2026-10-09 14:05 | SOL-USDT-SWAP | 109.73 | 110.05/109.40 | 109.64 | sup 108.75 (ha 15 candles) | 1.0329 | 0.0018% | — | sem_zona |
| 2026-10-09 14:05 | XRP-USDT-SWAP | 1.3844 | 1.3878/1.3791 | 1.3816 | sup 1.3176 (ha 23 candles) | 0.01169 | 0.0036% | — | sem_zona |
| 2026-10-09 14:05 | DOGE-USDT-SWAP | 0.08476 | 0.08498/0.08442 | 0.08459 | sup 0.08401 (ha 6 candles) | 0.00067 | -0.0027% | — | sem_zona |
| 2026-10-09 14:05 | ARB-USDT-SWAP | 0.18090 | 0.18337/0.18037 | 0.18077 | sup 0.17616 (ha 6 candles) | 0.00243 | -0.0078% | — | sem_zona |
| 2026-10-09 14:05 | WLD-USDT-SWAP | 0.49590 | 0.50480/0.49180 | 0.49250 | sup 0.45860 (ha 22 candles) | 0.00761 | 0.0026% | — | sem_zona |
| 2026-10-09 14:05 | SUI-USDT-SWAP | 1.0636 | 1.0691/1.0542 | 1.0571 | sup 1.0501 (ha 6 candles) | 0.01399 | 0.0015% | — | sem_zona |
| 2026-10-09 14:05 | UNI-USDT-SWAP | 7.3590 | 7.4300/7.3300 | 7.3600 | sup 7.0030 (ha 17 candles) | 0.09600 | 0.0068% | — | sem_zona |
| 2026-10-09 14:05 | LINK-USDT-SWAP | 12.83 | 12.87/12.78 | 12.81 | sup 12.72 (ha 6 candles) | 0.11907 | -0.0027% | — | sem_zona |
| 2026-10-09 15:05 | BTC-USDT-SWAP | 82677.4 | 82747.1/82482.9 | 82833.9 | sup 82353.1 (ha 7 candles) | 421.80 | 0.0043% | — | sem_zona |
| 2026-10-09 15:05 | ETH-USDT-SWAP | 2487.2 | 2492.0/2480.7 | 2487.6 | sup 2475.2 (ha 4 candles) | 15.70 | -0.0006% | — | sem_zona |
| 2026-10-09 15:05 | SOL-USDT-SWAP | 109.86 | 109.90/109.30 | 109.64 | sup 109.09 (ha 3 candles) | 1.0321 | 0.0035% | — | sem_zona |
| 2026-10-09 15:05 | XRP-USDT-SWAP | 1.3891 | 1.3904/1.3809 | 1.3816 | sup 1.3732 (ha 3 candles) | 0.01199 | 0.0005% | — | sem_zona |
| 2026-10-09 15:05 | DOGE-USDT-SWAP | 0.08491 | 0.08495/0.08438 | 0.08459 | sup 0.08376 (ha 3 candles) | 0.00068 | -0.0046% | — | sem_zona |
| 2026-10-09 15:05 | ARB-USDT-SWAP | 0.17946 | 0.18191/0.17906 | 0.18077 | sup 0.17616 (ha 7 candles) | 0.00245 | -0.0081% | — | sem_zona |
| 2026-10-09 15:05 | WLD-USDT-SWAP | 0.49710 | 0.49820/0.48950 | 0.49250 | sup 0.48590 (ha 3 candles) | 0.00774 | -0.0011% | — | sem_zona |
| 2026-10-09 15:05 | SUI-USDT-SWAP | 1.0695 | 1.0709/1.0565 | 1.0571 | sup 1.0480 (ha 3 candles) | 0.01426 | -0.0011% | — | sem_zona |
| 2026-10-09 15:05 | UNI-USDT-SWAP | 7.3240 | 7.3740/7.2870 | 7.3600 | sup 7.2550 (ha 3 candles) | 0.09757 | 0.0034% | — | sem_zona |
| 2026-10-09 15:05 | LINK-USDT-SWAP | 12.84 | 12.85/12.76 | 12.81 | sup 12.68 (ha 3 candles) | 0.11964 | -0.0034% | — | sem_zona |
| 2026-10-09 16:05 | BTC-USDT-SWAP | 82405.0 | 82699.9/82263.6 | 82833.9 | sup 82353.1 (ha 8 candles) | 430.63 | 0.0046% | — | sem_zona |
| 2026-10-09 16:05 | ETH-USDT-SWAP | 2482.5 | 2490.6/2477.3 | 2487.6 | sup 2475.2 (ha 5 candles) | 15.77 | 0.0014% | — | sem_zona |
| 2026-10-09 16:05 | SOL-USDT-SWAP | 109.44 | 109.97/109.12 | 109.64 | sup 109.09 (ha 4 candles) | 1.0200 | 0.0057% | — | sem_zona |
| 2026-10-09 16:05 | XRP-USDT-SWAP | 1.3877 | 1.3930/1.3829 | 1.3816 | sup 1.3732 (ha 4 candles) | 0.01219 | -0.0022% | — | sem_zona |
| 2026-10-09 16:05 | DOGE-USDT-SWAP | 0.08459 | 0.08497/0.08431 | 0.08459 | sup 0.08376 (ha 4 candles) | 0.00070 | -0.0057% | — | sem_zona |
| 2026-10-09 16:05 | ARB-USDT-SWAP | 0.17858 | 0.18006/0.17744 | 0.18077 | sup 0.17616 (ha 8 candles) | 0.00255 | -0.0077% | — | sem_zona |
| 2026-10-09 16:05 | WLD-USDT-SWAP | 0.49430 | 0.49890/0.49250 | 0.49250 | sup 0.48590 (ha 4 candles) | 0.00789 | -0.0028% | — | sem_zona |
| 2026-10-09 16:05 | SUI-USDT-SWAP | 1.0614 | 1.0722/1.0572 | 1.0571 | sup 1.0480 (ha 4 candles) | 0.01466 | -0.0024% | — | sem_zona |
| 2026-10-09 16:05 | UNI-USDT-SWAP | 7.2900 | 7.3940/7.2650 | 7.3600 | sup 7.2550 (ha 4 candles) | 0.10014 | 0.0010% | — | sem_zona |
| 2026-10-09 16:05 | LINK-USDT-SWAP | 12.80 | 12.86/12.76 | 12.81 | sup 12.68 (ha 4 candles) | 0.12143 | -0.0028% | — | sem_zona |
| 2026-10-09 17:05 | BTC-USDT-SWAP | 82297.6 | 82528.4/82234.8 | 82297.6 | sup 82353.1 (ha 9 candles) | 423.81 | 0.0044% | A/venda@82353.1 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-09 17:05 | ETH-USDT-SWAP | 2476.4 | 2486.8/2473.0 | 2476.4 | sup 2475.2 (ha 6 candles) | 15.77 | 0.0026% | — | sem_zona |
| 2026-10-09 17:05 | SOL-USDT-SWAP | 108.44 | 109.69/108.37 | 108.44 | sup 109.09 (ha 5 candles) | 1.0479 | 0.0077% | A/venda@109.09 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-09 17:05 | XRP-USDT-SWAP | 1.3829 | 1.3902/1.3798 | 1.3829 | sup 1.3732 (ha 5 candles) | 0.01217 | -0.0032% | — | sem_zona |
| 2026-10-09 17:05 | DOGE-USDT-SWAP | 0.08435 | 0.08475/0.08414 | 0.08435 | sup 0.08376 (ha 5 candles) | 0.00069 | -0.0053% | — | sem_zona |
| 2026-10-09 17:05 | ARB-USDT-SWAP | 0.17846 | 0.17929/0.17812 | 0.17846 | sup 0.17616 (ha 9 candles) | 0.00244 | -0.0060% | — | sem_zona |
| 2026-10-09 17:05 | WLD-USDT-SWAP | 0.49340 | 0.49840/0.49150 | 0.49340 | sup 0.48590 (ha 5 candles) | 0.00774 | -0.0044% | — | sem_zona |
| 2026-10-09 17:05 | SUI-USDT-SWAP | 1.0550 | 1.0662/1.0520 | 1.0550 | sup 1.0480 (ha 5 candles) | 0.01421 | -0.0028% | — | sem_zona |
| 2026-10-09 17:05 | UNI-USDT-SWAP | 7.2480 | 7.3090/7.2270 | 7.2480 | sup 7.2550 (ha 5 candles) | 0.09614 | 0.0008% | A/venda@7.2550 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-09 17:05 | LINK-USDT-SWAP | 12.75 | 12.84/12.71 | 12.75 | sup 12.68 (ha 5 candles) | 0.12300 | -0.0020% | — | sem_zona |
| 2026-10-09 18:05 | BTC-USDT-SWAP | 82470.0 | 82486.4/82276.1 | 82297.6 | sup 82353.1 (ha 10 candles) | 416.76 | 0.0043% | — | invalidado_setup_A |
| 2026-10-09 18:05 | ETH-USDT-SWAP | 2481.8 | 2482.6/2474.6 | 2476.4 | sup 2475.2 (ha 7 candles) | 15.48 | 0.0037% | — | sem_zona |
| 2026-10-09 18:05 | SOL-USDT-SWAP | 108.98 | 109.23/108.41 | 108.44 | sup 109.09 (ha 6 candles) | 1.0664 | 0.0090% | A/venda@109.09 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-09 18:05 | XRP-USDT-SWAP | 1.3887 | 1.3912/1.3827 | 1.3829 | sup 1.3732 (ha 6 candles) | 0.01225 | -0.0037% | — | sem_zona |
| 2026-10-09 18:05 | DOGE-USDT-SWAP | 0.08478 | 0.08486/0.08433 | 0.08435 | sup 0.08376 (ha 6 candles) | 0.00070 | -0.0038% | — | sem_zona |
| 2026-10-09 18:05 | ARB-USDT-SWAP | 0.18082 | 0.18110/0.17842 | 0.17846 | sup 0.17616 (ha 10 candles) | 0.00254 | -0.0066% | — | sem_zona |
| 2026-10-09 18:05 | WLD-USDT-SWAP | 0.50020 | 0.50060/0.49340 | 0.49340 | sup 0.48590 (ha 6 candles) | 0.00798 | -0.0038% | — | sem_zona |
| 2026-10-09 18:05 | SUI-USDT-SWAP | 1.0620 | 1.0624/1.0546 | 1.0550 | sup 1.0480 (ha 6 candles) | 0.01425 | 0.0019% | — | sem_zona |
| 2026-10-09 18:05 | UNI-USDT-SWAP | 7.3000 | 7.3110/7.2460 | 7.2480 | sup 7.2550 (ha 6 candles) | 0.09514 | 0.0048% | — | invalidado_setup_A |
| 2026-10-09 18:05 | LINK-USDT-SWAP | 12.79 | 12.81/12.75 | 12.75 | sup 12.68 (ha 6 candles) | 0.12371 | 0.0009% | — | sem_zona |
| 2026-10-09 19:05 | BTC-USDT-SWAP | 82500.0 | 82552.3/82469.4 | 82297.6 | sup 82353.1 (ha 11 candles) | 410.54 | 0.0031% | — | sem_zona |
| 2026-10-09 19:05 | ETH-USDT-SWAP | 2484.1 | 2484.5/2481.7 | 2476.4 | sup 2475.2 (ha 8 candles) | 15.00 | 0.0042% | — | sem_zona |
| 2026-10-09 19:05 | SOL-USDT-SWAP | 108.97 | 109.19/108.91 | 108.44 | sup 109.09 (ha 7 candles) | 1.0479 | 0.0100% | — | descartado_rr_baixo_setup_A |
| 2026-10-09 19:05 | XRP-USDT-SWAP | 1.3929 | 1.3940/1.3887 | 1.3829 | sup 1.3732 (ha 7 candles) | 0.01213 | -0.0009% | — | sem_zona |
| 2026-10-09 19:05 | DOGE-USDT-SWAP | 0.08526 | 0.08533/0.08478 | 0.08435 | sup 0.08376 (ha 7 candles) | 0.00072 | -0.0014% | — | sem_zona |
| 2026-10-09 19:05 | ARB-USDT-SWAP | 0.18043 | 0.18126/0.18035 | 0.17846 | sup 0.17744 (ha 3 candles) | 0.00245 | -0.0072% | — | sem_zona |
| 2026-10-09 19:05 | WLD-USDT-SWAP | 0.50590 | 0.50730/0.49860 | 0.49340 | sup 0.48590 (ha 7 candles) | 0.00792 | 0.0008% | — | sem_zona |
| 2026-10-09 19:05 | SUI-USDT-SWAP | 1.0669 | 1.0676/1.0607 | 1.0550 | sup 1.0480 (ha 7 candles) | 0.01372 | 0.0049% | — | sem_zona |
| 2026-10-09 19:05 | UNI-USDT-SWAP | 7.2820 | 7.3030/7.2700 | 7.2480 | sup 7.2550 (ha 7 candles) | 0.09236 | 0.0052% | — | sem_zona |
| 2026-10-09 19:05 | LINK-USDT-SWAP | 12.82 | 12.83/12.78 | 12.75 | sup 12.68 (ha 7 candles) | 0.11950 | 0.0038% | — | sem_zona |
| 2026-10-09 20:05 | BTC-USDT-SWAP | 82586.1 | 82611.4/82394.7 | 82297.6 | sup 82234.8 (ha 3 candles) | 408.64 | 0.0026% | — | sem_zona |
| 2026-10-09 20:05 | ETH-USDT-SWAP | 2487.9 | 2489.6/2478.4 | 2476.4 | sup 2473.0 (ha 3 candles) | 15.03 | 0.0037% | — | sem_zona |
| 2026-10-09 20:05 | SOL-USDT-SWAP | 109.15 | 109.38/108.55 | 108.44 | sup 108.37 (ha 3 candles) | 1.0479 | 0.0090% | — | sem_zona |
| 2026-10-09 20:05 | XRP-USDT-SWAP | 1.3946 | 1.3954/1.3888 | 1.3829 | sup 1.3732 (ha 8 candles) | 0.01201 | -0.0000% | — | sem_zona |
| 2026-10-09 20:05 | DOGE-USDT-SWAP | 0.08537 | 0.08549/0.08500 | 0.08435 | sup 0.08414 (ha 3 candles) | 0.00073 | -0.0020% | — | sem_zona |
| 2026-10-09 20:05 | ARB-USDT-SWAP | 0.18080 | 0.18174/0.17937 | 0.17846 | sup 0.17744 (ha 4 candles) | 0.00251 | -0.0066% | — | sem_zona |
| 2026-10-09 20:05 | WLD-USDT-SWAP | 0.50660 | 0.51180/0.50240 | 0.49340 | sup 0.48590 (ha 8 candles) | 0.00817 | 0.0019% | — | sem_zona |
| 2026-10-09 20:05 | SUI-USDT-SWAP | 1.0671 | 1.0725/1.0604 | 1.0550 | sup 1.0520 (ha 3 candles) | 0.01389 | 0.0058% | — | sem_zona |
| 2026-10-09 20:05 | UNI-USDT-SWAP | 7.2780 | 7.2970/7.2290 | 7.2480 | sup 7.2270 (ha 3 candles) | 0.09293 | 0.0053% | — | sem_zona |
| 2026-10-09 20:05 | LINK-USDT-SWAP | 12.82 | 12.83/12.75 | 12.75 | sup 12.71 (ha 3 candles) | 0.11721 | 0.0049% | — | sem_zona |
| 2026-10-09 21:05 | BTC-USDT-SWAP | 82586.8 | 82647.0/82537.1 | 82586.8 | sup 82234.8 (ha 4 candles) | 405.69 | 0.0016% | — | sem_zona |
| 2026-10-09 21:05 | ETH-USDT-SWAP | 2486.4 | 2489.5/2486.2 | 2486.4 | sup 2473.0 (ha 4 candles) | 14.71 | 0.0032% | — | sem_zona |
| 2026-10-09 21:05 | SOL-USDT-SWAP | 109.09 | 109.32/108.98 | 109.09 | sup 108.37 (ha 4 candles) | 1.0450 | 0.0082% | — | sem_zona |
| 2026-10-09 21:05 | XRP-USDT-SWAP | 1.3949 | 1.3966/1.3929 | 1.3949 | sup 1.3732 (ha 9 candles) | 0.01185 | -0.0007% | — | sem_zona |
| 2026-10-09 21:05 | DOGE-USDT-SWAP | 0.08531 | 0.08541/0.08520 | 0.08531 | sup 0.08414 (ha 4 candles) | 0.00072 | -0.0018% | — | sem_zona |
| 2026-10-09 21:05 | ARB-USDT-SWAP | 0.18252 | 0.18361/0.18043 | 0.18252 | sup 0.17744 (ha 5 candles) | 0.00266 | -0.0063% | — | sem_zona |
| 2026-10-09 21:05 | WLD-USDT-SWAP | 0.50690 | 0.50840/0.50410 | 0.50690 | sup 0.48590 (ha 9 candles) | 0.00824 | 0.0041% | — | sem_zona |
| 2026-10-09 21:05 | SUI-USDT-SWAP | 1.0691 | 1.0721/1.0652 | 1.0691 | sup 1.0520 (ha 4 candles) | 0.01394 | 0.0078% | — | sem_zona |
| 2026-10-09 21:05 | UNI-USDT-SWAP | 7.3160 | 7.3380/7.2640 | 7.3160 | sup 7.2270 (ha 4 candles) | 0.09407 | 0.0052% | — | sem_zona |
| 2026-10-09 21:05 | LINK-USDT-SWAP | 12.80 | 12.83/12.79 | 12.80 | sup 12.71 (ha 4 candles) | 0.11657 | 0.0051% | — | sem_zona |
| 2026-10-09 22:05 | BTC-USDT-SWAP | 82525.1 | 82601.7/82499.9 | 82586.8 | sup 82234.8 (ha 5 candles) | 389.40 | 0.0007% | — | sem_zona |
| 2026-10-09 22:05 | ETH-USDT-SWAP | 2488.0 | 2490.3/2484.8 | 2486.4 | sup 2473.0 (ha 5 candles) | 13.95 | 0.0026% | — | sem_zona |
| 2026-10-09 22:05 | SOL-USDT-SWAP | 109.34 | 109.50/108.90 | 109.09 | sup 108.37 (ha 5 candles) | 1.0029 | 0.0084% | — | sem_zona |
| 2026-10-09 22:05 | XRP-USDT-SWAP | 1.3979 | 1.4019/1.3949 | 1.3949 | sup 1.3732 (ha 10 candles) | 0.01082 | -0.0004% | — | sem_zona |
| 2026-10-09 22:05 | DOGE-USDT-SWAP | 0.08567 | 0.08589/0.08523 | 0.08531 | sup 0.08414 (ha 5 candles) | 0.00069 | -0.0024% | — | sem_zona |
| 2026-10-09 22:05 | ARB-USDT-SWAP | 0.18522 | 0.18536/0.18218 | 0.18252 | sup 0.17744 (ha 6 candles) | 0.00264 | -0.0072% | — | sem_zona |
| 2026-10-09 22:05 | WLD-USDT-SWAP | 0.50850 | 0.51240/0.50340 | 0.50690 | sup 0.48590 (ha 10 candles) | 0.00823 | 0.0072% | — | sem_zona |
| 2026-10-09 22:05 | SUI-USDT-SWAP | 1.0725 | 1.0765/1.0649 | 1.0691 | sup 1.0520 (ha 5 candles) | 0.01322 | 0.0100% | — | sem_zona |
| 2026-10-09 22:05 | UNI-USDT-SWAP | 7.3220 | 7.3710/7.3010 | 7.3160 | sup 7.2270 (ha 5 candles) | 0.09271 | 0.0030% | — | sem_zona |
| 2026-10-09 22:05 | LINK-USDT-SWAP | 12.80 | 12.84/12.78 | 12.80 | sup 12.71 (ha 5 candles) | 0.10779 | 0.0076% | — | sem_zona |
| 2026-10-09 23:05 | BTC-USDT-SWAP | 82657.7 | 82728.0/82525.0 | 82586.8 | sup 82234.8 (ha 6 candles) | 326.83 | 0.0008% | — | sem_zona |
| 2026-10-09 23:05 | ETH-USDT-SWAP | 2494.6 | 2495.1/2487.6 | 2486.4 | sup 2473.0 (ha 6 candles) | 12.15 | 0.0020% | — | sem_zona |
| 2026-10-09 23:05 | SOL-USDT-SWAP | 109.88 | 109.95/109.26 | 109.09 | sup 108.37 (ha 6 candles) | 0.86857 | 0.0071% | — | sem_zona |
| 2026-10-09 23:05 | XRP-USDT-SWAP | 1.4078 | 1.4102/1.3976 | 1.3949 | sup 1.3732 (ha 11 candles) | 0.00999 | -0.0014% | — | sem_zona |
| 2026-10-09 23:05 | DOGE-USDT-SWAP | 0.08615 | 0.08628/0.08561 | 0.08531 | sup 0.08414 (ha 6 candles) | 0.00063 | -0.0034% | — | sem_zona |
| 2026-10-09 23:05 | ARB-USDT-SWAP | 0.18596 | 0.18627/0.18355 | 0.18252 | sup 0.17744 (ha 7 candles) | 0.00252 | -0.0076% | — | sem_zona |
| 2026-10-09 23:05 | WLD-USDT-SWAP | 0.52290 | 0.52420/0.50730 | 0.50690 | sup 0.48590 (ha 11 candles) | 0.00856 | 0.0094% | B/venda@0.52210 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-09 23:05 | SUI-USDT-SWAP | 1.0900 | 1.0943/1.0700 | 1.0691 | sup 1.0520 (ha 6 candles) | 0.01325 | 0.0100% | — | sem_zona |
| 2026-10-09 23:05 | UNI-USDT-SWAP | 7.3820 | 7.3890/7.3110 | 7.3160 | sup 7.2270 (ha 6 candles) | 0.08671 | 0.0003% | — | sem_zona |
| 2026-10-09 23:05 | LINK-USDT-SWAP | 12.86 | 12.87/12.78 | 12.80 | sup 12.71 (ha 6 candles) | 0.09879 | 0.0084% | — | sem_zona |
| 2026-10-10 00:05 | BTC-USDT-SWAP | 82591.2 | 82703.4/82574.0 | 82586.8 | sup 82234.8 (ha 7 candles) | 299.37 | 0.0021% | — | sem_zona |
| 2026-10-10 00:05 | ETH-USDT-SWAP | 2492.0 | 2495.4/2490.8 | 2486.4 | sup 2473.0 (ha 7 candles) | 11.16 | 0.0013% | — | sem_zona |
| 2026-10-10 00:05 | SOL-USDT-SWAP | 109.88 | 110.02/109.65 | 109.09 | sup 108.37 (ha 7 candles) | 0.80857 | 0.0060% | — | sem_zona |
| 2026-10-10 00:05 | XRP-USDT-SWAP | 1.4060 | 1.4093/1.4047 | 1.3949 | sup 1.3732 (ha 12 candles) | 0.00915 | -0.0045% | — | sem_zona |
| 2026-10-10 00:05 | DOGE-USDT-SWAP | 0.08654 | 0.08666/0.08604 | 0.08531 | sup 0.08414 (ha 7 candles) | 0.00062 | -0.0031% | — | sem_zona |
| 2026-10-10 00:05 | ARB-USDT-SWAP | 0.18440 | 0.18599/0.18363 | 0.18252 | sup 0.17744 (ha 8 candles) | 0.00256 | -0.0099% | — | sem_zona |
| 2026-10-10 00:05 | WLD-USDT-SWAP | 0.52330 | 0.52880/0.51830 | 0.50690 | sup 0.48590 (ha 12 candles) | 0.00884 | 0.0100% | B/venda@0.52210 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-10 00:05 | SUI-USDT-SWAP | 1.0857 | 1.0941/1.0821 | 1.0691 | sup 1.0520 (ha 7 candles) | 0.01297 | 0.0100% | — | sem_zona |
| 2026-10-10 00:05 | UNI-USDT-SWAP | 7.3450 | 7.3990/7.3350 | 7.3160 | sup 7.2270 (ha 7 candles) | 0.08507 | -0.0049% | — | sem_zona |
| 2026-10-10 00:05 | LINK-USDT-SWAP | 12.84 | 12.87/12.82 | 12.80 | sup 12.71 (ha 7 candles) | 0.08936 | 0.0071% | — | sem_zona |
| 2026-10-10 01:05 | BTC-USDT-SWAP | 82563.3 | 82613.9/82530.0 | 82563.3 | sup 82234.8 (ha 8 candles) | 255.84 | 0.0039% | — | sem_zona |
| 2026-10-10 01:05 | ETH-USDT-SWAP | 2490.3 | 2492.8/2488.0 | 2490.3 | sup 2473.0 (ha 8 candles) | 9.5650 | 0.0009% | — | sem_zona |
| 2026-10-10 01:05 | SOL-USDT-SWAP | 109.64 | 109.89/109.50 | 109.64 | sup 108.37 (ha 8 candles) | 0.72714 | 0.0059% | — | sem_zona |
| 2026-10-10 01:05 | XRP-USDT-SWAP | 1.4030 | 1.4063/1.3992 | 1.4030 | — | 0.00852 | -0.0072% | — | sem_zona |
| 2026-10-10 01:05 | DOGE-USDT-SWAP | 0.08623 | 0.08660/0.08613 | 0.08623 | — | 0.00060 | -0.0039% | — | sem_zona |
| 2026-10-10 01:05 | ARB-USDT-SWAP | 0.18338 | 0.18508/0.18295 | 0.18338 | sup 0.17744 (ha 9 candles) | 0.00252 | -0.0112% | — | sem_zona |
| 2026-10-10 01:05 | WLD-USDT-SWAP | 0.52050 | 0.52430/0.51790 | 0.52050 | sup 0.48590 (ha 13 candles) | 0.00868 | 0.0081% | B/venda@0.52210 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-10 01:05 | SUI-USDT-SWAP | 1.0809 | 1.0878/1.0791 | 1.0809 | sup 1.0520 (ha 8 candles) | 0.01251 | 0.0078% | — | sem_zona |
| 2026-10-10 01:05 | UNI-USDT-SWAP | 7.3370 | 7.3860/7.2980 | 7.3370 | sup 7.2270 (ha 8 candles) | 0.08314 | -0.0102% | — | sem_zona |
| 2026-10-10 01:05 | LINK-USDT-SWAP | 12.81 | 12.84/12.77 | 12.81 | sup 12.71 (ha 8 candles) | 0.08643 | 0.0048% | — | sem_zona |
| 2026-10-10 02:05 | BTC-USDT-SWAP | 82650.0 | 82702.8/82563.2 | 82563.3 | sup 82234.8 (ha 9 candles) | 203.92 | 0.0051% | — | sem_zona |
| 2026-10-10 02:05 | ETH-USDT-SWAP | 2493.7 | 2494.3/2490.3 | 2490.3 | sup 2473.0 (ha 9 candles) | 8.0329 | 0.0010% | — | sem_zona |
| 2026-10-10 02:05 | SOL-USDT-SWAP | 109.80 | 109.94/109.56 | 109.64 | sup 108.37 (ha 9 candles) | 0.63286 | 0.0053% | — | sem_zona |
| 2026-10-10 02:05 | XRP-USDT-SWAP | 1.4068 | 1.4079/1.4026 | 1.4030 | — | 0.00758 | -0.0081% | — | sem_zona |
| 2026-10-10 02:05 | DOGE-USDT-SWAP | 0.08630 | 0.08668/0.08612 | 0.08623 | — | 0.00054 | -0.0034% | — | sem_zona |
| 2026-10-10 02:05 | ARB-USDT-SWAP | 0.18398 | 0.18487/0.18292 | 0.18338 | sup 0.17744 (ha 10 candles) | 0.00242 | -0.0106% | — | sem_zona |
| 2026-10-10 02:05 | WLD-USDT-SWAP | 0.53870 | 0.53900/0.52020 | 0.52050 | sup 0.48590 (ha 14 candles) | 0.00945 | 0.0099% | — | invalidado_setup_B |
| 2026-10-10 02:05 | SUI-USDT-SWAP | 1.0919 | 1.0953/1.0809 | 1.0809 | sup 1.0520 (ha 9 candles) | 0.01242 | 0.0065% | — | sem_zona |
| 2026-10-10 02:05 | UNI-USDT-SWAP | 7.4200 | 7.4310/7.3360 | 7.3370 | sup 7.2270 (ha 9 candles) | 0.07907 | -0.0140% | — | sem_zona |
| 2026-10-10 02:05 | LINK-USDT-SWAP | 12.81 | 12.85/12.78 | 12.81 | sup 12.71 (ha 9 candles) | 0.07700 | 0.0019% | — | sem_zona |
