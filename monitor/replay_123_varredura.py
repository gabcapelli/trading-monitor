"""
Varredura EXPLORATORIA de parametros do 1-2-3 de Mark Crisp no diario,
PRE-REGISTRADA em 22/09/2026, com validacao do vencedor numa amostra nova
(universo D, so Binance). Estudo avulso: NAO faz parte do checklist dos
Setups A/B/C nem do monitor de producao.

POR QUE ISTO E DIFERENTE DOS OUTROS ESTUDOS
--------------------------------------------
Os estudos 1-12 nao varrem parametros de proposito: com n~2600 e erro padrao
~0.042R, a melhor de N variacoes aparece ~2 erros padrao acima por puro
acaso. Aqui a varredura e feita de propria vontade e assumida como
EXPLORATORIA: o numero da varredura NAO e evidencia de nada. Quem decide e
so a amostra nova.
Historico do projeto que justifica a cautela: V15 do inside bar +0.197R no
treino -> -0.150R fora; 9.1 +0.394R -> +0.115R; Landry +0.338R -> -0.122R.

VARREDURA (universo A, 20 pares OKX, 1Dutc, historico inteiro)
--------------------------------------------------------------
Dimensoes (todas ja citadas no video ou no proprio setup; nenhuma inventada
para caber nos dados):
- MIN_MOV1: 2 ou 3 fechamentos seguidos no movimento 1 (o video nao da
  minimo).
- stop: fundo 3 (preferido pelo autor) ou fundo 1 (a outra opcao dele).
- alvo: 1.0x, 1.5x ou 2.0x a amplitude fundo 1 -> topo 2.
- filtro de tendencia: nenhum, MMA80 a favor, ou MME21 a favor.
= 2 x 2 x 3 x 3 = 36 celulas. Vencedora = maior expectancia liquida em R,
entre as com n >= 200.

VALIDACAO (universo D, amostra nova, DECIDE)
--------------------------------------------
Universo D: os 215 perpetuos USDT-M da Binance que NAO existem na OKX (fora
de A, B e C) e estao listados ha >= 400 dias em 22/09/2026 (lista congelada
em universo_d.txt antes de baixar precos). Os *mesmos* pares na Binance nao
serviriam: seriam o mesmo mercado no mesmo periodo.
Criterio, fixado ANTES de rodar:
1. A celula vencedora precisa de IC95 inteiro acima de zero no universo D
   (bootstrap reamostrando dias de entrada). Teste unico -- a correcao por
   multiplicidade e a propria amostra nova.
2. E precisa superar a regra ORIGINAL (MIN_MOV1=2, stop fundo 3, alvo 1.0x,
   sem filtro) no mesmo universo D. Se a original for igual ou melhor, a
   varredura nao achou nada: o ganho era ruido.
PASSA so se 1 e 2 valerem. O custo e o mesmo do estudo 12 (taker na entrada
e no stop, maker no alvo) e a regra do candle de entrada e a OHLC.
"""

import os
import sys

from replay_ema_ribbon import ic_bootstrap, CUSTO_RT, UNIVERSO, stop_vale_no_candle_entrada
from replay_stoch_vwap import baixar as baixar_okx, sma
from replay_91_williams import mme
from replay_123_carteira import TAKER, MAKER, SLIPPAGE, MIN_CANDLES
import dados_binance

MIN_MOV1S = [2, 3]
STOPS = ["fundo3", "fundo1"]
ALVOS = [1.0, 1.5, 2.0]
FILTROS = ["nenhum", "mma80", "mme21"]
ORIGINAL = (2, "fundo3", 1.0, "nenhum")
MIN_N = 200
AQUECIMENTO = 90


def universo_d():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "universo_d.txt")) as f:
        return f.read().split()


