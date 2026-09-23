"""
Estudo 24, parte M3 -- base de futuros trimestrais (cash-and-carry com
vencimento), 23/09/2026. MEDICAO, sem teste estatistico e fora do K.

Do acervo: "OKEX期现对冲" (spot x futuro), "OKEx跨期对冲策略" e "多品种期货跨期对冲策略"
(entre vencimentos). E a versao com vencimento do cash-and-carry do estudo 20.
Diferenca que importa: no perpetuo o retorno depende do funding FUTURO (que
secou em 2025-2026); no trimestral a base e TRAVADA na entrada -- comprar o
spot e vender o futuro garante (F/S - 1) no vencimento, qualquer que seja o
preco. Nao ha o que prever; a pergunta e so quanto a base paga, liquida.

MONTAGEM MEDIDA
---------------
Coin-M (BTC, ETH, BNB, SOL, XRP; contrato inverso em USD, desde 2020): compra
a moeda, deposita como margem e vende o trimestral no mesmo valor em USD. A
posicao fica neutra em USD sem capital extra (1x): retorno sobre o capital =
base travada. USDT-M (BTC, ETH, desde 2021) so como comparacao da base.
- Base anualizada no dia t: (F/S - 1) x 365 / dias ate o vencimento, com o
  fechamento diario do continuo CURRENT_QUARTER e NEXT_QUARTER e do spot.
  Vencimento: ultima sexta de mar/jun/set/dez, 08:00 UTC. Dias com menos de
  7 dias para vencer sao descartados (ruido de liquidacao).
- Carry realizado por trimestre: entra no 1o dia em que o contrato e o
  CURRENT_QUARTER, segura ate o vencimento. Custo 0.30% por ciclo (spot
  0.10% compra + 0.10% venda, futuro 0.05% + 0.05% de slippage), o mesmo do
  estudo 20.

Ressalvas: spot em USDT contra indice em USD (diferenca USDT/USD ignorada);
nao modela risco de corretora/custodia, nem de liquidacao se a margem nao for
exatamente 1x; preco de fechamento diario, nao o executavel.
"""

import calendar
import datetime as dt
import json
import os
import time
import urllib.request
from collections import defaultdict

import dados_binance as DB

CACHE = DB.CACHE_DIR
CUSTO_CICLO = 0.0030
MS_DIA = 86_400_000


def _get(url):
    for t in range(5):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "btc-monitor-script"})
            with urllib.request.urlopen(req, timeout=20) as r:
                return json.loads(r.read().decode())
        except Exception:
            if t == 4:
                raise
            time.sleep(2 + 2 * t)


def continuo(base, pair, ct):
    f = os.path.join(CACHE, f"{pair}_{ct}_1d.json")
    if os.path.exists(f):
        return json.load(open(f))
    out, cursor, agora = {}, 1_577_836_800_000, int(time.time() * 1000)
    while cursor < agora:
        raw = _get(f"{base}/continuousKlines?pair={pair}&contractType={ct}&interval=1d"
                   f"&startTime={cursor}&limit=500")
        time.sleep(0.2)
        if not raw:
            break
        for k in raw:
            if int(k[6]) < agora:
                out[int(k[0])] = float(k[4])
        cursor = int(raw[-1][0]) + MS_DIA
        if len(raw) < 500:
            break
    serie = sorted(out.items())
    json.dump(serie, open(f, "w"))
    return serie


def vencimentos():
    """Ultima sexta de mar/jun/set/dez, 08:00 UTC, 2020-2027, em ms."""
    out = []
    for ano in range(2020, 2028):
        for mes in (3, 6, 9, 12):
            ult = calendar.monthrange(ano, mes)[1]
            d = dt.date(ano, mes, ult)
            while d.weekday() != 4:
                d -= dt.timedelta(days=1)
            out.append(int(dt.datetime(ano, mes, d.day, 8, tzinfo=dt.timezone.utc).timestamp() * 1000))
    return out


VENC = vencimentos()


def venc_de(ts, ordem):
    """ordem 0 = CURRENT_QUARTER (1o vencimento depois de ts), 1 = NEXT."""
    futuros = [v for v in VENC if v > ts]
    return futuros[ordem]


def main():
    ativos = [("coin-M", "https://dapi.binance.com/dapi/v1", p, p.replace("USD", "USDT"))
              for p in ("BTCUSD", "ETHUSD", "BNBUSD", "SOLUSD", "XRPUSD")]
    ativos += [("USDT-M", "https://fapi.binance.com/fapi/v1", p, p) for p in ("BTCUSDT", "ETHUSDT")]
    hoje = int(time.time() * 1000)
    for tipo, base, pair, spot_sym in ativos:
        spot = dict((k[0], k[4]) for k in DB.baixar_spot(spot_sym, "1Dutc", 3000))
        print(f"\n{'='*96}\n{tipo} {pair} (spot {spot_sym})\n{'='*96}")
        por_ano = defaultdict(list)
        recentes = []
        for ordem, ct in enumerate(("CURRENT_QUARTER", "NEXT_QUARTER")):
            for ts, f in continuo(base, pair, ct):
                s = spot.get(ts)
                if not s:
                    continue
                v = venc_de(ts, ordem)
                dte = (v - ts) / MS_DIA
                if dte < 7:
                    continue
                anual = (f / s - 1) * 365 / dte
                if ordem == 0:
                    por_ano[time.gmtime(ts / 1000).tm_year].append(anual)
                if hoje - ts <= 30 * MS_DIA:
                    recentes.append((ct, dte, anual))
        print("  base anualizada do CURRENT_QUARTER, por ano (mediana | p10 - p90 | dias):")
        for ano in sorted(por_ano):
            xs = sorted(por_ano[ano])
            n = len(xs)
            print(f"    {ano}: {100*xs[n//2]:+6.2f}%  | {100*xs[n//10]:+6.2f}% a {100*xs[9*n//10]:+6.2f}% | {n}")
        for ct in ("CURRENT_QUARTER", "NEXT_QUARTER"):
            xs = sorted(a for c, _, a in recentes if c == ct)
            if xs:
                print(f"  ultimos 30 dias, {ct:<15}: mediana {100*xs[len(xs)//2]:+6.2f}%/ano "
                      f"(min {100*xs[0]:+.2f}, max {100*xs[-1]:+.2f})")
        # carry realizado: entra no 1o dia de cada contrato como CURRENT_QUARTER
        if tipo != "coin-M":
            continue
        serie = continuo(base, pair, "CURRENT_QUARTER")
        entradas = {}
        for ts, f in serie:
            v = venc_de(ts, 0)
            if v not in entradas and spot.get(ts) and (v - ts) / MS_DIA >= 60:
                entradas[v] = (ts, f, spot[ts])
        print("  carry realizado por trimestre (entra no 1o dia, segura ate vencer, liquido de 0.30%):")
        tot, anos = 1.0, 0.0
        linhas = []
        for v, (ts, f, s) in sorted(entradas.items()):
            if v > hoje:
                continue
            dias = (v - ts) / MS_DIA
            r = (f / s - 1) - CUSTO_CICLO
            tot *= 1 + r
            anos += dias / 365
            linhas.append(f"{time.strftime('%Y-%m', time.gmtime(v/1000))} {100*r*365/dias:+5.1f}%")
        for i in range(0, len(linhas), 6):
            print("    " + " | ".join(linhas[i:i + 6]))
        if anos:
            print(f"  acumulado {100*(tot-1):+.1f}% em {anos:.1f} anos = {100*(tot**(1/anos)-1):+.2f}%/ano")


if __name__ == "__main__":
    main()
