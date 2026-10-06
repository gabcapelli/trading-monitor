"""
Painel do repositorio: reescreve o README.md da raiz com o resumo de cada
estrategia, para ler direto no app do GitHub. Le os arquivos que os outros
scripts ja gravam (banco do diario e estados JSON); a unica chamada de API e um
ticker/price da fapi (via proxy) para marcar os abertos a mercado -- se falhar,
o painel sai igual, so sem o preco atual. So biblioteca padrao do Python.

Rode sem argumento (o workflow horario chama assim, depois dos registros).
"""

import json
import os
import sqlite3
import sys
from datetime import datetime, timedelta, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import fetch_and_check as M
import unlock_paper as U

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
README = os.path.join(RAIZ, "README.md")
DB = os.path.join(RAIZ, "claude", "trade_journal.db")
BRT = timezone(timedelta(hours=-3))
RECENTE_H = 24          # candidato mais velho que isso ja passou do ponto de entrada


def _json(nome):
    p = os.path.join(RAIZ, "monitor", nome)
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {}


def _data(dia):
    return (datetime(1970, 1, 1) + timedelta(days=dia)).strftime("%d/%m")


def _pct(x):
    return f"{100 * x:+.2f}%"


def diario(agora):
    """Setup A/B: gate dos 30 (resultado_r) e candidatos esperando o Gabriel."""
    c = sqlite3.connect(DB)
    fech = [r[0] for r in c.execute("SELECT resultado_r FROM trades WHERE status = 'entrado' "
                                    "AND conta_para_validacao = 1 AND resultado_r IS NOT NULL")]
    abertos = c.execute("SELECT COUNT(*) FROM trades WHERE status = 'entrado' AND resultado_r IS NULL").fetchone()[0]
    cand = c.execute("SELECT id, criado_em, par, setup, direcao, rr_sugerido FROM trades "
                     "WHERE status = 'candidato' ORDER BY id").fetchall()
    c.close()
    limite = (agora - timedelta(hours=RECENTE_H)).strftime("%Y-%m-%d %H:%M")
    recentes = [x for x in cand if x[1] >= limite]
    return fech, abertos, cand, recentes


def precos():
    """Preco atual de todos os perpetuos numa chamada so; {} se a fapi/proxy falhar."""
    r = U._json(f"{U.FAPI}/ticker/price") or []
    return {x["symbol"]: float(x["price"]) for x in r if isinstance(x, dict) and "price" in x}


def _hm(ms):
    return datetime.fromtimestamp(ms / 1000, BRT).strftime("%d/%m %H:%M")


