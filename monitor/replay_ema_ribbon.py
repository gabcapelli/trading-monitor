"""
Teste unico, PRE-REGISTRADO (21/09/2026), do setup "leque de medias" de um
video do YouTube ("Setup para operar criptomoedas em qualquer prazo
operacional"). Estudo avulso: NAO faz parte do checklist dos
Setups A/B/C nem do monitor de producao. Regras e criterio escritos ANTES de
baixar os dados.

REGRAS (fieis ao video; desvios marcados com [desvio])
------------------------------------------------------
- Medias: EMAs de 20, 25, 30, 35, 40, 45, 50 no fechamento -- a versao
  "classica" que o proprio video recomenda como mais confiavel.
  [desvio] a media principal por "raiz quadrada do preco do topo" foi
  descartada: nao e regra objetiva (depende de qual topo e de como
  "transformar em 3 digitos").
- Tendencia de alta no candle t: EMAs empilhadas (20 > 25 > ... > 50) e
  todas subindo (ema[t] > ema[t-1]). Baixa: espelho.
- Gatilho: em tendencia de alta, o candle t toca a primeira media
  (low <= EMA20). Arma ordem de compra stop na maxima de t.
- Ordem nao acionada: a cada candle fechado seguinte, a ordem passa para a
  maxima desse candle ("deixo entrada para ca"). Cancela quando um candle
  FECHA abaixo da EMA50 (a media mais longa). Alinhamento nao e exigido
  enquanto a ordem esta pendente (o video so cita o cancelamento).
- Execucao: aciona no candle j se high[j] >= gatilho; preco = max(gatilho, open[j]).
- Stop: logo abaixo da primeira media NAO tocada durante o recuo (do candle
  de ativacao ate j-1), no valor dela em j-1. Se todas as 7 foram tocadas,
  nao ha media de referencia -> trade descartado. Stop >= entrada -> descartado.
- Saida (a regra do video): metade em 2R, metade em 3R, stop original
  mantido nas duas metades. R = 0.5*perna1 + 0.5*perna2.
  Descritivo (nao decide): alvo cheio em 3R.
  [desvio] "se o alvo ficar percentualmente muito amplo, trabalhar 2:1"
  e discricionario -- nao modelado.
- Conservador em ambiguidade intra-candle: no candle da entrada so o stop
  pode ser atingido; se stop e alvo caem no mesmo candle, conta stop.
- Uma posicao por par por vez; setups durante trade aberto sao ignorados.
  Trades ainda abertos no fim do historico sao descartados.
- Custo: 0.18% do nocional ida+volta (0.04% taxa + 0.05% slippage por lado,
  mesmo valor do liquidation-cascade), convertido em R pela distancia do stop.
- Shorts: espelho exato.

DADOS
-----
OKX history-candles, os 10 pares do trading-monitor (PAIRS). Rerodado em
21/09/2026 no UNIVERSO de 20 pares (mesmas regras e criterio; a decisao
passa a ser sobre os 20).
4H e 1Dutc: todo o historico disponivel ate 2000 dias (o diario em 300 dias
teria poucos trades). 1H e 15m: 300 dias (mesma janela do replay.py).
Primeiros 150 candles de cada serie so aquecem as EMAs.

CRITERIO DE DECISAO (pre-registrado)
------------------------------------
Por tempo grafico, a estrategia PASSA se a expectancia liquida (R, regra
2R/3R) tiver IC95 inteiro acima de zero (bootstrap reamostrando DIAS de
entrada, pra respeitar a correlacao entre os 10 pares).
Decidem: 4H e 1D -- onde momentum tem alguma chance teorica.
15m e 1H: so descritivo (o video os inclui em "qualquer prazo"; 15m o
proprio autor chama de "desastre").
"""

import json
import os
import random
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone

import fetch_and_check as m

# Universo fixo pra TODOS os estudos avulsos de estrategia (decidido em
# 21/09/2026, antes de rodar qualquer estrategia nele): os 10 pares do monitor
# + 10 de grande market cap disponiveis na OKX (XMR e TON nao existem la).
# Nao trocar por estrategia -- escolher o universo depois de ver o resultado
# e so outra forma de otimizar. Vies de sobrevivencia: sao as grandes de HOJE.
PARES_NOVOS = [
    "BNB-USDT-SWAP", "TRX-USDT-SWAP", "ZEC-USDT-SWAP", "HYPE-USDT-SWAP",
    "ADA-USDT-SWAP", "XLM-USDT-SWAP", "NEAR-USDT-SWAP", "AVAX-USDT-SWAP",
    "LTC-USDT-SWAP", "BCH-USDT-SWAP",
]
UNIVERSO = list(m.PAIRS) + PARES_NOVOS

