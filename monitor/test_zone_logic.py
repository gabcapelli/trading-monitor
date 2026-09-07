#!/usr/bin/env python3
"""
Testes de regressao para a logica de mapeamento de zona (try_map_new_zone) e
deteccao de pivo (find_confirmed_pivots) de monitor/fetch_and_check.py.

Objetivo especifico: travar as duas classes de bug encontradas e corrigidas
em 07/09/2026 (ver CHANGELOG no topo de fetch_and_check.py), para que uma
edicao futura nao reintroduza silenciosamente o mesmo erro.

Rodar com: python3 -m pytest tests/test_zone_logic.py -v
(ou, sem pytest instalado: python3 tests/test_zone_logic.py)
"""

import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "monitor"))

import fetch_and_check as m  # noqa: E402


def make_candle(ts, o, h, l, c, confirm="1"):
    return {"ts": ts, "open": o, "high": h, "low": l, "close": c,
            "vol": 1.0, "volCcyQuote": 1.0, "confirm": confirm}


def candles_uptrend_no_recent_low_pivot():
    """
    Constroi uma sequencia de candles 1h que:
    - tem um topo fractal confirmado claro (resistencia) varias horas atras;
    - o preco ja fechou ACIMA dessa resistencia (rompimento real);
    - NAO tem nenhum fundo fractal confirmado nas ultimas horas (pullbacks
      recentes rasos demais para formar pivo de 3 candles de cada lado) --
      e exatamente o cenario que expunha o bug #1 (checava lows_1h em vez
      de highs_1h para tendencia de alta).
    """
    base = 1_000_000_000_000
    candles = []
    price = 100.0
    # sobe com pequenas oscilacoes, formando um topo fractal em torno do candle 10
    seq = [100, 101, 102, 103, 104, 106, 104.5, 103.5, 104.2, 104.8,
           106.5,  # topo fractal (idx 10) -- maior que os 3 de cada lado
           105.8, 105.9, 106.0, 106.1,
           # pullbacks rasos demais para formar fundo fractal (sempre subindo)
           106.3, 106.5, 106.7, 106.9, 107.1,
           107.3]  # fechamento final ACIMA do topo fractal (106.5) -- rompimento
    for i, c in enumerate(seq):
        o = seq[i - 1] if i > 0 else c
        h = max(o, c) + 0.05
        l = min(o, c) - 0.05
        candles.append(make_candle(base + i * 3_600_000, o, h, l, c))
    return candles


def test_bug1_setup_a_detects_breakout_without_recent_low_pivot():
    """
    Regressao do bug #1: mesmo sem fundo fractal confirmado recente, um
    rompimento real de resistencia em tendencia de alta DEVE gerar uma
    zona candidata de Setup A. Antes da correcao, isso retornava None
    porque o codigo checava `lows_1h` (vazio ou irrelevante) em vez de
    `highs_1h` (a lista que de fato define o nivel de rompimento).
    """
    candles_1h = candles_uptrend_no_recent_low_pivot()
    candles_4h = candles_1h  # simplificacao: mesma serie serve para o teste de trend
    atr_1h = 1.0  # valor fixo, so precisa ser truthy

    highs_1h, lows_1h, _ = m.find_confirmed_pivots(candles_1h)
    assert len(highs_1h) >= 1, "pre-condicao do teste falhou: esperava um topo fractal confirmado"

    zone = m.try_map_new_zone("alta", candles_1h, candles_4h, atr_1h)

    assert zone is not None, (
        "BUG #1 REGREDIU: Setup A nao detectou rompimento de resistencia "
        "quando nao havia fundo fractal confirmado recente."
    )
    assert zone["setup"] == "A"
    assert zone["direction"] == "compra"
    assert zone["level"] == highs_1h[-1][1], (
        "zona deveria usar o ultimo topo fractal (highs_1h) como nivel de referencia"
    )


