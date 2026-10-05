# Contexto do projeto — trading-monitor

> Este arquivo existe para que qualquer sessão do Claude Code neste repositório comece com o contexto que normalmente viveria só na cabeça do Gabriel (ou em conversas antigas no claude.ai). Leia antes de sugerir mudanças de arquitetura, calibrar parâmetros ou avaliar setups novos.

## O que é este projeto

Sistema pessoal de trading de futuros de criptomoedas (perpétuos USDT), centrado numa metodologia estruturada de price action / Smart Money Concepts (SMC/ICT). Corretora principal: Binance (BTC/USDT e outros pares); OKX é usada só para monitorar funding rate (BTC-USDT-SWAP). Objetivo central: comprovar edge com regras objetivas e rastreáveis **antes** de qualquer capital real — este é um restart de um projeto anterior similar, priorizando desde o início a formalização objetiva de regras e o rastreamento de expectância por setup.

**Gate de validação: 30 trades em papel** precisam ser completados, com checklist seguido à risca, antes de considerar capital real. O trade #1 do diário foi identificado retroativamente como backtest e não conta para essa contagem.

## Pares e posições

- Expandido de BTC-apenas para **10 pares** (decisão de 07/09/2026): BTC, ETH, SOL, XRP, DOGE, ARB, WLD, SUI, UNI, LINK — todos perpétuos USDT.
- A contagem de 30 trades é agregada entre todos os pares (não dividida por par).
- Máximo de **2 posições simultâneas** (global, entre os 10 pares — revisado de uma proposta inicial de 1).

## Os dois (em breve três) setups

> **Setups A/B ENCERRADOS em 25/09/2026 — não passaram.** A meta dos 30 fechou em 34 trades a −0.13R/trade (IC 95% [−0.62, +0.44]), na mesma direção do replay de 300 dias (n=534, IC inteiramente negativo). O filtro humano não foi testado, e o Gabriel decidiu não testar: **o objetivo do projeto é uma regra 100% mecânica.** `SETUP_AB_ENCERRADO = True` em `fetch_and_check.py`: as confirmações só alimentam `sinais_mecanicos` (calibração), sem candidato no diário nem push. Não reative nem recalibre os setups para "tentar de novo". O que passou até agora vem de mecanismo estrutural (evento/fluxo: desbloqueio de tokens, carry), não de padrão gráfico. Veja `claude/estudos-avulsos.md`, seção "Setups A/B".

- **Setup A — Rompimento + Retest**: continuação de tendência. Contexto no 4h, rompimento de estrutura no 1h a favor da tendência, entrada no retest com confirmação (rejeição ou higher low/lower high).
- **Setup B — Reversão em Zona**: reversão em order block/zona de oferta-demanda no 4h, após varredura de liquidez + rejeição no 1h.
- Regras comuns: R:R mínimo 1:2, zona expira após 8 candles de 1h sem toque ou 3 toques sem confirmação válida.
- **Setup C (em formalização, decidido 09/09/2026)**: baseado em order block + Fair Value Gap (FVG), inspirado num trade real do analista OTS. Ainda não tem código — precisa de implementação nova do zero (não existe detecção própria de order block/FVG no repo hoje). Amostra ainda pequena (1 trade observado); Gabriel decidiu seguir formalizando mesmo assim, buscando reunir mais amostras.

## Gestão de risco (não negociável, não é "calibração fina")

- 1% de risco por trade.
- Teto de alavancagem: 3x (nunca aumentar para "caber" um stop mais largo — o tamanho da posição que diminui).
- R:R mínimo 1:2 para entrar.
- Limite de perda diário -3R, semanal -6R.

## Arquitetura da automação — histórico importante

