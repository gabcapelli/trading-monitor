"""
Teste PRE-REGISTRADO (22/09/2026) da estrategia 24 (SKEW) do livro "Advanced
Futures Trading Strategies" (Robert Carver, 2023), adaptada a perpetuos de
cripto. Estudo avulso: NAO faz parte do checklist dos Setups A/B/C nem do
monitor de producao. [interp] = interpretacao/adaptacao minha.

A TESE (do livro)
------------------
Investidor gosta de ativo com skew positiva (loteria: perde pouco quase
sempre, ganha muito de vez em quando) e detesta skew negativa. Quem aceita
carregar skew negativa deveria ser pago por isso. Logo: comprar o que teve
skew NEGATIVA recente, vender o que teve skew positiva.
Em cripto isso e testavel e interessante porque memecoin e o caso extremo de
ativo-loteria.

REGRAS (parametros do livro)
-----------------------------
- Skew dos retornos percentuais diarios em janela w (60, 120 ou 240 dias):
  skew = media((r - media(r))^3) / desvio(r)^3.
- Forecast bruto = -skew (sinal invertido: skew negativa -> compra).
- Suavizacao: EWMA com span = w / 4 (regra do livro: "um quarto da janela").
- Escala: 33.3 (skew60), 37.2 (skew120), 39.2 (skew240); limite +-20.
- Primaria: media dos tres forecasts (o livro combina variacoes de
  velocidade; peso igual, FDM = 1.0 [interp: conservador]).
- Descritiva: skew CROSS-SECTIONAL -- forecast menos a mediana do dia entre
  instrumentos, reescalado pela mesma escala [interp: o livro cita a versao
  relativa mas nao da escala propria].
- Volatilidade, dimensionamento de posicao, buffering, limites de
  implementacao (aquecimento 60 dias, piso de vol, teto de 1x por
  instrumento e 3x bruto) e custo: identicos ao replay_carver_carry.py.
- Funding pago/recebido na simulacao, como no estudo de carry.

DADOS E AMOSTRAS
-----------------
Precos diarios e funding da Binance.
- Amostra A (20 pares): desenvolvimento, nao decide.
- Amostra D (215 perps so da Binance): DECIDE.
Ressalva registrada: esta e a TERCEIRA vez que a amostra D e usada (antes:
varredura do 1-2-3 e carry do Carver). Cada reuso a desgasta. Como cada uso
foi para uma estrategia diferente, e como o criterio exige DUAS condicoes
independentes (Sharpe e alfa), o risco de falso positivo acumulado ainda e
baixo -- mas depois deste estudo a amostra limpa restante e so o paper trade.

CRITERIO DE DECISAO (pre-registrado)
------------------------------------
Na amostra D, com os parametros do livro e sem varredura:
1. Sharpe anualizado liquido > 0 com IC95 inteiro acima de zero (bootstrap
   por blocos de semana).
2. Alfa contra a carteira equal-weight dos mesmos pares > 0 com IC95 acima
   de zero.
PASSA so se 1 e 2 valerem.
Sanidade: o livro reporta Sharpe em torno de 0.3-0.6 para skew isolada em
futuros. Resultado muito acima disso e suspeita de erro, nao descoberta.
"""

import statistics
import sys
from collections import defaultdict

from replay_carver_carry import (
    serie_instrumento, simular, mercado, sharpe, bootstrap_semana, alfa, ewma,
    CAP, UNIVERSO, universo_d,
)

JANELAS = [(60, 33.3), (120, 37.2), (240, 39.2)]


def skew_janela(rets, w):
    """Skew amostral dos ultimos w retornos, por dia (None ate ter janela)."""
    out = [None] * len(rets)
    for i in range(w - 1, len(rets)):
        j = rets[i - w + 1:i + 1]
        m = sum(j) / w
        dp = statistics.pstdev(j)
        if dp <= 0:
            continue
        out[i] = sum((x - m) ** 3 for x in j) / w / dp ** 3
    return out


