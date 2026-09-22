"""
Teste PRE-REGISTRADO (22/09/2026) de tres estrategias de "151 Trading
Strategies" (Kakushadze & Serur, 2018), capitulo 3 (Stocks), adaptadas ao
corte transversal de perpetuos de cripto:
  - 3.9 Mean-Reversion / Single Cluster: comprar quem caiu mais que a media
    do grupo e vender quem subiu mais, dollar-neutral. Duas velocidades:
    retorno de 1 dia e de 5 dias.
  - 3.4 Low-Volatility Anomaly: comprar os de menor volatilidade historica,
    vender os de maior, dollar-neutral.
Estudo avulso: NAO faz parte do checklist dos Setups A/B/C nem do monitor de
producao. [interp] = interpretacao/adaptacao minha.

POR QUE ESTAS
--------------
As duas sao de familias que ainda NAO foram testadas neste projeto:
- reversao CROSS-SECTIONAL (o estudo 16 testou reversao temporal, do preco
  contra a propria media -- aqui e contra o grupo, no mesmo dia);
- anomalia de baixa volatilidade (premio por risco, como a skew, mas medido
  por volatilidade em vez de assimetria).
Pairs trading (3.8) e o caso N=2 da 3.9 e fica para uma segunda rodada se
alguma destas mostrar algo.

REGRAS (do livro; formulas 3.28-3.31 e secao 3.4)
--------------------------------------------------
- Retorno demeanado no dia t: R~_i = R_i - media(R) entre os instrumentos do
  dia (o "cluster" e o universo inteiro de perpetuos [interp: o livro usa
  setor/industria; em cripto o analogo mais proximo e o mercado todo]).
- 3.9: forecast_i proporcional a -R~_i / vol_i (risk-adjusted, para o livro
  aceitar pesos nao uniformes: "w_i ~ 1/sigma_i").
- 3.4: forecast_i proporcional a -z_i, onde z_i e o escore padronizado da
  volatilidade anual do instrumento no dia (baixa vol -> forecast positivo).
  [interp: o livro descreve decis (compra o decil de menor vol, vende o de
  maior); o escore continuo e a versao suave da mesma ideia e aproveita todo
  o corte transversal.]
- Escala do forecast: metodo do Carver -- escala = 10 / media(|forecast
  bruto|), estimada SO na amostra A e fixada antes de rodar em D. Limite
  +-20.
- Dimensionamento, custo (0.06% do nocional), buffering de 10%, limites de
  implementacao e funding: identicos aos estudos 14-16.

AMOSTRAS
--------
- A (20 pares da Binance): desenvolvimento; so aqui se estima a escala.
- D (215 perps so da Binance): DECIDE.

CRITERIO DE DECISAO (pre-registrado, com multiplicidade)
---------------------------------------------------------
Tres testes na mesma amostra D -> IC de 98.33% (Bonferroni: 0.05/3).
Cada estrategia PASSA se, na amostra D:
1. Sharpe liquido > 0 com IC98.33 inteiro acima de zero (bootstrap por
   blocos de semana); E
2. alfa contra a carteira equal-weight > 0 com IC98.33 acima de zero.
Sanidade: reversao cross-sectional em acoes costuma render SR 0.3-0.8 bruto
antes de custo; em cripto o custo por giro e maior. Numero muito acima disso
e suspeita de erro.
"""

import random
import statistics
import sys
from collections import defaultdict

import replay_carver_carry as C
from replay_carver_carry import (
    serie_instrumento, mercado, sharpe, alfa, CAP, UNIVERSO, universo_d,
)

ALFA_FAMILIA = 0.05
N_TESTES = 3


