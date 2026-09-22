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

## Leitura conjunta

Mesma direção do achado da auditoria v6 sobre o checklist mecânico dos Setups A/B: nenhum dos dois setups de vídeo tem edge mecânico demonstrável nesses 20 pares, e ambos pioram quanto menor o tempo gráfico (custo em R cresce). Não reabrir esses testes sem uma regra nova pré-registrada — variar parâmetro em cima destes mesmos dados até algo ficar positivo invalida o critério.
