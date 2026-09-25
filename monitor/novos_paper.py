"""
Registro em PAPEL da venda de perpetuo recem-lancado, com stop. NAO envia
ordem. Registra em claude/novos-paper.md. So biblioteca padrao do Python.

Origem: repo `binance-listings` (estudo.py, 23/09/2026). Em 654 lancamentos
(2020-2026, inclusive deslistados) a maioria dos perpetuos novos cai (mediana
-27% em 30 dias no teste, 73% caem), mas poucos disparam (ate +3.072%) e a
venda SEM limite de perda deu media negativa: NAO PASSOU. A versao com stop
foi imaginada DEPOIS de ver esses dados, entao so pode ser testada em
lancamentos futuros -- e o que este registro faz.

REGRA CONGELADA (23/09/2026 -- nao alterar durante o teste; parametros
redondos escolhidos por principio, sem otimizar no historico)
-------------------------------------------------------------------------
- Evento: perpetuo USDT-M novo na Binance (primeiro candle diario no
  data.binance.vision = dia d0), de ativo cripto (underlyingType COIN na
  exchangeInfo; se a API estiver inacessivel, o tipo fica "?" e o trade e
  registrado com essa marca, e o tipo e reconsultado a cada execucao --
  nao-cripto confirmado depois vira descarte, mesmo ja aberto; adendo de
  25/09/2026 apos OURA, pre-IPO que passou como "?"), sem stablecoin e sem relistagem (ativo com
  outro ticker 1000X ja existente).
- VENDE na abertura de d0 + 2 (00:00 UTC).
- STOP: recompra se a maxima diaria atingir +50% sobre a entrada (no preco
  do stop, ou na abertura se ela ja abrir acima), + 0.05% de slippage.
- Sem stop acionado: recompra na abertura de d0 + 32 (30 dias).
- Deslistado no meio: recompra no ultimo fechamento.
- Registra em paralelo a mesma venda SEM stop (a regra do estudo) e o
  excesso sobre a cesta dos 20 majors na mesma janela.
- Custo 0.18% ida+volta; funding real (vendido recebe positivo, PAGA
  negativo -- em token novo costuma ser negativo e caro).

CRITERIO DE LEITURA (fixado agora, antes do 1o trade): so reavaliar com >= 100
trades fechados. Com desvio de ~40% por trade (medido no estudo), 100 e o
minimo para distinguir um ganho medio de ~+8% de zero. Ritmo: a maioria dos
lancamentos de 2026 e de acoes/commodities (69 de 73 nos ultimos 70 dias);
com ~50-70 lancamentos cripto por ano, a leitura leva ~1.5-2 anos.

Rode sem argumento (o workflow horario chama assim). `--sem-push`, `--seco`.
"""

import json
import os
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import unlock_paper as U

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = os.path.join(RAIZ, "claude", "novos-paper.md")
ESTADO = os.path.join(RAIZ, "monitor", "novos_paper_state.json")
ENTRADA = 2
HORIZ = 30
STOP = 0.50
SLIP = 0.0005
CUSTO = 0.0018
META = 100
STABLE = {"USDC", "FDUSD", "TUSD", "BUSD", "USDP", "USDE", "USD1", "RLUSD", "U", "DAI", "PYUSD", "EUR",
          "USDS", "XUSD", "AEUR", "BFUSD", "EURI"}


def base_do_ativo(sym):
    b = sym[:-4]
    for p in ("1000000", "1000", "1M"):
        if b.startswith(p) and len(b) > len(p):
            return b[len(p):]
    return b


def ohlc(sym, dia):
    """(open, high, low, close) do dia UTC pelo vision; reserva: API."""
    rows = U._csv_do_zip(f"{U.VISION}/daily/klines/{sym}/1d/{sym}-1d-{U._data(dia)}.zip")
    for r in rows or []:
        if r and r[0].isdigit():
            return float(r[1]), float(r[2]), float(r[3]), float(r[4])
    r = U._json(f"{U.FAPI}/klines?symbol={sym}&interval=1d&startTime={dia * U.MS_DIA}&limit=1")
    if r and int(r[0][0]) == dia * U.MS_DIA and int(r[0][6]) < time.time() * 1000:
        return tuple(float(x) for x in r[0][1:5])
    return None


