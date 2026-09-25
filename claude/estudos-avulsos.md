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
- **Bootstrap por bloco de semana** (não por dia) quando a duração média do trade passar de ~5 dias, e **teste de beta obrigatório** (excesso sobre entrada aleatória de mesma duração, mesmo par e mesmo lado) antes de declarar PASSA em qualquer estratégia direcional. Ambos decididos em 22/09/2026, depois de o estudo 13 passar no critério antigo e cair nos dois testes.
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

## 12. 1-2-3 do Crisp — follow-up: custo fiel, carteira e 3ª amostra — 22/09/2026

Script: `monitor/replay_123_carteira.py` · log: `claude/123_carteira.log`

**Não varre nenhum parâmetro do setup.** As regras do estudo 2 ficam intactas. Duas mudanças de mecanismo, decididas antes de rodar, mais uma amostra nova.

**Universo C (novo, decide):** perpétuos USDT de cripto da OKX listados há 400–1000 dias, fora de A e B → 83 pares. Ressalva: moedas recentes, muitas memecoins, histórico só de 2024–2026.

| Amostra | n | Expectância (custo fiel) | IC95 |
|---|---|---|---|
| A (20 pares, in-sample) | 2576 | +0.073R | [−0.011, +0.157] |
| B (80 pares) | 8991 | +0.044R | [−0.025, +0.116] |
| **C (83 novos, decide)** | 3451 | **+0.073R** | **[−0.022, +0.170]** |

**Veredito: NÃO PASSA** — terceira amostra positiva, IC ainda cruzando zero. As três estimativas pontuais positivas (+0.073, +0.044, +0.073) são consistentes, mas os períodos se sobrepõem e os pares são correlacionados, então não são três evidências independentes.

**1. Custo por tipo de saída (entrada taker 0.05%+0.05% slippage; saída no alvo maker 0.02% sem slippage; saída no stop taker).** Efeito: **+0.001 a +0.002R**, desprezível. O custo já era pequeno no diário (0.03–0.04R). Fica registrado: **não há ganho relevante a extrair do modelo de custo neste tempo gráfico** — ao contrário do intraday, onde o custo é o que mata.

**2. Carteira (1% de risco, 3x, 2 posições, trava −6R/semana, 200 sorteios da ordem dos sinais do mesmo dia):**

| Amostra | Período | Patrimônio (mediana) | CAGR | Drawdown mediano |
|---|---|---|---|---|
| A | 6.7 anos | 1.90× (p5 1.29 – p95 2.81) | +10.1%/ano | 27% |
| B | 6.7 anos | 1.37× (p5 0.81 – p95 2.10) | +4.8%/ano | 37% |
| C | 2.7 anos | 1.33× (p5 0.87 – p95 1.85) | +10.9%/ano | 19% |

**3. Mapa risco × posições (descritivo, bloco 4 do log).** Mais posições simultâneas aumentam CAGR e drawdown quase na mesma proporção, e reduzem a dispersão entre sorteios (menos dependência de qual sinal chegou primeiro). Ex. no universo A com 1% de risco: 1 posição → +5.4%/ano com DD 19%; 2 → +10.1% com DD 27%; 4 → +18.9% com DD 41%; 6 → +21.5% com DD 55%. **Escolher aqui o ponto de maior retorno seria ajuste a dados** — a escolha é do operador, pelo drawdown que tolera, e todos esses números pressupõem um edge que não está demonstrado.

### Amostras disponíveis e como estão sendo gastas

Amostra limpa é recurso finito. Situação em 22/09/2026:

| Amostra | O que é | Estado |
|---|---|---|
| A — 20 pares OKX | onde tudo nasceu | in-sample, gasta |
| B — 80 pares OKX | listados há ≥1000 dias, fora de A | gasta no 9.1 (estudo 6), inside bar (8), Landry (9), 123 de candles (10) e 1-2-3 (reexecução) |
| C — 83 pares OKX | listados há 400–1000 dias | gasta neste estudo |
| **D — 215 perps só da Binance** | não existem na OKX, ≥400 dias | **ainda limpa** |
| Paper trade | daqui para frente | único teste realmente fora da amostra no tempo |

**Infra da Binance** (`monitor/dados_binance.py`, criada em 22/09/2026): mesma interface de `baixar`, cache em `cache_binance/`, aceita os `instId` da OKX. Os 20 pares de A já estão baixados no diário.

**Atenção ao usar a Binance:** os *mesmos* pares na Binance **não são amostra independente** — é o mesmo mercado, no mesmo período, com séries quase idênticas. Servem para testar robustez de execução e diferença entre corretoras. A amostra realmente nova é a **D**: os 215 perpétuos que só existem na Binance.

## 13. 1-2-3 do Crisp — varredura de parâmetros + universo D — 22/09/2026

Script: `monitor/replay_123_varredura.py` · log: `claude/123_varredura.log`

Primeira varredura de parâmetros do projeto, feita a pedido e **assumida como exploratória**: os números da varredura não são evidência, porque a seleção infla o vencedor.

- **Varredura (20 pares OKX, 1D, 36 células):** mínimo do movimento 1 (2 ou 3), stop no fundo 3 ou 1, alvo 1.0/1.5/2.0× a amplitude, filtro de tendência (nenhum/MMA80/MME21).
- **Vencedora:** mov1≥3, stop no fundo 1, alvo 1.0×, filtro MME21 → +0.111R (n=632). Original: +0.066R.
- **Validação (universo D, amostra nova):** os 215 perpétuos USDT-M que só existem na **Binance**, fora de A, B e C, listados há ≥400 dias (lista congelada em `monitor/universo_d.txt`).
- **Critério pré-registrado:** IC95 > 0 no universo D **e** superar a regra original lá.

| Universo D (215 pares) | n | Expectância | IC95 |
|---|---|---|---|
| **Vencedora** | 2720 | **+0.071R** | [+0.004, +0.143] |
| Original | 11227 | −0.048R | [−0.137, +0.031] |

