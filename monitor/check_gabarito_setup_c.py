#!/usr/bin/env python3
"""
Cruza os detectores de zona do Setup C (lib smartmoneyconcepts vs caseiro)
contra os 3 exemplos GENUINOS do gabarito qualitativo (claude/setup-c-gabarito.md)
que caem dentro da janela de histórico coberta por replay_setup_c.py.

Pergunta: algum dos dois detectores gerou uma zona (OB ou FVG) cuja faixa de
preço [bottom, top] sobrepõe a faixa real descrita no gabarito, formada ANTES
do timestamp do trade real do OTS? Isso NÃO mede aceite/RR/desfecho -- só
presença da zona, que é o que o gabarito pede pra checar (ver "Próximo passo"
em claude/setup-c-gabarito.md).

Não roda o harness completo (walk-forward com filtro de tendência/RR) --
varre zonas cruas em janelas de 200 candles terminando em cada hora do
período de busca, sem filtro de alinhamento de tendência, porque a pergunta
é se a zona FOI DETECTADA, não se teria sido aceita como trade.

Também reporta a densidade TOTAL de zonas geradas na mesma janela (qualquer
preço/direção) por tipo (OB/FVG) -- um "hit" numa banda de preço só é
evidência de detecção real se o detector não estiver gerando dezenas de
candidatos espalhados por toda a janela (nesse caso, cair em alguma banda é
esperado por acaso). Essa checagem foi o que reconciliou uma aparente
contradição em 11/09/2026: uma primeira contagem sem separar por tipo sugeriu
"a lib acertou os 3 exemplos", mas quebrando por tipo ficou claro que os hits
da lib eram quase todos FVG (20-51 candidatos por janela -- ruído, mesmo
problema já flagrado em claude/setup-c-testes.md), enquanto o `smc.ob` da lib
não achou nada relevante em nenhum dos 3 casos -- confirmando, por caminho
independente, o achado original do gabarito. Ver a seção "Cruzamento com o
gabarito real" em claude/setup-c-testes.md para a tabela e a conclusão.

Uso (da raiz do repo, com PYTHONPATH=monitor):
    PYTHONPATH=monitor python monitor/check_gabarito_setup_c.py
"""
import datetime as dt

import fetch_and_check as m  # noqa: E402
from replay_setup_c import fetch_historico, lib_zones_novas, home_zones_novas, WINDOW  # noqa: E402

CASOS = [
    {
        "nome": "BTC short (ex.1, 09/09/2026, 1h Bybit)",
        "inst": "BTC-USDT-SWAP",
        "direcao": "venda",
        "banda": (79300, 79500),
        "confirm_utc": dt.datetime(2026, 9, 9, 5, 56, tzinfo=dt.timezone.utc),  # BRT 02:56 -> UTC
        "busca_dias_antes": 5,
    },
    {
        "nome": "BTC compra (ex.2, 28/06/2026, 15min Bybit)",
        "inst": "BTC-USDT-SWAP",
        "direcao": "compra",
        "banda": (58300, 59900),
        "confirm_utc": dt.datetime(2026, 6, 28, 15, 37, tzinfo=dt.timezone.utc),  # BRT 12:37 -> UTC
        "busca_dias_antes": 10,
    },
    {
        "nome": "SOL compra (ex.3, 30/06/2026, 15min Bybit)",
        "inst": "SOL-USDT-SWAP",
        "direcao": "compra",
        "banda": (71.000, 71.600),
        "confirm_utc": dt.datetime(2026, 6, 30, 8, 57, tzinfo=dt.timezone.utc),  # BRT 05:57 -> UTC
        "busca_dias_antes": 10,
    },
]

# nota de escala: o gabarito usa "." como separador de milhar nos precos do
# BTC (ex.: "79.220" = 79220 USD, nao 79,22) -- as bandas acima ja estao na
# escala correta (checada contra o preco de fechamento real no instante do
# trade, impresso abaixo). SOL nao tem esse problema (preco de dezenas).


def overlap(a, b, c, d):
    """[a,b] intersecta [c,d]?"""
    return max(a, c) <= min(b, d)


