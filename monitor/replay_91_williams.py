"""
Teste unico, PRE-REGISTRADO (22/09/2026), do "9.1 de Larry Williams" como
apresentado no video "Media movel de 9! Sistema de position e swing simples
e eficiente". Estudo avulso: NAO faz parte do checklist dos Setups A/B/C nem
do monitor de producao. Regras e criterio escritos ANTES de rodar qualquer
simulacao. [interp] = interpretacao minha (transcricao automatica ruim).

REGRAS -- COMPRA (venda e espelho exato)
----------------------------------------
- Media de 9 no fechamento (exponencial no original; aritmetica testada
  porque o video testa). "Virou para cima" no candle t: M[t] > M[t-1] e
  M[t-1] <= M[t-2].
- Entrada: compra stop na maxima do candle t que virou a media. Aciona no
  candle j > t se high[j] >= gatilho; preco = max(gatilho, open[j]).
  Cancela se a media virar para baixo antes de acionar [interp: o video nao
  diz; e a leitura usual do 9.1].
- Saida: quando a media vira para baixo num candle fechado, venda stop na
  minima desse candle; se a media virar de novo para cima antes de acionar,
  a saida e cancelada e a posicao segue. Aciona com preco = min(gatilho,
  open). So vale a partir do candle seguinte ao da virada (a virada so e
  conhecida no fechamento).
- Stop and reverse (o original): a mesma ordem que fecha a compra abre a
  venda ("se perder essa minima vai entrar vendido").

VARIACOES (as que o proprio video testa)
- Media: MME9 (original) ou MMA9.
- Stop: "sem" (original: so a saida pela virada) ou "minima": stop fixo na
  minima do candle que virou a media para cima (o candle de referencia da
  entrada). Stopado, fica fora ate a proxima virada. No candle da entrada so
  o stop pode ser atingido (conservador).
- Filtro: "nenhum" ou "mm50": so compra com a MMA50 subindo (MMA50[t] >
  MMA50[t-1]) no candle que virou a media [interp: aritmetica; o video diz
  "media de 50 virada para cima"]. Com filtro, o stop and reverse so reverte
  se o novo lado for permitido; se nao, a saida so zera a posicao.
[desvio] alvo fixo de 8% (citado de passagem) nao modelado.

MEDIDA
------
R = (saida - entrada) * lado / |entrada - minima do candle de referencia|,
ou seja, o stop que o plano de risco exigiria para dimensionar a posicao.
Na versao "sem" stop, uma perda pode passar de -1R -- e exatamente o que
aconteceria operando o original com tamanho calculado por esse stop.
Custo: 0.18% do nocional ida+volta convertido em R (igual aos outros estudos
avulsos). Descritivos: retorno % liquido por trade, so compras, so vendas.
Uma posicao por par; trades abertos no fim do historico sao descartados.

GRADE
-----
2 medias x 2 stops x 2 filtros = 8 combinacoes x 4 tempos graficos
(1H 300 dias; 4H 2000 dias; 1Dutc e 1Wutc 3000 dias) = 32 celulas.
O video cita 60 min e semanal como os melhores para seguidor de tendencia,
e o titulo fala em position e swing (semanal e diario).

DADOS
-----
OKX history-candles, universo de 20 pares de replay_ema_ribbon.py, cache
de replay_stoch_vwap.py. Primeiros 60 candles de cada serie so aquecem.

CRITERIO DE DECISAO (pre-registrado, mesmo protocolo do replay_stoch_vwap)
-------------------------------------------------------------------------
Holdout temporal: cada tempo grafico dividido no ponto medio do historico;
na PRIMEIRA metade escolhe-se a celula de maior expectancia liquida em R
(n >= 30 nessa metade); so ela e testada na SEGUNDA metade. PASSA se a
expectancia liquida la tiver IC95 inteiro acima de zero (bootstrap
reamostrando dias de entrada). Grade completa no log so como descritivo.
"""

import time

from replay_ema_ribbon import ic_bootstrap, CUSTO_RT, UNIVERSO
from replay_stoch_vwap import baixar, sma

MEDIAS = ["mme9", "mma9"]
STOPS = ["sem", "minima"]
FILTROS = ["nenhum", "mm50"]
TEMPOS = [("1H", 300), ("4H", 2000), ("1Dutc", 3000), ("1Wutc", 3000)]
AQUECIMENTO = 60
MIN_N_SELECAO = 30


