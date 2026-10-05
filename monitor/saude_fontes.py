"""
Checagem de saude da fapi da Binance (via proxy), da qual dependem os registros
em papel (unlock_paper.py, novos_paper.py, sabado_paper.py).

Por que existe: em 10/2026 o proxy da Vercel ficou fora por dias (deploy
automatico publicando a raiz do repo) e ninguem soube -- os scripts tratam
falha de rede como "dado pendente", o workflow termina com sucesso, e o tipo
do contrato e o funding ficam "?"/pendentes em silencio.

O que faz, a cada execucao do workflow:
- testa os tres endpoints que o proxy repassa (klines, fundingRate, exchangeInfo);
- grava o estado em monitor/saude_fontes.json (o painel le de la);
- manda UM push no ntfy na transicao: falha confirmada (2 execucoes seguidas,
  para nao avisar soluco de deploy) e recuperacao.
Nunca falha o workflow (sai sempre com 0). So biblioteca padrao.
"""

import json
import os
import sys
from datetime import datetime, timedelta, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import fetch_and_check as M
import unlock_paper as U

ARQ = os.path.join(os.path.dirname(os.path.abspath(__file__)), "saude_fontes.json")
FALHAS_PARA_AVISAR = 2


def checar_fapi():
    """None se ok; senao, texto curto do que falhou."""
    if not os.environ.get("UNLOCK_PAPER_FAPI"):
        return "secret UNLOCK_PAPER_FAPI vazio (fapi direta da 451 nos EUA)"
    k = U._json(f"{U.FAPI}/klines?symbol=BTCUSDT&interval=1h&limit=1")
    if not (isinstance(k, list) and k):
        return "klines sem resposta"
    f = U._json(f"{U.FAPI}/fundingRate?symbol=BTCUSDT&limit=1")
    if not (isinstance(f, list) and f):
        return "fundingRate sem resposta"
    e = U._json(f"{U.FAPI}/exchangeInfo")
    if not (isinstance(e, dict) and e.get("symbols")):
        return "exchangeInfo sem resposta"
    return None


def main():
    est = json.load(open(ARQ, encoding="utf-8")) if os.path.exists(ARQ) else {}
    fapi = est.get("fapi", {"ok": True, "falhas": 0, "avisado": False})
    agora = datetime.now(timezone(timedelta(hours=-3))).strftime("%d/%m %H:%M (Brasília)")
    try:
        erro = checar_fapi()
    except Exception as ex:   # qualquer surpresa conta como falha, nunca derruba o job
        erro = f"excecao: {ex}"

    if erro is None:
        if fapi.get("avisado"):
            M.send_ntfy("Proxy da fapi voltou",
                        f"Fora desde {fapi.get('desde')}. Os registros em papel reconsultam "
                        "tipo e funding sozinhos nas proximas execucoes.")
        fapi = {"ok": True, "falhas": 0, "avisado": False, "ultimo_ok": agora}
        print("[saude] fapi ok")
    else:
        fapi["falhas"] = fapi.get("falhas", 0) + 1
        if fapi.get("ok", True):
            fapi["desde"] = agora
        fapi.update({"ok": False, "erro": erro})
        print(f"::warning::fapi/proxy falhou ({fapi['falhas']}x seguidas): {erro}")
        if fapi["falhas"] >= FALHAS_PARA_AVISAR and not fapi.get("avisado"):
            M.send_ntfy("Proxy da fapi fora",
                        f"{erro}. Desde {fapi['desde']}. Registros em papel ficam com tipo '?' e "
                        "funding pendente ate voltar. Ver proxy-vercel/ e CLAUDE.md.", priority="high")
            fapi["avisado"] = True
    est["fapi"] = fapi
    with open(ARQ, "w", encoding="utf-8", newline="\n") as f:
        json.dump(est, f, indent=1, ensure_ascii=False)


if __name__ == "__main__":
    main()
