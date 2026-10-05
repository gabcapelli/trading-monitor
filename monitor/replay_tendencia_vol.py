"""
Estudo 43 -- comprado em BTC/ETH com freio: filtro de tendencia e alvo de
volatilidade. PRE-REGISTRADO em 05/10/2026, antes de rodar.

O QUE ESTE ESTUDO E (E NAO E)
----------------------------
Nao procura vantagem sobre o mercado (os estudos 22 e 34 ja mostraram que
tendencia nao bate comprar e segurar no excesso). Pergunta outra coisa, ligada
ao perfil do Gabriel (05/10/2026: meta 20-50%/ano, aguenta queda de 50%):
da para ficar com boa parte do retorno do mercado com bem menos queda? E uma
aposta no mercado com freio, nao uma vantagem.

DADOS
-----
- Fechamento diario do SPOT BTCUSDT/ETHUSDT da Binance (data.binance.vision),
  desde 08/2017 (inicio do historico).
- Janela que decide: 03/2021 a hoje (a mesma do estudo 42; inclui o topo de
  2021, 2022 inteiro e a lateralidade de 2025-26). Historico inteiro desde
  2017 como confirmacao.

VARIANTES (canonicas, sem otimizar; 3 por moeda)
------------------------------------------------
- T: TENDENCIA -- comprado 100% se o fechamento > media de 200 dias; caixa se nao.
- V: VOLATILIDADE -- posicao = min(1, 40% / vol realizada de 30 dias), sempre
  comprado, sem alavancagem.
- TV: as duas -- posicao de V quando o filtro de T esta ligado, caixa se nao.
- Execucao: sinal no fechamento do dia d, negociado no fechamento de d+1
  (um dia de atraso, folgado para o workflow horario). Custo 0.1% sobre o
  valor negociado (taxa de spot). Caixa rende ZERO (stablecoin a ~4% fica de
  fora; descritivo a parte).
- Referencia: comprar e segurar (BH).

CRITERIO (fixado antes)
-----------------------
Uma variante "SERVE" para o perfil se, na janela que decide E no historico
inteiro:
  (a) queda maxima <= 50%; e
  (b) retorno anual composto >= 70% do de comprar e segurar.
"ATENDE A META" se, alem disso, o retorno anual na janela que decide for
>= 20%.
Sem teste de significancia: e comparacao de perfil de risco num unico caminho
historico, e o log diz isso. Ressalva fixa: um caminho so, poucos ciclos de
mercado (2 a 3 grandes quedas).

DESCRITIVOS
-----------
- Por ano; exposicao media; numero de trocas; caixa a 4%/ano.

Uso (de dentro de monitor/):
    python replay_tendencia_vol.py
"""

import math
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone

import replay_deslistagem as D

DIA = 86_400_000
INICIO_DECIDE = int(datetime(2021, 3, 24, tzinfo=timezone.utc).timestamp() * 1000)
INICIO_HIST = int(datetime(2017, 8, 17, tzinfo=timezone.utc).timestamp() * 1000)
CUSTO = 0.001
ALVO_VOL = 0.40
MM = 200
JANELA_VOL = 30


