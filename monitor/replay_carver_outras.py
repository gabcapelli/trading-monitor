"""
Teste PRE-REGISTRADO (22/09/2026) de mais tres estrategias do livro "Advanced
Futures Trading Strategies" (Robert Carver, 2023), adaptadas a perpetuos de
cripto, no mesmo arcabouco dos estudos 14 (carry) e 15 (skew):
  - Estrategia 19: momentum cross-sectional.
  - Estrategia 23: aceleracao (variacao do forecast de tendencia).
  - Estrategia 26: mean reversion rapida (equilibrio EWMA de 5 dias, dados
    horarios, SEM buffering -- regra explicita do livro).
  - Estrategia 27: a mesma, com filtro de tendencia ("safer").
Estudo avulso: NAO faz parte do checklist dos Setups A/B/C nem do monitor de
producao. [interp] = interpretacao/adaptacao minha.

O QUE O LIVRO REPORTA (referencia de sanidade, em futuros)
-----------------------------------------------------------
Aceleracao: SR 0.20-0.59 | Mean reversion rapida: SR 0.44-0.75 (dados
horarios desde 2013) | Skew (estudo 15): 0.60-0.75, e nos achamos +0.67 em
cripto, o que sugere que o arcabouco esta implementado certo.
Value (estrategia 22) NAO e testada: o proprio livro reporta SR -0.06 para
ela isolada, usando-a so com 5% de peso numa combinacao.

REGRAS
------
- Estrategia 19 (momentum cross-sectional): forecast EWMAC(N, 4N) para
  N em {16, 32, 64}, media das tres, menos a mediana do dia entre
  instrumentos. [interp] escala estimada do proprio dado (metodo do livro:
  escala = 10 / media do valor absoluto do forecast bruto, calculada na
  amostra de desenvolvimento A e FIXADA antes de rodar em D).
- Estrategia 23 (aceleracao): forecast EWMAC(N,4N) escalado menos o mesmo
  forecast N dias atras, para N em {16, 32, 64}, media das tres. Escala pelo
  mesmo metodo. O livro descarta N=2 e N=4 por custo.
- Estrategia 26 (mean reversion rapida): equilibrio = EWMA(span 5) dos
  fechamentos DIARIOS; forecast horario = (equilibrio - preco) / vol diaria
  em unidades de preco; escala 9.3; limite +-20; SEM buffering.
- Estrategia 27: igual a 26, mas so aceita forecast a favor da tendencia de
  longo prazo (EWMAC(64,256) do mesmo instrumento); contra a tendencia, a
  posicao e zero [interp: o livro usa um filtro de tendencia; a forma exata
  varia, esta e a leitura mais simples].
- Volatilidade, dimensionamento, custo (0.06% do nocional), limites de
  implementacao e funding: identicos aos estudos 14 e 15.

AMOSTRAS
--------
- A (20 pares): desenvolvimento -- so aqui se estimam as escalas de forecast.
- D: validacao. Para 19 e 23 (dados diarios), os 215 pares. Para 26 e 27
  (dados horarios), uma SUBAMOSTRA de 60 pares sorteada com semente fixa
  ANTES de baixar os dados (baixar 1H dos 215 seria ~1 GB).

CRITERIO DE DECISAO (pre-registrado, com correcao de multiplicidade)
---------------------------------------------------------------------
Sao QUATRO testes na mesma amostra D. Para manter 5% de erro no conjunto,
cada teste usa IC de 98.75% (Bonferroni: 0.05/4), nao 95%. Cada estrategia
PASSA se, na amostra D:
1. Sharpe liquido > 0 com IC98.75 inteiro acima de zero (bootstrap por
   blocos de semana); E
2. alfa contra a carteira equal-weight > 0 com IC98.75 acima de zero.
A amostra A nao decide nada.
"""

import math
import statistics
import sys
from collections import defaultdict

import replay_carver_carry as C
from replay_carver_carry import (
    serie_instrumento, mercado, sharpe, alfa, ewma, CAP, UNIVERSO, universo_d,
)