def candidatos(c, d, min_mov1, k_alvo):
    """Setups 1-2-3 na direcao d. Mesma maquina de estados do replay_123_crisp,
    com minimo do movimento 1 e multiplo do alvo parametrizados."""
    if d == 1:
        o = [x[1] for x in c]; h = [x[2] for x in c]; lo = [x[3] for x in c]; cl = [x[4] for x in c]
    else:
        o = [-x[1] for x in c]; h = [-x[3] for x in c]; lo = [-x[2] for x in c]; cl = [-x[4] for x in c]
    out = []
    estado, run, ini_run = 0, 0, None
    fundo1 = topo2 = gatilho = ini_mov3 = None
    for t in range(1, len(c)):
        sobe, desce = cl[t] > cl[t - 1], cl[t] < cl[t - 1]
        if estado in (3, 4):
            if h[t] >= gatilho:
                entrada = max(gatilho, o[t])
                fundo3 = min(lo[ini_mov3:t])
                out.append({"j": t, "entrada": entrada, "fundo3": fundo3, "fundo1": fundo1,
                            "alvo": entrada + k_alvo * (topo2 - fundo1)})
                estado, run = 0, 0
                continue
            if cl[t] < fundo1:
                estado, run, ini_run = 0, 1, t
                continue
            if sobe:
                gatilho, estado = h[t], 4
            continue
        if estado == 0:
            if desce:
                if run == 0:
                    ini_run = t
                run += 1
            elif sobe:
                if run >= min_mov1:
                    fundo1, topo2, estado = min(lo[ini_run:t + 1]), h[t], 2
                run = 0
            continue
        if estado == 2:
            if sobe:
                topo2 = max(topo2, h[t])
            elif desce:
                if cl[t] < fundo1:
                    estado, run, ini_run = 0, 1, t
                    continue
                estado, gatilho, ini_mov3 = 3, topo2, t
    if d == -1:
        for x in out:
            for k in ("entrada", "fundo3", "fundo1", "alvo"):
                x[k] = -x[k]
    for x in out:
        x["d"] = d
    return out


def simular(c, min_mov1, stop_modo, k_alvo, filtro):
    closes = [x[4] for x in c]
    m80, m21 = sma(closes, 80), mme(closes, 21)
    cand = candidatos(c, 1, min_mov1, k_alvo) + candidatos(c, -1, min_mov1, k_alvo)
    trades, livre = [], AQUECIMENTO
    for s in sorted(cand, key=lambda x: x["j"]):
        j, d, entrada, alvo = s["j"], s["d"], s["entrada"], s["alvo"]
        stop = s[stop_modo]
        if j < livre or j >= len(c):
            continue
        if filtro == "mma80" and (m80[j - 1] is None or (m80[j - 1] - m80[j - 2]) * d <= 0):
            continue
        if filtro == "mme21" and (m21[j - 1] - m21[j - 2]) * d <= 0:
            continue
        risco = (entrada - stop) * d
        if risco <= 0 or (alvo - entrada) * d <= 0:
            continue
        rr = (alvo - entrada) * d / risco
        saida = None
        for t in range(j, len(c)):
            hi, lo = c[t][2], c[t][3]
            if ((lo <= stop) if d == 1 else (hi >= stop)) and \
                    (t > j or stop_vale_no_candle_entrada(c[j], d, entrada)):
                saida, r, no_alvo = t, -1.0, False
                break
            if t > j and ((hi >= alvo) if d == 1 else (lo <= alvo)):
                saida, r, no_alvo = t, rr, True
                break
        if saida is None:
            break
        custo_frac = (TAKER + SLIPPAGE) + (MAKER if no_alvo else TAKER + SLIPPAGE)
        custo_r = custo_frac * entrada / risco
        trades.append({"ts": c[j][0], "d": d, "r": r - custo_r, "bruto": r, "rr": rr, "custo_r": custo_r,
                       "j": j, "k": saida, "dur": saida - j,
                       "bruto_pct": 100 * r * risco / entrada,
                       "pct": 100 * (r * risco / entrada - custo_frac)})
        livre = saida + 1
    return trades


