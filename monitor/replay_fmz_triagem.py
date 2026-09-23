"""
Estudo 23 -- triagem do acervo FMZ (strategies-for-test), PRE-REGISTRADO em
23/09/2026, antes de rodar qualquer backtest.

O ACERVO
--------
5.807 estrategias (github.com/gabcapelli/strategies-for-test, biblioteca da
FMZ). Indice e classificacao em monitor/fmz/ (indexar.py, classificar.py):
91% PineScript, 80% republicados em serie de scripts do TradingView pela conta
"ChaoZhang". Pelo nome, ~85% sao combinacoes de indicadores das familias ja
testadas nos estudos 1-22 (media/tendencia, oscilador, rompimento de canal,
padrao de candle). Mecanismos distintos (Dual Thrust, balanceamento, base
trimestral, pares) tem estudo proprio (replay_fmz_mecanismos.py).

AMOSTRA REPRESENTATIVA (sem escolha a dedo)
-------------------------------------------
fmz/sortear.py: populacao = PineScript com strategy(), sem request.security,
codigo <= 6000 caracteres, familia de indicador tecnico (3.764 de 5.807).
Sorteio com semente 20260923; traduzidas na ordem da fila as 12 primeiras
traduziveis para o diario. Pulada: #13 "Revolut v1.0" (stop e alvo de 5 e 6
TICKS, sem sentido fora do tick do ativo original).

TRADUCAO
--------
Parametros padrao do script, sem nenhum ajuste. Desvios, todos pela intencao
evidente do autor quando o literal depende da escala de preco do ativo em que
o script foi escrito:
- #1: `position_size < 1` / `>= 1` (contratos) lido como "zerado"/"posicionado".
- #9: `stop=CCIoverSold` (-100 usado como PRECO de ordem stop) lido como ordem
  a mercado; o literal compraria sempre e so venderia moedas abaixo de US$100.
- #0 e #5: limiares absolutos (BP > 5, hist > 0.4) mantidos LITERAIS -- sao
  parte da regra; em moedas de preco baixo o sinal pode nunca disparar.
- Filtros de data (janela de backtest) removidos.
Tempo grafico: 1D (o unico com historico longo em A, D e E; nos estudos 1-22
todo intradiario morreu no custo).

MEDIDAS (fmz_motor.py)
----------------------
Por trade, em % do nocional: `liq` (custo 0.18% + 0.05% por ordem stop),
`abs` (liq menos funding real da Binance), `excesso` (teste de beta: sobre o mesmo
lado nas MESMAS datas em outros pares do universo -- linha de base transversal;
a de mesmo par do estudo 6 fica como descritivo, `excesso_par`, porque tem
vies demonstrado em passeio aleatorio, ver fmz_motor.py). Bootstrap por semana.

CRITERIO (pre-registrado)
-------------------------
Etapa 1, desenvolvimento, universo A (20 majors, Binance): avanca a estrategia
com n >= 100 trades, `liq` medio > 0 E `excesso` medio > 0 (estimativa pontual).
Etapa 2, decisao, universo DE (368 perps da Binance = D + E): PASSA se `abs` E
`excesso` tiverem IC inteiro acima de zero, com confianca 1 - 0.05/K, onde
K = estrategias que avancaram + 4 hipoteses de replay_fmz_mecanismos.py com
poder de decisao (Dual Thrust SAR, Dual Thrust intradiario, balanceamento, pares). D e E ja foram usados (estudos 13-22), mas para hipoteses de
outras familias; a reutilizacao fica declarada e coberta pelo Bonferroni.
As 12 tambem rodam em DE como descritivo (sem poder de decisao).
"""

import random
import sys
import time

import fmz_motor as M


# ---------------------------------------------------------------------------
# As 12 traducoes (numero = posicao na fila do sorteio)
# ---------------------------------------------------------------------------

