# Setup C — testes de detecção OB/FVG (11/09/2026)

> Continuação de [`setup-c-gabarito.md`](setup-c-gabarito.md): aqui já não é o gabarito qualitativo, é o backtest de pesquisa que ele pedia como "próximo passo" — comparar duas fontes de detecção de zona sobre o mesmo harness de saída (stop/alvo/RR/desfecho idênticos ao Setup A/B em produção), nos 10 pares do projeto. Scripts em `monitor/replay_setup_c.py` e `monitor/inspect_pair_setup_c.py`. **Só leitura — nenhum resultado daqui virou trade, parâmetro ou gate.**
>
> Nota de processo: esse teste já tinha sido rodado numa sessão anterior (10/09), mas só existia no scratchpad temporário de uma sessão de IDE — não persistido no repo. Este arquivo existe pra que isso não se repita.
>
> **Atualização 11/09/2026**: adicionada a seção "Cruzamento com o gabarito real" — checagem direta contra 3 trades reais do OTS. Depois, adicionada a seção "Backtest estendido (400 dias) e um bug real" — achado mais importante deste arquivo: as leituras positivas de ARB/XRP no backtest de 90 dias eram artefato de um bug de escopo no harness de replay, não edge real. **As tabelas "Resultado agregado" e "Por par" originais (90 dias) abaixo ficam só como registro histórico — os números de referência atuais são os da seção do backtest de 400 dias, corrigido.**

## Metodologia

Duas fontes de detecção de zona, mesmo harness de saída:

- **A) "lib como está"**: `smc.ob()` + `smc.fvg()` da biblioteca `smartmoneyconcepts`, com `swing_highs_lows()` dela mesma (`swing_length=10`).
- **B) "caseiro"**: mesma ideia de order block (último candle oposto antes do rompimento de estrutura), mas usando `find_confirmed_pivots` (`PIVOT_WINDOW=3`) do próprio projeto em vez do swing da lib — isola exatamente a variável que já causou a divergência conhecida em A/B (definição de pivô/swing, ver `CLAUDE.md`). FVG usa a mesma definição matemática (não ambígua) nas duas, com filtro de tamanho mínimo (`0.05 × ATR`) só na caseira.

Walk-forward sobre ~90 dias de candles 1h/4h (histórico paginado da OKX), janela de contexto de 200 candles por passo, zona só conta como "nova" se formada nos últimos 3 candles da janela. Zona só é aceita se alinhada com a tendência 4h (mesma regra de A/B), expira em `ZONE_MAX_CANDLES_1H` sem toque. Ao tocar: entrada no fechamento, stop a `STOP_BUFFER_ATR_MULT × ATR` do extremo da zona, alvo pelo pivô oposto mais próximo (`modo="proximo"`, regra v6), filtro `MIN_RR ≥ 2.0`, desfecho por `desfecho_mecanico()` (mesma função de produção).

## Resultado agregado (10 pares, 90 dias) — histórico, ver ressalva acima

| | A) smartmoneyconcepts | B) caseiro |
|---|---|---|
| Zonas → sinal | 2436 | 2876 |
| Aceitos (RR≥2) | 155 | 141 |
| Resolvidos | 154 | 137 |
| Wins | 41 (26,6%) | 33 (24,1%) |
| Expectância | +0,192R | +0,041R |
| IC 95% bootstrap | [-0,139, +0,565] | [-0,278, +0,384] |

**Os dois intervalos cruzam zero — sem edge estatisticamente distinguível de zero em nenhum dos dois detectores**, no agregado. Consistente com o que já foi encontrado em Setup A/B (`auditoria-v5.md`, `auditoria-v6.md`).

## Por par (90 dias) — histórico, ver ressalva acima

