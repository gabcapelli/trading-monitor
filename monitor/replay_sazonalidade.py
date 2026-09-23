"""
Teste PRE-REGISTRADO (22/09/2026) de SAZONALIDADE em perpetuos de cripto:
existe hora do dia ou dia da semana com retorno sistematicamente diferente?
Estudo avulso: NAO faz parte do checklist dos Setups A/B/C nem do monitor de
producao.

POR QUE ESTA
-------------
Cripto negocia 24/7, mas a atividade nao e uniforme: horario de Asia, Europa
e EUA tem participantes diferentes, e fim de semana tem menos liquidez e
menos fluxo institucional. Se existe um padrao, ele e o tipo de coisa que
roda 100% mecanicamente: e so um relogio. Nenhuma leitura de grafico.
E a ultima familia nao testada aqui (tendencia, premios transversais,
carrego, reversao e pairs ja foram).

REGRAS
------
Duas hipoteses, testadas separadamente:
- "hora": comprar numa hora fixa do dia (UTC) e sair na hora seguinte.
- "semana": comprar num dia fixo da semana (UTC) e sair no dia seguinte.
A carteira e equal-weight entre todos os pares do universo, sem alavancagem
(nocional = capital), e fica em caixa fora da janela escolhida.

SELECAO SEM GARIMPO (holdout, protocolo de estudos-avulsos.md)
---------------------------------------------------------------
1. DESENVOLVIMENTO (amostra A, 20 pares, primeira metade do historico):
   calcula-se o retorno medio de cada uma das 24 horas e de cada um dos 7
   dias; escolhe-se a MELHOR hora e o MELHOR dia (e tambem o pior, para a
   versao vendida, ficando com o maior |retorno|).
2. DECISAO (amostra E, 153 pares, historico inteiro -- pares que o passo 1
   nunca viu): so a hora e o dia escolhidos sao testados.
Custo: 0.06% do nocional por entrada+saida (uma ida e volta por janela).
Funding e pago/recebido no settlement que cair dentro da janela.

CRITERIO DE DECISAO (pre-registrado)
------------------------------------
Dois testes (hora e dia) -> IC de 97.5% (Bonferroni 0.05/2). Cada um PASSA
se, na amostra E: retorno liquido anual > 0 com IC97.5 inteiro acima de zero
E Sharpe > 0.5 com IC97.5 acima de zero.
"""

import random
import statistics
import sys
import time
from collections import defaultdict

import dados_binance as B
from replay_ema_ribbon import UNIVERSO
from replay_carver_carry import sharpe, MS_DIA
from replay_combo_premios import universo_e

CUSTO = 0.0006
MS_HORA = 3_600_000
N_RESAMPLES = 5000
SEED = 42
ALFA_FAMILIA = 0.05
N_TESTES = 2
MIN_HORAS = 24 * 300


