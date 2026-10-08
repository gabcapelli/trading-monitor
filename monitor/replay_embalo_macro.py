"""
Estudo 56 -- embalo depois do dado macro (CPI, payroll, FOMC) em BTC e ETH.
PRE-REGISTRADO em 08/10/2026, antes de ver qualquer resultado de preco.

HIPOTESE
--------
A reacao dos primeiros 15 minutos depois de um dado macro grande continua nas
horas seguintes (o mercado leva tempo para digerir e reposicionar). O estudo 32
testou a vespera do FOMC; aqui e o DEPOIS do anuncio, nos tres eventos de maior
impacto. Setup ativo, de horas, movimento grande por trade.

EVENTOS (2020-01 a 2026-09)
---------------------------
- CPI e payroll (Employment Situation): 8:30 de Nova York. Datas dos enderecos
  de arquivo do BLS (news.release/archives/cpi_MMDDYYYY.htm e empsit_...) no
  indice do Wayback Machine (o bls.gov bloqueia acesso automatico).
  Limpeza fixada antes: so dias uteis; quando um mes tem mais de uma data
  candidata, fica a de maior volume do BTC no minuto das 8:30 (regra cega
  para direcao).
- FOMC: as 53 reunioes regulares do estudo 32, comunicado as 14:00 de NY.
- Dia com dois eventos (ex.: CPI e FOMC): cada um conta no seu horario.

SETUP (BTCUSDT e ETHUSDT perpetuos, candles de 1 minuto)
--------------------------------------------------------
- T0 = minuto do anuncio. Janela = 15 minutos [T0, T0+15).
- d = sinal(fechamento do minuto T0+14 / abertura de T0 - 1). Zero: sem trade.
- Entrada na abertura do minuto T0+16 (1 minuto para ler e executar).
- Stop no extremo oposto da janela (minima se d=+1), com distancia minima de
  0.3% da entrada. 1R = essa distancia. Alvo 2R. Stop e alvo no mesmo minuto =
  stop. Sem toque: sai na abertura de T0+16+240 (4h).
- Custo 0.18% ida e volta (padrao do projeto) + funding real.
- Resultado do evento = media do R liquido de BTC e ETH (um numero por evento).

PLACEBO
-------
O mesmo setup no mesmo horario do relogio nos ate 10 dias uteis anteriores sem
nenhum evento (CPI, payroll ou FOMC). Excesso = R do evento - media do placebo.

CRITERIO (fixado antes; todos juntos)
-------------------------------------
1. n >= 150 eventos.
2. R liquido medio com IC95 inteiro > 0 (bootstrap por evento).
3. Excesso com IC95 inteiro > 0.
4. R liquido medio > 0 nas duas metades do periodo.
Poder declarado: com ~220 eventos e desvio de ~1.2R, so um efeito acima de
~0.16R por evento sai do zero.
Descritivo, sem poder de decisao: por tipo de evento, por moeda, compras e vendas, por ano.

Uso (de dentro de monitor/):
    python replay_embalo_macro.py
"""

import json
import os
import random
import re
import sys
import time
import urllib.request
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import replay_deslistagem as D
from replay_pre_fomc import FOMC

NY = ZoneInfo("America/New_York")
M = 60_000
DIA = 86_400_000
JANELA, ATRASO, SAIDA = 15, 16, 240
MIN_STOP, ALVO_R, CUSTO = 0.003, 2.0, 0.18
N_PLACEBO, N_BOOT, SEED = 10, 5000, 42
INICIO, FIM = "2020-01-01", "2026-10-01"
SYMS = ("BTCUSDT", "ETHUSDT")
AQUI = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(AQUI, "cache_1m")


def _get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read().decode()


def datas_bls(serie):
    fp = os.path.join(DIR, f"datas_{serie}.json")
    if os.path.exists(fp):
        return json.load(open(fp))
    txt = _get(f"http://web.archive.org/cdx/search/cdx?url=bls.gov/news.release/archives/{serie}_*"
               "&fl=original&collapse=urlkey&limit=5000")
    ds = sorted({f"{a[4:]}-{a[:2]}-{a[2:4]}" for a in re.findall(rf"{serie}_(\d{{8}})\.htm", txt)})
    ds = [d for d in ds if INICIO <= d < FIM]
    os.makedirs(DIR, exist_ok=True)
    json.dump(ds, open(fp, "w"))
    return ds


def t_ny(dia, h, m):
    y, mo, d = map(int, dia.split("-"))
    return int(datetime(y, mo, d, h, m, tzinfo=NY).timestamp() * 1000)


