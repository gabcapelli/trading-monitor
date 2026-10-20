# Log de Monitoramento Automatico -- Multi-Par (script gratuito, GitHub Actions)

> Gerado por script Python sem LLM (ver monitor/fetch_and_check.py). Fonte: OKX. Cobre os pares em PAIRS (configuracao no topo do script) -- BTC-USDT-SWAP e os demais adicionados na expansao de 07/09/2026. Leitura e MECANICA (regras objetivas da secao 4 do plano), sem a prosa qualitativa que o Claude gerava -- cole este log numa conversa do Claude se quiser a leitura interpretativa.

| Data/Hora (BRT) | Par | Close 1h | High/Low 1h | Close 4h | Swing 1h ref | ATR 1h | Funding | Zona ativa | Status checklist |
|---|---|---|---|---|---|---|---|---|---|
| 2026-10-18 08:05 | BTC-USDT-SWAP | 82056.1 | 82229.5/82056.0 | 81638.8 | res 82049.5 (ha 7 candles) | 300.17 | 0.0040% | A/compra@82049.5 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-18 08:05 | ETH-USDT-SWAP | 2418.2 | 2426.0/2418.0 | 2407.8 | — | 16.12 | 0.0100% | — | sem_zona |
| 2026-10-18 08:05 | SOL-USDT-SWAP | 103.95 | 104.27/103.79 | 103.25 | — | 0.89786 | 0.0037% | — | sem_zona |
| 2026-10-18 08:05 | XRP-USDT-SWAP | 1.2978 | 1.3013/1.2966 | 1.2921 | res 1.3048 (ha 7 candles) | 0.00942 | -0.0017% | — | sem_zona |
| 2026-10-18 08:05 | DOGE-USDT-SWAP | 0.07937 | 0.07953/0.07926 | 0.07898 | — | 0.00072 | 0.0086% | — | sem_zona |
| 2026-10-18 08:05 | ARB-USDT-SWAP | 0.18321 | 0.18468/0.18313 | 0.18182 | — | 0.00287 | -0.0035% | — | sem_zona |
| 2026-10-18 08:05 | WLD-USDT-SWAP | 0.50270 | 0.51110/0.50160 | 0.48870 | — | 0.00926 | -0.0126% | — | descartado_rr_baixo_setup_B |
| 2026-10-18 08:05 | SUI-USDT-SWAP | 0.98620 | 0.99060/0.98490 | 0.97880 | — | 0.01216 | 0.0071% | B/compra@0.99710 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-18 08:05 | UNI-USDT-SWAP | 7.2690 | 7.3220/7.2620 | 7.2320 | — | 0.08500 | 0.0026% | — | sem_zona |
| 2026-10-18 08:05 | LINK-USDT-SWAP | 12.01 | 12.05/11.98 | 11.98 | res 12.09 (ha 7 candles) | 0.10193 | 0.0052% | — | sem_zona |
| 2026-10-18 09:05 | BTC-USDT-SWAP | 82024.9 | 82110.0/81950.1 | 82024.9 | — | 245.99 | 0.0048% | A/compra@82049.5 (2t/0c) | zona_mapeada_setup_A |
| 2026-10-18 09:05 | ETH-USDT-SWAP | 2417.2 | 2420.9/2411.4 | 2417.2 | sup 2405.4 (ha 4 candles) | 11.86 | 0.0095% | — | sem_zona |
| 2026-10-18 09:05 | SOL-USDT-SWAP | 103.94 | 104.20/103.71 | 103.94 | sup 102.92 (ha 3 candles) | 0.70643 | 0.0040% | — | sem_zona |
| 2026-10-18 09:05 | XRP-USDT-SWAP | 1.2973 | 1.3010/1.2942 | 1.2973 | — | 0.00730 | 0.0006% | — | sem_zona |
| 2026-10-18 09:05 | DOGE-USDT-SWAP | 0.07940 | 0.07954/0.07913 | 0.07940 | sup 0.07873 (ha 3 candles) | 0.00050 | 0.0079% | — | sem_zona |
| 2026-10-18 09:05 | ARB-USDT-SWAP | 0.18269 | 0.18375/0.18195 | 0.18269 | res 0.18566 (ha 8 candles) | 0.00242 | -0.0012% | — | sem_zona |
| 2026-10-18 09:05 | WLD-USDT-SWAP | 0.49880 | 0.50430/0.49590 | 0.49880 | sup 0.48360 (ha 6 candles) | 0.00779 | -0.0030% | — | sem_zona |
| 2026-10-18 09:05 | SUI-USDT-SWAP | 0.98130 | 0.98640/0.97860 | 0.98130 | sup 0.97040 (ha 6 candles) | 0.00959 | 0.0080% | — | zona_expirada_setup_B |
| 2026-10-18 09:05 | UNI-USDT-SWAP | 7.2380 | 7.2820/7.2190 | 7.2380 | sup 7.1600 (ha 6 candles) | 0.07407 | 0.0028% | — | sem_zona |
| 2026-10-18 09:05 | LINK-USDT-SWAP | 12.02 | 12.03/11.97 | 12.02 | — | 0.07886 | 0.0079% | — | sem_zona |
| 2026-10-18 10:05 | BTC-USDT-SWAP | 81941.7 | 82083.9/81871.6 | 82024.9 | — | 238.01 | 0.0044% | — | invalidado_setup_A |
| 2026-10-18 10:05 | ETH-USDT-SWAP | 2416.9 | 2420.2/2412.1 | 2417.2 | sup 2405.4 (ha 5 candles) | 11.20 | 0.0091% | — | sem_zona |
| 2026-10-18 10:05 | SOL-USDT-SWAP | 104.00 | 104.26/103.86 | 103.94 | sup 102.92 (ha 4 candles) | 0.66000 | 0.0041% | — | sem_zona |
| 2026-10-18 10:05 | XRP-USDT-SWAP | 1.2960 | 1.2998/1.2936 | 1.2973 | — | 0.00714 | 0.0034% | — | sem_zona |
| 2026-10-18 10:05 | DOGE-USDT-SWAP | 0.07936 | 0.07965/0.07932 | 0.07940 | sup 0.07873 (ha 4 candles) | 0.00046 | 0.0049% | — | sem_zona |
| 2026-10-18 10:05 | ARB-USDT-SWAP | 0.18347 | 0.18374/0.18193 | 0.18269 | res 0.18566 (ha 9 candles) | 0.00235 | 0.0003% | — | sem_zona |
| 2026-10-18 10:05 | WLD-USDT-SWAP | 0.49650 | 0.50210/0.49360 | 0.49880 | sup 0.48360 (ha 7 candles) | 0.00781 | 0.0034% | — | sem_zona |
| 2026-10-18 10:05 | SUI-USDT-SWAP | 0.98210 | 0.98690/0.97970 | 0.98130 | sup 0.97040 (ha 7 candles) | 0.00933 | 0.0064% | — | sem_zona |
| 2026-10-18 10:05 | UNI-USDT-SWAP | 7.2620 | 7.2700/7.2070 | 7.2380 | sup 7.1600 (ha 7 candles) | 0.07371 | 0.0028% | — | sem_zona |
| 2026-10-18 10:05 | LINK-USDT-SWAP | 12.02 | 12.06/11.99 | 12.02 | — | 0.07721 | 0.0079% | — | sem_zona |
| 2026-10-18 11:05 | BTC-USDT-SWAP | 81504.8 | 81947.2/81278.8 | 82024.9 | — | 265.49 | 0.0050% | — | sem_zona |
| 2026-10-18 11:05 | ETH-USDT-SWAP | 2395.0 | 2416.9/2382.0 | 2417.2 | sup 2405.4 (ha 6 candles) | 12.73 | 0.0073% | A/venda@2405.4 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-18 11:05 | SOL-USDT-SWAP | 102.89 | 104.00/102.25 | 103.94 | sup 102.92 (ha 5 candles) | 0.72714 | 0.0029% | A/venda@102.92 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-18 11:05 | XRP-USDT-SWAP | 1.2818 | 1.2963/1.2759 | 1.2973 | — | 0.00799 | 0.0034% | B/compra@1.2826 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-18 11:05 | DOGE-USDT-SWAP | 0.07822 | 0.07937/0.07759 | 0.07940 | sup 0.07873 (ha 5 candles) | 0.00055 | 0.0021% | A/venda@0.07873 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-18 11:05 | ARB-USDT-SWAP | 0.18040 | 0.18354/0.17948 | 0.18269 | res 0.18468 (ha 3 candles) | 0.00250 | -0.0003% | B/compra@0.17900 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-18 11:05 | WLD-USDT-SWAP | 0.48450 | 0.49660/0.47880 | 0.49880 | sup 0.48360 (ha 8 candles) | 0.00865 | 0.0066% | — | sem_zona |
| 2026-10-18 11:05 | SUI-USDT-SWAP | 0.96790 | 0.98220/0.96230 | 0.98130 | sup 0.97040 (ha 8 candles) | 0.01007 | 0.0031% | A/venda@0.97040 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-18 11:05 | UNI-USDT-SWAP | 7.1260 | 7.2630/7.0900 | 7.2380 | sup 7.1600 (ha 8 candles) | 0.08150 | 0.0051% | A/venda@7.1600 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-18 11:06 | LINK-USDT-SWAP | 11.87 | 12.02/11.80 | 12.02 | — | 0.08729 | 0.0066% | B/compra@11.81 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-18 12:05 | BTC-USDT-SWAP | 81072.1 | 81529.3/81001.0 | 82024.9 | — | 289.02 | 0.0058% | B/compra@80961.3 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-18 12:05 | ETH-USDT-SWAP | 2375.9 | 2397.1/2366.7 | 2417.2 | sup 2405.4 (ha 7 candles) | 14.18 | 0.0055% | A/venda@2405.4 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-18 12:05 | SOL-USDT-SWAP | 102.07 | 103.00/101.82 | 103.94 | sup 102.92 (ha 6 candles) | 0.78786 | 0.0006% | — | descartado_rr_baixo_setup_A |
| 2026-10-18 12:05 | XRP-USDT-SWAP | 1.2748 | 1.2828/1.2710 | 1.2973 | — | 0.00836 | 0.0007% | — | invalidado_setup_B |
| 2026-10-18 12:05 | DOGE-USDT-SWAP | 0.07787 | 0.07834/0.07744 | 0.07940 | sup 0.07873 (ha 6 candles) | 0.00060 | 0.0006% | A/venda@0.07873 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-18 12:05 | ARB-USDT-SWAP | 0.17967 | 0.18080/0.17775 | 0.18269 | res 0.18468 (ha 4 candles) | 0.00263 | -0.0022% | B/compra@0.17900 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-18 12:05 | WLD-USDT-SWAP | 0.47780 | 0.48520/0.47430 | 0.49880 | sup 0.48360 (ha 9 candles) | 0.00909 | 0.0073% | A/venda@0.48360 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-18 12:05 | SUI-USDT-SWAP | 0.96030 | 0.96940/0.95270 | 0.98130 | sup 0.97040 (ha 9 candles) | 0.01085 | -0.0005% | A/venda@0.97040 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-18 12:05 | UNI-USDT-SWAP | 7.0250 | 7.1420/6.9910 | 7.2380 | sup 7.1600 (ha 9 candles) | 0.08807 | 0.0037% | — | descartado_rr_baixo_setup_A |
| 2026-10-18 12:05 | LINK-USDT-SWAP | 11.78 | 11.88/11.74 | 12.02 | — | 0.09364 | 0.0047% | — | invalidado_setup_B |
| 2026-10-18 13:05 | BTC-USDT-SWAP | 81135.5 | 81216.0/80958.0 | 81135.5 | — | 280.13 | 0.0063% | — | confirmado_calibracao_setup_B |
| 2026-10-18 13:05 | ETH-USDT-SWAP | 2378.2 | 2383.6/2370.3 | 2378.2 | sup 2405.4 (ha 8 candles) | 13.90 | 0.0039% | A/venda@2405.4 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-18 13:05 | SOL-USDT-SWAP | 102.16 | 102.46/101.67 | 102.16 | sup 102.92 (ha 7 candles) | 0.78357 | -0.0013% | — | sem_zona |
| 2026-10-18 13:05 | XRP-USDT-SWAP | 1.2730 | 1.2790/1.2680 | 1.2730 | — | 0.00854 | 0.0003% | — | sem_zona |
| 2026-10-18 13:05 | DOGE-USDT-SWAP | 0.07748 | 0.07816/0.07716 | 0.07748 | sup 0.07873 (ha 7 candles) | 0.00063 | 0.0013% | A/venda@0.07873 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-18 13:05 | ARB-USDT-SWAP | 0.17938 | 0.18048/0.17828 | 0.17938 | res 0.18468 (ha 5 candles) | 0.00258 | -0.0029% | B/compra@0.17900 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-18 13:05 | WLD-USDT-SWAP | 0.47630 | 0.48060/0.47210 | 0.47630 | sup 0.48360 (ha 10 candles) | 0.00924 | 0.0068% | A/venda@0.48360 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-18 13:05 | SUI-USDT-SWAP | 0.95970 | 0.96460/0.95360 | 0.95970 | sup 0.97040 (ha 10 candles) | 0.01071 | -0.0021% | A/venda@0.97040 (1t/1c) | zona_mapeada_setup_A |
| 2026-10-18 13:05 | UNI-USDT-SWAP | 6.9990 | 7.0600/6.9380 | 6.9990 | sup 7.1600 (ha 10 candles) | 0.08929 | 0.0035% | — | sem_zona |
| 2026-10-18 13:05 | LINK-USDT-SWAP | 11.77 | 11.82/11.70 | 11.77 | — | 0.09550 | 0.0027% | — | sem_zona |
| 2026-10-18 14:05 | BTC-USDT-SWAP | 81037.6 | 81230.0/80977.8 | 81135.5 | — | 279.74 | 0.0064% | — | sem_zona |
| 2026-10-18 14:05 | ETH-USDT-SWAP | 2365.5 | 2378.3/2360.3 | 2378.2 | sup 2405.4 (ha 9 candles) | 14.33 | 0.0053% | A/venda@2405.4 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-18 14:05 | SOL-USDT-SWAP | 102.02 | 102.16/101.72 | 102.16 | sup 102.92 (ha 8 candles) | 0.76571 | -0.0011% | — | sem_zona |
| 2026-10-18 14:05 | XRP-USDT-SWAP | 1.2707 | 1.2733/1.2682 | 1.2730 | — | 0.00851 | 0.0006% | — | sem_zona |
| 2026-10-18 14:05 | DOGE-USDT-SWAP | 0.07759 | 0.07773/0.07719 | 0.07748 | sup 0.07873 (ha 8 candles) | 0.00063 | 0.0055% | A/venda@0.07873 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-18 14:05 | ARB-USDT-SWAP | 0.18026 | 0.18043/0.17876 | 0.17938 | res 0.18468 (ha 6 candles) | 0.00259 | -0.0011% | — | descartado_rr_baixo_setup_B |
| 2026-10-18 14:05 | WLD-USDT-SWAP | 0.47660 | 0.47790/0.47360 | 0.47630 | sup 0.48360 (ha 11 candles) | 0.00924 | 0.0046% | A/venda@0.48360 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-18 14:05 | SUI-USDT-SWAP | 0.95840 | 0.96140/0.95430 | 0.95970 | sup 0.97040 (ha 11 candles) | 0.01057 | -0.0025% | A/venda@0.97040 (1t/2c) | zona_mapeada_setup_A |
| 2026-10-18 14:05 | UNI-USDT-SWAP | 6.9960 | 7.0180/6.9630 | 6.9990 | sup 7.1600 (ha 11 candles) | 0.08607 | 0.0045% | — | sem_zona |
| 2026-10-18 14:05 | LINK-USDT-SWAP | 11.75 | 11.77/11.71 | 11.77 | — | 0.09307 | 0.0007% | — | sem_zona |
| 2026-10-18 15:05 | BTC-USDT-SWAP | 81150.0 | 81191.1/81037.6 | 81135.5 | — | 267.81 | 0.0051% | — | sem_zona |
| 2026-10-18 15:05 | ETH-USDT-SWAP | 2369.0 | 2375.8/2365.1 | 2378.2 | sup 2405.4 (ha 10 candles) | 14.02 | 0.0055% | A/venda@2405.4 (0t/4c) | zona_mapeada_setup_A |
| 2026-10-18 15:05 | SOL-USDT-SWAP | 102.08 | 102.47/101.86 | 102.16 | sup 102.92 (ha 9 candles) | 0.73643 | -0.0012% | — | sem_zona |
| 2026-10-18 15:05 | XRP-USDT-SWAP | 1.2721 | 1.2758/1.2692 | 1.2730 | — | 0.00841 | 0.0005% | — | sem_zona |
| 2026-10-18 15:05 | DOGE-USDT-SWAP | 0.07775 | 0.07801/0.07758 | 0.07748 | sup 0.07873 (ha 9 candles) | 0.00062 | 0.0098% | A/venda@0.07873 (0t/4c) | zona_mapeada_setup_A |
| 2026-10-18 15:05 | ARB-USDT-SWAP | 0.17950 | 0.18141/0.17921 | 0.17938 | res 0.18468 (ha 7 candles) | 0.00249 | -0.0037% | — | sem_zona |
| 2026-10-18 15:05 | WLD-USDT-SWAP | 0.47220 | 0.48000/0.47160 | 0.47630 | sup 0.48360 (ha 12 candles) | 0.00938 | 0.0012% | A/venda@0.48360 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-18 15:06 | SUI-USDT-SWAP | 0.95940 | 0.96440/0.95750 | 0.95970 | sup 0.95270 (ha 3 candles) | 0.01016 | -0.0036% | A/venda@0.97040 (1t/3c) | zona_mapeada_setup_A |
| 2026-10-18 15:06 | UNI-USDT-SWAP | 6.9810 | 7.0400/6.9710 | 6.9990 | sup 7.1600 (ha 12 candles) | 0.08593 | 0.0040% | — | sem_zona |
| 2026-10-18 15:06 | LINK-USDT-SWAP | 11.77 | 11.81/11.74 | 11.77 | — | 0.09236 | -0.0006% | — | sem_zona |
| 2026-10-18 16:05 | BTC-USDT-SWAP | 81159.0 | 81246.3/81048.0 | 81135.5 | — | 270.14 | 0.0048% | — | sem_zona |
| 2026-10-18 16:05 | ETH-USDT-SWAP | 2367.3 | 2372.4/2360.4 | 2378.2 | sup 2405.4 (ha 11 candles) | 14.05 | 0.0070% | A/venda@2405.4 (0t/5c) | zona_mapeada_setup_A |
| 2026-10-18 16:05 | SOL-USDT-SWAP | 102.20 | 102.41/101.96 | 102.16 | sup 101.67 (ha 3 candles) | 0.71286 | 0.0001% | — | sem_zona |
| 2026-10-18 16:05 | XRP-USDT-SWAP | 1.2738 | 1.2756/1.2707 | 1.2730 | — | 0.00811 | 0.0023% | — | sem_zona |
| 2026-10-18 16:05 | DOGE-USDT-SWAP | 0.07765 | 0.07795/0.07749 | 0.07748 | sup 0.07716 (ha 3 candles) | 0.00062 | 0.0100% | A/venda@0.07873 (0t/5c) | zona_mapeada_setup_A |
| 2026-10-18 16:05 | ARB-USDT-SWAP | 0.17922 | 0.18014/0.17880 | 0.17938 | res 0.18468 (ha 8 candles) | 0.00231 | -0.0072% | — | sem_zona |
| 2026-10-18 16:05 | WLD-USDT-SWAP | 0.47030 | 0.47400/0.46660 | 0.47630 | sup 0.48360 (ha 13 candles) | 0.00941 | -0.0008% | A/venda@0.48360 (0t/4c) | zona_mapeada_setup_A |
| 2026-10-18 16:05 | SUI-USDT-SWAP | 0.96100 | 0.96300/0.95750 | 0.95970 | sup 0.95270 (ha 4 candles) | 0.00977 | -0.0036% | A/venda@0.97040 (1t/4c) | zona_mapeada_setup_A |
| 2026-10-18 16:06 | UNI-USDT-SWAP | 6.9600 | 7.0020/6.9530 | 6.9990 | sup 6.9380 (ha 3 candles) | 0.08400 | 0.0046% | — | sem_zona |
| 2026-10-18 16:06 | LINK-USDT-SWAP | 11.77 | 11.79/11.74 | 11.77 | — | 0.09050 | 0.0000% | — | sem_zona |
| 2026-10-18 17:05 | BTC-USDT-SWAP | 80844.0 | 81159.6/80755.0 | 80844.0 | — | 283.91 | 0.0047% | B/compra@80770.7 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-18 17:05 | ETH-USDT-SWAP | 2337.4 | 2369.0/2328.0 | 2337.4 | sup 2405.4 (ha 12 candles) | 16.20 | 0.0072% | A/venda@2405.4 (0t/6c) | zona_mapeada_setup_A |
| 2026-10-18 17:05 | SOL-USDT-SWAP | 100.77 | 102.31/100.34 | 100.77 | sup 101.67 (ha 4 candles) | 0.80500 | 0.0003% | A/venda@101.67 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-18 17:05 | XRP-USDT-SWAP | 1.2596 | 1.2765/1.2550 | 1.2596 | — | 0.00924 | 0.0012% | — | sem_zona |
| 2026-10-18 17:05 | DOGE-USDT-SWAP | 0.07633 | 0.07777/0.07603 | 0.07633 | sup 0.07716 (ha 4 candles) | 0.00070 | 0.0100% | A/venda@0.07873 (0t/6c) | zona_mapeada_setup_A |
| 2026-10-18 17:05 | ARB-USDT-SWAP | 0.17554 | 0.17976/0.17486 | 0.17554 | res 0.18468 (ha 9 candles) | 0.00249 | -0.0095% | B/compra@0.17409 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-18 17:05 | WLD-USDT-SWAP | 0.46230 | 0.47080/0.45940 | 0.46230 | sup 0.48360 (ha 14 candles) | 0.00973 | -0.0054% | A/venda@0.48360 (0t/5c) | zona_mapeada_setup_A |
| 2026-10-18 17:05 | SUI-USDT-SWAP | 0.94130 | 0.96230/0.93640 | 0.94130 | sup 0.95270 (ha 5 candles) | 0.01076 | -0.0036% | A/venda@0.97040 (1t/5c) | zona_mapeada_setup_A |
| 2026-10-18 17:05 | UNI-USDT-SWAP | 6.8130 | 6.9660/6.8030 | 6.8130 | sup 6.9380 (ha 4 candles) | 0.08914 | 0.0029% | A/venda@6.9380 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-18 17:05 | LINK-USDT-SWAP | 11.56 | 11.78/11.52 | 11.56 | — | 0.10286 | -0.0011% | — | sem_zona |
| 2026-10-18 18:05 | BTC-USDT-SWAP | 80933.7 | 80969.4/80621.4 | 80844.0 | — | 300.94 | 0.0057% | — | confirmado_calibracao_setup_B |
| 2026-10-18 18:05 | ETH-USDT-SWAP | 2350.1 | 2353.8/2333.3 | 2337.4 | sup 2405.4 (ha 13 candles) | 17.17 | 0.0066% | A/venda@2405.4 (0t/7c) | zona_mapeada_setup_A |
| 2026-10-18 18:05 | SOL-USDT-SWAP | 101.16 | 101.28/100.39 | 100.77 | sup 101.67 (ha 5 candles) | 0.83643 | 0.0014% | A/venda@101.67 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-18 18:05 | XRP-USDT-SWAP | 1.2634 | 1.2638/1.2562 | 1.2596 | — | 0.00933 | -0.0003% | — | sem_zona |
| 2026-10-18 18:05 | DOGE-USDT-SWAP | 0.07672 | 0.07672/0.07619 | 0.07633 | sup 0.07716 (ha 5 candles) | 0.00071 | 0.0100% | A/venda@0.07873 (0t/7c) | zona_mapeada_setup_A |
| 2026-10-18 18:05 | ARB-USDT-SWAP | 0.17680 | 0.17738/0.17537 | 0.17554 | res 0.18141 (ha 3 candles) | 0.00239 | -0.0120% | B/compra@0.17409 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-18 18:05 | WLD-USDT-SWAP | 0.46110 | 0.46730/0.45610 | 0.46230 | sup 0.48360 (ha 15 candles) | 0.00989 | -0.0084% | A/venda@0.48360 (0t/6c) | zona_mapeada_setup_A |
| 2026-10-18 18:05 | SUI-USDT-SWAP | 0.94690 | 0.94830/0.94060 | 0.94130 | sup 0.95270 (ha 6 candles) | 0.01055 | -0.0040% | A/venda@0.97040 (1t/6c) | zona_mapeada_setup_A |
| 2026-10-18 18:05 | UNI-USDT-SWAP | 6.8440 | 6.8770/6.8120 | 6.8130 | sup 6.9380 (ha 5 candles) | 0.08929 | 0.0017% | A/venda@6.9380 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-18 18:05 | LINK-USDT-SWAP | 11.64 | 11.64/11.54 | 11.56 | — | 0.10443 | -0.0019% | — | sem_zona |
| 2026-10-18 19:05 | BTC-USDT-SWAP | 81178.2 | 81214.0/80881.0 | 80844.0 | — | 313.66 | 0.0060% | B/compra@80961.3 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-18 19:05 | ETH-USDT-SWAP | 2369.8 | 2371.9/2349.8 | 2337.4 | sup 2405.4 (ha 14 candles) | 18.21 | 0.0068% | — | zona_expirada_setup_A |
| 2026-10-18 19:05 | SOL-USDT-SWAP | 102.05 | 102.11/101.01 | 100.77 | sup 101.67 (ha 6 candles) | 0.86714 | 0.0038% | — | invalidado_setup_A |
| 2026-10-18 19:05 | XRP-USDT-SWAP | 1.2747 | 1.2756/1.2632 | 1.2596 | — | 0.00976 | -0.0001% | — | sem_zona |
| 2026-10-18 19:05 | DOGE-USDT-SWAP | 0.07764 | 0.07770/0.07658 | 0.07633 | sup 0.07716 (ha 6 candles) | 0.00075 | 0.0100% | — | zona_expirada_setup_A |
| 2026-10-18 19:05 | ARB-USDT-SWAP | 0.17943 | 0.17969/0.17632 | 0.17554 | res 0.18141 (ha 4 candles) | 0.00248 | -0.0098% | B/compra@0.17409 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-18 19:05 | WLD-USDT-SWAP | 0.46640 | 0.46710/0.45920 | 0.46230 | sup 0.48360 (ha 16 candles) | 0.01004 | -0.0074% | A/venda@0.48360 (0t/7c) | zona_mapeada_setup_A |
| 2026-10-18 19:05 | SUI-USDT-SWAP | 0.95820 | 0.95910/0.94520 | 0.94130 | sup 0.95270 (ha 7 candles) | 0.01106 | -0.0027% | A/venda@0.97040 (1t/7c) | zona_mapeada_setup_A |
| 2026-10-18 19:05 | UNI-USDT-SWAP | 6.9570 | 6.9580/6.8430 | 6.8130 | sup 6.9380 (ha 6 candles) | 0.09371 | 0.0023% | A/venda@6.9380 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-18 19:06 | LINK-USDT-SWAP | 11.75 | 11.76/11.62 | 11.56 | — | 0.11000 | -0.0005% | — | sem_zona |
| 2026-10-18 20:05 | BTC-USDT-SWAP | 81727.5 | 81804.2/81178.1 | 80844.0 | — | 349.32 | 0.0068% | B/compra@80961.3 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-18 20:05 | ETH-USDT-SWAP | 2394.8 | 2398.0/2369.7 | 2337.4 | sup 2328.0 (ha 3 candles) | 19.72 | 0.0079% | — | sem_zona |
| 2026-10-18 20:05 | SOL-USDT-SWAP | 103.86 | 103.89/102.03 | 100.77 | sup 100.34 (ha 3 candles) | 0.97071 | 0.0062% | — | sem_zona |
| 2026-10-18 20:05 | XRP-USDT-SWAP | 1.3011 | 1.3025/1.2746 | 1.2596 | — | 0.01134 | 0.0005% | — | sem_zona |
| 2026-10-18 20:05 | DOGE-USDT-SWAP | 0.07917 | 0.07922/0.07762 | 0.07633 | sup 0.07603 (ha 3 candles) | 0.00085 | 0.0100% | — | sem_zona |
| 2026-10-18 20:05 | ARB-USDT-SWAP | 0.18422 | 0.18449/0.17939 | 0.17554 | res 0.18141 (ha 5 candles) | 0.00275 | -0.0086% | B/compra@0.17409 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-18 20:05 | WLD-USDT-SWAP | 0.48160 | 0.48290/0.46620 | 0.46230 | sup 0.48360 (ha 17 candles) | 0.01086 | -0.0098% | A/venda@0.48360 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-18 20:05 | SUI-USDT-SWAP | 0.98530 | 0.98580/0.95790 | 0.94130 | sup 0.93640 (ha 3 candles) | 0.01264 | -0.0037% | — | invalidado_setup_A |
| 2026-10-18 20:05 | UNI-USDT-SWAP | 7.1560 | 7.1810/6.9560 | 6.8130 | sup 6.8030 (ha 3 candles) | 0.10650 | 0.0016% | — | invalidado_setup_A |
| 2026-10-18 20:05 | LINK-USDT-SWAP | 11.98 | 11.99/11.75 | 11.56 | — | 0.12279 | 0.0005% | B/compra@12.06 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-18 21:05 | BTC-USDT-SWAP | 82069.5 | 82184.1/81659.6 | 82069.5 | sup 80621.4 (ha 3 candles) | 345.76 | 0.0068% | B/compra@80961.3 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-18 21:05 | ETH-USDT-SWAP | 2409.4 | 2413.7/2386.8 | 2409.4 | sup 2328.0 (ha 4 candles) | 20.27 | 0.0087% | — | sem_zona |
| 2026-10-18 21:05 | SOL-USDT-SWAP | 104.06 | 104.28/103.34 | 104.06 | sup 100.34 (ha 4 candles) | 0.95357 | 0.0065% | — | sem_zona |
| 2026-10-18 21:05 | XRP-USDT-SWAP | 1.3064 | 1.3094/1.2959 | 1.3064 | — | 0.01146 | 0.0016% | B/compra@1.3102 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-18 21:05 | DOGE-USDT-SWAP | 0.07941 | 0.07961/0.07886 | 0.07941 | sup 0.07603 (ha 4 candles) | 0.00085 | 0.0100% | — | sem_zona |
| 2026-10-18 21:05 | ARB-USDT-SWAP | 0.18691 | 0.18739/0.18345 | 0.18691 | res 0.18141 (ha 6 candles) | 0.00279 | -0.0046% | B/compra@0.17409 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-18 21:05 | WLD-USDT-SWAP | 0.48870 | 0.49020/0.48010 | 0.48870 | sup 0.45610 (ha 3 candles) | 0.01007 | -0.0096% | — | invalidado_setup_A |
| 2026-10-18 21:05 | SUI-USDT-SWAP | 0.99630 | 0.99870/0.98340 | 0.99630 | sup 0.93640 (ha 4 candles) | 0.01275 | -0.0041% | — | sem_zona |
| 2026-10-18 21:05 | UNI-USDT-SWAP | 7.1950 | 7.2080/7.1300 | 7.1950 | sup 6.8030 (ha 4 candles) | 0.10364 | 0.0049% | — | sem_zona |
| 2026-10-18 21:05 | LINK-USDT-SWAP | 12.03 | 12.06/11.94 | 12.03 | — | 0.12286 | 0.0011% | — | descartado_rr_baixo_setup_B |
| 2026-10-18 22:05 | BTC-USDT-SWAP | 82263.0 | 82508.2/81957.6 | 82069.5 | sup 80621.4 (ha 4 candles) | 372.69 | 0.0064% | B/compra@80961.3 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-18 22:05 | ETH-USDT-SWAP | 2413.0 | 2418.7/2402.2 | 2409.4 | sup 2328.0 (ha 5 candles) | 20.88 | 0.0088% | — | sem_zona |
| 2026-10-18 22:05 | SOL-USDT-SWAP | 104.21 | 104.57/103.71 | 104.06 | sup 100.34 (ha 5 candles) | 0.98071 | 0.0048% | — | sem_zona |
| 2026-10-18 22:05 | XRP-USDT-SWAP | 1.3056 | 1.3098/1.3011 | 1.3064 | — | 0.01174 | 0.0035% | — | invalidado_setup_B |
| 2026-10-18 22:05 | DOGE-USDT-SWAP | 0.07937 | 0.07966/0.07909 | 0.07941 | sup 0.07603 (ha 5 candles) | 0.00087 | 0.0098% | — | sem_zona |
| 2026-10-18 22:05 | ARB-USDT-SWAP | 0.18614 | 0.18783/0.18461 | 0.18691 | res 0.18141 (ha 7 candles) | 0.00290 | -0.0021% | B/compra@0.17409 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-18 22:05 | WLD-USDT-SWAP | 0.48400 | 0.49080/0.48370 | 0.48870 | sup 0.45610 (ha 4 candles) | 0.00990 | -0.0046% | — | sem_zona |
| 2026-10-18 22:05 | SUI-USDT-SWAP | 0.99660 | 1.0039/0.98850 | 0.99630 | sup 0.93640 (ha 5 candles) | 0.01344 | -0.0032% | — | sem_zona |
| 2026-10-18 22:05 | UNI-USDT-SWAP | 7.1880 | 7.2420/7.1370 | 7.1950 | sup 6.8030 (ha 5 candles) | 0.10686 | 0.0063% | — | sem_zona |
| 2026-10-18 22:05 | LINK-USDT-SWAP | 12.07 | 12.13/12.00 | 12.03 | — | 0.12743 | -0.0023% | B/compra@12.15 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-18 23:05 | BTC-USDT-SWAP | 82404.7 | 82532.0/82242.9 | 82069.5 | sup 80621.4 (ha 5 candles) | 381.92 | 0.0058% | B/compra@80961.3 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-18 23:05 | ETH-USDT-SWAP | 2423.4 | 2428.0/2412.6 | 2409.4 | sup 2328.0 (ha 6 candles) | 21.29 | 0.0095% | — | sem_zona |
| 2026-10-18 23:05 | SOL-USDT-SWAP | 104.83 | 104.95/104.21 | 104.06 | sup 100.34 (ha 6 candles) | 0.99857 | 0.0047% | B/venda@105.22 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-18 23:05 | XRP-USDT-SWAP | 1.3107 | 1.3131/1.3046 | 1.3064 | — | 0.01186 | 0.0046% | B/compra@1.3176 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-18 23:05 | DOGE-USDT-SWAP | 0.07974 | 0.07987/0.07931 | 0.07941 | sup 0.07603 (ha 6 candles) | 0.00088 | 0.0066% | — | sem_zona |
| 2026-10-18 23:05 | ARB-USDT-SWAP | 0.19000 | 0.19046/0.18581 | 0.18691 | res 0.18141 (ha 8 candles) | 0.00311 | -0.0006% | B/compra@0.17409 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-18 23:05 | WLD-USDT-SWAP | 0.48880 | 0.49050/0.48230 | 0.48870 | sup 0.45610 (ha 5 candles) | 0.00989 | 0.0003% | — | sem_zona |
| 2026-10-18 23:05 | SUI-USDT-SWAP | 1.0002 | 1.0023/0.99510 | 0.99630 | sup 0.93640 (ha 6 candles) | 0.01340 | -0.0015% | — | sem_zona |
| 2026-10-18 23:05 | UNI-USDT-SWAP | 7.2700 | 7.2920/7.1790 | 7.1950 | sup 6.8030 (ha 6 candles) | 0.11043 | 0.0070% | — | sem_zona |
| 2026-10-18 23:05 | LINK-USDT-SWAP | 12.17 | 12.17/12.07 | 12.03 | — | 0.13036 | -0.0032% | — | descartado_rr_baixo_setup_B |
| 2026-10-19 00:05 | BTC-USDT-SWAP | 82677.0 | 82777.0/82306.9 | 82069.5 | sup 80621.4 (ha 6 candles) | 400.34 | 0.0050% | B/compra@80961.3 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-19 00:05 | ETH-USDT-SWAP | 2425.7 | 2437.8/2415.1 | 2409.4 | sup 2328.0 (ha 7 candles) | 22.33 | 0.0099% | — | sem_zona |
| 2026-10-19 00:05 | SOL-USDT-SWAP | 105.44 | 105.86/104.76 | 104.06 | sup 100.34 (ha 7 candles) | 1.0486 | 0.0029% | B/venda@105.22 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-19 00:05 | XRP-USDT-SWAP | 1.3123 | 1.3161/1.3062 | 1.3064 | — | 0.01213 | 0.0064% | — | invalidado_setup_B |
| 2026-10-19 00:05 | DOGE-USDT-SWAP | 0.08001 | 0.08025/0.07946 | 0.07941 | sup 0.07603 (ha 7 candles) | 0.00091 | 0.0025% | — | sem_zona |
| 2026-10-19 00:05 | ARB-USDT-SWAP | 0.19220 | 0.19300/0.18883 | 0.18691 | res 0.18141 (ha 9 candles) | 0.00328 | -0.0006% | B/compra@0.17409 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-19 00:05 | WLD-USDT-SWAP | 0.49230 | 0.49510/0.48590 | 0.48870 | sup 0.45610 (ha 6 candles) | 0.00994 | 0.0051% | — | sem_zona |
| 2026-10-19 00:05 | SUI-USDT-SWAP | 1.0071 | 1.0109/0.99640 | 0.99630 | sup 0.93640 (ha 7 candles) | 0.01392 | 0.0001% | — | sem_zona |
| 2026-10-19 00:05 | UNI-USDT-SWAP | 7.2910 | 7.3250/7.2210 | 7.1950 | sup 6.8030 (ha 7 candles) | 0.11336 | 0.0083% | B/venda@7.3540 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 00:05 | LINK-USDT-SWAP | 12.21 | 12.26/12.13 | 12.03 | — | 0.13521 | -0.0015% | B/compra@12.25 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 01:05 | BTC-USDT-SWAP | 82475.8 | 82688.0/82429.6 | 82475.8 | sup 80621.4 (ha 7 candles) | 371.05 | 0.0038% | B/compra@80961.3 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-19 01:05 | ETH-USDT-SWAP | 2423.2 | 2428.6/2420.3 | 2423.2 | sup 2328.0 (ha 8 candles) | 20.43 | 0.0091% | — | sem_zona |
| 2026-10-19 01:05 | SOL-USDT-SWAP | 105.19 | 105.49/105.07 | 105.19 | sup 100.34 (ha 8 candles) | 0.95357 | 0.0018% | — | descartado_rr_baixo_setup_B |
| 2026-10-19 01:05 | XRP-USDT-SWAP | 1.3096 | 1.3130/1.3082 | 1.3096 | — | 0.01101 | 0.0066% | B/compra@1.3102 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 01:05 | DOGE-USDT-SWAP | 0.07961 | 0.08003/0.07954 | 0.07961 | sup 0.07603 (ha 8 candles) | 0.00082 | 0.0003% | — | sem_zona |
| 2026-10-19 01:05 | ARB-USDT-SWAP | 0.19274 | 0.19275/0.18987 | 0.19274 | res 0.18141 (ha 10 candles) | 0.00319 | -0.0014% | — | zona_expirada_setup_B |
| 2026-10-19 01:05 | WLD-USDT-SWAP | 0.49150 | 0.49340/0.48940 | 0.49150 | sup 0.45610 (ha 7 candles) | 0.00895 | 0.0086% | — | sem_zona |
| 2026-10-19 01:05 | SUI-USDT-SWAP | 1.0008 | 1.0076/0.99930 | 1.0008 | sup 0.93640 (ha 8 candles) | 0.01309 | -0.0011% | — | sem_zona |
| 2026-10-19 01:05 | UNI-USDT-SWAP | 7.2930 | 7.3240/7.2680 | 7.2930 | sup 6.8030 (ha 8 candles) | 0.10500 | 0.0048% | B/venda@7.3540 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-19 01:05 | LINK-USDT-SWAP | 12.17 | 12.22/12.17 | 12.17 | — | 0.12300 | 0.0011% | — | invalidado_setup_B |
| 2026-10-19 02:05 | BTC-USDT-SWAP | 82740.6 | 82846.5/82438.6 | 82475.8 | sup 80621.4 (ha 8 candles) | 362.45 | 0.0034% | B/compra@80961.3 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-19 02:05 | ETH-USDT-SWAP | 2427.9 | 2432.6/2419.1 | 2423.2 | sup 2328.0 (ha 9 candles) | 19.22 | 0.0088% | B/venda@2441.4 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 02:05 | SOL-USDT-SWAP | 105.63 | 105.95/105.04 | 105.19 | sup 100.34 (ha 9 candles) | 0.93429 | 0.0027% | — | sem_zona |
| 2026-10-19 02:05 | XRP-USDT-SWAP | 1.3125 | 1.3159/1.3086 | 1.3096 | — | 0.01069 | 0.0071% | B/compra@1.3102 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-19 02:05 | DOGE-USDT-SWAP | 0.07962 | 0.07996/0.07936 | 0.07961 | sup 0.07603 (ha 9 candles) | 0.00080 | 0.0026% | — | sem_zona |
| 2026-10-19 02:05 | ARB-USDT-SWAP | 0.19271 | 0.19431/0.19155 | 0.19274 | res 0.18141 (ha 11 candles) | 0.00317 | 0.0004% | A/compra@0.18141 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-19 02:05 | WLD-USDT-SWAP | 0.49450 | 0.49660/0.48920 | 0.49150 | sup 0.45610 (ha 8 candles) | 0.00870 | 0.0100% | — | sem_zona |
| 2026-10-19 02:05 | SUI-USDT-SWAP | 1.0071 | 1.0116/0.99720 | 1.0008 | sup 0.93640 (ha 9 candles) | 0.01293 | -0.0001% | — | sem_zona |
| 2026-10-19 02:05 | UNI-USDT-SWAP | 7.3670 | 7.4190/7.2760 | 7.2930 | sup 6.8030 (ha 9 candles) | 0.10443 | 0.0033% | B/venda@7.3540 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-19 02:06 | LINK-USDT-SWAP | 12.16 | 12.18/12.10 | 12.17 | — | 0.11886 | 0.0039% | B/compra@12.15 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 03:05 | BTC-USDT-SWAP | 82725.6 | 82749.8/82500.2 | 82475.8 | sup 80621.4 (ha 9 candles) | 361.85 | 0.0037% | — | zona_expirada_setup_B |
| 2026-10-19 03:05 | ETH-USDT-SWAP | 2430.6 | 2430.6/2420.2 | 2423.2 | sup 2328.0 (ha 10 candles) | 19.01 | 0.0089% | B/venda@2441.4 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-19 03:05 | SOL-USDT-SWAP | 105.64 | 105.79/105.19 | 105.19 | sup 100.34 (ha 10 candles) | 0.92071 | 0.0024% | — | sem_zona |
| 2026-10-19 03:05 | XRP-USDT-SWAP | 1.3128 | 1.3128/1.3076 | 1.3096 | — | 0.01028 | 0.0065% | — | descartado_rr_baixo_setup_B |
| 2026-10-19 03:05 | DOGE-USDT-SWAP | 0.07967 | 0.07967/0.07925 | 0.07961 | sup 0.07603 (ha 10 candles) | 0.00076 | 0.0055% | — | sem_zona |
| 2026-10-19 03:05 | ARB-USDT-SWAP | 0.19352 | 0.19421/0.19167 | 0.19274 | res 0.18141 (ha 12 candles) | 0.00320 | 0.0023% | A/compra@0.18141 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-19 03:05 | WLD-USDT-SWAP | 0.49560 | 0.49760/0.49050 | 0.49150 | sup 0.45610 (ha 9 candles) | 0.00860 | 0.0100% | — | sem_zona |
| 2026-10-19 03:05 | SUI-USDT-SWAP | 1.0095 | 1.0117/1.0006 | 1.0008 | sup 0.93640 (ha 10 candles) | 0.01294 | 0.0021% | — | sem_zona |
| 2026-10-19 03:05 | UNI-USDT-SWAP | 7.3860 | 7.4190/7.3290 | 7.2930 | sup 6.8030 (ha 10 candles) | 0.10214 | 0.0035% | — | invalidado_setup_B |
| 2026-10-19 03:05 | LINK-USDT-SWAP | 12.16 | 12.18/12.08 | 12.17 | — | 0.11771 | 0.0077% | — | descartado_rr_baixo_setup_B |
| 2026-10-19 04:05 | BTC-USDT-SWAP | 82808.5 | 82897.1/82646.2 | 82475.8 | sup 80621.4 (ha 10 candles) | 361.76 | 0.0044% | B/venda@82898.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 04:05 | ETH-USDT-SWAP | 2429.4 | 2435.6/2427.6 | 2423.2 | sup 2328.0 (ha 11 candles) | 18.30 | 0.0076% | B/venda@2441.4 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-19 04:05 | SOL-USDT-SWAP | 105.69 | 105.87/105.47 | 105.19 | sup 100.34 (ha 11 candles) | 0.91786 | 0.0023% | — | sem_zona |
| 2026-10-19 04:05 | XRP-USDT-SWAP | 1.3139 | 1.3152/1.3112 | 1.3096 | — | 0.01020 | 0.0066% | B/compra@1.3176 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 04:05 | DOGE-USDT-SWAP | 0.07980 | 0.07984/0.07953 | 0.07961 | sup 0.07603 (ha 11 candles) | 0.00074 | 0.0086% | — | sem_zona |
| 2026-10-19 04:05 | ARB-USDT-SWAP | 0.19549 | 0.19872/0.19338 | 0.19274 | res 0.18141 (ha 13 candles) | 0.00346 | 0.0015% | A/compra@0.18141 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-19 04:05 | WLD-USDT-SWAP | 0.49580 | 0.49870/0.49370 | 0.49150 | sup 0.45610 (ha 10 candles) | 0.00865 | 0.0083% | — | sem_zona |
| 2026-10-19 04:05 | SUI-USDT-SWAP | 1.0088 | 1.0115/1.0074 | 1.0008 | sup 0.93640 (ha 11 candles) | 0.01272 | 0.0035% | — | sem_zona |
| 2026-10-19 04:05 | UNI-USDT-SWAP | 7.3880 | 7.4050/7.3460 | 7.2930 | sup 6.8030 (ha 11 candles) | 0.10243 | 0.0039% | B/venda@7.4530 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 04:05 | LINK-USDT-SWAP | 12.20 | 12.21/12.13 | 12.17 | — | 0.11929 | 0.0097% | B/compra@12.25 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 05:05 | BTC-USDT-SWAP | 82690.5 | 83149.8/82639.3 | 82690.5 | sup 80621.4 (ha 11 candles) | 387.26 | 0.0061% | — | descartado_rr_baixo_setup_B |
| 2026-10-19 05:05 | ETH-USDT-SWAP | 2429.3 | 2446.0/2428.3 | 2429.3 | sup 2328.0 (ha 12 candles) | 18.80 | 0.0063% | — | descartado_rr_baixo_setup_B |
| 2026-10-19 05:05 | SOL-USDT-SWAP | 105.59 | 106.18/105.53 | 105.59 | sup 100.34 (ha 12 candles) | 0.92071 | 0.0029% | — | sem_zona |
| 2026-10-19 05:05 | XRP-USDT-SWAP | 1.3129 | 1.3212/1.3127 | 1.3129 | — | 0.01034 | 0.0062% | — | invalidado_setup_B |
| 2026-10-19 05:05 | DOGE-USDT-SWAP | 0.07973 | 0.08016/0.07969 | 0.07973 | sup 0.07603 (ha 12 candles) | 0.00074 | 0.0097% | — | sem_zona |
| 2026-10-19 05:05 | ARB-USDT-SWAP | 0.19800 | 0.19868/0.19544 | 0.19800 | — | 0.00353 | 0.0020% | A/compra@0.18141 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-19 05:05 | WLD-USDT-SWAP | 0.50740 | 0.51050/0.49550 | 0.50740 | sup 0.45610 (ha 11 candles) | 0.00912 | 0.0081% | B/venda@0.51160 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 05:05 | SUI-USDT-SWAP | 1.0119 | 1.0171/1.0087 | 1.0119 | sup 0.93640 (ha 12 candles) | 0.01283 | 0.0026% | — | sem_zona |
| 2026-10-19 05:05 | UNI-USDT-SWAP | 7.4370 | 7.4830/7.3860 | 7.4370 | sup 6.8030 (ha 12 candles) | 0.10443 | -0.0004% | B/venda@7.4530 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-19 05:05 | LINK-USDT-SWAP | 12.19 | 12.26/12.18 | 12.19 | — | 0.11986 | 0.0077% | — | invalidado_setup_B |
| 2026-10-19 06:05 | BTC-USDT-SWAP | 82788.1 | 82940.0/82550.0 | 82690.5 | sup 80621.4 (ha 12 candles) | 400.95 | 0.0084% | B/venda@82624.9 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 06:05 | ETH-USDT-SWAP | 2434.3 | 2439.0/2425.8 | 2429.3 | sup 2328.0 (ha 13 candles) | 18.89 | 0.0055% | — | sem_zona |
| 2026-10-19 06:05 | SOL-USDT-SWAP | 105.63 | 105.93/105.38 | 105.59 | sup 100.34 (ha 13 candles) | 0.92786 | 0.0036% | — | sem_zona |
| 2026-10-19 06:05 | XRP-USDT-SWAP | 1.3139 | 1.3165/1.3098 | 1.3129 | — | 0.01046 | 0.0057% | B/compra@1.3102 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 06:05 | DOGE-USDT-SWAP | 0.07973 | 0.07992/0.07943 | 0.07973 | sup 0.07925 (ha 3 candles) | 0.00075 | 0.0100% | — | sem_zona |
| 2026-10-19 06:05 | ARB-USDT-SWAP | 0.19838 | 0.20020/0.19764 | 0.19800 | — | 0.00362 | 0.0002% | A/compra@0.18141 (0t/4c) | zona_mapeada_setup_A |
| 2026-10-19 06:05 | WLD-USDT-SWAP | 0.50620 | 0.51140/0.50230 | 0.50740 | sup 0.45610 (ha 12 candles) | 0.00924 | 0.0100% | B/venda@0.51160 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-19 06:05 | SUI-USDT-SWAP | 1.0067 | 1.0138/1.0055 | 1.0119 | sup 0.93640 (ha 13 candles) | 0.01303 | 0.0049% | — | sem_zona |
| 2026-10-19 06:05 | UNI-USDT-SWAP | 7.4040 | 7.4460/7.3830 | 7.4370 | sup 6.8030 (ha 13 candles) | 0.10543 | -0.0007% | — | descartado_rr_baixo_setup_B |
| 2026-10-19 06:05 | LINK-USDT-SWAP | 12.16 | 12.21/12.15 | 12.19 | — | 0.12000 | 0.0091% | B/compra@12.15 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 07:05 | BTC-USDT-SWAP | 82733.0 | 83067.4/82702.2 | 82690.5 | sup 80621.4 (ha 13 candles) | 398.14 | 0.0099% | — | invalidado_setup_B |
| 2026-10-19 07:05 | ETH-USDT-SWAP | 2436.1 | 2445.4/2431.0 | 2429.3 | sup 2328.0 (ha 14 candles) | 16.99 | 0.0046% | — | sem_zona |
| 2026-10-19 07:05 | SOL-USDT-SWAP | 105.41 | 105.91/105.38 | 105.59 | sup 100.34 (ha 14 candles) | 0.82500 | 0.0035% | — | sem_zona |
| 2026-10-19 07:05 | XRP-USDT-SWAP | 1.3125 | 1.3170/1.3118 | 1.3129 | — | 0.00930 | 0.0052% | B/compra@1.3102 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-19 07:05 | DOGE-USDT-SWAP | 0.07969 | 0.07999/0.07960 | 0.07973 | sup 0.07925 (ha 4 candles) | 0.00065 | 0.0100% | — | sem_zona |
| 2026-10-19 07:05 | ARB-USDT-SWAP | 0.19755 | 0.19965/0.19728 | 0.19800 | — | 0.00344 | 0.0017% | A/compra@0.18141 (0t/5c) | zona_mapeada_setup_A |
| 2026-10-19 07:05 | WLD-USDT-SWAP | 0.50270 | 0.50890/0.50220 | 0.50740 | sup 0.45610 (ha 13 candles) | 0.00891 | 0.0100% | B/venda@0.51160 (1t/1c) | zona_mapeada_setup_B |
| 2026-10-19 07:05 | SUI-USDT-SWAP | 1.0049 | 1.0121/1.0041 | 1.0119 | sup 0.93640 (ha 14 candles) | 0.01175 | 0.0073% | — | sem_zona |
| 2026-10-19 07:05 | UNI-USDT-SWAP | 7.3920 | 7.4340/7.3810 | 7.4370 | sup 6.8030 (ha 14 candles) | 0.09757 | -0.0004% | B/venda@7.3540 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 07:05 | LINK-USDT-SWAP | 12.13 | 12.19/12.13 | 12.19 | — | 0.10571 | 0.0099% | B/compra@12.15 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-19 08:05 | BTC-USDT-SWAP | 82390.6 | 82872.8/82083.0 | 82690.5 | sup 80621.4 (ha 14 candles) | 429.69 | 0.0100% | — | sem_zona |
| 2026-10-19 08:05 | ETH-USDT-SWAP | 2425.3 | 2438.1/2414.0 | 2429.3 | sup 2328.0 (ha 15 candles) | 17.25 | 0.0053% | — | sem_zona |
| 2026-10-19 08:05 | SOL-USDT-SWAP | 104.93 | 105.59/104.38 | 105.59 | sup 100.34 (ha 15 candles) | 0.84786 | 0.0050% | — | sem_zona |
| 2026-10-19 08:05 | XRP-USDT-SWAP | 1.3041 | 1.3138/1.2985 | 1.3129 | — | 0.00985 | 0.0039% | — | invalidado_setup_B |
| 2026-10-19 08:05 | DOGE-USDT-SWAP | 0.07919 | 0.07978/0.07874 | 0.07973 | sup 0.07925 (ha 5 candles) | 0.00069 | 0.0097% | A/venda@0.07925 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-19 08:05 | ARB-USDT-SWAP | 0.19615 | 0.19813/0.19500 | 0.19800 | — | 0.00352 | 0.0069% | A/compra@0.18141 (0t/6c) | zona_mapeada_setup_A |
| 2026-10-19 08:05 | WLD-USDT-SWAP | 0.49880 | 0.50640/0.49330 | 0.50740 | sup 0.45610 (ha 14 candles) | 0.00904 | 0.0100% | B/venda@0.51160 (1t/2c) | zona_mapeada_setup_B |
| 2026-10-19 08:05 | SUI-USDT-SWAP | 0.99870 | 1.0072/0.99100 | 1.0119 | sup 0.93640 (ha 15 candles) | 0.01236 | 0.0094% | — | sem_zona |
| 2026-10-19 08:05 | UNI-USDT-SWAP | 7.3650 | 7.3990/7.3000 | 7.4370 | sup 6.8030 (ha 15 candles) | 0.10000 | 0.0028% | B/venda@7.3540 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-19 08:05 | LINK-USDT-SWAP | 12.07 | 12.16/12.02 | 12.19 | — | 0.10850 | 0.0099% | — | invalidado_setup_B |
| 2026-10-19 09:05 | BTC-USDT-SWAP | 82331.9 | 82390.6/82104.8 | 82331.9 | sup 80621.4 (ha 15 candles) | 426.32 | 0.0100% | — | sem_zona |
| 2026-10-19 09:05 | ETH-USDT-SWAP | 2418.9 | 2425.3/2411.0 | 2418.9 | sup 2328.0 (ha 16 candles) | 16.69 | 0.0061% | — | sem_zona |
| 2026-10-19 09:05 | SOL-USDT-SWAP | 104.64 | 104.93/104.31 | 104.64 | sup 100.34 (ha 16 candles) | 0.81357 | 0.0068% | B/venda@105.22 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 09:05 | XRP-USDT-SWAP | 1.3028 | 1.3046/1.2974 | 1.3028 | — | 0.00948 | 0.0027% | — | sem_zona |
| 2026-10-19 09:05 | DOGE-USDT-SWAP | 0.07910 | 0.07920/0.07868 | 0.07910 | sup 0.07925 (ha 6 candles) | 0.00064 | 0.0086% | A/venda@0.07925 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-19 09:05 | ARB-USDT-SWAP | 0.19529 | 0.19633/0.19440 | 0.19529 | — | 0.00342 | 0.0086% | A/compra@0.18141 (0t/7c) | zona_mapeada_setup_A |
| 2026-10-19 09:05 | WLD-USDT-SWAP | 0.49810 | 0.50060/0.49560 | 0.49810 | sup 0.45610 (ha 15 candles) | 0.00884 | 0.0100% | B/venda@0.51160 (1t/3c) | zona_mapeada_setup_B |
| 2026-10-19 09:05 | SUI-USDT-SWAP | 0.99550 | 0.99860/0.99070 | 0.99550 | sup 0.93640 (ha 16 candles) | 0.01194 | 0.0100% | — | sem_zona |
| 2026-10-19 09:05 | UNI-USDT-SWAP | 7.3420 | 7.3810/7.3080 | 7.3420 | sup 6.8030 (ha 16 candles) | 0.09700 | 0.0062% | B/venda@7.3540 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-19 09:05 | LINK-USDT-SWAP | 12.02 | 12.07/11.98 | 12.02 | — | 0.10464 | 0.0100% | B/compra@12.06 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 10:05 | BTC-USDT-SWAP | 82568.8 | 82665.6/82300.0 | 82331.9 | sup 80621.4 (ha 16 candles) | 407.71 | 0.0100% | — | sem_zona |
| 2026-10-19 10:05 | ETH-USDT-SWAP | 2422.8 | 2428.4/2417.5 | 2418.9 | sup 2328.0 (ha 17 candles) | 15.44 | 0.0063% | — | sem_zona |
| 2026-10-19 10:05 | SOL-USDT-SWAP | 105.25 | 105.50/104.57 | 104.64 | sup 100.34 (ha 17 candles) | 0.74714 | 0.0085% | B/venda@105.22 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-19 10:05 | XRP-USDT-SWAP | 1.3101 | 1.3119/1.3016 | 1.3028 | — | 0.00822 | 0.0015% | — | sem_zona |
| 2026-10-19 10:05 | DOGE-USDT-SWAP | 0.07977 | 0.07989/0.07903 | 0.07910 | sup 0.07925 (ha 7 candles) | 0.00059 | 0.0043% | — | invalidado_setup_A |
| 2026-10-19 10:05 | ARB-USDT-SWAP | 0.19750 | 0.19988/0.19511 | 0.19529 | — | 0.00339 | 0.0047% | — | zona_expirada_setup_A |
| 2026-10-19 10:05 | WLD-USDT-SWAP | 0.50670 | 0.51480/0.49750 | 0.49810 | sup 0.45610 (ha 16 candles) | 0.00888 | 0.0100% | B/venda@0.51160 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-19 10:05 | SUI-USDT-SWAP | 1.0045 | 1.0056/0.99430 | 0.99550 | sup 0.93640 (ha 17 candles) | 0.01075 | 0.0100% | — | sem_zona |
| 2026-10-19 10:05 | UNI-USDT-SWAP | 7.3800 | 7.4190/7.3320 | 7.3420 | sup 6.8030 (ha 17 candles) | 0.08714 | 0.0086% | — | invalidado_setup_B |
| 2026-10-19 10:05 | LINK-USDT-SWAP | 12.11 | 12.13/12.01 | 12.02 | — | 0.09636 | 0.0093% | — | descartado_rr_baixo_setup_B |
| 2026-10-19 11:05 | BTC-USDT-SWAP | 82089.0 | 82733.4/82014.4 | 82331.9 | sup 80621.4 (ha 17 candles) | 421.61 | 0.0100% | — | sem_zona |
| 2026-10-19 11:05 | ETH-USDT-SWAP | 2399.4 | 2429.0/2395.0 | 2418.9 | sup 2328.0 (ha 18 candles) | 15.95 | 0.0063% | — | sem_zona |
| 2026-10-19 11:05 | SOL-USDT-SWAP | 104.25 | 105.57/104.09 | 104.64 | sup 100.34 (ha 18 candles) | 0.78571 | 0.0097% | — | descartado_rr_baixo_setup_B |
| 2026-10-19 11:05 | XRP-USDT-SWAP | 1.3011 | 1.3146/1.2994 | 1.3028 | — | 0.00834 | 0.0002% | — | sem_zona |
| 2026-10-19 11:05 | DOGE-USDT-SWAP | 0.07912 | 0.07997/0.07901 | 0.07910 | sup 0.07925 (ha 8 candles) | 0.00061 | 0.0023% | — | sem_zona |
| 2026-10-19 11:05 | ARB-USDT-SWAP | 0.19558 | 0.19910/0.19501 | 0.19529 | — | 0.00340 | 0.0046% | B/venda@0.19508 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 11:05 | WLD-USDT-SWAP | 0.50980 | 0.51620/0.50560 | 0.49810 | sup 0.49330 (ha 3 candles) | 0.00891 | 0.0100% | — | zona_expirada_setup_B |
| 2026-10-19 11:05 | SUI-USDT-SWAP | 0.99350 | 1.0082/0.99230 | 0.99550 | sup 0.93640 (ha 18 candles) | 0.01079 | 0.0100% | — | sem_zona |
| 2026-10-19 11:05 | UNI-USDT-SWAP | 7.2810 | 7.4240/7.2660 | 7.3420 | sup 6.8030 (ha 18 candles) | 0.09286 | 0.0092% | — | sem_zona |
| 2026-10-19 11:05 | LINK-USDT-SWAP | 11.98 | 12.14/11.96 | 12.02 | — | 0.10064 | 0.0085% | — | sem_zona |
| 2026-10-19 12:05 | BTC-USDT-SWAP | 82264.0 | 82544.2/81720.0 | 82331.9 | sup 80621.4 (ha 18 candles) | 441.15 | 0.0100% | — | sem_zona |
| 2026-10-19 12:05 | ETH-USDT-SWAP | 2410.4 | 2423.9/2384.0 | 2418.9 | sup 2328.0 (ha 19 candles) | 17.62 | 0.0062% | — | sem_zona |
| 2026-10-19 12:05 | SOL-USDT-SWAP | 104.66 | 105.11/103.48 | 104.64 | sup 100.34 (ha 19 candles) | 0.84071 | 0.0100% | — | sem_zona |
| 2026-10-19 12:05 | XRP-USDT-SWAP | 1.3049 | 1.3134/1.2925 | 1.3028 | — | 0.00921 | 0.0020% | — | sem_zona |
| 2026-10-19 12:05 | DOGE-USDT-SWAP | 0.07952 | 0.08006/0.07854 | 0.07910 | sup 0.07925 (ha 9 candles) | 0.00067 | -0.0002% | — | sem_zona |
| 2026-10-19 12:05 | ARB-USDT-SWAP | 0.19766 | 0.19955/0.19308 | 0.19529 | — | 0.00364 | 0.0060% | — | invalidado_setup_B |
| 2026-10-19 12:05 | WLD-USDT-SWAP | 0.50830 | 0.51160/0.49790 | 0.49810 | sup 0.49330 (ha 4 candles) | 0.00939 | 0.0100% | — | sem_zona |
| 2026-10-19 12:05 | SUI-USDT-SWAP | 0.99970 | 1.0068/0.97920 | 0.99550 | sup 0.93640 (ha 19 candles) | 0.01166 | 0.0100% | — | sem_zona |
| 2026-10-19 12:05 | UNI-USDT-SWAP | 7.3420 | 7.3970/7.1790 | 7.3420 | sup 6.8030 (ha 19 candles) | 0.10093 | 0.0076% | — | sem_zona |
| 2026-10-19 12:05 | LINK-USDT-SWAP | 12.04 | 12.12/11.86 | 12.02 | — | 0.10921 | 0.0072% | — | sem_zona |
| 2026-10-19 13:05 | BTC-USDT-SWAP | 81912.4 | 82506.8/81875.0 | 81912.4 | sup 80621.4 (ha 19 candles) | 465.63 | 0.0100% | — | sem_zona |
| 2026-10-19 13:05 | ETH-USDT-SWAP | 2393.3 | 2421.0/2392.6 | 2393.3 | sup 2328.0 (ha 20 candles) | 18.55 | 0.0074% | — | sem_zona |
| 2026-10-19 13:05 | SOL-USDT-SWAP | 104.08 | 105.25/104.05 | 104.08 | sup 100.34 (ha 20 candles) | 0.87357 | 0.0089% | — | sem_zona |
| 2026-10-19 13:05 | XRP-USDT-SWAP | 1.2979 | 1.3109/1.2964 | 1.2979 | — | 0.00964 | 0.0046% | — | sem_zona |
| 2026-10-19 13:05 | DOGE-USDT-SWAP | 0.07903 | 0.07980/0.07898 | 0.07903 | sup 0.07925 (ha 10 candles) | 0.00069 | 0.0019% | — | sem_zona |
| 2026-10-19 13:05 | ARB-USDT-SWAP | 0.19565 | 0.19940/0.19526 | 0.19565 | — | 0.00360 | 0.0066% | B/compra@0.19834 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 13:05 | WLD-USDT-SWAP | 0.50630 | 0.51530/0.50420 | 0.50630 | sup 0.49330 (ha 5 candles) | 0.00959 | 0.0100% | — | sem_zona |
| 2026-10-19 13:05 | SUI-USDT-SWAP | 0.99120 | 1.0110/0.98900 | 0.99120 | sup 0.93640 (ha 20 candles) | 0.01272 | 0.0100% | — | sem_zona |
| 2026-10-19 13:05 | UNI-USDT-SWAP | 7.2880 | 7.3820/7.2830 | 7.2880 | sup 6.8030 (ha 20 candles) | 0.09993 | 0.0071% | — | sem_zona |
| 2026-10-19 13:05 | LINK-USDT-SWAP | 11.95 | 12.10/11.94 | 11.95 | sup 12.08 (ha 10 candles) | 0.11286 | 0.0073% | A/venda@12.08 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-19 14:05 | BTC-USDT-SWAP | 81948.2 | 82051.5/81682.0 | 81912.4 | sup 80621.4 (ha 20 candles) | 458.44 | 0.0100% | — | sem_zona |
| 2026-10-19 14:05 | ETH-USDT-SWAP | 2401.5 | 2404.9/2386.5 | 2393.3 | sup 2328.0 (ha 21 candles) | 18.24 | 0.0088% | — | sem_zona |
| 2026-10-19 14:05 | SOL-USDT-SWAP | 104.37 | 104.72/103.87 | 104.08 | sup 100.34 (ha 21 candles) | 0.85571 | 0.0090% | — | sem_zona |
| 2026-10-19 14:05 | XRP-USDT-SWAP | 1.3013 | 1.3052/1.2945 | 1.2979 | — | 0.00970 | 0.0071% | — | sem_zona |
| 2026-10-19 14:05 | DOGE-USDT-SWAP | 0.07926 | 0.07949/0.07887 | 0.07903 | sup 0.07925 (ha 11 candles) | 0.00068 | 0.0069% | — | sem_zona |
| 2026-10-19 14:05 | ARB-USDT-SWAP | 0.19565 | 0.19784/0.19524 | 0.19565 | — | 0.00349 | 0.0100% | — | invalidado_setup_B |
| 2026-10-19 14:05 | WLD-USDT-SWAP | 0.50990 | 0.51580/0.50430 | 0.50630 | sup 0.49330 (ha 6 candles) | 0.00976 | 0.0100% | — | sem_zona |
| 2026-10-19 14:05 | SUI-USDT-SWAP | 0.99100 | 0.99830/0.98780 | 0.99120 | sup 0.93640 (ha 21 candles) | 0.01244 | 0.0100% | — | sem_zona |
| 2026-10-19 14:05 | UNI-USDT-SWAP | 7.3110 | 7.3560/7.2560 | 7.2880 | sup 6.8030 (ha 21 candles) | 0.09964 | 0.0053% | — | sem_zona |
| 2026-10-19 14:05 | LINK-USDT-SWAP | 11.97 | 12.02/11.91 | 11.95 | sup 12.08 (ha 11 candles) | 0.11071 | 0.0100% | A/venda@12.08 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-19 15:05 | BTC-USDT-SWAP | 81894.1 | 82033.5/81800.0 | 81912.4 | sup 80621.4 (ha 21 candles) | 456.66 | 0.0100% | — | sem_zona |
| 2026-10-19 15:05 | ETH-USDT-SWAP | 2397.2 | 2404.8/2392.4 | 2393.3 | sup 2384.0 (ha 3 candles) | 18.54 | 0.0092% | — | sem_zona |
| 2026-10-19 15:05 | SOL-USDT-SWAP | 104.01 | 104.63/103.81 | 104.08 | sup 103.48 (ha 3 candles) | 0.88429 | 0.0088% | — | sem_zona |
| 2026-10-19 15:05 | XRP-USDT-SWAP | 1.3001 | 1.3044/1.2978 | 1.2979 | — | 0.00983 | 0.0100% | — | sem_zona |
| 2026-10-19 15:05 | DOGE-USDT-SWAP | 0.07904 | 0.07943/0.07893 | 0.07903 | sup 0.07854 (ha 3 candles) | 0.00068 | 0.0100% | — | sem_zona |
| 2026-10-19 15:05 | ARB-USDT-SWAP | 0.19362 | 0.19592/0.19339 | 0.19565 | — | 0.00346 | 0.0100% | — | sem_zona |
| 2026-10-19 15:05 | WLD-USDT-SWAP | 0.51150 | 0.51420/0.50710 | 0.50630 | sup 0.49330 (ha 7 candles) | 0.00998 | 0.0100% | — | sem_zona |
| 2026-10-19 15:05 | SUI-USDT-SWAP | 0.98630 | 0.99350/0.98420 | 0.99120 | sup 0.97920 (ha 3 candles) | 0.01251 | 0.0100% | — | sem_zona |
| 2026-10-19 15:05 | UNI-USDT-SWAP | 7.2510 | 7.3320/7.2460 | 7.2880 | sup 7.1790 (ha 3 candles) | 0.10179 | 0.0061% | — | sem_zona |
| 2026-10-19 15:05 | LINK-USDT-SWAP | 11.90 | 12.00/11.88 | 11.95 | sup 11.86 (ha 3 candles) | 0.11564 | 0.0100% | A/venda@12.08 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-19 16:05 | BTC-USDT-SWAP | 81928.8 | 82121.9/81759.3 | 81912.4 | sup 80621.4 (ha 22 candles) | 453.43 | 0.0099% | — | sem_zona |
| 2026-10-19 16:05 | ETH-USDT-SWAP | 2400.2 | 2407.6/2389.1 | 2393.3 | sup 2384.0 (ha 4 candles) | 18.90 | 0.0090% | — | sem_zona |
| 2026-10-19 16:05 | SOL-USDT-SWAP | 103.94 | 104.44/103.60 | 104.08 | sup 103.48 (ha 4 candles) | 0.87929 | 0.0088% | — | sem_zona |
| 2026-10-19 16:05 | XRP-USDT-SWAP | 1.3028 | 1.3054/1.2957 | 1.2979 | — | 0.01000 | 0.0100% | B/compra@1.3102 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 16:05 | DOGE-USDT-SWAP | 0.07925 | 0.07935/0.07870 | 0.07903 | sup 0.07854 (ha 4 candles) | 0.00068 | 0.0100% | — | sem_zona |
| 2026-10-19 16:05 | ARB-USDT-SWAP | 0.19391 | 0.19514/0.19267 | 0.19565 | — | 0.00344 | 0.0100% | — | sem_zona |
| 2026-10-19 16:05 | WLD-USDT-SWAP | 0.50710 | 0.51810/0.50120 | 0.50630 | sup 0.49330 (ha 8 candles) | 0.01066 | 0.0100% | — | sem_zona |
| 2026-10-19 16:05 | SUI-USDT-SWAP | 0.98770 | 0.99150/0.98020 | 0.99120 | sup 0.97920 (ha 4 candles) | 0.01229 | 0.0100% | — | sem_zona |
| 2026-10-19 16:05 | UNI-USDT-SWAP | 7.2400 | 7.2850/7.2020 | 7.2880 | sup 7.1790 (ha 4 candles) | 0.09750 | 0.0086% | — | sem_zona |
| 2026-10-19 16:05 | LINK-USDT-SWAP | 11.90 | 11.95/11.83 | 11.95 | sup 11.86 (ha 4 candles) | 0.11843 | 0.0100% | A/venda@12.08 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-19 17:05 | BTC-USDT-SWAP | 81839.9 | 82053.6/81758.0 | 81839.9 | — | 456.71 | 0.0100% | — | sem_zona |
| 2026-10-19 17:05 | ETH-USDT-SWAP | 2394.0 | 2403.9/2389.7 | 2394.0 | — | 19.17 | 0.0091% | B/compra@2391.7 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 17:05 | SOL-USDT-SWAP | 103.99 | 104.43/103.73 | 103.99 | — | 0.88643 | 0.0091% | — | sem_zona |
| 2026-10-19 17:05 | XRP-USDT-SWAP | 1.3003 | 1.3048/1.2972 | 1.3003 | sup 1.2925 (ha 5 candles) | 0.01017 | 0.0100% | B/compra@1.3102 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-19 17:05 | DOGE-USDT-SWAP | 0.07916 | 0.07941/0.07901 | 0.07916 | sup 0.07854 (ha 5 candles) | 0.00068 | 0.0098% | — | sem_zona |
| 2026-10-19 17:05 | ARB-USDT-SWAP | 0.19200 | 0.19397/0.19181 | 0.19200 | — | 0.00341 | 0.0100% | — | sem_zona |
| 2026-10-19 17:05 | WLD-USDT-SWAP | 0.50650 | 0.51240/0.50550 | 0.50650 | sup 0.49330 (ha 9 candles) | 0.01064 | 0.0100% | — | sem_zona |
| 2026-10-19 17:05 | SUI-USDT-SWAP | 0.98390 | 0.98900/0.98260 | 0.98390 | sup 0.97920 (ha 5 candles) | 0.01195 | 0.0100% | — | sem_zona |
| 2026-10-19 17:05 | UNI-USDT-SWAP | 7.1910 | 7.2400/7.1770 | 7.1910 | — | 0.09557 | 0.0099% | B/compra@7.2270 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 17:05 | LINK-USDT-SWAP | 11.87 | 11.95/11.86 | 11.87 | sup 11.86 (ha 5 candles) | 0.11771 | 0.0100% | A/venda@12.08 (0t/4c) | zona_mapeada_setup_A |
| 2026-10-19 18:05 | BTC-USDT-SWAP | 81983.2 | 82055.6/81807.0 | 81839.9 | — | 456.55 | 0.0095% | — | sem_zona |
| 2026-10-19 18:05 | ETH-USDT-SWAP | 2400.0 | 2402.7/2392.9 | 2394.0 | — | 19.29 | 0.0085% | — | confirmado_calibracao_setup_B |
| 2026-10-19 18:05 | SOL-USDT-SWAP | 104.50 | 104.75/103.91 | 103.99 | — | 0.91786 | 0.0078% | B/venda@104.76 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 18:05 | XRP-USDT-SWAP | 1.3009 | 1.3052/1.2991 | 1.3003 | sup 1.2925 (ha 6 candles) | 0.01032 | 0.0100% | B/compra@1.3102 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-19 18:05 | DOGE-USDT-SWAP | 0.07930 | 0.07952/0.07915 | 0.07916 | sup 0.07854 (ha 6 candles) | 0.00069 | 0.0089% | — | sem_zona |
| 2026-10-19 18:05 | ARB-USDT-SWAP | 0.19228 | 0.19322/0.19159 | 0.19200 | — | 0.00315 | 0.0100% | — | sem_zona |
| 2026-10-19 18:05 | WLD-USDT-SWAP | 0.51060 | 0.51800/0.50650 | 0.50650 | sup 0.49330 (ha 10 candles) | 0.01111 | 0.0100% | — | sem_zona |
| 2026-10-19 18:05 | SUI-USDT-SWAP | 0.98580 | 0.99100/0.98230 | 0.98390 | sup 0.97920 (ha 6 candles) | 0.01228 | 0.0100% | — | sem_zona |
| 2026-10-19 18:05 | UNI-USDT-SWAP | 7.2130 | 7.2310/7.1870 | 7.1910 | — | 0.09450 | 0.0100% | B/compra@7.2270 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-19 18:05 | LINK-USDT-SWAP | 11.91 | 11.94/11.87 | 11.87 | sup 11.86 (ha 6 candles) | 0.11686 | 0.0100% | A/venda@12.08 (0t/5c) | zona_mapeada_setup_A |
| 2026-10-19 19:05 | BTC-USDT-SWAP | 82010.0 | 82185.0/81972.6 | 81839.9 | — | 435.26 | 0.0089% | — | sem_zona |
| 2026-10-19 19:05 | ETH-USDT-SWAP | 2401.7 | 2409.4/2399.7 | 2394.0 | — | 18.72 | 0.0076% | B/compra@2407.5 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 19:05 | SOL-USDT-SWAP | 104.69 | 104.91/104.49 | 103.99 | — | 0.90143 | 0.0060% | B/venda@104.76 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-19 19:05 | XRP-USDT-SWAP | 1.3028 | 1.3059/1.3009 | 1.3003 | sup 1.2925 (ha 7 candles) | 0.01007 | 0.0100% | B/compra@1.3102 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-19 19:05 | DOGE-USDT-SWAP | 0.07948 | 0.07959/0.07930 | 0.07916 | sup 0.07870 (ha 3 candles) | 0.00067 | 0.0090% | — | sem_zona |
| 2026-10-19 19:05 | ARB-USDT-SWAP | 0.19608 | 0.20277/0.19215 | 0.19200 | — | 0.00368 | 0.0100% | B/compra@0.19734 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 19:05 | WLD-USDT-SWAP | 0.51660 | 0.51790/0.51070 | 0.50650 | sup 0.50120 (ha 3 candles) | 0.01056 | 0.0100% | B/venda@0.51160 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 19:05 | SUI-USDT-SWAP | 0.98940 | 0.99170/0.98590 | 0.98390 | sup 0.98020 (ha 3 candles) | 0.01210 | 0.0100% | — | sem_zona |
| 2026-10-19 19:05 | UNI-USDT-SWAP | 7.2490 | 7.2710/7.2130 | 7.1910 | — | 0.09171 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-10-19 19:05 | LINK-USDT-SWAP | 11.95 | 11.96/11.90 | 11.87 | sup 11.83 (ha 3 candles) | 0.11543 | 0.0100% | A/venda@12.08 (0t/6c) | zona_mapeada_setup_A |
| 2026-10-19 20:05 | BTC-USDT-SWAP | 82018.9 | 82243.4/82000.4 | 81839.9 | — | 424.76 | 0.0084% | — | sem_zona |
| 2026-10-19 20:05 | ETH-USDT-SWAP | 2405.9 | 2417.3/2401.7 | 2394.0 | — | 18.89 | 0.0075% | B/compra@2407.5 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-19 20:05 | SOL-USDT-SWAP | 105.12 | 105.64/104.70 | 103.99 | — | 0.93000 | 0.0055% | — | invalidado_setup_B |
| 2026-10-19 20:05 | XRP-USDT-SWAP | 1.3045 | 1.3108/1.3029 | 1.3003 | sup 1.2925 (ha 8 candles) | 0.01016 | 0.0100% | — | invalidado_setup_B |
| 2026-10-19 20:05 | DOGE-USDT-SWAP | 0.07967 | 0.08009/0.07949 | 0.07916 | sup 0.07870 (ha 4 candles) | 0.00068 | 0.0086% | — | sem_zona |
| 2026-10-19 20:05 | ARB-USDT-SWAP | 0.19703 | 0.20070/0.19551 | 0.19200 | — | 0.00386 | 0.0100% | B/compra@0.19734 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-19 20:05 | WLD-USDT-SWAP | 0.52840 | 0.53550/0.51650 | 0.50650 | sup 0.50120 (ha 4 candles) | 0.01126 | 0.0100% | B/venda@0.51160 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-19 20:05 | SUI-USDT-SWAP | 0.99850 | 1.0073/0.98950 | 0.98390 | sup 0.98020 (ha 4 candles) | 0.01279 | 0.0100% | — | sem_zona |
| 2026-10-19 20:05 | UNI-USDT-SWAP | 7.2960 | 7.3650/7.2500 | 7.1910 | — | 0.09550 | 0.0100% | B/venda@7.3540 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 20:05 | LINK-USDT-SWAP | 12.03 | 12.07/11.95 | 11.87 | sup 11.83 (ha 4 candles) | 0.12021 | 0.0100% | A/venda@12.08 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-19 21:06 | BTC-USDT-SWAP | 81909.6 | 82082.0/81895.0 | 81909.6 | — | 412.03 | 0.0084% | — | sem_zona |
| 2026-10-19 21:06 | ETH-USDT-SWAP | 2407.1 | 2411.1/2403.7 | 2407.1 | — | 18.40 | 0.0076% | B/compra@2407.5 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-19 21:06 | SOL-USDT-SWAP | 105.03 | 105.25/104.89 | 105.03 | — | 0.91786 | 0.0053% | B/venda@105.22 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 21:06 | XRP-USDT-SWAP | 1.3036 | 1.3059/1.3029 | 1.3036 | sup 1.2925 (ha 9 candles) | 0.01001 | 0.0100% | — | sem_zona |
| 2026-10-19 21:06 | DOGE-USDT-SWAP | 0.07970 | 0.07980/0.07951 | 0.07970 | sup 0.07870 (ha 5 candles) | 0.00068 | 0.0075% | — | sem_zona |
| 2026-10-19 21:06 | ARB-USDT-SWAP | 0.19708 | 0.19816/0.19660 | 0.19708 | — | 0.00381 | 0.0088% | B/compra@0.19734 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-19 21:06 | WLD-USDT-SWAP | 0.53320 | 0.53730/0.52580 | 0.53320 | sup 0.50120 (ha 5 candles) | 0.01161 | 0.0100% | B/venda@0.51160 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-19 21:06 | SUI-USDT-SWAP | 0.99850 | 1.0014/0.99540 | 0.99850 | sup 0.98020 (ha 5 candles) | 0.01264 | 0.0100% | — | sem_zona |
| 2026-10-19 21:06 | UNI-USDT-SWAP | 7.3120 | 7.3450/7.2720 | 7.3120 | — | 0.09693 | 0.0068% | B/venda@7.3540 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-19 21:06 | LINK-USDT-SWAP | 12.05 | 12.07/12.00 | 12.05 | sup 11.83 (ha 5 candles) | 0.12121 | 0.0100% | A/venda@12.08 (2t/0c) | zona_mapeada_setup_A |
| 2026-10-19 22:06 | BTC-USDT-SWAP | 81696.9 | 81984.9/81411.6 | 81909.6 | — | 396.56 | 0.0097% | — | sem_zona |
| 2026-10-19 22:06 | ETH-USDT-SWAP | 2400.7 | 2409.4/2391.1 | 2407.1 | — | 17.98 | 0.0077% | — | invalidado_setup_B |
| 2026-10-19 22:06 | SOL-USDT-SWAP | 104.71 | 105.12/104.26 | 105.03 | — | 0.89286 | 0.0052% | B/venda@105.22 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-19 22:06 | XRP-USDT-SWAP | 1.2977 | 1.3048/1.2954 | 1.3036 | sup 1.2925 (ha 10 candles) | 0.00959 | 0.0100% | — | sem_zona |
| 2026-10-19 22:06 | DOGE-USDT-SWAP | 0.07930 | 0.07978/0.07919 | 0.07970 | sup 0.07870 (ha 6 candles) | 0.00064 | 0.0084% | — | sem_zona |
| 2026-10-19 22:06 | ARB-USDT-SWAP | 0.19861 | 0.19929/0.19468 | 0.19708 | — | 0.00391 | 0.0058% | — | descartado_rr_baixo_setup_B |
| 2026-10-19 22:06 | WLD-USDT-SWAP | 0.53320 | 0.53930/0.52770 | 0.53320 | sup 0.50120 (ha 6 candles) | 0.01150 | 0.0100% | B/venda@0.51160 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-19 22:06 | SUI-USDT-SWAP | 0.99490 | 0.99990/0.99010 | 0.99850 | sup 0.98020 (ha 6 candles) | 0.01219 | 0.0100% | — | sem_zona |
| 2026-10-19 22:06 | UNI-USDT-SWAP | 7.2880 | 7.3250/7.2420 | 7.3120 | — | 0.09579 | 0.0056% | B/venda@7.3540 (1t/1c) | zona_mapeada_setup_B |
| 2026-10-19 22:06 | LINK-USDT-SWAP | 11.99 | 12.06/11.95 | 12.05 | sup 11.83 (ha 6 candles) | 0.11943 | 0.0100% | — | descartado_rr_baixo_setup_A |
| 2026-10-19 23:06 | BTC-USDT-SWAP | 81773.0 | 81824.9/81166.0 | 81909.6 | — | 423.21 | 0.0100% | — | sem_zona |
| 2026-10-19 23:06 | ETH-USDT-SWAP | 2398.3 | 2401.4/2369.0 | 2407.1 | — | 19.28 | 0.0069% | B/compra@2391.7 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 23:06 | SOL-USDT-SWAP | 104.83 | 104.92/103.61 | 105.03 | — | 0.94214 | 0.0063% | B/venda@105.22 (1t/1c) | zona_mapeada_setup_B |
| 2026-10-19 23:06 | XRP-USDT-SWAP | 1.3011 | 1.3028/1.2856 | 1.3036 | sup 1.2925 (ha 11 candles) | 0.01030 | 0.0100% | — | sem_zona |
| 2026-10-19 23:06 | DOGE-USDT-SWAP | 0.07932 | 0.07946/0.07842 | 0.07970 | sup 0.07870 (ha 7 candles) | 0.00068 | 0.0090% | — | sem_zona |
| 2026-10-19 23:06 | ARB-USDT-SWAP | 0.19913 | 0.20023/0.19465 | 0.19708 | — | 0.00417 | -0.0024% | B/compra@0.19938 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-19 23:06 | WLD-USDT-SWAP | 0.53290 | 0.54170/0.52210 | 0.53320 | sup 0.50120 (ha 7 candles) | 0.01254 | 0.0100% | B/venda@0.51160 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-19 23:06 | SUI-USDT-SWAP | 0.99110 | 0.99500/0.97530 | 0.99850 | sup 0.98020 (ha 7 candles) | 0.01302 | 0.0098% | — | sem_zona |
| 2026-10-19 23:06 | UNI-USDT-SWAP | 7.2760 | 7.3110/7.1800 | 7.3120 | — | 0.09993 | 0.0071% | B/venda@7.3540 (1t/2c) | zona_mapeada_setup_B |
| 2026-10-19 23:06 | LINK-USDT-SWAP | 11.97 | 12.00/11.83 | 12.05 | sup 11.83 (ha 7 candles) | 0.12521 | 0.0100% | — | sem_zona |
| 2026-10-20 00:06 | BTC-USDT-SWAP | 81765.2 | 81932.1/81503.0 | 81909.6 | — | 427.75 | 0.0100% | — | sem_zona |
| 2026-10-20 00:06 | ETH-USDT-SWAP | 2399.8 | 2406.7/2387.3 | 2407.1 | — | 19.89 | 0.0058% | — | descartado_rr_baixo_setup_B |
| 2026-10-20 00:06 | SOL-USDT-SWAP | 105.10 | 105.42/104.29 | 105.03 | — | 0.95643 | 0.0074% | B/venda@105.22 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-20 00:06 | XRP-USDT-SWAP | 1.3033 | 1.3061/1.2960 | 1.3036 | sup 1.2925 (ha 12 candles) | 0.01029 | 0.0100% | — | sem_zona |
| 2026-10-20 00:06 | DOGE-USDT-SWAP | 0.07951 | 0.07975/0.07898 | 0.07970 | sup 0.07870 (ha 8 candles) | 0.00067 | 0.0100% | — | sem_zona |
| 2026-10-20 00:06 | ARB-USDT-SWAP | 0.20127 | 0.20429/0.19778 | 0.19708 | — | 0.00430 | -0.0109% | B/compra@0.19938 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-20 00:06 | WLD-USDT-SWAP | 0.53870 | 0.54270/0.53100 | 0.53320 | sup 0.50120 (ha 8 candles) | 0.01214 | 0.0100% | B/venda@0.51160 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-20 00:06 | SUI-USDT-SWAP | 0.99760 | 1.0024/0.98440 | 0.99850 | sup 0.98020 (ha 8 candles) | 0.01350 | 0.0100% | — | sem_zona |
| 2026-10-20 00:06 | UNI-USDT-SWAP | 7.2680 | 7.3120/7.2230 | 7.3120 | — | 0.10007 | 0.0100% | B/venda@7.3540 (1t/3c) | zona_mapeada_setup_B |
| 2026-10-20 00:06 | LINK-USDT-SWAP | 12.03 | 12.07/11.92 | 12.05 | sup 11.83 (ha 8 candles) | 0.12686 | 0.0100% | — | sem_zona |
| 2026-10-20 01:06 | BTC-USDT-SWAP | 82098.8 | 82099.0/81741.9 | 82098.8 | — | 401.90 | 0.0100% | B/venda@82267.7 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 01:06 | ETH-USDT-SWAP | 2414.0 | 2414.8/2398.9 | 2414.0 | — | 18.59 | 0.0059% | B/compra@2407.5 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 01:06 | SOL-USDT-SWAP | 105.28 | 105.35/104.82 | 105.28 | res 105.64 (ha 5 candles) | 0.88857 | 0.0074% | — | zona_expirada_setup_B |
| 2026-10-20 01:06 | XRP-USDT-SWAP | 1.3060 | 1.3066/1.2996 | 1.3060 | sup 1.2925 (ha 13 candles) | 0.00970 | 0.0100% | — | sem_zona |
| 2026-10-20 01:06 | DOGE-USDT-SWAP | 0.07980 | 0.07980/0.07936 | 0.07980 | sup 0.07870 (ha 9 candles) | 0.00064 | 0.0100% | — | sem_zona |
| 2026-10-20 01:06 | ARB-USDT-SWAP | 0.20212 | 0.20249/0.19812 | 0.20212 | — | 0.00432 | -0.0166% | — | descartado_rr_baixo_setup_B |
| 2026-10-20 01:06 | WLD-USDT-SWAP | 0.54390 | 0.54890/0.53750 | 0.54390 | sup 0.50120 (ha 9 candles) | 0.01220 | 0.0100% | B/venda@0.51160 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-20 01:06 | SUI-USDT-SWAP | 1.0026 | 1.0026/0.99260 | 1.0026 | sup 0.98020 (ha 9 candles) | 0.01308 | 0.0100% | — | sem_zona |
| 2026-10-20 01:06 | UNI-USDT-SWAP | 7.3110 | 7.3110/7.2460 | 7.3110 | — | 0.09343 | 0.0100% | B/venda@7.3540 (1t/4c) | zona_mapeada_setup_B |
| 2026-10-20 01:06 | LINK-USDT-SWAP | 12.10 | 12.11/11.99 | 12.10 | sup 11.83 (ha 9 candles) | 0.12243 | 0.0100% | — | sem_zona |
| 2026-10-20 02:06 | BTC-USDT-SWAP | 82058.3 | 82240.0/82010.0 | 82098.8 | — | 359.46 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-10-20 02:06 | ETH-USDT-SWAP | 2411.6 | 2416.8/2408.8 | 2414.0 | — | 16.32 | 0.0053% | B/compra@2407.5 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-20 02:06 | SOL-USDT-SWAP | 105.18 | 105.47/105.08 | 105.28 | res 105.64 (ha 6 candles) | 0.80000 | 0.0067% | B/compra@105.61 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 02:06 | XRP-USDT-SWAP | 1.3044 | 1.3077/1.3031 | 1.3060 | sup 1.2856 (ha 3 candles) | 0.00854 | 0.0100% | — | sem_zona |
| 2026-10-20 02:06 | DOGE-USDT-SWAP | 0.07957 | 0.07987/0.07952 | 0.07980 | sup 0.07842 (ha 3 candles) | 0.00055 | 0.0100% | — | sem_zona |
| 2026-10-20 02:06 | ARB-USDT-SWAP | 0.19951 | 0.20219/0.19833 | 0.20212 | — | 0.00413 | -0.0180% | B/venda@0.20232 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 02:06 | WLD-USDT-SWAP | 0.54240 | 0.55390/0.54020 | 0.54390 | sup 0.50120 (ha 10 candles) | 0.01220 | 0.0100% | B/venda@0.51160 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-20 02:06 | SUI-USDT-SWAP | 0.99880 | 1.0061/0.99760 | 1.0026 | sup 0.97530 (ha 3 candles) | 0.01171 | 0.0099% | — | sem_zona |
| 2026-10-20 02:06 | UNI-USDT-SWAP | 7.2920 | 7.3410/7.2680 | 7.3110 | — | 0.08307 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-10-20 02:06 | LINK-USDT-SWAP | 12.04 | 12.11/12.04 | 12.10 | sup 11.83 (ha 3 candles) | 0.10900 | 0.0074% | — | sem_zona |
| 2026-10-20 03:06 | BTC-USDT-SWAP | 81677.8 | 82078.3/81671.8 | 82098.8 | — | 343.36 | 0.0096% | — | sem_zona |
| 2026-10-20 03:06 | ETH-USDT-SWAP | 2395.6 | 2412.8/2395.6 | 2414.0 | — | 15.52 | 0.0044% | — | invalidado_setup_B |
| 2026-10-20 03:06 | SOL-USDT-SWAP | 104.48 | 105.22/104.44 | 105.28 | res 105.64 (ha 7 candles) | 0.77000 | 0.0059% | B/compra@105.61 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-20 03:06 | XRP-USDT-SWAP | 1.3012 | 1.3065/1.3006 | 1.3060 | sup 1.2856 (ha 4 candles) | 0.00792 | 0.0100% | — | sem_zona |
| 2026-10-20 03:06 | DOGE-USDT-SWAP | 0.07923 | 0.07973/0.07919 | 0.07980 | sup 0.07842 (ha 4 candles) | 0.00053 | 0.0100% | — | sem_zona |
| 2026-10-20 03:06 | ARB-USDT-SWAP | 0.19783 | 0.20055/0.19749 | 0.20212 | — | 0.00405 | -0.0175% | B/venda@0.20232 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-20 03:06 | WLD-USDT-SWAP | 0.53650 | 0.54590/0.53450 | 0.54390 | sup 0.50120 (ha 11 candles) | 0.01222 | 0.0100% | — | zona_expirada_setup_B |
| 2026-10-20 03:06 | SUI-USDT-SWAP | 0.99120 | 1.0009/0.99060 | 1.0026 | sup 0.97530 (ha 4 candles) | 0.01088 | 0.0089% | — | sem_zona |
| 2026-10-20 03:06 | UNI-USDT-SWAP | 7.1960 | 7.2970/7.1960 | 7.3110 | — | 0.08321 | 0.0082% | B/compra@7.2270 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 03:06 | LINK-USDT-SWAP | 11.97 | 12.07/11.97 | 12.10 | sup 11.83 (ha 4 candles) | 0.10457 | 0.0046% | — | sem_zona |
| 2026-10-20 04:06 | BTC-USDT-SWAP | 81771.3 | 81844.6/81580.3 | 82098.8 | — | 335.85 | 0.0081% | — | sem_zona |
| 2026-10-20 04:06 | ETH-USDT-SWAP | 2397.5 | 2401.3/2390.3 | 2414.0 | — | 14.99 | 0.0054% | B/compra@2391.7 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 04:06 | SOL-USDT-SWAP | 104.63 | 104.87/104.16 | 105.28 | res 105.64 (ha 8 candles) | 0.76000 | 0.0065% | B/compra@105.61 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-20 04:06 | XRP-USDT-SWAP | 1.3008 | 1.3044/1.2989 | 1.3060 | sup 1.2856 (ha 5 candles) | 0.00755 | 0.0100% | — | sem_zona |
| 2026-10-20 04:06 | DOGE-USDT-SWAP | 0.07934 | 0.07948/0.07900 | 0.07980 | sup 0.07842 (ha 5 candles) | 0.00052 | 0.0100% | — | sem_zona |
| 2026-10-20 04:06 | ARB-USDT-SWAP | 0.19697 | 0.19941/0.19663 | 0.20212 | — | 0.00407 | -0.0128% | B/venda@0.20232 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-20 04:06 | WLD-USDT-SWAP | 0.54290 | 0.54560/0.53370 | 0.54390 | sup 0.50120 (ha 12 candles) | 0.01225 | 0.0100% | B/venda@0.53940 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 04:06 | SUI-USDT-SWAP | 0.99460 | 0.99880/0.98770 | 1.0026 | sup 0.97530 (ha 5 candles) | 0.01092 | 0.0096% | — | sem_zona |
| 2026-10-20 04:06 | UNI-USDT-SWAP | 7.1870 | 7.2250/7.1150 | 7.3110 | — | 0.08393 | 0.0076% | — | invalidado_setup_B |
| 2026-10-20 04:06 | LINK-USDT-SWAP | 12.00 | 12.04/11.94 | 12.10 | sup 11.83 (ha 5 candles) | 0.10407 | 0.0045% | — | sem_zona |
| 2026-10-20 05:06 | BTC-USDT-SWAP | 81514.6 | 81813.3/81420.0 | 81514.6 | — | 347.26 | 0.0046% | — | sem_zona |
| 2026-10-20 05:06 | ETH-USDT-SWAP | 2389.8 | 2398.5/2385.6 | 2389.8 | — | 15.03 | 0.0040% | B/compra@2391.7 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-20 05:06 | SOL-USDT-SWAP | 104.36 | 104.73/104.21 | 104.36 | res 105.47 (ha 3 candles) | 0.73857 | 0.0045% | B/compra@105.61 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-20 05:06 | XRP-USDT-SWAP | 1.2966 | 1.3023/1.2950 | 1.2966 | sup 1.2856 (ha 6 candles) | 0.00760 | 0.0077% | — | sem_zona |
| 2026-10-20 05:06 | DOGE-USDT-SWAP | 0.07923 | 0.07944/0.07910 | 0.07923 | sup 0.07842 (ha 6 candles) | 0.00051 | 0.0100% | — | sem_zona |
| 2026-10-20 05:06 | ARB-USDT-SWAP | 0.19311 | 0.19746/0.19211 | 0.19311 | — | 0.00427 | -0.0050% | B/venda@0.20232 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-20 05:06 | WLD-USDT-SWAP | 0.53950 | 0.54520/0.53660 | 0.53950 | sup 0.50120 (ha 13 candles) | 0.01236 | 0.0100% | — | confirmado_calibracao_setup_B |
| 2026-10-20 05:06 | SUI-USDT-SWAP | 0.99070 | 0.99650/0.98840 | 0.99070 | sup 0.97530 (ha 6 candles) | 0.01084 | 0.0088% | — | sem_zona |
| 2026-10-20 05:06 | UNI-USDT-SWAP | 7.1800 | 7.2070/7.1550 | 7.1800 | — | 0.08150 | 0.0078% | — | sem_zona |
| 2026-10-20 05:06 | LINK-USDT-SWAP | 11.96 | 12.02/11.94 | 11.96 | sup 11.83 (ha 6 candles) | 0.10086 | 0.0037% | — | sem_zona |
| 2026-10-20 06:06 | BTC-USDT-SWAP | 81499.9 | 81597.0/81323.3 | 81514.6 | — | 340.91 | 0.0025% | — | sem_zona |
| 2026-10-20 06:06 | ETH-USDT-SWAP | 2384.2 | 2391.3/2377.0 | 2389.8 | — | 14.73 | 0.0030% | — | invalidado_setup_B |
| 2026-10-20 06:06 | SOL-USDT-SWAP | 104.08 | 104.45/103.77 | 104.36 | res 105.47 (ha 4 candles) | 0.72714 | 0.0041% | B/compra@105.61 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-20 06:06 | XRP-USDT-SWAP | 1.2939 | 1.2996/1.2915 | 1.2966 | sup 1.2856 (ha 7 candles) | 0.00749 | 0.0040% | — | sem_zona |
| 2026-10-20 06:06 | DOGE-USDT-SWAP | 0.07897 | 0.07928/0.07874 | 0.07923 | sup 0.07842 (ha 7 candles) | 0.00050 | 0.0100% | — | sem_zona |
| 2026-10-20 06:06 | ARB-USDT-SWAP | 0.19007 | 0.19311/0.18888 | 0.19311 | — | 0.00439 | 0.0019% | B/venda@0.20232 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-20 06:06 | WLD-USDT-SWAP | 0.53650 | 0.54000/0.53410 | 0.53950 | sup 0.50120 (ha 14 candles) | 0.01157 | 0.0100% | B/venda@0.53360 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 06:06 | SUI-USDT-SWAP | 0.98700 | 0.99190/0.98280 | 0.99070 | sup 0.97530 (ha 7 candles) | 0.01068 | 0.0091% | — | sem_zona |
| 2026-10-20 06:06 | UNI-USDT-SWAP | 7.1420 | 7.1850/7.0930 | 7.1800 | — | 0.08214 | 0.0080% | B/compra@7.0890 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-20 06:06 | LINK-USDT-SWAP | 11.93 | 11.96/11.89 | 11.96 | sup 11.83 (ha 7 candles) | 0.09771 | 0.0044% | — | sem_zona |
| 2026-10-20 07:06 | BTC-USDT-SWAP | 81457.8 | 81581.9/81288.0 | 81514.6 | — | 340.79 | 0.0015% | — | sem_zona |
| 2026-10-20 07:06 | ETH-USDT-SWAP | 2383.1 | 2387.8/2375.4 | 2389.8 | — | 14.60 | 0.0014% | — | sem_zona |
| 2026-10-20 07:06 | SOL-USDT-SWAP | 104.00 | 104.29/103.74 | 104.36 | res 105.47 (ha 5 candles) | 0.71643 | 0.0045% | B/compra@105.61 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-20 07:06 | XRP-USDT-SWAP | 1.2931 | 1.2961/1.2895 | 1.2966 | sup 1.2856 (ha 8 candles) | 0.00741 | 0.0032% | — | sem_zona |
| 2026-10-20 07:06 | DOGE-USDT-SWAP | 0.07900 | 0.07910/0.07873 | 0.07923 | sup 0.07842 (ha 8 candles) | 0.00050 | 0.0100% | — | sem_zona |
| 2026-10-20 07:06 | ARB-USDT-SWAP | 0.18953 | 0.19067/0.18888 | 0.19311 | — | 0.00437 | 0.0087% | B/venda@0.20232 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-20 07:06 | WLD-USDT-SWAP | 0.53420 | 0.53830/0.52950 | 0.53950 | sup 0.50120 (ha 15 candles) | 0.01171 | 0.0100% | B/venda@0.53360 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-20 07:06 | SUI-USDT-SWAP | 0.98850 | 0.98910/0.98250 | 0.99070 | sup 0.97530 (ha 8 candles) | 0.01069 | 0.0100% | — | sem_zona |
| 2026-10-20 07:06 | UNI-USDT-SWAP | 7.1240 | 7.1600/7.0920 | 7.1800 | — | 0.08250 | 0.0082% | B/compra@7.0890 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-20 07:06 | LINK-USDT-SWAP | 11.93 | 11.95/11.88 | 11.96 | sup 11.83 (ha 8 candles) | 0.09621 | 0.0066% | — | sem_zona |
