"""
Teste PRE-REGISTRADO (22/09/2026) do CASH-AND-CARRY em cripto -- estrategia
6.2 de "151 Trading Strategies" (Kakushadze & Serur), adaptada a perpetuos.
Estudo avulso: NAO faz parte do checklist dos Setups A/B/C nem do monitor de
producao. [interp] = adaptacao minha.

POR QUE ESTA, E POR QUE AGORA
------------------------------
O estudo 14 (carry do Carver, direcional) achou o seguinte: o carry de
funding e real e coletavel, mas a VARIANCIA DO PRECO o engole. O
cash-and-carry remove exatamente essa variancia: compra o ativo no mercado a
vista e vende o perpetuo na mesma quantidade. A posicao fica neutra em preco;
o que sobra e o funding, pago por quem esta alavancado comprado.
E a unica estrategia testada ate aqui cujo retorno NAO depende de prever
nada -- so de carregar a posicao enquanto quem esta alavancado paga.

REGRAS
------
- Para cada par com mercado a vista e perpetuo na Binance: comprar spot e
  vender perpetuo com o MESMO nocional.
- Capital: metade no spot, metade como margem do perpetuo [interp
  conservador: uma conta de varejo nao usa o spot como colateral cruzado].
  Logo, o nocional por perna e 50% do capital alocado ao par.
- Receita: funding recebido pela perna vendida (3x ao dia; quando o funding
  e negativo, a posicao PAGA).
- Base: o resultado inclui a variacao da diferenca entre spot e perpetuo
  (convergencia/divergencia da base), que e o risco real da estrategia.
- Custo: 0.30% por ciclo completo (entrada e saida das duas pernas: spot
  taker 0.10% e perp taker 0.05%, ida e volta).
- Rebalanceamento das pernas quando o desequilibrio passa de 5% do nocional.
- Variantes:
  "sempre"      : carrega todos os pares elegiveis o tempo todo.
  "condicional" : (PRIMARIA) so carrega o par se a media de funding dos
                  ultimos 7 dias for positiva; sai quando deixa de ser.
  "top"         : so o quintil superior por funding medio de 7 dias.
- Pesos iguais entre os pares carregados no dia.

AMOSTRAS
--------
- A (20 pares): desenvolvimento.
- D (215 perps so da Binance, os que tiverem mercado a vista): DECIDE.
  Nunca usada para esta estrategia.

CRITERIO DE DECISAO (pre-registrado)
------------------------------------
Na amostra D, para a variante PRIMARIA ("condicional"):
1. Retorno liquido anual > 0 com IC95 inteiro acima de zero (bootstrap por
   blocos de semana); E
2. Sharpe liquido > 1.0 com IC95 inteiro acima de 0.
O limite de Sharpe 1.0 (mais exigente que nos outros estudos) existe porque
uma estrategia neutra em preco que so coleta funding deveria ter variancia
baixa; se o Sharpe for parecido com o das direcionais, a neutralidade nao
esta funcionando e o risco esta em outro lugar (base, liquidez).
As outras duas variantes sao descritivas.
"""

import random
import statistics
import sys
from collections import defaultdict

import dados_binance as B
from replay_ema_ribbon import UNIVERSO
from replay_123_varredura import universo_d
from replay_carver_carry import sharpe, MS_DIA

CUSTO_CICLO = 0.0030
FRACAO_NOCIONAL = 0.5
JANELA_FUNDING = 7
N_RESAMPLES = 5000
SEED = 42
MIN_DIAS = 400


