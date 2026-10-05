"""
Estudo 38 (DESCRITIVO) -- quanto do efeito dos anuncios da Binance ainda esta
disponivel com latencia de minutos, em vez da latencia horaria do workflow.
Escrito em 05/10/2026, antes de olhar qualquer candle de 1 minuto.

POR QUE
-------
Dois estudos acharam efeito real perdido so pela execucao horaria: listagem no
spot (29: o movimento acontece em < 2h) e Monitoring Tag (37: -9% entre o
anuncio e a entrada, em 80 de 85). Das tres causas recorrentes de fracasso, a
latencia e a unica que se resolve com engenharia. Antes de pensar em infra
(ouvinte de anuncios em tempo real, fora do GitHub Actions), medir se sobra
alguma coisa para quem chega em 1-15 minutos.

NATUREZA: DESCRITIVO, SEM PODER DE APROVAR
------------------------------------------
Os eventos ja foram usados nos estudos 28, 29 e 37. Nada aqui "passa". O que
este estudo decide e so se vale montar um TESTE DE PAPEL ADIANTE com execucao
rapida (o unico teste limpo que resta para essas familias).

Regra de decisao, fixada antes de rodar:
- Vale montar o papel rapido se, em ALGUMA familia, o retorno restante liquido
  com custo de 0.5% (slippage realista em noticia) entrando com 2 MINUTOS de
  latencia tiver media com IC95 > 0 em algum dos tres horizontes. 2 minutos e o
  que um ouvinte simples em servidor consegue de forma confiavel.
- Se so 1 minuto sobra: corrida de robo, a linha morre (nao da para garantir).
- Ressalva: 3 familias x 3 horizontes = 9 olhares; um unico IC95 > 0 isolado e
  fraco. O papel, se montado, e que decide.

EVENTOS (os mesmos dos estudos de origem, mesmos filtros)
---------------------------------------------------------
- listagem (29): comprado; perpetuo USDT-M existente no mes do anuncio.
- deslistagem (28): vendido.
- monitoring (37): vendido.

MEDIDAS (% do nocional, positivo = lado do estudo ganhou)
---------------------------------------------------------
- Candles de 1 minuto do perpetuo (data.binance.vision, arquivos diarios).
- p0 = abertura do minuto em que o anuncio saiu (preco antes da reacao, a
  menos de segundos).
- Entrada com latencia k em {1, 2, 5, 15, 30, 60} minutos: abertura do minuto
  floor(anuncio) + k.
- Saida em H em {60, 240, 1440} minutos apos floor(anuncio); na listagem,
  limitada a abertura do spot (a hipotese do 29 e "vende no fato").
- `total`  = p0 -> saida (o que existia).
- `resta_k` = entrada_k -> saida, menos custo (0.18% e 0.5%).
- Bootstrap por ANUNCIO, IC95, 5000 reamostragens.
- Sem excesso sobre mercado: em minutos/horas o beta pesa pouco; o papel mediria.

`--beta` (acrescentado DEPOIS de ver o resultado, 05/10/2026): excesso sobre
o BTC nas celulas que chamaram atencao, para descartar beta de mercado.

Uso (de dentro de monitor/):
    python replay_latencia.py
    python replay_latencia.py --beta
"""

import os
import random
import sys
import time
from collections import defaultdict
from datetime import datetime, timedelta, timezone

import replay_deslistagem as D
import replay_listagem as L
import replay_monitoring_tag as MT
from replay_deslistagem import _csv_zip, _get, _ms

MIN = 60_000
LATENCIAS = (1, 2, 5, 15, 30, 60)
HORIZONTES = (60, 240, 1440)
CUSTOS = (0.18, 0.5)
N_RESAMPLES = 5000
SEED = 42
DIR_1M = os.path.join(D.DIR_VISION, "1m")


def klines_1m_dia(sym, dia):
    """{ts: open} de 1 minuto num dia UTC (arquivo diario do vision, em cache)."""
    os.makedirs(DIR_1M, exist_ok=True)
    fpath = os.path.join(DIR_1M, f"{sym}_{dia:%Y-%m-%d}.csv")
    if os.path.exists(fpath):
        with open(fpath) as f:
            return {int(a): float(b) for a, b in (l.split(",") for l in f if l.strip())}
    raw = _get(f"{D.VISION}/futures/um/daily/klines/{sym}/1m/{sym}-1m-{dia:%Y-%m-%d}.zip")
    out = {_ms(r[0]): float(r[1]) for r in _csv_zip(raw)} if raw else {}
    if dia.date() < datetime.now(timezone.utc).date():
        with open(fpath, "w") as f:
            f.writelines(f"{k},{v}\n" for k, v in sorted(out.items()))
    return out


