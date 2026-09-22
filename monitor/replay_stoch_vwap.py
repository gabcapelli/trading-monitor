"""
Teste unico, PRE-REGISTRADO (22/09/2026), do sistema "estocastico + bandas
VWAP / media 144" de um video do YouTube ("operacoes Scalp em 5 minutos",
feito no indice futuro da B3). Estudo avulso: NAO faz parte do checklist dos
Setups A/B/C nem do monitor de producao. Regras e criterio escritos ANTES de
rodar qualquer simulacao. [interp] = interpretacao minha (transcricao
automatica ruim; o video remete a um video anterior que nao temos).

REGRAS -- COMPRA (venda e espelho exato)
----------------------------------------
Estocastico lento (n, suavizacao do %K, %D). Cruzamento de alta no candle t:
%K[t] > %D[t] e %K[t-1] <= %D[t-1].

V1 -- bandas VWAP (o foco do video; intraday)
- VWAP ancorada no dia UTC [interp: cripto nao tem pregao], preco tipico
  (H+L+C)/3 ponderado pelo volume em moeda base; bandas = VWAP +- k*desvio
  padrao ponderado desde a ancora.
- Toque: minima <= banda inferior arma a compra. Arma so a partir da 2a hora
  do dia UTC [interp: na primeira hora o desvio e quase zero e qualquer candle
  "toca"]. Toque na banda oposta troca o lado armado.
- Sinal: primeiro cruzamento de alta do estocastico no candle do toque ou
  depois. Cancela se um candle fechar acima da VWAP central antes do
  cruzamento, ou na virada do dia UTC [interp: o video nao diz ate quando
  espera].
- Stop: menor minima do toque ate o candle de sinal [interp: o video diz
  "stop nessa minima"; o extremo do recuo e a leitura mais conservadora].

V2 -- media movel 144 (o video a usa em 120/240 min, sem VWAP)
- Sinal: cruzamento de alta do estocastico com a MM144 simples subindo
  (MM[t] > MM[t-1]) [interp: simples; o video nao diz]. Contra a media o
  autor opera "posicao microscopica" -> nao modelado (nao opera).
- Stop: minima do candle de sinal.

Comum as duas
- Entrada (as duas testadas na grade):
  "abertura": abertura do candle seguinte ao sinal.
  "rompimento": compra stop na maxima do candle de sinal, valida enquanto o
  estocastico nao cruzar de volta para baixo ("por enquanto ta desfeito o
  sinal"); aciona no candle j se high[j] >= gatilho; preco = max(gatilho,
  open[j]); stop = menor minima do inicio do recuo (V1) ou do candle de sinal
  (V2) ate j-1.
- Alvo: 2R fixo ("alvo duas vezes o risco", o que ele mais repete). [desvio]
  alvos alternativos (topo anterior, 161%, sair/virar na banda oposta) nao
  modelados.
- Conservador intra-candle: no candle da entrada so o stop pode ser atingido;
  stop e alvo no mesmo candle = stop. Stop >= entrada -> descartado.
- Uma posicao por par por vez; sinais durante trade aberto ignorados.
  Trades ainda abertos no fim do historico sao descartados.
- Custo: 0.18% do nocional ida+volta convertido em R (igual aos outros
  estudos avulsos). Expectancia bruta (sem custo) reportada como descritivo,
  pra separar "sem edge" de "edge comido pelo custo".

GRADE (pedida pelo Gabriel em 22/09/2026)
-----------------------------------------
Estocastico (14,3,3), (8,3,3), (5,3,3) x entrada abertura/rompimento
x (so V1) bandas de 1 e 2 desvios.
V1: 5m e 10m (10m = 2 candles de 5m agregados; a OKX nao tem 10m), 300 dias.
[15m do descritivo tambem sai de 5m agregados, 3 a 3.]
V2: 2H e 4H, ate 2000 dias.
Celulas que concorrem: V1 = 12 combinacoes x 2 tempos = 24; V2 = 6 x 2 = 12.
Descritivo: V1 no 15m (300 dias), fora da selecao.

DADOS
-----
OKX history-candles com volume, universo de 20 pares de replay_ema_ribbon.py.
Primeiros 200 candles de cada serie so aquecem indicadores.

CRITERIO DE DECISAO (pre-registrado, com correcao para a grade)
---------------------------------------------------------------
Com 36 celulas, o IC95 celula a celula quase garante um falso positivo. Por
isso, holdout temporal, decidido por variante:
1. Cada tempo grafico e dividido no ponto medio (em tempo) do historico.
2. Na PRIMEIRA metade, escolhe-se a celula (combinacao x tempo grafico) de
   maior expectancia liquida, entre as com n >= 30 nessa metade.
3. So essa celula e testada na SEGUNDA metade. A variante PASSA se a
   expectancia liquida la tiver IC95 inteiro acima de zero (bootstrap
   reamostrando dias de entrada).
A grade completa aparece no log so como descritivo, sem poder de decisao.

Uso: python replay_stoch_vwap.py --baixar   (so baixa/cacheia, nao simula)
     python replay_stoch_vwap.py            (simula e decide)
"""

