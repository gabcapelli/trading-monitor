"""
Estudo 94 (corte de alavancagem maxima no perpetuo). PRE-REGISTRADO em 24/11/2026,
antes de olhar qualquer preco. Tentativa unica.

Hipotese: quando a Binance reduz a alavancagem maxima de um contrato, quem esta
acima do novo limite precisa reduzir a posicao (ou e liquidado) no horario
efetivo. Alavancagem alta em altcoin e majoritariamente comprada: pressao
vendedora do anuncio ate o horario efetivo.

EVENTOS
- cat49.json, titulos com "Leverage" (Leverage & Margin Tiers).
- Corpo do anuncio (cache em cache_anuncios/alavancagem_corpos.json).
- Por contrato XXXUSDT: alavancagem maxima ANTES = primeira faixa da tabela;
  DEPOIS = faixa na linha da segunda ocorrencia de "0 < Position" (primeira
  linha da tabela nova). CORTE = depois < antes (tratamento); IGUAL OU MAIOR =
  controle (descritivo).
- Horario efetivo: "AAAA-MM-DD HH:MM (UTC): ... XXX" na linha que cita o
  contrato; sem isso, a primeira data com hora do corpo.
- Um evento por contrato por anuncio; so USDT-M; contrato e anuncio repetido
  em menos de 7 dias: fica o primeiro.

OPERACAO (perpetuo, VENDIDO, sem stop, candles de 1h)
- Entrada: abertura da hora (anuncio arredondado para cima) + 1h.
- Saida: abertura da hora do horario efetivo (arredondado para baixo).
  Menos de 1h entre entrada e saida: fora.
- liq = -ret - 0.18% + funding recebido; excesso = -ret - (vender 20 majors).
- Bootstrap por ANUNCIO (contratos do mesmo anuncio no mesmo bloco), IC95.
- PASSA se liq E excesso com IC95 > 0. Menos de 30 anuncios: SEM AMOSTRA.
- DESCRITIVOS: controle (sem corte); saida 24h depois do efetivo; corte de
  50% ou mais; por ano; placebo 30 dias antes.
"""

import json
import os
import random
import re
from collections import defaultdict
from datetime import datetime, timezone

import launchpool_paper as LP
import replay_deslistagem as D

H, DIA = 3_600_000, 86_400_000
CUSTO = 0.18
ARQ = os.path.join(D.DIR_ANUNCIOS, "alavancagem_corpos.json")
RE_LEV = re.compile(r"^\s*(?:(\d+)\s*-\s*)?(\d+)x\s*$")
RE_DT = re.compile(r"(\d{4})-(\d{2})-(\d{2})\s+(\d{2}):(\d{2})\s*\(UTC\)")


def anuncios():
    a = json.load(open(os.path.join(D.DIR_ANUNCIOS, "cat49.json"), encoding="utf-8"))
    return sorted((x for x in a if "leverage" in x["title"].lower() and "margin" in x["title"].lower()),
                  key=lambda x: x["releaseDate"])


def corpos():
    c = json.load(open(ARQ, encoding="utf-8")) if os.path.exists(ARQ) else {}
    import time
    for a in anuncios():
        if c.get(a["code"]):
            continue
        for tent in range(4):
            t, _ = LP.corpo(a["code"])
            if t:
                break
            time.sleep(20 * (tent + 1))
        c[a["code"]] = t
        json.dump(c, open(ARQ, "w", encoding="utf-8"), ensure_ascii=False)
        time.sleep(1.5)
    return c


def _dt(m):
    a, mo, d, h, mi = map(int, m.groups())
    return int(datetime(a, mo, d, h, mi, tzinfo=timezone.utc).timestamp() * 1000)


def contratos(texto):
    """[(sym, lev_antes, lev_depois, efetivo_ts)]"""
    out = []
    partes = re.split(r"\n[^\n]*?\b([A-Z0-9]+USDT)\s*\(USD.-M Perpetual Contract\)\s*\n", texto)
    linhas_data = [(l, RE_DT.search(l)) for l in texto.split("\n") if RE_DT.search(l)]
    padrao = _dt(linhas_data[0][1]) if linhas_data else None
    for i in range(1, len(partes) - 1, 2):
        sym, bloco = partes[i], partes[i + 1]
        ls = [l.strip() for l in bloco.split("\n") if l.strip()]
        levs = [(j, int(RE_LEV.match(l).group(2))) for j, l in enumerate(ls) if RE_LEV.match(l)]
        zeros = [j for j, l in enumerate(ls) if l.startswith("0 < Position")]
        if not levs or len(zeros) < 2:
            continue
        antes = levs[0][1]
        prev = [v for j, v in levs if j < zeros[1]]
        depois = prev[-1] if prev else None
        if depois is None:
            continue
        ef = None
        for l, m in linhas_data:
            if sym in l or sym.replace("USDT", "") + "USDT" in l.replace(" ", ""):
                ef = _dt(m)
                break
        out.append((sym, antes, depois, ef or padrao))
    return out