def mme(v, n):
    k, e, out = 2 / (n + 1), v[0], []
    for x in v:
        e = x * k + e * (1 - k)
        out.append(e)
    return out


def viradas(M):
    """vr[t] = +1 virou pra cima, -1 virou pra baixo, 0 nada."""
    vr = [0] * len(M)
    for t in range(2, len(M)):
        if None in (M[t], M[t - 1], M[t - 2]):
            continue
        if M[t] > M[t - 1] and M[t - 1] <= M[t - 2]:
            vr[t] = 1
        elif M[t] < M[t - 1] and M[t - 1] >= M[t - 2]:
            vr[t] = -1
    return vr


def simular(c, media, stop_modo, filtro):
    closes = [x[4] for x in c]
    M = mme(closes, 9) if media == "mme9" else sma(closes, 9)
    vr = viradas(M)
    mm50 = sma(closes, 50)
    trades = []
    pos = None       # dict(d, entrada, ref, j, stop)
    ordem = None     # entrada pendente: dict(d, gatilho, ref)
    saida = None     # gatilho de saida/reversao da posicao aberta

    def permitido(d, t):
        if filtro == "nenhum":
            return True
        if mm50[t] is None or mm50[t - 1] is None:
            return False
        return (mm50[t] > mm50[t - 1]) if d == 1 else (mm50[t] < mm50[t - 1])

    def fechar(k, preco):
        d = pos["d"]
        risco = abs(pos["entrada"] - pos["ref"])
        custo_r = CUSTO_RT * pos["entrada"] / risco
        bruto = (preco - pos["entrada"]) * d / risco
        trades.append({"ts": c[pos["j"]][0], "j": pos["j"], "k": k, "d": d, "r": bruto - custo_r, "bruto": bruto,
                       "custo_r": custo_r, "pct": 100 * ((preco / pos["entrada"] - 1) * d - CUSTO_RT)})

    def abrir(k, d, preco, ref):
        if (preco - ref) * d <= 0:
            return None
        return {"d": d, "entrada": preco, "ref": ref, "j": k,
                "stop": ref if stop_modo == "minima" else None}

    for k in range(AQUECIMENTO, len(c)):
        o, hi, lo = c[k][1], c[k][2], c[k][3]

        # 1) ordens vindas de candles anteriores, na ordem em que o preco as encontraria
        if pos is not None:
            d = pos["d"]
            niveis = []
            if pos["stop"] is not None and ((lo <= pos["stop"]) if d == 1 else (hi >= pos["stop"])):
                niveis.append(("stop", pos["stop"]))
            if saida is not None and ((lo <= saida["gatilho"]) if d == 1 else (hi >= saida["gatilho"])):
                niveis.append(("saida", saida["gatilho"]))
            if niveis:
                # o preco caminha contra a posicao: encontra primeiro o nivel mais proximo
                tipo, nivel = max(niveis, key=lambda x: x[1] * d)
                preco = min(nivel, o) if d == 1 else max(nivel, o)
                fechar(k, preco)
                rev = saida if tipo == "saida" else None
                pos, saida = None, None
                if rev is not None and rev["permitido"]:
                    pos = abrir(k, -d, preco, rev["ref"])
                    # candle da entrada: so o stop pode ser atingido (conservador)
                    if pos and pos["stop"] is not None:
                        s = pos["stop"]
                        if (lo <= s) if pos["d"] == 1 else (hi >= s):
                            fechar(k, s)
                            pos = None
        elif ordem is not None:
            d = ordem["d"]
            if (hi >= ordem["gatilho"]) if d == 1 else (lo <= ordem["gatilho"]):
                preco = max(ordem["gatilho"], o) if d == 1 else min(ordem["gatilho"], o)
                pos = abrir(k, d, preco, ordem["ref"])
                ordem = None
                if pos and pos["stop"] is not None:
                    s = pos["stop"]
                    if (lo <= s) if d == 1 else (hi >= s):
                        fechar(k, s)
                        pos = None

        # 2) fechamento do candle k: viradas da media armam/cancelam ordens
        v = vr[k]
        if v == 0:
            continue
        if pos is not None:
            if v == -pos["d"]:
                # armar saida (e reversao) na minima/maxima do candle que virou
                gat = lo if pos["d"] == 1 else hi
                ref_novo = hi if pos["d"] == 1 else lo
                saida = {"gatilho": gat, "ref": ref_novo, "permitido": permitido(-pos["d"], k)}
            else:
                saida = None  # media voltou a favor: cancela a saida
        else:
            if permitido(v, k):
                ordem = {"d": v, "gatilho": hi if v == 1 else lo, "ref": lo if v == 1 else hi}
            else:
                ordem = None
    return trades


