"""
Motor comum dos estudos do acervo FMZ (strategies-for-test), 23/09/2026.

Emula o essencial do broker do PineScript no diario, para traduzir scripts do
acervo com fidelidade, e reune o que os estudos anteriores ja fixaram:

- Sinal no FECHAMENTO do candle t; ordem a mercado executa na ABERTURA de t+1
  (padrao do Pine, process_orders_on_close=false).
- strategy.entry na direcao oposta fecha tudo e abre a nova (reversao);
  na mesma direcao respeita `pyramiding` (padrao 1).
- strategy.exit (stop/limite) fica pendente e vale a partir do candle seguinte
  ao que o declarou, inclusive no candle em que a entrada executou. Dentro do
  candle, caminho OHLC (candle de alta O-L-H-C, de baixa O-H-L-C), a mesma
  heuristica de `stop_vale_no_candle_entrada` (estudo 8). Abertura alem do
  preco da ordem executa na abertura.
- Custo: CUSTO_RT = 0.18% do nocional ida+volta (replay_ema_ribbon) e mais
  SLIP_STOP = 0.05% por execucao de ordem stop (o gatilho exato e otimista,
  estudo 6).
- Funding: o historico REAL da Binance (dados_binance.baixar_funding) entra so
  no retorno absoluto; comprado paga funding positivo, vendido recebe.
- Trade aberto no fim da serie: fechado no ultimo fechamento, nao descartado.
- Excesso (teste de beta obrigatorio desde o estudo 13), DUAS linhas de base:
  * `excesso` (DECIDE): TRANSVERSAL na mesma janela -- mesmo lado, mesmas
    datas exatas de entrada e saida, em ate N_XS outros pares do universo
    sorteados entre os que tem candle nas duas datas. Remove a exposicao ao
    mercado no periodo do trade.
  * `excesso_par` (descritivo): a do estudo 6 -- mesmo par, mesmo lado, mesma
    duracao, entrada em candle sorteado de toda a serie.
  Por que a troca (23/09/2026, fmz_teste_passeio.py, ANTES de rodar dado real):
  num passeio aleatorio sem drift (120 series, 480 passos intra-candle) o bruto
  das 12 estrategias sorteadas fica em zero, mas `excesso_par` sai
  significativo em 5: +1.7% numa de contra-tendencia, -0.5 a -1.2% em
  seguidores de tendencia. A linha de base de mesmo par usa a deriva REALIZADA
  da serie inteira (inclusive o futuro do trade), e a direcao da estrategia se
  correlaciona com ela. A transversal nao tem esse vazamento: outros pares,
  mesma janela. Excesso = bruto - slippage de stop - media da linha de base;
  o custo a mercado se cancela dos dois lados.
- Bootstrap por bloco de SEMANA de entrada (protocolo desde o estudo 13),
  medias ponderadas pela quantidade do lote (saidas parciais do Pine).
"""

import bisect
import math
import os
import random
from collections import defaultdict

import dados_binance as DB
from replay_ema_ribbon import CUSTO_RT, UNIVERSO

MS_DIA = 86_400_000
MS_SEMANA = 7 * MS_DIA
SLIP_STOP = 0.05       # % por execucao de ordem stop
N_BASE = 200
N_XS = 30
N_RESAMPLES = 5000
SEED = 42
DIAS = 3000

AQUI = os.path.dirname(os.path.abspath(__file__))


# ---------------------------------------------------------------------------
# Universos
# ---------------------------------------------------------------------------

def _lista(nome):
    with open(os.path.join(AQUI, nome)) as f:
        return f.read().split()


def universo(nome):
    """A = os 20 de sempre (desenvolvimento); D e E = Binance (decidem, com
    Bonferroni, ver docstring de cada estudo)."""
    if nome == "A":
        return [DB.simbolo(i) for i in UNIVERSO]
    if nome == "D":
        return _lista("universo_d.txt")
    if nome == "E":
        return _lista("universo_e.txt")
    if nome == "DE":
        return _lista("universo_d.txt") + _lista("universo_e.txt")
    raise ValueError(nome)


