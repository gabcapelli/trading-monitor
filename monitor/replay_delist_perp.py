"""
Estudo 89 (24/11/2026) -- vender o perpetuo depois que a Binance anuncia que vai
retirar SO o perpetuo USDT-M. PRE-REGISTRADO antes de calcular retorno.

MECANISMO: quem esta comprado no perpetuo precisa fechar ate a data (liquidacao
forcada no fim), sem migrar para outro contrato da Binance. Diferente do estudo 28
(retirada do spot, venda opcional de quem tem o token).

EVENTOS: catalogo 161, titulo "Binance Futures Will Delist ... Perpetual" (e
"Will Delist and Update the Leverage..."), contratos XXXUSDT citados no titulo ou
no corpo. Fora: contratos BUSD (migracao de moeda), COIN-M, e tokens com retirada
do spot anunciada (eventos do estudo 28) a +-7 dias do aviso.

REGRA: vende na abertura da 2a hora cheia apos o aviso (igual ao 28); recompra na
abertura da hora que fica 2h antes do fim do perpetuo (ultimo candle + 1h).
Sem stop nem alvo. Custo 0.18% (descritivo com 0.5% e 1%), funding real.
Excesso = bruto - venda da cesta dos majors nas mesmas horas.
CRITERIO: abs E excesso com IC95 > 0 (bootstrap por anuncio); < 20 anuncios = SEM
AMOSTRA. Lembrete do 37: com cauda gorda o IC e otimista.
Descritivos: placebo -30 dias; saida 24h antes do fim; caminho (pior alta contra).
"""
import json, os, re, sys, time, urllib.request
from collections import defaultdict
import replay_deslistagem as D

ARQ = os.path.join(D.DIR_ANUNCIOS, "delist_perp_corpos.json")
URL = "https://www.binance.com/bapi/composite/v1/public/cms/article/detail/query?articleCode="

def anuncios():
    arts = json.load(open(os.path.join(D.DIR_ANUNCIOS, "cat161.json")))
    arts = [a for a in arts if re.search(r"Futures.*Delist|Delisting of USD", a["title"]) and "Perpetual" in a["title"]
            and not re.search(r"Postponed|COIN-M [A-Z]", a["title"]) or (re.search(r"Futures.*Delist", a["title"]) and "Multiple" in a["title"])]
    cache = json.load(open(ARQ)) if os.path.exists(ARQ) else {}
    for a in arts:
        if a["code"] in cache:
            continue
        for t in range(8):
            try:
                raw = urllib.request.urlopen(urllib.request.Request(URL + a["code"], headers={"User-Agent": "Mozilla/5.0"}), timeout=30).read()
                break
            except Exception:
                time.sleep(20 * (t + 1))
        cache[a["code"]] = (json.loads(raw)["data"] or {}).get("body") or ""
        json.dump(cache, open(ARQ, "w"))
        time.sleep(2)
    return arts, cache

def eventos():
    arts, corpos = anuncios()
    spot = defaultdict(list)
    for e in D.eventos():
        spot[e["token"]].append(e["ts"])
    out, fora = [], defaultdict(int)
    for a in arts:
        txt = a["title"] + " " + re.sub(r"<[^>]+>", " ", corpos.get(a["code"], ""))
        syms = dict.fromkeys(re.findall(r"\b((?:1000)?[A-Z0-9]{2,15}USDT)\b", txt))
        for s in syms:
            tk = re.sub(r"^1000", "", s[:-4])
            if any(abs(a["releaseDate"] - x) <= 7 * D.DIA for x in spot.get(tk, [])):
                fora["spot junto"] += 1; continue
            out.append({"token": tk, "sym": s, "ts": a["releaseDate"], "titulo": a["title"]})
    return out, fora

def caminho(serie, t0, t1):
    p0 = serie[t0][0]
    return max(serie[t][1] / p0 - 1 for t in serie if t0 <= t < t1)

def trade(e, horas_antes):
    meses = D.meses_disponiveis("futures/um", e["sym"])
    if not meses:
        return None, "sem perpetuo"
    serie = D.klines("futures/um", e["sym"], e["ts"] - 40 * D.DIA, e["ts"] + 60 * D.DIA)
    serie = {t: k for t, k in serie.items() if k[4] > 0} if serie and len(next(iter(serie.values()))) > 4 else serie
    if not serie or max(serie) < e["ts"]:
        return None, "sem candles depois do aviso"
    fim = max(serie) + D.H
    ent, sai = (e["ts"] // D.H + 2) * D.H, fim - horas_antes * D.H
    if sai <= ent or ent not in serie or sai not in serie:
        return None, "saida antes da entrada / sem candle"
    p_in, p_out = serie[ent][0], serie[sai][0]
    t = {**e, "ent": ent, "sai": sai, "dur_h": (sai - ent) / D.H, "bruto": -100 * (p_out / p_in - 1),
         "contra": 100 * caminho(serie, ent, sai), "reacao": -100 * (p_in / serie[e["ts"] // D.H * D.H][0] - 1) if e["ts"] // D.H * D.H in serie else None}
    a, b = serie.get(ent - 30 * D.DIA), serie.get(sai - 30 * D.DIA)
    t["placebo"] = -100 * (b[0] / a[0] - 1) if a and b else None
    return t, "ok"

def main(argv):
    evs, fora = eventos()
    print(f"eventos {len(evs)} em {len({e['ts'] for e in evs})} anuncios | fora: {dict(fora)}")
    cache = {}
    for h in (2, 24):
        tr, mot = [], defaultdict(int)
        for e in evs:
            t, m = trade(e, h); mot[m] += 1
            if t: tr.append(t)
        for t in tr:
            c = D.cesta(t["ent"], t["sai"], cache)
            t["excesso"] = None if c is None else t["bruto"] - c
            f = 100 * D.funding(t["sym"], t["ent"], t["sai"])
            t["abs"], t["abs05"], t["abs1"] = t["bruto"] - 0.18 + f, t["bruto"] - 0.5 + f, t["bruto"] - 1 + f
            t["fund"] = f
        print(f"\n== saida {h}h antes do fim | trades {len(tr)} em {len({t['ts'] for t in tr})} anuncios | {dict(mot)}")
        for k in ("abs", "excesso", "abs05", "abs1", "placebo", "reacao"):
            print(D.linha(k, tr, k)[0])
        if h == 2:
            for t in sorted(tr, key=lambda t: t["ts"]):
                print(f"   {time.strftime('%Y-%m-%d', time.gmtime(t['ts']/1000))} {t['sym']:<16}{t['dur_h']:6.0f}h abs {t['abs']:+7.1f}% exc {t['excesso'] if t['excesso'] is None else round(t['excesso'],1)!s:>7} contra max {t['contra']:+6.1f}% fund {t['fund']:+5.1f}")
            med = sorted(t["abs"] for t in tr); print("   mediana abs", med[len(med)//2], "positivos", sum(x > 0 for x in med), "/", len(med))

if __name__ == "__main__":
    main(sys.argv)
