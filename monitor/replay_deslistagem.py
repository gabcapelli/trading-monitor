"""
Estudo 28 -- vender o perpetuo depois do anuncio de deslistagem do spot na
Binance, PRE-REGISTRADO em 04/10/2026, antes de calcular qualquer retorno.

HIPOTESE
--------
Quando a Binance anuncia que vai tirar um token do spot, o preco cai forte nas
primeiras horas (relatos de -15% a -40%). A pergunta NAO e se ele cai -- e se
AINDA cai depois de uma latencia realista, ate a deslistagem: venda forcada de
quem so tem o token na Binance, market makers saindo, liquidez sumindo.
Mecanismo de evento, como o desbloqueio de tokens (estudo 25).

EVENTOS
-------
- Fonte: feed publico de anuncios da Binance (bapi/composite/v1/public/cms/
  article/list/query), catalogo 161 (Delisting, desde 02/2022) e titulos com
  "Delist" nos catalogos 48 e 49 (2020-2021). Cache em cache_anuncios/.
- Evento = um token em titulo "Binance Will Delist A, B and C on AAAA-MM-DD"
  (ou "Binance Will Delist Nome (TKR)"). Remocao de par isolado, de margem, so do
  perpetuo, opcoes e Alpha ficam de fora.
- Excluidos por construcao (nao sao precificados por fluxo): stablecoins e
  wrapped (USDS, SUSD, RENBTC, IDRT, VAI, USDP) e o anuncio Non-MiCA.
- Horario do anuncio: `releaseDate` do feed (ms UTC).

REGRA (vendido no perpetuo USDT-M da Binance, TKRUSDT ou 1000TKRUSDT)
---------------------------------------------------------------------
- Entrada: abertura da 2a hora cheia apos o anuncio (anuncio 07:00:30 ->
  08:00 e a 1a, entrada na abertura das 09:00). Cobre a latencia do workflow
  horario com folga.
- Saida: abertura da hora que fica 24h antes do PRIMEIRO de: (a) a data da
  deslistagem do spot no titulo (00:00 UTC); (b) o fim do perpetuo (ultimo
  candle + 1h), se ele acabar antes de 30 dias depois da data do spot.
- Sem stop, sem alvo. Trade com saida <= entrada, ou sem candle de entrada,
  fica de fora (contado no log).

MEDIDAS (% do nocional, positivo = o vendido ganhou)
----------------------------------------------------
- `bruto`: -(saida/entrada - 1).
- `liq`: bruto - 0.18% (custo ida+volta, o mesmo dos outros estudos).
- `abs` (decide): liq + funding real recebido pelo vendido no periodo
  (fundingRate do data.binance.vision; funding negativo = o vendido paga).
- `excesso` (decide): bruto - retorno de vender a cesta dos 20 majors (A) nas
  mesmas horas de entrada e saida. Remove o mercado; nao inclui funding.
- Bootstrap por ANUNCIO (tokens do mesmo anuncio sao reamostrados juntos),
  5000 reamostragens, media = soma / n.

CRITERIO
--------
PASSA se `abs` E `excesso` tiverem IC95 inteiro acima de zero.
Com menos de 20 anuncios com trade valido: SEM AMOSTRA PARA DECIDIR.
Poder: com ~30 anuncios, so um efeito grande (da ordem de -5% a -10% de
deriva apos a entrada) sai do zero. Um NAO PASSA aqui quer dizer "nao ha
efeito grande", nao "nao ha efeito".

DESCRITIVOS (sem poder de decisao)
----------------------------------
- Reacao perdida: abertura da hora do anuncio -> entrada (o que a latencia
  custou).
- Custo de 0.5% e 1.0% (perpetuos iliquidos).
- PLACEBO: mesmo token, mesma duracao, janela deslocada 30 dias para tras.
  Tokens deslistados ja vem caindo; se o placebo der o mesmo excesso, o
  resultado e "token morrendo", nao o anuncio.
- Spot (todos os eventos com par TKRUSDT no spot, inclusive sem perpetuo):
  reacao ate a entrada e deriva entrada -> 24h antes da deslistagem. Mede se
  o mecanismo existe, mesmo onde nao da para vender.

CORRECOES DE BUG (04/10/2026, depois da 1a rodada -- log em deslistagem_v1.log)
-------------------------------------------------------------------------------
Nenhuma muda regra ou criterio; as duas sao de execucao:
1. `_meses()` mantinha a hora do dia ao avancar o mes e perdia o ultimo mes
   quando o fim caia no dia 1 antes daquela hora. Deixou a cesta do ALPACA
   vazia (excesso None), justamente o pior trade, que saiu da media do excesso.
2. Perpetuo ja encerrado: o data.binance.vision traz o mes com candles planos e
   volume zero (6 trades: BTCST, SRM, BTS, IDEX, SXP, MDT). Nao e operavel; sai
   pela regra "sem candle de entrada", agora checada por volume > 0.

Uso (de dentro de monitor/):
    python replay_deslistagem.py --contar   # eventos e trades validos, sem retorno
    python replay_deslistagem.py
"""

