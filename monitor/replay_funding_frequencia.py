"""
Estudo 95 (funding liquidado com mais frequencia). PRE-REGISTRADO em 24/11/2026,
antes de olhar qualquer preco. Tentativa unica.

Hipotese: a Binance aumenta a frequencia do funding (8h -> 4h/1h) quando a taxa
bate no teto, ou seja, um lado esta lotado. A partir dai esse lado paga com mais
frequencia, e a posicao lotada tende a ser desmontada: operar CONTRA o lado que
paga.

EVENTOS
- cat49.json, titulos com "Settlement Frequency", SEM "Resum" (volta ao normal).
- Contratos: todos os XXXUSDT citados no corpo do anuncio. Um evento por
  contrato e anuncio; mesmo contrato em menos de 7 dias: o primeiro.

OPERACAO (perpetuo, candles 1h, sem stop)
- Entrada: abertura da hora (anuncio arredondado para cima) + 1h.
- Lado: soma do funding das 24h antes da entrada > 0 (comprado paga) -> VENDE;
  < 0 -> COMPRA; = 0 -> fora.
- Saida: entrada + 3 dias.
- liq = lado*ret - 0.18% - lado*funding (o que o lado paga);
  excesso = lado*(ret - retorno da cesta de 20 majors).
- Bootstrap por anuncio, IC95. PASSA se liq E excesso com IC95 > 0.
  Menos de 20 anuncios: SEM AMOSTRA.
- Descritivos: so vendidos / so comprados; saida em 1 e 7 dias; por ano;
  placebo 30 dias antes com o mesmo lado.
"""

import json
import os
import re
from datetime import datetime, timezone

import replay_deslistagem as D
from replay_corte_alavancagem import linha
import launchpool_paper as LP

H, DIA = 3_600_000, 86_400_000
CUSTO = 0.18
ARQ = os.path.join(D.DIR_ANUNCIOS, "funding_freq_corpos.json")


def eventos():
    a = json.load(open(os.path.join(D.DIR_ANUNCIOS, "cat49.json"), encoding="utf-8"))
    a = sorted((x for x in a if "settlement frequency" in x["title"].lower() and "resum" not in x["title"].lower()),
               key=lambda x: x["releaseDate"])
    c = json.load(open(ARQ, encoding="utf-8")) if os.path.exists(ARQ) else {}
    import time
    ev, ult = [], {}
    for x in a:
        if not c.get(x["code"]):
            for tent in range(4):
                t, _ = LP.corpo(x["code"])
                if t:
                    break
                time.sleep(20 * (tent + 1))
            c[x["code"]] = t
            json.dump(c, open(ARQ, "w", encoding="utf-8"), ensure_ascii=False)
            time.sleep(1.5)
        for sym in dict.fromkeys(re.findall(r"\b([A-Z0-9]{2,}USDT)\b", c[x["code"]] or "")):
            if sym in ult and x["releaseDate"] - ult[sym] < 7 * DIA:
                continue
            ult[sym] = x["releaseDate"]
            ev.append({"ts": x["releaseDate"], "sym": sym})
    return ev


def medir(e, cache, desloc=0, lado=None):
    ent = (e["ts"] // H + 2) * H - desloc
    s = D.klines("futures/um", e["sym"], ent - DIA, ent + 8 * DIA)
    if lado is None:
        f0 = D.funding(e["sym"], ent - DIA, ent)
        if f0 == 0:
            return None
        lado = -1 if f0 > 0 else 1
    a = D.abertura(s, ent)
    if not a:
        return None
    r = {"lado": lado}
    for nome, dias in (("", 3), ("_1d", 1), ("_7d", 7)):
        sai = ent + dias * DIA
        b = D.abertura(s, sai)
        c = D.cesta(ent, sai, cache)
        if not b:
            r["liq" + nome] = r["exc" + nome] = None
            continue
        ret = 100 * (b / a - 1)
        r["liq" + nome] = lado * ret - CUSTO - lado * 100 * D.funding(e["sym"], ent, sai)
        r["exc" + nome] = None if c is None else lado * (ret + c)   # cesta() = retorno de VENDER a cesta
    return r


def main():
    evs = eventos()
    print(f"Contrato-eventos: {len(evs)} em {len({e['ts'] for e in evs})} anuncios")
    cache, tr = {}, []
    for e in evs:
        r = medir(e, cache)
        if r and r["liq"] is not None:
            p = medir(e, cache, 30 * DIA, r["lado"])
            tr.append({**e, **r, "placebo": p["liq"] if p else None})
    print(f"Medidos: {len(tr)} (vendidos {sum(t['lado'] < 0 for t in tr)})\n")
    l1, lo1, g1 = linha("DECIDE liq 3d", tr, "liq")
    l2, lo2, _ = linha("DECIDE excesso 3d", tr, "exc")
    print(l1); print(l2); print("\n  descritivos:")
    print(linha("so vendidos (funding > 0)", [t for t in tr if t["lado"] < 0], "liq")[0])
    print(linha("so comprados (funding < 0)", [t for t in tr if t["lado"] > 0], "liq")[0])
    for k in ("_1d", "_7d"):
        print(linha(f"liq saida {k[1:]}", tr, "liq" + k)[0])
        print(linha(f"exc saida {k[1:]}", tr, "exc" + k)[0])
    print(linha("placebo -30d (mesmo lado)", tr, "placebo")[0])
    ano = lambda t: datetime.fromtimestamp(t["ts"] / 1000, timezone.utc).year
    for y in sorted({ano(t) for t in tr}):
        print(linha(f"liq {y}", [t for t in tr if ano(t) == y], "liq")[0])
    print("\nDECISAO:", "SEM AMOSTRA" if g1 < 20 else ("PASSA" if lo1 > 0 and lo2 > 0 else "NAO PASSA"))
    json.dump(tr, open(os.path.join(D.DIR_ANUNCIOS, "estudo95_trades.json"), "w"))


if __name__ == "__main__":
    main()
