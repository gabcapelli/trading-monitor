# Registro em papel — venda antes de desbloqueio de tokens

> Gerado por `monitor/unlock_paper.py`. **Nenhuma ordem é enviada.**
> Regra congelada em 23/09/2026 (repo `token-unlocks`): vender o perpétuo na abertura
> de 7 dias antes de todo desbloqueio ≥ 1% da oferta com ≥ 50% para insiders, e
> recomprar na abertura do dia do desbloqueio. **Puro** = só a venda; **com hedge** =
> venda + compra da cesta dos 20 majors. Custo 0.18% por perna e funding real.
> **Só reavaliar com 150 trades fechados.** Antes disso é ruído.

_Atualizado em 2026-10-25 (calendário de 2026-10-25)._

**Trades fechados:** 23 de 150 (15%)

**Média por trade:** puro +3.99% · com hedge -0.18% · hedge positivo em 10/23 (43%)

_Referência do backtest (2025–2026): puro +2.9%, excesso sobre o universo +2.1%._

## Abertos

| Token | Desbloqueio | % da oferta | Venda em (abertura) | Preço de entrada |
|---|---|---|---|---|
| ALT | 2026-10-27 | 3.3% | 2026-10-20 | 0.009214 |
| RESOLV | 2026-10-28 | 3.5% | 2026-10-21 | 0.01646 |
| GUN | 2026-10-31 | 6.6% | 2026-10-24 | 0.002115 |
| ZORA | 2026-10-31 | 2.9% | 2026-10-24 | 0.006474 |
| EIGEN | 2026-11-01 | 4.1% | 2026-10-25 | 0.2038 |

## Próximas entradas (calendário atual)

| Token | Desbloqueio | % da oferta | % insiders | Entrada prevista |
|---|---|---|---|---|
| ZETA | 2026-11-02 | 2.7% | 51% | 2026-10-26 |
| STO | 2026-11-03 | 4.7% | 61% | 2026-10-27 |
| MOVE | 2026-11-10 | 3.6% | 70% | 2026-11-03 |
| APT | 2026-11-12 | 1.3% | 60% | 2026-11-05 |
| BB | 2026-11-12 | 2.3% | 99% | 2026-11-05 |
| PUMP | 2026-11-12 | 1.3% | 100% | 2026-11-05 |
| SEI | 2026-11-14 | 1.6% | 89% | 2026-11-07 |
| ARB | 2026-11-16 | 1.3% | 99% | 2026-11-09 |
| VANA | 2026-11-17 | 1.7% | 78% | 2026-11-10 |
| ZK | 2026-11-17 | 2.4% | 100% | 2026-11-10 |
| SOLV | 2026-11-18 | 3.3% | 68% | 2026-11-11 |
| KAITO | 2026-11-20 | 3.6% | 53% | 2026-11-13 |
| ZRO | 2026-11-20 | 3.5% | 100% | 2026-11-13 |
| H | 2026-11-24 | 6.8% | 55% | 2026-11-17 |

_Passa pelos filtros (perpétuo com ≥ 30 dias, mesmo token a ≥ 14 dias) só no dia da entrada._

## Fechados

| Token | Desbloqueio | % da oferta | Retorno do token | Cesta | Puro | Com hedge | Obs. |
|---|---|---|---|---|---|---|---|
| H | 2026-10-24 | 7.3% | -0.90% | -3.48% | +0.96% | -2.76% |  |
| APR | 2026-10-24 | 47.2% | -46.90% | -3.48% | +47.07% | +43.35% |  |
| ZRO | 2026-10-21 | 3.6% | +0.10% | -0.57% | -0.15% | -0.96% |  |
| KAITO | 2026-10-20 | 3.7% | -8.70% | -0.73% | +8.70% | +7.75% |  |
| SOLV | 2026-10-19 | 3.4% | +9.75% | -8.17% | -9.72% | -18.11% |  |
| ZK | 2026-10-18 | 2.5% | -0.59% | -6.70% | +0.51% | -6.41% |  |
| UXLINK | 2026-10-18 | 3.9% | +0.00% | -6.70% | -0.18% | -7.10% |  |
| OMNI | 2026-10-18 | 20.6% | +0.00% | -6.70% | -0.18% | -7.10% |  |
| VANA | 2026-10-17 | 1.7% | -4.65% | -2.55% | +4.57% | +1.81% |  |
| ARB | 2026-10-16 | 1.3% | +13.29% | +0.36% | -13.57% | -13.41% |  |
| SEI | 2026-10-14 | 1.6% | -10.44% | -8.46% | +10.34% | +1.70% |  |
| PUMP | 2026-10-13 | 1.3% | -23.15% | -11.44% | +23.10% | +11.46% |  |
| BB | 2026-10-13 | 2.9% | -8.22% | -11.44% | +8.24% | -3.39% |  |
| APT | 2026-10-12 | 1.3% | +12.46% | -3.45% | -12.53% | -16.21% |  |
| CARV | 2026-10-11 | 6.1% | -6.44% | -5.76% | +2.18% | -3.80% |  |
| MOVE | 2026-10-10 | 3.7% | -8.44% | -6.35% | +8.09% | +1.52% |  |
| STO | 2026-10-03 | 4.9% | -5.63% | -3.73% | +5.64% | +1.65% |  |
| ZETA | 2026-10-02 | 2.8% | +0.69% | +0.45% | -0.64% | -0.46% |  |
| MAV | 2026-10-02 | 3.4% | -1.46% | -0.63% | +1.49% | +0.59% |  |
| EIGEN | 2026-10-02 | 4.3% | +3.48% | -0.63% | -3.45% | -4.35% |  |
| 2Z | 2026-10-02 | 47.8% | +1.16% | -0.63% | -3.73% | -4.62% |  |
| GUN | 2026-10-01 | 7.0% | +1.06% | +2.42% | -1.03% | +1.13% |  |
| ZORA | 2026-09-30 | 3.0% | -15.97% | -2.09% | +16.00% | +13.64% |  |

<details><summary>Descartados (1)</summary>

- SPK 2026-10-15: conhecido tarde

</details>
