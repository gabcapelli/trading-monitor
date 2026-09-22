"""
Follow-up PRE-REGISTRADO (22/09/2026) do 1-2-3 de Mark Crisp no diario
(replay_123_crisp.py, estudo 2 de estudos-avulsos.md). Depois da correcao da
regra do candle de entrada, o 1-2-3 no 1Dutc ficou em +0.078R (IC95
[-0.004, +0.160]) nos 20 pares e +0.043R (IC95 [-0.026, +0.115]) nos 80
pares fora da amostra -- o melhor resultado de todos os estudos avulsos, e
ainda assim sem IC inteiro acima de zero.

O QUE ESTE ESTUDO FAZ -- E O QUE NAO FAZ
----------------------------------------
NAO varre parametro nenhum do setup (minimo do movimento 1, posicao do stop,
alvo, filtro de tendencia). Varrer parametros nos mesmos dados e o garimpo
que estudos-avulsos.md proibe: com n=2603 e erro padrao ~0.042R, a melhor de
20 variacoes aparece ~2 erros padrao acima por acaso (~+0.08R).
Faz duas mudancas de mecanismo, decididas antes de rodar:

1. CUSTO MAIS FIEL. O modelo dos outros estudos cobra 0.18% do nocional em
   todo trade (0.04% taxa + 0.05% slippage por lado). Na pratica:
   - entrada por ordem stop: sempre taker -> TAKER + SLIPPAGE.
   - saida no alvo: ordem limite em repouso -> MAKER, sem slippage.
   - saida no stop: stop-market -> TAKER + SLIPPAGE.
   Taxas da OKX para perpetuos: maker 0.02%, taker 0.05%; slippage 0.05% por
   lado nas ordens a mercado/stop [mesma premissa dos outros estudos].
   Resultado: vencedor paga ~0.12%, perdedor ~0.20%.
2. CARTEIRA COM AS REGRAS DO PLANO. Expectancia por trade nao diz se da para
   operar. Simula 1% de risco por trade, teto de 3x de alavancagem, no
   maximo 2 posicoes simultaneas (global) e trava de -6R na semana. Quando
   varios pares disparam no mesmo dia a ordem entre eles e desconhecida ->
   200 sorteios dessa ordem, reportando mediana e faixa p5-p95.

AMOSTRA NOVA (universo C)
-------------------------
Os 80 pares de replay_91_beta.UNIVERSO_B ja foram usados para confirmar o
1-2-3; reutiliza-los agora nao seria mais fora da amostra. Universo C
(fixado antes de baixar precos): perpetuos USDT lineares da OKX, live,
instCategory 1 (cripto), listados ha 400-1000 dias em 22/09/2026, fora de A
e de B -> 83 pares (lista abaixo). Ressalva: sao moedas recentes, muitas
memecoins, e o historico cobre so 2024-2026 -- amostra fresca, mas nao
equivalente as outras.

CRITERIO DE DECISAO (pre-registrado)
------------------------------------
No universo C, com o custo mais fiel e a mesma regra do estudo 2 (stop no
fundo 3, 1Dutc, historico inteiro): PASSA se a expectancia liquida tiver
IC95 inteiro acima de zero (bootstrap reamostrando dias de entrada).
A troca do modelo de custo e deterministica (nao e inferencia) e a carteira
e descritiva: nenhuma das duas decide nada sozinha.
"""

import random
import sys
import time

from replay_ema_ribbon import ic_bootstrap, CUSTO_RT, UNIVERSO
from replay_stoch_vwap import baixar
from replay_123_crisp import candidatos
from replay_91_beta import UNIVERSO_B

TAKER, MAKER, SLIPPAGE = 0.0005, 0.0002, 0.0005
RISCO, ALAV, MAX_POS, LIM_SEMANA = 0.01, 3.0, 2, -0.06
MIN_CANDLES = 400
N_SORTEIOS = 200
SEED = 42

UNIVERSO_C = [f"{x}-USDT-SWAP" for x in """
METIS BONK JTO NMR LQTY JUP ZETA ONE STRK ACH ENJ RAY AEVO ETHFI W MEW WIF
MERL GLM NOT ATH ZK ZRO CVX ONDO RENDER BOME POPCAT BRETT TAO POL HMSTR
EIGEN MOODENG NEIRO GRASS PNUT ACT ARKM MORPHO MOVE ME VIRTUAL VANA PENGU
FARTCOIN AIXBT BIO TRUMP S ANIME BERA LAYER PI KAITO SHELL GPS PARTI
JELLYJELLY BABY WCT INIT SIGN WAL PLUME DOOD SOON HUMA SOPH A KMNO MUBARAK
RESOLV LA HOME SPK SAHARA H AERO SYRUP PUMP SPX USELESS
""".split()]


