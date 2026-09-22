"""
Teste PRE-REGISTRADO (22/09/2026) de um COMBO de tres premios de risco
transversais em perpetuos de cripto. Estudo avulso: NAO faz parte do
checklist dos Setups A/B/C nem do monitor de producao.

DE ONDE VEM A HIPOTESE (e por que nao e garimpo)
-------------------------------------------------
Tres estrategias ja testadas, de fontes diferentes, deram o mesmo sinal
fraco e positivo na amostra D, e todas medem a MESMA ideia economica --
comprar o ativo "chato" e vender o "loteria":
  - skew cross-sectional (Carver, estudo 15):        Sharpe +0.67
  - baixa volatilidade (Kakushadze 3.4, estudo 17):  Sharpe +0.49
  - carry cross-sectional (Carver 20, estudo 14):    Sharpe +0.30
Nenhuma passou sozinha: com ~6 anos de dados, Sharpe abaixo de ~0.8 nao e
distinguivel de zero. A hipotese aqui NAO e um parametro novo, e sim que os
tres sao medidas ruidosas do mesmo premio; combinadas, o ruido idiossincratico
se cancela e a razao sinal/ruido sobe. E a "alpha combo" do capitulo 3.20 de
Kakushadze & Serur e o metodo de combinacao de forecasts do Carver.

REGRAS
------
- Cada componente vira um forecast transversal padronizado (media zero no
  dia, escala fixada na amostra A pelo metodo do Carver: 10 / media do
  |bruto|), limitado a +-20:
  - skew: -skew(60/120/240d) suavizada, menos a mediana do dia (estudo 15).
  - baixa vol: -escore padronizado da vol anual do dia (estudo 17).
  - carry: -funding anualizado / vol, menos a mediana do dia, suavizado em
    90 dias (estudo 14).
- Combo = media simples dos tres forecasts disponiveis no dia (peso igual;
  SEM otimizacao de pesos, que seria ajuste a dados), limitado a +-20.
- Dimensionamento, custo (0.06%), buffering, limites e funding: identicos
  aos estudos 14-17.

AMOSTRA QUE DECIDE (nova para esta familia)
--------------------------------------------
Universo E: os 153 perpetuos da Binance que correspondem aos pares OKX dos
universos B e C, excluindo A e D (lista em `monitor/universo_e.txt`,
congelada antes de baixar precos). B e C foram usados em estudos de price
action (1-2-3, inside bar, Landry, 123 de candles), NUNCA nestas estrategias
de carteira -- e nenhum componente deste combo os viu.
A e D entram so como descritivo (foi neles que a hipotese nasceu).

CRITERIO DE DECISAO (pre-registrado)
------------------------------------
Um unico teste, no universo E:
1. Sharpe liquido > 0 com IC95 inteiro acima de zero (bootstrap por blocos
   de semana); E
2. alfa contra a carteira equal-weight > 0 com IC95 acima de zero.
PASSA so se 1 e 2 valerem. Os tres componentes isolados em E sao reportados
como descritivo (para saber se o combo ganha de cada parte), sem poder de
decisao.
"""

import statistics
import sys
from collections import defaultdict

import replay_carver_carry as C
import replay_carver_skew as SK
import replay_k151 as K
from replay_carver_carry import (
    serie_instrumento, mercado, sharpe, alfa, bootstrap_semana, CAP, UNIVERSO, universo_d,
)


def universo_e():
    import os
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "universo_e.txt")
    with open(p) as f:
        return [l.strip() for l in f if l.strip()]


def bruto_skew(series):
    fc = SK.forecasts_skew(series, "xs")
    return {d: dict(v) for d, v in fc.items()}


def bruto_carry(series):
    fc = C.forecasts(series, "20")
    return {d: dict(v) for d, v in fc.items()}


def bruto_lowvol(series):
    return K.brutos_lowvol(series)


def padroniza(bruto, escala):
    out = defaultdict(dict)
    for dia, vals in bruto.items():
        for i, x in vals.items():
            out[dia][i] = max(-CAP, min(CAP, x * escala))
    return out