def hoje_e_abertos(hoje, un, nv, mt, ct, sb_est, px):
    """Linhas de 'Hoje' (o que abriu/fechou desde as 21h de Brasilia = dia UTC) e
    'Abertos agora' (cada posicao aberta a preco de mercado, bruto)."""
    dia_ms = lambda ms: ms // 86_400_000
    curto = lambda s: s.replace("USDT", "")
    ev = []
    for t in un:
        if t["status"] == "aberto" and t["entrada"] == hoje:
            ev.append(f"Desbloqueio: vendeu {curto(t['par'])} a {t['px_in']:g} (desbloqueio {_data(t['t0'])})")
        if t["status"] == "fechado" and t["t0"] == hoje:
            ev.append(f"Desbloqueio: recomprou {curto(t['par'])}: puro {_pct(t['puro'])}, com hedge {_pct(t['hedge'])}"
                      if "hedge" in t else f"Desbloqueio: recomprou {curto(t['par'])} (funding pendente)")
    for t in nv:
        if t["status"] == "aberto" and t["entrada"] == hoje:
            ev.append(f"Perpétuo novo: vendeu {curto(t['par'])} a {t['px_in']:g} (stop {t['stop_px']:g})")
        if t["status"] == "fechado" and t.get("dia_saida_stop") == hoje:
            ev.append(f"Perpétuo novo: recomprou {curto(t['par'])}: com stop {_pct(t['com_stop'])}")
    for nome, ts in (("Monitoring Tag", mt), ("Rompimento 48h", ct)):
        for t in ts:
            if t["status"] in ("aberto", "fechado") and dia_ms(t["entrada_ts"]) == hoje:
                lado = "comprou" if t.get("lado", -1) > 0 else "vendeu"
                ev.append(f"{nome}: {lado} {curto(t['sym'])} a {t['p_in']:g} ({_hm(t['entrada_ts'])})")
            if t["status"] == "fechado" and dia_ms(t["saida_ts"]) == hoje:
                ev.append(f"{nome}: fechou {curto(t['sym'])}: líquido {t['liq']:+.2f}%")
    janela = sb_est.get("janela")
    if janela and janela["dia"] == hoje:
        ev.append("Sábado: comprou a cesta")
    for s in sb_est.get("sabados", []):
        if s["dia"] + 1 == hoje:
            ev.append(f"Sábado: vendeu a cesta: {_pct(s['principal'])}")

    linhas = []          # (estrategia, ativo, desde, entrada, retorno bruto ou None, obs)
    ret = lambda sym, p0, lado: (lado * (px[sym] / p0 - 1)) if sym in px and p0 else None
    for t in un:
        if t["status"] != "aberto":
            continue
        r = ret(t["par"], t["px_in"], -1)
        rc = [px[s] / p0 - 1 for s, p0 in t["cesta_in"].items() if s in px and p0]
        obs = f"com hedge {_pct(r + sum(rc) / len(rc))}; " if r is not None and rc else ""
        linhas.append(("Desbloqueio", t["par"], _data(t["entrada"]), t["px_in"], r,
                       obs + f"recompra {_data(t['t0'])}"))
    for t in nv:
        if t["status"] == "aberto":
            linhas.append(("Perpétuo novo", t["par"], _data(t["entrada"]), t["px_in"], ret(t["par"], t["px_in"], -1),
                           f"stop {t['stop_px']:g}; saída {_data(t['entrada'] + 30)}"))
    for nome, ts in (("Monitoring Tag", mt), ("Rompimento 48h", ct)):
        for t in ts:
            if t["status"] == "aberto":
                lado = t.get("lado", -1)
                linhas.append((nome, t["sym"], _hm(t["entrada_ts"]), t["p_in"], ret(t["sym"], t["p_in"], lado),
                               f"{'comprado' if lado > 0 else 'vendido'}; saída {_hm(t['saida_ts'])}"))
    if janela and janela.get("precos"):
        rs = [px[s] / p0 - 1 for s, p0 in janela["precos"].items() if s in px and p0]
        linhas.append(("Sábado", f"cesta ({len(janela['precos'])})", _data(janela["dia"] - 1) + " 21:00", None,
                       sum(rs) / len(rs) if rs else None, "comprado; saída sábado 21h"))

    L = ["", "## Hoje", "", "<sub>Desde o fechamento das 21h (Brasília).</sub>", ""]
    L += [f"- {e}" for e in ev] if ev else ["_Nada abriu nem fechou._"]
    if linhas:
        L += ["", "## Abertos agora", "", "| Estratégia | Ativo | Desde | Entrada | Agora | Resultado | Obs. |",
              "|---|---|---|---|---|---|---|"]
        for est, sym, desde, p0, r, obs in sorted(linhas, key=lambda x: (x[0], -(x[4] or 0))):
            agora_px = f"{px[sym]:g}" if sym in px else "—"
            res = "—" if r is None else (f"**{_pct(r)}**" if abs(r) >= 0.10 else _pct(r))
            L.append(f"| {est} | {curto(sym)} | {desde} | {'—' if p0 is None else f'{p0:g}'} | "
                     f"{agora_px} | {res} | {obs} |")
        L += ["", "<sub>Resultado a preço de mercado, bruto (sem custo nem funding), já no lado da posição: "
                  "positivo = a favor. Em negrito, movimentos de 10% ou mais. Com hedge = venda + cesta dos majors.</sub>"
              if px else "<sub>Sem preço atual: a fapi/proxy não respondeu nesta execução.</sub>"]
    return L