def eventos():
    c = corpos()
    ev, ult = [], {}
    for a in anuncios():
        t = c.get(a["code"])
        if not t:
            continue
        for sym, antes, depois, ef in contratos(t):
            if ef is None or (sym in ult and a["releaseDate"] - ult[sym] < 7 * DIA):
                continue
            ult[sym] = a["releaseDate"]
            ev.append({"ts": a["releaseDate"], "sym": sym, "antes": antes, "depois": depois, "efetivo": ef,
                       "corte": depois < antes})
    return ev


def medir(e, cache, desloc=0):
    ent = (e["ts"] // H + 1) * H + H - desloc
    sai = e["efetivo"] // H * H - desloc
    if sai - ent < H:
        return None
    serie = D.klines("futures/um", e["sym"], ent - DIA, sai + 2 * DIA)
    a, b, b24 = D.abertura(serie, ent), D.abertura(serie, sai), D.abertura(serie, sai + DIA)
    if not a or not b:
        return None
    bruto = -100 * (b / a - 1)
    c = D.cesta(ent, sai, cache)
    r = {"liq": bruto - CUSTO + 100 * D.funding(e["sym"], ent, sai), "exc": None if c is None else bruto - c,
         "horas": (sai - ent) / H}
    if b24:
        r["liq24"] = -100 * (b24 / a - 1) - CUSTO + 100 * D.funding(e["sym"], ent, sai + DIA)
    return r


def boot(itens, chave):
    g = defaultdict(list)
    for x in itens:
        if x.get(chave) is not None:
            g[x["ts"]].append(x[chave])
    gr = list(g.values())
    if len(gr) < 3:
        return None
    rng = random.Random(42)
    ms = []
    for _ in range(5000):
        s = n = 0
        for _ in gr:
            v = gr[rng.randrange(len(gr))]
            s += sum(v); n += len(v)
        ms.append(s / n)
    ms.sort()
    n = sum(len(v) for v in gr)
    return sum(sum(v) for v in gr) / n, ms[125], ms[4874], n, len(gr)


def linha(rot, itens, chave):
    r = boot(itens, chave)
    if not r:
        return f"  {rot:<36} (insuficiente)", None, 0
    m, lo, hi, n, g = r
    return f"  {rot:<36} n={n:>4} anuncios={g:>3} media {m:+7.2f}% IC95 [{lo:+7.2f}, {hi:+7.2f}]", lo, g


def main():
    evs = eventos()
    print(f"Contratos-evento: {len(evs)} (corte {sum(e['corte'] for e in evs)}) em {len({e['ts'] for e in evs})} anuncios")
    cache, tr = {}, []
    for e in evs:
        r = medir(e, cache)
        if r:
            p = medir(e, cache, 30 * DIA)
            tr.append({**e, **r, "placebo": p["liq"] if p else None})
    trat = [t for t in tr if t["corte"]]
    hs = sorted(t["horas"] for t in trat)
    print(f"Medidos: {len(tr)} · tratamento {len(trat)} · horas ate o efetivo (mediana) {hs[len(hs)//2] if hs else '-'}\n")
    l1, lo1, g1 = linha("DECIDE liq (corte)", trat, "liq")
    l2, lo2, _ = linha("DECIDE excesso (corte)", trat, "exc")
    print(l1); print(l2); print("\n  descritivos:")
    print(linha("controle (sem corte): liq", [t for t in tr if not t["corte"]], "liq")[0])
    print(linha("controle (sem corte): excesso", [t for t in tr if not t["corte"]], "exc")[0])
    print(linha("corte: saida 24h apos efetivo", trat, "liq24")[0])
    print(linha("corte >= 50%", [t for t in trat if t["depois"] <= t["antes"] / 2], "liq")[0])
    print(linha("corte: placebo -30d", trat, "placebo")[0])
    ano = lambda t: datetime.fromtimestamp(t["ts"] / 1000, timezone.utc).year
    for y in sorted({ano(t) for t in trat}):
        print(linha(f"corte {y}", [t for t in trat if ano(t) == y], "liq")[0])
    print("\nDECISAO:", "SEM AMOSTRA" if g1 < 30 else ("PASSA" if lo1 > 0 and lo2 > 0 else "NAO PASSA"))
    json.dump(tr, open(os.path.join(D.DIR_ANUNCIOS, "estudo94_trades.json"), "w"))


if __name__ == "__main__":
    main()
