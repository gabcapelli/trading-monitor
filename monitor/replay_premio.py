"""
Estudo 36 -- premio extremo do perpetuo sobre o indice, horario, PRE-REGISTRADO
em 04/10/2026, antes de calcular qualquer retorno.

HIPOTESE E SOBREPOSICAO
-----------------------
Quando o perpetuo negocia muito acima do indice spot (premio extremo), ha
comprados alavancados pagando caro para estar dentro; o funding forca a
convergencia e o excesso de alavancagem tende a se desfazer -> o perpetuo cai
nas horas seguintes (espelho para premio muito negativo).
Sobreposicao assumida com o estudo 27: o premio e o que gera o funding, e la o
funding extremo sozinho deu excesso zero. A diferenca testada aqui e a ESCALA:
sinal horario (o 27 usou a soma diaria de funding) e saida em horas.

DADOS
-----
data.binance.vision, futures/um/monthly/premiumIndexKlines/SYM/1h (desde
2020; valor = (perpetuo - indice) / indice). Precos: candles de 1h da Binance
(dados_binance, cache dos estudos 23/24). Funding real.

REGRA (por par, horario)
------------------------
- Premio da hora t = fechamento do premiumIndexKline de t.
- VENDA: premio >= p99 das 720 horas anteriores (>= 500 validas) E >= +0.3%.
- COMPRA: premio <= p1 das 720 horas anteriores E <= -0.3%.
  (+-0.3% = ~30x o premio que zera o funding padrao; p99/p1 = extremo para o
  proprio par.)
- Entra na abertura de t+1, sai na abertura de t+9 (8 horas = um periodo de
  funding). Sem stop. Uma posicao por par; sinal com trade aberto e ignorado.

MEDIDAS (% por trade)
---------------------
- `abs` (decide): bruto - 0.18% - funding pago no periodo.
- `excesso` (decide): bruto - d x retorno do BTC nas mesmas horas (tira o
  mercado; para o proprio BTC fica None).
- Bootstrap por semana de entrada.

CRITERIO
--------
A (20 majors): descritivo. DE (368 perps): PASSA se `abs` E `excesso` com
IC95 > 0. Menos de 200 trades no DE: sem amostra.

DESCRITIVOS
-----------
Por lado; saida em 1h e em 24h; so o premio extremo sem o piso absoluto.

Uso (de dentro de monitor/):
    python replay_premio.py --contar
    python replay_premio.py
"""

import io
import json
import os
import re
import sys
import time
import urllib.request
import zipfile
from concurrent.futures import ThreadPoolExecutor

import dados_binance as DB
import fmz_motor as M
from replay_ema_ribbon import CUSTO_RT

H = 3_600_000
JANELA, MIN_VALIDAS = 720, 500
P_ALTO, P_BAIXO = 0.99, 0.01
PISO = 0.003
HOLD = 8
MIN_DECIDIR = 200
AQUI = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(AQUI, "cache_vision", "premio")
VISION = "https://data.binance.vision/data/futures/um/monthly/premiumIndexKlines"
S3 = ("https://s3-ap-northeast-1.amazonaws.com/data.binance.vision?delimiter=/"
      "&prefix=data/futures/um/monthly/premiumIndexKlines/{s}/1h/")


def _get(url):
    for tentativa in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
        except Exception:
            pass
        time.sleep(2 + 2 * tentativa)
    return None


def _mes(sym, mes):
    raw = _get(f"{VISION}/{sym}/1h/{sym}-1h-{mes}.zip")
    if not raw:
        return {}
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        linhas = z.read(z.namelist()[0]).decode().splitlines()
    out = {}
    for l in linhas:
        p = l.split(",")
        if p and p[0][:1].isdigit():
            out[int(p[0])] = float(p[4])
    return out


def premio(sym):
    """{ts: premio de fechamento} com cache por simbolo."""
    os.makedirs(DIR, exist_ok=True)
    fpath = os.path.join(DIR, f"{sym}.json")
    if os.path.exists(fpath):
        with open(fpath) as f:
            return {int(k): v for k, v in json.load(f).items()}
    raw = _get(S3.format(s=sym))
    meses = sorted(set(re.findall(r"1h-(\d{4}-\d{2})\.zip<", raw.decode()))) if raw else []
    out = {}
    with ThreadPoolExecutor(12) as ex:
        for d in ex.map(lambda m: _mes(sym, m), meses):
            out.update(d)
    with open(fpath, "w") as f:
        json.dump(out, f)
    return out