def rodar(universo, params, binance=False):
    todos = []
    for inst in universo:
        c = dados_binance.baixar(inst, "1Dutc", 3000) if binance else baixar_okx(inst, "1Dutc", 3000)
        if len(c) < MIN_CANDLES:
            continue
        todos += simular(c, *params)
    return todos


def media(trades, chave="r"):
    return sum(x[chave] for x in trades) / len(trades) if trades else float("nan")


def acerto(trades):
    return 100 * sum(x["bruto"] > 0 for x in trades) / len(trades) if trades else float("nan")


def linha_ic(rotulo, trades):
    if len(trades) < 3:
        return f"  {rotulo}: n={len(trades)} (insuficiente)", False
    lo, hi, dias = ic_bootstrap(trades, "r")
    return (f"  {rotulo}: n={len(trades):>5} | dias={dias:>5} | exp {media(trades):+.3f}R | "
            f"IC95 [{lo:+.3f}, {hi:+.3f}] | acerto {acerto(trades):.1f}% | "
            f"custo {media(trades, 'custo_r'):.3f}R"), lo > 0


def combos():
    for mm in MIN_MOV1S:
        for st in STOPS:
            for a in ALVOS:
                for f in FILTROS:
                    yield (mm, st, a, f)


def nome(p):
    return f"mov1>={p[0]} {p[1]:<6} alvo={p[2]:g}x filtro={p[3]}"


def main():
    if "--baixar" in sys.argv:
        for s in universo_d():
            try:
                print(s, len(dados_binance.baixar(s, "1Dutc", 3000)), flush=True)
            except Exception as e:
                print(s, "FALHOU", type(e).__name__, str(e)[:60], flush=True)
        return

    print(f"{'='*100}\n1) VARREDURA EXPLORATORIA -- universo A (20 pares OKX), 1Dutc\n"
          f"   (os numeros abaixo NAO sao evidencia: a selecao infla o vencedor)\n{'='*100}")
    print(f"  {'combinacao':<42} {'n':>5} {'exp liq':>8} {'bruto':>7} {'acerto':>7}")
    resultados = []
    for p in combos():
        tr = rodar(UNIVERSO, p)
        resultados.append((p, tr))
        print(f"  {nome(p):<42} {len(tr):>5} {media(tr):>+8.3f} {media(tr, 'bruto'):>+7.3f} "
              f"{acerto(tr):>6.1f}%", flush=True)

    eleg = [(p, tr) for p, tr in resultados if len(tr) >= MIN_N]
    p_venc, tr_venc = max(eleg, key=lambda x: media(x[1]))
    print(f"\n  vencedora da varredura: {nome(p_venc)} -> {media(tr_venc):+.3f}R (n={len(tr_venc)})")
    print(f"  original                : {nome(ORIGINAL)} -> "
          f"{media(dict((tuple(p), tr) for p, tr in resultados)[ORIGINAL]):+.3f}R")

    print(f"\n{'='*100}\n2) VALIDACAO -- universo D ({len(universo_d())} perps so da Binance) -- DECIDE\n{'='*100}")
    d_venc = rodar(universo_d(), p_venc, binance=True)
    d_orig = rodar(universo_d(), ORIGINAL, binance=True)
    l1, ok1 = linha_ic(f"vencedora ({nome(p_venc)})", d_venc)
    print(l1)
    print(linha_ic(f"original  ({nome(ORIGINAL)})", d_orig)[0])
    ok2 = media(d_venc) > media(d_orig)
    print(f"\n  1) IC95 da vencedora acima de zero: {'sim' if ok1 else 'nao'}")
    print(f"  2) vencedora supera a original no universo D: {'sim' if ok2 else 'nao'} "
          f"({media(d_venc):+.3f}R vs {media(d_orig):+.3f}R)")
    print(f"\n==> DECISAO: {'PASSA' if ok1 and ok2 else 'NAO PASSA'}")


if __name__ == "__main__":
    main()
