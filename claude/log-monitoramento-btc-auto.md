# Log de Monitoramento Automatico -- Multi-Par (script gratuito, GitHub Actions)

> Gerado por script Python sem LLM (ver monitor/fetch_and_check.py). Fonte: OKX. Cobre os pares em PAIRS (configuracao no topo do script) -- BTC-USDT-SWAP e os demais adicionados na expansao de 07/09/2026. Leitura e MECANICA (regras objetivas da secao 4 do plano), sem a prosa qualitativa que o Claude gerava -- cole este log numa conversa do Claude se quiser a leitura interpretativa.

| Data/Hora (BRT) | Par | Close 1h | High/Low 1h | Close 4h | Swing 1h ref | ATR 1h | Funding | Zona ativa | Status checklist |
|---|---|---|---|---|---|---|---|---|---|
| 2026-11-14 07:06 | BTC-USDT-SWAP | 67370.2 | 67487.4/66952.8 | 67132.8 | sup 66400.1 (ha 5 candles) | 582.94 | -0.0017% | A/venda@68076.9 (0t/7c) | zona_mapeada_setup_A |
| 2026-11-14 07:06 | ETH-USDT-SWAP | 1912.3 | 1919.0/1893.5 | 1897.2 | sup 1875.0 (ha 7 candles) | 20.72 | -0.0013% | — | sem_zona |
| 2026-11-14 07:06 | SOL-USDT-SWAP | 75.90 | 76.17/75.17 | 75.20 | sup 74.77 (ha 5 candles) | 1.0464 | -0.0007% | A/venda@78.88 (0t/3c) | zona_mapeada_setup_A |
| 2026-11-14 07:06 | XRP-USDT-SWAP | 0.99070 | 0.99470/0.98250 | 0.98200 | sup 0.98350 (ha 7 candles) | 0.01159 | -0.0070% | — | invalidado_setup_A |
| 2026-11-14 07:06 | DOGE-USDT-SWAP | 0.06308 | 0.06328/0.06241 | 0.06257 | sup 0.06201 (ha 7 candles) | 0.00082 | -0.0041% | — | sem_zona |
| 2026-11-14 07:06 | ARB-USDT-SWAP | 0.14010 | 0.14047/0.13820 | 0.13863 | sup 0.13868 (ha 7 candles) | 0.00202 | -0.0036% | — | invalidado_setup_A |
| 2026-11-14 07:06 | WLD-USDT-SWAP | 0.28170 | 0.28310/0.27930 | 0.28090 | sup 0.28120 (ha 7 candles) | 0.00465 | -0.0229% | A/venda@0.29040 (0t/7c) | zona_mapeada_setup_A |
| 2026-11-14 07:06 | SUI-USDT-SWAP | 0.77450 | 0.77730/0.76690 | 0.76880 | sup 0.76660 (ha 7 candles) | 0.01076 | -0.0062% | — | sem_zona |
| 2026-11-14 07:06 | UNI-USDT-SWAP | 5.5460 | 5.5570/5.4970 | 5.4970 | sup 5.5090 (ha 7 candles) | 0.08679 | -0.0033% | — | invalidado_setup_A |
| 2026-11-14 07:06 | LINK-USDT-SWAP | 9.6410 | 9.6650/9.5440 | 9.5630 | sup 9.5210 (ha 7 candles) | 0.12207 | -0.0058% | — | sem_zona |
| 2026-11-14 08:06 | BTC-USDT-SWAP | 67269.4 | 67405.2/67140.5 | 67132.8 | sup 66400.1 (ha 6 candles) | 583.01 | -0.0009% | — | zona_expirada_setup_A |
| 2026-11-14 08:06 | ETH-USDT-SWAP | 1908.3 | 1914.0/1905.7 | 1897.2 | sup 1875.0 (ha 8 candles) | 20.47 | -0.0020% | — | sem_zona |
| 2026-11-14 08:06 | SOL-USDT-SWAP | 75.68 | 75.92/75.57 | 75.20 | sup 74.77 (ha 6 candles) | 1.0271 | -0.0021% | A/venda@78.88 (0t/4c) | zona_mapeada_setup_A |
| 2026-11-14 08:06 | XRP-USDT-SWAP | 0.99030 | 0.99260/0.98830 | 0.98200 | sup 0.97870 (ha 3 candles) | 0.01136 | -0.0069% | — | sem_zona |
| 2026-11-14 08:06 | DOGE-USDT-SWAP | 0.06287 | 0.06314/0.06282 | 0.06257 | sup 0.06222 (ha 3 candles) | 0.00081 | -0.0051% | — | sem_zona |
| 2026-11-14 08:06 | ARB-USDT-SWAP | 0.14002 | 0.14042/0.13937 | 0.13863 | sup 0.13868 (ha 8 candles) | 0.00195 | -0.0090% | — | sem_zona |
| 2026-11-14 08:06 | WLD-USDT-SWAP | 0.27860 | 0.28180/0.27810 | 0.28090 | sup 0.28120 (ha 8 candles) | 0.00459 | -0.0219% | — | zona_expirada_setup_A |
| 2026-11-14 08:06 | SUI-USDT-SWAP | 0.76980 | 0.77510/0.76900 | 0.76880 | sup 0.76420 (ha 3 candles) | 0.01050 | -0.0075% | — | sem_zona |
| 2026-11-14 08:06 | UNI-USDT-SWAP | 5.5050 | 5.5500/5.4980 | 5.4970 | sup 5.4760 (ha 3 candles) | 0.08436 | -0.0032% | — | sem_zona |
| 2026-11-14 08:06 | LINK-USDT-SWAP | 9.5980 | 9.6480/9.5960 | 9.5630 | sup 9.5030 (ha 3 candles) | 0.11993 | -0.0055% | — | sem_zona |
| 2026-11-14 09:06 | BTC-USDT-SWAP | 67246.3 | 67368.3/67065.5 | 67246.3 | sup 66400.1 (ha 7 candles) | 543.74 | 0.0012% | — | sem_zona |
| 2026-11-14 09:06 | ETH-USDT-SWAP | 1909.5 | 1910.8/1902.0 | 1909.5 | sup 1875.0 (ha 9 candles) | 19.05 | -0.0018% | — | sem_zona |
| 2026-11-14 09:06 | SOL-USDT-SWAP | 75.91 | 76.00/75.52 | 75.91 | sup 74.77 (ha 7 candles) | 0.95571 | -0.0027% | A/venda@78.88 (0t/5c) | zona_mapeada_setup_A |
| 2026-11-14 09:06 | XRP-USDT-SWAP | 0.99440 | 0.99440/0.98680 | 0.99440 | sup 0.97870 (ha 4 candles) | 0.01066 | -0.0058% | — | sem_zona |
| 2026-11-14 09:06 | DOGE-USDT-SWAP | 0.06300 | 0.06308/0.06273 | 0.06300 | sup 0.06222 (ha 4 candles) | 0.00076 | -0.0053% | — | sem_zona |
| 2026-11-14 09:06 | ARB-USDT-SWAP | 0.14165 | 0.14180/0.13968 | 0.14165 | sup 0.13800 (ha 3 candles) | 0.00199 | -0.0124% | — | sem_zona |
| 2026-11-14 09:06 | WLD-USDT-SWAP | 0.28010 | 0.28050/0.27730 | 0.28010 | sup 0.28120 (ha 9 candles) | 0.00449 | -0.0199% | A/venda@0.28120 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-14 09:06 | SUI-USDT-SWAP | 0.77210 | 0.77280/0.76740 | 0.77210 | sup 0.76420 (ha 4 candles) | 0.01015 | -0.0065% | — | sem_zona |
| 2026-11-14 09:06 | UNI-USDT-SWAP | 5.4980 | 5.5190/5.4590 | 5.4980 | sup 5.4760 (ha 4 candles) | 0.08136 | -0.0024% | — | sem_zona |
| 2026-11-14 09:06 | LINK-USDT-SWAP | 9.6100 | 9.6290/9.5550 | 9.6100 | sup 9.5030 (ha 4 candles) | 0.11564 | -0.0048% | — | sem_zona |
| 2026-11-14 10:06 | BTC-USDT-SWAP | 66980.0 | 67300.0/66886.4 | 67246.3 | sup 66400.1 (ha 8 candles) | 533.95 | 0.0029% | — | sem_zona |
| 2026-11-14 10:06 | ETH-USDT-SWAP | 1899.1 | 1911.0/1896.3 | 1909.5 | sup 1875.0 (ha 10 candles) | 18.84 | -0.0023% | — | sem_zona |
| 2026-11-14 10:06 | SOL-USDT-SWAP | 75.55 | 76.00/75.45 | 75.91 | sup 74.77 (ha 8 candles) | 0.90286 | -0.0039% | A/venda@78.88 (0t/6c) | zona_mapeada_setup_A |
| 2026-11-14 10:06 | XRP-USDT-SWAP | 0.99150 | 0.99630/0.99070 | 0.99440 | sup 0.97870 (ha 5 candles) | 0.01006 | -0.0042% | — | sem_zona |
| 2026-11-14 10:06 | DOGE-USDT-SWAP | 0.06264 | 0.06322/0.06258 | 0.06300 | sup 0.06222 (ha 5 candles) | 0.00074 | -0.0043% | — | sem_zona |
| 2026-11-14 10:06 | ARB-USDT-SWAP | 0.14024 | 0.14208/0.13973 | 0.14165 | sup 0.13800 (ha 4 candles) | 0.00205 | -0.0136% | — | sem_zona |
| 2026-11-14 10:06 | WLD-USDT-SWAP | 0.27690 | 0.28110/0.27550 | 0.28010 | sup 0.28120 (ha 10 candles) | 0.00453 | -0.0194% | — | descartado_rr_baixo_setup_A |
| 2026-11-14 10:06 | SUI-USDT-SWAP | 0.76550 | 0.77320/0.76450 | 0.77210 | sup 0.76420 (ha 5 candles) | 0.00977 | -0.0067% | — | sem_zona |
| 2026-11-14 10:06 | UNI-USDT-SWAP | 5.4250 | 5.5070/5.4100 | 5.4980 | sup 5.4760 (ha 5 candles) | 0.08186 | -0.0017% | A/venda@5.4760 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-14 10:06 | LINK-USDT-SWAP | 9.5410 | 9.6270/9.5330 | 9.6100 | sup 9.5030 (ha 5 candles) | 0.11171 | -0.0039% | — | sem_zona |
| 2026-11-14 11:06 | BTC-USDT-SWAP | 66814.8 | 67009.4/66509.9 | 67246.3 | sup 66400.1 (ha 9 candles) | 534.44 | 0.0045% | — | sem_zona |
| 2026-11-14 11:06 | ETH-USDT-SWAP | 1892.8 | 1899.5/1881.7 | 1909.5 | sup 1875.0 (ha 11 candles) | 19.12 | -0.0008% | — | sem_zona |
| 2026-11-14 11:06 | SOL-USDT-SWAP | 75.46 | 75.76/75.08 | 75.91 | sup 74.77 (ha 9 candles) | 0.87357 | -0.0031% | A/venda@78.88 (0t/7c) | zona_mapeada_setup_A |
| 2026-11-14 11:06 | XRP-USDT-SWAP | 0.99500 | 0.99770/0.98610 | 0.99440 | sup 0.97870 (ha 6 candles) | 0.01016 | -0.0023% | — | sem_zona |
| 2026-11-14 11:06 | DOGE-USDT-SWAP | 0.06254 | 0.06274/0.06227 | 0.06300 | sup 0.06222 (ha 6 candles) | 0.00072 | -0.0025% | — | sem_zona |
| 2026-11-14 11:06 | ARB-USDT-SWAP | 0.14023 | 0.14090/0.13944 | 0.14165 | sup 0.13800 (ha 5 candles) | 0.00200 | -0.0194% | — | sem_zona |
| 2026-11-14 11:06 | WLD-USDT-SWAP | 0.27660 | 0.27790/0.27520 | 0.28010 | sup 0.28120 (ha 11 candles) | 0.00445 | -0.0172% | — | sem_zona |
| 2026-11-14 11:06 | SUI-USDT-SWAP | 0.76170 | 0.76580/0.75890 | 0.77210 | sup 0.76420 (ha 6 candles) | 0.00959 | -0.0072% | A/venda@0.76420 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-14 11:06 | UNI-USDT-SWAP | 5.3440 | 5.4260/5.3300 | 5.4980 | sup 5.4760 (ha 6 candles) | 0.08457 | 0.0003% | A/venda@5.4760 (0t/1c) | zona_mapeada_setup_A |
| 2026-11-14 11:06 | LINK-USDT-SWAP | 9.5350 | 9.5740/9.4930 | 9.6100 | sup 9.5030 (ha 6 candles) | 0.10814 | -0.0048% | — | sem_zona |
| 2026-11-14 12:06 | BTC-USDT-SWAP | 65894.3 | 66851.2/65766.1 | 67246.3 | sup 66400.1 (ha 10 candles) | 588.98 | 0.0055% | A/venda@66400.1 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-14 12:06 | ETH-USDT-SWAP | 1853.0 | 1893.8/1841.4 | 1909.5 | sup 1875.0 (ha 12 candles) | 22.00 | -0.0020% | A/venda@1875.0 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-14 12:06 | SOL-USDT-SWAP | 74.04 | 75.52/73.66 | 75.91 | sup 74.77 (ha 10 candles) | 0.94429 | -0.0031% | — | zona_expirada_setup_A |
| 2026-11-14 12:06 | XRP-USDT-SWAP | 0.98170 | 0.99590/0.97640 | 0.99440 | sup 0.97870 (ha 7 candles) | 0.01117 | -0.0005% | — | sem_zona |
| 2026-11-14 12:06 | DOGE-USDT-SWAP | 0.06129 | 0.06258/0.06090 | 0.06300 | sup 0.06222 (ha 7 candles) | 0.00081 | -0.0010% | A/venda@0.06222 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-14 12:06 | ARB-USDT-SWAP | 0.13725 | 0.14050/0.13624 | 0.14165 | sup 0.13800 (ha 6 candles) | 0.00217 | -0.0160% | A/venda@0.13800 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-14 12:06 | WLD-USDT-SWAP | 0.27090 | 0.27680/0.26750 | 0.28010 | sup 0.28120 (ha 12 candles) | 0.00491 | -0.0141% | — | sem_zona |
| 2026-11-14 12:06 | SUI-USDT-SWAP | 0.74360 | 0.76220/0.74050 | 0.77210 | sup 0.76420 (ha 7 candles) | 0.01067 | -0.0067% | — | descartado_rr_baixo_setup_A |
| 2026-11-14 12:06 | UNI-USDT-SWAP | 5.1690 | 5.3470/5.1310 | 5.4980 | sup 5.4760 (ha 7 candles) | 0.09557 | 0.0008% | A/venda@5.4760 (0t/2c) | zona_mapeada_setup_A |
| 2026-11-14 12:06 | LINK-USDT-SWAP | 9.3180 | 9.5420/9.2470 | 9.6100 | sup 9.5030 (ha 7 candles) | 0.12443 | -0.0027% | A/venda@9.5030 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-14 13:06 | BTC-USDT-SWAP | 65714.3 | 66030.0/65030.3 | 65714.3 | sup 66400.1 (ha 11 candles) | 645.87 | 0.0045% | A/venda@66400.1 (0t/1c) | zona_mapeada_setup_A |
| 2026-11-14 13:06 | ETH-USDT-SWAP | 1840.3 | 1857.9/1823.2 | 1840.3 | sup 1875.0 (ha 13 candles) | 23.95 | -0.0032% | A/venda@1875.0 (0t/1c) | zona_mapeada_setup_A |
| 2026-11-14 13:06 | SOL-USDT-SWAP | 73.84 | 74.27/73.11 | 73.84 | sup 74.77 (ha 11 candles) | 0.96929 | -0.0028% | A/venda@74.77 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-14 13:06 | XRP-USDT-SWAP | 0.97150 | 0.98530/0.96630 | 0.97150 | sup 0.97870 (ha 8 candles) | 0.01206 | 0.0019% | A/venda@0.97870 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-14 13:06 | DOGE-USDT-SWAP | 0.06109 | 0.06149/0.06026 | 0.06109 | sup 0.06222 (ha 8 candles) | 0.00087 | -0.0003% | A/venda@0.06222 (0t/1c) | zona_mapeada_setup_A |
| 2026-11-14 13:06 | ARB-USDT-SWAP | 0.13825 | 0.13837/0.13578 | 0.13825 | sup 0.13800 (ha 7 candles) | 0.00226 | -0.0106% | A/venda@0.13800 (1t/0c) | zona_mapeada_setup_A |
| 2026-11-14 13:06 | WLD-USDT-SWAP | 0.27130 | 0.27340/0.26730 | 0.27130 | sup 0.28120 (ha 13 candles) | 0.00505 | -0.0138% | — | sem_zona |
| 2026-11-14 13:06 | SUI-USDT-SWAP | 0.74120 | 0.74680/0.73330 | 0.74120 | sup 0.76420 (ha 8 candles) | 0.01114 | -0.0068% | — | sem_zona |
| 2026-11-14 13:06 | UNI-USDT-SWAP | 5.1220 | 5.1860/5.0920 | 5.1220 | sup 5.4760 (ha 8 candles) | 0.09900 | 0.0029% | A/venda@5.4760 (0t/3c) | zona_mapeada_setup_A |
| 2026-11-14 13:06 | LINK-USDT-SWAP | 9.2730 | 9.3530/9.1780 | 9.2730 | sup 9.5030 (ha 8 candles) | 0.13129 | 0.0004% | A/venda@9.5030 (0t/1c) | zona_mapeada_setup_A |
| 2026-11-14 14:06 | BTC-USDT-SWAP | 65315.0 | 65719.5/64956.5 | 65714.3 | sup 66400.1 (ha 12 candles) | 598.26 | 0.0032% | A/venda@66400.1 (0t/2c) | zona_mapeada_setup_A |
| 2026-11-14 14:06 | ETH-USDT-SWAP | 1824.7 | 1841.1/1809.0 | 1840.3 | sup 1875.0 (ha 14 candles) | 22.45 | -0.0065% | A/venda@1875.0 (0t/2c) | zona_mapeada_setup_A |
| 2026-11-14 14:06 | SOL-USDT-SWAP | 72.36 | 73.91/71.85 | 73.84 | sup 74.77 (ha 12 candles) | 0.96429 | -0.0064% | A/venda@74.77 (0t/1c) | zona_mapeada_setup_A |
| 2026-11-14 14:06 | XRP-USDT-SWAP | 0.95620 | 0.97270/0.95000 | 0.97150 | sup 0.97870 (ha 9 candles) | 0.01197 | 0.0021% | A/venda@0.97870 (0t/1c) | zona_mapeada_setup_A |
| 2026-11-14 14:06 | DOGE-USDT-SWAP | 0.05992 | 0.06109/0.05943 | 0.06109 | sup 0.06222 (ha 9 candles) | 0.00083 | -0.0030% | A/venda@0.06222 (0t/2c) | zona_mapeada_setup_A |
| 2026-11-14 14:06 | ARB-USDT-SWAP | 0.13382 | 0.13831/0.13262 | 0.13825 | sup 0.13800 (ha 8 candles) | 0.00234 | -0.0058% | — | descartado_rr_baixo_setup_A |
| 2026-11-14 14:06 | WLD-USDT-SWAP | 0.26190 | 0.27190/0.25990 | 0.27130 | sup 0.28120 (ha 14 candles) | 0.00514 | -0.0164% | — | sem_zona |
| 2026-11-14 14:06 | SUI-USDT-SWAP | 0.72430 | 0.74240/0.71960 | 0.74120 | sup 0.76420 (ha 9 candles) | 0.01113 | -0.0100% | — | sem_zona |
| 2026-11-14 14:06 | UNI-USDT-SWAP | 4.9380 | 5.1310/4.9070 | 5.1220 | sup 5.4760 (ha 9 candles) | 0.10036 | -0.0006% | A/venda@5.4760 (0t/4c) | zona_mapeada_setup_A |
| 2026-11-14 14:06 | LINK-USDT-SWAP | 9.0720 | 9.2760/9.0140 | 9.2730 | sup 9.5030 (ha 9 candles) | 0.13150 | -0.0026% | A/venda@9.5030 (0t/2c) | zona_mapeada_setup_A |
| 2026-11-14 15:06 | BTC-USDT-SWAP | 65870.7 | 66170.9/65036.0 | 65714.3 | sup 66400.1 (ha 13 candles) | 596.06 | 0.0026% | A/venda@66400.1 (0t/3c) | zona_mapeada_setup_A |
| 2026-11-14 15:06 | ETH-USDT-SWAP | 1842.1 | 1857.3/1811.3 | 1840.3 | sup 1875.0 (ha 15 candles) | 23.03 | -0.0077% | A/venda@1875.0 (0t/3c) | zona_mapeada_setup_A |
| 2026-11-14 15:06 | SOL-USDT-SWAP | 72.80 | 73.63/71.95 | 73.84 | sup 74.77 (ha 13 candles) | 0.97857 | -0.0098% | A/venda@74.77 (0t/2c) | zona_mapeada_setup_A |
| 2026-11-14 15:06 | XRP-USDT-SWAP | 0.95940 | 0.96970/0.94490 | 0.97150 | sup 0.97870 (ha 10 candles) | 0.01261 | 0.0005% | A/venda@0.97870 (0t/2c) | zona_mapeada_setup_A |
| 2026-11-14 15:06 | DOGE-USDT-SWAP | 0.06034 | 0.06098/0.05950 | 0.06109 | sup 0.06222 (ha 10 candles) | 0.00085 | -0.0049% | A/venda@0.06222 (0t/3c) | zona_mapeada_setup_A |
| 2026-11-14 15:06 | ARB-USDT-SWAP | 0.13477 | 0.13694/0.13294 | 0.13825 | sup 0.13800 (ha 9 candles) | 0.00246 | -0.0030% | — | sem_zona |
| 2026-11-14 15:06 | WLD-USDT-SWAP | 0.26440 | 0.26870/0.25950 | 0.27130 | sup 0.28120 (ha 15 candles) | 0.00542 | -0.0218% | — | sem_zona |
| 2026-11-14 15:06 | SUI-USDT-SWAP | 0.73050 | 0.73860/0.71900 | 0.74120 | sup 0.76420 (ha 10 candles) | 0.01147 | -0.0118% | — | sem_zona |
| 2026-11-14 15:06 | UNI-USDT-SWAP | 5.0270 | 5.0980/4.9080 | 5.1220 | sup 5.4760 (ha 10 candles) | 0.10507 | -0.0026% | A/venda@5.4760 (0t/5c) | zona_mapeada_setup_A |
| 2026-11-14 15:06 | LINK-USDT-SWAP | 9.1590 | 9.2350/9.0130 | 9.2730 | sup 9.5030 (ha 10 candles) | 0.13407 | -0.0059% | A/venda@9.5030 (0t/3c) | zona_mapeada_setup_A |
| 2026-11-14 16:06 | BTC-USDT-SWAP | 65533.3 | 66049.4/65414.2 | 65714.3 | sup 66400.1 (ha 14 candles) | 585.62 | 0.0013% | A/venda@66400.1 (0t/4c) | zona_mapeada_setup_A |
| 2026-11-14 16:06 | ETH-USDT-SWAP | 1830.2 | 1847.1/1825.0 | 1840.3 | sup 1875.0 (ha 16 candles) | 22.74 | -0.0085% | A/venda@1875.0 (0t/4c) | zona_mapeada_setup_A |
| 2026-11-14 16:06 | SOL-USDT-SWAP | 72.19 | 73.08/71.99 | 73.84 | sup 74.77 (ha 14 candles) | 0.98643 | -0.0119% | A/venda@74.77 (0t/3c) | zona_mapeada_setup_A |
| 2026-11-14 16:06 | XRP-USDT-SWAP | 0.95430 | 0.96420/0.94860 | 0.97150 | sup 0.97870 (ha 11 candles) | 0.01299 | 0.0004% | A/venda@0.97870 (0t/3c) | zona_mapeada_setup_A |
| 2026-11-14 16:06 | DOGE-USDT-SWAP | 0.05996 | 0.06057/0.05974 | 0.06109 | sup 0.06222 (ha 11 candles) | 0.00085 | -0.0060% | A/venda@0.06222 (0t/4c) | zona_mapeada_setup_A |
| 2026-11-14 16:06 | ARB-USDT-SWAP | 0.13254 | 0.13541/0.13211 | 0.13825 | sup 0.13800 (ha 10 candles) | 0.00259 | -0.0006% | — | sem_zona |
| 2026-11-14 16:06 | WLD-USDT-SWAP | 0.26250 | 0.26560/0.26060 | 0.27130 | sup 0.28120 (ha 16 candles) | 0.00555 | -0.0205% | — | sem_zona |
| 2026-11-14 16:06 | SUI-USDT-SWAP | 0.72710 | 0.73400/0.72410 | 0.74120 | sup 0.76420 (ha 11 candles) | 0.01162 | -0.0117% | — | sem_zona |
| 2026-11-14 16:06 | UNI-USDT-SWAP | 4.9390 | 5.0500/4.9130 | 5.1220 | sup 5.4760 (ha 11 candles) | 0.10871 | -0.0035% | A/venda@5.4760 (0t/6c) | zona_mapeada_setup_A |
| 2026-11-14 16:06 | LINK-USDT-SWAP | 9.0950 | 9.2030/9.0640 | 9.2730 | sup 9.5030 (ha 11 candles) | 0.13550 | -0.0090% | A/venda@9.5030 (0t/4c) | zona_mapeada_setup_A |
| 2026-11-14 17:06 | BTC-USDT-SWAP | 65692.6 | 65834.0/65330.6 | 65692.6 | sup 64956.5 (ha 3 candles) | 588.94 | 0.0000% | A/venda@66400.1 (0t/5c) | zona_mapeada_setup_A |
| 2026-11-14 17:06 | ETH-USDT-SWAP | 1834.1 | 1840.9/1822.3 | 1834.1 | sup 1809.0 (ha 3 candles) | 22.98 | -0.0089% | A/venda@1875.0 (0t/5c) | zona_mapeada_setup_A |
| 2026-11-14 17:06 | SOL-USDT-SWAP | 72.19 | 72.52/71.61 | 72.19 | sup 74.77 (ha 15 candles) | 0.99714 | -0.0125% | A/venda@74.77 (0t/4c) | zona_mapeada_setup_A |
| 2026-11-14 17:06 | XRP-USDT-SWAP | 0.95280 | 0.95700/0.94590 | 0.95280 | sup 0.97870 (ha 12 candles) | 0.01324 | -0.0014% | A/venda@0.97870 (0t/4c) | zona_mapeada_setup_A |
| 2026-11-14 17:06 | DOGE-USDT-SWAP | 0.05970 | 0.06019/0.05936 | 0.05970 | sup 0.06222 (ha 12 candles) | 0.00088 | -0.0066% | A/venda@0.06222 (0t/5c) | zona_mapeada_setup_A |
| 2026-11-14 17:06 | ARB-USDT-SWAP | 0.13123 | 0.13307/0.13068 | 0.13123 | sup 0.13800 (ha 11 candles) | 0.00263 | 0.0000% | — | sem_zona |
| 2026-11-14 17:06 | WLD-USDT-SWAP | 0.25940 | 0.26390/0.25830 | 0.25940 | sup 0.28120 (ha 17 candles) | 0.00571 | -0.0220% | — | sem_zona |
| 2026-11-14 17:06 | SUI-USDT-SWAP | 0.72500 | 0.73020/0.72080 | 0.72500 | sup 0.76420 (ha 12 candles) | 0.01167 | -0.0123% | — | sem_zona |
| 2026-11-14 17:06 | UNI-USDT-SWAP | 4.9150 | 4.9580/4.8670 | 4.9150 | sup 5.4760 (ha 12 candles) | 0.11071 | -0.0049% | A/venda@5.4760 (0t/7c) | zona_mapeada_setup_A |
| 2026-11-14 17:06 | LINK-USDT-SWAP | 9.0630 | 9.1230/9.0080 | 9.0630 | sup 9.5030 (ha 12 candles) | 0.13693 | -0.0113% | A/venda@9.5030 (0t/5c) | zona_mapeada_setup_A |
| 2026-11-14 18:06 | BTC-USDT-SWAP | 64734.3 | 65853.6/64444.0 | 65692.6 | sup 64956.5 (ha 4 candles) | 669.59 | -0.0007% | A/venda@66400.1 (0t/6c) | zona_mapeada_setup_A |
| 2026-11-14 18:06 | ETH-USDT-SWAP | 1782.7 | 1838.7/1768.6 | 1834.1 | sup 1809.0 (ha 4 candles) | 27.24 | -0.0101% | A/venda@1875.0 (0t/6c) | zona_mapeada_setup_A |
| 2026-11-14 18:06 | SOL-USDT-SWAP | 70.48 | 72.47/70.01 | 72.19 | sup 74.77 (ha 16 candles) | 1.1164 | -0.0132% | A/venda@74.77 (0t/5c) | zona_mapeada_setup_A |
| 2026-11-14 18:06 | XRP-USDT-SWAP | 0.92660 | 0.95680/0.91400 | 0.95280 | sup 0.97870 (ha 13 candles) | 0.01571 | -0.0020% | A/venda@0.97870 (0t/5c) | zona_mapeada_setup_A |
| 2026-11-14 18:06 | DOGE-USDT-SWAP | 0.05773 | 0.05995/0.05714 | 0.05970 | sup 0.06222 (ha 13 candles) | 0.00104 | -0.0065% | A/venda@0.06222 (0t/6c) | zona_mapeada_setup_A |
| 2026-11-14 18:06 | ARB-USDT-SWAP | 0.12752 | 0.13170/0.12547 | 0.13123 | sup 0.13800 (ha 12 candles) | 0.00293 | 0.0064% | — | sem_zona |
| 2026-11-14 18:06 | WLD-USDT-SWAP | 0.24920 | 0.26070/0.24550 | 0.25940 | sup 0.28120 (ha 18 candles) | 0.00638 | -0.0261% | A/venda@0.28120 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-14 18:06 | SUI-USDT-SWAP | 0.69860 | 0.72810/0.69150 | 0.72500 | sup 0.76420 (ha 13 candles) | 0.01356 | -0.0132% | — | sem_zona |
| 2026-11-14 18:06 | UNI-USDT-SWAP | 4.7790 | 4.9410/4.7170 | 4.9150 | sup 5.4760 (ha 13 candles) | 0.12071 | -0.0031% | — | zona_expirada_setup_A |
| 2026-11-14 18:06 | LINK-USDT-SWAP | 8.8230 | 9.1040/8.7440 | 9.0630 | sup 9.5030 (ha 13 candles) | 0.15579 | -0.0120% | A/venda@9.5030 (0t/6c) | zona_mapeada_setup_A |
| 2026-11-14 19:06 | BTC-USDT-SWAP | 64422.1 | 64947.4/63856.5 | 65692.6 | sup 64956.5 (ha 5 candles) | 714.21 | -0.0032% | A/venda@66400.1 (0t/7c) | zona_mapeada_setup_A |
| 2026-11-14 19:06 | ETH-USDT-SWAP | 1772.4 | 1794.2/1750.0 | 1834.1 | sup 1809.0 (ha 5 candles) | 29.13 | -0.0112% | A/venda@1875.0 (0t/7c) | zona_mapeada_setup_A |
| 2026-11-14 19:06 | SOL-USDT-SWAP | 69.87 | 70.85/68.75 | 72.19 | sup 74.77 (ha 17 candles) | 1.2086 | -0.0126% | A/venda@74.77 (0t/6c) | zona_mapeada_setup_A |
| 2026-11-14 19:06 | XRP-USDT-SWAP | 0.90990 | 0.93110/0.90400 | 0.95280 | sup 0.97870 (ha 14 candles) | 0.01648 | 0.0002% | A/venda@0.97870 (0t/6c) | zona_mapeada_setup_A |
| 2026-11-14 19:06 | DOGE-USDT-SWAP | 0.05685 | 0.05807/0.05589 | 0.05970 | sup 0.06222 (ha 14 candles) | 0.00113 | -0.0057% | A/venda@0.06222 (0t/7c) | zona_mapeada_setup_A |
| 2026-11-14 19:06 | ARB-USDT-SWAP | 0.12707 | 0.12865/0.12427 | 0.13123 | sup 0.13800 (ha 13 candles) | 0.00308 | 0.0094% | — | sem_zona |
| 2026-11-14 19:06 | WLD-USDT-SWAP | 0.25110 | 0.25410/0.24230 | 0.25940 | sup 0.28120 (ha 19 candles) | 0.00682 | -0.0338% | A/venda@0.28120 (0t/1c) | zona_mapeada_setup_A |
| 2026-11-14 19:06 | SUI-USDT-SWAP | 0.69150 | 0.70320/0.67530 | 0.72500 | sup 0.76420 (ha 14 candles) | 0.01459 | -0.0160% | — | sem_zona |
| 2026-11-14 19:06 | UNI-USDT-SWAP | 4.7500 | 4.8100/4.6100 | 4.9150 | sup 5.4760 (ha 14 candles) | 0.12814 | -0.0020% | — | sem_zona |
| 2026-11-14 19:06 | LINK-USDT-SWAP | 8.7690 | 8.8710/8.6180 | 9.0630 | sup 9.5030 (ha 14 candles) | 0.16436 | -0.0115% | A/venda@9.5030 (0t/7c) | zona_mapeada_setup_A |
| 2026-11-14 20:06 | BTC-USDT-SWAP | 63509.2 | 64422.1/63272.2 | 65692.6 | sup 64956.5 (ha 6 candles) | 770.49 | -0.0044% | — | zona_expirada_setup_A |
| 2026-11-14 20:06 | ETH-USDT-SWAP | 1744.1 | 1772.4/1727.8 | 1834.1 | sup 1809.0 (ha 6 candles) | 31.40 | -0.0105% | — | zona_expirada_setup_A |
| 2026-11-14 20:06 | SOL-USDT-SWAP | 69.06 | 70.00/68.51 | 72.19 | sup 74.77 (ha 18 candles) | 1.2764 | -0.0114% | A/venda@74.77 (0t/7c) | zona_mapeada_setup_A |
| 2026-11-14 20:06 | XRP-USDT-SWAP | 0.89810 | 0.91410/0.89260 | 0.95280 | sup 0.97870 (ha 15 candles) | 0.01753 | 0.0014% | A/venda@0.97870 (0t/7c) | zona_mapeada_setup_A |
| 2026-11-14 20:06 | DOGE-USDT-SWAP | 0.05610 | 0.05688/0.05534 | 0.05970 | sup 0.06222 (ha 15 candles) | 0.00121 | -0.0031% | — | zona_expirada_setup_A |
| 2026-11-14 20:06 | ARB-USDT-SWAP | 0.12605 | 0.12745/0.12393 | 0.13123 | sup 0.13800 (ha 14 candles) | 0.00326 | 0.0100% | — | sem_zona |
| 2026-11-14 20:06 | WLD-USDT-SWAP | 0.24630 | 0.25260/0.24500 | 0.25940 | sup 0.28120 (ha 20 candles) | 0.00720 | -0.0403% | A/venda@0.28120 (0t/2c) | zona_mapeada_setup_A |
| 2026-11-14 20:06 | SUI-USDT-SWAP | 0.68340 | 0.69340/0.67470 | 0.72500 | sup 0.76420 (ha 15 candles) | 0.01554 | -0.0180% | A/venda@0.76420 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-14 20:06 | UNI-USDT-SWAP | 4.7270 | 4.8130/4.6610 | 4.9150 | sup 5.4760 (ha 15 candles) | 0.13521 | 0.0021% | — | sem_zona |
| 2026-11-14 20:06 | LINK-USDT-SWAP | 8.6770 | 8.7920/8.5670 | 9.0630 | sup 9.5030 (ha 15 candles) | 0.17629 | -0.0091% | — | zona_expirada_setup_A |
| 2026-11-14 21:06 | BTC-USDT-SWAP | 64124.8 | 64183.5/63299.9 | 64124.8 | sup 64956.5 (ha 7 candles) | 795.42 | -0.0037% | A/venda@64956.5 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-14 21:06 | ETH-USDT-SWAP | 1768.4 | 1771.5/1734.1 | 1768.4 | sup 1809.0 (ha 7 candles) | 32.26 | -0.0095% | A/venda@1809.0 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-14 21:06 | SOL-USDT-SWAP | 70.23 | 70.29/68.78 | 70.23 | sup 74.77 (ha 19 candles) | 1.3129 | -0.0120% | — | zona_expirada_setup_A |
| 2026-11-14 21:06 | XRP-USDT-SWAP | 0.91370 | 0.91480/0.89220 | 0.91370 | sup 0.97870 (ha 16 candles) | 0.01827 | -0.0008% | — | zona_expirada_setup_A |
| 2026-11-14 21:06 | DOGE-USDT-SWAP | 0.05733 | 0.05736/0.05595 | 0.05733 | sup 0.06222 (ha 16 candles) | 0.00125 | -0.0021% | — | sem_zona |
| 2026-11-14 21:06 | ARB-USDT-SWAP | 0.12794 | 0.12854/0.12545 | 0.12794 | sup 0.13800 (ha 15 candles) | 0.00332 | 0.0100% | — | sem_zona |
| 2026-11-14 21:06 | WLD-USDT-SWAP | 0.25500 | 0.25510/0.24520 | 0.25500 | sup 0.28120 (ha 21 candles) | 0.00764 | -0.0470% | A/venda@0.28120 (0t/3c) | zona_mapeada_setup_A |
| 2026-11-14 21:06 | SUI-USDT-SWAP | 0.70040 | 0.70050/0.68010 | 0.70040 | sup 0.76420 (ha 16 candles) | 0.01626 | -0.0171% | A/venda@0.76420 (0t/1c) | zona_mapeada_setup_A |
| 2026-11-14 21:06 | UNI-USDT-SWAP | 4.8820 | 4.9090/4.7090 | 4.8820 | sup 5.4760 (ha 16 candles) | 0.14521 | -0.0001% | — | sem_zona |
| 2026-11-14 21:06 | LINK-USDT-SWAP | 8.8780 | 8.8850/8.6450 | 8.8780 | sup 9.5030 (ha 16 candles) | 0.18479 | -0.0066% | — | sem_zona |
| 2026-11-14 22:06 | BTC-USDT-SWAP | 63394.8 | 64553.9/63374.7 | 64124.8 | sup 64956.5 (ha 8 candles) | 860.74 | -0.0030% | A/venda@64956.5 (0t/1c) | zona_mapeada_setup_A |
| 2026-11-14 22:06 | ETH-USDT-SWAP | 1739.9 | 1778.5/1737.0 | 1768.4 | sup 1809.0 (ha 8 candles) | 34.64 | -0.0081% | A/venda@1809.0 (0t/1c) | zona_mapeada_setup_A |
| 2026-11-14 22:06 | SOL-USDT-SWAP | 69.33 | 70.64/69.29 | 70.23 | sup 74.77 (ha 20 candles) | 1.3843 | -0.0131% | — | sem_zona |
| 2026-11-14 22:06 | XRP-USDT-SWAP | 0.92160 | 0.93630/0.91220 | 0.91370 | sup 0.97870 (ha 17 candles) | 0.01969 | -0.0042% | — | sem_zona |
| 2026-11-14 22:06 | DOGE-USDT-SWAP | 0.05678 | 0.05788/0.05670 | 0.05733 | sup 0.06222 (ha 17 candles) | 0.00131 | -0.0045% | — | sem_zona |
| 2026-11-14 22:06 | ARB-USDT-SWAP | 0.12662 | 0.12951/0.12655 | 0.12794 | sup 0.13800 (ha 16 candles) | 0.00345 | 0.0100% | A/venda@0.13800 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-14 22:06 | WLD-USDT-SWAP | 0.25230 | 0.25910/0.25230 | 0.25500 | sup 0.24230 (ha 3 candles) | 0.00786 | -0.0591% | A/venda@0.28120 (0t/4c) | zona_mapeada_setup_A |
| 2026-11-14 22:06 | SUI-USDT-SWAP | 0.69290 | 0.70650/0.69260 | 0.70040 | sup 0.76420 (ha 17 candles) | 0.01681 | -0.0200% | A/venda@0.76420 (0t/2c) | zona_mapeada_setup_A |
| 2026-11-14 22:06 | UNI-USDT-SWAP | 4.7670 | 4.8920/4.7560 | 4.8820 | sup 4.6100 (ha 3 candles) | 0.15121 | -0.0019% | — | sem_zona |
| 2026-11-14 22:06 | LINK-USDT-SWAP | 8.8120 | 8.9350/8.7880 | 8.8780 | sup 9.5030 (ha 17 candles) | 0.19157 | -0.0051% | — | sem_zona |
| 2026-11-14 23:06 | BTC-USDT-SWAP | 62592.7 | 63437.1/61931.1 | 64124.8 | sup 64956.5 (ha 9 candles) | 946.69 | -0.0020% | A/venda@64956.5 (0t/2c) | zona_mapeada_setup_A |
| 2026-11-14 23:06 | ETH-USDT-SWAP | 1729.8 | 1741.7/1709.1 | 1768.4 | sup 1809.0 (ha 9 candles) | 36.34 | -0.0064% | A/venda@1809.0 (0t/2c) | zona_mapeada_setup_A |
| 2026-11-14 23:06 | SOL-USDT-SWAP | 67.78 | 69.44/67.33 | 70.23 | sup 74.77 (ha 21 candles) | 1.5007 | -0.0165% | — | sem_zona |
| 2026-11-14 23:06 | XRP-USDT-SWAP | 0.90670 | 0.92270/0.89870 | 0.91370 | sup 0.97870 (ha 18 candles) | 0.02086 | -0.0029% | — | sem_zona |
| 2026-11-14 23:06 | DOGE-USDT-SWAP | 0.05613 | 0.05686/0.05542 | 0.05733 | sup 0.05534 (ha 3 candles) | 0.00138 | -0.0057% | — | sem_zona |
| 2026-11-14 23:06 | ARB-USDT-SWAP | 0.12441 | 0.12686/0.12273 | 0.12794 | sup 0.13800 (ha 17 candles) | 0.00360 | 0.0100% | A/venda@0.13800 (0t/1c) | zona_mapeada_setup_A |
| 2026-11-14 23:06 | WLD-USDT-SWAP | 0.24960 | 0.25320/0.24690 | 0.25500 | sup 0.24230 (ha 4 candles) | 0.00808 | -0.0568% | A/venda@0.28120 (0t/5c) | zona_mapeada_setup_A |
| 2026-11-14 23:06 | SUI-USDT-SWAP | 0.68280 | 0.69440/0.67520 | 0.70040 | sup 0.67470 (ha 3 candles) | 0.01780 | -0.0205% | A/venda@0.76420 (0t/3c) | zona_mapeada_setup_A |
| 2026-11-14 23:06 | UNI-USDT-SWAP | 4.7410 | 4.7890/4.6760 | 4.8820 | sup 4.6100 (ha 4 candles) | 0.15500 | -0.0013% | — | sem_zona |
| 2026-11-14 23:06 | LINK-USDT-SWAP | 8.7050 | 8.8310/8.6150 | 8.8780 | sup 8.5670 (ha 3 candles) | 0.20171 | -0.0030% | — | sem_zona |
| 2026-11-15 00:06 | BTC-USDT-SWAP | 64866.4 | 65117.9/62455.9 | 64124.8 | sup 64956.5 (ha 10 candles) | 1107.3 | -0.0006% | A/venda@64956.5 (1t/0c) | zona_mapeada_setup_A |
| 2026-11-15 00:06 | ETH-USDT-SWAP | 1814.4 | 1822.8/1725.0 | 1768.4 | sup 1809.0 (ha 10 candles) | 42.28 | -0.0062% | A/venda@1809.0 (1t/0c) | zona_mapeada_setup_A |
| 2026-11-15 00:06 | SOL-USDT-SWAP | 71.26 | 71.54/67.47 | 70.23 | sup 74.77 (ha 22 candles) | 1.7521 | -0.0210% | — | sem_zona |
| 2026-11-15 00:06 | XRP-USDT-SWAP | 0.95320 | 0.95620/0.90350 | 0.91370 | sup 0.89220 (ha 3 candles) | 0.02422 | -0.0026% | — | sem_zona |
| 2026-11-15 00:06 | DOGE-USDT-SWAP | 0.05852 | 0.05870/0.05589 | 0.05733 | sup 0.05534 (ha 4 candles) | 0.00154 | -0.0075% | — | sem_zona |
| 2026-11-15 00:06 | ARB-USDT-SWAP | 0.13016 | 0.13067/0.12389 | 0.12794 | sup 0.13800 (ha 18 candles) | 0.00391 | 0.0100% | A/venda@0.13800 (0t/2c) | zona_mapeada_setup_A |
| 2026-11-15 00:06 | WLD-USDT-SWAP | 0.26240 | 0.26320/0.24880 | 0.25500 | sup 0.24230 (ha 5 candles) | 0.00871 | -0.0613% | A/venda@0.28120 (0t/6c) | zona_mapeada_setup_A |
| 2026-11-15 00:06 | SUI-USDT-SWAP | 0.71770 | 0.71970/0.68010 | 0.70040 | sup 0.67470 (ha 4 candles) | 0.02001 | -0.0217% | A/venda@0.76420 (0t/4c) | zona_mapeada_setup_A |
| 2026-11-15 00:06 | UNI-USDT-SWAP | 5.0080 | 5.0320/4.7360 | 4.8820 | sup 4.6100 (ha 5 candles) | 0.16921 | -0.0076% | — | sem_zona |
| 2026-11-15 00:06 | LINK-USDT-SWAP | 9.0960 | 9.1240/8.6670 | 8.8780 | sup 8.5670 (ha 4 candles) | 0.22764 | -0.0032% | — | sem_zona |
| 2026-11-15 01:06 | BTC-USDT-SWAP | 64787.3 | 65555.0/64711.0 | 64787.3 | sup 64956.5 (ha 11 candles) | 1131.9 | -0.0004% | — | descartado_rr_baixo_setup_A |
| 2026-11-15 01:06 | ETH-USDT-SWAP | 1817.9 | 1833.9/1812.1 | 1817.9 | sup 1809.0 (ha 11 candles) | 42.57 | -0.0053% | — | invalidado_setup_A |
| 2026-11-15 01:06 | SOL-USDT-SWAP | 71.30 | 71.98/71.12 | 71.30 | sup 74.77 (ha 23 candles) | 1.7650 | -0.0239% | — | sem_zona |
| 2026-11-15 01:06 | XRP-USDT-SWAP | 0.96650 | 0.96790/0.95270 | 0.96650 | sup 0.89220 (ha 4 candles) | 0.02448 | -0.0027% | — | sem_zona |
| 2026-11-15 01:06 | DOGE-USDT-SWAP | 0.05881 | 0.05912/0.05849 | 0.05881 | sup 0.05534 (ha 5 candles) | 0.00155 | -0.0070% | — | sem_zona |
| 2026-11-15 01:06 | ARB-USDT-SWAP | 0.13164 | 0.13191/0.13014 | 0.13164 | sup 0.13800 (ha 19 candles) | 0.00393 | 0.0057% | A/venda@0.13800 (0t/3c) | zona_mapeada_setup_A |
| 2026-11-15 01:06 | WLD-USDT-SWAP | 0.26270 | 0.26530/0.26080 | 0.26270 | sup 0.24230 (ha 6 candles) | 0.00884 | -0.0627% | A/venda@0.28120 (0t/7c) | zona_mapeada_setup_A |
| 2026-11-15 01:06 | SUI-USDT-SWAP | 0.72070 | 0.72600/0.71600 | 0.72070 | sup 0.67470 (ha 5 candles) | 0.02023 | -0.0196% | A/venda@0.76420 (0t/5c) | zona_mapeada_setup_A |
| 2026-11-15 01:06 | UNI-USDT-SWAP | 5.0360 | 5.0860/4.9870 | 5.0360 | sup 4.6100 (ha 6 candles) | 0.16943 | -0.0081% | — | sem_zona |
| 2026-11-15 01:06 | LINK-USDT-SWAP | 9.1120 | 9.1940/9.0600 | 9.1120 | sup 8.5670 (ha 5 candles) | 0.23143 | -0.0025% | — | sem_zona |
| 2026-11-15 02:06 | BTC-USDT-SWAP | 64902.4 | 65151.9/64620.0 | 64787.3 | sup 61931.1 (ha 3 candles) | 1092.4 | 0.0004% | — | sem_zona |
| 2026-11-15 02:06 | ETH-USDT-SWAP | 1812.2 | 1822.8/1811.3 | 1817.9 | sup 1709.1 (ha 3 candles) | 39.64 | -0.0046% | — | sem_zona |
| 2026-11-15 02:06 | SOL-USDT-SWAP | 70.86 | 71.55/70.82 | 71.30 | sup 67.33 (ha 3 candles) | 1.6843 | -0.0213% | — | sem_zona |
| 2026-11-15 02:06 | XRP-USDT-SWAP | 0.97210 | 0.97890/0.96290 | 0.96650 | sup 0.89220 (ha 5 candles) | 0.02423 | -0.0038% | — | sem_zona |
| 2026-11-15 02:06 | DOGE-USDT-SWAP | 0.05840 | 0.05898/0.05836 | 0.05881 | sup 0.05534 (ha 6 candles) | 0.00147 | -0.0058% | — | sem_zona |
| 2026-11-15 02:06 | ARB-USDT-SWAP | 0.13143 | 0.13266/0.13123 | 0.13164 | sup 0.12273 (ha 3 candles) | 0.00373 | 0.0052% | A/venda@0.13800 (0t/4c) | zona_mapeada_setup_A |
| 2026-11-15 02:06 | WLD-USDT-SWAP | 0.26180 | 0.26430/0.26120 | 0.26270 | sup 0.24230 (ha 7 candles) | 0.00839 | -0.0609% | — | zona_expirada_setup_A |
| 2026-11-15 02:06 | SUI-USDT-SWAP | 0.72050 | 0.72530/0.71730 | 0.72070 | sup 0.67470 (ha 6 candles) | 0.01925 | -0.0144% | A/venda@0.76420 (0t/6c) | zona_mapeada_setup_A |
| 2026-11-15 02:06 | UNI-USDT-SWAP | 5.0370 | 5.0840/5.0110 | 5.0360 | sup 4.6100 (ha 7 candles) | 0.15921 | -0.0088% | — | sem_zona |
| 2026-11-15 02:06 | LINK-USDT-SWAP | 9.1110 | 9.1640/9.0910 | 9.1120 | sup 8.5670 (ha 6 candles) | 0.21557 | -0.0014% | — | sem_zona |
| 2026-11-15 03:06 | BTC-USDT-SWAP | 64478.6 | 64998.0/64414.0 | 64787.3 | sup 61931.1 (ha 4 candles) | 1062.7 | 0.0006% | — | sem_zona |
| 2026-11-15 03:06 | ETH-USDT-SWAP | 1799.5 | 1812.8/1798.4 | 1817.9 | sup 1709.1 (ha 4 candles) | 38.19 | -0.0054% | — | sem_zona |
| 2026-11-15 03:06 | SOL-USDT-SWAP | 70.75 | 71.23/70.65 | 71.30 | sup 67.33 (ha 4 candles) | 1.6429 | -0.0167% | — | sem_zona |
| 2026-11-15 03:06 | XRP-USDT-SWAP | 0.95840 | 0.97480/0.95790 | 0.96650 | sup 0.89220 (ha 6 candles) | 0.02408 | -0.0050% | — | sem_zona |
| 2026-11-15 03:06 | DOGE-USDT-SWAP | 0.05805 | 0.05854/0.05797 | 0.05881 | sup 0.05534 (ha 7 candles) | 0.00143 | -0.0034% | — | sem_zona |
| 2026-11-15 03:06 | ARB-USDT-SWAP | 0.13212 | 0.13342/0.13116 | 0.13164 | sup 0.12273 (ha 4 candles) | 0.00371 | 0.0034% | A/venda@0.13800 (0t/5c) | zona_mapeada_setup_A |
| 2026-11-15 03:06 | WLD-USDT-SWAP | 0.26090 | 0.26290/0.26080 | 0.26270 | sup 0.24230 (ha 8 candles) | 0.00811 | -0.0560% | — | sem_zona |
| 2026-11-15 03:06 | SUI-USDT-SWAP | 0.71950 | 0.72360/0.71830 | 0.72070 | sup 0.67470 (ha 7 candles) | 0.01866 | -0.0120% | A/venda@0.76420 (0t/7c) | zona_mapeada_setup_A |
| 2026-11-15 03:06 | UNI-USDT-SWAP | 5.0140 | 5.0820/5.0110 | 5.0360 | sup 4.6100 (ha 8 candles) | 0.15757 | -0.0046% | — | sem_zona |
| 2026-11-15 03:06 | LINK-USDT-SWAP | 9.1060 | 9.1550/9.0910 | 9.1120 | sup 8.5670 (ha 7 candles) | 0.20764 | -0.0005% | — | sem_zona |
| 2026-11-15 04:06 | BTC-USDT-SWAP | 64425.3 | 64614.0/64136.8 | 64787.3 | sup 61931.1 (ha 5 candles) | 1042.3 | 0.0010% | — | sem_zona |
| 2026-11-15 04:06 | ETH-USDT-SWAP | 1791.8 | 1800.5/1782.6 | 1817.9 | sup 1709.1 (ha 5 candles) | 37.17 | -0.0044% | — | sem_zona |
| 2026-11-15 04:06 | SOL-USDT-SWAP | 70.42 | 70.94/70.01 | 71.30 | sup 67.33 (ha 5 candles) | 1.5621 | -0.0095% | — | sem_zona |
| 2026-11-15 04:06 | XRP-USDT-SWAP | 0.95820 | 0.96380/0.95110 | 0.96650 | sup 0.89220 (ha 7 candles) | 0.02336 | -0.0027% | — | sem_zona |
| 2026-11-15 04:06 | DOGE-USDT-SWAP | 0.05785 | 0.05815/0.05758 | 0.05881 | sup 0.05534 (ha 8 candles) | 0.00135 | -0.0014% | — | sem_zona |
| 2026-11-15 04:06 | ARB-USDT-SWAP | 0.13309 | 0.13391/0.13135 | 0.13164 | sup 0.12273 (ha 5 candles) | 0.00349 | 0.0040% | A/venda@0.13800 (0t/6c) | zona_mapeada_setup_A |
| 2026-11-15 04:06 | WLD-USDT-SWAP | 0.26020 | 0.26140/0.25860 | 0.26270 | sup 0.24230 (ha 9 candles) | 0.00745 | -0.0468% | — | sem_zona |
| 2026-11-15 04:06 | SUI-USDT-SWAP | 0.71880 | 0.72150/0.71200 | 0.72070 | sup 0.67470 (ha 8 candles) | 0.01771 | -0.0096% | — | zona_expirada_setup_A |
| 2026-11-15 04:06 | UNI-USDT-SWAP | 4.9930 | 5.0300/4.9670 | 5.0360 | sup 4.6100 (ha 9 candles) | 0.14607 | 0.0031% | — | sem_zona |
| 2026-11-15 04:06 | LINK-USDT-SWAP | 9.1030 | 9.1340/9.0440 | 9.1120 | sup 8.5670 (ha 8 candles) | 0.19536 | -0.0005% | — | sem_zona |
| 2026-11-15 05:06 | BTC-USDT-SWAP | 63977.4 | 64500.0/63733.2 | 63977.4 | sup 61931.1 (ha 6 candles) | 1016.0 | -0.0000% | — | sem_zona |
| 2026-11-15 05:06 | ETH-USDT-SWAP | 1781.0 | 1796.4/1771.7 | 1781.0 | sup 1709.1 (ha 6 candles) | 35.66 | -0.0043% | — | sem_zona |
| 2026-11-15 05:06 | SOL-USDT-SWAP | 69.91 | 70.50/69.46 | 69.91 | sup 67.33 (ha 6 candles) | 1.5164 | -0.0047% | — | sem_zona |
| 2026-11-15 05:06 | XRP-USDT-SWAP | 0.94710 | 0.95820/0.94250 | 0.94710 | sup 0.89220 (ha 8 candles) | 0.02271 | -0.0024% | — | sem_zona |
| 2026-11-15 05:06 | DOGE-USDT-SWAP | 0.05752 | 0.05798/0.05707 | 0.05752 | sup 0.05534 (ha 9 candles) | 0.00131 | -0.0012% | — | sem_zona |
| 2026-11-15 05:06 | ARB-USDT-SWAP | 0.13214 | 0.13398/0.13155 | 0.13214 | sup 0.12273 (ha 6 candles) | 0.00337 | 0.0033% | A/venda@0.13800 (0t/7c) | zona_mapeada_setup_A |
| 2026-11-15 05:06 | WLD-USDT-SWAP | 0.25910 | 0.26100/0.25760 | 0.25910 | sup 0.24230 (ha 10 candles) | 0.00704 | -0.0375% | — | sem_zona |
| 2026-11-15 05:06 | SUI-USDT-SWAP | 0.71380 | 0.71890/0.71030 | 0.71380 | sup 0.67470 (ha 9 candles) | 0.01693 | -0.0086% | — | sem_zona |
| 2026-11-15 05:06 | UNI-USDT-SWAP | 4.9640 | 5.0090/4.9400 | 4.9640 | sup 4.6100 (ha 10 candles) | 0.13743 | 0.0071% | — | sem_zona |
| 2026-11-15 05:06 | LINK-USDT-SWAP | 9.0320 | 9.1160/8.9850 | 9.0320 | sup 8.5670 (ha 9 candles) | 0.18886 | -0.0004% | — | sem_zona |
| 2026-11-15 06:06 | BTC-USDT-SWAP | 65181.2 | 65264.9/63844.1 | 63977.4 | sup 61931.1 (ha 7 candles) | 1072.1 | -0.0004% | — | sem_zona |
| 2026-11-15 06:06 | ETH-USDT-SWAP | 1810.2 | 1813.0/1776.3 | 1781.0 | sup 1709.1 (ha 7 candles) | 36.70 | -0.0052% | — | sem_zona |
| 2026-11-15 06:06 | SOL-USDT-SWAP | 71.06 | 71.13/69.74 | 69.91 | sup 67.33 (ha 7 candles) | 1.5379 | -0.0037% | — | sem_zona |
| 2026-11-15 06:06 | XRP-USDT-SWAP | 0.95610 | 0.95780/0.94500 | 0.94710 | sup 0.89220 (ha 9 candles) | 0.02251 | -0.0024% | — | sem_zona |
| 2026-11-15 06:06 | DOGE-USDT-SWAP | 0.05831 | 0.05840/0.05728 | 0.05752 | sup 0.05534 (ha 10 candles) | 0.00133 | -0.0043% | — | sem_zona |
| 2026-11-15 06:06 | ARB-USDT-SWAP | 0.13300 | 0.13315/0.13055 | 0.13214 | sup 0.12273 (ha 7 candles) | 0.00332 | 0.0027% | — | zona_expirada_setup_A |
| 2026-11-15 06:06 | WLD-USDT-SWAP | 0.25880 | 0.25910/0.25560 | 0.25910 | sup 0.24230 (ha 11 candles) | 0.00693 | -0.0313% | — | sem_zona |
| 2026-11-15 06:06 | SUI-USDT-SWAP | 0.71660 | 0.71740/0.70720 | 0.71380 | sup 0.67470 (ha 10 candles) | 0.01695 | -0.0092% | — | sem_zona |
| 2026-11-15 06:06 | UNI-USDT-SWAP | 5.0110 | 5.0220/4.9260 | 4.9640 | sup 4.6100 (ha 11 candles) | 0.13450 | 0.0063% | — | sem_zona |
| 2026-11-15 06:06 | LINK-USDT-SWAP | 9.1300 | 9.1410/8.9870 | 9.0320 | sup 8.5670 (ha 10 candles) | 0.18993 | -0.0021% | — | sem_zona |
| 2026-11-15 07:06 | BTC-USDT-SWAP | 65317.8 | 66122.7/65079.4 | 63977.4 | sup 61931.1 (ha 8 candles) | 1110.7 | -0.0009% | — | sem_zona |
| 2026-11-15 07:06 | ETH-USDT-SWAP | 1821.4 | 1844.8/1806.4 | 1781.0 | sup 1709.1 (ha 8 candles) | 38.11 | -0.0048% | — | sem_zona |
| 2026-11-15 07:06 | SOL-USDT-SWAP | 71.65 | 72.44/70.89 | 69.91 | sup 67.33 (ha 8 candles) | 1.5836 | -0.0054% | — | sem_zona |
| 2026-11-15 07:06 | XRP-USDT-SWAP | 0.96290 | 0.97180/0.95460 | 0.94710 | sup 0.89220 (ha 10 candles) | 0.02295 | -0.0036% | — | sem_zona |
| 2026-11-15 07:06 | DOGE-USDT-SWAP | 0.05861 | 0.05922/0.05823 | 0.05752 | sup 0.05534 (ha 11 candles) | 0.00134 | -0.0068% | — | sem_zona |
| 2026-11-15 07:06 | ARB-USDT-SWAP | 0.13420 | 0.13626/0.13269 | 0.13214 | sup 0.12273 (ha 8 candles) | 0.00341 | 0.0018% | — | sem_zona |
| 2026-11-15 07:06 | WLD-USDT-SWAP | 0.25970 | 0.26300/0.25840 | 0.25910 | sup 0.24230 (ha 12 candles) | 0.00686 | -0.0325% | — | sem_zona |
| 2026-11-15 07:06 | SUI-USDT-SWAP | 0.72470 | 0.73320/0.71530 | 0.71380 | sup 0.67470 (ha 11 candles) | 0.01756 | -0.0098% | — | sem_zona |
| 2026-11-15 07:06 | UNI-USDT-SWAP | 5.1120 | 5.1500/4.9970 | 4.9640 | sup 4.6100 (ha 12 candles) | 0.13893 | 0.0019% | — | sem_zona |
| 2026-11-15 07:06 | LINK-USDT-SWAP | 9.2120 | 9.2830/9.1110 | 9.0320 | sup 8.5670 (ha 11 candles) | 0.19400 | -0.0024% | — | sem_zona |
| 2026-11-15 08:06 | BTC-USDT-SWAP | 65559.6 | 65641.1/65304.2 | 63977.4 | sup 63733.2 (ha 3 candles) | 1034.0 | -0.0015% | — | sem_zona |
| 2026-11-15 08:06 | ETH-USDT-SWAP | 1830.3 | 1832.7/1821.1 | 1781.0 | sup 1771.7 (ha 3 candles) | 33.94 | -0.0065% | — | sem_zona |
| 2026-11-15 08:06 | SOL-USDT-SWAP | 72.10 | 72.30/71.62 | 69.91 | sup 69.46 (ha 3 candles) | 1.4564 | -0.0090% | — | sem_zona |
| 2026-11-15 08:06 | XRP-USDT-SWAP | 0.96500 | 0.96910/0.96050 | 0.94710 | sup 0.94250 (ha 3 candles) | 0.02051 | -0.0062% | — | sem_zona |
| 2026-11-15 08:06 | DOGE-USDT-SWAP | 0.05914 | 0.05917/0.05857 | 0.05752 | sup 0.05707 (ha 3 candles) | 0.00118 | -0.0105% | — | sem_zona |
| 2026-11-15 08:06 | ARB-USDT-SWAP | 0.13534 | 0.13562/0.13420 | 0.13214 | sup 0.12273 (ha 9 candles) | 0.00306 | 0.0006% | — | sem_zona |
| 2026-11-15 08:06 | WLD-USDT-SWAP | 0.26290 | 0.26310/0.25950 | 0.25910 | sup 0.24230 (ha 13 candles) | 0.00603 | -0.0405% | — | sem_zona |
| 2026-11-15 08:06 | SUI-USDT-SWAP | 0.73140 | 0.73240/0.72420 | 0.71380 | sup 0.67470 (ha 12 candles) | 0.01553 | -0.0101% | — | sem_zona |
| 2026-11-15 08:06 | UNI-USDT-SWAP | 5.1470 | 5.1590/5.1080 | 4.9640 | sup 4.6100 (ha 13 candles) | 0.12657 | -0.0034% | — | sem_zona |
| 2026-11-15 08:06 | LINK-USDT-SWAP | 9.2680 | 9.2760/9.2080 | 9.0320 | sup 8.9850 (ha 3 candles) | 0.17314 | -0.0022% | — | sem_zona |
| 2026-11-15 09:06 | BTC-USDT-SWAP | 65321.7 | 65559.5/65205.6 | 65321.7 | sup 63733.2 (ha 4 candles) | 981.40 | -0.0002% | — | sem_zona |
| 2026-11-15 09:06 | ETH-USDT-SWAP | 1822.7 | 1837.9/1821.5 | 1822.7 | sup 1771.7 (ha 4 candles) | 31.96 | -0.0073% | — | sem_zona |
| 2026-11-15 09:06 | SOL-USDT-SWAP | 72.25 | 72.72/71.86 | 72.25 | sup 69.46 (ha 4 candles) | 1.3679 | -0.0142% | — | sem_zona |
| 2026-11-15 09:06 | XRP-USDT-SWAP | 0.96230 | 0.96840/0.96050 | 0.96230 | sup 0.94250 (ha 4 candles) | 0.01914 | -0.0080% | — | sem_zona |
| 2026-11-15 09:06 | DOGE-USDT-SWAP | 0.05900 | 0.05937/0.05864 | 0.05900 | sup 0.05707 (ha 4 candles) | 0.00108 | -0.0159% | — | sem_zona |
| 2026-11-15 09:06 | ARB-USDT-SWAP | 0.13490 | 0.13617/0.13485 | 0.13490 | sup 0.13055 (ha 3 candles) | 0.00285 | -0.0007% | — | sem_zona |
| 2026-11-15 09:06 | WLD-USDT-SWAP | 0.26570 | 0.26710/0.26210 | 0.26570 | sup 0.25560 (ha 3 candles) | 0.00554 | -0.0520% | — | sem_zona |
| 2026-11-15 09:06 | SUI-USDT-SWAP | 0.72690 | 0.73340/0.72680 | 0.72690 | sup 0.70720 (ha 3 candles) | 0.01401 | -0.0121% | — | sem_zona |
| 2026-11-15 09:06 | UNI-USDT-SWAP | 5.1310 | 5.1970/5.1160 | 5.1310 | sup 4.9260 (ha 3 candles) | 0.11807 | -0.0055% | — | sem_zona |
| 2026-11-15 09:06 | LINK-USDT-SWAP | 9.2270 | 9.2920/9.2220 | 9.2270 | sup 8.9850 (ha 4 candles) | 0.16007 | -0.0022% | — | sem_zona |
| 2026-11-15 10:06 | BTC-USDT-SWAP | 65478.0 | 65555.0/65151.5 | 65321.7 | sup 63733.2 (ha 5 candles) | 928.09 | 0.0001% | — | sem_zona |
| 2026-11-15 10:06 | ETH-USDT-SWAP | 1834.9 | 1841.2/1812.1 | 1822.7 | sup 1771.7 (ha 5 candles) | 30.85 | -0.0078% | — | sem_zona |
| 2026-11-15 10:06 | SOL-USDT-SWAP | 72.81 | 72.94/71.98 | 72.25 | sup 69.46 (ha 5 candles) | 1.3300 | -0.0186% | — | sem_zona |
| 2026-11-15 10:06 | XRP-USDT-SWAP | 0.96750 | 0.97350/0.95910 | 0.96230 | sup 0.94250 (ha 5 candles) | 0.01863 | -0.0085% | — | sem_zona |
| 2026-11-15 10:06 | DOGE-USDT-SWAP | 0.05930 | 0.05942/0.05879 | 0.05900 | sup 0.05707 (ha 5 candles) | 0.00102 | -0.0165% | — | sem_zona |
| 2026-11-15 10:06 | ARB-USDT-SWAP | 0.13601 | 0.13664/0.13448 | 0.13490 | sup 0.13055 (ha 4 candles) | 0.00275 | -0.0009% | — | sem_zona |
| 2026-11-15 10:06 | WLD-USDT-SWAP | 0.26570 | 0.26780/0.26470 | 0.26570 | sup 0.25560 (ha 4 candles) | 0.00522 | -0.0522% | — | sem_zona |
| 2026-11-15 10:06 | SUI-USDT-SWAP | 0.73400 | 0.73550/0.72540 | 0.72690 | sup 0.70720 (ha 4 candles) | 0.01339 | -0.0121% | — | sem_zona |
| 2026-11-15 10:06 | UNI-USDT-SWAP | 5.1680 | 5.1950/5.1210 | 5.1310 | sup 4.9260 (ha 4 candles) | 0.11250 | -0.0069% | — | sem_zona |
| 2026-11-15 10:06 | LINK-USDT-SWAP | 9.3240 | 9.3450/9.2000 | 9.2270 | sup 8.9850 (ha 5 candles) | 0.15436 | -0.0019% | — | sem_zona |
| 2026-11-15 11:06 | BTC-USDT-SWAP | 65405.3 | 65782.8/65333.0 | 65321.7 | sup 63733.2 (ha 6 candles) | 897.10 | 0.0007% | — | sem_zona |
| 2026-11-15 11:06 | ETH-USDT-SWAP | 1829.7 | 1840.6/1827.2 | 1822.7 | sup 1771.7 (ha 6 candles) | 29.13 | -0.0067% | — | sem_zona |
| 2026-11-15 11:06 | SOL-USDT-SWAP | 72.56 | 73.23/72.48 | 72.25 | sup 69.46 (ha 6 candles) | 1.2757 | -0.0204% | — | sem_zona |
| 2026-11-15 11:06 | XRP-USDT-SWAP | 0.96860 | 0.97790/0.96720 | 0.96230 | sup 0.94250 (ha 6 candles) | 0.01778 | -0.0083% | — | sem_zona |
| 2026-11-15 11:06 | DOGE-USDT-SWAP | 0.05919 | 0.05962/0.05919 | 0.05900 | sup 0.05707 (ha 6 candles) | 0.00095 | -0.0164% | — | sem_zona |
| 2026-11-15 11:06 | ARB-USDT-SWAP | 0.13534 | 0.13690/0.13525 | 0.13490 | sup 0.13055 (ha 5 candles) | 0.00265 | 0.0005% | — | sem_zona |
| 2026-11-15 11:06 | WLD-USDT-SWAP | 0.26380 | 0.26570/0.26360 | 0.26570 | sup 0.25560 (ha 5 candles) | 0.00466 | -0.0494% | — | sem_zona |
| 2026-11-15 11:06 | SUI-USDT-SWAP | 0.73010 | 0.73650/0.73010 | 0.72690 | sup 0.70720 (ha 5 candles) | 0.01239 | -0.0120% | — | sem_zona |
| 2026-11-15 11:06 | UNI-USDT-SWAP | 5.1640 | 5.2190/5.1530 | 5.1310 | sup 4.9260 (ha 5 candles) | 0.10293 | -0.0089% | — | sem_zona |
| 2026-11-15 11:06 | LINK-USDT-SWAP | 9.3090 | 9.3680/9.3080 | 9.2270 | sup 8.9850 (ha 6 candles) | 0.14150 | -0.0035% | — | sem_zona |
| 2026-11-15 12:06 | BTC-USDT-SWAP | 64736.8 | 65517.0/64411.7 | 65321.7 | sup 63733.2 (ha 7 candles) | 891.82 | 0.0016% | — | sem_zona |
| 2026-11-15 12:06 | ETH-USDT-SWAP | 1806.0 | 1832.6/1792.4 | 1822.7 | sup 1771.7 (ha 7 candles) | 29.04 | -0.0067% | — | sem_zona |
| 2026-11-15 12:06 | SOL-USDT-SWAP | 71.25 | 72.68/70.91 | 72.25 | sup 69.46 (ha 7 candles) | 1.3057 | -0.0190% | — | sem_zona |
| 2026-11-15 12:06 | XRP-USDT-SWAP | 0.95570 | 0.97220/0.95160 | 0.96230 | sup 0.94250 (ha 7 candles) | 0.01753 | -0.0092% | — | sem_zona |
| 2026-11-15 12:06 | DOGE-USDT-SWAP | 0.05844 | 0.05939/0.05806 | 0.05900 | sup 0.05707 (ha 7 candles) | 0.00096 | -0.0156% | — | sem_zona |
| 2026-11-15 12:06 | ARB-USDT-SWAP | 0.13558 | 0.13660/0.13403 | 0.13490 | sup 0.13055 (ha 6 candles) | 0.00262 | -0.0029% | — | sem_zona |
| 2026-11-15 12:06 | WLD-USDT-SWAP | 0.25930 | 0.26380/0.25660 | 0.26570 | sup 0.25560 (ha 6 candles) | 0.00469 | -0.0427% | — | sem_zona |
| 2026-11-15 12:06 | SUI-USDT-SWAP | 0.71940 | 0.73150/0.71350 | 0.72690 | sup 0.70720 (ha 6 candles) | 0.01269 | -0.0077% | — | sem_zona |
| 2026-11-15 12:06 | UNI-USDT-SWAP | 5.1250 | 5.2060/5.0730 | 5.1310 | sup 4.9260 (ha 6 candles) | 0.10271 | -0.0066% | — | sem_zona |
| 2026-11-15 12:06 | LINK-USDT-SWAP | 9.1810 | 9.3390/9.1200 | 9.2270 | sup 8.9850 (ha 7 candles) | 0.14664 | -0.0024% | — | sem_zona |
| 2026-11-15 13:06 | BTC-USDT-SWAP | 64719.1 | 64826.7/64434.6 | 64719.1 | sup 63733.2 (ha 8 candles) | 812.26 | 0.0010% | — | sem_zona |
| 2026-11-15 13:06 | ETH-USDT-SWAP | 1809.8 | 1813.1/1799.0 | 1809.8 | sup 1771.7 (ha 8 candles) | 27.72 | -0.0065% | — | sem_zona |
| 2026-11-15 13:06 | SOL-USDT-SWAP | 71.20 | 71.52/70.95 | 71.20 | sup 69.46 (ha 8 candles) | 1.1957 | -0.0153% | — | sem_zona |
| 2026-11-15 13:06 | XRP-USDT-SWAP | 0.95740 | 0.95930/0.95190 | 0.95740 | sup 0.94250 (ha 8 candles) | 0.01634 | -0.0085% | — | sem_zona |
| 2026-11-15 13:06 | DOGE-USDT-SWAP | 0.05852 | 0.05857/0.05819 | 0.05852 | sup 0.05707 (ha 8 candles) | 0.00088 | -0.0116% | — | sem_zona |
| 2026-11-15 13:06 | ARB-USDT-SWAP | 0.13468 | 0.13563/0.13352 | 0.13468 | sup 0.13055 (ha 7 candles) | 0.00247 | -0.0014% | — | sem_zona |
| 2026-11-15 13:06 | WLD-USDT-SWAP | 0.26210 | 0.26290/0.25830 | 0.26210 | sup 0.25560 (ha 7 candles) | 0.00457 | -0.0355% | — | sem_zona |
| 2026-11-15 13:06 | SUI-USDT-SWAP | 0.71970 | 0.72150/0.71570 | 0.71970 | sup 0.70720 (ha 7 candles) | 0.01173 | -0.0031% | — | sem_zona |
| 2026-11-15 13:06 | UNI-USDT-SWAP | 5.1290 | 5.1530/5.0990 | 5.1290 | sup 4.9260 (ha 7 candles) | 0.09850 | -0.0038% | — | sem_zona |
| 2026-11-15 13:06 | LINK-USDT-SWAP | 9.1980 | 9.2240/9.1500 | 9.1980 | sup 8.9850 (ha 8 candles) | 0.13650 | -0.0026% | — | sem_zona |
| 2026-11-15 14:06 | BTC-USDT-SWAP | 64674.9 | 64925.5/64224.4 | 64719.1 | sup 63733.2 (ha 9 candles) | 672.19 | 0.0011% | — | sem_zona |
| 2026-11-15 14:06 | ETH-USDT-SWAP | 1814.3 | 1829.9/1802.0 | 1809.8 | sup 1771.7 (ha 9 candles) | 22.72 | -0.0053% | — | sem_zona |
| 2026-11-15 14:06 | SOL-USDT-SWAP | 71.38 | 71.87/70.95 | 71.20 | sup 69.46 (ha 9 candles) | 0.97071 | -0.0104% | — | sem_zona |
| 2026-11-15 14:06 | XRP-USDT-SWAP | 0.95120 | 0.95990/0.94770 | 0.95740 | sup 0.94250 (ha 9 candles) | 0.01345 | -0.0079% | — | sem_zona |
| 2026-11-15 14:06 | DOGE-USDT-SWAP | 0.05840 | 0.05883/0.05818 | 0.05852 | sup 0.05707 (ha 9 candles) | 0.00073 | -0.0054% | — | sem_zona |
| 2026-11-15 14:06 | ARB-USDT-SWAP | 0.13595 | 0.13731/0.13433 | 0.13468 | sup 0.13055 (ha 8 candles) | 0.00220 | -0.0002% | — | sem_zona |
| 2026-11-15 14:06 | WLD-USDT-SWAP | 0.26340 | 0.26600/0.26090 | 0.26210 | sup 0.25560 (ha 8 candles) | 0.00391 | -0.0331% | — | sem_zona |
| 2026-11-15 14:06 | SUI-USDT-SWAP | 0.71810 | 0.72600/0.71560 | 0.71970 | sup 0.70720 (ha 8 candles) | 0.00964 | -0.0006% | — | sem_zona |
| 2026-11-15 14:06 | UNI-USDT-SWAP | 5.1510 | 5.2090/5.1170 | 5.1290 | sup 4.9260 (ha 8 candles) | 0.08393 | -0.0031% | — | sem_zona |
| 2026-11-15 14:06 | LINK-USDT-SWAP | 9.1840 | 9.2660/9.1440 | 9.1980 | sup 8.9850 (ha 9 candles) | 0.11257 | -0.0045% | — | sem_zona |
| 2026-11-15 15:06 | BTC-USDT-SWAP | 64539.7 | 64899.8/64366.1 | 64719.1 | sup 63733.2 (ha 10 candles) | 650.03 | 0.0019% | — | sem_zona |
| 2026-11-15 15:06 | ETH-USDT-SWAP | 1813.3 | 1818.8/1802.3 | 1809.8 | sup 1792.4 (ha 3 candles) | 22.34 | -0.0028% | — | sem_zona |
| 2026-11-15 15:06 | SOL-USDT-SWAP | 71.40 | 71.54/70.97 | 71.20 | sup 70.91 (ha 3 candles) | 0.95000 | -0.0057% | — | sem_zona |
| 2026-11-15 15:06 | XRP-USDT-SWAP | 0.94970 | 0.95340/0.94420 | 0.95740 | sup 0.94250 (ha 10 candles) | 0.01302 | -0.0064% | — | sem_zona |
| 2026-11-15 15:06 | DOGE-USDT-SWAP | 0.05867 | 0.05870/0.05836 | 0.05852 | sup 0.05806 (ha 3 candles) | 0.00070 | -0.0023% | — | sem_zona |
| 2026-11-15 15:06 | ARB-USDT-SWAP | 0.13519 | 0.13656/0.13442 | 0.13468 | sup 0.13055 (ha 9 candles) | 0.00223 | -0.0011% | — | sem_zona |
| 2026-11-15 15:06 | WLD-USDT-SWAP | 0.26340 | 0.26440/0.26140 | 0.26210 | sup 0.25660 (ha 3 candles) | 0.00380 | -0.0318% | — | sem_zona |
| 2026-11-15 15:06 | SUI-USDT-SWAP | 0.71890 | 0.72020/0.71390 | 0.71970 | sup 0.71350 (ha 3 candles) | 0.00938 | 0.0002% | — | sem_zona |
| 2026-11-15 15:06 | UNI-USDT-SWAP | 5.1450 | 5.1690/5.1110 | 5.1290 | sup 5.0730 (ha 3 candles) | 0.08100 | -0.0033% | — | sem_zona |
| 2026-11-15 15:06 | LINK-USDT-SWAP | 9.2140 | 9.2370/9.1670 | 9.1980 | sup 9.1200 (ha 3 candles) | 0.10800 | -0.0060% | — | sem_zona |
| 2026-11-15 16:06 | BTC-USDT-SWAP | 64702.5 | 64786.4/64467.0 | 64719.1 | sup 63733.2 (ha 11 candles) | 634.85 | 0.0025% | — | sem_zona |
| 2026-11-15 16:06 | ETH-USDT-SWAP | 1815.0 | 1819.0/1810.4 | 1809.8 | sup 1792.4 (ha 4 candles) | 22.14 | -0.0012% | — | sem_zona |
| 2026-11-15 16:06 | SOL-USDT-SWAP | 71.09 | 71.62/70.71 | 71.20 | sup 70.91 (ha 4 candles) | 0.96286 | -0.0013% | — | sem_zona |
| 2026-11-15 16:06 | XRP-USDT-SWAP | 0.95250 | 0.95270/0.94660 | 0.95740 | sup 0.94250 (ha 11 candles) | 0.01231 | -0.0047% | — | sem_zona |
| 2026-11-15 16:06 | DOGE-USDT-SWAP | 0.05867 | 0.05880/0.05849 | 0.05852 | sup 0.05806 (ha 4 candles) | 0.00068 | 0.0006% | — | sem_zona |
| 2026-11-15 16:06 | ARB-USDT-SWAP | 0.13472 | 0.13553/0.13427 | 0.13468 | sup 0.13352 (ha 3 candles) | 0.00222 | 0.0002% | — | sem_zona |
| 2026-11-15 16:06 | WLD-USDT-SWAP | 0.26450 | 0.26500/0.26230 | 0.26210 | sup 0.25660 (ha 4 candles) | 0.00377 | -0.0298% | — | sem_zona |
| 2026-11-15 16:06 | SUI-USDT-SWAP | 0.71940 | 0.72140/0.71440 | 0.71970 | sup 0.71350 (ha 4 candles) | 0.00931 | 0.0006% | — | sem_zona |
| 2026-11-15 16:06 | UNI-USDT-SWAP | 5.1540 | 5.1640/5.1230 | 5.1290 | sup 5.0730 (ha 4 candles) | 0.07871 | -0.0038% | — | sem_zona |
| 2026-11-15 16:06 | LINK-USDT-SWAP | 9.1960 | 9.2250/9.1550 | 9.1980 | sup 9.1200 (ha 4 candles) | 0.10779 | -0.0066% | — | sem_zona |
| 2026-11-15 17:06 | BTC-USDT-SWAP | 64915.2 | 65225.0/64670.8 | 64915.2 | sup 64224.4 (ha 3 candles) | 632.72 | 0.0022% | — | sem_zona |
| 2026-11-15 17:06 | ETH-USDT-SWAP | 1823.8 | 1830.0/1813.7 | 1823.8 | sup 1792.4 (ha 5 candles) | 22.28 | 0.0006% | — | sem_zona |
| 2026-11-15 17:06 | SOL-USDT-SWAP | 71.65 | 71.95/71.05 | 71.65 | sup 70.91 (ha 5 candles) | 0.98571 | 0.0012% | — | sem_zona |
| 2026-11-15 17:06 | XRP-USDT-SWAP | 0.96060 | 0.96190/0.95150 | 0.96060 | sup 0.94250 (ha 12 candles) | 0.01185 | -0.0043% | — | sem_zona |
| 2026-11-15 17:06 | DOGE-USDT-SWAP | 0.05899 | 0.05908/0.05864 | 0.05899 | sup 0.05806 (ha 5 candles) | 0.00067 | 0.0011% | — | sem_zona |
| 2026-11-15 17:06 | ARB-USDT-SWAP | 0.13498 | 0.13577/0.13453 | 0.13498 | sup 0.13352 (ha 4 candles) | 0.00214 | 0.0031% | — | sem_zona |
| 2026-11-15 17:06 | WLD-USDT-SWAP | 0.26470 | 0.26610/0.26350 | 0.26470 | sup 0.25660 (ha 5 candles) | 0.00381 | -0.0337% | — | sem_zona |
| 2026-11-15 17:06 | SUI-USDT-SWAP | 0.72490 | 0.72580/0.71900 | 0.72490 | sup 0.71350 (ha 5 candles) | 0.00941 | 0.0003% | — | sem_zona |
| 2026-11-15 17:06 | UNI-USDT-SWAP | 5.1840 | 5.2050/5.1460 | 5.1840 | sup 5.0730 (ha 5 candles) | 0.07786 | -0.0037% | — | sem_zona |
| 2026-11-15 17:06 | LINK-USDT-SWAP | 9.2320 | 9.2690/9.1930 | 9.2320 | sup 9.1200 (ha 5 candles) | 0.10864 | -0.0064% | — | sem_zona |
| 2026-11-15 18:06 | BTC-USDT-SWAP | 65102.4 | 65169.6/64637.4 | 64915.2 | sup 64224.4 (ha 4 candles) | 636.65 | 0.0009% | — | sem_zona |
| 2026-11-15 18:06 | ETH-USDT-SWAP | 1825.2 | 1833.8/1816.1 | 1823.8 | sup 1792.4 (ha 6 candles) | 22.26 | 0.0010% | — | sem_zona |
| 2026-11-15 18:06 | SOL-USDT-SWAP | 71.86 | 72.02/71.16 | 71.65 | sup 70.91 (ha 6 candles) | 0.98071 | 0.0018% | — | sem_zona |
| 2026-11-15 18:06 | XRP-USDT-SWAP | 0.96010 | 0.96490/0.95410 | 0.96060 | sup 0.94420 (ha 3 candles) | 0.01171 | -0.0048% | — | sem_zona |
| 2026-11-15 18:06 | DOGE-USDT-SWAP | 0.05893 | 0.05904/0.05853 | 0.05899 | sup 0.05806 (ha 6 candles) | 0.00067 | 0.0037% | — | sem_zona |
| 2026-11-15 18:06 | ARB-USDT-SWAP | 0.13461 | 0.13527/0.13397 | 0.13498 | sup 0.13352 (ha 5 candles) | 0.00205 | 0.0039% | — | sem_zona |
| 2026-11-15 18:06 | WLD-USDT-SWAP | 0.26530 | 0.26650/0.26310 | 0.26470 | sup 0.25660 (ha 6 candles) | 0.00385 | -0.0364% | — | sem_zona |
| 2026-11-15 18:06 | SUI-USDT-SWAP | 0.72870 | 0.73020/0.72100 | 0.72490 | sup 0.71350 (ha 6 candles) | 0.00939 | -0.0009% | — | sem_zona |
| 2026-11-15 18:06 | UNI-USDT-SWAP | 5.1680 | 5.2150/5.1420 | 5.1840 | sup 5.0730 (ha 6 candles) | 0.07857 | -0.0026% | — | sem_zona |
| 2026-11-15 18:06 | LINK-USDT-SWAP | 9.2380 | 9.2740/9.1670 | 9.2320 | sup 9.1200 (ha 6 candles) | 0.10986 | -0.0057% | — | sem_zona |
| 2026-11-15 19:06 | BTC-USDT-SWAP | 64982.3 | 65298.7/64862.3 | 64915.2 | sup 64224.4 (ha 5 candles) | 613.05 | 0.0005% | — | sem_zona |
| 2026-11-15 19:06 | ETH-USDT-SWAP | 1818.5 | 1826.5/1813.0 | 1823.8 | sup 1792.4 (ha 7 candles) | 21.46 | 0.0010% | — | sem_zona |
| 2026-11-15 19:06 | SOL-USDT-SWAP | 71.89 | 72.25/71.55 | 71.65 | sup 70.71 (ha 3 candles) | 0.95643 | 0.0011% | — | sem_zona |
| 2026-11-15 19:06 | XRP-USDT-SWAP | 0.96340 | 0.96820/0.95760 | 0.96060 | sup 0.94420 (ha 4 candles) | 0.01135 | -0.0064% | — | sem_zona |
| 2026-11-15 19:06 | DOGE-USDT-SWAP | 0.05896 | 0.05915/0.05869 | 0.05899 | sup 0.05806 (ha 7 candles) | 0.00064 | 0.0051% | — | sem_zona |
| 2026-11-15 19:06 | ARB-USDT-SWAP | 0.13419 | 0.13498/0.13370 | 0.13498 | sup 0.13352 (ha 6 candles) | 0.00197 | 0.0045% | — | sem_zona |
| 2026-11-15 19:06 | WLD-USDT-SWAP | 0.26660 | 0.26920/0.26320 | 0.26470 | sup 0.25660 (ha 7 candles) | 0.00404 | -0.0408% | — | sem_zona |
| 2026-11-15 19:06 | SUI-USDT-SWAP | 0.72790 | 0.73200/0.72450 | 0.72490 | sup 0.71350 (ha 7 candles) | 0.00931 | -0.0010% | — | sem_zona |
| 2026-11-15 19:06 | UNI-USDT-SWAP | 5.1480 | 5.1860/5.1260 | 5.1840 | sup 5.0730 (ha 7 candles) | 0.07793 | -0.0017% | — | sem_zona |
| 2026-11-15 19:06 | LINK-USDT-SWAP | 9.2440 | 9.2850/9.1990 | 9.2320 | sup 9.1200 (ha 7 candles) | 0.10664 | -0.0048% | — | sem_zona |
| 2026-11-15 20:06 | BTC-USDT-SWAP | 65198.0 | 65242.7/64903.2 | 64915.2 | sup 64224.4 (ha 6 candles) | 535.81 | -0.0005% | — | sem_zona |
| 2026-11-15 20:06 | ETH-USDT-SWAP | 1826.5 | 1829.2/1816.5 | 1823.8 | sup 1792.4 (ha 8 candles) | 19.75 | 0.0009% | — | sem_zona |
| 2026-11-15 20:06 | SOL-USDT-SWAP | 72.37 | 72.40/71.79 | 71.65 | sup 70.71 (ha 4 candles) | 0.90071 | -0.0015% | — | sem_zona |
| 2026-11-15 20:06 | XRP-USDT-SWAP | 0.97050 | 0.97050/0.96180 | 0.96060 | sup 0.94420 (ha 5 candles) | 0.01106 | -0.0066% | — | sem_zona |
| 2026-11-15 20:06 | DOGE-USDT-SWAP | 0.05931 | 0.05938/0.05890 | 0.05899 | sup 0.05806 (ha 8 candles) | 0.00059 | 0.0048% | — | sem_zona |
| 2026-11-15 20:06 | ARB-USDT-SWAP | 0.13461 | 0.13540/0.13407 | 0.13498 | sup 0.13352 (ha 7 candles) | 0.00188 | -0.0010% | — | sem_zona |
| 2026-11-15 20:06 | WLD-USDT-SWAP | 0.26730 | 0.26840/0.26630 | 0.26470 | sup 0.25660 (ha 8 candles) | 0.00394 | -0.0420% | — | sem_zona |
| 2026-11-15 20:06 | SUI-USDT-SWAP | 0.73170 | 0.73460/0.72690 | 0.72490 | sup 0.71350 (ha 8 candles) | 0.00914 | -0.0019% | — | sem_zona |
| 2026-11-15 20:06 | UNI-USDT-SWAP | 5.1580 | 5.1800/5.1410 | 5.1840 | sup 5.0730 (ha 8 candles) | 0.07386 | -0.0001% | — | sem_zona |
| 2026-11-15 20:06 | LINK-USDT-SWAP | 9.2570 | 9.2950/9.2330 | 9.2320 | sup 9.1200 (ha 8 candles) | 0.10007 | -0.0034% | — | sem_zona |
| 2026-11-15 21:06 | BTC-USDT-SWAP | 65311.0 | 65487.2/64785.6 | 65311.0 | sup 64224.4 (ha 7 candles) | 511.41 | -0.0013% | — | sem_zona |
| 2026-11-15 21:06 | ETH-USDT-SWAP | 1834.4 | 1843.0/1815.2 | 1834.4 | sup 1792.4 (ha 9 candles) | 18.99 | 0.0004% | — | sem_zona |
| 2026-11-15 21:06 | SOL-USDT-SWAP | 72.71 | 72.89/71.85 | 72.71 | sup 70.71 (ha 5 candles) | 0.86429 | -0.0038% | — | sem_zona |
| 2026-11-15 21:06 | XRP-USDT-SWAP | 0.97350 | 0.97730/0.96570 | 0.97350 | sup 0.94420 (ha 6 candles) | 0.01066 | -0.0070% | — | sem_zona |
| 2026-11-15 21:06 | DOGE-USDT-SWAP | 0.05984 | 0.06008/0.05901 | 0.05984 | sup 0.05806 (ha 9 candles) | 0.00060 | 0.0033% | — | sem_zona |
| 2026-11-15 21:06 | ARB-USDT-SWAP | 0.13467 | 0.13566/0.13372 | 0.13467 | sup 0.13352 (ha 8 candles) | 0.00176 | -0.0027% | — | sem_zona |
| 2026-11-15 21:06 | WLD-USDT-SWAP | 0.27110 | 0.27150/0.26720 | 0.27110 | sup 0.25660 (ha 9 candles) | 0.00391 | -0.0399% | — | sem_zona |
| 2026-11-15 21:06 | SUI-USDT-SWAP | 0.73700 | 0.73970/0.72960 | 0.73700 | sup 0.71350 (ha 9 candles) | 0.00858 | -0.0025% | — | sem_zona |
| 2026-11-15 21:06 | UNI-USDT-SWAP | 5.1790 | 5.2000/5.1170 | 5.1790 | sup 5.0730 (ha 9 candles) | 0.06886 | -0.0009% | — | sem_zona |
| 2026-11-15 21:06 | LINK-USDT-SWAP | 9.2900 | 9.3340/9.2120 | 9.2900 | sup 9.1200 (ha 9 candles) | 0.09650 | -0.0026% | — | sem_zona |
| 2026-11-15 22:06 | BTC-USDT-SWAP | 64884.7 | 65364.6/64617.1 | 65311.0 | sup 64224.4 (ha 8 candles) | 540.74 | -0.0028% | — | sem_zona |
| 2026-11-15 22:06 | ETH-USDT-SWAP | 1813.4 | 1837.6/1805.6 | 1834.4 | sup 1792.4 (ha 10 candles) | 20.44 | -0.0012% | — | sem_zona |
| 2026-11-15 22:06 | SOL-USDT-SWAP | 71.85 | 72.72/71.36 | 72.71 | sup 70.71 (ha 6 candles) | 0.91286 | -0.0063% | — | sem_zona |
| 2026-11-15 22:06 | XRP-USDT-SWAP | 0.96300 | 0.97410/0.95510 | 0.97350 | sup 0.94420 (ha 7 candles) | 0.01140 | -0.0080% | — | sem_zona |
| 2026-11-15 22:06 | DOGE-USDT-SWAP | 0.05926 | 0.05986/0.05888 | 0.05984 | sup 0.05806 (ha 10 candles) | 0.00062 | 0.0025% | — | sem_zona |
| 2026-11-15 22:06 | ARB-USDT-SWAP | 0.13351 | 0.13497/0.13295 | 0.13467 | sup 0.13352 (ha 9 candles) | 0.00181 | -0.0041% | A/venda@0.13352 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-15 22:06 | WLD-USDT-SWAP | 0.26560 | 0.27130/0.26380 | 0.27110 | sup 0.25660 (ha 10 candles) | 0.00419 | -0.0403% | — | sem_zona |
| 2026-11-15 22:06 | SUI-USDT-SWAP | 0.72780 | 0.73750/0.72280 | 0.73700 | sup 0.71350 (ha 10 candles) | 0.00904 | -0.0053% | — | sem_zona |
| 2026-11-15 22:06 | UNI-USDT-SWAP | 5.1200 | 5.1800/5.0810 | 5.1790 | sup 5.0730 (ha 10 candles) | 0.07229 | -0.0046% | — | sem_zona |
| 2026-11-15 22:06 | LINK-USDT-SWAP | 9.1800 | 9.3030/9.1310 | 9.2900 | sup 9.1200 (ha 10 candles) | 0.10393 | -0.0042% | — | sem_zona |
| 2026-11-15 23:06 | BTC-USDT-SWAP | 64537.4 | 64963.2/64510.7 | 65311.0 | sup 64224.4 (ha 9 candles) | 547.77 | -0.0033% | — | sem_zona |
| 2026-11-15 23:06 | ETH-USDT-SWAP | 1804.5 | 1816.3/1802.2 | 1834.4 | sup 1792.4 (ha 11 candles) | 20.27 | -0.0031% | — | sem_zona |
| 2026-11-15 23:06 | SOL-USDT-SWAP | 71.28 | 71.96/71.10 | 72.71 | sup 70.71 (ha 7 candles) | 0.91286 | -0.0081% | — | sem_zona |
| 2026-11-15 23:06 | XRP-USDT-SWAP | 0.95750 | 0.96450/0.95620 | 0.97350 | sup 0.94420 (ha 8 candles) | 0.01143 | -0.0083% | — | sem_zona |
| 2026-11-15 23:06 | DOGE-USDT-SWAP | 0.05852 | 0.05937/0.05844 | 0.05984 | sup 0.05806 (ha 11 candles) | 0.00064 | 0.0018% | — | sem_zona |
| 2026-11-15 23:06 | ARB-USDT-SWAP | 0.13334 | 0.13418/0.13300 | 0.13467 | sup 0.13352 (ha 10 candles) | 0.00180 | -0.0030% | — | confirmado_calibracao_setup_A |
| 2026-11-15 23:06 | WLD-USDT-SWAP | 0.26310 | 0.26600/0.26240 | 0.27110 | sup 0.25660 (ha 11 candles) | 0.00409 | -0.0369% | — | sem_zona |
| 2026-11-15 23:06 | SUI-USDT-SWAP | 0.72000 | 0.72890/0.71870 | 0.73700 | sup 0.71350 (ha 11 candles) | 0.00930 | -0.0067% | — | sem_zona |
| 2026-11-15 23:06 | UNI-USDT-SWAP | 5.1040 | 5.1350/5.0810 | 5.1790 | sup 5.0730 (ha 11 candles) | 0.07036 | -0.0051% | — | sem_zona |
| 2026-11-15 23:06 | LINK-USDT-SWAP | 9.1240 | 9.1940/9.1040 | 9.2900 | sup 9.1200 (ha 11 candles) | 0.10536 | -0.0033% | — | sem_zona |
| 2026-11-16 00:06 | BTC-USDT-SWAP | 65152.1 | 65338.9/64531.5 | 65311.0 | sup 64224.4 (ha 10 candles) | 576.62 | -0.0035% | — | sem_zona |
| 2026-11-16 00:06 | ETH-USDT-SWAP | 1824.3 | 1833.7/1803.9 | 1834.4 | sup 1792.4 (ha 12 candles) | 20.33 | -0.0046% | — | sem_zona |
| 2026-11-16 00:06 | SOL-USDT-SWAP | 72.19 | 72.69/71.24 | 72.71 | sup 70.71 (ha 8 candles) | 0.94786 | -0.0104% | — | sem_zona |
| 2026-11-16 00:06 | XRP-USDT-SWAP | 0.96600 | 0.97240/0.95690 | 0.97350 | sup 0.94420 (ha 9 candles) | 0.01151 | -0.0074% | — | sem_zona |
| 2026-11-16 00:06 | DOGE-USDT-SWAP | 0.05939 | 0.05956/0.05850 | 0.05984 | sup 0.05806 (ha 12 candles) | 0.00067 | 0.0011% | — | sem_zona |
| 2026-11-16 00:06 | ARB-USDT-SWAP | 0.13534 | 0.13612/0.13329 | 0.13467 | sup 0.13352 (ha 11 candles) | 0.00184 | -0.0030% | — | sem_zona |
| 2026-11-16 00:06 | WLD-USDT-SWAP | 0.26800 | 0.26920/0.26280 | 0.27110 | sup 0.25660 (ha 12 candles) | 0.00433 | -0.0345% | — | sem_zona |
| 2026-11-16 00:06 | SUI-USDT-SWAP | 0.73170 | 0.73440/0.71960 | 0.73700 | sup 0.71350 (ha 12 candles) | 0.00964 | -0.0064% | — | sem_zona |
| 2026-11-16 00:06 | UNI-USDT-SWAP | 5.2060 | 5.2420/5.1000 | 5.1790 | sup 5.0730 (ha 12 candles) | 0.07521 | -0.0075% | — | sem_zona |
| 2026-11-16 00:06 | LINK-USDT-SWAP | 9.2440 | 9.2970/9.1210 | 9.2900 | sup 9.1200 (ha 12 candles) | 0.10757 | -0.0024% | — | sem_zona |
| 2026-11-16 01:06 | BTC-USDT-SWAP | 65079.5 | 65211.7/64826.5 | 65079.5 | sup 64224.4 (ha 11 candles) | 572.01 | -0.0036% | — | sem_zona |
| 2026-11-16 01:06 | ETH-USDT-SWAP | 1826.6 | 1828.3/1815.1 | 1826.6 | sup 1792.4 (ha 13 candles) | 20.31 | -0.0066% | — | sem_zona |
| 2026-11-16 01:06 | SOL-USDT-SWAP | 72.12 | 72.38/71.63 | 72.12 | sup 70.71 (ha 9 candles) | 0.94786 | -0.0111% | — | sem_zona |
| 2026-11-16 01:06 | XRP-USDT-SWAP | 0.96310 | 0.96810/0.95840 | 0.96310 | sup 0.95510 (ha 3 candles) | 0.01144 | -0.0068% | — | sem_zona |
| 2026-11-16 01:06 | DOGE-USDT-SWAP | 0.05907 | 0.05945/0.05878 | 0.05907 | sup 0.05806 (ha 13 candles) | 0.00069 | 0.0011% | — | sem_zona |
| 2026-11-16 01:06 | ARB-USDT-SWAP | 0.13513 | 0.13566/0.13434 | 0.13513 | sup 0.13295 (ha 3 candles) | 0.00182 | -0.0033% | — | sem_zona |
| 2026-11-16 01:06 | WLD-USDT-SWAP | 0.26760 | 0.26970/0.26600 | 0.26760 | sup 0.25660 (ha 13 candles) | 0.00444 | -0.0313% | — | sem_zona |
| 2026-11-16 01:06 | SUI-USDT-SWAP | 0.72980 | 0.73380/0.72540 | 0.72980 | sup 0.71350 (ha 13 candles) | 0.00978 | -0.0067% | — | sem_zona |
| 2026-11-16 01:06 | UNI-USDT-SWAP | 5.2060 | 5.2340/5.1670 | 5.2060 | sup 5.0810 (ha 3 candles) | 0.07529 | -0.0079% | — | sem_zona |
| 2026-11-16 01:06 | LINK-USDT-SWAP | 9.2090 | 9.2490/9.1700 | 9.2090 | sup 9.1200 (ha 13 candles) | 0.10893 | -0.0012% | — | sem_zona |
| 2026-11-16 02:06 | BTC-USDT-SWAP | 64786.7 | 65159.3/64751.3 | 65079.5 | sup 64510.7 (ha 3 candles) | 522.20 | -0.0035% | — | sem_zona |
| 2026-11-16 02:06 | ETH-USDT-SWAP | 1817.5 | 1829.8/1816.0 | 1826.6 | sup 1802.2 (ha 3 candles) | 18.43 | -0.0080% | — | sem_zona |
| 2026-11-16 02:06 | SOL-USDT-SWAP | 71.54 | 72.28/71.41 | 72.12 | sup 71.10 (ha 3 candles) | 0.88357 | -0.0109% | — | sem_zona |
| 2026-11-16 02:06 | XRP-USDT-SWAP | 0.95750 | 0.96530/0.95670 | 0.96310 | sup 0.95510 (ha 4 candles) | 0.01058 | -0.0070% | — | sem_zona |
| 2026-11-16 02:06 | DOGE-USDT-SWAP | 0.05877 | 0.05922/0.05863 | 0.05907 | sup 0.05844 (ha 3 candles) | 0.00063 | 0.0015% | — | sem_zona |
| 2026-11-16 02:06 | ARB-USDT-SWAP | 0.13396 | 0.13549/0.13370 | 0.13513 | sup 0.13295 (ha 4 candles) | 0.00177 | -0.0021% | — | sem_zona |
| 2026-11-16 02:06 | WLD-USDT-SWAP | 0.26590 | 0.26870/0.26520 | 0.26760 | sup 0.26240 (ha 3 candles) | 0.00418 | -0.0273% | — | sem_zona |
| 2026-11-16 02:06 | SUI-USDT-SWAP | 0.72420 | 0.73220/0.72290 | 0.72980 | sup 0.71870 (ha 3 candles) | 0.00916 | -0.0053% | — | sem_zona |
| 2026-11-16 02:06 | UNI-USDT-SWAP | 5.1650 | 5.2270/5.1530 | 5.2060 | sup 5.0810 (ha 3 candles) | 0.07107 | -0.0063% | — | sem_zona |
| 2026-11-16 02:06 | LINK-USDT-SWAP | 9.1600 | 9.2380/9.1430 | 9.2090 | sup 9.1040 (ha 3 candles) | 0.10007 | -0.0003% | — | sem_zona |
| 2026-11-16 03:06 | BTC-USDT-SWAP | 64452.9 | 64893.7/64313.7 | 65079.5 | sup 64510.7 (ha 4 candles) | 535.62 | -0.0021% | A/venda@64510.7 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-16 03:06 | ETH-USDT-SWAP | 1812.3 | 1824.5/1806.2 | 1826.6 | sup 1802.2 (ha 4 candles) | 18.73 | -0.0073% | — | sem_zona |
| 2026-11-16 03:06 | SOL-USDT-SWAP | 71.20 | 71.85/70.98 | 72.12 | sup 71.10 (ha 4 candles) | 0.90500 | -0.0074% | — | sem_zona |
| 2026-11-16 03:06 | XRP-USDT-SWAP | 0.95230 | 0.96030/0.94960 | 0.96310 | sup 0.95510 (ha 5 candles) | 0.01081 | -0.0064% | A/venda@0.95510 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-16 03:06 | DOGE-USDT-SWAP | 0.05865 | 0.05903/0.05847 | 0.05907 | sup 0.05844 (ha 4 candles) | 0.00065 | 0.0011% | — | sem_zona |
| 2026-11-16 03:06 | ARB-USDT-SWAP | 0.13282 | 0.13405/0.13241 | 0.13513 | sup 0.13295 (ha 5 candles) | 0.00173 | -0.0021% | A/venda@0.13295 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-16 03:06 | WLD-USDT-SWAP | 0.26490 | 0.26680/0.26390 | 0.26760 | sup 0.26240 (ha 4 candles) | 0.00406 | -0.0238% | — | sem_zona |
| 2026-11-16 03:06 | SUI-USDT-SWAP | 0.72100 | 0.72680/0.71930 | 0.72980 | sup 0.71870 (ha 4 candles) | 0.00928 | -0.0043% | — | sem_zona |
| 2026-11-16 03:06 | UNI-USDT-SWAP | 5.1480 | 5.1870/5.1310 | 5.2060 | sup 5.0810 (ha 4 candles) | 0.07121 | -0.0034% | — | sem_zona |
| 2026-11-16 03:06 | LINK-USDT-SWAP | 9.1190 | 9.1920/9.0920 | 9.2090 | sup 9.1040 (ha 4 candles) | 0.10193 | -0.0016% | — | sem_zona |
| 2026-11-16 04:06 | BTC-USDT-SWAP | 64680.1 | 64734.9/64267.5 | 65079.5 | sup 64510.7 (ha 5 candles) | 518.93 | -0.0005% | — | invalidado_setup_A |
| 2026-11-16 04:06 | ETH-USDT-SWAP | 1816.4 | 1818.0/1806.0 | 1826.6 | sup 1802.2 (ha 5 candles) | 17.59 | -0.0061% | — | sem_zona |
| 2026-11-16 04:06 | SOL-USDT-SWAP | 71.21 | 71.43/70.78 | 72.12 | sup 71.10 (ha 5 candles) | 0.88571 | -0.0017% | — | sem_zona |
| 2026-11-16 04:06 | XRP-USDT-SWAP | 0.95480 | 0.95640/0.94870 | 0.96310 | sup 0.95510 (ha 6 candles) | 0.01049 | -0.0063% | A/venda@0.95510 (1t/0c) | zona_mapeada_setup_A |
| 2026-11-16 04:06 | DOGE-USDT-SWAP | 0.05887 | 0.05896/0.05840 | 0.05907 | sup 0.05844 (ha 5 candles) | 0.00064 | 0.0011% | — | sem_zona |
| 2026-11-16 04:06 | ARB-USDT-SWAP | 0.13284 | 0.13299/0.13172 | 0.13513 | sup 0.13295 (ha 6 candles) | 0.00161 | -0.0013% | A/venda@0.13295 (1t/0c) | zona_mapeada_setup_A |
| 2026-11-16 04:06 | WLD-USDT-SWAP | 0.26540 | 0.26600/0.26270 | 0.26760 | sup 0.26240 (ha 5 candles) | 0.00393 | -0.0218% | — | sem_zona |
| 2026-11-16 04:06 | SUI-USDT-SWAP | 0.72160 | 0.72360/0.71550 | 0.72980 | sup 0.71870 (ha 5 candles) | 0.00911 | -0.0034% | — | sem_zona |
| 2026-11-16 04:06 | UNI-USDT-SWAP | 5.1910 | 5.2050/5.1280 | 5.2060 | sup 5.0810 (ha 5 candles) | 0.07014 | -0.0009% | — | sem_zona |
| 2026-11-16 04:06 | LINK-USDT-SWAP | 9.1300 | 9.1470/9.0630 | 9.2090 | sup 9.1040 (ha 5 candles) | 0.09921 | -0.0024% | — | sem_zona |
| 2026-11-16 05:06 | BTC-USDT-SWAP | 64950.0 | 65039.9/64391.6 | 64950.0 | sup 64510.7 (ha 6 candles) | 527.11 | -0.0005% | — | sem_zona |
| 2026-11-16 05:06 | ETH-USDT-SWAP | 1820.4 | 1823.2/1803.7 | 1820.4 | sup 1802.2 (ha 6 candles) | 17.81 | -0.0051% | — | sem_zona |
| 2026-11-16 05:06 | SOL-USDT-SWAP | 71.34 | 71.54/70.58 | 71.34 | sup 71.10 (ha 6 candles) | 0.91357 | 0.0018% | — | sem_zona |
| 2026-11-16 05:06 | XRP-USDT-SWAP | 0.95930 | 0.96130/0.94890 | 0.95930 | sup 0.95510 (ha 7 candles) | 0.01072 | -0.0054% | — | invalidado_setup_A |
| 2026-11-16 05:06 | DOGE-USDT-SWAP | 0.05897 | 0.05910/0.05833 | 0.05897 | sup 0.05844 (ha 6 candles) | 0.00067 | 0.0009% | — | sem_zona |
| 2026-11-16 05:06 | ARB-USDT-SWAP | 0.13310 | 0.13375/0.13206 | 0.13310 | sup 0.13295 (ha 7 candles) | 0.00158 | 0.0014% | A/venda@0.13295 (2t/0c) | zona_mapeada_setup_A |
| 2026-11-16 05:06 | WLD-USDT-SWAP | 0.26560 | 0.26720/0.26330 | 0.26560 | sup 0.26240 (ha 6 candles) | 0.00399 | -0.0185% | — | sem_zona |
| 2026-11-16 05:06 | SUI-USDT-SWAP | 0.72350 | 0.72660/0.71690 | 0.72350 | sup 0.71870 (ha 6 candles) | 0.00936 | -0.0036% | — | sem_zona |
| 2026-11-16 05:06 | UNI-USDT-SWAP | 5.1890 | 5.2530/5.1620 | 5.1890 | sup 5.0810 (ha 6 candles) | 0.07250 | 0.0029% | — | sem_zona |
| 2026-11-16 05:06 | LINK-USDT-SWAP | 9.1610 | 9.1790/9.0590 | 9.1610 | sup 9.1040 (ha 6 candles) | 0.10279 | -0.0019% | — | sem_zona |
| 2026-11-16 06:06 | BTC-USDT-SWAP | 64431.4 | 64956.8/64384.1 | 64950.0 | sup 64510.7 (ha 7 candles) | 545.21 | -0.0005% | — | sem_zona |
| 2026-11-16 06:06 | ETH-USDT-SWAP | 1805.0 | 1820.7/1802.3 | 1820.4 | sup 1802.2 (ha 7 candles) | 18.50 | -0.0050% | — | sem_zona |
| 2026-11-16 06:06 | SOL-USDT-SWAP | 70.81 | 71.35/70.63 | 71.34 | sup 71.10 (ha 7 candles) | 0.90000 | 0.0023% | A/venda@71.10 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-16 06:06 | XRP-USDT-SWAP | 0.95160 | 0.95940/0.95050 | 0.95930 | sup 0.95510 (ha 8 candles) | 0.01092 | -0.0067% | — | sem_zona |
| 2026-11-16 06:06 | DOGE-USDT-SWAP | 0.05857 | 0.05897/0.05839 | 0.05897 | sup 0.05844 (ha 7 candles) | 0.00069 | 0.0002% | — | sem_zona |
| 2026-11-16 06:06 | ARB-USDT-SWAP | 0.13311 | 0.13399/0.13197 | 0.13310 | sup 0.13295 (ha 8 candles) | 0.00163 | 0.0016% | — | zona_expirada_setup_A |
| 2026-11-16 06:06 | WLD-USDT-SWAP | 0.26310 | 0.26570/0.26230 | 0.26560 | sup 0.26240 (ha 7 candles) | 0.00404 | -0.0188% | — | sem_zona |
| 2026-11-16 06:06 | SUI-USDT-SWAP | 0.71790 | 0.72360/0.71580 | 0.72350 | sup 0.71870 (ha 7 candles) | 0.00941 | -0.0086% | A/venda@0.71870 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-16 06:06 | UNI-USDT-SWAP | 5.1360 | 5.1920/5.1250 | 5.1890 | sup 5.0810 (ha 7 candles) | 0.07436 | 0.0002% | — | sem_zona |
| 2026-11-16 06:06 | LINK-USDT-SWAP | 9.0830 | 9.1610/9.0760 | 9.1610 | sup 9.1040 (ha 7 candles) | 0.10386 | -0.0040% | A/venda@9.1040 (0t/0c) | zona_mapeada_setup_A |