**Pelo critério pré-registrado: PASSA** (o primeiro em 13 estudos). A regra também fica positiva nos quatro universos: A +0.111R, B +0.064R, C +0.118R, D +0.071R.

### Mas não sobrevive aos testes de robustez — não usar

Três verificações feitas depois (todas enfraquecem, nenhuma foi usada para escolher nada):

1. **Bootstrap por semana em vez de por dia:** IC95 vai de [+0.004, +0.143] para **[−0.020, +0.159]**, cruzando zero. O critério usava reamostragem por dia; com trades de 23 dias de duração média, o dia é uma unidade otimista.
2. **O lucro é todo do lado vendido:** compras +0.019R (IC cruza zero), vendas +0.105R. Num universo de memecoins que caíram muito, isso é suspeito.
3. **Teste de beta (mesmo do estudo 6):** contra entradas aleatórias no mesmo par, mesma direção e mesma duração, o **excesso é +0.33%, IC [−1.12, +1.70]** — zero. Nas vendas, −0.14%. **O ganho é exposição à queda do universo, não timing.**

O que está saudável: 124 dos 212 pares positivos, mediana por par +0.092R, sem depender de um par isolado.

**Conclusão:** o critério pré-registrado era fraco demais para este caso. Duas lições incorporadas ao protocolo:
- **Bootstrap por bloco de semana** quando a duração média do trade passar de ~5 dias.
- **Teste de beta obrigatório** (excesso sobre entrada aleatória de mesma duração) antes de qualquer PASSA em estratégia direcional.

## 14. Carry do Carver (estratégias 10 e 20) — 22/09/2026

Script: `monitor/replay_carver_carry.py` · log: `claude/carver_carry.log` · fonte: *Advanced Futures Trading Strategies*, Robert Carver (2023)

Primeiro estudo **fora da família price action**: o sinal vem do **funding**, não do preço; a posição é contínua e dimensionada por volatilidade, sem stop nem alvo; a medida é Sharpe de carteira.

- **Carry no perpétuo** [interp]: `carry_anual = −funding médio do dia × 3 × 365`. Positivo = ficar comprado paga.
- **Forecast** = carry ÷ volatilidade (ambos anualizados) × 30 (estratégia 10) ou, relativo à mediana do dia e suavizado em 90 dias, × 50 (estratégia 20); limite ±20. Volatilidade como no livro: 0.3 da média de 10 anos + 0.7 de EWMA(32), anualizada.
- **Posição** = forecast/10 × peso × 20% de risco ÷ volatilidade, com buffer de 10%; funding pago/recebido na simulação; custo de 0.06% do nocional negociado.
- **Amostras:** A (20 pares) só desenvolvimento; **D (215 perps só da Binance) decide**.
- **Critério:** Sharpe com IC95 > 0 **e** alfa contra a carteira equal-weight com IC95 > 0.

| | Amostra A (desenvolvimento) | **Amostra D (decide)** |
|---|---|---|
| Estratégia 10 (carry simples) | Sharpe −0.40 | **Sharpe −0.20**, IC [−0.98, +0.61] |
| Estratégia 20 (carry relativo) | Sharpe **+1.77**, alfa +5.6%/ano (IC [+2.6, +8.8]) | **Sharpe +0.30**, IC [−0.48, +1.06]; alfa **−1.0%/ano**, IC [−4.2, +2.1] |

**Veredito: NÃO PASSA** (as duas). O Sharpe de +1.77 nos 20 pares não se replicou nos 215 — e ele já tinha acionado o alerta de sanidade pré-registrado (o livro reporta 0.8–1.0 para carry em futuros diversificados).

- **Por que a estratégia 10 é negativa:** o funding em cripto é quase sempre positivo (BTC: +11.6%/ano em média), então o carry simples fica quase sempre vendido, num período em que o mercado subiu. O carry relativo (20) é neutro por construção.
- **Erro de implementação encontrado na rodada de fumaça** (corrigido antes da rodada que decide, e registrado no docstring): nos primeiros dias de cada série a EWMA de volatilidade começa fria (chegava a 0.002% ao ano) e, como a posição divide pela volatilidade, isso gerava **posição de 1250× o capital** e retorno de +9376%/ano. Correções: descartar 60 dias de aquecimento, piso de 10% na volatilidade anual, teto de 1× por instrumento e 3× de alavancagem bruta.
- **Infra nova:** `dados_binance.baixar_funding` (histórico de funding desde 2019; a OKX limita a ~96 dias).

**Estado das amostras:** A, B, C gastas; **D agora foi usada duas vezes** (varredura do 1-2-3 e carry). Para o próximo estudo, a amostra limpa restante é o paper trade ou um universo novo (ex.: perps de outra corretora).

## 15. Skew do Carver (estratégia 24) — 22/09/2026

Script: `monitor/replay_carver_skew.py` · log: `claude/carver_skew.log`

**Tese:** investidor gosta de ativo-loteria (skew positiva) e paga prêmio para não carregar skew negativa. Então compra-se o que teve skew negativa recente e vende-se o que teve skew positiva. Em cripto isso é especialmente testável, porque memecoin é o caso extremo de ativo-loteria.

- **Forecast = −skew** dos retornos diários em janelas de 60, 120 e 240 dias, suavizado por EWMA de span = janela/4, escalas 33.3 / 37.2 / 39.2, limite ±20; a primária é a média das três.
- **Cross-sectional:** o mesmo forecast menos a mediana do dia.
- Dimensionamento, custo e limites: idênticos ao estudo 14.

| | Amostra A (desenvolvimento) | **Amostra D (decide)** |
|---|---|---|
| Skew combinada | Sharpe −0.65 | **Sharpe −0.26**, IC [−1.06, +0.51] |
| **Skew cross-sectional** | Sharpe **+0.64**, alfa +1.7%/ano | **Sharpe +0.67**, IC [−0.13, +1.44]; alfa +2.5%/ano, IC [−1.9, +7.0] |