PERIODOS = [20, 25, 30, 35, 40, 45, 50]
AQUECIMENTO = 150
CUSTO_RT = 0.0018
TEMPOS = [("4H", 2000, True), ("1Dutc", 2000, True), ("1H", 300, False), ("15m", 300, False)]
MS_BAR = {"15m": 900_000, "1H": 3_600_000, "4H": 14_400_000, "1Dutc": 86_400_000}
N_RESAMPLES = 5000
SEED = 42
CACHE_DIR = os.environ.get("EMA_RIBBON_CACHE", "cache_ema_ribbon")


# ---------------------------------------------------------------------------
# Dados
# ---------------------------------------------------------------------------

def baixar(inst_id, bar, dias):
    fpath = os.path.join(CACHE_DIR, f"{inst_id}_{bar}_{dias}.json")
    if os.path.exists(fpath):
        with open(fpath) as f:
            return json.load(f)
    limite = int(time.time() * 1000) - dias * 86_400_000
    todos, after = {}, None
    while True:
        params = {"instId": inst_id, "bar": bar, "limit": 100}
        if after:
            params["after"] = after
        for tentativa in range(5):
            try:
                raw = m.okx_get("/api/v5/market/history-candles", params)
                break
            except Exception as e:
                if tentativa == 4:
                    raise
                time.sleep(2 + 2 * tentativa)
        time.sleep(0.12)  # limite da OKX: 20 req / 2 s
        if not raw:
            break
        for r in raw:
            if r[8] == "1":  # so candles fechados
                todos[int(r[0])] = [int(r[0]), float(r[1]), float(r[2]), float(r[3]), float(r[4])]
        mais_antigo = min(int(r[0]) for r in raw)
        if mais_antigo <= limite:
            break
        after = str(mais_antigo)
    candles = [todos[k] for k in sorted(todos) if k >= limite]
    os.makedirs(CACHE_DIR, exist_ok=True)
    with open(fpath, "w") as f:
        json.dump(candles, f)
    return candles


def emas(closes):
    out = []
    for p in PERIODOS:
        k = 2 / (p + 1)
        e, serie = closes[0], []
        for c in closes:
            e = c * k + e * (1 - k)
            serie.append(e)
        out.append(serie)
    return out  # out[i][t] = EMA de PERIODOS[i] no candle t


# ---------------------------------------------------------------------------
# Simulacao
# ---------------------------------------------------------------------------

def tendencia(E, t):
    v = [E[i][t] for i in range(len(PERIODOS))]
    subindo = all(E[i][t] > E[i][t - 1] for i in range(len(PERIODOS)))
    caindo = all(E[i][t] < E[i][t - 1] for i in range(len(PERIODOS)))
    if subindo and all(v[i] > v[i + 1] for i in range(len(v) - 1)):
        return 1
    if caindo and all(v[i] < v[i + 1] for i in range(len(v) - 1)):
        return -1
    return 0


def desfecho(c, j, d, entrada, stop, alvos):
    """Resultado em R por perna, a partir do candle j (entrada). None = nao fechou."""
    risco = abs(entrada - stop)
    resultados = [None] * len(alvos)
    for t in range(j, len(c)):
        hi, lo = c[t][2], c[t][3]
        bateu_stop = lo <= stop if d == 1 else hi >= stop
        for n, a in enumerate(alvos):
            if resultados[n] is not None:
                continue
            if bateu_stop:
                resultados[n] = -1.0
            elif t > j:
                preco_alvo = entrada + d * a * risco
                if (hi >= preco_alvo) if d == 1 else (lo <= preco_alvo):
                    resultados[n] = float(a)
        if all(r is not None for r in resultados):
            return resultados, t
    return None, None


