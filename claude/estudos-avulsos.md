# Estudos avulsos — setups de terceiros testados fora dos Setups A/B/C

Testes pontuais de setups vistos em vídeo, **pré-registrados** (regras e critério escritos no docstring do script antes de baixar os dados). Nenhum deles faz parte do checklist nem do monitor de produção. Objetivo: descartar ou promover com critério objetivo, sem garimpar subconjuntos depois de ver o resultado.

Critério comum: por tempo gráfico, **PASSA** se a expectância líquida (em R, já com custo de 0.18% do nocional ida+volta convertido em R pela distância do stop) tiver **IC95 inteiro acima de zero**, bootstrap reamostrando **dias de entrada** (respeita a correlação entre pares). Só os tempos gráficos marcados "decide" contam; os demais são descritivos.

Universo final: 20 perpétuos USDT da OKX — os 10 do monitor (`PAIRS`) + BNB, TRX, ZEC, HYPE, ADA, XLM, NEAR, AVAX, LTC, BCH (`UNIVERSO` em `monitor/replay_ema_ribbon.py`). A primeira rodada (10 pares) teve o mesmo veredito; a decisão registrada é a dos 20.

## 1. Leque de médias (EMA 20–50) — 21/09/2026

Script: `monitor/replay_ema_ribbon.py` · log: `claude/ema_ribbon_20pares.log` (rodada de 10 pares: `claude/ema_ribbon.log`)

Regras em resumo: EMAs 20/25/30/35/40/45/50 empilhadas e todas subindo (baixa: espelho); candle toca a EMA20 → compra stop na máxima, arrastada para a máxima de cada candle seguinte, cancelada se um candle fechar além da EMA50; stop abaixo da primeira média não tocada no recuo; saída metade em 2R, metade em 3R. Desvios do vídeo (média por "raiz do topo", redução discricionária para 2:1) documentados no docstring.

| Tempo gráfico | Papel | n | Expectância | IC95 | % positivos |
|---|---|---|---|---|---|
| 4H (até 2000 d) | decide | 5786 | -0.099R | [-0.158, -0.040] | 32.8% |
| 1D (até 2000 d) | decide | 845 | +0.009R | [-0.118, +0.137] | 34.1% |
| 1H (300 d) | descritivo | 4056 | -0.306R | [-0.385, -0.226] | 30.8% |
| 15m (300 d) | descritivo | 16931 | -0.531R | [-0.589, -0.472] | 30.0% |

**Veredito: NÃO PASSA** (4H negativo com confiança; 1D indistinguível de zero). Custo médio vai de 0.035R no 1D a 0.54R no 15m — em prazo curto o custo sozinho inviabiliza.

Não tratar como pista: no 1D, o recorte "só 10 pares novos" dá +0.130R, IC [-0.042, +0.302], e "só vendas" +0.060R — são subconjuntos pós-hoc, com IC cruzando zero, e o recorte complementar (10 originais) é -0.097R. Promover um deles seria garimpo.

## 2. 1-2-3 de Mark Crisp — 21/09/2026

Script: `monitor/replay_123_crisp.py` (reusa fetch/cache/bootstrap do anterior) · log: `claude/123_crisp_20pares.log` (rodada de 10 pares: `claude/123_crisp.log`)

Regras em resumo: movimento 1 (≥2 fechamentos seguidos mais baixos) → movimento 2 (fechamentos mais altos, define topo 2) → movimento 3; fechar abaixo do fundo 1 cancela; compra stop na máxima do topo 2, puxada para a máxima de cada candle que fecha mais alto; stop abaixo do fundo 3 (opção preferida do autor); alvo = amplitude fundo 1→topo 2 projetada da entrada. Venda: espelho.

| Tempo gráfico | Papel | n | Expectância | IC95 | Acerto | Payoff |
|---|---|---|---|---|---|---|
| 1D (até 3000 d) | decide | 2743 | -0.112R | [-0.187, -0.036] | 29.7% | 2.14 |
| 1W (até 3000 d) | decide | 350 | -0.225R | [-0.397, -0.035] | 27.4% | 1.88 |
| 4H (até 2000 d) | descritivo | 15326 | -0.258R | [-0.292, -0.222] | 28.2% | 2.07 |
| 1H (300 d) | descritivo | 10588 | -0.428R | [-0.474, -0.381] | 29.2% | 2.01 |

**Veredito: NÃO PASSA** — negativo com confiança nos dois tempos gráficos que decidem.

O vídeo afirma 66–68% de acerto com payoff 1.3–1.4 no diário/semanal. Observado: ~30% de acerto com payoff ~2.1 (stop no fundo 3); mesmo com o stop mais largo no fundo 1 (descritivo), o acerto sobe só para ~45% e a expectância segue ≤ 0 (1D: -0.034R, IC [-0.105, +0.037]). A alegação do vídeo não se reproduz com as regras objetivadas.

## Protocolo com grade (a partir de 22/09/2026, estudos 3–5)

Quando o vídeo deixa parâmetros em aberto e testamos uma grade de combinações, o IC95 célula a célula quase garante um falso positivo. Por isso, **holdout temporal**:
1. Cada tempo gráfico é dividido no ponto médio do histórico.
2. Na **primeira metade**, escolhe-se a célula (combinação × tempo gráfico) de maior expectância líquida (n ≥ 30).
3. **Só essa célula** é testada na **segunda metade**. PASSA se o IC95 ficar inteiro acima de zero.

A grade completa fica no log, sem poder de decisão. Esses três estudos usam o cache com volume de `monitor/replay_stoch_vwap.py`; os logs estão em `claude/`.

## 3. Estocástico + bandas VWAP / MM144 ("scalp em 5 minutos") — 22/09/2026