| Par | Lib: n / win% / exp / IC95% | Caseiro: n / win% / exp / IC95% |
|---|---|---|
| ARB | 10 / 10,0% / -0,641R / [-1,000, +0,078] | 9 / 22,2% / +0,367R / [-1,000, +2,304] |
| BTC | 14 / 50,0% / +0,911R / [-0,106, +1,937] | 12 / 41,7% / +0,574R / [-0,434, +1,686] |
| DOGE | 13 / 30,8% / +0,256R / [-0,741, +1,389] | 12 / 25,0% / -0,082R / [-1,000, +0,960] |
| ETH | 19 / 15,8% / -0,432R / [-1,000, +0,239] | 14 / 14,3% / -0,457R / [-1,000, +0,395] |
| LINK | 15 / 13,3% / -0,468R / [-1,000, +0,277] | 16 / 6,2% / -0,702R / [-1,000, **-0,107**] |
| SOL | 10 / 20,0% / +0,276R / [-1,000, +2,225] | 10 / 10,0% / -0,699R / [-1,000, **-0,097**] |
| SUI | 8 / 25,0% / +0,031R / [-1,000, +1,425] | 6 / 16,7% / -0,245R / [-1,000, +1,265] |
| UNI | 33 / 24,2% / +0,228R / [-0,508, +1,089] | 28 / 25,0% / +0,319R / [-0,534, +1,425] |
| WLD | 16 / 18,8% / -0,234R / [-1,000, +0,625] | 17 / 17,6% / -0,279R / [-1,000, +0,529] |
| XRP | 16 / 56,2% / +1,776R / [**+0,349**, +3,595] | 13 / 61,5% / +1,407R / [**+0,309**, +2,470] |

Amostras por par são pequenas (n = 6 a 33) — nenhuma leitura por par deve ser tratada como calibração, só como indício pra investigar. Com 10 pares testados independentemente a 95%, ~0,5 "falso positivo" por acaso já é esperado estatisticamente — XRP sozinho com IC positivo nos dois detectores não é, por si, evidência de edge específico do par.

## XRP: checagem de sensibilidade a outlier

XRP foi o único par com IC 95% inteiramente positivo nos dois detectores — checado antes de dar peso a isso, porque amostra pequena com distribuição assimétrica (poucos wins grandes, vários -1R) é exatamente o cenário onde 1-2 trades dominam a soma.

| | Completo | Sem o maior trade | Sem os 2 maiores |
|---|---|---|---|
| **Lib** (n=16) | +1,776R — IC [+0,349, +3,596] | +1,086R — IC [+0,081, +2,149] | +0,815R — IC **[-0,188, +1,764]** |
| **Caseiro** (n=13) | +1,407R — IC [+0,309, +2,469] | +1,117R — IC [+0,107, +2,132] | +0,900R — IC **[-0,093, +1,892]** |

- Lib: um único trade (compra FVG, 03/07 13:00, entrada 1,1148 → alvo 1,1395, +12,13R) responde por **42,7%** da soma total dos 16 trades. Os 2 maiores juntos (+12,13R e +4,88R) somam **59,9%**.
- Caseiro: o maior trade (+4,88R, 05/09 04:00) sozinho é **26,7%** da soma.
- **Removendo os 2 maiores de cada lista, o IC 95% passa a incluir zero nos dois detectores.** O resultado "totalmente positivo" de XRP não é robusto a 1-2 trades.
- Achado extra: o trade de +12,13R (o que mais infla a lib) **não aparece na lista do caseiro** — a zona de FVG que gerou esse trade específico só existe na detecção via `swing_highs_lows` da lib, não na baseada no pivô próprio. Parte da vantagem aparente da lib sobre o caseiro no agregado (+0,192R vs +0,041R) vem de uma zona onde as duas abordagens discordam em detectar, não de uma diferença sistemática de qualidade de sinal.

**Conclusão sobre XRP: não tratar como par com edge demonstrado no Setup C.** Mesma régua que já vem sendo aplicada em A/B — um IC positivo que desaparece ao tirar 1-2 trades não é achado, é ruído com cara de achado.

## Cruzamento com o gabarito real (11/09/2026)