def candles(sym):
    return DB.baixar(sym, "1Dutc", DIAS)


class Funding:
    def __init__(self, sym):
        try:
            serie = DB.baixar_funding(sym, DIAS)
        except Exception:
            serie = []
        self.ts = [x[0] for x in serie]
        self.acum = [0.0]
        for x in serie:
            self.acum.append(self.acum[-1] + x[1])

    def soma(self, t0, t1):
        """Soma das taxas com fundingTime em [t0, t1)."""
        if not self.ts or t1 <= t0:
            return 0.0
        a = bisect.bisect_left(self.ts, t0)
        b = bisect.bisect_left(self.ts, t1)
        return self.acum[b] - self.acum[a]


# ---------------------------------------------------------------------------
# Indicadores no padrao do Pine (listas, None = na)
# ---------------------------------------------------------------------------

def sma(v, n):
    out, s, q = [None] * len(v), 0.0, []
    for i, x in enumerate(v):
        if x is None:
            q, s = [], 0.0
            continue
        q.append(x)
        s += x
        if len(q) > n:
            s -= q.pop(0)
        if len(q) == n:
            out[i] = s / n
    return out


def ema(v, n):
    """ta.ema: alpha = 2/(n+1), semente = primeiro valor (pseudo-codigo do manual)."""
    a, out, prev = 2 / (n + 1), [None] * len(v), None
    for i, x in enumerate(v):
        if x is None:
            continue
        prev = x if prev is None else a * x + (1 - a) * prev
        out[i] = prev
    return out


def rma(v, n):
    """ta.rma: semente = sma dos n primeiros."""
    out, prev, buf = [None] * len(v), None, []
    for i, x in enumerate(v):
        if x is None:
            continue
        if prev is None:
            buf.append(x)
            if len(buf) == n:
                prev = sum(buf) / n
                out[i] = prev
        else:
            prev = (x + (n - 1) * prev) / n
            out[i] = prev
    return out


def wma(v, n):
    out, pesos = [None] * len(v), n * (n + 1) / 2
    for i in range(n - 1, len(v)):
        jan = v[i - n + 1:i + 1]
        if None in jan:
            continue
        out[i] = sum(x * (k + 1) for k, x in enumerate(jan)) / pesos
    return out


