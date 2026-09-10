#!/usr/bin/env python3
"""
Monitoramento automatico multi-par (OKX) -- versao gratuita (GitHub Actions).

Replica a parte MECANICA do checklist da secao 4 de plano-trade-price-action.md:
- Le candles 1h e 4h da OKX (endpoint publico, sem API key).
- Classifica tendencia no 4h (HH/HL = alta, LH/LL = baixa, senao lateral) via pivos fractais.
- Mapeia zonas candidatas de Setup A (rompimento + retest) e Setup B (reversao em zona),
  com as mesmas regras de validade da secao 2 do plano (8 candles sem toque OU 3 toques
  sem confirmacao -> zona expira).
- So dispara notificacao (ntfy.sh, gratuito) quando o STATUS muda (zona nova mapeada,
  confirmacao, invalidacao ou expiracao) -- mesma logica de "silencio quando nao muda"
  da automacao original no Cowork.
- Atualiza claude/log-monitoramento-btc-auto.md (uma linha por execucao) e
  claude/status-simulacao.md (resumo do estado atual), no mesmo formato dos arquivos
  do projeto, para que voce (ou uma sessao do Claude) possa ler o contexto depois.

O QUE ESTE SCRIPT NAO FAZ (limitacao deliberada, leia antes de confiar cegamente):
- Nao gera a "leitura" qualitativa em prosa que o Claude fazia (juizo de contexto,
  forca de candle, etc.) -- so registra fatos objetivos (preco, zona, toques, ATR).
- A deteccao de estrutura (pivos fractais, janela=3) e uma APROXIMACAO geometrica,
  igual a usada no backtest (claude/backtest-setup-ab.md) -- nao substitui o seu
  julgamento discricionario. Trate confirmacoes daqui como candidatas a validar
  manualmente antes de contar como um dos 30 trades da secao 3.4 do plano.

Dependencias: NENHUMA alem da biblioteca padrao do Python (urllib, json, etc.)
-- roda em qualquer runner do GitHub Actions sem "pip install".

--------------------------------------------------------------------------------
CHANGELOG v5 (10/09/2026 -- auditoria de continuacao da v4, feita com o Claude
Code sobre o codigo + os 30 sinais ja no banco + 33 dias de historico da OKX):

CONTEXTO QUE IMPORTA: a v4 foi commitada DEPOIS da ultima execucao do monitor,
entao NUNCA RODOU. Prova: o state.json versionado nao tinha as chaves
"cooldown"/"contadores" (load_state as injetaria), e criado_em_ts/mae_r/mfe_r
estavam NULL em 30/30 trades. Ou seja, cooldown, revalidacao de tendencia e
acompanhamento automatico de desfecho existiam so no papel.

CORRECOES

1. COOLDOWN NAO COBRIA O CASO QUE O MOTIVOU: _set_cooldown era chamado em
   invalidacao, expiracao, tendencia virada e R:R baixo -- mas NAO no ramo
   "confirmado", o unico que limpa a zona num caminho de sucesso. E o dedupe
   por par (v3, item 3) so enxerga status='entrado', enquanto o insert nasce
   'candidato'. Na janela entre a confirmacao e a edicao manual do sinais.md
   nenhum dos dois guards estava ativo. LINK #25/#27 -- o proprio exemplo
   citado no CHANGELOG v4 item 3 -- caia exatamente nesse buraco. Varredura do
   banco: 11 dos 30 sinais reusavam um nivel ja sinalizado (ETH 2489.76 x3,
   XRP 1.3972 x3, DOGE 0.08995 x3, XRP 1.3907, BTC 78299.0, SOL 102.2,
   LINK 11.833, XRP 1.3623). Corrigido: confirmacao tambem arma cooldown.

2. SETUP A NUNCA CHECAVA COOLDOWN: try_map_new_zone retornava o Setup A antes
   de qualquer chamada a level_blocked_by_cooldown, que so aparecia nos dois
   loops do Setup B. Corrigido.

3. CICLO DE VIDA DA ZONA CONTAVA EXECUCOES, NAO CANDLES:
   candles_since_creation += 1 por chamada; created_at gravado e nunca lido; e
   last_1h_ts -- que existe em default_pair_state() desde a v2 -- nunca era
   escrito por caminho nenhum do codigo (era este guard, desenhado e nunca
   ligado). Enquanto o cron roda de hora em hora os numeros coincidem
   (conferido contra ARB e LINK em 10/09/2026, batiam exato), mas o CLAUDE.md
   documenta o schedule do GitHub Actions como historicamente irregular: um
   ciclo perdido fazia a zona viver mais candles do que a regra permite; dois
   ciclos na mesma hora contavam o MESMO candle como dois toques. Agora a
   idade sai de timestamp e o candle repetido e ignorado.

4. EXPIRACAO DIVERGIA DA REGRA DOCUMENTADA: o plano (secao 2) diz "8 candles
   SEM TOQUE ou 3 toques sem confirmacao"; o codigo nunca resetava o contador
   num toque, entao eram 8 candles totais -- uma zona ativa, sendo testada,
   morria por tempo. Corrigido (o plano e a spec). Vida maxima continua
   limitada por ZONE_MAX_TOUCHES.

5. ALVO ERA O PIVO MAIS RECENTE, NAO O MAIS PROXIMO: nearest_target_candidate
   devolvia candidatos[-1] (recencia) embora a intencao documentada seja
   "proxima zona de oferta/demanda relevante". Isso infla o R:R exatamente
   quando o preco vai contra a tese: XRP compra manteve alvo_sugerido 1.4388
   em #20 (entrada 1.4028), #23 (1.3914), #28 (1.3635) e #30 (1.3597) -- o
   preco caiu 3%, o alvo ficou parado e o R:R subiu de 3.36 pra 8.40. #20,
   #23 e #28 deram -1R. A REGRA AUTORITATIVA NAO FOI TROCADA de proposito:
   trocar no meio do gate de 30 quebraria a comparabilidade da amostra. Os
   dois alvos passam a ser gravados lado a lado (alvo_proximo/rr_proximo) pra
   que a troca seja decidida com dado.

6. zona_entrada/confirmacao gravados com ':.1f' em vez de fmt_price() (a v3
   criou fmt_price e nao atualizou insert_candidate_trade): no banco, DOGE
   ficou '0.1-0.1', SUI '0.8-0.8', XRP '1.4-1.4'. A coluna de auditoria da
   zona estava sem informacao em 9 dos 10 pares. Corrigido.

7. UM COOLDOWN POR PAR: pair_state["cooldown"] era um slot unico, entao um
   cooldown de compra apagava o de venda. Virou dict por direcao, com
   migracao que preserva o cooldown em andamento.

8. BACKFILL (monitor/backfill_mecanico.py): como a v4 nunca rodou, os 30
   trades nunca ganhariam criado_em_ts e portanto nunca teriam MAE/MFE. O
   backfill deriva criado_em_ts de criado_em, RECUPERA preco_entrada dos
   trades #3..#16 (a coluna nao existia, mas a definicao dela e "fechamento do
   candle de confirmacao", que agora sabemos qual e), e calcula desfecho
   mecanico + MAE/MFE. 28 dos 30 cobertos; #1/#2 nao tem stop_sugerido. O
   calculo mecanico concordou com 100% dos Resultados (R) que o Gabriel tinha
   preenchido a mao -- validacao independente da derivacao de timestamp.

9. TABELA DE CALIBRACAO (sinais_mecanicos + claude/calibracao.md): `trades`
   continua sendo o diario humano (gate dos 30, editado em sinais.md). A
   tabela nova registra TODA confirmacao mecanica, inclusive as descartadas
   por R:R -- que antes so incrementavam um contador inteiro no state.json e
   sumiam. Os descartes sao os contrafactuais: sem eles nao da pra saber se
   MIN_RR corta perdedores ou vencedores. E o desfecho mecanico e medido para
   todo sinal, nao so os 'entrado', porque medir MAE/MFE so nos que o Gabriel
   marcou enviesa o dado pela propria selecao que se quer isolar.
   resultado_mecanico_r e resultado_r sao colunas SEPARADAS de proposito: a
   primeira mede "o que a sugestao mecanica teria feito", a segunda e o trade
   que o Gabriel de fato tomou, e so ela conta para o gate dos 30.

10. PARAMETROS DESACOPLADOS: ZONE_ATR_MULT governava tres comportamentos
    diferentes (meia-largura da zona; 3 * ZONE_ATR_MULT como raio de
    proximidade do Setup B; e a tolerancia de nivel do cooldown), o que torna
    impossivel recalibrar um sem mexer nos outros. Agora sao
    ZONE_PROXIMITY_ATR_MULT e COOLDOWN_LEVEL_TOL_ATR_MULT, com os MESMOS
    valores efetivos de antes -- nada mudou de comportamento.

11. LOG GANHOU A COLUNA "Zona ativa" (setup/direcao/nivel/toques/candles): sem
    ela era impossivel reconstruir ciclo de vida de zona a partir do log. Em
    10/09/2026 o ARB alternou mapeada->invalidada->mapeada->invalidada em 4h e
    nao havia como saber se era o mesmo nivel. Migracao normaliza as linhas
    antigas por contagem de colunas (tolera os 3 formatos ja existentes).

12. HARNESS DE REPLAY (monitor/replay.py): roda a logica inteira sobre
    historico paginado da OKX e varre parametros. Com ~17 trades nada e
    calibravel; com 437 sinais em 33 dias comeca a ser. Usa as mesmas funcoes
    do monitor, entao nao pode divergir dele.

13. TESTES (monitor/test_v5_fixes.py): a v4 foi entregue com ZERO cobertura --
    os dois testes existentes sao ambos da v1 e cobrem so erro de indice. 12
    testes novos travam os itens 1, 2, 3, 4, 5 e 7 e o desfecho mecanico.

O QUE A AUDITORIA *NAO* MUDOU (e por que)

- classify_trend_4h continua exigindo os 2 ultimos topos E os 2 ultimos fundos
  na mesma direcao ("lateral" em ~60% dos casos). Segue sendo decisao de
  metodologia do Gabriel, como a v4 ja registrava.
- Nenhum parametro foi recalibrado. O replay sobre 437 sinais mostra que NAO
  EXISTE valor de STOP_BUFFER_ATR_MULT, regra de alvo ou MIN_RR que torne a
  expectancia positiva -- e que mesmo com n=416 o IC 95% da expectancia inclui
  zero. Nao ha edge demonstravel para calibrar, nem em favor nem contra.
- A regra de alvo nao foi trocada (item 5) nem o dedupe foi estendido a
  'candidato': o cooldown do item 1 ja cobre a evidencia, e bloquear o par por
  candidato nao revisado travaria o par indefinidamente.
- Nenhuma regra de trade nova foi criada. O achado de que 30-37% dos erros
  chegaram a 1R a favor antes de virar e material para uma regra de stop no
  breakeven, mas isso e metodologia, nao correcao de bug.

Relatorio completo da auditoria: claude/auditoria-v5.md

--------------------------------------------------------------------------------
CHANGELOG v4 (10/09/2026 -- fechamento de gaps encontrados numa sessao de
analise retroativa dos primeiros ~30 sinais com o Claude Code):

1. CONTA_PARA_VALIDACAO NUNCA ERA PREENCHIDO: a coluna existia no banco desde
   a v1 (default 0), mas nenhum caminho do codigo -- nem insert_candidate_
   trade, nem sync_edits_from_sinais_md -- jamais escrevia nela. Na pratica,
   a contagem "oficial" dos 30 trades de validacao nunca existiu de verdade;
   vinha sendo reconstruida de memoria em conversa. Corrigido: novo candidato
   ja nasce com conta_para_validacao=1 (assume-se que conta, por padrao);
   nova coluna editavel "Conta 30?" (sim/nao) em sinais.md, seguindo o mesmo
   padrao de Status/Resultado (SINAIS_COL_CONTA30, lido em
   sync_edits_from_sinais_md). Use "nao" pra excluir um trade que nao deveria
   contar (ex.: duplicata de um lote correlacionado).

2. GUARD DE TENDENCIA SO VALIA NO MAPEAMENTO DA ZONA, NUNCA NA CONFIRMACAO:
   uma zona de Setup B pode levar ate ZONE_MAX_CANDLES_1H candles pra
   confirmar. Se a tendencia 4h virasse nesse meio-tempo, o trade saia
   registrado sem nunca ter sido checado contra a regra que motivou o fix da
   v3 (item 1 abaixo). Corrigido: process_single_pair agora revalida trend
   no momento em que check_zone_confirmation retorna "confirmado" -- se a
   tendencia virou contra a direcao da zona, o resultado vira invalidacao
   (status "invalidado_tendencia_virou_setup_X") em vez de confirmacao.

3. MESMO NIVEL PODIA SER REMAPEADO NO CICLO SEGUINTE, SEM COOLDOWN: quando
   uma zona invalidava ou expirava, nada impedia o mesmo swing 4h de virar
   zona nova de novo no proximo ciclo -- achado real: LINK #25/#27 (mesmo
   nivel de referencia, ~4h de diferenca, dois stops seguidos antes do nivel
   finalmente resolver). Corrigido: toda vez que uma zona e limpa (invalidada,
   expirada, virada por tendencia, ou descartada por R:R baixo), o par entra
   em cooldown para aquele nivel+direcao por ZONE_COOLDOWN_CANDLES_1H candles
   de 1h (level_blocked_by_cooldown, checado dentro de try_map_new_zone).

4. RESULTADO DE TRADE 'ENTRADO' CONTINUAVA 100% MANUAL: o script ja busca as
   candles de 1h de cada par a cada execucao, mas nada comparava isso contra
   stop_sugerido/alvo_sugerido de um trade em andamento -- Resultado (R) so
   era preenchido por voce editando sinais.md (fonte de erro: ambiguidade de
   arredondamento de preco, ja vivida com LINK #25/#27). Corrigido: nova
   funcao track_open_trade_outcomes() roda por par a cada ciclo, ANTES de
   process_single_pair, e compara as candles de 1h fechadas desde a
   confirmacao (novo campo criado_em_ts) contra stop_sugerido/alvo_sugerido
   com precisao total -- se algum foi tocado, preenche resultado_r sozinho
   (convencao conservadora se os dois forem tocados no mesmo candle: considera
   o stop primeiro). De brinde, popula mae_r/mfe_r (excursao maxima contra/a
   favor em R) a cada ciclo, mesmo antes do trade fechar -- essas colunas
   existiam no banco desde a v1 e nunca tinham sido usadas. Como sempre,
   edicao manual em sinais.md tem prioridade (sync_edits_from_sinais_md roda
   antes) -- use isso se voce ajustou stop/alvo por julgamento no grafico, em
   vez de operar exatamente na sugestao mecanica. So funciona para trades
   criados a partir desta versao (precisam de criado_em_ts, que trades
   antigos nao tem).

5. NOTIFICACAO PUSH RESTRITA A SINAL DE VERDADE: antes, qualquer mudanca de
   status (zona mapeada, invalidada, expirada) virava push -- feedback do
   Gabriel foi que isso e ruido, ele so quer saber quando ha um candidato de
   verdade. Zona mapeada/invalidada/expirada continuam sendo gravadas no log
   e no status-simulacao.md (nada muda na auditoria), mas so eventos do tipo
   "sinal" (CONFIRMADO de Setup A/B, ou o aviso de posicao aberta ha muito
   tempo, item 6) chegam ao ntfy.

6. AVISO DE CONFIRMACOES CORRELACIONADAS NO MESMO CICLO: se 2+ pares
   confirmarem o mesmo setup+direcao no mesmo ciclo (o padrao do achado de
   09/09/2026, ETH/SOL/XRP/SUI simultaneos), a notificacao agora destaca isso
   explicitamente em vez de mandar os eventos separados com o mesmo tom de
   confianca de sempre.

7. AVISO DE POSICAO ABERTA HA MUITO TEMPO SEM RESULTADO: novo
   LONG_OPEN_CANDLES_1H -- se um trade 'entrado' ficar aberto (sem
   resultado_r, com criado_em_ts disponivel) alem desse limite, entra um
   aviso na notificacao (uma vez por trade, via flag no state.json, resetado
   quando o trade fecha).

8. VISIBILIDADE AGREGADA DE DESCARTES POR R:R BAIXO: contador cumulativo em
   state.json (nunca resetado), incrementado toda vez que um par cai em
   "descartado_rr_baixo_setup_X", exibido em status-simulacao.md -- antes
   essa informacao so existia espalhada no log linha a linha.

NAO IMPLEMENTADO (decisao pendente, nao e so bug fix): reconsiderar a regra
de classify_trend_4h (exige os 2 ultimos topos E os 2 ultimos fundos ambos
crescentes/decrescentes) -- na pratica isso faz "lateral" ser ~60% dos casos
(18/30 na amostra revisada), e o guard do item 2 so atua fora de "lateral".
Mudar isso e uma decisao de metodologia, nao uma correcao -- fica para o
Gabriel decidir com calma, nao foi alterado aqui.

--------------------------------------------------------------------------------
CHANGELOG v3 (08/09/2026 -- ajustes de fluxo, feedback do Gabriel):

1. FILTRO DE REGIME NO SETUP B (try_map_new_zone): antes, o bloco de Setup B
   mapeava zona de venda em resistencia 4h madura OU zona de compra em suporte
   4h maduro INDEPENDENTE do valor de `trend` -- inclusive contra uma tendencia
   de 4h ativa e clara (ex.: venda em resistencia com trend == "alta"). Isso
   nao respeitava o item do checklist da secao 4 do plano ("nao estou
   escolhendo o Setup B so porque 'chegou numa zona', contra uma tendencia de
   4h clara e ativa") -- a regra existia so no papel, nunca foi codificada.
   Corrigido com um guard de tendencia antes de cada loop: venda em resistencia
   so e candidata se trend != "alta"; compra em suporte so e candidata se
   trend != "baixa". Tendencia "lateral" continua gerando os dois lados sem
   restricao -- e onde o Setup B faz sentido sem essa ressalva. Efeito
   colateral esperado: menos candidatos de Setup B no total, e por consequencia
   mais peso relativo ao Setup A no fluxo (que ja era mais raro de capturar por
   causa da janela estreita do proprio gatilho de rompimento).

2. FILTRO DE R:R MINIMO (process_single_pair, ramo "confirmado"): candidatos
   com R:R sugerido abaixo de 2 (secao 3.3 do plano, R:R minimo 1:2) deixam de
   ser inseridos no banco e deixam de gerar notificacao -- antes, isso so era
   filtrado manualmente, depois do fato, revisando o diario. Agora o calculo
   de sugestao (compute_suggestion) roda ANTES da decisao de inserir, e o
   resultado vira um novo status "descartado_rr_baixo_setup_X" (visivel no
   log/status, sem push, sem linha no diario).

3. DEDUPE POR PAR COM POSICAO ABERTA (process_single_pair, ramo "zona is
   None"): nova funcao pair_has_open_position() checa se ja existe uma linha
   com status='entrado' E resultado_r IS NULL para aquele par especifico. Se
   sim, o script nao tenta mapear nem notificar zona nova para esse par neste
   ciclo (status vira "sem_zona_posicao_aberta") -- evita confundir voce com
   sinais novos de uma moeda que ja tem trade em andamento. Assim que voce
   marcar o resultado no sinais.md (mudanca #5), o par volta a ser vigiado
   normalmente no proximo ciclo.

4. PRECO DE ENTRADA UNICO, COM DECIMAIS DINAMICOS: a notificacao e o
   sinais.md deixam de mostrar a faixa de zona (ex. "6.8-6.9") e passam a
   mostrar um numero unico -- o fechamento do candle 1h que confirmou o setup
   (preco real de onde a confirmacao aconteceu). Nova coluna `preco_entrada`
   no banco (migracao aditiva, mesmo padrao das colunas de sugestao). A
   formatacao de preco tambem deixou de ser fixa (`.1f` / `.6g`, que quebrava
   para pares baratos como DOGE, com 4-5 casas decimais relevantes) -- nova
   funcao fmt_price() escolhe as casas decimais pela ordem de grandeza do
   preco. A zona (`zona_entrada`) continua sendo gravada no banco por
   completude/auditoria, so nao aparece mais na notificacao nem no sinais.md.

5. sinais.md COMO FONTE DE VERDADE (renomeado de candidatos-pendentes.md):
   antes, esse arquivo era so um espelho de LEITURA do banco -- marcar
   'entrado'/'descartado' e preencher resultado exigia abrir o .db (SQL
   Browser ou similar), o que na pratica nao era usavel do celular nem sem
   ferramenta extra. Agora o arquivo tem duas colunas editaveis por voce
   direto no GitHub (mobile ou web): Status e Resultado (R). Antes de
   regenerar o arquivo a cada execucao, o script LE o sinais.md existente
   (sync_edits_from_sinais_md) e aplica qualquer mudanca nessas duas colunas
   de volta ao banco -- so DEPOIS disso o arquivo e reescrito do zero a
   partir do banco ja atualizado, entao suas edicoes nunca sao perdidas na
   reescrita. O banco (.db) continua existindo como motor interno do script
   (contagem de posicoes abertas, dedupe por par, historico), mas voce nunca
   mais precisa abrir ele -- toda interacao manual acontece no .md.
   IMPORTANTE: o layout das colunas do sinais.md (ordem, nomes) e definido
   uma unica vez em SINAIS_COLUMNS, usado tanto para escrever quanto para ler
   o arquivo -- nao mude a ordem das colunas manualmente no arquivo, ou o
   parser de sync_edits_from_sinais_md vai desalinhar os valores. So os
   VALORES de Status e Resultado (R) devem ser editados, nunca a estrutura
   da tabela (cabecalho, ordem ou numero de colunas).

--------------------------------------------------------------------------------
CHANGELOG v2 (07/09/2026 -- generalizacao multi-par):

Decisao de escopo (07/09/2026): expandir de BTC-USDT-SWAP unico para os 10
pares definidos em PAIRS abaixo. Os 30 trades de validacao (secao 3.4 do
plano) continuam contados de forma AGREGADA entre todos os pares (nao
separado por par). Limite de posicoes simultaneas (secao 3.3) revisado para
ATE 2 (era 1), ainda GLOBAL entre os 10 pares (nao por par).

1. LOGICA DE ZONA (try_map_new_zone, check_zone_confirmation, find_confirmed_
   pivots, classify_trend_4h) NAO MUDOU na estrutura geral -- essas funcoes ja
   eram agnosticas ao par (recebem candles como parametro, nunca leem
   INST_ID global). So as funcoes de fetch/estado/log precisaram mudar. (Ver
   CHANGELOG v3, item 1, para a unica mudanca de comportamento adicionada
   depois dentro de try_map_new_zone.)

2. FETCH (okx_get, fetch_candles, fetch_funding_rate): fetch_candles e
   fetch_funding_rate passam a receber `inst_id` como parametro em vez de
   usar o global INST_ID (removido). O loop principal chama essas funcoes
   uma vez por par a cada execucao (10 pares x 3 chamadas = 30 requests/
   execucao -- folgado dentro do rate limit publico da OKX).

3. ESTADO (monitor/state.json): schema mudou de single-object
   ({status, zone, last_1h_ts}) para {"posicoes_abertas": [...],
   "pares": {inst_id: {status, zone, last_1h_ts}}}. MIGRACAO AUTOMATICA e
   TRANSPARENTE do schema antigo na primeira execucao desta versao (ver
   load_state()) -- a zona ja mapeada para BTC (Setup B, ativa no momento
   desta mudanca) e preservada, so realocada para dentro de
   pares["BTC-USDT-SWAP"].

4. LOG (claude/log-monitoramento-btc-auto.md): ganhou a coluna "Par" (logo
   apos a data). Linhas do formato antigo (sem essa coluna) sao migradas
   automaticamente no primeiro run desta versao (ver
   migrate_log_header_if_needed()), preenchendo "BTC-USDT-SWAP" retroativamente
   -- unico par que existia antes desta mudanca. O limite de retencao subiu
   de ~200 para LOG_MAX_LINES linhas, ja que cada execucao agora grava ate 10
   linhas (1 por par) em vez de 1.

5. STATUS (claude/status-simulacao.md): passou de "estado de 1 par" para uma
   tabela resumida dos 10 pares por execucao (write_status reescrita).

6. LIMITE DE POSICOES SIMULTANEAS -- DECISAO DE DESIGN IMPORTANTE: o script
   NAO bloqueia mapeamento nem confirmacao de zona em nenhum par por causa do
   limite de 2 posicoes simultaneas. Isso e deliberado, na mesma linha da
   separacao ja documentada no topo deste arquivo ("automacao so cuida do
   mecanico; risco/execucao ficam manuais"): o script nunca abre uma posicao
   sozinho, so registra candidatos em claude/trade_journal.db com
   status='candidato'. Em vez de travar a deteccao, o script CALCULA quantas
   posicoes estao com status='entrado' e ainda sem resultado_r preenchido
   (count_open_positions()) e expoe esse numero no status e na notificacao de
   confirmacao -- para voce decidir, com essa informacao na mao, se abre ou
   nao mais uma posicao. (Ver CHANGELOG v3, item 3, para o dedupe POR PAR
   especifico, que e diferente deste limite GLOBAL -- os dois convivem.)

7. NOTIFICACAO: passou a ser enviada em UMA UNICA chamada por execucao
   (send_batched_notifications), mesmo se varios pares mudarem de status no
   mesmo ciclo -- evita ate 10 pushes separados no mesmo horario.

8. ROBUSTEZ: o loop principal agora captura erro de fetch por par
   individualmente (um par com falha de API nao derruba a execucao inteira
   nem impede os outros 9 de serem processados neste ciclo).

--------------------------------------------------------------------------------
CHANGELOG v1 (correcoes desta versao, 07/09/2026):

1. BUG CORRIGIDO -- Setup A nunca disparava mesmo com rompimento claro:
   `try_map_new_zone` checava `lows_1h` (fundos) como condicao de entrada para
   detectar rompimento de RESISTENCIA em tendencia de alta -- lista errada.
   Se nao havia um fundo fractal confirmado recente (comum numa alta sustentada,
   onde pullbacks podem nao formar pivo de 3 candles de cada lado), o codigo caia
   direto em `broke = False`, mesmo com o preco ja tendo rompido a resistencia
   (`highs_1h`) ha varias horas. Corrigido para checar `highs_1h` (alta) /
   `lows_1h` (baixa) -- a lista que de fato define o nivel de rompimento.

2. BUG CORRIGIDO -- Setup B so olhava o swing 4h mais recente:
   o `break` do loop de swings maduros estava no mesmo nivel do `if` de
   maturidade (`STALE_4H_CANDLES`), entao o loop sempre parava depois do
   primeiro swing (mesmo que ainda "jovem demais"), nunca chegando a considerar
   o proximo swing mais antigo, que poderia ja estar maduro e perto do preco.
   Corrigido com `continue` explicito para pular swings imaturos.

3. LOG ENRIQUECIDO (sem custo de LLM, so campos objetivos a mais):
   - High/Low do candle 1h mais recente fechado (antes so tinha o close).
   - Ultimo swing 1h confirmado usado como referencia (nivel + ha quantos
     candles foi confirmado), para dar visibilidade ao que o script esta
     vigiando mesmo quando o status e "sem_zona".
   - ATR 1h atual (calculado internamente, mas antes nunca aparecia no log).

4. DIARIO DE TRADE EM SQLITE (claude/trade_journal.db), substituindo a
   transcricao manual dos campos mecanicos na tabela markdown da secao 5 do
   plano:
   - Quando uma zona e CONFIRMADA (resultado "confirmado" em
     check_zone_confirmation), o script insere uma linha com status
     'candidato' e os campos mecanicos ja calculados (setup, direcao, zona,
     nivel de referencia, tendencia 4h). Stop/alvo/R:R/alavancagem FINAIS
     (colunas 'stop', 'alvo', 'rr_planejado') nao sao calculados
     automaticamente -- isso continua exigindo julgamento e fica em branco
     ate voce (ou uma sessao do Claude) decidir e preencher.
   - status muda para 'entrado' ou 'descartado' -- desde a v3, isso e feito
     editando a coluna Status direto em claude/sinais.md (ver CHANGELOG v3,
     item 5), nao mais abrindo o .db. So trades com status='entrado' E
     conta_para_validacao=1 entram na estatistica da secao 3.5.
   - O banco e versionado no mesmo repo (commit a cada execucao que
     insere linha nova ou sincroniza edicao do sinais.md).

NOTA sobre a biblioteca smartmoneyconcepts (avaliada e descartada para a
deteccao de pivo/zona nesta versao): testada contra dado sintetico e
encontrada uma divergencia real (fora de casos de borda) na definicao de
swing high/low em relacao a regra estrita ja usada aqui (maximo/minimo dentro
de uma janela de +-3 candles) -- a lib parece usar um algoritmo sequencial
tipo zigue-zague, nao reavaliacao estrita por janela. Trocar a deteccao de
pivo por essa lib mudaria quais zonas de Setup A/B sao geradas, invalidando
a aplicabilidade do backtest ja rodado (claude/backtest-setup-ab.md) sem
re-rodar tudo. Os dois bugs reais (#1 e #2 acima) nao tinham relacao com a
qualidade da deteccao de pivo em si -- eram erro de indice/lista, corrigido
sem trocar a definicao de zona. Ver tests/test_zone_logic.py para testes que
travam essa classe de bug daqui pra frente.
--------------------------------------------------------------------------------
"""

