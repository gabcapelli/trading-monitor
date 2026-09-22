"""
Teste unico, PRE-REGISTRADO (22/09/2026), do "metodo de swing trade com mais
de 80% de acerto" (video do YouTube, acoes da B3): IFR curto sobrevendido
dentro de tendencia de alta, saida no primeiro fechamento lucrativo (Larry
Williams). Estudo avulso: NAO faz parte do checklist dos Setups A/B/C nem do
monitor de producao. Regras e criterio escritos ANTES de rodar qualquer
simulacao. [interp] = interpretacao minha (transcricao automatica ruim).

REGRAS -- SO COMPRA (o video so compra)
---------------------------------------
- Tendencia: MME rapida acima da MME lenta no fechamento do candle de sinal.
  O video comeca com 9 x 11 e termina com 17 x 20 ("comeca a melhorar").
- Sinal: IFR (Wilder) de periodo curto fecha abaixo do nivel.
- Entrada: abertura do candle seguinte ao sinal.
- Stop: minima do candle de sinal menos uma folga. O video usa "50 centavos
  abaixo" da minima -- numa acao de R$10-30, 2-5% de folga, bem longe da
  minima. Em cripto nao ha equivalente direto [interp]: testadas folga zero
  ("minima") e folga de 1 ATR(14) de Wilder no candle de sinal ("minima-1atr").
- Saida: fechamento do primeiro candle que fecha acima do preco de entrada
  (bruto, sem descontar custo [interp]). Variante do fim do video: so a
  partir do 2o candle da posicao ("tendo passado mais do que um dia").
- Variante "sem" stop (o video tambem roda assim): so DESCRITIVA, em % por
  trade, fora da selecao -- sem stop nao ha R para dimensionar pelo plano, e
  medir R pela minima do candle de sinal da numeros explosivos.
- Stop antes do fechamento no mesmo candle (o stop e intra-candle, a saida e
  no fechamento). Abertura ja abaixo do stop -> sinal descartado.
- Uma posicao por par; sinais durante trade aberto ignorados. Trade ainda
  aberto no fim do historico e FECHADO no ultimo fechamento (e nao
  descartado): descartar esconderia justamente a compra que nunca voltou ao
  lucro -- o pior caso da variante sem stop.
[desvio] stops percentuais de 2% / 1.4% (testados no video em acoes) nao
modelados; operacao com opcoes nao modelada.
Custo: 0.18% do nocional ida+volta convertido em R (igual aos outros).

GRADE
-----
Medias (9,11) e (17,20) x IFR 2 e 4 x nivel 25 e 35 x stop minima /
minima-1atr x saida 1o-lucro / 1o-lucro-apos-1-candle = 32 combinacoes, em
1H (300 dias) e 1Dutc (3000 dias), os dois tempos graficos do video = 64
celulas. Mais 16 combinacoes "sem" stop por tempo grafico, so descritivas.
Tambem reportado: taxa de acerto observada, pra comparar com os 80-97% que
o video mostra em acoes.

DADOS
-----
OKX history-candles, universo de 20 pares de replay_ema_ribbon.py, cache
de replay_stoch_vwap.py. Primeiros 60 candles de cada serie so aquecem.

CRITERIO DE DECISAO (pre-registrado, mesmo protocolo do replay_stoch_vwap)
-------------------------------------------------------------------------
Holdout temporal: cada tempo grafico dividido no ponto medio do historico;
na PRIMEIRA metade escolhe-se a celula de maior expectancia liquida em R
(n >= 30 nessa metade); so ela e testada na SEGUNDA metade. PASSA se a
expectancia liquida la tiver IC95 inteiro acima de zero (bootstrap
reamostrando dias de entrada). Grade completa no log so como descritivo.
"""

import time

from replay_ema_ribbon import ic_bootstrap, CUSTO_RT, UNIVERSO
from replay_stoch_vwap import baixar
from replay_91_williams import mme

MEDIAS = [(9, 11), (17, 20)]
IFRS = [2, 4]
NIVEIS = [25, 35]
STOPS = ["minima", "minima-1atr", "sem"]
ATR_N = 14
SAIDAS = ["1o-lucro", "1o-lucro-apos-1"]
TEMPOS = [("1H", 300), ("1Dutc", 3000)]
AQUECIMENTO = 60
MIN_N_SELECAO = 30


def ifr(closes, n):
    """IFR de Wilder."""
    out = [None] * len(closes)
    if len(closes) <= n:
        return out
    ganhos = [max(closes[i] - closes[i - 1], 0) for i in range(1, n + 1)]
    perdas = [max(closes[i - 1] - closes[i], 0) for i in range(1, n + 1)]
    mg, mp = sum(ganhos) / n, sum(perdas) / n
    for i in range(n, len(closes)):
        if i > n:
            dlt = closes[i] - closes[i - 1]
            mg = (mg * (n - 1) + max(dlt, 0)) / n
            mp = (mp * (n - 1) + max(-dlt, 0)) / n
        out[i] = 100.0 if mp == 0 else 100 - 100 / (1 + mg / mp)
    return out


def atr(c, n):
    """ATR de Wilder."""
    out = [None] * len(c)
    trs = [c[0][2] - c[0][3]] + [max(c[i][2], c[i - 1][4]) - min(c[i][3], c[i - 1][4]) for i in range(1, len(c))]
    if len(c) <= n:
        return out
    a = sum(trs[1:n + 1]) / n
    out[n] = a
    for i in range(n + 1, len(c)):
        a = (a * (n - 1) + trs[i]) / n
        out[i] = a
    return out


