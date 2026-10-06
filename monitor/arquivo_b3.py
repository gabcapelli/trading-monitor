"""
Arquiva os negocios da B3 de mini indice e mini dolar (e cheios) em candles de
1 minuto, daqui para frente. A B3 so guarda o tick a tick de ~4 semanas
(arquivos.b3.com.br/rapinegocios/tickercsv/AAAA-MM-DD), entao quem nao baixa
perde. Serve de amostra fora da amostra para estudos na B3 (estudo 47 e
seguintes): dado que ainda nao existia quando a regra foi escrita.

Saida: dados_b3/1min/AAAA-MM-DD.csv.gz com
  instrumento,sessao,minuto,abertura,maxima,minima,fechamento,contratos,negocios
(minuto = HH:MM do horario de Brasilia, como vem no arquivo). Negocios com
AcaoAtualizacao != 0 (correcao/cancelamento) ficam fora e sao contados em
dados_b3/resumo.json.

Idempotente: tenta os dias uteis dos ultimos 30 dias que ainda nao estao
arquivados, no maximo MAX_DIAS por execucao (cada arquivo tem ~200 MB).
Dia sem arquivo (feriado, ainda nao publicado) e tentado de novo depois.
Rode sem argumento (o workflow horario chama assim) ou com AAAA-MM-DD.
"""

import csv
import gzip
import io
import json
import os
import sys
import tempfile
import urllib.request
import zipfile
from datetime import date, timedelta

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(RAIZ, "dados_b3")
DIR_1MIN = os.path.join(DIR, "1min")
RESUMO = os.path.join(DIR, "resumo.json")
URL = "https://arquivos.b3.com.br/rapinegocios/tickercsv/{}"
PREFIXOS = ("WIN", "WDO", "IND", "DOL")
MAX_DIAS = 2
JANELA_DIAS = 30


def _baixar(dia, destino):
    req = urllib.request.Request(URL.format(dia), headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=300) as r, open(destino, "wb") as f:
        while bloco := r.read(1 << 20):
            f.write(bloco)
    return os.path.getsize(destino)


def _num(s):
    return float(s.replace(".", "").replace(",", "."))


def agregar(caminho_zip):
    barras, ignorados, lidos = {}, 0, 0
    with zipfile.ZipFile(caminho_zip) as z:
        with z.open(z.namelist()[0]) as bruto:
            leitor = csv.reader(io.TextIOWrapper(bruto, encoding="latin-1"), delimiter=";")
            cab = next(leitor)
            i_ins, i_acao = cab.index("CodigoInstrumento"), cab.index("AcaoAtualizacao")
            i_preco, i_qtd = cab.index("PrecoNegocio"), cab.index("QuantidadeNegociada")
            i_hora, i_sessao = cab.index("HoraFechamento"), cab.index("TipoSessaoPregao")
            for lin in leitor:
                ins = lin[i_ins]
                if len(ins) != 6 or not ins.startswith(PREFIXOS):
                    continue
                lidos += 1
                if lin[i_acao] != "0":
                    ignorados += 1
                    continue
                h = lin[i_hora].zfill(9)
                chave = (ins, lin[i_sessao], f"{h[:2]}:{h[2:4]}")
                p, q = _num(lin[i_preco]), int(lin[i_qtd])
                b = barras.get(chave)
                if b is None:
                    barras[chave] = [p, p, p, p, q, 1]
                else:
                    b[1] = max(b[1], p)
                    b[2] = min(b[2], p)
                    b[3] = p
                    b[4] += q
                    b[5] += 1
    return barras, lidos, ignorados


def arquivar(dia):
    destino = os.path.join(DIR_1MIN, f"{dia}.csv.gz")
    with tempfile.TemporaryDirectory() as tmp:
        zp = os.path.join(tmp, "t.zip")
        if _baixar(dia, zp) == 0:
            return None
        barras, lidos, ignorados = agregar(zp)
    os.makedirs(DIR_1MIN, exist_ok=True)
    with gzip.open(destino, "wt", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["instrumento", "sessao", "minuto", "abertura", "maxima", "minima",
                    "fechamento", "contratos", "negocios"])
        for chave in sorted(barras):
            w.writerow([*chave, *barras[chave]])
    return {"negocios_lidos": lidos, "ignorados_acao": ignorados, "barras": len(barras)}


def main():
    resumo = {}
    if os.path.exists(RESUMO):
        with open(RESUMO, encoding="utf-8") as f:
            resumo = json.load(f)
    if len(sys.argv) > 1:
        candidatos = [date.fromisoformat(sys.argv[1])]
    else:
        hoje = date.today()
        candidatos = [hoje - timedelta(days=k) for k in range(JANELA_DIAS, 0, -1)]
        candidatos = [d for d in candidatos if d.weekday() < 5 and str(d) not in resumo]
    feitos = 0
    for d in candidatos:
        if feitos >= MAX_DIAS:
            break
        try:
            info = arquivar(str(d))
        except Exception as e:  # rede/B3 fora: tenta na proxima execucao
            print(f"{d}: falhou ({e})")
            continue
        if info is None:
            print(f"{d}: sem arquivo")
            continue
        resumo[str(d)] = info
        feitos += 1
        print(f"{d}: {info}")
        with open(RESUMO, "w", encoding="utf-8") as f:
            json.dump(dict(sorted(resumo.items())), f, indent=1)


if __name__ == "__main__":
    main()