import json
import os
import sqlite3
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta

# ---------------------------------------------------------------------------
# Configuracao
# ---------------------------------------------------------------------------

OKX_BASE = "https://www.okx.com"

# Pares decididos na expansao de 07/09/2026 (liquidez OKX + precedente nos 56
# prints catalogados + historico de preco longo o suficiente para leitura
# estrutural). BTC-USDT-SWAP e o par original, mantido primeiro na lista.
PAIRS = [
    "BTC-USDT-SWAP",
    "ETH-USDT-SWAP",
    "SOL-USDT-SWAP",
    "XRP-USDT-SWAP",
    "DOGE-USDT-SWAP",
    "ARB-USDT-SWAP",
    "WLD-USDT-SWAP",
    "SUI-USDT-SWAP",
    "UNI-USDT-SWAP",
    "LINK-USDT-SWAP",
]

# Limite de posicoes simultaneas (secao 3.3 do plano, revisado em 07/09/2026
# de 1 para 2) -- GLOBAL entre os 10 pares, nao por par. Ver CHANGELOG v2,
# item 6, e CHANGELOG v3, item 3 (dedupe POR PAR, que e um filtro diferente
# e mais restrito, aplicado antes deste limite global entrar em jogo).
MAX_POSICOES_SIMULTANEAS = 2

