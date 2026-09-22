"""
Teste PRE-REGISTRADO (22/09/2026) do "momentum de qualidade" de
*Quantitative Momentum* (Wesley Gray & Jack Vogel, 2016), adaptado ao corte
transversal de perpetuos de cripto. Estudo avulso: NAO faz parte do
checklist dos Setups A/B/C nem do monitor de producao. [interp] = adaptacao.

A TESE (do livro)
------------------
Nem todo momentum e igual. Alta construida aos trancos (poucos dias enormes)
vem de atencao/loteria e reverte; alta construida devagar, com muitos dias
pequenos positivos, passa despercebida e continua. O livro mede isso com o
"frog in the pan" (Da, Gurun & Warachka, 2014):
    FIP = sinal(retorno passado) x (% dias negativos - % dias positivos)
Quanto MENOR o FIP, mais suave foi o caminho -- e melhor o momentum.

REGRAS
------
- Momentum: retorno dos ultimos 252 dias IGNORANDO os ultimos 21 ("12-2" do
  livro, em dias de cripto, que nao tem pregao) [interp].
- FIP: sobre os mesmos 252 dias.
- Corte transversal, rebalanceado a cada 21 dias (o livro usa mensal/
  trimestral), mantendo o forecast fixo entre rebalanceamentos:
  "puro"     : forecast = escore padronizado do momentum.
  "qualidade": dentro do quintil superior de momentum, compra os de MENOR
               FIP; dentro do quintil inferior, vende os de MAIOR FIP; o
               resto fica zerado [interp: o livro e long-only e usa decil;
               aqui usamos quintil e os dois lados, para ficar neutro].
- Escala do forecast estimada na amostra A (10 / media do |bruto|), limite
  +-20. Dimensionamento, custo (0.06%), buffering, limites e funding:
  identicos aos estudos 14-17.

AMOSTRAS E CRITERIO (pre-registrado)
-------------------------------------
A (20 pares) desenvolvimento; D (215 perps so da Binance) DECIDE.
Dois testes na mesma amostra -> IC de 97.5% (Bonferroni 0.05/2).
PASSA se, na amostra D: Sharpe com IC97.5 acima de zero E alfa contra a
carteira equal-weight com IC97.5 acima de zero.
Sanidade: o livro reporta ~1.5-3 pontos de retorno anual a mais para o
momentum de qualidade sobre o momentum puro em acoes; em cripto, esperar
menos. O controle ("puro") existe para medir se o FIP acrescenta algo.
"""

import random
import statistics
import sys
from collections import defaultdict

import replay_carver_carry as C
from replay_carver_carry import (
    serie_instrumento, mercado, sharpe, alfa, CAP, UNIVERSO, universo_d,
)

JANELA = 252
PULO = 21
REBAL = 21
ALFA_FAMILIA = 0.05
N_TESTES = 2


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


def momento_e_fip(s):
    """Por indice do dia: (momentum 252-21, FIP)."""
    precos = [x["preco"] for x in s]
    rets = [0.0] + [precos[i] / precos[i - 1] - 1 for i in range(1, len(precos))]
    out = [None] * len(s)
    for i in range(JANELA, len(s)):
        ini = i - JANELA
        fim = i - PULO
        if fim <= ini:
            continue
        mom = precos[fim] / precos[ini] - 1
        janela = rets[ini + 1:i + 1]
        pos = sum(1 for r in janela if r > 0) / len(janela)
        neg = sum(1 for r in janela if r < 0) / len(janela)
        fip = (1 if mom > 0 else -1) * (neg - pos)
        out[i] = (mom, fip)
    return out


def brutos(series, qualidade):
    dados = {i: momento_e_fip(s) for i, s in series.items()}
    idx = {i: {x["dia"]: j for j, x in enumerate(s)} for i, s in series.items()}
    dias = sorted({x["dia"] for s in series.values() for x in s})
    bruto = defaultdict(dict)
    atual = {}
    for n, dia in enumerate(dias):
        if n % REBAL == 0:
            vals = {}
            for i, s in series.items():
                j = idx[i].get(dia)
                if j is None or dados[i][j] is None:
                    continue
                vals[i] = dados[i][j]
            if len(vals) >= 10:
                moms = sorted(vals.items(), key=lambda x: x[1][0])
                n_q = max(len(moms) // 5, 1)
                if not qualidade:
                    m = [v[0] for _, v in vals.items()]
                    med, dp = sum(m) / len(m), statistics.pstdev(m)
                    atual = {i: (v[0] - med) / dp for i, v in vals.items()} if dp > 0 else {}
                else:
                    baixo = moms[:n_q]        # piores em momentum
                    alto = moms[-n_q:]        # melhores em momentum
                    # dentro dos melhores: compra os de MENOR fip (caminho suave)
                    alto_ord = sorted(alto, key=lambda x: x[1][1])
                    baixo_ord = sorted(baixo, key=lambda x: -x[1][1])
                    metade = max(len(alto_ord) // 2, 1)
                    atual = {}
                    for i, _ in alto_ord[:metade]:
                        atual[i] = 1.0
                    for i, _ in baixo_ord[:metade]:
                        atual[i] = -1.0
        for i, v in atual.items():
            if dia in idx[i]:
                bruto[dia][i] = v
    return bruto


def escala_de(bruto):
    v = [abs(x) for dia in bruto for x in bruto[dia].values()]
    m = sum(v) / len(v) if v else 0
    return 10.0 / m if m > 0 else 1.0


def aplica(bruto, escala):
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
          f"IC97.5 [{lo:+.2f}, {hi:+.2f}]")
    print(f"    alfa {100*a:+.1f}%/ano | IC97.5 [{100*alo:+.1f}%, {100*ahi:+.1f}%] | "
          f"mercado {sharpe(mkt):+.2f}")
    return (lo > 0 and alo > 0) if decide else None


def carrega(universo):
    s = {}
    for inst in universo:
        try:
            x = serie_instrumento(inst)
        except Exception:
            continue
        if x and len(x) > JANELA + 30:
            s[inst] = x
    return s


def main():
    alvo_d = universo_d()[:40] if "--rapido" in sys.argv else universo_d()
    A = carrega(list(UNIVERSO))
    D = carrega(alvo_d)
    print(f"amostra A: {len(A)} | amostra D: {len(D)}")
    resultados = {}
    for qualidade, rot in ((False, "momentum XS puro (controle)"), (True, "momentum de qualidade (FIP)")):
        print(f"\n{'='*100}\n{rot}\n{'='*100}")
        ba = brutos(A, qualidade)
        esc = escala_de(ba)
        print(f"  escala estimada na amostra A: {esc:.2f}")
        relatorio("  A (desenvolvimento)", A, aplica(ba, esc), decide=False)
        bd = brutos(D, qualidade)
        resultados[rot] = relatorio("  D (DECIDE)         ", D, aplica(bd, esc), decide=True)
    print(f"\n{'='*100}\nDECISAO (IC 97.5%, Bonferroni para {N_TESTES} testes)\n{'='*100}")
    for rot, ok in resultados.items():
        print(f"  {rot}: {'PASSA' if ok else 'NAO PASSA'}")


if __name__ == "__main__":
    main()
