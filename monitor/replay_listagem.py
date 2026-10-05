"""
Estudo 29 -- comprar o perpetuo depois do anuncio de listagem no SPOT da
Binance, PRE-REGISTRADO em 04/10/2026, antes de calcular qualquer retorno.

HIPOTESE
--------
A literatura (The Tie, 1.844 listagens 2023-2026) acha a alta no ANUNCIO, nao
na listagem: o preco sobe entre o anuncio e o inicio da negociacao e devolve em
~2 semanas. A pergunta e se essa alta ainda existe DEPOIS de uma latencia
realista -- comprando apos o anuncio e vendendo na abertura do spot ("compra no
boato, vende no fato"). Mesmo arcabouco do estudo 28 (replay_deslistagem.py),
lado comprado: sem o risco de squeeze contra que matou aquele.

EVENTOS (criterio estrutural, sem classificar titulo a mao)
-----------------------------------------------------------
- Anuncios do catalogo 48 (New Cryptocurrency Listing) do feed publico da
  Binance, desde 2017. Ticker = cada "(TKR)" no titulo.
- Inicio do spot = primeiro candle de 1h do token no spot da Binance, em
  qualquer par com cotacao USDT, BUSD, FDUSD, USDC, BTC, BNB ou TRY
  (data.binance.vision, que preserva pares removidos).
- Evento = (ticker, anuncio) com o inicio do spot DEPOIS do anuncio e no
  maximo 7 dias depois. Se varios anuncios citam o mesmo ticker nessa janela,
  vale o mais antigo.
- Excluidos: stablecoins e wrapped (ticker contendo USD, DAI, EUR, WBTC, WBETH,
  BETH, RENBTC).
- Operavel: perpetuo USDT-M da Binance (TKRUSDT ou 1000TKRUSDT) com volume > 0
  no candle de entrada.

REGRA (comprado no perpetuo)
----------------------------
- Entrada: abertura da 2a hora cheia apos o anuncio (igual ao estudo 28).
- Saida: abertura da hora em que o spot comeca a negociar.
- Sem stop, sem alvo. Saida <= entrada, ou perpetuo sem candle/volume na
  entrada ou na saida: fora (contado no log).

MEDIDAS (% do nocional, positivo = comprado ganhou)
---------------------------------------------------
- `abs` (decide): bruto - 0.18% de custo - funding pago pelo comprado.
- `excesso` (decide): bruto - retorno de comprar a cesta dos 20 majors nas
  mesmas horas. Sem funding.
- Bootstrap por ANUNCIO, 5000 reamostragens.

CRITERIO
--------
PASSA se `abs` E `excesso` tiverem IC95 inteiro acima de zero.
Com menos de 20 anuncios com trade valido: SEM AMOSTRA PARA DECIDIR.

DESCRITIVOS (sem poder de decisao)
----------------------------------
- Reacao perdida: abertura da hora do anuncio -> entrada.
- Depois da listagem: abertura do spot -> +24h e -> +7d (o "devolve").
- Custo de 0.5%.
- Por ano de anuncio (o premio vem encolhendo, segundo a literatura).
- PLACEBO: mesmo perpetuo, mesma duracao, janela 30 dias antes.

Uso (de dentro de monitor/):
    python replay_listagem.py --contar
    python replay_listagem.py
"""

import json
import os
import re
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone

import replay_deslistagem as R
from replay_ema_ribbon import CUSTO_RT

H, DIA = R.H, R.DIA
JANELA_LISTAGEM = 7 * DIA
COTACOES = ("USDT", "BUSD", "FDUSD", "USDC", "BTC", "BNB", "TRY")
EXCLUI_SUB = ("USD", "DAI", "EUR")
EXCLUI = {"WBTC", "WBETH", "BETH", "RENBTC"}
PLACEBO_DIAS = 30


def baixar_cat48():
    fpath = os.path.join(R.DIR_ANUNCIOS, "cat48.json")
    if os.path.exists(fpath):
        with open(fpath) as f:
            return json.load(f)
    url = ("https://www.binance.com/bapi/composite/v1/public/cms/article/list/query"
           "?type=1&catalogId=48&pageNo={}&pageSize=50")
    todos = []
    for p in range(1, 200):
        d = json.loads(R._get(url.format(p)))["data"]["catalogs"]
        if not d or not d[0]["articles"]:
            break
        todos += d[0]["articles"]
        time.sleep(0.25)
    os.makedirs(R.DIR_ANUNCIOS, exist_ok=True)
    with open(fpath, "w") as f:
        json.dump(todos, f)
    return todos