O agregado estatístico acima responde "qual detector dá mais R", mas não responde à pergunta original do gabarito (`setup-c-gabarito.md`): **os detectores marcam zona no mesmo lugar que o OTS operou de verdade?** Os 3 exemplos genuínos do gabarito caem dentro da janela de histórico já baixada (BTC short 09/09, BTC compra 28/06, SOL compra 30/06), então dá pra checar diretamente.

**Metodologia**: pra cada exemplo, rodei os dois detectores (sem filtro de tendência/RR — só presença de zona) em janelas de contexto de 200 candles, recomputadas a cada hora, numa busca de 5-10 dias antes do trade real. Um "hit" é qualquer zona (OB ou FVG) cuja faixa de preço sobrepõe a faixa descrita no gabarito, na direção certa. Script: `monitor/inspect_pair_setup_c.py` não serve pra isso — usei um script à parte (ver Reprodução).

**Correção de processo, registrada porque é relevante**: a primeira rodada contou 4-7 "hits" pra cada exemplo sem distinguir tipo, o que parecia contradizer o teste de ontem (que tinha concluído que `smc.ob` não reproduzia nenhum dos 3 exemplos). Quebrando por tipo (OB vs. FVG) e comparando contra quantas zonas *totais* (qualquer preço/direção) cada detector gerou na mesma janela, a aparente contradição se desfaz — ver tabela.

| Exemplo | Lib: OB hits / total gerado | Lib: FVG hits / total gerado | Caseiro: OB hits / total gerado | Caseiro: FVG hits / total gerado |
|---|---|---|---|---|
| BTC short (ex.1) | 0 / 0 | 1 / 20 | **2 / 10** | 0 / 16 |
| BTC compra (ex.2) | 0 / 2 | 1 / 42 | **2 / 20** | 1 / 38 |
| SOL compra (ex.3) | 0 / 0 | 4 / 51 | **3 / 20** | 4 / 45 |

- **`smc.ob` (lib) não achou order block perto da zona real em nenhum dos 3 casos** — em 2 dos 3, a lib nem gerou candidato de OB nenhum na janela inteira. **Confirma** o achado de ontem (`test_smc_gabarito.py`, mesma conclusão por caminho independente).
- Os hits reportados na primeira rodada vieram quase todos de FVG, que tem densidade alta (20-51 candidatos numa janela de poucos dias) — mesmo problema de ruído já sinalizado ontem: com esse volume, achar *algum* FVG perto de *qualquer* preço que o mercado revisitou não é evidência forte.
- **O detector caseiro de OB teve hit nos 3 casos** (2/10, 2/20, 3/20), com densidade total bem menor que FVG. Não é prova — n=3, sem linha de base formal de "chance" ajustada ao tamanho da banda vs. range de preço de cada janela — mas é o sinal mais concreto a favor do caseiro sobre a lib que apareceu em todo o teste do Setup C, mais nítido até que a diferença de expectância agregada (+0,192R lib vs. +0,041R caseiro).

**Conclusão desta seção**: entre os dois, a detecção caseira de order block é a que mais se aproxima do gabarito qualitativo — a lib erra sistematicamente o OB e só "acerta" via FVG ruidoso. Isso não decide sozinho se o Setup C deve usar a caseira (n=3 é pouco), mas é um motivo concreto pra não adotar `smartmoneyconcepts` como fonte de OB sem mais trabalho, reforçando o que a auditoria de A/B já tinha achado sobre essa lib.

## Backtest estendido (400 dias) e um bug real (11/09/2026)

Os 10 pares têm pelo menos 417 dias de histórico 1h consistentes na OKX — bem mais que os 90 dias usados acima. `replay_setup_c.py` ganhou um argumento `--dias` (default 90, preserva o comportamento original) pra rodar sobre uma janela maior sem precisar de script separado.

### O bug: escopo de histórico sem limite no harness de replay

Rodando `--dias 400`, ARB e XRP apareceram com IC 95% inteiramente positivo nos dois detectores (n=72-101 por par, bem maior que os 13-16 do teste de 90 dias) — e dessa vez sobrevivendo à checagem de sensibilidade a outlier de 1 trade (só cedia ao tirar 2). Antes de aceitar isso como achado, investiguei os trades específicos por trás do resultado.

