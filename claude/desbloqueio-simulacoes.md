# Desbloqueio de tokens: resumo das simulações (10/11/2026)

Base: 31 trades fechados do registro em papel (de 23/09 a 10/11/2026).
Resultado real, sem nenhuma regra extra: média de **+4,68%** por trade (venda pura).

## 1. Stop de preço

Testei parar a venda quando o preço sobe X% acima da entrada.

| Stop | Trades parados | Média por trade |
|---|---|---|
| Sem stop | 0 | +4,68% |
| 5% | 21 de 31 | +0,27% |
| 10% | 14 de 31 | +0,41% |
| 20% | 6 de 31 | +0,37% |

**Resultado:** o stop piora tudo. Os tokens costumam subir antes do desbloqueio e cair depois. O ALT subiu 70% e fechou com +20,7% para quem vendeu. O stop corta o trade na pior hora.

## 2. Limite de capital por token

Testei usar de 2% a 20% do capital em cada token.

| Capital por token | Retorno | Maior queda (drawdown) |
|---|---|---|
| 2% | +2,9% | 1,8% |
| 5% | +7,3% | 4,6% |
| 10% | +14,5% | 9,2% |
| 20% | +29,0% | 18,4% |

**Resultado:** retorno e queda sobem juntos, na mesma proporção. O limite não melhora nada, só define o tamanho do risco. Chegaram a 9 posições abertas ao mesmo tempo, e o pior caso (token que sobe 50% a 70% antes de cair) pesa mais que o pior trade real.

## 3. Tamanho pela porcentagem desbloqueada

Testei posições maiores ou menores conforme o desbloqueio é grande ou pequeno.

**Resultado:** não há relação (correlação −0,07). Nenhuma regra venceu o tamanho igual. A regra "maior nos desbloqueios pequenos" dobrou a queda máxima (8,1%). O grupo de desbloqueios grandes (20% ou mais) tem só 3 trades, e um deles (APR, +47%) explica o bom resultado do grupo.

## Pontos de atenção

- **Amostra pequena:** 31 trades em cerca de 7 semanas de mercado em queda. O protocolo pede 150 trades para reavaliar.
- **Um caso pesa muito:** sem o APR, o retorno cai de +7,3% para cerca de +4,9% (com 5% por token).
- **Hedge:** o resultado com hedge fica perto de zero (+0,62%), então boa parte do ganho do "puro" vem da queda geral do mercado.
- **Testes sobre os mesmos dados:** várias regras testadas sobre a mesma amostra aumentam o risco de ajuste fino.
- **Dados faltando:** 6 de 217 arquivos de candles não existiam (EIGEN, GUN, STO, ZETA e MOVE).

## Conclusão

Nenhuma das três regras melhorou a estratégia. **Stop prejudica, limite por token só muda a escala e dimensionar pelo tamanho do desbloqueio não tem base nos dados.** O que sobra para controlar risco é o **tamanho da posição**: usar tamanho igual por token e algo por volta de 2% do capital, calculado pelo pior caso. Antes de decidir qualquer coisa com dinheiro real, esperar os 150 trades.