def sinais(pr, piso=PISO):
    """[(ts, d)] em ordem."""
    ts = sorted(pr)
    v = [pr[t] for t in ts]
    out = []
    for i in range(JANELA, len(ts)):
        if ts[i] - ts[i - JANELA] > (JANELA + 48) * H:     # buraco grande na serie
            continue
        x = v[i]
        if abs(x) < piso:
            continue
        jan = sorted(v[i - JANELA:i])
        if len(jan) < MIN_VALIDAS:
            continue
        if x >= jan[int(P_ALTO * (len(jan) - 1))]:
            out.append((ts[i], -1))
        elif x <= jan[int(P_BAIXO * (len(jan) - 1))]:
            out.append((ts[i], 1))
    return out


def trades(sym, o, sin, btc_o, fund, hold):
    out, livre = [], 0
    for ts, d in sin:
        a, b = ts + H, ts + (1 + hold) * H
        if a < livre:
            continue
        p1, p2 = o.get(a), o.get(b)
        if not p1 or not p2:
            continue
        livre = b
        bruto = 100 * d * (p2 / p1 - 1)
        f = 100 * fund.soma(a, b) if fund else 0.0
        b1, b2 = btc_o.get(a), btc_o.get(b)
        exc = None if (sym == "BTCUSDT" or not b1 or not b2) else bruto - 100 * d * (b2 / b1 - 1)
        out.append({"ts": a, "d": d, "bruto": bruto, "abs": bruto - 100 * CUSTO_RT - d * f, "excesso": exc})
    return out


VARIANTES = [("PRIMARIA: premio extremo, 8h", PISO, HOLD), ("1h", PISO, 1), ("24h", PISO, 24),
             ("sem piso absoluto, 8h", 0.0, HOLD)]


def rodar(nome, btc_o, contar):
    res = {v[0]: [] for v in VARIANTES}
    n = 0
    for i, sym in enumerate(M.universo(nome)):
        pr = premio(sym)
        if len(pr) < JANELA + 100:
            continue
        try:
            c = DB.baixar(sym, "1H", M.DIAS)
        except Exception:
            continue
        n += 1
        o = {k[0]: k[1] for k in c}
        fund = None if contar else M.Funding(sym)
        for rot, piso, hold in VARIANTES:
            res[rot] += trades(sym, o, sinais(pr, piso), btc_o, fund, hold)
        if i % 50 == 0:
            print(f"    ... {i} pares", flush=True)
    print(f"  universo {nome}: {n} pares com premio e candles", flush=True)
    return res


def main(argv):
    t0 = time.time()
    contar = "--contar" in argv
    btc_o = {k[0]: k[1] for k in DB.baixar("BTCUSDT", "1H", M.DIAS)}
    decisao = None
    for nome, decide in (("A", False), ("DE", True)):
        print("\n" + "=" * 100 + f"\nUNIVERSO {nome} ({'DECIDE' if decide else 'descritivo'})"
              + (" -- SO CONTAGEM" if contar else "") + "\n" + "=" * 100, flush=True)
        res = rodar(nome, btc_o, contar)
        for rot, tr in res.items():
            vend = sum(1 for x in tr if x["d"] == -1)
            if contar:
                print(f"  {rot:<32} trades {len(tr):>6} | vendas {vend:>5} | compras {len(tr)-vend:>5} | "
                      f"semanas {len({x['ts'] // M.MS_SEMANA for x in tr}):>4}")
                continue
            print(f"\n  [{rot}]  trades {len(tr)} (vendas {vend})")
            for chave in ("bruto", "abs", "excesso"):
                print(M.linha(chave, tr, chave)[0])
            for d, lado in ((-1, "so vendas"), (1, "so compras")):
                sub = [x for x in tr if x["d"] == d]
                print(M.linha(f"{lado}: abs", sub, "abs")[0])
                print(M.linha(f"{lado}: excesso", sub, "excesso")[0])
        if decide and not contar:
            tr = res[VARIANTES[0][0]]
            if len(tr) < MIN_DECIDIR:
                decisao = f"SEM AMOSTRA PARA DECIDIR (n={len(tr)})"
            else:
                _, _, lo_a = M.linha("", tr, "abs")
                _, _, lo_e = M.linha("", tr, "excesso")
                decisao = "PASSA" if (lo_a > 0 and lo_e > 0) else "NAO PASSA"
    if decisao:
        print(f"\n  DECISAO (universo DE, regra primaria): {decisao}")
    print(f"\n  [{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main(sys.argv[1:])