def combos():
    for me in MEDIAS:
        for st in STOPS:
            for fi in FILTROS:
                yield f"{me} stop={st} filtro={fi}", me, st, fi


def media(trades, chave="r"):
    return sum(x[chave] for x in trades) / len(trades) if trades else float("nan")


def linha_ic(rotulo, trades):
    if len(trades) < 3:
        return f"  {rotulo}: n={len(trades)} (insuficiente)", False
    lo, hi, dias = ic_bootstrap(trades, "r")
    acerto = sum(x["bruto"] > 0 for x in trades) / len(trades)
    return (f"  {rotulo}: n={len(trades):>5} | dias={dias:>5} | exp {media(trades):+.3f}R | "
            f"IC95 [{lo:+.3f}, {hi:+.3f}] | bruto {media(trades, 'bruto'):+.3f}R | "
            f"%/trade {media(trades, 'pct'):+.2f}% | acerto {100*acerto:.1f}% | "
            f"custo {media(trades, 'custo_r'):.3f}R"), lo > 0


def main():
    celulas = []
    for bar, dias in TEMPOS:
        print(f"\n{'='*100}\n{bar} ({dias} dias max)\n{'='*100}")
        res = {nome: [] for nome, *_ in combos()}
        ts_min = ts_max = None
        for inst in UNIVERSO:
            c = baixar(inst, bar, dias)
            if len(c) <= AQUECIMENTO + 10:
                print(f"    {inst:<16} candles={len(c):>6} (curto demais, ignorado)")
                continue
            ts_min = c[0][0] if ts_min is None else min(ts_min, c[0][0])
            ts_max = c[-1][0] if ts_max is None else max(ts_max, c[-1][0])
            n_par = 0
            for nome, me, st, fi in combos():
                tr = simular(c, me, st, fi)
                for x in tr:
                    x["par"] = inst
                res[nome] += tr
                n_par += len(tr)
            print(f"    {inst:<16} candles={len(c):>6} trades(todas as combinacoes)={n_par:>6}", flush=True)
        meio = (ts_min + ts_max) // 2
        print(f"  ponto medio do holdout: {time.strftime('%Y-%m-%d', time.gmtime(meio / 1000))}")
        print(f"  {'combinacao':<34} {'n':>5} {'exp liq':>8} {'bruto':>7} {'%/tr':>6} {'acerto':>6} | "
              f"{'n tr':>5} {'exp tr':>7} | {'n te':>5} {'exp te':>7}")
        for nome, tr in res.items():
            treino = [x for x in tr if x["ts"] < meio]
            teste = [x for x in tr if x["ts"] >= meio]
            acerto = 100 * sum(x["bruto"] > 0 for x in tr) / len(tr) if tr else float("nan")
            print(f"  {nome:<34} {len(tr):>5} {media(tr):>+8.3f} {media(tr, 'bruto'):>+7.3f} "
                  f"{media(tr, 'pct'):>+6.2f} {acerto:>5.1f}% | {len(treino):>5} {media(treino):>+7.3f} | "
                  f"{len(teste):>5} {media(teste):>+7.3f}")
            celulas.append((bar, nome, treino, teste))

    print(f"\n{'='*100}\nHOLDOUT -- DECIDE\n{'='*100}")
    elegiveis = [x for x in celulas if len(x[2]) >= MIN_N_SELECAO]
    if not elegiveis:
        print(f"  nenhuma celula com n >= {MIN_N_SELECAO} no treino")
        print("\n==> DECISAO: NAO PASSA")
        return
    bar, nome, treino, teste = max(elegiveis, key=lambda x: media(x[2]))
    print(f"  selecionada no treino -> {bar} | {nome}")
    print(linha_ic("treino (1a metade, so referencia)", treino)[0])
    linha, ok = linha_ic("TESTE (2a metade, decide)       ", teste)
    print(linha)
    print(linha_ic("so compras (teste)               ", [x for x in teste if x["d"] == 1])[0])
    print(linha_ic("so vendas (teste)                ", [x for x in teste if x["d"] == -1])[0])
    print(f"\n==> DECISAO: {'PASSA' if ok else 'NAO PASSA'}")


if __name__ == "__main__":
    main()