import json
import os
import sys
import time
from collections import OrderedDict

import fetch_and_check as m
from replay_ema_ribbon import ic_bootstrap, CUSTO_RT, UNIVERSO

STOCHS = [(14, 3, 3), (8, 3, 3), (5, 3, 3)]
BANDAS = [1.0, 2.0]
ENTRADAS = ["abertura", "rompimento"]
ALVO_R = 2.0
MM_PERIODO = 144
AQUECIMENTO = 200
MIN_N_SELECAO = 30
MS_DIA = 86_400_000
MS_HORA = 3_600_000
CACHE_DIR = os.environ.get("STOCH_VWAP_CACHE", "cache_stoch_vwap")
# (rotulo, bar na OKX, dias, variante, concorre na selecao)
TEMPOS = [
    ("5m", "5m", 300, "V1", True),
    ("10m", "5m", 300, "V1", True),
    ("2H", "2H", 2000, "V2", True),
    ("4H", "4H", 2000, "V2", True),
    ("15m", "5m", 300, "V1", False),
]


# ---------------------------------------------------------------------------
# Dados
# ---------------------------------------------------------------------------

def baixar(inst_id, bar, dias):
    """Candles fechados [ts, o, h, l, c, vol_base], mais antigo -> mais recente."""
    fpath = os.path.join(CACHE_DIR, f"{inst_id}_{bar}_{dias}_vol.json")
    if os.path.exists(fpath):
        with open(fpath) as f:
            return json.load(f)
    limite = int(time.time() * 1000) - dias * MS_DIA
    todos, after = {}, None
    while True:
        params = {"instId": inst_id, "bar": bar, "limit": 100}
        if after:
            params["after"] = after
        for tentativa in range(5):
            try:
                raw = m.okx_get("/api/v5/market/history-candles", params)
                break
            except Exception:
                if tentativa == 4:
                    raise
                time.sleep(2 + 2 * tentativa)
        time.sleep(0.12)  # limite da OKX: 20 req / 2 s
        if not raw:
            break
        for r in raw:
            if r[8] == "1":  # so candles fechados
                todos[int(r[0])] = [int(r[0]), float(r[1]), float(r[2]), float(r[3]), float(r[4]), float(r[6])]
        mais_antigo = min(int(r[0]) for r in raw)
        if mais_antigo <= limite:
            break
        after = str(mais_antigo)
    candles = [todos[k] for k in sorted(todos) if k >= limite]
    os.makedirs(CACHE_DIR, exist_ok=True)
    with open(fpath, "w") as f:
        json.dump(candles, f)
    return candles


