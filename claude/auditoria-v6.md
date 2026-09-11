# Continuação — 10/09/2026 (v6): as 3 pendências da auditoria v5

> Continuação de [`auditoria-v5.md`](auditoria-v5.md). Não repete o que já foi coberto lá — cobre só a execução das 3 pendências que ficaram em aberto, na ordem que o Gabriel decidiu seguir: (1) trocar a regra do alvo, (2) rodar a simulação de novo, (3) reavaliar `MIN_RR` com o dado novo, (4) testar breakeven só na simulação.

---

## 1. Regra do alvo: trocada para "mais próximo"

`ALVO_REGRA_ATUAL = "proximo"` (era "recente", regra da v1). `compute_suggestion` deixou de devolver uma tupla posicional de 7 campos e passou a devolver um dict — mais claro e menos frágil pra crescer (já tinha virado difícil de ler com `extremo, stop_sug, alvo_sug, rr_sug, preco_entrada, alvo_prox, rr_prox = sug`).

O dict sempre calcula os dois alvos (`alvo_recente`/`rr_recente` e `alvo_proximo`/`rr_proximo`), independente de qual é autoritativo — isso é o que permite comparar as duas regras continuamente, não só numa foto única. `alvo_sugerido`/`rr_sugerido` (autoritativos) e `regra_alvo` (qual decidiu) são os campos que entram no filtro de `MIN_RR` e no diário.

**Trades anteriores a esta mudança não foram reescritos.** `alvo_sugerido`/`rr_sugerido` históricos continuam sendo o valor que de fato decidiu aquele trade na hora (reescrever seria revisionismo). Uma migração automática só rotulou essas 28 linhas com `regra_alvo='recente'`, preenchendo `alvo_recente`/`rr_recente` com o que já era o valor histórico — sem inventar dado novo.

## 2. Simulação rodada de novo com a regra corrigida

Com a regra "próxima", os alvos ficam mais perto do preço — o que significa R:R mais baixo pra maioria dos sinais, e menos sinais passam no filtro `MIN_RR ≥ 2`:

| | Regra "recente" (v5) | Regra "próxima" (v6) |
|---|---|---|
| Sinais aceitos (R:R ≥ 2) | 168 | **59** |
| Expectância | -0.167R | **-0.136R** |
| IC 95% bootstrap | [-0.425, +0.103] | [-0.533, +0.296] |
| Sem filtro de R:R (n) | 416 → -0.113R | 414 → -0.066R |
| IC 95% (sem filtro) | [-0.236, +0.019] | [-0.152, +0.027] |

Leve melhora na expectância central, mas **a amostra ficou menor** (menos sinais passam o filtro), então o intervalo de confiança ficou mais largo, não mais estreito. Continua sem edge demonstrável — nem a favor, nem contra.

## 3. O paradoxo de `MIN_RR` persistiu — achado mais forte do que se pensava

Na v5, a hipótese era que "exigir mais R:R piora o resultado" fosse **sintoma do bug do alvo** (R:R alto = selecionar alvo distante e velho, não tese melhor). Rodando a mesma varredura com a regra já corrigida:

```
MIN_RR 1.0 → n=121, 35.5% acertos, -0.017R
MIN_RR 1.5 → n= 85, 27.1% acertos, -0.110R
MIN_RR 2.0 → n= 59, 23.7% acertos, -0.136R   ← atual (regra do plano)
MIN_RR 2.5 → n= 33, 15.2% acertos, -0.352R
MIN_RR 3.0 → n= 27, 11.1% acertos, -0.485R
MIN_RR 4.0 → n= 14,  7.1% acertos, -0.596R
```

**A degradação monotônica continuou**, mesmo depois de corrigir o bug que era a explicação mais provável. Isso muda a conclusão: não é (só) um artefato de implementação — é um padrão mais geral de como o checklist mecânico atual está selecionando sinais. `MIN_RR = 2.0` é regra do plano de risco (seção 3.3), não parâmetro de calibração, e **não foi alterado**. Mas o achado é real e mais sólido do que na v5, e fica registrado explicitamente para você decidir com calma — isto é metodologia, não é correção de bug, e eu não vou decidir sozinho por você.

## 4. Stop no breakeven — testado só na simulação, não implementado

Adicionei `breakeven_apos_r` como parâmetro **opcional** em `desfecho_mecanico()` — usado exclusivamente por `monitor/replay.py --varrer breakeven`. Nenhum caminho de produção (`fetch_and_check.py`) chama essa opção; o comportamento ao vivo não mudou em nada.

```
sem breakeven (atual)  → n=59, -0.136R
breakeven em 0.50R     → n=59, +0.045R   ← único resultado positivo de toda a auditoria
breakeven em 0.75R     → n=59, -0.040R
breakeven em 1.00R     → n=59, -0.052R
breakeven em 1.50R     → n=59, -0.034R
breakeven em 2.00R     → n=59, -0.085R
```