def fechamentos(moeda):
    agora = int(time.time() * 1000)
    k = D.klines("spot", f"{moeda}USDT", INICIO_HIST, agora)
    out = {}
    for ts in sorted(k):
        out[ts // DIA * DIA] = k[ts][3]
    hoje = agora // DIA * DIA
    out.pop(hoje, None)           # dia corrente ainda nao fechou
    return out


def posicoes(dias, px, variante):
    alvo = {}
    for i, d in enumerate(dias):
        if i < MM:
            continue
        mm = sum(px[x] for x in dias[i - MM + 1:i + 1]) / MM
        r = [math.log(px[dias[j]] / px[dias[j - 1]]) for j in range(i - JANELA_VOL + 1, i + 1)]
        vol = math.sqrt(sum(x * x for x in r) / len(r) * 365)
        tend = px[d] > mm
        v = min(1.0, ALVO_VOL / vol) if vol > 0 else 1.0
        alvo[d] = {"BH": 1.0, "T": 1.0 if tend else 0.0, "V": v, "TV": v if tend else 0.0}[variante]
    return alvo


def simular(dias, px, alvo, t0, caixa_aa=0.0):
    """Curva de patrimonio a partir de t0. Posicao decidida em d vale de d+1 a d+2."""
    ds = [d for d in dias if d >= t0 and d in alvo]
    curva, pos, trocas, expo = [1.0], 0.0, 0, []
    for a, b in zip(ds, ds[1:]):
        # no fechamento de a executa o alvo decidido em a-1 (1 dia de atraso)
        novo = alvo.get(a - DIA, pos)
        if abs(novo - pos) > 1e-9:
            curva[-1] *= 1 - CUSTO * abs(novo - pos)
            trocas += 1
        pos = novo
        r = px[b] / px[a] - 1
        curva.append(curva[-1] * (1 + pos * r + (1 - pos) * caixa_aa / 365))
        expo.append(pos)
    anos = (ds[-1] - ds[0]) / DIA / 365
    pico, dd = 1.0, 0.0
    for v in curva:
        pico = max(pico, v)
        dd = min(dd, v / pico - 1)
    por_ano = defaultdict(lambda: [None, None])
    for d, v in zip(ds, curva):
        y = datetime.fromtimestamp(d / 1000, timezone.utc).year
        if por_ano[y][0] is None:
            por_ano[y][0] = v
        por_ano[y][1] = v
    return {"cagr": curva[-1] ** (1 / anos) - 1, "dd": dd, "trocas": trocas,
            "expo": sum(expo) / len(expo), "anos": {y: b / a - 1 for y, (a, b) in sorted(por_ano.items())}}


def main(argv):
    for moeda in ("BTC", "ETH"):
        px = fechamentos(moeda)
        dias = sorted(px)
        print("\n" + "=" * 100 + f"\n{moeda} spot ({datetime.fromtimestamp(dias[0]/1000, timezone.utc):%Y-%m-%d} a "
              f"{datetime.fromtimestamp(dias[-1]/1000, timezone.utc):%Y-%m-%d})\n" + "=" * 100)
        res = {}
        for var in ("BH", "T", "V", "TV"):
            alvo = posicoes(dias, px, var)
            t_hist = min(alvo) + DIA
            res[var] = (simular(dias, px, alvo, INICIO_DECIDE), simular(dias, px, alvo, t_hist),
                        simular(dias, px, alvo, INICIO_DECIDE, caixa_aa=0.04))
        bh_dec, bh_hist, _ = res["BH"]
        for var, nome in (("BH", "comprar e segurar"), ("T", "T: tendencia (MM200)"),
                          ("V", "V: alvo de vol 40%"), ("TV", "TV: tendencia + vol")):
            dec, hist, cx = res[var]
            serve = all(x["dd"] >= -0.50 for x in (dec, hist)) and \
                dec["cagr"] >= 0.7 * bh_dec["cagr"] and hist["cagr"] >= 0.7 * bh_hist["cagr"]
            meta = serve and dec["cagr"] >= 0.20
            veredito = "" if var == "BH" else (" -> ATENDE A META" if meta else " -> SERVE" if serve else " -> nao serve")
            print(f"  {nome:<24} 2021-26: {100*dec['cagr']:+6.1f}%/ano, queda {100*dec['dd']:6.1f}%, "
                  f"exposicao {100*dec['expo']:3.0f}%, {dec['trocas']:>3} trocas | "
                  f"desde 2018: {100*hist['cagr']:+6.1f}%/ano, queda {100*hist['dd']:6.1f}%"
                  f" | 2021-26 c/ caixa a 4%: {100*cx['cagr']:+5.1f}%{veredito}")
        print("\n  Por ano (2021-26, janela que decide):")
        anos = sorted(res["BH"][0]["anos"])
        print("    " + f"{'':<24}" + "".join(f"{a:>9}" for a in anos))
        for var in ("BH", "T", "V", "TV"):
            print("    " + f"{var:<24}" + "".join(f"{100*res[var][0]['anos'][a]:+8.0f}%" for a in anos))
        print("\n  Por ano (historico inteiro):")
        anos = sorted(res["BH"][1]["anos"])
        print("    " + f"{'':<24}" + "".join(f"{a:>9}" for a in anos))
        for var in ("BH", "T", "V", "TV"):
            print("    " + f"{var:<24}" + "".join(f"{100*res[var][1]['anos'][a]:+8.0f}%" for a in anos))


if __name__ == "__main__" and "--robustez" not in sys.argv and "--cesta" not in sys.argv:
    main(sys.argv[1:])


# ---------------------------------------------------------------------------
# ROBUSTEZ (acrescentada DEPOIS de ver o resultado, 05/10/2026; sem poder de
# decisao): a mesma regra, sem mudar nada, em outras moedas grandes com spot
# na Binance desde antes de 2021, e numa cesta de peso igual.
# Uso: python replay_tendencia_vol.py --robustez
# ---------------------------------------------------------------------------

OUTRAS = ["BNB", "XRP", "ADA", "DOGE", "LTC", "LINK", "BCH", "TRX", "XLM", "DOT", "SOL", "AVAX", "ATOM", "ETC", "MATIC"]


def robustez():
    print(f"{'moeda':<6} {'BH 21-26':>10} {'queda':>7} | {'TV 21-26':>9} {'queda':>7} | {'BH hist':>8} {'queda':>7} | "
          f"{'TV hist':>8} {'queda':>7} | veredito")
    linhas = []
    for m in OUTRAS:
        try:
            px = fechamentos(m)
        except Exception as e:
            print(f"{m:<6} sem dados ({e})")
            continue
        dias = sorted(px)
        if not dias or dias[0] > INICIO_DECIDE - (MM + 5) * DIA:
            print(f"{m:<6} historico curto (inicio {datetime.fromtimestamp(dias[0]/1000, timezone.utc):%Y-%m}) -- fora")
            continue
        r = {}
        for var in ("BH", "TV"):
            alvo = posicoes(dias, px, var)
            r[var] = (simular(dias, px, alvo, INICIO_DECIDE), simular(dias, px, alvo, min(alvo) + DIA))
        (bd, bh), (td, th) = r["BH"], r["TV"]
        serve = td["dd"] >= -0.5 and th["dd"] >= -0.5 and td["cagr"] >= 0.7 * bd["cagr"] and th["cagr"] >= 0.7 * bh["cagr"]
        meta = serve and td["cagr"] >= 0.20
        linhas.append((m, bd, td))
        print(f"{m:<6} {100*bd['cagr']:+9.1f}% {100*bd['dd']:6.0f}% | {100*td['cagr']:+8.1f}% {100*td['dd']:6.0f}% | "
              f"{100*bh['cagr']:+7.1f}% {100*bh['dd']:6.0f}% | {100*th['cagr']:+7.1f}% {100*th['dd']:6.0f}% | "
              f"{'ATENDE A META' if meta else 'serve' if serve else 'nao serve'}")
    melhor_cagr = sum(td["cagr"] > bd["cagr"] for _, bd, td in linhas)
    menor_dd = sum(td["dd"] > bd["dd"] for _, bd, td in linhas)
    print(f"\n2021-26: TV rendeu mais que BH em {melhor_cagr}/{len(linhas)} moedas; teve queda menor em {menor_dd}/{len(linhas)}; "
          f"TV >= 20%/ano em {sum(td['cagr'] >= 0.2 for _, _, td in linhas)}/{len(linhas)}")


if __name__ == "__main__" and "--robustez" in sys.argv:
    robustez()


def cesta():
    """Cesta de peso igual (rebalanceada todo dia) de TV e de BH em todas as moedas com historico."""
    series = {}
    for m in ["BTC", "ETH"] + OUTRAS:
        px = fechamentos(m)
        dias = sorted(px)
        if not dias or dias[0] > INICIO_DECIDE - (MM + 5) * DIA:
            continue
        for var in ("BH", "TV"):
            alvo = posicoes(dias, px, var)
            ds = [d for d in dias if d in alvo]
            pos, r = 0.0, {}
            for a, b in zip(ds, ds[1:]):
                novo = alvo.get(a - DIA, pos)
                c = CUSTO * abs(novo - pos)
                pos = novo
                r[b] = pos * (px[b] / px[a] - 1) - c
            series[(m, var)] = r
    for t0, nome in ((INICIO_DECIDE, "2021-26"), (int(datetime(2019, 1, 1, tzinfo=timezone.utc).timestamp() * 1000), "2019-26")):
        for var in ("BH", "TV"):
            dias = sorted({d for (m, v), r in series.items() if v == var for d in r if d >= t0})
            curva, pico, dd = 1.0, 1.0, 0.0
            for d in dias:
                xs = [r[d] for (m, v), r in series.items() if v == var and d in r]
                curva *= 1 + sum(xs) / len(xs)
                pico = max(pico, curva)
                dd = min(dd, curva / pico - 1)
            anos = (dias[-1] - dias[0]) / DIA / 365
            n = len({m for (m, v) in series if v == var})
            print(f"  cesta {var} ({n} moedas) {nome}: {100*(curva**(1/anos)-1):+.1f}%/ano | queda maxima {100*dd:.1f}%")


if __name__ == "__main__" and "--cesta" in sys.argv:
    cesta()