def s00_bandpass(c):
    """Bandpass Filter Strategy ver 2.0: BP de hl2, compra se BP > 5, vende se
    BP <= -5, mantem a posicao senao (stop and reverse)."""
    L, delta, sell_z, buy_z = 20, 0.5, 5, -5
    x = [(k[2] + k[3]) / 2 for k in c]
    beta = M.math.cos(3.14 * (360 / L) / 180)
    gamma = 1 / M.math.cos(3.14 * (720 * delta / L) / 180)
    alpha = gamma - M.math.sqrt(gamma * gamma - 1)
    bp = [0.0] * len(c)
    for t in range(2, len(c)):
        bp[t] = 0.5 * (1 - alpha) * (x[t] - x[t - 2]) + beta * (1 + alpha) * bp[t - 1] - alpha * bp[t - 2]
    pos = [0] * len(c)
    for t in range(1, len(c)):
        pos[t] = 1 if bp[t] > sell_z else (-1 if bp[t] <= buy_z else pos[t - 1])

    def logica(br, t):
        if pos[t] == 1:
            br.entry("Long", 1)
        elif pos[t] == -1:
            br.entry("Short", -1)
    return logica, 1


def s01_ema_hma_rsi(c):
    """EMA_HMA_RSI_Strategy: compra com HMA200 < EMA200 e HMA subindo e RSI13<70;
    aumenta (pyramiding 2) abaixo do preco medio no cruzamento do RSI por 30/40;
    realiza 20% no cruzamento do RSI para baixo de 80 no lucro; stop de 8% sobre
    o fechamento anterior, arrastado em candles de alta; sai no cruzamento da
    HMA para baixo da EMA no lucro."""
    cl = [k[4] for k in c]
    r = M.rsi(cl, 13)
    e = M.ema(cl, 200)
    h = M.hma(cl, 200)
    st = {"stop": 0.0}

    def logica(br, t):
        if None in (h[t], h[t - 2], e[t], r[t], r[t - 1]):
            return
        posicionado = br.pos > 0
        if not posicionado and h[t] < e[t] and h[t] > h[t - 2] and r[t] < 70:
            br.entry("Long Entry", 1)
        if posicionado and cl[t] < br.preco_medio and (M.cruza_acima(r, 30, t) or M.cruza_acima(r, 40, t)):
            br.entry("Long Entry", 1)
        if posicionado:
            if cl[t] > cl[t - 1] and cl[t] > c[t][1] and cl[t] > br.preco_medio:
                st["stop"] = cl[t - 1] * (1 - 0.08)
        else:
            st["stop"] = 0.0
        if posicionado and M.cruza_abaixo(r, 80, t) and cl[t] > br.preco_medio:
            br.close("Long Entry", 20)
        if posicionado and cl[t] < st["stop"]:
            br.close("Long Entry")
        if posicionado and cl[t] > br.preco_medio and M.cruza_abaixo(h, e, t):
            br.close("Long Entry")
    return logica, 2


def s02_ma_rsi(c):
    """Vitaliby MA and RSI: SMA9 x SMA21 com filtro de RSI14, stop and reverse."""
    cl = [k[4] for k in c]
    f, s, r = M.sma(cl, 9), M.sma(cl, 21), M.rsi(cl, 14)

    def logica(br, t):
        if r[t] is None:
            return
        lc = M.cruza_acima(f, s, t) and r[t] > 30
        sc = M.cruza_abaixo(f, s, t) and r[t] < 70
        if lc:
            br.entry("Long", 1)
        if sc:
            br.close("Long")
            br.entry("Short", -1)
        if lc:
            br.close("Short")
    return logica, 1


def s03_chandelier(c):
    """Chandelier Exit (22, 3.0, extremos de fechamento): compra na virada para
    alta, fecha na virada para baixa. So compra."""
    cl = [k[4] for k in c]
    a = M.atr(c, 22)
    hh, ll = M.highest(cl, 22), M.lowest(cl, 22)
    n = len(c)
    ls, ss, dr = [None] * n, [None] * n, [1] * n
    for t in range(n):
        if a[t] is None or hh[t] is None:
            continue
        l0, s0 = hh[t] - 3 * a[t], ll[t] + 3 * a[t]
        lp = ls[t - 1] if ls[t - 1] is not None else l0
        sp = ss[t - 1] if ss[t - 1] is not None else s0
        ls[t] = max(l0, lp) if cl[t - 1] > lp else l0
        ss[t] = min(s0, sp) if cl[t - 1] < sp else s0
        dr[t] = 1 if cl[t] > sp else (-1 if cl[t] < lp else dr[t - 1])

    def logica(br, t):
        if dr[t] == 1 and dr[t - 1] == -1:
            br.entry("Buy", 1)
        if dr[t] == -1 and dr[t - 1] == 1:
            br.close("Buy")
    return logica, 1


