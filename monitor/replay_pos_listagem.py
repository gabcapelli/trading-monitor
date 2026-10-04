"""
Estudo 30 -- vender o perpetuo na abertura do spot de uma listagem nova da
Binance, PRE-REGISTRADO em 04/10/2026, antes de calcular qualquer retorno
NESTA amostra.

DE ONDE VEM
-----------
Descritivo pre-registrado do estudo 29 (replay_listagem.py): nos 62 eventos
com perpetuo no anuncio, o perpetuo devolveu -9.9% em 24h e -20.6% em 7 dias
depois da abertura do spot, IC inteiro abaixo de zero. A literatura relata o
mesmo ("reverte em ~2 semanas"). Aquilo foi visto naqueles 62; aqui se testa a
regra em eventos que o estudo 29 NAO mediu.

AMOSTRA (limpa)
---------------
Eventos de replay_listagem.eventos() (anuncio do catalogo 48 citando o ticker,
spot abrindo ate 7 dias depois), MENOS os 62 que foram trade valido no estudo
29. Sobram sobretudo os 113 em que o perpetuo foi lancado depois do horario de
entrada do 29 e os 27 em que o spot abriu antes dela. Operavel aqui:
perpetuo USDT-M da Binance (TKRUSDT ou 1000TKRUSDT) com volume > 0 no candle
da abertura do spot.
Ressalva: mesmo periodo e mesmo mercado dos 62 -- eventos diferentes, nao
amostra independente no tempo.

REGRA (vendido no perpetuo)
---------------------------
- Entrada: abertura da hora em que o spot comeca a negociar (o horario e
  publicado no anuncio, entao nao ha latencia de deteccao).
- Saida: abertura da mesma hora 7 dias depois. Sem stop, sem alvo.
- Sem candle (ou sem volume) na entrada, ou sem candle na saida: fora.

MEDIDAS (% do nocional, positivo = vendido ganhou)
--------------------------------------------------
- `abs` (decide): bruto - 0.18% + funding recebido pelo vendido.
- `excesso` (decide): bruto - retorno de vender a cesta dos 20 majors nas
  mesmas horas. Sem funding.
- Bootstrap por ANUNCIO, 5000 reamostragens.

CRITERIO
--------
PASSA se `abs` E `excesso` tiverem IC95 inteiro acima de zero.
Menos de 20 anuncios com trade valido: SEM AMOSTRA PARA DECIDIR.

DESCRITIVOS
-----------
- Saida em 24h e em 14d.
- Os 62 do estudo 29 com esta mesma regra (amostra ja vista; so referencia).
- Por ano; cauda (5 piores) -- o risco de squeeze do estudo 28.
- Custo de 0.5%.

Uso (de dentro de monitor/):
    python replay_pos_listagem.py --contar
    python replay_pos_listagem.py
"""

import sys
import time
from collections import defaultdict
from datetime import datetime, timezone

import replay_deslistagem as R
import replay_listagem as L
from replay_ema_ribbon import CUSTO_RT

H, DIA = R.H, R.DIA
HORIZONTE = 7 * DIA


def trade(e, horizonte=HORIZONTE):
    entrada_ts = e["inicio_spot"] // H * H
    sym, _ = R.simbolo_perp(e["token"], entrada_ts)
    if not sym:
        return None, "sem perpetuo na abertura do spot"
    saida_ts = entrada_ts + horizonte
    serie = R.klines("futures/um", sym, entrada_ts - DIA, saida_ts + DIA)
    k_in, k_out = serie.get(entrada_ts), serie.get(saida_ts)
    if not k_in or k_in[4] == 0:
        return None, "perpetuo sem negociacao na entrada"
    if not k_out:
        return None, "sem candle de saida"
    return {**e, "sym": sym, "entrada_ts": entrada_ts, "saida_ts": saida_ts,
            "ano": datetime.fromtimestamp(e["ts"] / 1000, timezone.utc).year,
            "bruto": -100 * (k_out[0] / k_in[0] - 1)}, "ok"