def simular(c, rapida, lenta, n_ifr, nivel, stop_modo, saida_modo):
    closes = [x[4] for x in c]
    f, s = mme(closes, rapida), mme(closes, lenta)
    rsi = ifr(closes, n_ifr)
    at = atr(c, ATR_N)
    trades = []
    t = AQUECIMENTO
    while t < len(c) - 1:
        if rsi[t] is None or not (f[t] > s[t] and rsi[t] < nivel):
            t += 1
            continue
        j = t + 1
        entrada, ref = c[j][1], c[t][3] - (at[t] if stop_modo == "minima-1atr" else 0.0)
        if entrada <= ref:
            t += 1
            continue
        risco = entrada - ref
        saida = None
        for k in range(j, len(c)):
            if stop_modo != "sem" and c[k][3] <= ref:
                saida, preco = k, min(ref, c[k][1])
                break
            if c[k][4] > entrada and (saida_modo == "1o-lucro" or k > j):
                saida, preco = k, c[k][4]
                break
        aberto = saida is None
        if aberto:
            saida, preco = len(c) - 1, c[-1][4]
        custo_r = CUSTO_RT * entrada / risco
        bruto = (preco - entrada) / risco
        trades.append({"ts": c[j][0], "r": bruto - custo_r, "bruto": bruto, "custo_r": custo_r,
                       "pct": 100 * (preco / entrada - 1 - CUSTO_RT), "candles": saida - j + 1,
                       "aberto": aberto})
        t = saida + 1
    return trades


def combos():
    for rap, len_ in MEDIAS:
        for n in IFRS:
            for nv in NIVEIS:
                for st in STOPS:
                    for sa in SAIDAS:
                        yield f"mme{rap}x{len_} ifr{n}<{nv} stop={st} {sa}", (rap, len_, n, nv, st, sa)


def media(trades, chave="r"):
    return sum(x[chave] for x in trades) / len(trades) if trades else float("nan")


def linha_ic(rotulo, trades):
    if len(trades) < 3:
        return f"  {rotulo}: n={len(trades)} (insuficiente)", False
    lo, hi, dias = ic_bootstrap(trades, "r")
    acerto = sum(x["pct"] > 0 for x in trades) / len(trades)
    return (f"  {rotulo}: n={len(trades):>5} | dias={dias:>5} | exp {media(trades):+.3f}R | "
            f"IC95 [{lo:+.3f}, {hi:+.3f}] | bruto {media(trades, 'bruto'):+.3f}R | "
            f"%/trade {media(trades, 'pct'):+.2f}% | acerto liq {100*acerto:.1f}% | "
            f"pior {min(x['r'] for x in trades):+.1f}R | custo {media(trades, 'custo_r'):.3f}R"), lo > 0


def main():
    celulas = []
    for bar, dias in TEMPOS:
        print(f"\n{'='*110}\n{bar} ({dias} dias max)\n{'='*110}")
        res = {nome: [] for nome, _ in combos()}
        ts_min = ts_max = None
        for inst in UNIVERSO:
            c = baixar(inst, bar, dias)
            if len(c) <= AQUECIMENTO + 10:
                print(f"    {inst:<16} candles={len(c):>6} (curto demais, ignorado)")
                continue
            ts_min = c[0][0] if ts_min is None else min(ts_min, c[0][0])
            ts_max = c[-1][0] if ts_max is None else max(ts_max, c[-1][0])
            n_par = 0
            for nome, p in combos():
                tr = simular(c, *p)
                for x in tr:
                    x["par"] = inst
                res[nome] += tr
                n_par += len(tr)
            print(f"    {inst:<16} candles={len(c):>6} trades(todas as combinacoes)={n_par:>6}", flush=True)
        meio = (ts_min + ts_max) // 2
        print(f"  ponto medio do holdout: {time.strftime('%Y-%m-%d', time.gmtime(meio / 1000))}")
        print("  (stop=sem: so descritivo; exp em R sem sentido, olhar %/tr e acerto)")
        print(f"  {'combinacao':<42} {'n':>5} {'exp liq':>8} {'bruto':>7} {'%/tr':>6} {'acerto':>6} {'pior':>6} | "
              f"{'n tr':>5} {'exp tr':>7} | {'n te':>5} {'exp te':>7}")
        for nome, tr in res.items():
            treino = [x for x in tr if x["ts"] < meio]
            teste = [x for x in tr if x["ts"] >= meio]
            acerto = 100 * sum(x["pct"] > 0 for x in tr) / len(tr) if tr else float("nan")
            pior = min((x["r"] for x in tr), default=float("nan"))
            print(f"  {nome:<42} {len(tr):>5} {media(tr):>+8.3f} {media(tr, 'bruto'):>+7.3f} "
                  f"{media(tr, 'pct'):>+6.2f} {acerto:>5.1f}% {pior:>+6.1f} | {len(treino):>5} {media(treino):>+7.3f} | "
                  f"{len(teste):>5} {media(teste):>+7.3f}")
            if "stop=sem" not in nome:
                celulas.append((bar, nome, treino, teste))

    print(f"\n{'='*110}\nHOLDOUT -- DECIDE\n{'='*110}")
    elegiveis = [x for x in celulas if len(x[2]) >= MIN_N_SELECAO]
    if not elegiveis:
        print(f"  nenhuma celula com n >= {MIN_N_SELECAO} no treino")
        print("\n==> DECISAO: NAO PASSA")
        return
    bar, nome, treino, teste = max(elegiveis, key=lambda x: media(x[2]))
    print(f"  selecionada no treino -> {bar} | {nome}")
    print(linha_ic("treino (1a metade, so referencia)", treino)[0])
    linha, ok = linha_ic("TESTE (2a metade, decide)       ", teste)
    print(linha)
    print(f"\n==> DECISAO: {'PASSA' if ok else 'NAO PASSA'}")


if __name__ == "__main__":
    main()
