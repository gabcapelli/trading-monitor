"""
Estudo 37 -- vender o perpetuo depois que a Binance aplica a Monitoring Tag,
PRE-REGISTRADO em 05/10/2026, antes de calcular qualquer retorno.

HIPOTESE
--------
A Monitoring Tag marca um token como de alto risco e candidato a deslistagem:
o app passa a exigir um aviso de risco de quem compra, e o token entra em
revisao periodica. A hipotese e de pressao vendedora LENTA (dias), de quem
nao quer carregar um token sob ameaca de deslistagem -- diferente do estudo 28
(anuncio de deslistagem), aqui o spot continua listado e liquido, entao o
squeeze que destruiu o 28 no perpetuo deve ser menor. Mecanismo de evento
idiossincratico e agendado, como o desbloqueio (estudo 25), o unico que passou.

Direcao fixada A PRIORI pelo mecanismo: VENDIDO. Nao ha parametro a escolher,
entao nao ha periodo de desenvolvimento: a amostra inteira decide, e o recorte
2023-24 x 2025-26 sai so como descritivo.

EVENTOS
-------
- Fonte: feed de anuncios da Binance (mesmo de replay_deslistagem.py),
  catalogos 49 e 161, titulos com "Monitoring Tag". Cache em
  cache_anuncios/monitoring.json.
- Evento = um token em "Binance Will Extend the Monitoring Tag to (Include)
  A, B & C [, Remove ...] on AAAA-MM-DD". Titulos que so removem a tag ficam de
  fora. O anuncio de lancamento (26/07/2023) lista os tokens so no corpo, nao no
  titulo: fica de fora por construcao.
- Token que ja tinha recebido a tag num anuncio anterior: so vale a 1a vez.
- Excluidos por construcao: stablecoins (AEUR, VAI).
- Horario: `releaseDate` do feed (ms UTC).

REGRA (vendido no perpetuo USDT-M da Binance, TKRUSDT ou 1000TKRUSDT)
---------------------------------------------------------------------
- Perpetuo precisa ter candle com volume na entrada e 30 dias antes dela.
- Entrada: abertura da 2a hora cheia apos o anuncio (igual ao estudo 28).
- Duas janelas: saida na abertura de entrada + 7 dias e de entrada + 14 dias.
- Se o perpetuo acabar antes da saida: sai na abertura do ultimo candle com
  volume (contado no log).
- Sem stop, sem alvo.

MEDIDAS (% do nocional, positivo = o vendido ganhou)
----------------------------------------------------
- `bruto`: -(saida/entrada - 1).
- `abs` (decide): bruto - 0.18% de custo + funding real recebido pelo vendido.
- `excesso` (decide): bruto - retorno de vender a LINHA DE BASE nas mesmas horas.
  Linha de base = media de ate 30 perpetuos USDT-M sorteados (semente = hora do
  anuncio) entre TODOS os que tinham candle com volume na entrada e na saida e
  30 dias antes da entrada -- inclusive os deslistados depois (lista do S3 do
  data.binance.vision), para nao ter vies de sobrevivencia. Fora: os tokens do
  proprio anuncio e perpetuos de acao/commodity (underlyingType != COIN na
  exchangeInfo atual; simbolo ausente dela = deslistado = cripto).
- Bootstrap por ANUNCIO (tokens do mesmo anuncio sao reamostrados juntos),
  5000 reamostragens, media = soma / n.

CRITERIO
--------
PASSA se, em alguma das duas janelas, `abs` E `excesso` tiverem IC 97.5%
(Bonferroni para 2 janelas) inteiro acima de zero.
Com menos de 15 anuncios com trade valido: SEM AMOSTRA PARA DECIDIR.
Poder: ~25 anuncios. So um efeito grande sai do zero; um NAO PASSA quer dizer
"nao ha efeito grande", nao "nao ha efeito". Se o centro vier positivo com IC
cruzando zero, o caminho e teste de papel adiante, NAO grade de parametros.

DESCRITIVOS (sem poder de decisao)
----------------------------------
- PLACEBO: mesmo token, mesma janela deslocada 30 dias para tras. Token com tag
  ja vem caindo; se o placebo der o mesmo excesso, o resultado e "token
  morrendo", nao o anuncio.
- Reacao perdida: abertura da hora do anuncio -> entrada.
- Custo de 0.5% e 1.0%.
- Sem os trades cujo token teve anuncio de deslistagem dentro da janela
  (sobreposicao com o estudo 28).
- Recorte 2023-24 x 2025-26.
- Spot (tokens com par USDT no spot, inclusive sem perpetuo): deriva
  entrada -> +7 e +14 dias, positivo = preco subiu. Mede se o mecanismo existe.

VALIDACAO
---------
`--passeio [--semente N]`: troca todos os precos (tokens e linha de base) por
passeios aleatorios sem deriva, nas mesmas datas, com funding zero. Nenhuma
janela pode passar e o excesso medio tem de ficar perto de zero.
Acrescentado depois da 1a semente (05/10/2026, antes de qualquer retorno real):
a semente 0 deu o PLACEBO do excesso com IC inteiro negativo. Com caudas tao
pesadas (+-70% em 14 dias no sintetico) e 23 grupos, o IC pode cobrir menos
que o nominal; mede-se a taxa de falso positivo em 20 sementes.
Resultado (claude/monitoring_tag_passeio_sementes.log): medias em torno de zero
(sem vies); cada medida sai "significativa" em 1-3 de 20 sementes (nominal
~0.5) e a DECISAO deu PASSA falso em 1 de 20 (5%, nominal ~2.5%). O criterio
fica como esta, mas, dado o IC otimista, um PASSA aqui vale como candidato a
teste de papel, nao como prova. Registrado antes de rodar com precos reais.

Uso (de dentro de monitor/):
    python replay_monitoring_tag.py --contar    # eventos e trades validos, sem retorno
    python replay_monitoring_tag.py --passeio   # validacao
    python replay_monitoring_tag.py
"""