**Veredito: NÃO PASSA** — mas é o resultado mais interessante dos 15 estudos, e por um motivo diferente dos outros.

- **Replicou:** +0.64 nos 20 pares e +0.67 nos 215 pares da Binance. Nenhum outro estudo repetiu o número fora da amostra.
- **A magnitude é plausível:** o livro reporta 0.3–0.6 para skew isolada em futuros. Não acionou o alerta de sanidade (ao contrário do carry relativo, que deu +1.77 e não replicou).
- **A versão direcional (combinada) é negativa,** o que também faz sentido: ela fica comprada em quase tudo que caiu feio, num mercado de memecoins.

### Por que este estudo não pode ser decidido com os dados que existem

Com Sharpe de 0.65 e ~6.3 anos de histórico, o erro padrão do Sharpe é ≈ 1/√anos ≈ 0.40. Ou seja, o IC95 tem largura de ±0.78 **independentemente de quantos pares usemos** — os pares são correlacionados e o que conta é o tempo. Para o IC95 sair de cima do zero com Sharpe 0.65, seriam necessários **~9 a 10 anos** de histórico. Perpétuo de cripto só existe desde 2019/2020.

**Consequência:** não é possível "provar" esta estratégia com dados históricos de cripto, nem gastando mais amostras. As saídas são (a) paper trade adiante, sabendo que levaria anos para confirmar; (b) aceitar operar com evidência fraca e tamanho pequeno, o que é decisão do operador, não do teste; ou (c) arquivar.

**Estado das amostras:** A, B, C gastas; D usada três vezes (varredura do 1-2-3, carry, skew). Depois deste estudo, a amostra limpa restante é o paper trade.

## 16. Mais quatro do Carver: momentum XS, aceleração e mean reversion rápida — 22/09/2026

Scripts: `monitor/replay_carver_outras.py` (19 e 23) e `monitor/replay_carver_mr.py` (26 e 27) · logs: `claude/carver_outras.log`, `claude/carver_mr.log`

Família de **quatro testes na mesma amostra D**, então cada um usa **IC de 98.75%** (Bonferroni, 0.05/4) em vez de 95%. Mesmo arcabouço dos estudos 14 e 15.

| Estratégia | Sharpe no livro | Amostra A | **Amostra D (decide)** | Veredito |
|---|---|---|---|---|
| 19 — momentum cross-section | — | −0.00 | **−0.19** | não passa |
| 23 — aceleração | 0.20–0.59 | +0.25 | **+0.02** | não passa |
| 26 — mean reversion rápida (1H) | 0.44–0.75 | −1.29 | **−0.46** | não passa |
| 27 — idem, com filtro de tendência | — | −0.81 | **−0.34** | não passa |

**Value (estratégia 22) não foi testada:** o próprio livro reporta **SR −0.06** para ela isolada e só a usa com 5% de peso numa combinação. Gastar amostra nela não se justifica.

### O achado que vale: mean reversion tem o sinal invertido em cripto

Separei custo de sinal rodando a 26 com custo zero (8 pares, amostra A):

| | Sharpe |
|---|---|
| Com custo (0.06% por giro) | −1.53 |
| **Sem custo nenhum (bruto)** | **−0.80** |

**O custo não é a causa.** Comprar quando o preço cai abaixo do equilíbrio de 5 dias — que rende 0.44–0.75 em futuros — perde dinheiro em cripto **antes de qualquer custo**. No horizonte de horas, cripto **continua** o movimento em vez de reverter.

E o espelho (comprar o que se afastou para cima) não resolve: o bruto seria ≈ +0.80, mas girar de hora em hora custa ~0.73 de Sharpe, sobrando ~+0.07. É o mesmo muro dos 11 setups intradiários dos vídeos.

### Balanço do livro

Das 30 estratégias, 6 foram testadas — as que fazem sentido em perpétuo e não são pura tendência (carry 10/20, skew 24, momentum XS 19, aceleração 23, mean reversion 26/27). Só a **skew relativa** sobreviveu, com +0.67 contra os 0.60–0.75 que o livro reporta em futuros. As de tendência confirmaram o que 11 estudos de vídeo já indicavam, e o carry e a mean reversion falharam com mecanismo identificável.

## 17. Três de "151 Trading Strategies" (Kakushadze & Serur) — 22/09/2026

Script: `monitor/replay_k151.py` · log: `claude/k151.log` · fonte: *151 Trading Strategies*, cap. 3 (Stocks)

Famílias que ainda não tinham sido testadas: reversão **cross-sectional** (o estudo 16 testou reversão temporal) e anomalia de **baixa volatilidade**. Três testes na amostra D → IC de 98.33% (Bonferroni).

| Estratégia | Amostra A | **Amostra D (decide)** | Veredito |
|---|---|---|---|
| 3.9 reversão XS, 1 dia | Sharpe −1.96 | **−0.09** | não passa |
| 3.9 reversão XS, 5 dias | Sharpe −1.75 | **−0.37** | não passa |
| 3.4 baixa volatilidade | Sharpe −0.16 | **+0.49**, IC [−0.50, +1.45] | não passa |

**O que se aprende:**
- **Reversão cross-sectional é fortemente negativa nos 20 majors** (−1.96), ou seja, quem sobe mais que o grupo *continua* subindo no dia seguinte. É o mesmo sinal do estudo 16 (continuação, não reversão), agora no corte transversal.
- **Mas o espelho não serve:** momentum XS de 1 dia daria +1.96 nos majors e apenas **+0.09** nos 215 alts. O efeito existe só onde já olhamos, e some fora da amostra.
- **Baixa volatilidade inverte de sinal entre as amostras** (−0.16 e +0.49), o que é assinatura de ruído, não de prêmio de risco.

Pairs trading (3.8) não foi testada: é o caso N=2 da 3.9, que falhou.

## 18. Momentum de qualidade — "frog in the pan" (Gray & Vogel) — 22/09/2026

Script: `monitor/replay_qmom.py` · log: `claude/qmom.log` · fonte: *Quantitative Momentum*

