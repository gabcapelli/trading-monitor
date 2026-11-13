"""
Estudo 87 -- robustez DESCRITIVA, escrita DEPOIS do resultado (13/11/2026).
Nao decide nada: so mostra de onde vem a media do estudo pre-registrado.
"""

import sys
from datetime import datetime, timezone

import replay_latencia as RL
import replay_launchpool as LP


def linha(rot, ts, chave="liq"):
    print(f"  {rot:<46} {RL.fmt(RL.boot(ts, chave))}")


def main():
    trades = [t for t, _ in (LP.montar(e) for e in LP.eventos()[0]) if t]
    trades.sort(key=lambda t: t["ts"])
    print("Trade a trade (data do aviso, horas ate o farming, bruto, liquido, excesso):")
    for t in trades:
        d = datetime.fromtimestamp(t["ts"] / 1000, timezone.utc).strftime("%Y-%m-%d")
        print(f"  {d} {t['horas']:6.1f}h bruto {t['bruto']:+6.2f} liq {t['liq']:+6.2f} exc {t['excesso']:+6.2f}  {t['titulo'][12:50]}")
    por_liq = sorted(trades, key=lambda t: t["liq"])
    por_exc = sorted(trades, key=lambda t: t["excesso"])
    meio = len(trades) // 2
    print("\nRecortes (liquido | excesso):")
    for rot, sel in (("todos", trades), ("1a metade", trades[:meio]), ("2a metade", trades[meio:]),
                     ("ate 24h de espera", [t for t in trades if t["horas"] <= 24]),
                     ("mais de 24h de espera", [t for t in trades if t["horas"] > 24]),
                     ("2020-21", [t for t in trades if t["ts"] < 1640995200000]),
                     ("2022-23", [t for t in trades if 1640995200000 <= t["ts"] < 1704067200000]),
                     ("2024", [t for t in trades if 1704067200000 <= t["ts"] < 1735689600000]),
                     ("2025-26", [t for t in trades if t["ts"] >= 1735689600000])):
        linha(rot + " liq", sel)
        linha(rot + " exc", sel, "excesso")
    linha("sem os 3 maiores liquidos", por_liq[:-3])
    linha("sem os 5 maiores liquidos", por_liq[:-5])
    linha("sem os 3 maiores excessos (excesso)", por_exc[:-3], "excesso")
    linha("sem os 5 maiores excessos (excesso)", por_exc[:-5], "excesso")
    soma = sum(t["liq"] for t in trades)
    print(f"\n  soma do liquido {soma:+.1f}% | os 5 maiores somam {sum(t['liq'] for t in por_liq[-5:]):+.1f}%")


if __name__ == "__main__":
    main()
    sys.exit(0)
