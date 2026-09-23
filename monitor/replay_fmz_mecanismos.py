"""
Estudo 24 -- mecanismos distintos do acervo FMZ, PRE-REGISTRADO em 23/09/2026
junto com o estudo 23 (replay_fmz_triagem.py), antes de rodar qualquer backtest.

Do acervo, fora da sopa de indicadores, sobram poucos mecanismos testaveis com
candles. Quatro hipoteses com poder de decisao (entram no K do Bonferroni do
estudo 23) e uma medicao sem teste (replay_fmz_base_trimestral.py):

M1a DUAL THRUST, stop and reverse (fmz: "python版-Dual-Thrust-OKCoin-期货",
    parametros padrao NPeriod=4, Ks=Kx=0.5)
    Range = max(HH - LC, HC - LL) dos 4 dias UTC anteriores (o script da FMZ
    usa o candle ainda aberto no calculo; aqui so dias fechados, a definicao
    classica, sem lookahead). Linha de compra = abertura do dia + 0.5*Range,
    de venda = abertura - 0.5*Range. Tocou a de compra: comprado (revertendo a
    venda); tocou a de venda: vendido. Sempre posicionado depois do 1o sinal.
M1b DUAL THRUST intradiario: as mesmas linhas, com reversao dentro do dia, e
    zera no fechamento do dia UTC (a versao classica de futuros de commodity).
    Execucao dos dois no caminho de candles de 1h (caminho O-L-H-C/O-H-L-C
    dentro da hora), ordem stop no gatilho ou na abertura da hora se ela ja
    abriu alem; 0.05% de slippage por execucao stop (entrada e saida).
M2  BALANCEAMENTO 50/50 (fmz: "动态平衡策略-python-版"): metade em moeda, metade
    em caixa; quando |valor da moeda - caixa| > 5% do caixa, negocia metade da
    diferenca. Checado a cada 1h (o original checa a cada 60 s). Custo 0.15%
    do valor negociado (taxa taker de spot 0.10% + 0.05% de slippage); preco do
    perpetuo como aproximacao do spot. Medida: EXCESSO de LOG-retorno diario
    do balanceado sobre o 50/50 parado (buy and hold com o mesmo capital
    inicial), media de peso igual entre os pares do dia.
    [Corrigido em 23/09/2026, no desenvolvimento em A, antes de rodar DE: o
    registro original dizia retorno diario ARITMETICO. No A isso deu -10.6%/ano
    enquanto o balanceado terminava acima do parado em 15 de 20 pares (mediana
    4.71x contra 2.75x) -- a diferenca aritmetica nao mede a hipotese, que e de
    crescimento GEOMETRICO (menos arrasto de volatilidade com a mesma media). A
    aritmetica segue impressa como descritivo.] E a pergunta que importa: o
    rebalanceamento colhe volatilidade ("demonio de Shannon") ou so vende o
    que sobe? O retorno absoluto (metade comprado em cripto) e descritivo.
M4  PARES contra o BTC (fmz: "Pair-trading-strategy", SMA 20, z = 2): na razao
    moeda/BTC diaria, `cross` da razao com a banda inferior -> compra a razao
    (compra a moeda, vende BTC, mesmo nocional); com a superior -> vende a
    razao; `cross` com a media -> zera tudo. `cross` do Pine vale nas duas
    direcoes, mantido literal. Custo 0.36% (duas pernas) sobre o nocional de
    uma perna; funding real das duas pernas. Entrada na abertura seguinte.

MEDIDAS E BETA
--------------
M1a, M1b e M4: por trade, em % do nocional (fmz_motor.py): `abs` (custo,
slippage de stop, funding real) e `excesso` transversal (mesmo lado, mesmas
datas, outros pares; no Dual Thrust a linha de base entra na abertura da hora
seguinte ao gatilho, porque o trade entra no meio de um movimento de ~0.5 do
range de 4 dias e uma linha de base desde a abertura do dia incluiria esse
movimento do mercado; em pares, a linha de base e a razao outra_moeda/BTC).
M2: excesso diario de log-retorno (balanceado - parado), anualizado.

CRITERIO (pre-registrado)
-------------------------
Universo A (20 majors): so descritivo -- nao ha selecao, cada hipotese e uma
regra unica com os parametros do acervo.
Universo DE (368 perps da Binance), confianca 1 - 0.05/K (K do estudo 23):
- M1a, M1b, M4: PASSA se `abs` E `excesso` tiverem IC inteiro acima de zero
  (bootstrap por semana de entrada).
- M2: PASSA se o excesso de log-retorno anualizado sobre o 50/50 parado tiver
  IC inteiro acima de zero (bootstrap por bloco de semana da serie diaria da carteira).
"""

