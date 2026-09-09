# Log de Monitoramento Automatico -- Multi-Par (script gratuito, GitHub Actions)

> Gerado por script Python sem LLM (ver monitor/fetch_and_check.py). Fonte: OKX. Cobre os pares em PAIRS (configuracao no topo do script) -- BTC-USDT-SWAP e os demais adicionados na expansao de 07/09/2026. Leitura e MECANICA (regras objetivas da secao 4 do plano), sem a prosa qualitativa que o Claude gerava -- cole este log numa conversa do Claude se quiser a leitura interpretativa.

| Data/Hora (BRT) | Par | Close 1h | High/Low 1h | Close 4h | Swing 1h ref | ATR 1h | Funding | Status checklist |
|---|---|---|---|---|---|---|---|---|
| 2026-09-07 19:06 | BTC-USDT-SWAP | 79120.0 | 79241.5/79118.3 | 79324.2 | res 79611.0 (ha 8 candles) | 254.6 | 0.0039% | zona_expirada_setup_B |
| 2026-09-07 19:06 | ETH-USDT-SWAP | 2490.0 | 2496.1/2489.0 | 2495.0 | res 2498.8 (ha 4 candles) | 13.4 | 0.0091% | CONFIRMADO_setup_B |
| 2026-09-07 19:06 | SOL-USDT-SWAP | 103.8 | 104.1/103.7 | 104.3 | res 105.9 (ha 9 candles) | 0.7 | -0.0003% | invalidado_setup_B |
| 2026-09-07 19:06 | XRP-USDT-SWAP | 1.4 | 1.4/1.4 | 1.4 | — | 0.0 | 0.0049% | CONFIRMADO_setup_B |
| 2026-09-07 19:06 | DOGE-USDT-SWAP | 0.1 | 0.1/0.1 | 0.1 | res 0.1 (ha 8 candles) | 0.0 | 0.0100% | invalidado_setup_B |
| 2026-09-07 19:06 | ARB-USDT-SWAP | 0.2 | 0.2/0.2 | 0.2 | res 0.2 (ha 7 candles) | 0.0 | 0.0072% | sem_zona |
| 2026-09-07 19:06 | WLD-USDT-SWAP | 0.5 | 0.5/0.5 | 0.5 | — | 0.0 | 0.0100% | sem_zona |
| 2026-09-07 19:06 | SUI-USDT-SWAP | 0.8 | 0.8/0.8 | 0.8 | res 0.8 (ha 9 candles) | 0.0 | 0.0100% | zona_mapeada_setup_B |
| 2026-09-07 19:06 | UNI-USDT-SWAP | 6.9 | 7.0/6.9 | 6.9 | — | 0.1 | 0.0100% | sem_zona |
| 2026-09-07 19:06 | LINK-USDT-SWAP | 12.7 | 12.8/12.7 | 12.8 | res 13.7 (ha 15 candles) | 0.2 | -0.0017% | sem_zona |
| 2026-09-07 19:48 | BTC-USDT-SWAP | 79120.0 | 79241.5/79118.3 | 79324.2 | res 79611.0 (ha 8 candles) | 254.6 | 0.0036% | zona_mapeada_setup_B |
| 2026-09-07 19:48 | ETH-USDT-SWAP | 2490.0 | 2496.1/2489.0 | 2495.0 | res 2498.8 (ha 4 candles) | 13.4 | 0.0076% | zona_mapeada_setup_B |
| 2026-09-07 19:48 | SOL-USDT-SWAP | 103.8 | 104.1/103.7 | 104.3 | res 105.9 (ha 9 candles) | 0.7 | 0.0000% | zona_mapeada_setup_B |
| 2026-09-07 19:48 | XRP-USDT-SWAP | 1.4 | 1.4/1.4 | 1.4 | — | 0.0 | 0.0059% | zona_mapeada_setup_B |
| 2026-09-07 19:48 | DOGE-USDT-SWAP | 0.1 | 0.1/0.1 | 0.1 | res 0.1 (ha 8 candles) | 0.0 | 0.0100% | zona_mapeada_setup_B |
| 2026-09-07 19:48 | ARB-USDT-SWAP | 0.2 | 0.2/0.2 | 0.2 | res 0.2 (ha 7 candles) | 0.0 | 0.0068% | sem_zona |
| 2026-09-07 19:48 | WLD-USDT-SWAP | 0.5 | 0.5/0.5 | 0.5 | — | 0.0 | 0.0100% | sem_zona |
| 2026-09-07 19:48 | SUI-USDT-SWAP | 0.8 | 0.8/0.8 | 0.8 | res 0.8 (ha 9 candles) | 0.0 | 0.0100% | zona_mapeada_setup_B |
| 2026-09-07 19:48 | UNI-USDT-SWAP | 6.9 | 7.0/6.9 | 6.9 | — | 0.1 | 0.0100% | sem_zona |
| 2026-09-07 19:48 | LINK-USDT-SWAP | 12.7 | 12.8/12.7 | 12.8 | res 13.7 (ha 15 candles) | 0.2 | -0.0008% | sem_zona |
| 2026-09-07 19:49 | BTC-USDT-SWAP | 79120.0 | 79241.5/79118.3 | 79324.2 | res 79611.0 (ha 8 candles) | 254.6 | 0.0036% | CONFIRMADO_setup_B |
| 2026-09-07 19:49 | ETH-USDT-SWAP | 2490.0 | 2496.1/2489.0 | 2495.0 | res 2498.8 (ha 4 candles) | 13.4 | 0.0075% | CONFIRMADO_setup_B |
| 2026-09-07 19:49 | SOL-USDT-SWAP | 103.8 | 104.1/103.7 | 104.3 | res 105.9 (ha 9 candles) | 0.7 | -0.0000% | invalidado_setup_B |
| 2026-09-07 19:49 | XRP-USDT-SWAP | 1.4 | 1.4/1.4 | 1.4 | — | 0.0 | 0.0059% | CONFIRMADO_setup_B |
| 2026-09-07 19:49 | DOGE-USDT-SWAP | 0.1 | 0.1/0.1 | 0.1 | res 0.1 (ha 8 candles) | 0.0 | 0.0100% | zona_mapeada_setup_B |
| 2026-09-07 19:49 | ARB-USDT-SWAP | 0.2 | 0.2/0.2 | 0.2 | res 0.2 (ha 7 candles) | 0.0 | 0.0067% | sem_zona |
| 2026-09-07 19:49 | WLD-USDT-SWAP | 0.5 | 0.5/0.5 | 0.5 | — | 0.0 | 0.0100% | sem_zona |
| 2026-09-07 19:49 | SUI-USDT-SWAP | 0.8 | 0.8/0.8 | 0.8 | res 0.8 (ha 9 candles) | 0.0 | 0.0100% | zona_mapeada_setup_B |
| 2026-09-07 19:49 | UNI-USDT-SWAP | 6.9 | 7.0/6.9 | 6.9 | — | 0.1 | 0.0100% | sem_zona |
| 2026-09-07 19:49 | LINK-USDT-SWAP | 12.7 | 12.8/12.7 | 12.8 | res 13.7 (ha 15 candles) | 0.2 | -0.0007% | sem_zona |
| 2026-09-07 20:05 | BTC-USDT-SWAP | 78911.7 | 79180.0/78704.4 | 79324.2 | res 79383.4 (ha 3 candles) | 277.3 | 0.0037% | sem_zona |
| 2026-09-07 20:05 | ETH-USDT-SWAP | 2481.6 | 2491.1/2473.6 | 2495.0 | res 2498.8 (ha 5 candles) | 14.2 | 0.0070% | zona_mapeada_setup_B |
| 2026-09-07 20:05 | SOL-USDT-SWAP | 103.5 | 104.0/103.1 | 104.3 | res 104.4 (ha 3 candles) | 0.8 | 0.0002% | zona_mapeada_setup_B |
| 2026-09-07 20:05 | XRP-USDT-SWAP | 1.4 | 1.4/1.4 | 1.4 | — | 0.0 | 0.0057% | zona_mapeada_setup_B |
| 2026-09-07 20:05 | DOGE-USDT-SWAP | 0.1 | 0.1/0.1 | 0.1 | res 0.1 (ha 9 candles) | 0.0 | 0.0100% | zona_mapeada_setup_B |
| 2026-09-07 20:05 | ARB-USDT-SWAP | 0.2 | 0.2/0.2 | 0.2 | res 0.2 (ha 8 candles) | 0.0 | 0.0070% | sem_zona |
| 2026-09-07 20:05 | WLD-USDT-SWAP | 0.5 | 0.5/0.5 | 0.5 | — | 0.0 | 0.0098% | sem_zona |
| 2026-09-07 20:05 | SUI-USDT-SWAP | 0.8 | 0.8/0.8 | 0.8 | res 0.8 (ha 10 candles) | 0.0 | 0.0100% | zona_mapeada_setup_B |
| 2026-09-07 20:05 | UNI-USDT-SWAP | 6.8 | 6.9/6.7 | 6.9 | — | 0.1 | 0.0100% | sem_zona |
| 2026-09-07 20:05 | LINK-USDT-SWAP | 12.7 | 12.8/12.6 | 12.8 | res 13.7 (ha 16 candles) | 0.2 | -0.0006% | sem_zona |
| 2026-09-07 21:05 | BTC-USDT-SWAP | 79074.5 | 79176.5/78891.1 | 79074.5 | res 79383.4 (ha 4 candles) | 278.4 | 0.0029% | zona_mapeada_setup_B |
| 2026-09-07 21:05 | ETH-USDT-SWAP | 2489.0 | 2492.9/2480.9 | 2489.0 | res 2498.8 (ha 6 candles) | 14.1 | 0.0049% | zona_mapeada_setup_B |
| 2026-09-07 21:05 | SOL-USDT-SWAP | 103.7 | 104.0/103.4 | 103.7 | res 104.4 (ha 4 candles) | 0.7 | 0.0006% | zona_mapeada_setup_B |
| 2026-09-07 21:05 | XRP-USDT-SWAP | 1.4 | 1.4/1.4 | 1.4 | — | 0.0 | 0.0059% | zona_mapeada_setup_B |
| 2026-09-07 21:05 | DOGE-USDT-SWAP | 0.1 | 0.1/0.1 | 0.1 | res 0.1 (ha 3 candles) | 0.0 | 0.0100% | invalidado_setup_B |
| 2026-09-07 21:05 | ARB-USDT-SWAP | 0.2 | 0.2/0.2 | 0.2 | res 0.2 (ha 9 candles) | 0.0 | 0.0075% | sem_zona |
| 2026-09-07 21:05 | WLD-USDT-SWAP | 0.5 | 0.5/0.5 | 0.5 | — | 0.0 | 0.0078% | sem_zona |
| 2026-09-07 21:05 | SUI-USDT-SWAP | 0.8 | 0.8/0.8 | 0.8 | res 0.8 (ha 3 candles) | 0.0 | 0.0100% | invalidado_setup_B |
| 2026-09-07 21:05 | UNI-USDT-SWAP | 6.9 | 6.9/6.8 | 6.9 | — | 0.1 | 0.0100% | sem_zona |
| 2026-09-07 21:05 | LINK-USDT-SWAP | 12.7 | 12.8/12.7 | 12.7 | res 13.7 (ha 17 candles) | 0.2 | -0.0002% | sem_zona |
| 2026-09-07 22:05 | BTC-USDT-SWAP | 79278.4 | 79278.5/78925.0 | 79074.5 | res 79383.4 (ha 5 candles) | 293.5 | 0.0027% | zona_mapeada_setup_B |
| 2026-09-07 22:05 | ETH-USDT-SWAP | 2495.0 | 2495.0/2482.1 | 2489.0 | res 2498.8 (ha 7 candles) | 14.5 | 0.0038% | invalidado_setup_B |
| 2026-09-07 22:05 | SOL-USDT-SWAP | 104.0 | 104.1/103.4 | 103.7 | res 104.4 (ha 5 candles) | 0.8 | 0.0002% | invalidado_setup_B |
| 2026-09-07 22:05 | XRP-USDT-SWAP | 1.4 | 1.4/1.4 | 1.4 | — | 0.0 | 0.0056% | zona_mapeada_setup_B |
| 2026-09-07 22:05 | DOGE-USDT-SWAP | 0.1 | 0.1/0.1 | 0.1 | res 0.1 (ha 4 candles) | 0.0 | 0.0090% | zona_mapeada_setup_A |
| 2026-09-07 22:05 | ARB-USDT-SWAP | 0.2 | 0.2/0.2 | 0.2 | res 0.2 (ha 3 candles) | 0.0 | 0.0067% | sem_zona |
| 2026-09-07 22:05 | WLD-USDT-SWAP | 0.5 | 0.5/0.5 | 0.5 | — | 0.0 | 0.0097% | sem_zona |
| 2026-09-07 22:05 | SUI-USDT-SWAP | 0.8 | 0.8/0.8 | 0.8 | res 0.8 (ha 4 candles) | 0.0 | 0.0100% | sem_zona |
| 2026-09-07 22:05 | UNI-USDT-SWAP | 6.9 | 6.9/6.8 | 6.9 | — | 0.1 | 0.0100% | sem_zona |
| 2026-09-07 22:05 | LINK-USDT-SWAP | 12.8 | 12.8/12.7 | 12.7 | res 13.7 (ha 18 candles) | 0.2 | 0.0003% | sem_zona |
| 2026-09-07 23:05 | BTC-USDT-SWAP | 79402.4 | 79430.8/79225.5 | 79074.5 | res 79383.4 (ha 6 candles) | 292.7 | 0.0024% | invalidado_setup_B |
| 2026-09-07 23:05 | ETH-USDT-SWAP | 2503.2 | 2505.3/2492.4 | 2489.0 | res 2498.8 (ha 8 candles) | 14.9 | 0.0039% | zona_mapeada_setup_A |
| 2026-09-07 23:05 | SOL-USDT-SWAP | 104.3 | 104.4/103.9 | 103.7 | res 104.4 (ha 6 candles) | 0.8 | -0.0003% | sem_zona |
| 2026-09-07 23:05 | XRP-USDT-SWAP | 1.4 | 1.4/1.4 | 1.4 | — | 0.0 | 0.0061% | zona_mapeada_setup_B |
| 2026-09-07 23:05 | DOGE-USDT-SWAP | 0.1 | 0.1/0.1 | 0.1 | res 0.1 (ha 5 candles) | 0.0 | 0.0066% | zona_mapeada_setup_A |
| 2026-09-07 23:05 | ARB-USDT-SWAP | 0.2 | 0.2/0.2 | 0.2 | res 0.2 (ha 4 candles) | 0.0 | 0.0100% | sem_zona |
| 2026-09-07 23:05 | WLD-USDT-SWAP | 0.5 | 0.5/0.5 | 0.5 | — | 0.0 | 0.0099% | sem_zona |
| 2026-09-07 23:05 | SUI-USDT-SWAP | 0.8 | 0.8/0.8 | 0.8 | res 0.8 (ha 5 candles) | 0.0 | 0.0100% | sem_zona |
| 2026-09-07 23:05 | UNI-USDT-SWAP | 7.1 | 7.1/6.9 | 6.9 | — | 0.1 | 0.0100% | sem_zona |
| 2026-09-07 23:05 | LINK-USDT-SWAP | 12.8 | 12.8/12.7 | 12.7 | res 13.7 (ha 19 candles) | 0.2 | -0.0000% | sem_zona |
| 2026-09-08 00:05 | BTC-USDT-SWAP | 78893.9 | 79454.0/78893.9 | 79074.5 | res 79383.4 (ha 7 candles) | 316.6 | 0.0021% | sem_zona |
| 2026-09-08 00:05 | ETH-USDT-SWAP | 2483.5 | 2507.4/2483.4 | 2489.0 | res 2498.8 (ha 9 candles) | 15.2 | 0.0038% | invalidado_setup_A |
| 2026-09-08 00:05 | SOL-USDT-SWAP | 103.2 | 104.5/103.2 | 103.7 | res 104.4 (ha 7 candles) | 0.8 | -0.0011% | zona_mapeada_setup_B |
| 2026-09-08 00:05 | XRP-USDT-SWAP | 1.4 | 1.4/1.4 | 1.4 | — | 0.0 | 0.0059% | zona_mapeada_setup_B |
| 2026-09-08 00:05 | DOGE-USDT-SWAP | 0.1 | 0.1/0.1 | 0.1 | res 0.1 (ha 6 candles) | 0.0 | 0.0053% | invalidado_setup_A |
| 2026-09-08 00:05 | ARB-USDT-SWAP | 0.2 | 0.2/0.2 | 0.2 | res 0.2 (ha 5 candles) | 0.0 | 0.0100% | sem_zona |
| 2026-09-08 00:05 | WLD-USDT-SWAP | 0.5 | 0.5/0.5 | 0.5 | — | 0.0 | 0.0100% | sem_zona |
| 2026-09-08 00:05 | SUI-USDT-SWAP | 0.8 | 0.8/0.8 | 0.8 | res 0.8 (ha 6 candles) | 0.0 | 0.0100% | zona_mapeada_setup_B |
| 2026-09-08 00:05 | UNI-USDT-SWAP | 7.0 | 7.2/6.9 | 6.9 | — | 0.1 | 0.0100% | sem_zona |
| 2026-09-08 00:05 | LINK-USDT-SWAP | 12.6 | 12.8/12.6 | 12.7 | res 13.7 (ha 20 candles) | 0.2 | -0.0013% | zona_mapeada_setup_B |
| 2026-09-08 01:05 | BTC-USDT-SWAP | 78877.0 | 78976.7/78681.4 | 78877.0 | — | 312.9 | 0.0024% | sem_zona |
| 2026-09-08 01:05 | ETH-USDT-SWAP | 2485.1 | 2487.6/2476.5 | 2485.1 | res 2498.8 (ha 10 candles) | 14.7 | 0.0046% | zona_mapeada_setup_B |
| 2026-09-08 01:05 | SOL-USDT-SWAP | 103.3 | 103.4/102.6 | 103.3 | res 104.4 (ha 8 candles) | 0.8 | -0.0015% | zona_mapeada_setup_B |
| 2026-09-08 01:05 | XRP-USDT-SWAP | 1.4 | 1.4/1.4 | 1.4 | — | 0.0 | 0.0057% | zona_mapeada_setup_B |
| 2026-09-08 01:05 | DOGE-USDT-SWAP | 0.1 | 0.1/0.1 | 0.1 | — | 0.0 | 0.0037% | zona_mapeada_setup_B |
| 2026-09-08 01:05 | ARB-USDT-SWAP | 0.2 | 0.2/0.2 | 0.2 | res 0.2 (ha 6 candles) | 0.0 | 0.0100% | sem_zona |
| 2026-09-08 01:05 | WLD-USDT-SWAP | 0.5 | 0.5/0.5 | 0.5 | — | 0.0 | 0.0100% | sem_zona |
| 2026-09-08 01:05 | SUI-USDT-SWAP | 0.8 | 0.8/0.8 | 0.8 | res 0.8 (ha 7 candles) | 0.0 | 0.0100% | invalidado_setup_B |
| 2026-09-08 01:05 | UNI-USDT-SWAP | 7.0 | 7.0/7.0 | 7.0 | — | 0.1 | 0.0100% | sem_zona |
| 2026-09-08 01:05 | LINK-USDT-SWAP | 12.7 | 12.7/12.6 | 12.7 | res 13.7 (ha 21 candles) | 0.2 | -0.0017% | zona_mapeada_setup_B |
| 2026-09-08 02:05 | BTC-USDT-SWAP | 78644.1 | 78900.0/78622.5 | 78877.0 | — | 301.4 | 0.0034% | zona_mapeada_setup_B |
| 2026-09-08 02:05 | ETH-USDT-SWAP | 2478.2 | 2485.5/2478.0 | 2485.1 | res 2498.8 (ha 11 candles) | 13.6 | 0.0057% | zona_mapeada_setup_B |
| 2026-09-08 02:05 | SOL-USDT-SWAP | 102.9 | 103.4/102.9 | 103.3 | res 104.4 (ha 9 candles) | 0.7 | -0.0027% | CONFIRMADO_setup_B |
| 2026-09-08 02:05 | XRP-USDT-SWAP | 1.4 | 1.4/1.4 | 1.4 | — | 0.0 | 0.0060% | zona_mapeada_setup_B |
| 2026-09-08 02:05 | DOGE-USDT-SWAP | 0.1 | 0.1/0.1 | 0.1 | — | 0.0 | 0.0017% | CONFIRMADO_setup_B |
| 2026-09-08 02:05 | ARB-USDT-SWAP | 0.2 | 0.2/0.2 | 0.2 | res 0.2 (ha 3 candles) | 0.0 | 0.0100% | sem_zona |
| 2026-09-08 02:05 | WLD-USDT-SWAP | 0.5 | 0.5/0.5 | 0.5 | — | 0.0 | 0.0100% | sem_zona |
| 2026-09-08 02:05 | SUI-USDT-SWAP | 0.8 | 0.8/0.8 | 0.8 | res 0.8 (ha 8 candles) | 0.0 | 0.0100% | zona_mapeada_setup_B |
| 2026-09-08 02:05 | UNI-USDT-SWAP | 7.0 | 7.0/7.0 | 7.0 | — | 0.1 | 0.0100% | sem_zona |
| 2026-09-08 02:05 | LINK-USDT-SWAP | 12.6 | 12.7/12.6 | 12.7 | res 12.8 (ha 3 candles) | 0.1 | -0.0021% | zona_mapeada_setup_B |
| 2026-09-08 03:05 | BTC-USDT-SWAP | 78545.1 | 78850.0/78511.8 | 78877.0 | — | 287.2 | 0.0041% | zona_mapeada_setup_B |
| 2026-09-08 03:05 | ETH-USDT-SWAP | 2472.4 | 2484.0/2471.7 | 2485.1 | res 2507.4 (ha 3 candles) | 12.6 | 0.0071% | zona_mapeada_setup_B |
| 2026-09-08 03:05 | SOL-USDT-SWAP | 102.9 | 103.5/102.8 | 103.3 | res 104.5 (ha 3 candles) | 0.6 | -0.0040% | sem_zona |
| 2026-09-08 03:05 | XRP-USDT-SWAP | 1.4 | 1.4/1.4 | 1.4 | — | 0.0 | 0.0062% | zona_mapeada_setup_B |
| 2026-09-08 03:05 | DOGE-USDT-SWAP | 0.1 | 0.1/0.1 | 0.1 | — | 0.0 | 0.0004% | zona_mapeada_setup_B |
| 2026-09-08 03:05 | ARB-USDT-SWAP | 0.2 | 0.2/0.2 | 0.2 | res 0.2 (ha 4 candles) | 0.0 | 0.0100% | zona_mapeada_setup_A |
| 2026-09-08 03:05 | WLD-USDT-SWAP | 0.5 | 0.5/0.5 | 0.5 | — | 0.0 | 0.0100% | sem_zona |
| 2026-09-08 03:05 | SUI-USDT-SWAP | 0.8 | 0.8/0.8 | 0.8 | res 0.8 (ha 3 candles) | 0.0 | 0.0100% | invalidado_setup_B |
| 2026-09-08 03:05 | UNI-USDT-SWAP | 7.0 | 7.1/7.0 | 7.0 | — | 0.1 | 0.0100% | sem_zona |
| 2026-09-08 03:05 | LINK-USDT-SWAP | 12.6 | 12.7/12.6 | 12.7 | res 12.8 (ha 4 candles) | 0.1 | -0.0010% | zona_mapeada_setup_B |
| 2026-09-08 04:05 | BTC-USDT-SWAP | 78288.1 | 78608.5/78217.8 | 78877.0 | — | 298.0 | 0.0046% | invalidado_setup_B |
| 2026-09-08 04:05 | ETH-USDT-SWAP | 2467.6 | 2476.4/2461.5 | 2485.1 | res 2507.4 (ha 4 candles) | 12.8 | 0.0076% | zona_mapeada_setup_B |
| 2026-09-08 04:05 | SOL-USDT-SWAP | 102.6 | 103.0/102.2 | 103.3 | res 104.5 (ha 4 candles) | 0.7 | -0.0032% | zona_mapeada_setup_B |
| 2026-09-08 04:05 | XRP-USDT-SWAP | 1.4 | 1.4/1.4 | 1.4 | — | 0.0 | 0.0060% | zona_expirada_setup_B |
| 2026-09-08 04:05 | DOGE-USDT-SWAP | 0.1 | 0.1/0.1 | 0.1 | — | 0.0 | 0.0010% | zona_mapeada_setup_B |
| 2026-09-08 04:05 | ARB-USDT-SWAP | 0.2 | 0.2/0.2 | 0.2 | res 0.2 (ha 5 candles) | 0.0 | 0.0100% | invalidado_setup_A |
| 2026-09-08 04:05 | WLD-USDT-SWAP | 0.5 | 0.5/0.5 | 0.5 | — | 0.0 | 0.0100% | sem_zona |
| 2026-09-08 04:05 | SUI-USDT-SWAP | 0.8 | 0.8/0.8 | 0.8 | res 0.8 (ha 4 candles) | 0.0 | 0.0100% | zona_mapeada_setup_B |
| 2026-09-08 04:05 | UNI-USDT-SWAP | 7.0 | 7.1/7.0 | 7.0 | — | 0.1 | 0.0100% | sem_zona |
| 2026-09-08 04:05 | LINK-USDT-SWAP | 12.6 | 12.7/12.6 | 12.7 | res 12.8 (ha 5 candles) | 0.1 | -0.0004% | zona_mapeada_setup_B |
| 2026-09-08 05:05 | BTC-USDT-SWAP | 78443.9 | 78567.0/78123.2 | 78443.9 | — | 314.6 | 0.0057% | zona_mapeada_setup_B |
| 2026-09-08 05:05 | ETH-USDT-SWAP | 2478.5 | 2484.2/2466.9 | 2478.5 | res 2507.4 (ha 5 candles) | 12.7 | 0.0066% | zona_mapeada_setup_B |
| 2026-09-08 05:05 | SOL-USDT-SWAP | 102.9 | 103.1/102.5 | 102.9 | res 104.5 (ha 5 candles) | 0.7 | -0.0026% | zona_mapeada_setup_B |
| 2026-09-08 05:05 | XRP-USDT-SWAP | 1.4 | 1.4/1.4 | 1.4 | — | 0.0 | 0.0069% | zona_mapeada_setup_B |
| 2026-09-08 05:05 | DOGE-USDT-SWAP | 0.1 | 0.1/0.1 | 0.1 | — | 0.0 | 0.0023% | zona_mapeada_setup_B |
| 2026-09-08 05:05 | ARB-USDT-SWAP | 0.2 | 0.2/0.2 | 0.2 | res 0.2 (ha 6 candles) | 0.0 | 0.0100% | sem_zona |
| 2026-09-08 05:05 | WLD-USDT-SWAP | 0.5 | 0.5/0.5 | 0.5 | — | 0.0 | 0.0100% | sem_zona |
| 2026-09-08 05:05 | SUI-USDT-SWAP | 0.8 | 0.8/0.8 | 0.8 | res 0.8 (ha 5 candles) | 0.0 | 0.0100% | invalidado_setup_B |
| 2026-09-08 05:05 | UNI-USDT-SWAP | 7.0 | 7.1/7.0 | 7.0 | — | 0.1 | 0.0100% | sem_zona |
| 2026-09-08 05:05 | LINK-USDT-SWAP | 12.7 | 12.7/12.6 | 12.7 | res 12.8 (ha 6 candles) | 0.1 | -0.0020% | zona_mapeada_setup_B |
| 2026-09-08 06:05 | BTC-USDT-SWAP | 78389.1 | 78553.6/78250.0 | 78443.9 | — | 324.8 | 0.0072% | invalidado_setup_B |
| 2026-09-08 06:05 | ETH-USDT-SWAP | 2476.7 | 2482.4/2467.8 | 2478.5 | res 2507.4 (ha 6 candles) | 13.1 | 0.0055% | zona_mapeada_setup_B |
| 2026-09-08 06:05 | SOL-USDT-SWAP | 103.0 | 103.2/102.4 | 102.9 | res 104.5 (ha 6 candles) | 0.7 | -0.0023% | zona_mapeada_setup_B |
| 2026-09-08 06:05 | XRP-USDT-SWAP | 1.4 | 1.4/1.4 | 1.4 | — | 0.0 | 0.0084% | CONFIRMADO_setup_B |
| 2026-09-08 06:05 | DOGE-USDT-SWAP | 0.1 | 0.1/0.1 | 0.1 | — | 0.0 | 0.0051% | zona_mapeada_setup_B |
| 2026-09-08 06:05 | ARB-USDT-SWAP | 0.2 | 0.2/0.2 | 0.2 | res 0.2 (ha 3 candles) | 0.0 | 0.0071% | sem_zona |
| 2026-09-08 06:05 | WLD-USDT-SWAP | 0.5 | 0.5/0.5 | 0.5 | — | 0.0 | 0.0100% | sem_zona |
| 2026-09-08 06:06 | SUI-USDT-SWAP | 0.8 | 0.8/0.8 | 0.8 | res 0.8 (ha 6 candles) | 0.0 | 0.0100% | zona_mapeada_setup_B |
| 2026-09-08 06:06 | UNI-USDT-SWAP | 7.1 | 7.1/7.0 | 7.0 | — | 0.1 | 0.0100% | sem_zona |
| 2026-09-08 06:06 | LINK-USDT-SWAP | 12.6 | 12.7/12.6 | 12.7 | res 12.8 (ha 7 candles) | 0.1 | -0.0026% | zona_mapeada_setup_B |
| 2026-09-08 07:05 | BTC-USDT-SWAP | 78721.0 | 78765.0/78300.5 | 78443.9 | — | 338.8 | 0.0069% | zona_mapeada_setup_B |
| 2026-09-08 07:05 | ETH-USDT-SWAP | 2490.9 | 2494.4/2474.6 | 2478.5 | res 2507.4 (ha 7 candles) | 13.9 | 0.0043% | zona_mapeada_setup_B |
| 2026-09-08 07:05 | SOL-USDT-SWAP | 103.6 | 103.8/102.9 | 102.9 | res 104.5 (ha 7 candles) | 0.7 | -0.0020% | zona_mapeada_setup_B |
| 2026-09-08 07:05 | XRP-USDT-SWAP | 1.4 | 1.4/1.4 | 1.4 | — | 0.0 | 0.0100% | zona_mapeada_setup_B |
| 2026-09-08 07:05 | DOGE-USDT-SWAP | 0.1 | 0.1/0.1 | 0.1 | — | 0.0 | 0.0079% | invalidado_setup_B |
| 2026-09-08 07:05 | ARB-USDT-SWAP | 0.2 | 0.2/0.2 | 0.2 | res 0.2 (ha 4 candles) | 0.0 | 0.0071% | sem_zona |
| 2026-09-08 07:05 | WLD-USDT-SWAP | 0.5 | 0.5/0.5 | 0.5 | — | 0.0 | 0.0067% | sem_zona |
| 2026-09-08 07:05 | SUI-USDT-SWAP | 0.8 | 0.8/0.8 | 0.8 | res 0.8 (ha 7 candles) | 0.0 | 0.0100% | invalidado_setup_B |
| 2026-09-08 07:05 | UNI-USDT-SWAP | 7.1 | 7.2/7.0 | 7.0 | — | 0.1 | 0.0018% | sem_zona |
| 2026-09-08 07:05 | LINK-USDT-SWAP | 12.7 | 12.8/12.6 | 12.7 | res 12.8 (ha 8 candles) | 0.1 | -0.0021% | zona_mapeada_setup_B |
| 2026-09-08 08:05 | BTC-USDT-SWAP | 78526.1 | 78965.0/78523.5 | 78443.9 | — | 354.2 | 0.0054% | zona_mapeada_setup_B |
| 2026-09-08 08:05 | ETH-USDT-SWAP | 2480.2 | 2499.4/2478.9 | 2478.5 | res 2507.4 (ha 8 candles) | 14.6 | 0.0035% | CONFIRMADO_setup_B |
| 2026-09-08 08:05 | SOL-USDT-SWAP | 103.3 | 104.1/103.3 | 102.9 | res 104.5 (ha 8 candles) | 0.7 | -0.0007% | zona_mapeada_setup_B |
| 2026-09-08 08:05 | XRP-USDT-SWAP | 1.4 | 1.4/1.4 | 1.4 | — | 0.0 | 0.0100% | CONFIRMADO_setup_B |
| 2026-09-08 08:05 | DOGE-USDT-SWAP | 0.1 | 0.1/0.1 | 0.1 | — | 0.0 | 0.0099% | zona_mapeada_setup_B |
| 2026-09-08 08:05 | ARB-USDT-SWAP | 0.2 | 0.2/0.2 | 0.2 | res 0.2 (ha 5 candles) | 0.0 | 0.0084% | sem_zona |
| 2026-09-08 08:05 | WLD-USDT-SWAP | 0.5 | 0.5/0.5 | 0.5 | — | 0.0 | 0.0063% | sem_zona |
| 2026-09-08 08:05 | SUI-USDT-SWAP | 0.8 | 0.8/0.8 | 0.8 | res 0.8 (ha 8 candles) | 0.0 | 0.0100% | zona_mapeada_setup_B |
| 2026-09-08 08:05 | UNI-USDT-SWAP | 7.0 | 7.1/7.0 | 7.0 | — | 0.1 | -0.0059% | sem_zona |
| 2026-09-08 08:05 | LINK-USDT-SWAP | 12.6 | 12.8/12.6 | 12.7 | res 12.8 (ha 9 candles) | 0.1 | -0.0022% | zona_expirada_setup_B |
| 2026-09-08 09:05 | BTC-USDT-SWAP | 78398.8 | 78539.8/78253.5 | 78398.8 | — | 365.8 | 0.0059% | invalidado_setup_B |
| 2026-09-08 09:05 | ETH-USDT-SWAP | 2473.6 | 2481.6/2470.5 | 2473.6 | res 2507.4 (ha 9 candles) | 14.9 | 0.0040% | sem_zona |
| 2026-09-08 09:05 | SOL-USDT-SWAP | 102.8 | 103.4/102.6 | 102.8 | res 104.5 (ha 9 candles) | 0.7 | -0.0012% | zona_mapeada_setup_B |
| 2026-09-08 09:05 | XRP-USDT-SWAP | 1.4 | 1.4/1.4 | 1.4 | — | 0.0 | 0.0100% | zona_mapeada_setup_B |
| 2026-09-08 09:05 | DOGE-USDT-SWAP | 0.1 | 0.1/0.1 | 0.1 | — | 0.0 | 0.0100% | CONFIRMADO_setup_B |
| 2026-09-08 09:05 | ARB-USDT-SWAP | 0.2 | 0.2/0.2 | 0.2 | res 0.2 (ha 6 candles) | 0.0 | 0.0100% | sem_zona |
| 2026-09-08 09:05 | WLD-USDT-SWAP | 0.5 | 0.5/0.5 | 0.5 | — | 0.0 | 0.0071% | sem_zona |
| 2026-09-08 09:05 | SUI-USDT-SWAP | 0.8 | 0.8/0.8 | 0.8 | res 0.8 (ha 9 candles) | 0.0 | 0.0100% | CONFIRMADO_setup_B |
| 2026-09-08 09:05 | UNI-USDT-SWAP | 7.0 | 7.0/6.9 | 7.0 | sup 6.7 (ha 13 candles) | 0.1 | -0.0107% | sem_zona |
| 2026-09-08 09:05 | LINK-USDT-SWAP | 12.5 | 12.6/12.4 | 12.5 | res 12.8 (ha 10 candles) | 0.1 | -0.0038% | zona_mapeada_setup_B |
| 2026-09-08 10:05 | BTC-USDT-SWAP | 78422.0 | 78448.6/78187.0 | 78398.8 | — | 350.5 | 0.0077% | zona_mapeada_setup_B |
| 2026-09-08 10:05 | ETH-USDT-SWAP | 2472.1 | 2475.3/2467.3 | 2473.6 | res 2507.4 (ha 10 candles) | 14.2 | 0.0053% | sem_zona |
| 2026-09-08 10:05 | SOL-USDT-SWAP | 103.0 | 103.3/102.4 | 102.8 | res 104.5 (ha 10 candles) | 0.7 | -0.0006% | zona_mapeada_setup_B |
| 2026-09-08 10:05 | XRP-USDT-SWAP | 1.4 | 1.4/1.4 | 1.4 | — | 0.0 | 0.0100% | zona_mapeada_setup_B |
| 2026-09-08 10:05 | DOGE-USDT-SWAP | 0.1 | 0.1/0.1 | 0.1 | — | 0.0 | 0.0100% | zona_mapeada_setup_B |
| 2026-09-08 10:05 | ARB-USDT-SWAP | 0.2 | 0.2/0.2 | 0.2 | res 0.2 (ha 7 candles) | 0.0 | 0.0100% | sem_zona |
| 2026-09-08 10:05 | WLD-USDT-SWAP | 0.5 | 0.5/0.5 | 0.5 | — | 0.0 | 0.0100% | sem_zona |
| 2026-09-08 10:05 | SUI-USDT-SWAP | 0.8 | 0.8/0.8 | 0.8 | res 0.8 (ha 10 candles) | 0.0 | 0.0100% | zona_mapeada_setup_B |
| 2026-09-08 10:05 | UNI-USDT-SWAP | 6.9 | 7.1/6.9 | 7.0 | sup 6.7 (ha 14 candles) | 0.1 | -0.0075% | zona_mapeada_setup_B |
| 2026-09-08 10:05 | LINK-USDT-SWAP | 12.5 | 12.6/12.4 | 12.5 | res 12.8 (ha 11 candles) | 0.1 | -0.0040% | zona_mapeada_setup_B |
| 2026-09-08 11:06 | BTC-USDT-SWAP | 77941.9 | 78514.6/77574.3 | 78398.8 | — | 397.3 | 0.0086% | CONFIRMADO_setup_B |
| 2026-09-08 11:06 | ETH-USDT-SWAP | 2458.6 | 2474.9/2440.4 | 2473.6 | res 2499.4 (ha 3 candles) | 15.8 | 0.0066% | zona_mapeada_setup_B |
| 2026-09-08 11:06 | SOL-USDT-SWAP | 102.6 | 103.1/101.6 | 102.8 | res 104.1 (ha 3 candles) | 0.8 | -0.0008% | zona_mapeada_setup_B |
| 2026-09-08 11:06 | XRP-USDT-SWAP | 1.4 | 1.4/1.4 | 1.4 | — | 0.0 | 0.0100% | invalidado_setup_B |
| 2026-09-08 11:06 | DOGE-USDT-SWAP | 0.1 | 0.1/0.1 | 0.1 | — | 0.0 | 0.0100% | zona_mapeada_setup_B |
| 2026-09-08 11:06 | ARB-USDT-SWAP | 0.2 | 0.2/0.2 | 0.2 | res 0.2 (ha 3 candles) | 0.0 | 0.0100% | sem_zona |
| 2026-09-08 11:06 | WLD-USDT-SWAP | 0.5 | 0.5/0.5 | 0.5 | — | 0.0 | 0.0100% | sem_zona |
| 2026-09-08 11:06 | SUI-USDT-SWAP | 0.8 | 0.8/0.8 | 0.8 | res 0.8 (ha 3 candles) | 0.0 | 0.0100% | zona_mapeada_setup_B |
| 2026-09-08 11:06 | UNI-USDT-SWAP | 6.9 | 7.0/6.8 | 7.0 | sup 6.7 (ha 15 candles) | 0.1 | -0.0034% | zona_mapeada_setup_B |
| 2026-09-08 11:06 | LINK-USDT-SWAP | 12.5 | 12.5/12.3 | 12.5 | res 12.8 (ha 3 candles) | 0.1 | -0.0033% | zona_mapeada_setup_B |
| 2026-09-08 12:05 | BTC-USDT-SWAP | 78525.9 | 78598.3/77824.1 | 78398.8 | — | 427.4 | 0.0080% | zona_mapeada_setup_B |
| 2026-09-08 12:05 | ETH-USDT-SWAP | 2484.6 | 2485.6/2455.9 | 2473.6 | res 2499.4 (ha 4 candles) | 17.0 | 0.0062% | CONFIRMADO_setup_B |
| 2026-09-08 12:05 | SOL-USDT-SWAP | 103.3 | 103.4/102.4 | 102.8 | res 104.1 (ha 4 candles) | 0.8 | -0.0008% | zona_expirada_setup_B |
| 2026-09-08 12:05 | XRP-USDT-SWAP | 1.4 | 1.4/1.4 | 1.4 | — | 0.0 | 0.0100% | sem_zona |
| 2026-09-08 12:05 | DOGE-USDT-SWAP | 0.1 | 0.1/0.1 | 0.1 | — | 0.0 | 0.0100% | zona_mapeada_setup_B |
| 2026-09-08 12:05 | ARB-USDT-SWAP | 0.2 | 0.2/0.2 | 0.2 | res 0.2 (ha 4 candles) | 0.0 | 0.0100% | sem_zona |
| 2026-09-08 12:05 | WLD-USDT-SWAP | 0.5 | 0.5/0.5 | 0.5 | — | 0.0 | 0.0100% | sem_zona |
| 2026-09-08 12:05 | SUI-USDT-SWAP | 0.8 | 0.8/0.8 | 0.8 | res 0.8 (ha 4 candles) | 0.0 | 0.0100% | invalidado_setup_B |
| 2026-09-08 12:05 | UNI-USDT-SWAP | 6.9 | 7.0/6.8 | 7.0 | sup 6.7 (ha 16 candles) | 0.1 | -0.0026% | zona_mapeada_setup_B |
| 2026-09-08 12:05 | LINK-USDT-SWAP | 12.6 | 12.6/12.4 | 12.5 | res 12.8 (ha 4 candles) | 0.1 | -0.0033% | invalidado_setup_B |
| 2026-09-08 13:05 | BTC-USDT-SWAP | 78866.0 | 78873.1/78412.7 | 78866.0 | — | 445.6 | 0.0062% | zona_mapeada_setup_B |
| 2026-09-08 13:05 | ETH-USDT-SWAP | 2497.4 | 2500.7/2478.9 | 2497.4 | res 2499.4 (ha 5 candles) | 17.7 | 0.0055% | zona_mapeada_setup_B |
| 2026-09-08 13:05 | SOL-USDT-SWAP | 104.2 | 104.3/103.2 | 104.2 | res 104.1 (ha 5 candles) | 0.9 | -0.0001% | zona_mapeada_setup_A |
| 2026-09-08 13:05 | XRP-USDT-SWAP | 1.4 | 1.4/1.4 | 1.4 | — | 0.0 | 0.0100% | zona_mapeada_setup_B |
| 2026-09-08 13:05 | DOGE-USDT-SWAP | 0.1 | 0.1/0.1 | 0.1 | — | 0.0 | 0.0100% | invalidado_setup_B |
| 2026-09-08 13:05 | ARB-USDT-SWAP | 0.2 | 0.2/0.2 | 0.2 | res 0.2 (ha 5 candles) | 0.0 | 0.0100% | sem_zona |
| 2026-09-08 13:05 | WLD-USDT-SWAP | 0.5 | 0.5/0.5 | 0.5 | res 0.5 (ha 5 candles) | 0.0 | 0.0100% | sem_zona |
| 2026-09-08 13:05 | SUI-USDT-SWAP | 0.8 | 0.8/0.8 | 0.8 | res 0.8 (ha 5 candles) | 0.0 | 0.0100% | sem_zona |
| 2026-09-08 13:05 | UNI-USDT-SWAP | 6.9 | 6.9/6.8 | 6.9 | sup 6.7 (ha 17 candles) | 0.1 | -0.0002% | CONFIRMADO_setup_B |
| 2026-09-08 13:05 | LINK-USDT-SWAP | 12.7 | 12.7/12.6 | 12.7 | res 12.8 (ha 5 candles) | 0.1 | -0.0047% | sem_zona |
| 2026-09-08 14:05 | BTC-USDT-SWAP | 78698.0 | 78940.0/78535.3 | 78866.0 | — | 434.5 | 0.0050% | zona_mapeada_setup_B |
| 2026-09-08 14:05 | ETH-USDT-SWAP | 2495.5 | 2504.5/2485.7 | 2497.4 | res 2499.4 (ha 6 candles) | 17.3 | 0.0048% | invalidado_setup_B |
| 2026-09-08 14:05 | SOL-USDT-SWAP | 104.1 | 104.8/103.5 | 104.2 | res 104.1 (ha 6 candles) | 0.9 | -0.0013% | zona_mapeada_setup_A |
| 2026-09-08 14:05 | XRP-USDT-SWAP | 1.4 | 1.5/1.4 | 1.4 | — | 0.0 | 0.0100% | invalidado_setup_B |
| 2026-09-08 14:05 | DOGE-USDT-SWAP | 0.1 | 0.1/0.1 | 0.1 | — | 0.0 | 0.0100% | zona_mapeada_setup_B |
| 2026-09-08 14:05 | ARB-USDT-SWAP | 0.2 | 0.2/0.2 | 0.2 | res 0.2 (ha 6 candles) | 0.0 | 0.0100% | sem_zona |
| 2026-09-08 14:05 | WLD-USDT-SWAP | 0.5 | 0.5/0.5 | 0.5 | res 0.5 (ha 6 candles) | 0.0 | 0.0100% | sem_zona |
| 2026-09-08 14:05 | SUI-USDT-SWAP | 0.8 | 0.8/0.8 | 0.8 | res 0.8 (ha 6 candles) | 0.0 | 0.0100% | sem_zona |
| 2026-09-08 14:05 | UNI-USDT-SWAP | 6.9 | 6.9/6.8 | 6.9 | sup 6.8 (ha 3 candles) | 0.1 | 0.0024% | zona_mapeada_setup_B |
| 2026-09-08 14:05 | LINK-USDT-SWAP | 12.7 | 12.8/12.6 | 12.7 | res 12.8 (ha 6 candles) | 0.1 | -0.0042% | sem_zona |
| 2026-09-08 15:05 | BTC-USDT-SWAP | 78465.8 | 78860.3/78460.0 | 78866.0 | — | 442.0 | 0.0041% | zona_mapeada_setup_B |
| 2026-09-08 15:05 | ETH-USDT-SWAP | 2487.1 | 2501.5/2486.3 | 2497.4 | res 2499.4 (ha 7 candles) | 17.6 | 0.0041% | zona_mapeada_setup_B |
| 2026-09-08 15:05 | SOL-USDT-SWAP | 103.6 | 104.4/103.6 | 104.2 | res 104.1 (ha 7 candles) | 0.9 | -0.0028% | invalidado_setup_A |
| 2026-09-08 15:05 | XRP-USDT-SWAP | 1.4 | 1.4/1.4 | 1.4 | — | 0.0 | 0.0099% | zona_mapeada_setup_B |
| 2026-09-08 15:05 | DOGE-USDT-SWAP | 0.1 | 0.1/0.1 | 0.1 | — | 0.0 | 0.0100% | CONFIRMADO_setup_B |
| 2026-09-08 15:05 | ARB-USDT-SWAP | 0.2 | 0.2/0.2 | 0.2 | res 0.2 (ha 7 candles) | 0.0 | 0.0100% | sem_zona |
| 2026-09-08 15:05 | WLD-USDT-SWAP | 0.5 | 0.5/0.5 | 0.5 | res 0.5 (ha 7 candles) | 0.0 | 0.0100% | sem_zona |
| 2026-09-08 15:05 | SUI-USDT-SWAP | 0.8 | 0.8/0.8 | 0.8 | res 0.8 (ha 7 candles) | 0.0 | 0.0100% | zona_mapeada_setup_B |
| 2026-09-08 15:05 | UNI-USDT-SWAP | 6.8 | 6.9/6.8 | 6.9 | sup 6.8 (ha 4 candles) | 0.1 | 0.0023% | zona_mapeada_setup_B |
| 2026-09-08 15:05 | LINK-USDT-SWAP | 12.7 | 12.8/12.6 | 12.7 | res 12.8 (ha 7 candles) | 0.1 | -0.0022% | sem_zona |
| 2026-09-08 16:05 | BTC-USDT-SWAP | 78407.4 | 78782.1/78232.0 | 78866.0 | — | 461.44 | 0.0035% | invalidado_setup_B |
| 2026-09-08 16:05 | ETH-USDT-SWAP | 2485.7 | 2507.6/2475.5 | 2497.4 | res 2499.4 (ha 8 candles) | 19.33 | 0.0039% | descartado_rr_baixo_setup_B |
| 2026-09-08 16:05 | SOL-USDT-SWAP | 103.31 | 104.43/103.12 | 104.25 | res 104.06 (ha 8 candles) | 0.94786 | -0.0029% | sem_zona |
| 2026-09-08 16:05 | XRP-USDT-SWAP | 1.4302 | 1.4458/1.4231 | 1.4338 | — | 0.01499 | 0.0100% | zona_mapeada_setup_B |
| 2026-09-08 16:05 | DOGE-USDT-SWAP | 0.08949 | 0.09075/0.08915 | 0.09062 | — | 0.00113 | 0.0100% | zona_mapeada_setup_B |
| 2026-09-08 16:05 | ARB-USDT-SWAP | 0.16761 | 0.17015/0.16668 | 0.17027 | res 0.17870 (ha 8 candles) | 0.00493 | 0.0100% | sem_zona |
| 2026-09-08 16:05 | WLD-USDT-SWAP | 0.47100 | 0.48180/0.46940 | 0.48690 | res 0.49410 (ha 3 candles) | 0.01305 | 0.0100% | sem_zona |
| 2026-09-08 16:05 | SUI-USDT-SWAP | 0.81000 | 0.82670/0.80700 | 0.82740 | res 0.83350 (ha 8 candles) | 0.01519 | 0.0100% | descartado_rr_baixo_setup_B |
| 2026-09-08 16:05 | UNI-USDT-SWAP | 6.8170 | 6.9340/6.7630 | 6.9280 | sup 6.8110 (ha 5 candles) | 0.13229 | 0.0033% | invalidado_setup_B |
| 2026-09-08 16:05 | LINK-USDT-SWAP | 12.63 | 12.77/12.58 | 12.68 | res 12.80 (ha 8 candles) | 0.15979 | 0.0019% | sem_zona |
| 2026-09-08 17:05 | BTC-USDT-SWAP | 78410.1 | 78493.9/78280.0 | 78410.1 | — | 452.56 | 0.0029% | zona_mapeada_setup_B |
| 2026-09-08 17:05 | ETH-USDT-SWAP | 2481.3 | 2491.1/2475.4 | 2481.3 | res 2499.4 (ha 9 candles) | 19.57 | 0.0036% | sem_zona |
| 2026-09-08 17:05 | SOL-USDT-SWAP | 103.16 | 103.53/102.74 | 103.16 | res 104.78 (ha 3 candles) | 0.95786 | -0.0045% | sem_zona |
| 2026-09-08 17:05 | XRP-USDT-SWAP | 1.4225 | 1.4339/1.4158 | 1.4225 | res 1.4504 (ha 3 candles) | 0.01555 | 0.0089% | CONFIRMADO_setup_B |
| 2026-09-08 17:05 | DOGE-USDT-SWAP | 0.08955 | 0.09004/0.08930 | 0.08955 | — | 0.00111 | 0.0100% | zona_mapeada_setup_B |
| 2026-09-08 17:05 | ARB-USDT-SWAP | 0.16824 | 0.16950/0.16692 | 0.16824 | res 0.17870 (ha 9 candles) | 0.00466 | 0.0100% | sem_zona |
| 2026-09-08 17:05 | WLD-USDT-SWAP | 0.46330 | 0.47340/0.46210 | 0.46330 | res 0.49410 (ha 4 candles) | 0.01334 | 0.0095% | sem_zona |
| 2026-09-08 17:05 | SUI-USDT-SWAP | 0.81170 | 0.81570/0.80870 | 0.81170 | res 0.83410 (ha 3 candles) | 0.01471 | 0.0100% | sem_zona |
| 2026-09-08 17:05 | UNI-USDT-SWAP | 6.7580 | 6.8430/6.7350 | 6.7580 | sup 6.8110 (ha 6 candles) | 0.13250 | 0.0024% | zona_mapeada_setup_A |
| 2026-09-08 17:05 | LINK-USDT-SWAP | 12.56 | 12.65/12.53 | 12.56 | res 12.81 (ha 3 candles) | 0.16143 | 0.0053% | sem_zona |
| 2026-09-08 18:05 | BTC-USDT-SWAP | 78450.1 | 78585.4/78371.4 | 78410.1 | — | 439.94 | 0.0032% | invalidado_setup_B |
| 2026-09-08 18:05 | ETH-USDT-SWAP | 2482.0 | 2490.8/2479.3 | 2481.3 | res 2499.4 (ha 10 candles) | 19.32 | 0.0041% | sem_zona |
| 2026-09-08 18:05 | SOL-USDT-SWAP | 103.02 | 103.75/102.99 | 103.16 | res 104.78 (ha 4 candles) | 0.95500 | -0.0049% | sem_zona |
| 2026-09-08 18:05 | XRP-USDT-SWAP | 1.4142 | 1.4264/1.4128 | 1.4225 | res 1.4504 (ha 4 candles) | 0.01592 | 0.0094% | sem_zona |
| 2026-09-08 18:05 | DOGE-USDT-SWAP | 0.08963 | 0.09045/0.08944 | 0.08955 | — | 0.00112 | 0.0100% | zona_mapeada_setup_B |
| 2026-09-08 18:05 | ARB-USDT-SWAP | 0.16877 | 0.17031/0.16746 | 0.16824 | res 0.17870 (ha 10 candles) | 0.00452 | 0.0100% | sem_zona |
| 2026-09-08 18:05 | WLD-USDT-SWAP | 0.45940 | 0.46800/0.45740 | 0.46330 | res 0.49410 (ha 5 candles) | 0.01334 | 0.0042% | sem_zona |
| 2026-09-08 18:05 | SUI-USDT-SWAP | 0.81000 | 0.82210/0.80920 | 0.81170 | res 0.83410 (ha 4 candles) | 0.01479 | 0.0100% | sem_zona |
| 2026-09-08 18:05 | UNI-USDT-SWAP | 6.7400 | 6.7950/6.7370 | 6.7580 | sup 6.8110 (ha 7 candles) | 0.13014 | -0.0015% | descartado_rr_baixo_setup_A |
| 2026-09-08 18:05 | LINK-USDT-SWAP | 12.51 | 12.61/12.51 | 12.56 | res 12.81 (ha 4 candles) | 0.15850 | 0.0082% | sem_zona |
| 2026-09-08 19:05 | BTC-USDT-SWAP | 78459.9 | 78582.7/78370.0 | 78410.1 | — | 423.44 | 0.0034% | zona_mapeada_setup_B |
| 2026-09-08 19:05 | ETH-USDT-SWAP | 2481.9 | 2486.4/2477.4 | 2481.3 | res 2507.6 (ha 3 candles) | 18.72 | 0.0048% | sem_zona |
| 2026-09-08 19:05 | SOL-USDT-SWAP | 102.95 | 103.29/102.71 | 103.16 | res 104.78 (ha 5 candles) | 0.95643 | -0.0081% | sem_zona |
| 2026-09-08 19:05 | XRP-USDT-SWAP | 1.4165 | 1.4232/1.4135 | 1.4225 | res 1.4504 (ha 5 candles) | 0.01582 | 0.0100% | sem_zona |
| 2026-09-08 19:05 | DOGE-USDT-SWAP | 0.08953 | 0.09002/0.08923 | 0.08955 | — | 0.00111 | 0.0100% | descartado_rr_baixo_setup_B |
| 2026-09-08 19:05 | ARB-USDT-SWAP | 0.16722 | 0.16953/0.16539 | 0.16824 | res 0.17870 (ha 11 candles) | 0.00461 | 0.0100% | sem_zona |
| 2026-09-08 19:05 | WLD-USDT-SWAP | 0.45290 | 0.46070/0.45120 | 0.46330 | res 0.49410 (ha 6 candles) | 0.01279 | 0.0047% | sem_zona |
| 2026-09-08 19:05 | SUI-USDT-SWAP | 0.80860 | 0.81500/0.80560 | 0.81170 | res 0.83410 (ha 5 candles) | 0.01446 | 0.0100% | sem_zona |
| 2026-09-08 19:05 | UNI-USDT-SWAP | 6.6880 | 6.7590/6.6610 | 6.7580 | sup 6.8110 (ha 8 candles) | 0.12664 | -0.0037% | zona_mapeada_setup_A |
| 2026-09-08 19:05 | LINK-USDT-SWAP | 12.47 | 12.58/12.43 | 12.56 | res 12.81 (ha 5 candles) | 0.16100 | 0.0096% | sem_zona |
| 2026-09-08 20:05 | BTC-USDT-SWAP | 78526.2 | 78646.8/78420.0 | 78410.1 | — | 417.95 | 0.0042% | zona_mapeada_setup_B |
| 2026-09-08 20:05 | ETH-USDT-SWAP | 2488.0 | 2489.1/2480.5 | 2481.3 | res 2507.6 (ha 4 candles) | 18.29 | 0.0066% | sem_zona |
| 2026-09-08 20:05 | SOL-USDT-SWAP | 103.34 | 103.40/102.90 | 103.16 | res 104.78 (ha 6 candles) | 0.93500 | -0.0099% | sem_zona |
| 2026-09-08 20:05 | XRP-USDT-SWAP | 1.4177 | 1.4230/1.4161 | 1.4225 | res 1.4504 (ha 6 candles) | 0.01565 | 0.0100% | sem_zona |
| 2026-09-08 20:05 | DOGE-USDT-SWAP | 0.08997 | 0.09006/0.08948 | 0.08955 | — | 0.00110 | 0.0100% | zona_mapeada_setup_B |
| 2026-09-08 20:05 | ARB-USDT-SWAP | 0.16573 | 0.16823/0.16537 | 0.16824 | res 0.17870 (ha 12 candles) | 0.00459 | 0.0100% | sem_zona |
| 2026-09-08 20:05 | WLD-USDT-SWAP | 0.45460 | 0.45550/0.45120 | 0.46330 | res 0.49410 (ha 7 candles) | 0.01234 | 0.0050% | sem_zona |
| 2026-09-08 20:05 | SUI-USDT-SWAP | 0.81360 | 0.81510/0.80810 | 0.81170 | res 0.83410 (ha 6 candles) | 0.01407 | 0.0100% | sem_zona |
| 2026-09-08 20:05 | UNI-USDT-SWAP | 6.8020 | 6.8080/6.6880 | 6.7580 | sup 6.8110 (ha 9 candles) | 0.12886 | -0.0015% | zona_mapeada_setup_A |
| 2026-09-08 20:05 | LINK-USDT-SWAP | 12.54 | 12.54/12.47 | 12.56 | res 12.81 (ha 6 candles) | 0.15921 | 0.0100% | sem_zona |
| 2026-09-08 21:05 | BTC-USDT-SWAP | 78420.7 | 78534.4/78368.5 | 78420.7 | — | 396.62 | 0.0047% | invalidado_setup_B |
| 2026-09-08 21:05 | ETH-USDT-SWAP | 2484.1 | 2489.6/2481.7 | 2484.1 | res 2507.6 (ha 5 candles) | 17.44 | 0.0082% | sem_zona |
| 2026-09-08 21:05 | SOL-USDT-SWAP | 103.32 | 103.53/103.19 | 103.32 | res 104.78 (ha 7 candles) | 0.89214 | -0.0091% | sem_zona |
| 2026-09-08 21:05 | XRP-USDT-SWAP | 1.4165 | 1.4208/1.4146 | 1.4165 | res 1.4504 (ha 7 candles) | 0.01521 | 0.0100% | sem_zona |
| 2026-09-08 21:05 | DOGE-USDT-SWAP | 0.09000 | 0.09010/0.08980 | 0.09000 | — | 0.00099 | 0.0100% | zona_mapeada_setup_B |
| 2026-09-08 21:05 | ARB-USDT-SWAP | 0.16494 | 0.16606/0.16349 | 0.16494 | — | 0.00430 | 0.0100% | sem_zona |
| 2026-09-08 21:05 | WLD-USDT-SWAP | 0.45260 | 0.45580/0.45210 | 0.45260 | res 0.49410 (ha 8 candles) | 0.01150 | 0.0047% | sem_zona |
| 2026-09-08 21:05 | SUI-USDT-SWAP | 0.81070 | 0.81620/0.80870 | 0.81070 | res 0.83410 (ha 7 candles) | 0.01345 | 0.0100% | sem_zona |
| 2026-09-08 21:05 | UNI-USDT-SWAP | 6.7480 | 6.8200/6.7210 | 6.7480 | sup 6.8110 (ha 10 candles) | 0.12021 | 0.0008% | descartado_rr_baixo_setup_A |
| 2026-09-08 21:05 | LINK-USDT-SWAP | 12.51 | 12.55/12.49 | 12.51 | res 12.81 (ha 7 candles) | 0.15279 | 0.0092% | sem_zona |
| 2026-09-08 22:05 | BTC-USDT-SWAP | 78740.4 | 78761.3/78413.2 | 78420.7 | — | 389.95 | 0.0046% | zona_mapeada_setup_B |
| 2026-09-08 22:05 | ETH-USDT-SWAP | 2495.3 | 2496.6/2484.1 | 2484.1 | res 2507.6 (ha 6 candles) | 16.87 | 0.0099% | sem_zona |
| 2026-09-08 22:05 | SOL-USDT-SWAP | 103.72 | 103.86/103.28 | 103.32 | res 104.78 (ha 8 candles) | 0.88000 | -0.0084% | sem_zona |
| 2026-09-08 22:05 | XRP-USDT-SWAP | 1.4198 | 1.4247/1.4165 | 1.4165 | res 1.4504 (ha 8 candles) | 0.01529 | 0.0100% | sem_zona |
| 2026-09-08 22:05 | DOGE-USDT-SWAP | 0.09050 | 0.09099/0.08998 | 0.09000 | — | 0.00100 | 0.0100% | invalidado_setup_B |
| 2026-09-08 22:05 | ARB-USDT-SWAP | 0.16474 | 0.16646/0.16220 | 0.16494 | — | 0.00416 | 0.0100% | sem_zona |
| 2026-09-08 22:05 | WLD-USDT-SWAP | 0.45670 | 0.45810/0.44630 | 0.45260 | res 0.49410 (ha 9 candles) | 0.01128 | 0.0035% | sem_zona |
| 2026-09-08 22:05 | SUI-USDT-SWAP | 0.81730 | 0.82370/0.81060 | 0.81070 | res 0.83410 (ha 8 candles) | 0.01348 | 0.0100% | sem_zona |
| 2026-09-08 22:05 | UNI-USDT-SWAP | 6.7750 | 6.7900/6.7240 | 6.7480 | sup 6.6610 (ha 3 candles) | 0.11571 | 0.0036% | sem_zona |
| 2026-09-08 22:05 | LINK-USDT-SWAP | 12.52 | 12.57/12.46 | 12.51 | res 12.81 (ha 8 candles) | 0.14857 | 0.0071% | sem_zona |
| 2026-09-08 23:05 | BTC-USDT-SWAP | 78851.0 | 78851.0/78595.5 | 78420.7 | — | 387.75 | 0.0039% | descartado_rr_baixo_setup_B |
| 2026-09-08 23:05 | ETH-USDT-SWAP | 2496.5 | 2498.5/2488.4 | 2484.1 | res 2507.6 (ha 7 candles) | 16.80 | 0.0094% | sem_zona |
| 2026-09-08 23:05 | SOL-USDT-SWAP | 103.72 | 103.89/103.30 | 103.32 | res 104.78 (ha 9 candles) | 0.86357 | -0.0073% | sem_zona |
| 2026-09-08 23:05 | XRP-USDT-SWAP | 1.4169 | 1.4221/1.4094 | 1.4165 | res 1.4504 (ha 9 candles) | 0.01557 | 0.0100% | sem_zona |
| 2026-09-08 23:05 | DOGE-USDT-SWAP | 0.09023 | 0.09063/0.08985 | 0.09000 | — | 0.00098 | 0.0100% | zona_mapeada_setup_B |
| 2026-09-08 23:05 | ARB-USDT-SWAP | 0.16541 | 0.16565/0.16358 | 0.16494 | — | 0.00409 | 0.0100% | sem_zona |
| 2026-09-08 23:05 | WLD-USDT-SWAP | 0.45780 | 0.46030/0.45400 | 0.45260 | res 0.49410 (ha 10 candles) | 0.01064 | 0.0011% | sem_zona |
| 2026-09-08 23:05 | SUI-USDT-SWAP | 0.81570 | 0.81960/0.80980 | 0.81070 | res 0.83410 (ha 9 candles) | 0.01270 | 0.0100% | sem_zona |
| 2026-09-08 23:05 | UNI-USDT-SWAP | 6.7840 | 6.7920/6.7220 | 6.7480 | sup 6.6610 (ha 4 candles) | 0.11307 | 0.0047% | sem_zona |
| 2026-09-08 23:05 | LINK-USDT-SWAP | 12.49 | 12.53/12.45 | 12.51 | res 12.81 (ha 9 candles) | 0.13850 | 0.0058% | sem_zona |
| 2026-09-09 00:05 | BTC-USDT-SWAP | 78686.7 | 78888.0/78647.1 | 78420.7 | — | 386.27 | 0.0029% | zona_mapeada_setup_B |
| 2026-09-09 00:05 | ETH-USDT-SWAP | 2492.6 | 2499.0/2488.6 | 2484.1 | res 2507.6 (ha 8 candles) | 16.97 | 0.0082% | sem_zona |
| 2026-09-09 00:05 | SOL-USDT-SWAP | 103.41 | 103.97/103.27 | 103.32 | res 104.78 (ha 10 candles) | 0.84929 | -0.0071% | sem_zona |
| 2026-09-09 00:05 | XRP-USDT-SWAP | 1.4154 | 1.4211/1.4111 | 1.4165 | res 1.4504 (ha 10 candles) | 0.01527 | 0.0100% | sem_zona |
| 2026-09-09 00:05 | DOGE-USDT-SWAP | 0.08989 | 0.09043/0.08958 | 0.09000 | — | 0.00096 | 0.0100% | descartado_rr_baixo_setup_B |
| 2026-09-09 00:05 | ARB-USDT-SWAP | 0.16594 | 0.16719/0.16457 | 0.16494 | — | 0.00390 | 0.0100% | sem_zona |
| 2026-09-09 00:05 | WLD-USDT-SWAP | 0.45420 | 0.45830/0.45330 | 0.45260 | res 0.49410 (ha 11 candles) | 0.01009 | 0.0017% | sem_zona |
| 2026-09-09 00:05 | SUI-USDT-SWAP | 0.81060 | 0.82040/0.81020 | 0.81070 | res 0.83410 (ha 10 candles) | 0.01260 | 0.0100% | sem_zona |
| 2026-09-09 00:05 | UNI-USDT-SWAP | 6.7870 | 6.8170/6.7590 | 6.7480 | sup 6.6610 (ha 5 candles) | 0.10314 | 0.0014% | sem_zona |
| 2026-09-09 00:05 | LINK-USDT-SWAP | 12.44 | 12.52/12.43 | 12.51 | res 12.81 (ha 10 candles) | 0.13450 | 0.0059% | sem_zona |
| 2026-09-09 01:05 | BTC-USDT-SWAP | 78593.7 | 78686.8/78514.4 | 78593.7 | — | 331.42 | 0.0034% | zona_mapeada_setup_B |
| 2026-09-09 01:05 | ETH-USDT-SWAP | 2488.0 | 2492.6/2485.2 | 2488.0 | — | 15.04 | 0.0077% | zona_mapeada_setup_B |
| 2026-09-09 01:05 | SOL-USDT-SWAP | 103.23 | 103.43/102.91 | 103.23 | res 104.78 (ha 11 candles) | 0.77929 | -0.0072% | sem_zona |
| 2026-09-09 01:05 | XRP-USDT-SWAP | 1.4163 | 1.4176/1.4097 | 1.4163 | res 1.4247 (ha 3 candles) | 0.01405 | 0.0085% | sem_zona |
| 2026-09-09 01:05 | DOGE-USDT-SWAP | 0.08956 | 0.08991/0.08936 | 0.08956 | sup 0.08915 (ha 9 candles) | 0.00088 | 0.0100% | zona_mapeada_setup_B |
| 2026-09-09 01:05 | ARB-USDT-SWAP | 0.16493 | 0.16645/0.16424 | 0.16493 | — | 0.00348 | 0.0100% | sem_zona |
| 2026-09-09 01:05 | WLD-USDT-SWAP | 0.44970 | 0.45440/0.44840 | 0.44970 | res 0.49410 (ha 12 candles) | 0.00958 | 0.0053% | sem_zona |
| 2026-09-09 01:05 | SUI-USDT-SWAP | 0.80620 | 0.81090/0.80490 | 0.80620 | res 0.82370 (ha 3 candles) | 0.01162 | 0.0100% | sem_zona |
| 2026-09-09 01:05 | UNI-USDT-SWAP | 6.7880 | 6.8280/6.7480 | 6.7880 | sup 6.6610 (ha 6 candles) | 0.09500 | -0.0013% | sem_zona |
| 2026-09-09 01:05 | LINK-USDT-SWAP | 12.39 | 12.44/12.35 | 12.39 | res 12.81 (ha 11 candles) | 0.12229 | 0.0062% | sem_zona |
| 2026-09-09 02:05 | BTC-USDT-SWAP | 79136.0 | 79199.0/78593.7 | 78593.7 | — | 319.36 | 0.0040% | descartado_rr_baixo_setup_B |
| 2026-09-09 02:05 | ETH-USDT-SWAP | 2508.4 | 2513.4/2488.0 | 2488.0 | — | 14.74 | 0.0079% | invalidado_setup_B |
| 2026-09-09 02:05 | SOL-USDT-SWAP | 104.36 | 104.38/103.23 | 103.23 | res 104.78 (ha 12 candles) | 0.78786 | -0.0050% | sem_zona |
| 2026-09-09 02:05 | XRP-USDT-SWAP | 1.4359 | 1.4370/1.4163 | 1.4163 | res 1.4247 (ha 4 candles) | 0.01419 | 0.0097% | zona_mapeada_setup_A |
| 2026-09-09 02:05 | DOGE-USDT-SWAP | 0.09058 | 0.09078/0.08955 | 0.08956 | sup 0.08915 (ha 10 candles) | 0.00091 | 0.0100% | invalidado_setup_B |
| 2026-09-09 02:05 | ARB-USDT-SWAP | 0.16850 | 0.16931/0.16489 | 0.16493 | — | 0.00329 | 0.0100% | sem_zona |
| 2026-09-09 02:05 | WLD-USDT-SWAP | 0.45750 | 0.46040/0.44970 | 0.44970 | res 0.49410 (ha 13 candles) | 0.00960 | 0.0091% | sem_zona |
| 2026-09-09 02:05 | SUI-USDT-SWAP | 0.82150 | 0.82320/0.80610 | 0.80620 | res 0.82370 (ha 4 candles) | 0.01171 | 0.0100% | sem_zona |
| 2026-09-09 02:05 | UNI-USDT-SWAP | 6.9030 | 6.9190/6.7870 | 6.7880 | sup 6.6610 (ha 7 candles) | 0.09664 | -0.0051% | sem_zona |
| 2026-09-09 02:05 | LINK-USDT-SWAP | 12.58 | 12.59/12.39 | 12.39 | res 12.81 (ha 12 candles) | 0.12314 | 0.0054% | sem_zona |
| 2026-09-09 03:05 | BTC-USDT-SWAP | 78907.0 | 79377.2/78805.0 | 78593.7 | — | 327.34 | 0.0047% | zona_mapeada_setup_B |
| 2026-09-09 03:05 | ETH-USDT-SWAP | 2495.7 | 2511.0/2490.1 | 2488.0 | — | 14.68 | 0.0075% | zona_mapeada_setup_B |
| 2026-09-09 03:05 | SOL-USDT-SWAP | 104.02 | 104.68/103.65 | 103.23 | res 104.78 (ha 13 candles) | 0.77714 | -0.0040% | sem_zona |
| 2026-09-09 03:05 | XRP-USDT-SWAP | 1.4270 | 1.4364/1.4220 | 1.4163 | res 1.4247 (ha 5 candles) | 0.01360 | 0.0096% | zona_mapeada_setup_A |
| 2026-09-09 03:05 | DOGE-USDT-SWAP | 0.09005 | 0.09072/0.08979 | 0.08956 | sup 0.08915 (ha 11 candles) | 0.00089 | 0.0100% | zona_mapeada_setup_B |
| 2026-09-09 03:05 | ARB-USDT-SWAP | 0.16626 | 0.16852/0.16558 | 0.16493 | — | 0.00313 | 0.0100% | sem_zona |
| 2026-09-09 03:05 | WLD-USDT-SWAP | 0.45130 | 0.45780/0.45060 | 0.44970 | res 0.49410 (ha 14 candles) | 0.00863 | 0.0097% | sem_zona |
| 2026-09-09 03:05 | SUI-USDT-SWAP | 0.81200 | 0.82360/0.81050 | 0.80620 | res 0.82370 (ha 5 candles) | 0.01156 | 0.0100% | sem_zona |
| 2026-09-09 03:05 | UNI-USDT-SWAP | 6.8590 | 6.9120/6.8250 | 6.7880 | sup 6.6610 (ha 8 candles) | 0.09436 | -0.0057% | sem_zona |
| 2026-09-09 03:05 | LINK-USDT-SWAP | 12.50 | 12.60/12.44 | 12.39 | res 12.81 (ha 13 candles) | 0.12443 | 0.0049% | sem_zona |
| 2026-09-09 04:05 | BTC-USDT-SWAP | 79126.8 | 79275.0/78825.0 | 78593.7 | — | 330.58 | 0.0054% | descartado_rr_baixo_setup_B |
| 2026-09-09 04:05 | ETH-USDT-SWAP | 2500.0 | 2504.9/2491.2 | 2488.0 | — | 14.32 | 0.0068% | invalidado_setup_B |
| 2026-09-09 04:05 | SOL-USDT-SWAP | 104.46 | 104.73/103.93 | 103.23 | res 104.78 (ha 14 candles) | 0.74500 | -0.0036% | sem_zona |
| 2026-09-09 04:05 | XRP-USDT-SWAP | 1.4330 | 1.4402/1.4264 | 1.4163 | res 1.4247 (ha 6 candles) | 0.01278 | 0.0095% | zona_mapeada_setup_A |
| 2026-09-09 04:05 | DOGE-USDT-SWAP | 0.09041 | 0.09065/0.08993 | 0.08956 | sup 0.08936 (ha 3 candles) | 0.00086 | 0.0100% | invalidado_setup_B |
| 2026-09-09 04:05 | ARB-USDT-SWAP | 0.17220 | 0.17465/0.16619 | 0.16493 | — | 0.00343 | 0.0100% | sem_zona |
| 2026-09-09 04:05 | WLD-USDT-SWAP | 0.45510 | 0.45720/0.44910 | 0.44970 | res 0.49410 (ha 15 candles) | 0.00851 | 0.0100% | sem_zona |
| 2026-09-09 04:05 | SUI-USDT-SWAP | 0.82130 | 0.82220/0.81100 | 0.80620 | res 0.82370 (ha 6 candles) | 0.01120 | 0.0100% | sem_zona |
| 2026-09-09 04:05 | UNI-USDT-SWAP | 6.8950 | 6.9560/6.8590 | 6.7880 | sup 6.6610 (ha 9 candles) | 0.09329 | -0.0029% | sem_zona |
| 2026-09-09 04:05 | LINK-USDT-SWAP | 12.56 | 12.59/12.47 | 12.39 | res 12.81 (ha 14 candles) | 0.11743 | 0.0030% | sem_zona |
| 2026-09-09 05:05 | BTC-USDT-SWAP | 79247.4 | 79363.0/79118.8 | 79247.4 | — | 319.43 | 0.0069% | zona_mapeada_setup_B |
| 2026-09-09 05:05 | ETH-USDT-SWAP | 2509.2 | 2516.6/2498.8 | 2509.2 | — | 14.50 | 0.0044% | sem_zona |
| 2026-09-09 05:05 | SOL-USDT-SWAP | 104.52 | 105.15/104.42 | 104.52 | res 104.78 (ha 15 candles) | 0.74143 | -0.0027% | sem_zona |
| 2026-09-09 05:05 | XRP-USDT-SWAP | 1.4404 | 1.4426/1.4327 | 1.4404 | res 1.4247 (ha 7 candles) | 0.01249 | 0.0076% | zona_mapeada_setup_A |
| 2026-09-09 05:05 | DOGE-USDT-SWAP | 0.09084 | 0.09091/0.09037 | 0.09084 | sup 0.08936 (ha 4 candles) | 0.00083 | 0.0100% | zona_mapeada_setup_B |
| 2026-09-09 05:05 | ARB-USDT-SWAP | 0.17070 | 0.17235/0.16874 | 0.17070 | — | 0.00350 | 0.0100% | sem_zona |
| 2026-09-09 05:05 | WLD-USDT-SWAP | 0.45650 | 0.45830/0.45410 | 0.45650 | res 0.46040 (ha 3 candles) | 0.00794 | 0.0100% | sem_zona |
| 2026-09-09 05:05 | SUI-USDT-SWAP | 0.82280 | 0.82940/0.82050 | 0.82280 | — | 0.01092 | 0.0100% | sem_zona |
| 2026-09-09 05:05 | UNI-USDT-SWAP | 6.7990 | 6.9190/6.7680 | 6.7990 | sup 6.6610 (ha 10 candles) | 0.09964 | -0.0001% | sem_zona |
| 2026-09-09 05:05 | LINK-USDT-SWAP | 12.48 | 12.63/12.47 | 12.48 | — | 0.12007 | 0.0007% | zona_mapeada_setup_B |
| 2026-09-09 06:05 | BTC-USDT-SWAP | 79665.1 | 79744.4/79220.8 | 79247.4 | — | 317.54 | 0.0080% | invalidado_setup_B |
| 2026-09-09 06:05 | ETH-USDT-SWAP | 2518.6 | 2523.0/2509.0 | 2509.2 | — | 13.21 | 0.0036% | zona_mapeada_setup_B |
| 2026-09-09 06:05 | SOL-USDT-SWAP | 104.76 | 105.00/104.49 | 104.52 | res 104.78 (ha 16 candles) | 0.68429 | -0.0025% | sem_zona |
| 2026-09-09 06:05 | XRP-USDT-SWAP | 1.4376 | 1.4454/1.4348 | 1.4404 | res 1.4247 (ha 8 candles) | 0.01162 | 0.0065% | zona_mapeada_setup_A |
| 2026-09-09 06:05 | DOGE-USDT-SWAP | 0.09136 | 0.09139/0.09074 | 0.09084 | sup 0.08936 (ha 5 candles) | 0.00076 | 0.0081% | zona_mapeada_setup_B |
| 2026-09-09 06:05 | ARB-USDT-SWAP | 0.16970 | 0.17147/0.16887 | 0.17070 | — | 0.00344 | 0.0100% | sem_zona |
| 2026-09-09 06:05 | WLD-USDT-SWAP | 0.45680 | 0.46170/0.45480 | 0.45650 | res 0.46040 (ha 4 candles) | 0.00754 | 0.0097% | sem_zona |
| 2026-09-09 06:05 | SUI-USDT-SWAP | 0.82650 | 0.82870/0.82180 | 0.82280 | — | 0.01001 | 0.0100% | sem_zona |
| 2026-09-09 06:05 | UNI-USDT-SWAP | 6.8280 | 6.8640/6.7930 | 6.7990 | sup 6.6610 (ha 11 candles) | 0.09250 | 0.0018% | sem_zona |
| 2026-09-09 06:05 | LINK-USDT-SWAP | 12.49 | 12.51/12.46 | 12.48 | — | 0.11043 | -0.0002% | zona_mapeada_setup_B |
| 2026-09-09 07:05 | BTC-USDT-SWAP | 78920.0 | 79680.0/78860.0 | 79247.4 | — | 360.83 | 0.0087% | zona_mapeada_setup_B |
| 2026-09-09 07:05 | ETH-USDT-SWAP | 2489.5 | 2519.3/2489.0 | 2509.2 | — | 14.26 | 0.0039% | zona_mapeada_setup_B |
| 2026-09-09 07:05 | SOL-USDT-SWAP | 103.44 | 104.78/103.38 | 104.52 | res 104.78 (ha 17 candles) | 0.72786 | -0.0031% | sem_zona |
| 2026-09-09 07:05 | XRP-USDT-SWAP | 1.4194 | 1.4376/1.4186 | 1.4404 | res 1.4247 (ha 9 candles) | 0.01169 | 0.0038% | invalidado_setup_A |
| 2026-09-09 07:05 | DOGE-USDT-SWAP | 0.09005 | 0.09138/0.09001 | 0.09084 | sup 0.08936 (ha 6 candles) | 0.00081 | 0.0033% | descartado_rr_baixo_setup_B |
| 2026-09-09 07:05 | ARB-USDT-SWAP | 0.16642 | 0.17209/0.16565 | 0.17070 | — | 0.00372 | 0.0100% | sem_zona |
| 2026-09-09 07:05 | WLD-USDT-SWAP | 0.44560 | 0.45680/0.44320 | 0.45650 | res 0.46040 (ha 5 candles) | 0.00771 | 0.0063% | sem_zona |
| 2026-09-09 07:05 | SUI-USDT-SWAP | 0.80710 | 0.82690/0.80610 | 0.82280 | — | 0.01099 | 0.0100% | zona_mapeada_setup_B |
| 2026-09-09 07:05 | UNI-USDT-SWAP | 6.6490 | 6.8360/6.6380 | 6.7990 | sup 6.6610 (ha 12 candles) | 0.09893 | 0.0021% | zona_mapeada_setup_A |
| 2026-09-09 07:05 | LINK-USDT-SWAP | 12.24 | 12.49/12.19 | 12.48 | — | 0.12321 | -0.0016% | descartado_rr_baixo_setup_B |
| 2026-09-09 08:05 | BTC-USDT-SWAP | 78893.4 | 79157.2/78826.8 | 79247.4 | — | 369.14 | 0.0090% | invalidado_setup_B |
| 2026-09-09 08:05 | ETH-USDT-SWAP | 2486.6 | 2494.0/2480.9 | 2509.2 | — | 14.38 | 0.0052% | zona_mapeada_setup_B |
| 2026-09-09 08:05 | SOL-USDT-SWAP | 103.73 | 104.00/103.43 | 104.52 | res 105.15 (ha 3 candles) | 0.71429 | -0.0041% | sem_zona |
| 2026-09-09 08:05 | XRP-USDT-SWAP | 1.4219 | 1.4247/1.4179 | 1.4404 | res 1.4247 (ha 10 candles) | 0.01120 | 0.0009% | sem_zona |
| 2026-09-09 08:05 | DOGE-USDT-SWAP | 0.09072 | 0.09077/0.09004 | 0.09084 | sup 0.08936 (ha 7 candles) | 0.00079 | 0.0000% | zona_mapeada_setup_B |
| 2026-09-09 08:05 | ARB-USDT-SWAP | 0.16566 | 0.16819/0.16400 | 0.17070 | — | 0.00381 | 0.0045% | sem_zona |
| 2026-09-09 08:05 | WLD-USDT-SWAP | 0.44690 | 0.44710/0.44160 | 0.45650 | res 0.46040 (ha 6 candles) | 0.00734 | 0.0033% | sem_zona |
| 2026-09-09 08:05 | SUI-USDT-SWAP | 0.80850 | 0.81230/0.80640 | 0.82280 | — | 0.01049 | 0.0100% | zona_mapeada_setup_B |
| 2026-09-09 08:05 | UNI-USDT-SWAP | 6.6460 | 6.6760/6.5740 | 6.7990 | sup 6.6610 (ha 13 candles) | 0.10207 | 0.0062% | zona_mapeada_setup_A |
| 2026-09-09 08:05 | LINK-USDT-SWAP | 12.07 | 12.26/11.94 | 12.48 | — | 0.13843 | 0.0023% | zona_mapeada_setup_B |
| 2026-09-09 09:05 | BTC-USDT-SWAP | 79286.1 | 79367.7/78706.9 | 79286.1 | — | 401.15 | 0.0093% | zona_mapeada_setup_B |
| 2026-09-09 09:05 | ETH-USDT-SWAP | 2499.8 | 2504.8/2481.2 | 2499.8 | — | 15.42 | 0.0061% | zona_mapeada_setup_B |
| 2026-09-09 09:05 | SOL-USDT-SWAP | 104.18 | 104.27/103.24 | 104.18 | res 105.15 (ha 4 candles) | 0.74643 | -0.0029% | sem_zona |
| 2026-09-09 09:05 | XRP-USDT-SWAP | 1.4265 | 1.4283/1.4159 | 1.4265 | res 1.4454 (ha 3 candles) | 0.01139 | -0.0014% | sem_zona |
| 2026-09-09 09:05 | DOGE-USDT-SWAP | 0.09080 | 0.09091/0.09011 | 0.09080 | sup 0.08936 (ha 8 candles) | 0.00079 | -0.0020% | invalidado_setup_B |
| 2026-09-09 09:05 | ARB-USDT-SWAP | 0.16642 | 0.16695/0.16305 | 0.16642 | — | 0.00380 | 0.0016% | sem_zona |
| 2026-09-09 09:05 | WLD-USDT-SWAP | 0.45130 | 0.45140/0.44320 | 0.45130 | res 0.46170 (ha 3 candles) | 0.00725 | 0.0022% | sem_zona |
| 2026-09-09 09:05 | SUI-USDT-SWAP | 0.81230 | 0.81350/0.80170 | 0.81230 | — | 0.01066 | 0.0100% | zona_mapeada_setup_B |
| 2026-09-09 09:05 | UNI-USDT-SWAP | 6.6830 | 6.6980/6.5610 | 6.6830 | sup 6.6610 (ha 14 candles) | 0.10486 | 0.0062% | zona_mapeada_setup_A |
| 2026-09-09 09:05 | LINK-USDT-SWAP | 12.10 | 12.12/12.02 | 12.10 | — | 0.13529 | 0.0055% | zona_mapeada_setup_B |
| 2026-09-09 10:05 | BTC-USDT-SWAP | 79568.1 | 79636.6/79246.6 | 79286.1 | — | 412.81 | 0.0073% | invalidado_setup_B |
| 2026-09-09 10:05 | ETH-USDT-SWAP | 2510.4 | 2511.7/2497.2 | 2499.8 | — | 15.85 | 0.0042% | zona_mapeada_setup_B |
| 2026-09-09 10:05 | SOL-USDT-SWAP | 104.62 | 104.78/104.05 | 104.18 | res 105.15 (ha 5 candles) | 0.76286 | -0.0020% | sem_zona |
| 2026-09-09 10:05 | XRP-USDT-SWAP | 1.4362 | 1.4388/1.4250 | 1.4265 | res 1.4454 (ha 4 candles) | 0.01189 | -0.0023% | sem_zona |
| 2026-09-09 10:05 | DOGE-USDT-SWAP | 0.09131 | 0.09156/0.09063 | 0.09080 | sup 0.08936 (ha 9 candles) | 0.00081 | -0.0008% | zona_mapeada_setup_B |
| 2026-09-09 10:05 | ARB-USDT-SWAP | 0.16726 | 0.16821/0.16627 | 0.16642 | — | 0.00373 | -0.0002% | sem_zona |
| 2026-09-09 10:05 | WLD-USDT-SWAP | 0.45240 | 0.45530/0.44960 | 0.45130 | res 0.46170 (ha 4 candles) | 0.00735 | -0.0001% | sem_zona |
| 2026-09-09 10:05 | SUI-USDT-SWAP | 0.81770 | 0.82010/0.80990 | 0.81230 | — | 0.01089 | 0.0100% | invalidado_setup_B |
| 2026-09-09 10:05 | UNI-USDT-SWAP | 6.6740 | 6.7550/6.6700 | 6.6830 | sup 6.6610 (ha 15 candles) | 0.10236 | 0.0049% | descartado_rr_baixo_setup_A |
| 2026-09-09 10:05 | LINK-USDT-SWAP | 12.20 | 12.22/12.10 | 12.10 | — | 0.13900 | 0.0050% | zona_mapeada_setup_B |
| 2026-09-09 11:05 | BTC-USDT-SWAP | 79113.6 | 79649.9/79065.0 | 79286.1 | — | 442.74 | 0.0063% | zona_mapeada_setup_B |
| 2026-09-09 11:05 | ETH-USDT-SWAP | 2501.5 | 2520.4/2498.4 | 2499.8 | — | 16.86 | 0.0035% | descartado_rr_baixo_setup_B |
| 2026-09-09 11:05 | SOL-USDT-SWAP | 103.74 | 104.65/103.45 | 104.18 | res 105.15 (ha 6 candles) | 0.82429 | -0.0014% | sem_zona |
| 2026-09-09 11:05 | XRP-USDT-SWAP | 1.4283 | 1.4382/1.4219 | 1.4265 | res 1.4454 (ha 5 candles) | 0.01261 | -0.0020% | sem_zona |
| 2026-09-09 11:05 | DOGE-USDT-SWAP | 0.09030 | 0.09135/0.09012 | 0.09080 | sup 0.08936 (ha 10 candles) | 0.00088 | 0.0010% | zona_mapeada_setup_B |
| 2026-09-09 11:05 | ARB-USDT-SWAP | 0.16484 | 0.16859/0.16426 | 0.16642 | — | 0.00386 | -0.0021% | sem_zona |
| 2026-09-09 11:05 | WLD-USDT-SWAP | 0.44650 | 0.45510/0.44600 | 0.45130 | res 0.46170 (ha 5 candles) | 0.00774 | -0.0014% | sem_zona |
| 2026-09-09 11:05 | SUI-USDT-SWAP | 0.81060 | 0.81810/0.80560 | 0.81230 | — | 0.01125 | 0.0100% | zona_mapeada_setup_B |
| 2026-09-09 11:05 | UNI-USDT-SWAP | 6.6250 | 6.7260/6.6150 | 6.6830 | sup 6.6610 (ha 16 candles) | 0.10321 | 0.0056% | zona_mapeada_setup_A |
| 2026-09-09 11:05 | LINK-USDT-SWAP | 12.12 | 12.22/12.07 | 12.10 | — | 0.14614 | 0.0040% | descartado_rr_baixo_setup_B |
| 2026-09-09 12:05 | BTC-USDT-SWAP | 78927.1 | 79388.0/78837.5 | 79286.1 | — | 457.19 | 0.0065% | descartado_rr_baixo_setup_B |
| 2026-09-09 12:05 | ETH-USDT-SWAP | 2498.7 | 2513.3/2494.1 | 2499.8 | — | 17.34 | 0.0035% | zona_mapeada_setup_B |
| 2026-09-09 12:05 | SOL-USDT-SWAP | 103.42 | 104.14/103.30 | 104.18 | res 105.15 (ha 7 candles) | 0.84286 | -0.0020% | sem_zona |
| 2026-09-09 12:05 | XRP-USDT-SWAP | 1.4247 | 1.4325/1.4204 | 1.4265 | res 1.4454 (ha 6 candles) | 0.01289 | -0.0023% | sem_zona |
| 2026-09-09 12:05 | DOGE-USDT-SWAP | 0.08978 | 0.09060/0.08962 | 0.09080 | sup 0.08936 (ha 11 candles) | 0.00088 | 0.0013% | zona_mapeada_setup_B |
| 2026-09-09 12:05 | ARB-USDT-SWAP | 0.16356 | 0.16617/0.15982 | 0.16642 | — | 0.00401 | 0.0004% | sem_zona |
| 2026-09-09 12:05 | WLD-USDT-SWAP | 0.44520 | 0.45020/0.44420 | 0.45130 | res 0.46170 (ha 6 candles) | 0.00732 | -0.0015% | sem_zona |
| 2026-09-09 12:05 | SUI-USDT-SWAP | 0.80860 | 0.81520/0.80590 | 0.81230 | — | 0.01098 | 0.0092% | descartado_rr_baixo_setup_B |
| 2026-09-09 12:05 | UNI-USDT-SWAP | 6.6220 | 6.6800/6.5860 | 6.6830 | sup 6.5610 (ha 3 candles) | 0.10521 | 0.0067% | descartado_rr_baixo_setup_A |
| 2026-09-09 12:05 | LINK-USDT-SWAP | 12.07 | 12.20/12.04 | 12.10 | — | 0.14993 | 0.0036% | zona_mapeada_setup_B |
| 2026-09-09 13:05 | BTC-USDT-SWAP | 78569.3 | 79376.0/78028.0 | 78569.3 | — | 535.23 | 0.0071% | zona_mapeada_setup_B |
| 2026-09-09 13:05 | ETH-USDT-SWAP | 2489.3 | 2512.0/2468.6 | 2489.3 | — | 19.71 | 0.0045% | zona_mapeada_setup_B |
| 2026-09-09 13:05 | SOL-USDT-SWAP | 103.00 | 104.07/101.98 | 103.00 | res 104.78 (ha 3 candles) | 0.95000 | -0.0038% | sem_zona |
| 2026-09-09 13:05 | XRP-USDT-SWAP | 1.4166 | 1.4330/1.4046 | 1.4166 | res 1.4388 (ha 3 candles) | 0.01401 | -0.0029% | sem_zona |
| 2026-09-09 13:05 | DOGE-USDT-SWAP | 0.08888 | 0.09035/0.08808 | 0.08888 | sup 0.08936 (ha 12 candles) | 0.00098 | 0.0025% | zona_mapeada_setup_B |
| 2026-09-09 13:05 | ARB-USDT-SWAP | 0.15348 | 0.16455/0.15254 | 0.15348 | — | 0.00472 | 0.0004% | sem_zona |
| 2026-09-09 13:05 | WLD-USDT-SWAP | 0.43730 | 0.44930/0.43110 | 0.43730 | res 0.46170 (ha 7 candles) | 0.00817 | 0.0008% | sem_zona |
| 2026-09-09 13:05 | SUI-USDT-SWAP | 0.79410 | 0.81560/0.78330 | 0.79410 | — | 0.01259 | 0.0061% | zona_mapeada_setup_B |
| 2026-09-09 13:05 | UNI-USDT-SWAP | 6.5240 | 6.6640/6.4750 | 6.5240 | sup 6.5610 (ha 4 candles) | 0.11371 | 0.0065% | zona_mapeada_setup_A |
| 2026-09-09 13:05 | LINK-USDT-SWAP | 11.99 | 12.13/11.81 | 11.99 | — | 0.16764 | 0.0037% | zona_mapeada_setup_B |
| 2026-09-09 14:05 | BTC-USDT-SWAP | 78771.6 | 78902.4/78426.4 | 78569.3 | — | 552.02 | 0.0078% | invalidado_setup_B |
| 2026-09-09 14:05 | ETH-USDT-SWAP | 2494.9 | 2498.8/2484.0 | 2489.3 | — | 20.03 | 0.0057% | invalidado_setup_B |
| 2026-09-09 14:05 | SOL-USDT-SWAP | 103.33 | 103.47/102.68 | 103.00 | res 104.78 (ha 4 candles) | 0.95643 | -0.0035% | sem_zona |
| 2026-09-09 14:05 | XRP-USDT-SWAP | 1.4220 | 1.4225/1.4103 | 1.4166 | res 1.4388 (ha 4 candles) | 0.01416 | -0.0023% | sem_zona |
| 2026-09-09 14:05 | DOGE-USDT-SWAP | 0.08912 | 0.08937/0.08847 | 0.08888 | sup 0.08936 (ha 13 candles) | 0.00099 | 0.0038% | zona_mapeada_setup_B |
| 2026-09-09 14:05 | ARB-USDT-SWAP | 0.15124 | 0.15582/0.15105 | 0.15348 | — | 0.00487 | 0.0100% | sem_zona |
| 2026-09-09 14:05 | WLD-USDT-SWAP | 0.43410 | 0.43790/0.43010 | 0.43730 | res 0.46170 (ha 8 candles) | 0.00837 | 0.0043% | sem_zona |
| 2026-09-09 14:05 | SUI-USDT-SWAP | 0.79780 | 0.79990/0.78710 | 0.79410 | — | 0.01277 | 0.0069% | zona_mapeada_setup_B |
| 2026-09-09 14:05 | UNI-USDT-SWAP | 6.5860 | 6.5940/6.4820 | 6.5240 | sup 6.5610 (ha 5 candles) | 0.11757 | 0.0064% | zona_mapeada_setup_A |
| 2026-09-09 14:05 | LINK-USDT-SWAP | 12.01 | 12.05/11.94 | 11.99 | — | 0.16936 | 0.0021% | zona_mapeada_setup_B |
| 2026-09-09 15:05 | BTC-USDT-SWAP | 78743.9 | 78898.1/78630.8 | 78569.3 | — | 558.80 | 0.0084% | zona_mapeada_setup_B |
| 2026-09-09 15:05 | ETH-USDT-SWAP | 2493.0 | 2498.9/2487.4 | 2489.3 | — | 20.32 | 0.0074% | zona_mapeada_setup_B |
| 2026-09-09 15:05 | SOL-USDT-SWAP | 103.47 | 103.77/103.15 | 103.00 | res 104.78 (ha 5 candles) | 0.96357 | -0.0030% | sem_zona |
| 2026-09-09 15:05 | XRP-USDT-SWAP | 1.4214 | 1.4239/1.4178 | 1.4166 | res 1.4388 (ha 5 candles) | 0.01404 | -0.0009% | sem_zona |
| 2026-09-09 15:05 | DOGE-USDT-SWAP | 0.08906 | 0.08935/0.08884 | 0.08888 | sup 0.08936 (ha 14 candles) | 0.00098 | 0.0076% | zona_mapeada_setup_B |
| 2026-09-09 15:05 | ARB-USDT-SWAP | 0.15462 | 0.15500/0.15078 | 0.15348 | — | 0.00501 | 0.0100% | sem_zona |
| 2026-09-09 15:05 | WLD-USDT-SWAP | 0.43580 | 0.43770/0.43370 | 0.43730 | res 0.46170 (ha 9 candles) | 0.00823 | 0.0056% | sem_zona |
| 2026-09-09 15:05 | SUI-USDT-SWAP | 0.79900 | 0.80220/0.79510 | 0.79410 | — | 0.01285 | 0.0087% | zona_mapeada_setup_B |
| 2026-09-09 15:05 | UNI-USDT-SWAP | 6.6020 | 6.6330/6.5770 | 6.5240 | sup 6.5610 (ha 6 candles) | 0.11586 | 0.0062% | invalidado_setup_A |
| 2026-09-09 15:05 | LINK-USDT-SWAP | 11.99 | 12.05/11.97 | 11.99 | — | 0.16786 | 0.0025% | zona_mapeada_setup_B |
| 2026-09-09 16:05 | BTC-USDT-SWAP | 78388.4 | 78761.7/78374.6 | 78569.3 | — | 543.21 | 0.0100% | invalidado_setup_B |
| 2026-09-09 16:05 | ETH-USDT-SWAP | 2480.3 | 2494.8/2480.2 | 2489.3 | — | 19.55 | 0.0088% | descartado_rr_baixo_setup_B |
| 2026-09-09 16:05 | SOL-USDT-SWAP | 103.22 | 103.69/103.13 | 103.00 | res 104.78 (ha 6 candles) | 0.92143 | -0.0019% | sem_zona |
| 2026-09-09 16:05 | XRP-USDT-SWAP | 1.4166 | 1.4223/1.4158 | 1.4166 | res 1.4388 (ha 6 candles) | 0.01302 | -0.0010% | sem_zona |
| 2026-09-09 16:05 | DOGE-USDT-SWAP | 0.08854 | 0.08911/0.08851 | 0.08888 | sup 0.08808 (ha 3 candles) | 0.00094 | 0.0100% | zona_mapeada_setup_B |
| 2026-09-09 16:05 | ARB-USDT-SWAP | 0.15365 | 0.15509/0.15314 | 0.15348 | — | 0.00484 | 0.0100% | sem_zona |
| 2026-09-09 16:05 | WLD-USDT-SWAP | 0.43280 | 0.43860/0.43280 | 0.43730 | res 0.46170 (ha 10 candles) | 0.00788 | 0.0057% | sem_zona |
| 2026-09-09 16:05 | SUI-USDT-SWAP | 0.79690 | 0.80370/0.79560 | 0.79410 | — | 0.01221 | 0.0100% | descartado_rr_baixo_setup_B |
| 2026-09-09 16:05 | UNI-USDT-SWAP | 6.5930 | 6.6290/6.5840 | 6.5240 | sup 6.4750 (ha 3 candles) | 0.10964 | 0.0075% | zona_mapeada_setup_B |
| 2026-09-09 16:05 | LINK-USDT-SWAP | 11.92 | 12.01/11.91 | 11.99 | — | 0.16079 | 0.0040% | zona_mapeada_setup_B |
