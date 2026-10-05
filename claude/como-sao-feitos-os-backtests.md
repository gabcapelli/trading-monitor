# Como são feitos os backtests do trading-monitor

> Documento descritivo, escrito em 04/10/2026 a partir do código em `monitor/` e dos registros em `claude/` (`auditoria-v5.md`, `auditoria-v6.md`, `setup-c-testes.md`, `estudos-avulsos.md`). Descreve **o método**; os resultados completos continuam nos arquivos de origem. Quando houver divergência, vale o código e o registro original.

## 1. Visão geral

O projeto não tem um "motor de backtest" único. Existem **três famílias** de teste, com ferramentas e propósitos diferentes:

| Família | Pergunta que responde | Scripts | Registro |
|---|---|---|---|
| **A. Replay da lógica de produção** (Setups A/B e C) | "Se o monitor tivesse rodado sobre N dias de histórico, que desfecho teria cada sinal?" | `replay.py`, `replay_setup_c.py`, `backfill_mecanico.py` | `auditoria-v5.md`, `auditoria-v6.md`, `setup-c-testes.md` |
| **B. Estudos avulsos pré-registrados** (setups de terceiros, livros, acervo FMZ) | "Esta regra tem edge fora da amostra onde nasceu?" | `replay_<nome>.py` (≈30 scripts) | `estudos-avulsos.md`, `*.log` |
| **C. Teste de papel adiante** (forward test) | "A regra se sustenta em dados que ainda não existiam?" | `unlock_paper.py`, `novos_paper.py`, `sabado_paper.py` | `unlock-paper.md`, `novos-paper.md`, `sabado-paper.md` |

Princípio que atravessa as três: **o objetivo é provar edge com regras objetivas antes de qualquer capital real**, então o método é desenhado para *rejeitar* falsos positivos, não para encontrar parâmetros bonitos. Quase todo o protocolo estatístico (holdout, Bonferroni, bootstrap por bloco, teste de beta) existe porque um estudo anterior passou no critério antigo e caiu num teste mais rigoroso.

---

## 2. Família A — Replay da lógica de produção

### 2.1 Ideia central

O monitor (`monitor/fetch_and_check.py`) é composto de funções **puras** que recebem candles como parâmetro: `find_confirmed_pivots`, `classify_trend_4h`, `try_map_new_zone`, `check_zone_confirmation`, `compute_suggestion`, `desfecho_mecanico`. O replay (`monitor/replay.py`) importa o módulo como `m` e **chama exatamente essas funções**, um candle de 1h por vez, sobre histórico em vez de dados ao vivo. Se a lógica de produção mudar, o replay muda junto — esse é o ponto do desenho.

Ele **não** reproduz o backtest histórico original do plano (`backtest-setup-ab.md`, que vive em outro Projeto no claude.ai); reproduz o que *este script* faz, para medir o efeito de mexer em parâmetros.

### 2.2 Dados

- **Fonte:** OKX, endpoint público `/api/v5/market/history-candles`, paginado para trás com `after` (`fetch_historico`). Sem chave de API.
- **Pares:** os 10 de `PAIRS` (BTC, ETH, SOL, XRP, DOGE, ARB, WLD, SUI, UNI, LINK, todos `-USDT-SWAP`).
- **Tempos gráficos:** 1h (execução e desfecho) e 4h (tendência e zonas de Setup B).
- **Profundidade:** `--dias N` (padrão 33 dias ≈ 8 páginas de 100 candles; as rodadas relevantes usaram `--dias 300`, ~7.200 candles de 1h por par).
- **Funding fica fora** do replay (a OKX só devolve o valor atual). Hoje nenhuma regra do checklist mecânico usa funding, então não afeta o resultado; se virar filtro, o harness precisa buscar o histórico antes.

### 2.3 Algoritmo do walk-forward (`replay_par`)

Para cada par, o loop avança um candle de 1h por vez, começando após aquecimento mínimo (`ATR_PERIOD + 2·PIVOT_WINDOW + 2`):