def s04_short_sempre(c):
    """Short High-Grossing Forex Pair: vende sempre que zerado; sai apos 7
    candles, com -30% (alvo) ou +5% (stop), avaliado no fechamento."""
    cl = [k[4] for k in c]
    st = {"fim": None, "px": None}

    def logica(br, t):
        if br.abertos() == 0:
            br.entry("Short", -1)
            st["fim"], st["px"] = t + 7, cl[t]
            return
        px = st["px"]
        if t >= st["fim"] or cl[t] <= px * 0.70 or cl[t] >= px * 1.05:
            br.close("Short")
    return logica, 1


def s05_jims_macd(c):
    """Jim's MACD: MACD(12,26,9) e MME5; compra com histograma e sinal > 0, vende
    com os dois < 0 e preco abaixo da MME5; zera quando o histograma muda de sinal."""
    cl = [k[4] for k in c]
    ml, sg, hs = M.macd(cl)
    ma = M.ema(cl, 5)

    def logica(br, t):
        if hs[t] is None:
            return
        cz = M.cruza(ml, sg, t)
        if (cl[t] > ma[t] and cz and hs[t] > 0.4 and sg[t] > 0) or (hs[t] > 0 and sg[t] > 0):
            br.entry("BUY", 1)
        if (cl[t] < ma[t] and cz and hs[t] < -0.4 and sg[t] < 0) or (cl[t] < ma[t] and hs[t] < 0 and sg[t] < 0):
            br.entry("SELL", -1)
        if hs[t] < 0:
            br.close("BUY")
        if hs[t] > 0:
            br.close("SELL")
    return logica, 1


def s06_bandas_ema300(c):
    """Bandas de EMA 300 (+-2 desvios de 300): compra no cruzamento para cima da
    banda inferior, vende no cruzamento para baixo da superior; alvo limite a
    0.98% do fechamento, renovado a cada candle."""
    cl = [k[4] for k in c]
    e, d = M.ema(cl, 300), M.stdev(cl, 300)
    sup = [None if d[t] is None else e[t] + 2 * d[t] for t in range(len(c))]
    inf = [None if d[t] is None else e[t] - 2 * d[t] for t in range(len(c))]

    def logica(br, t):
        compra, venda = M.cruza_acima(cl, inf, t), M.cruza_abaixo(cl, sup, t)
        if compra:
            br.entry("Compra", 1)
        if venda:
            br.entry("Venda", -1)
        if br.pos > 0:
            br.exit("Compra", limit=cl[t] * (1 + 0.98 / 100))
        if br.pos < 0:
            br.exit("Venda", limit=cl[t] * (1 - 0.98 / 100))
    return logica, 1


def s07_winners(c):
    """I Like Winners And Hate Loosers: compra quando fecha acima da media de 10
    da maxima de 200; fecha abaixo dela menos 2 ATR14. So compra."""
    cl = [k[4] for k in c]
    h = M.sma(M.highest([k[2] for k in c], 200), 10)
    a = M.atr(c, 14)
    lo = [None if (h[t] is None or a[t] is None) else h[t] - 2 * a[t] for t in range(len(c))]

    def logica(br, t):
        if M.cruza_acima(cl, h, t):
            br.entry("Buy", 1)
        if M.cruza_abaixo(cl, lo, t):
            br.close("Buy")
    return logica, 1


def s08_sma14_28(c):
    """Tendies Heist: SMA14 x SMA28, stop and reverse (o dimensionamento por
    patrimonio nao muda o retorno por trade)."""
    cl = [k[4] for k in c]
    f, s = M.sma(cl, 14), M.sma(cl, 28)

    def logica(br, t):
        if M.cruza_acima(f, s, t):
            br.entry("L", 1)
        if M.cruza_abaixo(f, s, t):
            br.entry("S", -1)
    return logica, 1


