# Registro em papel — venda antes de desbloqueio de tokens

> Gerado por `monitor/unlock_paper.py`. **Nenhuma ordem é enviada.**
> Regra congelada em 23/09/2026 (repo `token-unlocks`): vender o perpétuo na abertura
> de 7 dias antes de todo desbloqueio ≥ 1% da oferta com ≥ 50% para insiders, e
> recomprar na abertura do dia do desbloqueio. **Puro** = só a venda; **com hedge** =
> venda + compra da cesta dos 20 majors. Custo 0.18% por perna e funding real.
> **Só reavaliar com 150 trades fechados.** Antes disso é ruído.

_Atualizado em 2026-10-09 (calendário de 2026-10-09)._

**Trades fechados:** 7 de 150 (5%)

**Média por trade:** puro +2.04% · com hedge +1.08% · hedge positivo em 4/7 (57%)

_Referência do backtest (2025–2026): puro +2.9%, excesso sobre o universo +2.1%._

## Abertos

| Token | Desbloqueio | % da oferta | Venda em (abertura) | Preço de entrada |
|---|---|---|---|---|
| MOVE | 2026-10-10 | 3.7% | 2026-10-03 | 0.009912 |
| CARV | 2026-10-11 | 6.1% | 2026-10-04 | 0.04427 |
| APT | 2026-10-12 | 1.3% | 2026-10-05 | 0.8008 |
| BB | 2026-10-13 | 2.9% | 2026-10-06 | 0.009883 |
| PUMP | 2026-10-13 | 1.3% | 2026-10-06 | 0.006463 |
| SEI | 2026-10-14 | 1.6% | 2026-10-07 | 0.07194 |
| ARB | 2026-10-16 | 1.3% | 2026-10-09 | 0.17263 |

## Próximas entradas (calendário atual)

| Token | Desbloqueio | % da oferta | % insiders | Entrada prevista |
|---|---|---|---|---|
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
| ZETA | 2026-11-02 | 2.7% | 51% | 2026-10-26 |
| STO | 2026-11-03 | 4.7% | 61% | 2026-10-27 |

_Passa pelos filtros (perpétuo com ≥ 30 dias, mesmo token a ≥ 14 dias) só no dia da entrada._

## Fechados

| Token | Desbloqueio | % da oferta | Retorno do token | Cesta | Puro | Com hedge | Obs. |
|---|---|---|---|---|---|---|---|
| STO | 2026-10-03 | 4.9% | -5.63% | -3.73% | +5.64% | +1.65% |  |
| ZETA | 2026-10-02 | 2.8% | +0.69% | +0.45% | -0.64% | -0.46% |  |
| MAV | 2026-10-02 | 3.4% | -1.46% | -0.63% | +1.49% | +0.59% |  |
| EIGEN | 2026-10-02 | 4.3% | +3.48% | -0.63% | -3.45% | -4.35% |  |
| 2Z | 2026-10-02 | 47.8% | +1.16% | -0.63% | -3.73% | -4.62% |  |
| GUN | 2026-10-01 | 7.0% | +1.06% | +2.42% | -1.03% | +1.13% |  |
| ZORA | 2026-09-30 | 3.0% | -15.97% | -2.09% | +16.00% | +13.64% |  |
