"""
Teste PRE-REGISTRADO (22/09/2026) das estrategias 26 (FAST MEAN REVERSION) e
27 (SAFER FAST MEAN REVERSION) do livro "Advanced Futures Trading Strategies"
(Robert Carver, 2023), adaptadas a perpetuos de cripto. Faz parte da mesma
familia de quatro testes de replay_carver_outras.py (mesma correcao de
multiplicidade). [interp] = interpretacao/adaptacao minha.

REGRAS (parametros do livro)
-----------------------------
- Equilibrio: EWMA de span 5 dos fechamentos DIARIOS, conhecido no fim do dia
  anterior ("pt-1 e o ultimo fechamento diario disponivel").
- Forecast, atualizado a cada HORA:
      (equilibrio - preco_hora) / (vol diaria em unidades de preco)
  com vol diaria = vol anual % / 16 x preco. Preco acima do equilibrio ->
  forecast negativo (vende); abaixo -> compra.
- Escala 9.3, limite +-20 (numeros do livro).
- SEM BUFFERING: o livro diz explicitamente que aplicar buffering aqui
  "destruiria a lucratividade". A posicao e reajustada toda hora.
- Estrategia 27 [interp]: so mantem posicao a favor da tendencia de longo
  prazo (sinal do EWMAC(64,256) diario); contra a tendencia, posicao zero.
  O livro descreve um filtro de tendencia; esta e a leitura mais simples.
- Dimensionamento, teto de 1x por instrumento e 3x bruto, custo de 0.06% do
  nocional negociado e funding: identicos aos estudos 14 e 15. Aqui o custo
  importa muito mais, porque o giro e horario.

AMOSTRAS
--------
Dados horarios da Binance desde 2019/2020.
- A (20 pares): desenvolvimento.
- D: subamostra de 60 pares dos 215, sorteada com semente fixa (42) ANTES de
  baixar os dados -- baixar 1H dos 215 seria ~1 GB. DECIDE.

CRITERIO DE DECISAO (pre-registrado)
------------------------------------
Mesmo da familia (4 testes, Bonferroni): na amostra D,
1. Sharpe liquido > 0 com IC98.75 inteiro acima de zero (bootstrap por
   blocos de semana sobre os retornos diarios agregados); E
2. alfa contra a carteira equal-weight comprada > 0 com IC98.75 acima de
   zero.
Sanidade: o livro reporta SR 0.44-0.75 em futuros com dados horarios desde
2013. Em cripto o custo por giro e maior, entao um numero bem abaixo disso
seria esperado; um numero bem acima e suspeita de erro.
"""

import random
import statistics
import sys
from collections import defaultdict

import dados_binance as B
import replay_carver_carry as C
from replay_carver_carry import (
    vol_diaria, sharpe, alfa, ewma, CAP, UNIVERSO, universo_d,
    VOL_MIN, TAU, POS_MAX, ALAV_MAX, CUSTO_NOCIONAL, AQUECIMENTO, MS_DIA,
)
from replay_carver_outras import bootstrap_bonf, ewmac_forecast

SPAN_EQ = 5
ESCALA = 9.3
SUBAMOSTRA = 60
MS_HORA = 3_600_000


