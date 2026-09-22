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

**Atualizações do protocolo (valem para os estudos seguintes; os anteriores não são refeitos):**
- **Confirmação fora da amostra** (desde o estudo 8): a célula escolhida também precisa ter IC95 > 0 nos 80 pares de `replay_91_beta.UNIVERSO_B`. PASSA só se as duas etapas passarem.
- **Mínimo de n ≥ 200 trades no treino** para uma célula concorrer (decidido em 22/09/2026, depois do estudo 9). No estudo 9, o mínimo de 30 deixou uma célula semanal com 40 trades vencer por sorte. A alternativa — seleção separada por tempo gráfico com o erro dividido entre eles — foi descartada por tirar poder justamente do diário, que tem mais dados. Se nenhuma célula tiver n ≥ 200 no treino, o estudo não tem amostra para decidir e é registrado assim, não como NÃO PASSA.

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

## 6. 9.1 — follow-up: timing ou beta? — 22/09/2026

Script: `monitor/replay_91_beta.py` · log: `claude/91_beta.log`

**Pergunta:** as compras do 9.1 rendem mais do que compras em datas aleatórias no mesmo par, com a mesma duração?

- **Regra:** uma só, o original (MME9, sem stop, sem filtro).
- **Linha de base:** 500 compras aleatórias por trade.
- **Excesso:** retorno bruto do 9.1 − 0.10% de margem de slippage − média da linha de base.
- **Por que a margem:** no teste sintético, o simulador preenche a ordem stop exatamente no gatilho e ganha ~0.3% por trade num passeio aleatório; o viés some com caminhos intra-candle mais finos.
- **Quem decide:** o **universo B**, com 80 perpétuos USDT de cripto da OKX listados há ≥ 1000 dias, **fora dos 20**. O universo A (os 20 de sempre, 18 com ≥ 1000 dias) é só descritivo.

| | Universo B (decide) | Universo A (descritivo) |
|---|---|---|
| **Compras: excesso sobre aleatório** | **+0.29%**, IC [−0.83, +1.46] | +0.90%, IC [−0.48, +2.38] |
| Compras: retorno absoluto (custo + funding) | +0.25%, IC [−0.88, +1.44] | +2.23%, IC [+0.76, +3.80] |
| Vendas: excesso sobre aleatório | +0.48%, IC [−0.39, +1.40] | +1.08%, IC [+0.15, +2.04] |
| Vendas: retorno absoluto | +0.12% | −0.75% |

**Veredito: NÃO PASSA.**

- **De onde vinha o resultado do A:** no universo onde a hipótese nasceu, ~2/3 do retorno bruto das compras (+2.65%) é o que uma compra aleatória de mesma duração também faria. Era sobretudo beta das moedas que sobreviveram e subiram.
- **Fora da amostra:** nos 80 pares, as compras do 9.1 **nem sequer ganham em termos absolutos** com confiança (+0.25%).
- **O que sobra:** as estimativas pontuais de excesso são positivas nos dois universos e nos dois lados. Isso é compatível com algum timing de seguidor de tendência, de no máximo ~1% por trade, mas não está demonstrado.
- **Poder do teste:** o IC no B tem ±1.1% de largura (os 80 pares se movem juntos, e o bootstrap é por dia), então o teste não detecta excesso menor que ~1% por trade.

Não há como estreitar isso com estes dados. O que resta é paper trade daqui para frente, se valer a pena.

## 7. Renko + VWAP ("um dos melhores sistemas de daytrade") — 22/09/2026

Script: `monitor/replay_renko_vwap.py` · log: `claude/renko_vwap.log`

O vídeo é quase todo um relato de um dia de operações; o setup Renko ocupa ~2 minutos e não diz o tamanho do tijolo. Versão objetivada:
- **Renko:** percentual, construído com os fechamentos de 5m (reversão de 2 tijolos).
- **Sinal:** tijolo de baixa cuja faixa contém a VWAP diária, seguido de tijolo de reversão.
- **Entrada:** no fechamento que completa a reversão.
- **Stop:** na base do tijolo de baixa.
- **Alvo:** a amplitude do padrão, em 1× ou 1.618×.
- **Grade:** tijolo 0.3/0.5/1% = 6 células, 300 dias, 20 pares.

"Parede de proteção" e "falha de rompimento" não foram testadas: dependem de gap e do primeiro candle do pregão, que cripto não tem.

| Célula escolhida no treino | Treino | **Teste (decide)** | IC95 teste |
|---|---|---|---|
| tijolo 1.0%, alvo 1× | −0.124R | **−0.106R** (n=1056) | [−0.186, −0.026] |

