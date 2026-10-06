"""
Estudo 47 -- reversao do dolar depois da PTAX de fim de mes, PRE-REGISTRADO
em 06/10/2026, antes de baixar ou calcular qualquer retorno.

Primeiro estudo fora de cripto: dado novo (nunca usado no projeto), mercado
novo (B3), operavel numa corretora so (WDO, mini dolar).

HIPOTESE
--------
Desde 01/07/2011 a PTAX e a media de quatro consultas do Banco Central aos
dealers, nas janelas das 10h, 11h, 12h e 13h. A PTAX de venda do ultimo dia
util do mes liquida o contrato de dolar futuro (DOL/WDO) que vence no 1o dia
util do mes seguinte, alem de NDFs, contratos de exportacao/importacao e cotas
de fundos. Quem tem posicao grande atrelada a ela tem incentivo para empurrar
o dolar DURANTE as janelas ("briga pela PTAX"). Depois da ultima janela (13h)
a pressao acaba e o preco devolve parte do movimento.

Mecanismo de fluxo forcado com hora marcada, como o desbloqueio (estudo 25).
A direcao do empurrao nao e conhecida a priori, mas e OBSERVAVEL antes da
entrada: e o movimento entre a 1a e a 4a janela. A regra opera CONTRA ele.
Sem parametro a escolher: nao ha periodo de desenvolvimento, a amostra
inteira decide.

DADOS
-----
- Boletins da PTAX (dolar, cotacao de venda), API Olinda do Banco Central,
  CotacaoMoedaPeriodo, 01/07/2011 a 30/09/2026. Por dia: Abertura (~10h),
  Intermediario (~11h), Intermediario (~12h), Intermediario (~13h). O boletim
  de Fechamento e a media dos quatro, nao um preco: fica fora.
- J10(D) = boletim de Abertura do dia D; J13(D) = ultimo Intermediario do dia
  D (o que sai depois das 12h30). Dia sem J10 ou sem J13: fora (contado no
  log).
- CDI diario: SGS 12 do Banco Central. Juro do dolar: Fed Funds efetivo
  (FRED, serie DFF). So para o ajuste de carrego (abaixo).

EVENTOS
-------
- D = ultimo dia util do mes com boletins (o ultimo dia do mes que tem J10 e
  J13 na API). D+1 = proximo dia com boletins.
- ~183 eventos (jul/2011 a set/2026).

REGRA
-----
- Sinal: m = J13(D) / J10(D) - 1 (movimento durante as janelas).
- m > 0: VENDIDO em dolar. m < 0: COMPRADO. m = 0: sem trade.
- Entrada: J13(D) (executavel no WDO por volta das 13h05-13h15).
- Duas saidas: (a) J10(D+1), na manha seguinte; (b) J13(D+1), um dia inteiro
  depois.
- Sem stop, sem alvo, sem filtro de tamanho de m.

MEDIDAS (% do nocional, positivo = a regra ganhou)
--------------------------------------------------
- `bruto` = lado x (saida / entrada - 1), lado = -1 vendido, +1 comprado.
- Ajuste de carrego: o boletim e dolar a vista; o WDO carrega a diferenca de
  juro. Comprado no futuro perde, por dia util, ~ (CDI - Fed Funds) / 252 em
  relacao ao a vista; vendido ganha o mesmo. `carrego` = -lado x (CDI_dia -
  FF_dia/252) x dias uteis entre entrada e saida (0 ou 1 no caso (a), 1 no
  (b); conta pelo calendario de dias com boletim). Aproximacao: ignora a base
  do cupom cambial sobre o Fed Funds.
- `liq` (decide) = bruto + carrego - 0.04% de custo ida e volta (~4 ticks de
  0.5 pt no WDO a ~R$5,20: spread, emolumentos e deslize). Descritivo com
  0.08%.
- `excesso` (decide) = liq - media de `liq` da MESMA regra (sinal J10->J13,
  entrada J13, mesma saida) em todos os OUTROS dias uteis do mesmo mes
  (placebo). Isola o efeito do fim de mes de uma eventual reversao do dolar
  depois das 13h que exista em qualquer dia.
- IR (20% day trade / 15% swing) fica fora: nao muda o sinal do resultado.
  Entra so na conta final de rentabilidade, se passar.

ESTATISTICA
-----------
- Bootstrap por evento (um evento por mes, sem sobreposicao), 5000
  reamostragens, semente 42.
- Validacao do simulador: a mesma regra em 20 sementes de passeio aleatorio
  sem drift (mesmos dias, retornos sorteados com a volatilidade realizada de
  cada trecho), com o bruto esperado em zero.

CRITERIO
--------
PASSA se, em alguma das duas saidas, `liq` E `excesso` tiverem IC 97.5%
(Bonferroni para 2 saidas) inteiro acima de zero.
Com menos de 120 eventos validos: SEM AMOSTRA PARA DECIDIR.

Descritivo, sem poder de decisao: metades (2011-18 x 2019-26), taxa de
acerto, resultado por tamanho de |m| (tercis) e o mesmo teste com custo de
0.08%.

Poder: com desvio de ~0.8% por evento e n ~183, o erro padrao da media fica
em ~0.06%. Um efeito de ~0.15% liquido sai do zero; um NAO PASSA quer dizer
"nao ha efeito desse tamanho", nao "nao ha efeito".

SE PASSAR
---------
Nao vai direto ao papel. Antes: (1) confirmar com o tick a tick do WDO da B3
(arquivado daqui para frente, ja que a B3 so guarda ~4 semanas) que o preco
negociavel do futuro reproduz o movimento dos boletins; (2) papel com a regra
congelada.

NAO FAZER DEPOIS DE VER O RESULTADO
-----------------------------------
- Trocar a janela do sinal (ex.: 11h->13h), o horario de saida, ou filtrar
  por tamanho de m.
- Restringir a meses "especiais" (fim de trimestre, fim de ano).
- Inverter o lado (continuacao em vez de reversao).
Cada uma dessas seria uma hipotese nova, que pede amostra nova (o papel).
"""