def hma(v, n):
    a, b = wma(v, n // 2), wma(v, n)
    d = [None if (x is None or y is None) else 2 * x - y for x, y in zip(a, b)]
    return wma(d, int(round(math.sqrt(n))))


def stdev(v, n):
    """ta.stdev: desvio populacional."""
    out = [None] * len(v)
    for i in range(n - 1, len(v)):
        jan = v[i - n + 1:i + 1]
        if None in jan:
            continue
        m = sum(jan) / n
        out[i] = math.sqrt(sum((x - m) ** 2 for x in jan) / n)
    return out


def rsi(v, n):
    up = [None] + [max(v[i] - v[i - 1], 0.0) for i in range(1, len(v))]
    dn = [None] + [max(v[i - 1] - v[i], 0.0) for i in range(1, len(v))]
    ru, rd = rma(up, n), rma(dn, n)
    out = [None] * len(v)
    for i in range(len(v)):
        if ru[i] is None or rd[i] is None:
            continue
        out[i] = 100.0 if rd[i] == 0 else (0.0 if ru[i] == 0 else 100 - 100 / (1 + ru[i] / rd[i]))
    return out


def true_range(c):
    tr = [c[0][2] - c[0][3]]
    for i in range(1, len(c)):
        h, l, pc = c[i][2], c[i][3], c[i - 1][4]
        tr.append(max(h - l, abs(h - pc), abs(l - pc)))
    return tr


def atr(c, n):
    return rma(true_range(c), n)


def cci(v, n):
    m = sma(v, n)
    out = [None] * len(v)
    for i in range(n - 1, len(v)):
        jan = v[i - n + 1:i + 1]
        dev = sum(abs(x - m[i]) for x in jan) / n
        out[i] = 0.0 if dev == 0 else (v[i] - m[i]) / (0.015 * dev)
    return out


def macd(v, f=12, s=26, sig=9):
    ef, es = ema(v, f), ema(v, s)
    linha = [None if (a is None or b is None) else a - b for a, b in zip(ef, es)]
    sinal = ema(linha, sig)
    hist = [None if (a is None or b is None) else a - b for a, b in zip(linha, sinal)]
    return linha, sinal, hist


def highest(v, n):
    return [None if i < n - 1 else max(v[i - n + 1:i + 1]) for i in range(len(v))]


def lowest(v, n):
    return [None if i < n - 1 else min(v[i - n + 1:i + 1]) for i in range(len(v))]


def cruza_acima(a, b, t):
    """ta.crossover(a, b) no candle t; b pode ser numero."""
    a0, a1 = a[t], a[t - 1]
    b0, b1 = (b[t], b[t - 1]) if isinstance(b, list) else (b, b)
    if None in (a0, a1, b0, b1):
        return False
    return a0 > b0 and a1 <= b1


def cruza_abaixo(a, b, t):
    a0, a1 = a[t], a[t - 1]
    b0, b1 = (b[t], b[t - 1]) if isinstance(b, list) else (b, b)
    if None in (a0, a1, b0, b1):
        return False
    return a0 < b0 and a1 >= b1


def cruza(a, b, t):
    return cruza_acima(a, b, t) or cruza_abaixo(a, b, t)


# ---------------------------------------------------------------------------
# Broker no estilo Pine
# ---------------------------------------------------------------------------

class Corretora:
    def __init__(self, c, pyramiding=1):
        self.c = c
        self.pyr = pyramiding
        self.lotes = []          # {id, d, j, px, q, stop_in}
        self.mercado = []        # ordens a mercado para a proxima abertura
        self.saidas = {}         # id da entrada -> {"limit": x, "stop": y}
        self.trades = []
        self._fechados = set()

    # --- estado visto pelo script no fechamento ---
    @property
    def pos(self):
        return sum(l["d"] * l["q"] for l in self.lotes)

    @property
    def preco_medio(self):
        q = sum(l["q"] for l in self.lotes)
        return sum(l["px"] * l["q"] for l in self.lotes) / q if q else None

    def abertos(self):
        return len(self.lotes)

    # --- ordens emitidas pelo script ---
    def entry(self, id_, d, q=1.0):
        self.mercado.append(("entry", id_, d, q))

    def close(self, id_, pct=100.0):
        self.mercado.append(("close", id_, pct))

    def close_all(self):
        self.mercado.append(("close_all",))

    def exit(self, id_, limit=None, stop=None):
        """Cada strategy.exit do Pine e uma ordem propria; alvo e stop declarados
        em chamadas separadas se somam. Vale ate o lote fechar."""
        s = self.saidas.setdefault(id_, {"limit": None, "stop": None})
        if limit is not None:
            s["limit"] = limit
        if stop is not None:
            s["stop"] = stop

    # --- execucao ---
    def _fecha(self, lote, px, k, q, n_stop_saida):
        self.trades.append({"d": lote["d"], "j": lote["j"], "k": k, "px_in": lote["px"], "px_out": px,
                            "q": q, "n_stop": lote["stop_in"] + n_stop_saida,
                            "intra": n_stop_saida >= 0 and px != self.c[k][1]})
        lote["q"] -= q
        if lote["q"] <= 1e-12:
            self._fechados.add(lote["id"])

    def _limpa(self):
        self.lotes = [l for l in self.lotes if l["q"] > 1e-12]
        ids = {l["id"] for l in self.lotes}
        for i in self._fechados - ids:
            self.saidas.pop(i, None)
        self._fechados = set()

    def abrir_lote(self, id_, d, px, t, q=1.0, via_stop=False):
        self.lotes.append({"id": id_, "d": d, "j": t, "px": px, "q": q, "stop_in": 1 if via_stop else 0})

    def processa(self, t):
        """Abertura e intra-candle de t."""
        o = self.c[t][1]
        for ordem in self.mercado:
            if ordem[0] == "entry":
                _, id_, d, q = ordem
                if any(l["d"] == -d for l in self.lotes):
                    for l in self.lotes:
                        self._fecha(l, o, t, l["q"], 0)
                    self._limpa()
                if sum(1 for l in self.lotes if l["d"] == d) < self.pyr and \
                        not (self.pyr == 1 and any(l["id"] == id_ for l in self.lotes)):
                    self.abrir_lote(id_, d, o, t, q)
            elif ordem[0] == "close":
                _, id_, pct = ordem
                for l in self.lotes:
                    if l["id"] == id_:
                        self._fecha(l, o, t, l["q"] * pct / 100, 0)
                self._limpa()
            else:
                for l in self.lotes:
                    self._fecha(l, o, t, l["q"], 0)
                self._limpa()
        self.mercado = []
        self._saidas_intra(t)

    def _saidas_intra(self, t):
        _, o, h, lo, cl = self.c[t][:5]
        caminho = [o, lo, h, cl] if cl >= o else [o, h, lo, cl]
        for l in list(self.lotes):
            s = self.saidas.get(l["id"])
            if not s:
                continue
            px, via_stop = _primeiro_toque(caminho, l["d"], s.get("stop"), s.get("limit"))
            if px is not None:
                self._fecha(l, px, t, l["q"], 1 if via_stop else 0)
        self._limpa()

    def encerra(self):
        t = len(self.c) - 1
        for l in self.lotes:
            self.trades.append({"d": l["d"], "j": l["j"], "k": t, "px_in": l["px"], "px_out": self.c[t][4],
                                "q": l["q"], "n_stop": l["stop_in"], "intra": True})
        self.lotes = []


def _primeiro_toque(caminho, d, stop, limite):
    """Primeiro preco de saida ao longo do caminho O-(L|H)-(H|L)-C.
    Comprado: stop abaixo, limite acima. Vendido: o espelho."""
    o = caminho[0]
    if stop is not None and (o <= stop if d == 1 else o >= stop):
        return o, True
    if limite is not None and (o >= limite if d == 1 else o <= limite):
        return o, False
    for a, b in zip(caminho, caminho[1:]):
        lo, hi = min(a, b), max(a, b)
        bate_stop = stop is not None and lo <= stop <= hi
        bate_lim = limite is not None and lo <= limite <= hi
        if bate_stop and bate_lim:
            # os dois no mesmo segmento: o mais perto do ponto de partida vem primeiro
            return (stop, True) if abs(stop - a) <= abs(limite - a) else (limite, False)
        if bate_stop:
            return stop, True
        if bate_lim:
            return limite, False
    return None, False


def rodar_script(c, logica, inicio, pyramiding=1):
    """Roda `logica(ctx, br, t)` no fechamento de cada candle t >= inicio."""
    br = Corretora(c, pyramiding)
    for t in range(inicio, len(c)):
        if t > inicio:
            br.processa(t)
        logica(br, t)
    br.encerra()
    return br.trades


# ---------------------------------------------------------------------------
# Medidas por trade
# ---------------------------------------------------------------------------

def medir(c, trades, funding, rng, inicio, sym=None, n_base=N_BASE):
    """Acrescenta a cada trade: liq (% com custo e slippage de stop), abs
    (liq menos funding real), excesso_par (linha de base de mesmo par), a
    janela exata (ts_in, ts_out, pontas) para o excesso transversal, dur, ts."""
    out = []
    for x in trades:
        d, j, k = x["d"], x["j"], x["k"]
        bruto = 100 * d * (x["px_out"] / x["px_in"] - 1)
        slip = SLIP_STOP * x["n_stop"]
        liq = bruto - 100 * CUSTO_RT - slip
        dur = k - j
        t_fim = c[k][0] + (MS_DIA // 2 if x["intra"] else 0)
        fund = 100 * funding.soma(c[j][0], t_fim) if funding else 0.0
        ultimo = len(c) - 1 - max(dur, 0) - (1 if dur == 0 else 0)
        if ultimo <= inicio:
            continue
        base = 0.0
        for _ in range(n_base):
            s = rng.randint(inicio, ultimo)
            saida = c[s + dur][1] if dur > 0 else c[s][4]
            base += 100 * d * (saida / c[s][1] - 1)
        # saida a mercado = abertura de k; saida intra-candle = fechamento de k
        out.append({**x, "bruto": bruto, "liq": liq, "abs": liq - d * fund,
                    "excesso_par": bruto - slip - base / n_base, "dur": dur, "ts": c[j][0],
                    "sym": sym, "ts_out": c[k][0], "ponta_out": 4 if x["intra"] else 1, "slip": slip})
    return out


class Precos:
    """Aberturas e fechamentos de todos os pares do universo, por timestamp,
    para a linha de base transversal."""
    def __init__(self):
        self.p = {}                       # sym -> {ts: candle}
        self.por_ts = defaultdict(list)   # ts -> [sym]

    def add(self, sym, c):
        self.p[sym] = {k[0]: k for k in c}
        for k in c:
            self.por_ts[k[0]].append(sym)

    def excesso(self, trades, rng, n=N_XS):
        """Preenche `excesso` (transversal); trade sem nenhum par comparavel na
        janela fica com None e sai das contas de excesso."""
        for x in trades:
            cand = [s for s in self.por_ts.get(x["ts"], ()) if s != x["sym"] and x["ts_out"] in self.p[s]]
            if not cand:
                x["excesso"] = None
                continue
            if len(cand) > n:
                cand = rng.sample(cand, n)
            base = 0.0
            for s in cand:
                ci, co = self.p[s][x["ts"]], self.p[s][x["ts_out"]]
                base += 100 * x["d"] * (co[x["ponta_out"]] / ci[1] - 1)
            x["excesso"] = x["bruto"] - x["slip"] - base / len(cand)


# ---------------------------------------------------------------------------
# Estatistica
# ---------------------------------------------------------------------------

def bootstrap_semana(trades, chave, conf=0.95, peso="q"):
    """Media ponderada e IC por reamostragem de semanas de entrada."""
    g = defaultdict(lambda: [0.0, 0.0])
    for x in trades:
        if x.get(chave) is None:
            continue
        w = x.get(peso, 1.0) if peso else 1.0
        s = g[x["ts"] // MS_SEMANA]
        s[0] += w * x[chave]
        s[1] += w
    grupos = list(g.values())
    if not grupos:
        return float("nan"), float("nan"), float("nan"), 0
    tot_w = sum(b for _, b in grupos)
    media = sum(a for a, _ in grupos) / tot_w
    rng = random.Random(SEED)
    medias, m = [], len(grupos)
    for _ in range(N_RESAMPLES):
        sa = sb = 0.0
        for _ in range(m):
            a, b = grupos[rng.randrange(m)]
            sa += a
            sb += b
        medias.append(sa / sb if sb else 0.0)
    medias.sort()
    alfa = (1 - conf) / 2
    lo = medias[int(alfa * N_RESAMPLES)]
    hi = medias[min(N_RESAMPLES - 1, int((1 - alfa) * N_RESAMPLES))]
    return media, lo, hi, m


def linha(rotulo, trades, chave, conf=0.95):
    trades = [x for x in trades if x.get(chave) is not None]
    if len(trades) < 3:
        return f"  {rotulo:<34} n={len(trades)} (insuficiente)", float("nan"), float("nan")
    m, lo, hi, sem = bootstrap_semana(trades, chave, conf)
    return (f"  {rotulo:<34} n={len(trades):>6} sem={sem:>4} media {m:+7.3f}% "
            f"IC{int(round(conf*1000))/10:g} [{lo:+7.3f}, {hi:+7.3f}]"), m, lo