def main():
    agora = datetime.now(BRT)
    fech, ab_d, cand, recentes = diario(agora)
    un = _json("unlock_paper_state.json").get("trades", {}).values()
    un_ab = [t for t in un if t["status"] == "aberto"]
    un_fe = [t for t in un if t["status"] == "fechado"]
    nv = _json("novos_paper_state.json").get("trades", {}).values()
    nv_ab = [t for t in nv if t["status"] == "aberto"]
    nv_fe = [t for t in nv if t["status"] == "fechado"]
    mt = [t for t in _json("monitoring_paper_state.json").get("trades", {}).values() if t["braco"] == "principal"]
    mt_ab = [t for t in mt if t["status"] == "aberto"]
    mt_fe = [t for t in mt if t["status"] == "fechado"]
    ct = _json("continuacao_paper_state.json").get("trades", [])
    ct_ab = [t for t in ct if t["status"] == "aberto"]
    ct_fe = [t for t in ct if t["status"] == "fechado"]
    sb_est = _json("sabado_paper_state.json")
    sab = sb_est.get("sabados", [])
    janela = sb_est.get("janela")      # cesta de sabado aberta (ainda nao registrada)

    media = lambda xs: sum(xs) / len(xs) if xs else None
    m_d, m_un, m_nv, m_sb = (media(fech), media([t["hedge"] for t in un_fe]),
                             media([t["com_stop"] for t in nv_fe]), media([s["principal"] for s in sab]))
    m_mt = media([t["liq"] for t in mt_fe])
    m_ct = media([t["liq"] for t in ct_fe])

    L = ["# Painel de estratégias", "",
         f"_Atualizado em {agora:%d/%m %H:%M} (Brasília), a cada hora. Tudo em papel: nenhuma ordem é enviada._", ""]

    L += ["## Precisa de você", ""]
    fapi = _json("saude_fontes.json").get("fapi", {})
    fapi_fora = bool(fapi) and not fapi.get("ok", True) and fapi.get("falhas", 0) >= 2
    if fapi_fora:
        L += [f"- **Proxy da fapi fora** desde {fapi.get('desde')} ({fapi.get('erro')}): registros em papel "
              "com tipo e funding pendentes até voltar. Ver `proxy-vercel/`.", ""]
    if recentes:
        L += [f"- **#{i}** {par.replace('/USDT', '')} Setup {st}, {dr}, R:R {rr:.2f} ({dt[8:10]}/{dt[5:7]} {dt[11:]})"
              for i, dt, par, st, dr, rr in recentes]
        L.append(f"- → marcar status e checks em [sinais.md](claude/sinais.md)")
    elif not fapi_fora:
        L.append("_Nada pendente._")
    antigos = len(cand) - len(recentes)
    if antigos:
        L += ["", f"<sub>{antigos} candidato(s) mais antigo(s) seguem sem decisão em sinais.md.</sub>"]

    L += ["", "## Estratégias", "",
          "| Estratégia | Abertos | Fechados | Média |", "|---|---|---|---|",
          f"| [Desbloqueio](claude/unlock-paper.md) | {len(un_ab)} | {len(un_fe)}/150 | "
          f"{'—' if m_un is None else _pct(m_un)} |",
          f"| [Perpétuo novo](claude/novos-paper.md) | {len(nv_ab)} | {len(nv_fe)}/100 | "
          f"{'—' if m_nv is None else _pct(m_nv)} |",
          f"| [Rompimento 48h](claude/continuacao-paper.md) · exceção | {len(ct_ab)} | {len(ct_fe)}/300 | "
          f"{'—' if m_ct is None else _pct(m_ct / 100)} |",
          f"| [Monitoring Tag](claude/monitoring-paper.md) | {len(mt_ab)} | {len({t['anuncio_id'] for t in mt_fe})}/24 | "
          f"{'—' if m_mt is None else _pct(m_mt / 100)} |",
          f"| [Sábado](claude/sabado-paper.md) | {1 if janela else 0} | {len(sab)}/104 | {'—' if m_sb is None else _pct(m_sb)} |",
          (f"| [Setup A/B](claude/estudos-avulsos.md#setups-ab--encerrado-em-25092026) · encerrado | — | {len(fech)} | "
           f"{'—' if m_d is None else f'{m_d:+.2f}R'} |" if M.SETUP_AB_ENCERRADO else
           f"| [Setup A/B](claude/sinais.md) | {ab_d}/2 | {len(fech)} (meta 30) | "
           f"{'—' if m_d is None else f'{m_d:+.2f}R'} |"),
          "",
          "<sub>Média: Setup A/B em R por trade; desbloqueio com hedge; perpétuo novo com stop; "
          "Monitoring Tag líquida (fechados em anúncios); sábado por fim de semana. Fechados = amostra atual / amostra mínima para reavaliar.</sub>"]

    hoje = int(agora.timestamp()) // 86400
    L += hoje_e_abertos(hoje, list(un), list(nv), mt, ct, sb_est, precos())

    prox = []            # (dia, texto), os mais proximos primeiro
    for d in sorted({t["t0"] for t in un_ab}):
        prox.append((d, f"Desbloqueio: recompra de {', '.join(sorted(t['par'][:-4] for t in un_ab if t['t0'] == d))}"))
    cal = _json("unlock_paper_state.json").get("calendario", {})
    hoje = int(agora.timestamp()) // 86400
    ja = {f"{t['par']}|{t['t0']}" for t in un}
    fut = sorted((c["t0"] - U.ANTES, c["par"][:-4]) for k, c in cal.items()
                 if k not in ja and c["t0"] - U.ANTES > hoje and c["frac"] >= U.FRAC_INS)
    if fut:
        prox.append((fut[0][0], f"Desbloqueio: venda prevista de {', '.join(p for d, p in fut if d == fut[0][0])}"))
    prox += [(t["entrada"] + 30, f"Perpétuo novo: saída de {t['par'][:-4]} (stop {t['stop_px']:g})") for t in nv_ab]
    if janela:
        prox.append((janela["dia"], "Sábado: saída da cesta (21h) e resultado"))
    else:              # proxima entrada: fechamento de sexta = 00:00 UTC de sabado
        sab_prox = hoje + (5 - datetime(1970, 1, 1).weekday() - hoje) % 7   # 5 = sabado
        prox.append((sab_prox - 1, "Sábado: entrada da cesta (21h)"))
    prox = [f"- {_data(d)} · {txt}" for d, txt in sorted(prox)[:4]]
    if prox:
        L += ["", "## Próximos eventos", ""] + prox

    L += ["", "## Outros", "",
          "- [Situação dos 10 pares agora](claude/status-simulacao.md) · [calibração mecânica](claude/calibracao.md)",
          "- [Estudos encerrados](claude/estudos-avulsos.md) · [auditoria v6](claude/auditoria-v6.md)",
          "- [Como o monitor funciona](monitor/README.md) · [contexto do projeto](CLAUDE.md)", ""]
    open(README, "w", encoding="utf-8", newline="\n").write("\n".join(L))


if __name__ == "__main__":
    main()