import json
import random
import sys
import time
from collections import defaultdict

import dados_binance as DB
import fmz_motor as M
from replay_ema_ribbon import CUSTO_RT

MS_H = 3_600_000
N_DT, K_DT = 4, 0.5
CUSTO_SPOT = 0.0015
LIMIAR_BAL = 0.05


def k_bonferroni():
    """K do estudo 23, lido do log dele (numero de estrategias que avancaram + 4)."""
    try:
        for l in open(M.os.path.join(M.AQUI, "..", "claude", "fmz_triagem.log"), encoding="utf-8"):
            if "| K = " in l:
                return int(l.split("| K = ")[1].split()[0])
    except OSError:
        pass
    print("  AVISO: log do estudo 23 sem K; usando K = 4 (nenhuma avancou)")
    return 4


# ---------------------------------------------------------------------------
# M1 -- Dual Thrust no caminho de 1h
# ---------------------------------------------------------------------------

def niveis_diarios(d):
    """{ts do dia: (linha_compra, linha_venda)} a partir de dias FECHADOS."""
    out = {}
    for t in range(N_DT, len(d)):
        jan = d[t - N_DT:t]
        hh, ll = max(x[2] for x in jan), min(x[3] for x in jan)
        hc, lc = max(x[4] for x in jan), min(x[4] for x in jan)
        rng_ = max(hh - lc, hc - ll)
        out[d[t][0]] = (d[t][1] + K_DT * rng_, d[t][1] - K_DT * rng_)
    return out


def dual_thrust(h, niveis, intradia):
    """Trades no formato do motor, com indices na serie de 1h."""
    trades, pos = [], None          # pos = {d, j, px}
    for i, k in enumerate(h):
        dia = k[0] - k[0] % M.MS_DIA
        if dia not in niveis:
            continue
        up, dn = niveis[dia]
        o, hi, lo, cl = k[1], k[2], k[3], k[4]
        caminho = [o, lo, hi, cl] if cl >= o else [o, hi, lo, cl]
        # gatilho ja ultrapassado na abertura da hora
        eventos = []
        if o >= up:
            eventos.append((0, 1, o))
        elif o <= dn:
            eventos.append((0, -1, o))
        for seg, (a, b) in enumerate(zip(caminho, caminho[1:]), start=1):
            a_, b_ = min(a, b), max(a, b)
            toques = []
            if a_ <= up <= b_ and b > a:
                toques.append((abs(up - a), 1, up))
            if a_ <= dn <= b_ and b < a:
                toques.append((abs(dn - a), -1, dn))
            for _, d_, px in sorted(toques):
                eventos.append((seg, d_, px))
        for _, d_, px in eventos:
            if pos and pos["d"] == d_:
                continue
            if pos:
                trades.append({"d": pos["d"], "j": pos["j"], "k": i, "px_in": pos["px"], "px_out": px,
                               "q": 1.0, "n_stop": 2, "intra": True})
            pos = {"d": d_, "j": i, "px": px}
        ultima_hora_do_dia = (k[0] + MS_H) % M.MS_DIA == 0
        if intradia and pos and ultima_hora_do_dia:
            trades.append({"d": pos["d"], "j": pos["j"], "k": i, "px_in": pos["px"], "px_out": cl,
                           "q": 1.0, "n_stop": 1, "intra": True})
            pos = None
    if pos:
        i = len(h) - 1
        trades.append({"d": pos["d"], "j": pos["j"], "k": i, "px_in": pos["px"], "px_out": h[i][4],
                       "q": 1.0, "n_stop": 1, "intra": True})
    return trades


