"""
Teste unico, PRE-REGISTRADO (22/09/2026), do "123" de tres candles do video
"Como operar o 123 -- Criptos, Indice, dolar e acoes". NAO e o 1-2-3 de Mark
Crisp (replay_123_crisp.py, movimentos de varios candles): aqui o padrao tem
exatamente 3 candles. Estudo avulso: NAO faz parte do checklist dos Setups
A/B/C nem do monitor de producao. Regras e criterio escritos ANTES de rodar
qualquer simulacao. [interp] = interpretacao minha.

REGRAS -- COMPRA (venda e espelho exato)
----------------------------------------
- Padrao nos candles t-2, t-1, t (1, 2, 3): low[t-1] < low[t-2] e
  low[t-1] < low[t] ("minima, minima mais baixa, minima mais alta").
- Entrada: compra stop na maxima do candle 3, valida so no candle t+1
  [interp]; preco = max(gatilho, open[t+1]).
- Amplitude = maior maxima - menor minima dos 3 candles.
- Stop (as tres opcoes do video, na grade):
  "c3": minima do candle 3 (melhor payoff, menor acerto).
  "c2": minima do candle 2 (a mais baixa do padrao).
  "amplo": minima do candle 2 menos a amplitude ("a amplitude inteira do
    conjunto projetada").
- Alvo: entrada + k x amplitude, k = 1.0 ou 1.618 ("em 161") [interp: nao
  fica claro se o alvo e a amplitude ou 161% dela; as duas na grade].
- Contexto (o ponto central do video; duas leituras, na grade):
  "tendencia": MME80 subindo e fechamento do candle 3 acima dela [interp:
    "numa tendencia de alta"; 123 de compra em tendencia de baixa e
    descartado].
  "tendencia+mm8": o anterior E MME8 subindo com os 3 candles fechando
    acima dela (o "123 fantastico"; entre a MM8 e a MM80 e a "zona neutra").
  [interp: exponenciais; o video nao diz]
  [desvio] "nao gosto quando o candle 3 e muito grande" e preferencia, nao
  regra -- nao modelado.
- Candle da entrada: toque no stop resolvido pela heuristica OHLC
  (stop_vale_no_candle_entrada); alvo nunca conta nele; stop e alvo no mesmo
  candle depois dele = stop.
- Uma posicao por par; trade aberto no fim fechado no ultimo fechamento.
  Custo: 0.18% ida+volta em R.

GRADE
-----
2 contextos x 3 stops x 2 alvos = 12 combinacoes, em 1Dutc (3000 dias) e 4H
(2000 dias) = 24 celulas, 20 pares. Descritivo: 1H (300 dias) e 1W (semanal
agregado do diario).

CRITERIO DE DECISAO (pre-registrado; protocolo de estudos-avulsos.md)
--------------------------------------------------------------------
1. Holdout temporal: na 1a metade escolhe-se a celula de maior expectancia
   liquida em R entre as com n >= 200 no treino; so ela e testada na 2a
   metade; IC95 inteiro acima de zero. Nenhuma celula com n >= 200 ->
   "sem amostra para decidir".
2. E a mesma celula nos 80 pares fora da amostra (replay_91_beta.UNIVERSO_B,
   historico inteiro; se a celula for 4H, baixa-se o 4H de 2000 dias desses
   pares), IC95 inteiro acima de zero.
PASSA so se 1 e 2 passarem.
"""

from replay_ema_ribbon import ic_bootstrap, CUSTO_RT, UNIVERSO, stop_vale_no_candle_entrada
from replay_stoch_vwap import baixar
from replay_91_williams import mme
from replay_inside_bar import semanal
from replay_91_beta import UNIVERSO_B

CONTEXTOS = ["tendencia", "tendencia+mm8"]
STOPS = ["c3", "c2", "amplo"]
ALVOS = [1.0, 1.618]
DECIDEM = [("1Dutc", 3000), ("4H", 2000)]
DESCRITIVOS = [("1H", 300), ("1W", 3000)]
AQUECIMENTO = 100
MIN_N_SELECAO = 200


def serie(inst, bar, dias):
    if bar == "1W":
        return semanal(baixar(inst, "1Dutc", 3000))
    return baixar(inst, bar, dias)


