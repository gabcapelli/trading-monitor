# Registro em papel — venda antes de desbloqueio de tokens

> Gerado por `monitor/unlock_paper.py`. **Nenhuma ordem é enviada.**
> Regra congelada em 23/09/2026 (repo `token-unlocks`): vender o perpétuo na abertura
> de 7 dias antes de todo desbloqueio ≥ 1% da oferta com ≥ 50% para insiders, e
> recomprar na abertura do dia do desbloqueio. **Puro** = só a venda; **com hedge** =
> venda + compra da cesta dos 20 majors. Custo 0.18% por perna e funding real.
> **Só reavaliar com 150 trades fechados.** Antes disso é ruído.

_Atualizado em 2026-10-02 (calendário de 2026-10-02)._

**Trades fechados:** 2 de 150 (1%)

**Média por trade:** puro +7.49% · com hedge +7.39% · hedge positivo em 2/2 (100%)

_Referência do backtest (2025–2026): puro +2.9%, excesso sobre o universo +2.1%._

## Abertos

| Token | Desbloqueio | % da oferta | Venda em (abertura) | Preço de entrada |
|---|---|---|---|---|
| 2Z | 2026-10-02 | 47.8% | 2026-09-25 | 0.05586 |
| EIGEN | 2026-10-02 | 4.3% | 2026-09-25 | 0.2383 |
| MAV | 2026-10-02 | 3.4% | 2026-09-25 | 0.011791 |
| ZETA | 2026-10-02 | 2.8% | 2026-09-25 | 0.05088 |
| STO | 2026-10-03 | 4.9% | 2026-09-26 | 0.04461 |

## Próximas entradas (calendário atual)

| Token | Desbloqueio | % da oferta | % insiders | Entrada prevista |
|---|---|---|---|---|
| MOVE | 2026-10-10 | 3.7% | 70% | 2026-10-03 |
| CARV | 2026-10-11 | 6.1% | 88% | 2026-10-04 |
| APT | 2026-10-12 | 1.3% | 60% | 2026-10-05 |
| BB | 2026-10-13 | 2.9% | 80% | 2026-10-06 |
| PUMP | 2026-10-13 | 1.3% | 100% | 2026-10-06 |
| SEI | 2026-10-14 | 1.6% | 89% | 2026-10-07 |
| ARB | 2026-10-16 | 1.3% | 99% | 2026-10-09 |
| VANA | 2026-10-17 | 1.7% | 78% | 2026-10-10 |
| OMNI | 2026-10-18 | 20.6% | 100% | 2026-10-11 |
| UXLINK | 2026-10-18 | 3.9% | 100% | 2026-10-11 |
| ZK | 2026-10-18 | 2.5% | 100% | 2026-10-11 |
| SOLV | 2026-10-19 | 3.4% | 68% | 2026-10-12 |
| KAITO | 2026-10-20 | 3.7% | 53% | 2026-10-13 |
| ZRO | 2026-10-21 | 3.6% | 100% | 2026-10-14 |
| APR | 2026-10-24 | 47.2% | 78% | 2026-10-17 |
| H | 2026-10-24 | 7.3% | 55% | 2026-10-17 |
| ALT | 2026-10-27 | 3.3% | 66% | 2026-10-20 |
| RESOLV | 2026-10-28 | 3.5% | 100% | 2026-10-21 |
| GUN | 2026-10-31 | 6.6% | 77% | 2026-10-24 |
| ZORA | 2026-10-31 | 2.9% | 75% | 2026-10-24 |
| EIGEN | 2026-11-01 | 4.1% | 100% | 2026-10-25 |

_Passa pelos filtros (perpétuo com ≥ 30 dias, mesmo token a ≥ 14 dias) só no dia da entrada._

## Fechados

| Token | Desbloqueio | % da oferta | Retorno do token | Cesta | Puro | Com hedge | Obs. |
|---|---|---|---|---|---|---|---|
| GUN | 2026-10-01 | 7.0% | +1.06% | +2.42% | -1.03% | +1.13% |  |
| ZORA | 2026-09-30 | 3.0% | -15.97% | -2.09% | +16.00% | +13.64% |  |