def resolver(c, cand):
    """Stop no fundo 3, alvo do 1-2-3; custo por tipo de saida."""
    trades, livre = [], 0
    for s in sorted(cand, key=lambda x: x["j"]):
        j, d, entrada, stop, alvo = s["j"], s["d"], s["entrada"], s["stop3"], s["alvo"]
        if j < livre:
            continue
        risco = (entrada - stop) * d
        if risco <= 0 or (alvo - entrada) * d <= 0:
            continue
        rr = (alvo - entrada) * d / risco
        saida = None
        for t in range(j, len(c)):
            hi, lo = c[t][2], c[t][3]
            if ((lo <= stop) if d == 1 else (hi >= stop)) and (t > j or _stop_vale(c[j], d, entrada)):
                saida, r, no_alvo = t, -1.0, False
                break
            if t > j and ((hi >= alvo) if d == 1 else (lo <= alvo)):
                saida, r, no_alvo = t, rr, True
                break
        if saida is None:
            break  # ainda aberto no fim do historico
        custo_frac = (TAKER + SLIPPAGE) + (MAKER if no_alvo else TAKER + SLIPPAGE)
        custo_r = custo_frac * entrada / risco
        custo_flat = CUSTO_RT * entrada / risco
        trades.append({"ts": c[j][0], "saida_ts": c[saida][0], "d": d, "bruto": r,
                       "r": r - custo_r, "r_flat": r - custo_flat, "custo_r": custo_r,
                       "risco_pct": risco / entrada, "ret_pct": r * risco / entrada - custo_frac})
        livre = saida + 1
    return trades


from replay_ema_ribbon import stop_vale_no_candle_entrada as _stop_vale  # noqa: E402


def trades_de(universo):
    todos = []
    for inst in universo:
        c = baixar(inst, "1Dutc", 3000)
        if len(c) < MIN_CANDLES:
            continue
        for x in resolver(c, candidatos(c, 1) + candidatos(c, -1)):
            x["par"] = inst
            todos.append(x)
    return todos


def media(trades, chave="r"):
    return sum(x[chave] for x in trades) / len(trades) if trades else float("nan")


def linha_ic(rotulo, trades, chave="r"):
    if len(trades) < 3:
        return f"  {rotulo}: n={len(trades)} (insuficiente)", False
    lo, hi, dias = ic_bootstrap(trades, chave)
    return (f"  {rotulo}: n={len(trades):>5} | dias={dias:>5} | exp {media(trades, chave):+.3f}R | "
            f"IC95 [{lo:+.3f}, {hi:+.3f}] | custo {media(trades, 'custo_r'):.3f}R"), lo > 0


def carteira(trades, rng):
    tr = sorted(trades, key=lambda x: (x["ts"], rng.random()))
    eq, pico, mdd = 1.0, 1.0, 0.0
    abertos, feitos = [], 0
    semana, perda_sem = None, 0.0

    def fechar_ate(ts):
        nonlocal eq, pico, mdd, perda_sem
        for p in sorted([p for p in abertos if p["saida_ts"] <= ts], key=lambda p: p["saida_ts"]):
            pnl = p["tam"] * p["ret_pct"]
            eq += pnl
            if p["sem"] == semana:
                perda_sem += pnl / p["eq0"]
            pico = max(pico, eq)
            mdd = max(mdd, 1 - eq / pico)
            abertos.remove(p)

    for x in tr:
        fechar_ate(x["ts"])
        sem = x["ts"] // (7 * 86_400_000)
        if sem != semana:
            semana, perda_sem = sem, 0.0
        if len(abertos) >= MAX_POS or perda_sem <= LIM_SEMANA or any(p["par"] == x["par"] for p in abertos):
            continue
        abertos.append({**x, "tam": min(RISCO / x["risco_pct"], ALAV) * eq, "eq0": eq, "sem": sem})
        feitos += 1
    fechar_ate(float("inf"))
    return eq, mdd, feitos


def relatorio_carteira(nome, trades):
    if not trades:
        print(f"  {nome}: sem trades")
        return
    t0, t1 = min(x["ts"] for x in trades), max(x["saida_ts"] for x in trades)
    anos = (t1 - t0) / (365.25 * 86_400_000)
    res = [carteira(trades, random.Random(s)) for s in range(N_SORTEIOS)]
    eqs = sorted(r[0] for r in res)
    mdds = sorted(r[1] for r in res)
    q = lambda v, p: v[int(p * (len(v) - 1))]
    cagr = lambda e: (e ** (1 / anos) - 1) * 100 if anos > 0 and e > 0 else float("nan")
    print(f"  {nome}: {time.strftime('%Y-%m', time.gmtime(t0/1000))} a "
          f"{time.strftime('%Y-%m', time.gmtime(t1/1000))} ({anos:.1f} anos), "
          f"{len(trades)} sinais, {sorted(r[2] for r in res)[N_SORTEIOS//2]} feitos")
    print(f"    patrimonio final: p5 {q(eqs,.05):.2f}x | mediana {q(eqs,.5):.2f}x | p95 {q(eqs,.95):.2f}x")
    print(f"    CAGR mediano {cagr(q(eqs,.5)):+.1f}%/ano | drawdown mediano {100*q(mdds,.5):.0f}% "
          f"| p95 {100*q(mdds,.95):.0f}%")