import csv
import io
import json
import os
import random
import re
import sys
import time
import urllib.error
import urllib.request
import zipfile
from collections import defaultdict
from datetime import datetime, timedelta, timezone

from replay_ema_ribbon import CUSTO_RT, UNIVERSO

H = 3_600_000
DIA = 24 * H
AQUI = os.path.dirname(os.path.abspath(__file__))
DIR_ANUNCIOS = os.path.join(AQUI, "cache_anuncios")
DIR_VISION = os.path.join(AQUI, "cache_vision")
VISION = "https://data.binance.vision/data"
EXCLUIDOS = {"USDS", "SUSD", "RENBTC", "IDRT", "VAI", "USDP"}
MIN_ANUNCIOS = 20
N_RESAMPLES = 5000
SEED = 42
PLACEBO_DIAS = 30
MAJORS = [s.replace("-SWAP", "").replace("-", "") for s in UNIVERSO]


# ---------------------------------------------------------------------------
# Eventos
# ---------------------------------------------------------------------------

def _get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    for tentativa in range(5):
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if tentativa == 4:
                raise
        except Exception:
            if tentativa == 4:
                raise
        time.sleep(2 + 2 * tentativa)


def baixar_anuncios():
    url = ("https://www.binance.com/bapi/composite/v1/public/cms/article/list/query"
           "?type=1&catalogId={}&pageNo={}&pageSize=50")
    os.makedirs(DIR_ANUNCIOS, exist_ok=True)
    for cat, so_delist in ((161, False), (48, True), (49, True)):
        todos = []
        for p in range(1, 200):
            d = json.loads(_get(url.format(cat, p)))["data"]["catalogs"]
            if not d or not d[0]["articles"]:
                break
            todos += d[0]["articles"]
            time.sleep(0.25)
        if so_delist:
            todos = [a for a in todos if re.search(r"[Dd]elist", a["title"])]
        nome = "cat161.json" if cat == 161 else f"cat{cat}_delist.json"
        with open(os.path.join(DIR_ANUNCIOS, nome), "w") as f:
            json.dump(todos, f)