1. **Janela idêntica à de produção.** `janela_1h` = últimos **150** candles de 1h até o instante atual; `janela_4h` = últimos **100** candles de 4h com `ts ≤ agora`. É exatamente o que `fetch_candles(limit=150/100)` entrega ao vivo (ver §2.6 — isto foi um bug corrigido).
2. **Tendência 4h** (`classify_trend_4h`, pivôs fractais com janela ±3 candles) e **ATR(14) do 1h**.
3. **Sem zona ativa:** `try_map_new_zone` tenta mapear uma zona candidata de Setup A (rompimento + retest) ou B (reversão em zona), respeitando cooldowns.
4. **Com zona ativa:** `check_zone_confirmation` devolve `confirmado`, `invalidado`, `tocou` ou nada.
   - `confirmado` (e não contra a tendência, no caso do Setup B) → `compute_suggestion` calcula **entrada** (fechamento do candle de confirmação do 1h), **stop** (extremo da varredura ± `STOP_BUFFER_ATR_MULT` × ATR) e **alvo**; o sinal é registrado e a zona entra em cooldown.
   - `invalidado` → cooldown, zona descartada.
   - `tocou` → incrementa toques; a zona expira com **3 toques sem confirmação** (`ZONE_MAX_TOUCHES`) ou **8 candles de 1h sem toque** (`ZONE_MAX_CANDLES_1H`).
5. **Filtro de R:R:** o sinal é `aceito` se `rr ≥ MIN_RR` (2.0). Os rejeitados **também têm o desfecho medido** — é isso que permite calibrar sem a seleção enviesar o dado.

### 2.4 Como o desfecho de cada sinal é medido (`desfecho_mecanico`)

Geometria pura de preço, sem julgamento. A partir dos candles de 1h **fechados** com `ts` posterior à confirmação:

- **Compra:** stop tocado se `low ≤ stop`; alvo tocado se `high ≥ alvo`. **Venda:** espelho.
- **Resultado:** `−1R` se o stop for tocado; `+rr` (o R:R sugerido) se o alvo for tocado; `None` enquanto nenhum dos dois ocorreu (trade ainda aberto, excluído da expectância).
- **Stop e alvo no mesmo candle:** não há dado intra-candle para saber a ordem, então vale a **convenção conservadora — stop primeiro**.
- **MAE / MFE:** excursão máxima contra / a favor, em múltiplos de R, calculadas mesmo sem desfecho.
- **Breakeven (apenas simulação):** `breakeven_apos_r` move o stop para a entrada depois que o preço andou X·R a favor (efetivo só a partir do candle seguinte). **Nunca usado em produção.**

A mesma função serve a três usos, para não existirem três cópias da aritmética: diário humano (`track_open_trade_outcomes`), calibração ao vivo (`track_mechanical_outcomes`) e backfill (`backfill_mecanico.py`).

### 2.5 Parâmetros e varreduras

Valores em vigor (`fetch_and_check.py`): `PIVOT_WINDOW = 3`, `ATR_PERIOD = 14`, `ZONE_ATR_MULT = 0.25` (meia-largura da zona), `STOP_BUFFER_ATR_MULT = 0.1`, `MIN_RR = 2.0`, `ALVO_REGRA_ATUAL = "proximo"`.

`replay.py --varrer <param>` varia um parâmetro e imprime sinais / aceitos / resolvidos / wins / soma de R / expectância:

| Flag | O que varia |
|---|---|
| `stop_buffer` | `STOP_BUFFER_ATR_MULT` de 0.0 a 1.0 |
| `alvo` | regra de alvo: pivô **mais recente** vs. **mais próximo** (a segunda é a autoritativa desde a v6) |
| `min_rr` | 0.0 a 4.0 (calculado sobre um único replay-base, só refiltrando) |
| `breakeven` | stop em zero a zero após 0.5 / 0.75 / 1.0 / 1.5 / 2.0 R |

A varredura de `stop_buffer` e `breakeven` sobrescreve temporariamente a constante do módulo (`m.STOP_BUFFER_ATR_MULT`) e a restaura num `finally`.

