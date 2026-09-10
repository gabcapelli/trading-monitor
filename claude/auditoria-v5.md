# Auditoria de continuação da v4 — 10/09/2026

> Feita com o Claude Code, sobre três fontes: o código de `monitor/fetch_and_check.py`, os 30 sinais já em `claude/trade_journal.db`, e 33 dias de histórico da OKX (437 sinais reproduzidos). Tudo afirmado aqui está ancorado em código ou dado do repositório — onde não havia dado suficiente, está escrito que não havia.
>
> Escopo: continuação da v4, não repetição dela. Os quatro gaps que a v4 fechou (`conta_para_validacao`, revalidação de tendência na confirmação, cooldown de nível, auto-detecção de resultado) não foram reauditados — foi auditado o que a v4 *deixou passar*.

---

## 0. O fato que muda a leitura de tudo: a v4 nunca executou

O commit da v4 (`f448851`) veio **depois** da última execução do monitor (`0de89a1`, 16:05 BRT de 10/09). Duas provas independentes no repositório:

1. `monitor/state.json` versionado não tinha as chaves `cooldown` nem `contadores` em nenhum par — `load_state()` as injeta via `setdefault` e `save_state()` as grava, então a ausência significa que `load_state()` da v4 nunca rodou.
2. `criado_em_ts`, `mae_r`, `mfe_r` e `motivo_resultado` estavam `NULL` em **30/30** trades.

Consequência prática: cooldown, revalidação de tendência e acompanhamento automático de desfecho existiam só no papel. E os `mae_r`/`mfe_r` que o pedido desta auditoria supunha "agora populados automaticamente" estavam, na verdade, todos vazios — e **nunca** seriam preenchidos pelo caminho normal, porque `track_open_trade_outcomes` exige `criado_em_ts` para saber de qual candle acompanhar, e nenhum trade antigo o tinha.

---

## 1. Correção — bugs encontrados

Todos corrigidos. Detalhe técnico de cada um no CHANGELOG v5 no topo de `monitor/fetch_and_check.py`; cada item tem teste de regressão em `monitor/test_v5_fixes.py`.

### B1 — O cooldown da v4 não cobria o caso que o motivou (alto)

`_set_cooldown` era chamado em quatro ramos — invalidado, expirado, tendência virada, R:R baixo. **Não** no ramo `confirmado`, que é o único que limpa a zona num caminho de sucesso.

E o outro guard não fechava o buraco: `pair_has_open_position()` filtra `status='entrado'`, mas `insert_candidate_trade` grava `status='candidato'`. Na janela entre a confirmação e a edição manual no `sinais.md`, **nenhum dos dois mecanismos estava ativo**.

O próprio exemplo citado no CHANGELOG v4 item 3 caía aí: LINK #25 (01:05) e #27 (05:06), `nivel_referencia = 11.833` nos dois, dois stops seguidos. A zona de #25 foi limpa por uma *confirmação*, não por uma falha — então a v4 não armaria cooldown nenhum.

Varredura do banco por nível+direção repetidos:

| Par / direção | Nível | Sinais |
|---|---|---|
| ETH venda | 2489.76 | #1, #4 (-1R), #9 |
| XRP venda | 1.3972 | #2, #5 (-1R), #10 (-1R) |
| DOGE venda | 0.08995 | #7 (-1R), #11, #16 |
| XRP compra | 1.3907 | #8 (+2.35R), #20 (-1R) |
| BTC venda | 78299.0 | #13, #24 (+2.17R) |
| SOL compra | 102.2 | #19 (-1R), #26 (-1R) |
| LINK venda | 11.833 | #25 (-1R), #27 (-1R) |
| XRP compra | 1.3623 | #28 (-1R), #30 |

**11 dos 30 sinais eram reuso de um nível já sinalizado.** Em 5 desses grupos o primeiro evento foi uma confirmação — exatamente o caminho sem cooldown.

### B2 — Setup A nunca checava cooldown (alto)

`try_map_new_zone` retornava o Setup A antes de qualquer chamada a `level_blocked_by_cooldown`, que só aparecia dentro dos dois loops do Setup B. O caminho é vivo: o LINK ficou com `zona_mapeada_setup_A` no ciclo seguinte a um `descartado_rr_baixo_setup_B`.