Verifiquei estatisticamente antes de dar qualquer peso a esse número positivo: **IC 95% bootstrap para breakeven em 0.5R = [-0.310, +0.444]** — inclui zero e inclui valores bem negativos. Com n=59, isso é ruído, não sinal. **Não implementei nada em produção.** Se quiser reabrir essa ideia no futuro, o caminho certo é acumular mais histórico (mais pares, mais tempo) antes de decidir, não confiar num resultado pontual como este.

---

## O que ficou pendente de verdade

Nada das 3 pendências virou "regra nova" na automação — como pedido, troquei o alvo (item 1, decisão já tomada e aplicada), rodei a simulação (item 2), e testei o breakeven só na simulação (item 4, sem implementar). O único item que continua em aberto, porque é decisão sua e não teria como eu decidir sozinho, é:

- **O que fazer com o achado do item 3** (exigir mais R:R piora o resultado, mesmo com o alvo corrigido). Não é evidência estatisticamente forte (amostras pequenas por faixa), mas é um padrão consistente que já sobreviveu a uma correção de bug. Vale a pena ficar de olho conforme mais trades reais forem se acumulando.

  **Atualização 11/09/2026 — ver seção abaixo: esse achado não sobreviveu a uma segunda correção de bug.** A instabilidade sempre esteve lá (IC muito largo nas faixas de R:R alto); o bug de escopo do replay só mascarava isso com um padrão que parecia mais liso do que a amostra realmente sustenta.

---

## Correção de escopo no replay (11/09/2026)

Pesquisando o Setup C (`claude/setup-c-testes.md`) sobre um histórico bem mais longo (400 dias), achei um trade com R:R de 40 — investigando, o alvo vinha de um candle de flash-crash de 1h de **11 meses antes**, tratado como "pivô confirmado" válido. Causa raiz: `nearest_target_candidate` (chamada por dentro de `compute_suggestion`) roda sobre o array de candles inteiro que recebe — e `monitor/replay.py` monta `janela_1h = c1h[:i + 1]`, que cresce sem limite a cada passo do walk-forward. Quanto mais longa a janela de replay, maior o risco de a busca por "pivô mais próximo em preço" alcançar algo estruturalmente irrelevante.

Isso nunca acontece ao vivo: a produção busca sempre `candles_1h = fetch_candles(..., limit=150)` e `candles_4h = fetch_candles(..., limit=100)` — nunca vê mais que isso. `replay.py` foi corrigido pra replicar exatamente esse limite (`janela_1h`/`janela_4h` agora truncadas aos últimos 150/100 candles a cada passo, em vez de acumular o histórico inteiro).

**Validação — os achados desta auditoria (v6) continuam de pé?** Rodei o replay ANTES e DEPOIS do fix sobre o mesmo dado (mesmos 800 candles de 1h, 33 dias, para não confundir o efeito do fix com a janela ter avançado no tempo):

| | Antes do fix | Depois do fix |
|---|---|---|
| MIN_RR=1.0 | n=117, exp -0,022R | n=108, exp -0,084R |
| MIN_RR=1.5 | n=86, exp -0,097R | n=75, exp -0,109R |
| MIN_RR=2.0 (produção) | n=63, exp -0,072R, IC95% [-0,446, +0,350] | n=56, exp -0,095R, IC95% [-0,538, +0,396] |
| MIN_RR=2.5 | n=40, exp -0,278R | n=37, exp -0,078R |
| MIN_RR=3.0 | n=29, exp -0,520R | n=28, exp -0,175R |
| MIN_RR=4.0 | n=15, exp -0,623R, IC95% [-1,000, +0,131] | n=17, exp +0,111R, IC95% [-1,000, +1,306] |

- **O achado central da v6 não muda**: em MIN_RR=2.0 (o filtro real de produção), IC cruza zero antes e depois, com magnitude parecida (-0,072R vs -0,095R) — continua sem edge demonstrável, com ou sem o bug.
- **O "paradoxo de MIN_RR" (item 3, degradação monotônica com R:R mais alto) não sobrevive.** Depois do fix, a curva deixa de ser monotônica e chega a inverter em MIN_RR=4.0 (+0,111R). Mas o IC em MIN_RR=4.0 é enorme dos dois lados (antes: [-1,000, +0,131]; depois: [-1,000, +1,306], n=15-17) — a mudança de sinal está inteiramente dentro do ruído. Conclusão: o padrão "mais liso" que a v6 reportou não era mais confiável que isso, o bug só mascarava a instabilidade real da amostra em faixas de R:R alto.
- Total de sinais mudou de 437 para 314 sobre o mesmo dado — o fix não afeta só o alvo, afeta toda a detecção de zona/tendência (as mesmas funções recebem a mesma janela limitada, replicando fielmente o que a produção vê a cada ciclo).

