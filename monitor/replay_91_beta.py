"""
Teste de follow-up, PRE-REGISTRADO (22/09/2026), do 9.1 de Larry Williams no
diario. Nasce de replay_91_williams.py: la, no 1Dutc, as 8 combinacoes deram
expectancia positiva nas duas metades, mas so as compras ganharam (+0.541R)
e as vendas perderam (-0.309R). Hipotese concorrente: o 9.1 so captura a alta
do mercado (beta) num universo de moedas que sobreviveram, sem timing.

PERGUNTA
--------
As compras do 9.1 rendem mais do que compras em datas ALEATORIAS no mesmo
par, com a mesma duracao? Se for so beta, a diferenca e zero.

REGRA TESTADA (unica, sem grade)
--------------------------------
O original: MME9, sem stop, sem filtro (replay_91_williams.simular com
"mme9", "sem", "nenhum"), so os trades comprados. No 9.1 com stop and
reverse, a compra entra e sai exatamente nos mesmos eventos que no 9.1 so
comprado (a saida da venda e a entrada da compra sao a mesma ordem), entao
os trades comprados sao identicos aos de uma versao so-compra. Escolhida por
ser o original do video, NAO a celula que ganhou no treino (MMA9) -- as 8
combinacoes foram parecidas e escolher a melhor seria garimpo.

LINHA DE BASE
-------------
Para cada compra do 9.1 (par p, entrada no candle j, saida no candle k,
duracao D = k - j): 500 compras aleatorias no mesmo par, entrada na abertura
de um candle s sorteado uniformemente (s >= 60 e s + D < fim da serie),
saida na abertura de s + D. Excesso do trade = retorno % bruto do 9.1 -
SLIPPAGE_STOP - media dos 500 retornos % aleatorios. Custo de 0.18% ida+volta
e funding sao iguais nos dois lados e se cancelam no excesso.
SLIPPAGE_STOP = 0.10% por trade (0.05% em cada ordem stop), margem
conservadora fixada depois do teste sintetico: num passeio aleatorio sem
drift o metodo deu excesso de +0.31% (IC [+0.01, +0.62]) com 24 passos
intra-candle, caindo para +0.17% e +0.11% (nao significativos) com 240 e
1440 passos -- o simulador preenche a ordem stop exatamente no gatilho,
enquanto o preco real pode pular por cima dele. A linha de base entra e sai
na abertura e nao tem essa vantagem; a margem cobre a diferenca.
Funding [interp]: a OKX so da ~3 meses de historico de funding. Assumido
0.03%/dia pago pelas compras (taxa-base de 0.01%/8h), so para o retorno
absoluto; nao afeta o excesso.

DADOS
-----
Universo B (FORA DA AMOSTRA, decide): perpetuos USDT lineares da OKX, live,
instCategory 1 (cripto), listados ha >= 1000 dias em 22/09/2026, excluindo
os 20 do UNIVERSO e stablecoins (USDC) -> 80 pares (lista abaixo, fixada
antes de baixar precos). Usa-se o que houver de 1Dutc ate 3000 dias; par com
menos de 1000 candles diarios e descartado.
Universo A (os 20 de sempre): so descritivo -- e onde a hipotese nasceu.
Ressalvas que o teste NAO resolve: (1) B tambem so tem moedas vivas hoje
(sobrevivencia); (2) B e fora da amostra nos pares, mas nao no tempo -- um
efeito proprio do periodo 2018-2026 apareceria nos dois universos.

CRITERIO DE DECISAO (pre-registrado)
------------------------------------
No universo B: PASSA se o excesso medio por trade tiver IC95 inteiro acima
de zero (bootstrap reamostrando dias de entrada, como nos outros estudos).
Descritivos: retorno absoluto (com custo e funding) no B e no A, excesso no
A, excesso das vendas contra vendas aleatorias (se ha timing, deveria ser
positivo mesmo com o retorno absoluto negativo), fracao do tempo posicionado.
"""

import random
import time
from collections import defaultdict

from replay_ema_ribbon import CUSTO_RT, UNIVERSO, N_RESAMPLES, SEED
from replay_stoch_vwap import baixar
from replay_91_williams import simular, AQUECIMENTO

UNIVERSO_B = [f"{x}-USDT-SWAP" for x in """
FIL ATOM ETC NEO ALGO COMP IOST IOTA ONT QTUM THETA XTZ SNX ZRX DOT BAT SUSHI
YFI CRV UMA BAND KSM TRB RSR ZIL AAVE GRT EGLD 1INCH MASK CFX CHZ MANA SAND
CRO LPT RVN SHIB ICP MINA AXS YGG AGLD DYDX CELO GALA ENS IMX PEOPLE BICO API3
APE GMT LUNA OP ETHW APT LDO GMX MAGIC CORE AR WOO BLUR FLOKI STX PEPE ORDI
HBAR BIGTIME GAS TIA MEME FLOW PYTH SSV INJ AUCTION TURBO SATS
""".split()]
DIAS = 3000
MIN_CANDLES = 1000
N_BASE = 500
FUNDING_DIA = 0.0003
SLIPPAGE_STOP = 0.10  # em %, por trade