def serie_horaria(inst):
    c = B.baixar(inst, "1H", 3000)
    if len(c) < MIN_HORAS:
        return None
    fund = {}
    for ts, taxa in B.baixar_funding(inst):
        fund[ts // MS_HORA * MS_HORA] = taxa
    return [(x[0], x[4], fund.get(x[0], 0.0)) for x in c]


def retornos_por_hora(series):
    """{hora_utc: [retornos]} e {dia_semana: [retornos]} da carteira equal-weight."""
    por_ts = defaultdict(list)
    for inst, s in series.items():
        for i in range(1, len(s)):
            ts, p, f = s[i]
            p_ant = s[i - 1][1]
            if p_ant > 0:
                por_ts[ts].append((p / p_ant - 1) - f)
    h, d = defaultdict(list), defaultdict(list)
    por_dia = defaultdict(list)
    for ts in sorted(por_ts):
        r = sum(por_ts[ts]) / len(por_ts[ts])
        t = time.gmtime(ts / 1000)
        h[t.tm_hour].append((ts, r))
        por_dia[ts // MS_DIA].append(r)
    for dia, v in por_dia.items():
        t = time.gmtime(dia * 86400)
        d[t.tm_wday].append((dia * MS_DIA, sum(v)))
    return h, d


def escolhe(buckets):
    """Melhor bucket por |retorno medio|; devolve (chave, lado)."""
    melhor, valor = None, 0.0
    for k, v in buckets.items():
        if len(v) < 50:
            continue
        m = sum(r for _, r in v) / len(v)
        if abs(m) > abs(valor):
            melhor, valor = k, m
    return melhor, (1 if valor > 0 else -1)


def serie_estrategia(buckets, chave, lado):
    return [(ts // MS_DIA, lado * r - CUSTO) for ts, r in buckets.get(chave, [])]


def bootstrap(rets, f):
    por_sem = defaultdict(list)
    for dia, r in rets:
        por_sem[dia // 7].append((dia, r))
    blocos = list(por_sem.values())
    rng = random.Random(SEED)
    vals = []
    for _ in range(N_RESAMPLES):
        amostra = []
        for _ in range(len(blocos)):
            amostra += blocos[rng.randrange(len(blocos))]
        vals.append(f(amostra))
    vals = [v for v in vals if v == v]
    vals.sort()
    a = ALFA_FAMILIA / N_TESTES / 2
    return vals[int(a * len(vals))], vals[int((1 - a) * len(vals)) - 1]


def ret_anual_periodico(rets, por_ano):
    """Retorno anual: media por evento x numero de eventos por ano."""
    return sum(r for _, r in rets) / len(rets) * por_ano


def relatorio(nome, rets, por_ano, decide):
    if len(rets) < 100:
        print(f"  {nome}: eventos insuficientes ({len(rets)})")
        return False
    ra = ret_anual_periodico(rets, por_ano)
    v = [r for _, r in rets]
    sr = (sum(v) / len(v)) / statistics.pstdev(v) * (por_ano ** 0.5) if statistics.pstdev(v) > 0 else 0
    rlo, rhi = bootstrap(rets, lambda a: ret_anual_periodico(a, por_ano))
    slo, shi = bootstrap(rets, lambda a: (sum(r for _, r in a) / len(a)) /
                         (statistics.pstdev([r for _, r in a]) or 1e-9) * (por_ano ** 0.5))
    print(f"  {nome}: eventos={len(rets)} | retorno {100*ra:+.1f}%/ano | IC97.5 [{100*rlo:+.1f}%, {100*rhi:+.1f}%]")
    print(f"    Sharpe {sr:+.2f} | IC97.5 [{slo:+.2f}, {shi:+.2f}]")
    return (rlo > 0 and slo > 0.5) if decide else None


def carrega(universo):
    s = {}
    for inst in universo:
        try:
            x = serie_horaria(inst)
        except Exception:
            continue
        if x:
            s[inst] = x
    return s


def main():
    import random as _r
    d_full = universo_e()
    _r.Random(42).shuffle(d_full)
    alvo_e = d_full[:12] if "--rapido" in sys.argv else d_full[:60]
    A = carrega([B.simbolo(x) for x in UNIVERSO])
    print(f"amostra A: {len(A)} pares com dados horarios")
    hA, dA = retornos_por_hora(A)
    # primeira metade do historico de A para escolher
    def metade(b):
        out = {}
        for k, v in b.items():
            v = sorted(v)
            out[k] = v[:len(v) // 2]
        return out
    hora, lado_h = escolhe(metade(hA))
    dia, lado_d = escolhe(metade(dA))
    nomes = ["segunda", "terca", "quarta", "quinta", "sexta", "sabado", "domingo"]
    print(f"\n  escolhidos na 1a metade da amostra A:")
    print(f"    hora {hora:02d}h UTC, lado {'comprado' if lado_h > 0 else 'vendido'}")
    print(f"    {nomes[dia]}, lado {'comprado' if lado_d > 0 else 'vendido'}")

    print(f"\n{'='*100}\nAMOSTRA A (desenvolvimento, historico inteiro)\n{'='*100}")
    relatorio(f"hora {hora:02d}h", serie_estrategia(hA, hora, lado_h), 365, decide=False)
    relatorio(f"{nomes[dia]}   ", serie_estrategia(dA, dia, lado_d), 52, decide=False)

    E = carrega(alvo_e)
    print(f"\namostra E: {len(E)} pares com dados horarios")
    hE, dE = retornos_por_hora(E)
    print(f"\n{'='*100}\nAMOSTRA E -- DECIDE (IC 97.5%, Bonferroni)\n{'='*100}")
    ok_h = relatorio(f"hora {hora:02d}h", serie_estrategia(hE, hora, lado_h), 365, decide=True)
    ok_d = relatorio(f"{nomes[dia]}   ", serie_estrategia(dE, dia, lado_d), 52, decide=True)
    print(f"\n==> DECISAO hora do dia: {'PASSA' if ok_h else 'NAO PASSA'}")
    print(f"==> DECISAO dia da semana: {'PASSA' if ok_d else 'NAO PASSA'}")


if __name__ == "__main__":
    main()
