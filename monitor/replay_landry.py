"""
Teste unico, PRE-REGISTRADO (22/09/2026), do pullback de Dave Landry como
apresentado no video "Setup de Swing Trade" (acoes da B3, com uma versao
"modificada no Brasil"). Estudo avulso: NAO faz parte do checklist dos
Setups A/B/C nem do monitor de producao. Regras e criterio escritos ANTES de
rodar qualquer simulacao. [interp] = interpretacao minha.

REGRAS -- COMPRA (venda e espelho exato)
----------------------------------------
- Tendencia, duas variantes:
  "mma21": MMA21 subindo (MMA21[t] > MMA21[t-1]) -- o original.
  "9-20-50": MMA9, MMA20 e MMA50 subindo ao mesmo tempo -- a modificacao do
    autor ("so quando as tres medias estiverem apontando para cima")
    [interp: aritmeticas, como a de 21; a transcricao diz "19 20 e 50" e
    depois "media de 9 subindo, 20 subindo, 50 subindo"].
- Sinal no candle t: low[t] < min(low[t-1], low[t-2]) com a tendencia valida.
- Ordem: compra stop na maxima de t; stop na minima de t; alvo 2R a partir
  da entrada. A cada novo candle que tambem faz sinal, a ordem desce para a
  maxima dele (e o stop para a minima dele). Media virou para baixo ->
  cancela ("cancela todas as compras").
- Candle que NAO faz sinal e nao aciona (duas leituras, na grade):
  "persistente": a ordem continua na ultima maxima armada.
  "1-candle": a ordem cai; espera o proximo sinal.
- Execucao: aciona no candle j se high[j] >= gatilho; preco = max(gatilho,
  open[j]). Candle da entrada: toque no stop resolvido pela heuristica OHLC
  (stop_vale_no_candle_entrada em replay_ema_ribbon.py); alvo nunca conta
  nele; stop e alvo no mesmo candle depois dele = stop.
- Uma posicao por par; sinais durante trade aberto ignorados. Trade aberto no
  fim do historico fechado no ultimo fechamento. Custo: 0.18% ida+volta em R.

GRADE
-----
2 tendencias x 2 leituras da ordem = 4 combinacoes, em 1Dutc e 1W (semanal
agregado do diario, segunda a domingo UTC, igual ao replay_inside_bar) =
8 celulas, 3000 dias, 20 pares. Descritivo: 4H (2000 dias) e 1H (300 dias),
que o video tambem cita. Reportado: taxa de acerto (o video diz ~50% no
diario e ~68% no semanal).

CRITERIO DE DECISAO (pre-registrado)
------------------------------------
1. Holdout temporal: na 1a metade escolhe-se a celula de maior expectancia
   liquida em R (n >= 30); so ela e testada na 2a metade; IC95 > 0.
2. E, obrigatoriamente, a mesma celula nos 80 pares fora da amostra
   (replay_91_beta.UNIVERSO_B, historico inteiro), IC95 > 0.
PASSA so se 1 e 2 passarem.
"""

from replay_ema_ribbon import ic_bootstrap, CUSTO_RT, UNIVERSO, stop_vale_no_candle_entrada
from replay_stoch_vwap import baixar, sma
from replay_inside_bar import semanal
from replay_91_beta import UNIVERSO_B

TENDENCIAS = ["mma21", "9-20-50"]
ORDENS = ["persistente", "1-candle"]
DECIDEM = ["1Dutc", "1W"]
DESCRITIVOS = [("4H", 2000), ("1H", 300)]
ALVO_R = 2.0
AQUECIMENTO = 60
MIN_N_SELECAO = 30


def serie(inst, bar, dias=3000):
    if bar == "1W":
        return semanal(baixar(inst, "1Dutc", 3000))
    return baixar(inst, bar, dias)


def tendencia(c, modo):
    closes = [x[4] for x in c]
    periodos = [21] if modo == "mma21" else [9, 20, 50]
    medias = [sma(closes, p) for p in periodos]
    out = [0] * len(c)
    for t in range(1, len(c)):
        if any(m[t] is None or m[t - 1] is None for m in medias):
            continue
        if all(m[t] > m[t - 1] for m in medias):
            out[t] = 1
        elif all(m[t] < m[t - 1] for m in medias):
            out[t] = -1
    return out


