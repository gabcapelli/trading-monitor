"""
Painel do repositorio: reescreve o README.md da raiz com o resumo de cada
estrategia, para ler direto no app do GitHub. So le os arquivos que os outros
scripts ja gravam (banco do diario e estados JSON) -- nenhuma chamada de API,
nenhuma conta nova. So biblioteca padrao do Python.

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


def main():
    agora = datetime.now(BRT)
    fech, ab_d, cand, recentes = diario(agora)
    un = _json("unlock_paper_state.json").get("trades", {}).values()
    un_ab = [t for t in un if t["status"] == "aberto"]
    un_fe = [t for t in un if t["status"] == "fechado"]
    nv = _json("novos_paper_state.json").get("trades", {}).values()
    nv_ab = [t for t in nv if t["status"] == "aberto"]
    nv_fe = [t for t in nv if t["status"] == "fechado"]
    sb_est = _json("sabado_paper_state.json")
    sab = sb_est.get("sabados", [])
    janela = sb_est.get("janela")      # cesta de sabado aberta (ainda nao registrada)

    media = lambda xs: sum(xs) / len(xs) if xs else None
    m_d, m_un, m_nv, m_sb = (media(fech), media([t["hedge"] for t in un_fe]),
                             media([t["com_stop"] for t in nv_fe]), media([s["principal"] for s in sab]))

    L = ["# Painel de estratégias", "",
         f"_Atualizado em {agora:%d/%m %H:%M} (Brasília), a cada hora. Tudo em papel: nenhuma ordem é enviada._", ""]

    L += ["## Precisa de você", ""]
    if recentes:
        L += [f"- **#{i}** {par.replace('/USDT', '')} Setup {st}, {dr}, R:R {rr:.2f} ({dt[8:10]}/{dt[5:7]} {dt[11:]})"
              for i, dt, par, st, dr, rr in recentes]
        L.append(f"- → marcar status e checks em [sinais.md](claude/sinais.md)")
    else:
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
          f"| [Sábado](claude/sabado-paper.md) | {1 if janela else 0} | {len(sab)}/104 | {'—' if m_sb is None else _pct(m_sb)} |",
          (f"| [Setup A/B](claude/estudos-avulsos.md#setups-ab--encerrado-em-25092026) · encerrado | — | {len(fech)} | "
           f"{'—' if m_d is None else f'{m_d:+.2f}R'} |" if M.SETUP_AB_ENCERRADO else
           f"| [Setup A/B](claude/sinais.md) | {ab_d}/2 | {len(fech)} (meta 30) | "
           f"{'—' if m_d is None else f'{m_d:+.2f}R'} |"),
          "",
          "<sub>Média: Setup A/B em R por trade; desbloqueio com hedge; perpétuo novo com stop; "
          "sábado por fim de semana. Fechados = amostra atual / amostra mínima para reavaliar.</sub>"]

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