**Tese:** alta construída devagar (muitos dias pequenos positivos) passa despercebida e continua; alta aos trancos vem de atenção e reverte. Mede-se com **FIP = sinal(retorno) × (% dias negativos − % dias positivos)** em 252 dias — quanto menor, mais suave a trajetória.

- Momentum 252 dias pulando os últimos 21 (o "12-2" do livro), rebalanceado a cada 21 dias.
- Versão "qualidade": dentro do quintil de maior momentum, compra os de menor FIP; no quintil inferior, vende os de maior FIP.
- Controle: momentum XS puro, sem o filtro.

| | Amostra A | **Amostra D (decide)** |
|---|---|---|
| Momentum XS puro (controle) | Sharpe −0.04 | **−0.24**, IC [−1.22, +0.75] |
| Momentum de qualidade (FIP) | Sharpe −0.22 | **−0.01**, IC [−1.05, +1.04] |

**Veredito: NÃO PASSA** (as duas). Momentum de 12 meses no corte transversal não funciona em cripto, com ou sem o filtro de qualidade — os dois ficam em torno de zero, sem diferença entre si. O prêmio que o livro documenta em ações não aparece aqui.

## 19. Combo de três prêmios transversais — e o que ele revela sobre a skew — 22/09/2026

Script: `monitor/replay_combo_premios.py` · log: `claude/combo_premios.log`

**Hipótese (não é garimpo de parâmetro):** skew (estudo 15, +0.67), baixa volatilidade (17, +0.49) e carry relativo (14, +0.30) medem a mesma ideia — comprar o "chato", vender o "loteria". Se são medidas ruidosas do mesmo prêmio, combiná-las cancela ruído idiossincrático. As correlações entre os forecasts confirmam que são medidas diferentes: +0.42 (skew × vol), −0.15 (skew × carry), −0.21 (vol × carry).

**Amostra nova (E):** os 153 perpétuos da Binance correspondentes aos pares OKX de B e C, fora de A e D (`monitor/universo_e.txt`). Nenhum componente deste combo os tinha visto.

| | Amostra A (desenvolvimento) | **Amostra E (decide)** |
|---|---|---|
| **Combo dos três** | Sharpe +1.29, alfa +3.2%/ano | **Sharpe +0.42**, IC [−0.30, +1.21], **alfa −0.1%/ano** |
| skew isolada | +0.59 | +0.20 |
| baixa volatilidade | −0.16 | +0.24 |
| carry relativo | +1.63 | +0.36 |

**Veredito: NÃO PASSA.**

### O que isso corrige no estudo 15

A skew deu **+0.64 (A), +0.67 (D) e agora +0.20 (E)**. A "replicação" que parecia forte não se sustentou numa terceira amostra. A leitura honesta passa a ser: **todos os prêmios transversais em cripto ficam entre +0.2 e +0.4 de Sharpe, com alfa contra o mercado ≈ 0**. Isso é indistinguível de zero com o histórico disponível, e a diferença entre eles é ruído.

Combinar não resolveu: o combo (+0.42) ficou na mesma faixa dos componentes, e não acima deles, o que indica que o pouco que existe é o mesmo pedaço de exposição em todos — não três fontes independentes de retorno.

## 20. Cash-and-carry (spot + perpétuo) — **PASSA**, com ressalva grande — 22/09/2026

Script: `monitor/replay_cash_and_carry.py` · log: `claude/cash_and_carry.log` · fonte: *151 Trading Strategies*, estratégia 6.2

**É a primeira estratégia a passar no critério pré-registrado, em 20 estudos.** Também é a única cujo retorno **não depende de prever nada**: compra-se o ativo no mercado à vista e vende-se o perpétuo na mesma quantidade. A posição fica neutra em preço e o que sobra é o funding, pago por quem está alavancado comprado. Ataca diretamente o achado do estudo 14 ("o carry é real e coletável, mas a variância do preço o engole").

- **Variante primária ("condicional"):** carrega o par só quando a média de funding dos últimos 7 dias é positiva.
- **Capital:** metade no spot, metade como margem do perpétuo (sem alavancagem; sem risco de liquidação).
- **Custo:** 0.30% por ciclo completo (as duas pernas, ida e volta).

| Amostra | Retorno | IC95 | Sharpe | Vol |
|---|---|---|---|---|
| A (19 majors, desenvolvimento) | +5.4%/ano | [+4.1%, +6.7%] | +5.50 | 1.0% |
| **D (144 alts, decide)** | **+6.3%/ano** | **[+4.8%, +8.0%]** | **+5.56** | 1.1% |

Drawdown máximo de **2.03%** em 6.6 anos; pior dia −0.30%. Média de 47 pares carregados por dia.

### A ressalva que muda a conclusão prática: o prêmio secou

| Período | D (alts) | A (majors) |
|---|---|---|
| 2020–2026 | +6.3%/ano | +5.4%/ano |
| 2024–2026 | +3.1%/ano | +1.6%/ano |
| **2025–2026** | **+1.0%/ano** (IC [+0.5, +1.5]) | **−0.9%/ano** (IC [−1.6, −0.2]) |

Ano a ano nos alts: 2020 +10.2%, 2021 +20.7%, **2022 −1.5%**, 2023 +4.1%, 2024 +6.6%, 2025 +0.9%, 2026 +0.9%.

O grosso do retorno veio de 2020–2021, quando havia alavancagem comprada em excesso. Depois disso o prêmio foi competido: hoje rende ~1%/ano nos alts e **negativo nos majors**. Isso bate com a literatura, que reporta o Sharpe do carry em cripto caindo de 6.4 (2020–2025) para negativo em 2025.

**Sensibilidade ao custo** (o risco operacional principal, porque em alt ilíquido 0.30% é otimista):

| Custo por ciclo | Retorno | Sharpe |
|---|---|---|
| 0.3% (modelado) | +6.3%/ano | +5.56 |
| 0.6% | +4.7%/ano | +3.95 |
| 1.0% | +2.6%/ano | +1.99 |
| 2.0% | **−2.7%/ano** | −1.56 |