def medir(trades, cache):
    for t in trades:
        c = R.cesta(t["entrada_ts"], t["saida_ts"], cache)
        t["excesso"] = None if c is None else t["bruto"] - c
        f = 100 * R.funding(t["sym"], t["entrada_ts"], t["saida_ts"])
        t["funding_recebido"] = f
        t["abs"] = t["bruto"] - 100 * CUSTO_RT + f
        t["abs_custo05"] = t["bruto"] - 0.5 + f


def bloco(rot, trades):
    print(f"\n  [{rot}]")
    for chave, nome in (("bruto", "bruto"), ("funding_recebido", "funding recebido"),
                        ("abs", "absoluto"), ("excesso", "excesso sobre majors"),
                        ("abs_custo05", "absoluto, custo 0.5%")):
        print(R.linha(nome, trades, chave)[0])
    v = sorted(t["abs"] for t in trades)
    if v:
        print(f"  abs: positivos {sum(x > 0 for x in v)}/{len(v)} | mediana {v[len(v)//2]:+.2f}% | "
              f"5 piores {[round(x, 1) for x in v[:5]]}")


def main(argv):
    t0 = time.time()
    evs = L.eventos()
    vistos = set()
    for e in evs:
        t, _ = L.montar_trade(e)
        if t:
            vistos.add((e["token"], e["ts"]))
    limpos = [e for e in evs if (e["token"], e["ts"]) not in vistos]
    print(f"Eventos: {len(evs)} | vistos no estudo 29: {len(vistos)} | amostra limpa: {len(limpos)}")

    trades, motivos = [], defaultdict(int)
    for e in limpos:
        t, m = trade(e)
        motivos[m] += 1
        if t:
            trades.append(t)
    por_ano = defaultdict(int)
    for t in trades:
        por_ano[t["ano"]] += 1
    print("Montagem:", dict(motivos))
    print(f"Trades validos: {len(trades)} em {len({t['ts'] for t in trades})} anuncios | por ano {dict(sorted(por_ano.items()))}")
    if "--contar" in argv:
        return

    cache = {}
    medir(trades, cache)
    print("\n" + "=" * 100 + "\nVENDIDO NO PERPETUO da abertura do spot ate +7d (positivo = vendido ganhou)\n" + "=" * 100)
    bloco("AMOSTRA LIMPA, H=7d (decide: absoluto E excesso)", trades)

    for rot, hz in (("amostra limpa, H=24h (descritivo)", DIA), ("amostra limpa, H=14d (descritivo)", 14 * DIA)):
        tr = [t for t in (trade(e, hz)[0] for e in limpos) if t]
        medir(tr, cache)
        bloco(rot, tr)
    ja = [t for t in (trade(e)[0] for e in evs if (e["token"], e["ts"]) in vistos) if t]
    medir(ja, cache)
    bloco("os 62 do estudo 29, H=7d (amostra JA VISTA, so referencia)", ja)

    print("\n  Por ano (amostra limpa, H=7d):")
    for ano in sorted(por_ano):
        sub = [t for t in trades if t["ano"] == ano]
        print(R.linha(f"{ano} abs", sub, "abs")[0])
        print(R.linha(f"{ano} excesso", sub, "excesso")[0])

    print("\n  Por trade (amostra limpa, H=7d):")
    for t in trades:
        print(f"    {datetime.fromtimestamp(t['entrada_ts']/1000, timezone.utc):%Y-%m-%d %H:%M} {t['sym']:<16} "
              f"bruto {t['bruto']:+7.2f}% | funding {t['funding_recebido']:+6.2f}% | abs {t['abs']:+7.2f}% | "
              f"excesso {t['excesso'] if t['excesso'] is not None else float('nan'):+7.2f}%")

    n = len({t["ts"] for t in trades})
    if n < R.MIN_ANUNCIOS:
        decisao = f"SEM AMOSTRA PARA DECIDIR ({n} anuncios < {R.MIN_ANUNCIOS})"
    else:
        _, lo_a = R.linha("", trades, "abs")
        _, lo_e = R.linha("", trades, "excesso")
        decisao = "PASSA" if (lo_a is not None and lo_e is not None and lo_a > 0 and lo_e > 0) else "NAO PASSA"
    print(f"\n  DECISAO: {decisao}\n  [{time.time()-t0:.0f}s]")


if __name__ == "__main__":
    main(sys.argv[1:])