def bootstrap(valores_por_dia):
    grupos = list(valores_por_dia.values())
    rng = random.Random(SEED)
    medias = []
    for _ in range(N_RESAMPLES):
        soma = n = 0
        for _ in range(len(grupos)):
            g = grupos[rng.randrange(len(grupos))]
            soma += sum(g)
            n += len(g)
        medias.append(soma / n)
    medias.sort()
    return medias[int(0.025 * N_RESAMPLES)], medias[int(0.975 * N_RESAMPLES) - 1], len(grupos)


def resumo(rotulo, trades, chave):
    if len(trades) < 3:
        return f"  {rotulo}: n={len(trades)} (insuficiente)", False
    por_dia = defaultdict(list)
    for x in trades:
        por_dia[x["ts"] // 86_400_000].append(x[chave])
    lo, hi, dias = bootstrap(por_dia)
    m = sum(x[chave] for x in trades) / len(trades)
    return f"  {rotulo}: n={len(trades):>5} | dias={dias:>5} | media {m:+.2f}% | IC95 [{lo:+.2f}, {hi:+.2f}]", lo > 0


def avaliar(c, rng):
    """Trades do 9.1 original com excesso contra a linha de base aleatoria."""
    trades = simular(c, "mme9", "sem", "nenhum")
    for x in trades:
        dur = x["k"] - x["j"]
        ultimo = len(c) - 1 - dur
        if dur < 1 or ultimo <= AQUECIMENTO:
            x["excesso"] = None
            continue
        base = []
        for _ in range(N_BASE):
            s = rng.randint(AQUECIMENTO, ultimo)
            base.append(100 * (c[s + dur][1] / c[s][1] - 1) * x["d"])
        bruto_pct = x["pct"] + 100 * CUSTO_RT  # pct ja vem liquido de custo
        x["bruto_pct"] = bruto_pct
        x["excesso"] = bruto_pct - SLIPPAGE_STOP - sum(base) / N_BASE
        x["abs"] = x["pct"] - (100 * FUNDING_DIA * dur if x["d"] == 1 else 0.0)
        x["dur"] = dur
    return [x for x in trades if x["excesso"] is not None]


def rodar(universo, rotulo):
    rng = random.Random(SEED)
    todos, expo, usados = [], [], 0
    print(f"\n{'='*100}\n{rotulo}\n{'='*100}")
    for inst in universo:
        c = baixar(inst, "1Dutc", DIAS)
        if len(c) < MIN_CANDLES:
            print(f"    {inst:<18} candles={len(c):>5} (menos de {MIN_CANDLES}, descartado)")
            continue
        usados += 1
        tr = avaliar(c, rng)
        for x in tr:
            x["par"] = inst
        todos += tr
        compras = [x for x in tr if x["d"] == 1]
        dias_comprado = sum(x["dur"] for x in compras)
        expo.append(dias_comprado / (len(c) - AQUECIMENTO))
        bh = 100 * (c[-1][4] / c[AQUECIMENTO][1] - 1)
        exc = sum(x["excesso"] for x in compras) / len(compras) if compras else float("nan")
        print(f"    {inst:<18} candles={len(c):>5} compras={len(compras):>4} excesso medio={exc:+6.2f}% "
              f"buy&hold={bh:+8.1f}%", flush=True)
    compras = [x for x in todos if x["d"] == 1]
    vendas = [x for x in todos if x["d"] == -1]
    print(f"  pares usados: {usados} | fracao media do tempo comprado: {100*sum(expo)/len(expo):.1f}%")
    print(f"  duracao media das compras: {sum(x['dur'] for x in compras)/len(compras):.1f} dias")
    linha, ok = resumo("COMPRAS: excesso sobre compra aleatoria", compras, "excesso")
    print(linha)
    print(resumo("compras: retorno bruto do 9.1         ", compras, "bruto_pct")[0])
    print(resumo("compras: retorno abs (custo+funding)  ", compras, "abs")[0])
    print(resumo("vendas: excesso sobre venda aleatoria ", vendas, "excesso")[0])
    print(resumo("vendas: retorno abs (custo)           ", vendas, "abs")[0])
    return ok


def main():
    t0 = time.time()
    ok_b = rodar(UNIVERSO_B, "UNIVERSO B -- 80 pares fora da amostra -- DECIDE")
    rodar(UNIVERSO, "UNIVERSO A -- os 20 de sempre -- descritivo (onde a hipotese nasceu)")
    print(f"\n==> DECISAO (universo B, excesso das compras): {'PASSA' if ok_b else 'NAO PASSA'}"
          f"   [{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main()