import json
import math
import os
import random
import re
import sys
import time
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone

import replay_deslistagem as D
from replay_deslistagem import CUSTO_RT, DIA, H, _get, abertura, funding, klines, meses_disponiveis

ARQ_ANUNCIOS = os.path.join(D.DIR_ANUNCIOS, "monitoring.json")
ARQ_UNIVERSO = os.path.join(D.DIR_VISION, "lista_um_simbolos.json")
ARQ_TIPOS = os.path.join(D.DIR_VISION, "tipos_um.json")
EXCLUIDOS = {"AEUR", "VAI"}
JANELAS = (7, 14)
N_XS = 30
MIN_ANUNCIOS = 15
CONF = 0.975
N_RESAMPLES = 5000
SEED = 42
PLACEBO_DIAS = 30
HIST_MIN = 30 * DIA


# ---------------------------------------------------------------------------
# Eventos
# ---------------------------------------------------------------------------

def baixar_anuncios():
    url = ("https://www.binance.com/bapi/composite/v1/public/cms/article/list/query"
           "?type=1&catalogId={}&pageNo={}&pageSize=50")
    todos = []
    for cat in (49, 161):
        for p in range(1, 200):
            d = json.loads(_get(url.format(cat, p)))["data"]["catalogs"]
            if not d or not d[0]["articles"]:
                break
            todos += [a for a in d[0]["articles"] if "monitoring tag" in a["title"].lower()]
            time.sleep(0.5)
    os.makedirs(D.DIR_ANUNCIOS, exist_ok=True)
    with open(ARQ_ANUNCIOS, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False)


def eventos():
    if not os.path.exists(ARQ_ANUNCIOS):
        baixar_anuncios()
    with open(ARQ_ANUNCIOS, encoding="utf-8") as f:
        arts = sorted({a["title"]: a for a in json.load(f)}.values(), key=lambda a: a["releaseDate"])
    padrao = re.compile(r"Extend the Monitoring Tag to (?:Include )?(.+?)"
                        r"(?:,? (?:and )?Remove .*)? on \d{4}-\d{2}-\d{2}\s*$")
    out, vistos = [], set()
    for a in arts:
        m = padrao.search(a["title"].strip())
        if not m:
            continue
        for tk in re.split(r",|&| and ", m.group(1)):
            tk = re.sub(r".*\((\w+)\)", r"\1", tk.strip())
            if not re.fullmatch(r"[A-Z0-9]{1,12}", tk) or tk in EXCLUIDOS or tk in vistos:
                continue
            vistos.add(tk)
            out.append({"token": tk, "ts": a["releaseDate"], "titulo": a["title"].strip()})
    return out


def deslistagens():
    """{token: [ts do anuncio de deslistagem]} a partir do estudo 28."""
    out = defaultdict(list)
    for e in D.eventos():
        out[e["token"]].append(e["ts"])
    return out


# ---------------------------------------------------------------------------
# Universo da linha de base
# ---------------------------------------------------------------------------

