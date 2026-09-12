# Log de Monitoramento Automatico -- Multi-Par (script gratuito, GitHub Actions)

> Gerado por script Python sem LLM (ver monitor/fetch_and_check.py). Fonte: OKX. Cobre os pares em PAIRS (configuracao no topo do script) -- BTC-USDT-SWAP e os demais adicionados na expansao de 07/09/2026. Leitura e MECANICA (regras objetivas da secao 4 do plano), sem a prosa qualitativa que o Claude gerava -- cole este log numa conversa do Claude se quiser a leitura interpretativa.

| Data/Hora (BRT) | Par | Close 1h | High/Low 1h | Close 4h | Swing 1h ref | ATR 1h | Funding | Zona ativa | Status checklist |
|---|---|---|---|---|---|---|---|---|---|
| 2026-09-10 19:13 | BTC-USDT-SWAP | 77120.9 | 77271.2/77077.1 | 77136.1 | sup 76607.1 (ha 9 candles) | 407.51 | 0.0100% | — | sem_zona |
| 2026-09-10 19:13 | ETH-USDT-SWAP | 2459.2 | 2462.0/2456.2 | 2461.5 | — | 17.93 | 0.0011% | — | sem_zona_posicao_aberta |
| 2026-09-10 19:13 | SOL-USDT-SWAP | 99.76 | 100.09/99.70 | 99.63 | sup 98.78 (ha 5 candles) | 0.90500 | 0.0006% | — | sem_zona |
| 2026-09-10 19:13 | XRP-USDT-SWAP | 1.3512 | 1.3562/1.3492 | 1.3502 | — | 0.01330 | 0.0091% | B/compra@1.3623 (0t/3c) | zona_mapeada_setup_B |
| 2026-09-10 19:13 | DOGE-USDT-SWAP | 0.08403 | 0.08424/0.08391 | 0.08388 | sup 0.08256 (ha 5 candles) | 0.00087 | -0.0021% | — | CONFIRMADO_setup_B |
| 2026-09-10 19:13 | ARB-USDT-SWAP | 0.14646 | 0.14851/0.14583 | 0.14744 | sup 0.14676 (ha 5 candles) | 0.00282 | -0.0026% | — | sem_zona |
| 2026-09-10 19:13 | WLD-USDT-SWAP | 0.40220 | 0.40370/0.40060 | 0.40110 | res 0.41860 (ha 17 candles) | 0.00623 | 0.0045% | — | sem_zona |
| 2026-09-10 19:13 | SUI-USDT-SWAP | 0.73810 | 0.74210/0.73710 | 0.73830 | — | 0.01021 | -0.0062% | B/compra@0.73760 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-10 19:13 | UNI-USDT-SWAP | 6.0060 | 6.0680/5.9960 | 6.0750 | sup 5.7820 (ha 9 candles) | 0.09443 | 0.0100% | B/venda@5.9670 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-10 19:14 | LINK-USDT-SWAP | 11.58 | 11.61/11.55 | 11.61 | sup 11.48 (ha 5 candles) | 0.11936 | -0.0028% | — | zona_expirada_setup_A |
| 2026-09-10 20:05 | BTC-USDT-SWAP | 76794.2 | 77183.9/76774.0 | 77136.1 | sup 76607.1 (ha 10 candles) | 426.15 | 0.0100% | — | sem_zona |
| 2026-09-10 20:05 | ETH-USDT-SWAP | 2444.2 | 2461.5/2442.1 | 2461.5 | — | 18.91 | 0.0024% | — | sem_zona_posicao_aberta |
| 2026-09-10 20:05 | SOL-USDT-SWAP | 99.21 | 100.05/99.17 | 99.63 | sup 98.78 (ha 6 candles) | 0.93929 | 0.0003% | — | sem_zona |
| 2026-09-10 20:05 | XRP-USDT-SWAP | 1.3423 | 1.3544/1.3420 | 1.3502 | — | 0.01383 | 0.0075% | B/compra@1.3623 (0t/4c) | zona_mapeada_setup_B |
| 2026-09-10 20:05 | DOGE-USDT-SWAP | 0.08349 | 0.08423/0.08345 | 0.08388 | sup 0.08256 (ha 6 candles) | 0.00090 | -0.0023% | — | sem_zona |
| 2026-09-10 20:05 | ARB-USDT-SWAP | 0.14233 | 0.14712/0.14169 | 0.14744 | sup 0.14676 (ha 6 candles) | 0.00308 | -0.0013% | — | sem_zona |
| 2026-09-10 20:05 | WLD-USDT-SWAP | 0.39880 | 0.40460/0.39820 | 0.40110 | res 0.41860 (ha 18 candles) | 0.00641 | 0.0030% | — | sem_zona |
| 2026-09-10 20:05 | SUI-USDT-SWAP | 0.73100 | 0.74040/0.73010 | 0.73830 | — | 0.01067 | -0.0089% | — | invalidado_setup_B |
| 2026-09-10 20:05 | UNI-USDT-SWAP | 5.9840 | 6.0360/5.9820 | 6.0750 | sup 5.7820 (ha 10 candles) | 0.09407 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-09-10 20:05 | LINK-USDT-SWAP | 11.51 | 11.64/11.51 | 11.61 | sup 11.48 (ha 6 candles) | 0.12557 | -0.0041% | B/venda@11.52 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-10 21:05 | BTC-USDT-SWAP | 76540.0 | 76848.3/76410.1 | 76540.0 | sup 76607.1 (ha 11 candles) | 435.31 | 0.0087% | A/venda@76607.1 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-10 21:05 | ETH-USDT-SWAP | 2437.2 | 2446.5/2433.4 | 2437.2 | — | 18.91 | 0.0033% | — | sem_zona_posicao_aberta |
| 2026-09-10 21:05 | SOL-USDT-SWAP | 98.61 | 99.34/98.54 | 98.61 | sup 98.78 (ha 7 candles) | 0.95071 | -0.0007% | A/venda@98.78 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-10 21:05 | XRP-USDT-SWAP | 1.3335 | 1.3437/1.3275 | 1.3335 | — | 0.01416 | 0.0046% | B/compra@1.3623 (0t/5c) | zona_mapeada_setup_B |
| 2026-09-10 21:05 | DOGE-USDT-SWAP | 0.08285 | 0.08357/0.08277 | 0.08285 | sup 0.08256 (ha 7 candles) | 0.00092 | -0.0004% | — | sem_zona |
| 2026-09-10 21:05 | ARB-USDT-SWAP | 0.13978 | 0.14341/0.13939 | 0.13978 | sup 0.14676 (ha 7 candles) | 0.00324 | 0.0041% | — | sem_zona |
| 2026-09-10 21:05 | WLD-USDT-SWAP | 0.39530 | 0.39940/0.39400 | 0.39530 | res 0.41860 (ha 19 candles) | 0.00636 | 0.0052% | — | sem_zona |
| 2026-09-10 21:05 | SUI-USDT-SWAP | 0.72710 | 0.73210/0.72300 | 0.72710 | — | 0.01072 | -0.0110% | B/compra@0.73270 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-10 21:05 | UNI-USDT-SWAP | 5.9470 | 5.9990/5.9330 | 5.9470 | sup 5.7820 (ha 11 candles) | 0.09371 | 0.0100% | — | sem_zona |
| 2026-09-10 21:05 | LINK-USDT-SWAP | 11.45 | 11.53/11.43 | 11.45 | sup 11.48 (ha 7 candles) | 0.12829 | -0.0011% | — | descartado_rr_baixo_setup_B |
| 2026-09-10 22:05 | BTC-USDT-SWAP | 76886.8 | 76921.0/76529.6 | 76540.0 | sup 76607.1 (ha 12 candles) | 446.35 | 0.0091% | — | invalidado_setup_A |
| 2026-09-10 22:05 | ETH-USDT-SWAP | 2455.1 | 2457.2/2436.4 | 2437.2 | — | 19.73 | 0.0024% | — | sem_zona_posicao_aberta |
| 2026-09-10 22:05 | SOL-USDT-SWAP | 99.12 | 99.36/98.52 | 98.61 | sup 98.78 (ha 8 candles) | 0.97143 | 0.0011% | — | invalidado_setup_A |
| 2026-09-10 22:05 | XRP-USDT-SWAP | 1.3408 | 1.3434/1.3329 | 1.3335 | — | 0.01407 | 0.0036% | B/compra@1.3623 (0t/6c) | zona_mapeada_setup_B |
| 2026-09-10 22:05 | DOGE-USDT-SWAP | 0.08342 | 0.08352/0.08283 | 0.08285 | sup 0.08256 (ha 8 candles) | 0.00093 | 0.0032% | — | sem_zona |
| 2026-09-10 22:05 | ARB-USDT-SWAP | 0.14322 | 0.14361/0.13978 | 0.13978 | sup 0.14676 (ha 8 candles) | 0.00332 | 0.0053% | — | sem_zona |
| 2026-09-10 22:05 | WLD-USDT-SWAP | 0.40020 | 0.40090/0.39540 | 0.39530 | res 0.41860 (ha 20 candles) | 0.00650 | 0.0089% | — | sem_zona |
| 2026-09-10 22:05 | SUI-USDT-SWAP | 0.73260 | 0.73370/0.72660 | 0.72710 | — | 0.01040 | -0.0116% | — | CONFIRMADO_setup_B |
| 2026-09-10 22:05 | UNI-USDT-SWAP | 6.0410 | 6.0430/5.9470 | 5.9470 | sup 5.7820 (ha 12 candles) | 0.09679 | 0.0100% | — | sem_zona |
| 2026-09-10 22:05 | LINK-USDT-SWAP | 11.51 | 11.52/11.43 | 11.45 | sup 11.48 (ha 8 candles) | 0.12993 | 0.0000% | — | sem_zona |
| 2026-09-10 23:05 | BTC-USDT-SWAP | 76950.0 | 76981.0/76630.8 | 76540.0 | sup 76607.1 (ha 13 candles) | 443.76 | 0.0098% | — | sem_zona |
| 2026-09-10 23:05 | ETH-USDT-SWAP | 2453.3 | 2459.1/2445.4 | 2437.2 | — | 19.86 | 0.0024% | — | sem_zona_posicao_aberta |
| 2026-09-10 23:05 | SOL-USDT-SWAP | 99.38 | 99.44/98.66 | 98.61 | sup 98.78 (ha 9 candles) | 0.97571 | 0.0013% | — | sem_zona |
| 2026-09-10 23:05 | XRP-USDT-SWAP | 1.3457 | 1.3458/1.3359 | 1.3335 | — | 0.01404 | 0.0036% | B/compra@1.3623 (0t/7c) | zona_mapeada_setup_B |
| 2026-09-10 23:05 | DOGE-USDT-SWAP | 0.08352 | 0.08363/0.08293 | 0.08285 | sup 0.08256 (ha 9 candles) | 0.00093 | 0.0070% | — | sem_zona |
| 2026-09-10 23:05 | ARB-USDT-SWAP | 0.14365 | 0.14416/0.14187 | 0.13978 | sup 0.14676 (ha 9 candles) | 0.00336 | 0.0033% | — | sem_zona |
| 2026-09-10 23:05 | WLD-USDT-SWAP | 0.39930 | 0.40160/0.39630 | 0.39530 | res 0.41860 (ha 21 candles) | 0.00646 | 0.0062% | — | sem_zona |
| 2026-09-10 23:05 | SUI-USDT-SWAP | 0.73420 | 0.73600/0.72780 | 0.72710 | — | 0.01028 | -0.0091% | B/compra@0.73760 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-10 23:05 | UNI-USDT-SWAP | 5.9980 | 6.0760/5.9160 | 5.9470 | sup 5.7820 (ha 13 candles) | 0.10307 | 0.0100% | — | sem_zona |
| 2026-09-10 23:05 | LINK-USDT-SWAP | 11.48 | 11.53/11.39 | 11.45 | sup 11.48 (ha 9 candles) | 0.13043 | 0.0003% | A/venda@11.48 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-11 00:05 | BTC-USDT-SWAP | 76816.1 | 76998.0/76733.7 | 76540.0 | sup 76410.1 (ha 3 candles) | 366.21 | 0.0100% | — | sem_zona |
| 2026-09-11 00:05 | ETH-USDT-SWAP | 2445.8 | 2454.3/2443.6 | 2437.2 | — | 16.29 | 0.0035% | — | sem_zona_posicao_aberta |
| 2026-09-11 00:05 | SOL-USDT-SWAP | 99.26 | 99.48/99.00 | 98.61 | sup 98.78 (ha 10 candles) | 0.78286 | 0.0026% | — | sem_zona |
| 2026-09-11 00:05 | XRP-USDT-SWAP | 1.3417 | 1.3460/1.3374 | 1.3335 | — | 0.01163 | 0.0035% | — | zona_expirada_setup_B |
| 2026-09-11 00:05 | DOGE-USDT-SWAP | 0.08344 | 0.08358/0.08312 | 0.08285 | sup 0.08277 (ha 3 candles) | 0.00071 | 0.0089% | — | sem_zona |
| 2026-09-11 00:05 | ARB-USDT-SWAP | 0.14448 | 0.14450/0.14294 | 0.13978 | sup 0.13939 (ha 3 candles) | 0.00320 | -0.0012% | — | sem_zona |
| 2026-09-11 00:05 | WLD-USDT-SWAP | 0.39760 | 0.39980/0.39650 | 0.39530 | res 0.41860 (ha 22 candles) | 0.00556 | 0.0028% | — | sem_zona |
| 2026-09-11 00:05 | SUI-USDT-SWAP | 0.73410 | 0.73500/0.73090 | 0.72710 | — | 0.00877 | -0.0043% | B/compra@0.73760 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-11 00:05 | UNI-USDT-SWAP | 5.9880 | 6.0190/5.9500 | 5.9470 | sup 5.7820 (ha 14 candles) | 0.09029 | 0.0096% | — | sem_zona |
| 2026-09-11 00:05 | LINK-USDT-SWAP | 11.47 | 11.50/11.45 | 11.45 | sup 11.48 (ha 10 candles) | 0.10714 | -0.0001% | A/venda@11.48 (1t/0c) | zona_mapeada_setup_A |
| 2026-09-11 01:05 | BTC-USDT-SWAP | 76860.0 | 76868.9/76670.0 | 76860.0 | sup 76410.1 (ha 4 candles) | 344.28 | 0.0100% | — | sem_zona |
| 2026-09-11 01:05 | ETH-USDT-SWAP | 2446.2 | 2447.7/2439.0 | 2446.2 | sup 2433.4 (ha 4 candles) | 14.68 | 0.0045% | — | sem_zona_posicao_aberta |
| 2026-09-11 01:05 | SOL-USDT-SWAP | 99.25 | 99.44/98.88 | 99.25 | sup 98.52 (ha 3 candles) | 0.75000 | 0.0042% | — | sem_zona |
| 2026-09-11 01:05 | XRP-USDT-SWAP | 1.3422 | 1.3430/1.3368 | 1.3422 | — | 0.01078 | 0.0024% | B/compra@1.3344 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 01:05 | DOGE-USDT-SWAP | 0.08370 | 0.08372/0.08323 | 0.08370 | sup 0.08277 (ha 4 candles) | 0.00068 | 0.0080% | — | sem_zona |
| 2026-09-11 01:05 | ARB-USDT-SWAP | 0.14601 | 0.14675/0.14345 | 0.14601 | sup 0.13939 (ha 4 candles) | 0.00323 | -0.0020% | B/venda@0.14674 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 01:05 | WLD-USDT-SWAP | 0.39780 | 0.39800/0.39450 | 0.39780 | res 0.41860 (ha 23 candles) | 0.00540 | 0.0030% | — | sem_zona |
| 2026-09-11 01:05 | SUI-USDT-SWAP | 0.73610 | 0.73830/0.73100 | 0.73610 | — | 0.00866 | -0.0008% | — | CONFIRMADO_setup_B |
| 2026-09-11 01:05 | UNI-USDT-SWAP | 6.0100 | 6.0150/5.9470 | 6.0100 | sup 5.7820 (ha 15 candles) | 0.08886 | 0.0072% | — | sem_zona |
| 2026-09-11 01:05 | LINK-USDT-SWAP | 11.49 | 11.50/11.45 | 11.49 | sup 11.48 (ha 11 candles) | 0.10093 | 0.0015% | A/venda@11.48 (2t/0c) | zona_mapeada_setup_A |
| 2026-09-11 02:05 | BTC-USDT-SWAP | 77070.4 | 77167.8/76844.9 | 76860.0 | sup 76410.1 (ha 5 candles) | 333.42 | 0.0084% | — | sem_zona |
| 2026-09-11 02:05 | ETH-USDT-SWAP | 2458.0 | 2463.9/2445.0 | 2446.2 | sup 2433.4 (ha 5 candles) | 14.77 | 0.0039% | — | sem_zona_posicao_aberta |
| 2026-09-11 02:05 | SOL-USDT-SWAP | 99.64 | 99.91/99.18 | 99.25 | sup 98.52 (ha 4 candles) | 0.72143 | 0.0060% | — | sem_zona |
| 2026-09-11 02:05 | XRP-USDT-SWAP | 1.3474 | 1.3494/1.3409 | 1.3422 | — | 0.01059 | 0.0008% | B/compra@1.3344 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-11 02:05 | DOGE-USDT-SWAP | 0.08403 | 0.08419/0.08362 | 0.08370 | sup 0.08277 (ha 5 candles) | 0.00065 | 0.0070% | — | sem_zona |
| 2026-09-11 02:05 | ARB-USDT-SWAP | 0.14766 | 0.14967/0.14564 | 0.14601 | sup 0.13939 (ha 5 candles) | 0.00320 | 0.0002% | — | invalidado_setup_B |
| 2026-09-11 02:05 | WLD-USDT-SWAP | 0.40110 | 0.40290/0.39780 | 0.39780 | res 0.41860 (ha 24 candles) | 0.00527 | 0.0039% | — | sem_zona |
| 2026-09-11 02:05 | SUI-USDT-SWAP | 0.73970 | 0.74220/0.73560 | 0.73610 | — | 0.00784 | -0.0016% | B/venda@0.73780 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 02:05 | UNI-USDT-SWAP | 6.1570 | 6.1860/5.9940 | 6.0100 | sup 5.9160 (ha 3 candles) | 0.09550 | 0.0061% | — | sem_zona |
| 2026-09-11 02:05 | LINK-USDT-SWAP | 11.53 | 11.56/11.48 | 11.49 | sup 11.39 (ha 3 candles) | 0.09579 | 0.0055% | — | invalidado_setup_A |
| 2026-09-11 03:05 | BTC-USDT-SWAP | 77224.5 | 77224.5/77027.0 | 76860.0 | sup 76410.1 (ha 6 candles) | 323.88 | 0.0075% | — | sem_zona |
| 2026-09-11 03:05 | ETH-USDT-SWAP | 2467.7 | 2468.2/2456.7 | 2446.2 | sup 2433.4 (ha 6 candles) | 14.66 | 0.0035% | — | sem_zona_posicao_aberta |
| 2026-09-11 03:05 | SOL-USDT-SWAP | 99.85 | 99.85/99.50 | 99.25 | sup 98.52 (ha 5 candles) | 0.69143 | 0.0071% | — | sem_zona |
| 2026-09-11 03:05 | XRP-USDT-SWAP | 1.3486 | 1.3494/1.3457 | 1.3422 | — | 0.01019 | -0.0004% | B/compra@1.3344 (0t/2c) | zona_mapeada_setup_B |
| 2026-09-11 03:05 | DOGE-USDT-SWAP | 0.08404 | 0.08408/0.08384 | 0.08370 | sup 0.08277 (ha 6 candles) | 0.00063 | 0.0033% | B/venda@0.08394 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 03:05 | ARB-USDT-SWAP | 0.14701 | 0.14774/0.14546 | 0.14601 | sup 0.13939 (ha 6 candles) | 0.00305 | 0.0021% | — | sem_zona |
| 2026-09-11 03:05 | WLD-USDT-SWAP | 0.40180 | 0.40370/0.40050 | 0.39780 | res 0.41860 (ha 25 candles) | 0.00517 | 0.0024% | — | sem_zona |
| 2026-09-11 03:05 | SUI-USDT-SWAP | 0.73980 | 0.74050/0.73750 | 0.73610 | — | 0.00746 | -0.0015% | — | invalidado_setup_B |
| 2026-09-11 03:05 | UNI-USDT-SWAP | 6.1600 | 6.1990/6.1080 | 6.0100 | sup 5.9160 (ha 4 candles) | 0.09393 | 0.0031% | — | sem_zona |
| 2026-09-11 03:05 | LINK-USDT-SWAP | 11.58 | 11.58/11.51 | 11.49 | sup 11.39 (ha 4 candles) | 0.09329 | 0.0100% | B/venda@11.52 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 04:05 | BTC-USDT-SWAP | 77268.0 | 77411.8/77140.8 | 76860.0 | sup 76410.1 (ha 7 candles) | 306.74 | 0.0066% | — | sem_zona |
| 2026-09-11 04:05 | ETH-USDT-SWAP | 2465.8 | 2470.0/2462.2 | 2446.2 | sup 2433.4 (ha 7 candles) | 13.88 | 0.0024% | — | sem_zona_posicao_aberta |
| 2026-09-11 04:05 | SOL-USDT-SWAP | 99.77 | 99.96/99.49 | 99.25 | sup 98.52 (ha 6 candles) | 0.64786 | 0.0071% | — | sem_zona |
| 2026-09-11 04:05 | XRP-USDT-SWAP | 1.3524 | 1.3527/1.3482 | 1.3422 | — | 0.00934 | -0.0009% | B/compra@1.3344 (0t/3c) | zona_mapeada_setup_B |
| 2026-09-11 04:05 | DOGE-USDT-SWAP | 0.08395 | 0.08415/0.08380 | 0.08370 | sup 0.08277 (ha 7 candles) | 0.00057 | 0.0028% | B/venda@0.08394 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-11 04:05 | ARB-USDT-SWAP | 0.14473 | 0.14701/0.14408 | 0.14601 | sup 0.13939 (ha 7 candles) | 0.00300 | 0.0033% | — | sem_zona |
| 2026-09-11 04:05 | WLD-USDT-SWAP | 0.40110 | 0.40510/0.39870 | 0.39780 | res 0.41860 (ha 26 candles) | 0.00491 | 0.0046% | — | sem_zona |
| 2026-09-11 04:05 | SUI-USDT-SWAP | 0.73680 | 0.74060/0.73590 | 0.73610 | — | 0.00680 | -0.0009% | B/compra@0.73270 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 04:05 | UNI-USDT-SWAP | 6.1520 | 6.2200/6.1390 | 6.0100 | sup 5.9160 (ha 5 candles) | 0.09157 | 0.0023% | — | sem_zona |
| 2026-09-11 04:05 | LINK-USDT-SWAP | 11.52 | 11.59/11.50 | 11.49 | sup 11.39 (ha 5 candles) | 0.08829 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-09-11 05:06 | BTC-USDT-SWAP | 77184.1 | 77379.7/77151.4 | 77184.1 | sup 76410.1 (ha 8 candles) | 293.05 | 0.0037% | — | sem_zona |
| 2026-09-11 05:06 | ETH-USDT-SWAP | 2466.3 | 2472.8/2464.7 | 2466.3 | sup 2433.4 (ha 8 candles) | 12.41 | 0.0022% | — | sem_zona_posicao_aberta |
| 2026-09-11 05:06 | SOL-USDT-SWAP | 99.69 | 100.10/99.64 | 99.69 | sup 98.52 (ha 7 candles) | 0.61429 | 0.0058% | — | sem_zona |
| 2026-09-11 05:06 | XRP-USDT-SWAP | 1.3508 | 1.3593/1.3504 | 1.3508 | — | 0.00906 | 0.0000% | B/compra@1.3344 (0t/4c) | zona_mapeada_setup_B |
| 2026-09-11 05:06 | DOGE-USDT-SWAP | 0.08377 | 0.08415/0.08371 | 0.08377 | sup 0.08277 (ha 8 candles) | 0.00054 | 0.0027% | — | CONFIRMADO_setup_B |
| 2026-09-11 05:06 | ARB-USDT-SWAP | 0.14381 | 0.14575/0.14324 | 0.14381 | sup 0.13939 (ha 8 candles) | 0.00297 | 0.0050% | — | sem_zona |
| 2026-09-11 05:06 | WLD-USDT-SWAP | 0.40040 | 0.40430/0.40000 | 0.40040 | res 0.41860 (ha 27 candles) | 0.00478 | 0.0044% | — | sem_zona |
| 2026-09-11 05:06 | SUI-USDT-SWAP | 0.73680 | 0.74220/0.73640 | 0.73680 | — | 0.00660 | -0.0009% | B/compra@0.73270 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-11 05:06 | UNI-USDT-SWAP | 6.0870 | 6.1580/6.0660 | 6.0870 | sup 5.9160 (ha 6 candles) | 0.08907 | 0.0018% | — | sem_zona |
| 2026-09-11 05:06 | LINK-USDT-SWAP | 11.47 | 11.56/11.47 | 11.47 | sup 11.39 (ha 6 candles) | 0.08564 | 0.0100% | B/venda@11.49 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 06:06 | BTC-USDT-SWAP | 77322.6 | 77458.0/77107.5 | 77184.1 | sup 76410.1 (ha 9 candles) | 292.09 | 0.0020% | — | sem_zona |
| 2026-09-11 06:06 | ETH-USDT-SWAP | 2475.5 | 2483.8/2462.4 | 2466.3 | sup 2433.4 (ha 9 candles) | 12.89 | 0.0024% | — | sem_zona |
| 2026-09-11 06:06 | SOL-USDT-SWAP | 99.87 | 100.25/99.43 | 99.69 | sup 98.52 (ha 8 candles) | 0.61571 | 0.0057% | — | sem_zona |
| 2026-09-11 06:06 | XRP-USDT-SWAP | 1.3528 | 1.3564/1.3477 | 1.3508 | — | 0.00872 | 0.0019% | B/compra@1.3344 (0t/5c) | zona_mapeada_setup_B |
| 2026-09-11 06:06 | DOGE-USDT-SWAP | 0.08399 | 0.08419/0.08366 | 0.08377 | sup 0.08277 (ha 9 candles) | 0.00053 | 0.0033% | — | sem_zona |
| 2026-09-11 06:06 | ARB-USDT-SWAP | 0.14326 | 0.14512/0.14313 | 0.14381 | sup 0.13939 (ha 9 candles) | 0.00297 | 0.0062% | — | sem_zona |
| 2026-09-11 06:06 | WLD-USDT-SWAP | 0.40130 | 0.40320/0.39900 | 0.40040 | res 0.41860 (ha 28 candles) | 0.00465 | 0.0029% | — | sem_zona |
| 2026-09-11 06:06 | SUI-USDT-SWAP | 0.73640 | 0.74060/0.73480 | 0.73680 | — | 0.00646 | 0.0010% | B/compra@0.73270 (0t/2c) | zona_mapeada_setup_B |
| 2026-09-11 06:06 | UNI-USDT-SWAP | 6.0770 | 6.1160/6.0500 | 6.0870 | sup 5.9160 (ha 7 candles) | 0.08650 | 0.0040% | — | sem_zona |
| 2026-09-11 06:06 | LINK-USDT-SWAP | 11.49 | 11.54/11.44 | 11.47 | sup 11.39 (ha 7 candles) | 0.08593 | 0.0100% | B/venda@11.49 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-11 07:06 | BTC-USDT-SWAP | 77001.8 | 77330.6/76826.9 | 77184.1 | sup 76410.1 (ha 10 candles) | 311.74 | 0.0012% | — | sem_zona |
| 2026-09-11 07:06 | ETH-USDT-SWAP | 2468.2 | 2476.6/2460.8 | 2466.3 | sup 2433.4 (ha 10 candles) | 13.14 | 0.0027% | — | sem_zona |
| 2026-09-11 07:06 | SOL-USDT-SWAP | 99.35 | 99.90/98.95 | 99.69 | sup 98.52 (ha 9 candles) | 0.64500 | 0.0050% | — | sem_zona |
| 2026-09-11 07:06 | XRP-USDT-SWAP | 1.3408 | 1.3540/1.3364 | 1.3508 | — | 0.00930 | 0.0051% | B/compra@1.3344 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-11 07:06 | DOGE-USDT-SWAP | 0.08365 | 0.08404/0.08329 | 0.08377 | sup 0.08277 (ha 10 candles) | 0.00054 | 0.0029% | — | sem_zona |
| 2026-09-11 07:06 | ARB-USDT-SWAP | 0.14193 | 0.14381/0.14123 | 0.14381 | sup 0.13939 (ha 10 candles) | 0.00297 | 0.0064% | — | sem_zona |
| 2026-09-11 07:06 | WLD-USDT-SWAP | 0.39740 | 0.40160/0.39540 | 0.40040 | res 0.40510 (ha 3 candles) | 0.00471 | 0.0039% | — | sem_zona |
| 2026-09-11 07:06 | SUI-USDT-SWAP | 0.73050 | 0.73650/0.72630 | 0.73680 | — | 0.00673 | 0.0028% | — | invalidado_setup_B |
| 2026-09-11 07:06 | UNI-USDT-SWAP | 6.0310 | 6.0890/6.0090 | 6.0870 | sup 5.9160 (ha 8 candles) | 0.08779 | 0.0066% | B/venda@5.9670 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 07:06 | LINK-USDT-SWAP | 11.43 | 11.50/11.39 | 11.47 | sup 11.39 (ha 8 candles) | 0.08871 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-09-11 08:06 | BTC-USDT-SWAP | 76960.7 | 77135.8/76927.7 | 77184.1 | sup 76410.1 (ha 11 candles) | 309.21 | 0.0017% | — | sem_zona |
| 2026-09-11 08:06 | ETH-USDT-SWAP | 2461.4 | 2474.9/2461.4 | 2466.3 | sup 2433.4 (ha 11 candles) | 13.53 | 0.0048% | — | sem_zona |
| 2026-09-11 08:06 | SOL-USDT-SWAP | 99.11 | 99.69/99.10 | 99.69 | sup 98.52 (ha 10 candles) | 0.65000 | 0.0035% | — | sem_zona |
| 2026-09-11 08:06 | XRP-USDT-SWAP | 1.3322 | 1.3442/1.3315 | 1.3508 | — | 0.00967 | 0.0072% | B/compra@1.3344 (2t/0c) | zona_mapeada_setup_B |
| 2026-09-11 08:06 | DOGE-USDT-SWAP | 0.08334 | 0.08388/0.08333 | 0.08377 | sup 0.08277 (ha 11 candles) | 0.00055 | 0.0042% | — | sem_zona |
| 2026-09-11 08:06 | ARB-USDT-SWAP | 0.14021 | 0.14254/0.13962 | 0.14381 | sup 0.13939 (ha 11 candles) | 0.00302 | 0.0091% | — | sem_zona |
| 2026-09-11 08:06 | WLD-USDT-SWAP | 0.39620 | 0.40160/0.39570 | 0.40040 | res 0.40510 (ha 4 candles) | 0.00485 | 0.0039% | — | sem_zona |
| 2026-09-11 08:06 | SUI-USDT-SWAP | 0.72550 | 0.73340/0.72540 | 0.73680 | — | 0.00680 | 0.0029% | B/compra@0.72910 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 08:06 | UNI-USDT-SWAP | 5.9470 | 6.0620/5.9400 | 6.0870 | sup 5.9160 (ha 9 candles) | 0.09350 | 0.0059% | — | descartado_rr_baixo_setup_B |
| 2026-09-11 08:06 | LINK-USDT-SWAP | 11.36 | 11.46/11.35 | 11.47 | sup 11.39 (ha 9 candles) | 0.09214 | 0.0100% | A/venda@11.39 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-11 09:06 | BTC-USDT-SWAP | 77000.1 | 77013.3/76716.2 | 77000.1 | sup 76410.1 (ha 12 candles) | 316.57 | 0.0027% | — | sem_zona |
| 2026-09-11 09:06 | ETH-USDT-SWAP | 2457.3 | 2461.4/2451.7 | 2457.3 | sup 2433.4 (ha 12 candles) | 13.81 | 0.0064% | — | sem_zona |
| 2026-09-11 09:06 | SOL-USDT-SWAP | 99.42 | 99.56/98.53 | 99.42 | sup 98.52 (ha 11 candles) | 0.69571 | 0.0011% | — | sem_zona |
| 2026-09-11 09:06 | XRP-USDT-SWAP | 1.3285 | 1.3328/1.3198 | 1.3285 | — | 0.01010 | 0.0093% | — | invalidado_setup_B |
| 2026-09-11 09:06 | DOGE-USDT-SWAP | 0.08363 | 0.08365/0.08287 | 0.08363 | sup 0.08277 (ha 12 candles) | 0.00058 | 0.0041% | — | sem_zona |
| 2026-09-11 09:06 | ARB-USDT-SWAP | 0.14008 | 0.14037/0.13794 | 0.14008 | sup 0.13939 (ha 12 candles) | 0.00301 | 0.0040% | — | sem_zona |
| 2026-09-11 09:06 | WLD-USDT-SWAP | 0.39650 | 0.39680/0.39110 | 0.39650 | res 0.40510 (ha 5 candles) | 0.00504 | 0.0069% | — | sem_zona |
| 2026-09-11 09:06 | SUI-USDT-SWAP | 0.71830 | 0.72600/0.70860 | 0.71830 | — | 0.00769 | 0.0021% | B/compra@0.72910 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-11 09:06 | UNI-USDT-SWAP | 5.9620 | 5.9910/5.9020 | 5.9620 | sup 5.9160 (ha 10 candles) | 0.09471 | 0.0100% | — | sem_zona |
| 2026-09-11 09:06 | LINK-USDT-SWAP | 11.39 | 11.42/11.28 | 11.39 | sup 11.39 (ha 10 candles) | 0.09743 | 0.0078% | A/venda@11.39 (1t/0c) | zona_mapeada_setup_A |
| 2026-09-11 10:06 | BTC-USDT-SWAP | 77990.1 | 78153.6/75866.0 | 77000.1 | sup 76410.1 (ha 13 candles) | 450.69 | 0.0024% | B/venda@78299.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 10:06 | ETH-USDT-SWAP | 2510.0 | 2514.9/2432.2 | 2457.3 | sup 2433.4 (ha 13 candles) | 18.33 | 0.0079% | B/venda@2523.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 10:06 | SOL-USDT-SWAP | 101.61 | 101.78/97.77 | 99.42 | sup 98.52 (ha 12 candles) | 0.91929 | -0.0000% | — | sem_zona |
| 2026-09-11 10:06 | XRP-USDT-SWAP | 1.3658 | 1.3706/1.3151 | 1.3285 | — | 0.01318 | 0.0071% | B/compra@1.3739 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 10:06 | DOGE-USDT-SWAP | 0.08512 | 0.08547/0.08213 | 0.08363 | sup 0.08277 (ha 13 candles) | 0.00076 | 0.0042% | B/venda@0.08567 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 10:06 | ARB-USDT-SWAP | 0.14373 | 0.14496/0.13881 | 0.14008 | sup 0.13939 (ha 13 candles) | 0.00306 | 0.0013% | — | sem_zona |
| 2026-09-11 10:06 | WLD-USDT-SWAP | 0.41030 | 0.41180/0.38620 | 0.39650 | res 0.40510 (ha 6 candles) | 0.00641 | 0.0026% | A/compra@0.40510 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-11 10:06 | SUI-USDT-SWAP | 0.73940 | 0.74060/0.70590 | 0.71830 | — | 0.00943 | -0.0001% | — | descartado_rr_baixo_setup_B |
| 2026-09-11 10:06 | UNI-USDT-SWAP | 6.1840 | 6.1910/5.8370 | 5.9620 | sup 5.9160 (ha 11 candles) | 0.11614 | 0.0100% | — | sem_zona |
| 2026-09-11 10:06 | LINK-USDT-SWAP | 11.68 | 11.69/11.22 | 11.39 | sup 11.39 (ha 11 candles) | 0.12143 | 0.0061% | — | invalidado_setup_A |
| 2026-09-11 11:06 | BTC-USDT-SWAP | 79202.9 | 79316.6/77220.0 | 77000.1 | sup 76410.1 (ha 14 candles) | 569.15 | 0.0043% | — | invalidado_setup_B |
| 2026-09-11 11:06 | ETH-USDT-SWAP | 2628.8 | 2648.0/2489.1 | 2457.3 | sup 2433.4 (ha 14 candles) | 28.75 | 0.0094% | — | invalidado_setup_B |
| 2026-09-11 11:06 | SOL-USDT-SWAP | 104.82 | 104.84/100.54 | 99.42 | sup 98.52 (ha 13 candles) | 1.1693 | 0.0000% | B/venda@105.15 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 11:06 | XRP-USDT-SWAP | 1.4149 | 1.4169/1.3530 | 1.3285 | — | 0.01659 | 0.0057% | — | descartado_rr_baixo_setup_B |
| 2026-09-11 11:06 | DOGE-USDT-SWAP | 0.08737 | 0.08751/0.08424 | 0.08363 | sup 0.08277 (ha 14 candles) | 0.00094 | 0.0060% | — | invalidado_setup_B |
| 2026-09-11 11:06 | ARB-USDT-SWAP | 0.15126 | 0.15133/0.14081 | 0.14008 | sup 0.13939 (ha 14 candles) | 0.00352 | -0.0034% | — | sem_zona |
| 2026-09-11 11:06 | WLD-USDT-SWAP | 0.42390 | 0.42510/0.40390 | 0.39650 | res 0.40510 (ha 7 candles) | 0.00754 | -0.0032% | — | descartado_rr_baixo_setup_A |
| 2026-09-11 11:06 | SUI-USDT-SWAP | 0.75860 | 0.76190/0.72530 | 0.71830 | — | 0.01139 | 0.0005% | B/venda@0.76340 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 11:06 | UNI-USDT-SWAP | 6.4790 | 6.4870/6.1020 | 5.9620 | sup 5.9160 (ha 12 candles) | 0.13893 | 0.0048% | B/venda@6.5420 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 11:06 | LINK-USDT-SWAP | 12.06 | 12.09/11.58 | 11.39 | sup 11.39 (ha 12 candles) | 0.15021 | 0.0043% | B/venda@12.17 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 12:06 | BTC-USDT-SWAP | 78762.8 | 79888.0/78470.6 | 77000.1 | sup 76410.1 (ha 15 candles) | 642.44 | 0.0048% | B/venda@79238.9 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 12:06 | ETH-USDT-SWAP | 2606.7 | 2667.3/2591.1 | 2457.3 | sup 2433.4 (ha 15 candles) | 32.71 | 0.0100% | — | sem_zona |
| 2026-09-11 12:06 | SOL-USDT-SWAP | 103.22 | 105.77/102.78 | 99.42 | sup 98.52 (ha 14 candles) | 1.3229 | 0.0010% | — | descartado_rr_baixo_setup_B |
| 2026-09-11 12:06 | XRP-USDT-SWAP | 1.3943 | 1.4323/1.3852 | 1.3285 | — | 0.01920 | 0.0072% | B/venda@1.3972 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 12:06 | DOGE-USDT-SWAP | 0.08646 | 0.08827/0.08595 | 0.08363 | sup 0.08277 (ha 15 candles) | 0.00106 | 0.0097% | B/venda@0.08645 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 12:06 | ARB-USDT-SWAP | 0.14672 | 0.15176/0.14564 | 0.14008 | sup 0.13794 (ha 3 candles) | 0.00369 | -0.0113% | B/venda@0.14674 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 12:06 | WLD-USDT-SWAP | 0.42110 | 0.42870/0.41610 | 0.39650 | res 0.40510 (ha 8 candles) | 0.00804 | -0.0047% | — | sem_zona |
| 2026-09-11 12:06 | SUI-USDT-SWAP | 0.74880 | 0.76610/0.74290 | 0.71830 | — | 0.01254 | 0.0012% | — | descartado_rr_baixo_setup_B |
| 2026-09-11 12:06 | UNI-USDT-SWAP | 6.3170 | 6.5300/6.2720 | 5.9620 | sup 5.9160 (ha 13 candles) | 0.15050 | -0.0017% | — | descartado_rr_baixo_setup_B |
| 2026-09-11 12:06 | LINK-USDT-SWAP | 11.92 | 12.20/11.84 | 11.39 | sup 11.39 (ha 13 candles) | 0.16993 | -0.0008% | — | descartado_rr_baixo_setup_B |
| 2026-09-11 13:06 | BTC-USDT-SWAP | 77687.8 | 78812.8/77252.1 | 77687.8 | sup 75866.0 (ha 3 candles) | 728.90 | 0.0055% | B/venda@79238.9 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-11 13:06 | ETH-USDT-SWAP | 2557.8 | 2616.4/2541.7 | 2557.8 | sup 2432.2 (ha 3 candles) | 37.06 | 0.0097% | B/venda@2536.9 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 13:06 | SOL-USDT-SWAP | 101.54 | 103.57/101.16 | 101.54 | sup 97.77 (ha 3 candles) | 1.4393 | 0.0014% | — | sem_zona |
| 2026-09-11 13:06 | XRP-USDT-SWAP | 1.3738 | 1.4051/1.3660 | 1.3738 | — | 0.02129 | 0.0082% | — | descartado_rr_baixo_setup_B |
| 2026-09-11 13:06 | DOGE-USDT-SWAP | 0.08494 | 0.08683/0.08434 | 0.08494 | sup 0.08213 (ha 3 candles) | 0.00118 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-09-11 13:06 | ARB-USDT-SWAP | 0.14393 | 0.15008/0.14315 | 0.14393 | sup 0.13794 (ha 4 candles) | 0.00402 | -0.0135% | — | descartado_rr_baixo_setup_B |
| 2026-09-11 13:06 | WLD-USDT-SWAP | 0.40880 | 0.42280/0.40530 | 0.40880 | res 0.40510 (ha 9 candles) | 0.00891 | -0.0062% | — | sem_zona |
| 2026-09-11 13:06 | SUI-USDT-SWAP | 0.73680 | 0.75710/0.73120 | 0.73680 | — | 0.01381 | 0.0009% | B/venda@0.73780 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 13:06 | UNI-USDT-SWAP | 6.1590 | 6.3960/6.1050 | 6.1590 | sup 5.8370 (ha 3 candles) | 0.15986 | -0.0065% | — | sem_zona |
| 2026-09-11 13:06 | LINK-USDT-SWAP | 11.70 | 12.01/11.63 | 11.70 | sup 11.22 (ha 3 candles) | 0.18650 | -0.0044% | B/venda@11.83 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 13:43 | BTC-USDT-SWAP | 77687.8 | 78812.8/77252.1 | 77687.8 | sup 75866.0 (ha 3 candles) | 728.90 | 0.0056% | B/venda@79238.9 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-11 13:43 | ETH-USDT-SWAP | 2557.8 | 2616.4/2541.7 | 2557.8 | sup 2432.2 (ha 3 candles) | 37.06 | 0.0083% | B/venda@2536.9 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 13:43 | SOL-USDT-SWAP | 101.54 | 103.57/101.16 | 101.54 | sup 97.77 (ha 3 candles) | 1.4393 | 0.0007% | — | sem_zona |
| 2026-09-11 13:43 | XRP-USDT-SWAP | 1.3738 | 1.4051/1.3660 | 1.3738 | — | 0.02129 | 0.0072% | — | descartado_rr_baixo_setup_B |
| 2026-09-11 13:43 | DOGE-USDT-SWAP | 0.08494 | 0.08683/0.08434 | 0.08494 | sup 0.08213 (ha 3 candles) | 0.00118 | 0.0100% | — | descartado_rr_baixo_setup_B |
| 2026-09-11 13:43 | ARB-USDT-SWAP | 0.14393 | 0.15008/0.14315 | 0.14393 | sup 0.13794 (ha 4 candles) | 0.00402 | -0.0122% | — | descartado_rr_baixo_setup_B |
| 2026-09-11 13:43 | WLD-USDT-SWAP | 0.40880 | 0.42280/0.40530 | 0.40880 | res 0.40510 (ha 9 candles) | 0.00891 | -0.0071% | — | sem_zona |
| 2026-09-11 13:43 | SUI-USDT-SWAP | 0.73680 | 0.75710/0.73120 | 0.73680 | — | 0.01381 | 0.0011% | B/venda@0.73780 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 13:43 | UNI-USDT-SWAP | 6.1590 | 6.3960/6.1050 | 6.1590 | sup 5.8370 (ha 3 candles) | 0.15986 | -0.0081% | — | sem_zona |
| 2026-09-11 13:43 | LINK-USDT-SWAP | 11.70 | 12.01/11.63 | 11.70 | sup 11.22 (ha 3 candles) | 0.18650 | -0.0046% | B/venda@11.83 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 14:06 | BTC-USDT-SWAP | 77878.8 | 78037.2/77350.0 | 77687.8 | sup 75866.0 (ha 4 candles) | 759.11 | 0.0058% | B/venda@79238.9 (0t/2c) | zona_mapeada_setup_B |
| 2026-09-11 14:06 | ETH-USDT-SWAP | 2576.2 | 2584.0/2542.3 | 2557.8 | sup 2432.2 (ha 4 candles) | 39.27 | 0.0073% | — | invalidado_setup_B |
| 2026-09-11 14:06 | SOL-USDT-SWAP | 102.27 | 102.36/101.23 | 101.54 | sup 97.77 (ha 4 candles) | 1.4857 | 0.0005% | — | sem_zona |
| 2026-09-11 14:06 | XRP-USDT-SWAP | 1.3757 | 1.3839/1.3676 | 1.3738 | — | 0.02184 | 0.0067% | B/compra@1.3804 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 14:06 | DOGE-USDT-SWAP | 0.08579 | 0.08584/0.08469 | 0.08494 | sup 0.08213 (ha 4 candles) | 0.00123 | 0.0100% | B/venda@0.08567 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 14:06 | ARB-USDT-SWAP | 0.14536 | 0.14640/0.14320 | 0.14393 | sup 0.13794 (ha 5 candles) | 0.00413 | -0.0122% | — | sem_zona |
| 2026-09-11 14:06 | WLD-USDT-SWAP | 0.41220 | 0.41290/0.40660 | 0.40880 | res 0.40510 (ha 10 candles) | 0.00912 | -0.0072% | — | sem_zona |
| 2026-09-11 14:06 | SUI-USDT-SWAP | 0.74140 | 0.74510/0.73410 | 0.73680 | — | 0.01430 | 0.0022% | — | invalidado_setup_B |
| 2026-09-11 14:06 | UNI-USDT-SWAP | 6.1780 | 6.2310/6.0960 | 6.1590 | sup 5.8370 (ha 4 candles) | 0.16457 | -0.0079% | — | sem_zona |
| 2026-09-11 14:06 | LINK-USDT-SWAP | 11.79 | 11.81/11.67 | 11.70 | sup 11.22 (ha 4 candles) | 0.19343 | -0.0050% | B/venda@11.83 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-11 14:28 | BTC-USDT-SWAP | 77878.8 | 78037.2/77350.0 | 77687.8 | sup 75866.0 (ha 4 candles) | 759.11 | 0.0061% | B/venda@79238.9 (0t/2c) | zona_mapeada_setup_B |
| 2026-09-11 14:28 | ETH-USDT-SWAP | 2576.2 | 2584.0/2542.3 | 2557.8 | sup 2432.2 (ha 4 candles) | 39.27 | 0.0064% | — | invalidado_setup_B |
| 2026-09-11 14:29 | SOL-USDT-SWAP | 102.27 | 102.36/101.23 | 101.54 | sup 97.77 (ha 4 candles) | 1.4857 | 0.0009% | — | sem_zona |
| 2026-09-11 14:29 | XRP-USDT-SWAP | 1.3757 | 1.3839/1.3676 | 1.3738 | — | 0.02184 | 0.0063% | B/compra@1.3804 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 14:29 | DOGE-USDT-SWAP | 0.08579 | 0.08584/0.08469 | 0.08494 | sup 0.08213 (ha 4 candles) | 0.00123 | 0.0090% | B/venda@0.08567 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 14:29 | ARB-USDT-SWAP | 0.14536 | 0.14640/0.14320 | 0.14393 | sup 0.13794 (ha 5 candles) | 0.00413 | -0.0114% | — | sem_zona |
| 2026-09-11 14:29 | WLD-USDT-SWAP | 0.41220 | 0.41290/0.40660 | 0.40880 | res 0.40510 (ha 10 candles) | 0.00912 | -0.0073% | — | sem_zona |
| 2026-09-11 14:29 | SUI-USDT-SWAP | 0.74140 | 0.74510/0.73410 | 0.73680 | — | 0.01430 | 0.0026% | — | invalidado_setup_B |
| 2026-09-11 14:29 | UNI-USDT-SWAP | 6.1780 | 6.2310/6.0960 | 6.1590 | sup 5.8370 (ha 4 candles) | 0.16457 | -0.0076% | — | sem_zona |
| 2026-09-11 14:29 | LINK-USDT-SWAP | 11.79 | 11.81/11.67 | 11.70 | sup 11.22 (ha 4 candles) | 0.19343 | -0.0059% | B/venda@11.83 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-11 15:06 | BTC-USDT-SWAP | 77500.4 | 77928.5/77455.6 | 77687.8 | sup 75866.0 (ha 5 candles) | 778.68 | 0.0068% | B/venda@79238.9 (0t/3c) | zona_mapeada_setup_B |
| 2026-09-11 15:06 | ETH-USDT-SWAP | 2565.3 | 2580.9/2561.6 | 2557.8 | sup 2432.2 (ha 5 candles) | 40.03 | 0.0053% | B/venda@2548.4 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 15:06 | SOL-USDT-SWAP | 101.88 | 102.43/101.75 | 101.54 | sup 97.77 (ha 5 candles) | 1.4943 | 0.0001% | — | sem_zona |
| 2026-09-11 15:06 | XRP-USDT-SWAP | 1.3669 | 1.3774/1.3645 | 1.3738 | — | 0.02231 | 0.0045% | — | invalidado_setup_B |
| 2026-09-11 15:06 | DOGE-USDT-SWAP | 0.08492 | 0.08590/0.08481 | 0.08494 | sup 0.08213 (ha 5 candles) | 0.00128 | 0.0076% | — | descartado_rr_baixo_setup_B |
| 2026-09-11 15:06 | ARB-USDT-SWAP | 0.14393 | 0.14574/0.14329 | 0.14393 | sup 0.13794 (ha 6 candles) | 0.00407 | -0.0103% | — | sem_zona |
| 2026-09-11 15:06 | WLD-USDT-SWAP | 0.40770 | 0.41340/0.40670 | 0.40880 | res 0.42870 (ha 3 candles) | 0.00935 | -0.0083% | — | sem_zona |
| 2026-09-11 15:06 | SUI-USDT-SWAP | 0.73220 | 0.74420/0.72960 | 0.73680 | — | 0.01482 | 0.0031% | B/compra@0.73760 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 15:06 | UNI-USDT-SWAP | 6.0900 | 6.1930/6.0580 | 6.1590 | sup 5.8370 (ha 5 candles) | 0.16936 | -0.0082% | B/venda@5.9670 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 15:06 | LINK-USDT-SWAP | 11.69 | 11.80/11.67 | 11.70 | sup 11.22 (ha 5 candles) | 0.19921 | -0.0062% | — | descartado_rr_baixo_setup_B |
| 2026-09-11 16:06 | BTC-USDT-SWAP | 77021.1 | 77515.6/76821.3 | 77687.8 | sup 75866.0 (ha 6 candles) | 805.21 | 0.0065% | B/venda@79238.9 (0t/4c) | zona_mapeada_setup_B |
| 2026-09-11 16:06 | ETH-USDT-SWAP | 2536.2 | 2567.2/2528.0 | 2557.8 | sup 2432.2 (ha 6 candles) | 41.48 | 0.0034% | — | descartado_rr_baixo_setup_B |
| 2026-09-11 16:06 | SOL-USDT-SWAP | 101.02 | 101.98/100.26 | 101.54 | sup 97.77 (ha 6 candles) | 1.5650 | -0.0011% | — | sem_zona |
| 2026-09-11 16:06 | XRP-USDT-SWAP | 1.3517 | 1.3683/1.3464 | 1.3738 | — | 0.02327 | 0.0022% | B/compra@1.3344 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 16:06 | DOGE-USDT-SWAP | 0.08404 | 0.08499/0.08345 | 0.08494 | sup 0.08213 (ha 6 candles) | 0.00135 | 0.0043% | B/venda@0.08394 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 16:06 | ARB-USDT-SWAP | 0.14021 | 0.14435/0.13929 | 0.14393 | sup 0.13794 (ha 7 candles) | 0.00415 | -0.0089% | — | sem_zona |
| 2026-09-11 16:06 | WLD-USDT-SWAP | 0.39770 | 0.40850/0.39400 | 0.40880 | res 0.42870 (ha 4 candles) | 0.01002 | -0.0071% | — | sem_zona |
| 2026-09-11 16:06 | SUI-USDT-SWAP | 0.72190 | 0.73310/0.72010 | 0.73680 | — | 0.01528 | 0.0013% | B/compra@0.73760 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-11 16:06 | UNI-USDT-SWAP | 6.0250 | 6.1110/5.9850 | 6.1590 | sup 5.8370 (ha 6 candles) | 0.16464 | -0.0050% | — | invalidado_setup_B |
| 2026-09-11 16:06 | LINK-USDT-SWAP | 11.53 | 11.71/11.50 | 11.70 | sup 11.22 (ha 6 candles) | 0.20807 | -0.0080% | B/venda@11.52 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 17:05 | BTC-USDT-SWAP | 77247.3 | 77334.0/76967.1 | 77247.3 | sup 75866.0 (ha 7 candles) | 817.31 | 0.0048% | B/venda@79238.9 (0t/5c) | zona_mapeada_setup_B |
| 2026-09-11 17:05 | ETH-USDT-SWAP | 2538.1 | 2547.4/2531.7 | 2538.1 | sup 2432.2 (ha 7 candles) | 41.77 | 0.0016% | B/venda@2523.0 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 17:05 | SOL-USDT-SWAP | 101.95 | 102.11/100.74 | 101.95 | sup 97.77 (ha 7 candles) | 1.6379 | -0.0011% | — | sem_zona |
| 2026-09-11 17:06 | XRP-USDT-SWAP | 1.3607 | 1.3621/1.3453 | 1.3607 | — | 0.02421 | 0.0006% | B/compra@1.3344 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-11 17:06 | DOGE-USDT-SWAP | 0.08444 | 0.08454/0.08369 | 0.08444 | sup 0.08213 (ha 7 candles) | 0.00139 | 0.0028% | — | invalidado_setup_B |
| 2026-09-11 17:06 | ARB-USDT-SWAP | 0.14153 | 0.14194/0.13969 | 0.14153 | sup 0.13794 (ha 8 candles) | 0.00415 | -0.0088% | — | sem_zona |
| 2026-09-11 17:06 | WLD-USDT-SWAP | 0.40170 | 0.40290/0.39570 | 0.40170 | res 0.42870 (ha 5 candles) | 0.01031 | -0.0058% | — | sem_zona |
| 2026-09-11 17:06 | SUI-USDT-SWAP | 0.72640 | 0.72790/0.71890 | 0.72640 | — | 0.01571 | 0.0004% | B/compra@0.73760 (0t/2c) | zona_mapeada_setup_B |
| 2026-09-11 17:06 | UNI-USDT-SWAP | 6.0740 | 6.0910/5.9970 | 6.0740 | sup 5.8370 (ha 7 candles) | 0.16486 | -0.0012% | — | sem_zona |
| 2026-09-11 17:06 | LINK-USDT-SWAP | 11.61 | 11.63/11.51 | 11.61 | sup 11.22 (ha 7 candles) | 0.21214 | -0.0068% | — | invalidado_setup_B |
| 2026-09-11 18:06 | BTC-USDT-SWAP | 77300.0 | 77470.7/77152.7 | 77247.3 | sup 75866.0 (ha 8 candles) | 820.66 | 0.0045% | B/venda@79238.9 (0t/6c) | zona_mapeada_setup_B |
| 2026-09-11 18:06 | ETH-USDT-SWAP | 2529.4 | 2547.1/2521.3 | 2538.1 | sup 2432.2 (ha 8 candles) | 43.06 | 0.0002% | — | descartado_rr_baixo_setup_B |
| 2026-09-11 18:06 | SOL-USDT-SWAP | 102.42 | 102.94/101.93 | 101.95 | sup 97.77 (ha 8 candles) | 1.6764 | 0.0011% | — | sem_zona |
| 2026-09-11 18:06 | XRP-USDT-SWAP | 1.3614 | 1.3675/1.3565 | 1.3607 | — | 0.02467 | -0.0007% | B/compra@1.3344 (0t/2c) | zona_mapeada_setup_B |
| 2026-09-11 18:06 | DOGE-USDT-SWAP | 0.08434 | 0.08472/0.08401 | 0.08444 | sup 0.08213 (ha 8 candles) | 0.00142 | 0.0034% | — | sem_zona |
| 2026-09-11 18:06 | ARB-USDT-SWAP | 0.13962 | 0.14254/0.13881 | 0.14153 | sup 0.13794 (ha 9 candles) | 0.00420 | -0.0089% | — | sem_zona |
| 2026-09-11 18:06 | WLD-USDT-SWAP | 0.39980 | 0.40370/0.39700 | 0.40170 | res 0.42870 (ha 6 candles) | 0.01033 | -0.0056% | — | sem_zona |
| 2026-09-11 18:06 | SUI-USDT-SWAP | 0.72760 | 0.73080/0.72340 | 0.72640 | — | 0.01590 | -0.0011% | B/compra@0.73760 (0t/3c) | zona_mapeada_setup_B |
| 2026-09-11 18:06 | UNI-USDT-SWAP | 6.0570 | 6.1050/6.0250 | 6.0740 | sup 5.8370 (ha 8 candles) | 0.16479 | 0.0036% | — | sem_zona |
| 2026-09-11 18:06 | LINK-USDT-SWAP | 11.58 | 11.64/11.54 | 11.61 | sup 11.22 (ha 8 candles) | 0.21300 | -0.0026% | — | sem_zona |
| 2026-09-11 19:06 | BTC-USDT-SWAP | 77079.9 | 77394.0/77044.9 | 77247.3 | sup 76821.3 (ha 3 candles) | 829.29 | 0.0048% | B/venda@79238.9 (0t/7c) | zona_mapeada_setup_B |
| 2026-09-11 19:06 | ETH-USDT-SWAP | 2515.4 | 2539.6/2511.5 | 2538.1 | sup 2432.2 (ha 9 candles) | 44.48 | 0.0009% | B/venda@2536.9 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-11 19:06 | SOL-USDT-SWAP | 102.05 | 103.09/101.99 | 101.95 | sup 100.26 (ha 3 candles) | 1.7221 | 0.0035% | — | sem_zona |
| 2026-09-11 19:06 | XRP-USDT-SWAP | 1.3521 | 1.3659/1.3511 | 1.3607 | — | 0.02509 | -0.0014% | B/compra@1.3344 (0t/3c) | zona_mapeada_setup_B |
| 2026-09-11 19:06 | DOGE-USDT-SWAP | 0.08394 | 0.08468/0.08378 | 0.08444 | sup 0.08345 (ha 3 candles) | 0.00145 | 0.0043% | — | sem_zona |
| 2026-09-11 19:06 | ARB-USDT-SWAP | 0.13837 | 0.14127/0.13754 | 0.14153 | sup 0.13794 (ha 10 candles) | 0.00429 | -0.0045% | — | sem_zona |
| 2026-09-11 19:06 | WLD-USDT-SWAP | 0.39610 | 0.40270/0.39510 | 0.40170 | res 0.42870 (ha 7 candles) | 0.01056 | -0.0051% | — | sem_zona |
| 2026-09-11 19:06 | SUI-USDT-SWAP | 0.72120 | 0.73190/0.72000 | 0.72640 | — | 0.01634 | -0.0018% | B/compra@0.73760 (0t/4c) | zona_mapeada_setup_B |
| 2026-09-11 19:06 | UNI-USDT-SWAP | 5.9860 | 6.0920/5.9740 | 6.0740 | sup 5.8370 (ha 9 candles) | 0.16664 | 0.0055% | — | sem_zona |
| 2026-09-11 19:06 | LINK-USDT-SWAP | 11.51 | 11.64/11.50 | 11.61 | sup 11.50 (ha 3 candles) | 0.21564 | 0.0001% | — | sem_zona |
| 2026-09-11 20:05 | BTC-USDT-SWAP | 77105.2 | 77199.8/76929.5 | 77247.3 | sup 76821.3 (ha 4 candles) | 823.56 | 0.0040% | — | zona_expirada_setup_B |
| 2026-09-11 20:06 | ETH-USDT-SWAP | 2510.8 | 2522.6/2504.1 | 2538.1 | sup 2432.2 (ha 10 candles) | 44.27 | 0.0012% | B/venda@2536.9 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-11 20:06 | SOL-USDT-SWAP | 101.83 | 102.44/101.47 | 101.95 | sup 100.26 (ha 4 candles) | 1.7329 | 0.0049% | — | sem_zona |
| 2026-09-11 20:06 | XRP-USDT-SWAP | 1.3495 | 1.3572/1.3456 | 1.3607 | — | 0.02530 | -0.0015% | B/compra@1.3344 (0t/4c) | zona_mapeada_setup_B |
| 2026-09-11 20:06 | DOGE-USDT-SWAP | 0.08376 | 0.08427/0.08350 | 0.08444 | sup 0.08345 (ha 4 candles) | 0.00147 | 0.0037% | — | sem_zona |
| 2026-09-11 20:06 | ARB-USDT-SWAP | 0.13771 | 0.13963/0.13729 | 0.14153 | sup 0.13794 (ha 11 candles) | 0.00432 | -0.0006% | A/venda@0.13794 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-11 20:06 | WLD-USDT-SWAP | 0.39550 | 0.39980/0.39440 | 0.40170 | res 0.42870 (ha 8 candles) | 0.01065 | -0.0053% | — | sem_zona |
| 2026-09-11 20:06 | SUI-USDT-SWAP | 0.72000 | 0.72520/0.71700 | 0.72640 | — | 0.01651 | -0.0040% | B/compra@0.73760 (0t/5c) | zona_mapeada_setup_B |
| 2026-09-11 20:06 | UNI-USDT-SWAP | 5.9750 | 6.0260/5.9540 | 6.0740 | sup 5.8370 (ha 10 candles) | 0.16707 | 0.0085% | — | sem_zona |
| 2026-09-11 20:06 | LINK-USDT-SWAP | 11.48 | 11.55/11.46 | 11.61 | sup 11.50 (ha 4 candles) | 0.21464 | -0.0014% | — | sem_zona |
| 2026-09-11 21:05 | BTC-USDT-SWAP | 77184.7 | 77190.0/77082.2 | 77184.7 | sup 76821.3 (ha 5 candles) | 795.29 | 0.0031% | — | sem_zona |
| 2026-09-11 21:05 | ETH-USDT-SWAP | 2515.4 | 2515.5/2508.0 | 2515.4 | sup 2432.2 (ha 11 candles) | 43.68 | 0.0030% | B/venda@2536.9 (0t/2c) | zona_mapeada_setup_B |
| 2026-09-11 21:05 | SOL-USDT-SWAP | 102.42 | 102.43/101.73 | 102.42 | sup 100.26 (ha 5 candles) | 1.7150 | 0.0061% | — | sem_zona |
| 2026-09-11 21:05 | XRP-USDT-SWAP | 1.3558 | 1.3565/1.3483 | 1.3558 | — | 0.02463 | -0.0017% | B/compra@1.3344 (0t/5c) | zona_mapeada_setup_B |
| 2026-09-11 21:05 | DOGE-USDT-SWAP | 0.08427 | 0.08431/0.08371 | 0.08427 | sup 0.08345 (ha 5 candles) | 0.00145 | 0.0054% | — | sem_zona |
| 2026-09-11 21:05 | ARB-USDT-SWAP | 0.13937 | 0.13949/0.13763 | 0.13937 | sup 0.13794 (ha 12 candles) | 0.00426 | 0.0031% | — | invalidado_setup_A |
| 2026-09-11 21:05 | WLD-USDT-SWAP | 0.39970 | 0.40020/0.39530 | 0.39970 | res 0.42870 (ha 9 candles) | 0.01056 | -0.0004% | — | sem_zona |
| 2026-09-11 21:05 | SUI-USDT-SWAP | 0.72520 | 0.72520/0.71910 | 0.72520 | — | 0.01621 | -0.0038% | B/compra@0.73760 (0t/6c) | zona_mapeada_setup_B |
| 2026-09-11 21:05 | UNI-USDT-SWAP | 6.0080 | 6.0080/5.9310 | 6.0080 | sup 5.8370 (ha 11 candles) | 0.16686 | 0.0100% | — | sem_zona |
| 2026-09-11 21:05 | LINK-USDT-SWAP | 11.54 | 11.55/11.47 | 11.54 | sup 11.50 (ha 5 candles) | 0.21214 | -0.0036% | — | sem_zona |
| 2026-09-11 22:05 | BTC-USDT-SWAP | 77250.0 | 77285.5/77161.0 | 77184.7 | sup 76821.3 (ha 6 candles) | 789.31 | 0.0024% | — | sem_zona |
| 2026-09-11 22:05 | ETH-USDT-SWAP | 2509.8 | 2517.2/2509.8 | 2515.4 | sup 2432.2 (ha 12 candles) | 43.24 | 0.0053% | B/venda@2536.9 (0t/3c) | zona_mapeada_setup_B |
| 2026-09-11 22:05 | SOL-USDT-SWAP | 101.87 | 102.53/101.72 | 102.42 | sup 100.26 (ha 6 candles) | 1.7307 | 0.0068% | — | sem_zona |
| 2026-09-11 22:06 | XRP-USDT-SWAP | 1.3563 | 1.3585/1.3538 | 1.3558 | — | 0.02406 | -0.0004% | B/compra@1.3344 (0t/6c) | zona_mapeada_setup_B |
| 2026-09-11 22:06 | DOGE-USDT-SWAP | 0.08416 | 0.08438/0.08408 | 0.08427 | sup 0.08345 (ha 6 candles) | 0.00144 | 0.0063% | — | sem_zona |
| 2026-09-11 22:06 | ARB-USDT-SWAP | 0.14155 | 0.14170/0.13925 | 0.13937 | sup 0.13794 (ha 13 candles) | 0.00423 | 0.0063% | — | sem_zona |
| 2026-09-11 22:06 | WLD-USDT-SWAP | 0.40260 | 0.40380/0.39930 | 0.39970 | res 0.42870 (ha 10 candles) | 0.01046 | 0.0039% | — | sem_zona |
| 2026-09-11 22:06 | SUI-USDT-SWAP | 0.72660 | 0.72760/0.72450 | 0.72520 | — | 0.01586 | -0.0037% | B/compra@0.73760 (0t/7c) | zona_mapeada_setup_B |
| 2026-09-11 22:06 | UNI-USDT-SWAP | 6.0130 | 6.0380/5.9900 | 6.0080 | sup 5.8370 (ha 12 candles) | 0.16157 | 0.0100% | — | sem_zona |
| 2026-09-11 22:06 | LINK-USDT-SWAP | 11.50 | 11.55/11.50 | 11.54 | sup 11.50 (ha 6 candles) | 0.20814 | -0.0061% | — | sem_zona |
| 2026-09-11 23:05 | BTC-USDT-SWAP | 77234.3 | 77348.7/77220.0 | 77184.7 | sup 76929.5 (ha 3 candles) | 777.29 | 0.0027% | — | sem_zona |
| 2026-09-11 23:05 | ETH-USDT-SWAP | 2512.8 | 2516.3/2508.5 | 2515.4 | sup 2504.1 (ha 3 candles) | 43.10 | 0.0072% | B/venda@2536.9 (0t/4c) | zona_mapeada_setup_B |
| 2026-09-11 23:05 | SOL-USDT-SWAP | 101.94 | 102.20/101.78 | 102.42 | sup 100.26 (ha 7 candles) | 1.6871 | 0.0084% | — | sem_zona |
| 2026-09-11 23:05 | XRP-USDT-SWAP | 1.3603 | 1.3631/1.3553 | 1.3558 | — | 0.02369 | 0.0008% | B/compra@1.3344 (0t/7c) | zona_mapeada_setup_B |
| 2026-09-11 23:05 | DOGE-USDT-SWAP | 0.08437 | 0.08454/0.08410 | 0.08427 | sup 0.08350 (ha 3 candles) | 0.00141 | 0.0078% | — | sem_zona |
| 2026-09-11 23:05 | ARB-USDT-SWAP | 0.14195 | 0.14291/0.14112 | 0.13937 | sup 0.13729 (ha 3 candles) | 0.00418 | 0.0077% | — | sem_zona |
| 2026-09-11 23:05 | WLD-USDT-SWAP | 0.40430 | 0.40620/0.40210 | 0.39970 | res 0.42870 (ha 11 candles) | 0.01034 | 0.0069% | — | sem_zona |
| 2026-09-11 23:05 | SUI-USDT-SWAP | 0.72840 | 0.73050/0.72610 | 0.72520 | — | 0.01494 | 0.0003% | — | zona_expirada_setup_B |
| 2026-09-11 23:05 | UNI-USDT-SWAP | 6.0470 | 6.0590/5.9790 | 6.0080 | sup 5.8370 (ha 13 candles) | 0.16093 | 0.0100% | — | sem_zona |
| 2026-09-11 23:05 | LINK-USDT-SWAP | 11.53 | 11.56/11.49 | 11.54 | sup 11.46 (ha 3 candles) | 0.20407 | -0.0064% | — | sem_zona |
| 2026-09-12 00:05 | BTC-USDT-SWAP | 77246.6 | 77292.2/77176.3 | 77184.7 | sup 76929.5 (ha 4 candles) | 622.16 | 0.0034% | — | sem_zona |
| 2026-09-12 00:05 | ETH-USDT-SWAP | 2513.2 | 2515.0/2511.2 | 2515.4 | sup 2504.1 (ha 4 candles) | 37.46 | 0.0081% | B/venda@2536.9 (0t/5c) | zona_mapeada_setup_B |
| 2026-09-12 00:05 | SOL-USDT-SWAP | 101.82 | 102.04/101.59 | 102.42 | sup 100.26 (ha 8 candles) | 1.4329 | 0.0079% | — | sem_zona |
| 2026-09-12 00:05 | XRP-USDT-SWAP | 1.3630 | 1.3635/1.3589 | 1.3558 | — | 0.02005 | 0.0026% | — | zona_expirada_setup_B |
| 2026-09-12 00:05 | DOGE-USDT-SWAP | 0.08444 | 0.08457/0.08429 | 0.08427 | sup 0.08350 (ha 4 candles) | 0.00119 | 0.0085% | — | sem_zona |
| 2026-09-12 00:05 | ARB-USDT-SWAP | 0.14080 | 0.14204/0.14009 | 0.13937 | sup 0.13729 (ha 4 candles) | 0.00388 | 0.0071% | — | sem_zona |
| 2026-09-12 00:05 | WLD-USDT-SWAP | 0.40400 | 0.40670/0.40300 | 0.39970 | res 0.42870 (ha 12 candles) | 0.00878 | 0.0083% | — | sem_zona |
| 2026-09-12 00:05 | SUI-USDT-SWAP | 0.72600 | 0.72950/0.72480 | 0.72520 | — | 0.01279 | 0.0041% | B/compra@0.73270 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-12 00:05 | UNI-USDT-SWAP | 6.0920 | 6.1360/6.0230 | 6.0080 | sup 5.9310 (ha 3 candles) | 0.14371 | 0.0100% | — | sem_zona |
| 2026-09-12 00:05 | LINK-USDT-SWAP | 11.51 | 11.55/11.48 | 11.54 | sup 11.46 (ha 4 candles) | 0.17536 | -0.0076% | — | sem_zona |
| 2026-09-12 01:05 | BTC-USDT-SWAP | 77244.9 | 77321.4/77201.3 | 77244.9 | — | 480.99 | 0.0044% | B/compra@77574.3 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-12 01:05 | ETH-USDT-SWAP | 2512.4 | 2515.5/2508.2 | 2512.4 | res 2667.3 (ha 13 candles) | 26.63 | 0.0082% | B/venda@2536.9 (0t/6c) | zona_mapeada_setup_B |
| 2026-09-12 01:05 | SOL-USDT-SWAP | 101.59 | 101.88/101.41 | 101.59 | — | 1.1593 | 0.0077% | B/compra@101.61 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-12 01:05 | XRP-USDT-SWAP | 1.3632 | 1.3654/1.3615 | 1.3632 | sup 1.3453 (ha 8 candles) | 0.01576 | 0.0025% | — | sem_zona |
| 2026-09-12 01:05 | DOGE-USDT-SWAP | 0.08440 | 0.08456/0.08431 | 0.08440 | — | 0.00098 | 0.0096% | B/venda@0.08394 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-12 01:05 | ARB-USDT-SWAP | 0.14102 | 0.14121/0.14014 | 0.14102 | sup 0.13729 (ha 5 candles) | 0.00321 | 0.0061% | — | sem_zona |
| 2026-09-12 01:05 | WLD-USDT-SWAP | 0.40330 | 0.40560/0.40270 | 0.40330 | — | 0.00747 | 0.0087% | B/venda@0.40810 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-12 01:05 | SUI-USDT-SWAP | 0.72690 | 0.72860/0.72360 | 0.72690 | sup 0.71700 (ha 5 candles) | 0.01054 | 0.0072% | B/compra@0.73270 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-12 01:05 | UNI-USDT-SWAP | 6.1440 | 6.1490/6.0730 | 6.1440 | — | 0.12164 | 0.0047% | — | sem_zona |
| 2026-09-12 01:05 | LINK-USDT-SWAP | 11.48 | 11.51/11.44 | 11.48 | sup 11.46 (ha 5 candles) | 0.14407 | -0.0075% | B/venda@11.52 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-12 02:05 | BTC-USDT-SWAP | 77198.1 | 77287.5/77189.7 | 77244.9 | — | 386.73 | 0.0067% | B/compra@77574.3 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-12 02:05 | ETH-USDT-SWAP | 2511.8 | 2514.8/2508.5 | 2512.4 | res 2667.3 (ha 14 candles) | 21.63 | 0.0084% | B/venda@2536.9 (0t/7c) | zona_mapeada_setup_B |
| 2026-09-12 02:05 | SOL-USDT-SWAP | 101.55 | 101.87/101.50 | 101.59 | — | 0.97214 | 0.0078% | B/compra@101.61 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-12 02:05 | XRP-USDT-SWAP | 1.3624 | 1.3656/1.3609 | 1.3632 | sup 1.3453 (ha 9 candles) | 0.01274 | 0.0029% | — | sem_zona |
| 2026-09-12 02:05 | DOGE-USDT-SWAP | 0.08435 | 0.08449/0.08421 | 0.08440 | — | 0.00083 | 0.0100% | B/venda@0.08394 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-12 02:05 | ARB-USDT-SWAP | 0.14074 | 0.14195/0.14066 | 0.14102 | sup 0.13729 (ha 6 candles) | 0.00286 | 0.0050% | — | sem_zona |
| 2026-09-12 02:05 | WLD-USDT-SWAP | 0.40130 | 0.40380/0.40060 | 0.40330 | — | 0.00680 | 0.0077% | B/venda@0.40810 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-12 02:05 | SUI-USDT-SWAP | 0.72290 | 0.72710/0.72130 | 0.72690 | sup 0.71700 (ha 6 candles) | 0.00929 | 0.0083% | B/compra@0.73270 (0t/2c) | zona_mapeada_setup_B |
| 2026-09-12 02:05 | UNI-USDT-SWAP | 6.1720 | 6.1860/6.1130 | 6.1440 | — | 0.10843 | 0.0003% | — | sem_zona |
| 2026-09-12 02:05 | LINK-USDT-SWAP | 11.49 | 11.53/11.47 | 11.48 | sup 11.46 (ha 6 candles) | 0.12207 | -0.0067% | B/venda@11.52 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-12 03:05 | BTC-USDT-SWAP | 77182.0 | 77229.6/77140.4 | 77244.9 | — | 281.62 | 0.0078% | B/compra@77574.3 (0t/2c) | zona_mapeada_setup_B |
| 2026-09-12 03:05 | ETH-USDT-SWAP | 2510.6 | 2512.0/2507.4 | 2512.4 | res 2667.3 (ha 15 candles) | 16.63 | 0.0080% | — | zona_expirada_setup_B |
| 2026-09-12 03:05 | SOL-USDT-SWAP | 101.59 | 101.68/101.32 | 101.59 | — | 0.82571 | 0.0075% | — | descartado_rr_baixo_setup_B |
| 2026-09-12 03:05 | XRP-USDT-SWAP | 1.3632 | 1.3646/1.3604 | 1.3632 | sup 1.3453 (ha 10 candles) | 0.01024 | 0.0017% | — | sem_zona |
| 2026-09-12 03:05 | DOGE-USDT-SWAP | 0.08439 | 0.08448/0.08420 | 0.08440 | — | 0.00067 | 0.0100% | B/venda@0.08394 (0t/2c) | zona_mapeada_setup_B |
| 2026-09-12 03:05 | ARB-USDT-SWAP | 0.14059 | 0.14149/0.14021 | 0.14102 | sup 0.13729 (ha 7 candles) | 0.00246 | 0.0011% | — | sem_zona |
| 2026-09-12 03:05 | WLD-USDT-SWAP | 0.39940 | 0.40160/0.39800 | 0.40330 | — | 0.00581 | 0.0067% | B/venda@0.40810 (0t/2c) | zona_mapeada_setup_B |
| 2026-09-12 03:05 | SUI-USDT-SWAP | 0.72250 | 0.72510/0.72010 | 0.72690 | sup 0.71700 (ha 7 candles) | 0.00780 | 0.0078% | B/compra@0.73270 (0t/3c) | zona_mapeada_setup_B |
| 2026-09-12 03:05 | UNI-USDT-SWAP | 6.2250 | 6.2320/6.1450 | 6.1440 | — | 0.09386 | -0.0014% | — | sem_zona |
| 2026-09-12 03:05 | LINK-USDT-SWAP | 11.51 | 11.53/11.48 | 11.48 | sup 11.46 (ha 7 candles) | 0.09900 | -0.0052% | B/venda@11.52 (2t/0c) | zona_mapeada_setup_B |
| 2026-09-12 04:05 | BTC-USDT-SWAP | 77267.1 | 77327.8/77175.3 | 77244.9 | — | 243.43 | 0.0093% | B/compra@77574.3 (0t/3c) | zona_mapeada_setup_B |
| 2026-09-12 04:05 | ETH-USDT-SWAP | 2518.2 | 2522.4/2509.1 | 2512.4 | res 2667.3 (ha 16 candles) | 14.60 | 0.0067% | — | sem_zona |
| 2026-09-12 04:05 | SOL-USDT-SWAP | 101.64 | 101.84/101.46 | 101.59 | — | 0.77214 | 0.0078% | B/compra@102.20 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-12 04:05 | XRP-USDT-SWAP | 1.3623 | 1.3647/1.3614 | 1.3632 | sup 1.3453 (ha 11 candles) | 0.00931 | 0.0015% | — | sem_zona |
| 2026-09-12 04:05 | DOGE-USDT-SWAP | 0.08438 | 0.08452/0.08432 | 0.08440 | — | 0.00061 | 0.0100% | B/venda@0.08394 (0t/3c) | zona_mapeada_setup_B |
| 2026-09-12 04:05 | ARB-USDT-SWAP | 0.14297 | 0.14380/0.14031 | 0.14102 | sup 0.13729 (ha 8 candles) | 0.00248 | 0.0014% | — | sem_zona |
| 2026-09-12 04:05 | WLD-USDT-SWAP | 0.40020 | 0.40170/0.39850 | 0.40330 | — | 0.00559 | 0.0027% | B/venda@0.40810 (0t/3c) | zona_mapeada_setup_B |
| 2026-09-12 04:05 | SUI-USDT-SWAP | 0.72310 | 0.72570/0.72160 | 0.72690 | sup 0.71700 (ha 8 candles) | 0.00731 | 0.0065% | B/compra@0.73270 (0t/4c) | zona_mapeada_setup_B |
| 2026-09-12 04:05 | UNI-USDT-SWAP | 6.2820 | 6.2850/6.1680 | 6.1440 | — | 0.09257 | -0.0012% | — | sem_zona |
| 2026-09-12 04:05 | LINK-USDT-SWAP | 11.51 | 11.54/11.49 | 11.48 | sup 11.44 (ha 3 candles) | 0.09243 | -0.0004% | — | zona_expirada_setup_B |
| 2026-09-12 05:05 | BTC-USDT-SWAP | 77236.9 | 77315.7/77225.0 | 77236.9 | — | 216.13 | 0.0084% | B/compra@77574.3 (0t/4c) | zona_mapeada_setup_B |
| 2026-09-12 05:05 | ETH-USDT-SWAP | 2522.7 | 2524.6/2518.2 | 2522.7 | res 2667.3 (ha 17 candles) | 13.68 | 0.0045% | — | sem_zona |
| 2026-09-12 05:05 | SOL-USDT-SWAP | 101.62 | 101.92/101.58 | 101.62 | — | 0.74786 | 0.0087% | B/compra@102.20 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-12 05:05 | XRP-USDT-SWAP | 1.3684 | 1.3696/1.3623 | 1.3684 | sup 1.3453 (ha 12 candles) | 0.00891 | 0.0014% | — | sem_zona |
| 2026-09-12 05:05 | DOGE-USDT-SWAP | 0.08473 | 0.08479/0.08437 | 0.08473 | — | 0.00056 | 0.0100% | B/venda@0.08394 (0t/4c) | zona_mapeada_setup_B |
| 2026-09-12 05:05 | ARB-USDT-SWAP | 0.14439 | 0.14627/0.14244 | 0.14439 | sup 0.13729 (ha 9 candles) | 0.00258 | 0.0014% | — | sem_zona |
| 2026-09-12 05:05 | WLD-USDT-SWAP | 0.40380 | 0.40420/0.39990 | 0.40380 | — | 0.00541 | 0.0024% | B/venda@0.40810 (0t/4c) | zona_mapeada_setup_B |
| 2026-09-12 05:05 | SUI-USDT-SWAP | 0.72780 | 0.72940/0.72300 | 0.72780 | sup 0.71700 (ha 9 candles) | 0.00672 | 0.0047% | B/compra@0.73270 (0t/5c) | zona_mapeada_setup_B |
| 2026-09-12 05:05 | UNI-USDT-SWAP | 6.3500 | 6.3770/6.2570 | 6.3500 | — | 0.09150 | -0.0039% | B/venda@6.3780 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-12 05:05 | LINK-USDT-SWAP | 11.56 | 11.58/11.51 | 11.56 | sup 11.44 (ha 4 candles) | 0.08814 | 0.0017% | — | sem_zona |
| 2026-09-12 06:05 | BTC-USDT-SWAP | 77322.6 | 77330.0/77231.4 | 77236.9 | — | 173.58 | 0.0069% | B/compra@77574.3 (0t/5c) | zona_mapeada_setup_B |
| 2026-09-12 06:05 | ETH-USDT-SWAP | 2532.1 | 2536.4/2521.8 | 2522.7 | res 2667.3 (ha 18 candles) | 11.92 | 0.0028% | — | sem_zona |
| 2026-09-12 06:05 | SOL-USDT-SWAP | 101.78 | 101.82/101.46 | 101.62 | — | 0.65071 | 0.0083% | B/compra@102.20 (0t/2c) | zona_mapeada_setup_B |
| 2026-09-12 06:05 | XRP-USDT-SWAP | 1.3662 | 1.3696/1.3641 | 1.3684 | sup 1.3453 (ha 13 candles) | 0.00774 | 0.0003% | — | sem_zona |
| 2026-09-12 06:05 | DOGE-USDT-SWAP | 0.08475 | 0.08487/0.08458 | 0.08473 | — | 0.00047 | 0.0100% | B/venda@0.08394 (0t/5c) | zona_mapeada_setup_B |
| 2026-09-12 06:05 | ARB-USDT-SWAP | 0.14339 | 0.14507/0.14321 | 0.14439 | sup 0.13729 (ha 10 candles) | 0.00235 | 0.0023% | — | sem_zona |
| 2026-09-12 06:05 | WLD-USDT-SWAP | 0.40200 | 0.40440/0.40030 | 0.40380 | — | 0.00467 | 0.0006% | B/venda@0.40810 (0t/5c) | zona_mapeada_setup_B |
| 2026-09-12 06:05 | SUI-USDT-SWAP | 0.72710 | 0.72970/0.72590 | 0.72780 | sup 0.72010 (ha 3 candles) | 0.00606 | 0.0039% | — | invalidado_setup_B |
| 2026-09-12 06:05 | UNI-USDT-SWAP | 6.3510 | 6.4210/6.3010 | 6.3500 | — | 0.09107 | -0.0038% | B/venda@6.3780 (1t/0c) | zona_mapeada_setup_B |
| 2026-09-12 06:05 | LINK-USDT-SWAP | 11.53 | 11.57/11.51 | 11.56 | sup 11.44 (ha 5 candles) | 0.07700 | 0.0024% | B/venda@11.49 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-12 07:05 | BTC-USDT-SWAP | 77314.8 | 77350.0/77287.6 | 77236.9 | — | 151.83 | 0.0051% | B/compra@77574.3 (0t/6c) | zona_mapeada_setup_B |
| 2026-09-12 07:05 | ETH-USDT-SWAP | 2529.6 | 2535.9/2527.6 | 2522.7 | res 2667.3 (ha 19 candles) | 11.39 | 0.0006% | — | sem_zona |
| 2026-09-12 07:05 | SOL-USDT-SWAP | 101.96 | 102.18/101.72 | 101.62 | — | 0.58571 | 0.0080% | — | invalidado_setup_B |
| 2026-09-12 07:05 | XRP-USDT-SWAP | 1.3691 | 1.3698/1.3654 | 1.3684 | sup 1.3453 (ha 14 candles) | 0.00686 | -0.0008% | — | sem_zona |
| 2026-09-12 07:05 | DOGE-USDT-SWAP | 0.08490 | 0.08493/0.08470 | 0.08473 | — | 0.00043 | 0.0075% | B/venda@0.08394 (0t/6c) | zona_mapeada_setup_B |
| 2026-09-12 07:05 | ARB-USDT-SWAP | 0.14284 | 0.14358/0.14238 | 0.14439 | sup 0.13729 (ha 11 candles) | 0.00228 | 0.0046% | — | sem_zona |
| 2026-09-12 07:05 | WLD-USDT-SWAP | 0.40110 | 0.40280/0.40010 | 0.40380 | — | 0.00435 | -0.0033% | B/venda@0.40810 (0t/6c) | zona_mapeada_setup_B |
| 2026-09-12 07:05 | SUI-USDT-SWAP | 0.72660 | 0.72720/0.72410 | 0.72780 | sup 0.72010 (ha 4 candles) | 0.00564 | 0.0029% | — | sem_zona |
| 2026-09-12 07:05 | UNI-USDT-SWAP | 6.3510 | 6.3840/6.3220 | 6.3500 | — | 0.08879 | -0.0028% | B/venda@6.3780 (2t/0c) | zona_mapeada_setup_B |
| 2026-09-12 07:05 | LINK-USDT-SWAP | 11.54 | 11.57/11.53 | 11.56 | sup 11.44 (ha 6 candles) | 0.07129 | 0.0027% | B/venda@11.49 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-12 08:05 | BTC-USDT-SWAP | 77292.5 | 77359.2/77275.3 | 77236.9 | — | 135.11 | 0.0040% | B/compra@77574.3 (0t/7c) | zona_mapeada_setup_B |
| 2026-09-12 08:05 | ETH-USDT-SWAP | 2532.3 | 2535.0/2529.6 | 2522.7 | res 2667.3 (ha 20 candles) | 9.9421 | -0.0009% | — | sem_zona |
| 2026-09-12 08:05 | SOL-USDT-SWAP | 102.10 | 102.22/101.91 | 101.62 | — | 0.53571 | 0.0088% | — | sem_zona |
| 2026-09-12 08:05 | XRP-USDT-SWAP | 1.3726 | 1.3737/1.3690 | 1.3684 | sup 1.3453 (ha 15 candles) | 0.00641 | -0.0004% | — | sem_zona |
| 2026-09-12 08:05 | DOGE-USDT-SWAP | 0.08496 | 0.08515/0.08484 | 0.08473 | — | 0.00040 | 0.0070% | B/venda@0.08394 (0t/7c) | zona_mapeada_setup_B |
| 2026-09-12 08:05 | ARB-USDT-SWAP | 0.14287 | 0.14355/0.14223 | 0.14439 | sup 0.13729 (ha 12 candles) | 0.00210 | 0.0057% | — | sem_zona |
| 2026-09-12 08:05 | WLD-USDT-SWAP | 0.40110 | 0.40220/0.40020 | 0.40380 | — | 0.00401 | -0.0073% | B/venda@0.40810 (0t/7c) | zona_mapeada_setup_B |
| 2026-09-12 08:05 | SUI-USDT-SWAP | 0.72620 | 0.72770/0.72490 | 0.72780 | sup 0.72010 (ha 5 candles) | 0.00531 | 0.0054% | — | sem_zona |
| 2026-09-12 08:05 | UNI-USDT-SWAP | 6.3620 | 6.3990/6.3430 | 6.3500 | — | 0.08707 | -0.0032% | — | zona_expirada_setup_B |
| 2026-09-12 08:05 | LINK-USDT-SWAP | 11.53 | 11.56/11.52 | 11.56 | sup 11.44 (ha 7 candles) | 0.06686 | 0.0030% | B/venda@11.49 (0t/2c) | zona_mapeada_setup_B |
| 2026-09-12 09:05 | BTC-USDT-SWAP | 77321.6 | 77321.7/77247.1 | 77321.6 | — | 115.50 | 0.0029% | — | zona_expirada_setup_B |
| 2026-09-12 09:05 | ETH-USDT-SWAP | 2534.9 | 2536.0/2528.6 | 2534.9 | res 2536.4 (ha 3 candles) | 8.4629 | -0.0016% | — | sem_zona |
| 2026-09-12 09:05 | SOL-USDT-SWAP | 102.07 | 102.20/101.88 | 102.07 | — | 0.48000 | 0.0078% | — | sem_zona |
| 2026-09-12 09:05 | XRP-USDT-SWAP | 1.3715 | 1.3735/1.3693 | 1.3715 | sup 1.3453 (ha 16 candles) | 0.00565 | -0.0009% | — | sem_zona |
| 2026-09-12 09:05 | DOGE-USDT-SWAP | 0.08502 | 0.08507/0.08488 | 0.08502 | — | 0.00035 | 0.0074% | — | zona_expirada_setup_B |
| 2026-09-12 09:05 | ARB-USDT-SWAP | 0.14340 | 0.14408/0.14201 | 0.14340 | sup 0.13729 (ha 13 candles) | 0.00199 | 0.0060% | — | sem_zona |
| 2026-09-12 09:05 | WLD-USDT-SWAP | 0.40220 | 0.40290/0.39960 | 0.40220 | — | 0.00371 | -0.0076% | — | zona_expirada_setup_B |
| 2026-09-12 09:05 | SUI-USDT-SWAP | 0.72850 | 0.72900/0.72480 | 0.72850 | sup 0.72010 (ha 6 candles) | 0.00476 | 0.0054% | — | sem_zona |
| 2026-09-12 09:05 | UNI-USDT-SWAP | 6.3790 | 6.3790/6.3110 | 6.3790 | — | 0.08350 | -0.0027% | — | sem_zona |
| 2026-09-12 09:05 | LINK-USDT-SWAP | 11.56 | 11.56/11.51 | 11.56 | sup 11.44 (ha 8 candles) | 0.06114 | 0.0019% | — | invalidado_setup_B |
| 2026-09-12 10:05 | BTC-USDT-SWAP | 77300.2 | 77321.7/77252.1 | 77321.6 | — | 101.16 | 0.0017% | — | sem_zona |
| 2026-09-12 10:05 | ETH-USDT-SWAP | 2534.3 | 2535.3/2530.7 | 2534.9 | res 2536.4 (ha 4 candles) | 7.4721 | -0.0027% | — | sem_zona |
| 2026-09-12 10:05 | SOL-USDT-SWAP | 102.01 | 102.35/101.88 | 102.07 | — | 0.44429 | 0.0062% | — | sem_zona |
| 2026-09-12 10:05 | XRP-USDT-SWAP | 1.3693 | 1.3722/1.3673 | 1.3715 | sup 1.3453 (ha 17 candles) | 0.00517 | -0.0021% | — | sem_zona |
| 2026-09-12 10:05 | DOGE-USDT-SWAP | 0.08498 | 0.08513/0.08491 | 0.08502 | — | 0.00031 | 0.0069% | — | sem_zona |
| 2026-09-12 10:05 | ARB-USDT-SWAP | 0.14434 | 0.14478/0.14291 | 0.14340 | sup 0.13729 (ha 14 candles) | 0.00195 | 0.0082% | — | sem_zona |
| 2026-09-12 10:05 | WLD-USDT-SWAP | 0.40080 | 0.40280/0.40020 | 0.40220 | — | 0.00351 | -0.0087% | — | sem_zona |
| 2026-09-12 10:05 | SUI-USDT-SWAP | 0.72750 | 0.72960/0.72630 | 0.72850 | sup 0.72010 (ha 7 candles) | 0.00441 | 0.0060% | — | sem_zona |
| 2026-09-12 10:05 | UNI-USDT-SWAP | 6.3650 | 6.4800/6.3420 | 6.3790 | — | 0.08821 | -0.0024% | — | sem_zona |
| 2026-09-12 10:05 | LINK-USDT-SWAP | 11.54 | 11.57/11.52 | 11.56 | sup 11.44 (ha 9 candles) | 0.05829 | 0.0014% | B/venda@11.52 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-12 11:05 | BTC-USDT-SWAP | 77332.9 | 77371.7/77200.0 | 77321.6 | — | 105.73 | 0.0025% | — | sem_zona |
| 2026-09-12 11:05 | ETH-USDT-SWAP | 2543.7 | 2546.5/2532.2 | 2534.9 | res 2536.4 (ha 5 candles) | 7.9564 | -0.0001% | A/compra@2536.4 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-12 11:05 | SOL-USDT-SWAP | 101.94 | 102.17/101.68 | 102.07 | — | 0.42929 | 0.0047% | — | sem_zona |
| 2026-09-12 11:05 | XRP-USDT-SWAP | 1.3674 | 1.3703/1.3652 | 1.3715 | sup 1.3453 (ha 18 candles) | 0.00495 | -0.0016% | — | sem_zona |
| 2026-09-12 11:05 | DOGE-USDT-SWAP | 0.08493 | 0.08506/0.08472 | 0.08502 | — | 0.00029 | 0.0056% | — | sem_zona |
| 2026-09-12 11:05 | ARB-USDT-SWAP | 0.14322 | 0.14499/0.14249 | 0.14340 | sup 0.13729 (ha 15 candles) | 0.00200 | 0.0050% | — | sem_zona |
| 2026-09-12 11:05 | WLD-USDT-SWAP | 0.40020 | 0.40180/0.39880 | 0.40220 | — | 0.00337 | -0.0108% | — | sem_zona |
| 2026-09-12 11:05 | SUI-USDT-SWAP | 0.72530 | 0.72790/0.72390 | 0.72850 | sup 0.72010 (ha 8 candles) | 0.00426 | 0.0064% | — | sem_zona |
| 2026-09-12 11:05 | UNI-USDT-SWAP | 6.3830 | 6.4210/6.3280 | 6.3790 | — | 0.08936 | -0.0020% | — | sem_zona |
| 2026-09-12 11:05 | LINK-USDT-SWAP | 11.55 | 11.56/11.52 | 11.56 | sup 11.44 (ha 10 candles) | 0.05593 | -0.0006% | — | invalidado_setup_B |
| 2026-09-12 12:05 | BTC-USDT-SWAP | 77426.6 | 77493.8/77332.9 | 77321.6 | — | 108.33 | 0.0034% | — | sem_zona |
| 2026-09-12 12:05 | ETH-USDT-SWAP | 2539.0 | 2544.5/2538.3 | 2534.9 | res 2536.4 (ha 6 candles) | 7.8693 | 0.0032% | A/compra@2536.4 (1t/0c) | zona_mapeada_setup_A |
| 2026-09-12 12:05 | SOL-USDT-SWAP | 101.95 | 102.06/101.84 | 102.07 | — | 0.38714 | 0.0044% | — | sem_zona |
| 2026-09-12 12:05 | XRP-USDT-SWAP | 1.3693 | 1.3708/1.3669 | 1.3715 | sup 1.3453 (ha 19 candles) | 0.00489 | -0.0006% | — | sem_zona |
| 2026-09-12 12:05 | DOGE-USDT-SWAP | 0.08510 | 0.08514/0.08491 | 0.08502 | — | 0.00028 | 0.0053% | — | sem_zona |
| 2026-09-12 12:05 | ARB-USDT-SWAP | 0.14347 | 0.14465/0.14312 | 0.14340 | sup 0.14201 (ha 3 candles) | 0.00193 | 0.0048% | — | sem_zona |
| 2026-09-12 12:05 | WLD-USDT-SWAP | 0.40480 | 0.40630/0.39950 | 0.40220 | — | 0.00354 | -0.0105% | — | sem_zona |
| 2026-09-12 12:05 | SUI-USDT-SWAP | 0.72610 | 0.72720/0.72490 | 0.72850 | sup 0.72010 (ha 9 candles) | 0.00421 | 0.0055% | — | sem_zona |
| 2026-09-12 12:05 | UNI-USDT-SWAP | 6.4130 | 6.4450/6.3680 | 6.3790 | — | 0.09143 | -0.0049% | — | sem_zona |
| 2026-09-12 12:05 | LINK-USDT-SWAP | 11.57 | 11.58/11.54 | 11.56 | sup 11.51 (ha 3 candles) | 0.05493 | -0.0022% | — | sem_zona |
| 2026-09-12 13:05 | BTC-USDT-SWAP | 77350.1 | 77447.2/77331.1 | 77350.1 | — | 107.43 | 0.0038% | — | sem_zona |
| 2026-09-12 13:05 | ETH-USDT-SWAP | 2534.1 | 2541.4/2528.6 | 2534.1 | res 2536.4 (ha 7 candles) | 8.2321 | 0.0049% | — | invalidado_setup_A |
| 2026-09-12 13:05 | SOL-USDT-SWAP | 102.01 | 102.11/101.80 | 102.01 | — | 0.37929 | 0.0038% | — | sem_zona |
| 2026-09-12 13:05 | XRP-USDT-SWAP | 1.3719 | 1.3736/1.3678 | 1.3719 | sup 1.3453 (ha 20 candles) | 0.00475 | 0.0025% | — | sem_zona |
| 2026-09-12 13:05 | DOGE-USDT-SWAP | 0.08506 | 0.08533/0.08493 | 0.08506 | — | 0.00028 | 0.0056% | — | sem_zona |
| 2026-09-12 13:05 | ARB-USDT-SWAP | 0.14364 | 0.14454/0.14317 | 0.14364 | sup 0.14201 (ha 4 candles) | 0.00190 | 0.0029% | — | sem_zona |
| 2026-09-12 13:05 | WLD-USDT-SWAP | 0.40660 | 0.40890/0.40350 | 0.40660 | — | 0.00363 | -0.0067% | — | sem_zona |
| 2026-09-12 13:05 | SUI-USDT-SWAP | 0.72800 | 0.72950/0.72520 | 0.72800 | sup 0.72010 (ha 10 candles) | 0.00420 | 0.0067% | — | sem_zona |
| 2026-09-12 13:05 | UNI-USDT-SWAP | 6.5120 | 6.5670/6.4020 | 6.5120 | — | 0.09750 | -0.0030% | B/venda@6.5420 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-12 13:05 | LINK-USDT-SWAP | 11.58 | 11.62/11.56 | 11.58 | sup 11.51 (ha 4 candles) | 0.05386 | 0.0006% | — | sem_zona |
| 2026-09-12 14:05 | BTC-USDT-SWAP | 77331.3 | 77391.2/77310.0 | 77350.1 | — | 104.95 | 0.0071% | — | sem_zona |
| 2026-09-12 14:05 | ETH-USDT-SWAP | 2530.7 | 2535.4/2529.2 | 2534.1 | res 2546.5 (ha 3 candles) | 8.4100 | 0.0067% | — | sem_zona |
| 2026-09-12 14:05 | SOL-USDT-SWAP | 102.02 | 102.07/101.87 | 102.01 | — | 0.36143 | 0.0041% | — | sem_zona |
| 2026-09-12 14:05 | XRP-USDT-SWAP | 1.3692 | 1.3724/1.3684 | 1.3719 | sup 1.3652 (ha 3 candles) | 0.00471 | 0.0042% | — | sem_zona |
| 2026-09-12 14:05 | DOGE-USDT-SWAP | 0.08500 | 0.08511/0.08491 | 0.08506 | — | 0.00027 | 0.0076% | — | sem_zona |
| 2026-09-12 14:05 | ARB-USDT-SWAP | 0.14246 | 0.14428/0.14095 | 0.14364 | sup 0.14201 (ha 5 candles) | 0.00200 | 0.0010% | — | sem_zona |
| 2026-09-12 14:05 | WLD-USDT-SWAP | 0.40740 | 0.41150/0.40500 | 0.40660 | — | 0.00383 | -0.0030% | B/venda@0.41000 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-12 14:05 | SUI-USDT-SWAP | 0.72700 | 0.72930/0.72650 | 0.72800 | sup 0.72390 (ha 3 candles) | 0.00406 | 0.0073% | — | sem_zona |
| 2026-09-12 14:05 | UNI-USDT-SWAP | 6.3750 | 6.5580/6.3270 | 6.5120 | — | 0.10593 | -0.0020% | — | CONFIRMADO_setup_B |
| 2026-09-12 14:05 | LINK-USDT-SWAP | 11.52 | 11.60/11.52 | 11.58 | sup 11.51 (ha 5 candles) | 0.05507 | 0.0033% | B/venda@11.49 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-12 15:05 | BTC-USDT-SWAP | 77185.3 | 77371.8/77147.4 | 77350.1 | — | 112.40 | 0.0099% | — | sem_zona |
| 2026-09-12 15:05 | ETH-USDT-SWAP | 2525.1 | 2533.6/2522.3 | 2534.1 | res 2546.5 (ha 4 candles) | 8.6971 | 0.0088% | — | sem_zona |
| 2026-09-12 15:05 | SOL-USDT-SWAP | 101.93 | 102.11/101.91 | 102.01 | — | 0.34214 | 0.0059% | — | sem_zona |
| 2026-09-12 15:05 | XRP-USDT-SWAP | 1.3663 | 1.3697/1.3655 | 1.3719 | sup 1.3652 (ha 4 candles) | 0.00473 | 0.0076% | — | sem_zona |
| 2026-09-12 15:05 | DOGE-USDT-SWAP | 0.08496 | 0.08508/0.08477 | 0.08506 | — | 0.00028 | 0.0097% | — | sem_zona |
| 2026-09-12 15:05 | ARB-USDT-SWAP | 0.14092 | 0.14257/0.14052 | 0.14364 | sup 0.14201 (ha 6 candles) | 0.00207 | 0.0009% | A/venda@0.14201 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-12 15:05 | WLD-USDT-SWAP | 0.40440 | 0.40810/0.40390 | 0.40660 | — | 0.00392 | 0.0007% | B/venda@0.41000 (0t/1c) | zona_mapeada_setup_B |
| 2026-09-12 15:05 | SUI-USDT-SWAP | 0.72510 | 0.72780/0.72420 | 0.72800 | sup 0.72390 (ha 4 candles) | 0.00396 | 0.0089% | — | sem_zona |
| 2026-09-12 15:05 | UNI-USDT-SWAP | 6.3470 | 6.3840/6.2580 | 6.5120 | — | 0.10950 | -0.0005% | B/venda@6.3780 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-12 15:05 | LINK-USDT-SWAP | 11.52 | 11.55/11.49 | 11.58 | sup 11.51 (ha 6 candles) | 0.05371 | 0.0020% | — | invalidado_setup_B |
| 2026-09-12 16:05 | BTC-USDT-SWAP | 77120.4 | 77198.1/77091.2 | 77350.1 | — | 113.05 | 0.0100% | — | sem_zona |
| 2026-09-12 16:05 | ETH-USDT-SWAP | 2521.8 | 2526.7/2519.8 | 2534.1 | res 2546.5 (ha 5 candles) | 8.7407 | 0.0100% | — | sem_zona |
| 2026-09-12 16:05 | SOL-USDT-SWAP | 101.62 | 101.94/101.54 | 102.01 | — | 0.34429 | 0.0065% | B/compra@101.61 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-12 16:05 | XRP-USDT-SWAP | 1.3627 | 1.3663/1.3622 | 1.3719 | sup 1.3652 (ha 5 candles) | 0.00469 | 0.0084% | A/venda@1.3652 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-12 16:05 | DOGE-USDT-SWAP | 0.08470 | 0.08496/0.08461 | 0.08506 | — | 0.00028 | 0.0095% | B/compra@0.08450 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-12 16:05 | ARB-USDT-SWAP | 0.14074 | 0.14111/0.14002 | 0.14364 | sup 0.14201 (ha 7 candles) | 0.00206 | 0.0030% | A/venda@0.14201 (0t/1c) | zona_mapeada_setup_A |
| 2026-09-12 16:05 | WLD-USDT-SWAP | 0.40140 | 0.40450/0.40120 | 0.40660 | — | 0.00393 | 0.0027% | B/venda@0.41000 (0t/2c) | zona_mapeada_setup_B |
| 2026-09-12 16:05 | SUI-USDT-SWAP | 0.72140 | 0.72510/0.72020 | 0.72800 | sup 0.72390 (ha 5 candles) | 0.00390 | 0.0065% | A/venda@0.72390 (0t/0c) | zona_mapeada_setup_A |
| 2026-09-12 16:05 | UNI-USDT-SWAP | 6.3020 | 6.3510/6.2830 | 6.5120 | — | 0.10914 | -0.0002% | — | CONFIRMADO_setup_B |
| 2026-09-12 16:05 | LINK-USDT-SWAP | 11.51 | 11.53/11.48 | 11.58 | sup 11.51 (ha 7 candles) | 0.05321 | 0.0016% | A/venda@11.51 (0t/0c) | zona_mapeada_setup_A |