def tipos():
    r = U._json(f"{U.FAPI}/exchangeInfo")
    if not r:
        return None
    return {s["symbol"]: s.get("underlyingType") for s in r.get("symbols", [])}


def novos_eventos(estado, hoje):
    """Descobre perpetuos novos (estreia com entrada >= inicio)."""
    perps = sorted(p for p in U.todos_os_perpetuos() if p.endswith("USDT"))
    if not perps:
        print("  listagem do vision indisponivel")
        return
    falta = [p for p in perps if p not in estado["estreia"]]
    with ThreadPoolExecutor(8) as ex:
        for p, d in zip(falta, ex.map(lambda s: U.estreia(s, {}), falta)):
            if d is not None:
                estado["estreia"][p] = d
    tp = None
    for p in perps:
        d0 = estado["estreia"].get(p)
        if d0 is None or d0 + ENTRADA < estado["inicio"] or p in estado["trades"]:
            continue
        a = base_do_ativo(p)
        anteriores = [q for q, dq in estado["estreia"].items() if q != p and base_do_ativo(q) == a and dq < d0]
        if tp is None:
            tp = tipos() or {}
        tipo = tp.get(p, "?")
        motivo = None
        if a in STABLE:
            motivo = "stablecoin"
        elif anteriores:
            motivo = f"relistagem ({anteriores[0]})"
        elif tipo not in ("COIN", "?"):
            motivo = f"nao-cripto ({tipo})"
        estado["trades"][p] = {"par": p, "d0": d0, "entrada": d0 + ENTRADA, "tipo": tipo,
                               "status": "descartado" if motivo else "aguardando", "motivo": motivo}


def revalida_tipo(estado):
    """Tipo '?' (exchangeInfo inacessivel na varredura): tenta de novo antes de abrir
    e enquanto aberto. Nao-cripto confirmado vira descarte, como na varredura."""
    pend = [t for t in estado["trades"].values() if t["tipo"] == "?" and t["status"] in ("aguardando", "aberto")]
    if not pend:
        return
    tp = tipos()
    if not tp:
        return
    for t in pend:
        tipo = tp.get(t["par"], "?")
        t["tipo"] = tipo
        if tipo not in ("COIN", "?"):
            quando = " (confirmado apos a abertura)" if t["status"] == "aberto" else ""
            t.update({"status": "descartado", "motivo": f"nao-cripto ({tipo}){quando}"})
            print(f"  DESCARTA {t['par']}: {t['motivo']}")


def processa(estado, hoje):
    abertos, fechados = [], []
    revalida_tipo(estado)
    for t in estado["trades"].values():
        if t["status"] == "aguardando" and hoje >= t["entrada"]:
            px = U.abertura(t["par"], t["entrada"])
            if px:
                cesta = {s: U.abertura(s, t["entrada"]) for s in U.CESTA}
                t.update({"status": "aberto", "px_in": px, "cesta_in": {k: v for k, v in cesta.items() if v},
                          "stop_px": px * (1 + STOP), "dias_vistos": []})
                abertos.append(t)
        if t["status"] != "aberto":
            continue
        fim = t["entrada"] + HORIZ
        # varre os dias fechados ainda nao vistos, procurando o stop
        for dia in range(t["entrada"], min(fim, hoje)):
            if dia in t["dias_vistos"] or t.get("stop_dia") is not None:
                continue
            k = ohlc(t["par"], dia)
            if k is None:
                if dia < hoje - 3 and U.ativo(t["par"], hoje) is False:
                    t["deslistado_dia"] = dia
                break
            t["dias_vistos"].append(dia)
            o, h = k[0], k[1]
            if h >= t["stop_px"]:
                t["stop_dia"], t["stop_saida"] = dia, max(o, t["stop_px"]) * (1 + SLIP)
        pronto = hoje >= fim or t.get("deslistado_dia") is not None
        if pronto and fecha(t, fim):
            fechados.append(t)
    for t in estado["trades"].values():
        if t["status"] == "fechado" and t.get("funding") == "pendente":
            completa_funding(t)
    return abertos, fechados


