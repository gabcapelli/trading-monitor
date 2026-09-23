"""Classifica o indice do acervo FMZ por familia de mecanismo (multi-rotulo) e
marca cada familia contra o que ja foi testado em claude/estudos-avulsos.md."""
import json, os, re
from collections import Counter

AQUI = os.path.dirname(os.path.abspath(__file__))
reg = json.load(open(os.path.join(AQUI, "indice.json"), encoding="utf-8"))

# (familia, regex sobre nome+descricao, regex sobre codigo) -- ordem = prioridade do rotulo primario
FAM = [
 ("ferramenta_nao_estrategia", r"template|模板|类库|library|工具|tool|monitor|监控|推送|报警|alert bot|webhook|plot only|仪表|display|行情收集|数据|回测系统|框架", None),
 ("arbitragem_hedge",   r"arbitrag|套利|对冲|hedg|spread|价差|basis|基差|期现|跨期|跨市场|三角|triangular|cash.and.carry|funding|资金费", r"funding|getFundingRate|exchanges\[1\]"),
 ("market_making_hft",  r"market.?mak|做市|高频|hft|order.?book|盘口|depth|挂单|scalping bot|冰山|iceberg", r"GetDepth"),
 ("grid_martingale_dca",r"grid|网格|martingal|马丁|dca|dollar.cost|定投|加仓|pyramid|金字塔|averag(e|ing) down|平均成本", None),
 ("ml_ia",              r"machine learning|机器学习|neural|神经网络|\bknn\b|lorentzian|\bsvm\b|lstm|random forest|gpt|人工智能|深度学习", None),
 ("pares_cointegracao", r"pair.?trad|配对|cointegr|协整|统计套利|stat.?arb", None),
 ("sazonal_calendario", r"seasonal|季节|weekday|day of week|星期|周末|weekend|monthly|month.end|月初|time.of.day|session|时段|夜盘|开盘", None),
 ("rompimento_volatilidade", r"dual.?thrust|r.?breaker|opening range|开盘区间|volatility breakout|波动率突破|larry williams.*break|orb\b|区间突破", None),
 ("rompimento_canal",   r"breakout|突破|donchian|唐奇安|turtle|海龟|channel|通道|keltner|肯特纳|atr band|high.low|新高|new high", r"ta\.highest|ta\.lowest|highest\(|lowest\("),
 ("smc_pivo_sr",        r"order block|订单块|fvg|fair value gap|smart money|smc|liquidity|流动性|pivot|枢轴|support|resistance|支撑|阻力|fibonacci|斐波那契|elliott|波浪|zigzag|zone|供需", r"pivothigh|pivotlow"),
 ("padrao_candle",      r"engulf|吞没|hammer|锤|doji|十字星|pin.?bar|harami|孕线|inside bar|内包|outside bar|morning star|晨星|123|1-2-3|candlestick|蜡烛|k线形态|heikin|平均k|renko|砖", None),
 ("volume_vwap_fluxo",  r"volume|成交量|vwap|obv|能量潮|money flow|资金流|mfi|accumulation|cvd|delta|量价", r"ta\.vwap|ta\.obv|ta\.mfi"),
 ("reversao_oscilador", r"rsi|相对强弱|stoch|随机|bollinger|布林|\bcci\b|williams|威廉|oversold|超卖|overbought|超买|mean.?revers|均值回归|反转|reversal|z.?score|divergen|背离", r"ta\.rsi|ta\.stoch|ta\.bb|ta\.cci|ta\.wpr"),
 ("tendencia_media",    r"moving average|均线|\bema\b|\bsma\b|\bma\b|macd|supertrend|超级趋势|adx|\bdmi\b|parabolic|sar|抛物线|ichimoku|一目|hull|趋势|trend|momentum|动量|crossover|交叉|alligator|鳄鱼|t3|kama|tema|dema|aroon|trix", r"ta\.ema|ta\.sma|ta\.macd|ta\.supertrend|ta\.crossover"),
]

def rotulos(r):
    txt = (r.get("Name", "") + " " + r["arquivo"]).lower()  # so o nome: as descricoes sao texto gerado em serie
    src = r.get("source", "")
    out = []
    nome = (r.get("Name", "") + " " + r["arquivo"]).lower()
    for fam, rx_txt, rx_src in FAM:
        if fam == "ferramenta_nao_estrategia":
            # so pelo nome, e Pine que declara strategy() nunca e ferramenta
            if re.search(rx_txt, nome) and not re.search(r"strategy\s*\(", src):
                out.append(fam)
            continue
        if re.search(rx_txt, txt) or (rx_src and re.search(rx_src, src)):
            out.append(fam)
    return out or ["sem_rotulo"]

prim, todos = Counter(), Counter()
for r in reg:
    rs = rotulos(r)
    r["familias"] = rs
    prim[rs[0]] += 1
    todos.update(rs)
    # quantos indicadores distintos o codigo usa (proxy de "sopa de indicadores")
    r["n_ind"] = len(set(re.findall(r"ta\.(\w+)\(", r.get("source", ""))))
    # stop/alvo explicitos no codigo?
    r["tem_stop"] = bool(re.search(r"stop\s*=|loss\s*=|strategy\.exit", r.get("source", "")))

json.dump(reg, open(os.path.join(AQUI, "indice_rotulado.json"), "w", encoding="utf-8"), ensure_ascii=False)
print(f"{'familia':<26}{'primaria':>9}{'qualquer':>10}")
for fam, _, _ in FAM + [("sem_rotulo", 0, 0)]:
    print(f"{fam:<26}{prim[fam]:>9}{todos[fam]:>10}")
pine = [r for r in reg if r.get("lang") == "PineScript"]
print("\nPine: mediana de indicadores ta.* distintos por script:", sorted(r["n_ind"] for r in pine)[len(pine)//2],
      "| com >=5:", sum(r["n_ind"] >= 5 for r in pine), "| com strategy.exit/stop:", sum(r["tem_stop"] for r in pine))
