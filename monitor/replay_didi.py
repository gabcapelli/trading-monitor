"""
Teste unico, PRE-REGISTRADO (22/09/2026), da "agulhada do Didi" do video
"[Melhor explicacao] do setup e operacional agulhada do didi passo a passo".
Estudo avulso: NAO faz parte do checklist dos Setups A/B/C nem do monitor de
producao. Regras e criterio escritos ANTES de rodar qualquer simulacao.
[interp] = interpretacao minha -- a transcricao e muito vaga (nao da
parametro de indicador, stop nem alvo); as regras abaixo sao o setup Didi
classico objetivado.

REGRAS -- COMPRA (venda e espelho exato)
----------------------------------------
- Didi Index: MMA3/MMA8 (curta) e MMA20/MMA8 (longa), a de 8 como linha 1.
- "Agulhada" de compra no candle t: a curta cruza 1 para cima e a longa
  cruza 1 para baixo no mesmo candle ou com 1 candle de tolerancia [interp:
  "as tres medias se cruzam no mesmo ponto"].
- Confirmacoes (os "quatro indicadores sincronizados"; na grade, isoladas,
  todas juntas ou nenhuma) [interp: parametros classicos do Didi]:
  "bollinger": Bollinger(8, 2) abrindo -- largura[t] > largura[t-1].
  "trix": TRIX(9) acima da sua linha de sinal (MME4 do TRIX).
  "estocastico": %K lento (8,3,3) acima do %D.
  "todas": as tres ao mesmo tempo.
- Entrada: abertura do candle seguinte ("na abertura desse candle").
- Stop: minima do candle da agulhada [interp: o video nao define stop; e o
  que o plano de risco exige para dimensionar a posicao].
- Saida (duas, na grade):
  "2R": alvo fixo de 2x o risco.
  "reversao": fecha no fechamento do candle em que a curta cruza 1 de volta
    (a agulhada se desfaz); o stop continua valendo.
- Candle da entrada: entrada na abertura, entao qualquer toque no stop nele
  e perda real (stop_vale_no_candle_entrada trata isso). Alvo nunca conta no
  candle da entrada; stop e alvo no mesmo candle depois dele = stop.
- Uma posicao por par; trade aberto no fim fechado no ultimo fechamento.
  Custo: 0.18% ida+volta em R.
[desvio] "pelo menos 200 pontos" e alvo em pontos do ouro/dolar, sem
traducao para cripto; "treinar o olho" e discricionario e nao e modelado.

GRADE
-----
5 confirmacoes x 2 saidas = 10 combinacoes, em 1Dutc (3000 dias) e 4H (2000
dias) = 20 celulas, 20 pares. Descritivo: 1H (300 dias).

CRITERIO DE DECISAO (pre-registrado; protocolo de estudos-avulsos.md)
--------------------------------------------------------------------
1. Holdout temporal: na 1a metade escolhe-se a celula de maior expectancia
   liquida em R entre as com n >= 200 no treino; so ela e testada na 2a
   metade; IC95 inteiro acima de zero. Nenhuma celula com n >= 200 ->
   "sem amostra para decidir".
2. E a mesma celula nos 80 pares fora da amostra (replay_91_beta.UNIVERSO_B;
   se a celula for 4H, baixa-se o 4H desses pares), IC95 inteiro acima de
   zero.
PASSA so se 1 e 2 passarem.
"""

from replay_ema_ribbon import ic_bootstrap, CUSTO_RT, UNIVERSO, stop_vale_no_candle_entrada
from replay_stoch_vwap import baixar, sma, estocastico
from replay_91_williams import mme
from replay_91_beta import UNIVERSO_B

CONFIRMACOES = ["nenhuma", "bollinger", "trix", "estocastico", "todas"]
SAIDAS = ["2R", "reversao"]
DECIDEM = [("1Dutc", 3000), ("4H", 2000)]
DESCRITIVOS = [("1H", 300)]
TOLERANCIA = 1
AQUECIMENTO = 80
MIN_N_SELECAO = 200


def trix_e_sinal(closes, n=9, ns=4):
    e3 = mme(mme(mme(closes, n), n), n)
    t = [None] + [e3[i] / e3[i - 1] - 1 for i in range(1, len(e3))]
    base = [x if x is not None else 0.0 for x in t]
    return t, mme(base, ns)


