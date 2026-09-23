"""
Teste PRE-REGISTRADO (22/09/2026) do TREND FOLLOWING CANONICO -- estrategia 9
do Carver ("multiple trend following rules"), direcional, dimensionado por
volatilidade, em carteira. Estudo avulso.

POR QUE, DEPOIS DE TANTA TENDENCIA JA TESTADA
----------------------------------------------
Os 11 estudos de video testaram tendencia com stop e alvo (medida em R por
trade). O estudo 16 testou momentum CROSS-SECTIONAL (19) e aceleracao (23).
Faltou a forma canonica: posicao continua e direcional, combinando varias
velocidades de EWMAC, com alvo de risco -- o que o livro chama de estrategia
9 e e a base da industria de managed futures. Este estudo fecha esse buraco.

REGRAS (do livro)
-----------------
- Forecast EWMAC(N, 4N) normalizado pela vol, para N em {8, 16, 32, 64}
  (as velocidades que o livro considera negociaveis em ativos com custo
  como o de cripto), media simples das quatro.
- Escala estimada na amostra A pelo metodo do livro (10 / media do |bruto|),
  limite +-20. SEM subtrair mediana: aqui a aposta e direcional.
- Dimensionamento, custo, buffering, limites e funding: identicos aos
  estudos 14-19.

AMOSTRAS E CRITERIO (pre-registrado)
-------------------------------------
A (20 pares) desenvolvimento; E (153 pares) DECIDE -- nunca usada para
tendencia direcional. Teste unico, IC95.
PASSA se na amostra E: Sharpe > 0 com IC95 acima de zero E alfa contra a
carteira equal-weight > 0 com IC95 acima de zero (o alfa e essencial aqui:
uma carteira que fica comprada na maior parte do tempo herda a alta do
mercado, e isso nao e edge).
"""
import sys
from collections import defaultdict

import replay_carver_carry as C
from replay_carver_carry import (serie_instrumento, mercado, sharpe, alfa,
                                 bootstrap_semana, CAP, UNIVERSO)
from replay_carver_outras import ewmac_forecast, escala_para_dez
from replay_combo_premios import universo_e

SPANS = [8, 16, 32, 64]


def brutos(series):
    fc, todos = defaultdict(dict), []
    for inst, s in series.items():
        precos = [x["preco"] for x in s]
        vols = [x["vol_a"] for x in s]
        partes = [ewmac_forecast(precos, vols, n) for n in SPANS]
        comb = [sum(p[i] for p in partes) / len(partes) for i in range(len(s))]
        todos += comb
        for i, x in enumerate(s):
            fc[x["dia"]][inst] = comb[i]
    return fc, todos


def aplica(fc, escala):
    out = defaultdict(dict)
    for dia, vals in fc.items():
        for i, v in vals.items():
            out[dia][i] = max(-CAP, min(CAP, v * escala))
    return out


def relatorio(nome, series, fc, decide):
    orig = C.forecasts
    C.forecasts = lambda s, m: fc
    try:
        rets = C.simular(series, "x")
    finally:
        C.forecasts = orig
    mkt = mercado(series); m = dict(mkt)
    sr = sharpe(rets); lo, hi = bootstrap_semana(rets, sharpe)
    a = alfa(rets, mkt)
    alo, ahi = bootstrap_semana([(d, r) for d, r in rets if d in m], lambda am: alfa(am, mkt))
    rr = sum(r for _, r in rets) / len(rets) * 365
    print(f"  {nome}: dias={len(rets)} | retorno {100*rr:+.1f}%/ano | Sharpe {sr:+.2f} | IC95 [{lo:+.2f}, {hi:+.2f}]")
    print(f"    alfa {100*a:+.1f}%/ano | IC95 [{100*alo:+.1f}%, {100*ahi:+.1f}%] | mercado {sharpe(mkt):+.2f}")
    return (lo > 0 and alo > 0) if decide else None


def carrega(u):
    s = {}
    for inst in u:
        try:
            x = serie_instrumento(inst)
        except Exception:
            continue
        if x:
            s[inst] = x
    return s


def main():
    alvo = universo_e()[:40] if "--rapido" in sys.argv else universo_e()
    A = carrega(list(UNIVERSO)); E = carrega(alvo)
    print(f"amostra A: {len(A)} | amostra E: {len(E)}")
    fa, todos = brutos(A)
    esc = escala_para_dez(todos)
    print(f"escala estimada em A: {esc:.2f}")
    print(f"\n{'='*100}\nAMOSTRA A (desenvolvimento)\n{'='*100}")
    relatorio("trend canonico", A, aplica(fa, esc), decide=False)
    fe, _ = brutos(E)
    print(f"\n{'='*100}\nAMOSTRA E -- DECIDE\n{'='*100}")
    ok = relatorio("trend canonico", E, aplica(fe, esc), decide=True)
    print(f"\n==> DECISAO trend following canonico: {'PASSA' if ok else 'NAO PASSA'}")


if __name__ == "__main__":
    main()