def universo():
    if os.path.exists(ARQ_UNIVERSO):
        with open(ARQ_UNIVERSO) as f:
            return [x for x in json.load(f) if re.fullmatch(r"[A-Z0-9]+USDT", x)]
    marcador, syms = "", []
    base = "https://s3-ap-northeast-1.amazonaws.com/data.binance.vision?delimiter=/&prefix=data/futures/um/monthly/klines/"
    while True:
        t = _get(base + (f"&marker={marcador}" if marcador else "")).decode()
        s = re.findall(r"<Prefix>data/futures/um/monthly/klines/([^/<]+)/</Prefix>", t)
        syms += s
        if "<IsTruncated>true" not in t or not s:
            break
        marcador = f"data/futures/um/monthly/klines/{s[-1]}/"
    syms = sorted(x for x in set(syms) if re.fullmatch(r"[A-Z0-9]+USDT", x))  # ha simbolos em chines
    with open(ARQ_UNIVERSO, "w") as f:
        json.dump(syms, f)
    return syms


def tipos():
    if os.path.exists(ARQ_TIPOS):
        with open(ARQ_TIPOS) as f:
            return json.load(f)
    d = json.loads(_get("https://fapi.binance.com/fapi/v1/exchangeInfo"))
    out = {s["symbol"]: s.get("underlyingType", "?") for s in d["symbols"]}
    with open(ARQ_TIPOS, "w") as f:
        json.dump(out, f)
    return out


def _mes(ts):
    return datetime.fromtimestamp(ts / 1000, timezone.utc).strftime("%Y-%m")


def candidatos_base(t_ini, t_fim, excluir):
    tp = tipos()
    precisa = {_mes(t_ini - HIST_MIN), _mes(t_ini), _mes(t_fim)}
    out = []
    for s in universo():
        if s in excluir or tp.get(s, "COIN") != "COIN":
            continue
        if precisa <= set(meses_disponiveis("futures/um", s)):
            out.append(s)
    return out


# ---------------------------------------------------------------------------
# Series (reais ou passeio aleatorio)
# ---------------------------------------------------------------------------

PASSEIO = False
SEMENTE_PASSEIO = 0
_series = {}


def serie(mercado, sym, t0, t1):
    if not PASSEIO:
        return klines(mercado, sym, t0, t1)
    chave = (mercado, sym, t0, t1)
    if chave not in _series:
        real = klines(mercado, sym, t0, t1)
        rng = random.Random(f"{sym}{t0}{SEMENTE_PASSEIO}")
        ts = sorted(real)
        rets = [math.log(real[b][3] / real[a][3]) for a, b in zip(ts, ts[1:]) if real[a][3] > 0 and real[b][3] > 0]
        sd = (sum(r * r for r in rets) / len(rets)) ** 0.5 if rets else 0.01
        p, out = 1.0, {}
        for t in ts:
            out[t] = [p, p, p, p, real[t][4]]
            p *= math.exp(rng.gauss(-sd * sd / 2, sd))
        _series[chave] = out
    return _series[chave]


def funding_ou_zero(sym, t0, t1):
    return 0.0 if PASSEIO else funding(sym, t0, t1)


def com_volume(s, ts):
    k = s.get(ts)
    return k is not None and k[4] > 0


# ---------------------------------------------------------------------------
# Trades
# ---------------------------------------------------------------------------

def simbolo_perp(tk, ts):
    for sym in (f"{tk}USDT", f"1000{tk}USDT"):
        if _mes(ts) in meses_disponiveis("futures/um", sym):
            return sym
    return None


