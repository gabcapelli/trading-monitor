"""
Teste PRE-REGISTRADO (22/09/2026) das estrategias de CARRY do livro
"Advanced Futures Trading Strategies" (Robert Carver, 2023), adaptadas a
perpetuos de cripto:
  - Estrategia 10 (basic carry): posicao pelo carry do proprio instrumento.
  - Estrategia 20 (cross-sectional carry): posicao pelo carry RELATIVO a
    mediana dos instrumentos.
Estudo avulso: NAO faz parte do checklist dos Setups A/B/C nem do monitor de
producao. [interp] = interpretacao/adaptacao minha.

POR QUE ESTA E DIFERENTE DOS ESTUDOS 1-13
------------------------------------------
Os 11 setups de video eram price action com stop e alvo, medidos em R por
trade. Aqui:
- o sinal NAO vem do preco: vem do funding, o dado que diz quem esta pagando
  quem no perpetuo;
- nao ha stop nem alvo: a posicao e continua, dimensionada por volatilidade;
- a medida e Sharpe da carteira, nao expectancia por trade.

REGRAS (do livro, com os parametros dele)
------------------------------------------
- Volatilidade (cap. "Position sizing"): sigma% diario = mistura de
  0.3 x media longa (10 anos) + 0.7 x EWMA(span 32) do desvio padrao dos
  retornos percentuais; anualizada por x16.
- Carry anualizado. No livro vem da estrutura a termo (contrato proximo vs
  distante). [interp] No perpetuo o analogo direto e o funding: quem esta
  comprado paga funding quando ele e positivo, entao
      carry_anual% = -funding_medio_do_dia x 3 x 365
  (3 settlements por dia na Binance). Sinal positivo = ser comprado PAGA.
- Forecast bruto = carry_anual% / sigma_anual% ("risk adjusted carry").
- Estrategia 10: forecast = bruto x 30, limitado a +-20 (escala e limite do
  livro). Variantes descritivas: media movel do carry em 20, 60 e 120 dias
  (o livro usa "carry60" como exemplo).
- Estrategia 20: carry relativo = forecast bruto - mediana do forecast bruto
  de todos os instrumentos no mesmo dia, suavizado por EWMA de span 90,
  x 50, limitado a +-20 (os numeros do livro para cross-sectional carry).
- Posicao: N = (forecast/10) x capital x tau / (sigma_anual% x preco), com
  tau = 20% de risco anual [interp: valor usado no livro como exemplo] e
  peso igual entre instrumentos. IDM fixado em 1.0 [interp: simplificacao
  conservadora -- o livro usaria um multiplicador de diversificacao > 1, que
  so escala o resultado, nao muda o Sharpe].
- Limites de implementacao [interp, decididos ANTES da rodada que decide,
  para corrigir erros de implementacao encontrados numa rodada de fumaca]:
  descarta os primeiros 60 dias de cada serie (a EWMA de volatilidade comeca
  fria e chegava a 0.002% ao ano, gerando posicao de 1250x o capital);
  piso de 10% na volatilidade anual; nocional maximo de 1x o capital por
  instrumento; e alavancagem bruta da carteira limitada a 3x (o teto do plano
  de risco do Gabriel), escalando todas as posicoes proporcionalmente quando
  estourar.
- Buffering: nao rebalanceia enquanto a posicao desejada estiver a menos de
  10% do risco medio da posicao atual (regra do livro para cortar custo).
- Custo: 0.06% do nocional negociado (taker 0.05% + slippage 0.01% numa
  ordem pequena e liquida) [interp: mais barato que os 0.18% dos estudos de
  price action porque aqui nao ha ordem stop a mercado -- o rebalanceamento
  e agendado e pode ser limite].
- Funding e recebido/pago de verdade na simulacao (3x ao dia), alem do
  retorno de preco.

DADOS
-----
Precos diarios e funding da Binance (`dados_binance.py`), desde 2019.
- Amostra A: os 20 pares do monitor -- DESENVOLVIMENTO (in-sample).
- Amostra D: os 215 perpetuos que so existem na Binance (universo_d.txt) --
  VALIDACAO, nunca usada para carry.

CRITERIO DE DECISAO (pre-registrado)
------------------------------------
Na amostra D, para cada uma das duas estrategias (10 e 20), com os
parametros do livro e sem varredura:
1. Sharpe anualizado da carteira liquida de custos > 0 com IC95 inteiro
   acima de zero (bootstrap reamostrando BLOCOS DE SEMANA, regra do
   protocolo para posicoes de duracao longa).
2. Alfa contra o mercado (carteira equal-weight dos mesmos pares) positivo
   com IC95 acima de zero -- o teste de beta do protocolo, na versao de
   carteira: o retorno nao pode ser so exposicao direcional disfarcada.
PASSA so se 1 e 2 valerem. A amostra A e so desenvolvimento: seu resultado
nao decide nada.
Comparacao de sanidade: o livro reporta Sharpe ~0.8-1.0 para carry em
futuros diversificados. Um numero muito acima disso em cripto e sinal de
erro de implementacao, nao de descoberta.
"""