### 2.6 Estatística

- **Métrica:** expectância em R por trade resolvido = soma de R ÷ nº de resolvidos; taxa de acerto; MAE mediano dos vencedores.
- **Intervalo de confiança:** bootstrap percentil 95% (5.000 reamostragens, semente 42) sobre os resultados em R, com reamostragem **por sinal**.
- **Limitação assumida:** os 10 pares são correlacionados (beta de mercado) e o bootstrap trata os sinais como i.i.d.; o IC real é provavelmente mais largo. Corrigir exigiria bootstrap por bloco de tempo — nesta família isso não foi implementado (nas famílias B e C foi).
- **Sem custos:** o replay padrão **não inclui** taxa, spread, slippage nem funding. Incluí-los só pioraria o número.

### 2.7 Bug de escopo corrigido em 11/09/2026 (importante para ler resultados antigos)

O replay originalmente passava `c1h[:i+1]` — uma janela que **crescia sem limite**. Isso deixava `nearest_target_candidate()` alcançar candles arbitrariamente antigos (no Setup C, um pavio de flash-crash de 11 meses antes virou "pivô" com R:R 40). Produção nunca vê mais que 150/100 candles. Corrigido truncando as janelas (`PROD_1H_LIMIT = 150`, `PROD_4H_LIMIT = 100`).

Consequências registradas: o "paradoxo do MIN_RR" (mais R:R → pior expectância, monotônico) era artefato e foi **revertido**; as leituras positivas de ARB/XRP no Setup C a 90/400 dias eram outliers ou o mesmo bug. O achado central — expectância negativa no checklist mecânico — sobreviveu.

### 2.8 Setup C (order block + FVG)

`replay_setup_c.py` reaproveita o mesmo harness de saída (stop/alvo/R:R/`desfecho_mecanico` idênticos aos de A/B) e troca só a **fonte de detecção de zona**:

- **A) "lib como está":** `smartmoneyconcepts` (`smc.ob()` + `smc.fvg()`, `swing_length=10`).
- **B) "caseiro":** mesmo conceito de order block (último candle oposto antes do rompimento de estrutura), mas com `find_confirmed_pivots` (`PIVOT_WINDOW=3`) do projeto; FVG com filtro de tamanho mínimo `0.05 × ATR`.

Walk-forward com janela de contexto de 200 candles por passo; zona só conta como nova se formada nos últimos 3 candles; só aceita zona alinhada com a tendência 4h; entrada no fechamento ao tocar, alvo pelo pivô mais próximo, `MIN_RR ≥ 2.0`. Há também um cruzamento qualitativo contra o **gabarito** de trades reais do analista OTS (`check_gabarito_setup_c.py`, `setup-c-gabarito.md`): "hit" = zona detectada que sobrepõe a faixa do gabarito, na direção certa. Esse cruzamento tem n=3 e é indício, não prova.

### 2.9 O que a família A concluiu

- Replay de 300 dias, 10 pares, `MIN_RR = 2.0`: n ≈ 534–539, expectância ≈ **−0.147R**, IC95 ≈ [−0.28, −0.001]. Reconfirmado em 14/09/2026 (n=534).
- Não há `MIN_RR` testado (0.0 a 4.0) com expectância positiva e confiável; baixar o R:R não ajuda.
- O diário ao vivo (34 trades, −0.13R, IC [−0.62, +0.44]) reproduziu o replay. **Setups A/B encerrados em 25/09/2026** (`SETUP_AB_ENCERRADO = True`); as confirmações continuam alimentando só `sinais_mecanicos`, para calibração.
- Setup C: sem edge positivo a 400 dias após a correção do bug; o detector caseiro ficou negativo com significância no agregado.

---

## 3. Família B — Estudos avulsos pré-registrados

### 3.1 Estrutura de um estudo