ALFA_FAMILIA = 0.05
N_TESTES = 4
SPANS = [16, 32, 64]
SPAN_EQ = 5
ESCALA_MR = 9.3
SUBAMOSTRA_D = 60


def bootstrap_bonf(rets, f):
    """Como bootstrap_semana, mas com IC de 98.75% (0.05/4)."""
    import random
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


def ewmac_forecast(precos, vols_a, n):
    """EWMAC(n, 4n) normalizado pela vol diaria em unidades de preco."""
    rap, len_ = ewma(precos, n), ewma(precos, 4 * n)
    out = []
    for i in range(len(precos)):
        vol_preco = vols_a[i] / 16 * precos[i]
        out.append((rap[i] - len_[i]) / vol_preco if vol_preco > 0 else 0.0)
    return out


def escala_para_dez(valores):
    """Metodo do livro: escala = 10 / media do |forecast| bruto."""
    v = [abs(x) for x in valores if x == x]
    m = sum(v) / len(v) if v else 0
    return 10.0 / m if m > 0 else 1.0


def forecasts_momentum(series, escala, acelera):
    fc = defaultdict(dict)
    brutos = []
    for inst, s in series.items():
        precos = [x["preco"] for x in s]
        vols = [x["vol_a"] for x in s]
        partes = []
        for n in SPANS:
            f = ewmac_forecast(precos, vols, n)
            if acelera:
                f = [f[i] - f[i - n] if i >= n else 0.0 for i in range(len(f))]
            partes.append(f)
        comb = [sum(p[i] for p in partes) / len(partes) for i in range(len(s))]
        brutos += comb
        for i, x in enumerate(s):
            fc[x["dia"]][inst] = comb[i]
    if escala is None:
        escala = escala_para_dez(brutos)
    out = defaultdict(dict)
    for dia, vals in fc.items():
        if len(vals) < 3:
            continue
        med = statistics.median(vals.values()) if not acelera else 0.0
        for inst, v in vals.items():
            out[dia][inst] = max(-CAP, min(CAP, (v - med) * escala))
    return out, escala


def relatorio(nome, series, fc_func, decide, titulo_extra=""):
    original = C.forecasts
    C.forecasts = lambda s, m: fc_func
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
    rot = "IC98.75" if decide else "IC98.75"
    print(f"  {nome}{titulo_extra}: dias={len(rets)} | retorno {100*rr:+.1f}%/ano | "
          f"Sharpe {sr:+.2f} | {rot} [{lo:+.2f}, {hi:+.2f}]")
    print(f"    alfa vs mercado {100*a:+.1f}%/ano | {rot} [{100*alo:+.1f}%, {100*ahi:+.1f}%] | "
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
    rapido = "--rapido" in sys.argv
    alvo_d = universo_d()[:40] if rapido else universo_d()
    A = carrega(list(UNIVERSO))
    D = carrega(alvo_d)
    print(f"amostra A: {len(A)} | amostra D: {len(D)}")

    resultados = {}
    for acelera, rot in ((False, "19 momentum cross-sectional"), (True, "23 aceleracao")):
        fa, escala = forecasts_momentum(A, None, acelera)
        print(f"\n{'='*100}\n{rot}\n{'='*100}")
        print(f"  escala estimada na amostra A: {escala:.2f}")
        relatorio("  A (desenvolvimento)", A, fa, decide=False)
        fd, _ = forecasts_momentum(D, escala, acelera)
        resultados[rot] = relatorio("  D (DECIDE)         ", D, fd, decide=True)

    print(f"\n{'='*100}\nDECISAO (IC 98.75%, Bonferroni para {N_TESTES} testes)\n{'='*100}")
    for rot, ok in resultados.items():
        print(f"  {rot}: {'PASSA' if ok else 'NAO PASSA'}")
    print("\n  (estrategias 26 e 27, mean reversion horaria, rodam em replay_carver_mr.py)")


if __name__ == "__main__":
    main()