def largura_bollinger(closes, n=8, k=2.0):
    out = [None] * len(closes)
    for i in range(n - 1, len(closes)):
        j = closes[i - n + 1:i + 1]
        m = sum(j) / n
        dp = (sum((x - m) ** 2 for x in j) / n) ** 0.5
        out[i] = 2 * k * dp / m if m else None
    return out


def agulhadas(closes):
    """ag[t] = +1 agulhada de compra, -1 de venda, 0 nada."""
    m3, m8, m20 = sma(closes, 3), sma(closes, 8), sma(closes, 20)
    curta = [None if None in (m3[i], m8[i]) else m3[i] / m8[i] for i in range(len(closes))]
    longa = [None if None in (m20[i], m8[i]) else m20[i] / m8[i] for i in range(len(closes))]

    def cruz(serie, i, d):
        if i < 1 or None in (serie[i], serie[i - 1]):
            return False
        return (serie[i] > 1 >= serie[i - 1]) if d == 1 else (serie[i] < 1 <= serie[i - 1])

    ag = [0] * len(closes)
    for t in range(1, len(closes)):
        for d in (1, -1):
            if not cruz(curta, t, d):
                continue
            # a longa cruza para o outro lado dentro da tolerancia; o sinal so
            # existe no ULTIMO dos dois cruzamentos (usar o candle seguinte
            # seria olhar o futuro: a entrada e na abertura dele)
            for k in range(-TOLERANCIA, TOLERANCIA + 1):
                u = t + k
                if 0 <= u < len(closes) and cruz(longa, u, -d):
                    ag[max(t, u)] = d
                    break
    return ag, curta


def simular(c, confirmacao, saida_modo):
    closes = [x[4] for x in c]
    ag, curta = agulhadas(closes)
    larg = largura_bollinger(closes)
    tx, tx_sinal = trix_e_sinal(closes)
    k_st, d_st = estocastico(c, 8, 3, 3)
    trades, t = [], AQUECIMENTO
    while t < len(c) - 1:
        d = ag[t]
        if d == 0:
            t += 1
            continue
        if confirmacao in ("bollinger", "todas"):
            if larg[t] is None or larg[t - 1] is None or larg[t] <= larg[t - 1]:
                t += 1
                continue
        if confirmacao in ("trix", "todas"):
            if tx[t] is None or (tx[t] - tx_sinal[t]) * d <= 0:
                t += 1
                continue
        if confirmacao in ("estocastico", "todas"):
            if k_st[t] is None or d_st[t] is None or (k_st[t] - d_st[t]) * d <= 0:
                t += 1
                continue
        j = t + 1
        entrada = c[j][1]
        stop = c[t][3] if d == 1 else c[t][2]
        risco = (entrada - stop) * d
        if risco <= 0:
            t += 1
            continue
        alvo = entrada + 2 * d * risco
        saida = None
        for q in range(j, len(c)):
            hi, lo = c[q][2], c[q][3]
            if ((lo <= stop) if d == 1 else (hi >= stop)) and (q > j or stop_vale_no_candle_entrada(c[j], d, entrada)):
                saida, preco = q, (min(stop, c[q][1]) if d == 1 else max(stop, c[q][1]))
                break
            if q == j:
                continue
            if saida_modo == "2R":
                if (hi >= alvo) if d == 1 else (lo <= alvo):
                    saida, preco = q, (max(alvo, c[q][1]) if d == 1 else min(alvo, c[q][1]))
                    break
            elif curta[q] is not None and ((curta[q] < 1) if d == 1 else (curta[q] > 1)):
                saida, preco = q, c[q][4]
                break
        if saida is None:
            saida, preco = len(c) - 1, c[-1][4]
        bruto = (preco - entrada) * d / risco
        custo_r = CUSTO_RT * entrada / risco
        trades.append({"ts": c[j][0], "d": d, "r": bruto - custo_r, "bruto": bruto, "custo_r": custo_r})
        t = saida + 1
    return trades