def simular(c, modo, ordem_modo):
    tend = tendencia(c, modo)
    trades = []
    ordem = None  # dict(d, gatilho, stop)
    t = AQUECIMENTO
    while t < len(c):
        # 1) ordem armada em candles anteriores: aciona neste?
        if ordem is not None:
            d = ordem["d"]
            if (c[t][2] >= ordem["gatilho"]) if d == 1 else (c[t][3] <= ordem["gatilho"]):
                entrada = max(ordem["gatilho"], c[t][1]) if d == 1 else min(ordem["gatilho"], c[t][1])
                stop = ordem["stop"]
                ordem = None
                risco = (entrada - stop) * d
                if risco > 0:
                    alvo = entrada + d * ALVO_R * risco
                    saida = None
                    for q in range(t, len(c)):
                        hi, lo = c[q][2], c[q][3]
                        if ((lo <= stop) if d == 1 else (hi >= stop)) and \
                                (q > t or stop_vale_no_candle_entrada(c[t], d, entrada)):
                            saida, preco = q, (min(stop, c[q][1]) if d == 1 else max(stop, c[q][1]))
                            break
                        if q > t and ((hi >= alvo) if d == 1 else (lo <= alvo)):
                            saida, preco = q, max(alvo, c[q][1]) if d == 1 else min(alvo, c[q][1])
                            break
                    if saida is None:
                        saida, preco = len(c) - 1, c[-1][4]
                    bruto = (preco - entrada) * d / risco
                    custo_r = CUSTO_RT * entrada / risco
                    trades.append({"ts": c[t][0], "d": d, "r": bruto - custo_r, "bruto": bruto, "custo_r": custo_r})
                    t = saida + 1
                    continue
        # 2) fechamento do candle t: arma, desce, mantem ou cancela a ordem
        d = tend[t]
        if ordem is not None and d != ordem["d"]:
            ordem = None  # a media deixou de apontar a favor: cancela
        sinal_c = d == 1 and c[t][3] < min(c[t - 1][3], c[t - 2][3])
        sinal_v = d == -1 and c[t][2] > max(c[t - 1][2], c[t - 2][2])
        if sinal_c:
            ordem = {"d": 1, "gatilho": c[t][2], "stop": c[t][3]}
        elif sinal_v:
            ordem = {"d": -1, "gatilho": c[t][3], "stop": c[t][2]}
        elif ordem is not None and ordem_modo == "1-candle":
            ordem = None
        t += 1
    return trades


def rodar(universo, bar, modo, ordem_modo, dias=3000):
    todos, ts = [], []
    for inst in universo:
        c = serie(inst, bar, dias)
        if len(c) <= AQUECIMENTO + 10:
            continue
        ts += [c[0][0], c[-1][0]]
        todos += simular(c, modo, ordem_modo)
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
    print(f"  {'combinacao':<34} {'n':>5} {'exp liq':>8} {'bruto':>7} {'acerto':>6} | "
          f"{'n tr':>5} {'exp tr':>7} | {'n te':>5} {'exp te':>7}")
    celulas = []
    for bar in DECIDEM:
        for modo in TENDENCIAS:
            for om in ORDENS:
                tr, meio = rodar(UNIVERSO, bar, modo, om)
                treino = [x for x in tr if x["ts"] < meio]
                teste = [x for x in tr if x["ts"] >= meio]
                nome = f"{bar:<5} {modo:<7} {om}"
                print(f"  {nome:<34} {len(tr):>5} {media(tr):>+8.3f} {media(tr, 'bruto'):>+7.3f} "
                      f"{acerto(tr):>5.1f}% | {len(treino):>5} {media(treino):>+7.3f} | "
                      f"{len(teste):>5} {media(teste):>+7.3f}", flush=True)
                celulas.append((nome, bar, modo, om, treino, teste))
    print("\n  descritivo (fora da selecao):")
    for bar, dias in DESCRITIVOS:
        for modo in TENDENCIAS:
            for om in ORDENS:
                tr, _ = rodar(UNIVERSO, bar, modo, om, dias)
                print(f"  {bar + ' ' + modo + ' ' + om:<34} {len(tr):>5} {media(tr):>+8.3f} "
                      f"{media(tr, 'bruto'):>+7.3f} {acerto(tr):>5.1f}%  custo {media(tr, 'custo_r'):.3f}R")

    print(f"\n{'='*104}\nDECISAO\n{'='*104}")
    eleg = [x for x in celulas if len(x[4]) >= MIN_N_SELECAO]
    nome, bar, modo, om, treino, teste = max(eleg, key=lambda x: media(x[4]))
    print(f"  selecionada no treino -> {nome}")
    print(linha_ic("treino (1a metade, so referencia)", treino)[0])
    l1, ok1 = linha_ic("1) TESTE (2a metade)              ", teste)
    print(l1)
    print(linha_ic("   so compras (teste)             ", [x for x in teste if x["d"] == 1])[0])
    print(linha_ic("   so vendas (teste)              ", [x for x in teste if x["d"] == -1])[0])
    tr_b, _ = rodar(UNIVERSO_B, bar, modo, om)
    l2, ok2 = linha_ic("2) 80 PARES FORA DA AMOSTRA        ", tr_b)
    print(l2)
    print(linha_ic("   so compras (fora)              ", [x for x in tr_b if x["d"] == 1])[0])
    print(linha_ic("   so vendas (fora)               ", [x for x in tr_b if x["d"] == -1])[0])
    print(f"\n==> DECISAO: holdout {'ok' if ok1 else 'falhou'}, fora da amostra {'ok' if ok2 else 'falhou'}"
          f" -> {'PASSA' if ok1 and ok2 else 'NAO PASSA'}")


if __name__ == "__main__":
    main()
