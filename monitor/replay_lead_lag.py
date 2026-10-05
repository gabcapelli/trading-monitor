"""
Estudo 33 -- lead-lag BTC -> altcoins em 1h, PRE-REGISTRADO em 04/10/2026,
antes de calcular qualquer retorno. Familia de 2 hipoteses no DE com o estudo
34 (replay_turtle.py): decisao com IC de 97.5% (Bonferroni, K = 2).

HIPOTESE
--------
A informacao chega primeiro ao BTC (mais liquido, onde o fluxo grande opera)
e as altcoins ajustam com atraso. Depois de uma hora de movimento forte do
BTC, as alts continuam na mesma direcao na hora seguinte -- MAIS do que o
proprio BTC (senao e so momentum horario do BTC, que o estudo 16 ja viu e que
seria mais barato operar no proprio BTC).

DADOS
-----
Candles de 1h da Binance (dados_binance, cache dos estudos 23/24), funding
real. Alts = universo sem o BTCUSDT.

REGRA
-----
- Sinal na hora t: |retorno do BTC na hora t| >= 2 x desvio-padrao dos
  retornos horarios do BTC nas 720 horas anteriores. d = sinal do retorno.
- Em CADA alt do universo com candle: entra na direcao d na abertura de t+1,
  sai na abertura de t+2 (1 hora). Sem stop.
- Execucao OTIMISTA: abertura de t+1 = fechamento de t, ou seja, entrada no
  instante em que o sinal fecha. Exige robo ao vivo (o workflow horario chega
  minutos depois). Se nem assim der, o resultado negativo e robusto.

MEDIDAS (% por trade)
---------------------
- `bruto`: d x (saida / entrada - 1).
- `abs` (decide): bruto - 0.18% - funding pago no periodo.
- `excesso_btc` (decide): bruto - bruto do BTC na mesma hora e direcao. Mede
  o atraso das alts, nao o momentum do BTC.
- Bootstrap por semana do sinal.

CRITERIO
--------
Etapa 1 (portao, universo A, 19 alts): se o BRUTO medio for <= 0.18% (o
custo), a regra nao tem como dar lucro -> NAO PASSA por custo, e o DE NAO e
usado.
Etapa 2 (DE, 368 perps): PASSA se `abs` E `excesso_btc` tiverem IC97.5
inteiro acima de zero.

DESCRITIVOS
-----------
2a hora (t+2 -> t+3); 4 horas (t+1 -> t+5); limiar de 3 sigma; o proprio BTC
em t+1 (momentum horario).

Uso (de dentro de monitor/):
    python replay_lead_lag.py
"""

import math
import sys
import time

import dados_binance as DB
import fmz_motor as M
from replay_ema_ribbon import CUSTO_RT

H = 3_600_000
JANELA = 720
CONF = 1 - 0.05 / 2


def sinais_btc(btc, sigmas):
    """{ts da hora t: d} e {ts: open} do BTC."""
    r = [None] + [btc[i][4] / btc[i - 1][4] - 1 for i in range(1, len(btc))]
    out = {}
    for t in range(JANELA + 1, len(btc)):
        if btc[t][0] - btc[t - 1][0] != H:
            continue
        jan = r[t - JANELA:t]
        m = sum(jan) / JANELA
        sd = math.sqrt(sum((x - m) ** 2 for x in jan) / (JANELA - 1))
        if sd > 0 and abs(r[t]) >= sigmas * sd:
            out[btc[t][0]] = 1 if r[t] > 0 else -1
    return out


def trades_alt(sym, c, sinais, btc_open, fund):
    o = {k[0]: k[1] for k in c}
    out = []
    for ts, d in sinais.items():
        p1, p2 = o.get(ts + H), o.get(ts + 2 * H)
        b1, b2 = btc_open.get(ts + H), btc_open.get(ts + 2 * H)
        if not (p1 and p2 and b1 and b2):
            continue
        bruto = 100 * d * (p2 / p1 - 1)
        f = 100 * fund.soma(ts + H, ts + 2 * H) if fund else 0.0
        p3, p5 = o.get(ts + 3 * H), o.get(ts + 5 * H)
        out.append({
            "ts": ts, "sym": sym, "bruto": bruto,
            "abs": bruto - 100 * CUSTO_RT - d * f,
            "excesso_btc": bruto - 100 * d * (b2 / b1 - 1),
            "hora2": None if not p3 else 100 * d * (p3 / p2 - 1),
            "h4": None if not p5 else 100 * d * (p5 / p1 - 1),
        })
    return out


def rodar(nome, sinais, btc_open, funding=True):
    trades, n = [], 0
    for sym in M.universo(nome):
        if sym == "BTCUSDT":
            continue
        try:
            c = DB.baixar(sym, "1H", M.DIAS)
        except Exception:
            continue
        if len(c) < 24 * 60:
            continue
        n += 1
        trades += trades_alt(sym, c, sinais, btc_open, M.Funding(sym) if funding else None)
    print(f"  universo {nome}: {n} alts | {len(trades)} trades", flush=True)
    return trades


def relatorio(trades, conf):
    for chave, nome in (("bruto", "bruto"), ("abs", "absoluto (custo+funding)"),
                        ("excesso_btc", "excesso sobre o BTC"), ("hora2", "descr.: 2a hora"),
                        ("h4", "descr.: 4 horas (bruto)")):
        print(M.linha(nome, trades, chave, conf)[0])


def main(argv):
    t0 = time.time()
    btc = DB.baixar("BTCUSDT", "1H", M.DIAS)
    btc_open = {k[0]: k[1] for k in btc}
    sin2, sin3 = sinais_btc(btc, 2.0), sinais_btc(btc, 3.0)
    print(f"BTC: {len(btc)} horas | sinais 2 sigma: {len(sin2)} | 3 sigma: {len(sin3)}")
    mom = []
    for ts, d in sin2.items():
        b1, b2 = btc_open.get(ts + H), btc_open.get(ts + 2 * H)
        if b1 and b2:
            mom.append({"ts": ts, "v": 100 * d * (b2 / b1 - 1)})
    print(M.linha("descr.: o proprio BTC em t+1", mom, "v")[0])

    print("\n" + "=" * 100 + "\nETAPA 1 -- universo A (portao: bruto medio > 0.18%?)\n" + "=" * 100)
    ta = rodar("A", sin2, btc_open)
    relatorio(ta, 0.95)
    print(M.linha("descr.: 3 sigma, bruto", rodar("A", sin3, btc_open, False), "bruto")[0])
    bruto_a = sum(x["bruto"] for x in ta) / len(ta)
    if bruto_a <= 100 * CUSTO_RT:
        print(f"\n  Bruto medio em A = {bruto_a:+.3f}% <= custo {100*CUSTO_RT:.2f}%: a regra nao cobre o custo.")
        print("  DECISAO: NAO PASSA (por custo, na etapa 1). Universo DE NAO usado.")
        print(f"\n  [{time.time()-t0:.0f}s]")
        return

    print("\n" + "=" * 100 + f"\nETAPA 2 -- universo DE (decide, IC{100*CONF:.1f})\n" + "=" * 100)
    td = rodar("DE", sin2, btc_open)
    relatorio(td, CONF)
    _, _, lo_a = M.linha("", td, "abs", CONF)
    _, _, lo_e = M.linha("", td, "excesso_btc", CONF)
    print(f"\n  DECISAO: {'PASSA' if lo_a > 0 and lo_e > 0 else 'NAO PASSA'}\n  [{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main(sys.argv[1:])