### B3 — Ciclo de vida da zona contava execuções, não candles (médio)

`candles_since_creation += 1` por chamada da função. `created_at` era gravado e nunca lido. E `last_1h_ts` — que existe em `default_pair_state()` desde a v2 — **nunca era escrito por caminho nenhum do código**: era precisamente o guard de "já processei este candle", desenhado e nunca ligado.

Verifiquei se já havia divergência e **não havia**: ARB (zona criada no candle 13:00, último fechado 16:00, contador 2) e LINK (10:00 → 16:00, contador 5) batiam exato com o número de execuções, e o log mostra cadência horária limpa nas últimas 30h. Mas o `CLAUDE.md` documenta o schedule do GitHub Actions como historicamente irregular — um ciclo perdido fazia a zona viver mais candles do que a regra permite, e dois ciclos na mesma hora contavam o mesmo candle como dois toques. Era fragilidade latente, não bug ativo.

### B4 — A expiração no código não era a regra documentada (médio)

Plano (seção 2): "8 candles **sem toque** ou 3 toques". O código nunca resetava o contador num toque — eram 8 candles totais, então uma zona ativa, sendo testada, morria por tempo. Decidido seguir o plano (é a spec; o código é que divergiu). A vida máxima continua finita por `ZONE_MAX_TOUCHES`.

### B5 — O alvo era o pivô mais *recente*, não o mais *próximo* (médio-alto)

`candidatos[-1]` é ordem de índice, ou seja recência, embora a intenção documentada seja "próxima zona de oferta/demanda relevante". A diferença não é cosmética: ela infla o R:R exatamente quando o preço vai contra a tese.

Caso real no banco: XRP compra manteve `alvo_sugerido = 1.4388` **constante** em #20 (entrada 1.4028), #23 (1.3914), #28 (1.3635) e #30 (1.3597). O preço caiu 3%, o alvo não se moveu, e o R:R subiu de 3.36 → 8.40 **enquanto a tese piorava**. #20, #23 e #28 deram -1R cada.

**A regra autoritativa não foi trocada, de propósito** — ver seção 3.

### B6 — `zona_entrada`/`confirmacao` com `:.1f` (baixo)

A v3 criou `fmt_price()` e não atualizou `insert_candidate_trade`. No banco: DOGE `'0.1-0.1'`, SUI `'0.8-0.8'`, XRP `'1.4-1.4'`. A coluna de auditoria da zona estava sem informação em 9 dos 10 pares — e é exatamente a coluna que serviria pra recalibrar `ZONE_ATR_MULT`.

### B7 — Um único slot de cooldown por par (baixo)
`pair_state["cooldown"]` era sobrescrito; um cooldown de compra apagava o de venda. Virou dict por direção, com migração que preserva o cooldown em andamento.

### B8 — O log não permitia reconstruir ciclo de vida de zona (baixo)
Só a string de status era gravada. Em 10/09 o ARB alternou mapeada → invalidada → mapeada → invalidada em 4h e não havia como saber se era o mesmo nível. Foi por isso que não consegui medir, com o dado do repo, quantos remapeamentos o cooldown da v4 teria barrado.

### B9 — Cobertura de teste da v4 era zero
Os dois testes existentes são ambos da v1 e cobrem só erro de índice/lista.

### Verificado e *sem* bug

Vale registrar o que foi testado e resistiu, pra não reauditar depois: `true_range`/`atr` (média simples em vez de Wilder é divergência conhecida, não erro); `find_confirmed_pivots` (janela simétrica, só candles fechados, exclui corretamente os últimos `window`); índice de `volCcyQuote`; dupla contagem do contador de descartes; insert duplicado sem notificação (não alcançável — o status alterna).

Uma hipótese minha foi **testada e derrubada**: supus que o Setup A sufocaria o Setup B (por retornar antes, em qualquer tendência definida). A sonda ao vivo nos 10 pares mostrou `broke=False` em BTC/SOL/UNI (tendência baixa) e WLD (alta) — nenhum Setup A mapeado, consistente com 1 Setup A em 30 sinais. Não há esse problema.