**O que o teste não modela:** slippage real em alts ilíquidos, risco de delistagem do perpétuo enquanto a posição está montada (a amostra só tem pares vivos hoje), risco de corretora/custódia, e mudanças de taxa por nível de volume.

**Veredito: PASSA o critério, e é mecanicamente operável — mas no regime atual rende ~1%/ano**, abaixo de aplicações em stablecoin, e com o custo real podendo zerar isso. A leitura honesta: a estratégia é real e o mecanismo existe, só que o prêmio hoje é pequeno demais para justificar o trabalho e os riscos operacionais. Se o funding voltar a níveis de 2020–2021, ela volta a fazer sentido — e é fácil monitorar isso, porque o próprio sinal (média de funding de 7 dias) diz quando o prêmio está de volta.

## 21. Sazonalidade (hora do dia e dia da semana) — 22/09/2026

Script: `monitor/replay_sazonalidade.py` · log: `claude/sazonalidade.log`

Cripto negocia 24/7, mas Ásia, Europa e EUA têm fluxos diferentes, e fim de semana tem menos liquidez. Se houver padrão, ele roda 100% mecanicamente — é só um relógio.

**Seleção sem garimpo:** a melhor hora e o melhor dia foram escolhidos na **primeira metade** do histórico dos 20 pares; só eles foram testados nos 60 pares da amostra E, que a seleção nunca viu.

| Escolhido no desenvolvimento | Amostra A (todo o histórico) | **Amostra E (decide)** |
|---|---|---|
| Comprado às 15h UTC | −10.1%/ano, Sharpe −0.53 | **−12.0%/ano**, Sharpe −0.54 |
| Comprado no sábado | +19.8%/ano, Sharpe +0.95 | **+16.0%/ano**, IC97.5 [−7.7%, +38.5%], Sharpe +0.60 |

**Veredito: NÃO PASSA** (as duas). O efeito de sábado aparece nas duas amostras com sinal positivo e tamanho parecido, mas o intervalo cruza zero: são só ~350 sábados em 6,6 anos, e cada um é um evento ruidoso. É o mesmo problema de poder estatístico da skew — não há amostra suficiente no tempo.

### Onde o efeito está (descritivo)

| Cesta | Média por sábado | % positivos | t | ~ao ano |
|---|---|---|---|---|
| Só BTC | +0.040% | 53.4% | +0.42 | +2.1% |
| Só ETH | +0.237% | 56.2% | +1.49 | +12.3% |
| 5 maiores | +0.409% | 58.9% | +2.77 | +21.3% |
| **20 majors** | **+0.441%** | **64.6%** | **+2.93** | +22.9% |
| 60 alts | +0.368% | 59.0% | +1.86 | +19.1% |

**Só BTC não tem efeito.** Ele aparece por diversificação: 83% dos pares individuais (35 de 42) têm sábado positivo, mas só 3 têm significância sozinhos — padrão de efeito pequeno e difuso. A sexta também aparece forte (+0.616% nos alts, t=+2.22), então parece ser um efeito de "fim de semana", não de sábado isolado.

**Fragilidades registradas:** os 5 melhores sábados somam +45.7% de um total de +106.6% (metade do retorno em 5 de 350 dias); 2022 ficou em −0.9% e 2026 está em −4.2% com 45% de acerto.

### Em teste de papel desde 23/09/2026

Script: `monitor/sabado_paper.py` · registro: `claude/sabado-paper.md` · workflow: `.github/workflows/sabado-paper.yml`

Regra **congelada** (não alterar durante o teste): comprar a cesta de peso igual no fechamento de sexta UTC, vender no fechamento de sábado, custo de 0.06% e funding descontados. Registra em paralelo a cesta de 20 majors (principal) e a de 5 maiores (operacionalmente mais simples). **Nenhuma ordem é enviada.**

**Critério de leitura, fixado antes de começar:** só reavaliar com **104 sábados novos (~2 anos)**. Qualquer leitura antes disso é ruído — com 52 observações por ano e a dispersão medida, nada menos que isso distingue +20%/ano de zero.

## 22. Trend following canônico (Carver, estratégia 9) — 22/09/2026

Script: `monitor/replay_carver_trend.py` · log: `claude/carver_trend.log`

Fecha um buraco: os 11 estudos de vídeo testaram tendência com stop e alvo; o estudo 16 testou a versão transversal e a aceleração. Faltava a **forma canônica**: posição contínua e direcional, combinando EWMAC(8,32), (16,64), (32,128) e (64,256), com alvo de risco — a base da indústria de managed futures.

| | Amostra A | **Amostra E (decide)** |
|---|---|---|
| Trend canônico | Sharpe +0.20, alfa +5.6%/ano | **Sharpe +0.01**, IC [−0.72, +0.75]; alfa +6.2%/ano, IC [−5.9%, +18.5%] |

**Veredito: NÃO PASSA.** Com isso, a família tendência foi testada em três formas independentes (setup com stop/alvo, transversal e canônica direcional) e as três dão zero em cripto.

## 23. Acervo FMZ (strategies-for-test) — triagem por amostra sorteada — 23/09/2026

Scripts: `monitor/fmz/` (índice, classificação, sorteio), `monitor/fmz_motor.py` (emulador do broker do Pine) e `monitor/replay_fmz_triagem.py` · log: `claude/fmz_triagem.log`

**O acervo:** 5.807 estratégias da biblioteca da FMZ (repo `strategies-for-test`). 91% são PineScript, e 80% foram republicadas em série pela conta "ChaoZhang" a partir de scripts do TradingView. Pela classificação por nome, ~85% são combinações de indicadores das famílias que os estudos 1–22 já cobriram:

