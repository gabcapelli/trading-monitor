# Setup C — gabarito de order block / FVG (OTS)

> Amostra de referência pra validar detecção de OB/FVG (ex.: `smartmoneyconcepts`) antes de qualquer implementação. Extraída do export do Telegram do canal OTS (`OTS/ChatExport_2026-09-10/`, fora deste repo). Não é dado estatístico — é gabarito qualitativo: serve pra checar se um detector automático marca zona no mesmo lugar que um trade real do OTS, não pra medir edge.

## Achado sobre a fonte

Das ~21 imagens de sinais do OTS analisadas, a maioria (18) mostra só uma caixa genérica de entrada/alvo/stop desenhada **à frente do preço atual**, num espaço ainda vazio do gráfico — isso é a representação visual padrão de sinal no TradingView, não uma marcação técnica de OB/FVG. A ausência de estrutura visível na maioria das imagens não significa que o OTS não usa OB/FVG para decidir a entrada; só significa que ele geralmente limpa a marcação de análise antes de postar o print. Os exemplos abaixo são os casos em que essa marcação ficou visível.

## Exemplos genuínos (zona desenhada sobre estrutura histórica, não à frente do preço)

### 1. BTC/USDT — short, order block bearish
- Fonte: mensagem OTS de 09/09/2026 02:56 (encaminhada do canal VIP, 08/09/2026 07:08:56), `photos/photo_1451@09-09-2026_02-56-43.jpg`.
- Gráfico: BTCUSDT.P, 1h, Bybit.
- Entrada 79.220 / Alvo 78.120 / Stop 79.500.
- Estrutura: pequena consolidação (~79.300-79.500) imediatamente antes de um candle de queda impulsiva (~79.400 → ~78.700). Zona = esse bloco de consolidação, um order block bearish formado dentro do próprio movimento intradiário (não um swing de 4h maduro). Entrada no retorno à borda inferior da zona (mitigação), antes de o preço continuar caindo até o alvo (mínima da perna anterior).

### 2. BTC/USDT — compra, order block de demanda
- Fonte: mensagem "BTC/USDT Scalp BUY Setup", `photos/photo_1376@28-06-2026_12-37-16.jpg`.
- Gráfico: BTCUSDT.P, 15min, Bybit.
- Entrada limite 59.120 / Alvo 61.060 / Stop 58.388.
- Estrutura: base de consolidação clara logo antes de uma queda impulsiva de vários candles (de ~61.600 até ~58.300). Zona = essa base, um order block de demanda; compra no retorno à zona esperando reversão pra cima.

### 3. SOL/USDT — compra, order block de demanda
- Fonte: mensagem "SOL/USDT Scalp BUY Setup", `photos/photo_1381@30-06-2026_05-57-01.jpg`.
- Gráfico: SOLUSDT.P, 15min, Bybit.
- Entrada limite 71.62 / Alvo 76.46 / Stop 69.65.
- Estrutura: mesmo padrão do exemplo 2 — base de consolidação (~71.0-71.6) na origem de um rally forte (até ~76), compra no retest da zona após o preço recuar.

## Exemplo borderline (zona real, mas não é OB clássico)

### 4. OP/USDT — venda, zona de resistência por dupla rejeição
- Fonte: mensagem "OP/USDT Scalp SHORT Setup", `photos/photo_1351@01-06-2026_22-39-02.jpg`.
- Gráfico: OPUSDT.P, 15min, Binance.
- Entrada ~0.1217 / Alvo 0.1141 / Stop 0.1250.
- Estrutura: faixa horizontal (~0.1242-0.1250) testada duas vezes pelo preço (topo duplo), não uma perna impulsiva de origem. É suporte/resistência simples por rejeição, não um order block — incluído aqui como contraste, não como exemplo positivo de OB/FVG.

## Próximo passo

Rodar a detecção de OB/FVG candidata (ex. `smartmoneyconcepts`) sobre os mesmos pares/janelas de tempo dos exemplos 1-3 e comparar se ela marca zona nos mesmos lugares. Divergência grosseira aqui é motivo pra não confiar na lib sem mais investigação — não precisa de mais amostra pra essa checagem específica.

**Feito em 11/09/2026** — ver [`setup-c-testes.md`](setup-c-testes.md): backtest comparando `smartmoneyconcepts` contra detecção caseira (pivô próprio) nos 10 pares do projeto. Nenhum dos dois mostrou edge estatisticamente distinguível de zero no agregado. Cruzamento direto contra os 3 exemplos genuínos deste gabarito **confirmou** que `smc.ob` não acha order block perto da zona real em nenhum dos 3 casos (a detecção caseira de OB acertou nos 3); Setup C segue sem código em produção.
