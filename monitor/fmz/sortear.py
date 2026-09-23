"""Sorteio PRE-REGISTRADO (23/09/2026) da amostra representativa do acervo.

Populacao: estrategias PineScript que declaram strategy(), sem request.security
(multi-tempo exige dados que D+E nao tem), com codigo <= 6000 caracteres, cuja
familia primaria (pelo nome) e uma das de indicador tecnico. Semente fixa.
Ordem do sorteio = ordem de traducao; estrategia intraduzivel para o diario
(ex.: depende de sessao de bolsa, de tick, de horario fixo) e pulada com o motivo
registrado, e entra a proxima da fila. Meta: 12 estrategias traduzidas.
"""
import json, os, random, re
AQUI = os.path.dirname(os.path.abspath(__file__))
reg = json.load(open(os.path.join(AQUI, "indice_rotulado.json"), encoding="utf-8"))
TA = {"tendencia_media", "reversao_oscilador", "rompimento_canal", "padrao_candle",
      "volume_vwap_fluxo", "smc_pivo_sr", "rompimento_volatilidade", "sem_rotulo"}
pop = [r for r in reg if r.get("lang") == "PineScript" and re.search(r"\bstrategy\s*\(", r.get("source", ""))
       and "request.security" not in r["source"] and "security(" not in r["source"]
       and len(r["source"]) <= 6000 and r["familias"][0] in TA]
pop.sort(key=lambda r: r["arquivo"])
fila = random.Random(20260923).sample(pop, 40)
json.dump([r["arquivo"] for r in fila], open(os.path.join(AQUI, "fila_sorteio.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
print("populacao elegivel:", len(pop), "de", len(reg))
for i, r in enumerate(fila):
    print(f"{i:>2} {r['familias'][0]:<22} {len(r['source']):>5} {r.get('Name','')[:90]}")