- A automação **migrou do ambiente Cowork do Claude para GitHub Actions gratuito**, para não consumir o uso semanal do plano Pro.
- `monitor/fetch_and_check.py`: só biblioteca padrão do Python, replica o checklist mecânico (classificação de tendência via pivôs fractais, mapeamento de zona, detecção de confirmação/invalidação).
- `btc-monitor.yml`: workflow do GitHub Actions, agendamento horário.
- Notificações push via ntfy.sh.
- **`README.md` da raiz é um painel gerado** por `monitor/painel.py` a cada execução (resumo de cada estratégia para ler no app do GitHub) — não edite à mão; mude o script. A documentação antiga do monitor foi para `monitor/README.md`.
- **O script deliberadamente NÃO faz interpretação qualitativa, dimensionamento de risco nem avaliação de estado pessoal** — isso é manual, feito colando atualizações de status numa conversa com o Claude. Essa separação é intencional e importante — não proponha automatizar isso.
- **Acesso à fapi da Binance pelo runner:** o GitHub Actions roda em IP dos EUA e leva 451. Os scripts em papel (`unlock_paper.py`, `novos_paper.py`, `sabado_paper.py`, `monitoring_paper.py`) chamam a fapi via o secret `UNLOCK_PAPER_FAPI`, que aponta para o proxy `proxy-vercel/` (função Vercel fixada em Tóquio, `hnd1`; projeto `binance-fapi-proxy`, domínio de produção `binance-fapi-proxy-orcin.vercel.app`). Sem ele, o tipo do contrato vem "?" e perpétuos de ações abrem no registro de perpétuo novo (aconteceu com CVNA/OKLO/RUM/TWST/XOM, descartados em 30/09/2026). **Não use Cloudflare Workers para isso:** a Binance responde 403 a requisições de Workers (`proxy/worker.js` fica só como registro).
- **Proxy fora em 10/2026 (resolvido em 05/10/2026):** o projeto da Vercel foi ligado ao repositório com Root Directory `.`, e cada commit do bot publicava a raiz do repo sem `api/` (404 em tudo, região `iad1`). Os registros em papel seguiram com "success" e tipo/funding pendentes, sem aviso. A correção foi Root Directory = `proxy-vercel`. Agora `monitor/saude_fontes.py` testa a fapi a cada execução, avisa no ntfy (2 falhas seguidas e recuperação) e põe o alerta em "Precisa de você" no painel.
- Problema conhecido e resolvido: o cron interno do GitHub Actions (`schedule`) era pouco confiável em repositórios novos (disparava irregular ou atrasado). Corrigido usando um cron job externo no Cloudflare como gatilho.
- Candidatos a trade ficam num banco SQLite (`claude/trade_journal.db`); a superfície principal de interação, porém, é o espelho em markdown **`claude/sinais.md`** — Gabriel edita status/resultado de trade direto ali (não no SQLite, que não é prático de editar do celular ou sem editor SQL). O script só deve *anexar* candidatos novos e atualizar campos mecânicos, nunca sobrescrever o que Gabriel editou manualmente.
- Notificações e `sinais.md` mostram **um único preço de entrada sugerido** (fechamento do candle de confirmação do 1h), não uma faixa/zona — decisão explícita: Gabriel quer um número acionável, não um range.
- Candidatos abaixo do R:R mínimo do plano (1:2) **não devem ser gerados nem notificados**.
- O script deve suprimir notificação de sinal novo para um par que já tem um trade aberto registrado.

## Decisões técnicas já tomadas (não reabrir sem motivo novo)

- `smartmoneyconcepts` (biblioteca Python) foi avaliada e **descartada** para detecção de pivô/zona: usa um algoritmo sequencial tipo zigue-zague, divergente da regra de pivô por janela fixa (±3 candles) já validada no backtest histórico (`claude/backtest-setup-ab.md`). Trocar invalidaria a aplicabilidade desse backtest já rodado.
- Frameworks genéricos (Freqtrade, Jesse, Lumibot) foram revisados e descartados por não corresponderem à abordagem do Gabriel.
- Repositório é público: `https://github.com/gabcapelli/trading-monitor`.

## Auditoria v5+v6 (10/09/2026) — o que mudou na arquitetura

Relatórios completos em `claude/auditoria-v5.md` e `claude/auditoria-v6.md` (v6 é a continuação, com as decisões que a v5 deixou em aberto). O que uma sessão nova precisa saber antes de mexer em parâmetro:

- **Dois registros, propósitos diferentes.** `trades` é o diário humano (gate dos 30, editado em `claude/sinais.md`, coluna `resultado_r`). `sinais_mecanicos` é a tabela de **calibração**: toda confirmação mecânica detectada, inclusive as descartadas por R:R baixo, com desfecho medido por geometria de preço (`resultado_mecanico_r`, `mae_r`, `mfe_r`). As duas colunas de resultado são separadas de propósito — só `resultado_r` conta para os 30. Espelho legível: `claude/calibracao.md` (só leitura; `sinais.md` continua sendo o único arquivo editável).
- **`monitor/replay.py`** roda a lógica de detecção inteira sobre histórico paginado da OKX e varre parâmetros (`--varrer stop_buffer|alvo|min_rr|breakeven`). Use isso em vez de calibrar com a amostra do diário.
- **Regra de alvo (v6): a autoritativa agora é "pivô mais próximo"**, não mais "mais recente" (`ALVO_REGRA_ATUAL` em `fetch_and_check.py`). `compute_suggestion` devolve um dict com `alvo_sugerido`/`rr_sugerido` (autoritativos), `regra_alvo` (qual decidiu — `'recente'` em trades anteriores a 10/09/2026, `'proximo'` depois) e sempre os dois alvos calculados (`alvo_recente`/`alvo_proximo`) para comparação contínua.
- **Atualizado 11/09/2026 — agora existe edge NEGATIVO demonstrável no checklist mecânico puro (RR 0 a 2.0), não mais "sem informação suficiente".** Com o bug de escopo do replay corrigido (ver item abaixo) e janela estendida pra 300 dias (10 pares, n bem maior que antes): MIN_RR=2.0 (regra atual) n=539, expectância -0.147R, IC 95% bootstrap **[-0.289, -0.001]** — intervalo inteiramente negativo. RR=1.0 (n=1209): -0.125R, IC [-0.205, -0.043]. RR=1.5 (n=794): -0.145R, IC [-0.252, -0.033]. Sem filtro (n=3190): -0.076R, IC [-0.110, -0.042]. **Baixar o MIN_RR não ajuda** — o centro fica igual ou pior, não melhor. Acima de RR=2.5 o IC volta a cruzar zero (amostra menor). Ressalvas: (1) isso é só o checklist mecânico, sem o filtro de julgamento humano que o plano pressupõe — ver seção "Como o Gabriel gosta de trabalhar"; (2) não inclui custo de execução (taxa/spread/slippage/funding), que só pioraria o número; (3) os 10 pares são correlacionados entre si (ver "Achado em investigação" abaixo), então o n efetivamente independente é menor que a contagem bruta — a direção do achado não muda, mas o IC real é provavelmente mais largo que o bootstrap ingênuo mostra. Detalhe completo em `claude/auditoria-v6.md`. Nenhum valor de `STOP_BUFFER_ATR_MULT` testado torna a expectância positiva.
- **Reconfirmado em 14/09/2026** — mesmo achado do item acima, replicado 3 dias depois com `--dias 300` de novo (n muda pouco: 534 em vez de 539 no MIN_RR=2.0, IC 95% [-0.283, -0.001], praticamente idêntico). Também testado o recorte exato do `claude/calibracao.md` (aceitos vs. descartados) na janela de 300 dias: aceitos (RR≥2.0, n=534) exp -0.146R IC [-0.283, -0.001]; descartados (RR<2.0, n=2626) exp -0.059R IC [-0.089, -0.028] — **os dois lados são negativos e estatisticamente significativos**, descartados só são "menos negativos". Isso corrige uma leitura errada que a amostra ao vivo do diário sugeriu (`calibracao.md` com n=78 mostrava descartados em +0.150R) — com n=44 aquilo era ruído; não existe um subconjunto de R:R baixo com edge positivo escondido. Não inverta o filtro nem baixe o MIN_RR esperando destravar expectância positiva — nenhum ponto testado (0.0 a 4.0) fica positivo com confiança.
- **Achado revertido em 11/09/2026** — não trate mais como sólido: "exigir mais R:R piora a expectância monotonicamente" era artefato de um bug de escopo no `replay.py` (`janela_1h` crescia sem limite a cada passo do walk-forward, diferente da produção que sempre busca só `limit=150`/`limit=100`). Corrigido; refeito o teste sobre o mesmo dado, o padrão monotônico não se repete e o IC em R:R alto é largo demais (n=15-17) pra sustentar qualquer leitura. Detalhe em `claude/auditoria-v6.md`, seção "Correção de escopo no replay". `MIN_RR=2.0` segue como está (é regra do plano de risco, não seria alterado de qualquer forma).
- **Stop no breakeven: testado só na simulação, não implementado.** `desfecho_mecanico()` aceita `breakeven_apos_r` (default `None`, nunca usado em produção). O único resultado positivo de toda a auditoria apareceu em breakeven a 0.5R (+0.045R), mas o IC 95% bootstrap ([-0.310, +0.444]) inclui zero e negativo — é ruído com n=59, não sinal. Não implemente essa regra sem mais dado.
- **Parâmetros desacoplados:** `ZONE_PROXIMITY_ATR_MULT` e `COOLDOWN_LEVEL_TOL_ATR_MULT` saíram de dentro de `ZONE_ATR_MULT` (que governava três comportamentos ao mesmo tempo), com os mesmos valores efetivos.