---

## 2. Metodologia — o que é palpite, o que está validado

O `CLAUDE.md` aponta `claude/backtest-setup-ab.md` como fonte do backtest, mas **esse arquivo não existe neste repositório**. Do ponto de vista daqui, nenhum número é rastreável a um backtest; só ao que o código diz de si mesmo:

| Parâmetro | Status real |
|---|---|
| `PIVOT_WINDOW = 3` | **Único ancorado em backtest.** É a razão declarada para descartar a `smartmoneyconcepts`. Tratar como travado. |
| `ZONE_MAX_CANDLES_1H = 8`, `ZONE_MAX_TOUCHES = 3` | Regra da seção 2 do plano. Regra, não calibração. |
| `MIN_RR = 2.0` | Regra de risco do plano, não negociável. |
| `ZONE_ATR_MULT = 0.25` | "Ponto de partida" — e governava **três** comportamentos ao mesmo tempo (meia-largura da zona; `3 * ZONE_ATR_MULT` como raio de proximidade; tolerância do cooldown). Desacoplado na v5 sem mudar valor efetivo. |
| `STALE_4H_CANDLES = 10` | "Ponto de partida". |
| `STOP_BUFFER_ATR_MULT = 0.1` | **O palpite mais puro.** O comentário do código diz: "convenção adotada nesta sessão ao calcular stop/alvo manualmente para os candidatos de ETH/XRP" — n=2, ad hoc. E define o denominador de todo R. |
| `ZONE_COOLDOWN_CANDLES_1H = 8`, `LONG_OPEN_CANDLES_1H = 48` | "Ponto de partida", v4, nunca executados. |

Nota: a largura da zona do Setup B escala com **ATR de 1h** embora a zona seja um swing de **4h**.

### 2.1 Sobre aumentar o win rate: não dá para saber — e agora isso foi medido, não suposto

Diário (17 resolvidos que contam): 2 acertos (11.8%), soma **-10.48R**, expectância **-0.616R/trade**. Média dos acertos 2.26R → win rate de breakeven 30.7%. Binomial: **P(≤2 acertos em 17 | p=0.307) = 0.069** — nem a conclusão *negativa* passa de 5%.

Com o harness de replay (`monitor/replay.py`), a mesma lógica rodou sobre 33 dias e 10 pares:

| Amostra | n resolvidos | Win rate | Expectância | IC 95% (bootstrap) |
|---|---|---|---|---|
| Replay, `MIN_RR=2` (atual) | 168 | 20.2% | **-0.167R** | [-0.425, **+0.103**] |
| Replay, sem filtro de R:R | 416 | 39.7% | **-0.113R** | [-0.236, **+0.019**] |

**Mesmo com n=416, o intervalo de confiança inclui zero.** A conclusão honesta não é "o sistema perde dinheiro" nem "é só calibrar" — é que **não há edge demonstrável em nenhuma das duas direções**, e nenhuma mudança de parâmetro se justifica estatisticamente com este dado.

Varredura de `STOP_BUFFER_ATR_MULT` (437 sinais):

```
buffer 0.00 → -0.258R    buffer 0.20 → -0.282R    buffer 0.75 → -0.487R
buffer 0.05 → -0.274R    buffer 0.30 → -0.241R    buffer 1.00 → -0.552R
buffer 0.10 → -0.167R ←  buffer 0.50 → -0.415R
```

**Nenhum valor torna a expectância positiva.** O 0.1 atual é o melhor dos oito testados — provavelmente sorte, mas ao menos não está mal posto, e não há justificativa pra mexer.

Varredura de `MIN_RR` — este é o achado mais substantivo:

```
MIN_RR 0.0 → n=416, 39.7% acertos, -0.113R
MIN_RR 1.0 → n=279, 26.9% acertos, -0.146R
MIN_RR 2.0 → n=168, 20.2% acertos, -0.167R   ← atual
MIN_RR 2.5 → n=122, 15.6% acertos, -0.252R
MIN_RR 3.0 → n= 95, 12.6% acertos, -0.318R
MIN_RR 4.0 → n= 60, 11.7% acertos, -0.273R
```