Script: `monitor/replay_stoch_vwap.py` · log: `claude/stoch_vwap.log`

- **V1:** toque na banda VWAP (dia UTC, 1σ ou 2σ) + cruzamento do estocástico; roda no 5m e no 10m.
- **V2:** cruzamento do estocástico a favor da inclinação da MM144; roda no 2H e no 4H.
- **Comum:** entrada na abertura seguinte ou no rompimento do candle de sinal; stop no extremo do recuo; alvo 2R.
- **Grade:** estocásticos 14/8/5, somando 36 células concorrendo.

| Variante | Célula escolhida no treino | Treino | **Teste (decide)** | IC95 teste |
|---|---|---|---|---|
| V1 | 10m, st 8-3-3, 2σ, rompimento | -0.340R | **-0.428R** (n=9330) | [-0.483, -0.372] |
| V2 | 4H, st 14-3-3, MM144, rompimento | -0.103R | **-0.157R** (n=6852) | [-0.211, -0.100] |

**Veredito: NÃO PASSA** (as duas variantes). Na V1, a expectância **bruta** fica em ±0.03R em **todas** as 36 células (5m, 10m e 15m): o sinal não carrega informação. O custo (0.3–1.0R por trade) só define o tamanho do prejuízo. Na V2, o resultado bruto é levemente negativo (-0.03 a -0.10R).

## 4. 9.1 de Larry Williams (MM9, stop and reverse) — 22/09/2026

Script: `monitor/replay_91_williams.py` · log: `claude/91_williams.log`

- **Regras:** a média de 9 vira; compra stop na máxima do candle que virou; saída e reversão na perda da mínima do candle que vira a média de volta.
- **Grade:** MME9/MMA9 × sem stop/stop na mínima × sem filtro/MM50 × 1H/4H/1D/1W = 32 células.
- **Medida:** R = distância até a mínima do candle de referência. Sem stop, uma perda pode passar de -1R.

| Célula escolhida no treino | Treino | **Teste (decide)** | IC95 teste |
|---|---|---|---|
| 1D, MMA9, sem stop, sem filtro | +0.394R (IC [+0.026, +0.872]) | **+0.115R** (n=2069) | [-0.141, +0.399] |

**Veredito: NÃO PASSA.** Mesmo assim, é o único estudo até agora com uma regularidade que vale registrar. No **1D, as 8 combinações têm expectância pontual positiva nas duas metades** (+0.11 a +0.27R). No 4H ficam perto de zero; no 1H, negativas (custo).

Não tratar como edge sem teste próprio: no teste, **compras +0.541R** (IC [+0.070, +1.075]) e **vendas −0.309R** (IC [−0.508, −0.100]). Um sistema sempre posicionado cujo lucro vem só do lado comprado, num universo formado pelas moedas grandes **de hoje** (viés de sobrevivência), é compatível com simples exposição à alta do mercado (beta), não com timing. Separar as duas coisas exige outro estudo pré-registrado (ex.: 9.1 só compra no 1D contra uma linha de base de entradas comprando aleatoriamente com a mesma duração média) — não um recorte destes dados.

## 5. IFR curto no recuo ("mais de 80% de acerto") — 22/09/2026

Script: `monitor/replay_ifr_recuo.py` · log: `claude/ifr_recuo.log`

- **Regras:** só compra; MME rápida acima da lenta + IFR curto sobrevendido; entrada na abertura seguinte; stop na mínima do candle de sinal (folga zero ou 1 ATR); saída no primeiro fechamento lucrativo.
- **Grade:** médias 9×11/17×20, IFR 2/4, níveis 25/35, 2 stops, 2 saídas, 1H e 1D = 64 células.
- **Sem stop:** entra só como descritivo, em %.
- **Trades abertos no fim do histórico:** fechados a mercado, não descartados. Descartar esconderia a compra que nunca voltou ao lucro.

| Célula escolhida no treino | Treino | **Teste (decide)** | IC95 teste |
|---|---|---|---|
| 1D, MME 17×20, IFR4<25, stop na mínima, 1º lucro após 1 candle | +0.709R | **−0.134R** (n=465) | [−0.545, +0.368] |

**Veredito: NÃO PASSA.**
- **Com stop de 1 ATR no 1D:** acerto de 70–80% (perto do que o vídeo promete), mas expectância líquida entre −0.01 e +0.08R, praticamente zero.
- **Sem stop no 1D:** acerto de 92–95% e +2–3% por trade, o número do vídeo. Mas é compra sem stop, só do lado comprado, num universo com viés de sobrevivência, e o plano de risco não consegue dimensionar essa posição.
- **Stop na mínima sem folga:** às vezes o stop fica em ~0.01% da entrada, e o custo convertido em R explode (pior trade: −1580R no 1H). Refeito com o dimensionamento do plano (1% de risco, teto de 3x), a célula que decidiu dá −0.133R contra −0.134R em R puro: o teto corta as duas caudas e o veredito não muda.

## Leitura conjunta

Mesma direção do achado da auditoria v6 sobre o checklist mecânico dos Setups A/B. Nenhum dos cinco setups de vídeo tem edge mecânico demonstrável nesses 20 pares:
- **Custo:** todos pioram quanto menor o tempo gráfico, porque o custo em R cresce.
- **Sinal:** nos intraday, o resultado bruto fica em torno de zero; o sinal não carrega informação.
- **Acerto alto:** as taxas de acerto altas prometidas nos vídeos se reproduzem (1-2-3 não; IFR sim), mas vêm de ganhos pequenos e perdas grandes, e não de edge.

A única regularidade, o 9.1 no diário, aparece só no lado comprado e ainda não se distingue de beta.

Não reabrir esses testes sem uma regra nova pré-registrada. Variar parâmetro sobre estes mesmos dados até algo ficar positivo invalida o critério.