def serie_par(inst):
    """Por dia: preco spot, preco perp e funding do dia."""
    try:
        spot = B.baixar_spot(inst, "1Dutc", 3000)
    except Exception:
        return None
    perp = B.baixar(inst, "1Dutc", 3000)
    if len(spot) < MIN_DIAS or len(perp) < MIN_DIAS:
        return None
    fund = defaultdict(list)
    for ts, taxa in B.baixar_funding(inst):
        fund[ts // MS_DIA].append(taxa)
    ps = {x[0] // MS_DIA: x[4] for x in spot}
    pp = {x[0] // MS_DIA: x[4] for x in perp}
    dias = sorted(set(ps) & set(pp) & set(fund))
    if len(dias) < MIN_DIAS:
        return None
    return {d: {"spot": ps[d], "perp": pp[d], "fund": sum(fund[d])} for d in dias}


def simular(series, modo):
    """Retornos diarios da carteira (fracao do capital), liquidos."""
    dias = sorted({d for s in series.values() for d in s})
    media_fund = {}
    for inst, s in series.items():
        ds = sorted(s)
        soma, jan, hist = 0.0, [], {}
        for d in ds:
            jan.append(s[d]["fund"])
            soma += s[d]["fund"]
            if len(jan) > JANELA_FUNDING:
                soma -= jan.pop(0)
            hist[d] = soma / len(jan)
        media_fund[inst] = hist
    carregados = set()
    retornos = []
    for k in range(1, len(dias)):
        dia, ant = dias[k], dias[k - 1]
        elegiveis = [i for i, s in series.items() if dia in s and ant in s]
        if not elegiveis:
            continue
        if modo == "sempre":
            alvo = set(elegiveis)
        elif modo == "condicional":
            alvo = {i for i in elegiveis if media_fund[i].get(ant, 0.0) > 0}
        else:  # top quintil
            ranked = sorted(elegiveis, key=lambda i: -media_fund[i].get(ant, 0.0))
            alvo = set(ranked[:max(len(ranked) // 5, 1)])
        entrando = alvo - carregados
        saindo = carregados - alvo
        carregados = alvo
        if not alvo:
            retornos.append((dia, 0.0))
            continue
        peso = 1.0 / len(alvo)
        pnl = 0.0
        for inst in alvo:
            s_ant, s_hoje = series[inst][ant], series[inst][dia]
            nocional = peso * FRACAO_NOCIONAL
            # funding recebido pela perna vendida
            pnl += nocional * s_hoje["fund"]
            # base: (spot_t/spot_{t-1}) - (perp_t/perp_{t-1})
            r_spot = s_hoje["spot"] / s_ant["spot"] - 1
            r_perp = s_hoje["perp"] / s_ant["perp"] - 1
            pnl += nocional * (r_spot - r_perp)
        pnl -= (len(entrando) + len(saindo)) * peso * FRACAO_NOCIONAL * CUSTO_CICLO / 2
        retornos.append((dia, pnl))
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


def relatorio(nome, series, modo, decide):
    rets = simular(series, modo)
    if len(rets) < 100:
        print(f"  {nome}: dados insuficientes")
        return False
    ra, sr = ret_anual(rets), sharpe(rets)
    rlo, rhi = bootstrap(rets, ret_anual)
    slo, shi = bootstrap(rets, sharpe)
    vol = statistics.pstdev([r for _, r in rets]) * (365 ** 0.5)
    print(f"  {nome}: dias={len(rets)} | retorno {100*ra:+.1f}%/ano | IC95 [{100*rlo:+.1f}%, {100*rhi:+.1f}%]")
    print(f"    Sharpe {sr:+.2f} | IC95 [{slo:+.2f}, {shi:+.2f}] | vol {100*vol:.1f}%/ano")
    return (rlo > 0 and slo > 1.0) if decide else None


def carrega(universo):
    s = {}
    for inst in universo:
        try:
            x = serie_par(inst)
        except Exception:
            continue
        if x:
            s[inst] = x
    return s


def main():
    alvo_d = universo_d()[:40] if "--rapido" in sys.argv else universo_d()
    A = carrega([B.simbolo(x) for x in UNIVERSO])
    D = carrega(alvo_d)
    print(f"amostra A: {len(A)} pares com spot | amostra D: {len(D)} pares com spot")

    print(f"\n{'='*100}\nAMOSTRA A (desenvolvimento)\n{'='*100}")
    for modo in ("condicional", "sempre", "top"):
        relatorio(f"{modo:<12}", A, modo, decide=False)

    print(f"\n{'='*100}\nAMOSTRA D -- DECIDE (primaria: condicional)\n{'='*100}")
    ok = relatorio("condicional (PRIMARIA)", D, "condicional", decide=True)
    for modo in ("sempre", "top"):
        relatorio(f"{modo:<12} (descritivo)", D, modo, decide=False)
    print(f"\n==> DECISAO cash-and-carry: {'PASSA' if ok else 'NAO PASSA'}")


if __name__ == "__main__":
    main()
