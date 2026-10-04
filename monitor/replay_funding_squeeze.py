"""
Estudo 27 -- funding extremo como gatilho de squeeze, PRE-REGISTRADO em
04/10/2026, antes de calcular qualquer retorno desta regra.

HIPOTESE
--------
O carry (estudos 14, 19, 20) usou o funding como PREMIO continuo. Aqui ele e
usado como TIMING direcional: funding muito alto = comprados alavancados
lotados; se o preco comeca a cair, a liquidacao em cascata empurra mais para
baixo (e o espelho para funding muito negativo). Mecanismo de fluxo, nao de
padrao grafico -- a linha que o CLAUDE.md aponta como a unica que ja deu algo.

REGRA (diario UTC, um par de cada vez)
--------------------------------------
- Funding do dia t: soma das taxas da Binance com fundingTime em
  [00:00, 24:00) UTC do dia t (soma, para contratos de 8h, 4h ou 1h ficarem na
  mesma unidade, % por dia). Todas sao conhecidas antes do fechamento do dia t.
  Dia sem nenhuma taxa = sem valor.
- Historico de referencia: os 180 dias anteriores a t (t-180 .. t-1), exigindo
  >= 90 dias com valor. Percentil por posto: p95 = ordenados[int(0.95*(n-1))],
  p5 = ordenados[int(0.05*(n-1))].
- VENDA (comprados lotados): funding(t) >= p95 E funding(t) >= +0.06%/dia
  (2x o padrao de 0.01% a cada 8h) E fechamento(t) < minima(t-1).
- COMPRA (vendidos lotados): funding(t) <= p5 E funding(t) <= -0.03%/dia
  E fechamento(t) > maxima(t-1).
- Entrada na abertura de t+1; saida na abertura de t+1+H, H = 3 dias. Sem stop
  nem alvo. Uma posicao por par; sinal durante trade aberto e ignorado.

Os limiares sao numeros redondos escolhidos sem olhar retorno: p95/p5 e o
"extremo" usual; os pisos absolutos impedem que o topo de uma serie quase
constante conte como extremo; o gatilho (perda da minima / rompimento da
maxima do dia anterior) e o "preco comecando a andar" que o mecanismo exige.

MEDIDAS (fmz_motor.py, % do nocional por trade)
-----------------------------------------------
- `liq`: bruto - 0.18% de custo ida+volta.
- `abs`: liq - funding real pago no periodo (o vendido no funding alto RECEBE).
- `excesso` (decide junto com abs): bruto - media de 30 outros pares do
  universo, mesmo lado, mesmas datas exatas de entrada e saida. NAO inclui
  funding: separa timing de preco do carry recebido.
- `excesso_par` (descritivo): linha de base de mesmo par (estudo 6).
- Bootstrap por bloco de SEMANA de entrada, 5000 reamostragens.

CRITERIO
--------
Universo A (20 majors): so descritivo. Nao ha grade nem selecao -- serve para
achar bug antes do universo que decide.
Universo DE (368 perps da Binance): PASSA se `abs` E `excesso` tiverem IC95
inteiro acima de zero na regra primaria (os dois lados juntos, H = 3).
Se o DE tiver menos de 200 trades na regra primaria, o estudo e registrado como
SEM AMOSTRA PARA DECIDIR, nao como NAO PASSA.

DESCRITIVOS (sem poder de decisao, impressos para leitura)
----------------------------------------------------------
- Por lado (so vendas / so compras).
- H = 1 e H = 7.
- Sem o gatilho de preco (so o funding extremo).
- PLACEBO: a mesma regra com o funding de 365 dias antes no lugar do de t.
  Sem relacao com o posicionamento atual, deve dar excesso ~ 0; se der algo,
  o resultado vem do gatilho de preco ou de um artefato, nao do funding.

NOTA SOBRE AMOSTRA
------------------
D e E ja foram usados em estudos anteriores (14-24), mas nunca com esta regra
nem com nenhuma variante de funding como timing. A regra e unica e congelada,
sem grade, entao nao ha selecao sobre DE.

Uso (rodar de dentro de monitor/):
    python replay_funding_squeeze.py --contar   # so conta sinais, sem retorno
    python replay_funding_squeeze.py            # estudo completo
"""

import random
import sys
import time

import dados_binance as DB
import fmz_motor as M

H_PRIMARIO = 3
JANELA = 180
MIN_HIST = 90
P_ALTO, P_BAIXO = 0.95, 0.05
PISO_VENDA = 0.0006      # +0.06%/dia
PISO_COMPRA = -0.0003    # -0.03%/dia
MIN_DECIDIR = 200


def funding_diario(sym):
    """{ts do dia UTC: soma das taxas do dia}."""
    try:
        serie = DB.baixar_funding(sym, M.DIAS)
    except Exception:
        return {}
    out = {}
    for ts, taxa in serie:
        dia = ts - ts % M.MS_DIA
        out[dia] = out.get(dia, 0.0) + taxa
    return out


