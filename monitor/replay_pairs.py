"""
Teste PRE-REGISTRADO (22/09/2026) de PAIRS TRADING / arbitragem estatistica
em perpetuos de cripto -- estrategias 3.8 e 3.18 de "151 Trading Strategies"
(Kakushadze & Serur), na formulacao classica de Gatev, Goetzmann &
Rouwenhorst (2006). Estudo avulso: NAO faz parte do checklist dos Setups
A/B/C nem do monitor de producao. [interp] = adaptacao minha.

POR QUE ESTA
-------------
E a ultima familia de ESTRATEGIA DE TRADING ainda nao testada aqui:
tendencia (11 estudos), premios transversais (14-19) e carrego (20) ja
foram. Pairs trading nao aposta direcao: aposta que dois ativos que andam
juntos voltam a andar juntos. Cripto e o caso ideal porque as L1s sao
altamente correlacionadas entre si.

REGRAS (Gatev et al., parametros do paper, sem otimizacao)
-----------------------------------------------------------
- Janela de FORMACAO: 252 dias. Precos normalizados (indice 1.0 no inicio).
  Distancia do par = soma dos quadrados das diferencas entre as duas series
  normalizadas. Selecionam-se os 20 pares de MENOR distancia [interp: o
  paper usa os 20 melhores entre centenas de acoes].
- Janela de NEGOCIACAO: os 126 dias seguintes. Depois, reforma-se tudo.
- Spread = diferenca entre as series normalizadas; z = spread / desvio
  padrao do spread na formacao.
- Entrada quando |z| >= 2 (vende o que subiu mais, compra o que subiu
  menos); saida quando o spread cruza zero; saida forcada no fim da janela
  de negociacao.
- Stop [interp, nao esta no paper]: |z| >= 4 encerra o par com prejuizo. O
  paper nao usa stop; sem ele um par que descola nunca fecha. Registrado
  como desvio consciente.
- Pesos iguais entre pares abertos; cada par e dollar-neutral (metade do
  nocional em cada perna).
- Custo: 0.06% do nocional negociado por perna (igual aos estudos 14-19).
  Funding pago/recebido nas duas pernas.

AMOSTRAS
--------
- A (20 pares da Binance): desenvolvimento.
- E (153 perps correspondentes aos universos OKX B e C): DECIDE. Foi usada
  no estudo 19 (combo de premios), mas nunca para arbitragem estatistica.

CRITERIO DE DECISAO (pre-registrado)
------------------------------------
Na amostra E:
1. Retorno liquido anual > 0 com IC95 inteiro acima de zero (bootstrap por
   blocos de semana); E
2. Sharpe liquido > 0.5 com IC95 acima de zero [interp: limite intermediario
   -- uma estrategia neutra deveria ter Sharpe melhor que as direcionais que
   ja falharam (~0.3), mas nao se exige o 1.0 do cash-and-carry, que e
   carrego puro].
PASSA so se 1 e 2 valerem.
"""

import random
import statistics
import sys
from collections import defaultdict

import dados_binance as B
from replay_ema_ribbon import UNIVERSO
from replay_carver_carry import sharpe, MS_DIA
from replay_combo_premios import universo_e

FORMACAO = 252
NEGOCIACAO = 126
N_PARES = 20
Z_ENTRA = 2.0
Z_STOP = 4.0
CUSTO = 0.0006
N_RESAMPLES = 5000
SEED = 42
MIN_DIAS = 450


