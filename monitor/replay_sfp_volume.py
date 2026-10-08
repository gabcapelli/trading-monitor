"""
Estudo 60 -- SFP / Turtle Soup (estudo 57) com UM filtro de volume.
PRE-REGISTRADO em 08/10/2026, antes de rodar. Tentativa unica: se nao passar,
o SFP fica encerrado, sem segunda rodada de filtros.

POR QUE ESTE FILTRO (e so ele)
------------------------------
A tese do SFP e que o pavio consome o estoque de stops amontoado alem da
maxima/minima. Se for verdade, o candle do pavio tem volume anormal (os stops
sendo executados). O filtro testa o mecanismo da propria ideia; nao foi
escolhido olhando o resultado. Ressalva: os sinais sem filtro ja foram vistos
no estudo 57 (1d com excesso de +0.07R, IC encostando em zero).

REGRA: identica ao estudo 57 (replay_sfp.py), mais:
- volume em dolar do candle do sinal >= 2x a media dos 20 candles anteriores.

CRITERIO: identico ao estudo 57 (1d e 4h, IC 97.5%, n >= 200, R liquido e
excesso sobre placebo de mesmo risco com IC > 0, duas metades > 0).

Uso (de dentro de monitor/):
    python replay_sfp_volume.py
"""

import sys

import replay_sfp as S

MULT_VOL = 2.0

_sinais_57 = S.sinais


def sinais(b):
    out = []
    for i, lado, pavio in _sinais_57(b):
        mv = sum(x[5] for x in b[i - S.N:i]) / S.N
        if mv > 0 and b[i][5] >= MULT_VOL * mv:
            out.append((i, lado, pavio))
    return out


if __name__ == "__main__":
    S.sinais = sinais
    S.main(sys.argv[1:])