import json
import math
import os
import random
import urllib.request
from collections import defaultdict
from datetime import date, datetime

AQUI = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(AQUI, "cache_ptax")
INICIO, FIM = date(2011, 7, 1), date(2026, 9, 30)
CUSTO, CUSTO_ALT = 0.04, 0.08          # % ida e volta
N_RESAMPLES, SEED = 5000, 42
ALFA = 0.025                           # IC 97.5% (Bonferroni, 2 saidas)
N_MIN = 120
SAIDAS = ("a_J10", "b_J13")


def _get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read().decode("utf-8")


def _cache(nome, baixar):
    os.makedirs(CACHE, exist_ok=True)
    caminho = os.path.join(CACHE, nome)
    if not os.path.exists(caminho):
        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(baixar(), f)
    with open(caminho, encoding="utf-8") as f:
        return json.load(f)


def baixar_boletins():
    url = ("https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/"
           "CotacaoMoedaPeriodo(moeda=@moeda,dataInicial=@dataInicial,"
           "dataFinalCotacao=@dataFinalCotacao)?@moeda='USD'"
           f"&@dataInicial='{INICIO:%m-%d-%Y}'&@dataFinalCotacao='{FIM:%m-%d-%Y}'"
           "&$format=json&$top=100000")
    return json.loads(_get(url))["value"]


def baixar_cdi():
    out = []
    for a0 in range(INICIO.year, FIM.year + 1, 5):
        a1 = min(a0 + 4, FIM.year)
        url = ("https://api.bcb.gov.br/dados/serie/bcdata.sgs.12/dados?formato=json"
               f"&dataInicial=01/01/{a0}&dataFinal=31/12/{a1}")
        out += json.loads(_get(url))
    return out