import math
import random
import statistics
import sys
from collections import defaultdict

import dados_binance as B
from replay_ema_ribbon import UNIVERSO
from replay_123_varredura import universo_d

TAU = 0.20              # alvo de risco anual
ESCALA_10 = 30.0
ESCALA_20 = 50.0
CAP = 20.0
SPAN_VOL = 32
PESO_LONGO = 0.3
SPAN_XS = 90
BUFFER = 0.10
CUSTO_NOCIONAL = 0.0006
MS_DIA = 86_400_000
N_RESAMPLES = 5000
SEED = 42
MIN_DIAS = 400
AQUECIMENTO = 60        # dias descartados: a EWMA de volatilidade comeca fria
VOL_MIN = 0.10          # piso da volatilidade anual (10%)
POS_MAX = 1.0           # nocional maximo por instrumento, em multiplos do capital
ALAV_MAX = 3.0          # alavancagem bruta maxima da carteira (teto do plano)


def ewma(v, span):
    a = 2 / (span + 1)
    out, e = [], None
    for x in v:
        e = x if e is None else a * x + (1 - a) * e
        out.append(e)
    return out


def vol_diaria(precos):
    """Desvio padrao diario misturado (0.3 longo + 0.7 curto), como no livro."""
    ret = [0.0] + [precos[i] / precos[i - 1] - 1 for i in range(1, len(precos))]
    var = ewma([r * r for r in ret], SPAN_VOL)
    curto = [math.sqrt(max(v, 1e-12)) for v in var]
    longo, soma, jan = [], 0.0, []
    for x in curto:
        jan.append(x)
        soma += x
        if len(jan) > 2520:  # ~10 anos
            soma -= jan.pop(0)
        longo.append(soma / len(jan))
    return [PESO_LONGO * longo[i] + (1 - PESO_LONGO) * curto[i] for i in range(len(curto))]