# Regras de zona (secao 2 do plano) -- pontos de partida, recalibrar com dados reais.
ZONE_MAX_CANDLES_1H = 8      # zona expira apos 8 candles de 1h SEM TOQUE (v5, item 4)
ZONE_MAX_TOUCHES = 3         # zona expira apos 3 toques sem confirmacao valida
ZONE_ATR_MULT = 0.25         # MEIA-largura da zona em multiplos de ATR 1h
STALE_4H_CANDLES = 10        # swing 4h so vira candidato a Setup B apos N candles "maduro"

# DESACOPLADO na v5 (item 10): estes dois valores eram escritos em funcao de
# ZONE_ATR_MULT (`3 * ZONE_ATR_MULT` no teste de proximidade do Setup B, e
# `ZONE_ATR_MULT` puro na tolerancia do cooldown). Na pratica um unico knob
# governava tres comportamentos diferentes, o que torna impossivel recalibrar
# a largura da zona sem mexer tambem em quais swings viram candidatos e em
# quando um nivel deixa de estar bloqueado. Os valores default abaixo sao
# EXATAMENTE os que estavam em vigor -- nada muda de comportamento agora.
ZONE_PROXIMITY_ATR_MULT = 0.75   # era 3 * ZONE_ATR_MULT
COOLDOWN_LEVEL_TOL_ATR_MULT = 0.25  # era ZONE_ATR_MULT

# R:R minimo do plano (secao 3.3) -- candidatos abaixo disso nao sao mais
# inseridos no diario nem notificados (ver CHANGELOG v3, item 2).
MIN_RR = 2.0

PIVOT_WINDOW = 3             # janela esquerda/direita para pivo fractal confirmado
ATR_PERIOD = 14

BRT = timezone(timedelta(hours=-3))

STATE_PATH = os.path.join("monitor", "state.json")
LOG_PATH = os.path.join("claude", "log-monitoramento-btc-auto.md")
STATUS_PATH = os.path.join("claude", "status-simulacao.md")
TRADE_DB_PATH = os.path.join("claude", "trade_journal.db")

# Renomeado de candidatos-pendentes.md para sinais.md na v3 -- deixou de ser
# so leitura, agora e a fonte de verdade editavel (ver CHANGELOG v3, item 5).
SINAIS_PATH = os.path.join("claude", "sinais.md")

# v5, item 9: espelho SO-LEITURA da tabela de calibracao
# (sinais_mecanicos). Mesma razao de sinais.md existir -- voce nao
# deve precisar abrir o .db. Diferenca: aqui nada e editavel.
CALIBRACAO_PATH = os.path.join("claude", "calibracao.md")

# Retencao do log: cada execucao agora grava ate len(PAIRS) linhas (1 por
# par), contra 1 antes -- subiu proporcionalmente de ~200 para manter uma
# janela de historico comparavel (~2 dias com 10 pares horarios).
LOG_MAX_LINES = 480

# Buffer de stop sobre o extremo da varredura, em multiplos de ATR 1h --
# convencao adotada nesta sessao ao calcular stop/alvo manualmente para os
# candidatos de ETH/XRP; formalizada aqui para o script calcular sozinho.
STOP_BUFFER_ATR_MULT = 0.1

# Cooldown apos uma zona falhar (invalidada, expirada, virada por mudanca de
# tendencia, ou descartada por R:R baixo) -- evita remapear o MESMO nivel
# imediatamente no ciclo seguinte (ver CHANGELOG v4, item 3). Ponto de
# partida, como os outros parametros de zona acima -- recalibrar com dados
# reais.
ZONE_COOLDOWN_CANDLES_1H = 8

# Se um trade 'entrado' ficar aberto (sem resultado_r) por mais que isso,
# entra um aviso na notificacao (CHANGELOG v4, item 7). Ponto de partida.
LONG_OPEN_CANDLES_1H = 48

# Layout das colunas de claude/sinais.md -- usado TANTO para escrever quanto
# para ler o arquivo (sync_edits_from_sinais_md). Nao mude a ordem aqui sem
# atualizar os dois lugares -- ver aviso no CHANGELOG v3, item 5.
SINAIS_COLUMNS = [
    "ID", "Par", "Setup", "Direcao", "Preco entrada", "Stop sugerido",
    "Alvo sugerido", "R:R sugerido", "Tend. 4h", "Status", "Resultado (R)",
    "Conta 30?", "Criado em",
]
SINAIS_COL_ID = 0
SINAIS_COL_STATUS = 9
SINAIS_COL_RESULTADO = 10
SINAIS_COL_CONTA30 = 11

NTFY_TOPIC = os.environ.get("NTFY_TOPIC", "").strip()  # definido via GitHub secret


def pair_label(inst_id):
    """'ETH-USDT-SWAP' -> 'ETH/USDT' -- rotulo curto para log/status/diario."""
    return inst_id.replace("-USDT-SWAP", "/USDT")


def fmt_price(v):
    """
    Formata preco com casas decimais escolhidas pela ordem de grandeza --
    substitui os formatos fixos (.1f / .6g) que quebravam para pares baratos
    como DOGE (0.08995), onde 1-2 casas decimais escondem a informacao
    relevante. Ver CHANGELOG v3, item 4.
    """
    if v is None:
        return "\u2014"
    av = abs(v)
    if av < 1:
        dec = 5
    elif av < 10:
        dec = 4
    elif av < 1000:
        dec = 2
    else:
        dec = 1
    return f"{v:.{dec}f}"


def fmt_ratio(v):
    """Formata R:R (nao e preco, sempre 2 casas -- ex.: 2.35)."""
    return f"{v:.2f}" if v is not None else "\u2014"


# ---------------------------------------------------------------------------
# Fetch OKX (sem dependencias externas -- so urllib)
# ---------------------------------------------------------------------------

def okx_get(path, params):
    query = "&".join(f"{k}={v}" for k, v in params.items())
    url = f"{OKX_BASE}{path}?{query}"
    req = urllib.request.Request(url, headers={"User-Agent": "btc-monitor-script"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        data = json.loads(resp.read().decode("utf-8"))
    if data.get("code") != "0":
        raise RuntimeError(f"OKX API error: {data}")
    return data["data"]


def fetch_candles(inst_id, bar, limit=150):
    """
    Retorna lista de candles mais RECENTE -> MAIS ANTIGO (como a OKX devolve),
    cada um: [ts_ms, open, high, low, close, vol, volCcyQuote, confirm]
    Reordena para MAIS ANTIGO -> MAIS RECENTE (mais facil de processar em sequencia).
    """
    raw = okx_get("/api/v5/market/candles", {"instId": inst_id, "bar": bar, "limit": limit})
    raw = list(reversed(raw))  # antigo -> recente
    candles = []
    for row in raw:
        candles.append({
            "ts": int(row[0]),
            "open": float(row[1]),
            "high": float(row[2]),
            "low": float(row[3]),
            "close": float(row[4]),
            "vol": float(row[5]),
            "volCcyQuote": float(row[7]) if len(row) > 7 else float(row[6]),
            "confirm": row[8] if len(row) > 8 else row[-1],
        })
    return candles


def fetch_funding_rate(inst_id):
    data = okx_get("/api/v5/public/funding-rate", {"instId": inst_id})
    return float(data[0]["fundingRate"])


# ---------------------------------------------------------------------------
# Indicadores / estrutura (mesma logica do backtest, simplificada para uso incremental)
# ---------------------------------------------------------------------------

def true_range(c_prev, c):
    return max(
        c["high"] - c["low"],
        abs(c["high"] - c_prev["close"]),
        abs(c["low"] - c_prev["close"]),
    )


def atr(candles, period=ATR_PERIOD):
    closed = [c for c in candles if c["confirm"] == "1"]
    if len(closed) < period + 1:
        return None
    trs = [true_range(closed[i - 1], closed[i]) for i in range(1, len(closed))]
    return sum(trs[-period:]) / period


def find_confirmed_pivots(candles, window=PIVOT_WINDOW):
    """
    Pivos fractais confirmados: candle i e topo se high[i] > high de 'window' candles
    de cada lado; fundo se low[i] < low de 'window' candles de cada lado.
    So considera candles fechados (confirm == '1'). Retorna listas de (idx, price).
    """
    closed = [c for c in candles if c["confirm"] == "1"]
    highs = []
    lows = []
    n = len(closed)
    for i in range(window, n - window):
        seg_h = [closed[j]["high"] for j in range(i - window, i + window + 1)]
        seg_l = [closed[j]["low"] for j in range(i - window, i + window + 1)]
        if closed[i]["high"] == max(seg_h):
            highs.append((i, closed[i]["high"]))
        if closed[i]["low"] == min(seg_l):
            lows.append((i, closed[i]["low"]))
    return highs, lows, closed


def classify_trend_4h(candles_4h):
    highs, lows, closed = find_confirmed_pivots(candles_4h)
    if len(highs) < 2 or len(lows) < 2:
        return "lateral", closed
    h1, h2 = highs[-2][1], highs[-1][1]
    l1, l2 = lows[-2][1], lows[-1][1]
    if h2 > h1 and l2 > l1:
        return "alta", closed
    if h2 < h1 and l2 < l1:
        return "baixa", closed
    return "lateral", closed


# ---------------------------------------------------------------------------
# Estado persistente (zonas candidatas, status atual)
# ---------------------------------------------------------------------------

def default_pair_state():
    return {
        "status": "sem_zona",
        "zone": None,
        # ts (ms) do ultimo candle 1h ja processado neste par -- guard contra
        # processar o MESMO candle duas vezes se o cron disparar duas vezes na
        # mesma hora (CHANGELOG v5, item 3). O campo existia desde a v2 e nunca
        # era escrito por caminho nenhum do codigo.
        "last_1h_ts": None,
        "cooldowns": {},  # {direcao: {level, until_ts}} -- CHANGELOG v5, item 7
        "avisado_aberto_longo": False,  # ver CHANGELOG v4, item 7
    }


def load_state():
    """
    Schema atual: {"posicoes_abertas": [...], "pares": {inst_id: {status, zone,
    last_1h_ts}}}. Migra automaticamente e sem perda de dado o schema antigo
    (single-pair, sempre BTC): {"status", "zone", "last_1h_ts"} direto na raiz
    -- ver CHANGELOG v2, item 3.
    """
    if not os.path.exists(STATE_PATH):
        return {
            "posicoes_abertas": [],
            "pares": {p: default_pair_state() for p in PAIRS},
            "contadores": {"descartes_rr_baixo_total": 0},
        }

    with open(STATE_PATH, "r", encoding="utf-8") as f:
        raw = json.load(f)

    if "pares" not in raw:
        raw = {
            "posicoes_abertas": [],
            "pares": {
                "BTC-USDT-SWAP": {
                    "status": raw.get("status", "sem_zona"),
                    "zone": raw.get("zone"),
                    "last_1h_ts": raw.get("last_1h_ts"),
                }
            },
        }
        print("[migracao] state.json antigo (single-pair) migrado para o schema multi-par "
              "-- zona em andamento, se houver, foi preservada em pares['BTC-USDT-SWAP'].")

    # garante entrada para todo par da lista atual (cobre par novo adicionado depois)
    for p in PAIRS:
        raw["pares"].setdefault(p, default_pair_state())
        ps = raw["pares"][p]
        # migracao aditiva v4 -- pares ja existentes no state.json antigo nao
        # tem essas chaves ainda (ver CHANGELOG v4, itens 3 e 7).
        ps.setdefault("last_1h_ts", None)
        ps.setdefault("avisado_aberto_longo", False)
        # migracao v5, item 7: o slot unico "cooldown" virou um dict por
        # direcao -- antes, um cooldown de compra apagava o de venda no mesmo
        # par. Preserva o cooldown em andamento, se houver.
        antigo = ps.pop("cooldown", None)
        ps.setdefault("cooldowns", {})
        if isinstance(antigo, dict) and antigo.get("direction"):
            ps["cooldowns"].setdefault(antigo["direction"], {
                "level": antigo.get("level"),
                "until_ts": antigo.get("until_ts", 0),
            })
        # migracao v5, itens 3 e 4: o ciclo de vida da zona passou a ser
        # contado em CANDLES (a partir de timestamps) em vez de execucoes do
        # script. Zonas ja em andamento ganham o campo novo derivado do que
        # existia, sem perder o progresso ja acumulado.
        z = ps.get("zone")
        if z is not None and "last_touch_ts" not in z:
            z["last_touch_ts"] = z.get("created_at")
    raw.setdefault("posicoes_abertas", [])
    raw.setdefault("contadores", {})
    raw["contadores"].setdefault("descartes_rr_baixo_total", 0)
    return raw


def save_state(state):
    os.makedirs(os.path.dirname(STATE_PATH), exist_ok=True)
    with open(STATE_PATH, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)


# ---------------------------------------------------------------------------
# Diario de trade em SQLite (claude/trade_journal.db)
#
# Motor interno do script -- desde a v3, voce nunca mais precisa abrir este
# arquivo diretamente; toda interacao manual acontece em claude/sinais.md
# (ver sync_edits_from_sinais_md / write_sinais, e CHANGELOG v3 item 5).
# Colunas de decisao (checklist_ok, conta_para_validacao, stop/alvo/
# alavancagem finais) continuam em branco ate voce (ou uma sessao do Claude)
# revisar o candidato e preencher -- o script nunca marca um trade como
# 'entrado' sozinho.
# ---------------------------------------------------------------------------

def ensure_trade_db():
    os.makedirs(os.path.dirname(TRADE_DB_PATH), exist_ok=True)
    conn = sqlite3.connect(TRADE_DB_PATH)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS trades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            status TEXT NOT NULL DEFAULT 'candidato'
                CHECK(status IN ('candidato', 'entrado', 'descartado')),
            data TEXT NOT NULL,
            par TEXT NOT NULL DEFAULT 'BTC/USDT Perpetual (Binance)',
            setup TEXT NOT NULL CHECK(setup IN ('A', 'B')),
            direcao TEXT,
            nivel_referencia REAL,
            zona_entrada TEXT,
            confirmacao TEXT,
            tendencia_4h TEXT,
            stop REAL,
            alvo REAL,
            rr_planejado REAL,
            alavancagem REAL,
            checklist_ok INTEGER,
            conta_para_validacao INTEGER NOT NULL DEFAULT 0,
            resultado_r REAL,
            mae_r REAL,
            mfe_r REAL,
            rr_realizado REAL,
            motivo_resultado TEXT,
            observacoes TEXT,
            criado_em TEXT NOT NULL
        )
        """
    )
    conn.commit()

    # Migracao aditiva (07/09/2026 e 08/09/2026): novas colunas de sugestao
    # mecanica automatica de stop/alvo/R:R, e (v3) preco de entrada unico.
    # ALTER TABLE ADD COLUMN e seguro em bancos ja existentes -- so falha
    # (silenciosamente ignorado) se a coluna ja existir, nao apaga nem move
    # nenhum dado.
    for col, coltype in [
        ("extremo_varredura", "REAL"),
        ("stop_sugerido", "REAL"),
        ("alvo_sugerido", "REAL"),
        ("rr_sugerido", "REAL"),
        ("preco_entrada", "REAL"),
        ("criado_em_ts", "INTEGER"),  # ts (ms) do candle 1h de confirmacao -- CHANGELOG v4, item 4
        # v5, item 5: alvo alternativo ("pivo oposto mais PROXIMO", em vez do
        # "mais RECENTE" que a v1 escolheu). Gravado em paralelo, NAO
        # autoritativo -- serve pra medir a diferenca antes de trocar a regra.
        ("alvo_proximo", "REAL"),
        ("rr_proximo", "REAL"),
    ]:
        try:
            conn.execute(f"ALTER TABLE trades ADD COLUMN {col} {coltype}")
        except sqlite3.OperationalError:
            pass  # coluna ja existe -- migracao ja rodou antes
    conn.commit()

    # ------------------------------------------------------------------
    # v5, item 9: TABELA DE CALIBRACAO (sinais_mecanicos).
    #
    # `trades` continua sendo o DIARIO HUMANO: so o que passou no filtro de
    # R:R, com Status/Resultado editados por voce, contando para o gate dos
    # 30. Esta tabela e outra coisa -- o registro MECANICO de TODA confirmacao
    # detectada, inclusive as descartadas por R:R baixo, com o desfecho
    # calculado por geometria de preco e sem nenhuma decisao humana no meio.
    #
    # Por que separado: os descartes sao os contrafactuais. Sem eles nao ha
    # como saber se MIN_RR=2 corta perdedores ou vencedores, e o MAE/MFE
    # medido so nos trades que voce marcou 'entrado' ja nasce enviesado pela
    # sua propria selecao -- que e justamente a variavel que se quer isolar
    # pra calibrar STOP_BUFFER_ATR_MULT / ZONE_ATR_MULT / STALE_4H_CANDLES.
    # ------------------------------------------------------------------
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS sinais_mecanicos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            trade_id INTEGER,            -- id em `trades`, ou NULL se descartado
            par TEXT NOT NULL,
            setup TEXT NOT NULL,
            direcao TEXT NOT NULL,
            tendencia_4h TEXT,
            nivel_referencia REAL,
            zona_low REAL,
            zona_high REAL,
            atr_1h REAL,
            preco_entrada REAL,
            extremo_varredura REAL,
            stop_sugerido REAL,
            alvo_sugerido REAL,          -- pivo oposto mais RECENTE (regra atual)
            rr_sugerido REAL,
            alvo_proximo REAL,           -- pivo oposto mais PROXIMO (regra alternativa)
            rr_proximo REAL,
            aceito INTEGER NOT NULL,     -- 1 = virou linha em `trades`; 0 = descartado por R:R
            motivo_descarte TEXT,
            candles_ate_confirmar INTEGER,
            toques_ate_confirmar INTEGER,
            -- desfecho puramente mecanico, preenchido pelos ciclos seguintes
            resultado_mecanico_r REAL,
            motivo_mecanico TEXT,
            mae_r REAL,
            mfe_r REAL,
            candles_ate_desfecho INTEGER,
            criado_em TEXT NOT NULL,
            criado_em_ts INTEGER NOT NULL,
            UNIQUE(par, direcao, criado_em_ts)
        )
        """
    )
    conn.commit()
    conn.close()