## Estudos avulsos (setups de terceiros)

Setups vistos em vídeo são testados em scripts separados, pré-registrados, fora do monitor de produção. Resultados em `claude/estudos-avulsos.md`. Cinco setups foram testados em 20 pares e **nenhum passou**:
- 21/09/2026: o **leque de médias (EMA 20–50)** e o **1-2-3 de Mark Crisp**.
- 22/09/2026: **estocástico + VWAP/MM144**, **9.1 de Larry Williams**, **IFR curto no recuo** e **Renko + VWAP**.

Estudos com grade de parâmetros usam **holdout temporal**: escolhe-se a célula na 1ª metade, entre as com **n ≥ 200** trades no treino, e testa-se só essa célula na 2ª. Desde o estudo 8, a célula também precisa passar nos **80 pares fora da amostra**.

O 9.1 no diário, que parecia positivo, foi checado contra compras aleatórias de mesma duração em 80 pares fora da amostra (`monitor/replay_91_beta.py`). Era sobretudo beta, e fora da amostra nem o retorno absoluto se sustenta.

Não reabra esses testes variando parâmetros sobre os mesmos dados.

### Rodada de 04/10/2026 — estudos 27 a 36 (nenhum passou)

Busca de estratégias **direcionais** fora de padrão gráfico (evento, fluxo, calendário), seguindo o protocolo acima. Detalhe e números em `claude/estudos-avulsos.md`, seções 27–36. Resumo:
- 27 funding extremo + gatilho de preço · 31 capitulação (queda + open interest despencando) · 36 prêmio extremo do perpétuo (horário): **funding, prêmio e open interest não preveem direção** em nenhuma escala testada. O que parece funcionar nos 20 majors some nos 368 pares do DE.
- 28 vender o perpétuo após anúncio de deslistagem: o trade típico ganha (mediana +19%), mas a cauda de short squeeze (ALPACA −2245%) destrói. O mecanismo existe no spot, não no perpétuo.
- 29 comprar após anúncio de listagem: o efeito (+22%) acontece em menos de 2h, antes de qualquer latência horária.
- 30 vender o perpétuo na abertura do spot de listagem nova: **o mais perto de passar** (excesso +13%, IC > 0), mas o absoluto não passou (funding de −4%/semana + squeeze). Inconclusivo. **O Gabriel decidiu não levar ao papel:** teste adiante de 1,5–2 anos para resultado inconclusivo não vale o tempo.
- 32 drift pré-FOMC: centro +0.6%, sem poder estatístico (53 eventos), zero desde 2023.
- 33 lead-lag BTC → alts em 1h: sinal bruto zero mesmo com execução otimista.
- 34 Turtle canônico: **fecha a família tendência** (quatro formas, todas zero). Os +16% nos majors eram beta (só compras, viés de sobrevivência). O Gabriel perguntou sobre operar só comprado e sobre variações; a resposta registrada é que "só compras" escolhido depois de ver o dado é garimpo, e não sobra amostra limpa para testar.
- 35 gap da CME: fecha em 69% (vs. 47% no placebo), mas a expectância é negativa.

### Estudo 37 — Monitoring Tag (05/10/2026, não passou)

Vender o perpétuo depois que a Binance aplica a Monitoring Tag. Os dados (anúncios de 2023 a 2026) eram nunca usados. A linha de base inclui perpétuos deslistados (sem viés de sobrevivência). Resultado: excesso de +1.9%/+2.7% com IC de ±10%. O trade típico ganha (mediana +10%), mas os squeezes (até −233%) destroem a média. O anúncio derruba −9% antes da entrada horária, e o placebo de −30 dias dá o mesmo excesso. **Não testar "com stop" sobre esses dados.** O passeio aleatório em 20 sementes mostrou que, com caudas pesadas e cerca de 20 grupos, o IC bootstrap é otimista (5% de falso PASSA contra ~2,5% nominal). Vale para estudos de evento futuros. Script reaproveitável: `monitor/replay_monitoring_tag.py` (universo completo de perpétuos USDT-M do S3, inclusive deslistados, e `--passeio --semente N`).

