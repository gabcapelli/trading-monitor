"""
Teste unico, PRE-REGISTRADO (21/09/2026), do "1-2-3 de Mark Crisp" como
apresentado no video "Swing trade, tecnica simples e eficiente! Price Action
na veia". Estudo avulso, fora dos Setups A/B/C. Regras e criterio escritos
ANTES de baixar os dados. Reusa fetch/cache/bootstrap de replay_ema_ribbon.py.

REGRAS -- COMPRA (venda e espelho exato); [interp] = interpretacao minha
-------------------------------------------------------------------------
Tudo pelo FECHAMENTO comparado ao fechamento anterior.
- Movimento 1: >= 2 fechamentos seguidos mais baixos [interp: o video nao da
  minimo; os exemplos sempre tem mais de um]. Termina no primeiro candle que
  fecha mais alto. Fundo 1 = menor minima do movimento 1 (incluindo o candle
  que o encerra).
- Movimento 2: fechamentos mais altos. Topo 2 = maior maxima do movimento 2.
  Termina no primeiro candle que fecha mais baixo -> comeca o movimento 3.
- Movimento 3: fechamentos mais baixos. Fechar abaixo do fundo 1 cancela o
  setup (em qualquer momento antes da entrada).
- Entrada ("o que acontecer primeiro"): desde o inicio do movimento 3 fica
  armada compra stop na maxima do topo 2. Todo candle que fecha mais alto
  que o anterior (o primeiro deles encerra o movimento 3) puxa a entrada
  para a maxima dele. Aciona no candle j se high[j] >= gatilho;
  preco = max(gatilho, open[j]).
- Stop: abaixo do fundo 3 = menor minima desde o inicio do movimento 3 ate
  j-1 (a opcao que o autor diz preferir). Descritivo: abaixo do fundo 1.
- Alvo: amplitude fundo 1 -> topo 2, projetada a partir do preco de entrada.
- Saida so por alvo ou stop. [desvio] a saida por "sinal inverso",
  mencionada uma vez no video, nao foi modelada.
- Deteccao de setup e independente da posicao; depois, por par, pega os
  trades em ordem cronologica ignorando os que entrariam com outro aberto.
- Conservador intra-candle: no candle da entrada so o stop pode ser
  atingido; stop e alvo no mesmo candle = stop.
- Custo: 0.18% do nocional ida+volta, convertido em R (igual ao ema_ribbon).

DADOS
-----
OKX, os 10 pares do trading-monitor. Rerodado em 21/09/2026 no UNIVERSO
de 20 pares (replay_ema_ribbon.py); mesmas regras e criterio, decisao
sobre os 20. 1Dutc e 1Wutc: todo o historico ate 3000 dias. 4H: ate 2000
dias. 1H: 300 dias.

CRITERIO DE DECISAO (pre-registrado)
------------------------------------
Por tempo grafico, PASSA se a expectancia liquida (R, stop no fundo 3) tiver
IC95 inteiro acima de zero (bootstrap reamostrando dias de entrada).
Decidem: 1D e 1W (onde o autor recomenda usar e afirma 66-68% de acerto com
payoff 1.3-1.4). 4H e 1H: descritivo (intraday, segundo ele, ~55% e 1.1-1.2).
Tambem reportados: taxa de acerto e payoff observados, pra comparar com o
que o video afirma.
"""

import sys

import fetch_and_check as m
from replay_ema_ribbon import baixar, ic_bootstrap, CUSTO_RT, UNIVERSO, PARES_NOVOS

MIN_MOV1 = 2
TEMPOS = [("1Dutc", 3000, True), ("1Wutc", 3000, True), ("4H", 2000, False), ("1H", 300, False)]