def insert_candidate_trade(inst_id, zone, trend, extremo=None, stop_sug=None,
                            alvo_sug=None, rr_sug=None, preco_entrada=None,
                            confirm_ts=None, alvo_prox=None, rr_prox=None):
    """
    Insere uma linha 'candidato' quando uma zona e CONFIRMADA (rejeicao
    valida no candle 1h) E o R:R sugerido atende ao minimo do plano (ver
    CHANGELOG v3, item 2 -- o caller ja filtra isso antes de chamar esta
    funcao). Os campos mecanicos vem preenchidos; stop/alvo/R:R FINAIS
    (colunas 'stop', 'alvo', 'rr_planejado') continuam em branco ate voce
    decidir -- extremo_varredura/stop_sugerido/alvo_sugerido/rr_sugerido/
    preco_entrada sao a SUGESTAO mecanica automatica, guardada em colunas
    separadas para nunca ser confundida com a decisao real.

    conta_para_validacao ja nasce em 1 (conta por padrao) -- edite a coluna
    "Conta 30?" em sinais.md pra "nao" se este trade nao devesse contar (ex.:
    duplicata de lote correlacionado). Ver CHANGELOG v4, item 1.

    confirm_ts (ts em ms do candle 1h que confirmou a zona) e gravado em
    criado_em_ts -- usado por track_open_trade_outcomes() pra saber a partir
    de qual candle acompanhar o desfecho (CHANGELOG v4, item 4).

    Retorna o id da linha inserida (usado pra ligar a linha correspondente em
    sinais_mecanicos -- CHANGELOG v5, item 9).
    """
    ensure_trade_db()
    now_brt = datetime.now(BRT).strftime("%Y-%m-%d %H:%M")
    conn = sqlite3.connect(TRADE_DB_PATH)
    # CORRIGIDO (v5, item 6): zona_entrada e confirmacao usavam ':.1f' fixo, de
    # antes de fmt_price() existir (v3) -- o que gravava '0.1-0.1' pra DOGE,
    # '0.8-0.8' pra SUI e '1.4-1.4' pra XRP. A coluna de auditoria da zona
    # estava sem informacao nenhuma em 9 dos 10 pares.
    cur = conn.execute(
        """
        INSERT INTO trades
            (status, data, par, setup, direcao, nivel_referencia, zona_entrada,
             confirmacao, tendencia_4h, criado_em, conta_para_validacao,
             extremo_varredura, stop_sugerido, alvo_sugerido, rr_sugerido,
             preco_entrada, criado_em_ts, alvo_proximo, rr_proximo)
        VALUES ('candidato', ?, ?, ?, ?, ?, ?, ?, ?, ?, 1, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            now_brt,
            pair_label(inst_id),
            zone["setup"],
            zone["direction"],
            zone["level"],
            f"{fmt_price(zone['zone_low'])}-{fmt_price(zone['zone_high'])}",
            "Rejeicao confirmada no candle 1h mais recente "
            f"(nivel de referencia {fmt_price(zone['level'])})",
            trend,
            now_brt,
            extremo,
            stop_sug,
            alvo_sug,
            rr_sug,
            preco_entrada,
            confirm_ts,
            alvo_prox,
            rr_prox,
        ),
    )
    trade_id = cur.lastrowid
    conn.commit()
    conn.close()
    return trade_id


def registrar_sinal_mecanico(inst_id, zone, trend, atr_1h, sug, aceito,
                             trade_id=None, motivo_descarte=None,
                             confirm_ts=None):
    """
    Grava TODA confirmacao mecanica em sinais_mecanicos -- aceita ou descartada
    por R:R baixo (CHANGELOG v5, item 9). Esta e a tabela de calibracao; ela
    existe justamente pra que os descartes, que antes so incrementavam um
    contador inteiro no state.json e sumiam, virem dado analisavel.

    `sug` e a tupla de compute_suggestion(). Idempotente por (par, direcao,
    criado_em_ts): se o mesmo candle for processado de novo, o INSERT OR IGNORE
    nao duplica a linha.
    """
    extremo, stop_sug, alvo_sug, rr_sug, preco_entrada, alvo_prox, rr_prox = sug
    ensure_trade_db()
    conn = sqlite3.connect(TRADE_DB_PATH)
    try:
        conn.execute(
            """
            INSERT OR IGNORE INTO sinais_mecanicos
                (trade_id, par, setup, direcao, tendencia_4h, nivel_referencia,
                 zona_low, zona_high, atr_1h, preco_entrada, extremo_varredura,
                 stop_sugerido, alvo_sugerido, rr_sugerido, alvo_proximo,
                 rr_proximo, aceito, motivo_descarte, candles_ate_confirmar,
                 toques_ate_confirmar, criado_em, criado_em_ts)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (
                trade_id, pair_label(inst_id), zone["setup"], zone["direction"],
                trend, zone["level"], zone["zone_low"], zone["zone_high"],
                atr_1h, preco_entrada, extremo, stop_sug, alvo_sug, rr_sug,
                alvo_prox, rr_prox, 1 if aceito else 0, motivo_descarte,
                zone.get("candles_since_creation"), zone.get("touches"),
                datetime.now(BRT).strftime("%Y-%m-%d %H:%M"), confirm_ts,
            ),
        )
        conn.commit()
    finally:
        conn.close()


def count_open_positions():
    """
    Numero de trades com status='entrado' e ainda sem resultado_r preenchido
    -- proxy de "posicao aberta agora" a partir do proprio diario (nao exige
    campo extra no state.json). Limite GLOBAL (secao 3.3, ate 2) -- usado so
    para informar, nunca para bloquear a deteccao de zona. Ver
    pair_has_open_position() para o dedupe POR PAR (CHANGELOG v3, item 3),
    que e um filtro diferente e mais restrito.
    """
    if not os.path.exists(TRADE_DB_PATH):
        return 0
    conn = sqlite3.connect(TRADE_DB_PATH)
    try:
        cur = conn.execute(
            "SELECT COUNT(*) FROM trades WHERE status='entrado' AND resultado_r IS NULL"
        )
        return cur.fetchone()[0]
    finally:
        conn.close()


def open_positions_detail():
    """Lista os pares (rotulo) com posicao 'entrado' e ainda sem resultado registrado."""
    if not os.path.exists(TRADE_DB_PATH):
        return []
    conn = sqlite3.connect(TRADE_DB_PATH)
    try:
        cur = conn.execute(
            "SELECT par FROM trades WHERE status='entrado' AND resultado_r IS NULL"
        )
        return [row[0] for row in cur.fetchall()]
    finally:
        conn.close()


def pair_has_open_position(par_label_value):
    """
    True se ESTE par especifico ja tem uma linha 'entrado' sem resultado
    registrado. Usado para suprimir mapeamento/notificacao de zona nova
    nesse par enquanto o trade atual nao fechar -- ver CHANGELOG v3, item 3.
    Diferente de count_open_positions()/MAX_POSICOES_SIMULTANEAS, que e o
    limite GLOBAL entre os 10 pares (secao 3.3) -- os dois convivem: este
    dedupe roda primeiro, por par; o limite global continua so informativo.
    """
    if not os.path.exists(TRADE_DB_PATH):
        return False
    conn = sqlite3.connect(TRADE_DB_PATH)
    try:
        cur = conn.execute(
            "SELECT COUNT(*) FROM trades WHERE status='entrado' AND resultado_r IS NULL AND par=?",
            (par_label_value,),
        )
        return cur.fetchone()[0] > 0
    finally:
        conn.close()


def desfecho_mecanico(direcao, preco_entrada, stop_sug, alvo_sug, rr_sug,
                      criado_ts, closed_1h):
    """
    Geometria pura de preco: percorre as candles de 1h FECHADAS depois de
    criado_ts e devolve (resultado_r, motivo, mae_r, mfe_r, candles_ate_
    desfecho). Nenhum julgamento qualitativo -- mesma limitacao deliberada do
    topo do arquivo.

    resultado_r vem None enquanto nem stop nem alvo foram tocados (trade ainda
    em aberto); mae/mfe (excursao maxima contra / a favor, em multiplos de R)
    sao devolvidos de qualquer jeito, e e justamente isso que permite calibrar
    STOP_BUFFER_ATR_MULT e a regra de alvo sem esperar o trade fechar.

    Se stop e alvo foram tocados no MESMO candle nao ha dado intra-candle pra
    saber a ordem real -- convencao conservadora, considera o stop primeiro.

    Extraida de track_open_trade_outcomes na v5 pra ser compartilhada com
    track_mechanical_outcomes e com o backfill (monitor/backfill_mecanico.py),
    em vez de existirem tres copias da mesma aritmetica.
    """
    if criado_ts is None or stop_sug is None or preco_entrada is None:
        return None, None, None, None, None

    posteriores = [c for c in closed_1h if c["ts"] > criado_ts]
    if not posteriores:
        return None, None, None, None, None

    risco = abs(preco_entrada - stop_sug)
    mae = 0.0
    mfe = 0.0

    for n, c in enumerate(posteriores, start=1):
        if direcao == "compra":
            excursao_contra = preco_entrada - c["low"]
            excursao_favor = c["high"] - preco_entrada
            stop_tocado = c["low"] <= stop_sug
            alvo_tocado = alvo_sug is not None and c["high"] >= alvo_sug
        else:
            excursao_contra = c["high"] - preco_entrada
            excursao_favor = preco_entrada - c["low"]
            stop_tocado = c["high"] >= stop_sug
            alvo_tocado = alvo_sug is not None and c["low"] <= alvo_sug

        if risco:
            mae = max(mae, excursao_contra / risco)
            mfe = max(mfe, excursao_favor / risco)

        if stop_tocado:
            return -1.0, "stop_automatico", round(mae, 3), round(mfe, 3), n
        if alvo_tocado:
            return rr_sug, "alvo_automatico", round(mae, 3), round(mfe, 3), n

    return None, None, round(mae, 3), round(mfe, 3), None


