# Log de Monitoramento Automatico -- Multi-Par (script gratuito, GitHub Actions)

> Gerado por script Python sem LLM (ver monitor/fetch_and_check.py). Fonte: OKX. Cobre os pares em PAIRS (configuracao no topo do script) -- BTC-USDT-SWAP e os demais adicionados na expansao de 07/09/2026. Leitura e MECANICA (regras objetivas da secao 4 do plano), sem a prosa qualitativa que o Claude gerava -- cole este log numa conversa do Claude se quiser a leitura interpretativa.

| Data/Hora (BRT) | Par | Close 1h | High/Low 1h | Close 4h | Swing 1h ref | ATR 1h | Funding | Zona ativa | Status checklist |
|---|---|---|---|---|---|---|---|---|---|
| 2026-11-19 16:06 | BTC-USDT-SWAP | 62859.9 | 63281.4/62634.7 | 63075.1 | sup 62354.2 (ha 15 candles) | 527.64 | 0.0069% | — | sem_zona |
| 2026-11-19 16:06 | ETH-USDT-SWAP | 1776.8 | 1791.0/1767.7 | 1781.0 | sup 1763.0 (ha 15 candles) | 18.64 | 0.0009% | — | sem_zona |
| 2026-11-19 16:06 | SOL-USDT-SWAP | 74.03 | 74.65/73.67 | 73.51 | res 75.62 (ha 4 candles) | 0.84643 | 0.0011% | — | sem_zona |
| 2026-11-19 16:06 | XRP-USDT-SWAP | 0.97330 | 0.98020/0.96710 | 0.96890 | res 0.99730 (ha 4 candles) | 0.01156 | 0.0005% | — | sem_zona |
| 2026-11-19 16:06 | DOGE-USDT-SWAP | 0.05883 | 0.05911/0.05840 | 0.05850 | res 0.05984 (ha 7 candles) | 0.00057 | -0.0078% | — | sem_zona |
| 2026-11-19 16:06 | ARB-USDT-SWAP | 0.12475 | 0.12569/0.12284 | 0.12370 | sup 0.12530 (ha 15 candles) | 0.00168 | 0.0011% | A/venda@0.12530 (1t/0c) | zona_mapeada_setup_A |
| 2026-11-19 16:06 | WLD-USDT-SWAP | 0.26120 | 0.26380/0.25870 | 0.25860 | — | 0.00395 | -0.0296% | — | zona_expirada_setup_B |
| 2026-11-19 16:06 | SUI-USDT-SWAP | 0.71710 | 0.72280/0.71180 | 0.71370 | — | 0.00806 | -0.0002% | B/compra@0.70750 (1t/1c) | zona_mapeada_setup_B |
| 2026-11-19 16:06 | UNI-USDT-SWAP | 5.0040 | 5.0210/4.9200 | 4.9430 | — | 0.07171 | 0.0031% | B/compra@5.0280 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-19 16:06 | LINK-USDT-SWAP | 9.0620 | 9.1320/8.9960 | 9.0180 | — | 0.09671 | 0.0050% | — | zona_expirada_setup_B |
| 2026-11-19 17:06 | BTC-USDT-SWAP | 62341.0 | 62892.0/62266.0 | 62341.0 | sup 62354.2 (ha 16 candles) | 550.35 | 0.0078% | A/venda@62354.2 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-19 17:06 | ETH-USDT-SWAP | 1770.0 | 1782.3/1767.5 | 1770.0 | sup 1763.0 (ha 16 candles) | 19.26 | 0.0022% | — | sem_zona |
| 2026-11-19 17:06 | SOL-USDT-SWAP | 73.54 | 74.04/73.46 | 73.54 | res 75.62 (ha 5 candles) | 0.86857 | 0.0013% | — | sem_zona |
| 2026-11-19 17:06 | XRP-USDT-SWAP | 0.96660 | 0.97360/0.96470 | 0.96660 | res 0.99730 (ha 5 candles) | 0.01186 | 0.0016% | — | sem_zona |
| 2026-11-19 17:06 | DOGE-USDT-SWAP | 0.05860 | 0.05890/0.05855 | 0.05860 | res 0.05984 (ha 8 candles) | 0.00058 | -0.0063% | — | sem_zona |
| 2026-11-19 17:06 | ARB-USDT-SWAP | 0.12419 | 0.12486/0.12379 | 0.12419 | sup 0.12530 (ha 16 candles) | 0.00169 | 0.0012% | A/venda@0.12530 (1t/1c) | zona_mapeada_setup_A |
| 2026-11-19 17:06 | WLD-USDT-SWAP | 0.26000 | 0.26210/0.25980 | 0.26000 | — | 0.00397 | -0.0258% | — | sem_zona |
| 2026-11-19 17:06 | SUI-USDT-SWAP | 0.71500 | 0.71890/0.71380 | 0.71500 | — | 0.00816 | 0.0003% | B/compra@0.70750 (1t/2c) | zona_mapeada_setup_B |
| 2026-11-19 17:06 | UNI-USDT-SWAP | 5.0250 | 5.0600/4.9870 | 5.0250 | sup 4.8970 (ha 4 candles) | 0.07436 | 0.0087% | B/compra@5.0280 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-19 17:06 | LINK-USDT-SWAP | 9.0290 | 9.0820/9.0230 | 9.0290 | — | 0.09779 | 0.0050% | — | sem_zona |
| 2026-11-19 18:06 | BTC-USDT-SWAP | 62097.7 | 62437.7/61712.0 | 62341.0 | sup 62354.2 (ha 17 candles) | 572.59 | 0.0057% | A/venda@62354.2 (1t/0c) | zona_mapeada_setup_A |
| 2026-11-19 18:06 | ETH-USDT-SWAP | 1760.2 | 1770.0/1751.0 | 1770.0 | sup 1748.9 (ha 3 candles) | 19.88 | 0.0030% | — | sem_zona |
| 2026-11-19 18:06 | SOL-USDT-SWAP | 73.03 | 73.55/72.54 | 73.54 | res 75.62 (ha 6 candles) | 0.90286 | -0.0004% | — | sem_zona |
| 2026-11-19 18:06 | XRP-USDT-SWAP | 0.96170 | 0.96770/0.95590 | 0.96660 | res 0.99730 (ha 6 candles) | 0.01194 | -0.0012% | — | sem_zona |
| 2026-11-19 18:06 | DOGE-USDT-SWAP | 0.05817 | 0.05863/0.05794 | 0.05860 | res 0.05984 (ha 9 candles) | 0.00060 | -0.0067% | B/compra@0.05794 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-19 18:06 | ARB-USDT-SWAP | 0.12289 | 0.12418/0.12227 | 0.12419 | sup 0.12164 (ha 3 candles) | 0.00173 | 0.0033% | A/venda@0.12530 (1t/2c) | zona_mapeada_setup_A |
| 2026-11-19 18:06 | WLD-USDT-SWAP | 0.25750 | 0.26000/0.25600 | 0.26000 | — | 0.00409 | -0.0255% | B/compra@0.25590 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-19 18:06 | SUI-USDT-SWAP | 0.70810 | 0.71540/0.70510 | 0.71500 | — | 0.00854 | -0.0010% | B/compra@0.70750 (2t/0c) | zona_mapeada_setup_B |
| 2026-11-19 18:06 | UNI-USDT-SWAP | 4.9720 | 5.0250/4.9370 | 5.0250 | sup 4.8970 (ha 5 candles) | 0.07743 | 0.0100% | — | invalidado_setup_B |
| 2026-11-19 18:06 | LINK-USDT-SWAP | 8.9650 | 9.0450/8.9280 | 9.0290 | — | 0.10179 | 0.0029% | B/compra@8.9300 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-19 19:06 | BTC-USDT-SWAP | 61514.3 | 62141.6/61388.0 | 62341.0 | sup 62354.2 (ha 18 candles) | 601.70 | 0.0034% | A/venda@62354.2 (1t/1c) | zona_mapeada_setup_A |
| 2026-11-19 19:06 | ETH-USDT-SWAP | 1740.8 | 1761.3/1735.1 | 1770.0 | sup 1748.9 (ha 4 candles) | 21.01 | 0.0031% | A/venda@1748.9 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-19 19:06 | SOL-USDT-SWAP | 72.19 | 73.05/72.05 | 73.54 | res 75.62 (ha 7 candles) | 0.92786 | -0.0020% | — | sem_zona |
| 2026-11-19 19:06 | XRP-USDT-SWAP | 0.95310 | 0.96220/0.95220 | 0.96660 | res 0.99730 (ha 7 candles) | 0.01216 | -0.0029% | B/compra@0.94500 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-19 19:06 | DOGE-USDT-SWAP | 0.05751 | 0.05824/0.05742 | 0.05860 | res 0.05984 (ha 10 candles) | 0.00064 | -0.0063% | — | invalidado_setup_B |
| 2026-11-19 19:06 | ARB-USDT-SWAP | 0.12182 | 0.12299/0.12178 | 0.12419 | sup 0.12164 (ha 4 candles) | 0.00174 | 0.0048% | A/venda@0.12530 (1t/3c) | zona_mapeada_setup_A |
| 2026-11-19 19:06 | WLD-USDT-SWAP | 0.25140 | 0.25780/0.25030 | 0.26000 | — | 0.00446 | -0.0250% | — | invalidado_setup_B |
| 2026-11-19 19:06 | SUI-USDT-SWAP | 0.69970 | 0.70890/0.69870 | 0.71500 | — | 0.00893 | -0.0014% | — | invalidado_setup_B |
| 2026-11-19 19:06 | UNI-USDT-SWAP | 4.9140 | 4.9840/4.9110 | 5.0250 | sup 4.8970 (ha 6 candles) | 0.07957 | 0.0100% | — | sem_zona |
| 2026-11-19 19:06 | LINK-USDT-SWAP | 8.8740 | 8.9710/8.8380 | 9.0290 | — | 0.10807 | 0.0013% | — | invalidado_setup_B |
| 2026-11-19 20:06 | BTC-USDT-SWAP | 62134.6 | 62317.1/61488.6 | 62341.0 | sup 62354.2 (ha 19 candles) | 640.23 | -0.0001% | A/venda@62354.2 (2t/0c) | zona_mapeada_setup_A |
| 2026-11-19 20:06 | ETH-USDT-SWAP | 1759.7 | 1765.8/1737.7 | 1770.0 | sup 1748.9 (ha 5 candles) | 22.29 | 0.0032% | — | invalidado_setup_A |
| 2026-11-19 20:06 | SOL-USDT-SWAP | 73.22 | 73.27/72.16 | 73.54 | res 75.62 (ha 8 candles) | 0.96286 | -0.0031% | — | sem_zona |
| 2026-11-19 20:06 | XRP-USDT-SWAP | 0.96120 | 0.96420/0.95200 | 0.96660 | res 0.99730 (ha 8 candles) | 0.01266 | -0.0036% | B/compra@0.94500 (0t/1c) | zona_mapeada_setup_B |
| 2026-11-19 20:06 | DOGE-USDT-SWAP | 0.05820 | 0.05832/0.05743 | 0.05860 | res 0.05984 (ha 11 candles) | 0.00068 | -0.0063% | — | sem_zona |
| 2026-11-19 20:06 | ARB-USDT-SWAP | 0.12237 | 0.12287/0.12124 | 0.12419 | sup 0.12164 (ha 5 candles) | 0.00180 | 0.0045% | A/venda@0.12530 (1t/4c) | zona_mapeada_setup_A |
| 2026-11-19 20:06 | WLD-USDT-SWAP | 0.25420 | 0.25550/0.24990 | 0.26000 | — | 0.00466 | -0.0235% | — | sem_zona |
| 2026-11-19 20:06 | SUI-USDT-SWAP | 0.70770 | 0.70990/0.69950 | 0.71500 | — | 0.00929 | 0.0007% | — | sem_zona |
| 2026-11-19 20:06 | UNI-USDT-SWAP | 4.9450 | 4.9620/4.8960 | 5.0250 | sup 4.8970 (ha 7 candles) | 0.08129 | 0.0100% | — | sem_zona |
| 2026-11-19 20:06 | LINK-USDT-SWAP | 8.9820 | 9.0100/8.8680 | 9.0290 | — | 0.11486 | -0.0003% | B/compra@9.0030 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-19 21:06 | BTC-USDT-SWAP | 61949.1 | 62202.0/61741.9 | 61949.1 | sup 62354.2 (ha 20 candles) | 654.34 | -0.0018% | A/venda@62354.2 (2t/1c) | zona_mapeada_setup_A |
| 2026-11-19 21:06 | ETH-USDT-SWAP | 1756.9 | 1761.2/1747.2 | 1756.9 | sup 1748.9 (ha 6 candles) | 22.52 | 0.0038% | — | sem_zona |
| 2026-11-19 21:06 | SOL-USDT-SWAP | 73.11 | 73.41/72.82 | 73.11 | res 75.62 (ha 9 candles) | 0.96643 | -0.0025% | — | sem_zona |
| 2026-11-19 21:06 | XRP-USDT-SWAP | 0.95980 | 0.96350/0.95810 | 0.95980 | res 0.99730 (ha 9 candles) | 0.01260 | -0.0032% | B/compra@0.94500 (0t/2c) | zona_mapeada_setup_B |
| 2026-11-19 21:06 | DOGE-USDT-SWAP | 0.05819 | 0.05832/0.05792 | 0.05819 | — | 0.00068 | -0.0045% | — | sem_zona |
| 2026-11-19 21:06 | ARB-USDT-SWAP | 0.12230 | 0.12274/0.12156 | 0.12230 | sup 0.12164 (ha 6 candles) | 0.00181 | 0.0053% | A/venda@0.12530 (1t/5c) | zona_mapeada_setup_A |
| 2026-11-19 21:06 | WLD-USDT-SWAP | 0.25290 | 0.25490/0.25220 | 0.25290 | — | 0.00473 | -0.0196% | — | sem_zona |
| 2026-11-19 21:06 | SUI-USDT-SWAP | 0.71010 | 0.71080/0.70440 | 0.71010 | sup 0.70460 (ha 6 candles) | 0.00938 | 0.0010% | — | sem_zona |
| 2026-11-19 21:06 | UNI-USDT-SWAP | 4.9310 | 4.9580/4.8950 | 4.9310 | sup 4.8970 (ha 8 candles) | 0.08300 | 0.0100% | — | sem_zona |
| 2026-11-19 21:06 | LINK-USDT-SWAP | 9.0010 | 9.0080/8.9450 | 9.0010 | — | 0.11457 | -0.0006% | — | descartado_rr_baixo_setup_B |
| 2026-11-19 22:06 | BTC-USDT-SWAP | 62120.0 | 62228.3/61920.7 | 61949.1 | sup 61388.0 (ha 3 candles) | 662.57 | -0.0020% | — | zona_expirada_setup_A |
| 2026-11-19 22:06 | ETH-USDT-SWAP | 1756.9 | 1763.2/1750.0 | 1756.9 | sup 1735.1 (ha 3 candles) | 22.62 | 0.0049% | — | sem_zona |
| 2026-11-19 22:06 | SOL-USDT-SWAP | 73.00 | 73.33/72.68 | 73.11 | res 75.62 (ha 10 candles) | 0.98429 | -0.0020% | — | sem_zona |
| 2026-11-19 22:06 | XRP-USDT-SWAP | 0.96170 | 0.96500/0.95760 | 0.95980 | res 0.99730 (ha 10 candles) | 0.01261 | -0.0035% | B/compra@0.94500 (0t/3c) | zona_mapeada_setup_B |
| 2026-11-19 22:06 | DOGE-USDT-SWAP | 0.05809 | 0.05837/0.05786 | 0.05819 | — | 0.00070 | -0.0029% | — | sem_zona |
| 2026-11-19 22:06 | ARB-USDT-SWAP | 0.12114 | 0.12258/0.12079 | 0.12230 | sup 0.12164 (ha 7 candles) | 0.00189 | 0.0062% | A/venda@0.12530 (1t/6c) | zona_mapeada_setup_A |
| 2026-11-19 22:06 | WLD-USDT-SWAP | 0.25070 | 0.25340/0.24940 | 0.25290 | — | 0.00489 | -0.0240% | — | sem_zona |
| 2026-11-19 22:06 | SUI-USDT-SWAP | 0.71080 | 0.71240/0.70780 | 0.71010 | sup 0.69870 (ha 3 candles) | 0.00946 | -0.0014% | — | sem_zona |
| 2026-11-19 22:06 | UNI-USDT-SWAP | 4.9270 | 4.9530/4.9080 | 4.9310 | sup 4.8970 (ha 9 candles) | 0.08350 | 0.0100% | — | sem_zona |
| 2026-11-19 22:06 | LINK-USDT-SWAP | 9.0160 | 9.0270/8.9710 | 9.0010 | — | 0.11500 | 0.0010% | B/compra@8.9300 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-19 23:06 | BTC-USDT-SWAP | 61547.2 | 62621.5/61256.6 | 61949.1 | sup 61388.0 (ha 4 candles) | 731.51 | -0.0002% | — | sem_zona |
| 2026-11-19 23:06 | ETH-USDT-SWAP | 1734.8 | 1769.9/1722.0 | 1756.9 | sup 1735.1 (ha 4 candles) | 25.17 | 0.0048% | A/venda@1735.1 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-19 23:06 | SOL-USDT-SWAP | 72.06 | 73.52/71.70 | 73.11 | res 75.62 (ha 11 candles) | 1.0643 | -0.0008% | — | sem_zona |
| 2026-11-19 23:06 | XRP-USDT-SWAP | 0.95290 | 0.96880/0.94910 | 0.95980 | res 0.99730 (ha 11 candles) | 0.01311 | -0.0033% | B/compra@0.94500 (0t/4c) | zona_mapeada_setup_B |
| 2026-11-19 23:06 | DOGE-USDT-SWAP | 0.05725 | 0.05846/0.05694 | 0.05819 | — | 0.00077 | -0.0012% | B/compra@0.05738 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-19 23:06 | ARB-USDT-SWAP | 0.11855 | 0.12186/0.11758 | 0.12230 | sup 0.12164 (ha 8 candles) | 0.00209 | 0.0067% | A/venda@0.12530 (1t/7c) | zona_mapeada_setup_A |
| 2026-11-19 23:06 | WLD-USDT-SWAP | 0.24410 | 0.25250/0.24110 | 0.25290 | — | 0.00537 | -0.0323% | B/compra@0.24230 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-19 23:06 | SUI-USDT-SWAP | 0.70140 | 0.71630/0.69540 | 0.71010 | sup 0.69870 (ha 4 candles) | 0.01044 | -0.0046% | — | sem_zona |
| 2026-11-19 23:06 | UNI-USDT-SWAP | 4.8360 | 4.9790/4.7890 | 4.9310 | sup 4.8970 (ha 10 candles) | 0.09350 | 0.0090% | A/venda@4.8970 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-19 23:06 | LINK-USDT-SWAP | 8.8600 | 9.0770/8.7880 | 9.0010 | — | 0.13143 | 0.0021% | — | invalidado_setup_B |
| 2026-11-20 00:06 | BTC-USDT-SWAP | 62245.6 | 62258.4/61258.0 | 61949.1 | sup 61388.0 (ha 5 candles) | 774.62 | 0.0009% | — | sem_zona |
| 2026-11-20 00:06 | ETH-USDT-SWAP | 1749.0 | 1749.4/1725.1 | 1756.9 | sup 1735.1 (ha 5 candles) | 25.84 | 0.0037% | — | invalidado_setup_A |
| 2026-11-20 00:06 | SOL-USDT-SWAP | 72.94 | 72.95/71.54 | 73.11 | res 75.62 (ha 12 candles) | 1.1050 | 0.0002% | — | sem_zona |
| 2026-11-20 00:06 | XRP-USDT-SWAP | 0.95930 | 0.95930/0.94700 | 0.95980 | res 0.99730 (ha 12 candles) | 0.01305 | -0.0044% | — | descartado_rr_baixo_setup_B |
| 2026-11-20 00:06 | DOGE-USDT-SWAP | 0.05771 | 0.05772/0.05674 | 0.05819 | — | 0.00079 | -0.0018% | — | descartado_rr_baixo_setup_B |
| 2026-11-20 00:06 | ARB-USDT-SWAP | 0.11916 | 0.11917/0.11743 | 0.12230 | sup 0.12164 (ha 9 candles) | 0.00207 | 0.0073% | — | zona_expirada_setup_A |
| 2026-11-20 00:06 | WLD-USDT-SWAP | 0.24640 | 0.24660/0.24240 | 0.25290 | — | 0.00529 | -0.0388% | — | confirmado_calibracao_setup_B |
| 2026-11-20 00:06 | SUI-USDT-SWAP | 0.70470 | 0.70480/0.69460 | 0.71010 | sup 0.69870 (ha 5 candles) | 0.01045 | -0.0102% | — | sem_zona |
| 2026-11-20 00:06 | UNI-USDT-SWAP | 4.8780 | 4.8790/4.8030 | 4.9310 | sup 4.8970 (ha 11 candles) | 0.09236 | 0.0100% | A/venda@4.8970 (1t/0c) | zona_mapeada_setup_A |
| 2026-11-20 00:06 | LINK-USDT-SWAP | 8.9200 | 8.9200/8.7800 | 9.0010 | — | 0.13364 | 0.0011% | B/compra@9.0030 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-20 01:06 | BTC-USDT-SWAP | 62123.7 | 62380.8/61780.0 | 62123.7 | sup 61388.0 (ha 6 candles) | 788.83 | 0.0008% | — | sem_zona |
| 2026-11-20 01:06 | ETH-USDT-SWAP | 1745.5 | 1755.4/1733.5 | 1745.5 | sup 1735.1 (ha 6 candles) | 26.39 | 0.0032% | — | sem_zona |
| 2026-11-20 01:06 | SOL-USDT-SWAP | 72.86 | 73.16/72.17 | 72.86 | — | 1.1293 | 0.0003% | B/venda@72.90 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-20 01:06 | XRP-USDT-SWAP | 0.96260 | 0.96540/0.94970 | 0.96260 | — | 0.01358 | -0.0043% | — | sem_zona |
| 2026-11-20 01:06 | DOGE-USDT-SWAP | 0.05743 | 0.05786/0.05704 | 0.05743 | — | 0.00083 | -0.0024% | B/compra@0.05794 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-20 01:06 | ARB-USDT-SWAP | 0.11774 | 0.11939/0.11719 | 0.11774 | sup 0.12164 (ha 10 candles) | 0.00215 | 0.0080% | A/venda@0.12164 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-20 01:06 | WLD-USDT-SWAP | 0.24430 | 0.24720/0.24280 | 0.24430 | sup 0.25510 (ha 10 candles) | 0.00541 | -0.0491% | A/venda@0.25510 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-20 01:06 | SUI-USDT-SWAP | 0.69900 | 0.70600/0.69530 | 0.69900 | sup 0.69870 (ha 6 candles) | 0.01094 | -0.0158% | — | sem_zona |
| 2026-11-20 01:06 | UNI-USDT-SWAP | 4.8060 | 4.8880/4.8060 | 4.8060 | sup 4.8970 (ha 12 candles) | 0.09643 | 0.0100% | — | confirmado_calibracao_setup_A |
| 2026-11-20 01:06 | LINK-USDT-SWAP | 8.8870 | 8.9460/8.8260 | 8.8870 | sup 8.8380 (ha 6 candles) | 0.13871 | 0.0016% | B/compra@9.0030 (0t/1c) | zona_mapeada_setup_B |
| 2026-11-20 02:06 | BTC-USDT-SWAP | 61484.5 | 62126.5/61350.0 | 62123.7 | sup 61256.6 (ha 3 candles) | 801.01 | 0.0004% | — | sem_zona |
| 2026-11-20 02:06 | ETH-USDT-SWAP | 1726.6 | 1745.8/1717.0 | 1745.5 | sup 1735.1 (ha 7 candles) | 26.81 | 0.0046% | — | sem_zona |
| 2026-11-20 02:06 | SOL-USDT-SWAP | 72.09 | 72.88/71.84 | 72.86 | — | 1.1400 | -0.0001% | — | descartado_rr_baixo_setup_B |
| 2026-11-20 02:06 | XRP-USDT-SWAP | 0.96040 | 0.96300/0.95460 | 0.96260 | — | 0.01329 | -0.0045% | — | sem_zona |
| 2026-11-20 02:06 | DOGE-USDT-SWAP | 0.05689 | 0.05746/0.05664 | 0.05743 | — | 0.00085 | -0.0019% | B/compra@0.05794 (0t/1c) | zona_mapeada_setup_B |
| 2026-11-20 02:06 | ARB-USDT-SWAP | 0.11677 | 0.11792/0.11628 | 0.11774 | sup 0.12164 (ha 11 candles) | 0.00212 | 0.0084% | A/venda@0.12164 (0t/1c) | zona_mapeada_setup_A |
| 2026-11-20 02:06 | WLD-USDT-SWAP | 0.24450 | 0.24550/0.24280 | 0.24430 | sup 0.24110 (ha 3 candles) | 0.00531 | -0.0523% | A/venda@0.25510 (0t/1c) | zona_mapeada_setup_A |
| 2026-11-20 02:06 | SUI-USDT-SWAP | 0.68970 | 0.69930/0.68860 | 0.69900 | sup 0.69870 (ha 7 candles) | 0.01105 | -0.0161% | A/venda@0.69870 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-20 02:06 | UNI-USDT-SWAP | 4.7530 | 4.8100/4.7260 | 4.8060 | sup 4.8970 (ha 13 candles) | 0.09286 | 0.0083% | — | sem_zona |
| 2026-11-20 02:06 | LINK-USDT-SWAP | 8.7700 | 8.8890/8.7510 | 8.8870 | sup 8.8380 (ha 7 candles) | 0.13986 | 0.0013% | B/compra@9.0030 (0t/2c) | zona_mapeada_setup_B |
| 2026-11-20 03:06 | BTC-USDT-SWAP | 61881.3 | 61994.4/61390.6 | 62123.7 | sup 61256.6 (ha 4 candles) | 763.04 | -0.0008% | — | sem_zona |
| 2026-11-20 03:06 | ETH-USDT-SWAP | 1740.6 | 1742.3/1719.0 | 1745.5 | sup 1735.1 (ha 8 candles) | 25.04 | 0.0035% | — | sem_zona |
| 2026-11-20 03:06 | SOL-USDT-SWAP | 72.67 | 72.89/71.83 | 72.86 | — | 1.0743 | -0.0006% | B/venda@73.23 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-20 03:06 | XRP-USDT-SWAP | 0.96970 | 0.97260/0.95870 | 0.96260 | — | 0.01219 | -0.0037% | B/venda@0.97650 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-20 03:06 | DOGE-USDT-SWAP | 0.05756 | 0.05767/0.05679 | 0.05743 | — | 0.00080 | -0.0038% | B/compra@0.05794 (0t/2c) | zona_mapeada_setup_B |
| 2026-11-20 03:06 | ARB-USDT-SWAP | 0.11786 | 0.11800/0.11622 | 0.11774 | sup 0.12164 (ha 12 candles) | 0.00198 | 0.0087% | A/venda@0.12164 (0t/2c) | zona_mapeada_setup_A |
| 2026-11-20 03:06 | WLD-USDT-SWAP | 0.24840 | 0.24890/0.24350 | 0.24430 | sup 0.24110 (ha 4 candles) | 0.00505 | -0.0543% | A/venda@0.25510 (0t/2c) | zona_mapeada_setup_A |
| 2026-11-20 03:06 | SUI-USDT-SWAP | 0.69800 | 0.70120/0.68680 | 0.69900 | sup 0.69870 (ha 8 candles) | 0.01066 | -0.0173% | A/venda@0.69870 (1t/0c) | zona_mapeada_setup_A |
| 2026-11-20 03:06 | UNI-USDT-SWAP | 4.8210 | 4.8310/4.7340 | 4.8060 | sup 4.8970 (ha 14 candles) | 0.08736 | 0.0062% | — | sem_zona |
| 2026-11-20 03:06 | LINK-USDT-SWAP | 8.8940 | 8.9020/8.7490 | 8.8870 | sup 8.8380 (ha 8 candles) | 0.13229 | 0.0004% | B/compra@9.0030 (0t/3c) | zona_mapeada_setup_B |
| 2026-11-20 04:06 | BTC-USDT-SWAP | 62023.5 | 62032.0/61670.8 | 62123.7 | sup 61256.6 (ha 5 candles) | 733.11 | -0.0019% | — | sem_zona |
| 2026-11-20 04:06 | ETH-USDT-SWAP | 1749.0 | 1750.0/1737.2 | 1745.5 | sup 1735.1 (ha 9 candles) | 24.05 | 0.0024% | — | sem_zona |
| 2026-11-20 04:06 | SOL-USDT-SWAP | 72.85 | 72.86/72.32 | 72.86 | — | 1.0357 | 0.0002% | B/venda@73.23 (0t/1c) | zona_mapeada_setup_B |
| 2026-11-20 04:06 | XRP-USDT-SWAP | 0.97140 | 0.97150/0.96210 | 0.96260 | — | 0.01191 | -0.0037% | B/venda@0.97650 (0t/1c) | zona_mapeada_setup_B |
| 2026-11-20 04:06 | DOGE-USDT-SWAP | 0.05769 | 0.05769/0.05734 | 0.05743 | — | 0.00077 | -0.0041% | B/compra@0.05794 (0t/3c) | zona_mapeada_setup_B |
| 2026-11-20 04:06 | ARB-USDT-SWAP | 0.11921 | 0.11950/0.11741 | 0.11774 | sup 0.12164 (ha 13 candles) | 0.00198 | 0.0090% | A/venda@0.12164 (0t/3c) | zona_mapeada_setup_A |
| 2026-11-20 04:06 | WLD-USDT-SWAP | 0.24730 | 0.24870/0.24420 | 0.24430 | sup 0.24110 (ha 5 candles) | 0.00508 | -0.0488% | A/venda@0.25510 (0t/3c) | zona_mapeada_setup_A |
| 2026-11-20 04:06 | SUI-USDT-SWAP | 0.70020 | 0.70030/0.69440 | 0.69900 | sup 0.69870 (ha 9 candles) | 0.01041 | -0.0147% | A/venda@0.69870 (2t/0c) | zona_mapeada_setup_A |
| 2026-11-20 04:06 | UNI-USDT-SWAP | 4.8450 | 4.8550/4.7840 | 4.8060 | sup 4.8970 (ha 15 candles) | 0.08607 | 0.0043% | — | sem_zona |
| 2026-11-20 04:06 | LINK-USDT-SWAP | 8.9000 | 8.9080/8.8500 | 8.8870 | sup 8.8380 (ha 9 candles) | 0.12821 | 0.0013% | B/compra@9.0030 (0t/4c) | zona_mapeada_setup_B |
| 2026-11-20 05:06 | BTC-USDT-SWAP | 61818.1 | 62023.5/61441.3 | 61818.1 | sup 61256.6 (ha 6 candles) | 688.43 | -0.0037% | — | sem_zona |
| 2026-11-20 05:06 | ETH-USDT-SWAP | 1752.0 | 1754.4/1738.2 | 1752.0 | sup 1717.0 (ha 3 candles) | 22.42 | 0.0014% | — | sem_zona |
| 2026-11-20 05:06 | SOL-USDT-SWAP | 72.62 | 72.86/72.19 | 72.62 | — | 0.96071 | -0.0000% | B/venda@73.23 (0t/2c) | zona_mapeada_setup_B |
| 2026-11-20 05:06 | XRP-USDT-SWAP | 0.96470 | 0.97210/0.95920 | 0.96470 | — | 0.01151 | -0.0031% | B/venda@0.97650 (0t/2c) | zona_mapeada_setup_B |
| 2026-11-20 05:06 | DOGE-USDT-SWAP | 0.05752 | 0.05768/0.05714 | 0.05752 | — | 0.00073 | -0.0029% | B/compra@0.05794 (0t/4c) | zona_mapeada_setup_B |
| 2026-11-20 05:06 | ARB-USDT-SWAP | 0.12062 | 0.12096/0.11854 | 0.12062 | sup 0.12164 (ha 14 candles) | 0.00199 | 0.0081% | A/venda@0.12164 (0t/4c) | zona_mapeada_setup_A |
| 2026-11-20 05:06 | WLD-USDT-SWAP | 0.24850 | 0.24950/0.24600 | 0.24850 | sup 0.24110 (ha 6 candles) | 0.00481 | -0.0465% | A/venda@0.25510 (0t/4c) | zona_mapeada_setup_A |
| 2026-11-20 05:06 | SUI-USDT-SWAP | 0.69820 | 0.70020/0.69350 | 0.69820 | sup 0.69870 (ha 10 candles) | 0.00982 | -0.0116% | — | zona_expirada_setup_A |
| 2026-11-20 05:06 | UNI-USDT-SWAP | 4.8680 | 4.8770/4.8170 | 4.8680 | sup 4.7260 (ha 3 candles) | 0.08350 | 0.0016% | — | sem_zona |
| 2026-11-20 05:06 | LINK-USDT-SWAP | 8.8740 | 8.9020/8.8120 | 8.8740 | sup 8.8380 (ha 10 candles) | 0.12100 | 0.0028% | B/compra@9.0030 (0t/5c) | zona_mapeada_setup_B |
| 2026-11-20 06:06 | BTC-USDT-SWAP | 61796.5 | 62029.9/61691.9 | 61818.1 | sup 61256.6 (ha 7 candles) | 666.38 | -0.0049% | — | sem_zona |
| 2026-11-20 06:06 | ETH-USDT-SWAP | 1750.6 | 1758.9/1747.0 | 1752.0 | sup 1717.0 (ha 4 candles) | 21.60 | 0.0012% | — | sem_zona |
| 2026-11-20 06:06 | SOL-USDT-SWAP | 72.49 | 72.81/72.46 | 72.62 | — | 0.91571 | 0.0013% | B/venda@73.23 (0t/3c) | zona_mapeada_setup_B |
| 2026-11-20 06:06 | XRP-USDT-SWAP | 0.95920 | 0.96790/0.95890 | 0.96470 | — | 0.01121 | -0.0027% | B/venda@0.97650 (0t/3c) | zona_mapeada_setup_B |
| 2026-11-20 06:06 | DOGE-USDT-SWAP | 0.05728 | 0.05772/0.05727 | 0.05752 | — | 0.00072 | -0.0018% | B/compra@0.05794 (0t/5c) | zona_mapeada_setup_B |
| 2026-11-20 06:06 | ARB-USDT-SWAP | 0.12032 | 0.12161/0.12018 | 0.12062 | sup 0.11622 (ha 3 candles) | 0.00188 | 0.0083% | — | confirmado_calibracao_setup_A |
| 2026-11-20 06:06 | WLD-USDT-SWAP | 0.24800 | 0.25010/0.24770 | 0.24850 | sup 0.24110 (ha 7 candles) | 0.00461 | -0.0449% | A/venda@0.25510 (0t/5c) | zona_mapeada_setup_A |
| 2026-11-20 06:06 | SUI-USDT-SWAP | 0.69530 | 0.70170/0.69510 | 0.69820 | sup 0.68680 (ha 3 candles) | 0.00951 | -0.0087% | — | sem_zona |
| 2026-11-20 06:06 | UNI-USDT-SWAP | 4.8390 | 4.8870/4.8380 | 4.8680 | sup 4.7260 (ha 4 candles) | 0.07979 | -0.0007% | — | sem_zona |
| 2026-11-20 06:06 | LINK-USDT-SWAP | 8.8600 | 8.9220/8.8590 | 8.8740 | sup 8.7490 (ha 3 candles) | 0.11579 | 0.0046% | B/compra@9.0030 (0t/6c) | zona_mapeada_setup_B |
| 2026-11-20 07:06 | BTC-USDT-SWAP | 61609.7 | 61840.6/61520.0 | 61818.1 | sup 61256.6 (ha 8 candles) | 644.56 | -0.0044% | — | sem_zona |
| 2026-11-20 07:06 | ETH-USDT-SWAP | 1745.3 | 1753.5/1742.2 | 1752.0 | sup 1717.0 (ha 5 candles) | 21.35 | 0.0017% | — | sem_zona |
| 2026-11-20 07:06 | SOL-USDT-SWAP | 71.97 | 72.52/71.95 | 72.62 | — | 0.91500 | 0.0011% | B/venda@73.23 (0t/4c) | zona_mapeada_setup_B |
| 2026-11-20 07:06 | XRP-USDT-SWAP | 0.95540 | 0.96160/0.95410 | 0.96470 | — | 0.01111 | -0.0030% | B/venda@0.97650 (0t/4c) | zona_mapeada_setup_B |
| 2026-11-20 07:06 | DOGE-USDT-SWAP | 0.05700 | 0.05730/0.05689 | 0.05752 | — | 0.00072 | 0.0013% | B/compra@0.05794 (0t/6c) | zona_mapeada_setup_B |
| 2026-11-20 07:06 | ARB-USDT-SWAP | 0.11962 | 0.12045/0.11947 | 0.12062 | sup 0.11622 (ha 4 candles) | 0.00188 | 0.0075% | — | sem_zona |
| 2026-11-20 07:06 | WLD-USDT-SWAP | 0.24760 | 0.24920/0.24730 | 0.24850 | sup 0.24110 (ha 8 candles) | 0.00459 | -0.0447% | A/venda@0.25510 (0t/6c) | zona_mapeada_setup_A |
| 2026-11-20 07:06 | SUI-USDT-SWAP | 0.69350 | 0.69590/0.69140 | 0.69820 | sup 0.68680 (ha 4 candles) | 0.00946 | -0.0091% | — | sem_zona |
| 2026-11-20 07:06 | UNI-USDT-SWAP | 4.8040 | 4.8400/4.8010 | 4.8680 | sup 4.7260 (ha 5 candles) | 0.07736 | -0.0009% | — | sem_zona |
| 2026-11-20 07:06 | LINK-USDT-SWAP | 8.8230 | 8.8660/8.8130 | 8.8740 | sup 8.7490 (ha 4 candles) | 0.11536 | 0.0041% | B/compra@9.0030 (0t/7c) | zona_mapeada_setup_B |
| 2026-11-20 08:06 | BTC-USDT-SWAP | 62017.5 | 62317.1/61600.0 | 61818.1 | sup 61256.6 (ha 9 candles) | 643.95 | -0.0024% | — | sem_zona |
| 2026-11-20 08:06 | ETH-USDT-SWAP | 1756.0 | 1762.6/1744.7 | 1752.0 | sup 1717.0 (ha 6 candles) | 21.27 | 0.0016% | — | sem_zona |
| 2026-11-20 08:06 | SOL-USDT-SWAP | 72.38 | 72.71/71.78 | 72.62 | — | 0.90929 | 0.0005% | B/venda@73.23 (0t/5c) | zona_mapeada_setup_B |
| 2026-11-20 08:06 | XRP-USDT-SWAP | 0.96220 | 0.96790/0.95520 | 0.96470 | — | 0.01118 | -0.0029% | B/venda@0.97650 (0t/5c) | zona_mapeada_setup_B |
| 2026-11-20 08:06 | DOGE-USDT-SWAP | 0.05726 | 0.05752/0.05691 | 0.05752 | — | 0.00071 | 0.0023% | B/compra@0.05794 (0t/7c) | zona_mapeada_setup_B |
| 2026-11-20 08:06 | ARB-USDT-SWAP | 0.11916 | 0.12011/0.11882 | 0.12062 | sup 0.11622 (ha 5 candles) | 0.00183 | 0.0064% | — | sem_zona |
| 2026-11-20 08:06 | WLD-USDT-SWAP | 0.24750 | 0.24880/0.24630 | 0.24850 | sup 0.24110 (ha 9 candles) | 0.00448 | -0.0403% | A/venda@0.25510 (0t/7c) | zona_mapeada_setup_A |
| 2026-11-20 08:06 | SUI-USDT-SWAP | 0.68890 | 0.69830/0.68770 | 0.69820 | sup 0.68680 (ha 5 candles) | 0.00949 | -0.0149% | — | sem_zona |
| 2026-11-20 08:06 | UNI-USDT-SWAP | 4.8220 | 4.8510/4.7760 | 4.8680 | sup 4.7260 (ha 6 candles) | 0.07643 | -0.0027% | — | sem_zona |
| 2026-11-20 08:06 | LINK-USDT-SWAP | 8.8750 | 8.9170/8.8180 | 8.8740 | sup 8.7490 (ha 5 candles) | 0.11407 | 0.0028% | — | zona_expirada_setup_B |
| 2026-11-20 09:06 | BTC-USDT-SWAP | 61782.1 | 62063.7/61676.2 | 61782.1 | sup 61256.6 (ha 10 candles) | 617.80 | -0.0013% | — | sem_zona |
| 2026-11-20 09:06 | ETH-USDT-SWAP | 1748.1 | 1757.9/1745.7 | 1748.1 | sup 1717.0 (ha 7 candles) | 20.27 | 0.0015% | — | sem_zona |
| 2026-11-20 09:06 | SOL-USDT-SWAP | 71.73 | 72.46/71.59 | 71.73 | — | 0.90000 | -0.0009% | B/venda@73.23 (0t/6c) | zona_mapeada_setup_B |
| 2026-11-20 09:06 | XRP-USDT-SWAP | 0.95180 | 0.96340/0.95080 | 0.95180 | — | 0.01136 | -0.0044% | B/venda@0.97650 (0t/6c) | zona_mapeada_setup_B |
| 2026-11-20 09:06 | DOGE-USDT-SWAP | 0.05685 | 0.05732/0.05678 | 0.05685 | — | 0.00069 | 0.0034% | — | zona_expirada_setup_B |
| 2026-11-20 09:06 | ARB-USDT-SWAP | 0.11839 | 0.11936/0.11814 | 0.11839 | sup 0.11622 (ha 6 candles) | 0.00183 | 0.0086% | — | sem_zona |
| 2026-11-20 09:06 | WLD-USDT-SWAP | 0.24650 | 0.24850/0.24590 | 0.24650 | sup 0.24110 (ha 10 candles) | 0.00413 | -0.0380% | — | zona_expirada_setup_A |
| 2026-11-20 09:06 | SUI-USDT-SWAP | 0.68600 | 0.69050/0.68330 | 0.68600 | sup 0.68680 (ha 6 candles) | 0.00927 | -0.0177% | A/venda@0.68680 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-20 09:06 | UNI-USDT-SWAP | 4.7950 | 4.8350/4.7800 | 4.7950 | sup 4.7260 (ha 7 candles) | 0.07514 | -0.0015% | — | sem_zona |
| 2026-11-20 09:06 | LINK-USDT-SWAP | 8.7790 | 8.8870/8.7760 | 8.7790 | sup 8.7490 (ha 6 candles) | 0.11250 | 0.0006% | — | sem_zona |
| 2026-11-20 10:06 | BTC-USDT-SWAP | 61536.7 | 61824.3/61175.0 | 61782.1 | sup 61256.6 (ha 11 candles) | 605.00 | 0.0001% | — | sem_zona |
| 2026-11-20 10:06 | ETH-USDT-SWAP | 1738.6 | 1749.7/1726.4 | 1748.1 | sup 1717.0 (ha 8 candles) | 19.93 | 0.0017% | — | sem_zona |
| 2026-11-20 10:06 | SOL-USDT-SWAP | 71.06 | 71.77/70.80 | 71.73 | — | 0.89000 | -0.0035% | B/venda@73.23 (0t/7c) | zona_mapeada_setup_B |
| 2026-11-20 10:06 | XRP-USDT-SWAP | 0.94460 | 0.95280/0.94250 | 0.95180 | — | 0.01123 | -0.0064% | B/venda@0.97650 (0t/7c) | zona_mapeada_setup_B |
| 2026-11-20 10:06 | DOGE-USDT-SWAP | 0.05652 | 0.05692/0.05621 | 0.05685 | — | 0.00068 | 0.0008% | — | sem_zona |
| 2026-11-20 10:06 | ARB-USDT-SWAP | 0.11740 | 0.11849/0.11714 | 0.11839 | sup 0.11622 (ha 7 candles) | 0.00181 | 0.0077% | — | sem_zona |
| 2026-11-20 10:06 | WLD-USDT-SWAP | 0.24270 | 0.24660/0.24260 | 0.24650 | sup 0.24110 (ha 11 candles) | 0.00401 | -0.0394% | — | sem_zona |
| 2026-11-20 10:06 | SUI-USDT-SWAP | 0.68340 | 0.68640/0.67750 | 0.68600 | sup 0.68680 (ha 7 candles) | 0.00916 | -0.0182% | A/venda@0.68680 (1t/0c) | zona_mapeada_setup_A |
| 2026-11-20 10:06 | UNI-USDT-SWAP | 4.7330 | 4.8030/4.7330 | 4.7950 | sup 4.7260 (ha 8 candles) | 0.07543 | -0.0033% | — | sem_zona |
| 2026-11-20 10:06 | LINK-USDT-SWAP | 8.7590 | 8.7980/8.6890 | 8.7790 | sup 8.7490 (ha 7 candles) | 0.11014 | -0.0040% | — | sem_zona |
| 2026-11-20 11:06 | BTC-USDT-SWAP | 61856.8 | 61978.2/61295.2 | 61782.1 | sup 61256.6 (ha 12 candles) | 620.92 | 0.0035% | — | sem_zona |
| 2026-11-20 11:06 | ETH-USDT-SWAP | 1753.8 | 1757.0/1727.2 | 1748.1 | sup 1717.0 (ha 9 candles) | 21.05 | 0.0031% | — | sem_zona |
| 2026-11-20 11:06 | SOL-USDT-SWAP | 71.31 | 71.45/70.50 | 71.73 | — | 0.91571 | -0.0047% | — | zona_expirada_setup_B |
| 2026-11-20 11:06 | XRP-USDT-SWAP | 0.94720 | 0.94940/0.93250 | 0.95180 | — | 0.01205 | -0.0056% | — | zona_expirada_setup_B |
| 2026-11-20 11:06 | DOGE-USDT-SWAP | 0.05654 | 0.05674/0.05583 | 0.05685 | — | 0.00072 | -0.0014% | — | sem_zona |
| 2026-11-20 11:06 | ARB-USDT-SWAP | 0.11799 | 0.11804/0.11679 | 0.11839 | sup 0.11622 (ha 8 candles) | 0.00182 | 0.0053% | — | sem_zona |
| 2026-11-20 11:06 | WLD-USDT-SWAP | 0.24140 | 0.24320/0.23830 | 0.24650 | sup 0.24110 (ha 12 candles) | 0.00417 | -0.0365% | — | sem_zona |
| 2026-11-20 11:06 | SUI-USDT-SWAP | 0.68210 | 0.68490/0.67220 | 0.68600 | sup 0.68680 (ha 8 candles) | 0.00961 | -0.0187% | A/venda@0.68680 (2t/0c) | zona_mapeada_setup_A |
| 2026-11-20 11:06 | UNI-USDT-SWAP | 4.7370 | 4.7530/4.6600 | 4.7950 | sup 4.7260 (ha 9 candles) | 0.07757 | -0.0062% | — | sem_zona |
| 2026-11-20 11:06 | LINK-USDT-SWAP | 8.7820 | 8.7980/8.6680 | 8.7790 | sup 8.7490 (ha 8 candles) | 0.11493 | -0.0060% | — | sem_zona |
| 2026-11-20 12:06 | BTC-USDT-SWAP | 61740.8 | 62155.0/61317.1 | 61782.1 | sup 61256.6 (ha 13 candles) | 658.80 | 0.0053% | — | sem_zona |
| 2026-11-20 12:06 | ETH-USDT-SWAP | 1742.5 | 1758.9/1723.3 | 1748.1 | sup 1717.0 (ha 10 candles) | 22.64 | 0.0028% | — | sem_zona |
| 2026-11-20 12:06 | SOL-USDT-SWAP | 71.02 | 71.69/70.41 | 71.73 | — | 0.96071 | -0.0055% | B/compra@71.00 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-20 12:06 | XRP-USDT-SWAP | 0.94370 | 0.95280/0.93610 | 0.95180 | — | 0.01271 | -0.0046% | B/compra@0.94500 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-20 12:06 | DOGE-USDT-SWAP | 0.05633 | 0.05689/0.05584 | 0.05685 | — | 0.00076 | -0.0030% | — | sem_zona |
| 2026-11-20 12:06 | ARB-USDT-SWAP | 0.11831 | 0.11876/0.11745 | 0.11839 | sup 0.11622 (ha 9 candles) | 0.00178 | 0.0038% | — | sem_zona |
| 2026-11-20 12:06 | WLD-USDT-SWAP | 0.24380 | 0.24450/0.23950 | 0.24650 | sup 0.24110 (ha 13 candles) | 0.00424 | -0.0356% | — | sem_zona |
| 2026-11-20 12:06 | SUI-USDT-SWAP | 0.68230 | 0.68720/0.67550 | 0.68600 | sup 0.68680 (ha 9 candles) | 0.01012 | -0.0192% | — | zona_expirada_setup_A |
| 2026-11-20 12:06 | UNI-USDT-SWAP | 4.7310 | 4.7600/4.6810 | 4.7950 | sup 4.7260 (ha 10 candles) | 0.08000 | -0.0113% | — | sem_zona |
| 2026-11-20 12:06 | LINK-USDT-SWAP | 8.7600 | 8.8400/8.6780 | 8.7790 | sup 8.7490 (ha 9 candles) | 0.12250 | -0.0051% | — | sem_zona |
| 2026-11-20 13:06 | BTC-USDT-SWAP | 59444.4 | 61928.5/59360.0 | 59444.4 | sup 61256.6 (ha 14 candles) | 744.77 | 0.0034% | A/venda@61256.6 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-20 13:06 | ETH-USDT-SWAP | 1654.4 | 1748.0/1648.0 | 1654.4 | sup 1717.0 (ha 11 candles) | 26.36 | -0.0008% | A/venda@1717.0 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-20 13:06 | SOL-USDT-SWAP | 68.31 | 71.15/67.84 | 68.31 | — | 1.0671 | -0.0083% | — | invalidado_setup_B |
| 2026-11-20 13:06 | XRP-USDT-SWAP | 0.91000 | 0.94680/0.90340 | 0.91000 | — | 0.01441 | -0.0048% | — | invalidado_setup_B |
| 2026-11-20 13:06 | DOGE-USDT-SWAP | 0.05381 | 0.05650/0.05346 | 0.05381 | — | 0.00087 | -0.0045% | — | sem_zona |
| 2026-11-20 13:06 | ARB-USDT-SWAP | 0.11384 | 0.11871/0.11289 | 0.11384 | sup 0.11622 (ha 10 candles) | 0.00189 | 0.0064% | A/venda@0.11622 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-20 13:06 | WLD-USDT-SWAP | 0.23290 | 0.24450/0.22990 | 0.23290 | sup 0.24110 (ha 14 candles) | 0.00447 | -0.0313% | A/venda@0.24110 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-20 13:06 | SUI-USDT-SWAP | 0.65220 | 0.68440/0.64840 | 0.65220 | sup 0.68680 (ha 10 candles) | 0.01120 | -0.0196% | — | sem_zona |
| 2026-11-20 13:06 | UNI-USDT-SWAP | 4.4740 | 4.7430/4.3970 | 4.4740 | sup 4.7260 (ha 11 candles) | 0.09114 | -0.0101% | A/venda@4.7260 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-20 13:06 | LINK-USDT-SWAP | 8.3370 | 8.7850/8.3010 | 8.3370 | sup 8.7490 (ha 10 candles) | 0.13643 | -0.0055% | A/venda@8.7490 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-20 14:06 | BTC-USDT-SWAP | 59515.1 | 59796.3/58726.0 | 59444.4 | sup 61256.6 (ha 15 candles) | 749.76 | 0.0017% | A/venda@61256.6 (0t/1c) | zona_mapeada_setup_A |
| 2026-11-20 14:06 | ETH-USDT-SWAP | 1644.4 | 1659.7/1623.0 | 1654.4 | sup 1717.0 (ha 12 candles) | 27.25 | -0.0050% | A/venda@1717.0 (0t/1c) | zona_mapeada_setup_A |
| 2026-11-20 14:06 | SOL-USDT-SWAP | 69.44 | 69.52/67.73 | 68.31 | — | 1.0943 | -0.0128% | B/compra@69.87 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-20 14:06 | XRP-USDT-SWAP | 0.91070 | 0.92100/0.90220 | 0.91000 | — | 0.01487 | -0.0060% | — | sem_zona |
| 2026-11-20 14:06 | DOGE-USDT-SWAP | 0.05401 | 0.05430/0.05314 | 0.05381 | — | 0.00088 | -0.0069% | — | sem_zona |
| 2026-11-20 14:06 | ARB-USDT-SWAP | 0.11401 | 0.11563/0.11274 | 0.11384 | sup 0.11622 (ha 11 candles) | 0.00198 | 0.0055% | A/venda@0.11622 (0t/1c) | zona_mapeada_setup_A |
| 2026-11-20 14:06 | WLD-USDT-SWAP | 0.23200 | 0.23540/0.22980 | 0.23290 | sup 0.24110 (ha 15 candles) | 0.00457 | -0.0322% | A/venda@0.24110 (0t/1c) | zona_mapeada_setup_A |
| 2026-11-20 14:06 | SUI-USDT-SWAP | 0.65460 | 0.66080/0.64340 | 0.65220 | sup 0.68680 (ha 11 candles) | 0.01171 | -0.0243% | — | sem_zona |
| 2026-11-20 14:06 | UNI-USDT-SWAP | 4.4370 | 4.5410/4.4340 | 4.4740 | sup 4.7260 (ha 12 candles) | 0.09336 | -0.0091% | A/venda@4.7260 (0t/1c) | zona_mapeada_setup_A |
| 2026-11-20 14:06 | LINK-USDT-SWAP | 8.3990 | 8.4480/8.2380 | 8.3370 | sup 8.7490 (ha 11 candles) | 0.14143 | -0.0081% | A/venda@8.7490 (0t/1c) | zona_mapeada_setup_A |
| 2026-11-20 15:06 | BTC-USDT-SWAP | 59141.7 | 59568.0/58866.1 | 59444.4 | sup 61256.6 (ha 16 candles) | 756.99 | 0.0025% | A/venda@61256.6 (0t/2c) | zona_mapeada_setup_A |
| 2026-11-20 15:06 | ETH-USDT-SWAP | 1630.2 | 1644.4/1617.2 | 1654.4 | sup 1717.0 (ha 13 candles) | 27.63 | -0.0084% | A/venda@1717.0 (0t/2c) | zona_mapeada_setup_A |
| 2026-11-20 15:06 | SOL-USDT-SWAP | 69.22 | 69.45/68.68 | 68.31 | — | 1.0786 | -0.0166% | B/compra@69.87 (0t/1c) | zona_mapeada_setup_B |
| 2026-11-20 15:06 | XRP-USDT-SWAP | 0.90710 | 0.91070/0.89940 | 0.91000 | — | 0.01456 | -0.0058% | — | sem_zona |
| 2026-11-20 15:06 | DOGE-USDT-SWAP | 0.05383 | 0.05403/0.05336 | 0.05381 | — | 0.00087 | -0.0076% | — | sem_zona |
| 2026-11-20 15:06 | ARB-USDT-SWAP | 0.11347 | 0.11404/0.11248 | 0.11384 | sup 0.11622 (ha 12 candles) | 0.00193 | 0.0095% | A/venda@0.11622 (0t/2c) | zona_mapeada_setup_A |
| 2026-11-20 15:06 | WLD-USDT-SWAP | 0.23200 | 0.23220/0.22780 | 0.23290 | sup 0.24110 (ha 16 candles) | 0.00457 | -0.0348% | A/venda@0.24110 (0t/2c) | zona_mapeada_setup_A |
| 2026-11-20 15:06 | SUI-USDT-SWAP | 0.65250 | 0.65500/0.64610 | 0.65220 | sup 0.68680 (ha 12 candles) | 0.01159 | -0.0248% | — | sem_zona |
| 2026-11-20 15:06 | UNI-USDT-SWAP | 4.4510 | 4.4680/4.3940 | 4.4740 | sup 4.7260 (ha 13 candles) | 0.09279 | -0.0055% | A/venda@4.7260 (0t/2c) | zona_mapeada_setup_A |
| 2026-11-20 15:06 | LINK-USDT-SWAP | 8.3790 | 8.3990/8.3090 | 8.3370 | sup 8.7490 (ha 12 candles) | 0.13929 | -0.0071% | A/venda@8.7490 (0t/2c) | zona_mapeada_setup_A |
| 2026-11-20 16:06 | BTC-USDT-SWAP | 58371.7 | 59286.9/57900.0 | 59444.4 | sup 61256.6 (ha 17 candles) | 800.59 | 0.0023% | A/venda@61256.6 (0t/3c) | zona_mapeada_setup_A |
| 2026-11-20 16:06 | ETH-USDT-SWAP | 1615.5 | 1642.7/1608.4 | 1654.4 | sup 1717.0 (ha 14 candles) | 28.02 | -0.0100% | A/venda@1717.0 (0t/3c) | zona_mapeada_setup_A |
| 2026-11-20 16:06 | SOL-USDT-SWAP | 68.82 | 69.72/68.39 | 68.31 | — | 1.0993 | -0.0163% | — | invalidado_setup_B |
| 2026-11-20 16:06 | XRP-USDT-SWAP | 0.90500 | 0.91500/0.89950 | 0.91000 | — | 0.01506 | -0.0024% | — | sem_zona |
| 2026-11-20 16:06 | DOGE-USDT-SWAP | 0.05382 | 0.05453/0.05348 | 0.05381 | — | 0.00088 | -0.0067% | — | sem_zona |
| 2026-11-20 16:06 | ARB-USDT-SWAP | 0.11280 | 0.11424/0.11164 | 0.11384 | sup 0.11622 (ha 13 candles) | 0.00200 | 0.0100% | A/venda@0.11622 (0t/3c) | zona_mapeada_setup_A |
| 2026-11-20 16:06 | WLD-USDT-SWAP | 0.23170 | 0.23590/0.22880 | 0.23290 | sup 0.24110 (ha 17 candles) | 0.00489 | -0.0286% | A/venda@0.24110 (0t/3c) | zona_mapeada_setup_A |
| 2026-11-20 16:06 | SUI-USDT-SWAP | 0.65000 | 0.66050/0.64460 | 0.65220 | sup 0.68680 (ha 13 candles) | 0.01196 | -0.0230% | — | sem_zona |
| 2026-11-20 16:06 | UNI-USDT-SWAP | 4.4170 | 4.5160/4.3830 | 4.4740 | sup 4.7260 (ha 14 candles) | 0.09629 | -0.0012% | A/venda@4.7260 (0t/3c) | zona_mapeada_setup_A |
| 2026-11-20 16:06 | LINK-USDT-SWAP | 8.3950 | 8.4900/8.3220 | 8.3370 | sup 8.7490 (ha 13 candles) | 0.14143 | -0.0064% | A/venda@8.7490 (0t/3c) | zona_mapeada_setup_A |
| 2026-11-20 17:06 | BTC-USDT-SWAP | 58522.5 | 58875.0/57695.3 | 58522.5 | sup 61256.6 (ha 18 candles) | 841.72 | -0.0010% | A/venda@61256.6 (0t/4c) | zona_mapeada_setup_A |
| 2026-11-20 17:06 | ETH-USDT-SWAP | 1606.9 | 1618.0/1578.9 | 1606.9 | sup 1717.0 (ha 15 candles) | 29.15 | -0.0136% | A/venda@1717.0 (0t/4c) | zona_mapeada_setup_A |
| 2026-11-20 17:06 | SOL-USDT-SWAP | 68.16 | 68.88/67.41 | 68.16 | — | 1.1286 | -0.0150% | B/compra@67.33 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-20 17:06 | XRP-USDT-SWAP | 0.89430 | 0.90620/0.89080 | 0.89430 | — | 0.01517 | -0.0007% | B/compra@0.89220 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-20 17:06 | DOGE-USDT-SWAP | 0.05313 | 0.05389/0.05276 | 0.05313 | — | 0.00090 | -0.0074% | — | sem_zona |
| 2026-11-20 17:06 | ARB-USDT-SWAP | 0.11164 | 0.11311/0.11032 | 0.11164 | sup 0.11622 (ha 14 candles) | 0.00207 | 0.0100% | A/venda@0.11622 (0t/4c) | zona_mapeada_setup_A |
| 2026-11-20 17:06 | WLD-USDT-SWAP | 0.22850 | 0.23190/0.22620 | 0.22850 | sup 0.24110 (ha 18 candles) | 0.00491 | -0.0257% | A/venda@0.24110 (0t/4c) | zona_mapeada_setup_A |
| 2026-11-20 17:06 | SUI-USDT-SWAP | 0.64080 | 0.65040/0.63620 | 0.64080 | sup 0.68680 (ha 14 candles) | 0.01194 | -0.0206% | — | sem_zona |
| 2026-11-20 17:06 | UNI-USDT-SWAP | 4.3510 | 4.4280/4.3190 | 4.3510 | sup 4.7260 (ha 15 candles) | 0.09714 | 0.0026% | A/venda@4.7260 (0t/4c) | zona_mapeada_setup_A |
| 2026-11-20 17:06 | LINK-USDT-SWAP | 8.3580 | 8.4360/8.2610 | 8.3580 | sup 8.2380 (ha 3 candles) | 0.14300 | -0.0082% | A/venda@8.7490 (0t/4c) | zona_mapeada_setup_A |
| 2026-11-20 18:06 | BTC-USDT-SWAP | 58437.4 | 58771.4/58179.1 | 58522.5 | sup 61256.6 (ha 19 candles) | 858.23 | -0.0025% | A/venda@61256.6 (0t/5c) | zona_mapeada_setup_A |
| 2026-11-20 18:06 | ETH-USDT-SWAP | 1601.0 | 1615.7/1585.0 | 1606.9 | sup 1717.0 (ha 16 candles) | 30.42 | -0.0188% | A/venda@1717.0 (0t/5c) | zona_mapeada_setup_A |
| 2026-11-20 18:06 | SOL-USDT-SWAP | 67.46 | 68.54/67.10 | 68.16 | — | 1.1929 | -0.0136% | B/compra@67.33 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-20 18:06 | XRP-USDT-SWAP | 0.88780 | 0.89870/0.88370 | 0.89430 | — | 0.01557 | 0.0006% | — | invalidado_setup_B |
| 2026-11-20 18:06 | DOGE-USDT-SWAP | 0.05280 | 0.05340/0.05253 | 0.05313 | — | 0.00094 | -0.0074% | — | sem_zona |
| 2026-11-20 18:06 | ARB-USDT-SWAP | 0.11145 | 0.11217/0.11059 | 0.11164 | sup 0.11622 (ha 15 candles) | 0.00203 | 0.0100% | A/venda@0.11622 (0t/5c) | zona_mapeada_setup_A |
| 2026-11-20 18:06 | WLD-USDT-SWAP | 0.22660 | 0.22930/0.22450 | 0.22850 | sup 0.24110 (ha 19 candles) | 0.00493 | -0.0250% | A/venda@0.24110 (0t/5c) | zona_mapeada_setup_A |
| 2026-11-20 18:06 | SUI-USDT-SWAP | 0.63490 | 0.64250/0.63140 | 0.64080 | sup 0.68680 (ha 15 candles) | 0.01231 | -0.0194% | — | sem_zona |
| 2026-11-20 18:06 | UNI-USDT-SWAP | 4.3610 | 4.3770/4.3080 | 4.3510 | sup 4.7260 (ha 16 candles) | 0.09700 | 0.0051% | A/venda@4.7260 (0t/5c) | zona_mapeada_setup_A |
| 2026-11-20 18:06 | LINK-USDT-SWAP | 8.3260 | 8.4050/8.2670 | 8.3580 | sup 8.2380 (ha 4 candles) | 0.14871 | -0.0101% | A/venda@8.7490 (0t/5c) | zona_mapeada_setup_A |
| 2026-11-20 19:06 | BTC-USDT-SWAP | 58982.2 | 59374.0/58166.0 | 58522.5 | sup 61256.6 (ha 20 candles) | 902.93 | -0.0036% | A/venda@61256.6 (0t/6c) | zona_mapeada_setup_A |
| 2026-11-20 19:06 | ETH-USDT-SWAP | 1618.3 | 1631.7/1593.5 | 1606.9 | sup 1717.0 (ha 17 candles) | 32.00 | -0.0213% | A/venda@1717.0 (0t/6c) | zona_mapeada_setup_A |
| 2026-11-20 19:06 | SOL-USDT-SWAP | 69.03 | 69.05/67.09 | 68.16 | — | 1.2850 | -0.0135% | — | descartado_rr_baixo_setup_B |
| 2026-11-20 19:06 | XRP-USDT-SWAP | 0.90840 | 0.91150/0.88360 | 0.89430 | — | 0.01664 | 0.0002% | — | sem_zona |
| 2026-11-20 19:06 | DOGE-USDT-SWAP | 0.05404 | 0.05415/0.05251 | 0.05313 | — | 0.00102 | -0.0054% | — | sem_zona |
| 2026-11-20 19:06 | ARB-USDT-SWAP | 0.11385 | 0.11422/0.11087 | 0.11164 | sup 0.11622 (ha 16 candles) | 0.00210 | 0.0100% | A/venda@0.11622 (0t/6c) | zona_mapeada_setup_A |
| 2026-11-20 19:06 | WLD-USDT-SWAP | 0.23050 | 0.23230/0.22420 | 0.22850 | sup 0.24110 (ha 20 candles) | 0.00526 | -0.0228% | A/venda@0.24110 (0t/6c) | zona_mapeada_setup_A |
| 2026-11-20 19:06 | SUI-USDT-SWAP | 0.64970 | 0.65250/0.63110 | 0.64080 | sup 0.68680 (ha 16 candles) | 0.01336 | -0.0166% | — | sem_zona |
| 2026-11-20 19:06 | UNI-USDT-SWAP | 4.4480 | 4.4820/4.3430 | 4.3510 | sup 4.7260 (ha 17 candles) | 0.10264 | 0.0060% | A/venda@4.7260 (0t/6c) | zona_mapeada_setup_A |
| 2026-11-20 19:06 | LINK-USDT-SWAP | 8.5070 | 8.5170/8.2830 | 8.3580 | sup 8.2380 (ha 5 candles) | 0.15900 | -0.0113% | A/venda@8.7490 (0t/6c) | zona_mapeada_setup_A |
| 2026-11-20 20:06 | BTC-USDT-SWAP | 59130.4 | 59265.4/58856.8 | 58522.5 | sup 57695.3 (ha 3 candles) | 907.97 | -0.0051% | A/venda@61256.6 (0t/7c) | zona_mapeada_setup_A |
| 2026-11-20 20:06 | ETH-USDT-SWAP | 1621.6 | 1627.3/1613.4 | 1606.9 | sup 1578.9 (ha 3 candles) | 32.14 | -0.0204% | A/venda@1717.0 (0t/7c) | zona_mapeada_setup_A |
| 2026-11-20 20:06 | SOL-USDT-SWAP | 69.29 | 69.45/68.82 | 68.16 | — | 1.3050 | -0.0124% | B/compra@69.87 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-20 20:06 | XRP-USDT-SWAP | 0.91420 | 0.91600/0.90620 | 0.89430 | — | 0.01670 | -0.0015% | — | sem_zona |
| 2026-11-20 20:06 | DOGE-USDT-SWAP | 0.05453 | 0.05460/0.05392 | 0.05313 | — | 0.00103 | -0.0046% | — | sem_zona |
| 2026-11-20 20:06 | ARB-USDT-SWAP | 0.11477 | 0.11505/0.11352 | 0.11164 | sup 0.11032 (ha 3 candles) | 0.00211 | 0.0097% | A/venda@0.11622 (0t/7c) | zona_mapeada_setup_A |
| 2026-11-20 20:06 | WLD-USDT-SWAP | 0.23150 | 0.23210/0.22910 | 0.22850 | sup 0.24110 (ha 21 candles) | 0.00530 | -0.0219% | A/venda@0.24110 (0t/7c) | zona_mapeada_setup_A |
| 2026-11-20 20:06 | SUI-USDT-SWAP | 0.65570 | 0.65670/0.64820 | 0.64080 | sup 0.68680 (ha 17 candles) | 0.01350 | -0.0157% | A/venda@0.68680 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-20 20:06 | UNI-USDT-SWAP | 4.4580 | 4.4640/4.4140 | 4.3510 | sup 4.7260 (ha 18 candles) | 0.10271 | 0.0033% | A/venda@4.7260 (0t/7c) | zona_mapeada_setup_A |
| 2026-11-20 20:06 | LINK-USDT-SWAP | 8.5810 | 8.5890/8.4900 | 8.3580 | sup 8.2380 (ha 6 candles) | 0.16157 | -0.0109% | A/venda@8.7490 (0t/7c) | zona_mapeada_setup_A |
| 2026-11-20 21:06 | BTC-USDT-SWAP | 58919.5 | 59258.8/58823.9 | 58919.5 | sup 57695.3 (ha 4 candles) | 916.14 | -0.0060% | — | zona_expirada_setup_A |
| 2026-11-20 21:06 | ETH-USDT-SWAP | 1622.0 | 1628.6/1618.0 | 1622.0 | sup 1578.9 (ha 4 candles) | 32.09 | -0.0193% | — | zona_expirada_setup_A |
| 2026-11-20 21:06 | SOL-USDT-SWAP | 68.82 | 69.58/68.79 | 68.82 | — | 1.3207 | -0.0133% | — | invalidado_setup_B |
| 2026-11-20 21:06 | XRP-USDT-SWAP | 0.91010 | 0.91750/0.90820 | 0.91010 | — | 0.01683 | -0.0032% | — | sem_zona |
| 2026-11-20 21:06 | DOGE-USDT-SWAP | 0.05437 | 0.05479/0.05431 | 0.05437 | — | 0.00104 | -0.0025% | — | sem_zona |
| 2026-11-20 21:06 | ARB-USDT-SWAP | 0.11417 | 0.11550/0.11410 | 0.11417 | sup 0.11032 (ha 4 candles) | 0.00214 | 0.0037% | — | zona_expirada_setup_A |
| 2026-11-20 21:06 | WLD-USDT-SWAP | 0.22980 | 0.23270/0.22980 | 0.22980 | sup 0.24110 (ha 22 candles) | 0.00537 | -0.0247% | — | zona_expirada_setup_A |
| 2026-11-20 21:06 | SUI-USDT-SWAP | 0.65130 | 0.65910/0.65090 | 0.65130 | sup 0.68680 (ha 18 candles) | 0.01376 | -0.0140% | A/venda@0.68680 (0t/1c) | zona_mapeada_setup_A |
| 2026-11-20 21:06 | UNI-USDT-SWAP | 4.4720 | 4.5030/4.4540 | 4.4720 | sup 4.3080 (ha 3 candles) | 0.10343 | -0.0006% | — | zona_expirada_setup_A |
| 2026-11-20 21:06 | LINK-USDT-SWAP | 8.5400 | 8.6180/8.5330 | 8.5400 | sup 8.2380 (ha 7 candles) | 0.16386 | -0.0115% | — | zona_expirada_setup_A |
| 2026-11-20 22:06 | BTC-USDT-SWAP | 58996.2 | 59136.8/58850.0 | 58919.5 | sup 57695.3 (ha 5 candles) | 885.40 | -0.0072% | — | sem_zona |
| 2026-11-20 22:06 | ETH-USDT-SWAP | 1622.3 | 1627.6/1620.2 | 1622.0 | sup 1578.9 (ha 5 candles) | 31.35 | -0.0198% | — | sem_zona |
| 2026-11-20 22:06 | SOL-USDT-SWAP | 68.92 | 69.11/68.72 | 68.82 | — | 1.2821 | -0.0141% | — | sem_zona |
| 2026-11-20 22:06 | XRP-USDT-SWAP | 0.90950 | 0.91360/0.90860 | 0.91010 | — | 0.01628 | -0.0049% | — | sem_zona |
| 2026-11-20 22:06 | DOGE-USDT-SWAP | 0.05441 | 0.05446/0.05420 | 0.05437 | — | 0.00101 | 0.0007% | — | sem_zona |
| 2026-11-20 22:06 | ARB-USDT-SWAP | 0.11301 | 0.11426/0.11288 | 0.11417 | sup 0.11032 (ha 5 candles) | 0.00215 | 0.0009% | — | sem_zona |
| 2026-11-20 22:06 | WLD-USDT-SWAP | 0.22780 | 0.23000/0.22780 | 0.22980 | sup 0.22420 (ha 3 candles) | 0.00535 | -0.0298% | — | sem_zona |
| 2026-11-20 22:06 | SUI-USDT-SWAP | 0.64920 | 0.65190/0.64700 | 0.65130 | sup 0.63110 (ha 3 candles) | 0.01336 | -0.0144% | A/venda@0.68680 (0t/2c) | zona_mapeada_setup_A |
| 2026-11-20 22:06 | UNI-USDT-SWAP | 4.4790 | 4.4920/4.4450 | 4.4720 | sup 4.3080 (ha 4 candles) | 0.10143 | -0.0041% | — | sem_zona |
| 2026-11-20 22:06 | LINK-USDT-SWAP | 8.5510 | 8.5710/8.5180 | 8.5400 | sup 8.2380 (ha 8 candles) | 0.16057 | -0.0129% | — | sem_zona |
| 2026-11-20 23:06 | BTC-USDT-SWAP | 59002.2 | 59209.9/58880.0 | 58919.5 | sup 57695.3 (ha 6 candles) | 881.29 | -0.0075% | — | sem_zona |
| 2026-11-20 23:06 | ETH-USDT-SWAP | 1625.1 | 1628.5/1616.7 | 1622.0 | sup 1578.9 (ha 6 candles) | 31.32 | -0.0192% | — | sem_zona |
| 2026-11-20 23:06 | SOL-USDT-SWAP | 68.78 | 69.15/68.52 | 68.82 | — | 1.2650 | -0.0133% | — | sem_zona |
| 2026-11-20 23:06 | XRP-USDT-SWAP | 0.91030 | 0.91200/0.90440 | 0.91010 | — | 0.01592 | -0.0048% | — | sem_zona |
| 2026-11-20 23:06 | DOGE-USDT-SWAP | 0.05454 | 0.05462/0.05424 | 0.05437 | — | 0.00100 | 0.0047% | — | sem_zona |
| 2026-11-20 23:06 | ARB-USDT-SWAP | 0.11296 | 0.11338/0.11220 | 0.11417 | sup 0.11032 (ha 6 candles) | 0.00214 | -0.0022% | — | sem_zona |
| 2026-11-20 23:06 | WLD-USDT-SWAP | 0.22750 | 0.22840/0.22520 | 0.22980 | sup 0.22420 (ha 4 candles) | 0.00539 | -0.0287% | — | sem_zona |
| 2026-11-20 23:06 | SUI-USDT-SWAP | 0.64730 | 0.65070/0.64380 | 0.65130 | sup 0.63110 (ha 4 candles) | 0.01334 | -0.0134% | A/venda@0.68680 (0t/3c) | zona_mapeada_setup_A |
| 2026-11-20 23:06 | UNI-USDT-SWAP | 4.4860 | 4.4920/4.4590 | 4.4720 | sup 4.3080 (ha 5 candles) | 0.09986 | -0.0071% | — | sem_zona |
| 2026-11-20 23:06 | LINK-USDT-SWAP | 8.5640 | 8.5830/8.5170 | 8.5400 | sup 8.2380 (ha 9 candles) | 0.15736 | -0.0123% | — | sem_zona |
| 2026-11-21 00:06 | BTC-USDT-SWAP | 58570.9 | 59053.3/58541.0 | 58919.5 | sup 57695.3 (ha 7 candles) | 871.50 | -0.0062% | — | sem_zona |
| 2026-11-21 00:06 | ETH-USDT-SWAP | 1619.2 | 1627.4/1615.2 | 1622.0 | sup 1578.9 (ha 7 candles) | 30.54 | -0.0176% | — | sem_zona |
| 2026-11-21 00:06 | SOL-USDT-SWAP | 68.53 | 68.92/68.38 | 68.82 | — | 1.2343 | -0.0116% | — | sem_zona |
| 2026-11-21 00:06 | XRP-USDT-SWAP | 0.90200 | 0.91220/0.90030 | 0.91010 | — | 0.01604 | -0.0040% | — | sem_zona |
| 2026-11-21 00:06 | DOGE-USDT-SWAP | 0.05418 | 0.05474/0.05407 | 0.05437 | — | 0.00100 | 0.0050% | — | sem_zona |
| 2026-11-21 00:06 | ARB-USDT-SWAP | 0.11208 | 0.11335/0.11186 | 0.11417 | sup 0.11032 (ha 7 candles) | 0.00215 | -0.0012% | — | sem_zona |
| 2026-11-21 00:06 | WLD-USDT-SWAP | 0.22390 | 0.22790/0.22330 | 0.22980 | sup 0.22420 (ha 5 candles) | 0.00544 | -0.0290% | A/venda@0.22420 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-21 00:06 | SUI-USDT-SWAP | 0.63850 | 0.64860/0.63770 | 0.65130 | sup 0.63110 (ha 5 candles) | 0.01348 | -0.0124% | A/venda@0.68680 (0t/4c) | zona_mapeada_setup_A |
| 2026-11-21 00:06 | UNI-USDT-SWAP | 4.4420 | 4.4980/4.4230 | 4.4720 | sup 4.3080 (ha 6 candles) | 0.10021 | -0.0094% | — | sem_zona |
| 2026-11-21 00:06 | LINK-USDT-SWAP | 8.4840 | 8.5830/8.4730 | 8.5400 | sup 8.2380 (ha 10 candles) | 0.15743 | -0.0101% | — | sem_zona |
| 2026-11-21 01:06 | BTC-USDT-SWAP | 56700.1 | 58570.9/56334.2 | 56700.1 | sup 57695.3 (ha 8 candles) | 982.48 | -0.0066% | A/venda@57695.3 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-21 01:06 | ETH-USDT-SWAP | 1570.9 | 1619.8/1553.3 | 1570.9 | sup 1578.9 (ha 8 candles) | 33.16 | -0.0173% | A/venda@1578.9 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-21 01:06 | SOL-USDT-SWAP | 66.24 | 68.54/65.72 | 66.24 | — | 1.3679 | -0.0118% | — | sem_zona |
| 2026-11-21 01:06 | XRP-USDT-SWAP | 0.88080 | 0.90190/0.87140 | 0.88080 | — | 0.01701 | -0.0034% | — | sem_zona |
| 2026-11-21 01:06 | DOGE-USDT-SWAP | 0.05207 | 0.05419/0.05162 | 0.05207 | — | 0.00112 | 0.0051% | — | sem_zona |
| 2026-11-21 01:06 | ARB-USDT-SWAP | 0.10811 | 0.11222/0.10701 | 0.10811 | sup 0.11032 (ha 8 candles) | 0.00244 | 0.0011% | A/venda@0.11032 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-21 01:06 | WLD-USDT-SWAP | 0.21450 | 0.22400/0.21180 | 0.21450 | sup 0.22420 (ha 6 candles) | 0.00596 | -0.0320% | — | descartado_rr_baixo_setup_A |
| 2026-11-21 01:06 | SUI-USDT-SWAP | 0.60990 | 0.63840/0.60280 | 0.60990 | sup 0.63110 (ha 6 candles) | 0.01512 | -0.0113% | A/venda@0.68680 (0t/5c) | zona_mapeada_setup_A |
| 2026-11-21 01:06 | UNI-USDT-SWAP | 4.3020 | 4.4480/4.2390 | 4.3020 | sup 4.3080 (ha 7 candles) | 0.10850 | -0.0090% | A/venda@4.3080 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-21 01:06 | LINK-USDT-SWAP | 8.1810 | 8.4840/8.1040 | 8.1810 | sup 8.2380 (ha 11 candles) | 0.17529 | -0.0071% | A/venda@8.2380 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-21 02:06 | BTC-USDT-SWAP | 56270.7 | 56806.5/55500.0 | 56700.1 | sup 57695.3 (ha 9 candles) | 1016.0 | -0.0067% | A/venda@57695.3 (0t/1c) | zona_mapeada_setup_A |
| 2026-11-21 02:06 | ETH-USDT-SWAP | 1560.4 | 1573.0/1536.3 | 1570.9 | sup 1578.9 (ha 9 candles) | 33.24 | -0.0158% | A/venda@1578.9 (1t/0c) | zona_mapeada_setup_A |
| 2026-11-21 02:06 | SOL-USDT-SWAP | 66.00 | 66.45/65.10 | 66.24 | — | 1.3729 | -0.0112% | — | sem_zona |
| 2026-11-21 02:06 | XRP-USDT-SWAP | 0.87570 | 0.88340/0.86710 | 0.88080 | — | 0.01699 | -0.0030% | — | sem_zona |
| 2026-11-21 02:06 | DOGE-USDT-SWAP | 0.05184 | 0.05223/0.05096 | 0.05207 | — | 0.00113 | 0.0030% | — | sem_zona |
| 2026-11-21 02:06 | ARB-USDT-SWAP | 0.10747 | 0.10842/0.10585 | 0.10811 | sup 0.11032 (ha 9 candles) | 0.00253 | 0.0035% | A/venda@0.11032 (0t/1c) | zona_mapeada_setup_A |
| 2026-11-21 02:06 | WLD-USDT-SWAP | 0.21560 | 0.21620/0.21010 | 0.21450 | sup 0.22420 (ha 7 candles) | 0.00604 | -0.0377% | — | sem_zona |
| 2026-11-21 02:06 | SUI-USDT-SWAP | 0.60420 | 0.61260/0.59530 | 0.60990 | sup 0.63110 (ha 7 candles) | 0.01552 | -0.0112% | A/venda@0.68680 (0t/6c) | zona_mapeada_setup_A |
| 2026-11-21 02:06 | UNI-USDT-SWAP | 4.2540 | 4.3130/4.2140 | 4.3020 | sup 4.3080 (ha 8 candles) | 0.10993 | -0.0040% | A/venda@4.3080 (1t/0c) | zona_mapeada_setup_A |
| 2026-11-21 02:06 | LINK-USDT-SWAP | 8.1530 | 8.2080/7.9940 | 8.1810 | sup 8.2380 (ha 12 candles) | 0.17900 | -0.0049% | A/venda@8.2380 (1t/0c) | zona_mapeada_setup_A |
| 2026-11-21 03:06 | BTC-USDT-SWAP | 55778.3 | 56480.0/55680.5 | 56700.1 | sup 57695.3 (ha 10 candles) | 889.59 | -0.0042% | A/venda@57695.3 (0t/2c) | zona_mapeada_setup_A |
| 2026-11-21 03:06 | ETH-USDT-SWAP | 1561.4 | 1574.6/1557.2 | 1570.9 | sup 1578.9 (ha 10 candles) | 27.34 | -0.0132% | A/venda@1578.9 (2t/0c) | zona_mapeada_setup_A |
| 2026-11-21 03:06 | SOL-USDT-SWAP | 65.41 | 66.36/65.28 | 66.24 | — | 1.2136 | -0.0107% | — | sem_zona |
| 2026-11-21 03:06 | XRP-USDT-SWAP | 0.87170 | 0.88090/0.86970 | 0.88080 | — | 0.01469 | -0.0025% | — | sem_zona |
| 2026-11-21 03:06 | DOGE-USDT-SWAP | 0.05151 | 0.05216/0.05139 | 0.05207 | — | 0.00097 | 0.0015% | — | sem_zona |
| 2026-11-21 03:06 | ARB-USDT-SWAP | 0.10617 | 0.10786/0.10601 | 0.10811 | sup 0.11032 (ha 10 candles) | 0.00224 | 0.0040% | A/venda@0.11032 (0t/2c) | zona_mapeada_setup_A |
| 2026-11-21 03:06 | WLD-USDT-SWAP | 0.21300 | 0.21650/0.21260 | 0.21450 | sup 0.22420 (ha 8 candles) | 0.00527 | -0.0408% | — | sem_zona |
| 2026-11-21 03:06 | SUI-USDT-SWAP | 0.59560 | 0.60650/0.59470 | 0.60990 | sup 0.63110 (ha 8 candles) | 0.01379 | -0.0116% | A/venda@0.68680 (0t/7c) | zona_mapeada_setup_A |
| 2026-11-21 03:06 | UNI-USDT-SWAP | 4.2530 | 4.2830/4.2350 | 4.3020 | sup 4.3080 (ha 9 candles) | 0.08864 | -0.0006% | A/venda@4.3080 (2t/0c) | zona_mapeada_setup_A |
| 2026-11-21 03:06 | LINK-USDT-SWAP | 8.0510 | 8.1860/8.0340 | 8.1810 | sup 8.2380 (ha 13 candles) | 0.15529 | -0.0002% | A/venda@8.2380 (1t/1c) | zona_mapeada_setup_A |
| 2026-11-21 04:06 | BTC-USDT-SWAP | 58020.0 | 58076.1/55100.0 | 56700.1 | sup 57695.3 (ha 11 candles) | 1025.7 | -0.0034% | — | invalidado_setup_A |
| 2026-11-21 04:06 | ETH-USDT-SWAP | 1639.7 | 1656.9/1543.4 | 1570.9 | sup 1578.9 (ha 11 candles) | 32.82 | -0.0083% | — | invalidado_setup_A |
| 2026-11-21 04:06 | SOL-USDT-SWAP | 68.20 | 68.48/64.79 | 66.24 | — | 1.3493 | -0.0114% | B/compra@67.33 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-21 04:06 | XRP-USDT-SWAP | 0.90010 | 0.90240/0.85930 | 0.88080 | — | 0.01642 | -0.0002% | B/compra@0.89220 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-21 04:06 | DOGE-USDT-SWAP | 0.05365 | 0.05383/0.05073 | 0.05207 | — | 0.00111 | 0.0006% | — | sem_zona |
| 2026-11-21 04:06 | ARB-USDT-SWAP | 0.10933 | 0.10988/0.10415 | 0.10811 | sup 0.11032 (ha 11 candles) | 0.00244 | 0.0071% | A/venda@0.11032 (1t/0c) | zona_mapeada_setup_A |
| 2026-11-21 04:06 | WLD-USDT-SWAP | 0.22100 | 0.22290/0.20890 | 0.21450 | sup 0.22420 (ha 9 candles) | 0.00587 | -0.0388% | — | sem_zona |
| 2026-11-21 04:06 | SUI-USDT-SWAP | 0.62500 | 0.62650/0.58730 | 0.60990 | sup 0.63110 (ha 9 candles) | 0.01535 | -0.0120% | — | zona_expirada_setup_A |
| 2026-11-21 04:06 | UNI-USDT-SWAP | 4.4470 | 4.4710/4.1830 | 4.3020 | sup 4.3080 (ha 10 candles) | 0.10157 | 0.0018% | — | invalidado_setup_A |
| 2026-11-21 04:06 | LINK-USDT-SWAP | 8.4000 | 8.4470/7.9650 | 8.1810 | sup 8.2380 (ha 14 candles) | 0.17471 | 0.0031% | — | invalidado_setup_A |
| 2026-11-21 05:06 | BTC-USDT-SWAP | 57959.6 | 58636.2/57701.0 | 57959.6 | sup 57695.3 (ha 12 candles) | 1042.4 | -0.0047% | — | sem_zona |
| 2026-11-21 05:06 | ETH-USDT-SWAP | 1630.0 | 1645.8/1625.1 | 1630.0 | sup 1536.3 (ha 3 candles) | 32.35 | -0.0041% | — | sem_zona |
| 2026-11-21 05:06 | SOL-USDT-SWAP | 67.35 | 68.40/67.32 | 67.35 | — | 1.3714 | -0.0127% | B/compra@67.33 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-21 05:06 | XRP-USDT-SWAP | 0.89100 | 0.90330/0.89010 | 0.89100 | — | 0.01656 | -0.0006% | B/compra@0.89220 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-21 05:06 | DOGE-USDT-SWAP | 0.05287 | 0.05382/0.05282 | 0.05287 | — | 0.00113 | -0.0030% | — | sem_zona |
| 2026-11-21 05:06 | ARB-USDT-SWAP | 0.10681 | 0.10941/0.10648 | 0.10681 | sup 0.11032 (ha 12 candles) | 0.00254 | 0.0064% | A/venda@0.11032 (1t/1c) | zona_mapeada_setup_A |
| 2026-11-21 05:06 | WLD-USDT-SWAP | 0.21600 | 0.22240/0.21580 | 0.21600 | sup 0.22420 (ha 10 candles) | 0.00603 | -0.0362% | — | sem_zona |
| 2026-11-21 05:06 | SUI-USDT-SWAP | 0.61580 | 0.62760/0.61530 | 0.61580 | sup 0.63110 (ha 10 candles) | 0.01559 | -0.0153% | A/venda@0.63110 (0t/0c) | zona_mapeada_setup_A |
| 2026-11-21 05:06 | UNI-USDT-SWAP | 4.3760 | 4.4670/4.3750 | 4.3760 | sup 4.3080 (ha 11 candles) | 0.10286 | -0.0008% | — | sem_zona |
| 2026-11-21 05:06 | LINK-USDT-SWAP | 8.3240 | 8.4250/8.3090 | 8.3240 | sup 8.2380 (ha 15 candles) | 0.17657 | 0.0032% | — | sem_zona |
| 2026-11-21 06:06 | BTC-USDT-SWAP | 57771.0 | 58119.4/57341.3 | 57959.6 | sup 57695.3 (ha 13 candles) | 998.90 | -0.0057% | — | sem_zona |
| 2026-11-21 06:06 | ETH-USDT-SWAP | 1627.4 | 1636.6/1617.2 | 1630.0 | sup 1536.3 (ha 4 candles) | 31.29 | -0.0022% | — | sem_zona |
| 2026-11-21 06:06 | SOL-USDT-SWAP | 67.25 | 67.66/66.64 | 67.35 | — | 1.3493 | -0.0157% | B/compra@67.33 (2t/0c) | zona_mapeada_setup_B |
| 2026-11-21 06:06 | XRP-USDT-SWAP | 0.88600 | 0.89300/0.87980 | 0.89100 | — | 0.01639 | -0.0008% | — | invalidado_setup_B |
| 2026-11-21 06:06 | DOGE-USDT-SWAP | 0.05273 | 0.05306/0.05234 | 0.05287 | — | 0.00111 | -0.0039% | — | sem_zona |
| 2026-11-21 06:06 | ARB-USDT-SWAP | 0.10634 | 0.10723/0.10519 | 0.10681 | sup 0.11032 (ha 13 candles) | 0.00250 | 0.0078% | A/venda@0.11032 (1t/2c) | zona_mapeada_setup_A |
| 2026-11-21 06:06 | WLD-USDT-SWAP | 0.21550 | 0.21700/0.21250 | 0.21600 | sup 0.22420 (ha 11 candles) | 0.00584 | -0.0332% | — | sem_zona |
| 2026-11-21 06:06 | SUI-USDT-SWAP | 0.61260 | 0.61850/0.60830 | 0.61580 | sup 0.63110 (ha 11 candles) | 0.01519 | -0.0172% | A/venda@0.63110 (0t/1c) | zona_mapeada_setup_A |
| 2026-11-21 06:06 | UNI-USDT-SWAP | 4.3220 | 4.3800/4.2830 | 4.3760 | sup 4.3080 (ha 12 candles) | 0.10029 | 0.0001% | — | sem_zona |
| 2026-11-21 06:06 | LINK-USDT-SWAP | 8.3010 | 8.3510/8.2410 | 8.3240 | sup 8.2380 (ha 16 candles) | 0.17243 | 0.0038% | — | sem_zona |
| 2026-11-21 07:06 | BTC-USDT-SWAP | 57995.0 | 58071.6/57733.0 | 57959.6 | sup 55100.0 (ha 3 candles) | 938.82 | -0.0063% | — | sem_zona |
| 2026-11-21 07:06 | ETH-USDT-SWAP | 1638.4 | 1642.8/1626.2 | 1630.0 | sup 1536.3 (ha 5 candles) | 29.69 | -0.0010% | — | sem_zona |
| 2026-11-21 07:06 | SOL-USDT-SWAP | 68.05 | 68.22/67.16 | 67.35 | — | 1.3200 | -0.0190% | — | descartado_rr_baixo_setup_B |
| 2026-11-21 07:06 | XRP-USDT-SWAP | 0.89500 | 0.89740/0.88610 | 0.89100 | — | 0.01611 | -0.0007% | — | sem_zona |
| 2026-11-21 07:06 | DOGE-USDT-SWAP | 0.05321 | 0.05330/0.05271 | 0.05287 | — | 0.00107 | -0.0046% | — | sem_zona |
| 2026-11-21 07:06 | ARB-USDT-SWAP | 0.10751 | 0.10804/0.10628 | 0.10681 | sup 0.10415 (ha 3 candles) | 0.00243 | 0.0057% | A/venda@0.11032 (1t/3c) | zona_mapeada_setup_A |
| 2026-11-21 07:06 | WLD-USDT-SWAP | 0.22100 | 0.22140/0.21500 | 0.21600 | sup 0.20890 (ha 3 candles) | 0.00589 | -0.0379% | — | sem_zona |
| 2026-11-21 07:06 | SUI-USDT-SWAP | 0.62160 | 0.62280/0.61150 | 0.61580 | sup 0.58730 (ha 3 candles) | 0.01498 | -0.0193% | A/venda@0.63110 (0t/2c) | zona_mapeada_setup_A |
| 2026-11-21 07:06 | UNI-USDT-SWAP | 4.3970 | 4.4050/4.3130 | 4.3760 | sup 4.1830 (ha 3 candles) | 0.09907 | -0.0004% | — | sem_zona |
| 2026-11-21 07:06 | LINK-USDT-SWAP | 8.3900 | 8.4170/8.2950 | 8.3240 | sup 7.9650 (ha 3 candles) | 0.16864 | 0.0032% | — | sem_zona |
| 2026-11-21 08:06 | BTC-USDT-SWAP | 57903.8 | 58199.7/57812.9 | 57959.6 | sup 55100.0 (ha 4 candles) | 924.14 | -0.0050% | — | sem_zona |
| 2026-11-21 08:06 | ETH-USDT-SWAP | 1640.2 | 1647.5/1634.1 | 1630.0 | sup 1536.3 (ha 6 candles) | 28.46 | 0.0004% | — | sem_zona |
| 2026-11-21 08:06 | SOL-USDT-SWAP | 68.05 | 68.38/67.89 | 67.35 | — | 1.2521 | -0.0213% | — | sem_zona |
| 2026-11-21 08:06 | XRP-USDT-SWAP | 0.89560 | 0.89870/0.89010 | 0.89100 | — | 0.01565 | 0.0010% | — | sem_zona |
| 2026-11-21 08:06 | DOGE-USDT-SWAP | 0.05301 | 0.05325/0.05286 | 0.05287 | — | 0.00104 | -0.0039% | — | sem_zona |
| 2026-11-21 08:06 | ARB-USDT-SWAP | 0.10815 | 0.10870/0.10654 | 0.10681 | sup 0.10415 (ha 4 candles) | 0.00247 | 0.0044% | A/venda@0.11032 (1t/4c) | zona_mapeada_setup_A |
| 2026-11-21 08:06 | WLD-USDT-SWAP | 0.21910 | 0.22140/0.21880 | 0.21600 | sup 0.20890 (ha 4 candles) | 0.00574 | -0.0360% | — | sem_zona |
| 2026-11-21 08:06 | SUI-USDT-SWAP | 0.62120 | 0.62460/0.61730 | 0.61580 | sup 0.58730 (ha 4 candles) | 0.01471 | -0.0189% | A/venda@0.63110 (0t/3c) | zona_mapeada_setup_A |
| 2026-11-21 08:06 | UNI-USDT-SWAP | 4.4130 | 4.4380/4.3700 | 4.3760 | sup 4.1830 (ha 4 candles) | 0.09900 | -0.0026% | — | sem_zona |
| 2026-11-21 08:06 | LINK-USDT-SWAP | 8.3750 | 8.4080/8.3350 | 8.3240 | sup 7.9650 (ha 4 candles) | 0.16400 | 0.0035% | — | sem_zona |
| 2026-11-21 09:06 | BTC-USDT-SWAP | 58177.2 | 58627.9/57828.9 | 58177.2 | sup 55100.0 (ha 5 candles) | 894.93 | -0.0029% | — | sem_zona |
| 2026-11-21 09:06 | ETH-USDT-SWAP | 1651.9 | 1672.0/1638.4 | 1651.9 | sup 1536.3 (ha 7 candles) | 28.13 | 0.0019% | — | sem_zona |
| 2026-11-21 09:06 | SOL-USDT-SWAP | 68.80 | 69.40/67.94 | 68.80 | — | 1.2164 | -0.0223% | — | sem_zona |
| 2026-11-21 09:06 | XRP-USDT-SWAP | 0.90320 | 0.91260/0.89510 | 0.90320 | — | 0.01491 | 0.0028% | — | sem_zona |
| 2026-11-21 09:06 | DOGE-USDT-SWAP | 0.05372 | 0.05419/0.05297 | 0.05372 | — | 0.00101 | -0.0026% | — | sem_zona |
| 2026-11-21 09:06 | ARB-USDT-SWAP | 0.10957 | 0.11117/0.10814 | 0.10957 | sup 0.10415 (ha 5 candles) | 0.00245 | 0.0045% | A/venda@0.11032 (2t/0c) | zona_mapeada_setup_A |
| 2026-11-21 09:06 | WLD-USDT-SWAP | 0.22190 | 0.22530/0.21860 | 0.22190 | sup 0.20890 (ha 5 candles) | 0.00564 | -0.0341% | — | sem_zona |
| 2026-11-21 09:06 | SUI-USDT-SWAP | 0.62730 | 0.63580/0.61920 | 0.62730 | sup 0.58730 (ha 5 candles) | 0.01436 | -0.0166% | A/venda@0.63110 (1t/0c) | zona_mapeada_setup_A |
| 2026-11-21 09:06 | UNI-USDT-SWAP | 4.5080 | 4.5490/4.4090 | 4.5080 | sup 4.1830 (ha 5 candles) | 0.09907 | -0.0043% | — | sem_zona |
| 2026-11-21 09:06 | LINK-USDT-SWAP | 8.4510 | 8.5420/8.3680 | 8.4510 | sup 7.9650 (ha 5 candles) | 0.15971 | 0.0047% | — | sem_zona |
| 2026-11-21 10:06 | BTC-USDT-SWAP | 58833.4 | 59159.0/58115.0 | 58177.2 | sup 55100.0 (ha 6 candles) | 940.31 | -0.0019% | — | sem_zona |
| 2026-11-21 10:06 | ETH-USDT-SWAP | 1662.9 | 1678.7/1649.2 | 1651.9 | sup 1536.3 (ha 8 candles) | 29.25 | 0.0022% | — | sem_zona |
| 2026-11-21 10:06 | SOL-USDT-SWAP | 69.18 | 69.77/68.69 | 68.80 | — | 1.2486 | -0.0227% | B/compra@69.87 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-21 10:06 | XRP-USDT-SWAP | 0.90480 | 0.91130/0.90080 | 0.90320 | — | 0.01496 | 0.0041% | — | sem_zona |
| 2026-11-21 10:06 | DOGE-USDT-SWAP | 0.05403 | 0.05455/0.05365 | 0.05372 | — | 0.00102 | -0.0001% | — | sem_zona |
| 2026-11-21 10:06 | ARB-USDT-SWAP | 0.10925 | 0.11136/0.10900 | 0.10957 | sup 0.10415 (ha 6 candles) | 0.00251 | 0.0039% | — | confirmado_calibracao_setup_A |
| 2026-11-21 10:06 | WLD-USDT-SWAP | 0.22340 | 0.22520/0.22120 | 0.22190 | sup 0.20890 (ha 6 candles) | 0.00571 | -0.0313% | — | sem_zona |
| 2026-11-21 10:06 | SUI-USDT-SWAP | 0.63510 | 0.63980/0.62590 | 0.62730 | sup 0.58730 (ha 6 candles) | 0.01475 | -0.0150% | — | invalidado_setup_A |
| 2026-11-21 10:06 | UNI-USDT-SWAP | 4.4700 | 4.5520/4.4580 | 4.5080 | sup 4.1830 (ha 6 candles) | 0.10221 | -0.0055% | — | sem_zona |
| 2026-11-21 10:06 | LINK-USDT-SWAP | 8.4900 | 8.5770/8.4350 | 8.4510 | sup 7.9650 (ha 6 candles) | 0.16279 | 0.0055% | — | sem_zona |
| 2026-11-21 11:06 | BTC-USDT-SWAP | 60520.2 | 60921.9/58768.2 | 58177.2 | sup 55100.0 (ha 7 candles) | 1063.1 | -0.0010% | — | sem_zona |
| 2026-11-21 11:06 | ETH-USDT-SWAP | 1700.9 | 1716.0/1661.5 | 1651.9 | sup 1536.3 (ha 9 candles) | 32.39 | 0.0018% | — | sem_zona |
| 2026-11-21 11:06 | SOL-USDT-SWAP | 70.70 | 70.90/69.06 | 68.80 | — | 1.3236 | -0.0216% | — | descartado_rr_baixo_setup_B |
| 2026-11-21 11:06 | XRP-USDT-SWAP | 0.93080 | 0.93250/0.90300 | 0.90320 | — | 0.01640 | 0.0029% | B/compra@0.94130 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-21 11:06 | DOGE-USDT-SWAP | 0.05527 | 0.05557/0.05394 | 0.05372 | — | 0.00111 | 0.0013% | B/compra@0.05534 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-21 11:06 | ARB-USDT-SWAP | 0.11362 | 0.11436/0.10915 | 0.10957 | sup 0.10415 (ha 7 candles) | 0.00278 | 0.0005% | — | sem_zona |
| 2026-11-21 11:06 | WLD-USDT-SWAP | 0.23030 | 0.23100/0.22290 | 0.22190 | sup 0.20890 (ha 7 candles) | 0.00608 | -0.0281% | — | sem_zona |
| 2026-11-21 11:06 | SUI-USDT-SWAP | 0.65160 | 0.65460/0.63400 | 0.62730 | sup 0.58730 (ha 7 candles) | 0.01564 | -0.0153% | — | sem_zona |
| 2026-11-21 11:06 | UNI-USDT-SWAP | 4.7210 | 4.7890/4.4650 | 4.5080 | sup 4.1830 (ha 7 candles) | 0.12186 | -0.0017% | — | sem_zona |
| 2026-11-21 11:06 | LINK-USDT-SWAP | 8.6720 | 8.7080/8.4790 | 8.4510 | sup 7.9650 (ha 7 candles) | 0.17307 | 0.0060% | — | sem_zona |
| 2026-11-21 12:06 | BTC-USDT-SWAP | 60306.9 | 60970.0/60125.7 | 58177.2 | sup 55100.0 (ha 8 candles) | 1102.9 | -0.0003% | — | sem_zona |
| 2026-11-21 12:06 | ETH-USDT-SWAP | 1690.0 | 1712.4/1683.0 | 1651.9 | sup 1536.3 (ha 10 candles) | 33.96 | -0.0001% | — | sem_zona |
| 2026-11-21 12:06 | SOL-USDT-SWAP | 70.55 | 71.07/70.18 | 68.80 | — | 1.3593 | -0.0201% | B/compra@71.00 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-21 12:06 | XRP-USDT-SWAP | 0.93020 | 0.93430/0.92350 | 0.90320 | — | 0.01681 | 0.0008% | B/compra@0.94130 (0t/1c) | zona_mapeada_setup_B |
| 2026-11-21 12:06 | DOGE-USDT-SWAP | 0.05533 | 0.05558/0.05498 | 0.05372 | — | 0.00113 | 0.0031% | B/compra@0.05534 (1t/0c) | zona_mapeada_setup_B |
| 2026-11-21 12:06 | ARB-USDT-SWAP | 0.11325 | 0.11406/0.11247 | 0.10957 | sup 0.10415 (ha 8 candles) | 0.00279 | -0.0030% | — | sem_zona |
| 2026-11-21 12:06 | WLD-USDT-SWAP | 0.22960 | 0.23190/0.22870 | 0.22190 | sup 0.20890 (ha 8 candles) | 0.00615 | -0.0287% | — | sem_zona |
| 2026-11-21 12:06 | SUI-USDT-SWAP | 0.65040 | 0.65290/0.64520 | 0.62730 | sup 0.58730 (ha 8 candles) | 0.01584 | -0.0131% | — | sem_zona |
| 2026-11-21 12:06 | UNI-USDT-SWAP | 4.7260 | 4.7400/4.6820 | 4.5080 | sup 4.1830 (ha 8 candles) | 0.12264 | 0.0035% | — | sem_zona |
| 2026-11-21 12:06 | LINK-USDT-SWAP | 8.6460 | 8.6940/8.6000 | 8.4510 | sup 7.9650 (ha 8 candles) | 0.17600 | 0.0056% | — | sem_zona |
| 2026-11-21 13:06 | BTC-USDT-SWAP | 59908.9 | 60478.2/59654.6 | 59908.9 | sup 55100.0 (ha 9 candles) | 1138.2 | 0.0001% | — | sem_zona |
| 2026-11-21 13:06 | ETH-USDT-SWAP | 1683.8 | 1696.9/1672.3 | 1683.8 | sup 1536.3 (ha 11 candles) | 34.88 | -0.0013% | — | sem_zona |
| 2026-11-21 13:06 | SOL-USDT-SWAP | 70.38 | 71.00/70.07 | 70.38 | — | 1.3807 | -0.0158% | — | invalidado_setup_B |
| 2026-11-21 13:06 | XRP-USDT-SWAP | 0.92350 | 0.93380/0.92050 | 0.92350 | — | 0.01722 | -0.0003% | B/compra@0.94130 (0t/2c) | zona_mapeada_setup_B |
| 2026-11-21 13:06 | DOGE-USDT-SWAP | 0.05513 | 0.05567/0.05493 | 0.05513 | — | 0.00116 | 0.0047% | B/compra@0.05534 (2t/0c) | zona_mapeada_setup_B |
| 2026-11-21 13:06 | ARB-USDT-SWAP | 0.11201 | 0.11386/0.11182 | 0.11201 | sup 0.10415 (ha 9 candles) | 0.00286 | -0.0045% | — | sem_zona |
| 2026-11-21 13:06 | WLD-USDT-SWAP | 0.22820 | 0.23130/0.22740 | 0.22820 | sup 0.20890 (ha 9 candles) | 0.00620 | -0.0232% | — | sem_zona |
| 2026-11-21 13:06 | SUI-USDT-SWAP | 0.64610 | 0.65330/0.64300 | 0.64610 | sup 0.58730 (ha 9 candles) | 0.01608 | -0.0123% | — | sem_zona |
| 2026-11-21 13:06 | UNI-USDT-SWAP | 4.7030 | 4.7660/4.6620 | 4.7030 | sup 4.1830 (ha 9 candles) | 0.12771 | 0.0056% | — | sem_zona |
| 2026-11-21 13:06 | LINK-USDT-SWAP | 8.5930 | 8.6850/8.5560 | 8.5930 | sup 7.9650 (ha 9 candles) | 0.18050 | 0.0051% | — | sem_zona |
| 2026-11-21 14:06 | BTC-USDT-SWAP | 60028.6 | 60228.2/59750.0 | 59908.9 | sup 55100.0 (ha 10 candles) | 1135.7 | -0.0004% | — | sem_zona |
| 2026-11-21 14:06 | ETH-USDT-SWAP | 1683.0 | 1687.5/1676.0 | 1683.8 | sup 1536.3 (ha 12 candles) | 34.82 | -0.0011% | — | sem_zona |
| 2026-11-21 14:06 | SOL-USDT-SWAP | 70.63 | 70.75/70.06 | 70.38 | — | 1.3914 | -0.0127% | B/compra@69.87 (0t/0c) | zona_mapeada_setup_B |
| 2026-11-21 14:06 | XRP-USDT-SWAP | 0.92950 | 0.93090/0.92230 | 0.92350 | — | 0.01699 | 0.0003% | B/compra@0.94130 (0t/3c) | zona_mapeada_setup_B |
| 2026-11-21 14:06 | DOGE-USDT-SWAP | 0.05507 | 0.05515/0.05489 | 0.05513 | — | 0.00113 | 0.0074% | — | zona_expirada_setup_B |
| 2026-11-21 14:06 | ARB-USDT-SWAP | 0.11158 | 0.11205/0.11121 | 0.11201 | sup 0.10415 (ha 10 candles) | 0.00281 | -0.0040% | — | sem_zona |
| 2026-11-21 14:06 | WLD-USDT-SWAP | 0.22660 | 0.22830/0.22550 | 0.22820 | sup 0.20890 (ha 10 candles) | 0.00607 | -0.0168% | — | sem_zona |
| 2026-11-21 14:06 | SUI-USDT-SWAP | 0.64660 | 0.64730/0.64290 | 0.64610 | sup 0.58730 (ha 10 candles) | 0.01561 | -0.0120% | — | sem_zona |
| 2026-11-21 14:06 | UNI-USDT-SWAP | 4.7340 | 4.7570/4.6810 | 4.7030 | sup 4.1830 (ha 10 candles) | 0.12779 | 0.0070% | — | sem_zona |
| 2026-11-21 14:06 | LINK-USDT-SWAP | 8.5920 | 8.6130/8.5510 | 8.5930 | sup 7.9650 (ha 10 candles) | 0.17707 | 0.0062% | — | sem_zona |
| 2026-11-21 15:06 | BTC-USDT-SWAP | 60047.7 | 60317.0/59919.1 | 59908.9 | sup 55100.0 (ha 11 candles) | 1004.4 | -0.0008% | — | sem_zona |
| 2026-11-21 15:06 | ETH-USDT-SWAP | 1681.3 | 1688.2/1677.1 | 1683.8 | sup 1536.3 (ha 13 candles) | 30.86 | -0.0014% | — | sem_zona |
| 2026-11-21 15:06 | SOL-USDT-SWAP | 70.59 | 70.87/70.48 | 70.38 | — | 1.2179 | -0.0112% | B/compra@69.87 (0t/1c) | zona_mapeada_setup_B |
| 2026-11-21 15:06 | XRP-USDT-SWAP | 0.93360 | 0.93660/0.92910 | 0.92350 | — | 0.01534 | 0.0005% | B/compra@0.94130 (0t/4c) | zona_mapeada_setup_B |
| 2026-11-21 15:06 | DOGE-USDT-SWAP | 0.05513 | 0.05538/0.05505 | 0.05513 | — | 0.00097 | 0.0070% | — | sem_zona |
| 2026-11-21 15:06 | ARB-USDT-SWAP | 0.11260 | 0.11278/0.11154 | 0.11201 | sup 0.10415 (ha 11 candles) | 0.00253 | -0.0051% | — | sem_zona |
| 2026-11-21 15:06 | WLD-USDT-SWAP | 0.22850 | 0.22910/0.22630 | 0.22820 | sup 0.20890 (ha 11 candles) | 0.00540 | -0.0110% | — | sem_zona |
| 2026-11-21 15:06 | SUI-USDT-SWAP | 0.64740 | 0.65080/0.64650 | 0.64610 | sup 0.58730 (ha 11 candles) | 0.01337 | -0.0122% | — | sem_zona |
| 2026-11-21 15:06 | UNI-USDT-SWAP | 4.7170 | 4.7570/4.7170 | 4.7030 | sup 4.1830 (ha 11 candles) | 0.11571 | 0.0070% | — | sem_zona |
| 2026-11-21 15:06 | LINK-USDT-SWAP | 8.5820 | 8.6120/8.5720 | 8.5930 | sup 7.9650 (ha 11 candles) | 0.15279 | 0.0065% | — | sem_zona |