def rodar(universo, bar, dias, conf, saida):
    todos, ts = [], []
    for inst in universo:
        c = baixar(inst, bar, dias)
        if len(c) <= AQUECIMENTO + 10:
            continue
        ts += [c[0][0], c[-1][0]]
        todos += simular(c, conf, saida)
    return todos, ((min(ts) + max(ts)) // 2 if ts else 0)


def media(trades, chave="r"):
    return sum(x[chave] for x in trades) / len(trades) if trades else float("nan")


def acerto(trades):
    return 100 * sum(x["bruto"] > 0 for x in trades) / len(trades) if trades else float("nan")


def linha_ic(rotulo, trades):
    if len(trades) < 3:
        return f"  {rotulo}: n={len(trades)} (insuficiente)", False
    lo, hi, dias = ic_bootstrap(trades, "r")
    return (f"  {rotulo}: n={len(trades):>5} | dias={dias:>5} | exp {media(trades):+.3f}R | "
            f"IC95 [{lo:+.3f}, {hi:+.3f}] | bruto {media(trades, 'bruto'):+.3f}R | "
            f"acerto {acerto(trades):.1f}% | custo {media(trades, 'custo_r'):.3f}R"), lo > 0


def main():
    print(f"{'='*104}\nUNIVERSO A (20 pares) -- grade\n{'='*104}")
    print(f"  {'combinacao':<36} {'n':>6} {'exp liq':>8} {'bruto':>7} {'acerto':>6} {'custo':>6} | "
          f"{'n tr':>5} {'exp tr':>7} | {'n te':>5} {'exp te':>7}")
    celulas = []
    for bar, dias in DECIDEM:
        for conf in CONFIRMACOES:
            for saida in SAIDAS:
                tr, meio = rodar(UNIVERSO, bar, dias, conf, saida)
                treino = [x for x in tr if x["ts"] < meio]
                teste = [x for x in tr if x["ts"] >= meio]
                nome = f"{bar:<5} conf={conf:<11} saida={saida}"
                print(f"  {nome:<36} {len(tr):>6} {media(tr):>+8.3f} {media(tr, 'bruto'):>+7.3f} "
                      f"{acerto(tr):>5.1f}% {media(tr, 'custo_r'):>6.3f} | {len(treino):>5} {media(treino):>+7.3f} | "
                      f"{len(teste):>5} {media(teste):>+7.3f}", flush=True)
                celulas.append((nome, bar, dias, conf, saida, treino, teste))
    print("\n  descritivo (fora da selecao):")
    for bar, dias in DESCRITIVOS:
        for conf in CONFIRMACOES:
            for saida in SAIDAS:
                tr, _ = rodar(UNIVERSO, bar, dias, conf, saida)
                nome = f"{bar:<5} conf={conf:<11} saida={saida}"
                print(f"  {nome:<36} {len(tr):>6} {media(tr):>+8.3f} {media(tr, 'bruto'):>+7.3f} "
                      f"{acerto(tr):>5.1f}% {media(tr, 'custo_r'):>6.3f}", flush=True)

    print(f"\n{'='*104}\nDECISAO\n{'='*104}")
    eleg = [x for x in celulas if len(x[5]) >= MIN_N_SELECAO]
    if not eleg:
        print(f"  nenhuma celula com n >= {MIN_N_SELECAO} no treino -> SEM AMOSTRA PARA DECIDIR")
        return
    nome, bar, dias, conf, saida, treino, teste = max(eleg, key=lambda x: media(x[5]))
    print(f"  selecionada no treino -> {nome}   ({len(eleg)} de {len(celulas)} celulas com n >= {MIN_N_SELECAO})")
    print(linha_ic("treino (1a metade, so referencia)", treino)[0])
    l1, ok1 = linha_ic("1) TESTE (2a metade)              ", teste)
    print(l1)
    print(linha_ic("   so compras (teste)             ", [x for x in teste if x["d"] == 1])[0])
    print(linha_ic("   so vendas (teste)              ", [x for x in teste if x["d"] == -1])[0])
    tr_b, _ = rodar(UNIVERSO_B, bar, dias, conf, saida)
    l2, ok2 = linha_ic("2) 80 PARES FORA DA AMOSTRA        ", tr_b)
    print(l2)
    print(f"\n==> DECISAO: holdout {'ok' if ok1 else 'falhou'}, fora da amostra {'ok' if ok2 else 'falhou'}"
          f" -> {'PASSA' if ok1 and ok2 else 'NAO PASSA'}")


if __name__ == "__main__":
    main()
