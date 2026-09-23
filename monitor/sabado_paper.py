"""
Registro em PAPEL do efeito de sabado (estudo 21 de claude/estudos-avulsos.md).
NAO envia ordem. Apenas calcula o que a regra mandaria fazer e registra o
resultado em claude/sabado-paper.md.

Rode sem argumento para registrar o ultimo sabado ja fechado. So biblioteca
padrao do Python (mesma restricao do fetch_and_check.py).

REGRA PRE-REGISTRADA (congelada em 22/09/2026, nao alterar durante o teste)
---------------------------------------------------------------------------
- Cesta PRINCIPAL: os 20 perpetuos USDT do UNIVERSO (replay_ema_ribbon.py),
  peso igual, comprado. Foi a cesta com melhor medida no estudo 21
  (t=+2.93, 64.6% de sabados positivos).
- Cesta SECUNDARIA (registrada em paralelo, custo zero por ser papel): os 5
  maiores (BTC, ETH, SOL, XRP, DOGE) -- versao operacionalmente mais simples
  (5 ordens em vez de 20), que no estudo capturou quase todo o efeito
  (t=+2.77).
- Janela: compra no fechamento de SEXTA 00:00 UTC do dia seguinte (isto e,
  no fechamento do candle diario de sexta) e vende no fechamento de SABADO.
  Uma operacao por semana.
- Custo: 0.06% do nocional (ida e volta, ordens limite em pares liquidos).
- Funding: os settlements de sabado sao pagos pela posicao comprada e
  entram no resultado.
- Sem stop, sem alvo, sem discricao.

O QUE ESTE TESTE PRECISA PARA VALER
------------------------------------
O estudo 21 achou +19.8%/ano (20 majors) e +16.0%/ano (60 alts), mas com
IC95 cruzando zero: ~350 sabados nao bastam. Este registro acumula sabados
NOVOS, que nenhum backtest viu. Com ~52 por ano, sao necessarios varios anos
para concluir -- a promessa aqui e honestidade, nao rapidez.
Criterio de leitura (fixado agora): so faz sentido reavaliar quando houver
>= 104 sabados novos (2 anos). Antes disso, qualquer leitura e ruido.
"""

import json
import os
import sys
import time
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import dados_binance as B

PRINCIPAL = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "XRPUSDT", "DOGEUSDT", "ARBUSDT", "WLDUSDT",
             "SUIUSDT", "UNIUSDT", "LINKUSDT", "BNBUSDT", "TRXUSDT", "ZECUSDT", "HYPEUSDT",
             "ADAUSDT", "XLMUSDT", "NEARUSDT", "AVAXUSDT", "LTCUSDT", "BCHUSDT"]
SECUNDARIA = ["BTCUSDT", "ETHUSDT", "SOLUSDT", "XRPUSDT", "DOGEUSDT"]
CUSTO = 0.0006
MS_DIA = 86_400_000
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = os.path.join(RAIZ, "claude", "sabado-paper.md")
ESTADO = os.path.join(RAIZ, "monitor", "sabado_paper_state.json")


def ultimo_sabado_fechado(agora=None):
    """Dia (epoch/MS_DIA) do ultimo sabado UTC ja encerrado."""
    agora = agora or datetime.now(timezone.utc)
    dia = int(agora.timestamp()) // 86400
    # tm_wday: 5 = sabado. Recua ate achar um sabado anterior ao dia de hoje.
    d = dia - 1
    while time.gmtime(d * 86400).tm_wday != 5:
        d -= 1
    return d


