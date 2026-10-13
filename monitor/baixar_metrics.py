"""
Baixa da Binance Vision o historico de 'metrics' dos perpetuos USDT-M (5 min, desde
2020-09): open interest, proporcao de comprados/vendidos dos top traders (contas e
posicoes), de todas as contas e do taker. Arquivo so diario (~12 KB).

Escopo: os dias em que o simbolo esta entre os 50 de maior volume (mesmo ranking do
estudo 57), mais os 30 dias anteriores a cada dia (historico para z-score).

Cache: cache_metrics/{SYM}_{AAAA-MM}.json = {ts_hora: [oi_usd, top_contas,
top_posicoes, contas, taker]}, com o ultimo registro de 5 min de cada hora (estado
no fechamento da hora). Retoma de onde parou: mes ja gravado nao e baixado de novo.

Uso (de dentro de monitor/):
    python baixar_metrics.py
"""

import json
import os
import sys
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

import replay_continuacao_top20 as T
import replay_deslistagem as D
import replay_fluxo_spot_perp as F
import replay_sfp as S

DIA, H = S.DIA, S.H
DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cache_metrics")
INICIO_METRICS = int(datetime(2020, 9, 1, tzinfo=timezone.utc).timestamp() * 1000)


def _f(x):
    try:
        return float(x)
    except ValueError:
        return None


def dia(sym, d):
    data = datetime.fromtimestamp(d / 1000, timezone.utc).strftime("%Y-%m-%d")
    raw = D._get(f"{D.VISION}/futures/um/daily/metrics/{sym}/{sym}-metrics-{data}.zip")
    if not raw:
        return {}
    out = {}
    for r in D._csv_zip(raw):
        ts = int(datetime.strptime(r[0], "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone.utc).timestamp() * 1000)
        out[ts // H * H] = [_f(r[3]), _f(r[4]), _f(r[5]), _f(r[6]), _f(r[7])]   # ultimo da hora vence
    return out


def caminho(sym, mes):
    return os.path.join(DIR, f"{sym}_{mes}.json")


def carregar(sym, meses):
    out = {}
    for m in meses:
        fp = caminho(sym, m)
        if os.path.exists(fp):
            out.update({int(k): v for k, v in json.load(open(fp)).items()})
    return out


def main(argv):
    t0 = time.time()
    os.makedirs(DIR, exist_ok=True)
    syms = T.simbolos()
    with ThreadPoolExecutor(16) as ex:
        vols = dict(zip(syms, ex.map(T.diario, syms)))
    vols = {s: v for s, v in vols.items() if v}
    T.TOP = S.TOP
    rk = T.ranking(vols)
    precisa = defaultdict(set)
    for d, ss in rk.items():
        if not (max(F.INICIO, INICIO_METRICS) <= d < F.FIM):
            continue
        for s in ss:
            for k in range(31):
                if d - k * DIA >= INICIO_METRICS:
                    precisa[s].add(d - k * DIA)
    tarefas = defaultdict(list)                           # (sym, mes) -> dias
    for s, dias in precisa.items():
        for d in dias:
            tarefas[(s, datetime.fromtimestamp(d / 1000, timezone.utc).strftime("%Y-%m"))].append(d)
    falta = {k: v for k, v in tarefas.items() if not os.path.exists(caminho(*k))}
    total = sum(len(v) for v in falta.values())
    print(f"{len(precisa)} simbolos, {sum(len(v) for v in tarefas.values())} dias; faltam {total} dias "
          f"em {len(falta)} meses", flush=True)
    feitos = 0
    with ThreadPoolExecutor(16) as ex:
        for n, ((s, mes), dias) in enumerate(sorted(falta.items())):
            out = {}
            for x in ex.map(lambda d: dia(s, d), sorted(dias)):
                out.update(x)
            tmp = caminho(s, mes) + ".tmp"
            json.dump(out, open(tmp, "w"))
            os.replace(tmp, caminho(s, mes))
            feitos += len(dias)
            if n % 50 == 0:
                print(f"  {feitos}/{total} dias ({time.time()-t0:.0f}s)", flush=True)
    print(f"pronto em {time.time()-t0:.0f}s")


if __name__ == "__main__":
    main(sys.argv[1:])
