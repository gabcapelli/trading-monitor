#!/usr/bin/env python3
"""
Detalha os trades individuais de UM par nos dois detectores do Setup C
(replay_setup_c.py), pra checar se uma expectancia agregada positiva vem de
varios trades consistentes ou de 1-2 outliers dominando a soma.

Motivo de existir: em 11/09/2026 o agregado de XRP saiu com IC 95% bootstrap
inteiramente positivo nos dois detectores -- mas so 1-2 trades (ver
claude/setup-c-testes.md) respondiam por 43-60% da soma. Sem esse detalhe por
trade, um IC positivo no agregado pode enganar.

Uso (da raiz do repo, com PYTHONPATH=monitor):
    PYTHONPATH=monitor python monitor/inspect_pair_setup_c.py XRP-USDT-SWAP
"""
import sys

import fetch_and_check as m  # noqa: E402
from replay_setup_c import fetch_historico, replay_setup_c  # noqa: E402

if __name__ == "__main__":
    inst = sys.argv[1] if len(sys.argv) > 1 else "XRP-USDT-SWAP"
    c1h = fetch_historico(inst, "1H", paginas=22)
    c4h = fetch_historico(inst, "4H", paginas=16)
    print(f"{m.pair_label(inst)}: {len(c1h)} candles 1h, {len(c4h)} candles 4h")

    for rotulo, detector in [("A) lib", "lib"), ("B) caseiro", "home")]:
        sinais = replay_setup_c(c1h, c4h, detector)
        aceitos = sorted([s for s in sinais if s["aceito"] and s["resultado"] is not None],
                         key=lambda s: s["ts"])
        print(f"\n=== {rotulo} -- {len(aceitos)} trades aceitos ===")
        for s in aceitos:
            print(f"  {m.fmt_brt(s['ts'])} | {s['tipo']:>3} {s['direcao']:<6} | "
                  f"entrada {s['entrada']:.4f} stop {s['stop']:.4f} alvo {s['alvo']:.4f} "
                  f"rr {s['rr']:.2f} | resultado {s['resultado']:+.2f}R")
        if not aceitos:
            continue
        soma = sum(s["resultado"] for s in aceitos)
        print(f"  soma = {soma:+.2f}R em {len(aceitos)} trades | media = {soma/len(aceitos):+.3f}R")