**Achado**: os 3 maiores trades de XRP (lib e caseiro, idênticos) tinham `alvo = 1.15730` — o mesmo valor exato, apesar de entradas bem diferentes (1,6995 / 1,6759 / 1,7468), gerando RR de 40,02 / 22,11 / 11,19. Rastreando a origem: `1.15730` é o `low` de um único candle de 1h em **2025-10-10 18:00** — `open=2,4941, high=2,5488, close=2,2279`, volume ~60-75x o normal da época. É um pavio de flash-crash de 1 candle, não uma estrutura de mercado real.

**Causa raiz**: `nearest_target_candidate(direcao, candles_1h, ...)` roda `find_confirmed_pivots` sobre o array `candles_1h` inteiro que recebe. No replay, `janela_1h = c1h[:i+1]` cresce a cada passo do walk-forward — com 400 dias de histórico acumulado, a busca por "pivô mais próximo em preço" (regra v6) pode alcançar qualquer candle já visto, incluindo esse pavio de 11 meses antes. Ele "ganha" por estar mais próximo em preço do que qualquer pivô estrutural de verdade, e vira alvo de 3 trades distintos meses depois — o RR gigante é artefato de escopo, não edge.

**Isso não acontece ao vivo**: `fetch_candles()` (produção) busca só `limit=150` candles (~6,25 dias) — nunca vê 11 meses de histórico. O bug é exclusivo de harnesses de replay que simulam uma janela crescente sem limitar a busca de alvo a algo equivalente ao que a produção veria.

**Implicação pro resto do projeto**: `monitor/replay.py` (harness oficial de A/B, usado nas auditorias v5/v6) tem o mesmo padrão — `janela_1h = c1h[:i + 1]` alimentando `compute_suggestion` (que chama `nearest_target_candidate` por dentro) sem limite. As rodadas de replay de A/B até agora cobriram janelas mais curtas (~33-40 dias), o que reduz a chance de alcançar um candle anômalo antigo, mas o mecanismo do bug é o mesmo e não foi corrigido lá. **Não mexi em `replay.py`** — é o harness que já embasou decisões reais (troca da regra de alvo em v6), então a correção lá merece decisão explícita, não uma edição de passagem. Sinalizando pra você decidir se vale corrigir antes de confiar em replay de A/B sobre janelas mais longas no futuro.

**Correção aplicada aqui**: `replay_setup_c.py` agora limita a busca de alvo aos últimos `ALVO_LOOKBACK = 150` candles (mesmo valor do `limit` de produção) em vez do histórico inteiro.

### Resultado agregado, 400 dias, corrigido

| | A) smartmoneyconcepts | B) caseiro |
|---|---|---|
| Aceitos (RR≥2) | 1665 | 1518 |
| Resolvidos | 1663 | 1515 |
| Wins | 368 (22,1%) | 321 (21,2%) |
| Expectância | -0,052R | **-0,112R** |
| IC 95% bootstrap | [-0,143, +0,042] | **[-0,200, -0,018]** |

Com ~5x mais amostra que o teste de 90 dias, o quadro mudou de "sem informação suficiente" para **"provável leve edge negativo"**: o caseiro agora tem IC inteiramente negativo (não cruza zero, n=1515). A lib fica bem perto de zero, levemente negativa, cruzando por pouco.

### Por par, 400 dias, corrigido