def baixar_ff():
    txt = _get("https://fred.stlouisfed.org/graph/fredgraph.csv?id=DFF"
               f"&cosd={INICIO}&coed={FIM}")
    out = {}
    for linha_csv in txt.strip().splitlines()[1:]:
        d, v = linha_csv.split(",")
        if v not in (".", ""):
            out[d] = float(v)
    return out


def montar_dias(boletins):
    """{date: (J10, J13)} so com dias que tem os dois."""
    por_dia = defaultdict(list)
    for b in boletins:
        dt = datetime.strptime(b["dataHoraCotacao"][:19], "%Y-%m-%d %H:%M:%S")
        por_dia[dt.date()].append((dt, b["tipoBoletim"], float(b["cotacaoVenda"])))
    dias, faltas = {}, 0
    for d, bs in por_dia.items():
        j10 = [v for dt, t, v in bs if t == "Abertura"]
        j13 = sorted((dt, v) for dt, t, v in bs
                     if t.startswith("Intermedi") and (dt.hour, dt.minute) >= (12, 30))
        if j10 and j13:
            dias[d] = (j10[0], j13[-1][1])
        else:
            faltas += 1
    return dias, faltas, len(por_dia)


def trade(dias, seq, i, cdi, ff):
    """Regra no dia seq[i] com saida em seq[i+1]. None se m == 0."""
    d, d1 = seq[i], seq[i + 1]
    j10, j13 = dias[d]
    m = j13 / j10 - 1
    if m == 0:
        return None
    lado = -1 if m > 0 else 1
    c, f = cdi.get(d), ff.get(str(d))
    carrego = -lado * (c - f / 252) if c is not None and f is not None else 0.0
    t = {"d": d, "m": m, "lado": lado, "carrego": carrego}
    for nome, saida in zip(SAIDAS, dias[d1]):
        bruto = lado * (saida / j13 - 1) * 100
        t[nome + "_bruto"] = bruto
        t[nome] = bruto + carrego - CUSTO
        t[nome + "_alt"] = bruto + carrego - CUSTO_ALT
    return t


def ic(valores, alfa=ALFA, semente=SEED):
    rng = random.Random(semente)
    n = len(valores)
    medias = sorted(sum(valores[rng.randrange(n)] for _ in range(n)) / n
                    for _ in range(N_RESAMPLES))
    return medias[int(alfa / 2 * N_RESAMPLES)], medias[int((1 - alfa / 2) * N_RESAMPLES) - 1]


def linha(rotulo, v, alfa=ALFA):
    media = sum(v) / len(v)
    lo, hi = ic(v, alfa)
    acerto = 100 * sum(x > 0 for x in v) / len(v)
    return (f"  {rotulo:<32} n={len(v):>4} | media {media:+.3f}% | "
            f"IC{100 * (1 - alfa):.1f} [{lo:+.3f}, {hi:+.3f}] | acerto {acerto:.0f}%"), lo > 0


def passeio(dias, seq, eventos_idx, semente):
    """Mesmos dias; retornos log-normais sorteados com a vol realizada de cada trecho."""
    intra = [math.log(dias[d][1] / dias[d][0]) for d in seq]
    noite = [math.log(dias[seq[i + 1]][0] / dias[seq[i]][1]) for i in range(len(seq) - 1)]
    sd_i = (sum(x * x for x in intra) / len(intra)) ** 0.5
    sd_n = (sum(x * x for x in noite) / len(noite)) ** 0.5
    rng = random.Random(semente)
    fake, p = {}, 1.0
    for d in seq:
        j13 = p * math.exp(rng.gauss(0, sd_i))
        fake[d] = (p, j13)
        p = j13 * math.exp(rng.gauss(0, sd_n))
    res = {s: [] for s in SAIDAS}
    for i in eventos_idx:
        t = trade(fake, seq, i, {}, {})
        if t:
            for s in SAIDAS:
                res[s].append(t[s + "_bruto"])
    return res