def track_open_trade_outcomes(par_lbl, candles_1h):
    """
    Preenche o Resultado (R) do DIARIO HUMANO: para trades 'entrado' deste par
    ainda sem resultado_r, compara as candles fechadas desde a confirmacao
    contra stop_sugerido/alvo_sugerido (ver desfecho_mecanico) -- CHANGELOG
    v4, item 4.

    Edicao manual sempre tem prioridade: sync_edits_from_sinais_md roda antes
    desta funcao a cada execucao, e a query abaixo so pega resultado_r IS NULL.

    v5, item 8: mae_r/mfe_r continuam sendo espelhados aqui por conveniencia de
    leitura, mas a fonte de calibracao passou a ser sinais_mecanicos, que cobre
    TODO sinal confirmado -- inclusive os descartados por R:R e os que voce
    nunca marcou 'entrado'. Medir MAE/MFE so nos 'entrado' enviesa o dado pela
    sua propria selecao, que e a variavel que se quer isolar.
    """
    if not os.path.exists(TRADE_DB_PATH):
        return
    conn = sqlite3.connect(TRADE_DB_PATH)
    try:
        cur = conn.execute(
            "SELECT id, direcao, preco_entrada, stop_sugerido, alvo_sugerido, "
            "rr_sugerido, criado_em_ts FROM trades "
            "WHERE status='entrado' AND resultado_r IS NULL AND par=?",
            (par_lbl,),
        )
        rows = cur.fetchall()
        if not rows:
            return

        closed = [c for c in candles_1h if c["confirm"] == "1"]

        for (tid, direcao, preco_entrada, stop_sug, alvo_sug, rr_sug, criado_ts) in rows:
            resultado, motivo, mae, mfe, _ = desfecho_mecanico(
                direcao, preco_entrada, stop_sug, alvo_sug, rr_sug, criado_ts, closed
            )
            if mae is None:
                continue  # trade antigo sem criado_em_ts, ou sem candle novo ainda
            conn.execute(
                "UPDATE trades SET mae_r=?, mfe_r=? WHERE id=?", (mae, mfe, tid)
            )
            if resultado is not None:
                conn.execute(
                    "UPDATE trades SET resultado_r=?, motivo_resultado=? WHERE id=?",
                    (resultado, motivo, tid),
                )
        conn.commit()
    finally:
        conn.close()


def track_mechanical_outcomes(par_lbl, candles_1h):
    """
    Preenche o desfecho da TABELA DE CALIBRACAO (sinais_mecanicos) -- todo
    sinal confirmado deste par que ainda nao resolveu, aceito ou descartado
    por R:R, independente de voce ter marcado qualquer coisa em sinais.md.
    CHANGELOG v5, item 9.

    mae_r/mfe_r sao reescritos a cada ciclo enquanto o sinal esta em aberto
    (a excursao maxima so cresce); resultado_mecanico_r e escrito uma vez, no
    ciclo em que stop ou alvo e tocado, e nunca mais mexido.

    Para sinais DESCARTADOS por R:R baixo nao ha rr_sugerido utilizavel como
    payoff, entao o desfecho e medido contra o alvo mesmo assim e o R do
    acerto e o proprio rr_sugerido calculado na epoca -- e exatamente a
    pergunta que interessa: "o que o filtro de MIN_RR jogou fora?".
    """
    if not os.path.exists(TRADE_DB_PATH):
        return
    conn = sqlite3.connect(TRADE_DB_PATH)
    try:
        cur = conn.execute(
            "SELECT id, direcao, preco_entrada, stop_sugerido, alvo_sugerido, "
            "rr_sugerido, criado_em_ts FROM sinais_mecanicos "
            "WHERE resultado_mecanico_r IS NULL AND par=?",
            (par_lbl,),
        )
        rows = cur.fetchall()
        if not rows:
            return

        closed = [c for c in candles_1h if c["confirm"] == "1"]

        for (sid, direcao, preco_entrada, stop_sug, alvo_sug, rr_sug, criado_ts) in rows:
            resultado, motivo, mae, mfe, ncandles = desfecho_mecanico(
                direcao, preco_entrada, stop_sug, alvo_sug, rr_sug, criado_ts, closed
            )
            if mae is None:
                continue
            conn.execute(
                "UPDATE sinais_mecanicos SET mae_r=?, mfe_r=? WHERE id=?",
                (mae, mfe, sid),
            )
            if resultado is not None:
                conn.execute(
                    "UPDATE sinais_mecanicos SET resultado_mecanico_r=?, "
                    "motivo_mecanico=?, candles_ate_desfecho=? WHERE id=?",
                    (resultado, motivo, ncandles, sid),
                )
        conn.commit()
    finally:
        conn.close()


def check_long_open_alert(par_lbl, pair_state, now_ts):
    """
    Se este par tem um trade 'entrado' sem resultado, aberto ha mais de
    LONG_OPEN_CANDLES_1H candles de 1h (a partir de criado_em_ts), devolve um
    evento de aviso -- uma unica vez por trade (pair_state["avisado_aberto_
    longo"] evita repetir o aviso todo ciclo; reseta sozinho quando o trade
    fecha ou nenhum trade antigo aberto e mais encontrado). Ver CHANGELOG v4,
    item 7. So considera trades com criado_em_ts preenchido (pos-v4).
    """
    if not os.path.exists(TRADE_DB_PATH) or now_ts is None:
        return None
    conn = sqlite3.connect(TRADE_DB_PATH)
    try:
        cur = conn.execute(
            "SELECT id, criado_em FROM trades WHERE status='entrado' "
            "AND resultado_r IS NULL AND par=? AND criado_em_ts IS NOT NULL "
            "AND ? - criado_em_ts >= ?",
            (par_lbl, now_ts, LONG_OPEN_CANDLES_1H * 3600_000),
        )
        antigos = cur.fetchall()
    finally:
        conn.close()

    if not antigos:
        pair_state["avisado_aberto_longo"] = False
        return None
    if pair_state.get("avisado_aberto_longo"):
        return None

    pair_state["avisado_aberto_longo"] = True
    ids_txt = ", ".join(f"#{tid} ({criado})" for tid, criado in antigos)
    return {
        "tipo": "sinal",
        "titulo": f"{par_lbl} -- posicao aberta ha mais de {LONG_OPEN_CANDLES_1H} candles sem resultado",
        "mensagem": f"Trade(s) {ids_txt} -- confira se ainda faz sentido continuar aberto.",
    }


def sync_edits_from_sinais_md():
    """
    Le claude/sinais.md (se existir) e aplica ao banco qualquer mudanca
    manual nas colunas Status, Resultado (R) e Conta 30? -- essas sao as
    unicas tres colunas que voce deve editar no arquivo (a terceira desde
    CHANGELOG v4, item 1). Roda SEMPRE no inicio de main(), ANTES de
    qualquer insercao nova ou reescrita do arquivo, para suas edicoes nunca
    serem perdidas. Ver CHANGELOG v3, item 5.

    Parsing deliberadamente simples e defensivo: ignora silenciosamente
    qualquer linha que nao comece com um ID numerico (cabecalho, separador
    markdown, linha em branco, linha corrompida) em vez de falhar a execucao
    inteira por causa de uma edicao malformada.
    """
    if not os.path.exists(SINAIS_PATH):
        return

    with open(SINAIS_PATH, "r", encoding="utf-8") as f:
        linhas = f.readlines()

    conn = sqlite3.connect(TRADE_DB_PATH)
    atualizados = 0
    for linha in linhas:
        if not linha.strip().startswith("|"):
            continue
        cols = [c.strip() for c in linha.strip().strip("|").split("|")]
        if len(cols) <= max(SINAIS_COL_ID, SINAIS_COL_STATUS, SINAIS_COL_RESULTADO,
                             SINAIS_COL_CONTA30):
            continue
        id_txt = cols[SINAIS_COL_ID]
        if not id_txt.isdigit():
            continue  # cabecalho, separador (---), ou linha inesperada

        id_ = int(id_txt)
        status_txt = cols[SINAIS_COL_STATUS]
        resultado_txt = cols[SINAIS_COL_RESULTADO]
        conta30_txt = cols[SINAIS_COL_CONTA30].strip().lower()

        if status_txt not in ("candidato", "entrado", "descartado"):
            print(f"[aviso] sinais.md linha ID {id_}: status '{status_txt}' invalido "
                  f"(esperado candidato/entrado/descartado) -- ignorando esta linha.")
            continue

        if resultado_txt in ("\u2014", "-", ""):
            resultado_val = None
        else:
            try:
                resultado_val = float(resultado_txt.replace(",", "."))
            except ValueError:
                print(f"[aviso] sinais.md linha ID {id_}: resultado '{resultado_txt}' "
                      f"nao e um numero valido -- ignorando este campo (status ainda e aplicado).")
                resultado_val = "__skip__"

        if conta30_txt in ("sim", "1", "s"):
            conta30_val = 1
        elif conta30_txt in ("nao", "n\u00e3o", "0", "n"):
            conta30_val = 0
        else:
            print(f"[aviso] sinais.md linha ID {id_}: 'Conta 30?' = '{conta30_txt}' "
                  f"invalido (esperado sim/nao) -- mantendo valor atual no banco.")
            conta30_val = "__skip__"

        if resultado_val == "__skip__":
            conn.execute("UPDATE trades SET status=? WHERE id=?", (status_txt, id_))
        else:
            conn.execute(
                "UPDATE trades SET status=?, resultado_r=? WHERE id=?",
                (status_txt, resultado_val, id_),
            )
        if conta30_val != "__skip__":
            conn.execute(
                "UPDATE trades SET conta_para_validacao=? WHERE id=?",
                (conta30_val, id_),
            )
        atualizados += 1

    conn.commit()
    conn.close()
    if atualizados:
        print(f"[sync] {atualizados} linha(s) de sinais.md sincronizada(s) para o banco.")


# ---------------------------------------------------------------------------
# Logica de checklist mecanico (Setup A / Setup B), secao 2 e 4 do plano
# ---------------------------------------------------------------------------

def last_closed(candles):
    closed = [c for c in candles if c["confirm"] == "1"]
    return closed[-1] if closed else None


def _nova_zona(setup, direction, level, atr_1h, now_ts):
    """
    Constroi o dict de zona. Existe pra que os tres pontos que criam zona
    (Setup A, Setup B venda, Setup B compra) nao possam divergir em campos --
    foi assim que `last_touch_ts` (v5, itens 3 e 4) entrou em um lugar so.

    `candles_since_creation` continua no dict, mas agora e um valor DERIVADO,
    recalculado a cada ciclo a partir de last_touch_ts -- fica aqui so pra
    leitura humana no state.json e no status-simulacao.md.
    """
    return {
        "setup": setup,
        "direction": direction,
        "level": level,
        "zone_low": level - ZONE_ATR_MULT * atr_1h,
        "zone_high": level + ZONE_ATR_MULT * atr_1h,
        "candles_since_creation": 0,
        "touches": 0,
        "created_at": now_ts,
        "last_touch_ts": now_ts,
    }


def level_blocked_by_cooldown(cooldowns, direction, level, atr_1h, now_ts):
    """
    True se este nivel+direcao ja gerou um sinal (ou uma falha) recentemente
    neste par e ainda esta em cooldown -- mesma tolerancia de distancia usada
    pra mapear a zona (ZONE_ATR_MULT * ATR).

    v5, item 7: `cooldowns` e um dict {direcao: {level, until_ts}}. Antes era
    um slot unico por par, entao um cooldown de compra apagava o de venda.
    Aceita tambem o formato antigo (dict com chave "direction") pra nao quebrar
    um state.json que ainda nao passou pela migracao de load_state().
    """
    if not cooldowns or atr_1h is None:
        return False
    if "direction" in cooldowns:  # formato antigo, slot unico
        cd = cooldowns if cooldowns.get("direction") == direction else None
    else:
        cd = cooldowns.get(direction)
    if not cd:
        return False
    if now_ts >= cd.get("until_ts", 0):
        return False
    return abs(level - (cd.get("level") or 0)) <= COOLDOWN_LEVEL_TOL_ATR_MULT * atr_1h


def try_map_new_zone(trend, candles_1h, candles_4h, atr_1h, cooldowns=None):
    """
    Tenta mapear uma nova zona candidata (Setup A se ha tendencia 4h definida,
    Setup B se preco esta perto de um swing 4h "maduro" E alinhado com a
    tendencia -- ver CHANGELOG v3, item 1). Retorna dict da zona ou None se
    nada relevante for encontrado agora.

    `cooldowns` (opcional): niveis+direcoes que acabaram de gerar sinal ou
    falhar neste par e ainda nao podem ser remapeados -- ver CHANGELOG v4,
    item 3, e v5, itens 1, 2 e 7.
    """
    highs_1h, lows_1h, closed_1h = find_confirmed_pivots(candles_1h)
    last = closed_1h[-1]

    if trend in ("alta", "baixa") and atr_1h:
        # Setup A: procura o ultimo swing 1h confirmado NA DIRECAO DO ROMPIMENTO
        # (resistencia para alta, suporte para baixa) e verifica se o preco ja
        # rompeu esse nivel (condicao para comecar a vigiar um retest).
        # CORRIGIDO (v1): antes checava a lista errada (lows_1h para tendencia
        # de alta), o que fazia o rompimento nunca ser detectado quando nao
        # havia um fundo fractal confirmado recente -- mesmo com o preco ja
        # tendo rompido a resistencia (highs_1h) ha varias horas.
        ref_swing = None
        broke = False
        if trend == "alta" and highs_1h:
            ref_swing = highs_1h[-1][1]
            broke = last["close"] > ref_swing
        elif trend == "baixa" and lows_1h:
            ref_swing = lows_1h[-1][1]
            broke = last["close"] < ref_swing

        direcao_a = "compra" if trend == "alta" else "venda"
        # CORRIGIDO (v5, item 2): o Setup A retornava aqui ANTES de qualquer
        # checagem de cooldown -- level_blocked_by_cooldown so era chamado
        # dentro dos dois loops do Setup B. Ou seja, o fix da v4 item 3 nunca
        # valeu pra este ramo, e ele e vivo (LINK ficou com zona_mapeada_
        # setup_A no ciclo seguinte a um descarte, em 10/09/2026).
        if (ref_swing is not None and broke
                and not level_blocked_by_cooldown(
                    cooldowns, direcao_a, ref_swing, atr_1h, last["ts"])):
            return _nova_zona("A", direcao_a, ref_swing, atr_1h, last["ts"])

    # Setup B: swing 4h maduro (>= STALE_4H_CANDLES desde a confirmacao) como zona.
    # CORRIGIDO (v1, 1a rodada): o `break` estava fora do `if` de maturidade,
    # entao o loop sempre parava no primeiro swing (mesmo imaturo).
    # CORRIGIDO (v1, 2a rodada -- pego pelo teste automatizado, nao por
    # inspecao manual): mesmo depois do primeiro fix, um `break` sobrava apos
    # o `if` de distancia -- entao o loop ainda desistia no primeiro swing
    # MADURO que encontrasse, mesmo se ele estivesse longe do preco, sem
    # chegar a um swing mais antigo que pudesse estar maduro E perto. Ambos
    # os `break` foram removidos: agora o loop percorre todos os swings
    # maduros (do mais recente ao mais antigo) ate achar um dentro da
    # distancia, ou esgotar a lista.
    #
    # FILTRO DE REGIME (v3, CHANGELOG item 1): antes, os dois loops abaixo
    # rodavam sempre, independente de `trend` -- gerando, por exemplo, venda
    # em resistencia mesmo com trend == "alta" (contra uma tendencia de 4h
    # ativa e clara), o que contrariava o item do checklist da secao 4 que
    # pede exatamente para NAO fazer isso. Agora cada loop so roda se nao
    # estiver brigando com uma tendencia ativa na direcao oposta -- "lateral"
    # continua liberando os dois lados sem restricao.
    highs_4h, lows_4h, closed_4h = find_confirmed_pivots(candles_4h)

    if trend != "alta":  # venda em resistencia: nao gerar contra tendencia de alta ativa
        for idx, price in reversed(highs_4h):
            if len(closed_4h) - 1 - idx < STALE_4H_CANDLES:
                continue  # ainda recente demais -- tenta o proximo swing mais antigo
            if level_blocked_by_cooldown(cooldowns, "venda", price, atr_1h, last["ts"]):
                continue  # nivel falhou recentemente -- CHANGELOG v4, item 3
            if atr_1h and abs(last["close"] - price) <= ZONE_PROXIMITY_ATR_MULT * atr_1h:
                return _nova_zona("B", "venda", price, atr_1h, last["ts"])
            # maduro mas longe -- nao retorna nem para; tenta o proximo mais antigo

    if trend != "baixa":  # compra em suporte: nao gerar contra tendencia de baixa ativa
        for idx, price in reversed(lows_4h):
            if len(closed_4h) - 1 - idx < STALE_4H_CANDLES:
                continue
            if level_blocked_by_cooldown(cooldowns, "compra", price, atr_1h, last["ts"]):
                continue  # nivel falhou recentemente -- CHANGELOG v4, item 3
            if atr_1h and abs(last["close"] - price) <= ZONE_PROXIMITY_ATR_MULT * atr_1h:
                return _nova_zona("B", "compra", price, atr_1h, last["ts"])

    return None