**Veredito: NÃO PASSA.**
- **Sinal:** o bruto fica entre −0.04 e +0.01R em todas as células; o padrão não carrega informação.
- **VWAP:** o mesmo padrão **sem** a condição da VWAP dá resultado igual. A VWAP não acrescenta nada.
- **Custo:** 0.08R com tijolo de 1%, 0.25R com tijolo de 0.3%.

## 8. Inside bar + estocástico lento (tendência e "V15") — 22/09/2026

Script: `monitor/replay_inside_bar.py` · log: `claude/inside_bar.log`

- **Sinal:** inside bar com o estocástico lento abaixo de 20 (compra) ou acima de 80 (venda).
- **Entrada e stop:** entrada por stop no rompimento, válida só no candle seguinte; stop no outro extremo do inside bar.
- **Contextos:**
  - *tendência*: MMA80 a favor, no 1D e no 1W.
  - *V15*: o sinal de calendário do vídeo; perto do dia 15 ou do dia 1º, depois de a quinzena ter andado contra; só no 1D.
- **Alvos:** 2R, topo anterior (máxima de 20 candles) ou banda de Bollinger(20,2).
- **Grade:** 3 estocásticos, somando 27 células.
- **Critério:** holdout **e** confirmação obrigatória nos 80 pares fora da amostra.

| Célula escolhida no treino | Treino | 1) Teste (2ª metade) | 2) 80 pares fora da amostra |
|---|---|---|---|
| V15, 1D, st 8-3-3, alvo topo | +0.457R (n=90) | **+0.197R**, IC [−0.227, +0.664] | **−0.150R**, IC [−0.402, +0.133] |

**Veredito: NÃO PASSA** — nenhuma das duas etapas.
- **V15:** o +0.197R da 2ª metade, com n=181 e acerto de 21%, não se sustenta; nos 80 pares o acerto cai para 13% e a expectância fica negativa.
- **Semanal:** as células têm n de 22 a 45, pouco demais para ler qualquer coisa.

### Viés do simulador encontrado aqui — afeta estudos anteriores

Até o estudo 7, os scripts usavam a regra "conservadora": no candle da entrada, qualquer toque no stop conta como perda.

- **O problema:** quando a entrada é por ordem **stop** e o stop está a menos de um candle de distância, essa regra é enviesada contra o trade. Muitas vezes o preço tocou o stop **antes** de acionar a entrada.
- **Medida:** num passeio aleatório com caminho intra-candle fino (480 passos), a regra conservadora dá **−0.13 a −0.21R** bruto no inside bar; a heurística OHLC (candle a favor: extremo contra antes do gatilho; candle contra: o inverso) dá **−0.01 a +0.04R**, dentro do ruído. Daqui em diante, OHLC.
- **Quem não é afetado:** entrada na abertura (IFR, `abertura` do estocástico+VWAP), entrada no fechamento (Renko) e sem stop (9.1 original, estudo 6). Nesses casos, qualquer toque no stop depois da entrada é perda de fato.
- **Afetados, com viés negativo:** leque de médias (1), 1-2-3 (2), células `rompimento` do estocástico+VWAP (3) e variante `stop=minima` do 9.1 (4). O tamanho depende da distância entre gatilho e stop em relação ao candle. Refeitos logo abaixo.

### Reexecução dos estudos 1–4 com a regra corrigida — 22/09/2026

A regra agora fica num lugar só: `stop_vale_no_candle_entrada` em `monitor/replay_ema_ribbon.py`, padrão OHLC; `REGRA_CANDLE_ENTRADA=conservadora` reproduz a antiga.

- **Mesmos dados nas duas rodadas:** os estudos 1 e 2 passaram a ler o cache com volume, porque o cache original não estava nesta máquina. Cada estudo rodou duas vezes nesses dados, uma com cada regra, então a diferença é só a regra. A regra antiga nos dados novos reproduz os números originais (ex.: 1-2-3 1D, n=2743, −0.112R).
- **Critérios:** os pré-registrados, inalterados. É correção de bug, não mudança de regra.
- **Logs novos:** `*_ohlc.log`. Os antigos ficam como histórico.

| Estudo | Regra antiga | **Regra OHLC** | IC95 (OHLC) | Veredito |
|---|---|---|---|---|
| 1. Leque, 4H | −0.099R | −0.045R | [−0.106, +0.017] | não passa |
| 1. Leque, 1D | +0.015R | +0.058R | [−0.069, +0.192] | não passa |
| 2. 1-2-3, 1D | −0.112R | **+0.078R** | [−0.004, +0.160] | não passa (no limite) |
| 2. 1-2-3, 1W | −0.225R | −0.107R | [−0.285, +0.085] | não passa |
| 3. Estocástico+VWAP V1 (teste) | −0.428R | −0.407R | [−0.462, −0.352] | não passa |
| 3. Estocástico+MM144 V2 (teste) | −0.157R | −0.081R | [−0.140, −0.021] | não passa |
| 4. 9.1 (célula escolhida, sem stop) | +0.115R | +0.115R | não afetada | não passa |