def main():
    boletins = _cache("boletins.json", baixar_boletins)
    cdi = {datetime.strptime(r["data"], "%d/%m/%Y").date(): float(r["valor"])
           for r in _cache("cdi.json", baixar_cdi)}
    ff = _cache("ff.json", baixar_ff)
    dias, faltas, total = montar_dias(boletins)
    seq = sorted(dias)
    pos = {d: i for i, d in enumerate(seq)}

    por_mes = defaultdict(list)
    for d in seq:
        por_mes[(d.year, d.month)].append(d)
    eventos, placebo = [], defaultdict(list)
    for mes, ds in sorted(por_mes.items()):
        D = ds[-1]
        if pos[D] + 1 >= len(seq):
            continue  # mes sem dia seguinte na amostra
        t = trade(dias, seq, pos[D], cdi, ff)
        if t:
            eventos.append(t)
        for d in ds[:-1]:
            tp = trade(dias, seq, pos[d], cdi, ff)
            if tp:
                placebo[mes].append(tp)

    print("Estudo 47 -- reversao do dolar depois da PTAX de fim de mes")
    print(f"Dias com boletim: {total} | sem J10 ou J13 (fora): {faltas} | validos: {len(seq)}")
    print(f"Eventos (ultimo dia util do mes): {len(eventos)} "
          f"({eventos[0]['d']} a {eventos[-1]['d']})")
    print(f"Carrego medio por trade: {sum(t['carrego'] for t in eventos) / len(eventos):+.4f}%")
    if len(eventos) < N_MIN:
        print("SEM AMOSTRA PARA DECIDIR")
        return

    passa_algum = False
    for s in SAIDAS:
        for t in eventos:
            pl = placebo[(t["d"].year, t["d"].month)]
            t[s + "_exc"] = t[s] - sum(p[s] for p in pl) / len(pl)
        print(f"\nSaida {s} (decide)")
        l1, ok1 = linha("liq (custo 0.04%)", [t[s] for t in eventos])
        l2, ok2 = linha("excesso sobre placebo", [t[s + "_exc"] for t in eventos])
        print(l1)
        print(l2)
        print(f"  -> {'PASSA' if ok1 and ok2 else 'nao passa'} nesta saida")
        passa_algum |= ok1 and ok2

        print("  Descritivo (IC95):")
        print(linha("bruto", [t[s + "_bruto"] for t in eventos], 0.05)[0])
        print(linha("liq com custo 0.08%", [t[s + "_alt"] for t in eventos], 0.05)[0])
        todos_pl = [p[s] for pl in placebo.values() for p in pl]
        print(linha("placebo (outros dias, liq)", todos_pl, 0.05)[0])
        for a, b in ((2011, 2018), (2019, 2026)):
            v = [t[s] for t in eventos if a <= t["d"].year <= b]
            print(linha(f"liq {a}-{b}", v, 0.05)[0])
        ordem = sorted(eventos, key=lambda t: abs(t["m"]))
        k = len(ordem) // 3
        for nome, fatia in (("liq |m| tercil baixo", ordem[:k]),
                            ("liq |m| tercil medio", ordem[k:2 * k]),
                            ("liq |m| tercil alto", ordem[2 * k:])):
            print(linha(nome, [t[s] for t in fatia], 0.05)[0])

    print(f"\nVEREDITO: {'PASSA' if passa_algum else 'NAO PASSA'}")

    print("\nValidacao: passeio aleatorio, 20 sementes (bruto, IC97.5)")
    idx = [pos[t["d"]] for t in eventos]
    falsos = {s: 0 for s in SAIDAS}
    medias = {s: [] for s in SAIDAS}
    for sem in range(20):
        r = passeio(dias, seq, idx, sem)
        for s in SAIDAS:
            medias[s].append(sum(r[s]) / len(r[s]))
            falsos[s] += ic(r[s], ALFA, sem)[0] > 0
    for s in SAIDAS:
        print(f"  {s}: media das medias {sum(medias[s]) / 20:+.4f}% | "
              f"IC inteiro > 0 em {falsos[s]} de 20")


if __name__ == "__main__":
    main()
