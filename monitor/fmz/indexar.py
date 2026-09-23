"""Indexa o acervo strategies-for-test (biblioteca FMZ, 5.807 .md) em fmz/indice.json.

Cada arquivo tem secoes '> Name', '> Author', '> Strategy Description',
'> Strategy Arguments', '> Source (<lang>)', '> Detail', '> Last Modified'.
"""
import json, os, re, sys

RAIZ = sys.argv[1] if len(sys.argv) > 1 else r"D:\VSCode\strategies-for-test"
SEC = re.compile(r"^> (Name|Author|Strategy Description|Strategy Arguments|Source \((\w+)\)|Detail|Last Modified)\s*$", re.M)

def parse(txt):
    out, marcas = {}, list(SEC.finditer(txt))
    for i, m in enumerate(marcas):
        fim = marcas[i + 1].start() if i + 1 < len(marcas) else len(txt)
        corpo = txt[m.end():fim].strip()
        chave = m.group(1)
        if chave.startswith("Source"):
            out["lang"] = m.group(2)
            chave = "source"
        out[chave] = corpo
    return out

reg = []
for nome in sorted(os.listdir(RAIZ)):
    if not nome.endswith(".md"):
        continue
    with open(os.path.join(RAIZ, nome), encoding="utf-8", errors="replace") as f:
        d = parse(f.read())
    d["arquivo"] = nome
    reg.append(d)
json.dump(reg, open(os.path.join(os.path.dirname(__file__), "indice.json"), "w", encoding="utf-8"), ensure_ascii=False)
print(len(reg), "estrategias")
from collections import Counter
print(Counter(r.get("lang") for r in reg).most_common())
print(Counter(r.get("Author", "?")[:30] for r in reg).most_common(8))
print(Counter(r.get("Last Modified", "?")[:4] for r in reg).most_common())
