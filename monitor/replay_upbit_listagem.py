"""
Estudo 41 -- comprar o perpetuo da Binance logo depois que a Upbit anuncia a
listagem de um token que ja negocia ha tempo. PRE-REGISTRADO em 05/10/2026,
antes de olhar qualquer preco.

POR QUE
-------
O estudo 38 mostrou que o dinheiro dos anuncios esta nos primeiros minutos;
o monitor horario chega tarde. Antes de pensar em servidor de execucao
rapida, testar no historico um evento que nunca foi usado aqui: o "efeito
Upbit" (listagem nova na maior corretora coreana costuma disparar o preco do
token no mundo todo em minutos). Se nao aparecer nem no historico com 1 min de
latencia, a ideia do servidor morre aqui.

EVENTOS
-------
- Feed publico da Upbit (cache_anuncios/upbit_trade.json, mesmo do estudo 39).
- Evento = cada "(TKR)" num titulo com "신규 거래지원" (novo suporte de
  negociacao). Mesmo token listado de novo: vale o 1o anuncio.
- Braco PRINCIPAL (decide): titulo inclui o mercado "KRW" (o que move preco).
  Braco descritivo: listagem so em BTC/USDT.
- Operavel: perpetuo USDT-M da Binance (TKRUSDT ou 1000TKRUSDT) com candle de
  1h com volume na hora do anuncio e 30 dias antes -- o token ja negociava;
  a alta tem de vir da noticia da Upbit, nao de um contrato novo.
- Fora: token com anuncio da Binance (catalogo 48, listagem) entre 2 dias antes
  e 1 dia depois.
- Horario: `listed_at` (com fuso).

REGRA (comprado no perpetuo)
----------------------------
- Entrada: abertura do minuto floor(anuncio) + 1 (0-60 s depois; o que um
  servidor que consulta a Upbit a cada poucos segundos alcanca).
- Saida: abertura do minuto floor(anuncio) + H, H em {15, 60, 240} minutos.
- Sem stop.

MEDIDAS (% do nocional, positivo = comprado ganhou)
---------------------------------------------------
- `liq` = bruto - 0.5% (slippage de noticia) - funding pago pelo comprado.
- `excesso` = bruto - retorno de comprar o BTCUSDT nos mesmos minutos.
- Bootstrap por ANUNCIO, 5000 reamostragens.

CRITERIO
--------
PASSA se, em algum H, `liq` E `excesso` tiverem IC 98.33% (Bonferroni, 3
horizontes) inteiro acima de zero E a media de `liq` sem os 3 maiores trades
continuar > 0 (protecao contra media puxada por poucos trades enormes, a
fragilidade vista na listagem da Binance no estudo 38).
Com menos de 15 anuncios com trade no braco principal: SEM AMOSTRA.

DESCRITIVOS
-----------
- Entrada com 2, 5 e 15 min de latencia; custo de 1.0%.
- Total (abertura do minuto do anuncio -> saida) e mediana.
- PRE-MOVIMENTO: abertura de -15 min -> minuto do anuncio. Se o preco ja subiu
  antes, o `listed_at` esta atrasado ou houve vazamento; o resultado fica suspeito.
- Braco so BTC/USDT; recorte 2025-26.

Uso (de dentro de monitor/):
    python replay_upbit_listagem.py --contar
    python replay_upbit_listagem.py
"""

import json
import os
import re
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone

import replay_deslistagem as D
import replay_latencia as RL
import replay_upbit_alerta as UA
from replay_deslistagem import DIA, H

MIN = 60_000
LATENCIAS = (1, 2, 5, 15)
HORIZONTES = (15, 60, 240)
CUSTO = 0.5
CONF = 1 - 0.05 / 3
MIN_ANUNCIOS = 15


def listagens_binance():
    out = defaultdict(list)
    fp = os.path.join(D.DIR_ANUNCIOS, "cat48.json")
    if os.path.exists(fp):
        for a in json.load(open(fp, encoding="utf-8")):
            for tk in re.findall(r"\(([A-Z0-9]{2,12})\)", a["title"]):
                out[tk].append(a["releaseDate"])
    return out


