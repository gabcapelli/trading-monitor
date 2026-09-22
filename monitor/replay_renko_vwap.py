"""
Teste unico, PRE-REGISTRADO (22/09/2026), do setup Renko + VWAP do video
"Um dos melhores sistemas de Daytrade: Renko! Como operar?" (dolar futuro da
B3). Estudo avulso: NAO faz parte do checklist dos Setups A/B/C nem do
monitor de producao. Regras e criterio escritos ANTES de rodar qualquer
simulacao. [interp] = interpretacao minha. O video e quase todo um relato de
dia de operacoes; o setup Renko ocupa ~2 minutos (14:20-16:30) e deixa em
aberto o tamanho do tijolo e o que e "engolfar" num Renko.

REGRAS -- COMPRA (venda e espelho exato)
----------------------------------------
- Renko percentual [interp: o "12 R" do dolar nao tem traducao]: niveis
  geometricos P0*(1+b)^n; tijolos construidos pelo FECHAMENTO de cada candle
  de 5m [interp: sem dado de tick; tijolo grande em relacao ao 5m torna a
  aproximacao aceitavel]. Continuacao = 1 nivel; reversao = 2 niveis
  (Renko classico). Um candle pode formar varios tijolos.
- VWAP ancorada no dia UTC, igual ao replay_stoch_vwap (volume em moeda base);
  sinais so a partir da 2a hora do dia UTC.
- Sinal: tijolo de baixa cuja faixa [base, topo] contem a VWAP do candle que
  o formou ("preto encostando na VWAP"), seguido IMEDIATAMENTE de um tijolo
  de reversao de alta ("engolfado pelo branco") [interp: no Renko classico o
  tijolo de reversao nao sobrepoe o anterior; a reversao e a leitura mais
  proxima].
- Entrada: fechamento do candle de 5m que completou o tijolo de reversao
  [interp: "entrada nessa altura"; o fechamento pode ficar acima do nivel,
  e o preco que se consegue de fato].
- Stop: base do tijolo de baixa ("stop nessa minima").
- Alvo: amplitude do padrao (topo do tijolo de reversao - base do tijolo de
  baixa) projetada da entrada, em 1x (a parcial do video) ou 1.618x (a
  expansao "161" que ele usa o video inteiro). [desvio] saida parcial +
  conducao do resto nao modelada: cada celula usa um alvo so.
- Stop e alvo avaliados nas maximas/minimas reais dos candles de 5m seguintes;
  stop e alvo no mesmo candle = stop.
- Uma posicao por par por vez. Trade aberto no fim do historico: fechado no
  ultimo fechamento.
- Custo: 0.18% do nocional ida+volta convertido em R (igual aos outros).

GRADE
-----
Tijolo 0.3%, 0.5%, 1.0% x alvo 1.0 / 1.618 = 6 celulas, 5m de 300 dias,
universo de 20 pares, cache de replay_stoch_vwap.py.
Descritivo: o mesmo padrao SEM a condicao da VWAP (qualquer reversao apos
tijolo de baixa), pra ver se a VWAP acrescenta alguma coisa.

CRITERIO DE DECISAO (pre-registrado, mesmo protocolo do replay_stoch_vwap)
-------------------------------------------------------------------------
Holdout temporal no ponto medio; na 1a metade escolhe-se a celula de maior
expectancia liquida em R (n >= 30); so ela e testada na 2a metade. PASSA se
o IC95 la ficar inteiro acima de zero. Grade completa so como descritivo.
"""

import math
import time

from replay_ema_ribbon import ic_bootstrap, CUSTO_RT, UNIVERSO
from replay_stoch_vwap import baixar, vwap_bandas, MS_DIA, MS_HORA

TIJOLOS = [0.003, 0.005, 0.010]
ALVOS = [1.0, 1.618]
MIN_N_SELECAO = 30


def renko(c, b):
    """Tijolos (t_candle, d, base, topo) a partir dos fechamentos."""
    lb = math.log(1 + b)
    ref = math.log(c[0][4])
    nivel = lambda n: math.exp(ref + n * lb)
    tijolos = []
    topo_n = base_n = 0  # indices do ultimo tijolo (ainda nenhum)
    d = 0
    for t, x in enumerate(c):
        n = (math.log(x[4]) - ref) / lb
        while True:
            if d >= 0 and n >= topo_n + 1:          # continuacao de alta (ou primeiro)
                base_n, topo_n, d = topo_n, topo_n + 1, 1
            elif d <= 0 and n <= base_n - 1:        # continuacao de baixa (ou primeiro)
                base_n, topo_n, d = base_n - 1, base_n, -1
            elif d == 1 and n <= base_n - 1:        # reversao para baixo
                base_n, topo_n, d = base_n - 1, base_n, -1
            elif d == -1 and n >= topo_n + 1:       # reversao para cima
                base_n, topo_n, d = topo_n, topo_n + 1, 1
            else:
                break
            tijolos.append((t, d, nivel(base_n), nivel(topo_n)))
    return tijolos


def sinais(c, tij, vw, usar_vwap):
    out = []
    for i in range(1, len(tij)):
        t0, d0, b0, s0 = tij[i - 1]
        t1, d1, b1, s1 = tij[i]
        if d1 != -d0 or d0 == 0:
            continue
        if (c[t1][0] % MS_DIA) < MS_HORA or vw[t0] is None:
            continue
        if usar_vwap and not (b0 <= vw[t0] <= s0):
            continue
        d = d1
        # compra: stop na base do tijolo de baixa, amplitude ate o topo da reversao
        stop = b0 if d == 1 else s0
        extremo = s1 if d == 1 else b1
        out.append({"t": t1, "d": d, "stop": stop, "amp": abs(extremo - stop)})
    return out


