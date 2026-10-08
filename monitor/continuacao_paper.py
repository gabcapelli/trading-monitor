"""
Registro em papel -- rompimento de 7 dias com volume no top 20 de volume,
segurando 48h (estudo 46). REGRA CONGELADA em 05/10/2026. Nenhuma ordem e
enviada.

ORIGEM E EXCECAO
----------------
Estudo 46: liquido +0.76% por trade, IC95 [-0.03, +1.60] (falhou por um fio);
excesso +0.79% com IC > 0; metades e trades fora das majors positivos. A regra
do Gabriel era so ir ao papel com o criterio completo; em 05/10/2026 ele optou
por ABRIR UMA EXCECAO consciente, sabendo que e caso limitrofe.

REGRA (identica ao estudo 46)
-----------------------------
- Universo do dia (recalculado 1x por dia UTC): perpetuos USDT-M cripto
  negociando (underlyingType COIN, sem base com USD/DAI/EUR); as 20 de maior
  volume em dolar nos 30 dias anteriores (candles de 1d). Pre-filtro: as 60 de
  maior volume de 24h.
- Barras de 4h (00, 04, 08... UTC). COMPRA se o fechamento da barra > maxima
  das 42 barras anteriores (7 dias) E volume em dolar da barra >= 2x a media
  das 180 anteriores (30 dias). VENDA no espelho. So pares do top 20 do dia.
- Entrada na abertura da barra seguinte; saida na abertura da hora 48h depois.
  Sem stop. Um trade por par de cada vez.
- Custo 0.18% ida e volta + funding real.
- Volume da barra: o "quote volume" do candle de 4h da Binance (no estudo, a
  soma de volume x fechamento das 4 horas; equivalente, conferido no teste).
- Registra tambem o preco REAL alcancavel (abertura do minuto em que o script
  roda), na entrada e na saida: o atraso do workflow (~5 min) fica medido.

MEDIDAS (% do nocional)
-----------------------
- `liq` (decide) = bruto pelos precos da regra - 0.18% + funding.
- `liq_real` = idem com os precos alcancaveis (descritivo de execucao).
- `excesso` = bruto - media do mesmo lado nos outros pares do top 20 do dia,
  mesmas horas.

LEITURA (fixada antes do 1o trade)
----------------------------------
So reavaliar com 300 TRADES FECHADOS (~7 meses no ritmo do estudo). Decide:
`liq` e `excesso` com IC95 inteiro > 0, bootstrap por semana de entrada.
Antes disso e ruido. Leitura sobre `liq_real` como confirmacao de execucao.

VARIANTE COM STOP NO NIVEL ROMPIDO (acrescentada em 08/10/2026, estudo 61)
--------------------------------------------------------------------------
No estudo 61, todo o ganho do 46 veio dos rompimentos que nunca voltaram ao
nivel rompido (+6.3% a mercado); os que voltaram perderam -2.4%. Hipotese
nascida desse dado, por isso testada so daqui para frente, nos MESMOS sinais e
sem mudar a regra acima (que continua decidindo o papel do 46):
- nivel = maxima das 42 barras de 4h anteriores a barra do sinal (minima na venda);
- stop: primeira hora (candles de 1h, da entrada ate a saida de 48h) cuja minima
  toca o nivel (maxima na venda); sai a min(nivel, abertura da hora) na compra;
- sem toque: sai igual ao 46. Custo 0.18% + funding ate a saida.
- `liq_stop` em % e `r_stop` = liq_stop / risco, risco = |entrada - nivel| em %.
Leitura (fixada agora, antes de qualquer trade da variante): com os mesmos 300
trades, `liq_stop` com IC95 inteiro > 0 (bootstrap por semana) E media de
`liq_stop - liq` > 0. Os trades abertos antes de 08/10/2026 recebem o nivel
calculado dos candles anteriores ao sinal (dado que ja existia no sinal).

Rode sem argumento (o workflow horario chama assim).
"""

import json
import os
import random
import re
import sys
import time
from datetime import datetime, timedelta, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import unlock_paper as U

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_TESTE = os.environ.get("CONTINUACAO_PAPER_DIR")
LEDGER = os.path.join(_TESTE or os.path.join(RAIZ, "claude"), "continuacao-paper.md")
ESTADO = os.path.join(_TESTE or os.path.join(RAIZ, "monitor"), "continuacao_paper_state.json")

MIN = 60_000
H = 60 * MIN
B4 = 4 * H
DIA = 24 * H
TOP = 20
PRE = 60
JANELA_MAX = 42
JANELA_VOL = 180
MULT_VOL = 2.0
SAIDA_H = 48
CUSTO = 0.18
META = 300
BRT = timezone(timedelta(hours=-3))


