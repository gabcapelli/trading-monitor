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