def eventos():
    with open(UA.ARQ, encoding="utf-8") as f:
        notas = sorted(json.load(f), key=lambda n: n["listed_at"])
    bn = listagens_binance()
    out, vistos, motivos = [], set(), defaultdict(int)
    for n in notas:
        t = n["title"]
        if "신규 거래지원" not in t:
            continue
        ts = int(datetime.fromisoformat(n["listed_at"]).timestamp() * 1000)
        krw = "KRW" in t
        for tk in re.findall(r"\(([A-Z0-9]{1,12})\)", t):
            if tk in UA.EXCLUIDOS or tk in vistos or tk in ("KRW", "BTC", "USDT"):
                continue
            vistos.add(tk)
            if any(ts - 2 * DIA <= b <= ts + DIA for b in bn.get(tk, [])):
                motivos["listagem da Binance colada"] += 1
                continue
            out.append({"token": tk, "ts": ts, "krw": krw, "titulo": t})
    return out, motivos


def montar(e):
    sym, _ = D.simbolo_perp(e["token"], e["ts"])
    if not sym:
        return None, "sem perpetuo"
    s1h = D.klines("futures/um", sym, e["ts"] - 31 * DIA, e["ts"] + H)
    hh = e["ts"] // H * H
    if s1h.get(hh, [0] * 5)[4] == 0 or s1h.get(hh - 30 * DIA, [0] * 5)[4] == 0:
        return None, "sem volume ou listado ha menos de 30 dias"
    b = e["ts"] // MIN * MIN
    s = RL.serie_1m(sym, b - 16 * MIN, b + max(HORIZONTES) * MIN + MIN)
    bt = RL.serie_1m("BTCUSDT", b - 16 * MIN, b + max(HORIZONTES) * MIN + MIN)
    p0, p_pre = s.get(b), s.get(b - 15 * MIN)
    if p0 is None or s.get(b + MIN) is None:
        return None, "sem candle de 1m"
    t = {**e, "sym": sym, "pre": None if p_pre is None else 100 * (p0 / p_pre - 1)}
    for h in HORIZONTES:
        sai = b + h * MIN
        p_out, b_out = s.get(sai), bt.get(sai)
        if p_out is None or b_out is None:
            continue
        t[f"total_{h}"] = 100 * (p_out / p0 - 1)
        f = None
        for k in LATENCIAS:
            if k >= h:
                continue
            p_in, b_in = s.get(b + k * MIN), bt.get(b + k * MIN)
            if p_in is None or b_in is None:
                continue
            if f is None:
                f = 100 * D.funding(sym, b + MIN, sai)   # pago pelo comprado se positivo
            bruto = 100 * (p_out / p_in - 1)
            t[f"liq_{k}_{h}"] = bruto - CUSTO - f
            t[f"liq10_{k}_{h}"] = bruto - 1.0 - f
            t[f"exc_{k}_{h}"] = bruto - 100 * (b_out / b_in - 1)
    return t, "ok"


def sem_top3(itens, chave):
    v = sorted(x[chave] for x in itens if x.get(chave) is not None)
    return sum(v[:-3]) / len(v[:-3]) if len(v) > 3 else None


def linha(rot, itens, chave, conf=CONF):
    # RL.boot devolve IC95; aqui o IC e recalculado no nivel pedido
    from collections import defaultdict as dd
    import random
    g = dd(list)
    for x in itens:
        if x.get(chave) is not None:
            g[x["ts"]].append(x[chave])
    grupos = list(g.values())
    if len(grupos) < 5:
        return f"    {rot:<36} (insuficiente)", None
    n = sum(len(v) for v in grupos)
    media = sum(sum(v) for v in grupos) / n
    rng = random.Random(42)
    ms = []
    for _ in range(5000):
        s_ = k_ = 0
        for _ in range(len(grupos)):
            v = grupos[rng.randrange(len(grupos))]
            s_ += sum(v)
            k_ += len(v)
        ms.append(s_ / k_)
    ms.sort()
    a = (1 - conf) / 2
    lo, hi = ms[int(a * 5000)], ms[int((1 - a) * 5000) - 1]
    vals = sorted(x for v in grupos for x in v)
    return (f"    {rot:<36} n={n:>4} an={len(grupos):>3} media {media:+7.2f}% IC{100*conf:.4g} "
            f"[{lo:+7.2f}, {hi:+7.2f}] mediana {vals[len(vals)//2]:+6.2f}%"), lo