def serie_1m(sym, t0, t1):
    out = {}
    d = datetime.fromtimestamp(t0 / 1000, timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    while d.timestamp() * 1000 <= t1:
        out.update(klines_1m_dia(sym, d))
        d += timedelta(days=1)
    return out


def familias():
    evs = {}
    evs["listagem"] = (+1, [{**e, "limite": e["inicio_spot"]} for e in L.eventos()])
    evs["deslistagem"] = (-1, [{**e, "limite": None} for e in D.eventos()])
    evs["monitoring"] = (-1, [{**e, "limite": None} for e in MT.eventos()])
    return evs


def medir(sinal, e):
    sym, _ = D.simbolo_perp(e["token"], e["ts"])
    if not sym:
        return None, "sem perpetuo"
    base = e["ts"] // MIN * MIN
    s = serie_1m(sym, base - MIN, base + max(HORIZONTES) * MIN + MIN)
    p0 = s.get(base)
    if p0 is None:
        return None, "sem candle de 1m no anuncio"
    out = {"ts": e["ts"], "sym": sym}
    for h in HORIZONTES:
        sai = base + h * MIN
        if e["limite"] is not None:
            sai = min(sai, e["limite"] // MIN * MIN)
        p_out = s.get(sai)
        if p_out is None or sai <= base:
            continue
        out[f"total_{h}"] = sinal * 100 * (p_out / p0 - 1)
        for k in LATENCIAS:
            p_in = s.get(base + k * MIN)
            if p_in is None or base + k * MIN >= sai:
                continue
            bruto = sinal * 100 * (p_out / p_in - 1)
            for c in CUSTOS:
                out[f"resta_{k}_{h}_{c}"] = bruto - c
    return out, "ok"


def boot(itens, chave):
    g = defaultdict(list)
    for x in itens:
        if x.get(chave) is not None:
            g[x["ts"]].append(x[chave])
    grupos = list(g.values())
    if len(grupos) < 5:
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
    vals = sorted(v for gr in grupos for v in gr)
    return media, ms[int(0.025 * N_RESAMPLES)], ms[int(0.975 * N_RESAMPLES) - 1], n, len(grupos), vals[len(vals) // 2]


def fmt(r):
    if r is None:
        return "(insuficiente)"
    m, lo, hi, n, g, med = r
    return f"n={n:>4} an={g:>3} media {m:+7.2f}% IC95 [{lo:+7.2f}, {hi:+7.2f}] mediana {med:+6.2f}%"


def beta():
    """Excesso sobre o BTC (custo 0.5%) nas celulas que chamaram atencao."""
    for nome, sinal, evs, celulas in (("monitoring", -1, MT.eventos(), ((2, 1440), (60, 1440))),
                                      ("deslistagem", -1, D.eventos(), ((15, 240), (60, 240)))):
        for k, h in celulas:
            res = []
            for e in evs:
                sym, _ = D.simbolo_perp(e["token"], e["ts"])
                if not sym:
                    continue
                b = e["ts"] // MIN * MIN
                s, bt = (serie_1m(x, b - MIN, b + h * MIN + MIN) for x in (sym, "BTCUSDT"))
                pi, po, bi, bo = s.get(b + k * MIN), s.get(b + h * MIN), bt.get(b + k * MIN), bt.get(b + h * MIN)
                if None in (pi, po, bi, bo):
                    continue
                v, vb = sinal * 100 * (po / pi - 1), sinal * 100 * (bo / bi - 1)
                res.append({"ts": e["ts"], "bruto": v - 0.5, "exc": v - vb - 0.5, "btc": vb})
            for c in ("bruto", "exc", "btc"):
                print(f"  {nome} +{k}->{h} min {c:<6} {fmt(boot(res, c))}")


def main(argv):
    t0 = time.time()
    if "--beta" in argv:
        return beta()
    decisao = []
    for nome, (sinal, evs) in familias().items():
        res, motivos = [], defaultdict(int)
        for e in evs:
            r, m = medir(sinal, e)
            motivos[m] += 1
            if r:
                res.append(r)
        lado = "comprado" if sinal > 0 else "vendido"
        print("\n" + "=" * 110 + f"\n{nome.upper()} ({lado}) -- {dict(motivos)}\n" + "=" * 110)
        for h in HORIZONTES:
            print(f"\n  Saida em {h} min{' (ou abertura do spot)' if nome == 'listagem' else ''}:")
            print(f"    {'total (p0 -> saida, sem custo)':<38} {fmt(boot(res, f'total_{h}'))}")
            for k in LATENCIAS:
                for c in CUSTOS:
                    r = boot(res, f"resta_{k}_{h}_{c}")
                    print(f"    {f'entra +{k} min, custo {c}%':<38} {fmt(r)}")
                    if k == 2 and c == 0.5 and r is not None and r[1] > 0:
                        decisao.append(f"{nome}, saida {h} min")
    print("\n  DECISAO (regra fixada antes de rodar): "
          + (f"VALE MONTAR PAPEL RAPIDO -- {decisao}" if decisao else
             "NAO VALE: nada sobra com 2 min de latencia e custo de 0.5%"))
    print(f"  [{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main(sys.argv[1:])