def simular(c, contexto, stop_modo, k_alvo):
    closes = [x[4] for x in c]
    m8, m80 = mme(closes, 8), mme(closes, 80)
    trades, t = [], AQUECIMENTO
    while t < len(c) - 1:
        c1, c2, c3 = c[t - 2], c[t - 1], c[t]
        if c2[3] < c1[3] and c2[3] < c3[3]:
            d = 1
        elif c2[2] > c1[2] and c2[2] > c3[2]:
            d = -1
        else:
            t += 1
            continue
        ok = (m80[t] - m80[t - 1]) * d > 0 and (c3[4] - m80[t]) * d > 0
        if ok and contexto == "tendencia+mm8":
            ok = (m8[t] - m8[t - 1]) * d > 0 and all((c[i][4] - m8[i]) * d > 0 for i in (t - 2, t - 1, t))
        if not ok:
            t += 1
            continue
        j = t + 1
        gat = c3[2] if d == 1 else c3[3]
        if not ((c[j][2] >= gat) if d == 1 else (c[j][3] <= gat)):
            t += 1
            continue
        entrada = max(gat, c[j][1]) if d == 1 else min(gat, c[j][1])
        amp = max(x[2] for x in (c1, c2, c3)) - min(x[3] for x in (c1, c2, c3))
        extremo2 = c2[3] if d == 1 else c2[2]
        stop = {"c3": c3[3] if d == 1 else c3[2], "c2": extremo2, "amplo": extremo2 - d * amp}[stop_modo]
        risco = (entrada - stop) * d
        if risco <= 0 or amp <= 0:
            t += 1
            continue
        alvo = entrada + d * k_alvo * amp
        saida = None
        for q in range(j, len(c)):
            hi, lo = c[q][2], c[q][3]
            if ((lo <= stop) if d == 1 else (hi >= stop)) and (q > j or stop_vale_no_candle_entrada(c[j], d, entrada)):
                saida, preco = q, (min(stop, c[q][1]) if d == 1 else max(stop, c[q][1]))
                break
            if q > j and ((hi >= alvo) if d == 1 else (lo <= alvo)):
                saida, preco = q, (max(alvo, c[q][1]) if d == 1 else min(alvo, c[q][1]))
                break
        if saida is None:
            saida, preco = len(c) - 1, c[-1][4]
        bruto = (preco - entrada) * d / risco
        custo_r = CUSTO_RT * entrada / risco
        trades.append({"ts": c[j][0], "d": d, "r": bruto - custo_r, "bruto": bruto, "custo_r": custo_r})
        t = saida + 1
    return trades


def rodar(universo, bar, dias, ctx, st, k):
    todos, ts = [], []
    for inst in universo:
        c = serie(inst, bar, dias)
        if len(c) <= AQUECIMENTO + 10:
            continue
        ts += [c[0][0], c[-1][0]]
        todos += simular(c, ctx, st, k)
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


def combos():
    for ctx in CONTEXTOS:
        for st in STOPS:
            for k in ALVOS:
                yield ctx, st, k


def main():
    print(f"{'='*108}\nUNIVERSO A (20 pares) -- grade\n{'='*108}")
    print(f"  {'combinacao':<40} {'n':>6} {'exp liq':>8} {'bruto':>7} {'acerto':>6} {'custo':>6} | "
          f"{'n tr':>5} {'exp tr':>7} | {'n te':>5} {'exp te':>7}")
    celulas = []
    for bar, dias in DECIDEM:
        for ctx, st, k in combos():
            tr, meio = rodar(UNIVERSO, bar, dias, ctx, st, k)
            treino = [x for x in tr if x["ts"] < meio]
            teste = [x for x in tr if x["ts"] >= meio]
            nome = f"{bar:<5} {ctx:<13} stop={st:<5} alvo={k:g}x"
            print(f"  {nome:<40} {len(tr):>6} {media(tr):>+8.3f} {media(tr, 'bruto'):>+7.3f} {acerto(tr):>5.1f}% "
                  f"{media(tr, 'custo_r'):>6.3f} | {len(treino):>5} {media(treino):>+7.3f} | "
                  f"{len(teste):>5} {media(teste):>+7.3f}", flush=True)
            celulas.append((nome, bar, dias, ctx, st, k, treino, teste))
    print("\n  descritivo (fora da selecao):")
    for bar, dias in DESCRITIVOS:
        for ctx, st, k in combos():
            tr, _ = rodar(UNIVERSO, bar, dias, ctx, st, k)
            nome = f"{bar:<5} {ctx:<13} stop={st:<5} alvo={k:g}x"
            print(f"  {nome:<40} {len(tr):>6} {media(tr):>+8.3f} {media(tr, 'bruto'):>+7.3f} {acerto(tr):>5.1f}% "
                  f"{media(tr, 'custo_r'):>6.3f}", flush=True)

    print(f"\n{'='*108}\nDECISAO\n{'='*108}")
    eleg = [x for x in celulas if len(x[6]) >= MIN_N_SELECAO]
    if not eleg:
        print(f"  nenhuma celula com n >= {MIN_N_SELECAO} no treino -> SEM AMOSTRA PARA DECIDIR")
        return
    nome, bar, dias, ctx, st, k, treino, teste = max(eleg, key=lambda x: media(x[6]))
    print(f"  selecionada no treino -> {nome}   ({len(eleg)} de {len(celulas)} celulas com n >= {MIN_N_SELECAO})")
    print(linha_ic("treino (1a metade, so referencia)", treino)[0])
    l1, ok1 = linha_ic("1) TESTE (2a metade)              ", teste)
    print(l1)
    print(linha_ic("   so compras (teste)             ", [x for x in teste if x["d"] == 1])[0])
    print(linha_ic("   so vendas (teste)              ", [x for x in teste if x["d"] == -1])[0])
    tr_b, _ = rodar(UNIVERSO_B, bar, dias, ctx, st, k)
    l2, ok2 = linha_ic("2) 80 PARES FORA DA AMOSTRA        ", tr_b)
    print(l2)
    print(linha_ic("   so compras (fora)              ", [x for x in tr_b if x["d"] == 1])[0])
    print(linha_ic("   so vendas (fora)               ", [x for x in tr_b if x["d"] == -1])[0])
    print(f"\n==> DECISAO: holdout {'ok' if ok1 else 'falhou'}, fora da amostra {'ok' if ok2 else 'falhou'}"
          f" -> {'PASSA' if ok1 and ok2 else 'NAO PASSA'}")


if __name__ == "__main__":
    main()
