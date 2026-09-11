# Log de Monitoramento Automatico -- Multi-Par (script gratuito, GitHub Actions)

> Gerado por script Python sem LLM (ver monitor/fetch_and_check.py). Fonte: OKX. Cobre os pares em PAIRS (configuracao no topo do script) -- BTC-USDT-SWAP e os demais adicionados na expansao de 07/09/2026. Leitura e MECANICA (regras objetivas da secao 4 do plano), sem a prosa qualitativa que o Claude gerava -- cole este log numa conversa do Claude se quiser a leitura interpretativa.

| Data/Hora (BRT) | Par | Close 1h | High/Low 1h | Close 4h | Swing 1h ref | ATR 1h | Funding | Zona ativa | Status checklist |
|---|---|---|---|---|---|---|---|---|---|
| 2026-09-09 18:05 | BTC-USDT-SWAP | 78283.3 | 78304.4/77865.6 | 78196.3 | — | 532.16 | 0.0091% | — | zona_mapeada_setup_B |
| 2026-09-09 18:05 | ETH-USDT-SWAP | 2470.6 | 2471.4/2451.7 | 2464.2 | — | 20.11 | 0.0058% | — | CONFIRMADO_setup_B |
| 2026-09-09 18:05 | SOL-USDT-SWAP | 102.50 | 102.62/101.75 | 102.28 | — | 0.94000 | -0.0041% | — | CONFIRMADO_setup_B |
| 2026-09-09 18:05 | XRP-USDT-SWAP | 1.4028 | 1.4046/1.3934 | 1.4008 | res 1.4388 (ha 8 candles) | 0.01329 | -0.0046% | — | CONFIRMADO_setup_B |
| 2026-09-09 18:05 | DOGE-USDT-SWAP | 0.08699 | 0.08709/0.08587 | 0.08699 | sup 0.08808 (ha 5 candles) | 0.00107 | 0.0100% | — | zona_expirada_setup_B |
| 2026-09-09 18:05 | ARB-USDT-SWAP | 0.15076 | 0.15205/0.14954 | 0.15118 | — | 0.00450 | 0.0100% | — | sem_zona |
| 2026-09-09 18:05 | WLD-USDT-SWAP | 0.42790 | 0.42800/0.42230 | 0.42650 | res 0.46170 (ha 12 candles) | 0.00782 | 0.0044% | — | sem_zona |
| 2026-09-09 18:05 | SUI-USDT-SWAP | 0.78540 | 0.78830/0.77650 | 0.78500 | — | 0.01259 | 0.0100% | — | CONFIRMADO_setup_B |
| 2026-09-09 18:05 | UNI-USDT-SWAP | 6.3870 | 6.5250/6.3550 | 6.4980 | sup 6.4750 (ha 5 candles) | 0.11721 | 0.0098% | — | zona_mapeada_setup_A |
| 2026-09-09 18:05 | LINK-USDT-SWAP | 11.80 | 11.89/11.71 | 11.86 | — | 0.16300 | 0.0033% | — | zona_mapeada_setup_B |
| 2026-09-09 19:05 | BTC-USDT-SWAP | 78115.3 | 78300.0/77952.6 | 78196.3 | — | 539.54 | 0.0074% | — | zona_mapeada_setup_B |
| 2026-09-09 19:05 | ETH-USDT-SWAP | 2460.7 | 2471.3/2455.0 | 2464.2 | — | 20.00 | 0.0041% | — | zona_mapeada_setup_B |
| 2026-09-09 19:05 | SOL-USDT-SWAP | 102.05 | 102.55/101.74 | 102.28 | — | 0.94571 | -0.0066% | — | zona_mapeada_setup_B |
| 2026-09-09 19:05 | XRP-USDT-SWAP | 1.3953 | 1.4029/1.3908 | 1.4008 | res 1.4388 (ha 9 candles) | 0.01344 | -0.0072% | — | zona_mapeada_setup_B |
| 2026-09-09 19:05 | DOGE-USDT-SWAP | 0.08644 | 0.08703/0.08608 | 0.08699 | sup 0.08808 (ha 6 candles) | 0.00110 | 0.0100% | — | zona_mapeada_setup_A |
| 2026-09-09 19:05 | ARB-USDT-SWAP | 0.15232 | 0.15240/0.15021 | 0.15118 | — | 0.00440 | 0.0100% | — | sem_zona |
| 2026-09-09 19:05 | WLD-USDT-SWAP | 0.42290 | 0.42810/0.42040 | 0.42650 | res 0.46170 (ha 13 candles) | 0.00807 | 0.0039% | — | sem_zona |
| 2026-09-09 19:05 | SUI-USDT-SWAP | 0.77730 | 0.78570/0.77000 | 0.78500 | — | 0.01307 | 0.0100% | — | zona_mapeada_setup_B |
| 2026-09-09 19:05 | UNI-USDT-SWAP | 6.2880 | 6.3990/6.2670 | 6.4980 | sup 6.4750 (ha 6 candles) | 0.11586 | 0.0100% | — | zona_mapeada_setup_A |
| 2026-09-09 19:05 | LINK-USDT-SWAP | 11.74 | 11.82/11.69 | 11.86 | — | 0.16057 | 0.0020% | — | zona_mapeada_setup_B |
| 2026-09-09 20:05 | BTC-USDT-SWAP | 77886.6 | 78166.7/77710.0 | 78196.3 | — | 534.76 | 0.0064% | — | descartado_rr_baixo_setup_B |
| 2026-09-09 20:05 | ETH-USDT-SWAP | 2449.0 | 2462.4/2442.0 | 2464.2 | — | 20.46 | 0.0027% | — | invalidado_setup_B |
| 2026-09-09 20:05 | SOL-USDT-SWAP | 100.75 | 102.14/100.15 | 102.28 | — | 1.0514 | -0.0082% | — | invalidado_setup_B |
| 2026-09-09 20:05 | XRP-USDT-SWAP | 1.3835 | 1.3966/1.3763 | 1.4008 | res 1.4388 (ha 10 candles) | 0.01414 | -0.0094% | — | invalidado_setup_B |
| 2026-09-09 20:05 | DOGE-USDT-SWAP | 0.08552 | 0.08656/0.08450 | 0.08699 | sup 0.08808 (ha 7 candles) | 0.00120 | 0.0078% | — | zona_mapeada_setup_A |
| 2026-09-09 20:05 | ARB-USDT-SWAP | 0.15167 | 0.15289/0.14970 | 0.15118 | — | 0.00444 | 0.0100% | — | sem_zona |
| 2026-09-09 20:05 | WLD-USDT-SWAP | 0.41150 | 0.42380/0.40800 | 0.42650 | res 0.46170 (ha 14 candles) | 0.00871 | 0.0022% | — | sem_zona |
| 2026-09-09 20:05 | SUI-USDT-SWAP | 0.76410 | 0.77850/0.76130 | 0.78500 | — | 0.01381 | 0.0100% | — | zona_mapeada_setup_B |
| 2026-09-09 20:05 | UNI-USDT-SWAP | 6.1280 | 6.2990/6.1200 | 6.4980 | sup 6.4750 (ha 7 candles) | 0.12357 | 0.0082% | — | zona_mapeada_setup_A |
| 2026-09-09 20:05 | LINK-USDT-SWAP | 11.67 | 11.75/11.58 | 11.86 | — | 0.16964 | 0.0011% | — | zona_expirada_setup_B |
| 2026-09-09 21:05 | BTC-USDT-SWAP | 78265.0 | 78293.4/77881.5 | 78265.0 | sup 78028.0 (ha 8 candles) | 505.61 | 0.0047% | — | zona_mapeada_setup_B |
| 2026-09-09 21:05 | ETH-USDT-SWAP | 2467.0 | 2467.8/2448.8 | 2467.0 | sup 2468.6 (ha 8 candles) | 19.65 | 0.0017% | — | zona_mapeada_setup_A |
| 2026-09-09 21:05 | SOL-USDT-SWAP | 101.50 | 101.70/100.65 | 101.50 | — | 1.0264 | -0.0092% | — | zona_mapeada_setup_B |
| 2026-09-09 21:05 | XRP-USDT-SWAP | 1.3941 | 1.3947/1.3832 | 1.3941 | — | 0.01360 | -0.0102% | — | zona_mapeada_setup_B |
| 2026-09-09 21:05 | DOGE-USDT-SWAP | 0.08611 | 0.08620/0.08549 | 0.08611 | sup 0.08808 (ha 8 candles) | 0.00116 | 0.0050% | — | zona_mapeada_setup_A |
| 2026-09-09 21:05 | ARB-USDT-SWAP | 0.14944 | 0.15402/0.14818 | 0.14944 | — | 0.00440 | 0.0100% | — | zona_mapeada_setup_B |
| 2026-09-09 21:05 | WLD-USDT-SWAP | 0.41490 | 0.41670/0.41140 | 0.41490 | res 0.46170 (ha 15 candles) | 0.00811 | 0.0001% | — | sem_zona |
| 2026-09-09 21:05 | SUI-USDT-SWAP | 0.77170 | 0.77290/0.76380 | 0.77170 | — | 0.01297 | 0.0100% | — | zona_mapeada_setup_B |
| 2026-09-09 21:05 | UNI-USDT-SWAP | 6.1550 | 6.2290/6.1040 | 6.1550 | sup 6.4750 (ha 8 candles) | 0.11836 | 0.0090% | — | zona_mapeada_setup_A |
| 2026-09-09 21:05 | LINK-USDT-SWAP | 11.80 | 11.81/11.67 | 11.80 | — | 0.15821 | 0.0001% | — | zona_mapeada_setup_B |
| 2026-09-09 22:05 | BTC-USDT-SWAP | 78132.9 | 78347.8/78048.7 | 78265.0 | sup 78028.0 (ha 9 candles) | 503.37 | 0.0048% | — | descartado_rr_baixo_setup_B |
| 2026-09-09 22:05 | ETH-USDT-SWAP | 2463.7 | 2470.6/2461.2 | 2467.0 | sup 2468.6 (ha 9 candles) | 19.39 | 0.0002% | — | CONFIRMADO_setup_A |
| 2026-09-09 22:05 | SOL-USDT-SWAP | 100.94 | 101.67/100.88 | 101.50 | — | 1.0421 | -0.0088% | — | zona_mapeada_setup_B |
| 2026-09-09 22:05 | XRP-USDT-SWAP | 1.3865 | 1.3956/1.3851 | 1.3941 | — | 0.01386 | -0.0097% | — | descartado_rr_baixo_setup_B |
| 2026-09-09 22:05 | DOGE-USDT-SWAP | 0.08558 | 0.08617/0.08550 | 0.08611 | sup 0.08808 (ha 9 candles) | 0.00115 | 0.0019% | — | zona_mapeada_setup_A |
| 2026-09-09 22:05 | ARB-USDT-SWAP | 0.14790 | 0.15054/0.14750 | 0.14944 | — | 0.00432 | 0.0100% | — | invalidado_setup_B |
| 2026-09-09 22:05 | WLD-USDT-SWAP | 0.40580 | 0.41630/0.40390 | 0.41490 | res 0.46170 (ha 16 candles) | 0.00861 | -0.0013% | — | sem_zona |
| 2026-09-09 22:05 | SUI-USDT-SWAP | 0.76420 | 0.77220/0.76280 | 0.77170 | — | 0.01322 | 0.0100% | — | zona_mapeada_setup_B |
| 2026-09-09 22:05 | UNI-USDT-SWAP | 6.1390 | 6.1740/6.0860 | 6.1550 | sup 6.4750 (ha 9 candles) | 0.11736 | 0.0100% | — | zona_mapeada_setup_A |
| 2026-09-09 22:05 | LINK-USDT-SWAP | 11.71 | 11.81/11.70 | 11.80 | — | 0.14400 | -0.0023% | — | descartado_rr_baixo_setup_B |
| 2026-09-09 23:05 | BTC-USDT-SWAP | 78060.3 | 78479.0/77904.4 | 78265.0 | sup 77710.0 (ha 3 candles) | 497.21 | 0.0045% | — | zona_mapeada_setup_B |
| 2026-09-09 23:05 | ETH-USDT-SWAP | 2462.8 | 2478.2/2453.4 | 2467.0 | sup 2442.0 (ha 3 candles) | 19.47 | 0.0005% | — | sem_zona |
| 2026-09-09 23:05 | SOL-USDT-SWAP | 101.00 | 101.69/100.32 | 101.50 | — | 1.0664 | -0.0082% | — | zona_mapeada_setup_B |
| 2026-09-09 23:05 | XRP-USDT-SWAP | 1.3827 | 1.3949/1.3761 | 1.3941 | — | 0.01432 | -0.0068% | — | zona_mapeada_setup_B |
| 2026-09-09 23:05 | DOGE-USDT-SWAP | 0.08548 | 0.08623/0.08507 | 0.08611 | sup 0.08450 (ha 3 candles) | 0.00118 | 0.0001% | — | zona_mapeada_setup_A |
| 2026-09-09 23:05 | ARB-USDT-SWAP | 0.14629 | 0.14923/0.14547 | 0.14944 | — | 0.00431 | 0.0100% | — | zona_mapeada_setup_B |
| 2026-09-09 23:05 | WLD-USDT-SWAP | 0.40460 | 0.40990/0.40110 | 0.41490 | res 0.46170 (ha 17 candles) | 0.00865 | 0.0005% | — | sem_zona |
| 2026-09-09 23:05 | SUI-USDT-SWAP | 0.76110 | 0.77260/0.75680 | 0.77170 | — | 0.01351 | 0.0099% | — | zona_mapeada_setup_B |
| 2026-09-09 23:05 | UNI-USDT-SWAP | 5.9950 | 6.2140/5.9330 | 6.1550 | sup 6.4750 (ha 10 candles) | 0.12764 | 0.0088% | — | zona_mapeada_setup_A |
| 2026-09-09 23:05 | LINK-USDT-SWAP | 11.70 | 11.81/11.64 | 11.80 | — | 0.14914 | -0.0018% | — | sem_zona |
| 2026-09-10 00:05 | BTC-USDT-SWAP | 78324.9 | 78348.1/77939.0 | 78265.0 | sup 77710.0 (ha 4 candles) | 498.58 | 0.0059% | — | zona_mapeada_setup_B |
| 2026-09-10 00:05 | ETH-USDT-SWAP | 2473.7 | 2474.9/2459.1 | 2467.0 | sup 2442.0 (ha 4 candles) | 19.56 | 0.0022% | — | sem_zona |
| 2026-09-10 00:05 | SOL-USDT-SWAP | 101.83 | 101.84/100.93 | 101.50 | — | 1.0793 | -0.0069% | — | zona_mapeada_setup_B |
| 2026-09-10 00:05 | XRP-USDT-SWAP | 1.3914 | 1.3917/1.3797 | 1.3941 | — | 0.01419 | -0.0040% | — | CONFIRMADO_setup_B |
| 2026-09-10 00:05 | DOGE-USDT-SWAP | 0.08597 | 0.08601/0.08524 | 0.08611 | sup 0.08450 (ha 4 candles) | 0.00117 | 0.0009% | — | zona_mapeada_setup_A |
| 2026-09-10 00:05 | ARB-USDT-SWAP | 0.14923 | 0.14955/0.14592 | 0.14944 | — | 0.00443 | 0.0100% | — | invalidado_setup_B |
| 2026-09-10 00:05 | WLD-USDT-SWAP | 0.41290 | 0.41380/0.40400 | 0.41490 | res 0.46170 (ha 18 candles) | 0.00894 | 0.0009% | — | sem_zona |
| 2026-09-10 00:05 | SUI-USDT-SWAP | 0.76960 | 0.76970/0.76020 | 0.77170 | — | 0.01346 | 0.0100% | — | zona_mapeada_setup_B |
| 2026-09-10 00:05 | UNI-USDT-SWAP | 6.0180 | 6.0720/5.9650 | 6.1550 | sup 6.4750 (ha 11 candles) | 0.12921 | 0.0047% | — | zona_mapeada_setup_A |
| 2026-09-10 00:05 | LINK-USDT-SWAP | 11.84 | 11.85/11.69 | 11.80 | — | 0.15121 | -0.0001% | — | zona_mapeada_setup_B |
| 2026-09-10 01:05 | BTC-USDT-SWAP | 78297.4 | 78520.0/78238.5 | 78297.4 | sup 77710.0 (ha 5 candles) | 476.91 | 0.0077% | — | CONFIRMADO_setup_B |
| 2026-09-10 01:05 | ETH-USDT-SWAP | 2474.2 | 2478.0/2470.8 | 2474.2 | sup 2442.0 (ha 5 candles) | 18.50 | 0.0029% | — | sem_zona |
| 2026-09-10 01:05 | SOL-USDT-SWAP | 101.77 | 102.01/101.60 | 101.77 | — | 1.0229 | -0.0068% | — | invalidado_setup_B |
| 2026-09-10 01:05 | XRP-USDT-SWAP | 1.3899 | 1.3941/1.3882 | 1.3899 | — | 0.01345 | -0.0021% | — | zona_mapeada_setup_B |
| 2026-09-10 01:05 | DOGE-USDT-SWAP | 0.08595 | 0.08617/0.08578 | 0.08595 | sup 0.08450 (ha 5 candles) | 0.00111 | 0.0011% | — | zona_mapeada_setup_A |
| 2026-09-10 01:05 | ARB-USDT-SWAP | 0.15051 | 0.15095/0.14914 | 0.15051 | — | 0.00425 | 0.0100% | — | sem_zona |
| 2026-09-10 01:05 | WLD-USDT-SWAP | 0.41510 | 0.41640/0.41290 | 0.41510 | res 0.46170 (ha 19 candles) | 0.00854 | -0.0006% | — | sem_zona |
| 2026-09-10 01:05 | SUI-USDT-SWAP | 0.76960 | 0.77230/0.76720 | 0.76960 | — | 0.01293 | 0.0100% | — | zona_mapeada_setup_B |
| 2026-09-10 01:05 | UNI-USDT-SWAP | 6.0710 | 6.1110/6.0100 | 6.0710 | sup 6.4750 (ha 12 candles) | 0.12850 | -0.0019% | — | zona_mapeada_setup_A |
| 2026-09-10 01:05 | LINK-USDT-SWAP | 11.81 | 11.87/11.78 | 11.81 | — | 0.14657 | 0.0040% | — | CONFIRMADO_setup_B |
| 2026-09-10 02:05 | BTC-USDT-SWAP | 78372.4 | 78411.9/78267.1 | 78297.4 | sup 77710.0 (ha 6 candles) | 447.93 | 0.0082% | — | zona_mapeada_setup_B |
| 2026-09-10 02:05 | ETH-USDT-SWAP | 2477.6 | 2479.9/2473.7 | 2474.2 | sup 2442.0 (ha 6 candles) | 17.56 | 0.0032% | — | zona_mapeada_setup_B |
| 2026-09-10 02:05 | SOL-USDT-SWAP | 101.93 | 102.24/101.72 | 101.77 | — | 1.00000 | -0.0067% | — | zona_mapeada_setup_B |
| 2026-09-10 02:05 | XRP-USDT-SWAP | 1.3879 | 1.3925/1.3863 | 1.3899 | — | 0.01303 | -0.0018% | — | zona_mapeada_setup_B |
| 2026-09-10 02:05 | DOGE-USDT-SWAP | 0.08573 | 0.08608/0.08568 | 0.08595 | sup 0.08450 (ha 6 candles) | 0.00107 | 0.0023% | — | zona_mapeada_setup_A |
| 2026-09-10 02:05 | ARB-USDT-SWAP | 0.15144 | 0.15196/0.14976 | 0.15051 | — | 0.00395 | 0.0100% | — | sem_zona |
| 2026-09-10 02:05 | WLD-USDT-SWAP | 0.41460 | 0.41860/0.41360 | 0.41510 | res 0.46170 (ha 20 candles) | 0.00847 | -0.0015% | — | sem_zona |
| 2026-09-10 02:05 | SUI-USDT-SWAP | 0.76920 | 0.77150/0.76700 | 0.76960 | — | 0.01259 | 0.0080% | — | zona_mapeada_setup_B |
| 2026-09-10 02:05 | UNI-USDT-SWAP | 6.0680 | 6.1160/6.0600 | 6.0710 | sup 5.9330 (ha 3 candles) | 0.12579 | -0.0004% | — | zona_expirada_setup_A |
| 2026-09-10 02:05 | LINK-USDT-SWAP | 11.81 | 11.83/11.79 | 11.81 | — | 0.13764 | 0.0056% | — | zona_mapeada_setup_B |
| 2026-09-10 03:05 | BTC-USDT-SWAP | 78497.2 | 78519.4/78238.5 | 78297.4 | sup 77710.0 (ha 7 candles) | 371.71 | 0.0084% | — | invalidado_setup_B |
| 2026-09-10 03:05 | ETH-USDT-SWAP | 2480.9 | 2482.8/2472.7 | 2474.2 | sup 2442.0 (ha 7 candles) | 15.19 | 0.0032% | — | zona_mapeada_setup_B |
| 2026-09-10 03:05 | SOL-USDT-SWAP | 102.05 | 102.14/101.53 | 101.77 | — | 0.89429 | -0.0058% | — | CONFIRMADO_setup_B |
| 2026-09-10 03:05 | XRP-USDT-SWAP | 1.3913 | 1.3925/1.3847 | 1.3899 | — | 0.01156 | -0.0008% | — | zona_mapeada_setup_B |
| 2026-09-10 03:05 | DOGE-USDT-SWAP | 0.08600 | 0.08617/0.08543 | 0.08595 | sup 0.08450 (ha 7 candles) | 0.00096 | 0.0040% | — | zona_expirada_setup_A |
| 2026-09-10 03:05 | ARB-USDT-SWAP | 0.15184 | 0.15325/0.15014 | 0.15051 | — | 0.00331 | 0.0100% | — | sem_zona |
| 2026-09-10 03:05 | WLD-USDT-SWAP | 0.41630 | 0.41750/0.41230 | 0.41510 | res 0.46170 (ha 21 candles) | 0.00754 | -0.0028% | — | sem_zona |
| 2026-09-10 03:05 | SUI-USDT-SWAP | 0.77080 | 0.77270/0.76510 | 0.76960 | — | 0.01082 | 0.0063% | — | zona_expirada_setup_B |
| 2026-09-10 03:05 | UNI-USDT-SWAP | 6.1000 | 6.1090/6.0350 | 6.0710 | sup 5.9330 (ha 4 candles) | 0.11757 | 0.0002% | — | sem_zona |
| 2026-09-10 03:05 | LINK-USDT-SWAP | 11.86 | 11.87/11.78 | 11.81 | — | 0.12143 | 0.0059% | — | zona_mapeada_setup_B |
| 2026-09-10 04:05 | BTC-USDT-SWAP | 78387.4 | 78505.2/78116.7 | 78297.4 | sup 77710.0 (ha 8 candles) | 365.46 | 0.0081% | — | zona_mapeada_setup_B |
| 2026-09-10 04:05 | ETH-USDT-SWAP | 2479.2 | 2483.7/2470.2 | 2474.2 | sup 2442.0 (ha 8 candles) | 15.10 | 0.0034% | — | zona_mapeada_setup_B |
| 2026-09-10 04:05 | SOL-USDT-SWAP | 101.87 | 102.10/101.34 | 101.77 | — | 0.89214 | -0.0049% | — | zona_mapeada_setup_B |
| 2026-09-10 04:05 | XRP-USDT-SWAP | 1.3883 | 1.3913/1.3812 | 1.3899 | — | 0.01141 | -0.0002% | — | zona_mapeada_setup_B |
| 2026-09-10 04:05 | DOGE-USDT-SWAP | 0.08575 | 0.08601/0.08538 | 0.08595 | sup 0.08450 (ha 8 candles) | 0.00094 | 0.0059% | — | zona_mapeada_setup_B |
| 2026-09-10 04:05 | ARB-USDT-SWAP | 0.15047 | 0.15186/0.14959 | 0.15051 | — | 0.00314 | 0.0100% | — | sem_zona |
| 2026-09-10 04:05 | WLD-USDT-SWAP | 0.41370 | 0.41630/0.40860 | 0.41510 | res 0.46170 (ha 22 candles) | 0.00754 | -0.0013% | — | sem_zona |
| 2026-09-10 04:05 | SUI-USDT-SWAP | 0.77120 | 0.77280/0.76350 | 0.76960 | — | 0.01057 | 0.0032% | — | zona_mapeada_setup_B |
| 2026-09-10 04:05 | UNI-USDT-SWAP | 6.0150 | 6.1060/5.9830 | 6.0710 | sup 5.9330 (ha 5 candles) | 0.11836 | 0.0011% | — | zona_mapeada_setup_B |
| 2026-09-10 04:05 | LINK-USDT-SWAP | 11.86 | 11.89/11.76 | 11.81 | — | 0.12236 | 0.0032% | — | zona_mapeada_setup_B |
| 2026-09-10 05:05 | BTC-USDT-SWAP | 78070.9 | 78392.9/77875.0 | 78070.9 | sup 77710.0 (ha 9 candles) | 383.36 | 0.0076% | — | descartado_rr_baixo_setup_B |
| 2026-09-10 05:05 | ETH-USDT-SWAP | 2471.8 | 2479.2/2462.5 | 2471.8 | sup 2442.0 (ha 9 candles) | 15.47 | 0.0035% | — | zona_mapeada_setup_B |
| 2026-09-10 05:05 | SOL-USDT-SWAP | 101.26 | 101.88/100.77 | 101.26 | — | 0.92714 | -0.0029% | — | zona_mapeada_setup_B |
| 2026-09-10 05:05 | XRP-USDT-SWAP | 1.3820 | 1.3883/1.3762 | 1.3820 | — | 0.01184 | 0.0002% | — | zona_mapeada_setup_B |
| 2026-09-10 05:05 | DOGE-USDT-SWAP | 0.08532 | 0.08575/0.08461 | 0.08532 | sup 0.08450 (ha 9 candles) | 0.00098 | 0.0072% | — | zona_mapeada_setup_B |
| 2026-09-10 05:05 | ARB-USDT-SWAP | 0.14949 | 0.15052/0.14801 | 0.14949 | — | 0.00301 | 0.0100% | — | sem_zona |
| 2026-09-10 05:06 | WLD-USDT-SWAP | 0.41060 | 0.41380/0.40740 | 0.41060 | res 0.41860 (ha 3 candles) | 0.00771 | 0.0030% | — | sem_zona |
| 2026-09-10 05:06 | SUI-USDT-SWAP | 0.76360 | 0.77120/0.76030 | 0.76360 | — | 0.01084 | 0.0020% | — | descartado_rr_baixo_setup_B |
| 2026-09-10 05:06 | UNI-USDT-SWAP | 5.9830 | 6.0230/5.9410 | 5.9830 | sup 5.9330 (ha 6 candles) | 0.12021 | 0.0040% | — | zona_mapeada_setup_B |
| 2026-09-10 05:06 | LINK-USDT-SWAP | 11.78 | 11.86/11.73 | 11.78 | — | 0.12636 | 0.0022% | — | CONFIRMADO_setup_B |
| 2026-09-10 06:05 | BTC-USDT-SWAP | 78077.8 | 78150.0/78001.0 | 78070.9 | sup 77710.0 (ha 10 candles) | 366.35 | 0.0071% | — | zona_mapeada_setup_B |
| 2026-09-10 06:05 | ETH-USDT-SWAP | 2470.4 | 2473.8/2468.2 | 2471.8 | sup 2442.0 (ha 10 candles) | 14.82 | 0.0034% | — | zona_mapeada_setup_B |
| 2026-09-10 06:05 | SOL-USDT-SWAP | 101.11 | 101.37/100.97 | 101.26 | — | 0.91571 | -0.0011% | — | zona_mapeada_setup_B |
| 2026-09-10 06:05 | XRP-USDT-SWAP | 1.3816 | 1.3840/1.3790 | 1.3820 | — | 0.01173 | 0.0037% | — | zona_mapeada_setup_B |
| 2026-09-10 06:05 | DOGE-USDT-SWAP | 0.08526 | 0.08551/0.08516 | 0.08532 | sup 0.08450 (ha 10 candles) | 0.00096 | 0.0086% | — | zona_mapeada_setup_B |
| 2026-09-10 06:05 | ARB-USDT-SWAP | 0.14902 | 0.15072/0.14881 | 0.14949 | — | 0.00301 | 0.0100% | — | sem_zona |
| 2026-09-10 06:05 | WLD-USDT-SWAP | 0.41040 | 0.41320/0.40930 | 0.41060 | res 0.41860 (ha 4 candles) | 0.00757 | 0.0038% | — | sem_zona |
| 2026-09-10 06:05 | SUI-USDT-SWAP | 0.76370 | 0.76590/0.76200 | 0.76360 | — | 0.01054 | 0.0047% | — | zona_mapeada_setup_B |
| 2026-09-10 06:05 | UNI-USDT-SWAP | 5.9890 | 6.0220/5.9630 | 5.9830 | sup 5.9330 (ha 7 candles) | 0.12121 | 0.0054% | — | zona_mapeada_setup_B |
| 2026-09-10 06:05 | LINK-USDT-SWAP | 11.77 | 11.79/11.75 | 11.78 | — | 0.12229 | 0.0034% | — | zona_mapeada_setup_B |
| 2026-09-10 07:05 | BTC-USDT-SWAP | 77967.5 | 78198.0/77888.0 | 78070.9 | sup 77710.0 (ha 11 candles) | 357.87 | 0.0079% | — | zona_mapeada_setup_B |
| 2026-09-10 07:05 | ETH-USDT-SWAP | 2467.7 | 2476.7/2463.5 | 2471.8 | sup 2442.0 (ha 11 candles) | 14.14 | 0.0036% | — | zona_mapeada_setup_B |
| 2026-09-10 07:05 | SOL-USDT-SWAP | 101.08 | 101.38/100.74 | 101.26 | — | 0.87429 | 0.0005% | — | zona_mapeada_setup_B |
| 2026-09-10 07:05 | XRP-USDT-SWAP | 1.3776 | 1.3841/1.3726 | 1.3820 | — | 0.01107 | 0.0059% | — | zona_mapeada_setup_B |
| 2026-09-10 07:05 | DOGE-USDT-SWAP | 0.08494 | 0.08535/0.08478 | 0.08532 | sup 0.08450 (ha 11 candles) | 0.00084 | 0.0100% | — | zona_mapeada_setup_B |
| 2026-09-10 07:05 | ARB-USDT-SWAP | 0.14943 | 0.14960/0.14786 | 0.14949 | — | 0.00284 | 0.0100% | — | sem_zona |
| 2026-09-10 07:05 | WLD-USDT-SWAP | 0.40770 | 0.41120/0.40510 | 0.41060 | res 0.41860 (ha 5 candles) | 0.00738 | 0.0066% | — | sem_zona |
| 2026-09-10 07:05 | SUI-USDT-SWAP | 0.76130 | 0.76640/0.75800 | 0.76360 | — | 0.00987 | 0.0052% | — | descartado_rr_baixo_setup_B |
| 2026-09-10 07:05 | UNI-USDT-SWAP | 6.0130 | 6.0340/5.9630 | 5.9830 | sup 5.9330 (ha 8 candles) | 0.11771 | 0.0070% | — | invalidado_setup_B |
| 2026-09-10 07:05 | LINK-USDT-SWAP | 11.80 | 11.83/11.76 | 11.78 | — | 0.11893 | 0.0024% | — | zona_mapeada_setup_B |
| 2026-09-10 08:05 | BTC-USDT-SWAP | 77832.2 | 78024.8/77788.0 | 78070.9 | sup 77710.0 (ha 12 candles) | 343.44 | 0.0095% | — | zona_mapeada_setup_B |
| 2026-09-10 08:05 | ETH-USDT-SWAP | 2463.4 | 2471.0/2461.8 | 2471.8 | sup 2442.0 (ha 12 candles) | 13.39 | 0.0044% | — | zona_mapeada_setup_B |
| 2026-09-10 08:05 | SOL-USDT-SWAP | 101.00 | 101.35/100.80 | 101.26 | — | 0.85143 | 0.0018% | — | zona_mapeada_setup_B |
| 2026-09-10 08:05 | XRP-USDT-SWAP | 1.3746 | 1.3803/1.3685 | 1.3820 | — | 0.01111 | 0.0079% | — | zona_mapeada_setup_B |
| 2026-09-10 08:05 | DOGE-USDT-SWAP | 0.08501 | 0.08540/0.08487 | 0.08532 | sup 0.08461 (ha 3 candles) | 0.00079 | 0.0100% | — | zona_mapeada_setup_B |
| 2026-09-10 08:05 | ARB-USDT-SWAP | 0.14778 | 0.15024/0.14756 | 0.14949 | — | 0.00285 | 0.0100% | — | zona_mapeada_setup_B |
| 2026-09-10 08:05 | WLD-USDT-SWAP | 0.40790 | 0.41050/0.40690 | 0.41060 | res 0.41860 (ha 6 candles) | 0.00723 | 0.0096% | — | sem_zona |
| 2026-09-10 08:06 | SUI-USDT-SWAP | 0.75860 | 0.76340/0.75180 | 0.76360 | — | 0.00986 | 0.0074% | — | zona_mapeada_setup_B |
| 2026-09-10 08:06 | UNI-USDT-SWAP | 5.9900 | 6.0420/5.9890 | 5.9830 | sup 5.9410 (ha 3 candles) | 0.10936 | 0.0070% | — | zona_mapeada_setup_B |
| 2026-09-10 08:06 | LINK-USDT-SWAP | 11.77 | 11.83/11.77 | 11.78 | — | 0.11050 | 0.0031% | — | descartado_rr_baixo_setup_B |
| 2026-09-10 09:05 | BTC-USDT-SWAP | 77805.1 | 78027.1/77640.6 | 77805.1 | sup 77710.0 (ha 13 candles) | 346.24 | 0.0094% | — | zona_mapeada_setup_B |
| 2026-09-10 09:05 | ETH-USDT-SWAP | 2461.1 | 2468.9/2456.9 | 2461.1 | — | 13.08 | 0.0060% | — | zona_mapeada_setup_B |
| 2026-09-10 09:05 | SOL-USDT-SWAP | 100.93 | 101.48/100.76 | 100.93 | sup 100.15 (ha 13 candles) | 0.84500 | 0.0021% | — | zona_mapeada_setup_B |
| 2026-09-10 09:05 | XRP-USDT-SWAP | 1.3757 | 1.3821/1.3718 | 1.3757 | — | 0.01099 | 0.0080% | — | zona_expirada_setup_B |
| 2026-09-10 09:05 | DOGE-USDT-SWAP | 0.08507 | 0.08548/0.08475 | 0.08507 | sup 0.08461 (ha 4 candles) | 0.00077 | 0.0089% | — | zona_mapeada_setup_B |
| 2026-09-10 09:05 | ARB-USDT-SWAP | 0.14810 | 0.14901/0.14725 | 0.14810 | — | 0.00282 | 0.0100% | — | invalidado_setup_B |
| 2026-09-10 09:05 | WLD-USDT-SWAP | 0.40900 | 0.41250/0.40660 | 0.40900 | res 0.41860 (ha 7 candles) | 0.00710 | 0.0100% | — | sem_zona |
| 2026-09-10 09:05 | SUI-USDT-SWAP | 0.75990 | 0.76590/0.75600 | 0.75990 | — | 0.00944 | 0.0074% | — | zona_mapeada_setup_B |
| 2026-09-10 09:05 | UNI-USDT-SWAP | 6.0150 | 6.0430/5.9710 | 6.0150 | sup 5.9410 (ha 4 candles) | 0.10507 | 0.0074% | — | invalidado_setup_B |
| 2026-09-10 09:05 | LINK-USDT-SWAP | 11.81 | 11.88/11.74 | 11.81 | sup 11.73 (ha 4 candles) | 0.11107 | 0.0022% | — | zona_mapeada_setup_B |
| 2026-09-10 10:05 | BTC-USDT-SWAP | 76868.3 | 77957.0/76607.1 | 77805.1 | sup 77710.0 (ha 14 candles) | 410.04 | 0.0100% | — | zona_mapeada_setup_B |
| 2026-09-10 10:05 | ETH-USDT-SWAP | 2413.7 | 2466.7/2406.0 | 2461.1 | — | 15.96 | 0.0053% | — | zona_expirada_setup_B |
| 2026-09-10 10:05 | SOL-USDT-SWAP | 98.87 | 101.48/98.30 | 100.93 | sup 100.15 (ha 14 candles) | 0.93000 | 0.0016% | — | zona_mapeada_setup_B |
| 2026-09-10 10:05 | XRP-USDT-SWAP | 1.3576 | 1.3810/1.3386 | 1.3757 | — | 0.01256 | 0.0061% | — | zona_mapeada_setup_B |
| 2026-09-10 10:05 | DOGE-USDT-SWAP | 0.08369 | 0.08547/0.08202 | 0.08507 | sup 0.08461 (ha 5 candles) | 0.00087 | 0.0065% | — | zona_mapeada_setup_B |
| 2026-09-10 10:05 | ARB-USDT-SWAP | 0.14809 | 0.14926/0.14554 | 0.14810 | — | 0.00286 | 0.0100% | — | zona_mapeada_setup_B |
| 2026-09-10 10:05 | WLD-USDT-SWAP | 0.40390 | 0.41120/0.39530 | 0.40900 | res 0.41860 (ha 8 candles) | 0.00711 | 0.0100% | — | sem_zona |
| 2026-09-10 10:05 | SUI-USDT-SWAP | 0.75020 | 0.76590/0.74070 | 0.75990 | — | 0.01001 | 0.0098% | — | descartado_rr_baixo_setup_B |
| 2026-09-10 10:05 | UNI-USDT-SWAP | 5.8800 | 6.0300/5.7820 | 6.0150 | sup 5.9410 (ha 5 candles) | 0.11000 | 0.0074% | — | zona_mapeada_setup_A |
| 2026-09-10 10:05 | LINK-USDT-SWAP | 11.61 | 11.84/11.46 | 11.81 | sup 11.73 (ha 5 candles) | 0.12514 | 0.0053% | — | descartado_rr_baixo_setup_B |
| 2026-09-10 11:05 | BTC-USDT-SWAP | 77136.8 | 77217.8/76711.8 | 77805.1 | sup 77710.0 (ha 15 candles) | 416.76 | 0.0100% | — | zona_mapeada_setup_B |
| 2026-09-10 11:05 | ETH-USDT-SWAP | 2433.6 | 2435.3/2404.0 | 2461.1 | — | 16.84 | 0.0009% | — | zona_mapeada_setup_B |
| 2026-09-10 11:05 | SOL-USDT-SWAP | 99.68 | 99.83/98.81 | 100.93 | sup 100.15 (ha 15 candles) | 0.92786 | 0.0004% | — | zona_mapeada_setup_B |
| 2026-09-10 11:06 | XRP-USDT-SWAP | 1.3635 | 1.3661/1.3480 | 1.3757 | — | 0.01304 | 0.0026% | — | CONFIRMADO_setup_B |
| 2026-09-10 11:06 | DOGE-USDT-SWAP | 0.08394 | 0.08415/0.08318 | 0.08507 | sup 0.08461 (ha 6 candles) | 0.00089 | 0.0062% | — | zona_mapeada_setup_B |
| 2026-09-10 11:06 | ARB-USDT-SWAP | 0.14951 | 0.15012/0.14711 | 0.14810 | — | 0.00265 | 0.0100% | — | invalidado_setup_B |
| 2026-09-10 11:06 | WLD-USDT-SWAP | 0.40490 | 0.40740/0.40170 | 0.40900 | res 0.41860 (ha 9 candles) | 0.00714 | 0.0083% | — | sem_zona |
| 2026-09-10 11:06 | SUI-USDT-SWAP | 0.75000 | 0.75470/0.74580 | 0.75990 | — | 0.01000 | 0.0100% | — | zona_mapeada_setup_B |
| 2026-09-10 11:06 | UNI-USDT-SWAP | 5.9280 | 5.9360/5.8480 | 6.0150 | sup 5.9410 (ha 6 candles) | 0.10736 | 0.0100% | — | zona_mapeada_setup_A |
| 2026-09-10 11:06 | LINK-USDT-SWAP | 11.70 | 11.72/11.58 | 11.81 | sup 11.73 (ha 6 candles) | 0.12457 | 0.0090% | — | zona_mapeada_setup_A |
| 2026-09-10 12:05 | BTC-USDT-SWAP | 77387.0 | 77399.9/76925.0 | 77805.1 | sup 77710.0 (ha 16 candles) | 429.31 | 0.0100% | — | zona_mapeada_setup_B |
| 2026-09-10 12:05 | ETH-USDT-SWAP | 2442.4 | 2443.0/2425.4 | 2461.1 | — | 17.42 | -0.0037% | — | CONFIRMADO_setup_B |
| 2026-09-10 12:05 | SOL-USDT-SWAP | 100.14 | 100.31/99.18 | 100.93 | sup 100.15 (ha 16 candles) | 0.95214 | -0.0016% | — | zona_expirada_setup_B |
| 2026-09-10 12:05 | XRP-USDT-SWAP | 1.3595 | 1.3680/1.3568 | 1.3757 | — | 0.01309 | 0.0001% | — | zona_mapeada_setup_B |
| 2026-09-10 12:05 | DOGE-USDT-SWAP | 0.08377 | 0.08425/0.08336 | 0.08507 | sup 0.08461 (ha 7 candles) | 0.00091 | 0.0022% | — | zona_expirada_setup_B |
| 2026-09-10 12:05 | ARB-USDT-SWAP | 0.15202 | 0.15378/0.14936 | 0.14810 | — | 0.00275 | 0.0100% | — | sem_zona |
| 2026-09-10 12:05 | WLD-USDT-SWAP | 0.40380 | 0.40770/0.40080 | 0.40900 | res 0.41860 (ha 10 candles) | 0.00674 | 0.0031% | — | sem_zona |
| 2026-09-10 12:05 | SUI-USDT-SWAP | 0.74720 | 0.75370/0.73570 | 0.75990 | — | 0.01061 | 0.0100% | — | zona_mapeada_setup_B |
| 2026-09-10 12:05 | UNI-USDT-SWAP | 5.9460 | 5.9730/5.8740 | 6.0150 | sup 5.9410 (ha 7 candles) | 0.10814 | 0.0100% | — | zona_mapeada_setup_A |
| 2026-09-10 12:05 | LINK-USDT-SWAP | 11.66 | 11.73/11.57 | 11.81 | sup 11.73 (ha 7 candles) | 0.12750 | 0.0098% | — | zona_mapeada_setup_A |
| 2026-09-10 13:05 | BTC-USDT-SWAP | 77221.1 | 77387.1/77056.0 | 77221.1 | sup 76607.1 (ha 3 candles) | 411.92 | 0.0096% | — | zona_mapeada_setup_B |
| 2026-09-10 13:05 | ETH-USDT-SWAP | 2440.1 | 2444.0/2431.0 | 2440.1 | — | 16.58 | -0.0063% | — | zona_mapeada_setup_B |
| 2026-09-10 13:05 | SOL-USDT-SWAP | 99.67 | 100.14/99.37 | 99.67 | sup 98.30 (ha 3 candles) | 0.90929 | -0.0033% | — | sem_zona |
| 2026-09-10 13:05 | XRP-USDT-SWAP | 1.3560 | 1.3601/1.3509 | 1.3560 | — | 0.01240 | -0.0013% | — | invalidado_setup_B |
| 2026-09-10 13:05 | DOGE-USDT-SWAP | 0.08367 | 0.08380/0.08324 | 0.08367 | sup 0.08202 (ha 3 candles) | 0.00087 | -0.0017% | — | zona_mapeada_setup_B |
| 2026-09-10 13:05 | ARB-USDT-SWAP | 0.14984 | 0.15345/0.14917 | 0.14984 | sup 0.14554 (ha 3 candles) | 0.00279 | 0.0100% | — | sem_zona |
| 2026-09-10 13:05 | WLD-USDT-SWAP | 0.40550 | 0.40610/0.40150 | 0.40550 | res 0.41860 (ha 11 candles) | 0.00644 | 0.0012% | — | sem_zona |
| 2026-09-10 13:05 | SUI-USDT-SWAP | 0.74430 | 0.74850/0.74010 | 0.74430 | — | 0.01009 | 0.0100% | — | zona_mapeada_setup_B |
| 2026-09-10 13:05 | UNI-USDT-SWAP | 5.9980 | 6.0070/5.8940 | 5.9980 | sup 5.7820 (ha 3 candles) | 0.09614 | 0.0100% | — | invalidado_setup_A |
| 2026-09-10 13:05 | LINK-USDT-SWAP | 11.63 | 11.69/11.59 | 11.63 | sup 11.46 (ha 3 candles) | 0.12271 | 0.0097% | — | zona_mapeada_setup_A |
| 2026-09-10 14:05 | BTC-USDT-SWAP | 77177.7 | 77282.3/76771.3 | 77221.1 | sup 76607.1 (ha 4 candles) | 419.20 | 0.0100% | — | zona_expirada_setup_B |
| 2026-09-10 14:05 | ETH-USDT-SWAP | 2447.5 | 2449.8/2431.0 | 2440.1 | — | 16.79 | -0.0092% | — | descartado_rr_baixo_setup_B |
| 2026-09-10 14:05 | SOL-USDT-SWAP | 99.62 | 99.86/98.78 | 99.67 | sup 98.30 (ha 4 candles) | 0.92143 | -0.0030% | — | sem_zona |
| 2026-09-10 14:05 | XRP-USDT-SWAP | 1.3537 | 1.3583/1.3419 | 1.3560 | — | 0.01271 | -0.0006% | — | zona_mapeada_setup_B |
| 2026-09-10 14:05 | DOGE-USDT-SWAP | 0.08350 | 0.08378/0.08256 | 0.08367 | sup 0.08202 (ha 4 candles) | 0.00090 | -0.0022% | — | zona_mapeada_setup_B |
| 2026-09-10 14:05 | ARB-USDT-SWAP | 0.14821 | 0.15050/0.14676 | 0.14984 | sup 0.14554 (ha 4 candles) | 0.00280 | 0.0100% | — | zona_mapeada_setup_B |
| 2026-09-10 14:05 | WLD-USDT-SWAP | 0.40170 | 0.40680/0.39670 | 0.40550 | res 0.41860 (ha 12 candles) | 0.00646 | 0.0014% | — | sem_zona |
| 2026-09-10 14:05 | SUI-USDT-SWAP | 0.74060 | 0.74530/0.73140 | 0.74430 | — | 0.01040 | 0.0100% | — | zona_mapeada_setup_B |
| 2026-09-10 14:05 | UNI-USDT-SWAP | 5.9920 | 6.0170/5.9030 | 5.9980 | sup 5.7820 (ha 4 candles) | 0.09664 | 0.0100% | — | zona_mapeada_setup_B |
| 2026-09-10 14:05 | LINK-USDT-SWAP | 11.61 | 11.64/11.48 | 11.63 | sup 11.46 (ha 4 candles) | 0.12329 | 0.0097% | — | zona_mapeada_setup_A |
| 2026-09-10 15:05 | BTC-USDT-SWAP | 77304.3 | 77519.9/77100.0 | 77221.1 | sup 76607.1 (ha 5 candles) | 429.09 | 0.0100% | — | sem_zona |
| 2026-09-10 15:05 | ETH-USDT-SWAP | 2464.8 | 2474.3/2445.6 | 2440.1 | — | 18.33 | -0.0088% | — | zona_mapeada_setup_B |
| 2026-09-10 15:05 | SOL-USDT-SWAP | 99.92 | 100.43/99.50 | 99.67 | sup 98.30 (ha 5 candles) | 0.95857 | -0.0016% | — | sem_zona |
| 2026-09-10 15:05 | XRP-USDT-SWAP | 1.3597 | 1.3645/1.3516 | 1.3560 | — | 0.01321 | 0.0015% | — | CONFIRMADO_setup_B |
| 2026-09-10 15:05 | DOGE-USDT-SWAP | 0.08384 | 0.08416/0.08336 | 0.08367 | sup 0.08202 (ha 5 candles) | 0.00093 | -0.0031% | — | zona_mapeada_setup_B |
| 2026-09-10 15:05 | ARB-USDT-SWAP | 0.15013 | 0.15059/0.14764 | 0.14984 | sup 0.14554 (ha 5 candles) | 0.00288 | 0.0100% | — | zona_mapeada_setup_B |
| 2026-09-10 15:05 | WLD-USDT-SWAP | 0.40470 | 0.40700/0.40090 | 0.40550 | res 0.41860 (ha 13 candles) | 0.00665 | 0.0019% | — | sem_zona |
| 2026-09-10 15:05 | SUI-USDT-SWAP | 0.74250 | 0.74770/0.73910 | 0.74430 | — | 0.01065 | 0.0100% | — | zona_expirada_setup_B |
| 2026-09-10 15:05 | UNI-USDT-SWAP | 6.0600 | 6.0870/5.9600 | 5.9980 | sup 5.7820 (ha 5 candles) | 0.09850 | 0.0100% | — | invalidado_setup_B |
| 2026-09-10 15:05 | LINK-USDT-SWAP | 11.67 | 11.73/11.60 | 11.63 | sup 11.46 (ha 5 candles) | 0.12629 | 0.0089% | — | zona_mapeada_setup_A |
| 2026-09-10 16:05 | BTC-USDT-SWAP | 77225.1 | 77320.0/76956.0 | 77221.1 | sup 76607.1 (ha 6 candles) | 444.74 | 0.0100% | — | sem_zona |
| 2026-09-10 16:05 | ETH-USDT-SWAP | 2467.1 | 2467.9/2453.2 | 2440.1 | — | 18.94 | -0.0075% | — | descartado_rr_baixo_setup_B |
| 2026-09-10 16:05 | SOL-USDT-SWAP | 99.87 | 99.95/99.15 | 99.67 | sup 98.30 (ha 6 candles) | 0.97857 | -0.0013% | — | sem_zona |
| 2026-09-10 16:05 | XRP-USDT-SWAP | 1.3553 | 1.3601/1.3467 | 1.3560 | — | 0.01373 | 0.0020% | — | zona_mapeada_setup_B |
| 2026-09-10 16:05 | DOGE-USDT-SWAP | 0.08395 | 0.08398/0.08321 | 0.08367 | sup 0.08202 (ha 6 candles) | 0.00095 | -0.0042% | — | zona_expirada_setup_B |
| 2026-09-10 16:05 | ARB-USDT-SWAP | 0.14988 | 0.15031/0.14839 | 0.14984 | sup 0.14554 (ha 6 candles) | 0.00286 | 0.0067% | — | zona_mapeada_setup_B |
| 2026-09-10 16:05 | WLD-USDT-SWAP | 0.40540 | 0.40620/0.40020 | 0.40550 | res 0.41860 (ha 14 candles) | 0.00672 | 0.0042% | — | sem_zona |
| 2026-09-10 16:05 | SUI-USDT-SWAP | 0.74110 | 0.74300/0.73520 | 0.74430 | — | 0.01089 | 0.0100% | — | zona_mapeada_setup_B |
| 2026-09-10 16:05 | UNI-USDT-SWAP | 6.0790 | 6.0960/5.9940 | 5.9980 | sup 5.7820 (ha 6 candles) | 0.10179 | 0.0100% | — | sem_zona |
| 2026-09-10 16:05 | LINK-USDT-SWAP | 11.67 | 11.69/11.59 | 11.63 | sup 11.46 (ha 6 candles) | 0.13079 | 0.0051% | — | zona_mapeada_setup_A |
| 2026-09-10 17:05 | BTC-USDT-SWAP | 77136.1 | 77279.6/77051.1 | 77136.1 | sup 76607.1 (ha 7 candles) | 441.00 | 0.0100% | — | sem_zona |
| 2026-09-10 17:05 | ETH-USDT-SWAP | 2461.5 | 2471.6/2459.3 | 2461.5 | — | 19.09 | -0.0047% | — | sem_zona_posicao_aberta |
| 2026-09-10 17:05 | SOL-USDT-SWAP | 99.63 | 100.07/99.53 | 99.63 | sup 98.78 (ha 3 candles) | 0.97357 | -0.0006% | — | sem_zona |
| 2026-09-10 17:05 | XRP-USDT-SWAP | 1.3502 | 1.3586/1.3491 | 1.3502 | — | 0.01385 | 0.0050% | — | zona_mapeada_setup_B |
| 2026-09-10 17:05 | DOGE-USDT-SWAP | 0.08388 | 0.08430/0.08375 | 0.08388 | sup 0.08256 (ha 3 candles) | 0.00094 | -0.0032% | — | zona_mapeada_setup_B |
| 2026-09-10 17:05 | ARB-USDT-SWAP | 0.14744 | 0.14988/0.14734 | 0.14744 | sup 0.14676 (ha 3 candles) | 0.00282 | 0.0010% | — | invalidado_setup_B |
| 2026-09-10 17:05 | WLD-USDT-SWAP | 0.40110 | 0.40540/0.40000 | 0.40110 | res 0.41860 (ha 15 candles) | 0.00674 | 0.0054% | — | sem_zona |
| 2026-09-10 17:05 | SUI-USDT-SWAP | 0.73830 | 0.74110/0.73470 | 0.73830 | — | 0.01080 | 0.0066% | — | zona_mapeada_setup_B |
| 2026-09-10 17:05 | UNI-USDT-SWAP | 6.0750 | 6.0990/6.0370 | 6.0750 | sup 5.7820 (ha 7 candles) | 0.10093 | 0.0100% | — | sem_zona |
| 2026-09-10 17:05 | LINK-USDT-SWAP | 11.61 | 11.67/11.60 | 11.61 | sup 11.48 (ha 3 candles) | 0.12893 | 0.0017% | — | zona_mapeada_setup_A |
| 2026-09-10 18:05 | BTC-USDT-SWAP | 77242.8 | 77323.5/77080.0 | 77136.1 | sup 76607.1 (ha 8 candles) | 430.64 | 0.0100% | — | sem_zona |
| 2026-09-10 18:05 | ETH-USDT-SWAP | 2460.6 | 2467.9/2459.8 | 2461.5 | — | 18.71 | -0.0019% | — | sem_zona_posicao_aberta |
| 2026-09-10 18:05 | SOL-USDT-SWAP | 99.99 | 100.09/99.57 | 99.63 | sup 98.78 (ha 4 candles) | 0.95643 | -0.0003% | — | sem_zona |
| 2026-09-10 18:05 | XRP-USDT-SWAP | 1.3534 | 1.3573/1.3498 | 1.3502 | — | 0.01366 | 0.0086% | — | zona_mapeada_setup_B |
| 2026-09-10 18:05 | DOGE-USDT-SWAP | 0.08412 | 0.08429/0.08384 | 0.08388 | sup 0.08256 (ha 4 candles) | 0.00093 | -0.0035% | — | zona_mapeada_setup_B |
| 2026-09-10 18:05 | ARB-USDT-SWAP | 0.14813 | 0.14884/0.14665 | 0.14744 | sup 0.14676 (ha 4 candles) | 0.00281 | -0.0035% | — | sem_zona |
| 2026-09-10 18:05 | WLD-USDT-SWAP | 0.40240 | 0.40460/0.40070 | 0.40110 | res 0.41860 (ha 16 candles) | 0.00646 | 0.0046% | — | sem_zona |
| 2026-09-10 18:05 | SUI-USDT-SWAP | 0.74020 | 0.74260/0.73560 | 0.73830 | — | 0.01064 | -0.0011% | — | zona_mapeada_setup_B |
| 2026-09-10 18:05 | UNI-USDT-SWAP | 6.0650 | 6.1030/6.0610 | 6.0750 | sup 5.7820 (ha 8 candles) | 0.09514 | 0.0100% | — | sem_zona |
| 2026-09-10 18:05 | LINK-USDT-SWAP | 11.59 | 11.64/11.58 | 11.61 | sup 11.48 (ha 4 candles) | 0.12429 | -0.0001% | — | zona_mapeada_setup_A |
| 2026-09-10 18:35 | BTC-USDT-SWAP | 77242.8 | 77323.5/77080.0 | 77136.1 | sup 76607.1 (ha 8 candles) | 430.64 | 0.0100% | — | sem_zona |
| 2026-09-10 18:35 | ETH-USDT-SWAP | 2460.6 | 2467.9/2459.8 | 2461.5 | — | 18.71 | -0.0006% | — | sem_zona_posicao_aberta |
| 2026-09-10 18:35 | SOL-USDT-SWAP | 99.99 | 100.09/99.57 | 99.63 | sup 98.78 (ha 4 candles) | 0.95643 | -0.0002% | — | sem_zona |
| 2026-09-10 18:35 | XRP-USDT-SWAP | 1.3534 | 1.3573/1.3498 | 1.3502 | — | 0.01366 | 0.0090% | B/compra@1.3623 (0t/2c) | zona_mapeada_setup_B |
| 2026-09-10 18:35 | DOGE-USDT-SWAP | 0.08412 | 0.08429/0.08384 | 0.08388 | sup 0.08256 (ha 4 candles) | 0.00093 | -0.0034% | B/venda@0.08394 (2t/0c) | zona_mapeada_setup_B |
| 2026-09-10 18:35 | ARB-USDT-SWAP | 0.14813 | 0.14884/0.14665 | 0.14744 | sup 0.14676 (ha 4 candles) | 0.00281 | -0.0037% | — | sem_zona |
| 2026-09-10 18:35 | WLD-USDT-SWAP | 0.40240 | 0.40460/0.40070 | 0.40110 | res 0.41860 (ha 16 candles) | 0.00646 | 0.0044% | — | sem_zona |
| 2026-09-10 18:35 | SUI-USDT-SWAP | 0.74020 | 0.74260/0.73560 | 0.73830 | — | 0.01064 | -0.0039% | — | zona_expirada_setup_B |
| 2026-09-10 18:35 | UNI-USDT-SWAP | 6.0650 | 6.1030/6.0610 | 6.0750 | sup 5.7820 (ha 8 candles) | 0.09514 | 0.0100% | — | sem_zona |
| 2026-09-10 18:35 | LINK-USDT-SWAP | 11.59 | 11.64/11.58 | 11.61 | sup 11.48 (ha 4 candles) | 0.12429 | -0.0013% | A/venda@11.73 (2t/7c) | zona_mapeada_setup_A |
| 2026-09-10 18:35 | BTC-USDT-SWAP | 77242.8 | 77323.5/77080.0 | 77136.1 | sup 76607.1 (ha 8 candles) | 430.64 | 0.0100% | — | sem_zona |
| 2026-09-10 18:35 | ETH-USDT-SWAP | 2460.6 | 2467.9/2459.8 | 2461.5 | — | 18.71 | -0.0006% | — | sem_zona_posicao_aberta |
| 2026-09-10 18:35 | SOL-USDT-SWAP | 99.99 | 100.09/99.57 | 99.63 | sup 98.78 (ha 4 candles) | 0.95643 | -0.0002% | — | sem_zona |
| 2026-09-10 18:35 | XRP-USDT-SWAP | 1.3534 | 1.3573/1.3498 | 1.3502 | — | 0.01366 | 0.0090% | B/compra@1.3623 (0t/2c) | zona_mapeada_setup_B |
| 2026-09-10 18:35 | DOGE-USDT-SWAP | 0.08412 | 0.08429/0.08384 | 0.08388 | sup 0.08256 (ha 4 candles) | 0.00093 | -0.0034% | B/venda@0.08394 (2t/0c) | zona_mapeada_setup_B |
| 2026-09-10 18:36 | ARB-USDT-SWAP | 0.14813 | 0.14884/0.14665 | 0.14744 | sup 0.14676 (ha 4 candles) | 0.00281 | -0.0037% | — | sem_zona |
| 2026-09-10 18:36 | WLD-USDT-SWAP | 0.40240 | 0.40460/0.40070 | 0.40110 | res 0.41860 (ha 16 candles) | 0.00646 | 0.0044% | — | sem_zona |
| 2026-09-10 18:36 | SUI-USDT-SWAP | 0.74020 | 0.74260/0.73560 | 0.73830 | — | 0.01064 | -0.0039% | — | zona_expirada_setup_B |
| 2026-09-10 18:36 | UNI-USDT-SWAP | 6.0650 | 6.1030/6.0610 | 6.0750 | sup 5.7820 (ha 8 candles) | 0.09514 | 0.0100% | — | sem_zona |
| 2026-09-10 18:36 | LINK-USDT-SWAP | 11.59 | 11.64/11.58 | 11.61 | sup 11.48 (ha 4 candles) | 0.12429 | -0.0013% | A/venda@11.73 (2t/7c) | zona_mapeada_setup_A |
| 2026-09-10 19:05 | BTC-USDT-SWAP | 77120.9 | 77271.2/77077.1 | 77136.1 | sup 76607.1 (ha 9 candles) | 407.51 | 0.0100% | — | sem_zona |
| 2026-09-10 19:05 | ETH-USDT-SWAP | 2459.2 | 2462.0/2456.2 | 2461.5 | — | 17.93 | 0.0007% | — | sem_zona_posicao_aberta |
| 2026-09-10 19:05 | SOL-USDT-SWAP | 99.76 | 100.09/99.70 | 99.63 | sup 98.78 (ha 5 candles) | 0.90500 | 0.0005% | — | sem_zona |
| 2026-09-10 19:05 | XRP-USDT-SWAP | 1.3512 | 1.3562/1.3492 | 1.3502 | — | 0.01330 | 0.0093% | B/compra@1.3623 (0t/3c) | zona_mapeada_setup_B |
| 2026-09-10 19:05 | DOGE-USDT-SWAP | 0.08403 | 0.08424/0.08391 | 0.08388 | sup 0.08256 (ha 5 candles) | 0.00087 | -0.0021% | — | CONFIRMADO_setup_B |
| 2026-09-10 19:05 | ARB-USDT-SWAP | 0.14646 | 0.14851/0.14583 | 0.14744 | sup 0.14676 (ha 5 candles) | 0.00282 | -0.0028% | — | sem_zona |
| 2026-09-10 19:05 | WLD-USDT-SWAP | 0.40220 | 0.40370/0.40060 | 0.40110 | res 0.41860 (ha 17 candles) | 0.00623 | 0.0052% | — | sem_zona |
| 2026-09-10 19:05 | SUI-USDT-SWAP | 0.73810 | 0.74210/0.73710 | 0.73830 | — | 0.01021 | -0.0052% | B/compra@0.73760 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-10 19:05 | UNI-USDT-SWAP | 6.0060 | 6.0680/5.9960 | 6.0750 | sup 5.7820 (ha 9 candles) | 0.09443 | 0.0100% | B/venda@5.9670 (0t/0c) | zona_mapeada_setup_B |
| 2026-09-10 19:05 | LINK-USDT-SWAP | 11.58 | 11.61/11.55 | 11.61 | sup 11.48 (ha 5 candles) | 0.11936 | -0.0024% | — | zona_expirada_setup_A |
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