def s09_cci(c):
    """CCI 0Trend: CCI(hlc3,20) cruza -100 para cima -> compra; cruza 100 para
    baixo -> vende. Stop and reverse."""
    x = [(k[2] + k[3] + k[4]) / 3 for k in c]
    v = M.cci(x, 20)

    def logica(br, t):
        if M.cruza_acima(v, -100, t):
            br.entry("CCI_L", 1)
        if M.cruza_abaixo(v, 100, t):
            br.entry("CCI_S", -1)
    return logica, 1


def s10_big3(c):
    """Big 3: SMA20>40>80 com derivada da SMA40 positiva -> compra; espelho
    vende; zera quando a derivada vira."""
    cl = [k[4] for k in c]
    f, m, s = M.sma(cl, 20), M.sma(cl, 40), M.sma(cl, 80)

    def logica(br, t):
        if s[t] is None or m[t - 2] is None:
            return
        der = 3 * m[t] - 4 * m[t - 1] + m[t - 2]
        if f[t] > m[t] > s[t] and der > 0:
            br.entry("long", 1)
        if der <= 0:
            br.close("long")
        if f[t] < m[t] < s[t] and der < 0:
            br.entry("short", -1)
        if der >= 0:
            br.close("short")
    return logica, 1


def s11_bb_fib_macd_rsi(c):
    """Demo GPT Bollinger/Fibonacci/MACD/RSI: compra se QUALQUER um de quatro
    sinais de compra, vende se qualquer um de venda (os dois podem valer no
    mesmo candle); saidas por alvo 5% e stop 2% sobre a maxima desde a entrada
    (variavel `var` nunca reiniciada, como no original)."""
    cl, hi, lo_ = [k[4] for k in c], [k[2] for k in c], [k[3] for k in c]
    bas, dv = M.sma(cl, 20), M.stdev(cl, 20)
    sup = [None if dv[t] is None else bas[t] + 2 * dv[t] for t in range(len(c))]
    inf = [None if dv[t] is None else bas[t] - 2 * dv[t] for t in range(len(c))]
    hh, ll = M.highest(hi, 50), M.lowest(lo_, 50)
    ml, sg, _ = M.macd(cl)
    r = M.rsi(cl, 14)
    st = {"mpp": None}

    def logica(br, t):
        if None in (hh[t], r[t], sg[t], sup[t]):
            return
        f23 = ll[t] + 0.236 * (hh[t] - ll[t])
        f61 = ll[t] + 0.618 * (hh[t] - ll[t])
        lcond = (M.cruza_acima(cl, inf, t) or (ll[t] <= cl[t] <= f23)
                 or M.cruza_acima(ml, sg, t) or r[t] < 30)
        scond = (M.cruza_abaixo(cl, sup, t) or (f61 <= cl[t] <= hh[t])
                 or M.cruza_abaixo(ml, sg, t) or r[t] > 70)
        if br.abertos() > 0:
            st["mpp"] = br.lotes[0]["px"] if st["mpp"] is None else max(st["mpp"], hi[t])
        if st["mpp"] is not None and br.abertos() > 0:
            tp, sl = st["mpp"] * 1.05, st["mpp"] * 0.98
            if cl[t] >= tp:
                br.exit("Long", limit=tp)
            if cl[t] <= sl:
                br.exit("Long", stop=sl)
            if cl[t] <= tp:
                br.exit("Short", limit=tp)
            if cl[t] >= sl:
                br.exit("Short", stop=sl)
        if lcond:
            br.entry("Long", 1)
        if scond:
            br.entry("Short", -1)
    return logica, 1