def check_zone_confirmation(zone, candles_1h):
    """
    Verifica se o candle 1h mais recente fechado confirma a zona (rejeicao clara
    ou higher-low/lower-high), invalida (fechamento contra, alem do stop implicito)
    ou apenas "toca" sem confirmar (conta como 1 toque).
    Retorna: "confirmado" | "invalidado" | "tocou" | "sem_toque"
    """
    closed = [c for c in candles_1h if c["confirm"] == "1"]
    last = closed[-1]
    touched = zone["zone_low"] <= last["low"] <= zone["zone_high"] or \
              zone["zone_low"] <= last["high"] <= zone["zone_high"] or \
              (last["low"] <= zone["zone_low"] and last["high"] >= zone["zone_high"])

    if not touched:
        return "sem_toque"

    body = abs(last["close"] - last["open"])
    rang = max(last["high"] - last["low"], 1e-9)

    if zone["direction"] == "compra":
        rejection = (last["close"] - last["low"]) / rang >= 0.6 and last["close"] > last["open"]
        invalidated = last["close"] < zone["zone_low"]
    else:
        rejection = (last["high"] - last["close"]) / rang >= 0.6 and last["close"] < last["open"]
        invalidated = last["close"] > zone["zone_high"]

    if invalidated:
        return "invalidado"
    if rejection:
        return "confirmado"
    return "tocou"


def sweep_extreme(zone, last_candle):
    """Ponto mais distante tocado antes da rejeicao -- referencia de stop (secao 2 do plano)."""
    return last_candle["high"] if zone["direction"] == "venda" else last_candle["low"]


def suggest_stop(extremo, atr_1h, direction):
    """Stop sugerido = extremo da varredura + pequena folga (0.1x ATR 1h)."""
    if atr_1h is None:
        return None
    buffer = STOP_BUFFER_ATR_MULT * atr_1h
    return extremo + buffer if direction == "venda" else extremo - buffer


def nearest_target_candidate(direction, candles_1h, price_ref, modo="recente"):
    """
    Alvo CANDIDATO (nao autoritativo): um pivo 1h confirmado do lado oposto,
    ainda nao rompido pelo preco atual. Aproximacao mecanica simples -- a
    "proxima zona de oferta/demanda relevante" (secao 2) continua exigindo
    julgamento no grafico.

    modo="recente" (default, comportamento historico): o pivo oposto MAIS
    RECENTE por indice. modo="proximo": o pivo oposto mais PROXIMO do preco.

    Por que os dois existem (v5, item 5): o codigo sempre usou "mais recente"
    embora a intencao documentada seja "proxima zona relevante". A diferenca
    nao e cosmetica -- ela infla o R:R justamente quando o preco esta indo
    contra a tese. Caso real no diario: XRP compra manteve alvo_sugerido =
    1.4388 em #20 (entrada 1.4028), #23 (1.3914), #28 (1.3635) e #30 (1.3597);
    o preco caiu 3%, o alvo nao se moveu e o R:R subiu de 3.36 para 8.40
    enquanto a tese piorava. #20, #23 e #28 deram -1R cada.

    A regra autoritativa NAO foi trocada de proposito: trocar no meio do gate
    de 30 trades quebraria a comparabilidade da amostra ja coletada. Os dois
    valores passam a ser gravados lado a lado (colunas alvo_proximo/rr_proximo
    em `trades` e em `sinais_mecanicos`) pra que a troca possa ser decidida
    com dado, e nao com opiniao.
    """
    highs_1h, lows_1h, _ = find_confirmed_pivots(candles_1h)
    if direction == "venda":
        candidatos = [p for _, p in lows_1h if p < price_ref]
    else:
        candidatos = [p for _, p in highs_1h if p > price_ref]
    if not candidatos:
        return None
    if modo == "proximo":
        # o mais proximo do preco: o maior fundo abaixo (venda), o menor topo
        # acima (compra)
        return max(candidatos) if direction == "venda" else min(candidatos)
    return candidatos[-1]


def _rr(preco_entrada, stop_sug, alvo):
    if stop_sug is None or alvo is None:
        return None
    risco = abs(stop_sug - preco_entrada)
    return (abs(preco_entrada - alvo) / risco) if risco else None


def compute_suggestion(zone, candles_1h, atr_1h):
    """
    Retorna (extremo, stop_sugerido, alvo_sugerido, rr_sugerido, preco_entrada,
    alvo_proximo, rr_proximo) para uma zona recem-confirmada. `preco_entrada` e
    o fechamento do candle 1h de confirmacao (v3, CHANGELOG item 4).

    alvo_sugerido/rr_sugerido continuam sendo os AUTORITATIVOS (regra "pivo
    oposto mais recente"); alvo_proximo/rr_proximo sao a regra alternativa
    gravada em paralelo pra calibracao -- ver nearest_target_candidate.

    Qualquer valor pode vir None se faltar dado (ATR ainda nao calculavel, ou
    nenhum pivo oposto na janela).
    """
    last = last_closed(candles_1h)
    preco_entrada = last["close"]
    extremo = sweep_extreme(zone, last)
    stop_sug = suggest_stop(extremo, atr_1h, zone["direction"])
    alvo_sug = nearest_target_candidate(zone["direction"], candles_1h, preco_entrada)
    alvo_prox = nearest_target_candidate(
        zone["direction"], candles_1h, preco_entrada, modo="proximo"
    )
    return (extremo, stop_sug, alvo_sug, _rr(preco_entrada, stop_sug, alvo_sug),
            preco_entrada, alvo_prox, _rr(preco_entrada, stop_sug, alvo_prox))


# ---------------------------------------------------------------------------
# Logica por par (extraida do antigo main() single-pair para ser reutilizada
# em loop, uma vez por par -- ver CHANGELOG v2)
# ---------------------------------------------------------------------------

