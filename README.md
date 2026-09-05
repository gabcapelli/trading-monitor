# Monitoramento BTC-USDT-SWAP -- versao gratuita (sem API do Claude)

Automacao equivalente a tarefa do Cowork, mas rodando de graca no GitHub Actions.
Nenhuma parte deste script chama a API do Claude -- toda a logica de checklist
(secoes 2 e 4 de `plano-trade-price-action.md`) e mecanica, em Python puro.

## O que este pacote faz

- A cada hora (`cron: "2 * * * *"`), busca candles 1h/4h e funding rate na OKX
  (`BTC-USDT-SWAP`), API publica, sem chave.
- Classifica tendencia de 4h (pivos fractais), mapeia zonas candidatas de
  Setup A (rompimento + retest) e Setup B (reversao em zona), com as mesmas
  regras de validade do plano (8 candles sem toque / 3 toques sem confirmacao).
- So notifica (push gratuito via [ntfy.sh](https://ntfy.sh)) quando o **status muda**
  (zona nova, confirmacao, invalidacao, expiracao) -- silencio nas horas sem novidade.
- Atualiza `claude/log-monitoramento-btc-auto.md` e `claude/status-simulacao.md`
  no mesmo espirito dos arquivos que ja existem no seu projeto, e commita de volta
  no repositorio automaticamente.

## O que este pacote NAO faz (leia antes de usar)

- **Nao gera a leitura qualitativa em prosa** que o Claude fazia (forca de candle,
  contexto fino, julgamento de "isso parece rejeicao forte ou fraca"). Registra
  so fatos objetivos. Se quiser a leitura interpretativa, cole o conteudo de
  `claude/status-simulacao.md` + as ultimas linhas do log numa conversa aqui no
  claude.ai (usa seu limite do Pro, nao a API).
- **A deteccao de estrutura e uma aproximacao geometrica** (pivos fractais, janela
  fixa), igual a usada no backtest (`claude/backtest-setup-ab.md`) -- nao substitui
  seu julgamento discricionario nem a validacao ao vivo da secao 3.4 do plano.
  Trate confirmacoes deste script como **candidatas a checar manualmente**, nao
  como um trade automaticamente valido para os 30 da validacao.
- So opera BTC-USDT-SWAP na OKX (mesmo proxy ja documentado no projeto) -- ainda
  e uma venue diferente da Binance; confira valores exatos em decisoes de fronteira.

## Passo a passo para colocar no ar

1. **Crie um repositorio no GitHub** (pode ser privado) e suba estes arquivos
   mantendo a estrutura de pastas (`monitor/`, `claude/`, `.github/workflows/`).

2. **(Opcional, mas recomendado) Configure notificacao push gratuita via ntfy.sh:**
   - Abra o app ntfy (Android/iOS) ou o site https://ntfy.sh
   - Escolha um "topic" unico e dificil de adivinhar, ex: `gabriel-btc-monitor-8f2k`
   - Se inscreva nesse topic no app/site (assim voce recebe o push no celular)
   - No GitHub: **Settings do repositorio -> Secrets and variables -> Actions ->
     New repository secret**, nome `NTFY_TOPIC`, valor = o topic escolhido.
   - Sem esse secret, o script ainda funciona e atualiza os arquivos, so nao
     manda push (fica so no log/status, que voce confere quando quiser).

3. **Ative o workflow:** va na aba **Actions** do repositorio no GitHub -- o
   workflow "BTC Monitor" ja aparece agendado para rodar a cada hora. Voce
   tambem pode clicar em "Run workflow" para testar manualmente na hora.

4. **Confirme que esta commitando de volta:** a primeira execucao ja deve criar/
   atualizar `claude/log-monitoramento-btc-auto.md`, `claude/status-simulacao.md`
   e `monitor/state.json`, e commitar isso automaticamente (usa o token padrao
   do GitHub Actions, sem precisar configurar nada extra).

## Arquivos deste pacote

- `monitor/fetch_and_check.py` -- o script principal (unico arquivo com logica).
- `monitor/state.json` -- estado persistente (zona candidata atual, status).
  Comeca vazio; o proprio script cria/atualiza.
- `claude/log-monitoramento-btc-auto.md` -- log incremental (uma linha/execucao).
- `claude/status-simulacao.md` -- resumo do estado atual, reescrito a cada execucao.
- `.github/workflows/btc-monitor.yml` -- agendamento (cron) e commit automatico.

## Custo

Zero, dentro do uso normal: OKX (API publica gratuita), ntfy.sh (gratuito, sem
cadastro), GitHub Actions (24 execucoes/dia de um script leve fica bem dentro
do limite gratuito de minutos/mes para repositorios publicos ou privados de
conta pessoal).

## Proximo passo sugerido

Depois de rodar por alguns dias, compare o log deste script com o log antigo
gerado pelo Cowork (`claude/log-monitoramento-btc-auto-archive.md`) para
verificar se a deteccao mecanica de zonas esta razoavelmente alinhada com a
leitura que voce faria manualmente -- ajuste os parametros no topo do script
(`ZONE_MAX_CANDLES_1H`, `ZONE_MAX_TOUCHES`, `ZONE_ATR_MULT`, `STALE_4H_CANDLES`)
se notar zonas mapeadas cedo/tarde demais.