| Par | Lib: n / win% / exp / IC95% | Caseiro: n / win% / exp / IC95% |
|---|---|---|
| ARB | 141 / 19,9% / -0,132R / [-0,423, +0,178] | 137 / 20,4% / -0,071R / [-0,387, +0,274] |
| BTC | 192 / 22,4% / -0,077R / [-0,323, +0,192] | 169 / 23,7% / -0,032R / [-0,299, +0,255] |
| DOGE | 142 / 19,7% / -0,075R / [-0,407, +0,303] | 143 / 15,4% / **-0,344R / [-0,596, -0,070]** |
| ETH | 153 / 19,0% / -0,176R / [-0,448, +0,121] | 129 / 16,3% / **-0,319R / [-0,580, -0,033]** |
| LINK | 162 / 20,4% / -0,193R / [-0,443, +0,082] | 148 / 19,6% / **-0,270R / [-0,501, -0,018]** |
| SOL | 159 / 23,3% / +0,024R / [-0,280, +0,341] | 144 / 23,6% / -0,020R / [-0,314, +0,310] |
| SUI | 174 / 19,0% / -0,167R / [-0,438, +0,116] | 159 / 17,6% / -0,191R / [-0,471, +0,122] |
| UNI | 193 / 21,2% / -0,090R / [-0,343, +0,179] | 175 / 20,0% / -0,153R / [-0,410, +0,124] |
| WLD | 158 / 28,5% / +0,271R / [-0,065, +0,630] | 141 / 29,1% / +0,252R / [-0,083, +0,620] |
| XRP | 189 / 27,0% / +0,081R / [-0,178, +0,351] | 170 / 25,3% / +0,001R / [-0,266, +0,285] |

- **ARB e XRP, antes "positivos e robustos", desaparecem** com a correção — confirma que eram artefato do bug, não edge real. Nenhum par mostra IC positivo em nenhum dos dois detectores agora.
- **DOGE, ETH e LINK aparecem negativos no caseiro** — mas só nesse detector, não na lib. Pela mesma régua já aplicada a XRP antes (só confiar em padrão que se repete nos dois detectores independentes), **não** trato isso como achado — pode ser peculiaridade da lógica de OB/FVG caseira nesses pares, não do Setup C em si.
- Nenhum par sobrevive como candidato positivo isolado. O agregado do caseiro (-0,112R, IC totalmente negativo, n=1515) é hoje o resultado mais bem-fundamentado deste arquivo inteiro.

## Conclusão geral

- **Com o bug de escopo corrigido e ~5x mais amostra (400 dias), o Setup C não mostra edge positivo em lugar nenhum** — nem no agregado, nem por par, em nenhum dos dois detectores. O caseiro tem inclusive expectância negativa estatisticamente significativa no agregado.
- As leituras positivas do teste de 90 dias (XRP, e depois ARB/XRP a 400 dias antes da correção) eram, respectivamente, sensibilidade a 1-2 outliers e um bug real de escopo de histórico — nenhuma sobreviveu a investigação mais funda. Isso reforça o valor de nunca aceitar IC positivo sem antes checar a robustez por trás dele.
- A vantagem aparente da lib sobre o caseiro no teste de 90 dias não se sustenta a 400 dias — na verdade inverteu: o caseiro agora é o mais negativo dos dois no agregado.
- Isso **não decide** se o Setup C deve usar a lib, a detecção caseira, ou nenhuma das duas — mas pesa contra as duas por performance agregada. A escolha de qual detector usar (se algum dia o setup for implementado) continua mais apoiada no cruzamento com o gabarito qualitativo (seção acima: caseiro bate melhor com os 3 trades reais do OTS) do que em expectância de backtest.
- Setup C continua sem código em produção — isso é só pesquisa preparatória. Com o dado atual, não há base estatística pra justificar implementá-lo esperando lucro.
- **Pendente**: `monitor/replay.py` (harness oficial de A/B) tem o mesmo bug de escopo — não corrigido, sinalizado acima. Vale decidir se merece correção antes de confiar em qualquer replay futuro de A/B sobre janelas mais longas que as já rodadas.

## Reprodução

```bash
PYTHONPATH=monitor python monitor/replay_setup_c.py                        # backtest, 90 dias (default)
PYTHONPATH=monitor python monitor/replay_setup_c.py --dias 400             # backtest estendido, 400 dias
PYTHONPATH=monitor python monitor/inspect_pair_setup_c.py XRP-USDT-SWAP    # trades individuais de 1 par (90 dias)
PYTHONPATH=monitor python monitor/check_gabarito_setup_c.py                # cruzamento com os 3 exemplos reais do gabarito
```