def candidatos(c, d):
    """Setups 1-2-3 na direcao d (1 compra, -1 venda). Independente de posicao."""
    # espelho: pra venda, inverte o sinal dos precos (maxima vira minima)
    if d == 1:
        o = [x[1] for x in c]; h = [x[2] for x in c]; lo = [x[3] for x in c]; cl = [x[4] for x in c]
    else:
        o = [-x[1] for x in c]; h = [-x[3] for x in c]; lo = [-x[2] for x in c]; cl = [-x[4] for x in c]

    out = []
    estado, run, ini_run = 0, 0, None
    fundo1 = topo2 = gatilho = None
    ini_mov3 = None
    for t in range(1, len(c)):
        sobe, desce = cl[t] > cl[t - 1], cl[t] < cl[t - 1]

        if estado in (3, 4):
            if h[t] >= gatilho:  # acionou
                entrada = max(gatilho, o[t])
                fundo3 = min(lo[ini_mov3:t])
                out.append({"j": t, "entrada": entrada, "stop3": fundo3, "stop1": fundo1,
                            "alvo": entrada + (topo2 - fundo1)})
                estado, run = 0, 0
                continue
            if cl[t] < fundo1:  # perdeu o fundo 1 -> cancela
                estado, run, ini_run = 0, 1, t
                continue
            if sobe:
                gatilho = h[t]  # fechamento mais alto puxa a entrada pra maxima dele
                estado = 4
            continue

        if estado == 0:
            if desce:
                if run == 0:
                    ini_run = t
                run += 1
            elif sobe:
                if run >= MIN_MOV1:
                    fundo1 = min(lo[ini_run:t + 1])
                    topo2 = h[t]
                    estado = 2
                run = 0
            continue

        if estado == 2:
            if sobe:
                topo2 = max(topo2, h[t])
            elif desce:
                if cl[t] < fundo1:
                    estado, run, ini_run = 0, 1, t
                    continue
                estado, gatilho, ini_mov3 = 3, topo2, t
    # volta pra escala de preco real
    if d == -1:
        for x in out:
            for k in ("entrada", "stop3", "stop1", "alvo"):
                x[k] = -x[k]
    for x in out:
        x["d"] = d
    return out


def resolver(c, cand, chave_stop):
    """Aplica stop/alvo; retorna trades (uma posicao por vez por par)."""
    trades, livre_a_partir = [], 0
    for s in sorted(cand, key=lambda x: x["j"]):
        j, d, entrada, stop, alvo = s["j"], s["d"], s["entrada"], s[chave_stop], s["alvo"]
        if j < livre_a_partir:
            continue
        risco = (entrada - stop) * d
        if risco <= 0 or (alvo - entrada) * d <= 0:
            continue
        rr = (alvo - entrada) * d / risco
        saida = None
        for t in range(j, len(c)):
            hi, lo = c[t][2], c[t][3]
            if (lo <= stop) if d == 1 else (hi >= stop):
                saida, r = t, -1.0
                break
            if t > j and ((hi >= alvo) if d == 1 else (lo <= alvo)):
                saida, r = t, rr
                break
        if saida is None:
            break  # ainda aberto no fim do historico
        custo_r = CUSTO_RT * entrada / (risco)
        trades.append({"ts": c[j][0], "d": d, "r": r - custo_r, "bruto": r, "rr": rr, "custo_r": custo_r})
        livre_a_partir = saida + 1
    return trades


def resumo(rotulo, trades):
    if len(trades) < 3:
        print(f"  {rotulo}: n={len(trades)} (insuficiente)")
        return False
    v = [x["r"] for x in trades]
    lo, hi, dias = ic_bootstrap(trades, "r")
    ganhos = [x for x in trades if x["bruto"] > 0]
    acerto = len(ganhos) / len(trades)
    payoff = sum(x["rr"] for x in ganhos) / len(ganhos) if ganhos else float("nan")
    print(f"  {rotulo}: n={len(v):>5} | dias={dias:>5} | exp {sum(v)/len(v):+.3f}R | "
          f"IC95 [{lo:+.3f}, {hi:+.3f}] | acerto {100*acerto:.1f}% | payoff {payoff:.2f} | "
          f"custo {sum(x['custo_r'] for x in trades)/len(trades):.3f}R")
    return lo > 0


def main():
    decisao = {}
    for bar, dias, decide in TEMPOS:
        print(f"\n{'='*96}\n{bar} ({dias} dias max){'  -- DECIDE' if decide else '  -- descritivo'}\n{'='*96}")
        t3, t1 = [], []
        for inst in UNIVERSO:
            c = baixar(inst, bar, dias)
            cand = candidatos(c, 1) + candidatos(c, -1)
            a, b = resolver(c, cand, "stop3"), resolver(c, cand, "stop1")
            for x in a:
                x["par"] = inst
            t3 += a
            t1 += b
            exp = sum(x["r"] for x in a) / len(a) if a else float("nan")
            print(f"    {inst:<16} candles={len(c):>6} trades={len(a):>4} exp={exp:+.3f}R", flush=True)
        ok = resumo("stop fundo 3 (principal)", t3)
        resumo("so compras           ", [x for x in t3 if x["d"] == 1])
        resumo("so vendas            ", [x for x in t3 if x["d"] == -1])
        resumo("so 10 pares originais", [x for x in t3 if x["par"] not in PARES_NOVOS])
        resumo("so 10 pares novos    ", [x for x in t3 if x["par"] in PARES_NOVOS])
        resumo("descr.: stop fundo 1 ", t1)
        if decide:
            decisao[bar] = ok
    print(f"\n==> DECISAO: " + ", ".join(f"{b}: {'PASSA' if ok else 'NAO PASSA'}" for b, ok in decisao.items()))


if __name__ == "__main__":
    main()