def main(argv):
    t0 = time.time()
    evs, mot = eventos()
    print(f"Listagens na Upbit (token, 1o anuncio): {len(evs)} | fora por listagem da Binance colada: "
          f"{mot.get('listagem da Binance colada', 0)}")
    trades, motivos = [], defaultdict(int)
    for e in evs:
        t, m = montar(e)
        motivos[(m, e["krw"])] += 1
        if t:
            trades.append(t)
    print("Montagem (motivo, KRW?):", dict(motivos))
    princ = [t for t in trades if t["krw"]]
    outros = [t for t in trades if not t["krw"]]
    n_an = len({t["ts"] for t in princ})
    print(f"Trades validos: principal (KRW) {len(princ)} em {n_an} anuncios | so BTC/USDT {len(outros)}")
    if "--contar" in argv:
        anos = defaultdict(int)
        for t in princ:
            anos[datetime.fromtimestamp(t["ts"] / 1000, timezone.utc).year] += 1
        print("Principal por ano:", dict(sorted(anos.items())))
        return

    passa = []
    for nome, grupo in (("PRINCIPAL: listagem com mercado KRW", princ), ("DESCRITIVO: so BTC/USDT", outros)):
        print("\n" + "=" * 110 + f"\n{nome} (comprado; positivo = comprado ganhou)\n" + "=" * 110)
        print(linha("pre-movimento (-15 min -> anuncio)", grupo, "pre", 0.95)[0])
        for h in HORIZONTES:
            print(f"\n  Saida em {h} min:")
            print(linha("total (anuncio -> saida, sem custo)", grupo, f"total_{h}", 0.95)[0])
            for k in LATENCIAS:
                if k >= h:
                    continue
                dec = grupo is princ and k == 1
                tl, lo_l = linha(f"+{k} min: LIQUIDO custo 0.5%{' (decide)' if dec else ''}", grupo, f"liq_{k}_{h}",
                                 CONF if dec else 0.95)
                te, lo_e = linha(f"+{k} min: EXCESSO s/ BTC{' (decide)' if dec else ''}", grupo, f"exc_{k}_{h}",
                                 CONF if dec else 0.95)
                print(tl)
                print(te)
                if k == 1:
                    print(linha(f"+{k} min: liquido, custo 1.0%", grupo, f"liq10_{k}_{h}", 0.95)[0])
                    st = sem_top3(grupo, f"liq_{k}_{h}")
                    print(f"    {'+1 min: liquido sem os 3 maiores':<36} "
                          f"{'—' if st is None else f'{st:+7.2f}%'}")
                if dec and lo_l is not None and lo_e is not None and lo_l > 0 and lo_e > 0 \
                        and (sem_top3(grupo, f"liq_{k}_{h}") or -1) > 0:
                    passa.append(h)
        if grupo is princ:
            rec = [t for t in grupo if t["ts"] >= 1735689600000]
            print("\n" + linha("+1 min, saida 60 min, liquido, so 2025-26", rec, "liq_1_60", 0.95)[0])

    if n_an < MIN_ANUNCIOS:
        dec = f"SEM AMOSTRA PARA DECIDIR ({n_an} < {MIN_ANUNCIOS} anuncios)"
    else:
        dec = f"PASSA (saida em {passa} min)" if passa else "NAO PASSA"
    print(f"\n  DECISAO: {dec}\n  [{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main(sys.argv[1:])