def resolver(c, sin, alvo_mult):
    trades, livre = [], 0
    for s in sin:
        t, d = s["t"], s["d"]
        if t < livre or t + 1 >= len(c):
            continue
        entrada = c[t][4]
        risco = (entrada - s["stop"]) * d
        if risco <= 0:
            continue
        alvo = entrada + d * alvo_mult * s["amp"]
        saida = None
        for k in range(t + 1, len(c)):
            hi, lo = c[k][2], c[k][3]
            if (lo <= s["stop"]) if d == 1 else (hi >= s["stop"]):
                saida, preco = k, (min(s["stop"], c[k][1]) if d == 1 else max(s["stop"], c[k][1]))
                break
            if (hi >= alvo) if d == 1 else (lo <= alvo):
                saida, preco = k, alvo
                break
        if saida is None:
            saida, preco = len(c) - 1, c[-1][4]
        bruto = (preco - entrada) * d / risco
        custo_r = CUSTO_RT * entrada / risco
        trades.append({"ts": c[t][0], "d": d, "r": bruto - custo_r, "bruto": bruto, "custo_r": custo_r})
        livre = saida + 1
    return trades


def media(trades, chave="r"):
    return sum(x[chave] for x in trades) / len(trades) if trades else float("nan")


def linha_ic(rotulo, trades):
    if len(trades) < 3:
        return f"  {rotulo}: n={len(trades)} (insuficiente)", False
    lo, hi, dias = ic_bootstrap(trades, "r")
    acerto = sum(x["bruto"] > 0 for x in trades) / len(trades)
    return (f"  {rotulo}: n={len(trades):>5} | dias={dias:>4} | exp {media(trades):+.3f}R | "
            f"IC95 [{lo:+.3f}, {hi:+.3f}] | bruto {media(trades, 'bruto'):+.3f}R | "
            f"acerto {100*acerto:.1f}% | custo {media(trades, 'custo_r'):.3f}R"), lo > 0


def main():
    res = {}
    ts_min = ts_max = None
    print(f"{'='*100}\n5m (300 dias) -- Renko percentual + VWAP diaria UTC\n{'='*100}")
    for inst in UNIVERSO:
        c = baixar(inst, "5m", 300)
        ts_min = c[0][0] if ts_min is None else min(ts_min, c[0][0])
        ts_max = c[-1][0] if ts_max is None else max(ts_max, c[-1][0])
        vw, _ = vwap_bandas(c)
        n_par = 0
        for b in TIJOLOS:
            tij = renko(c, b)
            for usar_vwap in (True, False):
                sin = sinais(c, tij, vw, usar_vwap)
                for a in ALVOS:
                    nome = f"tijolo {100*b:.1f}% alvo {a:g}x{'' if usar_vwap else ' SEM VWAP (descr.)'}"
                    tr = resolver(c, sin, a)
                    res.setdefault(nome, []).extend(tr)
                    n_par += len(tr)
        print(f"    {inst:<16} candles={len(c):>6} trades(todas)={n_par:>6}", flush=True)
    meio = (ts_min + ts_max) // 2
    print(f"  ponto medio do holdout: {time.strftime('%Y-%m-%d', time.gmtime(meio / 1000))}")
    print(f"  {'combinacao':<38} {'n':>6} {'exp liq':>8} {'bruto':>7} {'custo':>6} {'acerto':>6} | "
          f"{'n tr':>5} {'exp tr':>7} | {'n te':>5} {'exp te':>7}")
    celulas = []
    for nome, tr in res.items():
        treino = [x for x in tr if x["ts"] < meio]
        teste = [x for x in tr if x["ts"] >= meio]
        acerto = 100 * sum(x["bruto"] > 0 for x in tr) / len(tr) if tr else float("nan")
        print(f"  {nome:<38} {len(tr):>6} {media(tr):>+8.3f} {media(tr, 'bruto'):>+7.3f} "
              f"{media(tr, 'custo_r'):>6.3f} {acerto:>5.1f}% | {len(treino):>5} {media(treino):>+7.3f} | "
              f"{len(teste):>5} {media(teste):>+7.3f}")
        if "SEM VWAP" not in nome:
            celulas.append((nome, treino, teste))

    print(f"\n{'='*100}\nHOLDOUT -- DECIDE\n{'='*100}")
    eleg = [x for x in celulas if len(x[1]) >= MIN_N_SELECAO]
    nome, treino, teste = max(eleg, key=lambda x: media(x[1]))
    print(f"  selecionada no treino -> {nome}")
    print(linha_ic("treino (1a metade, so referencia)", treino)[0])
    linha, ok = linha_ic("TESTE (2a metade, decide)       ", teste)
    print(linha)
    print(linha_ic("so compras (teste)               ", [x for x in teste if x["d"] == 1])[0])
    print(linha_ic("so vendas (teste)                ", [x for x in teste if x["d"] == -1])[0])
    print(f"\n==> DECISAO: {'PASSA' if ok else 'NAO PASSA'}")


if __name__ == "__main__":
    main()
