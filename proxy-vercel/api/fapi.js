// Proxy somente-leitura para a API de futuros da Binance (fapi), na Vercel.
//
// Por que existe: o GitHub Actions roda em IPs dos EUA e a Binance responde 451
// para eles. O proxy da Cloudflare (proxy/worker.js) nao serve: a Binance
// responde 403 a qualquer requisicao que saia de um Worker (30/09/2026). Aqui a
// funcao roda em Toquio (vercel.json: hnd1) e sai por IP da AWS.
//
// Uso: UNLOCK_PAPER_FAPI = https://<projeto>.vercel.app/<PROXY_TOKEN>/fapi/v1
// So repassa GET de dados publicos (klines, fundingRate, exchangeInfo); nada de conta/ordem.
// Desde 05/10/2026 tambem a lista publica de anuncios da Binance (monitoring_paper.py):
//   https://<projeto>.vercel.app/<PROXY_TOKEN>/cms?catalogId=49&pageNo=1&pageSize=20

const PERMITIDOS = new Set(["klines", "fundingRate", "exchangeInfo"]);

export default async function handler(req, res) {
  if (req.method !== "GET") return res.status(405).send("metodo");
  const url = new URL(req.url, "http://x");
  const partes = (url.searchParams.get("p") || "").split("/").filter(Boolean); // [token, "fapi", "v1", endpoint]
  const token = process.env.PROXY_TOKEN;
  if (!token || partes[0] !== token) return res.status(404).send("nao");
  url.searchParams.delete("p");
  if (partes.length === 2 && partes[1] === "cms") {
    const q = new URLSearchParams({ type: "1" });
    for (const k of ["catalogId", "pageNo", "pageSize"]) {
      const v = url.searchParams.get(k);
      if (!v || !/^\d{1,4}$/.test(v)) return res.status(400).send("parametro");
      q.set(k, v);
    }
    const r = await fetch(`https://www.binance.com/bapi/composite/v1/public/cms/article/list/query?${q}`, {
      headers: { "User-Agent": "Mozilla/5.0 trading-monitor-proxy" },
    });
    res.status(r.status);
    res.setHeader("Content-Type", r.headers.get("Content-Type") || "application/json");
    return res.send(Buffer.from(await r.arrayBuffer()));
  }
  // ticker/24hr (volume de 24h de todos os perpetuos numa chamada; continuacao_paper.py, desde 05/10/2026)
  const ticker24 = partes.length === 5 && partes[3] === "ticker" && partes[4] === "24hr";
  if (!ticker24 && (partes.length !== 4 || !PERMITIDOS.has(partes[3])))
    return res.status(400).send("endpoint");
  if (partes[1] !== "fapi" || partes[2] !== "v1") return res.status(400).send("endpoint");
  const qs = url.searchParams.toString();
  const ep = ticker24 ? "ticker/24hr" : partes[3];
  const r = await fetch(`https://fapi.binance.com/fapi/v1/${ep}${qs ? "?" + qs : ""}`, {
    headers: { "User-Agent": "trading-monitor-proxy" },
  });
  res.status(r.status);
  res.setHeader("Content-Type", r.headers.get("Content-Type") || "application/json");
  res.send(Buffer.from(await r.arrayBuffer()));
}
