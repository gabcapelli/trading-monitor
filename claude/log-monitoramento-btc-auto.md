# Log de Monitoramento Automatico -- Multi-Par (script gratuito, GitHub Actions)

> Gerado por script Python sem LLM (ver monitor/fetch_and_check.py). Fonte: OKX. Cobre os pares em PAIRS (configuracao no topo do script) -- BTC-USDT-SWAP e os demais adicionados na expansao de 07/09/2026. Leitura e MECANICA (regras objetivas da secao 4 do plano), sem a prosa qualitativa que o Claude gerava -- cole este log numa conversa do Claude se quiser a leitura interpretativa.

| Data/Hora (BRT) | Par | Close 1h | High/Low 1h | Close 4h | Swing 1h ref | ATR 1h | Funding | Zona ativa | Status checklist |
|---|---|---|---|---|---|---|---|---|---|
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
| 2026-10-13 16:05 | BTC-USDT-SWAP | 83133.1 | 83339.0/82950.0 | 83392.4 | — | 457.44 | 0.0053% | B/compra@82850.8 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-13 16:05 | ETH-USDT-SWAP | 2508.7 | 2512.2/2499.2 | 2515.4 | — | 19.38 | 0.0032% | B/compra@2532.6 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-13 16:05 | SOL-USDT-SWAP | 107.82 | 107.98/107.07 | 107.33 | — | 1.1393 | 0.0046% | B/compra@108.37 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-13 16:05 | XRP-USDT-SWAP | 1.3720 | 1.3733/1.3632 | 1.3698 | — | 0.01180 | -0.0002% | — | sem_zona |
| 2026-10-13 16:05 | DOGE-USDT-SWAP | 0.08451 | 0.08454/0.08398 | 0.08416 | — | 0.00082 | 0.0025% | — | descartado_rr_baixo_setup_B |
| 2026-10-13 16:05 | ARB-USDT-SWAP | 0.18896 | 0.18958/0.18712 | 0.18464 | res 0.19060 (ha 12 candles) | 0.00285 | 0.0044% | — | descartado_rr_baixo_setup_B |
| 2026-10-13 16:05 | WLD-USDT-SWAP | 0.51930 | 0.52200/0.51090 | 0.50480 | — | 0.00934 | -0.0130% | B/venda@0.52210 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-13 16:05 | SUI-USDT-SWAP | 1.0509 | 1.0532/1.0438 | 1.0388 | — | 0.01478 | -0.0052% | — | sem_zona |
| 2026-10-13 16:05 | UNI-USDT-SWAP | 7.6170 | 7.6230/7.5130 | 7.5730 | — | 0.12907 | 0.0041% | B/venda@7.4530 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-13 16:05 | LINK-USDT-SWAP | 12.95 | 12.96/12.87 | 12.89 | — | 0.15564 | 0.0013% | — | sem_zona |
| 2026-10-13 17:05 | BTC-USDT-SWAP | 83255.9 | 83276.5/83122.3 | 83255.9 | — | 429.85 | 0.0046% | B/compra@82850.8 (2t/1c) | zona_mapeada_setup_B |
| 2026-10-13 17:05 | ETH-USDT-SWAP | 2507.4 | 2513.8/2502.0 | 2507.4 | sup 2487.3 (ha 8 candles) | 18.38 | 0.0052% | B/compra@2532.6 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-13 17:05 | SOL-USDT-SWAP | 107.50 | 108.23/107.23 | 107.50 | — | 1.1436 | 0.0065% | — | invalidado_setup_B |
| 2026-10-13 17:05 | XRP-USDT-SWAP | 1.3713 | 1.3760/1.3685 | 1.3713 | — | 0.01165 | -0.0005% | — | sem_zona |
| 2026-10-13 17:05 | DOGE-USDT-SWAP | 0.08454 | 0.08491/0.08427 | 0.08454 | — | 0.00081 | 0.0054% | B/compra@0.08477 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-13 17:05 | ARB-USDT-SWAP | 0.18954 | 0.19107/0.18843 | 0.18954 | res 0.19060 (ha 13 candles) | 0.00286 | 0.0038% | B/compra@0.19156 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-13 17:05 | WLD-USDT-SWAP | 0.52100 | 0.52500/0.51840 | 0.52100 | — | 0.00929 | -0.0088% | B/venda@0.52210 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-13 17:05 | SUI-USDT-SWAP | 1.0526 | 1.0603/1.0481 | 1.0526 | — | 0.01452 | -0.0025% | — | sem_zona |
| 2026-10-13 17:05 | UNI-USDT-SWAP | 7.5490 | 7.6430/7.5330 | 7.5490 | — | 0.12850 | 0.0061% | B/venda@7.4530 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-13 17:05 | LINK-USDT-SWAP | 12.92 | 12.99/12.87 | 12.92 | sup 12.71 (ha 8 candles) | 0.14957 | 0.0028% | — | sem_zona |
| 2026-10-13 18:05 | BTC-USDT-SWAP | 83365.9 | 83396.3/83138.5 | 83255.9 | — | 431.15 | 0.0022% | B/compra@82850.8 (2t/2c) | zona_mapeada_setup_B |
| 2026-10-13 18:05 | ETH-USDT-SWAP | 2509.8 | 2511.7/2505.0 | 2507.4 | sup 2494.1 (ha 3 candles) | 18.11 | 0.0063% | B/compra@2532.6 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-13 18:05 | SOL-USDT-SWAP | 107.10 | 107.64/106.97 | 107.50 | — | 1.1429 | 0.0092% | — | sem_zona |
| 2026-10-13 18:05 | XRP-USDT-SWAP | 1.3691 | 1.3749/1.3678 | 1.3713 | — | 0.01169 | -0.0020% | — | sem_zona |
| 2026-10-13 18:05 | DOGE-USDT-SWAP | 0.08460 | 0.08472/0.08437 | 0.08454 | — | 0.00080 | 0.0062% | — | descartado_rr_baixo_setup_B |
| 2026-10-13 18:05 | ARB-USDT-SWAP | 0.19080 | 0.19175/0.18819 | 0.18954 | res 0.19060 (ha 14 candles) | 0.00294 | 0.0042% | — | invalidado_setup_B |
| 2026-10-13 18:05 | WLD-USDT-SWAP | 0.51760 | 0.52390/0.51680 | 0.52100 | — | 0.00948 | -0.0040% | — | descartado_rr_baixo_setup_B |
| 2026-10-13 18:05 | SUI-USDT-SWAP | 1.0526 | 1.0564/1.0497 | 1.0526 | — | 0.01444 | 0.0020% | — | sem_zona |
| 2026-10-13 18:05 | UNI-USDT-SWAP | 7.5740 | 7.6040/7.5170 | 7.5490 | — | 0.12607 | 0.0072% | B/venda@7.4530 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-13 18:05 | LINK-USDT-SWAP | 12.92 | 12.96/12.89 | 12.92 | sup 12.71 (ha 9 candles) | 0.14629 | 0.0031% | — | sem_zona |
| 2026-10-13 19:05 | BTC-USDT-SWAP | 83479.9 | 83493.6/83258.0 | 83255.9 | — | 417.31 | -0.0018% | B/compra@82850.8 (2t/3c) | zona_mapeada_setup_B |
| 2026-10-13 19:05 | ETH-USDT-SWAP | 2510.9 | 2512.6/2505.6 | 2507.4 | sup 2494.1 (ha 4 candles) | 17.64 | 0.0066% | B/compra@2532.6 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-13 19:05 | SOL-USDT-SWAP | 107.09 | 107.22/106.86 | 107.50 | — | 1.0879 | 0.0100% | — | sem_zona |
| 2026-10-13 19:05 | XRP-USDT-SWAP | 1.3694 | 1.3708/1.3662 | 1.3713 | — | 0.01139 | -0.0027% | — | sem_zona |
| 2026-10-13 19:05 | DOGE-USDT-SWAP | 0.08461 | 0.08472/0.08439 | 0.08454 | — | 0.00078 | 0.0066% | — | sem_zona |
| 2026-10-13 19:05 | ARB-USDT-SWAP | 0.19102 | 0.19196/0.18974 | 0.18954 | res 0.19060 (ha 15 candles) | 0.00295 | 0.0021% | A/compra@0.19060 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-13 19:05 | WLD-USDT-SWAP | 0.51390 | 0.51790/0.51180 | 0.52100 | — | 0.00939 | 0.0012% | B/compra@0.50770 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-13 19:05 | SUI-USDT-SWAP | 1.0514 | 1.0539/1.0475 | 1.0526 | — | 0.01396 | 0.0048% | — | sem_zona |
| 2026-10-13 19:05 | UNI-USDT-SWAP | 7.6040 | 7.6240/7.5380 | 7.5490 | — | 0.12300 | 0.0076% | B/venda@7.4530 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-13 19:05 | LINK-USDT-SWAP | 12.92 | 12.94/12.88 | 12.92 | sup 12.71 (ha 10 candles) | 0.14100 | 0.0026% | — | sem_zona |
| 2026-10-13 20:05 | BTC-USDT-SWAP | 83479.4 | 83499.9/83350.0 | 83255.9 | — | 385.66 | -0.0040% | B/compra@82850.8 (2t/4c) | zona_mapeada_setup_B |
| 2026-10-13 20:05 | ETH-USDT-SWAP | 2510.1 | 2514.7/2506.5 | 2507.4 | sup 2494.1 (ha 5 candles) | 16.82 | 0.0063% | — | zona_expirada_setup_B |
| 2026-10-13 20:05 | SOL-USDT-SWAP | 106.98 | 107.10/106.74 | 107.50 | — | 1.0193 | 0.0100% | — | sem_zona |
| 2026-10-13 20:05 | XRP-USDT-SWAP | 1.3703 | 1.3718/1.3663 | 1.3713 | — | 0.01111 | -0.0032% | — | sem_zona |
| 2026-10-13 20:05 | DOGE-USDT-SWAP | 0.08461 | 0.08467/0.08433 | 0.08454 | — | 0.00074 | 0.0056% | — | sem_zona |
| 2026-10-13 20:05 | ARB-USDT-SWAP | 0.19007 | 0.19100/0.18965 | 0.18954 | res 0.19060 (ha 16 candles) | 0.00290 | -0.0028% | A/compra@0.19060 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-13 20:05 | WLD-USDT-SWAP | 0.51400 | 0.51980/0.51140 | 0.52100 | — | 0.00954 | 0.0042% | B/compra@0.50770 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-13 20:05 | SUI-USDT-SWAP | 1.0498 | 1.0520/1.0456 | 1.0526 | — | 0.01341 | 0.0059% | — | sem_zona |
| 2026-10-13 20:05 | UNI-USDT-SWAP | 7.5960 | 7.6080/7.5590 | 7.5490 | — | 0.12257 | 0.0066% | B/venda@7.4530 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-13 20:05 | LINK-USDT-SWAP | 12.93 | 12.94/12.89 | 12.92 | sup 12.71 (ha 11 candles) | 0.13636 | 0.0016% | — | sem_zona |
| 2026-10-13 21:06 | BTC-USDT-SWAP | 83136.6 | 83479.5/83100.0 | 83136.6 | sup 82907.7 (ha 6 candles) | 385.64 | -0.0029% | B/compra@82850.8 (2t/5c) | zona_mapeada_setup_B |
| 2026-10-13 21:06 | ETH-USDT-SWAP | 2497.0 | 2510.1/2496.1 | 2497.0 | sup 2494.1 (ha 6 candles) | 16.83 | 0.0070% | — | sem_zona |
| 2026-10-13 21:06 | SOL-USDT-SWAP | 106.79 | 106.99/106.59 | 106.79 | — | 0.98071 | 0.0100% | — | sem_zona |
| 2026-10-13 21:06 | XRP-USDT-SWAP | 1.3653 | 1.3703/1.3633 | 1.3653 | sup 1.3485 (ha 12 candles) | 0.01066 | -0.0032% | — | sem_zona |
| 2026-10-13 21:06 | DOGE-USDT-SWAP | 0.08434 | 0.08461/0.08418 | 0.08434 | — | 0.00072 | 0.0044% | — | sem_zona |
| 2026-10-13 21:06 | ARB-USDT-SWAP | 0.19114 | 0.19153/0.18922 | 0.19114 | res 0.19060 (ha 17 candles) | 0.00287 | -0.0031% | — | confirmado_calibracao_setup_A |
| 2026-10-13 21:06 | WLD-USDT-SWAP | 0.51290 | 0.51540/0.51100 | 0.51290 | — | 0.00902 | 0.0059% | B/compra@0.50770 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-13 21:06 | SUI-USDT-SWAP | 1.0470 | 1.0499/1.0449 | 1.0470 | — | 0.01266 | 0.0060% | — | sem_zona |
| 2026-10-13 21:06 | UNI-USDT-SWAP | 7.5380 | 7.5950/7.5260 | 7.5380 | — | 0.12086 | 0.0084% | B/venda@7.4530 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-13 21:06 | LINK-USDT-SWAP | 12.88 | 12.93/12.86 | 12.88 | sup 12.71 (ha 12 candles) | 0.13407 | 0.0013% | — | sem_zona |
| 2026-10-13 22:06 | BTC-USDT-SWAP | 83384.2 | 83665.0/83136.6 | 83136.6 | sup 82907.7 (ha 7 candles) | 391.68 | -0.0020% | B/compra@82850.8 (2t/6c) | zona_mapeada_setup_B |
| 2026-10-13 22:06 | ETH-USDT-SWAP | 2507.0 | 2519.6/2497.0 | 2497.0 | sup 2494.1 (ha 7 candles) | 16.68 | 0.0074% | B/venda@2518.3 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-13 22:06 | SOL-USDT-SWAP | 107.40 | 107.99/106.76 | 106.79 | — | 0.99214 | 0.0100% | — | sem_zona |
| 2026-10-13 22:06 | XRP-USDT-SWAP | 1.3723 | 1.3783/1.3652 | 1.3653 | sup 1.3485 (ha 13 candles) | 0.01090 | -0.0016% | — | sem_zona |
| 2026-10-13 22:06 | DOGE-USDT-SWAP | 0.08461 | 0.08517/0.08433 | 0.08434 | — | 0.00073 | 0.0063% | — | sem_zona |
| 2026-10-13 22:06 | ARB-USDT-SWAP | 0.19146 | 0.19508/0.19106 | 0.19114 | res 0.19060 (ha 18 candles) | 0.00298 | -0.0061% | B/compra@0.19156 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-13 22:06 | WLD-USDT-SWAP | 0.51540 | 0.52210/0.51270 | 0.51290 | — | 0.00908 | 0.0028% | B/compra@0.50770 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-13 22:06 | SUI-USDT-SWAP | 1.0555 | 1.0646/1.0462 | 1.0470 | — | 0.01311 | 0.0045% | — | sem_zona |
| 2026-10-13 22:06 | UNI-USDT-SWAP | 7.5540 | 7.6730/7.5340 | 7.5380 | — | 0.12129 | 0.0071% | B/venda@7.4530 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-13 22:06 | LINK-USDT-SWAP | 12.95 | 13.03/12.88 | 12.88 | sup 12.71 (ha 13 candles) | 0.13243 | 0.0013% | — | sem_zona |
| 2026-10-13 23:06 | BTC-USDT-SWAP | 83291.7 | 83431.3/83126.4 | 83136.6 | sup 82907.7 (ha 8 candles) | 368.81 | -0.0008% | B/compra@82850.8 (2t/7c) | zona_mapeada_setup_B |
| 2026-10-13 23:06 | ETH-USDT-SWAP | 2505.3 | 2510.7/2497.7 | 2497.0 | sup 2494.1 (ha 8 candles) | 14.96 | 0.0070% | B/venda@2518.3 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-13 23:06 | SOL-USDT-SWAP | 107.36 | 107.62/106.91 | 106.79 | — | 0.90786 | 0.0100% | — | sem_zona |
| 2026-10-13 23:06 | XRP-USDT-SWAP | 1.3690 | 1.3729/1.3655 | 1.3653 | sup 1.3485 (ha 14 candles) | 0.01004 | -0.0001% | — | sem_zona |
| 2026-10-13 23:06 | DOGE-USDT-SWAP | 0.08457 | 0.08480/0.08433 | 0.08434 | — | 0.00066 | 0.0077% | — | sem_zona |
| 2026-10-13 23:06 | ARB-USDT-SWAP | 0.19153 | 0.19193/0.18993 | 0.19114 | res 0.19060 (ha 19 candles) | 0.00282 | -0.0079% | — | confirmado_calibracao_setup_B |
| 2026-10-13 23:06 | WLD-USDT-SWAP | 0.51630 | 0.51900/0.51170 | 0.51290 | — | 0.00866 | 0.0005% | B/compra@0.50770 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-13 23:06 | SUI-USDT-SWAP | 1.0564 | 1.0610/1.0508 | 1.0470 | — | 0.01236 | 0.0018% | — | sem_zona |
| 2026-10-13 23:06 | UNI-USDT-SWAP | 7.5090 | 7.5710/7.4710 | 7.5380 | — | 0.11671 | 0.0048% | — | invalidado_setup_B |
| 2026-10-13 23:06 | LINK-USDT-SWAP | 12.93 | 12.99/12.90 | 12.88 | sup 12.71 (ha 14 candles) | 0.12143 | 0.0016% | B/venda@12.96 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-14 00:06 | BTC-USDT-SWAP | 83604.6 | 83655.9/83182.4 | 83136.6 | sup 83100.0 (ha 3 candles) | 373.76 | -0.0004% | — | zona_expirada_setup_B |
| 2026-10-14 00:06 | ETH-USDT-SWAP | 2513.1 | 2515.7/2499.7 | 2497.0 | sup 2496.1 (ha 3 candles) | 15.10 | 0.0065% | B/venda@2518.3 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-14 00:06 | SOL-USDT-SWAP | 107.72 | 107.90/107.08 | 106.79 | — | 0.89000 | 0.0100% | — | sem_zona |
| 2026-10-14 00:06 | XRP-USDT-SWAP | 1.3725 | 1.3739/1.3655 | 1.3653 | sup 1.3633 (ha 3 candles) | 0.00977 | 0.0033% | — | sem_zona |
| 2026-10-14 00:06 | DOGE-USDT-SWAP | 0.08486 | 0.08495/0.08442 | 0.08434 | — | 0.00063 | 0.0071% | — | sem_zona |
| 2026-10-14 00:06 | ARB-USDT-SWAP | 0.19298 | 0.19335/0.19146 | 0.19114 | res 0.19060 (ha 20 candles) | 0.00271 | -0.0076% | A/compra@0.19060 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-14 00:06 | WLD-USDT-SWAP | 0.51530 | 0.51830/0.51170 | 0.51290 | — | 0.00841 | -0.0021% | B/compra@0.50770 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-14 00:06 | SUI-USDT-SWAP | 1.0610 | 1.0635/1.0529 | 1.0470 | — | 0.01209 | 0.0015% | — | sem_zona |
| 2026-10-14 00:06 | UNI-USDT-SWAP | 7.5360 | 7.5450/7.4700 | 7.5380 | — | 0.11364 | 0.0065% | B/compra@7.4520 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-14 00:06 | LINK-USDT-SWAP | 12.99 | 13.00/12.89 | 12.88 | sup 12.86 (ha 3 candles) | 0.11486 | 0.0029% | B/venda@12.96 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-14 01:06 | BTC-USDT-SWAP | 83666.0 | 83949.9/83604.5 | 83666.0 | sup 83100.0 (ha 4 candles) | 360.31 | -0.0002% | B/venda@83499.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-14 01:06 | ETH-USDT-SWAP | 2512.5 | 2521.6/2509.7 | 2512.5 | sup 2496.1 (ha 4 candles) | 14.21 | 0.0063% | — | descartado_rr_baixo_setup_B |
| 2026-10-14 01:06 | SOL-USDT-SWAP | 107.78 | 108.28/107.57 | 107.78 | — | 0.84000 | 0.0100% | B/compra@108.37 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-14 01:06 | XRP-USDT-SWAP | 1.3730 | 1.3784/1.3701 | 1.3730 | sup 1.3633 (ha 4 candles) | 0.00949 | 0.0052% | — | sem_zona |
| 2026-10-14 01:06 | DOGE-USDT-SWAP | 0.08485 | 0.08515/0.08472 | 0.08485 | — | 0.00059 | 0.0051% | — | sem_zona |
| 2026-10-14 01:06 | ARB-USDT-SWAP | 0.19081 | 0.19305/0.19074 | 0.19081 | res 0.19508 (ha 3 candles) | 0.00264 | -0.0079% | A/compra@0.19060 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-14 01:06 | WLD-USDT-SWAP | 0.51480 | 0.51780/0.51370 | 0.51480 | — | 0.00801 | -0.0071% | B/compra@0.50770 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-14 01:06 | SUI-USDT-SWAP | 1.0602 | 1.0682/1.0574 | 1.0602 | — | 0.01176 | -0.0021% | — | sem_zona |
| 2026-10-14 01:06 | UNI-USDT-SWAP | 7.4800 | 7.5440/7.4750 | 7.4800 | — | 0.10807 | 0.0060% | B/compra@7.4520 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-14 01:06 | LINK-USDT-SWAP | 13.00 | 13.07/12.95 | 13.00 | sup 12.86 (ha 4 candles) | 0.10979 | 0.0004% | — | invalidado_setup_B |
| 2026-10-14 02:06 | BTC-USDT-SWAP | 83711.2 | 83857.8/83580.2 | 83666.0 | sup 83100.0 (ha 5 candles) | 334.78 | 0.0022% | — | invalidado_setup_B |
| 2026-10-14 02:06 | ETH-USDT-SWAP | 2513.8 | 2516.9/2506.3 | 2512.5 | sup 2496.1 (ha 5 candles) | 13.00 | 0.0063% | — | sem_zona |
| 2026-10-14 02:06 | SOL-USDT-SWAP | 107.91 | 108.24/107.37 | 107.78 | — | 0.76071 | 0.0100% | — | invalidado_setup_B |
| 2026-10-14 02:06 | XRP-USDT-SWAP | 1.3744 | 1.3777/1.3683 | 1.3730 | sup 1.3633 (ha 5 candles) | 0.00871 | 0.0060% | — | sem_zona |
| 2026-10-14 02:06 | DOGE-USDT-SWAP | 0.08512 | 0.08522/0.08464 | 0.08485 | — | 0.00054 | 0.0064% | B/compra@0.08477 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-14 02:06 | ARB-USDT-SWAP | 0.19147 | 0.19243/0.19041 | 0.19081 | res 0.19508 (ha 4 candles) | 0.00249 | -0.0065% | A/compra@0.19060 (2t/0c) | zona_mapeada_setup_A |
| 2026-10-14 02:06 | WLD-USDT-SWAP | 0.51680 | 0.52090/0.51310 | 0.51480 | — | 0.00777 | -0.0104% | B/compra@0.50770 (0t/7c) | zona_mapeada_setup_B |
| 2026-10-14 02:06 | SUI-USDT-SWAP | 1.0610 | 1.0652/1.0556 | 1.0602 | — | 0.01049 | -0.0044% | — | sem_zona |
| 2026-10-14 02:06 | UNI-USDT-SWAP | 7.4800 | 7.5100/7.4410 | 7.4800 | — | 0.09114 | 0.0086% | B/compra@7.4520 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-14 02:06 | LINK-USDT-SWAP | 13.03 | 13.04/12.95 | 13.00 | sup 12.86 (ha 5 candles) | 0.09971 | -0.0009% | — | sem_zona |
| 2026-10-14 03:06 | BTC-USDT-SWAP | 83436.0 | 83711.3/83363.2 | 83666.0 | sup 83100.0 (ha 6 candles) | 322.33 | 0.0041% | — | sem_zona |
| 2026-10-14 03:06 | ETH-USDT-SWAP | 2502.7 | 2513.8/2499.0 | 2512.5 | sup 2496.1 (ha 6 candles) | 12.71 | 0.0061% | — | sem_zona |
| 2026-10-14 03:06 | SOL-USDT-SWAP | 107.14 | 107.91/106.93 | 107.78 | — | 0.73929 | 0.0100% | — | sem_zona |
| 2026-10-14 03:06 | XRP-USDT-SWAP | 1.3641 | 1.3745/1.3627 | 1.3730 | sup 1.3633 (ha 6 candles) | 0.00851 | 0.0044% | — | sem_zona |
| 2026-10-14 03:06 | DOGE-USDT-SWAP | 0.08446 | 0.08513/0.08432 | 0.08485 | — | 0.00053 | 0.0052% | — | invalidado_setup_B |
| 2026-10-14 03:06 | ARB-USDT-SWAP | 0.18926 | 0.19146/0.18857 | 0.19081 | res 0.19508 (ha 5 candles) | 0.00252 | -0.0055% | — | invalidado_setup_A |
| 2026-10-14 03:06 | WLD-USDT-SWAP | 0.50880 | 0.51680/0.50710 | 0.51480 | — | 0.00792 | -0.0132% | B/compra@0.50770 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-14 03:06 | SUI-USDT-SWAP | 1.0469 | 1.0609/1.0451 | 1.0602 | — | 0.01021 | -0.0046% | — | sem_zona |
| 2026-10-14 03:06 | UNI-USDT-SWAP | 7.2980 | 7.4790/7.2520 | 7.4800 | — | 0.09843 | 0.0095% | — | invalidado_setup_B |
| 2026-10-14 03:06 | LINK-USDT-SWAP | 12.86 | 13.03/12.84 | 13.00 | sup 12.86 (ha 6 candles) | 0.09843 | -0.0033% | — | sem_zona |
| 2026-10-14 04:06 | BTC-USDT-SWAP | 83404.4 | 83604.4/83312.0 | 83666.0 | sup 83100.0 (ha 7 candles) | 326.33 | 0.0056% | — | sem_zona |
| 2026-10-14 04:06 | ETH-USDT-SWAP | 2504.0 | 2509.1/2498.7 | 2512.5 | sup 2496.1 (ha 7 candles) | 12.69 | 0.0056% | — | sem_zona |
| 2026-10-14 04:06 | SOL-USDT-SWAP | 107.13 | 107.43/106.92 | 107.78 | — | 0.72929 | 0.0100% | — | sem_zona |
| 2026-10-14 04:06 | XRP-USDT-SWAP | 1.3677 | 1.3687/1.3617 | 1.3730 | sup 1.3633 (ha 7 candles) | 0.00831 | 0.0030% | — | sem_zona |
| 2026-10-14 04:06 | DOGE-USDT-SWAP | 0.08454 | 0.08468/0.08427 | 0.08485 | — | 0.00052 | 0.0034% | — | sem_zona |
| 2026-10-14 04:06 | ARB-USDT-SWAP | 0.18926 | 0.18979/0.18840 | 0.19081 | res 0.19508 (ha 6 candles) | 0.00242 | -0.0022% | B/compra@0.18820 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-14 04:06 | WLD-USDT-SWAP | 0.51100 | 0.51360/0.50610 | 0.51480 | — | 0.00734 | -0.0093% | — | descartado_rr_baixo_setup_B |
| 2026-10-14 04:06 | SUI-USDT-SWAP | 1.0493 | 1.0524/1.0435 | 1.0602 | — | 0.00999 | -0.0023% | — | sem_zona |
| 2026-10-14 04:06 | UNI-USDT-SWAP | 7.3540 | 7.3920/7.2780 | 7.4800 | — | 0.10007 | 0.0100% | — | sem_zona |
| 2026-10-14 04:06 | LINK-USDT-SWAP | 12.88 | 12.91/12.84 | 13.00 | sup 12.86 (ha 7 candles) | 0.09764 | -0.0050% | — | sem_zona |
| 2026-10-14 05:06 | BTC-USDT-SWAP | 83537.7 | 83610.0/83294.1 | 83537.7 | — | 318.01 | 0.0063% | — | sem_zona |
| 2026-10-14 05:06 | ETH-USDT-SWAP | 2510.1 | 2511.4/2501.6 | 2510.1 | sup 2496.1 (ha 8 candles) | 12.12 | 0.0035% | — | sem_zona |
| 2026-10-14 05:06 | SOL-USDT-SWAP | 107.43 | 107.59/106.95 | 107.43 | — | 0.72643 | 0.0091% | — | sem_zona |
| 2026-10-14 05:06 | XRP-USDT-SWAP | 1.3724 | 1.3746/1.3656 | 1.3724 | sup 1.3633 (ha 8 candles) | 0.00830 | 0.0031% | — | sem_zona |
| 2026-10-14 05:06 | DOGE-USDT-SWAP | 0.08470 | 0.08489/0.08446 | 0.08470 | — | 0.00051 | 0.0015% | — | sem_zona |
| 2026-10-14 05:06 | ARB-USDT-SWAP | 0.18976 | 0.19011/0.18882 | 0.18976 | res 0.19508 (ha 7 candles) | 0.00231 | -0.0002% | B/compra@0.18820 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-14 05:06 | WLD-USDT-SWAP | 0.51330 | 0.51550/0.50990 | 0.51330 | sup 0.51100 (ha 8 candles) | 0.00726 | -0.0034% | — | sem_zona |
| 2026-10-14 05:06 | SUI-USDT-SWAP | 1.0557 | 1.0576/1.0469 | 1.0557 | — | 0.01009 | -0.0020% | — | sem_zona |
| 2026-10-14 05:06 | UNI-USDT-SWAP | 7.3930 | 7.3980/7.3440 | 7.3930 | — | 0.09714 | 0.0100% | — | sem_zona |
| 2026-10-14 05:06 | LINK-USDT-SWAP | 12.92 | 12.94/12.86 | 12.92 | sup 12.86 (ha 8 candles) | 0.09707 | -0.0035% | — | sem_zona |
| 2026-10-14 06:06 | BTC-USDT-SWAP | 83400.1 | 84116.3/83323.8 | 83537.7 | — | 346.84 | 0.0074% | — | sem_zona |
| 2026-10-14 06:06 | ETH-USDT-SWAP | 2504.6 | 2529.9/2502.6 | 2510.1 | sup 2496.1 (ha 9 candles) | 13.14 | 0.0022% | — | sem_zona |
| 2026-10-14 06:06 | SOL-USDT-SWAP | 106.97 | 108.64/106.97 | 107.43 | — | 0.78071 | 0.0081% | — | sem_zona |
| 2026-10-14 06:06 | XRP-USDT-SWAP | 1.3698 | 1.3861/1.3685 | 1.3724 | sup 1.3633 (ha 9 candles) | 0.00884 | 0.0018% | — | sem_zona |
| 2026-10-14 06:06 | DOGE-USDT-SWAP | 0.08444 | 0.08563/0.08444 | 0.08470 | — | 0.00056 | 0.0021% | — | sem_zona |
| 2026-10-14 06:06 | ARB-USDT-SWAP | 0.18796 | 0.19168/0.18759 | 0.18976 | res 0.19508 (ha 8 candles) | 0.00243 | -0.0008% | B/compra@0.18820 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-14 06:06 | WLD-USDT-SWAP | 0.50800 | 0.52090/0.50790 | 0.51330 | sup 0.51100 (ha 9 candles) | 0.00740 | -0.0018% | A/venda@0.51100 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-14 06:06 | SUI-USDT-SWAP | 1.0511 | 1.0708/1.0494 | 1.0557 | — | 0.01094 | -0.0035% | — | sem_zona |
| 2026-10-14 06:06 | UNI-USDT-SWAP | 7.3450 | 7.5010/7.3330 | 7.3930 | — | 0.10129 | 0.0100% | — | sem_zona |
| 2026-10-14 06:06 | LINK-USDT-SWAP | 12.93 | 13.10/12.91 | 12.92 | sup 12.86 (ha 9 candles) | 0.10407 | -0.0021% | — | sem_zona |
| 2026-10-14 07:06 | BTC-USDT-SWAP | 83226.0 | 83505.6/83177.0 | 83537.7 | — | 359.29 | 0.0097% | B/compra@83123.1 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-14 07:06 | ETH-USDT-SWAP | 2495.7 | 2507.9/2492.8 | 2510.1 | sup 2496.1 (ha 10 candles) | 13.38 | 0.0012% | A/venda@2496.1 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-14 07:06 | SOL-USDT-SWAP | 106.57 | 107.21/106.47 | 107.43 | — | 0.76214 | 0.0064% | — | sem_zona |
| 2026-10-14 07:06 | XRP-USDT-SWAP | 1.3659 | 1.3719/1.3624 | 1.3724 | sup 1.3617 (ha 3 candles) | 0.00898 | 0.0003% | — | sem_zona |
| 2026-10-14 07:06 | DOGE-USDT-SWAP | 0.08419 | 0.08453/0.08398 | 0.08470 | — | 0.00055 | 0.0043% | — | sem_zona |
| 2026-10-14 07:06 | ARB-USDT-SWAP | 0.18742 | 0.18865/0.18693 | 0.18976 | res 0.19508 (ha 9 candles) | 0.00236 | 0.0019% | — | invalidado_setup_B |
| 2026-10-14 07:06 | WLD-USDT-SWAP | 0.50760 | 0.51070/0.50440 | 0.51330 | sup 0.51100 (ha 10 candles) | 0.00738 | -0.0006% | A/venda@0.51100 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-14 07:06 | SUI-USDT-SWAP | 1.0469 | 1.0548/1.0416 | 1.0557 | — | 0.01101 | -0.0033% | — | sem_zona |
| 2026-10-14 07:06 | UNI-USDT-SWAP | 7.3450 | 7.3760/7.3260 | 7.3930 | — | 0.09700 | 0.0100% | — | sem_zona |
| 2026-10-14 07:06 | LINK-USDT-SWAP | 12.89 | 12.98/12.87 | 12.92 | sup 12.84 (ha 3 candles) | 0.10393 | -0.0003% | — | sem_zona |
| 2026-10-14 08:06 | BTC-USDT-SWAP | 83436.6 | 83436.7/83000.0 | 83537.7 | — | 372.07 | 0.0096% | — | descartado_rr_baixo_setup_B |
| 2026-10-14 08:06 | ETH-USDT-SWAP | 2506.4 | 2506.4/2475.2 | 2510.1 | sup 2496.1 (ha 11 candles) | 15.13 | 0.0007% | — | invalidado_setup_A |
| 2026-10-14 08:06 | SOL-USDT-SWAP | 107.15 | 107.15/106.01 | 107.43 | — | 0.79571 | 0.0054% | — | sem_zona |
| 2026-10-14 08:06 | XRP-USDT-SWAP | 1.3744 | 1.3750/1.3608 | 1.3724 | sup 1.3617 (ha 4 candles) | 0.00949 | 0.0003% | — | sem_zona |
| 2026-10-14 08:06 | DOGE-USDT-SWAP | 0.08441 | 0.08441/0.08381 | 0.08470 | — | 0.00057 | 0.0058% | — | sem_zona |
| 2026-10-14 08:06 | ARB-USDT-SWAP | 0.18771 | 0.18788/0.18653 | 0.18976 | res 0.19508 (ha 10 candles) | 0.00221 | 0.0018% | — | sem_zona |
| 2026-10-14 08:06 | WLD-USDT-SWAP | 0.50910 | 0.51010/0.50560 | 0.51330 | sup 0.51100 (ha 11 candles) | 0.00719 | 0.0031% | A/venda@0.51100 (2t/0c) | zona_mapeada_setup_A |
| 2026-10-14 08:06 | SUI-USDT-SWAP | 1.0514 | 1.0517/1.0431 | 1.0557 | — | 0.01115 | -0.0027% | — | sem_zona |
| 2026-10-14 08:06 | UNI-USDT-SWAP | 7.3580 | 7.3820/7.3260 | 7.3930 | — | 0.09479 | 0.0100% | — | sem_zona |
| 2026-10-14 08:06 | LINK-USDT-SWAP | 12.92 | 12.93/12.81 | 12.92 | sup 12.84 (ha 4 candles) | 0.10671 | 0.0018% | — | sem_zona |
| 2026-10-14 09:06 | BTC-USDT-SWAP | 83435.9 | 83479.6/83294.4 | 83435.9 | — | 368.47 | 0.0090% | — | sem_zona |
| 2026-10-14 09:06 | ETH-USDT-SWAP | 2503.5 | 2506.7/2499.2 | 2503.5 | sup 2496.1 (ha 12 candles) | 15.16 | 0.0009% | — | sem_zona |
| 2026-10-14 09:06 | SOL-USDT-SWAP | 107.11 | 107.24/106.58 | 107.11 | — | 0.81714 | 0.0047% | — | sem_zona |
| 2026-10-14 09:06 | XRP-USDT-SWAP | 1.3734 | 1.3747/1.3696 | 1.3734 | sup 1.3617 (ha 5 candles) | 0.00952 | 0.0005% | — | sem_zona |
| 2026-10-14 09:06 | DOGE-USDT-SWAP | 0.08436 | 0.08446/0.08403 | 0.08436 | — | 0.00057 | 0.0049% | — | sem_zona |
| 2026-10-14 09:06 | ARB-USDT-SWAP | 0.18863 | 0.18879/0.18652 | 0.18863 | res 0.19168 (ha 3 candles) | 0.00221 | 0.0026% | — | sem_zona |
| 2026-10-14 09:06 | WLD-USDT-SWAP | 0.51060 | 0.51220/0.50550 | 0.51060 | sup 0.51100 (ha 12 candles) | 0.00724 | 0.0046% | — | zona_expirada_setup_A |
| 2026-10-14 09:06 | SUI-USDT-SWAP | 1.0543 | 1.0565/1.0460 | 1.0543 | — | 0.01144 | -0.0019% | — | sem_zona |
| 2026-10-14 09:06 | UNI-USDT-SWAP | 7.3590 | 7.3700/7.3120 | 7.3590 | — | 0.09279 | 0.0100% | — | sem_zona |
| 2026-10-14 09:06 | LINK-USDT-SWAP | 12.90 | 12.94/12.86 | 12.90 | sup 12.84 (ha 5 candles) | 0.10786 | 0.0045% | B/venda@12.96 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-14 10:06 | BTC-USDT-SWAP | 82702.4 | 83910.0/82571.0 | 83435.9 | — | 453.41 | 0.0090% | B/compra@82752.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-14 10:06 | ETH-USDT-SWAP | 2475.3 | 2520.0/2472.4 | 2503.5 | sup 2496.1 (ha 13 candles) | 17.97 | -0.0002% | — | sem_zona |
| 2026-10-14 10:06 | SOL-USDT-SWAP | 105.42 | 107.89/105.33 | 107.11 | — | 0.97429 | 0.0030% | B/compra@105.61 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-14 10:06 | XRP-USDT-SWAP | 1.3572 | 1.3829/1.3543 | 1.3734 | sup 1.3617 (ha 6 candles) | 0.01117 | 0.0025% | A/venda@1.3617 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-14 10:06 | DOGE-USDT-SWAP | 0.08322 | 0.08496/0.08303 | 0.08436 | — | 0.00069 | 0.0037% | — | sem_zona |
| 2026-10-14 10:06 | ARB-USDT-SWAP | 0.18400 | 0.18994/0.18251 | 0.18863 | res 0.19168 (ha 4 candles) | 0.00264 | 0.0034% | — | sem_zona |
| 2026-10-14 10:06 | WLD-USDT-SWAP | 0.49980 | 0.51490/0.49250 | 0.51060 | sup 0.51100 (ha 13 candles) | 0.00824 | 0.0051% | — | sem_zona |
| 2026-10-14 10:06 | SUI-USDT-SWAP | 1.0280 | 1.0647/1.0081 | 1.0543 | — | 0.01503 | -0.0028% | — | sem_zona |
| 2026-10-14 10:06 | UNI-USDT-SWAP | 7.1990 | 7.4100/7.1870 | 7.3590 | — | 0.10521 | 0.0100% | B/compra@7.2270 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-14 10:06 | LINK-USDT-SWAP | 12.70 | 13.02/12.69 | 12.90 | sup 12.84 (ha 6 candles) | 0.12714 | 0.0068% | — | descartado_rr_baixo_setup_B |
| 2026-10-14 11:06 | BTC-USDT-SWAP | 82291.6 | 83079.9/82265.1 | 83435.9 | — | 484.50 | 0.0090% | — | invalidado_setup_B |
| 2026-10-14 11:06 | ETH-USDT-SWAP | 2451.2 | 2486.4/2450.2 | 2503.5 | sup 2496.1 (ha 14 candles) | 19.57 | -0.0001% | — | sem_zona |
| 2026-10-14 11:06 | SOL-USDT-SWAP | 104.79 | 106.36/104.46 | 107.11 | — | 1.0814 | 0.0017% | — | invalidado_setup_B |
| 2026-10-14 11:06 | XRP-USDT-SWAP | 1.3490 | 1.3664/1.3484 | 1.3734 | sup 1.3617 (ha 7 candles) | 0.01196 | 0.0060% | — | descartado_rr_baixo_setup_A |
| 2026-10-14 11:06 | DOGE-USDT-SWAP | 0.08259 | 0.08372/0.08232 | 0.08436 | — | 0.00076 | 0.0059% | — | sem_zona |
| 2026-10-14 11:06 | ARB-USDT-SWAP | 0.18266 | 0.18573/0.18210 | 0.18863 | res 0.19168 (ha 5 candles) | 0.00274 | 0.0042% | — | sem_zona |
| 2026-10-14 11:06 | WLD-USDT-SWAP | 0.49490 | 0.50440/0.49280 | 0.51060 | sup 0.51100 (ha 14 candles) | 0.00875 | 0.0033% | — | sem_zona |
| 2026-10-14 11:06 | SUI-USDT-SWAP | 1.0204 | 1.0377/1.0136 | 1.0543 | — | 0.01639 | -0.0023% | — | sem_zona |
| 2026-10-14 11:06 | UNI-USDT-SWAP | 7.2440 | 7.3390/7.1530 | 7.3590 | — | 0.11350 | 0.0100% | B/compra@7.2270 (1t/0c) | zona_mapeada_setup_B |
| 2026-10-14 11:06 | LINK-USDT-SWAP | 12.54 | 12.80/12.54 | 12.90 | sup 12.84 (ha 7 candles) | 0.14000 | 0.0050% | A/venda@12.84 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-14 12:06 | BTC-USDT-SWAP | 81929.1 | 82496.9/81666.6 | 83435.9 | — | 506.06 | 0.0079% | — | sem_zona |
| 2026-10-14 12:06 | ETH-USDT-SWAP | 2433.6 | 2456.4/2416.0 | 2503.5 | sup 2496.1 (ha 15 candles) | 20.84 | 0.0007% | — | sem_zona |
| 2026-10-14 12:06 | SOL-USDT-SWAP | 104.32 | 105.20/103.45 | 107.11 | — | 1.1186 | 0.0017% | — | sem_zona |
| 2026-10-14 12:06 | XRP-USDT-SWAP | 1.3351 | 1.3524/1.3275 | 1.3734 | sup 1.3617 (ha 8 candles) | 0.01280 | 0.0066% | — | sem_zona |
| 2026-10-14 12:06 | DOGE-USDT-SWAP | 0.08235 | 0.08275/0.08176 | 0.08436 | — | 0.00077 | 0.0059% | — | sem_zona |
| 2026-10-14 12:06 | ARB-USDT-SWAP | 0.18127 | 0.18354/0.17951 | 0.18863 | res 0.19168 (ha 6 candles) | 0.00274 | 0.0040% | — | sem_zona |
| 2026-10-14 12:06 | WLD-USDT-SWAP | 0.49250 | 0.49640/0.48590 | 0.51060 | sup 0.51100 (ha 15 candles) | 0.00883 | 0.0034% | — | sem_zona |
| 2026-10-14 12:06 | SUI-USDT-SWAP | 1.0176 | 1.0243/1.0047 | 1.0543 | — | 0.01648 | -0.0036% | — | sem_zona |
| 2026-10-14 12:06 | UNI-USDT-SWAP | 7.2050 | 7.2740/7.1340 | 7.3590 | — | 0.11357 | 0.0100% | B/compra@7.2270 (2t/0c) | zona_mapeada_setup_B |
| 2026-10-14 12:06 | LINK-USDT-SWAP | 12.40 | 12.58/12.30 | 12.90 | sup 12.84 (ha 8 candles) | 0.14900 | 0.0036% | A/venda@12.84 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-14 13:06 | BTC-USDT-SWAP | 81604.5 | 82062.6/81550.0 | 81604.5 | — | 520.90 | 0.0071% | — | sem_zona |
| 2026-10-14 13:06 | ETH-USDT-SWAP | 2429.0 | 2446.4/2420.2 | 2429.0 | sup 2496.1 (ha 16 candles) | 21.78 | 0.0023% | — | sem_zona |
| 2026-10-14 13:06 | SOL-USDT-SWAP | 103.80 | 104.82/103.53 | 103.80 | — | 1.1600 | 0.0001% | — | sem_zona |
| 2026-10-14 13:06 | XRP-USDT-SWAP | 1.3266 | 1.3391/1.3262 | 1.3266 | sup 1.3617 (ha 9 candles) | 0.01319 | 0.0056% | — | sem_zona |
| 2026-10-14 13:06 | DOGE-USDT-SWAP | 0.08198 | 0.08267/0.08181 | 0.08198 | — | 0.00080 | 0.0064% | — | sem_zona |
| 2026-10-14 13:06 | ARB-USDT-SWAP | 0.18212 | 0.18268/0.17907 | 0.18212 | — | 0.00285 | 0.0034% | — | sem_zona |
| 2026-10-14 13:06 | WLD-USDT-SWAP | 0.48900 | 0.49260/0.48500 | 0.48900 | sup 0.51100 (ha 16 candles) | 0.00885 | 0.0083% | — | sem_zona |
| 2026-10-14 13:06 | SUI-USDT-SWAP | 1.0081 | 1.0186/1.0055 | 1.0081 | — | 0.01669 | -0.0025% | B/compra@0.99710 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-14 13:06 | UNI-USDT-SWAP | 7.1470 | 7.2750/7.1230 | 7.1470 | sup 7.2520 (ha 10 candles) | 0.11729 | 0.0100% | — | invalidado_setup_B |
| 2026-10-14 13:06 | LINK-USDT-SWAP | 12.41 | 12.49/12.33 | 12.41 | sup 12.84 (ha 9 candles) | 0.15486 | 0.0011% | A/venda@12.84 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-14 14:06 | BTC-USDT-SWAP | 81976.0 | 81981.1/81542.8 | 81604.5 | — | 518.39 | 0.0070% | — | sem_zona |
| 2026-10-14 14:06 | ETH-USDT-SWAP | 2447.9 | 2448.0/2426.0 | 2429.0 | sup 2496.1 (ha 17 candles) | 22.21 | 0.0039% | — | sem_zona |
| 2026-10-14 14:06 | SOL-USDT-SWAP | 104.91 | 105.00/103.72 | 103.80 | — | 1.1929 | -0.0006% | — | sem_zona |
| 2026-10-14 14:06 | XRP-USDT-SWAP | 1.3359 | 1.3385/1.3250 | 1.3266 | sup 1.3617 (ha 10 candles) | 0.01356 | 0.0059% | — | sem_zona |
| 2026-10-14 14:06 | DOGE-USDT-SWAP | 0.08296 | 0.08296/0.08197 | 0.08198 | — | 0.00083 | 0.0095% | — | sem_zona |
| 2026-10-14 14:06 | ARB-USDT-SWAP | 0.18567 | 0.18644/0.18214 | 0.18212 | — | 0.00303 | 0.0010% | — | sem_zona |
| 2026-10-14 14:06 | WLD-USDT-SWAP | 0.49680 | 0.49830/0.48810 | 0.48900 | sup 0.51100 (ha 17 candles) | 0.00911 | 0.0100% | — | sem_zona |
| 2026-10-14 14:06 | SUI-USDT-SWAP | 1.0305 | 1.0306/1.0078 | 1.0081 | — | 0.01756 | -0.0019% | B/compra@0.99710 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-14 14:06 | UNI-USDT-SWAP | 7.2550 | 7.2820/7.1470 | 7.1470 | sup 7.2520 (ha 11 candles) | 0.12157 | 0.0100% | — | sem_zona |
| 2026-10-14 14:06 | LINK-USDT-SWAP | 12.58 | 12.58/12.41 | 12.41 | sup 12.84 (ha 10 candles) | 0.15936 | 0.0015% | A/venda@12.84 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-14 15:06 | BTC-USDT-SWAP | 81560.9 | 82061.6/81452.9 | 81604.5 | — | 537.19 | 0.0060% | — | sem_zona |
| 2026-10-14 15:06 | ETH-USDT-SWAP | 2431.0 | 2452.7/2427.1 | 2429.0 | sup 2416.0 (ha 3 candles) | 23.20 | 0.0054% | — | sem_zona |
| 2026-10-14 15:06 | SOL-USDT-SWAP | 104.37 | 105.33/104.27 | 103.80 | — | 1.2179 | -0.0004% | — | sem_zona |
| 2026-10-14 15:06 | XRP-USDT-SWAP | 1.3286 | 1.3396/1.3267 | 1.3266 | sup 1.3617 (ha 11 candles) | 0.01389 | 0.0059% | — | sem_zona |
| 2026-10-14 15:06 | DOGE-USDT-SWAP | 0.08207 | 0.08321/0.08200 | 0.08198 | — | 0.00088 | 0.0100% | — | sem_zona |
| 2026-10-14 15:06 | ARB-USDT-SWAP | 0.18289 | 0.18633/0.18259 | 0.18212 | — | 0.00313 | -0.0027% | — | sem_zona |
| 2026-10-14 15:06 | WLD-USDT-SWAP | 0.49240 | 0.50020/0.49090 | 0.48900 | sup 0.51100 (ha 18 candles) | 0.00948 | 0.0100% | — | sem_zona |
| 2026-10-14 15:06 | SUI-USDT-SWAP | 1.0264 | 1.0366/1.0243 | 1.0081 | — | 0.01766 | -0.0017% | B/compra@0.99710 (0t/2c) | zona_mapeada_setup_B |
| 2026-10-14 15:06 | UNI-USDT-SWAP | 7.1390 | 7.2850/7.1140 | 7.1470 | sup 7.2520 (ha 12 candles) | 0.12886 | 0.0100% | A/venda@7.2520 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-14 15:06 | LINK-USDT-SWAP | 12.45 | 12.62/12.44 | 12.41 | sup 12.30 (ha 3 candles) | 0.16457 | 0.0018% | A/venda@12.84 (0t/4c) | zona_mapeada_setup_A |
| 2026-10-14 16:06 | BTC-USDT-SWAP | 81680.8 | 81746.4/81492.5 | 81604.5 | — | 535.50 | 0.0053% | — | sem_zona |
| 2026-10-14 16:06 | ETH-USDT-SWAP | 2430.7 | 2433.6/2422.2 | 2429.0 | sup 2416.0 (ha 4 candles) | 23.26 | 0.0070% | — | sem_zona |
| 2026-10-14 16:06 | SOL-USDT-SWAP | 104.30 | 104.52/103.87 | 103.80 | — | 1.2021 | 0.0016% | — | sem_zona |
| 2026-10-14 16:06 | XRP-USDT-SWAP | 1.3283 | 1.3306/1.3214 | 1.3266 | sup 1.3617 (ha 12 candles) | 0.01387 | 0.0051% | — | sem_zona |
| 2026-10-14 16:06 | DOGE-USDT-SWAP | 0.08201 | 0.08215/0.08168 | 0.08198 | — | 0.00088 | 0.0100% | — | sem_zona |
| 2026-10-14 16:06 | ARB-USDT-SWAP | 0.18211 | 0.18340/0.18132 | 0.18212 | — | 0.00313 | -0.0044% | — | sem_zona |
| 2026-10-14 16:06 | WLD-USDT-SWAP | 0.49090 | 0.49270/0.48760 | 0.48900 | sup 0.48500 (ha 3 candles) | 0.00929 | 0.0100% | — | sem_zona |
| 2026-10-14 16:06 | SUI-USDT-SWAP | 1.0233 | 1.0282/1.0198 | 1.0081 | — | 0.01758 | 0.0016% | B/compra@0.99710 (0t/3c) | zona_mapeada_setup_B |
| 2026-10-14 16:06 | UNI-USDT-SWAP | 7.1110 | 7.1680/7.0840 | 7.1470 | sup 7.2520 (ha 13 candles) | 0.12993 | 0.0100% | A/venda@7.2520 (0t/1c) | zona_mapeada_setup_A |
| 2026-10-14 16:06 | LINK-USDT-SWAP | 12.41 | 12.46/12.36 | 12.41 | sup 12.30 (ha 4 candles) | 0.16500 | 0.0017% | A/venda@12.84 (0t/5c) | zona_mapeada_setup_A |
| 2026-10-14 17:06 | BTC-USDT-SWAP | 81796.0 | 81861.6/81500.0 | 81796.0 | — | 536.46 | 0.0046% | — | sem_zona |
| 2026-10-14 17:06 | ETH-USDT-SWAP | 2429.9 | 2436.6/2420.4 | 2429.9 | sup 2416.0 (ha 5 candles) | 23.35 | 0.0075% | — | sem_zona |
| 2026-10-14 17:06 | SOL-USDT-SWAP | 104.17 | 104.75/103.72 | 104.17 | — | 1.2057 | 0.0027% | — | sem_zona |
| 2026-10-14 17:06 | XRP-USDT-SWAP | 1.3254 | 1.3324/1.3218 | 1.3254 | sup 1.3617 (ha 13 candles) | 0.01379 | 0.0026% | — | sem_zona |
| 2026-10-14 17:06 | DOGE-USDT-SWAP | 0.08200 | 0.08228/0.08164 | 0.08200 | — | 0.00086 | 0.0100% | — | sem_zona |
| 2026-10-14 17:06 | ARB-USDT-SWAP | 0.18139 | 0.18211/0.18028 | 0.18139 | — | 0.00306 | -0.0053% | — | sem_zona |
| 2026-10-14 17:06 | WLD-USDT-SWAP | 0.48950 | 0.49120/0.48580 | 0.48950 | sup 0.48500 (ha 4 candles) | 0.00898 | 0.0100% | — | sem_zona |
| 2026-10-14 17:06 | SUI-USDT-SWAP | 1.0210 | 1.0249/1.0164 | 1.0210 | — | 0.01705 | 0.0043% | B/compra@0.99710 (0t/4c) | zona_mapeada_setup_B |
| 2026-10-14 17:06 | UNI-USDT-SWAP | 7.1120 | 7.1300/7.0740 | 7.1120 | sup 7.2520 (ha 14 candles) | 0.11764 | 0.0100% | A/venda@7.2520 (0t/2c) | zona_mapeada_setup_A |
| 2026-10-14 17:06 | LINK-USDT-SWAP | 12.42 | 12.49/12.35 | 12.42 | sup 12.30 (ha 5 candles) | 0.16193 | 0.0027% | A/venda@12.84 (0t/6c) | zona_mapeada_setup_A |
| 2026-10-14 18:06 | BTC-USDT-SWAP | 81736.7 | 81942.3/81604.2 | 81796.0 | — | 539.73 | 0.0031% | — | sem_zona |
| 2026-10-14 18:06 | ETH-USDT-SWAP | 2416.0 | 2434.3/2404.0 | 2429.9 | sup 2416.0 (ha 6 candles) | 24.77 | 0.0068% | A/venda@2416.0 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-14 18:06 | SOL-USDT-SWAP | 104.06 | 104.51/103.63 | 104.17 | — | 1.2321 | 0.0026% | — | sem_zona |
| 2026-10-14 18:06 | XRP-USDT-SWAP | 1.3239 | 1.3296/1.3183 | 1.3254 | sup 1.3617 (ha 14 candles) | 0.01409 | 0.0006% | — | sem_zona |
| 2026-10-14 18:06 | DOGE-USDT-SWAP | 0.08168 | 0.08227/0.08129 | 0.08200 | — | 0.00090 | 0.0100% | — | sem_zona |
| 2026-10-14 18:06 | ARB-USDT-SWAP | 0.18098 | 0.18211/0.18037 | 0.18139 | — | 0.00308 | -0.0064% | B/compra@0.17900 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-14 18:06 | WLD-USDT-SWAP | 0.48850 | 0.49160/0.48660 | 0.48950 | sup 0.48500 (ha 5 candles) | 0.00880 | 0.0100% | — | sem_zona |
| 2026-10-14 18:06 | SUI-USDT-SWAP | 1.0183 | 1.0250/1.0148 | 1.0210 | — | 0.01714 | 0.0055% | B/compra@0.99710 (0t/5c) | zona_mapeada_setup_B |
| 2026-10-14 18:06 | UNI-USDT-SWAP | 7.0860 | 7.1400/7.0720 | 7.1120 | sup 7.2520 (ha 15 candles) | 0.11436 | 0.0100% | A/venda@7.2520 (0t/3c) | zona_mapeada_setup_A |
| 2026-10-14 18:06 | LINK-USDT-SWAP | 12.38 | 12.45/12.36 | 12.42 | sup 12.30 (ha 6 candles) | 0.16271 | 0.0021% | A/venda@12.84 (0t/7c) | zona_mapeada_setup_A |
| 2026-10-14 19:06 | BTC-USDT-SWAP | 81741.0 | 81931.2/81601.8 | 81796.0 | — | 540.69 | 0.0022% | — | sem_zona |
| 2026-10-14 19:06 | ETH-USDT-SWAP | 2419.6 | 2429.6/2402.0 | 2429.9 | sup 2416.0 (ha 7 candles) | 26.05 | 0.0071% | A/venda@2416.0 (1t/0c) | zona_mapeada_setup_A |
| 2026-10-14 19:06 | SOL-USDT-SWAP | 104.68 | 104.92/103.76 | 104.17 | — | 1.2693 | 0.0022% | B/compra@105.61 (0t/0c) | zona_mapeada_setup_B |
| 2026-10-14 19:06 | XRP-USDT-SWAP | 1.3341 | 1.3359/1.3199 | 1.3254 | sup 1.3617 (ha 15 candles) | 0.01459 | -0.0009% | A/venda@1.3617 (0t/0c) | zona_mapeada_setup_A |
| 2026-10-14 19:06 | DOGE-USDT-SWAP | 0.08186 | 0.08213/0.08128 | 0.08200 | — | 0.00093 | 0.0100% | — | sem_zona |
| 2026-10-14 19:06 | ARB-USDT-SWAP | 0.18189 | 0.18229/0.18021 | 0.18139 | — | 0.00314 | -0.0069% | B/compra@0.17900 (0t/1c) | zona_mapeada_setup_B |
| 2026-10-14 19:06 | WLD-USDT-SWAP | 0.49520 | 0.49570/0.48650 | 0.48950 | sup 0.48500 (ha 6 candles) | 0.00906 | 0.0100% | — | sem_zona |
| 2026-10-14 19:06 | SUI-USDT-SWAP | 1.0244 | 1.0261/1.0141 | 1.0210 | — | 0.01724 | 0.0066% | B/compra@0.99710 (0t/6c) | zona_mapeada_setup_B |
| 2026-10-14 19:06 | UNI-USDT-SWAP | 7.1210 | 7.1460/7.0560 | 7.1120 | sup 7.2520 (ha 16 candles) | 0.11693 | 0.0100% | A/venda@7.2520 (0t/4c) | zona_mapeada_setup_A |
| 2026-10-14 19:06 | LINK-USDT-SWAP | 12.43 | 12.47/12.33 | 12.42 | sup 12.30 (ha 7 candles) | 0.16700 | 0.0034% | — | zona_expirada_setup_A |