Nos intraday descritivos, a correção melhora bastante, mas continua negativo (1-2-3 4H: −0.258 → −0.057R; 1H: −0.428 → −0.264R). No 9.1 com stop, as células do 1D sobem para +0.17 a +0.28R, parecidas com as sem stop — valem as mesmas ressalvas de beta do estudo 6.

**1-2-3 no diário — confirmação fora da amostra** (pré-registrada antes de rodar, no docstring de `replay_123_crisp.py`): a mesma regra, sem mudança, nos 80 pares do estudo 6. Log: `claude/123_crisp_fora_amostra.log`.

| | n | Expectância | IC95 |
|---|---|---|---|
| **80 pares fora da amostra** | 8991 | **+0.043R** | [−0.026, +0.115] |
| só compras | 4993 | −0.011R | [−0.111, +0.088] |
| só vendas | 3998 | +0.110R | [+0.005, +0.219] |

**Não passa.** O resultado no limite dos 20 pares encolhe fora da amostra. Não tratar "só vendas" como pista: é um recorte depois de ver o resultado, e nos 20 pares eram as compras que iam melhor.

## 9. Pullback de Dave Landry ("Setup de Swing Trade") — 22/09/2026

Script: `monitor/replay_landry.py` · log: `claude/landry.log`

- **Tendência:** MMA21 subindo (original) ou MMA 9, 20 e 50 subindo juntas (a modificação do autor).
- **Sinal:** candle com mínima abaixo das mínimas dos 2 anteriores.
- **Ordem:** compra stop na máxima, stop na mínima, alvo 2R. A cada novo sinal, a ordem desce para o candle novo; cancela se a média virar.
- **Candle sem sinal e sem acionamento:** duas leituras — a ordem persiste, ou cai (1 candle).
- **Grade e critério:** 1D e 1W, 8 células; holdout **e** confirmação nos 80 pares.
- **Validação:** passeio aleatório com caminho fino dá bruto −0.006 a +0.025R e acerto ~33% (o esperado para 2R sem edge).

| Célula escolhida no treino | Treino | 1) Teste (2ª metade) | 2) 80 pares fora da amostra |
|---|---|---|---|
| 1W, 9-20-50, 1 candle | +0.338R (**n=40**) | **−0.122R**, IC [−0.520, +0.340] | **−0.097R**, IC [−0.343, +0.160] |

**Veredito: NÃO PASSA.**
- **Diário (grade descritiva):** o original (MMA21) fica levemente positivo, +0.02 a +0.05R líquido, nas duas metades (n≈2.500) — pequeno demais para distinguir de zero.
- **Acerto:** 33–36%, não os ~50% do vídeo; no semanal, 28–35%, não os ~68%.
- **4H e 1H:** o bruto fica em +0.01 a +0.05R, e o custo (0.10–0.28R) o transforma em negativo.

**Falha de protocolo exposta aqui:** o mínimo de n ≥ 30 na seleção deixou uma célula semanal com 40 trades vencer diárias com ~1.000. Com amostra tão pequena, a "melhor" célula é quase sempre a de mais sorte. O holdout pegou (−0.122R), mas o teste foi gasto numa célula ruim.

**Proposta para os próximos estudos (a decidir antes de rodar):** mínimo de n ≥ 200 no treino para concorrer, ou seleção separada por tempo gráfico.

## 10. 123 de três candles (contexto MM8/MM80) — 22/09/2026

Script: `monitor/replay_123_candles.py` · log: `claude/123_candles.log`

Não é o 1-2-3 do Crisp (estudo 2); aqui o padrão tem exatamente 3 candles.
- **Padrão de compra:** a mínima do candle 2 fica abaixo da do 1 e da do 3; compra stop na máxima do candle 3, válida no candle seguinte.
- **Stops (as 3 opções do vídeo):** mínima do candle 3; mínima do candle 2; mínima do candle 2 menos a amplitude do padrão.
- **Alvo:** 1× ou 1.618× a amplitude dos 3 candles.
- **Contexto:** *tendência* (MME80 inclinada a favor e candle 3 do lado certo dela) ou *tendência + MM8* (também MME8 a favor, com os 3 candles fechando além dela — o "123 fantástico", fora da "zona neutra").
- **Grade e critério:** 1D e 4H, 24 células, primeiro estudo com **n ≥ 200** na seleção (as 24 atingiram); holdout **e** 80 pares.
- **Validação:** passeio aleatório com caminho fino dá bruto −0.02 a +0.035R.

