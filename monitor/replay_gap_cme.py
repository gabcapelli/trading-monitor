"""
Estudo 35 -- "o gap da CME sempre fecha" no BTC, PRE-REGISTRADO em
04/10/2026, antes de calcular qualquer retorno.

HIPOTESE (alegacao popular)
---------------------------
A CME (futuro de BTC) fecha no fim de semana; o BTC continua negociando 24/7.
Quando a CME reabre no domingo com o preco longe do fechamento de sexta, o
preco "volta" para fechar o gap. Testado como regra operavel no perpetuo.

HORARIOS
--------
CME: fecha sexta 16:00 de Chicago, reabre domingo 17:00. Em UTC: 21:00 / 22:00
no horario de verao dos EUA (2o domingo de marco a 1o domingo de novembro),
22:00 / 23:00 fora dele.
Preco: perpetuo BTCUSDT da Binance, candles de 1h (data.binance.vision).
F = abertura da hora do fechamento da CME na sexta; P0 = abertura da hora da
reabertura no domingo. Gap = P0 / F - 1.

REGRA
-----
- Opera se |gap| >= 1% (gap menor que ~5x o custo nao paga o trade).
- Direcao: na direcao do fechamento (gap para cima -> vende; para baixo ->
  compra), entrada em P0.
- Alvo: F (ordem limitada; tocou F em qualquer hora a partir da entrada, sai
  em F -- a entrada e na abertura, entao qualquer toque e posterior).
- Saida por tempo: abertura da hora do fechamento da CME na sexta seguinte.
- Sem stop.

MEDIDAS (% por evento)
----------------------
- `abs` (decide): retorno - 0.18% - funding pago.
- `excesso` (decide): retorno - d x deriva media do BTC na mesma duracao, nos
  365 dias ANTERIORES (so passado). Os dois lados operam, entao o beta ja
  tende a se cancelar; o excesso confere.
- Bootstrap por evento (um evento por fim de semana).

CRITERIO
--------
PASSA se `abs` E `excesso` tiverem IC95 inteiro acima de zero.

DESCRITIVOS
-----------
- Taxa de fechamento do gap (% que tocou F antes da saida por tempo).
- PLACEBO: o mesmo procedimento com um "gap" falso de meio de semana, de
  terca no horario de fechamento ate quinta no horario de reabertura (mesma
  distancia em horas). Se o placebo fecha na mesma proporcao, o "gap da CME"
  e so o preco voltando a um nivel recente, nada especial da CME.
- Limiar de 2%.

Uso (de dentro de monitor/):
    python replay_gap_cme.py
"""

import random
import sys
from datetime import datetime, timedelta, timezone

import replay_deslistagem as R
from replay_ema_ribbon import CUSTO_RT
from replay_pre_fomc import _domingo

H, DIA = R.H, R.DIA
N_RESAMPLES, SEED = 5000, 42
INICIO = datetime(2019, 9, 13, tzinfo=timezone.utc)   # 1a sexta com o perpetuo BTCUSDT
FIM = datetime(2026, 9, 25, tzinfo=timezone.utc)


def verao(d):
    return _domingo(d.year, 3, 2) <= d < _domingo(d.year, 11, 1)


def ms(d):
    return int(d.timestamp() * 1000)


def eventos(placebo=False):
    """[(t_ref, t_entrada, t_saida)] em ms. Real: sexta fechamento -> domingo
    reabertura -> sexta seguinte. Placebo: terca -> quinta -> terca seguinte."""
    out = []
    d = INICIO
    while d <= FIM:
        base = d - timedelta(days=3) if placebo else d          # terca ou sexta
        h_fecha = 21 if verao(base) else 22
        ref = base.replace(hour=h_fecha)
        ent = ref + timedelta(hours=49)                          # domingo 22/23 ou quinta
        sai = ref + timedelta(days=7)
        out.append((ms(ref), ms(ent), ms(sai)))
        d += timedelta(days=7)
    return out


def simular(s, evs, limiar, deriva):
    res = []
    for ref, ent, sai in evs:
        F, P0 = R.abertura(s, ref), R.abertura(s, ent)
        if not F or not P0:
            continue
        gap = P0 / F - 1
        if abs(gap) < limiar:
            continue
        d = -1 if gap > 0 else 1
        saida, fechou = None, False
        for t in range(ent, sai, H):
            k = s.get(t)
            if not k:
                continue
            if (d == -1 and k[2] <= F) or (d == 1 and k[1] >= F):
                saida, fechou = F, True
                t_fim = t + H
                break
        if saida is None:
            saida, t_fim = R.abertura(s, sai), sai
            if not saida:
                continue
        bruto = 100 * d * (saida / P0 - 1)
        f = 100 * R.funding("BTCUSDT", ent, t_fim)
        dur = t_fim - ent
        res.append({"ts": ent, "gap": 100 * gap, "fechou": fechou, "bruto": bruto,
                    "abs": bruto - 100 * CUSTO_RT - d * f,
                    "excesso": bruto - d * deriva(ent, dur)})
    return res


def boot(v):
    v = [x for x in v if x is not None]
    rng = random.Random(SEED)
    ms_ = sorted(sum(rng.choice(v) for _ in v) / len(v) for _ in range(N_RESAMPLES))
    return sum(v) / len(v), ms_[int(0.025 * N_RESAMPLES)], ms_[int(0.975 * N_RESAMPLES) - 1]


def bloco(rot, res):
    print(f"\n  [{rot}]  eventos {len(res)} | gap fechou em {sum(x['fechou'] for x in res)} "
          f"({100*sum(x['fechou'] for x in res)/max(len(res),1):.0f}%)")
    los = []
    for chave in ("bruto", "abs", "excesso"):
        if len(res) < 3:
            print("    insuficiente")
            return None
        m, lo, hi = boot([x[chave] for x in res])
        los.append(lo)
        print(f"    {chave:<8} media {m:+6.2f}% IC95 [{lo:+6.2f}, {hi:+6.2f}] | positivos "
              f"{sum(x[chave] > 0 for x in res)}")
    return los


def main(argv):
    s = R.klines("futures/um", "BTCUSDT", ms(INICIO) - 400 * DIA, ms(FIM) + 10 * DIA)
    abert = sorted(s)

    def deriva(t, dur):
        """Retorno % medio do BTC em janelas de `dur`, iniciando a cada 24h nos 365 dias antes de t."""
        v = []
        for k in range(1, 366):
            a = t - k * DIA - dur
            p0, p1 = R.abertura(s, a), R.abertura(s, a + dur)
            if p0 and p1:
                v.append(100 * (p1 / p0 - 1))
        return sum(v) / len(v) if len(v) > 100 else 0.0

    print(f"BTCUSDT 1h: {len(abert)} candles | fins de semana: {len(eventos())}")
    real = simular(s, eventos(), 0.01, deriva)
    los = bloco("CME, |gap| >= 1% (decide: abs e excesso)", real)
    bloco("CME, |gap| >= 2% (descritivo)", simular(s, eventos(), 0.02, deriva))
    bloco("PLACEBO terca -> quinta, |gap| >= 1%", simular(s, eventos(True), 0.01, deriva))
    ok = los is not None and los[1] > 0 and los[2] > 0
    print(f"\n  DECISAO: {'PASSA' if ok else 'NAO PASSA'}")


if __name__ == "__main__":
    main(sys.argv[1:])