### Estudo 38 — latência (05/10/2026, descritivo)

Mede quanto do efeito dos anúncios sobra entrando 1–60 min depois, com candles de 1 minuto. **Listagem:** corrida de robô (de +21%, sobra ~2% com 2 min). **Monitoring Tag:** vendido até 24h após o anúncio, +5.2% [+2.1, +8.1] com 2 min e **+3.4% [+1.8, +5.2] com 60 min**, sem beta. Cumpre a regra de decisão pré-fixada e é alcançável pelo workflow horário, sem infraestrutura nova. O efeito está nas primeiras 24h, e o estudo 37 segurava 7–14 dias. **Deslistagem 4h:** positivo de +5 a +60 min, mas fora da regra (exploratório). Nada disso é prova (mesmos eventos já usados, 24 anúncios, IC otimista). **Em teste de papel desde 05/10/2026:** `monitor/monitoring_paper.py` → `claude/monitoring-paper.md`. A regra está congelada no docstring: vende no minuto da detecção (5–65 min) e recompra 24h após o anúncio, com custo de 0.5% e funding real. Há um braço exploratório de deslistagem com saída em 4h. O script lê o feed pela rota `/cms` do proxy. **Só reavaliar com 24 anúncios fechados** (~2 anos).

### Estudo 39 — réplica na Upbit (05/10/2026, não passou)

A mesma regra do papel (vendido de +60 min a +24h) aplicada à designação de "token de alerta" da Upbit, com eventos independentes (31 anúncios). Excesso sobre o BTC de +2.0% [−0.1, +4.3], líquido de +0.5% [−1.6, +2.8] e placebo em zero. A direção é a mesma do 38, com tamanho menor. Não confirma nem desmente. O papel da Binance segue decidindo, e convém esperar um resultado abaixo dos +3.4%. Não juntar as amostras.

### Estudo 40 — réplica da deslistagem na Upbit (05/10/2026, não passou)

Vendido de +60 min a +4h após o fim de suporte da Upbit, 15 anúncios: líquido −1.8% [−6.3, +1.0], mediana ~0. O efeito (−7%) acontece na primeira hora. Não sustenta o braço exploratório de deslistagem do papel. **A família "anúncios de corretora" está praticamente esgotada.** O que resta é o papel da Monitoring Tag.

### Estudo 41 — "efeito Upbit" (05/10/2026, não passou)

Comprar o perpétuo após a Upbit anunciar uma listagem em KRW (43 anúncios): o movimento é de **+16%**, mas acontece **inteiro no primeiro minuto**. Entrando com 1 minuto, sobra +0.3% [−1.4, +2.2], e sem os 3 maiores trades fica negativo. **Encerra a ideia de um servidor de execução rápida para anúncios**, porque é corrida de milissegundos. Em anúncios, só a Monitoring Tag (24h) dura além do primeiro minuto.

### Estudo 42 — venda de volatilidade (05/10/2026, não passou)

**Perfil do Gabriel definido em 05/10/2026:** meta de 20–50% ao ano, aceita quedas de 50% ou mais, horizonte indiferente, aberto a spot, opções e outros mercados. Daí veio o teste de vender puts no dinheiro de 30 dias (DVOL da Deribit, 2021–2026). O prêmio de variância existe no BTC (+7.9 pts), mas está encolhendo (−3 em 2026). No ETH sumiu. A put no BTC rendeu +11.9%/ano com queda de −43%, com IC cruzando zero e abaixo da meta. **Nem comprar e segurar BTC ou ETH deu 20%/ano na janela 2021–26** (+9.5%/+10.3%, quedas de ~−78%).

### Estudo 43 — comprado com freio (05/10/2026)

Regra TV (comprado se acima da média de 200 dias, com posição = min(1, 40% ÷ vol de 30 dias)), sem otimizar. **Corta a queda máxima para cerca de um terço em 16 de 16 moedas e na cesta.** Cesta de peso igual de 16 moedas: 2021–26 +12.8%/ano com queda de −26% (comprar e segurar: +12.3%, −77%); 2019–26 +22.4% com −27% (comprar e segurar: +56%, −77%). Não é vantagem: o retorno vem do mercado. ETH (+21%) e SOL (+36%) atingiram a meta, mas escolhê-los seria olhar para trás. É o único resultado que se encaixa no perfil de risco do Gabriel.

