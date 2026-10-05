"""
Estudo 40 -- replica do braco exploratorio de deslistagem (estudo 38: vendido
ate 4h apos o anuncio) num conjunto INDEPENDENTE de eventos: o fim de suporte
(거래지원 종료) da Upbit. PRE-REGISTRADO em 05/10/2026, antes de olhar precos.

POR QUE
-------
No estudo 38, vender o perpetuo depois do anuncio de deslistagem da Binance e
recomprar 4h depois deu +4.1% [+1.1, +6.9] entrando com 60 min -- mas fora da
regra pre-registrada (exploratorio), e com os eventos do estudo 28. Esta e a
mesma regra, sem ajuste, em eventos de outra corretora.

Leitura, fixada antes:
- passa: o braco de deslistagem do papel ganha peso (segue exploratorio ate o
  papel decidir);
- nao passa: o +4.1% do 38 era provavelmente ruido/selecao.
Ressalva ja sabida (estudo 39): evento da Upbit mexe menos no perpetuo da
Binance que evento da propria Binance.

EVENTOS
-------
- Mesmo feed do estudo 39 (cache_anuncios/upbit_trade.json).
- Evento = cada "(TKR)" num titulo com "거래지원 종료" (fim de suporte).
- Fora: remocao so de um mercado ("마켓"), pares especificos ("MYST/BTC"; a barra das datas nao conta),
  correcao/mudanca de data/retomada ("변경", "정정", "재개"), e token com anuncio
  da Binance (Monitoring Tag ou deslistagem) entre 2 dias antes e 1 dia depois.
- Mesmo token anunciado mais de uma vez: vale o 1o anuncio.

REGRA E MEDIDAS: as do estudo 39 (replay_upbit_alerta.montar), com saida em
floor(anuncio) + 4h em vez de 24h. Entrada +60 min, custo 0.5% + funding,
excesso sobre o BTC, bootstrap por anuncio.

CRITERIO
--------
PASSA se `liq` E `excesso` tiverem IC95 inteiro acima de zero. Com menos de 15
anuncios com trade: SEM AMOSTRA PARA DECIDIR.

Uso (de dentro de monitor/):
    python replay_upbit_deslistagem.py --contar
    python replay_upbit_deslistagem.py
"""

import json
import re
import sys
from collections import defaultdict
from datetime import datetime

import replay_deslistagem as D
import replay_monitoring_tag as MT
import replay_upbit_alerta as UA
from replay_deslistagem import DIA


def eventos():
    with open(UA.ARQ, encoding="utf-8") as f:
        notas = sorted(json.load(f), key=lambda n: n["listed_at"])
    binance = defaultdict(list)
    for e in MT.eventos() + D.eventos():
        binance[e["token"]].append(e["ts"])
    out, vistos, motivos = [], set(), defaultdict(int)
    for n in notas:
        t = n["title"]
        if "거래지원 종료" not in t:
            continue
        if "마켓" in t or re.search(r"[A-Z]+/[A-Z]+", t) or any(x in t for x in ("변경", "정정", "재개")):
            motivos["fora pelo titulo"] += 1
            continue
        ts = int(datetime.fromisoformat(n["listed_at"]).timestamp() * 1000)
        for tk in re.findall(r"\(([A-Z0-9]{1,12})\)", t):
            if tk in UA.EXCLUIDOS or tk in vistos:
                continue
            vistos.add(tk)
            if any(ts - 2 * DIA <= b <= ts + DIA for b in binance.get(tk, [])):
                motivos["anuncio da Binance colado"] += 1
                continue
            out.append({"token": tk, "ts": ts, "titulo": t})
    return sorted(out, key=lambda e: e["ts"]), motivos


if __name__ == "__main__":
    UA.SAIDA_MIN = 4 * 60
    UA.eventos = eventos
    print("Estudo 40: fim de suporte na Upbit, vendido de +60 min a +4h (saida 4h, nao 24h)")
    UA.main(sys.argv[1:])
