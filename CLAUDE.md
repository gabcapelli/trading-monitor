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
- **O script deliberadamente NÃO faz interpretação qualitativa, dimensionamento de risco nem avaliação de estado pessoal** — isso é manual, feito colando atualizações de status numa conversa com o Claude. Essa separação é intencional e importante — não proponha automatizar isso.
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
- **Não existe edge demonstrável no dado atual**, mesmo depois da correção do alvo. Com a regra corrigida: 59 sinais aceitos (R:R≥2) em 33 dias, expectância -0.136R, IC 95% bootstrap [-0.533, +0.296]. Sem filtro (n=414): -0.066R, IC [-0.152, +0.027]. Nenhum valor de `STOP_BUFFER_ATR_MULT` testado torna a expectância positiva. Não proponha recalibrar parâmetro "para melhorar o win rate" — o dado não sustenta.
- **Achado que sobreviveu à correção, decisão do Gabriel:** exigir mais R:R continua piorando a expectância monotonicamente (MIN_RR 1.0 → -0.017R; MIN_RR 4.0 → -0.596R) **mesmo com a regra de alvo já corrigida** — não era só sintoma do bug antigo, é um padrão mais geral do checklist mecânico atual. `MIN_RR=2.0` não foi alterado (é regra do plano de risco, seção 3.3, não parâmetro de calibração), mas o achado ficou mais sólido e vale acompanhar.
- **Stop no breakeven: testado só na simulação, não implementado.** `desfecho_mecanico()` aceita `breakeven_apos_r` (default `None`, nunca usado em produção). O único resultado positivo de toda a auditoria apareceu em breakeven a 0.5R (+0.045R), mas o IC 95% bootstrap ([-0.310, +0.444]) inclui zero e negativo — é ruído com n=59, não sinal. Não implemente essa regra sem mais dado.
- **Parâmetros desacoplados:** `ZONE_PROXIMITY_ATR_MULT` e `COOLDOWN_LEVEL_TOL_ATR_MULT` saíram de dentro de `ZONE_ATR_MULT` (que governava três comportamentos ao mesmo tempo), com os mesmos valores efetivos.

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