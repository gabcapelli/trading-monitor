"""
Teste unico, PRE-REGISTRADO (22/09/2026), do "inside bar + estocastico lento"
do video "Como fazer swing trade? simples e objetivo! Inside bar e
estocastico" (acoes da B3). Estudo avulso: NAO faz parte do checklist dos
Setups A/B/C nem do monitor de producao. Regras e criterio escritos ANTES de
rodar qualquer simulacao. [interp] = interpretacao minha.

REGRAS -- COMPRA (venda e espelho exato)
----------------------------------------
- Inside bar no candle t: high[t] < high[t-1] e low[t] > low[t-1].
- Estocastico lento (%K suavizado) abaixo de 20 no fechamento de t.
- Contexto, duas variantes:
  "tendencia": MMA80 subindo (MMA80[t] > MMA80[t-1]) [interp: simples].
  "v15" (o "V15" do video, contra a tendencia, so no diario): t cai nos dias
    13-17 do mes (virada da quinzena) ou 29-3 (virada do mes) [interp:
    "dia 15 ou dia primeiro", com 2 dias de folga para cada lado] e o
    fechamento de t esta abaixo da abertura do dia-ancora anterior (1 ou 16)
    -- "caiu reto na primeira quinzena" [interp]. Sem filtro de media.
- Entrada: compra stop na maxima de t, valida so no candle t+1 [interp];
  preco = max(gatilho, open[t+1]).
- Stop: minima de t.
- Alvo (tres, testados na grade):
  "2R": entrada + 2x risco (o alvo do outro setup do mesmo video).
  "topo": maior maxima dos 20 candles antes de t [interp: "topo anterior"];
    se nao estiver acima da entrada, o sinal e descartado.
  "bollinger": banda superior de Bollinger(20, 2) do candle anterior, como
    ordem limite atualizada a cada candle.
- Candle da entrada ambiguo (aciona o gatilho E toca o stop): heuristica de
  caminho OHLC -- candle de alta vai O-L-H-C (a minima veio antes do gatilho:
  o stop nao vale ainda), candle de baixa vai O-H-L-C (entrou e foi stopado).
  Alvo nunca e contado no candle da entrada; stop e alvo no mesmo candle
  depois dele = stop. Por que nao a regra "conservadora" dos estudos 1-7
  (no candle da entrada, qualquer toque no stop = perda): com gatilho e stop
  a menos de 1 candle de distancia -- o caso do inside bar -- ela da -0.24R
  bruto num passeio aleatorio. Medido num caminho intra-candle de 48 passos
  (200 mil candles): a perda no candle da entrada e real em 67% dos casos
  ambiguos; a regra conservadora acerta 67%, a heuristica OHLC 79%.
- Uma posicao por par; trade aberto no fim do historico fechado no ultimo
  fechamento. Custo: 0.18% ida+volta convertido em R (igual aos outros).
[desvio] V15 intraday ("metade do dia") e V15 semanal ("semestre") nao
modelados: cripto nao tem pregao e o semestral daria poucos trades.

GRADE
-----
Estocastico (14,3,3), (8,3,3), (5,3,3) x alvo 2R/topo/bollinger x
{tendencia no 1Dutc, tendencia no 1Wutc, v15 no 1Dutc} = 27 celulas, 3000
dias, universo de 20 pares, cache de replay_stoch_vwap.py.
Descritivo: inside bar + estocastico SEM contexto nenhum, pra medir o que a
media e o calendario acrescentam.

CRITERIO DE DECISAO (pre-registrado)
------------------------------------
1. Holdout temporal (mesmo protocolo do replay_stoch_vwap): na 1a metade
   escolhe-se a celula de maior expectancia liquida em R (n >= 30); so ela e
   testada na 2a metade; precisa de IC95 inteiro acima de zero.
2. E, OBRIGATORIAMENTE, a mesma celula nos 80 pares fora da amostra de
   replay_91_beta.py (historico inteiro; semanal agregado do diario, semanas
   de segunda a domingo UTC) tambem com IC95 inteiro acima de zero.
PASSA so se 1 e 2 passarem.
"""

import time

from replay_ema_ribbon import ic_bootstrap, CUSTO_RT, UNIVERSO
from replay_stoch_vwap import baixar, sma, estocastico
from replay_91_beta import UNIVERSO_B

STOCHS = [(14, 3, 3), (8, 3, 3), (5, 3, 3)]
ALVOS = ["2R", "topo", "bollinger"]
CELULAS = [("tendencia", "1Dutc"), ("tendencia", "1Wutc"), ("v15", "1Dutc")]
MM_N = 80
AQUECIMENTO = 90
MIN_N_SELECAO = 30
MS_DIA = 86_400_000