**Exigir mais R:R piora a expectância, monotonicamente.** Isso confirma o mecanismo de seleção adversa do B5: com a regra de alvo "pivô mais recente", exigir R:R alto é o mesmo que exigir alvo distante, ou seja, selecionar trades improváveis. O win rate desaba de 39.7% para 11.7% e o aumento do payoff não compensa.

A tabela de calibração (`claude/calibracao.md`), construída a partir dos 30 sinais reais, aponta na mesma direção por um caminho independente:

| Grupo | Sinais | Resolvidos | Acertos | Expectância |
|---|---|---|---|---|
| Aceitos (R:R ≥ 2) | 22 | 21 | 2 (10%) | **-0.689R/sinal** |
| Descartados por R:R baixo | 7 | 6 | 5 (83%) | **+0.265R/sinal** |

Com n=6 nos descartados isso sozinho não prova nada. Mas é a mesma direção que o replay mostra com n=416, por dados diferentes. **Isto é a coisa mais acionável desta auditoria** — e é uma decisão de metodologia que fica com você (seção 4), porque `MIN_RR=2` é regra do plano de risco, não parâmetro de calibração.

### 2.2 O que o MAE/MFE diz sobre onde está o problema

Do replay (n=168 aceitos resolvidos):

- **Acertos**: MAE mediano **0.52R**, p90 **0.94R**, 24% acima de 0.8R. Ou seja, os trades que dão certo rotineiramente vão 0.5R contra antes de funcionar, e um quarto deles chega perto de 1R contra. **Não há folga para apertar o stop** — apertar mataria os acertos, o que a varredura de buffer confirma.
- **Erros**: MFE mediano **0.70R**; 37% chegaram a 1R a favor, 63% a 0.5R.

O segundo número é material real para uma regra de stop no breakeven (mover o stop para a entrada depois de 1R a favor transformaria ~37% dos erros em zero em vez de -1R). Não implementei: **isso é regra de trade nova, não correção de bug nem mudança de arquitetura** — ver seção 4.

---

## 3. Mudanças de arquitetura aplicadas

O gargalo não era falta de trades — era que o script só registrava o que **aceitava**.

1. **Tabela de calibração `sinais_mecanicos`** + espelho legível `claude/calibracao.md`. Registra **toda** confirmação mecânica, inclusive as descartadas por R:R, com desfecho medido por geometria de preço. Os descartes são os contrafactuais: sem eles não há como saber se o `MIN_RR` corta perdedores ou vencedores — e foi exatamente isso que permitiu a tabela da seção 2.1. Antes, um descarte só incrementava um contador inteiro no `state.json` e sumia.

2. **Duas colunas de resultado, separadas de propósito.** `resultado_r` continua sendo o trade que você de fato tomou (editado em `sinais.md`, único que conta para o gate dos 30). `resultado_mecanico_r` mede "o que a sugestão mecânica teria feito a partir do candle de confirmação" e vale para **todo** sinal, não só os `'entrado'` — porque medir MAE/MFE só nos que você marcou enviesa o dado pela sua própria seleção, que é justamente a variável a isolar.

3. **`claude/sinais.md` não mudou.** Continua com as mesmas 13 colunas e as mesmas 3 editáveis. A superfície que você usa no celular não virou painel de calibração; o dado novo vive em `calibracao.md`, que é só leitura.

4. **Harness de replay (`monitor/replay.py`).** As funções de detecção já eram puras e recebiam candles como parâmetro, então foi possível rodar a lógica inteira sobre histórico paginado da OKX sem reescrever nada. É o que tornou a seção 2.1 possível. Também é o caminho para re-rodar tudo caso `PIVOT_WINDOW` mude um dia — o risco que o `CLAUDE.md` levanta ao justificar o descarte da `smartmoneyconcepts`.

5. **Parâmetros desacoplados.** `ZONE_PROXIMITY_ATR_MULT` e `COOLDOWN_LEVEL_TOL_ATR_MULT` saíram de dentro de `ZONE_ATR_MULT`, com os mesmos valores efetivos. Sem isso, recalibrar a largura da zona mudava silenciosamente quais swings viram candidatos e quando um nível desbloqueia.