def checar(caso):
    inst = caso["inst"]
    fim = caso["confirm_utc"] + dt.timedelta(hours=6)
    inicio = caso["confirm_utc"] - dt.timedelta(days=caso["busca_dias_antes"])

    print(f"\n{'='*70}\n{caso['nome']} -- {inst}")
    c1h = fetch_historico(inst, "1H", paginas=40)
    if not c1h:
        print("  [erro] sem candles")
        return
    ts_min = c1h[0]["ts"]
    ts_max = c1h[-1]["ts"]
    print(f"  historico disponivel: {dt.datetime.fromtimestamp(ts_min/1000, dt.timezone.utc)} "
          f"-> {dt.datetime.fromtimestamp(ts_max/1000, dt.timezone.utc)}")

    alvo_ts = int(caso["confirm_utc"].timestamp() * 1000)
    if alvo_ts < ts_min or alvo_ts > ts_max:
        print(f"  [fora da janela] confirm_utc={caso['confirm_utc']} nao esta no historico baixado -- pulando")
        return

    # preco de fechamento no instante do trade, pra checar escala/sanidade
    candle_no_trade = min(c1h, key=lambda c: abs(c["ts"] - alvo_ts))
    print(f"  candle mais proximo do trade real: {dt.datetime.fromtimestamp(candle_no_trade['ts']/1000, dt.timezone.utc)} "
          f"close={candle_no_trade['close']}")
    print(f"  banda do gabarito: {caso['banda']}")

    inicio_ts = int(inicio.timestamp() * 1000)
    fim_ts = int(fim.timestamp() * 1000)

    achados_lib, achados_home = [], []
    vistas_lib, vistas_home = set(), set()

    idx_inicio = None
    for idx, c in enumerate(c1h):
        if c["ts"] >= inicio_ts - WINDOW * 3600_000:
            idx_inicio = max(idx, WINDOW)
            break
    if idx_inicio is None:
        print("  [erro] nao achei indice de inicio")
        return

    for i in range(idx_inicio, len(c1h)):
        if c1h[i]["ts"] > fim_ts:
            break
        if c1h[i]["ts"] < inicio_ts:
            continue
        contexto = c1h[max(0, i - WINDOW + 1):i + 1]
        if len(contexto) < 60:
            continue

        for z in lib_zones_novas(contexto):
            chave = (z["tipo"], z["direcao"], round(z["top"], 2), round(z["bottom"], 2))
            if chave in vistas_lib:
                continue
            vistas_lib.add(chave)
            if z["direcao"] != caso["direcao"]:
                continue
            if overlap(z["bottom"], z["top"], *caso["banda"]):
                achados_lib.append({**z, "detectado_em": c1h[i]["ts"]})

        atr_1h = m.atr(contexto)
        for z in home_zones_novas(contexto, atr_1h):
            chave = (z["tipo"], z["direcao"], round(z["top"], 2), round(z["bottom"], 2))
            if chave in vistas_home:
                continue
            vistas_home.add(chave)
            if z["direcao"] != caso["direcao"]:
                continue
            if overlap(z["bottom"], z["top"], *caso["banda"]):
                achados_home.append({**z, "detectado_em": c1h[i]["ts"]})

    def fmt(lista, rotulo):
        print(f"\n  -- {rotulo}: {len(lista)} zona(s) na banda --")
        for z in lista:
            print(f"     {z['tipo']:>3} {z['direcao']:<6} [{z['bottom']:.4f}, {z['top']:.4f}] "
                  f"detectado ate {dt.datetime.fromtimestamp(z['detectado_em']/1000, dt.timezone.utc)}")
        if not lista:
            print("     (nenhuma zona da direcao/banda esperada apareceu)")

    fmt(achados_lib, "A) lib")
    fmt(achados_home, "B) caseiro")

    # densidade de ruido: quantas zonas TOTAIS (qualquer preco/direcao) cada
    # detector gerou na mesma janela de busca -- se for muito alto, um "hit"
    # na banda pode ser coincidencia, nao deteccao valida.
    def contar_por_tipo(vistas):
        n_ob = sum(1 for chave in vistas if chave[0] == "OB")
        n_fvg = sum(1 for chave in vistas if chave[0] == "FVG")
        return n_ob, n_fvg

    dias_janela = (fim_ts - inicio_ts) / 1000 / 3600 / 24
    ob_lib, fvg_lib = contar_por_tipo(vistas_lib)
    ob_home, fvg_home = contar_por_tipo(vistas_home)
    print(f"\n  -- densidade total na janela de busca ({dias_janela:.1f} dias) --")
    print(f"     lib:     {ob_lib} OB, {fvg_lib} FVG distintos (qualquer preco/direcao)")
    print(f"     caseiro: {ob_home} OB, {fvg_home} FVG distintos (qualquer preco/direcao)")


if __name__ == "__main__":
    for caso in CASOS:
        checar(caso)