def mapa_risco(dados):
    """Descritivo: risco por trade x posicoes simultaneas. Nao decide nada --
    escolher o ponto de maior retorno neste historico seria ajuste a dados."""
    global RISCO, MAX_POS
    risco0, pos0 = RISCO, MAX_POS
    print(f"\n{'='*100}\n4) MAPA RISCO x POSICOES (descritivo; mediana de {N_SORTEIOS} sorteios)\n{'='*100}")
    for nome, tr in dados.items():
        if not tr:
            continue
        t0, t1 = min(x["ts"] for x in tr), max(x["saida_ts"] for x in tr)
        anos = (t1 - t0) / (365.25 * 86_400_000)
        print(f"  {nome} ({anos:.1f} anos)")
        print(f"    {'risco':>6} {'pos':>4} | {'CAGR med':>9} {'DD med':>7} {'DD p95':>7} "
              f"{'p5':>6} {'p95':>6} {'trades':>7}")
        for risco in (0.005, 0.01, 0.02):
            for pos in (1, 2, 4, 6):
                RISCO, MAX_POS = risco, pos
                res = [carteira(tr, random.Random(s)) for s in range(N_SORTEIOS)]
                eqs = sorted(r[0] for r in res)
                mdds = sorted(r[1] for r in res)
                q = lambda v, pp: v[int(pp * (len(v) - 1))]
                cagr = (q(eqs, .5) ** (1 / anos) - 1) * 100 if q(eqs, .5) > 0 else float("nan")
                print(f"    {100*risco:>5.1f}% {pos:>4} | {cagr:>+8.1f}% {100*q(mdds,.5):>6.0f}% "
                      f"{100*q(mdds,.95):>6.0f}% {q(eqs,.05):>6.2f} {q(eqs,.95):>6.2f} "
                      f"{sorted(r[2] for r in res)[N_SORTEIOS//2]:>7}", flush=True)
    RISCO, MAX_POS = risco0, pos0


def main():
    if "--baixar" in sys.argv:
        for inst in UNIVERSO_C:
            print(inst, len(baixar(inst, "1Dutc", 3000)), flush=True)
        return

    print(f"{'='*100}\n1) CUSTO: flat 0.18% x custo por tipo de saida (descritivo)\n{'='*100}")
    dados = {}
    for nome, uni in (("A (20 pares)", UNIVERSO), ("B (80 pares)", UNIVERSO_B), ("C (83 novos)", UNIVERSO_C)):
        tr = trades_de(uni)
        dados[nome] = tr
        if not tr:
            continue
        print(f"  {nome}:")
        print(linha_ic("    custo flat 0.18%           ", tr, "r_flat")[0])
        print(linha_ic("    custo por tipo de saida    ", tr, "r")[0])
        alvo = [x for x in tr if x["bruto"] > 0]
        print(f"    saidas no alvo: {100*len(alvo)/len(tr):.1f}% | custo medio no alvo "
              f"{media(alvo, 'custo_r'):.3f}R | no stop {media([x for x in tr if x['bruto'] < 0], 'custo_r'):.3f}R")

    print(f"\n{'='*100}\n2) CARTEIRA (1% de risco, 3x, 2 posicoes, trava -6R/semana; 200 sorteios)\n{'='*100}")
    for nome, tr in dados.items():
        relatorio_carteira(nome, tr)

    print(f"\n{'='*100}\n3) DECISAO -- universo C (amostra nova)\n{'='*100}")
    linha, ok = linha_ic("C (83 pares novos), custo por tipo de saida", dados.get("C (83 novos)", []))
    print(linha)
    print(linha_ic("  so compras                               ",
                   [x for x in dados.get("C (83 novos)", []) if x["d"] == 1])[0])
    print(linha_ic("  so vendas                                ",
                   [x for x in dados.get("C (83 novos)", []) if x["d"] == -1])[0])
    print(f"\n==> DECISAO: {'PASSA' if ok else 'NAO PASSA'}")
    mapa_risco(dados)


if __name__ == "__main__":
    main()
