# Registro em papel — venda antes de desbloqueio de tokens

> Gerado por `monitor/unlock_paper.py`. **Nenhuma ordem é enviada.**
> Regra congelada em 23/09/2026 (repo `token-unlocks`): vender o perpétuo na abertura
> de 7 dias antes de todo desbloqueio ≥ 1% da oferta com ≥ 50% para insiders, e
> recomprar na abertura do dia do desbloqueio. **Puro** = só a venda; **com hedge** =
> venda + compra da cesta dos 20 majors. Custo 0.18% por perna e funding real.
> **Só reavaliar com 150 trades fechados.** Antes disso é ruído.

_Atualizado em 2026-10-13 (calendário de 2026-10-13)._

**Trades fechados:** 12 de 150 (8%)

**Média por trade:** puro +3.61% · com hedge -0.24% · hedge positivo em 6/12 (50%)

_Referência do backtest (2025–2026): puro +2.9%, excesso sobre o universo +2.1%._

## Abertos

| Token | Desbloqueio | % da oferta | Venda em (abertura) | Preço de entrada |
|---|---|---|---|---|
| SEI | 2026-10-14 | 1.6% | 2026-10-07 | 0.07194 |
| ARB | 2026-10-16 | 1.3% | 2026-10-09 | 0.17263 |
| VANA | 2026-10-17 | 1.7% | 2026-10-10 | 1.0484 |
| OMNI | 2026-10-18 | 20.6% | 2026-10-11 | 4.274 |
| UXLINK | 2026-10-18 | 3.9% | 2026-10-11 | 0.0729 |
| ZK | 2026-10-18 | 2.5% | 2026-10-11 | 0.015167 |
| SOLV | 2026-10-19 | 3.4% | 2026-10-12 | 0.004144 |
| KAITO | 2026-10-20 | 3.7% | 2026-10-13 | 0.3034 |

## Próximas entradas (calendário atual)

| Token | Desbloqueio | % da oferta | % insiders | Entrada prevista |
|---|---|---|---|---|
| ZRO | 2026-10-21 | 3.6% | 100% | 2026-10-14 |
| APR | 2026-10-24 | 47.2% | 78% | 2026-10-17 |
| H | 2026-10-24 | 7.3% | 55% | 2026-10-17 |
| ALT | 2026-10-27 | 3.3% | 66% | 2026-10-20 |
| RESOLV | 2026-10-28 | 3.5% | 100% | 2026-10-21 |
| GUN | 2026-10-31 | 6.6% | 77% | 2026-10-24 |
| ZORA | 2026-10-31 | 2.9% | 75% | 2026-10-24 |
| EIGEN | 2026-11-01 | 4.1% | 100% | 2026-10-25 |
| ZETA | 2026-11-02 | 2.7% | 51% | 2026-10-26 |
| STO | 2026-11-03 | 4.7% | 61% | 2026-10-27 |
| MOVE | 2026-11-10 | 3.6% | 70% | 2026-11-03 |
| APT | 2026-11-12 | 1.3% | 60% | 2026-11-05 |
| BB | 2026-11-12 | 2.3% | 99% | 2026-11-05 |
| PUMP | 2026-11-12 | 1.3% | 100% | 2026-11-05 |

_Passa pelos filtros (perpétuo com ≥ 30 dias, mesmo token a ≥ 14 dias) só no dia da entrada._

## Fechados

| Token | Desbloqueio | % da oferta | Retorno do token | Cesta | Puro | Com hedge | Obs. |
|---|---|---|---|---|---|---|---|
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