| Célula escolhida no treino | Treino | 1) Teste (2ª metade) | 2) 80 pares fora da amostra |
|---|---|---|---|
| 1D, tendência+MM8, stop no candle 2, alvo 1.618× | +0.095R (n=411) | **+0.007R**, IC [−0.143, +0.157] | **−0.017R**, IC [−0.117, +0.083] |

**Veredito: NÃO PASSA.**
- **Diário:** todas as 12 combinações ficam entre −0.01 e +0.05R líquido — o mesmo "levemente positivo, indistinguível de zero" do Landry e do 1-2-3 corrigido.
- **Contexto da MM8:** não acrescenta nada; os resultados com e sem ela são parecidos.
- **4H:** o bruto fica em 0 a +0.09R, e o custo (0.03–0.12R) deixa tudo negativo.
- **Semanal (descritivo):** todas as combinações negativas.
- **Acerto:** vai de 28% (stop curto, alvo longo) a 65% (stop amplo, alvo 1×) sem mudar a expectância. É o trade-off que o vídeo descreve, sem edge por trás.

## 11. Agulhada do Didi — 22/09/2026

Script: `monitor/replay_didi.py` · log: `claude/didi.log`

- **Agulhada:** Didi Index (MMA3/MMA8 e MMA20/MMA8); a curta cruza 1 para cima e a longa para baixo, com 1 candle de tolerância.
- **Confirmações** (os "quatro indicadores sincronizados"): Bollinger(8,2) abrindo, TRIX(9) acima do sinal, estocástico lento (8,3,3) — testadas isoladas, todas juntas e nenhuma.
- **Entrada:** abertura do candle seguinte. **Stop:** mínima do candle da agulhada (o vídeo não define stop). **Saída:** 2R ou quando a agulhada se desfaz.
- **Grade:** 1D e 4H, 20 células; 1H descritivo.

| | n | Expectância | IC95 |
|---|---|---|---|
| Treino — **melhor** célula da grade (4H, Bollinger, 2R) | 536 | **−0.232R** | [−0.440, −0.006] |
| Teste (2ª metade) | 698 | **−0.036R** | [−0.179, +0.109] |

**Veredito: NÃO PASSA** pelo holdout. A confirmação nos 80 pares não chegou a rodar (exigia baixar o 4H desses pares, ~1h20; interrompido, já que o veredito estava decidido).

- **Único estudo em que a melhor célula do treino já era negativa.** Nos anteriores a vencedora sempre parecia positiva por sorte e morria no teste.
- **O motivo é o custo:** o bruto fica em −0.05 a +0.15R e o custo sozinho é de 0.19R no 4H e 0.43–0.62R no 1H. O stop na mínima do candle da agulhada é curtíssimo, e 0.18% de custo vira um R inteiro.
- **Lookahead corrigido antes de rodar:** a tolerância de 1 candle aceitava o cruzamento da linha longa no candle seguinte, que ainda não fechou quando a entrada acontece na abertura dele. Num passeio aleatório isso dava +0.17 a +0.38R de vantagem falsa; corrigido (o sinal vale no último dos dois cruzamentos), o viés some. **Vale como alerta para os próximos estudos:** qualquer "tolerância de N candles" precisa ser checada nesse sentido.
- **Sinal raro:** ~22 agulhadas em 2.456 candles diários do BTC; só 10 das 20 células chegaram a n ≥ 200 no treino.

## Leitura conjunta

Mesma direção do achado da auditoria v6 sobre o checklist mecânico dos Setups A/B. Nenhum dos dez setups de vídeo tem edge mecânico demonstrável nesses 20 pares (o 9.1 também não, fora da amostra, nos 80 pares do estudo 6):
- **Regra do candle da entrada:** vale com a regra corrigida (reexecução acima). O mais perto de passar foi o 1-2-3 no diário, que não se confirmou nos 80 pares.
- **Custo:** todos pioram quanto menor o tempo gráfico, porque o custo em R cresce.
- **Sinal:** nos intraday, o resultado bruto fica em torno de zero; o sinal não carrega informação.
- **Acerto alto:** as taxas de acerto altas prometidas nos vídeos se reproduzem (1-2-3 não; IFR sim), mas vêm de ganhos pequenos e perdas grandes, e não de edge.

A única regularidade, o 9.1 no diário, vinha sobretudo de beta. Fora da amostra, nem o retorno absoluto se sustenta. Se existir algum timing, ele fica abaixo do que estes dados conseguem detectar (~1% por trade).

Não reabrir esses testes sem uma regra nova pré-registrada. Variar parâmetro sobre estes mesmos dados até algo ficar positivo invalida o critério.