def forecasts_skew(series, modo):
    """{dia: {inst: forecast}} -- 'combinada' (media das 3 janelas) ou 'xs'."""
    fc_inst = {}
    for inst, s in series.items():
        precos = [x["preco"] for x in s]
        rets = [0.0] + [precos[i] / precos[i - 1] - 1 for i in range(1, len(precos))]
        partes = []
        for w, escala in JANELAS:
            sk = skew_janela(rets, w)
            base = [(-x if x is not None else 0.0) for x in sk]
            suav = ewma(base, max(w // 4, 2))
            partes.append([(None if sk[i] is None else max(-CAP, min(CAP, suav[i] * escala)))
                           for i in range(len(sk))])
        comb = []
        for i in range(len(s)):
            vals = [p[i] for p in partes if p[i] is not None]
            comb.append(sum(vals) / len(vals) if vals else None)
        fc_inst[inst] = {s[i]["dia"]: comb[i] for i in range(len(s)) if comb[i] is not None}
    fc = defaultdict(dict)
    for inst, porc in fc_inst.items():
        for dia, v in porc.items():
            fc[dia][inst] = v
    if modo == "combinada":
        return fc
    fc_xs = defaultdict(dict)
    for dia, vals in fc.items():
        if len(vals) < 3:
            continue
        med = statistics.median(vals.values())
        for inst, v in vals.items():
            fc_xs[dia][inst] = max(-CAP, min(CAP, v - med))
    return fc_xs


def relatorio(nome, series, modo, decide):
    import replay_carver_carry as C
    original = C.forecasts
    C.forecasts = lambda s, m: forecasts_skew(s, modo)   # injeta o forecast de skew
    try:
        rets = simular(series, modo)
    finally:
        C.forecasts = original
    mkt = mercado(series)
    sr = sharpe(rets)
    lo, hi = bootstrap_semana(rets, sharpe)
    m = dict(mkt)
    a = alfa(rets, mkt)
    alo, ahi = bootstrap_semana([(d, r) for d, r in rets if d in m], lambda am: alfa(am, mkt))
    ret_anual = sum(r for _, r in rets) / len(rets) * 365
    print(f"  {nome}: dias={len(rets)} | retorno {100*ret_anual:+.1f}%/ano | "
          f"Sharpe {sr:+.2f} | IC95 [{lo:+.2f}, {hi:+.2f}]")
    print(f"    alfa vs mercado {100*a:+.1f}%/ano | IC95 [{100*alo:+.1f}%, {100*ahi:+.1f}%] | "
          f"Sharpe do mercado {sharpe(mkt):+.2f}")
    return (lo > 0 and alo > 0) if decide else None


def main():
    alvo_d = universo_d()
    if "--rapido" in sys.argv:
        alvo_d = alvo_d[:40]
    series = {}
    for nome, universo in (("A", list(UNIVERSO)), ("D", alvo_d)):
        s = {}
        for inst in universo:
            try:
                x = serie_instrumento(inst)
            except Exception:
                continue
            if x:
                s[inst] = x
        series[nome] = s
        print(f"amostra {nome}: {len(s)} instrumentos")

    print(f"\n{'='*100}\nAMOSTRA A (20 pares) -- desenvolvimento, nao decide\n{'='*100}")
    for modo, rot in (("combinada", "skew combinada (60/120/240)"), ("xs", "skew cross-sectional")):
        relatorio(rot, series["A"], modo, decide=False)

    print(f"\n{'='*100}\nAMOSTRA D ({len(series['D'])} pares) -- DECIDE\n{'='*100}")
    oks = {}
    for modo, rot in (("combinada", "skew combinada (60/120/240)"), ("xs", "skew cross-sectional")):
        oks[rot] = relatorio(rot, series["D"], modo, decide=True)
    for rot, ok in oks.items():
        print(f"\n==> DECISAO {rot}: {'PASSA' if ok else 'NAO PASSA'}")


if __name__ == "__main__":
    main()