**Conclusão**: o bug era real e o fix é correto, mas não muda nenhuma decisão de produção já tomada — o risco pra v5/v6 era baixo porque a janela usada (33 dias, no máximo ~5x o limite de produção) nunca chegou perto de algo tão extremo quanto o pavio de 11 meses que apareceu no teste de 400 dias do Setup C (lá a janela chegava a ~64x o limite de produção). O item pendente acima ("exigir mais R:R piora o resultado") deixa de ser um achado a acompanhar — era um artefato de janela sem limite combinado com amostra pequena, não um padrão real do checklist mecânico.

## Janela estendida (300 dias) e um resultado que muda de categoria (11/09/2026)

Pergunta do Gabriel: "se diminuirmos o R:R mínimo, o resultado melhora?" Com o bug de escopo corrigido, `replay.py` ganhou o mesmo argumento `--dias` do `replay_setup_c.py` (default 33, preserva o comportamento original) — dá pra responder com muito mais amostra do que os 33 dias de sempre.

Rodei `--varrer min_rr --dias 300` (10 pares, ~7.200 candles de 1h por par) e recalculei o IC 95% bootstrap pra cada faixa (o `resumir()` padrão do script não imprime IC, só soma/expectância):

| MIN_RR | n | Expectância | IC 95% bootstrap |
|---|---|---|---|
| 0,0 (sem filtro) | 3190 | -0,076R | **[-0,110, -0,042]** |
| 1,0 | 1209 | -0,125R | **[-0,205, -0,043]** |
| 1,5 | 794 | -0,145R | **[-0,252, -0,033]** |
| 2,0 (produção atual) | 539 | -0,147R | **[-0,289, -0,001]** |
| 2,5 | 361 | -0,147R | [-0,333, +0,053] |
| 3,0 | 256 | -0,095R | [-0,331, +0,156] |
| 4,0 | 122 | -0,111R | [-0,454, +0,283] |

**Isso muda de categoria em relação a tudo que já foi reportado nas auditorias v5/v6**: de "amostra pequena demais pra concluir" (IC sempre cruzando zero) para **expectância negativa estatisticamente significativa em MIN_RR de 0,0 até 2,0** — o IC bootstrap fica inteiramente abaixo de zero nessas quatro faixas, coisa que nunca tinha acontecido antes neste projeto (nem nos 437 sinais da v6 original, nem nos 314 pós-fix a 33 dias).

**Resposta direta à pergunta**: baixar `MIN_RR` para 1,5 ou 1,0 **não ajuda** — o ponto central fica igual ou um pouco pior (-0,125R a -0,147R) do que o `MIN_RR=2,0` atual (-0,147R), não melhor. Não existe, nesta amostra, uma faixa de R:R baixo que vire positiva. Acima de 2,5 o IC volta a cruzar zero, mas por causa de n menor (256-361), não porque o resultado melhorou de verdade.

**Ressalvas, pra não overclaim**:
1. Isto é só o checklist mecânico puro (`sinais_mecanicos`/replay), sem o filtro de julgamento humano que o plano pressupõe (seção 4) — o Gabriel já foi alertado antes que está operando o sistema mecânico sem essa camada.
2. Não inclui custo de execução (taxa, spread, slippage, funding) — incluir só pioraria o número, nunca melhora.
3. **Os 10 pares não são observações independentes.** O `CLAUDE.md` já registra um achado de 09/09/2026 sobre confirmações correlacionadas entre pares de altcoin (beta de mercado, não sinal técnico independente). O bootstrap acima trata os 3190/539/etc. sinais como i.i.d., o que infla artificialmente a confiança quando vários deles vêm do mesmo movimento de mercado batendo em múltiplos pares ao mesmo tempo. A direção do achado (negativo) não muda, mas o IC real é provavelmente mais largo do que o mostrado aqui. Não tenho, hoje, uma forma calibrada de corrigir por essa correlação (exigiria block bootstrap por janela de tempo, não por sinal) — registrar como limitação conhecida, não decidido.

**O que isso significa pra decisão de produção**: `MIN_RR=2.0` é regra do plano de risco (seção 3.3), não parâmetro de calibração — não mudei e não proponho mudar por causa disto. Mas agora há uma base mais sólida pra dizer que o checklist mecânico puro, do jeito que está, tem edge negativo — o que reforça (com dado bem mais forte que antes) a recomendação já feita de que a camada de julgamento humano na seção 4 precisa estar sendo genuinamente exercida, não só carimbada.