def eventos():
    arts = []
    for nome in ("cat161.json", "cat48_delist.json", "cat49_delist.json"):
        with open(os.path.join(DIR_ANUNCIOS, nome)) as f:
            arts += json.load(f)
    lista = re.compile(r"^Binance (?:Will )?Delist (.+?) on (\d{4})[-/](\d{2})[-/](\d{2})\s*$")
    out, vistos = [], set()
    for a in arts:
        t = a["title"].strip()
        m = lista.match(t)
        if not m:
            continue
        data_spot = int(datetime(int(m.group(2)), int(m.group(3)), int(m.group(4)),
                                 tzinfo=timezone.utc).timestamp() * 1000)
        for tk in re.split(r",|&| and ", m.group(1)):
            tk = re.sub(r".*\((\w+)\)", r"\1", tk.strip())
            if not re.fullmatch(r"[A-Z0-9]{1,12}", tk) or tk in EXCLUIDOS:
                continue
            chave = (tk, a["releaseDate"] // DIA)
            if chave in vistos:
                continue
            vistos.add(chave)
            out.append({"token": tk, "ts": a["releaseDate"], "data_spot": data_spot, "titulo": t})
    return sorted(out, key=lambda e: e["ts"])


# ---------------------------------------------------------------------------
# data.binance.vision
# ---------------------------------------------------------------------------

def _meses(t0, t1):
    d = datetime.fromtimestamp(t0 / 1000, timezone.utc).replace(day=1, hour=0, minute=0, second=0,
                                                                 microsecond=0)
    fim = datetime.fromtimestamp(t1 / 1000, timezone.utc)
    while d <= fim:
        yield d.strftime("%Y-%m")
        d = d.replace(year=d.year + (d.month == 12), month=d.month % 12 + 1)


def _csv_zip(raw):
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        texto = z.read(z.namelist()[0]).decode()
    return [r for r in csv.reader(io.StringIO(texto)) if r and r[0][:1].isdigit()]


def _ms(x):
    x = int(x)
    return x // 1000 if x > 10**14 else x   # spot desde 2025 vem em microssegundos


def klines_mes(mercado, sym, mes):
    """{ts: (o, h, l, c, volume)} de 1h; mercado 'futures/um' ou 'spot'. Mes
    corrente ou ainda sem arquivo mensal: arquivos diarios."""
    os.makedirs(DIR_VISION, exist_ok=True)
    fpath = os.path.join(DIR_VISION, f"{mercado.replace('/', '_')}_{sym}_1h_{mes}_v.json")
    if os.path.exists(fpath):
        with open(fpath) as f:
            return {int(k): v for k, v in json.load(f).items()}
    raw = _get(f"{VISION}/{mercado}/monthly/klines/{sym}/1h/{sym}-1h-{mes}.zip")
    linhas = []
    hoje = datetime.now(timezone.utc)
    mes_anterior = (hoje.replace(day=1) - timedelta(days=1)).strftime("%Y-%m")
    if raw:
        linhas = _csv_zip(raw)
    elif mes >= mes_anterior:
        # so o mes corrente e o anterior podem ainda nao ter arquivo mensal;
        # mes antigo sem arquivo = simbolo nao negociava nele
        ano, m = map(int, mes.split("-"))
        for dia in range(1, 32):
            try:
                d = datetime(ano, m, dia, tzinfo=timezone.utc)
            except ValueError:
                break
            if d >= hoje:
                break
            r = _get(f"{VISION}/{mercado}/daily/klines/{sym}/1h/{sym}-1h-{d:%Y-%m-%d}.zip")
            if r:
                linhas += _csv_zip(r)
    out = {_ms(r[0]): [float(r[1]), float(r[2]), float(r[3]), float(r[4]), float(r[5])] for r in linhas}
    mes_fechado = mes < datetime.now(timezone.utc).strftime("%Y-%m")
    if mes_fechado:
        with open(fpath, "w") as f:
            json.dump(out, f)
    return out


def klines(mercado, sym, t0, t1):
    out = {}
    for mes in _meses(t0, t1):
        out.update(klines_mes(mercado, sym, mes))
    return out


def meses_disponiveis(mercado, sym):
    fpath = os.path.join(DIR_VISION, f"lista_{mercado.replace('/', '_')}_{sym}.json")
    if os.path.exists(fpath):
        with open(fpath) as f:
            return json.load(f)
    url = ("https://s3-ap-northeast-1.amazonaws.com/data.binance.vision?delimiter=/"
           f"&prefix=data/{mercado}/monthly/klines/{sym}/1h/")
    meses = sorted(set(re.findall(r"1h-(\d{4}-\d{2})\.zip<", _get(url).decode())))
    os.makedirs(DIR_VISION, exist_ok=True)
    with open(fpath, "w") as f:
        json.dump(meses, f)
    return meses


def funding(sym, t0, t1):
    """Soma das taxas com calc_time em [t0, t1)."""
    soma = 0.0
    for mes in _meses(t0, t1):
        fpath = os.path.join(DIR_VISION, f"funding_{sym}_{mes}.json")
        if os.path.exists(fpath):
            with open(fpath) as f:
                linhas = json.load(f)
        else:
            raw = _get(f"{VISION}/futures/um/monthly/fundingRate/{sym}/{sym}-fundingRate-{mes}.zip")
            linhas = [[_ms(r[0]), float(r[2])] for r in _csv_zip(raw)] if raw else []
            if mes < datetime.now(timezone.utc).strftime("%Y-%m"):
                with open(fpath, "w") as f:
                    json.dump(linhas, f)
        soma += sum(x for ts, x in linhas if t0 <= ts < t1)
    return soma


# ---------------------------------------------------------------------------
# Trades
# ---------------------------------------------------------------------------

def simbolo_perp(tk, ts):
    mes = datetime.fromtimestamp(ts / 1000, timezone.utc).strftime("%Y-%m")
    for sym in (f"{tk}USDT", f"1000{tk}USDT"):
        meses = meses_disponiveis("futures/um", sym)
        if mes in meses:
            return sym, meses
    return None, None


def abertura(serie, ts):
    k = serie.get(ts)
    return k[0] if k else None


def montar_trade(e):
    sym, meses = simbolo_perp(e["token"], e["ts"])
    if not sym:
        return None, "sem perpetuo"
    entrada_ts = (e["ts"] // H + 2) * H
    fim_mes = meses[-1]
    serie = klines("futures/um", sym, e["ts"] - 40 * DIA, e["data_spot"] + 31 * DIA)
    if not serie:
        return None, "sem candles"
    ultimo = max(serie)
    limite = e["data_spot"]
    if ultimo + H < e["data_spot"] + 30 * DIA:
        limite = min(limite, ultimo + H)
    saida_ts = (limite - DIA) // H * H
    if saida_ts <= entrada_ts:
        return None, "saida antes da entrada"
    p_in, p_out = abertura(serie, entrada_ts), abertura(serie, saida_ts)
    if p_in is None or p_out is None:
        return None, "sem candle de entrada/saida"
    if serie[entrada_ts][4] == 0:
        return None, "perpetuo sem negociacao na entrada"
    p_anuncio = abertura(serie, e["ts"] // H * H)
    t = {**e, "sym": sym, "entrada_ts": entrada_ts, "saida_ts": saida_ts,
         "dur_d": (saida_ts - entrada_ts) / DIA, "fim_mes_perp": fim_mes,
         "bruto": -100 * (p_out / p_in - 1),
         "reacao": None if p_anuncio is None else -100 * (p_in / p_anuncio - 1)}
    pl_in, pl_out = abertura(serie, entrada_ts - PLACEBO_DIAS * DIA), abertura(serie, saida_ts - PLACEBO_DIAS * DIA)
    t["placebo_bruto"] = None if (pl_in is None or pl_out is None) else -100 * (pl_out / pl_in - 1)
    return t, "ok"


def cesta(t0, t1, cache):
    """Retorno % de VENDER a cesta de majors de abertura t0 a abertura t1."""
    rets = []
    for sym in MAJORS:
        if sym not in cache:
            cache[sym] = {}
        for mes in _meses(t0, t1):
            if (sym, mes) not in cache:
                cache[(sym, mes)] = True
                cache[sym].update(klines_mes("futures/um", sym, mes))
        a, b = abertura(cache[sym], t0), abertura(cache[sym], t1)
        if a and b:
            rets.append(-100 * (b / a - 1))
    return sum(rets) / len(rets) if rets else None


def spot_descritivo(e):
    sym = f"{e['token']}USDT"
    mes = datetime.fromtimestamp(e["ts"] / 1000, timezone.utc).strftime("%Y-%m")
    if mes not in meses_disponiveis("spot", sym):
        return None
    serie = klines("spot", sym, e["ts"] - DIA, e["data_spot"])
    entrada_ts = (e["ts"] // H + 2) * H
    saida_ts = (e["data_spot"] - DIA) // H * H
    a, p_in, p_out = abertura(serie, e["ts"] // H * H), abertura(serie, entrada_ts), abertura(serie, saida_ts)
    if None in (a, p_in, p_out) or saida_ts <= entrada_ts:
        return None
    return {"ts": e["ts"], "reacao": 100 * (p_in / a - 1), "deriva": 100 * (p_out / p_in - 1)}


# ---------------------------------------------------------------------------
# Estatistica
# ---------------------------------------------------------------------------

def boot_anuncio(itens, chave):
    g = defaultdict(list)
    for x in itens:
        if x.get(chave) is not None:
            g[x["ts"]].append(x[chave])
    grupos = list(g.values())
    if len(grupos) < 3:
        return None
    n = sum(len(v) for v in grupos)
    media = sum(sum(v) for v in grupos) / n
    rng = random.Random(SEED)
    ms = []
    for _ in range(N_RESAMPLES):
        s = k = 0
        for _ in range(len(grupos)):
            v = grupos[rng.randrange(len(grupos))]
            s += sum(v)
            k += len(v)
        ms.append(s / k)
    ms.sort()
    return media, ms[int(0.025 * N_RESAMPLES)], ms[int(0.975 * N_RESAMPLES) - 1], n, len(grupos)


def linha(rot, itens, chave):
    r = boot_anuncio(itens, chave)
    if r is None:
        return f"  {rot:<40} (insuficiente)", None
    m, lo, hi, n, g = r
    return f"  {rot:<40} n={n:>4} anuncios={g:>3} media {m:+8.2f}% IC95 [{lo:+8.2f}, {hi:+8.2f}]", lo


def main(argv):
    t0 = time.time()
    if "--baixar-anuncios" in argv or not os.path.exists(os.path.join(DIR_ANUNCIOS, "cat161.json")):
        baixar_anuncios()
    evs = eventos()
    print(f"Eventos (token x anuncio), sem stablecoins/wrapped: {len(evs)} em "
          f"{len({e['ts'] for e in evs})} anuncios")
    trades, motivos = [], defaultdict(int)
    for e in evs:
        t, motivo = montar_trade(e)
        motivos[motivo] += 1
        if t:
            trades.append(t)
    print("Montagem:", dict(motivos))
    print(f"Trades validos: {len(trades)} em {len({t['ts'] for t in trades})} anuncios | "
          f"duracao media {sum(t['dur_d'] for t in trades)/max(len(trades),1):.1f} d")
    if "--contar" in argv:
        for t in trades:
            print(f"    {datetime.fromtimestamp(t['ts']/1000, timezone.utc):%Y-%m-%d %H:%M} "
                  f"{t['sym']:<14} {t['dur_d']:>5.1f} d")
        return

    cache = {}
    for t in trades:
        c = cesta(t["entrada_ts"], t["saida_ts"], cache)
        t["excesso"] = None if c is None else t["bruto"] - c
        f = funding(t["sym"], t["entrada_ts"], t["saida_ts"])
        t["funding_recebido"] = 100 * f
        t["liq"] = t["bruto"] - 100 * CUSTO_RT
        t["abs"] = t["liq"] + 100 * f
        t["abs_custo05"] = t["bruto"] - 0.5 + 100 * f
        t["abs_custo10"] = t["bruto"] - 1.0 + 100 * f
        if t["placebo_bruto"] is not None:
            cp = cesta(t["entrada_ts"] - PLACEBO_DIAS * DIA, t["saida_ts"] - PLACEBO_DIAS * DIA, cache)
            t["placebo_excesso"] = None if cp is None else t["placebo_bruto"] - cp
        else:
            t["placebo_excesso"] = None

    print("\n" + "=" * 100 + "\nVENDIDO NO PERPETUO (positivo = vendido ganhou)\n" + "=" * 100)
    for chave, rot in (("bruto", "bruto"), ("liq", "liquido (custo 0.18%)"),
                       ("funding_recebido", "funding recebido"),
                       ("abs", "ABSOLUTO (decide)"), ("excesso", "EXCESSO sobre majors (decide)"),
                       ("abs_custo05", "absoluto, custo 0.5%"), ("abs_custo10", "absoluto, custo 1.0%"),
                       ("reacao", "reacao perdida (anuncio -> entrada)"),
                       ("placebo_bruto", "PLACEBO -30d: bruto"), ("placebo_excesso", "PLACEBO -30d: excesso")):
        print(linha(rot, trades, chave)[0])

    sp = [s for s in (spot_descritivo(e) for e in evs) if s]
    print("\n" + "=" * 100 + "\nSPOT, todos os eventos com par USDT (descritivo; positivo = preco subiu)\n" + "=" * 100)
    print(linha("reacao (anuncio -> entrada)", sp, "reacao")[0])
    print(linha("deriva (entrada -> 24h antes do delist)", sp, "deriva")[0])

    print("\n  Por trade (perpetuo):")
    for t in trades:
        print(f"    {datetime.fromtimestamp(t['ts']/1000, timezone.utc):%Y-%m-%d} {t['sym']:<14} "
              f"{t['dur_d']:>5.1f} d | reacao {t['reacao'] if t['reacao'] is not None else float('nan'):+7.1f}% "
              f"| bruto {t['bruto']:+7.1f}% | funding {t['funding_recebido']:+6.2f}% | abs {t['abs']:+7.1f}% "
              f"| excesso {t['excesso'] if t['excesso'] is not None else float('nan'):+7.1f}%")

    n_anuncios = len({t["ts"] for t in trades})
    if n_anuncios < MIN_ANUNCIOS:
        decisao = f"SEM AMOSTRA PARA DECIDIR ({n_anuncios} anuncios < {MIN_ANUNCIOS})"
    else:
        _, lo_a = linha("", trades, "abs")
        _, lo_e = linha("", trades, "excesso")
        decisao = "PASSA" if (lo_a is not None and lo_e is not None and lo_a > 0 and lo_e > 0) else "NAO PASSA"
    print(f"\n  DECISAO: {decisao}\n  [{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main(sys.argv[1:])