Cada estudo é um script `monitor/replay_<nome>.py` autocontido, com **regras e critério de aprovação escritos no docstring antes de baixar os dados** (pré-registro). O resultado vai para `claude/<nome>.log` e é resumido em `estudos-avulsos.md`. Estudos listados lá cobrem: leque de médias, 1-2-3 (Crisp e de 3 candles), estocástico+VWAP, 9.1 de Williams, IFR curto, Renko+VWAP, inside bar, Landry, Didi, estratégias do Carver (carry, skew, momentum, aceleração, mean reversion, tendência canônica), "151 Trading Strategies", momentum de qualidade, cash-and-carry, sazonalidade, e o acervo FMZ (triagem + mecanismos).

### 3.2 Dados e universos

- **Fonte:** candles OKX (cache local por script; o cache com volume de `replay_stoch_vwap.py` é compartilhado por vários estudos) e, desde 22/09/2026, Binance USDT-M (`dados_binance.py`: klines com retentativa, cache em `cache_binance/`, histórico de funding desde 2019, e spot para cash-and-carry). A Binance aceita os `instId` da OKX (`BTC-USDT-SWAP` → `BTCUSDT`).
- **Só candles fechados** entram (`closeTime` no passado).
- **Amostras separadas** — recurso finito, gasto à medida que são usadas:

| Amostra | Conteúdo | Papel |
|---|---|---|
| **A** | 20 perpétuos OKX (os 10 do monitor + BNB, TRX, ZEC, HYPE, ADA, XLM, NEAR, AVAX, LTC, BCH) | onde a ideia nasce; *desenvolvimento / descritivo* |
| **B** | 80 perpétuos OKX listados há ≥ 1000 dias, fora de A | confirmação fora da amostra |
| **C** | 83 perpétuos OKX listados há 400–1000 dias | confirmação |
| **D** | 215 perpétuos que só existem na Binance (`universo_d.txt`) | amostra independente de pares |
| **E** | 153 perpétuos Binance correspondentes a B e C (`universo_e.txt`) | amostra nova para o combo de prêmios |
| **Papel** | dados daqui para frente | único teste realmente fora da amostra *no tempo* |

Ressalva registrada: os **mesmos pares na Binance não são amostra independente** do mesmo par na OKX (mesmo mercado, mesmo período).

### 3.3 Simulação de execução

- **Custo:** padrão 0.18% do nocional ida+volta, convertido em R pela distância do stop (`CUSTO_RT = 0.0018`). Isso explica por que stops curtos e tempos gráficos curtos são destruídos pelo custo (0.035R no 1D vs. 0.54R no 15m, no estudo 1). Estudos posteriores usam custo por tipo de saída (entrada taker 0.05% + 0.05% slippage; alvo maker 0.02%; stop taker), funding real da Binance, ou 0.06% do nocional negociado nas estratégias contínuas.
- **Candle da entrada (regra OHLC):** quando a entrada é por **ordem stop** e o stop também é tocado no mesmo candle, a regra antiga ("conservadora": qualquer toque é perda) era enviesada contra o trade. Padrão atual (`stop_vale_no_candle_entrada`): se o candle fechou **a favor**, o extremo contra veio *antes* do gatilho e o stop não vale; se fechou contra, vale. Entrada na abertura ou no fechamento não é afetada. `REGRA_CANDLE_ENTRADA=conservadora` reproduz a regra antiga. Os estudos 1–4 foram reexecutados com a regra corrigida.
- **Trades abertos no fim do histórico:** fechados a mercado, não descartados (descartar esconderia a compra que nunca voltou ao lucro).
- **Dimensionamento (quando aplicável):** 1% de risco, teto de 3x, 2 posições simultâneas, trava de −6R por semana, com 200 sorteios da ordem de sinais do mesmo dia (`replay_123_carteira.py`).
- **Posição contínua** (Carver): dimensionada por volatilidade (EWMA(32) + 0.3 da média longa, piso de 10%), aquecimento de 60 dias descartado, teto de 1× por instrumento e 3× bruto — correção feita depois de uma posição de 1250× o capital aparecer na rodada de fumaça.

### 3.4 Protocolo estatístico