def bootstrap_bonf(rets, f):
    por_sem = defaultdict(list)
    for dia, r in rets:
        por_sem[dia // 7].append((dia, r))
    blocos = list(por_sem.values())
    rng = random.Random(C.SEED)
    vals = []
    for _ in range(C.N_RESAMPLES):
        amostra = []
        for _ in range(len(blocos)):
            amostra += blocos[rng.randrange(len(blocos))]
        vals.append(f(amostra))
    vals = [v for v in vals if v == v]
    vals.sort()
    a = ALFA_FAMILIA / N_TESTES / 2
    return vals[int(a * len(vals))], vals[int((1 - a) * len(vals)) - 1]


def brutos_reversao(series, k):
    """-retorno demeanado dos ultimos k dias, dividido pela vol."""
    idx = {i: {x["dia"]: x for x in s} for i, s in series.items()}
    dias = sorted({d for m in idx.values() for d in m})
    pos_por_inst = {i: sorted(m) for i, m in idx.items()}
    ordem = {i: {d: j for j, d in enumerate(ds)} for i, ds in pos_por_inst.items()}
    bruto = defaultdict(dict)
    for dia in dias:
        rets = {}
        for i, m in idx.items():
            j = ordem[i].get(dia)
            if j is None or j < k:
                continue
            ant = pos_por_inst[i][j - k]
            r = m[dia]["preco"] / m[ant]["preco"] - 1
            rets[i] = r / max(m[dia]["vol_a"], 1e-6)
        if len(rets) < 5:
            continue
        media = sum(rets.values()) / len(rets)
        for i, r in rets.items():
            bruto[dia][i] = -(r - media)
    return bruto


def brutos_lowvol(series):
    """-escore padronizado da volatilidade anual no dia."""
    idx = {i: {x["dia"]: x for x in s} for i, s in series.items()}
    dias = sorted({d for m in idx.values() for d in m})
    bruto = defaultdict(dict)
    for dia in dias:
        vols = {i: m[dia]["vol_a"] for i, m in idx.items() if dia in m}
        if len(vols) < 5:
            continue
        v = list(vols.values())
        media = sum(v) / len(v)
        dp = statistics.pstdev(v)
        if dp <= 0:
            continue
        for i, x in vols.items():
            bruto[dia][i] = -(x - media) / dp
    return bruto


def escala_de(bruto):
    v = [abs(x) for dia in bruto for x in bruto[dia].values()]
    m = sum(v) / len(v) if v else 0
    return 10.0 / m if m > 0 else 1.0


def aplica_escala(bruto, escala):
    fc = defaultdict(dict)
    for dia, vals in bruto.items():
        for i, x in vals.items():
            fc[dia][i] = max(-CAP, min(CAP, x * escala))
    return fc


def relatorio(nome, series, fc, decide):
    original = C.forecasts
    C.forecasts = lambda s, m: fc
    try:
        rets = C.simular(series, "x")
    finally:
        C.forecasts = original
    mkt = mercado(series)
    m = dict(mkt)
    sr = sharpe(rets)
    lo, hi = bootstrap_bonf(rets, sharpe)
    a = alfa(rets, mkt)
    alo, ahi = bootstrap_bonf([(d, r) for d, r in rets if d in m], lambda am: alfa(am, mkt))
    rr = sum(r for _, r in rets) / len(rets) * 365
    print(f"  {nome}: dias={len(rets)} | retorno {100*rr:+.1f}%/ano | Sharpe {sr:+.2f} | "
          f"IC98.33 [{lo:+.2f}, {hi:+.2f}]")
    print(f"    alfa {100*a:+.1f}%/ano | IC98.33 [{100*alo:+.1f}%, {100*ahi:+.1f}%] | "
          f"mercado {sharpe(mkt):+.2f}")
    return (lo > 0 and alo > 0) if decide else None


def carrega(universo):
    s = {}
    for inst in universo:
        try:
            x = serie_instrumento(inst)
        except Exception:
            continue
        if x:
            s[inst] = x
    return s


def main():
    alvo_d = universo_d()[:40] if "--rapido" in sys.argv else universo_d()
    A = carrega(list(UNIVERSO))
    D = carrega(alvo_d)
    print(f"amostra A: {len(A)} | amostra D: {len(D)}")

    testes = [
        ("3.9 reversao XS 1 dia ", lambda s: brutos_reversao(s, 1)),
        ("3.9 reversao XS 5 dias", lambda s: brutos_reversao(s, 5)),
        ("3.4 baixa volatilidade", lambda s: brutos_lowvol(s)),
    ]
    resultados = {}
    for nome, func in testes:
        print(f"\n{'='*100}\n{nome}\n{'='*100}")
        ba = func(A)
        escala = escala_de(ba)
        print(f"  escala estimada na amostra A: {escala:.2f}")
        relatorio("  A (desenvolvimento)", A, aplica_escala(ba, escala), decide=False)
        bd = func(D)
        resultados[nome] = relatorio("  D (DECIDE)         ", D, aplica_escala(bd, escala), decide=True)

    print(f"\n{'='*100}\nDECISAO (IC 98.33%, Bonferroni para {N_TESTES} testes)\n{'='*100}")
    for nome, ok in resultados.items():
        print(f"  {nome}: {'PASSA' if ok else 'NAO PASSA'}")


if __name__ == "__main__":
    main()