def dados_instrumento(inst):
    """Serie horaria + equilibrio/vol/funding diarios alinhados."""
    diario = B.baixar(inst, "1Dutc", 3000)
    horario = B.baixar(inst, "1H", 3000)
    if len(diario) < 400 or len(horario) < 400 * 24:
        return None
    fechos = [x[4] for x in diario]
    eq = ewma(fechos, SPAN_EQ)
    vols = vol_diaria(fechos)
    tend = ewmac_forecast(fechos, [max(v * 16, VOL_MIN) for v in vols], 64)
    fund = defaultdict(list)
    for ts, taxa in B.baixar_funding(inst):
        fund[ts // MS_DIA].append(taxa)
    por_dia = {}
    for i in range(AQUECIMENTO, len(diario)):
        d = diario[i][0] // MS_DIA
        vol_a = max(vols[i] * 16, VOL_MIN)
        por_dia[d] = {"eq": eq[i], "vol_a": vol_a, "vol_preco": vol_a / 16 * fechos[i],
                      "tend": tend[i], "fund": sum(fund.get(d, [])) / 3 if fund.get(d) else 0.0}
    horas = [(x[0], x[4]) for x in horario if (x[0] // MS_DIA) - 1 in por_dia]
    return {"horas": horas, "dia": por_dia}


def simular_mr(dados, filtro_tendencia):
    """Retornos DIARIOS da carteira (fracao do capital)."""
    instrumentos = list(dados)
    if not instrumentos:
        return []
    por_hora = defaultdict(dict)
    for inst in instrumentos:
        for ts, preco in dados[inst]["horas"]:
            por_hora[ts][inst] = preco
    horas = sorted(por_hora)
    pos = {}
    por_dia = defaultdict(float)
    for k in range(len(horas) - 1):
        ts, prox = horas[k], horas[k + 1]
        ativos = [i for i in por_hora[ts] if i in por_hora[prox]]
        if len(ativos) < 3:
            continue
        peso = 1.0 / len(ativos)
        desejados = {}
        for inst in ativos:
            d_ant = dados[inst]["dia"].get(ts // MS_DIA - 1)
            if not d_ant or d_ant["vol_preco"] <= 0:
                desejados[inst] = 0.0
                continue
            f = (d_ant["eq"] - por_hora[ts][inst]) / d_ant["vol_preco"] * ESCALA
            f = max(-CAP, min(CAP, f))
            if filtro_tendencia and f * d_ant["tend"] < 0:
                f = 0.0
            p = (f / 10.0) * peso * TAU / d_ant["vol_a"]
            desejados[inst] = max(-POS_MAX, min(POS_MAX, p))
        bruta = sum(abs(v) for v in desejados.values())
        if bruta > ALAV_MAX:
            desejados = {i: v * ALAV_MAX / bruta for i, v in desejados.items()}
        pnl = 0.0
        for inst in ativos:
            atual, alvo = pos.get(inst, 0.0), desejados[inst]
            if alvo != atual:
                pnl -= abs(alvo - atual) * CUSTO_NOCIONAL
                atual = alvo
            pos[inst] = atual
            pnl += atual * (por_hora[prox][inst] / por_hora[ts][inst] - 1)
            if ts % (8 * MS_HORA) == 0:  # settlement de funding
                d_ant = dados[inst]["dia"].get(ts // MS_DIA - 1)
                if d_ant:
                    pnl -= atual * d_ant["fund"]
        por_dia[ts // MS_DIA] += pnl
    return sorted(por_dia.items())


def mercado_diario(dados):
    por_dia = defaultdict(list)
    for inst, d in dados.items():
        dias = sorted(d["dia"])
        for i in range(1, len(dias)):
            a, h = d["dia"][dias[i - 1]], d["dia"][dias[i]]
            if a["eq"] > 0:
                por_dia[dias[i]].append(h["eq"] / a["eq"] - 1)
    return [(d, sum(v) / len(v)) for d, v in sorted(por_dia.items()) if v]


def relatorio(nome, dados, filtro, decide):
    rets = simular_mr(dados, filtro)
    if len(rets) < 100:
        print(f"  {nome}: dados insuficientes ({len(rets)} dias)")
        return False
    mkt = mercado_diario(dados)
    m = dict(mkt)
    sr = sharpe(rets)
    lo, hi = bootstrap_bonf(rets, sharpe)
    a = alfa(rets, mkt)
    alo, ahi = bootstrap_bonf([(d, r) for d, r in rets if d in m], lambda am: alfa(am, mkt))
    rr = sum(r for _, r in rets) / len(rets) * 365
    print(f"  {nome}: dias={len(rets)} | retorno {100*rr:+.1f}%/ano | Sharpe {sr:+.2f} | "
          f"IC98.75 [{lo:+.2f}, {hi:+.2f}]")
    print(f"    alfa vs mercado {100*a:+.1f}%/ano | IC98.75 [{100*alo:+.1f}%, {100*ahi:+.1f}%] | "
          f"mercado {sharpe(mkt):+.2f}")
    return (lo > 0 and alo > 0) if decide else None


def carrega(universo):
    out = {}
    for inst in universo:
        try:
            d = dados_instrumento(inst)
        except Exception:
            continue
        if d:
            out[inst] = d
    return out


def main():
    d = universo_d()
    random.Random(42).shuffle(d)
    alvo_d = d[:SUBAMOSTRA]
    if "--rapido" in sys.argv:
        alvo_d = alvo_d[:12]
    A = carrega(list(UNIVERSO))
    D = carrega(alvo_d)
    print(f"amostra A: {len(A)} | amostra D: {len(D)}")

    print(f"\n{'='*100}\nAMOSTRA A (desenvolvimento)\n{'='*100}")
    relatorio("26 mean reversion rapida ", A, False, decide=False)
    relatorio("27 com filtro de tendencia", A, True, decide=False)

    print(f"\n{'='*100}\nAMOSTRA D -- DECIDE (IC 98.75%, Bonferroni)\n{'='*100}")
    ok26 = relatorio("26 mean reversion rapida ", D, False, decide=True)
    ok27 = relatorio("27 com filtro de tendencia", D, True, decide=True)
    print(f"\n==> DECISAO 26: {'PASSA' if ok26 else 'NAO PASSA'}")
    print(f"==> DECISAO 27: {'PASSA' if ok27 else 'NAO PASSA'}")


if __name__ == "__main__":
    main()