def process_single_pair(inst_id, pair_state, candles_1h, candles_4h, trend, atr_1h):
    """
    Roda a logica mecanica (mapear zona nova, ou checar confirmacao/invalidacao/
    expiracao de uma zona existente) para UM par, a partir do estado anterior
    desse par. Muta e retorna pair_state; retorna tambem um dict de evento
    (titulo + mensagem) se o status mudou neste ciclo, ou None se nao mudou
    (== sem notificacao para este par).
    """
    zone = pair_state.get("zone")
    prev_status = pair_state.get("status")
    new_status = prev_status
    evento = None
    par_lbl = pair_label(inst_id)
    last_candle = last_closed(candles_1h)
    last_ts = last_candle["ts"] if last_candle else None

    # GUARD DE CANDLE JA PROCESSADO (v5, item 3): toda a logica de ciclo de
    # vida da zona (toques, expiracao, confirmacao) le exatamente UM candle --
    # o ultimo fechado. Se o cron disparar duas vezes dentro da mesma hora, o
    # mesmo candle era contado como um segundo toque e como mais um candle de
    # idade da zona. O campo last_1h_ts existia em default_pair_state() desde
    # a v2 e nunca era escrito por caminho nenhum do codigo -- era exatamente
    # este guard, desenhado e nunca ligado.
    if last_ts is not None and pair_state.get("last_1h_ts") == last_ts:
        return pair_state, None
    if last_ts is not None:
        pair_state["last_1h_ts"] = last_ts

    def _set_cooldown(zona):
        # CHANGELOG v4, item 3 (+ v5, itens 1 e 7): nivel que acabou de gerar
        # sinal OU de falhar nao pode ser remapeado imediatamente. Um slot por
        # DIRECAO -- antes era um slot unico por par, entao um cooldown de
        # compra apagava o de venda.
        if last_ts is not None:
            pair_state.setdefault("cooldowns", {})[zona["direction"]] = {
                "level": zona["level"],
                "until_ts": last_ts + ZONE_COOLDOWN_CANDLES_1H * 3600_000,
            }

    if zone is None:
        # DEDUPE POR PAR (v3, CHANGELOG item 3): nao mapear zona nova para um
        # par que ja tem trade 'entrado' em andamento -- evita sinal novo
        # confuso enquanto uma posicao real ainda esta aberta nesse par.
        if pair_has_open_position(par_lbl):
            new_status = "sem_zona_posicao_aberta"
        else:
            candidate = try_map_new_zone(
                trend, candles_1h, candles_4h, atr_1h, pair_state.get("cooldowns")
            )
            if candidate:
                pair_state["zone"] = candidate
                new_status = f"zona_mapeada_setup_{candidate['setup']}"
                evento = {
                    "tipo": "info",
                    "titulo": f"{par_lbl} -- Nova zona candidata -- Setup {candidate['setup']}",
                    "mensagem": (
                        f"Direcao: {candidate['direction']}\n"
                        f"Nivel: {fmt_price(candidate['level'])}\n"
                        f"Tendencia 4h: {trend}\n"
                        f"Cole este alerta + o log no Claude para leitura qualitativa."
                    ),
                }
            else:
                new_status = "sem_zona"
    else:
        result = check_zone_confirmation(zone, candles_1h)

        # REVALIDACAO DE TENDENCIA NA CONFIRMACAO (CHANGELOG v4, item 2): o
        # guard de tendencia do Setup B (v3, item 1) so era checado no
        # mapeamento da zona. Se a tendencia 4h virou contra a direcao da
        # zona enquanto ela esperava confirmar, trata como invalidacao em vez
        # de aceitar o trade.
        contra_tendencia_agora = (
            zone["setup"] == "B"
            and (
                (zone["direction"] == "venda" and trend == "alta")
                or (zone["direction"] == "compra" and trend == "baixa")
            )
        )

        if result == "confirmado" and contra_tendencia_agora:
            new_status = f"invalidado_tendencia_virou_setup_{zone['setup']}"
            evento = {
                "tipo": "info",
                "titulo": f"{par_lbl} -- Setup {zone['setup']} invalidado (tendencia virou)",
                "mensagem": (
                    f"Zona confirmaria, mas a tendencia 4h agora e '{trend}', contra a "
                    f"direcao da zona ({zone['direction']}) -- descartado sem entrar no "
                    f"diario. Ver CHANGELOG v4, item 2."
                ),
            }
            _set_cooldown(zone)
            pair_state["zone"] = None
        elif result == "confirmado":
            sug = compute_suggestion(zone, candles_1h, atr_1h)
            extremo, stop_sug, alvo_sug, rr_sug, preco_entrada, alvo_prox, rr_prox = sug

            # FILTRO DE R:R MINIMO (v3, CHANGELOG item 2): so vira candidato
            # de verdade (insercao no diario + notificacao) se o R:R sugerido
            # atender ao minimo do plano (secao 3.3). Abaixo disso, descarta
            # sem ruido -- fica visivel no log/status, sem push.
            if rr_sug is None or rr_sug < MIN_RR:
                new_status = f"descartado_rr_baixo_setup_{zone['setup']}"
                # v5, item 9: o descarte deixa de ser so um contador inteiro
                # no state.json -- vira linha na tabela de calibracao, com o
                # desfecho acompanhado nos ciclos seguintes. Sem isso nao ha
                # como saber se MIN_RR corta perdedores ou vencedores.
                registrar_sinal_mecanico(
                    inst_id, zone, trend, atr_1h, sug, aceito=False,
                    motivo_descarte=("rr_indisponivel" if rr_sug is None
                                     else f"rr_{rr_sug:.2f}_abaixo_de_{MIN_RR:.1f}"),
                    confirm_ts=last_ts,
                )
                _set_cooldown(zone)
                pair_state["zone"] = None
            else:
                new_status = f"CONFIRMADO_setup_{zone['setup']}"
                trade_id = insert_candidate_trade(
                    inst_id, zone, trend, extremo, stop_sug, alvo_sug, rr_sug,
                    preco_entrada, confirm_ts=last_ts,
                    alvo_prox=alvo_prox, rr_prox=rr_prox,
                )
                registrar_sinal_mecanico(
                    inst_id, zone, trend, atr_1h, sug, aceito=True,
                    trade_id=trade_id, confirm_ts=last_ts,
                )
                abertas = count_open_positions()

                evento = {
                    "tipo": "sinal",
                    "setup": zone["setup"],
                    "direcao": zone["direction"],
                    "par": par_lbl,
                    "titulo": f"{par_lbl} -- CONFIRMACAO -- Setup {zone['setup']} ({zone['direction']})",
                    "mensagem": (
                        f"Preco de entrada: {fmt_price(preco_entrada)}\n"
                        f"Stop sugerido: {fmt_price(stop_sug)} | "
                        f"Alvo candidato: {fmt_price(alvo_sug)} | "
                        f"R:R sugerido: {fmt_ratio(rr_sug)} \u2705\n"
                        f"(Sugestao mecanica simples -- extremo da varredura + buffer de ATR; "
                        f"pivo 1h oposto mais recente. Valide no grafico, nao substitui a secao 4.)\n"
                        f"Posicoes abertas no diario agora: {abertas}/{MAX_POSICOES_SIMULTANEAS}\n"
                        f"Candidato salvo em claude/sinais.md -- edite Status/Resultado (R) direto la."
                    ),
                }
                # CORRIGIDO (v5, item 1): este ramo era o UNICO que limpava a
                # zona sem armar cooldown -- _set_cooldown so era chamado em
                # invalidacao, expiracao, tendencia virada e R:R baixo. Como o
                # dedupe por par (v3, item 3) so enxerga status='entrado' e o
                # insert nasce como 'candidato', na janela entre a confirmacao
                # e a sua edicao no sinais.md NENHUM dos dois guards estava
                # ativo -- e o mesmo nivel voltava a virar sinal.
                # Evidencia no diario: LINK #25/#27 (nivel 11.833, ambos -1R,
                # o proprio caso citado no CHANGELOG v4 item 3), XRP #28/#30
                # (1.3623), SOL #19/#26 (102.2), XRP #8/#20 (1.3907).
                # No total, 11 dos 30 sinais reusavam um nivel ja sinalizado.
                _set_cooldown(zone)
                pair_state["zone"] = None
        elif result == "invalidado":
            new_status = f"invalidado_setup_{zone['setup']}"
            evento = {
                "tipo": "info",
                "titulo": f"{par_lbl} -- Setup {zone['setup']} invalidado",
                "mensagem": (
                    f"Fechamento contra a zona "
                    f"{fmt_price(zone['zone_low'])}-{fmt_price(zone['zone_high'])}."
                ),
            }
            _set_cooldown(zone)
            pair_state["zone"] = None
        else:
            # CICLO DE VIDA CONTADO EM CANDLES, NAO EM EXECUCOES (v5, item 3):
            # antes era `candles_since_creation += 1` por chamada da funcao, e
            # `created_at` era gravado mas nunca lido. Enquanto o cron roda
            # certinho de hora em hora os dois numeros coincidem (conferi
            # contra ARB e LINK em 10/09/2026 e batiam exato), mas o CLAUDE.md
            # documenta o schedule do GitHub Actions como historicamente
            # irregular -- um ciclo perdido fazia a zona viver mais candles do
            # que a regra permite. Agora sai de timestamp.
            #
            # RESET NO TOQUE (v5, item 4): a regra da secao 2 do plano e "8
            # candles SEM TOQUE ou 3 toques sem confirmacao". O codigo nunca
            # resetava o contador num toque, entao na pratica eram 8 candles
            # totais -- uma zona ativa, sendo testada, expirava por tempo.
            # A vida maxima continua limitada por ZONE_MAX_TOUCHES.
            if result == "tocou":
                zone["touches"] += 1
                zone["last_touch_ts"] = last_ts
            ref_ts = zone.get("last_touch_ts") or zone.get("created_at")
            candles_sem_toque = (
                int((last_ts - ref_ts) // 3600_000) if (last_ts and ref_ts) else 0
            )
            zone["candles_since_creation"] = candles_sem_toque  # derivado, so pra leitura
            if zone["touches"] >= ZONE_MAX_TOUCHES or candles_sem_toque >= ZONE_MAX_CANDLES_1H:
                motivo = ("limite de toques" if zone["touches"] >= ZONE_MAX_TOUCHES
                          else f"{candles_sem_toque} candles de 1h sem toque")
                new_status = f"zona_expirada_setup_{zone['setup']}"
                evento = {
                    "tipo": "info",
                    "titulo": f"{par_lbl} -- Zona do Setup {zone['setup']} expirou",
                    "mensagem": f"Expirou por {motivo} -- releitura de contexto necessaria.",
                }
                _set_cooldown(zone)
                pair_state["zone"] = None
            else:
                new_status = prev_status  # sem mudanca -> sem notificacao

    pair_state["status"] = new_status
    return pair_state, (evento if new_status != prev_status else None)


# ---------------------------------------------------------------------------
# Notificacao gratuita via ntfy.sh (sem custo, sem API key -- so um "topic" secreto)
# ---------------------------------------------------------------------------

def send_ntfy(title, message, priority="default"):
    if not NTFY_TOPIC:
        print("[aviso] NTFY_TOPIC nao configurado -- pulando notificacao push.")
        return
    url = f"https://ntfy.sh/{NTFY_TOPIC}"
    req = urllib.request.Request(
        url,
        data=message.encode("utf-8"),
        headers={"Title": title.encode("utf-8"), "Priority": priority},
        method="POST",
    )
    try:
        urllib.request.urlopen(req, timeout=10)
    except urllib.error.URLError as e:
        print(f"[erro] Falha ao enviar notificacao ntfy: {e}")


def send_batched_notifications(eventos):
    """
    Envia UMA chamada ao ntfy por execucao, mesmo com varios pares mudando de
    status no mesmo ciclo -- evita ate len(PAIRS) pushes separados na mesma hora.
    """
    if not eventos:
        return
    if len(eventos) == 1:
        send_ntfy(eventos[0]["titulo"], eventos[0]["mensagem"], priority="high")
        return
    titulo = f"{len(eventos)} mudancas de status neste ciclo"
    corpo = "\n\n".join(f"### {ev['titulo']}\n{ev['mensagem']}" for ev in eventos)
    send_ntfy(titulo, corpo, priority="high")


# ---------------------------------------------------------------------------
# Escrita dos arquivos de log / status (mesmo formato do projeto)
# ---------------------------------------------------------------------------

def fmt_brt(ts_ms):
    return datetime.fromtimestamp(ts_ms / 1000, tz=BRT).strftime("%Y-%m-%d %H:%M")


def last_swing_ref_text(trend, candles_1h):
    """
    Texto curto descrevendo o ultimo swing 1h confirmado relevante para a
    tendencia atual (resistencia em alta, suporte em baixa) -- so para dar
    visibilidade no log ao que o script esta vigiando, mesmo em sem_zona.
    """
    highs_1h, lows_1h, closed_1h = find_confirmed_pivots(candles_1h)
    n = len(closed_1h)
    if trend == "alta" and highs_1h:
        idx, price = highs_1h[-1]
        return f"res {fmt_price(price)} (ha {n - 1 - idx} candles)"
    if trend == "baixa" and lows_1h:
        idx, price = lows_1h[-1]
        return f"sup {fmt_price(price)} (ha {n - 1 - idx} candles)"
    return "\u2014"


LOG_HEADER = (
    "# Log de Monitoramento Automatico -- Multi-Par (script gratuito, GitHub Actions)\n\n"
    "> Gerado por script Python sem LLM (ver monitor/fetch_and_check.py). Fonte: OKX. "
    "Cobre os pares em PAIRS (configuracao no topo do script) -- BTC-USDT-SWAP e os demais "
    "adicionados na expansao de 07/09/2026. Leitura e MECANICA (regras objetivas da secao 4 "
    "do plano), sem a prosa qualitativa que o Claude gerava -- cole este log numa conversa "
    "do Claude se quiser a leitura interpretativa.\n\n"
    "| Data/Hora (BRT) | Par | Close 1h | High/Low 1h | Close 4h | Swing 1h ref | ATR 1h | Funding | Zona ativa | Status checklist |\n"
    "|---|---|---|---|---|---|---|---|---|---|\n"
)

# v5, item 11: a coluna "Zona ativa" (setup/direcao/nivel) nao existia -- o log
# so guardava a string de status. Isso tornava impossivel reconstruir o ciclo
# de vida de uma zona a partir do log: em 10/09/2026 o ARB alternou
# mapeada -> invalidada -> mapeada -> invalidada em 4 horas e nao ha como saber
# se era o mesmo nivel. Justamente o dado necessario pra medir quanto o
# cooldown esta barrando.
LOG_COLS_V5 = 10


def migrate_log_header_if_needed():
    """
    Se o log existir no formato antigo (sem a coluna 'Par', de antes da
    expansao multi-par de 07/09/2026), reescreve o header e insere
    'BTC-USDT-SWAP' como Par em cada linha de dado ja existente -- unico par
    que existia antes desta versao. Preserva o historico em vez de descarta-lo.
    Idempotente: nao faz nada se o log ja estiver no formato novo.
    """
    if not os.path.exists(LOG_PATH):
        return
    with open(LOG_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # A checagem e por NUMERO DE COLUNAS de cada linha, nao pelo cabecalho:
    # o log pode conter linhas de formatos diferentes ao mesmo tempo (v1 sem
    # 'Par', v2 sem 'Zona ativa', v5 completo) se uma execucao gravar antes da
    # migracao rodar. Cada linha e normalizada individualmente para
    # LOG_COLS_V5 colunas, e a funcao continua idempotente.
    data_lines = [l for l in lines if l.startswith("| 2")]
    migrated = []
    n_mig = 0
    for l in data_lines:
        parts = l.rstrip("\n").split("|")
        cells = parts[1:-1] if len(parts) >= 3 else None
        if not cells:
            migrated.append(l)  # linha inesperada -- preserva em vez de corromper
            continue
        antes = len(cells)
        if len(cells) == LOG_COLS_V5 - 2:
            # formato v1: sem a coluna 'Par' (so existia BTC na epoca)
            cells.insert(1, " BTC-USDT-SWAP ")
        if len(cells) == LOG_COLS_V5 - 1:
            # formato v2/v4: sem 'Zona ativa'. Entra em branco antes do Status
            # (ultima coluna) -- esse dado nao existe retroativamente.
            cells.insert(len(cells) - 1, " — ")
        if len(cells) != antes:
            n_mig += 1
        migrated.append("|" + "|".join(cells) + "|\n")

    ja_ok = (n_mig == 0 and lines and any(
        l.startswith("| Data/Hora (BRT) | Par | Close 1h") and "Zona ativa" in l
        for l in lines))
    if ja_ok:
        return

    with open(LOG_PATH, "w", encoding="utf-8") as f:
        f.write(LOG_HEADER)
        f.writelines(migrated)
    print(f"[migracao] log reescrito no formato v5 ({n_mig} linha(s) precisaram "
          f"de coluna nova, {len(migrated)} preservadas no total).")


def zona_log_text(zone):
    """Identificacao compacta da zona ativa para o log -- v5, item 11."""
    if not zone:
        return "\u2014"
    return (f"{zone['setup']}/{zone['direction']}@{fmt_price(zone['level'])} "
            f"({zone.get('touches', 0)}t/{zone.get('candles_since_creation', 0)}c)")


def append_log_line(inst_id, candles_1h, candles_4h, funding, status_text, trend,
                    atr_1h, zone=None):
    last_1h = last_closed(candles_1h)
    last_4h = last_closed(candles_4h)
    now_brt = datetime.now(BRT).strftime("%Y-%m-%d %H:%M")
    swing_ref = last_swing_ref_text(trend, candles_1h)
    atr_txt = fmt_price(atr_1h) if atr_1h else "\u2014"

    if not os.path.exists(LOG_PATH):
        os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)
        with open(LOG_PATH, "w", encoding="utf-8") as f:
            f.write(LOG_HEADER)

    line = (
        f"| {now_brt} | {inst_id} | {fmt_price(last_1h['close'])} | "
        f"{fmt_price(last_1h['high'])}/{fmt_price(last_1h['low'])} | "
        f"{fmt_price(last_4h['close'])} | {swing_ref} | {atr_txt} | "
        f"{funding*100:.4f}% | {zona_log_text(zone)} | {status_text} |\n"
    )
    with open(LOG_PATH, "a", encoding="utf-8") as f:
        f.write(line)


def archive_log_if_needed(max_lines=LOG_MAX_LINES):
    """
    Arquivamento simples: mantem so as ultimas `max_lines` linhas de dados.
    Chamada UMA VEZ por execucao (nao por par) -- ver CHANGELOG v2, evita
    reler/reescrever o arquivo len(PAIRS) vezes no mesmo ciclo.
    """
    if not os.path.exists(LOG_PATH):
        return
    with open(LOG_PATH, "r", encoding="utf-8") as f:
        lines = f.readlines()
    data_lines = [l for l in lines if l.startswith("| 2")]
    if len(data_lines) > max_lines:
        head = [l for l in lines if not l.startswith("| 2")]
        with open(LOG_PATH, "w", encoding="utf-8") as f:
            f.writelines(head)
            f.writelines(data_lines[-max_lines:])


def write_sinais():
    """
    Regenera claude/sinais.md a partir do banco -- SEMPRE chamada DEPOIS de
    sync_edits_from_sinais_md() (main() garante essa ordem), entao qualquer
    edicao manual de Status/Resultado (R) ja foi aplicada ao banco antes
    desta reescrita, e portanto nao se perde. Ver CHANGELOG v3, item 5.

    Mostra TODAS as linhas da tabela (nao so status='candidato' como antes)
    -- desde o filtro de R:R minimo (item 2), tudo que e inserido ja passou
    no criterio do plano, entao faz sentido acompanhar o ciclo de vida
    inteiro (candidato -> entrado -> resultado) no mesmo arquivo, sem
    precisar ir atras dele em outro lugar.
    """
    if not os.path.exists(TRADE_DB_PATH):
        rows = []
    else:
        conn = sqlite3.connect(TRADE_DB_PATH)
        try:
            cur = conn.execute(
                "SELECT id, par, setup, direcao, preco_entrada, stop_sugerido, "
                "alvo_sugerido, rr_sugerido, tendencia_4h, status, resultado_r, "
                "conta_para_validacao, criado_em "
                "FROM trades ORDER BY id DESC"
            )
            rows = cur.fetchall()
        finally:
            conn.close()

    now_brt = datetime.now(BRT).strftime("%Y-%m-%d %H:%M")

    if not rows:
        body = "Nenhum sinal registrado ainda.\n"
    else:
        header = "| " + " | ".join(SINAIS_COLUMNS) + " |\n"
        header += "|" + "---|" * len(SINAIS_COLUMNS) + "\n"
        linhas = []
        for (id_, par, setup, direcao, preco_entrada, stop_s, alvo_s, rr_s,
             tend, status, resultado, conta30, criado) in rows:
            resultado_txt = f"{resultado:.2f}" if resultado is not None else "\u2014"
            conta30_txt = "sim" if conta30 else "nao"
            linhas.append(
                f"| {id_} | {par} | {setup} | {direcao} | {fmt_price(preco_entrada)} | "
                f"{fmt_price(stop_s)} | {fmt_price(alvo_s)} | {fmt_ratio(rr_s)} | {tend} | "
                f"{status} | {resultado_txt} | {conta30_txt} | {criado} |"
            )
        body = header + "\n".join(linhas) + "\n"

    content = (
        f"# Sinais -- atualizado {now_brt} BRT\n\n"
        f"> Gerado a partir de `claude/trade_journal.db` a cada execucao. "
        f"**Edite as colunas Status (candidato/entrado/descartado), Resultado (R) e "
        f"Conta 30? (sim/nao) direto neste arquivo** -- a proxima execucao le suas "
        f"mudancas e aplica ao banco antes de reescrever o arquivo, entao suas "
        f"edicoes nunca se perdem. NAO edite a ordem ou os nomes das colunas, so os "
        f"valores dessas tres. Resultado (R) de um trade 'entrado' pode ser "
        f"preenchido automaticamente pelo script quando o stop ou o alvo sugerido "
        f"forem tocados numa candle de 1h -- edite manualmente so se voce operou com "
        f"stop/alvo diferentes dos sugeridos (sua edicao sempre tem prioridade). "
        f"Conta 30? nasce 'sim' -- mude para 'nao' se este trade nao deve contar para "
        f"o gate de validacao (ex.: duplicata de um lote correlacionado). "
        f"Preco de entrada / Stop / Alvo / R:R aqui sao SUGESTOES MECANICAS SIMPLES "
        f"(preco de entrada = fechamento do candle 1h de confirmacao; stop = extremo "
        f"da varredura + buffer de ATR; alvo = pivo 1h oposto mais recente) -- "
        f"validar no grafico antes de usar, nao substituem o checklist da secao 4 do "
        f"plano. So aparecem aqui sinais que ja passaram no filtro de R:R minimo "
        f"({MIN_RR:.0f}) do plano.\n\n"
        + body
    )
    os.makedirs(os.path.dirname(SINAIS_PATH), exist_ok=True)
    with open(SINAIS_PATH, "w", encoding="utf-8") as f:
        f.write(content)


def write_calibracao():
    """
    Espelho em markdown da tabela sinais_mecanicos (v5, item 9) -- mesma razao
    de sinais.md existir: voce nao deve precisar abrir o .db pra ver o dado.

    Este arquivo e SO LEITURA (ao contrario de sinais.md): nada aqui e editavel,
    porque nada aqui e decisao sua -- e o registro mecanico, sem julgamento
    humano no meio, que serve pra calibrar parametro.
    """
    if not os.path.exists(TRADE_DB_PATH):
        return
    conn = sqlite3.connect(TRADE_DB_PATH)
    try:
        linhas = list(conn.execute(
            "SELECT par, setup, direcao, aceito, rr_sugerido, rr_proximo, "
            "resultado_mecanico_r, mae_r, mfe_r, candles_ate_desfecho, criado_em "
            "FROM sinais_mecanicos ORDER BY criado_em_ts DESC"
        ))
    finally:
        conn.close()

    def _bloco(rotulo, rs):
        resolvidos = [r for r in rs if r[6] is not None]
        if not resolvidos:
            return f"| {rotulo} | {len(rs)} | — | — | — |\n"
        wins = [r for r in resolvidos if r[6] > 0]
        soma = sum(r[6] for r in resolvidos)
        return (f"| {rotulo} | {len(rs)} | {len(resolvidos)} | "
                f"{len(wins)} ({100*len(wins)/len(resolvidos):.0f}%) | "
                f"{soma:+.2f}R ({soma/len(resolvidos):+.3f}R/sinal) |\n")

    aceitos = [r for r in linhas if r[3] == 1]
    descartados = [r for r in linhas if r[3] == 0]

    corpo = (
        "| Grupo | Sinais | Resolvidos | Acertos | Soma (expectancia) |\n"
        "|---|---|---|---|---|\n"
        + _bloco(f"Aceitos (R:R >= {MIN_RR:.0f})", aceitos)
        + _bloco("Descartados por R:R baixo", descartados)
        + _bloco("TODOS", linhas)
    )

    # distribuicoes que respondem as perguntas de calibracao
    venc = [r for r in linhas if r[6] is not None and r[6] > 0 and r[7] is not None]
    perd = [r for r in linhas if r[6] is not None and r[6] < 0 and r[8] is not None]
    extra = ""
    if venc:
        maes = sorted(r[7] for r in venc)
        acima = sum(1 for x in maes if x > 0.8)
        extra += (
            f"\n**MAE dos acertos** (quanto o preco foi CONTRA antes de dar certo) "
            f"— n={len(maes)}, mediana {maes[len(maes)//2]:.2f}R, "
            f"maximo {maes[-1]:.2f}R, {100*acima/len(maes):.0f}% acima de 0.8R.\n\n"
            f"> Le-se assim: apertar `STOP_BUFFER_ATR_MULT` mata os acertos cujo "
            f"MAE ja esta perto de 1R. Se essa cauda for gorda, nao ha folga pra "
            f"apertar o stop.\n"
        )
    if perd:
        mfes = sorted(r[8] for r in perd)
        um_r = sum(1 for x in mfes if x >= 1.0)
        extra += (
            f"\n**MFE dos erros** (quanto o preco foi A FAVOR antes de bater stop) "
            f"— n={len(mfes)}, mediana {mfes[len(mfes)//2]:.2f}R, "
            f"{100*um_r/len(mfes):.0f}% chegaram a 1R a favor.\n\n"
            f"> Le-se assim: se muitos erros chegaram perto de 1R antes de virar, "
            f"o problema esta no ALVO/saida, nao na entrada. Se a mediana for "
            f"baixa, o problema esta na entrada e mexer no alvo nao resolve.\n"
        )

    ultimas = linhas[:25]
    tabela = (
        "\n## Ultimos 25 sinais mecanicos\n\n"
        "| Par | Setup | Direcao | Aceito | R:R (recente) | R:R (proximo) | "
        "Resultado | MAE | MFE | Candles | Quando |\n"
        "|---|---|---|---|---|---|---|---|---|---|---|\n"
    )
    for (par, setup, dir_, aceito, rr, rrp, res, mae, mfe, nc, quando) in ultimas:
        tabela += (
            f"| {par} | {setup} | {dir_} | {'sim' if aceito else 'nao'} | "
            f"{fmt_ratio(rr)} | {fmt_ratio(rrp)} | "
            f"{f'{res:+.2f}' if res is not None else 'aberto'} | "
            f"{mae if mae is not None else '—'} | {mfe if mfe is not None else '—'} | "
            f"{nc if nc is not None else '—'} | {quando} |\n"
        )

    content = (
        f"# Calibracao — registro mecanico de sinais "
        f"(atualizado {datetime.now(BRT).strftime('%Y-%m-%d %H:%M')} BRT)\n\n"
        f"> **Nao edite este arquivo** — ele e reescrito a cada execucao a partir "
        f"da tabela `sinais_mecanicos`. Diferente de `sinais.md`, aqui nao ha "
        f"nenhuma decisao sua: e TODA confirmacao mecanica detectada, inclusive "
        f"as descartadas por R:R baixo, com desfecho medido por geometria de "
        f"preco (OHLC de 1h contra stop/alvo sugeridos).\n>\n"
        f"> Existe porque medir MAE/MFE so nos trades que voce marcou 'entrado' "
        f"enviesa o dado pela sua propria selecao — que e justamente a variavel "
        f"que se quer isolar pra calibrar parametro. Os descartes sao os "
        f"contrafactuais: sem eles nao da pra saber se `MIN_RR` corta perdedores "
        f"ou vencedores.\n>\n"
        f"> Amostra pequena nao vira evidencia por estar numa tabela. Para varrer "
        f"parametros com historico de verdade, use `python monitor/replay.py "
        f"--varrer stop_buffer` (ou `alvo`, ou `min_rr`).\n\n"
        + corpo + extra + tabela
    )
    os.makedirs(os.path.dirname(CALIBRACAO_PATH), exist_ok=True)
    with open(CALIBRACAO_PATH, "w", encoding="utf-8") as f:
        f.write(content)


def write_status(state, per_pair_data):
    """
    per_pair_data: dict inst_id -> {"trend", "last_1h", "last_4h", "funding", "atr_1h"}
    para os pares processados com sucesso neste ciclo (pares que falharam no
    fetch nao aparecem -- ver comentario no loop principal).
    """
    now_brt = datetime.now(BRT).strftime("%Y-%m-%d %H:%M")
    abertas = count_open_positions()
    detalhe_abertas = open_positions_detail()
    descartes_rr = state.get("contadores", {}).get("descartes_rr_baixo_total", 0)

    linhas = []
    for inst_id in PAIRS:
        d = per_pair_data.get(inst_id)
        pair_state = state["pares"][inst_id]
        if d is None:
            linhas.append(f"| {pair_label(inst_id)} | \u2014 | \u2014 | \u2014 | \u2014 | falha_fetch_neste_ciclo |")
            continue

        zone = pair_state.get("zone")
        if zone:
            zona_txt = (
                f"Setup {zone['setup']} ({zone['direction']}) "
                f"{fmt_price(zone['zone_low'])}-{fmt_price(zone['zone_high'])} "
                f"({zone['touches']}/{ZONE_MAX_TOUCHES} toques, "
                f"{zone['candles_since_creation']}/{ZONE_MAX_CANDLES_1H} candles)"
            )
        else:
            zona_txt = "\u2014"

        linhas.append(
            f"| {pair_label(inst_id)} | {d['trend']} | {fmt_price(d['last_1h']['close'])} | "
            f"{d['funding']*100:.4f}% | {zona_txt} | {pair_state['status']} |"
        )

    detalhe_txt = f" -- {', '.join(detalhe_abertas)}" if detalhe_abertas else ""

    content = (
        f"# Situacao atual -- Multi-Par (script gratuito, sem LLM) -- atualizado {now_brt} BRT\n\n"
        f"> Gerado por `monitor/fetch_and_check.py` via GitHub Actions, sem chamar a API "
        f"do Claude. Registra fatos objetivos; a interpretacao qualitativa fica a seu "
        f"criterio (ou cole este arquivo + o log numa conversa do Claude).\n\n"
        f"**Posicoes abertas (diario, status='entrado' sem resultado ainda):** "
        f"{abertas}/{MAX_POSICOES_SIMULTANEAS}{detalhe_txt}\n\n"
        f"**Confirmacoes descartadas por R:R < {MIN_RR:.0f} (total acumulado, "
        f"CHANGELOG v4 item 8):** {descartes_rr}\n\n"
        f"| Par | Tendencia 4h | Close 1h | Funding | Zona / setup candidato | Status |\n"
        f"|---|---|---|---|---|---|\n"
        + "\n".join(linhas) + "\n"
    )
    os.makedirs(os.path.dirname(STATUS_PATH), exist_ok=True)
    with open(STATUS_PATH, "w", encoding="utf-8") as f:
        f.write(content)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    # Garante que claude/trade_journal.db exista desde a PRIMEIRA execucao,
    # mesmo sem nenhuma zona confirmada ainda -- senao o `git add` do workflow
    # falha com "pathspec did not match any files" toda vez que nenhum par
    # confirmar (a maioria das execucoes). O arquivo criado aqui e so o
    # schema vazio; insert_candidate_trade() so roda quando ha de fato uma
    # confirmacao acima do R:R minimo, em qualquer par.
    ensure_trade_db()
    migrate_log_header_if_needed()

    # SEMPRE primeiro: aplica ao banco qualquer edicao manual feita em
    # claude/sinais.md desde a ultima execucao (Status / Resultado (R)) --
    # antes de qualquer insercao nova ou reescrita do arquivo. Ver
    # CHANGELOG v3, item 5.
    sync_edits_from_sinais_md()

    state = load_state()
    eventos = []
    per_pair_data = {}

    for inst_id in PAIRS:
        try:
            candles_1h = fetch_candles(inst_id, "1H", limit=150)
            candles_4h = fetch_candles(inst_id, "4H", limit=100)
            funding = fetch_funding_rate(inst_id)
        except (RuntimeError, urllib.error.URLError, TimeoutError) as e:
            # um par com falha de API nao derruba a execucao inteira nem
            # impede os outros 9 de serem processados neste ciclo -- so fica
            # sem atualizacao (log/status) ate o proximo run.
            print(f"[erro] Falha ao buscar dados de {inst_id}: {e} -- pulando este par neste ciclo.")
            continue

        trend, _ = classify_trend_4h(candles_4h)
        atr_1h = atr(candles_1h)
        par_lbl = pair_label(inst_id)

        # CHANGELOG v4, item 4: acompanha trades 'entrado' deste par contra as
        # candles novas ANTES da logica de zona -- se resolver aqui, o par ja
        # fica livre pra mapear zona nova no mesmo ciclo (pair_has_open_
        # position consulta o banco, ja teria enxergado o resultado novo).
        track_open_trade_outcomes(par_lbl, candles_1h)
        # v5, item 9: desfecho da tabela de calibracao -- cobre TODO sinal
        # confirmado (aceito ou descartado por R:R), nao so os que voce marcou
        # 'entrado'. E o dado que permite recalibrar STOP_BUFFER_ATR_MULT e a
        # regra de alvo sem esperar acumular mais trades.
        track_mechanical_outcomes(par_lbl, candles_1h)

        pair_state, evento = process_single_pair(
            inst_id, state["pares"][inst_id], candles_1h, candles_4h, trend, atr_1h
        )
        state["pares"][inst_id] = pair_state
        if evento:
            eventos.append(evento)
        if pair_state["status"].startswith("descartado_rr_baixo"):
            # CHANGELOG v4, item 8: contador cumulativo, nunca resetado.
            state["contadores"]["descartes_rr_baixo_total"] += 1

        ultima_1h = last_closed(candles_1h)
        aviso_aberto = check_long_open_alert(
            par_lbl, pair_state, ultima_1h["ts"] if ultima_1h else None
        )
        if aviso_aberto:
            eventos.append(aviso_aberto)

        append_log_line(inst_id, candles_1h, candles_4h, funding,
                        pair_state["status"], trend, atr_1h,
                        zone=pair_state.get("zone"))
        per_pair_data[inst_id] = {
            "trend": trend,
            "last_1h": last_closed(candles_1h),
            "last_4h": last_closed(candles_4h),
            "funding": funding,
            "atr_1h": atr_1h,
        }
        print(f"[{inst_id}] status = {pair_state['status']}" + (" (MUDOU)" if evento else ""))

    # AVISO DE CONFIRMACOES CORRELACIONADAS (CHANGELOG v4, item 6): se 2+
    # pares confirmaram o mesmo setup+direcao neste ciclo, isso vira um
    # evento extra destacando a correlacao -- em vez de mandar os eventos
    # individuais com o mesmo tom de confianca de sempre (achado de
    # 09/09/2026: ETH/SOL/XRP/SUI simultaneos, todos -1R).
    grupos_confirmados = {}
    for ev in eventos:
        if ev.get("tipo") == "sinal" and "setup" in ev:
            grupos_confirmados.setdefault((ev["setup"], ev["direcao"]), []).append(ev["par"])
    for (setup, direcao), pares in grupos_confirmados.items():
        if len(pares) >= 2:
            eventos.insert(0, {
                "tipo": "sinal",
                "titulo": f"⚠️ {len(pares)} confirmacoes simultaneas -- Setup {setup} ({direcao})",
                "mensagem": (
                    f"Pares: {', '.join(pares)}. Mesma janela de execucao -- ver achado de "
                    f"09/09/2026 (CLAUDE.md): sinais correlacionados podem refletir beta de "
                    f"mercado, nao confirmacoes tecnicamente independentes por par."
                ),
            })

    archive_log_if_needed()
    save_state(state)
    write_status(state, per_pair_data)
    write_sinais()
    write_calibracao()

    # NOTIFICACAO PUSH SO PRA SINAL DE VERDADE (CHANGELOG v4, item 5):
    # zona_mapeada/invalidado/expirado continuam gravados no log e no
    # status-simulacao.md (eventos, acima, e usado so pra decidir o push --
    # nada muda na auditoria em arquivo).
    eventos_push = [ev for ev in eventos if ev.get("tipo") == "sinal"]
    send_batched_notifications(eventos_push)

    if eventos:
        print(f"[resumo] {len(eventos)} mudanca(s) de status neste ciclo "
              f"({len(eventos_push)} notificacao(oes) push enviada(s)).")
    else:
        print("[resumo] nenhuma mudanca de status neste ciclo.")


if __name__ == "__main__":
    main()