def simular_par(c):
    closes = [x[4] for x in c]
    E = emas(closes)
    trades = []
    t = AQUECIMENTO
    pendente = None  # dict(d, gatilho, ativacao)
    while t < len(c):
        if pendente is None:
            d = tendencia(E, t)
            toque = (d == 1 and c[t][3] <= E[0][t]) or (d == -1 and c[t][2] >= E[0][t])
            if d != 0 and toque:
                pendente = {"d": d, "gatilho": c[t][2] if d == 1 else c[t][3], "ativacao": t}
            t += 1
            continue

        d, j = pendente["d"], t
        acionou = c[j][2] >= pendente["gatilho"] if d == 1 else c[j][3] <= pendente["gatilho"]
        if acionou:
            entrada = max(pendente["gatilho"], c[j][1]) if d == 1 else min(pendente["gatilho"], c[j][1])
            recuo = range(pendente["ativacao"], j)
            if d == 1:
                extremo = min(c[k][3] for k in recuo)
                tocadas = [i for i in range(len(PERIODOS)) if any(c[k][3] <= E[i][k] for k in recuo)]
            else:
                extremo = max(c[k][2] for k in recuo)
                tocadas = [i for i in range(len(PERIODOS)) if any(c[k][2] >= E[i][k] for k in recuo)]
            pendente = None
            ref = max(tocadas) + 1
            if ref >= len(PERIODOS):
                t = j + 1
                continue
            stop = E[ref][j - 1]
            if (d == 1 and stop >= entrada) or (d == -1 and stop <= entrada):
                t = j + 1
                continue
            res, t_saida = desfecho(c, j, d, entrada, stop, [2, 3])
            if res is None:
                break
            custo_r = CUSTO_RT * entrada / abs(entrada - stop)
            trades.append({
                "ts": c[j][0], "d": d,
                "r_video": 0.5 * res[0] + 0.5 * res[1] - custo_r,
                "r_3r": res[1] - custo_r,
                "custo_r": custo_r,
            })
            t = t_saida + 1
            continue

        fechou_alem = c[j][4] < E[-1][j] if d == 1 else c[j][4] > E[-1][j]
        if fechou_alem:
            pendente = None
        else:
            pendente["gatilho"] = c[j][2] if d == 1 else c[j][3]
        t += 1
    return trades


# ---------------------------------------------------------------------------
# Estatistica
# ---------------------------------------------------------------------------

def ic_bootstrap(trades, chave):
    por_dia = defaultdict(list)
    for tr in trades:
        por_dia[tr["ts"] // 86_400_000].append(tr[chave])
    grupos = list(por_dia.values())
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
    v = [tr[chave] for tr in trades]
    media = sum(v) / len(v)
    lo, hi, dias = ic_bootstrap(trades, chave)
    return (f"  {rotulo}: n={len(v):>5} | dias={dias:>5} | exp {media:+.3f}R | "
            f"IC95 [{lo:+.3f}, {hi:+.3f}] | %pos {100*sum(x > 0 for x in v)/len(v):.1f}%"), lo > 0


def main():
    decisao = {}
    for bar, dias, decide in TEMPOS:
        todos = []
        periodo = []
        print(f"\n{'='*88}\n{bar}  ({dias} dias max){'  -- DECIDE' if decide else '  -- descritivo'}\n{'='*88}")
        for inst in UNIVERSO:
            c = baixar(inst, bar, dias)
            tr = simular_par(c)
            for x in tr:
                x["par"] = inst
            todos += tr
            if c:
                ini = datetime.fromtimestamp(c[0][0] / 1000, tz=timezone.utc).strftime("%Y-%m-%d")
                periodo.append(f"{inst.split('-')[0]}:{ini}")
            exp = sum(x["r_video"] for x in tr) / len(tr) if tr else float("nan")
            print(f"    {inst:<16} candles={len(c):>6} trades={len(tr):>4} exp={exp:+.3f}R", flush=True)
        linha, ok = resumo("regra do video (2R/3R)", todos, "r_video")
        print(linha)
        print(resumo("descritivo: 3R cheio   ", todos, "r_3r")[0])
        print(resumo("so compras (video)     ", [x for x in todos if x["d"] == 1], "r_video")[0])
        print(resumo("so vendas (video)      ", [x for x in todos if x["d"] == -1], "r_video")[0])
        print(resumo("so 10 pares originais  ", [x for x in todos if x["par"] not in PARES_NOVOS], "r_video")[0])
        print(resumo("so 10 pares novos      ", [x for x in todos if x["par"] in PARES_NOVOS], "r_video")[0])
        if todos:
            print(f"  custo medio por trade: {sum(x['custo_r'] for x in todos)/len(todos):.3f}R")
        print(f"  inicio dos dados: {', '.join(periodo)}")
        if decide:
            decisao[bar] = ok
    print(f"\n==> DECISAO: " + ", ".join(f"{b}: {'PASSA' if ok else 'NAO PASSA'}" for b, ok in decisao.items()))


if __name__ == "__main__":
    main()
