"""
Candles da Binance (perpetuos USDT-M) para servir de AMOSTRA INDEPENDENTE nos
estudos avulsos. Criado em 22/09/2026, depois de as tres amostras da OKX
(20 pares, 80 pares, 83 pares novos) terem sido usadas.

Mesma interface de replay_stoch_vwap.baixar: devolve
[ts, open, high, low, close, volume_base], mais antigo -> mais recente, so
candles fechados. Aceita os instId da OKX (BTC-USDT-SWAP -> BTCUSDT).

Nao e a mesma serie da OKX: outra corretora, outro livro, outro horario de
listagem de cada par. Para o mesmo par e o mesmo periodo, os dois conjuntos
sao altamente correlacionados -- serve para testar robustez de execucao e
diferencas de venue, NAO como amostra estatisticamente independente no tempo.
"""

import json
import os
import time
import urllib.request

BASE = "https://fapi.binance.com"
CACHE_DIR = os.environ.get("BINANCE_CACHE", "cache_binance")
MS_DIA = 86_400_000
LIMITE = 1500


def simbolo(inst_id):
    """BTC-USDT-SWAP -> BTCUSDT"""
    return inst_id.replace("-SWAP", "").replace("-", "")


def _get(path, params):
    query = "&".join(f"{k}={v}" for k, v in params.items())
    req = urllib.request.Request(f"{BASE}{path}?{query}", headers={"User-Agent": "btc-monitor-script"})
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


def baixar(inst_id, bar="1Dutc", dias=3000):
    """Candles fechados [ts, o, h, l, c, vol_base]."""
    intervalo = {"1Dutc": "1d", "1W": "1w", "4H": "4h", "1H": "1h", "5m": "5m", "15m": "15m"}[bar]
    fpath = os.path.join(CACHE_DIR, f"{simbolo(inst_id)}_{intervalo}_{dias}.json")
    if os.path.exists(fpath):
        with open(fpath) as f:
            return json.load(f)
    agora = int(time.time() * 1000)
    inicio = agora - dias * MS_DIA
    todos, cursor = {}, inicio
    while cursor < agora:
        for tentativa in range(5):
            try:
                raw = _get("/fapi/v1/klines", {"symbol": simbolo(inst_id), "interval": intervalo,
                                               "startTime": cursor, "limit": LIMITE})
                break
            except Exception:
                if tentativa == 4:
                    raise
                time.sleep(2 + 2 * tentativa)
        time.sleep(0.15)
        if not raw:
            break
        for k in raw:
            if int(k[6]) < agora:  # so candles ja fechados (closeTime no passado)
                todos[int(k[0])] = [int(k[0]), float(k[1]), float(k[2]), float(k[3]), float(k[4]), float(k[5])]
        proximo = int(raw[-1][0]) + 1
        if proximo <= cursor:
            break
        cursor = proximo
        if len(raw) < LIMITE:
            break
    candles = [todos[k] for k in sorted(todos)]
    os.makedirs(CACHE_DIR, exist_ok=True)
    with open(fpath, "w") as f:
        json.dump(candles, f)
    return candles


if __name__ == "__main__":
    import sys
    from replay_ema_ribbon import UNIVERSO
    alvo = UNIVERSO if "--universo" in sys.argv else ["BTC-USDT-SWAP"]
    for inst in alvo:
        try:
            c = baixar(inst, "1Dutc", 3000)
            ini = time.strftime("%Y-%m-%d", time.gmtime(c[0][0] / 1000)) if c else "-"
            print(f"{inst:<18} {simbolo(inst):<12} candles={len(c):>5} desde {ini}", flush=True)
        except Exception as e:
            print(f"{inst:<18} {simbolo(inst):<12} FALHOU: {type(e).__name__} {str(e)[:80]}", flush=True)


def baixar_funding(inst_id, dias=3000):
    """Historico de funding [ts, taxa]. A Binance devolve desde a criacao do
    contrato (a OKX limita a ~96 dias, por isso a Binance aqui)."""
    fpath = os.path.join(CACHE_DIR, f"{simbolo(inst_id)}_funding.json")
    if os.path.exists(fpath):
        with open(fpath) as f:
            return json.load(f)
    agora = int(time.time() * 1000)
    cursor, out = agora - dias * MS_DIA, {}
    while cursor < agora:
        for tentativa in range(5):
            try:
                raw = _get("/fapi/v1/fundingRate", {"symbol": simbolo(inst_id),
                                                    "startTime": cursor, "limit": 1000})
                break
            except Exception:
                if tentativa == 4:
                    raise
                time.sleep(2 + 2 * tentativa)
        time.sleep(0.15)
        if not raw:
            break
        for r in raw:
            out[int(r["fundingTime"])] = float(r["fundingRate"])
        proximo = int(raw[-1]["fundingTime"]) + 1
        if proximo <= cursor:
            break
        cursor = proximo
        if len(raw) < 1000:
            break
    serie = [[k, out[k]] for k in sorted(out)]
    os.makedirs(CACHE_DIR, exist_ok=True)
    with open(fpath, "w") as f:
        json.dump(serie, f)
    return serie