def candles_for_stale_4h_scan():
    """
    Dois swings 4h de topo, com valores de "high" explicitos e sem empate
    (evita que a checagem `== max(seg)` do pivo capture dois candles ao
    mesmo tempo, o que mascararia o cenario do teste):
    - idx 5: topo MADURO (>= STALE_4H_CANDLES candles depois dele) e alto
      (200) -- perto do preco atual no fechamento do ultimo candle.
    - idx 20: topo IMATURO (< STALE_4H_CANDLES candles depois dele) e mais
      baixo (150) -- nao deveria ser escolhido, mas expunha o bug #2 porque
      o loop desistia nele (por ser o mais recente) sem chegar ao maduro.
    Preco final (ultimo candle) fecha perto de 200, para so passar no filtro
    de distancia da zona se o swing MADURO (idx 5) for de fato considerado.
    """
    base = 2_000_000_000_000
    n = 30
    # baseline com leve variacao (seno) para evitar empates de "high" entre
    # candles planos -- mantido bem abaixo dos dois picos (97-103 vs 150/200)
    highs = [100.0 + 3.0 * math.sin(i * 0.7) for i in range(n)]
    highs[5] = 200.0    # topo maduro
    highs[20] = 150.0   # topo imaturo, mais baixo -- nunca deve "vencer" por engano
    closes = [99.0 + 3.0 * math.sin(i * 0.7) for i in range(n)]
    closes[-1] = 199.0  # fechamento final perto do topo MADURO, longe do imaturo

    candles = []
    for i in range(n):
        h = highs[i]
        c = closes[i]
        o = c - 1.0
        l = min(o, c) - 1.0
        candles.append(make_candle(base + i * 4 * 3_600_000, o, h, l, c))
    return candles


def test_bug2_setup_b_scans_past_immature_swing():
    """
    Regressao do bug #2: o mapeamento de Setup B deve continuar procurando
    um swing 4h maduro mesmo quando o mais recente ainda nao maturou,
    em vez de desistir no primeiro candidato encontrado.
    """
    candles_4h = candles_for_stale_4h_scan()
    candles_1h = candles_4h  # simplificacao para o teste

    highs_4h, lows_4h, closed_4h = m.find_confirmed_pivots(candles_4h)
    # o baseline com seno pode gerar pivos pequenos legitimos alem dos dois
    # picos que nos interessam -- filtramos so os picos > 140 para a pre-condicao
    big_peaks = [(i, p) for i, p in highs_4h if p > 140]
    assert big_peaks == [(5, 200.0), (20, 150.0)], (
        f"pre-condicao do teste falhou: esperava os dois picos (5,200.0) e "
        f"(20,150.0), achou {big_peaks} (todos os pivos: {highs_4h})"
    )

    # trend "lateral" forca o codigo a pular a logica de Setup A e cair no Setup B
    # atr_1h=2.0 -> zona de distancia (3*0.25*2.0=1.5) cobre a folga de 1.0
    # entre o fechamento final (199) e o topo maduro (200)
    zone = m.try_map_new_zone("lateral", candles_1h, candles_4h, atr_1h=2.0)

    assert zone is not None, (
        "BUG #2 REGREDIU: Setup B nao encontrou o swing 4h maduro porque parou "
        "no primeiro swing (imaturo) da lista."
    )
    assert zone["setup"] == "B"
    mature_level = highs_4h[0][1]  # o mais antigo confirmado, portanto o mais maduro
    assert zone["level"] == mature_level, (
        f"esperava o swing maduro mais antigo ({mature_level}), "
        f"achou {zone['level']} -- provavel regressao do bug do break/continue"
    )


def _run_all():
    tests = [v for k, v in globals().items() if k.startswith("test_")]
    failed = 0
    for t in tests:
        try:
            t()
            print(f"PASS  {t.__name__}")
        except AssertionError as e:
            failed += 1
            print(f"FAIL  {t.__name__}: {e}")
    print(f"\n{len(tests) - failed}/{len(tests)} testes passaram")
    if failed:
        sys.exit(1)


if __name__ == "__main__":
    _run_all()