def fecha(t, fim):
    if t.get("deslistado_dia") is not None:
        k = ohlc(t["par"], t["deslistado_dia"] - 1)
        if not k:
            return False
        px_fim, dia_fim = k[3], t["deslistado_dia"]
    else:
        px_fim, dia_fim = U.abertura(t["par"], fim), fim
        if px_fim is None:
            return False
    rc = [U.abertura(s, dia_fim) / p0 - 1 for s, p0 in t["cesta_in"].items() if U.abertura(s, dia_fim)]
    t.update({"status": "fechado", "px_fim": px_fim, "dia_fim": dia_fim,
              "ret_sem_stop": px_fim / t["px_in"] - 1, "ret_cesta": sum(rc) / len(rc) if rc else 0.0})
    if t.get("stop_dia") is not None:
        t["ret_com_stop"], t["dia_saida_stop"] = t["stop_saida"] / t["px_in"] - 1, t["stop_dia"] + 1
    else:
        t["ret_com_stop"], t["dia_saida_stop"] = t["ret_sem_stop"], dia_fim
    completa_funding(t)
    return True


def completa_funding(t):
    f_sem = U.funding(t["par"], t["entrada"], t["dia_fim"])
    f_com = U.funding(t["par"], t["entrada"], t["dia_saida_stop"])
    pend = f_sem is None or f_com is None
    t["funding"] = "pendente" if pend else "ok"
    f_sem, f_com = f_sem or 0.0, f_com or 0.0
    # vendido: ganha -retorno, recebe funding positivo
    t["sem_stop"] = -t["ret_sem_stop"] - CUSTO + f_sem
    t["com_stop"] = -t["ret_com_stop"] - CUSTO + f_com
    t["excesso"] = -(t["ret_sem_stop"] - t["ret_cesta"])


def escreve_ledger(estado, hoje):
    tr = list(estado["trades"].values())
    fech = sorted([t for t in tr if t["status"] == "fechado"], key=lambda t: t["entrada"])
    abertos = sorted([t for t in tr if t["status"] == "aberto"], key=lambda t: t["entrada"])
    agu = sorted([t for t in tr if t["status"] == "aguardando"], key=lambda t: t["entrada"])
    desc = [t for t in tr if t["status"] == "descartado"]
    L = ["# Registro em papel — venda de perpétuo recém-lançado, com stop",
         "",
         "> Gerado por `monitor/novos_paper.py`. **Nenhuma ordem é enviada.**",
         "> Regra congelada em 23/09/2026 (repo `binance-listings`): vender o perpétuo novo na abertura",
         "> do 2º dia após o lançamento; recomprar se subir **50%** (stop) ou em **30 dias**. Registra",
         "> em paralelo a venda **sem stop** (a regra do estudo, que não passou). Custo 0.18% e funding real.",
         f"> **Só reavaliar com {META} trades fechados.** Antes disso é ruído.",
         "",
         f"_Atualizado em {U._data(hoje)}._", ""]
    if fech:
        n = len(fech)
        mc = sum(t["com_stop"] for t in fech) / n
        ms = sum(t["sem_stop"] for t in fech) / n
        st = sum(1 for t in fech if t.get("stop_dia") is not None)
        pos = sum(1 for t in fech if t["com_stop"] > 0)
        L += [f"**Trades fechados:** {n} de {META} ({100*n/META:.0f}%)", "",
              f"**Média por trade:** com stop {100*mc:+.2f}% · sem stop {100*ms:+.2f}% · "
              f"stop acionado em {st}/{n} · positivos (com stop) {pos}/{n}", ""]
    L += ["## Abertos", ""]
    if abertos:
        L += ["| Token | Lançado | Venda em | Entrada | Stop (+50%) | Saída prevista |", "|---|---|---|---|---|---|"]
        L += [f"| {t['par'].replace('USDT', '')} | {U._data(t['d0'])} | {U._data(t['entrada'])} | {t['px_in']:g} | "
              f"{t['stop_px']:g}{' **acionado**' if t.get('stop_dia') is not None else ''} | "
              f"{U._data(t['entrada'] + HORIZ)}{' (tipo não confirmado)' if t['tipo'] == '?' else ''} |" for t in abertos]
    else:
        L.append("_Nenhum._")
    if agu:
        L += ["", "## Aguardando a entrada", ""]
        L += [f"- {t['par'].replace('USDT', '')}: lançado {U._data(t['d0'])}, venda em {U._data(t['entrada'])}"
              + (" (tipo não confirmado)" if t["tipo"] == "?" else "") for t in agu]
    L += ["", "## Fechados", ""]
    if fech:
        L += ["| Token | Venda | Token no período | Com stop | Sem stop | Excesso s/ cesta | Obs. |", "|---|---|---|---|---|---|---|"]
        for t in reversed(fech):
            obs = [x for x, c in (("stop", t.get("stop_dia") is not None), ("deslistado", t.get("deslistado_dia") is not None),
                                  ("funding pendente", t.get("funding") == "pendente"), ("tipo ?", t["tipo"] == "?")) if c]
            L.append(f"| {t['par'].replace('USDT', '')} | {U._data(t['entrada'])} | {100*t['ret_sem_stop']:+.1f}% | "
                     f"{100*t['com_stop']:+.2f}% | {100*t['sem_stop']:+.2f}% | {100*t['excesso']:+.2f}% | {', '.join(obs)} |")
    else:
        L.append("_Nenhum ainda._")
    if desc:
        L += ["", f"<details><summary>Descartados ({len(desc)})</summary>", ""]
        L += [f"- {t['par']} ({U._data(t['d0'])}): {t['motivo']}" for t in sorted(desc, key=lambda t: t["d0"])]
        L += ["", "</details>"]
    L.append("")
    open(LEDGER, "w", encoding="utf-8").write("\n".join(L))