def escala_de(bruto):
    v = [abs(x) for dia in bruto for x in bruto[dia].values()]
    m = sum(v) / len(v) if v else 0
    return 10.0 / m if m > 0 else 1.0


def combina(partes):
    dias = set()
    for p in partes:
        dias |= set(p)
    fc = defaultdict(dict)
    for dia in dias:
        insts = set()
        for p in partes:
            insts |= set(p.get(dia, {}))
        for i in insts:
            vals = [p[dia][i] for p in partes if i in p.get(dia, {})]
            if vals:
                fc[dia][i] = max(-CAP, min(CAP, sum(vals) / len(vals)))
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
    lo, hi = bootstrap_semana(rets, sharpe)
    a = alfa(rets, mkt)
    alo, ahi = bootstrap_semana([(d, r) for d, r in rets if d in m], lambda am: alfa(am, mkt))
    rr = sum(r for _, r in rets) / len(rets) * 365
    print(f"  {nome}: dias={len(rets)} | retorno {100*rr:+.1f}%/ano | Sharpe {sr:+.2f} | "
          f"IC95 [{lo:+.2f}, {hi:+.2f}]")
    print(f"    alfa {100*a:+.1f}%/ano | IC95 [{100*alo:+.1f}%, {100*ahi:+.1f}%] | "
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


def partes_de(series, escalas=None):
    crus = {"skew": bruto_skew(series), "lowvol": bruto_lowvol(series), "carry": bruto_carry(series)}
    if escalas is None:
        escalas = {k: escala_de(v) for k, v in crus.items()}
    return {k: padroniza(v, escalas[k]) for k, v in crus.items()}, escalas


def correlacao_componentes(partes):
    """Correlacao media entre os forecasts dos componentes (diagnostico)."""
    nomes = list(partes)
    pares = []
    for a in range(len(nomes)):
        for b in range(a + 1, len(nomes)):
            xa, xb = partes[nomes[a]], partes[nomes[b]]
            v1, v2 = [], []
            for dia in set(xa) & set(xb):
                for i in set(xa[dia]) & set(xb[dia]):
                    v1.append(xa[dia][i])
                    v2.append(xb[dia][i])
            if len(v1) > 100:
                m1, m2 = sum(v1) / len(v1), sum(v2) / len(v2)
                s1, s2 = statistics.pstdev(v1), statistics.pstdev(v2)
                if s1 > 0 and s2 > 0:
                    cov = sum((v1[i] - m1) * (v2[i] - m2) for i in range(len(v1))) / len(v1)
                    pares.append((f"{nomes[a]} x {nomes[b]}", cov / (s1 * s2)))
    return pares


def main():
    rapido = "--rapido" in sys.argv
    A = carrega(list(UNIVERSO))
    E = carrega(universo_e()[:40] if rapido else universo_e())
    print(f"amostra A: {len(A)} | amostra E: {len(E)}")

    partes_a, escalas = partes_de(A)
    print("\n  escalas estimadas na amostra A:", {k: round(v, 2) for k, v in escalas.items()})
    print("  correlacao entre componentes (amostra A):")
    for nome, c in correlacao_componentes(partes_a):
        print(f"    {nome}: {c:+.2f}")

    print(f"\n{'='*100}\nAMOSTRA A (desenvolvimento, nao decide)\n{'='*100}")
    relatorio("combo (3 premios)", A, combina(list(partes_a.values())), decide=False)

    print(f"\n{'='*100}\nAMOSTRA E ({len(E)} pares novos) -- DECIDE\n{'='*100}")
    partes_e, _ = partes_de(E, escalas)
    ok = relatorio("combo (3 premios)", E, combina(list(partes_e.values())), decide=True)
    print("\n  componentes isolados em E (descritivo):")
    for nome, p in partes_e.items():
        relatorio(f"  {nome:<8}", E, p, decide=False)

    print(f"\n==> DECISAO combo: {'PASSA' if ok else 'NAO PASSA'}")


if __name__ == "__main__":
    main()