def inicio_spot(tk):
    """Primeiro candle de 1h do token no spot da Binance (ms) ou None."""
    fpath = os.path.join(R.DIR_VISION, f"inicio_spot_{tk}.json")
    if os.path.exists(fpath):
        with open(fpath) as f:
            return json.load(f)["inicio"]
    inicio = None
    url = ("https://s3-ap-northeast-1.amazonaws.com/data.binance.vision?delimiter=/"
           f"&prefix=data/spot/monthly/klines/{tk}")
    dirs = set(re.findall(r"klines/([A-Z0-9]+)/</Prefix>", R._get(url).decode()))
    for q in COTACOES:
        sym = tk + q
        if sym not in dirs:
            continue
        meses = R.meses_disponiveis("spot", sym)
        if not meses:
            continue
        serie = R.klines_mes("spot", sym, meses[0])
        if serie:
            t = min(serie)
            inicio = t if inicio is None else min(inicio, t)
    os.makedirs(R.DIR_VISION, exist_ok=True)
    with open(fpath, "w") as f:
        json.dump({"inicio": inicio}, f)
    return inicio


def eventos():
    arts = sorted(baixar_cat48(), key=lambda a: a["releaseDate"])
    por_tk = defaultdict(list)
    for a in arts:
        for tk in set(re.findall(r"\(([A-Z0-9]{2,12})\)", a["title"])):
            if tk in EXCLUI or any(s in tk for s in EXCLUI_SUB):
                continue
            por_tk[tk].append(a)
    out = []
    for i, (tk, lista) in enumerate(sorted(por_tk.items())):
        ini = inicio_spot(tk)
        if ini is None:
            continue
        validos = [a for a in lista if a["releaseDate"] < ini <= a["releaseDate"] + JANELA_LISTAGEM]
        if validos:
            a = validos[0]
            out.append({"token": tk, "ts": a["releaseDate"], "inicio_spot": ini, "titulo": a["title"]})
        if i % 200 == 0:
            print(f"  ... {i}/{len(por_tk)} tickers", flush=True)
    return sorted(out, key=lambda e: e["ts"])