| Família (rótulo primário, pelo nome) | Estratégias |
|---|---|
| rompimento de canal / Donchian / breakout | 1.590 |
| tendência / médias / MACD / Supertrend | 1.415 |
| oscilador / reversão (RSI, Bollinger, CCI) | 1.158 |
| sem rótulo / ferramentas / utilitários | 704 |
| SMC / pivôs / suporte-resistência | 188 |
| volume / VWAP | 182 |
| grid / martingale / DCA | 141 |
| padrões de candle | 119 |
| market making / HFT / order book | 116 |
| arbitragem / hedge / base | 88 |
| sazonal, rompimento de volatilidade, pares, ML | 106 |

**Amostra representativa, sem escolha a dedo:** população de 3.764 scripts (Pine com `strategy()`, sem `request.security`, até 6.000 caracteres, família de indicador). Sorteio com semente 20260923 (`monitor/fmz/fila_sorteio.json`). Foram traduzidas as 12 primeiras traduzíveis, com os **parâmetros padrão de cada script**; uma foi pulada (stop e alvo em *ticks*). No diário, com custo de 0.18%, 0.05% de slippage por ordem stop e o funding real da Binance.

**Critério:** etapa 1 em A (avança com n ≥ 100, líquido > 0 e excesso > 0); etapa 2 em DE (368 perps da Binance = D + E), decide com `abs` e `excesso` IC > 0 a 1 − 0.05/K. K = 7 que avançaram + 4 hipóteses do estudo 24 = **11**, confiança 99.55%.

| Estratégia sorteada | A: líquido | A: excesso | **DE: absoluto** | **DE: excesso** | Veredito |
|---|---|---|---|---|---|
| 00 bandpass (SAR) | +1.12% | +1.30% | +0.61% | +0.38% | não passa |
| 01 EMA/HMA200 + RSI | +6.91% | −2.10% | — | — | parou em A |
| 02 SMA 9×21 + RSI (SAR) | +4.30% | **+2.08%** | +0.63% | +0.09% | não passa |
| 03 Chandelier exit | +30.8% | +16.3% | +2.55% | +0.11% | não passa |
| 04 vende sempre, 7 dias | −1.09% | +0.09% | — | — | parou em A |
| 05 Jim's MACD | +3.41% | **+1.24%** | +0.42% | +0.17% | não passa |
| 06 bandas EMA300 | −1.25% | +0.10% | — | — | parou em A |
| 07 máxima de 200 / ATR | +17.1% | +5.55% | +1.01% | −0.43% | não passa |
| 08 SMA 14×28 (SAR) | +6.88% | **+3.03%** | +1.17% | +0.54% | não passa |
| 09 CCI ±100 (SAR) | −4.68% | −0.93% | — | — | parou em A |
| 10 Big 3 (SMA 20/40/80) | +5.84% | +0.67% | +0.78% | −0.31% | não passa |
| 11 BB/Fib/MACD/RSI ("GPT") | −0.34% | −0.08% | — | — | parou em A |

(% por trade; em negrito, excesso com IC95 > 0 em A. Todos os IC de DE cruzam zero.)

**Veredito: NÃO PASSA** — nenhuma das 12.
- **Em A, 7 de 12 pareciam boas**, e três cruzamentos de médias tinham até excesso transversal significativo. Em 368 pares, tudo cai para ±0.5% por trade, indistinguível de zero. É o mesmo padrão de todos os estudos anteriores: o que "funciona" nos 20 majors é a história desses 20 ativos em 2019–2026.
- **Custo:** a de maior giro (11, "GPT", 0.8 dia por trade) perde com confiança; o custo sozinho a mata.
- **Leitura para o acervo inteiro:** com 12 sorteadas e nenhuma sobrevivendo, a proporção de estratégias com edge nesse acervo é baixa (IC95 de Clopper-Pearson para 0/12: até 26%). Isso não prova que nenhuma das 3.764 funciona. Diz que achar uma exigiria testar muitas, e cada teste consome a mesma amostra.

### Viés da linha de base de mesmo par — encontrado aqui, afeta o teste de beta dos estudos 6 e 13

Antes de rodar dado real, as 12 traduções rodaram num passeio aleatório sem drift (`monitor/fmz_teste_passeio.py`, 120 séries, 480 passos intra-candle):
- **O motor está limpo:** o bruto fica em zero nas 12.
- **A linha de base do estudo 6 não está:** o "excesso sobre entrada aleatória no mesmo par" sai significativo em 5 das 12. Dá +1.7% numa estratégia de contra-tendência e −0.5 a −1.2% nos seguidores de tendência.
- **Causa:** a linha de base usa a deriva realizada da série inteira, inclusive o futuro do trade, e a direção da estratégia se correlaciona com ela.

**Correção adotada daqui em diante:** linha de base **transversal**, com o mesmo lado e as mesmas datas exatas em até 30 outros pares do universo. No passeio aleatório ela acompanha o bruto e não gera falso positivo. Em dado real, remove a exposição ao mercado no período do trade, que era exatamente a preocupação dos estudos 6 e 13. A de mesmo par fica impressa como descritivo (`excesso_par`).

Nos estudos 6 e 13 o viés não mudaria o veredito: os dois eram NÃO PASSA pelo teste de beta. O 9.1 e o 1-2-3 são seguidores de tendência, e para eles a linha de base antiga é enviesada **contra** a estratégia. O excesso "zero" de lá pode ter sido levemente pessimista. Fica o alerta: essa linha de base não serve para aprovar nada, e sobretudo não serve para aprovar contra-tendência.

## 24. Acervo FMZ — os mecanismos distintos — 23/09/2026

Scripts: `monitor/replay_fmz_mecanismos.py` e `monitor/replay_fmz_base_trimestral.py` · logs: `claude/fmz_mecanismos.log`, `claude/fmz_base_trimestral.log`

Fora da sopa de indicadores, o acervo tem poucos mecanismos testáveis com candles. Market making, HFT e arbitragem entre corretoras (~200 scripts) precisam de livro de ofertas e ficaram de fora. Martingale também: o plano de risco (1% por trade) o proíbe por construção. Quatro hipóteses com poder de decisão, pré-registradas com o estudo 23 e dentro do mesmo K = 11 (confiança 99.55% em DE):

