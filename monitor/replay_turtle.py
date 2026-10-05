"""
Estudo 34 -- Turtle canonico (Donchian), PRE-REGISTRADO em 04/10/2026, antes
de calcular qualquer retorno. Familia de 2 hipoteses no DE com o estudo 33
(replay_lead_lag.py): IC de 97.5% (Bonferroni, K = 2). O 33 parou no portao
da etapa 1 sem usar o DE; o K = 2 fica como registrado (conservador).

POR QUE
-------
Tendencia ja deu zero em tres formas (setups com stop/alvo, transversal,
EWMAC do Carver). A forma mais famosa de rompimento de canal -- as regras dos
Turtles -- nunca foi testada como regra unica com os parametros publicados.
Fecha a familia: se der zero, nao ha motivo para reabrir tendencia.

REGRA (Sistema 2, diario UTC, os dois lados, parametros originais)
------------------------------------------------------------------
- N = ATR(20) (media de Wilder do true range).
- Entrada: fechamento(t) acima da maxima dos 55 dias anteriores -> compra na
  abertura de t+1; abaixo da minima dos 55 -> venda. (Os Turtles entravam no
  rompimento intradiario; aqui o sinal e no fechamento, simplificacao comum,
  sem lookahead.)
- Stop: 2N a partir do fechamento do dia do sinal, ordem stop ativa desde o
  candle da entrada (caminho OHLC do fmz_motor).
- Saida: fechamento abaixo da minima dos 20 dias anteriores (comprado) /
  acima da maxima dos 20 (vendido) -> sai na abertura seguinte.
- Sem piramidacao, uma posicao por par; sinal contrario reverte.
Omitidos por simplificacao: piramidacao em 1/2 N e o filtro do Sistema 1 de
pular o sinal depois de um trade vencedor.

MEDIDAS E CRITERIO (fmz_motor.py, % por trade)
----------------------------------------------
`abs` (custo 0.18% + 0.05% por execucao stop + funding real), `excesso`
transversal (mesmo lado, mesmas datas, 30 outros pares). Bootstrap por semana.
A (20 majors): descritivo. DE (368 perps): PASSA se `abs` E `excesso` com
IC97.5 > 0 no Sistema 2. Menos de 200 trades no DE: sem amostra.

DESCRITIVO
----------
Sistema 1 (entrada 20, saida 10, mesmo stop); so compras; so vendas.

Uso (de dentro de monitor/):
    python replay_turtle.py
"""

import random
import sys
import time

import fmz_motor as M

CONF_DE = 1 - 0.05 / 2
MIN_DECIDIR = 200


def canal(c, n, i, f):
    """f(max/min) do indice i (2=high, 3=low) nos n candles ANTERIORES a t."""
    out = [None] * len(c)
    for t in range(n, len(c)):
        out[t] = f(x[i] for x in c[t - n:t])
    return out


def logica_turtle(c, n_in, n_out):
    hh_in, ll_in = canal(c, n_in, 2, max), canal(c, n_in, 3, min)
    hh_out, ll_out = canal(c, n_out, 2, max), canal(c, n_out, 3, min)
    N = M.atr(c, 20)

    def logica(br, t):
        if hh_in[t] is None or N[t] is None:
            return
        cl, pos = c[t][4], br.pos
        if pos > 0 and cl < ll_out[t]:
            br.close("L")
        if pos < 0 and cl > hh_out[t]:
            br.close("S")
        if pos <= 0 and cl > hh_in[t]:
            br.entry("L", 1)
            br.exit("L", stop=cl - 2 * N[t])
        elif pos >= 0 and cl < ll_in[t]:
            br.entry("S", -1)
            br.exit("S", stop=cl + 2 * N[t])
    return logica


SISTEMAS = [("SISTEMA 2 (55/20) -- decide", 55, 20), ("Sistema 1 (20/10) -- descritivo", 20, 10)]


def rodar(nome):
    rng = random.Random(M.SEED)
    res = {s[0]: [] for s in SISTEMAS}
    precos = M.Precos()
    n = 0
    for sym in M.universo(nome):
        try:
            c = M.candles(sym)
        except Exception:
            continue
        if len(c) < 400:
            continue
        n += 1
        precos.add(sym, c)
        fund = M.Funding(sym)
        for rot, a, b in SISTEMAS:
            tr = M.rodar_script(c, logica_turtle(c, a, b), 60)
            res[rot] += M.medir(c, tr, fund, rng, 60, sym=sym)
    for tr in res.values():
        precos.excesso(tr, rng)
    print(f"  universo {nome}: {n} pares", flush=True)
    return res


def main(argv):
    t0 = time.time()
    decisao = None
    for nome, conf, decide in (("A", 0.95, False), ("DE", CONF_DE, True)):
        print("\n" + "=" * 100 + f"\nUNIVERSO {nome} ({'DECIDE, IC97.5' if decide else 'descritivo'})\n" + "=" * 100)
        res = rodar(nome)
        for rot, tr in res.items():
            dur = sum(x["dur"] for x in tr) / len(tr) if tr else 0
            print(f"\n  [{rot}]  trades {len(tr)} | duracao media {dur:.1f} d | "
                  f"acerto {100*sum(x['liq'] > 0 for x in tr)/max(len(tr),1):.1f}%")
            for chave, n in (("liq", "liquido (custo)"), ("abs", "absoluto (custo+funding)"),
                             ("excesso", "excesso transversal"), ("excesso_par", "excesso mesmo par (descr.)")):
                print(M.linha(n, tr, chave, conf)[0])
            for d, lado in ((1, "so compras"), (-1, "so vendas")):
                sub = [x for x in tr if x["d"] == d]
                print(M.linha(f"{lado}: abs", sub, "abs", conf)[0])
                print(M.linha(f"{lado}: excesso", sub, "excesso", conf)[0])
        if decide:
            tr = res[SISTEMAS[0][0]]
            if len(tr) < MIN_DECIDIR:
                decisao = f"SEM AMOSTRA PARA DECIDIR (n={len(tr)})"
            else:
                _, _, lo_a = M.linha("", tr, "abs", conf)
                _, _, lo_e = M.linha("", tr, "excesso", conf)
                decisao = "PASSA" if (lo_a > 0 and lo_e > 0) else "NAO PASSA"
    print(f"\n  DECISAO (universo DE, Sistema 2): {decisao}\n  [{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main(sys.argv[1:])