def mes_de(ts):
    return datetime.fromtimestamp(ts / 1000, timezone.utc).strftime("%Y-%m")


def klines_mes(sym, mes):
    """{ts: [o, h, l, c, volume]} de 1 minuto do perpetuo."""
    fp = os.path.join(DIR, f"{sym}_{mes}.json")
    if os.path.exists(fp):
        return {int(k): v for k, v in json.load(open(fp)).items()}
    raw = D._get(f"{D.VISION}/futures/um/monthly/klines/{sym}/1m/{sym}-1m-{mes}.zip")
    out = {D._ms(r[0]): [float(r[1]), float(r[2]), float(r[3]), float(r[4]), float(r[5])]
           for r in (D._csv_zip(raw) if raw else [])}
    tmp = fp + ".tmp"
    json.dump(out, open(tmp, "w"))
    os.replace(tmp, fp)
    return out


class Serie:
    def __init__(self, sym):
        self.sym, self.c = sym, {}

    def get(self, ts):
        m = mes_de(ts)
        if m not in self.c:
            self.c[m] = klines_mes(self.sym, m)
        return self.c[m].get(ts)


def limpar(datas, btc):
    """So dias uteis; um por mes, o de maior volume no minuto das 8:30 NY."""
    por_mes = defaultdict(list)
    for d in datas:
        if datetime.strptime(d, "%Y-%m-%d").weekday() < 5:
            por_mes[d[:7]].append(d)
    out = []
    for m, ds in sorted(por_mes.items()):
        if len(ds) == 1:
            out.append(ds[0])
            continue
        vol = lambda d: (btc.get(t_ny(d, 8, 30)) or [0] * 5)[4]
        out.append(max(ds, key=vol))
    return out


def simular(s, t0):
    """R liquido do setup no minuto t0 (anuncio). None se faltar dado."""
    jan = [s.get(t0 + k * M) for k in range(JANELA)]
    if any(x is None for x in jan):
        return None
    d = (jan[-1][3] > jan[0][0]) - (jan[-1][3] < jan[0][0])
    if d == 0:
        return None
    ent_t = t0 + ATRASO * M
    b = s.get(ent_t)
    if b is None:
        return None
    e = b[0]
    ext = min(x[2] for x in jan) if d > 0 else max(x[1] for x in jan)
    risco = max(d * (e - ext) / e, MIN_STOP)
    stop, alvo = e * (1 - d * risco), e * (1 + d * ALVO_R * risco)
    bruto, sai = None, ent_t + SAIDA * M
    for k in range(SAIDA):
        x = s.get(ent_t + k * M)
        if x is None:
            return None
        if (x[2] <= stop) if d > 0 else (x[1] >= stop):
            bruto, sai = -risco * 100, ent_t + (k + 1) * M
            break
        if (x[1] >= alvo) if d > 0 else (x[2] <= alvo):
            bruto, sai = ALVO_R * risco * 100, ent_t + (k + 1) * M
            break
    if bruto is None:
        x = s.get(sai)
        if x is None:
            return None
        bruto = d * 100 * (x[0] / e - 1)
    f = -d * 100 * sum(r for ts, r in s.fund if ent_t <= ts < sai)
    return {"d": d, "r": (bruto - CUSTO + f) / (risco * 100), "risco": risco}


def boot(v, conf=0.95):
    v = [x for x in v if x is not None]
    if len(v) < 2:
        return None
    rng = random.Random(SEED)
    ms = sorted(sum(rng.choice(v) for _ in v) / len(v) for _ in range(N_BOOT))
    a = (1 - conf) / 2
    return sum(v) / len(v), ms[int(a * N_BOOT)], ms[int((1 - a) * N_BOOT) - 1], len(v)


def fmt(b):
    return "n/a" if b is None else f"{b[0]:+.3f}R  IC95 [{b[1]:+.3f}, {b[2]:+.3f}]  n={b[3]}"


