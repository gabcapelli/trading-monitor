"""
Estudo 32 -- drift pre-FOMC em cripto, PRE-REGISTRADO em 04/10/2026, antes
de calcular qualquer retorno.

HIPOTESE
--------
Em acoes, o S&P 500 sobe nas 24h antes do anuncio do FOMC (Lucca & Moench,
2015, "The Pre-FOMC Announcement Drift"). Se o mecanismo (premio por risco
resolvido no anuncio / posicionamento antes dele) vale para ativos de risco
em geral, o BTC deveria subir na mesma janela. Unica hipotese de calendario
com direcao esperada documentada; CPI e vencimento de opcoes ficaram de fora
por nao terem direcao esperada.

EVENTOS
-------
Reunioes REGULARES do FOMC de 2020 a 09/2026 (federalreserve.gov,
fomccalendars.htm e fomchistorical2020.htm), dia do comunicado = 2o dia.
Excluidas: reunioes nao agendadas de marco/2020 (e a regular cancelada) e
votos por notacao. Comunicado as 14:00 de Nova York = 18:00 UTC no horario de
verao dos EUA, 19:00 UTC fora dele. 53 eventos.

REGRA
-----
Comprado no perpetuo BTCUSDT da Binance da abertura da hora T-24h ate a
abertura da hora T (T = horario do comunicado). Sem stop.

MEDIDAS (% por evento)
----------------------
- `abs` (decide): retorno - 0.18% de custo - funding pago pelo comprado.
- `excesso` (decide): retorno - media dos retornos de 24h do BTC terminando
  na mesma hora UTC, nos 365 dias ANTERIORES ao evento (so passado; a linha
  de base de serie inteira vaza o futuro, ver estudo 23).
- Bootstrap por evento (cada evento uma observacao), 5000 reamostragens.

CRITERIO
--------
PASSA se `abs` E `excesso` tiverem IC95 inteiro acima de zero.
Poder: com 53 eventos e desvio de ~3% num dia de BTC, o IC tem cerca de
+-0.8%; so um drift acima de ~1% por evento sai do zero. O efeito em acoes
(~0.5%) estaria abaixo disso. NAO PASSA aqui = "nao ha drift grande".

DESCRITIVOS
-----------
ETHUSDT; cesta de peso igual dos 20 majors; 24h DEPOIS do comunicado (T ->
T+24h); 2020-2022 vs 2023-2026.

Uso (de dentro de monitor/):
    python replay_pre_fomc.py
"""

import random
import sys
from datetime import datetime, timedelta, timezone

import replay_deslistagem as R
from replay_ema_ribbon import CUSTO_RT

H, DIA = R.H, R.DIA
N_RESAMPLES, SEED = 5000, 42

# dia do comunicado (2o dia de cada reuniao regular)
FOMC = """
2020-01-29 2020-04-29 2020-06-10 2020-07-29 2020-09-16 2020-11-05 2020-12-16
2021-01-27 2021-03-17 2021-04-28 2021-06-16 2021-07-28 2021-09-22 2021-11-03 2021-12-15
2022-01-26 2022-03-16 2022-05-04 2022-06-15 2022-07-27 2022-09-21 2022-11-02 2022-12-14
2023-02-01 2023-03-22 2023-05-03 2023-06-14 2023-07-26 2023-09-20 2023-11-01 2023-12-13
2024-01-31 2024-03-20 2024-05-01 2024-06-12 2024-07-31 2024-09-18 2024-11-07 2024-12-18
2025-01-29 2025-03-19 2025-05-07 2025-06-18 2025-07-30 2025-09-17 2025-10-29 2025-12-10
2026-01-28 2026-03-18 2026-04-29 2026-06-17 2026-07-29 2026-09-16
""".split()


def _domingo(ano, mes, n):
    d = datetime(ano, mes, 1, tzinfo=timezone.utc)
    d += timedelta(days=(6 - d.weekday()) % 7)
    return d + timedelta(weeks=n - 1)