def serie_instrumento(inst):
    """Por dia UTC: preco de fechamento, vol diaria e carry anualizado (%)."""
    c = B.baixar(inst, "1Dutc", 3000)
    if len(c) < MIN_DIAS:
        return None
    fund = B.baixar_funding(inst)
    por_dia = defaultdict(list)
    for ts, taxa in fund:
        por_dia[ts // MS_DIA].append(taxa)
    dias = [x[0] // MS_DIA for x in c]
    precos = [x[4] for x in c]
    vols = vol_diaria(precos)
    out = []
    for i, d in enumerate(dias):
        taxas = por_dia.get(d)
        if not taxas or vols[i] <= 0:
            out.append(None)
            continue
        carry_anual = -sum(taxas) / len(taxas) * 3 * 365
        vol_anual = vols[i] * 16
        out.append({"dia": d, "preco": precos[i], "vol_d": vols[i], "vol_a": max(vol_anual, VOL_MIN),
                    "carry": carry_anual, "bruto": carry_anual / max(vol_anual, VOL_MIN),
                    "funding_dia": sum(taxas)})
    return [x for x in out if x is not None][AQUECIMENTO:]


def forecasts(series, modo):
    """{dia: {inst: forecast limitado}}"""
    porcentagem = defaultdict(dict)
    for inst, s in series.items():
        for x in s:
            porcentagem[x["dia"]][inst] = x["bruto"]
    fc = defaultdict(dict)
    if modo == "10":
        for dia, brutos in porcentagem.items():
            for inst, b in brutos.items():
                fc[dia][inst] = max(-CAP, min(CAP, b * ESCALA_10))
        return fc
    # cross-sectional: bruto - mediana do dia, suavizado por EWMA(90) por instrumento
    rel = defaultdict(list)
    dias_ord = sorted(porcentagem)
    for dia in dias_ord:
        brutos = porcentagem[dia]
        if len(brutos) < 3:
            continue
        med = statistics.median(brutos.values())
        for inst, b in brutos.items():
            rel[inst].append((dia, b - med))
    for inst, pares in rel.items():
        suav = ewma([p[1] for p in pares], SPAN_XS)
        for (dia, _), s in zip(pares, suav):
            fc[dia][inst] = max(-CAP, min(CAP, s * ESCALA_20))
    return fc


def simular(series, modo):
    """Retornos diarios da carteira (fracao do capital), liquidos de custo."""
    fc = forecasts(series, modo)
    idx = {inst: {x["dia"]: x for x in s} for inst, s in series.items()}
    dias = sorted(fc)
    pos = {}       # inst -> nocional/capital assinado do dia anterior
    retornos = []
    for k in range(1, len(dias)):
        dia, ant = dias[k], dias[k - 1]
        ativos = [i for i in fc[ant] if dia in idx[i] and ant in idx[i]]
        if len(ativos) < 3:
            retornos.append((dia, 0.0))
            continue
        peso = 1.0 / len(ativos)
        pnl, custo = 0.0, 0.0
        novos = {}
        desejados = {}
        for inst in ativos:
            a = idx[inst][ant]
            d_i = (fc[ant][inst] / 10.0) * peso * TAU / a["vol_a"]
            desejados[inst] = max(-POS_MAX, min(POS_MAX, d_i))
        bruta = sum(abs(v) for v in desejados.values())
        if bruta > ALAV_MAX:
            fator = ALAV_MAX / bruta
            desejados = {i: v * fator for i, v in desejados.items()}
        for inst in ativos:
            a, h = idx[inst][ant], idx[inst][dia]
            desejado = desejados[inst]
            atual = pos.get(inst, 0.0)
            risco_pos = peso * TAU / a["vol_a"]
            if abs(desejado - atual) > BUFFER * max(risco_pos, 1e-9):
                custo += abs(desejado - atual) * CUSTO_NOCIONAL
                atual = desejado
            novos[inst] = atual
            ret_preco = h["preco"] / a["preco"] - 1
            pnl += atual * ret_preco
            pnl -= atual * h["funding_dia"]   # comprado paga funding positivo; vendido recebe
        pos = novos
        retornos.append((dia, pnl - custo))
    return retornos


def mercado(series):
    """Carteira equal-weight comprada (proxy de mercado), sem alavancagem."""
    idx = {inst: {x["dia"]: x for x in s} for inst, s in series.items()}
    dias = sorted({d for s in series.values() for d in [x["dia"] for x in s]})
    out = []
    for k in range(1, len(dias)):
        dia, ant = dias[k], dias[k - 1]
        rets = [idx[i][dia]["preco"] / idx[i][ant]["preco"] - 1
                for i in series if dia in idx[i] and ant in idx[i]]
        out.append((dia, sum(rets) / len(rets) if rets else 0.0))
    return out


def sharpe(rets):
    v = [r for _, r in rets]
    if len(v) < 30:
        return float("nan")
    m, s = sum(v) / len(v), statistics.pstdev(v)
    return m / s * math.sqrt(365) if s > 0 else float("nan")


def bootstrap_semana(rets, f):
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


def alfa(rets, mkt):
    m = dict(mkt)
    pares = [(r, m[d]) for d, r in rets if d in m]
    if len(pares) < 30:
        return float("nan")
    my = sum(p[1] for p in pares) / len(pares)
    mx = sum(p[0] for p in pares) / len(pares)
    var = sum((p[1] - my) ** 2 for p in pares)
    if var <= 0:
        return float("nan")
    beta = sum((p[0] - mx) * (p[1] - my) for p in pares) / var
    return (mx - beta * my) * 365  # alfa anualizado


def relatorio(nome, series, modo, decide):
    rets = simular(series, modo)
    mkt = mercado(series)
    sr = sharpe(rets)
    lo, hi = bootstrap_semana(rets, sharpe)
    a = alfa(rets, mkt)
    m = dict(mkt)
    alo, ahi = bootstrap_semana([(d, r) for d, r in rets if d in m], lambda am: alfa(am, mkt))
    ret_anual = sum(r for _, r in rets) / len(rets) * 365
    print(f"  {nome}: dias={len(rets)} | retorno {100*ret_anual:+.1f}%/ano | "
          f"Sharpe {sr:+.2f} | IC95 [{lo:+.2f}, {hi:+.2f}]")
    print(f"    alfa vs mercado {100*a:+.1f}%/ano | IC95 [{100*alo:+.1f}%, {100*ahi:+.1f}%] | "
          f"Sharpe do mercado {sharpe(mkt):+.2f}")
    return (lo > 0 and alo > 0) if decide else None


def main():
    alvo_a = list(UNIVERSO)
    alvo_d = universo_d()
    if "--rapido" in sys.argv:
        alvo_d = alvo_d[:40]
    series = {}
    for nome, universo in (("A", alvo_a), ("D", alvo_d)):
        s = {}
        for inst in universo:
            try:
                x = serie_instrumento(inst)
            except Exception as e:
                print(f"    {inst}: falhou ({type(e).__name__})")
                continue
            if x:
                s[inst] = x
        series[nome] = s
        print(f"amostra {nome}: {len(s)} instrumentos com dados")

    print(f"\n{'='*100}\nAMOSTRA A (20 pares) -- desenvolvimento, nao decide\n{'='*100}")
    for modo, rot in (("10", "estrategia 10 (basic carry)"), ("20", "estrategia 20 (cross-sectional)")):
        relatorio(rot, series["A"], modo, decide=False)

    print(f"\n{'='*100}\nAMOSTRA D ({len(series['D'])} pares so da Binance) -- DECIDE\n{'='*100}")
    oks = {}
    for modo, rot in (("10", "estrategia 10 (basic carry)"), ("20", "estrategia 20 (cross-sectional)")):
        oks[rot] = relatorio(rot, series["D"], modo, decide=True)
    for rot, ok in oks.items():
        print(f"\n==> DECISAO {rot}: {'PASSA' if ok else 'NAO PASSA'}")


if __name__ == "__main__":
    main()