### Estudo 45 — continuação de 48h nas líquidas (05/10/2026, não passou)

Rompimento de 7 dias com volume ≥ 2× em barras de 4h, segurando 48h, nos 50 pares mais líquidos de DE: +0.27% por trade com IC [−0.44, +1.05]; excesso +0.24% com IC cruzando zero. Nas majors dá +0.93% com IC > 0, o mesmo filme de sempre. **Regra do Gabriel (05/10/2026): só vai para o papel o que passar no critério completo.**

**Leitura acumulada (37 estudos):** nenhuma regra direcional passou. Os fracassos têm três causas recorrentes: efeito rápido demais para latência horária, efeito que é do mercado inteiro (beta) e custo de carregar a posição (funding, squeeze). O que funcionou foi estrutural e sem previsão: cash-and-carry (estudo 20; prêmio secou), base trimestral (24) e desbloqueio de tokens (25, no papel).

**Infra nova (reaproveitável):**
- `monitor/replay_deslistagem.py`: carregadores do `data.binance.vision` (candles de 1h com volume, funding e listagem do S3 de perpétuos e spot, inclusive contratos removidos) e do feed de anúncios da Binance (cache versionado em `monitor/cache_anuncios/`).
- Open interest histórico: `replay_capitulacao.py`.
- Prêmio horário: `replay_premio.py`.
- O cache grande fica em `monitor/cache_vision/` (no `.gitignore`).

**Estado das amostras:** A, B, C, D e E gastas, com D/E muito reusadas (cada estudo novo nelas tem menos poder e mais risco de falso positivo). A amostra limpa da hipótese pós-listagem (estudo 30) também foi gasta.

**Ideias levantadas e ainda não testadas** (para retomar):
- Compressão de volatilidade (NR7/squeeze): descartada por ser rompimento com parâmetros em aberto.
- Turtle com piramidação: só com K=3 no DE; recomendação é não insistir.
- Diferença de funding entre Binance e Bybit (neutro em preço, família que funcionou): **o Gabriel não gostou da ideia**; não reabrir sem ele pedir.

Ao retomar, a pergunta em aberto é se vale continuar buscando regra direcional ou se o projeto deve olhar para os mecanismos estruturais e os testes de papel que já estão rodando.

## Achado em investigação (não é regra ainda)

Em 09/09/2026, um lote de confirmações mecânicas de Setup B (compra) disparou simultaneamente em ETH, SOL, XRP e SUI, coincidindo com queda correlacionada de todo o mercado. SUI e XRP bateram stop nas horas seguintes (ambos -1R). Hipótese a investigar: sinais de Setup B em múltiplos pares de altcoin ao mesmo tempo podem estar refletindo beta de mercado (correlação com BTC/ETH), não confirmações tecnicamente independentes por par. Nenhum critério atual do Setup B filtra por correlação entre pares — candidato a virar um novo dado contextual (no espírito de volume/funding), ainda não decidido se vira filtro de invalidação.

## Como o Gabriel gosta de trabalhar (aplica-se ao Claude Code também)

- Fonte de verdade são os arquivos de documentação estruturada do projeto — não assuma nada que não esteja documentado.
- Padrão de qualidade alto para pesquisa/decisão técnica: testar hipóteses em vez de assumi-las, exigir critérios objetivos de credibilidade em vez de "nome conhecido".
- Ao identificar um problema específico no output, ele nomeia diretamente e espera correção substantiva — revisão superficial não é aceita.
- Atualizações de automação são avaliadas de forma conservadora: construir e testar em paralelo, só migrar depois que a versão anterior estiver validada.
- Separação disciplinada entre o que é automação (mecânico) e o que é julgamento humano — não proponha apagar essa fronteira.
- Para decisões sobre candidato a trade: começar com um resumo objetivo e compacto (entrada/stop/alvo/R:R/status do checklist/ação sugerida) antes de qualquer discussão ou ressalva — ele decide primeiro, discute depois, só se pedir.

## Onde NÃO está o contexto

Este repositório não tem o texto completo do plano de trade original (`plano-trade-price-action.md`), do log de monitoramento manual, nem da análise dos 56 prints de Telegram que calibraram os setups — esses documentos vivem num Projeto separado no claude.ai. Se precisar de detalhe fino de uma regra (ex. texto exato do checklist da seção 4), pergunte ao Gabriel em vez de reconstruir de memória.