- **M1a Dual Thrust (stop and reverse):** parâmetros do acervo, N=4 e K=0.5, executado no caminho de 1h. Sempre posicionado.
- **M1b Dual Thrust intradiário:** as mesmas linhas, zerando no fim do dia UTC.
- **M2 Balanceamento 50/50:** gatilho de 5%, checado de hora em hora, custo de spot 0.15%. Medido contra o 50/50 parado.
- **M4 Pares:** Bollinger(20, 2) na razão moeda/BTC, saída na média, duas pernas (0.36% de custo).

Validação no passeio aleatório (`monitor/fmz_teste_passeio_mec.py`): pares e Dual Thrust SAR dão bruto zero. O intradiário tinha +0.11% com 20 passos por hora, que cai para +0.04% (não significativo, abaixo do slippage cobrado) com 120 passos. Era discretização do sintético.

**Correção de registro feita em A, antes de rodar DE:** a medida do M2 estava registrada como diferença **aritmética** de retornos diários. Em A ela deu −10.6%/ano, enquanto o balanceado terminava acima do parado em 15 de 20 pares (mediana 4.71× contra 2.75×). A hipótese ("demônio de Shannon") é de ganho **geométrico**, então a medida que decide passou a ser a diferença de **log-retornos**. A aritmética segue no log.

| Hipótese | A (descritivo) | **DE: absoluto** | **DE: excesso** | Veredito |
|---|---|---|---|---|
| M1a Dual Thrust SAR (5.1 dias/trade) | +0.31%, excesso +0.31% (IC95 > 0) | −0.11% | **−0.26%**, IC99.5 [−0.48, −0.05] | não passa |
| M1b Dual Thrust intradiário | −0.14% | −0.27% | **−0.16%**, IC99.5 [−0.24, −0.09] | não passa |
| M4 pares moeda/BTC | **−3.59%**, IC95 [−6.5, −1.3] | +0.14% | +0.23%, IC99.5 [−0.45, +0.82] | não passa |
| M2 balanceamento (excesso de log-retorno) | +5.3%/ano, IC95 [−8, +19] | — | +7.0%/ano, IC99.5 [−8.3, +22.6] | não passa |

**Veredito: NÃO PASSA** (os quatro).
- **Dual Thrust:** o excesso positivo em A se inverte em DE e fica **negativo com confiança** nas duas versões. O rompimento de 0.5× o range de 4 dias entra tarde. O intradiário, com ~150 mil trades, perde até o custo.
- **Pares:** em A, comprar a moeda que caiu contra o BTC perde com confiança (−3.6%/trade). Em DE fica em zero. É o mesmo "continuação, não reversão" dos estudos 16 e 17.
- **Balanceamento:** centro positivo nas duas amostras (+5 a +7%/ano de log-retorno), mas com IC de ±15%/ano. Terminou acima do parado em 75% dos majors e só em 55% dos 368 pares, onde a mediana dos dois é de **perda** (0.66× contra 0.58×). Mesmo que o excesso fosse real, é 50% comprado em cripto: ele reduz o arrasto de volatilidade, mas não cria retorno positivo onde o ativo cai.

**Uso das amostras:** D e E foram usados de novo, agora para 11 hipóteses (estudos 23 e 24), com Bonferroni.

### M3 — base de futuros trimestrais (medição, sem teste)

É o 期现对冲 / 跨期对冲 do acervo e a versão com vencimento do cash-and-carry do estudo 20. **A diferença que importa:** no perpétuo o retorno depende do funding *futuro*; no trimestral, a base fica **travada na entrada**. A montagem coin-M funciona assim: compra a moeda, deposita como margem e vende o trimestral inverso no mesmo valor em USD. Fica neutra em dólar sem capital extra e é **praticamente não liquidável**: patrimônio e margem de manutenção escalam juntos com 1/preço, e só a divergência entre marcação e índice mexe nisso. O retorno sobre o capital é F/S − 1 no vencimento.

| Coin-M | Carry realizado 2020–2026 (1º dia do contrato até o vencimento, líquido de 0.30%/ciclo) | Pior trimestre (anualizado) | Base hoje (mediana 30 d, anualizada) |
|---|---|---|---|
| **BTC** | **+7.1%/ano** (+50% em 6.0 anos) | −0.7% | 4.2% (trimestre atual), 4.7% (próximo) |
| **ETH** | **+7.0%/ano** (+49% em 5.9 anos) | −2.4% | 4.5% / 3.4% |
| XRP | +5.5%/ano | −8.4% | 1.5% / 4.1% |
| SOL (1.7 ano) | +1.2%/ano | −3.8% | 3.3% / 2.1% |
| BNB | −1.7%/ano (base negativa 2022–2024) | −11.4% | 8.3% / 5.5% |

Base anualizada mediana do trimestre corrente, BTC: 2020 11.2% · 2021 13.0% · 2022 1.6% · 2023 5.5% · 2024 10.0% · 2025 6.1% · **2026 2.6%**.

**Leitura:** dos três mecanismos sem previsão nenhuma (estudo 20, este e o balanceamento), o trimestral em BTC/ETH é o de melhor histórico. Rendeu ~7%/ano por seis anos, com o pior trimestre em −0.7%, e o prêmio **não secou como o do perpétuo**: em 2025 ainda pagou 6%. Em 2026, porém, a mediana caiu para ~2–3%. Nos últimos 30 dias ele trava ~4.5%/ano bruto. O custo é de ~1.2%/ano rolando a cada trimestre, ou ~0.6% no contrato do semestre seguinte, o que deixa **~3.5–4%/ano líquido**. É mecanicamente operável, sem risco de preço e praticamente sem risco de liquidação na montagem coin-M. Mas o retorno atual é de renda fixa, não de trading, e só se justifica se vencer o que o mesmo capital renderia parado em stablecoin. Riscos não modelados: corretora e custódia, USDT contra USD, e o preço executável contra o fechamento diário.