def semanal(c1d):
    """Agrega diario em semanas de segunda a domingo UTC (1970-01-01 foi quinta)."""
    out, chave = [], None
    for x in c1d:
        k = (x[0] // MS_DIA + 3) // 7
        if k != chave:
            out.append(list(x))
            chave = k
        else:
            w = out[-1]
            w[2], w[3], w[4], w[5] = max(w[2], x[2]), min(w[3], x[3]), x[4], w[5] + x[5]
    return out[:-1]  # ultima semana pode estar incompleta


def bollinger_sup(closes, n=20, k=2.0):
    out = [None] * len(closes)
    for i in range(n - 1, len(closes)):
        j = closes[i - n + 1:i + 1]
        m = sum(j) / n
        out[i] = m + k * (sum((x - m) ** 2 for x in j) / n) ** 0.5
    return out


def bollinger_inf(closes, n=20, k=2.0):
    out = [None] * len(closes)
    for i in range(n - 1, len(closes)):
        j = closes[i - n + 1:i + 1]
        m = sum(j) / n
        out[i] = m - k * (sum((x - m) ** 2 for x in j) / n) ** 0.5
    return out


def contexto_v15(c, t, d):
    dia = time.gmtime(c[t][0] / 1000).tm_mday
    if not (13 <= dia <= 17 or dia >= 29 or dia <= 3):
        return False
    # dia-ancora anterior: o ultimo dia 1 ou 16 antes de t (no maximo 20 candles atras)
    for a in range(t - 1, max(t - 20, 0), -1):
        if time.gmtime(c[a][0] / 1000).tm_mday in (1, 16):
            return (c[t][4] < c[a][1]) if d == 1 else (c[t][4] > c[a][1])
    return False


def simular(c, st, alvo_modo, contexto):
    closes = [x[4] for x in c]
    k, _ = estocastico(c, *st)
    mm = sma(closes, MM_N)
    bs, bi = bollinger_sup(closes), bollinger_inf(closes)
    trades, t = [], AQUECIMENTO
    while t < len(c) - 1:
        if k[t] is None or not (c[t][2] < c[t - 1][2] and c[t][3] > c[t - 1][3]):
            t += 1
            continue
        d = 1 if k[t] < 20 else -1 if k[t] > 80 else 0
        if d == 0:
            t += 1
            continue
        if contexto == "tendencia":
            if mm[t] is None or mm[t - 1] is None or (mm[t] - mm[t - 1]) * d <= 0:
                t += 1
                continue
        elif contexto == "v15" and not contexto_v15(c, t, d):
            t += 1
            continue
        j = t + 1
        gat = c[t][2] if d == 1 else c[t][3]
        if not ((c[j][2] >= gat) if d == 1 else (c[j][3] <= gat)):
            t += 1
            continue
        entrada = max(gat, c[j][1]) if d == 1 else min(gat, c[j][1])
        stop = c[t][3] if d == 1 else c[t][2]
        risco = (entrada - stop) * d
        if risco <= 0:
            t += 1
            continue
        alvo_fixo = None
        if alvo_modo == "2R":
            alvo_fixo = entrada + 2 * d * risco
        elif alvo_modo == "topo":
            janela = c[max(t - 20, 0):t]
            alvo_fixo = max(x[2] for x in janela) if d == 1 else min(x[3] for x in janela)
            if (alvo_fixo - entrada) * d <= 0:
                t += 1
                continue
        saida = None
        for q in range(j, len(c)):
            hi, lo = c[q][2], c[q][3]
            if (lo <= stop) if d == 1 else (hi >= stop):
                a_favor = (c[q][4] >= c[q][1]) if d == 1 else (c[q][4] <= c[q][1])
                if not (q == j and a_favor):  # OHLC: no candle a favor o extremo contra veio antes do gatilho
                    preco = min(stop, c[q][1]) if d == 1 else max(stop, c[q][1])
                    saida = q
                    break
            if q == j:
                continue
            alvo = alvo_fixo if alvo_fixo is not None else (bs[q - 1] if d == 1 else bi[q - 1])
            if alvo is not None and ((hi >= alvo) if d == 1 else (lo <= alvo)):
                preco = max(alvo, c[q][1]) if d == 1 else min(alvo, c[q][1])
                saida = q
                break
        if saida is None:
            saida, preco = len(c) - 1, c[-1][4]
        bruto = (preco - entrada) * d / risco
        custo_r = CUSTO_RT * entrada / risco
        trades.append({"ts": c[j][0], "d": d, "r": bruto - custo_r, "bruto": bruto, "custo_r": custo_r})
        t = saida + 1
    return trades


def serie(inst, bar):
    c = baixar(inst, "1Dutc", 3000)
    return semanal(c) if bar == "1Wutc" else c


def combos():
    for ctx, bar in CELULAS:
        for st in STOCHS:
            for a in ALVOS:
                yield f"{ctx:<9} {bar:<5} st{st[0]}-{st[1]}-{st[2]} alvo={a}", ctx, bar, st, a


def media(trades, chave="r"):
    return sum(x[chave] for x in trades) / len(trades) if trades else float("nan")


def linha_ic(rotulo, trades):
    if len(trades) < 3:
        return f"  {rotulo}: n={len(trades)} (insuficiente)", False
    lo, hi, dias = ic_bootstrap(trades, "r")
    acerto = sum(x["bruto"] > 0 for x in trades) / len(trades)
    return (f"  {rotulo}: n={len(trades):>5} | dias={dias:>5} | exp {media(trades):+.3f}R | "
            f"IC95 [{lo:+.3f}, {hi:+.3f}] | bruto {media(trades, 'bruto'):+.3f}R | "
            f"acerto {100*acerto:.1f}% | custo {media(trades, 'custo_r'):.3f}R"), lo > 0


def rodar_celula(universo, ctx, bar, st, a):
    todos, ts = [], []
    for inst in universo:
        c = serie(inst, bar)
        if len(c) <= AQUECIMENTO + 10:
            continue
        ts += [c[0][0], c[-1][0]]
        todos += simular(c, st, a, ctx)
    return todos, (min(ts) + max(ts)) // 2 if ts else 0


def main():
    print(f"{'='*104}\nUNIVERSO A (20 pares) -- grade\n{'='*104}")
    print(f"  {'combinacao':<40} {'n':>5} {'exp liq':>8} {'bruto':>7} {'acerto':>6} | "
          f"{'n tr':>5} {'exp tr':>7} | {'n te':>5} {'exp te':>7}")
    celulas = []
    for nome, ctx, bar, st, a in combos():
        tr, meio = rodar_celula(UNIVERSO, ctx, bar, st, a)
        treino = [x for x in tr if x["ts"] < meio]
        teste = [x for x in tr if x["ts"] >= meio]
        acerto = 100 * sum(x["bruto"] > 0 for x in tr) / len(tr) if tr else float("nan")
        print(f"  {nome:<40} {len(tr):>5} {media(tr):>+8.3f} {media(tr, 'bruto'):>+7.3f} {acerto:>5.1f}% | "
              f"{len(treino):>5} {media(treino):>+7.3f} | {len(teste):>5} {media(teste):>+7.3f}", flush=True)
        celulas.append((nome, ctx, bar, st, a, treino, teste))
    print("\n  descritivo -- inside bar + estocastico SEM contexto:")
    for bar in ("1Dutc", "1Wutc"):
        for a in ALVOS:
            tr, _ = rodar_celula(UNIVERSO, "nenhum", bar, (14, 3, 3), a)
            print(f"  {'nenhum    ' + bar + ' st14-3-3 alvo=' + a:<40} {len(tr):>5} {media(tr):>+8.3f} "
                  f"{media(tr, 'bruto'):>+7.3f}")

    print(f"\n{'='*104}\nDECISAO\n{'='*104}")
    eleg = [x for x in celulas if len(x[5]) >= MIN_N_SELECAO]
    nome, ctx, bar, st, a, treino, teste = max(eleg, key=lambda x: media(x[5]))
    print(f"  selecionada no treino -> {nome}")
    print(linha_ic("treino (1a metade, so referencia)", treino)[0])
    l1, ok1 = linha_ic("1) TESTE (2a metade)              ", teste)
    print(l1)
    tr_b, _ = rodar_celula(UNIVERSO_B, ctx, bar, st, a)
    l2, ok2 = linha_ic("2) 80 PARES FORA DA AMOSTRA        ", tr_b)
    print(l2)
    print(f"\n==> DECISAO: holdout {'ok' if ok1 else 'falhou'}, fora da amostra {'ok' if ok2 else 'falhou'}"
          f" -> {'PASSA' if ok1 and ok2 else 'NAO PASSA'}")


if __name__ == "__main__":
    main()