1. **Critério PASSA:** expectância líquida com **IC95 inteiro acima de zero**. Na prática, só "decide" o tempo gráfico/amostra marcados como tal; os demais são descritivos.
2. **Bootstrap** reamostrando **dias de entrada** (não trades), para respeitar a correlação entre pares (`ic_bootstrap`, 5.000 reamostragens, semente 42). Desde 22/09: **bloco de semana** quando a duração média do trade passa de ~5 dias.
3. **Holdout temporal** (estudos com grade de parâmetros): divide o histórico no ponto médio; escolhe-se a célula de maior expectância líquida na **1ª metade**; **só essa célula** é testada na 2ª. A grade completa vai para o log, sem poder de decisão.
4. **n ≥ 200 trades no treino** para a célula concorrer (no estudo 9, o mínimo de 30 deixou uma célula semanal de 40 trades vencer por sorte). Sem nenhuma célula com n ≥ 200, registra-se "sem amostra para decidir", não "não passa".
5. **Confirmação fora da amostra** (desde o estudo 8): a célula escolhida também precisa ter IC95 > 0 nos 80 pares da amostra B.
6. **Teste de beta obrigatório** antes de qualquer PASSA direcional: excesso sobre entradas aleatórias de mesma duração e mesmo lado. A linha de base foi corrigida no estudo 23 para ser **transversal** (mesmas datas e lado em até 30 outros pares), porque a versão "mesmo par" usa a deriva realizada da série inteira e gerava falso positivo em 5 de 12 estratégias num passeio aleatório.
7. **Correção de Bonferroni** em famílias de hipóteses testadas na mesma amostra (ex.: IC de 98.75% para 4 testes; 99.55% para K = 11 no acervo FMZ).
8. **Alerta de sanidade:** comparar o Sharpe observado com o reportado na fonte; um valor muito acima (ex.: carry relativo +1.77 vs. 0.8–1.0 do livro) é tratado como suspeito.

### 3.5 Validação do próprio simulador

Antes de confiar num resultado, o simulador é testado num **passeio aleatório sem drift**, com caminho intra-candle fino (120–480 passos): o resultado bruto deve ficar em zero. Isso já expôs três problemas — viés da regra conservadora no candle de entrada, viés da linha de base "mesmo par" e lookahead numa tolerância de "N candles" no Didi (dava +0.17 a +0.38R falsos). Scripts: `fmz_teste_passeio.py`, `fmz_teste_passeio_mec.py`.

### 3.6 Acervo FMZ (`strategies-for-test`)

5.807 estratégias, 91% PineScript. Triagem por **amostra sorteada** (semente 20260923, população de 3.764 scripts traduzíveis), sem escolha a dedo. `fmz_motor.py` emula o broker do Pine; cada estratégia roda com os **parâmetros padrão do script**. Duas etapas: em A (avança com n ≥ 100, líquido > 0 e excesso > 0) e em D+E (368 pares; decide com IC ajustado por Bonferroni). Resultado: 0 de 12 sobreviveram.

### 3.7 Regra de ouro

Os estudos **não se reabrem variando parâmetros sobre os mesmos dados**. Uma nova versão exige regra nova pré-registrada e amostra ainda não consumida. Resultados exploratórios (como a varredura do 1-2-3, estudo 13) são declarados como tal — a seleção infla o vencedor — e o veredito vem de amostra nova.

---

## 4. Família C — Teste de papel (forward test)

Para hipóteses que passaram ou ficaram promissoras e só podem ser confirmadas com tempo:

- **Scripts:** `unlock_paper.py` (venda de perpétuo antes de desbloqueio de tokens para insiders), `novos_paper.py` (venda de perpétuo recém-lançado com stop de +50%), `sabado_paper.py` (cesta comprada de sexta a sábado), `monitoring_paper.py` (venda de perpétuo nas 24h após a Monitoring Tag, desde 05/10/2026).
- **Regra congelada** no docstring, não alterável durante o teste; registra versões em paralelo (ex.: pura vs. com hedge) com custo e funding reais. **Nenhuma ordem é enviada.**
- **Critério de leitura fixado antes de começar:** só reavaliar com 150 trades fechados (desbloqueio), 100 (lançamentos), 104 sábados (~2 anos) ou 24 anúncios (Monitoring Tag). Antes disso, qualquer leitura é ruído.
- **Execução:** workflow horário no GitHub Actions. A fapi da Binance responde 451 a IPs dos EUA, então os scripts chamam o proxy `proxy-vercel/` (Tóquio) via o secret `UNLOCK_PAPER_FAPI`; preços de fechamento vêm do `data.binance.vision`. Eventos que só aparecem no calendário *depois* da data de entrada são descartados ("conhecido tarde") para não olhar o futuro.

---

## 5. Os dois registros de resultado do monitor ao vivo

Separados de propósito (`CLAUDE.md`):

- **`trades`** (`claude/trade_journal.db`, espelho editável em `claude/sinais.md`): diário humano; só a coluna `resultado_r` conta para o gate de 30 trades. O trade #1 foi identificado retroativamente como backtest e não conta.
- **`sinais_mecanicos`**: toda confirmação detectada, inclusive as descartadas por R:R, com `resultado_mecanico_r`, `mae_r` e `mfe_r` medidos por `desfecho_mecanico`. Espelho somente leitura em `claude/calibracao.md`. Medir só os trades "entrados" enviesaria a calibração pela própria seleção.

---

## 6. Como rodar

Da raiz do repositório (Python; os scripts de replay usam só biblioteca padrão, exceto `replay_setup_c.py`, que usa `numpy` e `smartmoneyconcepts`):

```
python monitor/replay.py                              # parâmetros atuais, 10 pares, 33 dias
python monitor/replay.py --dias 300                   # janela longa
python monitor/replay.py --pares BTC,ETH              # subconjunto
python monitor/replay.py --varrer min_rr --dias 300   # também: stop_buffer | alvo | breakeven
python monitor/replay_setup_c.py                      # Setup C (lib vs. caseiro)
python monitor/replay_ema_ribbon.py                   # exemplo de estudo avulso (cada um tem o seu)
python monitor/dados_binance.py --universo            # pré-baixa candles da Binance para o cache
```

Os estudos avulsos baixam e guardam cache em pastas próprias (`cache_stoch_vwap/`, `cache_binance/`, `cache_ema_ribbon/`); apagar o cache força novo download. Os logs de cada rodada ficam em `claude/*.log`. Os testes de regressão da lógica de zonas estão em `monitor/test_zone_logic.py` e `monitor/test_v5_fixes.py`.

---

## 7. Limitações conhecidas

1. **Replay A/B/C sem custos** e sem funding; bootstrap por sinal (não por bloco de tempo) com pares correlacionados — IC provavelmente otimista.
2. **Resolução de 1h:** stop e alvo no mesmo candle contam como stop. Entradas por ordem stop em candles curtos dependem da heurística OHLC, validada só em passeio aleatório.
3. **Viés de sobrevivência:** todos os universos são formados por perpétuos listados **hoje**; delistados e moedas que morreram não entram (exceção parcial: o estudo de lançamentos incluiu deslistados).
4. **Histórico curto:** perpétuos de cripto existem desde ~2019/2020, ≈ 6–7 anos. Para efeitos de Sharpe ~0.6, o erro padrão (~1/√anos ≈ 0.4) torna a prova com dados históricos inviável independentemente do número de pares — daí o teste de papel.
5. **Amostras gastas:** A, B, C e D já foram usadas várias vezes; novas hipóteses só têm E, universos novos ou papel.
6. **Filtro humano nunca testado:** o replay mede o checklist mecânico puro; o filtro de julgamento do plano nunca foi preenchido nos 34 trades do diário, e a decisão do projeto é uma regra 100% mecânica.
7. **Detalhe fino do plano** (texto do `plano-trade-price-action.md`, backtest original `backtest-setup-ab.md`) vive num Projeto separado do claude.ai e não está neste repositório.