def horario_utc(dia):
    """14:00 de Nova York em ms UTC (horario de verao: 2o domingo de marco
    ao 1o domingo de novembro)."""
    d = datetime.strptime(dia, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    verao = _domingo(d.year, 3, 2) <= d < _domingo(d.year, 11, 1)
    return int((d + timedelta(hours=18 if verao else 19)).timestamp() * 1000)


def serie(sym, t0, t1):
    return R.klines("futures/um", sym, t0, t1)


def ret(s, a, b):
    ka, kb = s.get(a), s.get(b)
    return None if not ka or not kb else 100 * (kb[0] / ka[0] - 1)


def boot(v):
    v = [x for x in v if x is not None]
    if len(v) < 3:
        return None
    rng = random.Random(SEED)
    ms = sorted(sum(rng.choice(v) for _ in v) / len(v) for _ in range(N_RESAMPLES))
    return sum(v) / len(v), ms[int(0.025 * N_RESAMPLES)], ms[int(0.975 * N_RESAMPLES) - 1], len(v)


def linha(rot, v):
    b = boot(v)
    if not b:
        return f"  {rot:<46} (insuficiente)", None
    m, lo, hi, n = b
    return f"  {rot:<46} n={n:>3} media {m:+6.2f}% IC95 [{lo:+6.2f}, {hi:+6.2f}] | positivos {sum(x > 0 for x in v if x is not None)}", lo


def main(argv):
    T = [horario_utc(d) for d in FOMC]
    s_btc = serie("BTCUSDT", T[0] - 400 * DIA, T[-1] + 2 * DIA)
    s_eth = serie("ETHUSDT", T[0] - 2 * DIA, T[-1] + 2 * DIA)
    majors = {m: serie(m, T[0] - 2 * DIA, T[-1] + 2 * DIA) for m in R.MAJORS}

    linhas = []
    for dia, t in zip(FOMC, T):
        a = t - DIA
        r = ret(s_btc, a, t)
        if r is None:
            continue
        f = 100 * R.funding("BTCUSDT", a, t)
        base = [ret(s_btc, t - k * DIA - DIA, t - k * DIA) for k in range(1, 366)]
        base = [x for x in base if x is not None]
        cesta = [x for x in (ret(s, a, t) for s in majors.values()) if x is not None]
        linhas.append({
            "dia": dia, "ano": int(dia[:4]), "ret": r, "funding": f,
            "abs": r - 100 * CUSTO_RT - f,
            "excesso": r - sum(base) / len(base) if len(base) > 200 else None,
            "eth": ret(s_eth, a, t),
            "cesta": sum(cesta) / len(cesta) if cesta else None,
            "pos": ret(s_btc, t, t + DIA),
        })

    print(f"Eventos FOMC regulares com dado: {len(linhas)} de {len(FOMC)}\n")
    print("BTCUSDT perpetuo, comprado de T-24h ate T (T = comunicado)")
    print(linha("retorno bruto", [x["ret"] for x in linhas])[0])
    print(linha("funding pago", [x["funding"] for x in linhas])[0])
    out_a, lo_a = linha("ABSOLUTO (decide)", [x["abs"] for x in linhas])
    out_e, lo_e = linha("EXCESSO sobre 24h tipicas, 365d antes (decide)", [x["excesso"] for x in linhas])
    print(out_a)
    print(out_e)
    print("\nDescritivos")
    print(linha("ETHUSDT, T-24h -> T", [x["eth"] for x in linhas])[0])
    print(linha("cesta 20 majors, T-24h -> T", [x["cesta"] for x in linhas])[0])
    print(linha("BTC DEPOIS: T -> T+24h", [x["pos"] for x in linhas])[0])
    print(linha("BTC abs 2020-2022", [x["abs"] for x in linhas if x["ano"] <= 2022])[0])
    print(linha("BTC abs 2023-2026", [x["abs"] for x in linhas if x["ano"] >= 2023])[0])

    print("\n  Por evento:")
    for x in linhas:
        print(f"    {x['dia']}  BTC {x['ret']:+6.2f}%  abs {x['abs']:+6.2f}%  "
              f"excesso {x['excesso'] if x['excesso'] is not None else float('nan'):+6.2f}%  "
              f"depois {x['pos'] if x['pos'] is not None else float('nan'):+6.2f}%")

    ok = lo_a is not None and lo_e is not None and lo_a > 0 and lo_e > 0
    print(f"\n  DECISAO: {'PASSA' if ok else 'NAO PASSA'}")


if __name__ == "__main__":
    main(sys.argv[1:])