def montar(e, deslist):
    sym = simbolo_perp(e["token"], e["ts"])
    if not sym:
        return None, "sem perpetuo"
    ent = (e["ts"] // H + 2) * H
    s = serie("futures/um", sym, ent - HIST_MIN - PLACEBO_DIAS * DIA - DIA, ent + max(JANELAS) * DIA + DIA)
    if not com_volume(s, ent):
        return None, "sem candle com volume na entrada"
    if not com_volume(s, ent - HIST_MIN):
        return None, "listado ha menos de 30 dias"
    ultimo = max(t for t in s if s[t][4] > 0)
    t = {**e, "sym": sym, "entrada_ts": ent, "p_in": s[ent][0], "saidas": {}, "cortado": False}
    p_anuncio = abertura(s, e["ts"] // H * H)
    t["reacao"] = None if p_anuncio is None else -100 * (t["p_in"] / p_anuncio - 1)
    for j in JANELAS:
        sai = ent + j * DIA
        if sai > ultimo:
            sai, t["cortado"] = ultimo, True
        t["saidas"][j] = (sai, s[sai][0])
        pl_in, pl_out = abertura(s, ent - PLACEBO_DIAS * DIA), abertura(s, sai - PLACEBO_DIAS * DIA)
        t[f"placebo_bruto_{j}"] = None if (pl_in is None or pl_out is None) else -100 * (pl_out / pl_in - 1)
    t["deslist_na_janela"] = any(ent - DIA <= d <= ent + max(JANELAS) * DIA for d in deslist.get(e["token"], []))
    return t, "ok"


def base_vendida(cands, t0, t1):
    rets = []
    for x in cands:
        s = serie("futures/um", x, t0 - DIA, t1 + DIA)
        if com_volume(s, t0) and com_volume(s, t1):
            rets.append(-100 * (s[t1][0] / s[t0][0] - 1))
    return sum(rets) / len(rets) if rets else None


def medir(trades):
    por_anuncio = defaultdict(list)
    for t in trades:
        por_anuncio[t["ts"]].append(t)
    for ts, grupo in por_anuncio.items():
        ent = grupo[0]["entrada_ts"]
        cands = candidatos_base(ent, ent + max(JANELAS) * DIA, {t["sym"] for t in grupo})
        rng = random.Random(ts)
        sorteio = rng.sample(cands, min(N_XS, len(cands)))
        for t in grupo:
            t["n_base"] = len(sorteio)
            for j in JANELAS:
                sai, p_out = t["saidas"][j]
                bruto = -100 * (p_out / t["p_in"] - 1)
                f = 100 * funding_ou_zero(t["sym"], ent, sai)
                b = base_vendida(sorteio, ent, sai)
                t[f"bruto_{j}"] = bruto
                t[f"funding_{j}"] = f
                t[f"abs_{j}"] = bruto - 100 * CUSTO_RT + f
                t[f"abs05_{j}"] = bruto - 0.5 + f
                t[f"abs10_{j}"] = bruto - 1.0 + f
                t[f"excesso_{j}"] = None if b is None else bruto - b
                pb = t[f"placebo_bruto_{j}"]
                bp = base_vendida(sorteio, ent - PLACEBO_DIAS * DIA, sai - PLACEBO_DIAS * DIA) if pb is not None else None
                t[f"placebo_excesso_{j}"] = None if (pb is None or bp is None) else pb - bp


def spot_descritivo(e):
    sym = f"{e['token']}USDT"
    if _mes(e["ts"]) not in meses_disponiveis("spot", sym):
        return None
    ent = (e["ts"] // H + 2) * H
    s = serie("spot", sym, ent - DIA, ent + max(JANELAS) * DIA + DIA)
    p_in = abertura(s, ent)
    if p_in is None:
        return None
    out = {"ts": e["ts"]}
    for j in JANELAS:
        p = abertura(s, ent + j * DIA)
        out[f"deriva_{j}"] = None if p is None else 100 * (p / p_in - 1)
    return out


# ---------------------------------------------------------------------------
# Estatistica
# ---------------------------------------------------------------------------

def boot(itens, chave, conf=CONF):
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
    a = (1 - conf) / 2
    return media, ms[int(a * N_RESAMPLES)], ms[int((1 - a) * N_RESAMPLES) - 1], n, len(grupos)


def linha(rot, itens, chave, conf=CONF):
    r = boot(itens, chave, conf)
    if r is None:
        return f"  {rot:<44} (insuficiente)", None
    m, lo, hi, n, g = r
    return (f"  {rot:<44} n={n:>4} anuncios={g:>3} media {m:+7.2f}% "
            f"IC{100*conf:g} [{lo:+7.2f}, {hi:+7.2f}]"), lo


# ---------------------------------------------------------------------------

def main(argv):
    global PASSEIO, SEMENTE_PASSEIO
    t0 = time.time()
    PASSEIO = "--passeio" in argv
    if "--semente" in argv:
        SEMENTE_PASSEIO = int(argv[argv.index("--semente") + 1])
    if "--baixar-anuncios" in argv:
        baixar_anuncios()
    evs = eventos()
    print(f"Eventos (token x anuncio), sem stablecoins e sem repeticao: {len(evs)} em "
          f"{len({e['ts'] for e in evs})} anuncios")
    deslist = deslistagens()
    trades, motivos = [], defaultdict(int)
    for e in evs:
        t, motivo = montar(e, deslist)
        motivos[motivo] += 1
        if t:
            trades.append(t)
    print("Montagem:", dict(motivos))
    print(f"Trades validos: {len(trades)} em {len({t['ts'] for t in trades})} anuncios | "
          f"perpetuo acabou antes da saida: {sum(t['cortado'] for t in trades)} | "
          f"deslistagem anunciada na janela: {sum(t['deslist_na_janela'] for t in trades)}")
    if "--contar" in argv:
        por = defaultdict(list)
        for t in trades:
            por[t["ts"]].append(t["sym"])
        for ts in sorted({e["ts"] for e in evs}):
            print(f"    {datetime.fromtimestamp(ts/1000, timezone.utc):%Y-%m-%d %H:%M}  "
                  f"{len(por.get(ts, [])):>2} com perp: {' '.join(por.get(ts, []))}")
        return

    medir(trades)
    if PASSEIO:
        print("\n*** PASSEIO ALEATORIO (validacao): precos sinteticos sem deriva, funding zero ***")

    decisao_lo = {}
    for j in JANELAS:
        print("\n" + "=" * 104 + f"\nJANELA 0 -> +{j} DIAS, VENDIDO (positivo = vendido ganhou)\n" + "=" * 104)
        for chave, rot in ((f"bruto_{j}", "bruto"), (f"funding_{j}", "funding recebido"),
                           (f"abs_{j}", "ABSOLUTO, custo 0.18% (decide)"),
                           (f"excesso_{j}", "EXCESSO sobre a base (decide)"),
                           (f"abs05_{j}", "absoluto, custo 0.5%"), (f"abs10_{j}", "absoluto, custo 1.0%"),
                           (f"placebo_bruto_{j}", "PLACEBO -30d: bruto"),
                           (f"placebo_excesso_{j}", "PLACEBO -30d: excesso")):
            txt, lo = linha(rot, trades, chave)
            print(txt)
            if chave in (f"abs_{j}", f"excesso_{j}"):
                decisao_lo[chave] = lo
        sem_d = [t for t in trades if not t["deslist_na_janela"]]
        print(linha("excesso, sem deslistagem na janela", sem_d, f"excesso_{j}")[0])
        print(linha("excesso, anuncios 2023-24", [t for t in trades if t["ts"] < 1735689600000], f"excesso_{j}", 0.95)[0])
        print(linha("excesso, anuncios 2025-26", [t for t in trades if t["ts"] >= 1735689600000], f"excesso_{j}", 0.95)[0])
    print()
    print(linha("reacao perdida (anuncio -> entrada)", trades, "reacao", 0.95)[0])

    sp = [s for s in (spot_descritivo(e) for e in evs) if s]
    print("\n" + "=" * 104 + "\nSPOT, todos os tokens com par USDT (descritivo; positivo = preco SUBIU)\n" + "=" * 104)
    for j in JANELAS:
        print(linha(f"deriva entrada -> +{j} d", sp, f"deriva_{j}", 0.95)[0])

    print("\n  Por trade:")
    for t in trades:
        print(f"    {datetime.fromtimestamp(t['ts']/1000, timezone.utc):%Y-%m-%d} {t['sym']:<14} base={t['n_base']:>2} "
              f"| reacao {t['reacao'] if t['reacao'] is not None else float('nan'):+6.1f}% "
              + " ".join(f"| +{j}d bruto {t[f'bruto_{j}']:+6.1f}% exc "
                         f"{t[f'excesso_{j}'] if t[f'excesso_{j}'] is not None else float('nan'):+6.1f}% "
                         f"fund {t[f'funding_{j}']:+5.2f}%" for j in JANELAS)
              + (" [deslist]" if t["deslist_na_janela"] else "") + (" [cortado]" if t["cortado"] else ""))

    n_anuncios = len({t["ts"] for t in trades})
    if n_anuncios < MIN_ANUNCIOS:
        decisao = f"SEM AMOSTRA PARA DECIDIR ({n_anuncios} anuncios < {MIN_ANUNCIOS})"
    else:
        passa = [j for j in JANELAS
                 if all(decisao_lo.get(k) is not None and decisao_lo[k] > 0 for k in (f"abs_{j}", f"excesso_{j}"))]
        decisao = f"PASSA (janela {passa})" if passa else "NAO PASSA"
    print(f"\n  DECISAO{' (PASSEIO)' if PASSEIO else ''}: {decisao}\n  [{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main(sys.argv[1:])