def medir_1h(h, trades, fund, sym):
    out = []
    for x in trades:
        d, j, k = x["d"], x["j"], x["k"]
        bruto = 100 * d * (x["px_out"] / x["px_in"] - 1)
        slip = M.SLIP_STOP * x["n_stop"]
        liq = bruto - 100 * CUSTO_RT - slip
        fnd = 100 * fund.soma(h[j][0], h[k][0] + MS_H)
        ts_in = h[j + 1][0] if j + 1 < len(h) else None
        out.append({**x, "bruto": bruto, "liq": liq, "abs": liq - d * fnd, "slip": slip,
                    "dur": (k - j) / 24, "ts": h[j][0], "ts_in": ts_in, "ts_out": h[k][0], "sym": sym})
    return out


def excesso_transversal(trades, precos, rng, n=M.N_XS):
    """precos: {sym: {ts: candle}} so com os timestamps necessarios. Linha de
    base: abertura de ts_in -> fechamento de ts_out, mesmo lado, outros pares."""
    por_ts = defaultdict(list)
    for s, p in precos.items():
        for ts in p:
            por_ts[ts].append(s)
    for x in trades:
        x["excesso"] = None
        if x["ts_in"] is None or x["ts_in"] > x["ts_out"]:
            continue
        cand = [s for s in por_ts.get(x["ts_in"], ()) if s != x["sym"] and x["ts_out"] in precos[s]]
        if not cand:
            continue
        if len(cand) > n:
            cand = rng.sample(cand, n)
        base = sum(100 * x["d"] * (precos[s][x["ts_out"]][4] / precos[s][x["ts_in"]][1] - 1) for s in cand)
        x["excesso"] = x["bruto"] - x["slip"] - base / len(cand)


def rodar_dual_thrust(nome_universo):
    rng = random.Random(M.SEED)
    res = {"M1a SAR": [], "M1b intradiario": []}
    syms = []
    for sym in M.universo(nome_universo):
        try:
            d = M.candles(sym)
            h = DB.baixar(sym, "1H", M.DIAS)
        except Exception as e:
            print(f"    {sym:<16} FALHOU: {type(e).__name__}", flush=True)
            continue
        if len(d) < 400 or len(h) < 24 * 300:
            continue
        syms.append(sym)
        niv = niveis_diarios(d)
        fund = M.Funding(sym)
        res["M1a SAR"] += medir_1h(h, dual_thrust(h, niv, False), fund, sym)
        res["M1b intradiario"] += medir_1h(h, dual_thrust(h, niv, True), fund, sym)
    # segunda passada: so os precos de 1h nos timestamps que a linha de base usa
    precisa = set()
    for tr in res.values():
        for x in tr:
            if x["ts_in"] is not None:
                precisa.add(x["ts_in"])
                precisa.add(x["ts_out"])
    precos = {}
    for sym in syms:
        precos[sym] = {k[0]: k for k in DB.baixar(sym, "1H", M.DIAS) if k[0] in precisa}
    for tr in res.values():
        excesso_transversal(tr, precos, rng)
    print(f"  Dual Thrust, universo {nome_universo}: {len(syms)} pares", flush=True)
    return res


# ---------------------------------------------------------------------------
# M2 -- balanceamento 50/50
# ---------------------------------------------------------------------------