## 25. Desbloqueio de tokens para insiders — teste de papel desde 23/09/2026

Estudo feito no repo separado `token-unlocks` (desenho, resultado e robustez no README de lá). Vender o perpétuo 7 dias antes de um desbloqueio ≥ 1% da oferta com ≥ 50% para insiders **passou** no teste pré-registrado de 2025–2026: excesso de +2.1% por evento, IC98.75 [+0.8, +3.4], e +2.9% absoluto. Sobreviveu a bootstrap por token, placebo e dose-resposta. A ressalva é de concentração: sem os 3 maiores contribuidores, o IC toca zero.

**Teste de papel:** `monitor/unlock_paper.py` · registro: `claude/unlock-paper.md` · roda no workflow horário (`btc-monitor.yml`), com `continue-on-error`.
- **Regra congelada:** descrita no docstring. Registra a versão **pura** (só a venda) e a **com hedge** (venda + cesta dos 20 majors), com custo e funding real. **Nenhuma ordem é enviada.**
- **Calendário:** a DefiLlama é atualizada 1× por dia. Evento que aparece depois da data de entrada é descartado ("conhecido tarde"), para não olhar o futuro.
- **Preços:** vêm do data.binance.vision, com a API como reserva, porque os runners do GitHub ficam nos EUA. Sem a API, o funding fica pendente até o arquivo mensal sair. Os dois caminhos foram validados em simulação.
- **Critério de leitura, fixado antes de começar:** só reavaliar com **150 trades fechados** (~7–8 meses no ritmo de 2025–2026).

## 26. Perpétuo recém-lançado com stop — teste de papel desde 23/09/2026

Estudo no repo separado `binance-listings`. Vender perpétuo novo **não passou**: em 654 lançamentos (2020–2026, inclusive deslistados), 73% caem em 30 dias (mediana −27% no teste), mas altas de até +3.072% deixam a média negativa, e o vendido ainda paga funding. Uma versão com stop só pode ser testada em lançamentos futuros, porque foi imaginada depois de ver os dados.

**Teste de papel:** `monitor/novos_paper.py` · registro: `claude/novos-paper.md` · workflow horário, com `continue-on-error`.
- **Regra congelada, com parâmetros redondos e sem otimizar no histórico:** vender na abertura do 2º dia após o lançamento, recompra obrigatória a +50%, saída em 30 dias.
- **Comparação:** registra junto a versão sem stop e o excesso sobre os 20 majors.
- **Leitura:** só com **100 trades fechados**. A maioria dos lançamentos de 2026 é de ações e commodities (69 de 73 nos últimos 70 dias), então isso leva ~1.5–2 anos.

## Leitura conjunta

Mesma direção do achado da auditoria v6 sobre o checklist mecânico dos Setups A/B. Nenhum dos dez setups de vídeo tem edge mecânico demonstrável nesses 20 pares (o 9.1 também não, fora da amostra, nos 80 pares do estudo 6):
- **Regra do candle da entrada:** vale com a regra corrigida (reexecução acima). O mais perto de passar foi o 1-2-3 no diário, que não se confirmou nos 80 pares.
- **Custo:** todos pioram quanto menor o tempo gráfico, porque o custo em R cresce.
- **Sinal:** nos intraday, o resultado bruto fica em torno de zero; o sinal não carrega informação.
- **Acerto alto:** as taxas de acerto altas prometidas nos vídeos se reproduzem (1-2-3 não; IFR sim), mas vêm de ganhos pequenos e perdas grandes, e não de edge.

A única regularidade, o 9.1 no diário, vinha sobretudo de beta. Fora da amostra, nem o retorno absoluto se sustenta. Se existir algum timing, ele fica abaixo do que estes dados conseguem detectar (~1% por trade).

O acervo FMZ (estudos 23 e 24, 5.807 estratégias) não mudou o quadro:
- **Amostra sorteada:** 12 estratégias de indicador, nenhuma sobreviveu. Sete pareciam boas nos 20 majors e todas desabaram nos 368 pares.
- **Mecanismos distintos:** nenhum dos quatro passou.
- **O único operável** continua sendo carry sem previsão. O trimestral coin-M em BTC/ETH rendeu ~7%/ano em 2020–2026 e hoje trava ~3.5–4%/ano líquido.

Não reabrir esses testes sem uma regra nova pré-registrada. Variar parâmetro sobre estes mesmos dados até algo ficar positivo invalida o critério.

## Setups A/B — encerrado em 25/09/2026

Não é setup de terceiro, mas o veredito fica registrado aqui junto dos outros.

| Fonte | n | Média | IC 95% |
|---|---|---|---|
| Diário (meta dos 30, `conta_para_validacao = 1`) | 34 | −0.13R | [−0.62, +0.44] |
| Replay de 300 dias, MIN_RR = 2.0 (auditoria v6) | 534 | −0.15R | [−0.28, −0.00] |

**Veredito: NÃO PASSA.**
- O diário ao vivo reproduz o replay. O IC do diário é largo e cruza zero: 30 trades nunca teriam poder para mostrar edge (±0.5R de largura). O que decide é o replay, com o IC inteiramente negativo.
- O n efetivo do diário é menor que 34: há lotes disparados juntos (BTC/ETH/XRP em 07/09, BTC+ETH e SOL+LINK em 15/09, BTC+LINK em 16/09).
- Só 3 dos 34 são Setup A. Não há leitura separada dele.
- O filtro humano (checks de correlação, regime e qualidade) nunca foi preenchido nos 34 trades, então não foi testado. O Gabriel decidiu não testá-lo: o objetivo do projeto é uma regra 100% mecânica.

**O que muda no código:** `SETUP_AB_ENCERRADO = True` em `fetch_and_check.py`. Toda confirmação continua indo para `sinais_mecanicos`, com o desfecho mecânico medido como antes (calibração). A que passa no R:R deixa de virar candidato no diário e não gera push. Os 13 candidatos pendentes (17/09 a 24/09) foram marcados como descartados em `sinais.md`.