ESTRATEGIAS = [
    ("00 bandpass (SAR)", s00_bandpass, 60),
    ("01 EMA/HMA200+RSI (piramide)", s01_ema_hma_rsi, 210),
    ("02 SMA9x21+RSI (SAR)", s02_ma_rsi, 60),
    ("03 chandelier exit (so compra)", s03_chandelier, 60),
    ("04 vende sempre 7d", s04_short_sempre, 60),
    ("05 Jim's MACD", s05_jims_macd, 60),
    ("06 bandas EMA300", s06_bandas_ema300, 310),
    ("07 maxima 200 / ATR (so compra)", s07_winners, 220),
    ("08 SMA14x28 (SAR)", s08_sma14_28, 60),
    ("09 CCI +-100 (SAR)", s09_cci, 60),
    ("10 Big 3 SMA20/40/80", s10_big3, 100),
    ("11 BB/Fib/MACD/RSI (GPT)", s11_bb_fib_macd_rsi, 60),
]


def rodar_universo(nome, estrategias, min_candles=400):
    """Devolve {rotulo: [trades medidos]} somando todos os pares do universo."""
    rng = random.Random(M.SEED)
    res = {r: [] for r, _, _ in estrategias}
    precos = M.Precos()
    usados = 0
    for sym in M.universo(nome):
        try:
            c = M.candles(sym)
        except Exception as e:
            print(f"    {sym:<16} FALHOU: {type(e).__name__}", flush=True)
            continue
        if len(c) < min_candles:
            continue
        usados += 1
        precos.add(sym, c)
        fund = M.Funding(sym)
        for rot, fab, inicio in estrategias:
            if len(c) < inicio + 100:
                continue
            logica, pyr = fab(c)
            tr = M.rodar_script(c, logica, inicio, pyr)
            res[rot] += M.medir(c, tr, fund, rng, inicio, sym=sym)
    for tr in res.values():
        precos.excesso(tr, rng)
    print(f"  universo {nome}: {usados} pares com >= {min_candles} candles diarios", flush=True)
    return res


def relatorio(res, conf=0.95):
    for rot, tr in res.items():
        dur = sum(x["dur"] for x in tr) / len(tr) if tr else 0
        compras = sum(x["q"] for x in tr if x["d"] == 1) / max(1e-9, sum(x["q"] for x in tr))
        print(f"\n  [{rot}]  duracao media {dur:.1f} d | {100*compras:.0f}% compras")
        for chave, nome in (("liq", "liquido (custo)"), ("abs", "absoluto (custo+funding)"),
                            ("excesso_par", "excesso mesmo par (descritivo)"),
                            ("excesso", "EXCESSO transversal (decide)")):
            print(M.linha(nome, tr, chave, conf)[0])


def main():
    t0 = time.time()
    print("=" * 100 + "\nETAPA 1 -- universo A (20 majors, desenvolvimento)\n" + "=" * 100)
    resA = rodar_universo("A", ESTRATEGIAS)
    relatorio(resA)
    avancam = []
    for rot, tr in resA.items():
        tot = sum(x["q"] for x in tr) or 1
        liq = sum(x["q"] * x["liq"] for x in tr) / tot
        tv = [x for x in tr if x["excesso"] is not None]
        exc = sum(x["q"] * x["excesso"] for x in tv) / (sum(x["q"] for x in tv) or 1)
        ok = len(tr) >= 100 and liq > 0 and exc > 0
        print(f"  etapa 1 {rot:<34} n={len(tr):>5} liq={liq:+.3f}% exc={exc:+.3f}% -> {'AVANCA' if ok else 'para'}")
        if ok:
            avancam.append(rot)
    K = len(avancam) + 4
    conf = 1 - 0.05 / K
    print(f"\n  avancam: {avancam or 'nenhuma'} | K = {K} | confianca da etapa 2 = {100*conf:.2f}%")

    print("\n" + "=" * 100 + "\nETAPA 2 -- universo DE (368 perps da Binance; decide so para as que avancaram)\n" + "=" * 100)
    resDE = rodar_universo("DE", ESTRATEGIAS)
    relatorio(resDE, conf)
    print("\n  DECISAO:")
    for rot in avancam:
        tr = resDE[rot]
        _, _, lo_abs = M.linha("", tr, "abs", conf)
        _, _, lo_exc = M.linha("", tr, "excesso", conf)
        print(f"    {rot:<34} {'PASSA' if (lo_abs > 0 and lo_exc > 0) else 'NAO PASSA'}")
    if not avancam:
        print("    nenhuma estrategia avancou da etapa 1")
    print(f"\n  [{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main()