def balanceamento(h):
    """Serie diaria (ts_dia, ret_balanceado, ret_parado) a partir de 1h."""
    moeda, caixa = 0.5 / h[0][4], 0.5
    parado = 0.5 / h[0][4]
    diario, ult_v, ult_p, dia_atual = [], 1.0, 1.0, h[0][0] - h[0][0] % M.MS_DIA
    for k in h:
        px = k[4]
        valor = moeda * px
        dif = valor - caixa
        if dif > caixa * LIMIAR_BAL:
            q = dif / 2
            moeda -= q / px
            caixa += q * (1 - CUSTO_SPOT)
        elif dif < -caixa * LIMIAR_BAL:
            q = -dif / 2
            moeda += q * (1 - CUSTO_SPOT) / px
            caixa -= q
        dia = k[0] - k[0] % M.MS_DIA
        if (k[0] + MS_H) % M.MS_DIA == 0:
            v = moeda * px + caixa
            p = parado * px + 0.5
            diario.append((dia, v / ult_v, p / ult_p))
            ult_v, ult_p = v, p
    return diario


def rodar_balanceamento(nome_universo):
    por_dia, por_dia_arit = defaultdict(list), defaultdict(list)
    fim_v, fim_p, n = [], [], 0
    for sym in M.universo(nome_universo):
        try:
            h = DB.baixar(sym, "1H", M.DIAS)
        except Exception:
            continue
        if len(h) < 24 * 300:
            continue
        n += 1
        serie = balanceamento(h)
        v = p = 1.0
        for dia, fv, fp in serie:
            por_dia[dia].append(M.math.log(fv) - M.math.log(fp))
            por_dia_arit[dia].append(fv - fp)
            v *= fv
            p *= fp
        fim_v.append(v)
        fim_p.append(p)
    dias = sorted(por_dia)
    exc = [(d, sum(por_dia[d]) / len(por_dia[d])) for d in dias]
    arit = [(d, sum(por_dia_arit[d]) / len(por_dia_arit[d])) for d in dias]
    ganha = sum(1 for a, b in zip(fim_v, fim_p) if a > b)
    print(f"  Balanceamento, universo {nome_universo}: {n} pares; balanceado > parado no fim em {ganha} "
          f"({100*ganha/max(n,1):.0f}%); mediana fim balanceado {sorted(fim_v)[n//2]:.2f}x, "
          f"parado {sorted(fim_p)[n//2]:.2f}x", flush=True)
    return exc, arit