6. **Coluna "Zona ativa" no log** (setup/direção/nível/toques/candles), com migração que normaliza as 480 linhas existentes por contagem de colunas — tolera os três formatos que já conviviam no arquivo.

### Backfill

`monitor/backfill_mecanico.py`, rodado uma vez. Deriva `criado_em_ts` de `criado_em` (execução em HH:05 lê como último fechado o candle de ts (HH-1):00 — conferido contra os `created_at` de ARB e LINK no `state.json`), **recupera `preco_entrada` dos trades #3–#16** (a coluna não existia, mas a definição dela é "fechamento do candle de confirmação", que agora sabemos qual é — não é estimativa) e calcula desfecho mecânico + MAE/MFE.

**28 dos 30 trades cobertos** (#1 e #2 não têm `stop_sugerido`). Validação independente: o cálculo mecânico concordou com **100%** dos `Resultado (R)` que você havia preenchido à mão — zero divergências. `resultado_r` de trades `'descartado'` não foi preenchido, mesmo onde o alvo foi batido (#6, #9, #11, #12, #14 bateram): esse desfecho existe e está em `sinais_mecanicos`, mas colocá-lo no diário faria um trade que você nunca tomou entrar na contagem dos 30.

Não é recuperável: os sinais **descartados por R:R antes da v5**. Nunca foram gravados em lugar nenhum. A tabela de calibração só recebe descartes a partir de agora.

---

## 4. O que fica para você decidir

Implementei as quatro decisões que ficaram abertas na primeira rodada (expiração por toque, alvo em paralelo, cooldown na confirmação, duas colunas de resultado). Estas três são novas, saíram do dado que o backfill e o replay produziram, e **são metodologia, não correção** — não toquei nelas:

1. **`MIN_RR = 2.0` pode estar invertido de sinal.** A varredura mostra degradação monotônica acima de 2.0 (n=416), e os descartados reais tiveram expectância positiva contra negativa dos aceitos (n=6+21). Mas `MIN_RR` é regra do plano de risco, não parâmetro de calibração — e baixá-lo muda o que conta como trade válido no gate dos 30. Se quiser investigar sem mexer na regra: `python monitor/replay.py --varrer min_rr`.

2. **Trocar a regra de alvo para "pivô mais próximo".** Mantive a regra atual como autoritativa para não quebrar a comparabilidade da amostra no meio do gate; os dois alvos já estão gravados lado a lado em todos os sinais (inclusive retroativamente). No replay: `recente` -0.167R com 168 sinais, `proximo` -0.109R com 61. Menos ruim, não decisivamente melhor, e corta 2/3 dos sinais.

3. **Stop no breakeven após 1R a favor.** 37% dos erros chegaram a 1R a favor antes de virar. É a mudança com maior efeito aritmético potencial, e é uma regra de trade nova — fora do escopo de uma auditoria.

E uma pendência que a v4 já registrava e continua aberta: `classify_trend_4h` exigir os dois últimos topos **e** os dois últimos fundos na mesma direção faz "lateral" ser ~60% dos casos, e o guard de tendência só atua fora de "lateral".

---

## 5. Como verificar

```bash
python monitor/test_zone_logic.py     # 2 testes (v1)
python monitor/test_v5_fixes.py       # 12 testes (v5)

python monitor/replay.py                      # expectância por par, parâmetros atuais
python monitor/replay.py --varrer min_rr      # a varredura da seção 2.1
python monitor/replay.py --varrer stop_buffer
python monitor/replay.py --varrer alvo
```

Arquivos novos: `monitor/replay.py`, `monitor/backfill_mecanico.py`, `monitor/test_v5_fixes.py`, `claude/calibracao.md`, este relatório.

> Lembrete que vale repetir: o replay mede o efeito de mexer num parâmetro sobre a **mesma** lógica. Não valida a lógica, não substitui o backtest histórico do plano, e não inclui custo de execução (taxa, spread, slippage, funding) — que só torna tudo acima pior, nunca melhor.