def serie(inst):
    c = B.baixar(inst, "1Dutc", 3000)
    if len(c) < MIN_DIAS:
        return None
    fund = defaultdict(list)
    for ts, taxa in B.baixar_funding(inst):
        fund[ts // MS_DIA].append(taxa)
    return {x[0] // MS_DIA: {"p": x[4], "f": sum(fund.get(x[0] // MS_DIA, []))} for x in c}


def escolhe_pares(series, dias_form):
    """Os N pares de menor distancia entre series normalizadas."""
    norm = {}
    for inst, s in series.items():
        vals = [s[d]["p"] for d in dias_form if d in s]
        if len(vals) < len(dias_form) * 0.9 or vals[0] <= 0:
            continue
        norm[inst] = [v / vals[0] for v in vals]
    insts = sorted(norm)
    dists = []
    for i in range(len(insts)):
        for j in range(i + 1, len(insts)):
            a, b = norm[insts[i]], norm[insts[j]]
            n = min(len(a), len(b))
            if n < len(dias_form) * 0.9:
                continue
            d = sum((a[k] - b[k]) ** 2 for k in range(n)) / n
            dists.append((d, insts[i], insts[j]))
    dists.sort()
    out = []
    for d, x, y in dists[:N_PARES]:
        a, b = norm[x], norm[y]
        n = min(len(a), len(b))
        spread = [a[k] - b[k] for k in range(n)]
        dp = statistics.pstdev(spread)
        if dp > 0:
            out.append((x, y, dp))
    return out


def simular(series):
    dias = sorted({d for s in series.values() for d in s})
    retornos = []
    pos = {}          # (x,y) -> (lado, p_x0, p_y0)
    pares = []
    base = {}
    for k in range(FORMACAO, len(dias) - 1):
        dia, prox = dias[k], dias[k + 1]
        if (k - FORMACAO) % NEGOCIACAO == 0:
            pares = escolhe_pares(series, dias[k - FORMACAO:k])
            base = {}
            for x, y, dp in pares:
                if x in series and y in series and dia in series[x] and dia in series[y]:
                    base[(x, y)] = (series[x][dia]["p"], series[y][dia]["p"], dp)
            pos = {}
        pnl, custo = 0.0, 0.0
        abertos = len(pos)
        peso = 1.0 / max(N_PARES, 1)
        for (x, y), (px0, py0, dp) in base.items():
            if dia not in series.get(x, {}) or dia not in series.get(y, {}):
                continue
            if prox not in series.get(x, {}) or prox not in series.get(y, {}):
                continue
            sx = series[x][dia]["p"] / px0
            sy = series[y][dia]["p"] / py0
            z = (sx - sy) / dp
            lado = pos.get((x, y))
            if lado is None:
                if abs(z) >= Z_ENTRA:
                    lado = -1 if z > 0 else 1   # z>0: x caro -> vende x, compra y
                    pos[(x, y)] = lado
                    custo += peso * CUSTO * 2
            else:
                fechou = (z * lado > 0) or (abs(z) >= Z_STOP)
                if fechou:
                    del pos[(x, y)]
                    custo += peso * CUSTO * 2
                    lado = None
            if lado is not None:
                rx = series[x][prox]["p"] / series[x][dia]["p"] - 1
                ry = series[y][prox]["p"] / series[y][dia]["p"] - 1
                pnl += peso / 2 * lado * (rx - ry)
                pnl -= peso / 2 * (lado * series[x][prox]["f"] - lado * series[y][prox]["f"])
        retornos.append((prox, pnl - custo))
    return retornos


def bootstrap(rets, f):
    por_sem = defaultdict(list)
    for dia, r in rets:
        por_sem[dia // 7].append((dia, r))
    blocos = list(por_sem.values())
    rng = random.Random(SEED)
    vals = []
    for _ in range(N_RESAMPLES):
        amostra = []
        for _ in range(len(blocos)):
            amostra += blocos[rng.randrange(len(blocos))]
        vals.append(f(amostra))
    vals = [v for v in vals if v == v]
    vals.sort()
    return vals[int(0.025 * len(vals))], vals[int(0.975 * len(vals)) - 1]


def ret_anual(rets):
    return sum(r for _, r in rets) / len(rets) * 365


def relatorio(nome, series, decide):
    rets = simular(series)
    if len(rets) < 100:
        print(f"  {nome}: dados insuficientes")
        return False
    ra, sr = ret_anual(rets), sharpe(rets)
    rlo, rhi = bootstrap(rets, ret_anual)
    slo, shi = bootstrap(rets, sharpe)
    vol = statistics.pstdev([r for _, r in rets]) * (365 ** 0.5)
    print(f"  {nome}: dias={len(rets)} | retorno {100*ra:+.1f}%/ano | IC95 [{100*rlo:+.1f}%, {100*rhi:+.1f}%]")
    print(f"    Sharpe {sr:+.2f} | IC95 [{slo:+.2f}, {shi:+.2f}] | vol {100*vol:.1f}%/ano")
    return (rlo > 0 and slo > 0.5) if decide else None


def carrega(universo):
    s = {}
    for inst in universo:
        try:
            x = serie(inst)
        except Exception:
            continue
        if x:
            s[inst] = x
    return s


def main():
    alvo_e = universo_e()[:40] if "--rapido" in sys.argv else universo_e()
    A = carrega([B.simbolo(x) for x in UNIVERSO])
    E = carrega(alvo_e)
    print(f"amostra A: {len(A)} | amostra E: {len(E)}")
    print(f"\n{'='*100}\nAMOSTRA A (desenvolvimento)\n{'='*100}")
    relatorio("pairs trading", A, decide=False)
    print(f"\n{'='*100}\nAMOSTRA E -- DECIDE\n{'='*100}")
    ok = relatorio("pairs trading", E, decide=True)
    print(f"\n==> DECISAO pairs trading: {'PASSA' if ok else 'NAO PASSA'}")


if __name__ == "__main__":
    main()