def montar_trade(e):
    sym, _ = R.simbolo_perp(e["token"], e["ts"])
    if not sym:
        return None, "sem perpetuo"
    entrada_ts = (e["ts"] // H + 2) * H
    saida_ts = e["inicio_spot"] // H * H
    if saida_ts <= entrada_ts:
        return None, "spot abriu antes da entrada"
    serie = R.klines("futures/um", sym, e["ts"] - 40 * DIA, saida_ts + 8 * DIA)
    k_in, k_out = serie.get(entrada_ts), serie.get(saida_ts)
    if not k_in or not k_out:
        return None, "sem candle de entrada/saida"
    if k_in[4] == 0 or k_out[4] == 0:
        return None, "perpetuo sem negociacao"
    p_in, p_out = k_in[0], k_out[0]

    def ret(a, b):
        ka, kb = serie.get(a), serie.get(b)
        return None if not ka or not kb else 100 * (kb[0] / ka[0] - 1)

    t = {**e, "sym": sym, "entrada_ts": entrada_ts, "saida_ts": saida_ts,
         "dur_h": (saida_ts - entrada_ts) / H, "ano": datetime.fromtimestamp(e["ts"] / 1000, timezone.utc).year,
         "bruto": 100 * (p_out / p_in - 1),
         "reacao": ret(e["ts"] // H * H, entrada_ts),
         "pos_24h": ret(saida_ts, saida_ts + DIA),
         "pos_7d": ret(saida_ts, saida_ts + 7 * DIA),
         "placebo_bruto": ret(entrada_ts - PLACEBO_DIAS * DIA, saida_ts - PLACEBO_DIAS * DIA)}
    return t, "ok"


def main(argv):
    t0 = time.time()
    evs = eventos()
    print(f"Eventos de listagem no spot (anuncio -> spot em ate 7 d): {len(evs)} em "
          f"{len({e['ts'] for e in evs})} anuncios")
    trades, motivos = [], defaultdict(int)
    for e in evs:
        t, motivo = montar_trade(e)
        motivos[motivo] += 1
        if t:
            trades.append(t)
    print("Montagem:", dict(motivos))
    print(f"Trades validos: {len(trades)} em {len({t['ts'] for t in trades})} anuncios | "
          f"duracao mediana {sorted(t['dur_h'] for t in trades)[len(trades)//2] if trades else 0:.0f} h")
    por_ano = defaultdict(int)
    for t in trades:
        por_ano[t["ano"]] += 1
    print("Por ano:", dict(sorted(por_ano.items())))
    if "--contar" in argv:
        return

    cache = {}
    for t in trades:
        c = R.cesta(t["entrada_ts"], t["saida_ts"], cache)       # retorno de VENDER a cesta
        t["excesso"] = None if c is None else t["bruto"] + c
        f = 100 * R.funding(t["sym"], t["entrada_ts"], t["saida_ts"])
        t["funding_pago"] = f
        t["abs"] = t["bruto"] - 100 * CUSTO_RT - f
        t["abs_custo05"] = t["bruto"] - 0.5 - f
        if t["placebo_bruto"] is not None:
            cp = R.cesta(t["entrada_ts"] - PLACEBO_DIAS * DIA, t["saida_ts"] - PLACEBO_DIAS * DIA, cache)
            t["placebo_excesso"] = None if cp is None else t["placebo_bruto"] + cp
        else:
            t["placebo_excesso"] = None

    print("\n" + "=" * 100 + "\nCOMPRADO NO PERPETUO, anuncio -> abertura do spot (positivo = comprado ganhou)\n"
          + "=" * 100)
    for chave, rot in (("bruto", "bruto"), ("funding_pago", "funding pago"),
                       ("abs", "ABSOLUTO (decide)"), ("excesso", "EXCESSO sobre majors (decide)"),
                       ("abs_custo05", "absoluto, custo 0.5%"),
                       ("reacao", "reacao perdida (anuncio -> entrada)"),
                       ("pos_24h", "depois: abertura do spot -> +24h"),
                       ("pos_7d", "depois: abertura do spot -> +7d"),
                       ("placebo_bruto", "PLACEBO -30d: bruto"), ("placebo_excesso", "PLACEBO -30d: excesso")):
        print(R.linha(rot, trades, chave)[0])
    print("\n  Por ano (descritivo):")
    for ano in sorted({t["ano"] for t in trades}):
        sub = [t for t in trades if t["ano"] == ano]
        print(R.linha(f"{ano} abs", sub, "abs")[0])
        print(R.linha(f"{ano} excesso", sub, "excesso")[0])

    v = sorted(t["abs"] for t in trades)
    if v:
        print(f"\n  abs: positivos {sum(x > 0 for x in v)}/{len(v)} | mediana {v[len(v)//2]:+.2f}% | "
              f"5 piores {[round(x, 1) for x in v[:5]]} | 5 melhores {[round(x, 1) for x in v[-5:]]}")
    print("\n  Por trade:")
    for t in trades:
        print(f"    {datetime.fromtimestamp(t['ts']/1000, timezone.utc):%Y-%m-%d %H:%M} {t['sym']:<16} "
              f"{t['dur_h']:>5.0f} h | bruto {t['bruto']:+7.2f}% | abs {t['abs']:+7.2f}% | excesso "
              f"{t['excesso'] if t['excesso'] is not None else float('nan'):+7.2f}%")

    n_anuncios = len({t["ts"] for t in trades})
    if n_anuncios < R.MIN_ANUNCIOS:
        decisao = f"SEM AMOSTRA PARA DECIDIR ({n_anuncios} anuncios < {R.MIN_ANUNCIOS})"
    else:
        _, lo_a = R.linha("", trades, "abs")
        _, lo_e = R.linha("", trades, "excesso")
        decisao = "PASSA" if (lo_a is not None and lo_e is not None and lo_a > 0 and lo_e > 0) else "NAO PASSA"
    print(f"\n  DECISAO: {decisao}\n  [{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main(sys.argv[1:])
