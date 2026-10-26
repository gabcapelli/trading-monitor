# Log de Monitoramento Automatico -- Multi-Par (script gratuito, GitHub Actions)

> Gerado por script Python sem LLM (ver monitor/fetch_and_check.py). Fonte: OKX. Cobre os pares em PAIRS (configuracao no topo do script) -- BTC-USDT-SWAP e os demais adicionados na expansao de 07/09/2026. Leitura e MECANICA (regras objetivas da secao 4 do plano), sem a prosa qualitativa que o Claude gerava -- cole este log numa conversa do Claude se quiser a leitura interpretativa.

| Data/Hora (BRT) | Par | Close 1h | High/Low 1h | Close 4h | Swing 1h ref | ATR 1h | Funding | Zona ativa | Status checklist |
|---|---|---|---|---|---|---|---|---|---|
| 2026-10-24 04:06 | BTC-USDT-SWAP | 80748.2 | 80797.4/80650.5 | 80930.6 | sup 80456.6 (ha 7 candles) | 337.04 | 0.0039% | — | sem_zona |
| 2026-10-24 04:06 | ETH-USDT-SWAP | 2377.8 | 2379.8/2373.4 | 2381.6 | sup 2350.1 (ha 8 candles) | 14.42 | 0.0099% | — | sem_zona |
| 2026-10-24 04:06 | SOL-USDT-SWAP | 102.12 | 102.38/101.98 | 102.61 | sup 101.64 (ha 8 candles) | 0.71000 | 0.0100% | — | sem_zona |
| 2026-10-24 04:06 | XRP-USDT-SWAP | 1.2886 | 1.2894/1.2859 | 1.2906 | — | 0.00870 | 0.0048% | — | descartado_rr_baixo_setup_B |
| 2026-10-24 04:06 | DOGE-USDT-SWAP | 0.07823 | 0.07840/0.07816 | 0.07878 | sup 0.07734 (ha 8 candles) | 0.00061 | 0.0063% | — | sem_zona |
| 2026-10-24 04:06 | ARB-USDT-SWAP | 0.17026 | 0.17096/0.16966 | 0.17172 | sup 0.16712 (ha 6 candles) | 0.00284 | 0.0028% | — | zona_expirada_setup_A |
| 2026-10-24 04:06 | WLD-USDT-SWAP | 0.47430 | 0.47780/0.47410 | 0.47960 | — | 0.00946 | 0.0073% | — | invalidado_setup_B |
| 2026-10-24 04:06 | SUI-USDT-SWAP | 0.95700 | 0.95980/0.95480 | 0.96230 | sup 0.93870 (ha 8 candles) | 0.01113 | 0.0091% | — | sem_zona |
| 2026-10-24 04:06 | UNI-USDT-SWAP | 6.9100 | 6.9390/6.8970 | 6.9650 | sup 6.7930 (ha 8 candles) | 0.09707 | 0.0095% | — | sem_zona |
| 2026-10-24 04:06 | LINK-USDT-SWAP | 11.79 | 11.82/11.78 | 11.86 | sup 11.59 (ha 8 candles) | 0.10586 | 0.0100% | — | sem_zona |
| 2026-10-24 05:06 | BTC-USDT-SWAP | 80699.9 | 80888.5/80666.9 | 80699.9 | sup 80456.6 (ha 8 candles) | 333.28 | 0.0052% | — | sem_zona |
| 2026-10-24 05:06 | ETH-USDT-SWAP | 2373.9 | 2383.3/2372.2 | 2373.9 | sup 2350.1 (ha 9 candles) | 14.56 | 0.0091% | — | sem_zona |
| 2026-10-24 05:06 | SOL-USDT-SWAP | 101.87 | 102.40/101.76 | 101.87 | sup 101.64 (ha 9 candles) | 0.72357 | 0.0100% | — | sem_zona |
| 2026-10-24 05:06 | XRP-USDT-SWAP | 1.2845 | 1.2917/1.2832 | 1.2845 | — | 0.00891 | 0.0028% | B/compra@1.2886 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-24 05:06 | DOGE-USDT-SWAP | 0.07777 | 0.07843/0.07755 | 0.07777 | sup 0.07734 (ha 9 candles) | 0.00065 | 0.0040% | — | sem_zona |
| 2026-10-24 05:06 | ARB-USDT-SWAP | 0.16847 | 0.17092/0.16828 | 0.16847 | sup 0.16712 (ha 7 candles) | 0.00287 | 0.0025% | — | sem_zona |
| 2026-10-24 05:06 | WLD-USDT-SWAP | 0.47230 | 0.47710/0.46720 | 0.47230 | — | 0.00981 | 0.0074% | B/compra@0.47260 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-24 05:06 | SUI-USDT-SWAP | 0.94860 | 0.96090/0.94780 | 0.94860 | sup 0.93870 (ha 9 candles) | 0.01165 | 0.0096% | — | sem_zona |
| 2026-10-24 05:06 | UNI-USDT-SWAP | 6.8480 | 6.9380/6.8370 | 6.8480 | sup 6.7930 (ha 9 candles) | 0.10057 | 0.0073% | — | sem_zona |
| 2026-10-24 05:06 | LINK-USDT-SWAP | 11.71 | 11.82/11.70 | 11.71 | sup 11.59 (ha 9 candles) | 0.11071 | 0.0099% | — | sem_zona |
| 2026-10-24 06:06 | BTC-USDT-SWAP | 80680.2 | 80790.0/80593.8 | 80699.9 | sup 80456.6 (ha 9 candles) | 329.26 | 0.0069% | — | sem_zona |
| 2026-10-24 06:06 | ETH-USDT-SWAP | 2368.3 | 2375.8/2366.0 | 2373.9 | sup 2350.1 (ha 10 candles) | 14.51 | 0.0097% | — | sem_zona |
| 2026-10-24 06:06 | SOL-USDT-SWAP | 101.92 | 102.16/101.71 | 101.87 | sup 101.64 (ha 10 candles) | 0.72000 | 0.0100% | — | sem_zona |
| 2026-10-24 06:06 | XRP-USDT-SWAP | 1.2801 | 1.2856/1.2783 | 1.2845 | — | 0.00903 | 0.0011% | B/compra@1.2886 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-24 06:06 | DOGE-USDT-SWAP | 0.07753 | 0.07789/0.07742 | 0.07777 | sup 0.07734 (ha 10 candles) | 0.00065 | 0.0053% | — | sem_zona |
| 2026-10-24 06:06 | ARB-USDT-SWAP | 0.16899 | 0.16950/0.16813 | 0.16847 | sup 0.16712 (ha 8 candles) | 0.00276 | 0.0043% | — | sem_zona |
| 2026-10-24 06:06 | WLD-USDT-SWAP | 0.46860 | 0.47450/0.46600 | 0.47230 | — | 0.00989 | 0.0095% | — | invalidado_setup_B |
| 2026-10-24 06:06 | SUI-USDT-SWAP | 0.94670 | 0.95070/0.94500 | 0.94860 | sup 0.93870 (ha 10 candles) | 0.01140 | 0.0100% | — | sem_zona |
| 2026-10-24 06:06 | UNI-USDT-SWAP | 6.8380 | 6.8700/6.8220 | 6.8480 | sup 6.7930 (ha 10 candles) | 0.09871 | 0.0063% | — | sem_zona |
| 2026-10-24 06:06 | LINK-USDT-SWAP | 11.64 | 11.73/11.62 | 11.71 | sup 11.59 (ha 10 candles) | 0.11207 | 0.0100% | — | sem_zona |
| 2026-10-24 07:06 | BTC-USDT-SWAP | 80593.8 | 80680.3/80390.5 | 80699.9 | sup 80456.6 (ha 10 candles) | 334.06 | 0.0083% | — | sem_zona |
| 2026-10-24 07:06 | ETH-USDT-SWAP | 2366.5 | 2368.5/2356.1 | 2373.9 | sup 2350.1 (ha 11 candles) | 14.72 | 0.0100% | — | sem_zona |
| 2026-10-24 07:06 | SOL-USDT-SWAP | 101.36 | 101.94/101.08 | 101.87 | sup 101.64 (ha 11 candles) | 0.73214 | 0.0100% | A/venda@101.64 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-24 07:06 | XRP-USDT-SWAP | 1.2762 | 1.2809/1.2725 | 1.2845 | — | 0.00892 | -0.0006% | B/compra@1.2886 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-24 07:06 | DOGE-USDT-SWAP | 0.07725 | 0.07757/0.07682 | 0.07777 | sup 0.07734 (ha 11 candles) | 0.00066 | 0.0043% | A/venda@0.07734 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-24 07:06 | ARB-USDT-SWAP | 0.16910 | 0.16940/0.16814 | 0.16847 | sup 0.16712 (ha 9 candles) | 0.00266 | 0.0056% | — | sem_zona |
| 2026-10-24 07:06 | WLD-USDT-SWAP | 0.46760 | 0.46890/0.46390 | 0.47230 | — | 0.00936 | 0.0100% | B/compra@0.46070 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-24 07:06 | SUI-USDT-SWAP | 0.94370 | 0.94720/0.93880 | 0.94860 | sup 0.93870 (ha 11 candles) | 0.01113 | 0.0100% | — | sem_zona |
| 2026-10-24 07:06 | UNI-USDT-SWAP | 6.8350 | 6.8450/6.7820 | 6.8480 | sup 6.7930 (ha 11 candles) | 0.09786 | 0.0039% | — | sem_zona |
| 2026-10-24 07:06 | LINK-USDT-SWAP | 11.56 | 11.63/11.52 | 11.71 | sup 11.59 (ha 11 candles) | 0.11379 | 0.0081% | A/venda@11.59 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-24 08:06 | BTC-USDT-SWAP | 80638.8 | 80712.2/80488.0 | 80699.9 | sup 80456.6 (ha 11 candles) | 333.53 | 0.0099% | — | sem_zona |
| 2026-10-24 08:06 | ETH-USDT-SWAP | 2369.0 | 2372.7/2363.1 | 2373.9 | sup 2350.1 (ha 12 candles) | 14.58 | 0.0100% | — | sem_zona |
| 2026-10-24 08:06 | SOL-USDT-SWAP | 101.68 | 101.82/101.30 | 101.87 | sup 101.64 (ha 12 candles) | 0.72000 | 0.0100% | A/venda@101.64 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-24 08:06 | XRP-USDT-SWAP | 1.2813 | 1.2827/1.2749 | 1.2845 | — | 0.00884 | -0.0005% | B/compra@1.2886 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-24 08:06 | DOGE-USDT-SWAP | 0.07756 | 0.07757/0.07714 | 0.07777 | sup 0.07734 (ha 12 candles) | 0.00066 | 0.0038% | — | invalidado_setup_A |
| 2026-10-24 08:06 | ARB-USDT-SWAP | 0.16876 | 0.16943/0.16813 | 0.16847 | sup 0.16712 (ha 10 candles) | 0.00256 | 0.0048% | — | sem_zona |
| 2026-10-24 08:06 | WLD-USDT-SWAP | 0.46980 | 0.47110/0.46550 | 0.47230 | — | 0.00935 | 0.0046% | B/compra@0.46070 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-24 08:06 | SUI-USDT-SWAP | 0.94720 | 0.94870/0.94210 | 0.94860 | sup 0.93870 (ha 12 candles) | 0.01099 | 0.0100% | — | sem_zona |
| 2026-10-24 08:06 | UNI-USDT-SWAP | 6.8670 | 6.8800/6.8230 | 6.8480 | sup 6.7930 (ha 12 candles) | 0.09579 | 0.0034% | — | sem_zona |
| 2026-10-24 08:06 | LINK-USDT-SWAP | 11.61 | 11.62/11.54 | 11.71 | sup 11.59 (ha 12 candles) | 0.11393 | 0.0057% | A/venda@11.59 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-24 09:06 | BTC-USDT-SWAP | 80563.3 | 80684.8/80541.2 | 80563.3 | sup 80456.6 (ha 12 candles) | 331.21 | 0.0100% | — | sem_zona |
| 2026-10-24 09:06 | ETH-USDT-SWAP | 2364.6 | 2371.5/2363.9 | 2364.6 | sup 2350.1 (ha 13 candles) | 14.47 | 0.0100% | — | sem_zona |
| 2026-10-24 09:06 | SOL-USDT-SWAP | 101.48 | 101.71/101.24 | 101.48 | sup 101.64 (ha 13 candles) | 0.71071 | 0.0100% | A/venda@101.64 (2t/0c) | zona_mapeada_setup_A |
| 2026-10-24 09:06 | XRP-USDT-SWAP | 1.2808 | 1.2827/1.2775 | 1.2808 | — | 0.00881 | -0.0010% | B/compra@1.2886 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-24 09:06 | DOGE-USDT-SWAP | 0.07755 | 0.07765/0.07734 | 0.07755 | sup 0.07734 (ha 13 candles) | 0.00065 | 0.0031% | — | sem_zona |
| 2026-10-24 09:06 | ARB-USDT-SWAP | 0.16893 | 0.16911/0.16838 | 0.16893 | sup 0.16813 (ha 3 candles) | 0.00249 | 0.0033% | — | sem_zona |
| 2026-10-24 09:06 | WLD-USDT-SWAP | 0.47210 | 0.47270/0.46820 | 0.47210 | — | 0.00909 | -0.0016% | B/compra@0.46070 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-24 09:06 | SUI-USDT-SWAP | 0.94760 | 0.94870/0.94470 | 0.94760 | sup 0.93870 (ha 13 candles) | 0.01071 | 0.0100% | — | sem_zona |
| 2026-10-24 09:06 | UNI-USDT-SWAP | 6.8100 | 6.8810/6.8040 | 6.8100 | sup 6.7930 (ha 13 candles) | 0.09579 | 0.0047% | — | sem_zona |
| 2026-10-24 09:06 | LINK-USDT-SWAP | 11.60 | 11.63/11.59 | 11.60 | sup 11.59 (ha 13 candles) | 0.11079 | 0.0040% | — | descartado_rr_baixo_setup_A |
| 2026-10-24 10:06 | BTC-USDT-SWAP | 80737.6 | 80813.0/80516.0 | 80563.3 | sup 80390.5 (ha 3 candles) | 288.66 | 0.0100% | — | sem_zona |
| 2026-10-24 10:06 | ETH-USDT-SWAP | 2368.2 | 2372.3/2362.3 | 2364.6 | sup 2356.1 (ha 3 candles) | 11.46 | 0.0100% | — | sem_zona |
| 2026-10-24 10:06 | SOL-USDT-SWAP | 101.54 | 101.69/101.27 | 101.48 | sup 101.08 (ha 3 candles) | 0.58571 | 0.0084% | — | zona_expirada_setup_A |
| 2026-10-24 10:06 | XRP-USDT-SWAP | 1.2841 | 1.2869/1.2786 | 1.2808 | — | 0.00739 | -0.0025% | — | invalidado_setup_B |
| 2026-10-24 10:06 | DOGE-USDT-SWAP | 0.07752 | 0.07773/0.07727 | 0.07755 | sup 0.07682 (ha 3 candles) | 0.00053 | -0.0010% | — | sem_zona |
| 2026-10-24 10:06 | ARB-USDT-SWAP | 0.17070 | 0.17148/0.16846 | 0.16893 | sup 0.16813 (ha 4 candles) | 0.00206 | 0.0016% | — | sem_zona |
| 2026-10-24 10:06 | WLD-USDT-SWAP | 0.47040 | 0.47380/0.46930 | 0.47210 | — | 0.00659 | -0.0082% | B/compra@0.46070 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-24 10:06 | SUI-USDT-SWAP | 0.94760 | 0.95230/0.94610 | 0.94760 | sup 0.93880 (ha 3 candles) | 0.00839 | 0.0087% | — | sem_zona |
| 2026-10-24 10:06 | UNI-USDT-SWAP | 6.8210 | 6.8520/6.7900 | 6.8100 | sup 6.7820 (ha 3 candles) | 0.07771 | 0.0051% | — | sem_zona |
| 2026-10-24 10:06 | LINK-USDT-SWAP | 11.62 | 11.64/11.57 | 11.60 | sup 11.52 (ha 3 candles) | 0.08986 | 0.0024% | — | sem_zona |
| 2026-10-24 11:06 | BTC-USDT-SWAP | 80670.2 | 80817.8/80623.0 | 80563.3 | sup 80390.5 (ha 4 candles) | 252.34 | 0.0100% | — | sem_zona |
| 2026-10-24 11:06 | ETH-USDT-SWAP | 2367.3 | 2371.9/2364.0 | 2364.6 | sup 2356.1 (ha 4 candles) | 9.7829 | 0.0092% | — | sem_zona |
| 2026-10-24 11:06 | SOL-USDT-SWAP | 101.37 | 101.75/101.18 | 101.48 | sup 101.08 (ha 4 candles) | 0.54286 | 0.0062% | — | sem_zona |
| 2026-10-24 11:06 | XRP-USDT-SWAP | 1.2832 | 1.2873/1.2806 | 1.2808 | — | 0.00689 | -0.0035% | B/compra@1.2856 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-24 11:06 | DOGE-USDT-SWAP | 0.07749 | 0.07768/0.07727 | 0.07755 | sup 0.07682 (ha 4 candles) | 0.00047 | -0.0036% | — | sem_zona |
| 2026-10-24 11:06 | ARB-USDT-SWAP | 0.16882 | 0.17129/0.16881 | 0.16893 | sup 0.16813 (ha 3 candles) | 0.00200 | -0.0012% | — | sem_zona |
| 2026-10-24 11:06 | WLD-USDT-SWAP | 0.46660 | 0.47160/0.46380 | 0.47210 | — | 0.00651 | -0.0111% | B/compra@0.46070 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-24 11:06 | SUI-USDT-SWAP | 0.94420 | 0.95040/0.94180 | 0.94760 | sup 0.93880 (ha 4 candles) | 0.00762 | 0.0063% | — | sem_zona |
| 2026-10-24 11:06 | UNI-USDT-SWAP | 6.8480 | 6.8560/6.8050 | 6.8100 | sup 6.7820 (ha 4 candles) | 0.07029 | 0.0043% | — | sem_zona |
| 2026-10-24 11:06 | LINK-USDT-SWAP | 11.58 | 11.65/11.57 | 11.60 | sup 11.52 (ha 4 candles) | 0.08186 | 0.0028% | — | sem_zona |
| 2026-10-24 12:06 | BTC-USDT-SWAP | 80168.7 | 80730.2/79758.0 | 80563.3 | sup 80390.5 (ha 5 candles) | 277.79 | 0.0079% | A/venda@80390.5 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-24 12:06 | ETH-USDT-SWAP | 2341.2 | 2369.1/2326.8 | 2364.6 | sup 2356.1 (ha 5 candles) | 11.43 | 0.0061% | A/venda@2356.1 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-24 12:06 | SOL-USDT-SWAP | 100.33 | 101.45/99.58 | 101.48 | sup 101.08 (ha 5 candles) | 0.61214 | 0.0020% | A/venda@101.08 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-24 12:06 | XRP-USDT-SWAP | 1.2732 | 1.2854/1.2644 | 1.2808 | — | 0.00749 | -0.0028% | — | invalidado_setup_B |
| 2026-10-24 12:06 | DOGE-USDT-SWAP | 0.07615 | 0.07760/0.07546 | 0.07755 | sup 0.07682 (ha 5 candles) | 0.00058 | -0.0025% | A/venda@0.07682 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-24 12:06 | ARB-USDT-SWAP | 0.16714 | 0.16902/0.16433 | 0.16893 | sup 0.16813 (ha 4 candles) | 0.00201 | -0.0017% | A/venda@0.16813 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-24 12:06 | WLD-USDT-SWAP | 0.46350 | 0.47000/0.45720 | 0.47210 | — | 0.00661 | -0.0108% | B/compra@0.46070 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-24 12:06 | SUI-USDT-SWAP | 0.92760 | 0.94570/0.91440 | 0.94760 | sup 0.93880 (ha 5 candles) | 0.00892 | 0.0037% | A/venda@0.93880 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-24 12:06 | UNI-USDT-SWAP | 6.6980 | 6.8600/6.5990 | 6.8100 | sup 6.7820 (ha 5 candles) | 0.08057 | 0.0032% | A/venda@6.7820 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-24 12:06 | LINK-USDT-SWAP | 11.46 | 11.61/11.35 | 11.60 | sup 11.52 (ha 5 candles) | 0.09086 | 0.0021% | A/venda@11.52 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-24 13:06 | BTC-USDT-SWAP | 79755.1 | 80194.4/79168.0 | 79755.1 | sup 80390.5 (ha 6 candles) | 325.68 | 0.0044% | A/venda@80390.5 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-24 13:06 | ETH-USDT-SWAP | 2304.7 | 2342.4/2281.0 | 2304.7 | sup 2356.1 (ha 6 candles) | 14.99 | 0.0018% | A/venda@2356.1 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-24 13:06 | SOL-USDT-SWAP | 99.73 | 100.43/98.54 | 99.73 | sup 101.08 (ha 6 candles) | 0.70786 | -0.0009% | A/venda@101.08 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-24 13:06 | XRP-USDT-SWAP | 1.2676 | 1.2745/1.2539 | 1.2676 | — | 0.00844 | -0.0035% | B/compra@1.2692 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-24 13:06 | DOGE-USDT-SWAP | 0.07565 | 0.07620/0.07469 | 0.07565 | sup 0.07682 (ha 6 candles) | 0.00065 | -0.0034% | A/venda@0.07682 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-24 13:06 | ARB-USDT-SWAP | 0.16571 | 0.16739/0.16332 | 0.16571 | sup 0.16813 (ha 5 candles) | 0.00212 | -0.0008% | A/venda@0.16813 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-24 13:06 | WLD-USDT-SWAP | 0.46190 | 0.46480/0.45790 | 0.46190 | — | 0.00670 | -0.0097% | B/compra@0.46070 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-24 13:06 | SUI-USDT-SWAP | 0.92490 | 0.92900/0.91080 | 0.92490 | sup 0.93880 (ha 6 candles) | 0.00951 | 0.0013% | A/venda@0.93880 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-24 13:06 | UNI-USDT-SWAP | 6.6020 | 6.7060/6.5130 | 6.6020 | sup 6.7820 (ha 6 candles) | 0.08786 | 0.0000% | A/venda@6.7820 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-24 13:06 | LINK-USDT-SWAP | 11.38 | 11.47/11.23 | 11.38 | sup 11.52 (ha 6 candles) | 0.10121 | -0.0005% | A/venda@11.52 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-24 14:06 | BTC-USDT-SWAP | 80175.1 | 80266.4/79526.9 | 79755.1 | sup 80390.5 (ha 7 candles) | 367.00 | 0.0019% | A/venda@80390.5 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-24 14:06 | ETH-USDT-SWAP | 2317.0 | 2320.4/2293.0 | 2304.7 | sup 2356.1 (ha 7 candles) | 16.48 | -0.0006% | A/venda@2356.1 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-24 14:06 | SOL-USDT-SWAP | 100.44 | 100.62/99.42 | 99.73 | sup 101.08 (ha 7 candles) | 0.76929 | -0.0020% | A/venda@101.08 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-24 14:06 | XRP-USDT-SWAP | 1.2764 | 1.2774/1.2624 | 1.2676 | — | 0.00924 | -0.0031% | — | descartado_rr_baixo_setup_B |
| 2026-10-24 14:06 | DOGE-USDT-SWAP | 0.07643 | 0.07648/0.07546 | 0.07565 | sup 0.07682 (ha 7 candles) | 0.00071 | -0.0025% | A/venda@0.07682 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-24 14:06 | ARB-USDT-SWAP | 0.16595 | 0.16649/0.16366 | 0.16571 | sup 0.16813 (ha 6 candles) | 0.00218 | 0.0031% | A/venda@0.16813 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-24 14:06 | WLD-USDT-SWAP | 0.46460 | 0.46710/0.45780 | 0.46190 | — | 0.00684 | -0.0101% | — | descartado_rr_baixo_setup_B |
| 2026-10-24 14:06 | SUI-USDT-SWAP | 0.92980 | 0.93200/0.91800 | 0.92490 | sup 0.93880 (ha 7 candles) | 0.01016 | -0.0002% | A/venda@0.93880 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-24 14:06 | UNI-USDT-SWAP | 6.6620 | 6.6700/6.5450 | 6.6020 | sup 6.7820 (ha 7 candles) | 0.09307 | -0.0013% | A/venda@6.7820 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-24 14:06 | LINK-USDT-SWAP | 11.46 | 11.47/11.31 | 11.38 | sup 11.52 (ha 7 candles) | 0.10893 | -0.0015% | A/venda@11.52 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-24 15:06 | BTC-USDT-SWAP | 80233.5 | 80280.4/80065.0 | 79755.1 | sup 80390.5 (ha 8 candles) | 364.88 | 0.0004% | A/venda@80390.5 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-24 15:06 | ETH-USDT-SWAP | 2321.8 | 2325.9/2313.1 | 2304.7 | sup 2356.1 (ha 8 candles) | 16.60 | -0.0021% | A/venda@2356.1 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-24 15:06 | SOL-USDT-SWAP | 100.45 | 100.53/100.04 | 99.73 | sup 101.08 (ha 8 candles) | 0.75857 | -0.0015% | A/venda@101.08 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-24 15:06 | XRP-USDT-SWAP | 1.2758 | 1.2789/1.2727 | 1.2676 | — | 0.00914 | -0.0023% | B/compra@1.2826 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-24 15:06 | DOGE-USDT-SWAP | 0.07646 | 0.07654/0.07615 | 0.07565 | sup 0.07682 (ha 8 candles) | 0.00070 | -0.0004% | A/venda@0.07682 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-24 15:06 | ARB-USDT-SWAP | 0.16545 | 0.16600/0.16378 | 0.16571 | sup 0.16813 (ha 7 candles) | 0.00219 | 0.0056% | A/venda@0.16813 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-24 15:06 | WLD-USDT-SWAP | 0.45830 | 0.46470/0.45710 | 0.46190 | — | 0.00694 | -0.0108% | B/compra@0.45610 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-24 15:06 | SUI-USDT-SWAP | 0.92380 | 0.93000/0.91980 | 0.92490 | sup 0.93880 (ha 8 candles) | 0.01026 | 0.0018% | A/venda@0.93880 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-24 15:06 | UNI-USDT-SWAP | 6.6650 | 6.6890/6.6230 | 6.6020 | sup 6.7820 (ha 8 candles) | 0.09164 | -0.0034% | A/venda@6.7820 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-24 15:06 | LINK-USDT-SWAP | 11.42 | 11.46/11.39 | 11.38 | sup 11.52 (ha 8 candles) | 0.10893 | 0.0001% | A/venda@11.52 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-24 16:06 | BTC-USDT-SWAP | 80502.5 | 80600.0/80209.0 | 79755.1 | sup 79168.0 (ha 3 candles) | 374.28 | -0.0002% | — | invalidado_setup_A |
| 2026-10-24 16:06 | ETH-USDT-SWAP | 2336.8 | 2341.7/2321.2 | 2304.7 | sup 2281.0 (ha 3 candles) | 17.61 | -0.0033% | A/venda@2356.1 (0t/4c) | zona_mapeada_setup_A |
| 2026-10-24 16:06 | SOL-USDT-SWAP | 101.26 | 101.42/100.42 | 99.73 | sup 98.54 (ha 3 candles) | 0.80571 | -0.0006% | — | invalidado_setup_A |
| 2026-10-24 16:06 | XRP-USDT-SWAP | 1.2861 | 1.2884/1.2747 | 1.2676 | — | 0.00981 | -0.0018% | — | descartado_rr_baixo_setup_B |
| 2026-10-24 16:06 | DOGE-USDT-SWAP | 0.07705 | 0.07720/0.07637 | 0.07565 | sup 0.07469 (ha 3 candles) | 0.00074 | 0.0021% | — | invalidado_setup_A |
| 2026-10-24 16:06 | ARB-USDT-SWAP | 0.16816 | 0.16860/0.16525 | 0.16571 | sup 0.16332 (ha 3 candles) | 0.00232 | 0.0072% | A/venda@0.16813 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-24 16:06 | WLD-USDT-SWAP | 0.46680 | 0.46820/0.45800 | 0.46190 | — | 0.00734 | -0.0121% | B/compra@0.45610 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-24 16:06 | SUI-USDT-SWAP | 0.93580 | 0.93790/0.92230 | 0.92490 | sup 0.91080 (ha 3 candles) | 0.01096 | 0.0006% | A/venda@0.93880 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-24 16:06 | UNI-USDT-SWAP | 6.7580 | 6.7790/6.6640 | 6.6020 | sup 6.5130 (ha 3 candles) | 0.09514 | -0.0034% | A/venda@6.7820 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-24 16:06 | LINK-USDT-SWAP | 11.53 | 11.56/11.41 | 11.38 | sup 11.23 (ha 3 candles) | 0.11479 | 0.0009% | A/venda@11.52 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-24 17:06 | BTC-USDT-SWAP | 80443.8 | 80576.7/80443.7 | 80443.8 | sup 79168.0 (ha 4 candles) | 370.83 | -0.0000% | — | sem_zona |
| 2026-10-24 17:06 | ETH-USDT-SWAP | 2338.4 | 2340.8/2334.4 | 2338.4 | sup 2281.0 (ha 4 candles) | 17.55 | -0.0040% | A/venda@2356.1 (0t/5c) | zona_mapeada_setup_A |
| 2026-10-24 17:06 | SOL-USDT-SWAP | 101.10 | 101.32/101.00 | 101.10 | sup 98.54 (ha 4 candles) | 0.79286 | 0.0010% | — | sem_zona |
| 2026-10-24 17:06 | XRP-USDT-SWAP | 1.2882 | 1.2906/1.2847 | 1.2882 | — | 0.00986 | -0.0015% | B/compra@1.2943 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-24 17:06 | DOGE-USDT-SWAP | 0.07707 | 0.07718/0.07691 | 0.07707 | sup 0.07469 (ha 4 candles) | 0.00072 | 0.0015% | — | sem_zona |
| 2026-10-24 17:06 | ARB-USDT-SWAP | 0.16735 | 0.16818/0.16678 | 0.16735 | sup 0.16332 (ha 4 candles) | 0.00233 | 0.0059% | A/venda@0.16813 (2t/0c) | zona_mapeada_setup_A |
| 2026-10-24 17:06 | WLD-USDT-SWAP | 0.46390 | 0.46670/0.46250 | 0.46390 | — | 0.00719 | -0.0121% | B/compra@0.45610 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-24 17:06 | SUI-USDT-SWAP | 0.93500 | 0.93730/0.93320 | 0.93500 | sup 0.91080 (ha 4 candles) | 0.01079 | -0.0013% | A/venda@0.93880 (2t/0c) | zona_mapeada_setup_A |
| 2026-10-24 17:06 | UNI-USDT-SWAP | 6.7690 | 6.7800/6.7470 | 6.7690 | sup 6.5130 (ha 4 candles) | 0.09243 | -0.0014% | A/venda@6.7820 (2t/0c) | zona_mapeada_setup_A |
| 2026-10-24 17:06 | LINK-USDT-SWAP | 11.54 | 11.55/11.51 | 11.54 | sup 11.23 (ha 4 candles) | 0.11200 | 0.0015% | A/venda@11.52 (2t/0c) | zona_mapeada_setup_A |
| 2026-10-24 18:06 | BTC-USDT-SWAP | 80480.5 | 80588.0/80443.8 | 80443.8 | sup 79168.0 (ha 5 candles) | 370.64 | 0.0002% | — | sem_zona |
| 2026-10-24 18:06 | ETH-USDT-SWAP | 2346.0 | 2349.0/2338.4 | 2338.4 | sup 2281.0 (ha 5 candles) | 17.85 | -0.0028% | A/venda@2356.1 (0t/6c) | zona_mapeada_setup_A |
| 2026-10-24 18:06 | SOL-USDT-SWAP | 101.54 | 101.65/101.11 | 101.10 | sup 98.54 (ha 5 candles) | 0.80357 | 0.0032% | — | sem_zona |
| 2026-10-24 18:06 | XRP-USDT-SWAP | 1.2908 | 1.2944/1.2882 | 1.2882 | — | 0.01006 | -0.0005% | — | invalidado_setup_B |
| 2026-10-24 18:06 | DOGE-USDT-SWAP | 0.07724 | 0.07747/0.07706 | 0.07707 | sup 0.07469 (ha 5 candles) | 0.00073 | -0.0004% | — | sem_zona |
| 2026-10-24 18:06 | ARB-USDT-SWAP | 0.16759 | 0.16886/0.16734 | 0.16735 | sup 0.16332 (ha 5 candles) | 0.00235 | 0.0032% | — | zona_expirada_setup_A |
| 2026-10-24 18:06 | WLD-USDT-SWAP | 0.46620 | 0.46980/0.46400 | 0.46390 | — | 0.00734 | -0.0140% | B/compra@0.45610 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-24 18:06 | SUI-USDT-SWAP | 0.93660 | 0.94060/0.93500 | 0.93500 | sup 0.91080 (ha 5 candles) | 0.01083 | -0.0029% | — | zona_expirada_setup_A |
| 2026-10-24 18:06 | UNI-USDT-SWAP | 6.8000 | 6.8270/6.7700 | 6.7690 | sup 6.5130 (ha 5 candles) | 0.09357 | 0.0003% | — | zona_expirada_setup_A |
| 2026-10-24 18:06 | LINK-USDT-SWAP | 11.57 | 11.61/11.54 | 11.54 | sup 11.23 (ha 5 candles) | 0.11414 | 0.0027% | — | invalidado_setup_A |
| 2026-10-24 19:06 | BTC-USDT-SWAP | 80380.9 | 80484.7/80260.0 | 80443.8 | sup 79168.0 (ha 6 candles) | 370.86 | 0.0010% | — | sem_zona |
| 2026-10-24 19:06 | ETH-USDT-SWAP | 2339.1 | 2346.3/2333.0 | 2338.4 | sup 2281.0 (ha 6 candles) | 18.00 | -0.0015% | A/venda@2356.1 (0t/7c) | zona_mapeada_setup_A |
| 2026-10-24 19:06 | SOL-USDT-SWAP | 101.33 | 101.55/101.05 | 101.10 | sup 98.54 (ha 6 candles) | 0.79357 | 0.0052% | — | sem_zona |
| 2026-10-24 19:06 | XRP-USDT-SWAP | 1.2920 | 1.2942/1.2888 | 1.2882 | — | 0.00984 | 0.0013% | B/compra@1.2856 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-24 19:06 | DOGE-USDT-SWAP | 0.07709 | 0.07726/0.07691 | 0.07707 | sup 0.07469 (ha 6 candles) | 0.00070 | -0.0008% | — | sem_zona |
| 2026-10-24 19:06 | ARB-USDT-SWAP | 0.16653 | 0.16761/0.16640 | 0.16735 | sup 0.16332 (ha 6 candles) | 0.00225 | 0.0040% | — | sem_zona |
| 2026-10-24 19:06 | WLD-USDT-SWAP | 0.46330 | 0.46650/0.46200 | 0.46390 | — | 0.00696 | -0.0116% | B/compra@0.45610 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-24 19:06 | SUI-USDT-SWAP | 0.92840 | 0.93690/0.92790 | 0.93500 | sup 0.91080 (ha 6 candles) | 0.01054 | -0.0029% | — | sem_zona |
| 2026-10-24 19:06 | UNI-USDT-SWAP | 6.7670 | 6.8050/6.7550 | 6.7690 | sup 6.5130 (ha 6 candles) | 0.08993 | 0.0036% | — | sem_zona |
| 2026-10-24 19:06 | LINK-USDT-SWAP | 11.52 | 11.57/11.49 | 11.54 | sup 11.23 (ha 6 candles) | 0.11136 | 0.0063% | — | sem_zona |
| 2026-10-24 20:06 | BTC-USDT-SWAP | 80563.3 | 80616.6/80380.9 | 80443.8 | sup 79168.0 (ha 7 candles) | 373.68 | 0.0016% | — | sem_zona |
| 2026-10-24 20:06 | ETH-USDT-SWAP | 2345.5 | 2345.5/2339.0 | 2338.4 | sup 2281.0 (ha 7 candles) | 17.76 | 0.0006% | — | zona_expirada_setup_A |
| 2026-10-24 20:06 | SOL-USDT-SWAP | 101.56 | 101.70/101.33 | 101.10 | sup 98.54 (ha 7 candles) | 0.78786 | 0.0058% | — | sem_zona |
| 2026-10-24 20:06 | XRP-USDT-SWAP | 1.2933 | 1.2955/1.2899 | 1.2882 | — | 0.00971 | 0.0033% | B/compra@1.2856 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-24 20:06 | DOGE-USDT-SWAP | 0.07734 | 0.07737/0.07708 | 0.07707 | sup 0.07469 (ha 7 candles) | 0.00068 | -0.0021% | — | sem_zona |
| 2026-10-24 20:06 | ARB-USDT-SWAP | 0.16751 | 0.16774/0.16640 | 0.16735 | sup 0.16332 (ha 7 candles) | 0.00224 | 0.0008% | — | sem_zona |
| 2026-10-24 20:06 | WLD-USDT-SWAP | 0.46450 | 0.46490/0.45830 | 0.46390 | — | 0.00682 | -0.0068% | B/compra@0.45610 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-24 20:06 | SUI-USDT-SWAP | 0.93230 | 0.93240/0.92820 | 0.93500 | sup 0.91080 (ha 7 candles) | 0.01043 | -0.0023% | — | sem_zona |
| 2026-10-24 20:06 | UNI-USDT-SWAP | 6.8170 | 6.8250/6.7640 | 6.7690 | sup 6.5130 (ha 7 candles) | 0.09086 | 0.0046% | — | sem_zona |
| 2026-10-24 20:06 | LINK-USDT-SWAP | 11.56 | 11.57/11.52 | 11.54 | sup 11.23 (ha 7 candles) | 0.10779 | 0.0079% | — | sem_zona |
| 2026-10-24 21:06 | BTC-USDT-SWAP | 80850.0 | 80897.6/80498.6 | 80850.0 | sup 79168.0 (ha 8 candles) | 381.48 | 0.0023% | — | sem_zona |
| 2026-10-24 21:06 | ETH-USDT-SWAP | 2357.4 | 2361.0/2341.7 | 2357.4 | sup 2281.0 (ha 8 candles) | 18.26 | 0.0013% | — | sem_zona |
| 2026-10-24 21:06 | SOL-USDT-SWAP | 102.30 | 102.52/101.50 | 102.30 | sup 98.54 (ha 8 candles) | 0.79929 | 0.0041% | — | sem_zona |
| 2026-10-24 21:06 | XRP-USDT-SWAP | 1.2988 | 1.3009/1.2910 | 1.2988 | — | 0.00982 | 0.0053% | B/compra@1.2856 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-24 21:06 | DOGE-USDT-SWAP | 0.07763 | 0.07777/0.07715 | 0.07763 | sup 0.07469 (ha 8 candles) | 0.00067 | -0.0026% | — | sem_zona |
| 2026-10-24 21:06 | ARB-USDT-SWAP | 0.16914 | 0.16986/0.16717 | 0.16914 | sup 0.16332 (ha 8 candles) | 0.00235 | -0.0023% | — | sem_zona |
| 2026-10-24 21:06 | WLD-USDT-SWAP | 0.46860 | 0.46980/0.46360 | 0.46860 | — | 0.00691 | -0.0077% | B/compra@0.45610 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-24 21:06 | SUI-USDT-SWAP | 0.93810 | 0.94120/0.93150 | 0.93810 | sup 0.91080 (ha 8 candles) | 0.01052 | -0.0011% | — | sem_zona |
| 2026-10-24 21:06 | UNI-USDT-SWAP | 6.8610 | 6.8930/6.8110 | 6.8610 | sup 6.5130 (ha 8 candles) | 0.09221 | 0.0050% | — | sem_zona |
| 2026-10-24 21:06 | LINK-USDT-SWAP | 11.62 | 11.65/11.55 | 11.62 | sup 11.23 (ha 8 candles) | 0.10636 | 0.0080% | — | sem_zona |
| 2026-10-24 22:06 | BTC-USDT-SWAP | 80844.4 | 80879.9/80732.6 | 80850.0 | sup 79168.0 (ha 9 candles) | 375.99 | 0.0032% | — | sem_zona |
| 2026-10-24 22:06 | ETH-USDT-SWAP | 2359.3 | 2362.7/2354.0 | 2357.4 | sup 2281.0 (ha 9 candles) | 18.19 | 0.0013% | — | sem_zona |
| 2026-10-24 22:06 | SOL-USDT-SWAP | 102.40 | 102.55/102.14 | 102.30 | sup 98.54 (ha 9 candles) | 0.79143 | 0.0016% | — | sem_zona |
| 2026-10-24 22:06 | XRP-USDT-SWAP | 1.3043 | 1.3059/1.2977 | 1.2988 | — | 0.00985 | 0.0049% | B/compra@1.2856 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-24 22:06 | DOGE-USDT-SWAP | 0.07783 | 0.07803/0.07754 | 0.07763 | sup 0.07469 (ha 9 candles) | 0.00068 | -0.0033% | — | sem_zona |
| 2026-10-24 22:06 | ARB-USDT-SWAP | 0.17068 | 0.17079/0.16892 | 0.16914 | sup 0.16332 (ha 9 candles) | 0.00239 | -0.0052% | — | sem_zona |
| 2026-10-24 22:06 | WLD-USDT-SWAP | 0.47000 | 0.47220/0.46660 | 0.46860 | — | 0.00691 | -0.0087% | B/compra@0.45610 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-24 22:06 | SUI-USDT-SWAP | 0.94010 | 0.94230/0.93640 | 0.93810 | sup 0.91080 (ha 9 candles) | 0.01047 | -0.0038% | — | sem_zona |
| 2026-10-24 22:06 | UNI-USDT-SWAP | 6.8710 | 6.8950/6.8510 | 6.8610 | sup 6.5130 (ha 9 candles) | 0.09129 | 0.0048% | — | sem_zona |
| 2026-10-24 22:06 | LINK-USDT-SWAP | 11.63 | 11.64/11.60 | 11.62 | sup 11.23 (ha 9 candles) | 0.10364 | 0.0089% | — | sem_zona |
| 2026-10-24 23:06 | BTC-USDT-SWAP | 80872.6 | 80895.2/80745.4 | 80850.0 | sup 79168.0 (ha 10 candles) | 376.43 | 0.0041% | — | sem_zona |
| 2026-10-24 23:06 | ETH-USDT-SWAP | 2363.5 | 2364.2/2354.9 | 2357.4 | sup 2281.0 (ha 10 candles) | 18.32 | 0.0013% | — | sem_zona |
| 2026-10-24 23:06 | SOL-USDT-SWAP | 102.43 | 102.54/102.11 | 102.30 | sup 98.54 (ha 10 candles) | 0.78857 | -0.0004% | — | sem_zona |
| 2026-10-24 23:06 | XRP-USDT-SWAP | 1.3067 | 1.3067/1.2997 | 1.2988 | — | 0.00998 | 0.0037% | B/compra@1.2856 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-24 23:06 | DOGE-USDT-SWAP | 0.07787 | 0.07796/0.07765 | 0.07763 | sup 0.07469 (ha 10 candles) | 0.00068 | -0.0033% | — | sem_zona |
| 2026-10-24 23:06 | ARB-USDT-SWAP | 0.16990 | 0.17072/0.16953 | 0.16914 | sup 0.16640 (ha 3 candles) | 0.00242 | -0.0088% | — | sem_zona |
| 2026-10-24 23:06 | WLD-USDT-SWAP | 0.46860 | 0.47270/0.46700 | 0.46860 | — | 0.00699 | -0.0102% | — | zona_expirada_setup_B |
| 2026-10-24 23:06 | SUI-USDT-SWAP | 0.93910 | 0.94010/0.93660 | 0.93810 | sup 0.91080 (ha 10 candles) | 0.01044 | -0.0030% | — | sem_zona |
| 2026-10-24 23:06 | UNI-USDT-SWAP | 6.8400 | 6.8750/6.8260 | 6.8610 | sup 6.5130 (ha 10 candles) | 0.08929 | 0.0064% | — | sem_zona |
| 2026-10-24 23:06 | LINK-USDT-SWAP | 11.62 | 11.63/11.59 | 11.62 | sup 11.23 (ha 10 candles) | 0.10364 | 0.0100% | — | sem_zona |
| 2026-10-25 00:06 | BTC-USDT-SWAP | 80880.1 | 80978.0/80778.0 | 80850.0 | sup 79168.0 (ha 11 candles) | 369.50 | 0.0060% | — | sem_zona |
| 2026-10-25 00:06 | ETH-USDT-SWAP | 2364.5 | 2371.0/2359.6 | 2357.4 | sup 2281.0 (ha 11 candles) | 18.41 | 0.0015% | — | sem_zona |
| 2026-10-25 00:06 | SOL-USDT-SWAP | 102.37 | 102.59/102.21 | 102.30 | sup 98.54 (ha 11 candles) | 0.78571 | -0.0031% | — | sem_zona |
| 2026-10-25 00:06 | XRP-USDT-SWAP | 1.3108 | 1.3125/1.3040 | 1.2988 | — | 0.00999 | 0.0031% | B/compra@1.2856 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-25 00:06 | DOGE-USDT-SWAP | 0.07771 | 0.07797/0.07767 | 0.07763 | sup 0.07469 (ha 11 candles) | 0.00067 | -0.0039% | — | sem_zona |
| 2026-10-25 00:06 | ARB-USDT-SWAP | 0.16848 | 0.17016/0.16848 | 0.16914 | sup 0.16640 (ha 4 candles) | 0.00232 | -0.0103% | — | sem_zona |
| 2026-10-25 00:06 | WLD-USDT-SWAP | 0.46620 | 0.47140/0.46580 | 0.46860 | — | 0.00707 | -0.0105% | — | sem_zona |
| 2026-10-25 00:06 | SUI-USDT-SWAP | 0.93510 | 0.94080/0.93430 | 0.93810 | sup 0.91080 (ha 11 candles) | 0.01046 | -0.0027% | — | sem_zona |
| 2026-10-25 00:06 | UNI-USDT-SWAP | 6.8170 | 6.8610/6.8090 | 6.8610 | sup 6.5130 (ha 11 candles) | 0.08857 | 0.0024% | — | sem_zona |
| 2026-10-25 00:06 | LINK-USDT-SWAP | 11.58 | 11.63/11.58 | 11.62 | sup 11.23 (ha 11 candles) | 0.10243 | 0.0100% | — | sem_zona |
| 2026-10-25 01:06 | BTC-USDT-SWAP | 80826.6 | 81008.0/80819.0 | 80826.6 | sup 79168.0 (ha 12 candles) | 369.09 | 0.0076% | — | sem_zona |
| 2026-10-25 01:06 | ETH-USDT-SWAP | 2361.6 | 2368.4/2360.7 | 2361.6 | sup 2281.0 (ha 12 candles) | 18.40 | 0.0010% | — | sem_zona |
| 2026-10-25 01:06 | SOL-USDT-SWAP | 102.37 | 102.67/102.29 | 102.37 | sup 98.54 (ha 12 candles) | 0.77214 | -0.0055% | — | sem_zona |
| 2026-10-25 01:06 | XRP-USDT-SWAP | 1.3104 | 1.3125/1.3082 | 1.3104 | sup 1.2539 (ha 12 candles) | 0.00982 | 0.0028% | B/compra@1.2856 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-25 01:06 | DOGE-USDT-SWAP | 0.07782 | 0.07790/0.07763 | 0.07782 | sup 0.07469 (ha 12 candles) | 0.00066 | -0.0051% | — | sem_zona |
| 2026-10-25 01:06 | ARB-USDT-SWAP | 0.16791 | 0.16887/0.16778 | 0.16791 | sup 0.16640 (ha 5 candles) | 0.00223 | -0.0076% | — | sem_zona |
| 2026-10-25 01:06 | WLD-USDT-SWAP | 0.46870 | 0.47170/0.46570 | 0.46870 | — | 0.00694 | -0.0116% | B/compra@0.47260 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-25 01:06 | SUI-USDT-SWAP | 0.93650 | 0.93950/0.93420 | 0.93650 | sup 0.91080 (ha 12 candles) | 0.01022 | -0.0038% | — | sem_zona |
| 2026-10-25 01:06 | UNI-USDT-SWAP | 6.8200 | 6.8430/6.8010 | 6.8200 | sup 6.5130 (ha 12 candles) | 0.08793 | -0.0002% | — | sem_zona |
| 2026-10-25 01:06 | LINK-USDT-SWAP | 11.58 | 11.62/11.57 | 11.58 | sup 11.23 (ha 12 candles) | 0.09950 | 0.0100% | — | sem_zona |
| 2026-10-25 02:06 | BTC-USDT-SWAP | 80896.3 | 80925.9/80786.1 | 80826.6 | sup 79168.0 (ha 13 candles) | 309.63 | 0.0082% | — | sem_zona |
| 2026-10-25 02:06 | ETH-USDT-SWAP | 2367.1 | 2368.6/2361.1 | 2361.6 | sup 2281.0 (ha 13 candles) | 15.91 | 0.0010% | — | sem_zona |
| 2026-10-25 02:06 | SOL-USDT-SWAP | 102.56 | 102.72/102.30 | 102.37 | sup 98.54 (ha 13 candles) | 0.66857 | -0.0061% | — | sem_zona |
| 2026-10-25 02:06 | XRP-USDT-SWAP | 1.3132 | 1.3153/1.3082 | 1.3104 | sup 1.2539 (ha 13 candles) | 0.00883 | 0.0029% | B/compra@1.2856 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-25 02:06 | DOGE-USDT-SWAP | 0.07788 | 0.07799/0.07778 | 0.07782 | sup 0.07469 (ha 13 candles) | 0.00052 | -0.0057% | — | sem_zona |
| 2026-10-25 02:06 | ARB-USDT-SWAP | 0.16754 | 0.16831/0.16741 | 0.16791 | sup 0.16640 (ha 6 candles) | 0.00195 | -0.0029% | — | sem_zona |
| 2026-10-25 02:06 | WLD-USDT-SWAP | 0.46920 | 0.47090/0.46740 | 0.46870 | — | 0.00628 | -0.0117% | — | invalidado_setup_B |
| 2026-10-25 02:06 | SUI-USDT-SWAP | 0.93190 | 0.93690/0.93180 | 0.93650 | sup 0.91080 (ha 13 candles) | 0.00835 | -0.0010% | — | sem_zona |
| 2026-10-25 02:06 | UNI-USDT-SWAP | 6.8220 | 6.8300/6.7960 | 6.8200 | sup 6.5130 (ha 13 candles) | 0.07171 | 0.0009% | — | sem_zona |
| 2026-10-25 02:06 | LINK-USDT-SWAP | 11.58 | 11.60/11.57 | 11.58 | sup 11.23 (ha 13 candles) | 0.08264 | 0.0100% | — | sem_zona |
| 2026-10-25 03:06 | BTC-USDT-SWAP | 80578.7 | 80896.7/80459.6 | 80826.6 | sup 79168.0 (ha 14 candles) | 267.54 | 0.0082% | — | sem_zona |
| 2026-10-25 03:06 | ETH-USDT-SWAP | 2352.3 | 2367.7/2345.9 | 2361.6 | sup 2281.0 (ha 14 candles) | 13.08 | 0.0001% | — | sem_zona |
| 2026-10-25 03:06 | SOL-USDT-SWAP | 101.91 | 102.58/101.68 | 102.37 | sup 98.54 (ha 14 candles) | 0.59786 | -0.0056% | — | sem_zona |
| 2026-10-25 03:06 | XRP-USDT-SWAP | 1.3000 | 1.3135/1.2982 | 1.3104 | sup 1.2539 (ha 14 candles) | 0.00845 | 0.0028% | — | zona_expirada_setup_B |
| 2026-10-25 03:06 | DOGE-USDT-SWAP | 0.07705 | 0.07790/0.07686 | 0.07782 | sup 0.07469 (ha 14 candles) | 0.00049 | -0.0068% | — | sem_zona |
| 2026-10-25 03:06 | ARB-USDT-SWAP | 0.16673 | 0.16776/0.16615 | 0.16791 | sup 0.16640 (ha 7 candles) | 0.00178 | -0.0012% | — | sem_zona |
| 2026-10-25 03:06 | WLD-USDT-SWAP | 0.46580 | 0.47030/0.46450 | 0.46870 | — | 0.00620 | -0.0091% | — | sem_zona |
| 2026-10-25 03:06 | SUI-USDT-SWAP | 0.91980 | 0.93210/0.91620 | 0.93650 | sup 0.91080 (ha 14 candles) | 0.00819 | 0.0023% | — | sem_zona |
| 2026-10-25 03:06 | UNI-USDT-SWAP | 6.7790 | 6.8410/6.7550 | 6.8200 | sup 6.5130 (ha 14 candles) | 0.06407 | 0.0013% | — | sem_zona |
| 2026-10-25 03:06 | LINK-USDT-SWAP | 11.44 | 11.58/11.42 | 11.58 | sup 11.23 (ha 14 candles) | 0.07707 | 0.0099% | — | sem_zona |
| 2026-10-25 04:06 | BTC-USDT-SWAP | 80467.3 | 80648.6/80391.7 | 80826.6 | sup 79168.0 (ha 15 candles) | 233.06 | 0.0090% | — | sem_zona |
| 2026-10-25 04:06 | ETH-USDT-SWAP | 2339.9 | 2353.2/2335.0 | 2361.6 | sup 2281.0 (ha 15 candles) | 12.43 | 0.0009% | — | sem_zona |
| 2026-10-25 04:06 | SOL-USDT-SWAP | 101.27 | 101.95/101.17 | 102.37 | sup 98.54 (ha 15 candles) | 0.56786 | -0.0039% | — | sem_zona |
| 2026-10-25 04:06 | XRP-USDT-SWAP | 1.2943 | 1.3025/1.2935 | 1.3104 | sup 1.2539 (ha 15 candles) | 0.00802 | 0.0041% | — | sem_zona |
| 2026-10-25 04:06 | DOGE-USDT-SWAP | 0.07667 | 0.07709/0.07651 | 0.07782 | sup 0.07469 (ha 15 candles) | 0.00045 | -0.0061% | — | sem_zona |
| 2026-10-25 04:06 | ARB-USDT-SWAP | 0.16544 | 0.16680/0.16485 | 0.16791 | sup 0.16640 (ha 8 candles) | 0.00172 | 0.0022% | A/venda@0.16640 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-25 04:06 | WLD-USDT-SWAP | 0.46310 | 0.46630/0.46010 | 0.46870 | — | 0.00598 | -0.0066% | B/compra@0.46070 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-25 04:06 | SUI-USDT-SWAP | 0.91500 | 0.92190/0.91210 | 0.93650 | sup 0.91080 (ha 15 candles) | 0.00789 | 0.0051% | — | sem_zona |
| 2026-10-25 04:06 | UNI-USDT-SWAP | 6.7260 | 6.7860/6.7090 | 6.8200 | sup 6.5130 (ha 15 candles) | 0.06064 | 0.0034% | — | sem_zona |
| 2026-10-25 04:06 | LINK-USDT-SWAP | 11.36 | 11.45/11.33 | 11.58 | sup 11.23 (ha 15 candles) | 0.07436 | 0.0094% | — | sem_zona |
| 2026-10-25 05:06 | BTC-USDT-SWAP | 80648.0 | 80690.5/80467.3 | 80648.0 | sup 79168.0 (ha 16 candles) | 233.62 | 0.0094% | — | sem_zona |
| 2026-10-25 05:06 | ETH-USDT-SWAP | 2347.1 | 2349.9/2339.9 | 2347.1 | sup 2281.0 (ha 16 candles) | 12.23 | 0.0013% | — | sem_zona |
| 2026-10-25 05:06 | SOL-USDT-SWAP | 101.60 | 101.83/101.26 | 101.60 | sup 98.54 (ha 16 candles) | 0.57357 | -0.0021% | — | sem_zona |
| 2026-10-25 05:06 | XRP-USDT-SWAP | 1.3014 | 1.3047/1.2942 | 1.3014 | sup 1.2539 (ha 16 candles) | 0.00833 | 0.0058% | — | sem_zona |
| 2026-10-25 05:06 | DOGE-USDT-SWAP | 0.07692 | 0.07709/0.07664 | 0.07692 | sup 0.07469 (ha 16 candles) | 0.00046 | -0.0049% | — | sem_zona |
| 2026-10-25 05:06 | ARB-USDT-SWAP | 0.16638 | 0.16680/0.16524 | 0.16638 | sup 0.16640 (ha 9 candles) | 0.00167 | 0.0031% | A/venda@0.16640 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-25 05:06 | WLD-USDT-SWAP | 0.46560 | 0.46650/0.46190 | 0.46560 | — | 0.00576 | -0.0038% | — | descartado_rr_baixo_setup_B |
| 2026-10-25 05:06 | SUI-USDT-SWAP | 0.91830 | 0.92110/0.91380 | 0.91830 | sup 0.91080 (ha 16 candles) | 0.00768 | 0.0066% | — | sem_zona |
| 2026-10-25 05:06 | UNI-USDT-SWAP | 6.7720 | 6.7920/6.7160 | 6.7720 | sup 6.5130 (ha 16 candles) | 0.06136 | 0.0013% | — | sem_zona |
| 2026-10-25 05:06 | LINK-USDT-SWAP | 11.40 | 11.42/11.35 | 11.40 | sup 11.23 (ha 16 candles) | 0.07364 | 0.0084% | — | sem_zona |
| 2026-10-25 06:06 | BTC-USDT-SWAP | 80373.0 | 80671.3/80331.8 | 80648.0 | sup 79168.0 (ha 17 candles) | 229.94 | 0.0091% | — | sem_zona |
| 2026-10-25 06:06 | ETH-USDT-SWAP | 2334.2 | 2347.6/2331.1 | 2347.1 | sup 2281.0 (ha 17 candles) | 11.94 | 0.0020% | — | sem_zona |
| 2026-10-25 06:06 | SOL-USDT-SWAP | 100.78 | 101.61/100.62 | 101.60 | sup 98.54 (ha 17 candles) | 0.57286 | -0.0011% | — | sem_zona |
| 2026-10-25 06:06 | XRP-USDT-SWAP | 1.2946 | 1.3028/1.2918 | 1.3014 | sup 1.2539 (ha 17 candles) | 0.00814 | 0.0064% | — | sem_zona |
| 2026-10-25 06:06 | DOGE-USDT-SWAP | 0.07628 | 0.07694/0.07617 | 0.07692 | sup 0.07469 (ha 17 candles) | 0.00045 | -0.0033% | — | sem_zona |
| 2026-10-25 06:06 | ARB-USDT-SWAP | 0.16389 | 0.16654/0.16314 | 0.16638 | sup 0.16640 (ha 10 candles) | 0.00167 | 0.0033% | — | descartado_rr_baixo_setup_A |
| 2026-10-25 06:06 | WLD-USDT-SWAP | 0.44200 | 0.46570/0.43160 | 0.46560 | — | 0.00747 | 0.0005% | — | sem_zona |
| 2026-10-25 06:06 | SUI-USDT-SWAP | 0.90960 | 0.92010/0.90770 | 0.91830 | sup 0.91080 (ha 17 candles) | 0.00745 | 0.0063% | A/venda@0.91080 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-25 06:06 | UNI-USDT-SWAP | 6.6800 | 6.7750/6.6670 | 6.7720 | sup 6.5130 (ha 17 candles) | 0.06086 | -0.0004% | — | sem_zona |
| 2026-10-25 06:06 | LINK-USDT-SWAP | 11.32 | 11.41/11.29 | 11.40 | sup 11.23 (ha 17 candles) | 0.07157 | 0.0070% | — | sem_zona |
| 2026-10-25 07:06 | BTC-USDT-SWAP | 80300.1 | 80424.9/80050.0 | 80648.0 | sup 79168.0 (ha 18 candles) | 247.22 | 0.0100% | — | sem_zona |
| 2026-10-25 07:06 | ETH-USDT-SWAP | 2326.7 | 2336.0/2316.0 | 2347.1 | sup 2281.0 (ha 18 candles) | 12.91 | 0.0036% | — | sem_zona |
| 2026-10-25 07:06 | SOL-USDT-SWAP | 100.84 | 100.96/100.28 | 101.60 | sup 98.54 (ha 18 candles) | 0.59857 | 0.0015% | — | sem_zona |
| 2026-10-25 07:06 | XRP-USDT-SWAP | 1.2937 | 1.2968/1.2884 | 1.3014 | sup 1.2539 (ha 18 candles) | 0.00831 | 0.0076% | — | sem_zona |
| 2026-10-25 07:06 | DOGE-USDT-SWAP | 0.07648 | 0.07651/0.07591 | 0.07692 | sup 0.07469 (ha 18 candles) | 0.00048 | 0.0003% | — | sem_zona |
| 2026-10-25 07:06 | ARB-USDT-SWAP | 0.16461 | 0.16474/0.16304 | 0.16638 | sup 0.16640 (ha 11 candles) | 0.00169 | 0.0054% | — | sem_zona |
| 2026-10-25 07:06 | WLD-USDT-SWAP | 0.44680 | 0.44800/0.43690 | 0.46560 | — | 0.00796 | 0.0018% | — | sem_zona |
| 2026-10-25 07:06 | SUI-USDT-SWAP | 0.91180 | 0.91280/0.90340 | 0.91830 | sup 0.91080 (ha 18 candles) | 0.00783 | 0.0064% | A/venda@0.91080 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-25 07:06 | UNI-USDT-SWAP | 6.7000 | 6.7050/6.6380 | 6.7720 | sup 6.5130 (ha 18 candles) | 0.06329 | 0.0014% | — | sem_zona |
| 2026-10-25 07:06 | LINK-USDT-SWAP | 11.32 | 11.34/11.25 | 11.40 | sup 11.23 (ha 18 candles) | 0.07529 | 0.0051% | — | sem_zona |
| 2026-10-25 08:06 | BTC-USDT-SWAP | 80240.0 | 80392.7/80176.1 | 80648.0 | sup 79168.0 (ha 19 candles) | 252.39 | 0.0100% | — | sem_zona |
| 2026-10-25 08:06 | ETH-USDT-SWAP | 2325.5 | 2331.3/2321.4 | 2347.1 | sup 2281.0 (ha 19 candles) | 12.86 | 0.0044% | — | sem_zona |
| 2026-10-25 08:06 | SOL-USDT-SWAP | 100.68 | 100.93/100.51 | 101.60 | sup 98.54 (ha 19 candles) | 0.58929 | 0.0023% | — | sem_zona |
| 2026-10-25 08:06 | XRP-USDT-SWAP | 1.2920 | 1.2957/1.2894 | 1.3014 | sup 1.2539 (ha 19 candles) | 0.00832 | 0.0076% | — | sem_zona |
| 2026-10-25 08:06 | DOGE-USDT-SWAP | 0.07640 | 0.07664/0.07632 | 0.07692 | sup 0.07469 (ha 19 candles) | 0.00047 | 0.0009% | — | sem_zona |
| 2026-10-25 08:06 | ARB-USDT-SWAP | 0.16424 | 0.16487/0.16399 | 0.16638 | sup 0.16640 (ha 12 candles) | 0.00165 | 0.0066% | — | sem_zona |
| 2026-10-25 08:06 | WLD-USDT-SWAP | 0.44390 | 0.44720/0.44100 | 0.46560 | — | 0.00798 | 0.0058% | — | sem_zona |
| 2026-10-25 08:06 | SUI-USDT-SWAP | 0.90950 | 0.91320/0.90750 | 0.91830 | sup 0.91080 (ha 19 candles) | 0.00784 | 0.0065% | — | descartado_rr_baixo_setup_A |
| 2026-10-25 08:06 | UNI-USDT-SWAP | 6.6680 | 6.7120/6.6580 | 6.7720 | sup 6.5130 (ha 19 candles) | 0.06300 | 0.0023% | — | sem_zona |
| 2026-10-25 08:06 | LINK-USDT-SWAP | 11.31 | 11.33/11.29 | 11.40 | sup 11.23 (ha 19 candles) | 0.07343 | 0.0025% | — | sem_zona |
| 2026-10-25 09:06 | BTC-USDT-SWAP | 80543.3 | 80611.5/80240.0 | 80543.3 | sup 79168.0 (ha 20 candles) | 262.88 | 0.0100% | — | sem_zona |
| 2026-10-25 09:06 | ETH-USDT-SWAP | 2338.7 | 2343.0/2324.5 | 2338.7 | sup 2281.0 (ha 20 candles) | 13.23 | 0.0056% | — | sem_zona |
| 2026-10-25 09:06 | SOL-USDT-SWAP | 101.27 | 101.33/100.61 | 101.27 | sup 98.54 (ha 20 candles) | 0.60500 | 0.0034% | — | sem_zona |
| 2026-10-25 09:06 | XRP-USDT-SWAP | 1.2993 | 1.3018/1.2910 | 1.2993 | sup 1.2539 (ha 20 candles) | 0.00871 | 0.0081% | — | sem_zona |
| 2026-10-25 09:06 | DOGE-USDT-SWAP | 0.07674 | 0.07684/0.07638 | 0.07674 | sup 0.07469 (ha 20 candles) | 0.00048 | 0.0028% | — | sem_zona |
| 2026-10-25 09:06 | ARB-USDT-SWAP | 0.16621 | 0.16631/0.16382 | 0.16621 | sup 0.16640 (ha 13 candles) | 0.00174 | 0.0073% | — | sem_zona |
| 2026-10-25 09:06 | WLD-USDT-SWAP | 0.45320 | 0.45600/0.44250 | 0.45320 | — | 0.00862 | 0.0057% | B/compra@0.45610 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-25 09:06 | SUI-USDT-SWAP | 0.91900 | 0.92060/0.90920 | 0.91900 | sup 0.91080 (ha 20 candles) | 0.00801 | 0.0046% | — | sem_zona |
| 2026-10-25 09:06 | UNI-USDT-SWAP | 6.7560 | 6.7690/6.6620 | 6.7560 | sup 6.5130 (ha 20 candles) | 0.06707 | 0.0006% | — | sem_zona |
| 2026-10-25 09:06 | LINK-USDT-SWAP | 11.40 | 11.42/11.31 | 11.40 | sup 11.23 (ha 20 candles) | 0.07507 | 0.0007% | — | sem_zona |
| 2026-10-25 10:06 | BTC-USDT-SWAP | 80412.7 | 80543.4/80282.6 | 80543.3 | sup 80050.0 (ha 3 candles) | 264.67 | 0.0099% | — | sem_zona |
| 2026-10-25 10:06 | ETH-USDT-SWAP | 2333.9 | 2338.8/2326.5 | 2338.7 | sup 2316.0 (ha 3 candles) | 13.64 | 0.0057% | — | sem_zona |
| 2026-10-25 10:06 | SOL-USDT-SWAP | 100.98 | 101.28/100.64 | 101.27 | sup 100.28 (ha 3 candles) | 0.62429 | 0.0061% | — | sem_zona |
| 2026-10-25 10:06 | XRP-USDT-SWAP | 1.2962 | 1.3000/1.2933 | 1.2993 | sup 1.2884 (ha 3 candles) | 0.00879 | 0.0079% | — | sem_zona |
| 2026-10-25 10:06 | DOGE-USDT-SWAP | 0.07663 | 0.07675/0.07638 | 0.07674 | sup 0.07591 (ha 3 candles) | 0.00049 | 0.0034% | — | sem_zona |
| 2026-10-25 10:06 | ARB-USDT-SWAP | 0.16560 | 0.16634/0.16455 | 0.16621 | sup 0.16304 (ha 3 candles) | 0.00177 | 0.0050% | — | sem_zona |
| 2026-10-25 10:06 | WLD-USDT-SWAP | 0.45000 | 0.45450/0.44540 | 0.45320 | — | 0.00880 | 0.0040% | — | invalidado_setup_B |
| 2026-10-25 10:06 | SUI-USDT-SWAP | 0.91700 | 0.92020/0.91370 | 0.91900 | sup 0.90340 (ha 3 candles) | 0.00817 | -0.0000% | — | sem_zona |
| 2026-10-25 10:06 | UNI-USDT-SWAP | 6.7120 | 6.7620/6.6890 | 6.7560 | sup 6.6380 (ha 3 candles) | 0.06793 | 0.0003% | — | sem_zona |
| 2026-10-25 10:06 | LINK-USDT-SWAP | 11.38 | 11.40/11.33 | 11.40 | sup 11.25 (ha 3 candles) | 0.07679 | -0.0002% | — | sem_zona |
| 2026-10-25 11:07 | BTC-USDT-SWAP | 80344.5 | 80430.5/80199.0 | 80543.3 | sup 80050.0 (ha 4 candles) | 252.71 | 0.0085% | — | sem_zona |
| 2026-10-25 11:07 | ETH-USDT-SWAP | 2333.2 | 2338.7/2325.3 | 2338.7 | sup 2316.0 (ha 4 candles) | 13.22 | 0.0047% | — | sem_zona |
| 2026-10-25 11:07 | SOL-USDT-SWAP | 100.71 | 101.16/100.68 | 101.27 | sup 100.28 (ha 4 candles) | 0.58571 | 0.0074% | — | sem_zona |
| 2026-10-25 11:07 | XRP-USDT-SWAP | 1.2959 | 1.2994/1.2934 | 1.2993 | sup 1.2884 (ha 4 candles) | 0.00851 | 0.0079% | — | sem_zona |
| 2026-10-25 11:07 | DOGE-USDT-SWAP | 0.07672 | 0.07697/0.07652 | 0.07674 | sup 0.07591 (ha 4 candles) | 0.00047 | 0.0018% | — | sem_zona |
| 2026-10-25 11:07 | ARB-USDT-SWAP | 0.16534 | 0.16618/0.16464 | 0.16621 | sup 0.16304 (ha 4 candles) | 0.00169 | 0.0047% | — | sem_zona |
| 2026-10-25 11:07 | WLD-USDT-SWAP | 0.44920 | 0.45220/0.44780 | 0.45320 | — | 0.00867 | 0.0048% | — | sem_zona |
| 2026-10-25 11:07 | SUI-USDT-SWAP | 0.91150 | 0.91920/0.91130 | 0.91900 | sup 0.90340 (ha 4 candles) | 0.00804 | 0.0007% | — | sem_zona |
| 2026-10-25 11:07 | UNI-USDT-SWAP | 6.7220 | 6.7580/6.7000 | 6.7560 | sup 6.6380 (ha 4 candles) | 0.06621 | -0.0010% | — | sem_zona |
| 2026-10-25 11:07 | LINK-USDT-SWAP | 11.37 | 11.41/11.35 | 11.40 | sup 11.25 (ha 4 candles) | 0.07457 | -0.0006% | — | sem_zona |
| 2026-10-25 12:06 | BTC-USDT-SWAP | 80611.9 | 80620.0/80260.0 | 80543.3 | sup 80050.0 (ha 5 candles) | 267.90 | 0.0078% | — | sem_zona |
| 2026-10-25 12:06 | ETH-USDT-SWAP | 2342.7 | 2344.0/2329.4 | 2338.7 | sup 2316.0 (ha 5 candles) | 13.64 | 0.0045% | — | sem_zona |
| 2026-10-25 12:06 | SOL-USDT-SWAP | 101.32 | 101.34/100.56 | 101.27 | sup 100.28 (ha 5 candles) | 0.61214 | 0.0081% | — | sem_zona |
| 2026-10-25 12:06 | XRP-USDT-SWAP | 1.2982 | 1.2994/1.2913 | 1.2993 | sup 1.2884 (ha 5 candles) | 0.00850 | 0.0069% | — | sem_zona |
| 2026-10-25 12:06 | DOGE-USDT-SWAP | 0.07707 | 0.07713/0.07650 | 0.07674 | sup 0.07591 (ha 5 candles) | 0.00048 | 0.0003% | — | sem_zona |
| 2026-10-25 12:06 | ARB-USDT-SWAP | 0.16737 | 0.16747/0.16496 | 0.16621 | sup 0.16304 (ha 5 candles) | 0.00174 | 0.0041% | — | sem_zona |
| 2026-10-25 12:06 | WLD-USDT-SWAP | 0.45190 | 0.45380/0.44610 | 0.45320 | — | 0.00882 | 0.0042% | — | sem_zona |
| 2026-10-25 12:06 | SUI-USDT-SWAP | 0.91390 | 0.91420/0.90720 | 0.91900 | sup 0.90340 (ha 5 candles) | 0.00812 | 0.0021% | — | sem_zona |
| 2026-10-25 12:06 | UNI-USDT-SWAP | 6.7890 | 6.7920/6.7100 | 6.7560 | sup 6.6380 (ha 5 candles) | 0.06893 | -0.0007% | — | sem_zona |
| 2026-10-25 12:06 | LINK-USDT-SWAP | 11.40 | 11.41/11.32 | 11.40 | sup 11.25 (ha 5 candles) | 0.07764 | 0.0009% | — | sem_zona |
| 2026-10-25 13:06 | BTC-USDT-SWAP | 80599.9 | 80765.0/80476.4 | 80599.9 | sup 80050.0 (ha 6 candles) | 277.81 | 0.0054% | — | sem_zona |
| 2026-10-25 13:06 | ETH-USDT-SWAP | 2343.1 | 2349.4/2334.8 | 2343.1 | sup 2316.0 (ha 6 candles) | 14.01 | 0.0033% | — | sem_zona |
| 2026-10-25 13:06 | SOL-USDT-SWAP | 101.58 | 101.84/101.11 | 101.58 | sup 100.28 (ha 6 candles) | 0.63357 | 0.0076% | — | sem_zona |
| 2026-10-25 13:06 | XRP-USDT-SWAP | 1.2996 | 1.3019/1.2951 | 1.2996 | sup 1.2884 (ha 6 candles) | 0.00849 | 0.0060% | — | sem_zona |
| 2026-10-25 13:06 | DOGE-USDT-SWAP | 0.07720 | 0.07741/0.07687 | 0.07720 | sup 0.07591 (ha 6 candles) | 0.00050 | -0.0021% | — | sem_zona |
| 2026-10-25 13:06 | ARB-USDT-SWAP | 0.16738 | 0.16866/0.16699 | 0.16738 | sup 0.16304 (ha 6 candles) | 0.00177 | 0.0031% | — | sem_zona |
| 2026-10-25 13:06 | WLD-USDT-SWAP | 0.45650 | 0.45960/0.45190 | 0.45650 | — | 0.00896 | 0.0018% | B/compra@0.46070 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-25 13:06 | SUI-USDT-SWAP | 0.91690 | 0.91990/0.91350 | 0.91690 | sup 0.90340 (ha 6 candles) | 0.00833 | 0.0017% | — | sem_zona |
| 2026-10-25 13:06 | UNI-USDT-SWAP | 6.8550 | 6.8890/6.7800 | 6.8550 | sup 6.6380 (ha 6 candles) | 0.07321 | -0.0021% | — | sem_zona |
| 2026-10-25 13:06 | LINK-USDT-SWAP | 11.42 | 11.46/11.36 | 11.42 | sup 11.25 (ha 6 candles) | 0.08157 | 0.0014% | — | sem_zona |
| 2026-10-25 14:06 | BTC-USDT-SWAP | 80772.1 | 80821.0/80493.7 | 80599.9 | sup 80050.0 (ha 7 candles) | 286.91 | 0.0053% | — | sem_zona |
| 2026-10-25 14:06 | ETH-USDT-SWAP | 2355.8 | 2360.3/2340.3 | 2343.1 | sup 2316.0 (ha 7 candles) | 14.63 | 0.0027% | — | sem_zona |
| 2026-10-25 14:06 | SOL-USDT-SWAP | 101.92 | 102.04/101.22 | 101.58 | sup 100.28 (ha 7 candles) | 0.66500 | 0.0068% | — | sem_zona |
| 2026-10-25 14:06 | XRP-USDT-SWAP | 1.3069 | 1.3084/1.2968 | 1.2996 | sup 1.2884 (ha 7 candles) | 0.00871 | 0.0059% | — | sem_zona |
| 2026-10-25 14:06 | DOGE-USDT-SWAP | 0.07747 | 0.07754/0.07691 | 0.07720 | sup 0.07591 (ha 7 candles) | 0.00052 | -0.0026% | — | sem_zona |
| 2026-10-25 14:06 | ARB-USDT-SWAP | 0.16927 | 0.16961/0.16669 | 0.16738 | sup 0.16304 (ha 7 candles) | 0.00186 | 0.0003% | — | sem_zona |
| 2026-10-25 14:06 | WLD-USDT-SWAP | 0.46060 | 0.46140/0.45360 | 0.45650 | — | 0.00912 | -0.0031% | — | descartado_rr_baixo_setup_B |
| 2026-10-25 14:06 | SUI-USDT-SWAP | 0.92970 | 0.93180/0.91480 | 0.91690 | sup 0.90340 (ha 7 candles) | 0.00908 | -0.0014% | — | sem_zona |
| 2026-10-25 14:06 | UNI-USDT-SWAP | 6.9610 | 6.9690/6.8290 | 6.8550 | sup 6.6380 (ha 7 candles) | 0.07950 | -0.0030% | — | sem_zona |
| 2026-10-25 14:06 | LINK-USDT-SWAP | 11.49 | 11.51/11.39 | 11.42 | sup 11.25 (ha 7 candles) | 0.08650 | 0.0019% | — | sem_zona |
| 2026-10-25 15:06 | BTC-USDT-SWAP | 80762.4 | 80919.0/80705.0 | 80599.9 | sup 80050.0 (ha 8 candles) | 288.69 | 0.0055% | — | sem_zona |
| 2026-10-25 15:06 | ETH-USDT-SWAP | 2357.6 | 2364.7/2352.3 | 2343.1 | sup 2316.0 (ha 8 candles) | 14.96 | 0.0031% | — | sem_zona |
| 2026-10-25 15:06 | SOL-USDT-SWAP | 101.94 | 102.23/101.68 | 101.58 | sup 100.56 (ha 3 candles) | 0.67714 | 0.0054% | — | sem_zona |
| 2026-10-25 15:06 | XRP-USDT-SWAP | 1.3050 | 1.3103/1.3031 | 1.2996 | sup 1.2884 (ha 8 candles) | 0.00891 | 0.0057% | — | sem_zona |
| 2026-10-25 15:06 | DOGE-USDT-SWAP | 0.07740 | 0.07766/0.07730 | 0.07720 | sup 0.07591 (ha 8 candles) | 0.00053 | -0.0009% | — | sem_zona |
| 2026-10-25 15:06 | ARB-USDT-SWAP | 0.16974 | 0.17104/0.16888 | 0.16738 | sup 0.16304 (ha 8 candles) | 0.00193 | -0.0066% | — | sem_zona |
| 2026-10-25 15:06 | WLD-USDT-SWAP | 0.46210 | 0.46430/0.45750 | 0.45650 | — | 0.00918 | -0.0079% | B/compra@0.45610 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-25 15:06 | SUI-USDT-SWAP | 0.93210 | 0.93350/0.92680 | 0.91690 | sup 0.90720 (ha 3 candles) | 0.00918 | -0.0051% | — | sem_zona |
| 2026-10-25 15:06 | UNI-USDT-SWAP | 6.9420 | 6.9810/6.9140 | 6.8550 | sup 6.6380 (ha 8 candles) | 0.08129 | -0.0017% | — | sem_zona |
| 2026-10-25 15:06 | LINK-USDT-SWAP | 11.53 | 11.54/11.47 | 11.42 | sup 11.25 (ha 8 candles) | 0.08850 | 0.0039% | — | sem_zona |
| 2026-10-25 16:06 | BTC-USDT-SWAP | 80629.1 | 80789.4/80613.3 | 80599.9 | sup 80050.0 (ha 9 candles) | 291.29 | 0.0057% | — | sem_zona |
| 2026-10-25 16:06 | ETH-USDT-SWAP | 2354.5 | 2358.9/2353.0 | 2343.1 | sup 2316.0 (ha 9 candles) | 14.85 | 0.0038% | — | sem_zona |
| 2026-10-25 16:06 | SOL-USDT-SWAP | 101.76 | 101.98/101.66 | 101.58 | sup 100.56 (ha 4 candles) | 0.67000 | 0.0051% | — | sem_zona |
| 2026-10-25 16:06 | XRP-USDT-SWAP | 1.2999 | 1.3051/1.2992 | 1.2996 | sup 1.2884 (ha 9 candles) | 0.00883 | 0.0055% | — | sem_zona |
| 2026-10-25 16:06 | DOGE-USDT-SWAP | 0.07729 | 0.07742/0.07717 | 0.07720 | sup 0.07591 (ha 9 candles) | 0.00053 | -0.0017% | — | sem_zona |
| 2026-10-25 16:06 | ARB-USDT-SWAP | 0.16940 | 0.17025/0.16898 | 0.16738 | sup 0.16304 (ha 9 candles) | 0.00196 | -0.0106% | — | sem_zona |
| 2026-10-25 16:06 | WLD-USDT-SWAP | 0.45840 | 0.46310/0.45650 | 0.45650 | — | 0.00940 | -0.0101% | B/compra@0.45610 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-25 16:06 | SUI-USDT-SWAP | 0.92980 | 0.93320/0.92830 | 0.91690 | sup 0.90720 (ha 4 candles) | 0.00916 | -0.0081% | — | sem_zona |
| 2026-10-25 16:06 | UNI-USDT-SWAP | 6.9520 | 6.9930/6.9210 | 6.8550 | sup 6.6380 (ha 9 candles) | 0.08400 | 0.0011% | — | sem_zona |
| 2026-10-25 16:06 | LINK-USDT-SWAP | 11.52 | 11.54/11.50 | 11.42 | sup 11.25 (ha 9 candles) | 0.08993 | 0.0061% | — | sem_zona |
| 2026-10-25 17:06 | BTC-USDT-SWAP | 80540.9 | 80649.1/80509.5 | 80540.9 | sup 80050.0 (ha 10 candles) | 270.04 | 0.0072% | — | sem_zona |
| 2026-10-25 17:06 | ETH-USDT-SWAP | 2350.1 | 2354.9/2348.6 | 2350.1 | sup 2316.0 (ha 10 candles) | 13.74 | 0.0046% | — | sem_zona |
| 2026-10-25 17:06 | SOL-USDT-SWAP | 101.75 | 101.83/101.56 | 101.75 | sup 100.56 (ha 5 candles) | 0.62500 | 0.0050% | — | sem_zona |
| 2026-10-25 17:06 | XRP-USDT-SWAP | 1.2998 | 1.3016/1.2981 | 1.2998 | sup 1.2884 (ha 10 candles) | 0.00799 | 0.0066% | — | sem_zona |
| 2026-10-25 17:06 | DOGE-USDT-SWAP | 0.07726 | 0.07736/0.07713 | 0.07726 | sup 0.07591 (ha 10 candles) | 0.00047 | -0.0011% | — | sem_zona |
| 2026-10-25 17:06 | ARB-USDT-SWAP | 0.16969 | 0.16990/0.16865 | 0.16969 | sup 0.16304 (ha 10 candles) | 0.00194 | -0.0102% | — | sem_zona |
| 2026-10-25 17:06 | WLD-USDT-SWAP | 0.45610 | 0.45900/0.45440 | 0.45610 | — | 0.00931 | -0.0059% | B/compra@0.45610 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-25 17:06 | SUI-USDT-SWAP | 0.92820 | 0.93100/0.92540 | 0.92820 | sup 0.90720 (ha 5 candles) | 0.00843 | -0.0067% | — | sem_zona |
| 2026-10-25 17:06 | UNI-USDT-SWAP | 6.9900 | 6.9900/6.9430 | 6.9900 | sup 6.6380 (ha 10 candles) | 0.08121 | 0.0056% | — | sem_zona |
| 2026-10-25 17:06 | LINK-USDT-SWAP | 11.48 | 11.53/11.47 | 11.48 | sup 11.25 (ha 10 candles) | 0.08243 | 0.0091% | — | sem_zona |
| 2026-10-25 18:06 | BTC-USDT-SWAP | 80461.8 | 80595.2/80399.0 | 80540.9 | sup 80050.0 (ha 11 candles) | 265.70 | 0.0081% | — | sem_zona |
| 2026-10-25 18:06 | ETH-USDT-SWAP | 2346.3 | 2351.8/2343.4 | 2350.1 | sup 2316.0 (ha 11 candles) | 13.05 | 0.0053% | — | sem_zona |
| 2026-10-25 18:06 | SOL-USDT-SWAP | 101.63 | 101.80/101.45 | 101.75 | sup 100.56 (ha 6 candles) | 0.59429 | 0.0048% | — | sem_zona |
| 2026-10-25 18:06 | XRP-USDT-SWAP | 1.2998 | 1.3009/1.2971 | 1.2998 | sup 1.2884 (ha 11 candles) | 0.00761 | 0.0078% | — | sem_zona |
| 2026-10-25 18:06 | DOGE-USDT-SWAP | 0.07721 | 0.07732/0.07706 | 0.07726 | sup 0.07591 (ha 11 candles) | 0.00045 | -0.0011% | — | sem_zona |
| 2026-10-25 18:06 | ARB-USDT-SWAP | 0.16990 | 0.17008/0.16902 | 0.16969 | sup 0.16304 (ha 11 candles) | 0.00187 | -0.0079% | — | sem_zona |
| 2026-10-25 18:06 | WLD-USDT-SWAP | 0.45430 | 0.45650/0.45270 | 0.45610 | — | 0.00914 | -0.0011% | — | zona_expirada_setup_B |
| 2026-10-25 18:06 | SUI-USDT-SWAP | 0.92590 | 0.92820/0.92270 | 0.92820 | sup 0.90720 (ha 6 candles) | 0.00812 | -0.0022% | — | sem_zona |
| 2026-10-25 18:06 | UNI-USDT-SWAP | 6.9700 | 6.9950/6.9380 | 6.9900 | sup 6.6380 (ha 11 candles) | 0.07979 | 0.0100% | — | sem_zona |
| 2026-10-25 18:06 | LINK-USDT-SWAP | 11.49 | 11.50/11.45 | 11.48 | sup 11.25 (ha 11 candles) | 0.07771 | 0.0100% | — | sem_zona |
| 2026-10-25 19:06 | BTC-USDT-SWAP | 80232.1 | 80499.0/80157.0 | 80540.9 | sup 80050.0 (ha 12 candles) | 274.19 | 0.0087% | — | sem_zona |
| 2026-10-25 19:06 | ETH-USDT-SWAP | 2331.2 | 2346.4/2327.8 | 2350.1 | sup 2316.0 (ha 12 candles) | 13.66 | 0.0051% | — | sem_zona |
| 2026-10-25 19:06 | SOL-USDT-SWAP | 101.07 | 101.64/100.86 | 101.75 | sup 100.56 (ha 7 candles) | 0.60929 | 0.0040% | — | sem_zona |
| 2026-10-25 19:06 | XRP-USDT-SWAP | 1.2921 | 1.3004/1.2901 | 1.2998 | sup 1.2884 (ha 12 candles) | 0.00760 | 0.0076% | — | sem_zona |
| 2026-10-25 19:06 | DOGE-USDT-SWAP | 0.07669 | 0.07721/0.07658 | 0.07726 | sup 0.07591 (ha 12 candles) | 0.00046 | -0.0017% | — | sem_zona |
| 2026-10-25 19:06 | ARB-USDT-SWAP | 0.16858 | 0.16990/0.16826 | 0.16969 | sup 0.16304 (ha 12 candles) | 0.00188 | -0.0026% | — | sem_zona |
| 2026-10-25 19:06 | WLD-USDT-SWAP | 0.45080 | 0.45470/0.44860 | 0.45610 | — | 0.00925 | 0.0021% | — | sem_zona |
| 2026-10-25 19:06 | SUI-USDT-SWAP | 0.91570 | 0.92600/0.91230 | 0.92820 | sup 0.90720 (ha 7 candles) | 0.00858 | 0.0011% | — | sem_zona |
| 2026-10-25 19:06 | UNI-USDT-SWAP | 6.9230 | 6.9750/6.9140 | 6.9900 | sup 6.6380 (ha 12 candles) | 0.07871 | 0.0100% | — | sem_zona |
| 2026-10-25 19:06 | LINK-USDT-SWAP | 11.41 | 11.49/11.39 | 11.48 | sup 11.25 (ha 12 candles) | 0.07979 | 0.0100% | — | sem_zona |
| 2026-10-25 20:06 | BTC-USDT-SWAP | 80436.0 | 80721.7/80215.9 | 80540.9 | sup 80050.0 (ha 13 candles) | 286.06 | 0.0081% | — | sem_zona |
| 2026-10-25 20:06 | ETH-USDT-SWAP | 2341.1 | 2351.8/2331.0 | 2350.1 | sup 2316.0 (ha 13 candles) | 13.96 | 0.0040% | — | sem_zona |
| 2026-10-25 20:06 | SOL-USDT-SWAP | 101.54 | 102.04/101.06 | 101.75 | sup 100.56 (ha 8 candles) | 0.60857 | 0.0024% | — | sem_zona |
| 2026-10-25 20:06 | XRP-USDT-SWAP | 1.2991 | 1.3024/1.2916 | 1.2998 | sup 1.2884 (ha 13 candles) | 0.00759 | 0.0076% | — | sem_zona |
| 2026-10-25 20:06 | DOGE-USDT-SWAP | 0.07717 | 0.07742/0.07668 | 0.07726 | sup 0.07591 (ha 13 candles) | 0.00046 | -0.0031% | — | sem_zona |
| 2026-10-25 20:06 | ARB-USDT-SWAP | 0.16960 | 0.17109/0.16858 | 0.16969 | sup 0.16304 (ha 13 candles) | 0.00181 | -0.0022% | — | sem_zona |
| 2026-10-25 20:06 | WLD-USDT-SWAP | 0.45190 | 0.45790/0.45080 | 0.45610 | — | 0.00732 | 0.0018% | — | sem_zona |
| 2026-10-25 20:06 | SUI-USDT-SWAP | 0.92190 | 0.92630/0.91530 | 0.92820 | sup 0.90720 (ha 8 candles) | 0.00848 | 0.0019% | — | sem_zona |
| 2026-10-25 20:06 | UNI-USDT-SWAP | 6.9590 | 7.0350/6.9200 | 6.9900 | sup 6.6380 (ha 13 candles) | 0.07921 | 0.0099% | — | sem_zona |
| 2026-10-25 20:06 | LINK-USDT-SWAP | 11.48 | 11.55/11.41 | 11.48 | sup 11.25 (ha 13 candles) | 0.08150 | 0.0100% | — | sem_zona |
| 2026-10-25 21:06 | BTC-USDT-SWAP | 80119.1 | 80444.1/79773.1 | 80119.1 | sup 80050.0 (ha 14 candles) | 307.21 | 0.0068% | — | sem_zona |
| 2026-10-25 21:06 | ETH-USDT-SWAP | 2328.7 | 2341.1/2308.0 | 2328.7 | sup 2316.0 (ha 14 candles) | 14.90 | 0.0034% | — | sem_zona |
| 2026-10-25 21:06 | SOL-USDT-SWAP | 101.34 | 101.64/100.56 | 101.34 | — | 0.63714 | 0.0021% | B/compra@101.15 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-25 21:06 | XRP-USDT-SWAP | 1.2956 | 1.2997/1.2840 | 1.2956 | sup 1.2884 (ha 14 candles) | 0.00811 | 0.0070% | — | sem_zona |
| 2026-10-25 21:06 | DOGE-USDT-SWAP | 0.07688 | 0.07725/0.07616 | 0.07688 | — | 0.00050 | -0.0025% | B/compra@0.07694 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-25 21:06 | ARB-USDT-SWAP | 0.16871 | 0.16990/0.16679 | 0.16871 | sup 0.16304 (ha 14 candles) | 0.00191 | 0.0014% | — | sem_zona |
| 2026-10-25 21:06 | WLD-USDT-SWAP | 0.45010 | 0.45280/0.44370 | 0.45010 | — | 0.00718 | 0.0038% | — | sem_zona |
| 2026-10-25 21:06 | SUI-USDT-SWAP | 0.92000 | 0.92420/0.90960 | 0.92000 | sup 0.90720 (ha 9 candles) | 0.00885 | 0.0036% | — | sem_zona |
| 2026-10-25 21:06 | UNI-USDT-SWAP | 6.9190 | 6.9710/6.8340 | 6.9190 | — | 0.08421 | 0.0061% | B/compra@6.8830 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-25 21:06 | LINK-USDT-SWAP | 11.45 | 11.50/11.31 | 11.45 | — | 0.08864 | 0.0098% | — | sem_zona |
| 2026-10-25 22:06 | BTC-USDT-SWAP | 80136.8 | 80350.0/79850.0 | 80119.1 | sup 80050.0 (ha 15 candles) | 327.46 | 0.0064% | — | sem_zona |
| 2026-10-25 22:06 | ETH-USDT-SWAP | 2328.9 | 2337.8/2317.1 | 2328.7 | sup 2316.0 (ha 15 candles) | 15.67 | 0.0037% | — | sem_zona |
| 2026-10-25 22:06 | SOL-USDT-SWAP | 101.49 | 101.63/101.05 | 101.34 | — | 0.64857 | 0.0043% | — | descartado_rr_baixo_setup_B |
| 2026-10-25 22:06 | XRP-USDT-SWAP | 1.2960 | 1.3000/1.2918 | 1.2956 | sup 1.2884 (ha 15 candles) | 0.00824 | 0.0091% | — | sem_zona |
| 2026-10-25 22:06 | DOGE-USDT-SWAP | 0.07703 | 0.07717/0.07667 | 0.07688 | — | 0.00051 | -0.0005% | — | descartado_rr_baixo_setup_B |
| 2026-10-25 22:06 | ARB-USDT-SWAP | 0.16903 | 0.16982/0.16815 | 0.16871 | sup 0.16304 (ha 15 candles) | 0.00197 | 0.0034% | — | sem_zona |
| 2026-10-25 22:06 | WLD-USDT-SWAP | 0.44820 | 0.45260/0.44520 | 0.45010 | — | 0.00726 | 0.0091% | — | sem_zona |
| 2026-10-25 22:06 | SUI-USDT-SWAP | 0.92140 | 0.92370/0.91690 | 0.92000 | sup 0.90720 (ha 10 candles) | 0.00893 | 0.0062% | — | sem_zona |
| 2026-10-25 22:06 | UNI-USDT-SWAP | 6.9450 | 6.9660/6.8930 | 6.9190 | — | 0.08557 | 0.0070% | — | descartado_rr_baixo_setup_B |
| 2026-10-25 22:06 | LINK-USDT-SWAP | 11.46 | 11.49/11.40 | 11.45 | — | 0.09221 | 0.0100% | B/compra@11.52 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-25 23:07 | BTC-USDT-SWAP | 79720.1 | 80237.1/79340.0 | 80119.1 | sup 80050.0 (ha 16 candles) | 365.00 | 0.0065% | A/venda@80050.0 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-25 23:07 | ETH-USDT-SWAP | 2314.0 | 2332.8/2298.4 | 2328.7 | sup 2316.0 (ha 16 candles) | 16.82 | 0.0037% | A/venda@2316.0 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-25 23:07 | SOL-USDT-SWAP | 101.04 | 101.63/100.32 | 101.34 | — | 0.69071 | 0.0071% | — | sem_zona |
| 2026-10-25 23:07 | XRP-USDT-SWAP | 1.2907 | 1.2980/1.2826 | 1.2956 | sup 1.2884 (ha 16 candles) | 0.00857 | 0.0100% | — | sem_zona |
| 2026-10-25 23:07 | DOGE-USDT-SWAP | 0.07649 | 0.07713/0.07602 | 0.07688 | — | 0.00056 | 0.0014% | — | sem_zona |
| 2026-10-25 23:07 | ARB-USDT-SWAP | 0.16727 | 0.16963/0.16600 | 0.16871 | sup 0.16304 (ha 16 candles) | 0.00205 | 0.0071% | — | sem_zona |
| 2026-10-25 23:07 | WLD-USDT-SWAP | 0.44580 | 0.44900/0.44230 | 0.45010 | — | 0.00678 | 0.0100% | — | sem_zona |
| 2026-10-25 23:07 | SUI-USDT-SWAP | 0.91160 | 0.92360/0.90050 | 0.92000 | sup 0.90720 (ha 11 candles) | 0.00976 | 0.0071% | — | sem_zona |
| 2026-10-25 23:07 | UNI-USDT-SWAP | 6.8840 | 6.9560/6.8050 | 6.9190 | — | 0.08871 | 0.0087% | — | sem_zona |
| 2026-10-25 23:07 | LINK-USDT-SWAP | 11.38 | 11.48/11.29 | 11.45 | — | 0.09757 | 0.0100% | B/compra@11.52 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-26 00:06 | BTC-USDT-SWAP | 79545.6 | 79937.1/79422.3 | 80119.1 | sup 80050.0 (ha 17 candles) | 383.14 | 0.0062% | A/venda@80050.0 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-26 00:06 | ETH-USDT-SWAP | 2304.0 | 2320.5/2295.8 | 2328.7 | sup 2316.0 (ha 17 candles) | 17.70 | 0.0046% | — | descartado_rr_baixo_setup_A |
| 2026-10-26 00:06 | SOL-USDT-SWAP | 100.55 | 101.38/100.31 | 101.34 | — | 0.72143 | 0.0087% | B/compra@100.34 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-26 00:06 | XRP-USDT-SWAP | 1.2826 | 1.2956/1.2792 | 1.2956 | sup 1.2884 (ha 17 candles) | 0.00926 | 0.0100% | A/venda@1.2884 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-26 00:06 | DOGE-USDT-SWAP | 0.07633 | 0.07683/0.07614 | 0.07688 | — | 0.00058 | 0.0018% | B/compra@0.07603 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-26 00:06 | ARB-USDT-SWAP | 0.16656 | 0.16813/0.16588 | 0.16871 | sup 0.16304 (ha 17 candles) | 0.00209 | 0.0065% | — | sem_zona |
| 2026-10-26 00:06 | WLD-USDT-SWAP | 0.44340 | 0.44770/0.44090 | 0.45010 | — | 0.00661 | 0.0100% | — | sem_zona |
| 2026-10-26 00:06 | SUI-USDT-SWAP | 0.90730 | 0.91680/0.90420 | 0.92000 | sup 0.90720 (ha 12 candles) | 0.01020 | 0.0100% | — | sem_zona |
| 2026-10-26 00:06 | UNI-USDT-SWAP | 6.8220 | 6.9190/6.7930 | 6.9190 | — | 0.09250 | 0.0099% | B/compra@6.8030 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-26 00:06 | LINK-USDT-SWAP | 11.33 | 11.43/11.30 | 11.45 | — | 0.10121 | 0.0100% | B/compra@11.52 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-26 01:06 | BTC-USDT-SWAP | 79560.3 | 79789.8/79322.9 | 79560.3 | sup 80050.0 (ha 18 candles) | 399.96 | 0.0058% | A/venda@80050.0 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-26 01:06 | ETH-USDT-SWAP | 2302.1 | 2317.8/2291.7 | 2302.1 | sup 2316.0 (ha 18 candles) | 18.61 | 0.0049% | — | sem_zona |
| 2026-10-26 01:06 | SOL-USDT-SWAP | 100.19 | 101.25/99.83 | 100.19 | — | 0.78857 | 0.0100% | B/compra@100.34 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-26 01:06 | XRP-USDT-SWAP | 1.2770 | 1.2893/1.2723 | 1.2770 | sup 1.2884 (ha 18 candles) | 0.01005 | 0.0100% | — | descartado_rr_baixo_setup_A |
| 2026-10-26 01:06 | DOGE-USDT-SWAP | 0.07626 | 0.07691/0.07592 | 0.07626 | — | 0.00062 | 0.0025% | B/compra@0.07603 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-26 01:06 | ARB-USDT-SWAP | 0.16644 | 0.16847/0.16534 | 0.16644 | sup 0.16304 (ha 18 candles) | 0.00220 | 0.0058% | — | sem_zona |
| 2026-10-26 01:06 | WLD-USDT-SWAP | 0.43990 | 0.44750/0.43500 | 0.43990 | — | 0.00719 | 0.0100% | — | sem_zona |
| 2026-10-26 01:06 | SUI-USDT-SWAP | 0.90420 | 0.91610/0.89950 | 0.90420 | sup 0.90720 (ha 13 candles) | 0.01082 | 0.0100% | A/venda@0.90720 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-26 01:06 | UNI-USDT-SWAP | 6.8240 | 6.8940/6.7700 | 6.8240 | — | 0.09721 | 0.0077% | B/compra@6.8030 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-26 01:06 | LINK-USDT-SWAP | 11.32 | 11.42/11.26 | 11.32 | — | 0.10829 | 0.0100% | B/compra@11.52 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-26 02:06 | BTC-USDT-SWAP | 80105.9 | 80128.5/79540.1 | 79560.3 | sup 80050.0 (ha 19 candles) | 416.27 | 0.0062% | A/venda@80050.0 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-26 02:06 | ETH-USDT-SWAP | 2321.0 | 2322.8/2301.0 | 2302.1 | sup 2316.0 (ha 19 candles) | 19.12 | 0.0046% | — | sem_zona |
| 2026-10-26 02:06 | SOL-USDT-SWAP | 101.25 | 101.35/100.15 | 100.19 | — | 0.81857 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-10-26 02:06 | XRP-USDT-SWAP | 1.2878 | 1.2894/1.2765 | 1.2770 | sup 1.2884 (ha 19 candles) | 0.01039 | 0.0087% | — | sem_zona |
| 2026-10-26 02:06 | DOGE-USDT-SWAP | 0.07697 | 0.07699/0.07623 | 0.07626 | — | 0.00063 | 0.0016% | B/compra@0.07603 (1t/1c) | zona_mapeada_setup_B |
| 2026-10-26 02:06 | ARB-USDT-SWAP | 0.16737 | 0.16752/0.16606 | 0.16644 | sup 0.16304 (ha 19 candles) | 0.00212 | 0.0065% | — | sem_zona |
| 2026-10-26 02:06 | WLD-USDT-SWAP | 0.44430 | 0.44520/0.43870 | 0.43990 | — | 0.00711 | 0.0100% | — | sem_zona |
| 2026-10-26 02:06 | SUI-USDT-SWAP | 0.91470 | 0.91500/0.90390 | 0.90420 | sup 0.90720 (ha 14 candles) | 0.01111 | 0.0100% | — | invalidado_setup_A |
| 2026-10-26 02:06 | UNI-USDT-SWAP | 6.9220 | 6.9230/6.8170 | 6.8240 | — | 0.09893 | 0.0092% | — | descartado_rr_baixo_setup_B |
| 2026-10-26 02:06 | LINK-USDT-SWAP | 11.43 | 11.43/11.31 | 11.32 | — | 0.11036 | 0.0100% | B/compra@11.52 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-26 03:06 | BTC-USDT-SWAP | 80236.4 | 80268.0/80036.4 | 79560.3 | sup 80050.0 (ha 20 candles) | 412.20 | 0.0078% | — | invalidado_setup_A |
| 2026-10-26 03:06 | ETH-USDT-SWAP | 2326.3 | 2329.2/2318.9 | 2302.1 | sup 2316.0 (ha 20 candles) | 18.82 | 0.0037% | — | sem_zona |
| 2026-10-26 03:06 | SOL-USDT-SWAP | 101.40 | 101.56/101.18 | 100.19 | — | 0.79357 | 0.0100% | B/compra@101.15 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-26 03:06 | XRP-USDT-SWAP | 1.2913 | 1.2932/1.2869 | 1.2770 | sup 1.2884 (ha 20 candles) | 0.01036 | 0.0067% | — | sem_zona |
| 2026-10-26 03:06 | DOGE-USDT-SWAP | 0.07725 | 0.07728/0.07697 | 0.07626 | — | 0.00061 | -0.0007% | B/compra@0.07603 (1t/2c) | zona_mapeada_setup_B |
| 2026-10-26 03:06 | ARB-USDT-SWAP | 0.16943 | 0.17009/0.16738 | 0.16644 | sup 0.16304 (ha 20 candles) | 0.00220 | 0.0031% | — | sem_zona |
| 2026-10-26 03:06 | WLD-USDT-SWAP | 0.44240 | 0.44650/0.44200 | 0.43990 | — | 0.00688 | 0.0095% | — | sem_zona |
| 2026-10-26 03:06 | SUI-USDT-SWAP | 0.91760 | 0.91910/0.91460 | 0.90420 | sup 0.90720 (ha 15 candles) | 0.01098 | 0.0100% | — | sem_zona |
| 2026-10-26 03:06 | UNI-USDT-SWAP | 6.9840 | 6.9980/6.9080 | 6.8240 | — | 0.09757 | 0.0077% | B/compra@6.9810 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-26 03:06 | LINK-USDT-SWAP | 11.46 | 11.48/11.42 | 11.32 | — | 0.10779 | 0.0100% | B/compra@11.52 (0t/5c) | zona_mapeada_setup_B |