def main(argv):
    t0 = time.time()
    os.makedirs(DIR, exist_ok=True)
    meses = sorted({f"{y}-{m:02d}" for y in range(2019, 2027) for m in range(1, 13) if "2019-12" <= f"{y}-{m:02d}" <= "2026-09"})
    with ThreadPoolExecutor(8) as ex:
        list(ex.map(lambda a: klines_mes(*a), [(s, m) for s in SYMS for m in meses]))
    series = {s: Serie(s) for s in SYMS}
    for s in SYMS:
        D.funding(s, int(datetime(2019, 12, 1, tzinfo=timezone.utc).timestamp() * 1000),
                  int(datetime(2026, 10, 1, tzinfo=timezone.utc).timestamp() * 1000))
        fund = []
        for m in meses:
            fp = os.path.join(D.DIR_VISION, f"funding_{s}_{m}.json")
            if os.path.exists(fp):
                fund += [tuple(x) for x in json.load(open(fp))]
        series[s].fund = sorted(fund)
    print(f"dados ok [{time.time()-t0:.0f}s]", flush=True)

    btc = series["BTCUSDT"]
    cpi, nfp = limpar(datas_bls("cpi"), btc), limpar(datas_bls("empsit"), btc)
    evs = [("CPI", d, t_ny(d, 8, 30)) for d in cpi] + [("payroll", d, t_ny(d, 8, 30)) for d in nfp] + \
          [("FOMC", d, t_ny(d, 14, 0)) for d in FOMC if INICIO <= d < FIM]
    evs.sort(key=lambda x: x[2])
    dias_ev = {d for _, d, _ in evs}
    print(f"eventos: CPI {len(cpi)} | payroll {len(nfp)} | FOMC {sum(1 for e in evs if e[0]=='FOMC')}")

    linhas = []
    for tipo, dia, t in evs:
        rs = {s: simular(series[s], t) for s in SYMS}
        if any(v is None for v in rs.values()):
            continue
        r = sum(v["r"] for v in rs.values()) / len(SYMS)
        hh, mm = (8, 30) if tipo != "FOMC" else (14, 0)
        pl, dd = [], datetime.strptime(dia, "%Y-%m-%d")
        while len(pl) < N_PLACEBO and (datetime.strptime(dia, "%Y-%m-%d") - dd).days < 30:
            dd -= timedelta(days=1)
            ds = dd.strftime("%Y-%m-%d")
            if dd.weekday() >= 5 or ds in dias_ev:
                continue
            ps = [simular(series[s], t_ny(ds, hh, mm)) for s in SYMS]
            ps = [p["r"] for p in ps if p is not None]
            if ps:
                pl.append(sum(ps) / len(ps))
        linhas.append({"tipo": tipo, "dia": dia, "t": t, "r": r, "exc": r - sum(pl) / len(pl) if pl else None,
                       "btc": rs["BTCUSDT"]["r"], "eth": rs["ETHUSDT"]["r"], "d": rs["BTCUSDT"]["d"],
                       "risco": rs["BTCUSDT"]["risco"]})

    mm = lambda v: sum(v) / len(v) if v else float("nan")
    meio = sorted(x["t"] for x in linhas)[len(linhas) // 2]
    b, ex = boot([x["r"] for x in linhas]), boot([x["exc"] for x in linhas])
    h1, h2 = mm([x["r"] for x in linhas if x["t"] < meio]), mm([x["r"] for x in linhas if x["t"] >= meio])
    print("\n" + "=" * 90 + "\nEMBALO DEPOIS DO DADO MACRO (media BTC+ETH por evento)\n" + "=" * 90)
    print(f"  R liquido  {fmt(b)}")
    print(f"  excesso    {fmt(ex)}")
    print(f"  metades: 1a {h1:+.3f}R | 2a {h2:+.3f}R")
    print(f"  risco medio BTC {mm([x['risco'] for x in linhas])*100:.2f}% | acerto {mm([x['r'] > 0 for x in linhas])*100:.1f}%")
    for tp in ("CPI", "payroll", "FOMC"):
        sub = [x for x in linhas if x["tipo"] == tp]
        print(f"  {tp:<8} R {fmt(boot([x['r'] for x in sub]))} | excesso {fmt(boot([x['exc'] for x in sub]))}")
    print(f"  so BTC   {fmt(boot([x['btc'] for x in linhas]))}")
    print(f"  so ETH   {fmt(boot([x['eth'] for x in linhas]))}")
    for d, nm in ((1, "compras"), (-1, "vendas")):
        print(f"  {nm:<8} {fmt(boot([x['r'] for x in linhas if x['d'] == d]))}")
    pa = defaultdict(list)
    for x in linhas:
        pa[x["dia"][:4]].append(x["r"])
    print("  por ano: " + " | ".join(f"{a} {mm(v):+.2f} ({len(v)})" for a, v in sorted(pa.items())))
    ok = b and ex and b[3] >= 150 and b[1] > 0 and ex[1] > 0 and h1 > 0 and h2 > 0
    print(f"\n  DECISAO: {'PASSA' if ok else 'NAO PASSA'}  [{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main(sys.argv[1:])