def bootstrap_serie_semana(serie, conf):
    """Media anualizada (x365) de uma serie diaria, IC por bloco de semana."""
    g = defaultdict(list)
    for d, x in serie:
        g[d // M.MS_SEMANA].append(x)
    blocos = list(g.values())
    media = 365 * sum(sum(b) for b in blocos) / sum(len(b) for b in blocos)
    rng = random.Random(M.SEED)
    ms = []
    for _ in range(M.N_RESAMPLES):
        s = n = 0
        for _ in range(len(blocos)):
            b = blocos[rng.randrange(len(blocos))]
            s += sum(b)
            n += len(b)
        ms.append(365 * s / n)
    ms.sort()
    a = (1 - conf) / 2
    return media, ms[int(a * M.N_RESAMPLES)], ms[min(M.N_RESAMPLES - 1, int((1 - a) * M.N_RESAMPLES))]


# ---------------------------------------------------------------------------
# M4 -- pares contra o BTC
# ---------------------------------------------------------------------------

def razao(c, btc):
    """Candles diarios da razao moeda/BTC nas datas comuns: [ts, o, h, l, c]."""
    b = {k[0]: k for k in btc}
    out = []
    for k in c:
        if k[0] in b:
            kb = b[k[0]]
            o, cl = k[1] / kb[1], k[4] / kb[4]
            out.append([k[0], o, max(o, cl), min(o, cl), cl, 0.0])
    return out


def pares_logica(r):
    cl = [k[4] for k in r]
    ma, dv = M.sma(cl, 20), M.stdev(cl, 20)
    sup = [None if dv[t] is None else ma[t] + 2 * dv[t] for t in range(len(r))]
    inf = [None if dv[t] is None else ma[t] - 2 * dv[t] for t in range(len(r))]

    def logica(br, t):
        if M.cruza(cl, inf, t):
            br.entry("le", 1)
        if M.cruza(cl, sup, t):
            br.entry("se", -1)
        if M.cruza(cl, ma, t):
            br.close_all()
    return logica


def rodar_pares(nome_universo):
    btc = M.candles("BTCUSDT")
    fbtc = M.Funding("BTCUSDT")
    rng = random.Random(M.SEED)
    trades, precos = [], M.Precos()
    for sym in M.universo(nome_universo):
        if sym == "BTCUSDT":
            continue
        try:
            c = M.candles(sym)
        except Exception:
            continue
        r = razao(c, btc)
        if len(r) < 400:
            continue
        precos.add(sym, r)
        fund = M.Funding(sym)
        tr = M.rodar_script(r, pares_logica(r), 25)
        med = M.medir(r, tr, None, rng, 25, sym=sym)
        for x in med:
            x["liq"] = x["bruto"] - 2 * 100 * CUSTO_RT
            t_fim = r[x["k"]][0]
            f = fund.soma(x["ts"], t_fim) - fbtc.soma(x["ts"], t_fim)
            x["abs"] = x["liq"] - x["d"] * 100 * f
        trades += med
    precos.excesso(trades, rng)
    print(f"  Pares, universo {nome_universo}: {len(precos.p)} razoes moeda/BTC", flush=True)
    return trades


# ---------------------------------------------------------------------------

def relatorio_trades(rot, tr, conf):
    dur = sum(x["dur"] for x in tr) / len(tr) if tr else 0
    print(f"\n  [{rot}]  duracao media {dur:.2f} d | trades {len(tr)}")
    for chave, nome in (("liq", "liquido (custo)"), ("abs", "absoluto (custo+funding)"),
                        ("excesso", "EXCESSO transversal (decide)")):
        print(M.linha(nome, tr, chave, conf)[0])
    _, _, lo_a = M.linha("", tr, "abs", conf)
    _, _, lo_e = M.linha("", tr, "excesso", conf)
    return lo_a > 0 and lo_e > 0


def main():
    t0 = time.time()
    K = k_bonferroni()
    conf = 1 - 0.05 / K
    print(f"K = {K} (estudo 23) | confianca no universo DE = {100*conf:.2f}%")
    decisao = {}
    for nome, cf, decide in (("A", 0.95, False), ("DE", conf, True)):
        print("\n" + "=" * 100 + f"\nUNIVERSO {nome} ({'DECIDE' if decide else 'descritivo'})\n" + "=" * 100)
        dt = rodar_dual_thrust(nome)
        for rot, tr in dt.items():
            ok = relatorio_trades(rot, tr, cf)
            if decide:
                decisao[rot] = ok
        pr = rodar_pares(nome)
        ok = relatorio_trades("M4 pares moeda/BTC (Bollinger 20, z=2)", pr, cf)
        if decide:
            decisao["M4 pares"] = ok
        exc, arit = rodar_balanceamento(nome)
        m, lo, hi = bootstrap_serie_semana(exc, cf)
        ma, la, ha = bootstrap_serie_semana(arit, cf)
        print(f"\n  [M2 balanceamento 50/50, 5%]  excesso de LOG-retorno sobre 50/50 parado (decide): "
              f"{100*m:+.2f}%/ano IC{100*cf:.2f} [{100*lo:+.2f}, {100*hi:+.2f}]")
        print(f"  [M2] excesso aritmetico (registro original, descritivo): {100*ma:+.2f}%/ano "
              f"[{100*la:+.2f}, {100*ha:+.2f}]")
        if decide:
            decisao["M2 balanceamento"] = lo > 0
    print("\n  DECISAO (universo DE):")
    for k, v in decisao.items():
        print(f"    {k:<24} {'PASSA' if v else 'NAO PASSA'}")
    print(f"\n  [{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main()