# ---------------------------------------------------------------------------
# Binance (via proxy)
# ---------------------------------------------------------------------------

def klines(sym, intervalo, **kw):
    q = "&".join(f"{k}={v}" for k, v in kw.items())
    return U._json(f"{U.FAPI}/klines?symbol={sym}&interval={intervalo}&{q}")


def abertura(sym, intervalo, ts):
    k = klines(sym, intervalo, startTime=ts, limit=1)
    return float(k[0][1]) if k and int(k[0][0]) == ts else None


def funding(sym, t0, t1):
    r = U._json(f"{U.FAPI}/fundingRate?symbol={sym}&startTime={t0}&endTime={t1 - 1}&limit=1000")
    return None if r is None else 100 * sum(float(x["fundingRate"]) for x in r if t0 <= int(x["fundingTime"]) < t1)


def top20(dia):
    info = U._json(f"{U.FAPI}/exchangeInfo")
    tick = U._json(f"{U.FAPI}/ticker/24hr")
    if not info or not tick:
        return None
    ok = {s["symbol"] for s in info["symbols"]
          if s.get("contractType") == "PERPETUAL" and s.get("quoteAsset") == "USDT" and s.get("status") == "TRADING"
          and s.get("underlyingType", "COIN") == "COIN" and not re.search(r"USD|DAI|EUR", s.get("baseAsset", ""))}
    pre = sorted((float(t["quoteVolume"]), t["symbol"]) for t in tick if t["symbol"] in ok)[-PRE:]
    vol30 = []
    for _, s in pre:
        k = klines(s, "1d", endTime=dia - 1, limit=30)
        if k:
            vol30.append((sum(float(x[7]) for x in k), s))
    return [s for _, s in sorted(vol30)[-TOP:]]


# ---------------------------------------------------------------------------
# Regra
# ---------------------------------------------------------------------------

def sinal(sym, barra):
    """Sinal na barra de 4h que comeca em `barra` (ja fechada): +1, -1 ou 0."""
    k = klines(sym, "4h", endTime=barra + B4 - 1, limit=JANELA_VOL + 1)
    if not k or int(k[-1][0]) != barra or len(k) < JANELA_VOL + 1:
        return None
    hi = [float(x[2]) for x in k]
    lo = [float(x[3]) for x in k]
    vol = [float(x[7]) for x in k]
    c = float(k[-1][4])
    if vol[-1] < MULT_VOL * sum(vol[-1 - JANELA_VOL:-1]) / JANELA_VOL:
        return 0
    if c > max(hi[-1 - JANELA_MAX:-1]):
        return +1
    if c < min(lo[-1 - JANELA_MAX:-1]):
        return -1
    return 0


def nivel_rompido(sym, barra, lado):
    k = klines(sym, "4h", endTime=barra - 1, limit=JANELA_MAX)
    if not k or len(k) < JANELA_MAX:
        return None
    return max(float(x[2]) for x in k) if lado > 0 else min(float(x[3]) for x in k)


def com_stop(t):
    """Resultado da variante com stop no nivel rompido. None se faltar dado."""
    nivel = t.get("nivel")
    if nivel is None:
        nivel = nivel_rompido(t["sym"], t["barra"], t["lado"])
        if nivel is None:
            return None
        t["nivel"] = nivel
    k = klines(t["sym"], "1h", startTime=t["entrada_ts"], limit=SAIDA_H)
    if not k or len(k) < SAIDA_H:
        return None
    lado, p_in = t["lado"], t["p_in"]
    risco = lado * 100 * (p_in - nivel) / p_in
    for x in k:
        o, hi, lo = float(x[1]), float(x[2]), float(x[3])
        if (lo <= nivel) if lado > 0 else (hi >= nivel):
            p_out = min(nivel, o) if lado > 0 else max(nivel, o)
            sai = int(x[0]) + H
            f = funding(t["sym"], t["entrada_ts"], sai)
            if f is None:
                return None
            liq = lado * 100 * (p_out / p_in - 1) - CUSTO - lado * f
            return {"nivel": nivel, "stop_ts": int(x[0]), "liq_stop": liq,
                    "r_stop": liq / risco if risco > 0 else None}
    return {"nivel": nivel, "stop_ts": None, "liq_stop": t["liq"],
            "r_stop": t["liq"] / risco if risco > 0 else None}


