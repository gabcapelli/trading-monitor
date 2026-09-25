// Proxy somente-leitura para a API de futuros da Binance (fapi).
//
// Por que existe: o GitHub Actions roda em IPs dos EUA e a Binance responde 451
// para eles. Sem a fapi, unlock_paper/novos_paper so conseguem o preco de
// abertura do dia quando o Binance Vision publica o arquivo diario (~4-5h
// depois da meia-noite UTC), e o aviso das 21h BRT chegava de madrugada.
//
// Uso: UNLOCK_PAPER_FAPI = https://<worker>/<PROXY_TOKEN>/fapi/v1
// So repassa GET de dados publicos (klines, fundingRate, exchangeInfo); nada de conta/ordem.

const PERMITIDOS = new Set(["klines", "fundingRate", "exchangeInfo"]);

export default {
  async fetch(req, env) {
    if (req.method !== "GET") return new Response("metodo", { status: 405 });
    const url = new URL(req.url);
    const partes = url.pathname.split("/").filter(Boolean); // [token, "fapi", "v1", endpoint]
    if (!env.PROXY_TOKEN || partes[0] !== env.PROXY_TOKEN) return new Response("nao", { status: 404 });
    if (partes.length !== 4 || partes[1] !== "fapi" || partes[2] !== "v1" || !PERMITIDOS.has(partes[3]))
      return new Response("endpoint", { status: 400 });
    const alvo = `https://fapi.binance.com/fapi/v1/${partes[3]}${url.search}`;
    const r = await fetch(alvo, { headers: { "User-Agent": "trading-monitor-proxy" } });
    return new Response(r.body, {
      status: r.status,
      headers: { "Content-Type": r.headers.get("Content-Type") || "application/json" },
    });
  },
};