def agregar(c5, n):
    """n candles de 5m -> um de 5n minutos; descarta blocos incompletos."""
    ms = n * 300_000
    blocos = OrderedDict()
    for x in c5:
        blocos.setdefault(x[0] // ms, []).append(x)
    out = []
    for k, b in blocos.items():
        if len(b) != n:
            continue
        out.append([k * ms, b[0][1], max(x[2] for x in b), min(x[3] for x in b), b[-1][4], sum(x[5] for x in b)])
    return out


def serie(rotulo, bar, dias, inst):
    c = baixar(inst, bar, dias)
    return {"10m": lambda: agregar(c, 2), "15m": lambda: agregar(c, 3)}.get(rotulo, lambda: c)()


# ---------------------------------------------------------------------------
# Indicadores
# ---------------------------------------------------------------------------

def sma(v, n):
    out, soma = [None] * len(v), 0.0
    fila = []
    for i, x in enumerate(v):
        if x is None:
            fila, soma = [], 0.0
            continue
        fila.append(x)
        soma += x
        if len(fila) > n:
            soma -= fila.pop(0)
        if len(fila) == n:
            out[i] = soma / n
    return out


def estocastico(c, n, ks, nd):
    raw = []
    for i in range(len(c)):
        if i < n - 1:
            raw.append(None)
            continue
        hh = max(x[2] for x in c[i - n + 1:i + 1])
        ll = min(x[3] for x in c[i - n + 1:i + 1])
        raw.append(50.0 if hh == ll else 100 * (c[i][4] - ll) / (hh - ll))
    k = sma(raw, ks)
    return k, sma(k, nd)


def cruzamentos(k, d):
    """cz[t] = +1 cruzou pra cima, -1 pra baixo, 0 nada."""
    cz = [0] * len(k)
    for t in range(1, len(k)):
        if None in (k[t], d[t], k[t - 1], d[t - 1]):
            continue
        if k[t] > d[t] and k[t - 1] <= d[t - 1]:
            cz[t] = 1
        elif k[t] < d[t] and k[t - 1] >= d[t - 1]:
            cz[t] = -1
    return cz


def vwap_bandas(c):
    """VWAP ancorada no dia UTC e desvio padrao ponderado desde a ancora."""
    vw, sd = [], []
    dia, sv, spv, sp2v = None, 0.0, 0.0, 0.0
    for x in c:
        if x[0] // MS_DIA != dia:
            dia, sv, spv, sp2v = x[0] // MS_DIA, 0.0, 0.0, 0.0
        tp = (x[2] + x[3] + x[4]) / 3
        sv += x[5]
        spv += tp * x[5]
        sp2v += tp * tp * x[5]
        if sv <= 0:
            vw.append(None)
            sd.append(None)
            continue
        media = spv / sv
        vw.append(media)
        sd.append(max(sp2v / sv - media * media, 0.0) ** 0.5)
    return vw, sd


# ---------------------------------------------------------------------------
# Sinais
# ---------------------------------------------------------------------------

def sinais_v1(c, cz, vw, sd, banda):
    """Lista de (t_sinal, d, t_inicio_recuo)."""
    out, armado = [], None  # armado = (d, t_toque)
    for t in range(AQUECIMENTO, len(c)):
        if vw[t] is None:
            continue
        if armado and c[t][0] // MS_DIA != c[armado[1]][0] // MS_DIA:
            armado = None
        if (c[t][0] % MS_DIA) >= MS_HORA:
            if c[t][3] <= vw[t] - banda * sd[t]:
                if not armado or armado[0] != 1:
                    armado = (1, t)
            elif c[t][2] >= vw[t] + banda * sd[t]:
                if not armado or armado[0] != -1:
                    armado = (-1, t)
        if not armado:
            continue
        d, ta = armado
        if cz[t] == d:
            out.append((t, d, ta))
            armado = None
        elif (c[t][4] > vw[t]) if d == 1 else (c[t][4] < vw[t]):
            armado = None
    return out


def sinais_v2(c, cz, mm):
    out = []
    for t in range(AQUECIMENTO, len(c)):
        if cz[t] == 0 or mm[t] is None or mm[t - 1] is None:
            continue
        inclinacao = 1 if mm[t] > mm[t - 1] else -1 if mm[t] < mm[t - 1] else 0
        if cz[t] == inclinacao:
            out.append((t, cz[t], t))
    return out


def candidatos(c, cz, sinais, entrada):
    """Transforma sinais em entradas {j, d, entrada, stop}. Independente de posicao."""
    out = []
    for t, d, ini in sinais:
        if entrada == "abertura":
            j = t + 1
            if j >= len(c):
                continue
            preco = c[j][1]
        else:
            gatilho, j = (c[t][2] if d == 1 else c[t][3]), None
            for k in range(t + 1, len(c)):
                if (c[k][2] >= gatilho) if d == 1 else (c[k][3] <= gatilho):
                    j = k
                    break
                if cz[k] == -d:
                    break
            if j is None:
                continue
            preco = max(gatilho, c[j][1]) if d == 1 else min(gatilho, c[j][1])
        recuo = range(ini, j)
        stop = min(c[k][3] for k in recuo) if d == 1 else max(c[k][2] for k in recuo)
        if (preco - stop) * d <= 0:
            continue
        out.append({"j": j, "d": d, "entrada": preco, "stop": stop})
    return out


def resolver(c, cand):
    """Stop/alvo 2R; uma posicao por vez por par."""
    trades, livre_a_partir = [], 0
    for s in sorted(cand, key=lambda x: x["j"]):
        j, d, entrada, stop = s["j"], s["d"], s["entrada"], s["stop"]
        if j < livre_a_partir:
            continue
        risco = (entrada - stop) * d
        alvo = entrada + d * ALVO_R * risco
        saida = None
        for t in range(j, len(c)):
            hi, lo = c[t][2], c[t][3]
            if (lo <= stop) if d == 1 else (hi >= stop):
                saida, r = t, -1.0
                break
            if t > j and ((hi >= alvo) if d == 1 else (lo <= alvo)):
                saida, r = t, ALVO_R
                break
        if saida is None:
            break  # ainda aberto no fim do historico
        custo_r = CUSTO_RT * entrada / risco
        trades.append({"ts": c[j][0], "d": d, "r": r - custo_r, "bruto": r, "custo_r": custo_r})
        livre_a_partir = saida + 1
    return trades


# ---------------------------------------------------------------------------
# Execucao
# ---------------------------------------------------------------------------

def combos(variante):
    for st in STOCHS:
        for en in ENTRADAS:
            if variante == "V1":
                for b in BANDAS:
                    yield f"st{st[0]}-{st[1]}-{st[2]} b{b:g}sd {en}", st, b, en
            else:
                yield f"st{st[0]}-{st[1]}-{st[2]} mm144 {en}", st, None, en


def rodar_tempo(rotulo, bar, dias, variante):
    """Retorna {nome_combo: trades} para o universo inteiro e o ts do ponto medio."""
    res = {nome: [] for nome, *_ in combos(variante)}
    ts_min, ts_max = None, None
    for inst in UNIVERSO:
        c = serie(rotulo, bar, dias, inst)
        if len(c) <= AQUECIMENTO + 10:
            print(f"    {inst:<16} candles={len(c):>6} (curto demais, ignorado)")
            continue
        ts_min = c[0][0] if ts_min is None else min(ts_min, c[0][0])
        ts_max = c[-1][0] if ts_max is None else max(ts_max, c[-1][0])
        if variante == "V1":
            vw, sd = vwap_bandas(c)
        else:
            mm = sma([x[4] for x in c], MM_PERIODO)
        cache_cz = {st: cruzamentos(*estocastico(c, *st)) for st in STOCHS}
        n_par = 0
        for nome, st, b, en in combos(variante):
            cz = cache_cz[st]
            sin = sinais_v1(c, cz, vw, sd, b) if variante == "V1" else sinais_v2(c, cz, mm)
            tr = resolver(c, candidatos(c, cz, sin, en))
            for x in tr:
                x["par"] = inst
            res[nome] += tr
            n_par += len(tr)
        print(f"    {inst:<16} candles={len(c):>6} trades(todas as combinacoes)={n_par:>6}", flush=True)
    meio = (ts_min + ts_max) // 2 if ts_min is not None else 0
    return res, meio


def media(trades, chave="r"):
    return sum(x[chave] for x in trades) / len(trades) if trades else float("nan")


def linha_ic(rotulo, trades):
    if len(trades) < 3:
        return f"  {rotulo}: n={len(trades)} (insuficiente)", False
    lo, hi, dias = ic_bootstrap(trades, "r")
    acerto = sum(x["bruto"] > 0 for x in trades) / len(trades)
    return (f"  {rotulo}: n={len(trades):>6} | dias={dias:>5} | exp {media(trades):+.3f}R | "
            f"IC95 [{lo:+.3f}, {hi:+.3f}] | bruto {media(trades, 'bruto'):+.3f}R | "
            f"acerto {100*acerto:.1f}% | custo {media(trades, 'custo_r'):.3f}R"), lo > 0


def main():
    if "--baixar" in sys.argv:
        for rotulo, bar, dias, _, _ in TEMPOS:
            if rotulo in ("10m", "15m"):
                continue  # saem do cache de 5m
            for inst in UNIVERSO:
                c = baixar(inst, bar, dias)
                print(f"{bar:<4} {inst:<16} candles={len(c)}", flush=True)
        return

    celulas = []  # (variante, tempo, combo, treino, teste, todos)
    for rotulo, bar, dias, variante, concorre in TEMPOS:
        print(f"\n{'='*100}\n{rotulo} ({dias} dias max) -- {variante}"
              f"{'' if concorre else ' -- descritivo, fora da selecao'}\n{'='*100}")
        res, meio = rodar_tempo(rotulo, bar, dias, variante)
        print(f"  ponto medio do holdout: {time.strftime('%Y-%m-%d', time.gmtime(meio / 1000))}")
        print(f"  {'combinacao':<32} {'n':>6} {'exp liq':>8} {'bruto':>7} {'custo':>6} | "
              f"{'n tr':>5} {'exp tr':>7} | {'n te':>5} {'exp te':>7}")
        for nome, tr in res.items():
            treino = [x for x in tr if x["ts"] < meio]
            teste = [x for x in tr if x["ts"] >= meio]
            print(f"  {nome:<32} {len(tr):>6} {media(tr):>+8.3f} {media(tr, 'bruto'):>+7.3f} "
                  f"{media(tr, 'custo_r'):>6.3f} | {len(treino):>5} {media(treino):>+7.3f} | "
                  f"{len(teste):>5} {media(teste):>+7.3f}")
            if concorre:
                celulas.append((variante, rotulo, nome, treino, teste, tr))

    print(f"\n{'='*100}\nHOLDOUT -- DECIDE\n{'='*100}")
    decisao = {}
    for variante in ("V1", "V2"):
        elegiveis = [x for x in celulas if x[0] == variante and len(x[3]) >= MIN_N_SELECAO]
        if not elegiveis:
            print(f"  {variante}: nenhuma celula com n >= {MIN_N_SELECAO} no treino")
            decisao[variante] = False
            continue
        v, rot, nome, treino, teste, todos = max(elegiveis, key=lambda x: media(x[3]))
        print(f"\n  {variante}: selecionada no treino -> {rot} | {nome}")
        print(linha_ic("treino (1a metade, so referencia)", treino)[0])
        linha, ok = linha_ic("TESTE (2a metade, decide)       ", teste)
        print(linha)
        print(linha_ic("so compras (teste)               ", [x for x in teste if x["d"] == 1])[0])
        print(linha_ic("so vendas (teste)                ", [x for x in teste if x["d"] == -1])[0])
        decisao[variante] = ok
    print(f"\n==> DECISAO: " + ", ".join(f"{v}: {'PASSA' if ok else 'NAO PASSA'}" for v, ok in decisao.items()))


if __name__ == "__main__":
    main()