def retorno_cesta(pares, dia_sabado):
    """Retorno liquido da cesta comprada no sabado (sexta->sabado), e detalhe."""
    linhas, rets = [], []
    for sym in pares:
        try:
            c = B.baixar(sym, "1Dutc", 3000)
        except Exception:
            continue
        por_dia = {x[0] // MS_DIA: x for x in c}
        sab, sex = por_dia.get(dia_sabado), por_dia.get(dia_sabado - 1)
        if not sab or not sex or sex[4] <= 0:
            continue
        r = sab[4] / sex[4] - 1
        try:
            fund = sum(t for ts, t in B.baixar_funding(sym) if ts // MS_DIA == dia_sabado)
        except Exception:
            fund = 0.0
        rets.append(r - fund)
        linhas.append((sym.replace("USDT", ""), sex[4], sab[4], 100 * r, 100 * fund))
    if not rets:
        return None, []
    return sum(rets) / len(rets) - CUSTO, linhas


def carrega_estado():
    if os.path.exists(ESTADO):
        with open(ESTADO) as f:
            return json.load(f)
    return {"inicio": None, "sabados": []}


def salva_estado(e):
    with open(ESTADO, "w") as f:
        json.dump(e, f, indent=1)


def escreve_ledger(estado):
    linhas = ["# Registro em papel — efeito de sábado",
              "",
              "> Gerado por `monitor/sabado_paper.py`. **Nenhuma ordem é enviada.**",
              "> Regra congelada em 22/09/2026 (estudo 21 de `estudos-avulsos.md`):",
              "> comprar a cesta de peso igual no fechamento de sexta (UTC) e vender no",
              "> fechamento de sábado. Custo de 0.06% e funding já descontados.",
              "> **Só reavaliar com 104 sábados novos (~2 anos).** Antes disso é ruído.",
              ""]
    sab = estado["sabados"]
    if sab:
        acum_p = acum_s = 0.0
        pos_p = 0
        for s in sab:
            acum_p += s["principal"]
            acum_s += s["secundaria"]
            pos_p += 1 if s["principal"] > 0 else 0
        linhas += [f"**Sábados registrados:** {len(sab)} de 104 necessários "
                   f"({100*len(sab)/104:.0f}%)", "",
                   f"**Acumulado (20 majors):** {100*acum_p:+.2f}% | "
                   f"positivos: {pos_p}/{len(sab)} ({100*pos_p/len(sab):.0f}%)", "",
                   f"**Acumulado (5 maiores):** {100*acum_s:+.2f}%", "",
                   "| Sábado | 20 majors | 5 maiores | acum. 20 majors |",
                   "|---|---|---|---|"]
        acum = 0.0
        for s in sab:
            acum += s["principal"]
            linhas.append(f"| {s['data']} | {100*s['principal']:+.2f}% | "
                          f"{100*s['secundaria']:+.2f}% | {100*acum:+.2f}% |")
    else:
        linhas.append("_Nenhum sábado registrado ainda._")
    linhas.append("")
    with open(LEDGER, "w", encoding="utf-8") as f:
        f.write("\n".join(linhas))


def main():
    estado = carrega_estado()
    hoje = int(time.time()) // 86400
    if estado["inicio"] is None:
        estado["inicio"] = hoje
        print(f"iniciando registro em {time.strftime('%d/%m/%Y', time.gmtime(hoje*86400))}")
    alvo = ultimo_sabado_fechado()
    if alvo < estado["inicio"]:
        print("ainda nao houve sabado desde o inicio do registro")
        salva_estado(estado)
        escreve_ledger(estado)
        return
    if any(s["dia"] == alvo for s in estado["sabados"]):
        print(f"sabado {time.strftime('%d/%m/%Y', time.gmtime(alvo*86400))} ja registrado")
        escreve_ledger(estado)
        return
    rp, detalhe = retorno_cesta(PRINCIPAL, alvo)
    rs, _ = retorno_cesta(SECUNDARIA, alvo)
    if rp is None:
        print("sem dados para o sabado alvo")
        return
    estado["sabados"].append({"dia": alvo,
                              "data": time.strftime("%d/%m/%Y", time.gmtime(alvo * 86400)),
                              "principal": rp, "secundaria": rs})
    estado["sabados"].sort(key=lambda s: s["dia"])
    salva_estado(estado)
    escreve_ledger(estado)
    print(f"sabado {time.strftime('%d/%m/%Y', time.gmtime(alvo*86400))}: "
          f"20 majors {100*rp:+.2f}% | 5 maiores {100*rs:+.2f}%")
    for sym, p_sex, p_sab, r, f in sorted(detalhe, key=lambda x: -x[3])[:5]:
        print(f"    {sym:<6} {p_sex:>12.4f} -> {p_sab:>12.4f}  {r:+.2f}% (funding {f:+.3f}%)")


if __name__ == "__main__":
    main()