def notifica(abertos, fechados):
    import fetch_and_check as m
    if abertos:
        m.send_ntfy(f"Perpetuo novo: {len(abertos)} venda(s) em papel",
                    "\n".join(f"VENDER {t['par']} a {t['px_in']:g}; stop (recompra) em {t['stop_px']:g}; "
                              f"saida em {U._data(t['entrada'] + HORIZ)}"
                              + (" (TIPO NAO CONFIRMADO: pode ser acao/pre-IPO)" if t["tipo"] == "?" else "")
                              for t in abertos)
                    + "\nRegistro em papel, nao e ordem.")
    if fechados:
        m.send_ntfy(f"Perpetuo novo: {len(fechados)} trade(s) fechado(s) em papel",
                    "\n".join(f"{t['par']}: com stop {100*t['com_stop']:+.2f}% | sem stop {100*t['sem_stop']:+.2f}%"
                              for t in fechados) + "\nVer claude/novos-paper.md.")


def main():
    hoje = int(datetime.now(timezone.utc).timestamp()) // 86400
    estado = json.load(open(ESTADO, encoding="utf-8")) if os.path.exists(ESTADO) else \
        {"inicio": None, "ultimo_scan": None, "estreia": {}, "trades": {}}
    if estado["inicio"] is None:
        estado["inicio"] = hoje
        print(f"iniciando registro em {U._data(hoje)}")
    if estado.get("ultimo_scan") != hoje:
        novos_eventos(estado, hoje)
        estado["ultimo_scan"] = hoje
    abertos, fechados = processa(estado, hoje)
    for t in abertos:
        print(f"  ABRE  {t['par']} a {t['px_in']:g} (stop {t['stop_px']:g})")
    for t in fechados:
        print(f"  FECHA {t['par']} com stop {100*t['com_stop']:+.2f}% | sem stop {100*t['sem_stop']:+.2f}%")
    print(f"  aguardando: {sum(t['status'] == 'aguardando' for t in estado['trades'].values())} | "
          f"abertos: {sum(t['status'] == 'aberto' for t in estado['trades'].values())}")
    if "--seco" in sys.argv:
        return
    json.dump(estado, open(ESTADO, "w", encoding="utf-8"), indent=0, sort_keys=True)
    escreve_ledger(estado, hoje)
    if "--sem-push" not in sys.argv and (abertos or fechados):
        notifica(abertos, fechados)


if __name__ == "__main__":
    main()