def processa(estado, agora):
    abertos, fechados = [], []
    dia = agora // DIA * DIA
    if estado.get("dia_top") != dia:
        t = top20(dia)
        if t:
            estado["top"], estado["dia_top"] = t, dia
    top = estado.get("top") or []
    if not top:
        return abertos, fechados
    minuto = agora // MIN * MIN
    # barras de 4h fechadas ainda nao avaliadas (no maximo as 2 ultimas, se o cron atrasou)
    ult = estado.setdefault("ultima_barra", agora // B4 * B4 - B4)   # 1a execucao: nada de barra antiga
    barras = [b for b in range(ult + B4, agora // B4 * B4, B4)][-2:]
    for b in barras:
        for s in top:
            if any(t["sym"] == s and t["status"] == "aberto" for t in estado["trades"]):
                continue
            lado = sinal(s, b)
            if not lado:
                continue
            ent = b + B4
            nivel = nivel_rompido(s, b, lado)
            p_regra = abertura(s, "1h", ent)
            p_real = abertura(s, "1m", minuto)
            if p_regra is None:
                continue
            t = {"sym": s, "lado": lado, "barra": b, "entrada_ts": ent, "detectado": minuto,
                 "p_in": p_regra, "p_in_real": p_real, "saida_ts": ent + SAIDA_H * H,
                 "top": [x for x in top if x != s], "status": "aberto", "nivel": nivel}
            estado["trades"].append(t)
            abertos.append(t)
        estado["ultima_barra"] = b
    for t in estado["trades"]:
        if t["status"] != "aberto" or agora < t["saida_ts"] + 2 * MIN:
            continue
        p_out = abertura(t["sym"], "1h", t["saida_ts"])
        f = funding(t["sym"], t["entrada_ts"], t["saida_ts"])
        if p_out is None or f is None:
            if agora - t["saida_ts"] > 3 * DIA:
                t.update({"status": "descartado", "motivo": "sem preco de saida em 3 dias"})
            continue
        p_out_real = abertura(t["sym"], "1m", minuto)
        rets = []
        for x in t["top"]:
            a, b2 = abertura(x, "1h", t["entrada_ts"]), abertura(x, "1h", t["saida_ts"])
            if a and b2:
                rets.append(t["lado"] * 100 * (b2 / a - 1))
        bruto = t["lado"] * 100 * (p_out / t["p_in"] - 1)
        fl = -t["lado"] * f
        t.update({"status": "fechado", "p_out": p_out, "funding": fl, "bruto": bruto,
                  "liq": bruto - CUSTO + fl,
                  "excesso": bruto - sum(rets) / len(rets) if rets else None})
        if t.get("p_in_real") and p_out_real:
            t["liq_real"] = t["lado"] * 100 * (p_out_real / t["p_in_real"] - 1) - CUSTO + fl
        fechados.append(t)
    for t in estado["trades"]:   # variante com stop (inclui fechados antes dela existir)
        if t["status"] == "fechado" and "liq_stop" not in t:
            v = com_stop(t)
            if v:
                t.update(v)
    return abertos, fechados


# ---------------------------------------------------------------------------
# Registro
# ---------------------------------------------------------------------------

def _h(ts):
    return datetime.fromtimestamp(ts / 1000, BRT).strftime("%d/%m %H:%M")


def _boot(xs_por_semana):
    grupos = list(xs_por_semana.values())
    if len(grupos) < 5:
        return None
    n = sum(len(v) for v in grupos)
    rng = random.Random(42)
    ms = []
    for _ in range(3000):
        s = k = 0
        for _ in range(len(grupos)):
            v = grupos[rng.randrange(len(grupos))]
            s += sum(v)
            k += len(v)
        ms.append(s / k)
    ms.sort()
    return sum(sum(v) for v in grupos) / n, ms[75], ms[2924]


def escreve_ledger(estado, agora):
    tr = estado.get("trades", [])
    fe = [t for t in tr if t["status"] == "fechado"]
    ab = [t for t in tr if t["status"] == "aberto"]
    L = ["# Registro em papel — rompimento de 7 dias no top 20, segurando 48h", "",
         "> Gerado por `monitor/continuacao_paper.py`. **Nenhuma ordem é enviada.**",
         "> Regra congelada em 05/10/2026 (estudo 46), aberta como **exceção** pelo Gabriel: o estudo falhou",
         "> o critério por um fio. Custo 0.18% e funding real. **Só reavaliar com 300 trades fechados.**", "",
         f"_Atualizado em {_h(agora)} (Brasília). Top 20 do dia: {', '.join(x.replace('USDT', '') for x in estado.get('top', []))}._", "",
         f"**Trades fechados:** {len(fe)} de {META} ({100 * len(fe) // META}%)"]
    if fe:
        m = lambda k: sum(t[k] for t in fe if t.get(k) is not None) / max(sum(t.get(k) is not None for t in fe), 1)
        L.append(f"\n**Média por trade:** líquido {m('liq'):+.2f}% · excesso {m('excesso'):+.2f}% · "
                 f"com o preço real alcançável {m('liq_real'):+.2f}% · positivos {sum(t['liq'] > 0 for t in fe)}/{len(fe)}")
        sem = {}
        for t in fe:
            sem.setdefault(t["entrada_ts"] // (7 * DIA), []).append(t["liq"])
        b = _boot(sem)
        if b:
            L.append(f"\n_IC95 do líquido (ainda sem valor de decisão): [{b[1]:+.2f}, {b[2]:+.2f}]_")
    L.append("\n_Referência do estudo 46: +0.76% líquido, +0.79% de excesso por trade._")
    vs = [t for t in fe if t.get("liq_stop") is not None]
    if vs:
        rs = [t["r_stop"] for t in vs if t.get("r_stop") is not None]
        L.append(f"\n**Variante com stop no nível rompido** (hipótese do estudo 61, desde 08/10/2026; mesmos sinais): "
                 f"líquido {sum(t['liq_stop'] for t in vs) / len(vs):+.2f}% · "
                 f"{(sum(rs) / len(rs) if rs else float('nan')):+.2f}R · "
                 f"diferença para a regra {sum(t['liq_stop'] - t['liq'] for t in vs) / len(vs):+.2f}% · "
                 f"stopados {sum(t.get('stop_ts') is not None for t in vs)}/{len(vs)}")
        sem = {}
        for t in vs:
            sem.setdefault(t["entrada_ts"] // (7 * DIA), []).append(t["liq_stop"])
        b = _boot(sem)
        if b:
            L.append(f"\n_IC95 da variante (ainda sem valor de decisão): [{b[1]:+.2f}, {b[2]:+.2f}]_")
    L.append("")
    if ab:
        L += ["## Abertos", "", "| Par | Lado | Entrada | Preço | Saída |", "|---|---|---|---|---|"]
        L += [f"| {t['sym'].replace('USDT', '')} | {'compra' if t['lado'] > 0 else 'venda'} | {_h(t['entrada_ts'])} | "
              f"{t['p_in']:g} | {_h(t['saida_ts'])} |" for t in sorted(ab, key=lambda t: t["saida_ts"])]
        L.append("")
    if fe:
        L += ["## Fechados (mais recentes primeiro)", "",
              "| Par | Lado | Entrada | Bruto | Funding | Líquido | Excesso | Líquido real | Com stop no nível |",
              "|---|---|---|---|---|---|---|---|---|"]
        for t in sorted(fe, key=lambda t: -t["entrada_ts"])[:100]:
            exc = f"{t['excesso']:+.2f}%" if t.get("excesso") is not None else "—"
            lr = f"{t['liq_real']:+.2f}%" if t.get("liq_real") is not None else "—"
            ls = "—"
            if t.get("liq_stop") is not None:
                ls = f"{t['liq_stop']:+.2f}%" + (" (stop)" if t.get("stop_ts") is not None else "")
            L.append(f"| {t['sym'].replace('USDT', '')} | {'compra' if t['lado'] > 0 else 'venda'} | {_h(t['entrada_ts'])} | "
                     f"{t['bruto']:+.2f}% | {t['funding']:+.3f}% | {t['liq']:+.2f}% | {exc} | {lr} | {ls} |")
        L.append("")
    with open(LEDGER, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(L))


def notifica(abertos, fechados):
    linhas = [f"{'Compra' if t['lado'] > 0 else 'Venda'} {t['sym'].replace('USDT', '')} a {t['p_in']:g} (sai {_h(t['saida_ts'])})"
              for t in abertos]
    linhas += [f"Fecha {t['sym'].replace('USDT', '')}: liq {t['liq']:+.2f}%" for t in fechados]
    if linhas:
        import fetch_and_check as M
        M.send_ntfy("Rompimento 48h (papel)", "\n".join(linhas))


def main(argv):
    agora = int(time.time() * 1000)
    estado = json.load(open(ESTADO, encoding="utf-8")) if os.path.exists(ESTADO) else {}
    estado.setdefault("trades", [])
    estado.setdefault("iniciado", agora)
    abertos, fechados = processa(estado, agora)
    if "--sem-push" not in argv:
        notifica(abertos, fechados)
    with open(ESTADO, "w", encoding="utf-8", newline="\n") as f:
        json.dump(estado, f, indent=1)
    escreve_ledger(estado, agora)
    print(f"[continuacao_paper] top20: {len(estado.get('top', []))} | abertos agora: {len(abertos)} | "
          f"fechados agora: {len(fechados)} | total: {len(estado['trades'])}")


if __name__ == "__main__":
    main(sys.argv[1:])