def sinais(c, fdia, gatilho=True, defasagem_dias=0):
    """Lista de (t, d): sinal no fechamento do candle t, d = +1 compra / -1 venda."""
    out = []
    desloc = defasagem_dias * M.MS_DIA
    for t in range(1, len(c)):
        ts = c[t][0]
        f = fdia.get(ts - desloc)
        if f is None:
            continue
        hist = [fdia[ts - desloc - k * M.MS_DIA] for k in range(1, JANELA + 1)
                if ts - desloc - k * M.MS_DIA in fdia]
        if len(hist) < MIN_HIST:
            continue
        hist.sort()
        p_alto = hist[int(P_ALTO * (len(hist) - 1))]
        p_baixo = hist[int(P_BAIXO * (len(hist) - 1))]
        if f >= p_alto and f >= PISO_VENDA and (not gatilho or c[t][4] < c[t - 1][3]):
            out.append((t, -1))
        elif f <= p_baixo and f <= PISO_COMPRA and (not gatilho or c[t][4] > c[t - 1][2]):
            out.append((t, 1))
    return out


def trades_de(c, sin, h):
    """Formato do motor: entrada na abertura de t+1, saida na abertura de t+1+h."""
    out, livre_em = [], 0
    for t, d in sin:
        j, k = t + 1, t + 1 + h
        if j < livre_em or k >= len(c):
            continue
        out.append({"d": d, "j": j, "k": k, "px_in": c[j][1], "px_out": c[k][1],
                    "q": 1.0, "n_stop": 0, "intra": False})
        livre_em = k
    return out


VARIANTES = [
    # rotulo, gatilho, H, defasagem (placebo)
    ("PRIMARIA (gatilho, H=3)", True, H_PRIMARIO, 0),
    ("gatilho, H=1", True, 1, 0),
    ("gatilho, H=7", True, 7, 0),
    ("sem gatilho, H=3", False, H_PRIMARIO, 0),
    ("PLACEBO funding -365d, H=3", True, H_PRIMARIO, 365),
]


def rodar(nome_universo, contar=False):
    rng = random.Random(M.SEED)
    res = {v[0]: [] for v in VARIANTES}
    precos = M.Precos()
    n_pares = 0
    for sym in M.universo(nome_universo):
        try:
            c = M.candles(sym)
        except Exception as e:
            print(f"    {sym:<16} FALHOU: {type(e).__name__}", flush=True)
            continue
        fdia = funding_diario(sym)
        if len(c) < 400 or len(fdia) < MIN_HIST + 30:
            continue
        n_pares += 1
        precos.add(sym, c)
        fund = None if contar else M.Funding(sym)
        for rot, gat, h, desl in VARIANTES:
            tr = trades_de(c, sinais(c, fdia, gat, desl), h)
            if contar:
                res[rot] += [{"d": x["d"], "ts": c[x["j"]][0]} for x in tr]
            else:
                res[rot] += M.medir(c, tr, fund, rng, 1, sym=sym)
    if not contar:
        for tr in res.values():
            precos.excesso(tr, rng)
    print(f"  universo {nome_universo}: {n_pares} pares com candles e funding", flush=True)
    return res


def relatorio(rot, tr):
    print(f"\n  [{rot}]  trades {len(tr)}")
    for chave, nome in (("liq", "liquido (custo)"), ("abs", "absoluto (custo+funding)"),
                        ("excesso", "excesso transversal"), ("excesso_par", "excesso mesmo par (descr.)")):
        print(M.linha(nome, tr, chave)[0])
    for d, lado in ((-1, "so vendas"), (1, "so compras")):
        sub = [x for x in tr if x["d"] == d]
        print(M.linha(f"{lado}: abs", sub, "abs")[0])
        print(M.linha(f"{lado}: excesso", sub, "excesso")[0])


def main(argv):
    t0 = time.time()
    contar = "--contar" in argv
    decisao = None
    for nome, decide in (("A", False), ("DE", True)):
        print("\n" + "=" * 100 + f"\nUNIVERSO {nome} ({'DECIDE' if decide else 'descritivo'})"
              + (" -- SO CONTAGEM, sem retorno" if contar else "") + "\n" + "=" * 100)
        res = rodar(nome, contar)
        if contar:
            for rot, tr in res.items():
                vend = sum(1 for x in tr if x["d"] == -1)
                semanas = len({x["ts"] // M.MS_SEMANA for x in tr})
                print(f"  {rot:<30} trades {len(tr):>6} | vendas {vend:>5} | compras {len(tr)-vend:>5} "
                      f"| semanas distintas {semanas:>4}")
            continue
        for rot, tr in res.items():
            relatorio(rot, tr)
        if decide:
            tr = res[VARIANTES[0][0]]
            if len(tr) < MIN_DECIDIR:
                decisao = f"SEM AMOSTRA PARA DECIDIR (n={len(tr)} < {MIN_DECIDIR})"
            else:
                _, _, lo_a = M.linha("", tr, "abs")
                _, _, lo_e = M.linha("", tr, "excesso")
                decisao = "PASSA" if (lo_a > 0 and lo_e > 0) else "NAO PASSA"
    if decisao:
        print(f"\n  DECISAO (universo DE, regra primaria): {decisao}")
    print(f"\n  [{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main(sys.argv[1:])
