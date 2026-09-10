#!/usr/bin/env python3
"""
Testes de regressao das correcoes da v5 (auditoria de 10/09/2026).

Complementa monitor/test_zone_logic.py, que cobre so os dois bugs de
indice/lista da v1. A v4 (cooldown, revalidacao de tendencia, acompanhamento
automatico de desfecho) foi entregue com ZERO cobertura -- e foi justamente
onde a auditoria achou os buracos maiores.

Rodar: python monitor/test_v5_fixes.py
"""

import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import fetch_and_check as m  # noqa: E402

# process_single_pair (via registrar_sinal_mecanico/insert_candidate_trade)
# escreve no banco apontado por m.TRADE_DB_PATH. Sem isolar isso, os testes
# que confirmam zona (item 1, por ex.) gravavam linhas de verdade em
# claude/trade_journal.db com par='TEST-USDT-SWAP' -- poluindo o diario real.
# Redireciona para um arquivo temporario pela duracao do modulo inteiro.
_TMP_DB = tempfile.NamedTemporaryFile(suffix=".db", delete=False)
_TMP_DB.close()
m.TRADE_DB_PATH = _TMP_DB.name

H = 3_600_000  # 1h em ms
T0 = 1_000_000_000_000


def make_candle(ts, o, h, l, c, confirm="1"):
    return {"ts": ts, "open": o, "high": h, "low": l, "close": c,
            "vol": 1.0, "volCcyQuote": 1.0, "confirm": confirm}


def candles_planos(n=30, preco=100.0, base=T0):
    """Pano de fundo neutro, quando o teste so precisa de historico valido."""
    return [make_candle(base + i * H, preco, preco + 0.1, preco - 0.1, preco)
            for i in range(n)]


def candles_alta_com_rompimento():
    """
    Tendencia de alta com um topo fractal confirmado e fechamento acima dele --
    o cenario que faz try_map_new_zone devolver um Setup A.
    """
    seq = [100, 101, 102, 103, 104, 106, 104.5, 103.5, 104.2, 104.8,
           106.5, 105.8, 105.9, 106.0, 106.1, 106.3, 106.5, 106.7,
           106.9, 107.1, 107.3]
    out = []
    for i, c in enumerate(seq):
        o = seq[i - 1] if i > 0 else c
        out.append(make_candle(T0 + i * H, o, max(o, c) + 0.05,
                               min(o, c) - 0.05, c))
    return out


# ---------------------------------------------------------------------------
# v5, item 1 -- confirmar uma zona tambem arma cooldown
# ---------------------------------------------------------------------------

def test_v5_item1_confirmacao_arma_cooldown():
    """
    O ramo 'confirmado' era o UNICO que limpava a zona sem armar cooldown, e o
    dedupe por par so enxerga status='entrado' (o insert nasce 'candidato').
    Na janela entre a confirmacao e a edicao manual do sinais.md nenhum dos
    dois guards estava ativo. Evidencia real: LINK #25/#27, mesmo nivel 11.833,
    ambos -1R -- o proprio caso que o CHANGELOG v4 item 3 dizia ter corrigido.
    """
    zone = m._nova_zona("B", "compra", 100.0, 1.0, T0)
    # candle dentro da zona, corpo de alta, fecha colado na maxima -> rejeicao
    conf = make_candle(T0 + H, 99.9, 100.3, 99.85, 100.28)
    candles = candles_planos(30, 100.0) + [conf]
    assert m.check_zone_confirmation(zone, candles) == "confirmado", \
        "cenario mal construido: este candle deveria confirmar a zona"

    pair_state = m.default_pair_state()
    pair_state["zone"] = zone
    pair_state["status"] = "zona_mapeada_setup_B"

    m.process_single_pair("TEST-USDT-SWAP", pair_state, candles,
                          candles_planos(60, 100.0), "lateral", 1.0)

    cds = pair_state.get("cooldowns", {})
    assert "compra" in cds, (
        "BUG v5 #1 REGREDIU: confirmar a zona limpou o estado sem armar "
        "cooldown -- o mesmo nivel volta a virar sinal no ciclo seguinte."
    )
    assert abs(cds["compra"]["level"] - 100.0) < 1e-9
    assert cds["compra"]["until_ts"] > candles[-1]["ts"]


# ---------------------------------------------------------------------------
# v5, item 2 -- Setup A tambem respeita cooldown
# ---------------------------------------------------------------------------

def test_v5_item2_setup_a_respeita_cooldown():
    """
    level_blocked_by_cooldown so era chamado dentro dos dois loops do Setup B;
    o ramo do Setup A retornava antes de qualquer checagem.
    """
    candles = candles_alta_com_rompimento()
    zona = m.try_map_new_zone("alta", candles, candles, 1.0, None)
    assert zona is not None and zona["setup"] == "A", \
        "cenario mal construido: esperava um Setup A aqui"

    cooldowns = {"compra": {"level": zona["level"],
                            "until_ts": candles[-1]["ts"] + 8 * H}}
    bloqueada = m.try_map_new_zone("alta", candles, candles, 1.0, cooldowns)
    assert bloqueada is None or bloqueada["setup"] != "A", (
        "BUG v5 #2 REGREDIU: Setup A mapeou zona num nivel em cooldown."
    )


# ---------------------------------------------------------------------------
# v5, item 3 -- o mesmo candle nao pode ser processado duas vezes
# ---------------------------------------------------------------------------

def test_v5_item3_candle_repetido_nao_conta_duas_vezes():
    """
    Toda a logica de ciclo de vida le exatamente um candle (o ultimo fechado).
    Se o cron disparar duas vezes na mesma hora, o mesmo candle contava um
    segundo toque e mais um candle de idade. last_1h_ts existia desde a v2 e
    nunca era escrito por caminho nenhum do codigo.
    """
    zone = m._nova_zona("B", "venda", 100.0, 1.0, T0)
    toque = make_candle(T0 + H, 99.9, 100.1, 99.8, 99.95)  # toca, nao confirma
    candles = candles_planos(30, 99.0) + [toque]
    c4h = candles_planos(60, 99.0)

    pair_state = m.default_pair_state()
    pair_state["zone"] = zone
    pair_state["status"] = "zona_mapeada_setup_B"

    m.process_single_pair("TEST", pair_state, candles, c4h, "lateral", 1.0)
    toques_1 = pair_state["zone"]["touches"]
    m.process_single_pair("TEST", pair_state, candles, c4h, "lateral", 1.0)
    toques_2 = pair_state["zone"]["touches"]

    assert toques_1 == 1, f"o toque deveria ter sido contado uma vez, veio {toques_1}"
    assert toques_1 == toques_2, (
        f"BUG v5 #3 REGREDIU: reprocessar o MESMO candle mudou os toques "
        f"({toques_1} -> {toques_2})."
    )


# ---------------------------------------------------------------------------
# v5, item 4 -- toque reseta o contador de expiracao
# ---------------------------------------------------------------------------

def _avanca(pair_state, c4h, ts, preco, zona_preco=None):
    """Roda um ciclo com um candle novo em `ts`."""
    if zona_preco is None:
        c = make_candle(ts, preco, preco + 0.2, preco - 0.2, preco)
    else:
        c = zona_preco
    m.process_single_pair("TEST", pair_state, candles_planos(30, preco) + [c],
                          c4h, "lateral", 1.0)


def test_v5_item4_toque_reseta_contador_de_expiracao():
    """
    A regra da secao 2 do plano e '8 candles SEM TOQUE ou 3 toques'. O codigo
    nunca resetava no toque, entao eram 8 candles totais -- uma zona ativa,
    sendo testada, expirava por tempo.
    """
    zone = m._nova_zona("B", "venda", 100.0, 1.0, T0)
    c4h = candles_planos(60, 98.0)
    pair_state = m.default_pair_state()
    pair_state["zone"] = zone
    pair_state["status"] = "zona_mapeada_setup_B"

    for i in range(1, 7):  # 6 candles longe da zona
        _avanca(pair_state, c4h, T0 + i * H, 98.0)
    assert pair_state["zone"] is not None, "expirou cedo demais (antes de 8)"

    toque = make_candle(T0 + 7 * H, 99.9, 100.1, 99.8, 99.95)
    _avanca(pair_state, c4h, T0 + 7 * H, 99.0, zona_preco=toque)
    assert pair_state["zone"] is not None, "nao deveria expirar no toque"
    assert pair_state["zone"]["candles_since_creation"] == 0, (
        "BUG v5 #4 REGREDIU: o toque nao resetou o contador de candles sem toque."
    )

    for i in range(8, 14):  # mais 6 sem toque -- ainda vive
        _avanca(pair_state, c4h, T0 + i * H, 98.0)
    assert pair_state["zone"] is not None, (
        "BUG v5 #4 REGREDIU: expirou contando desde a criacao, nao desde o "
        "ultimo toque."
    )


def test_v5_item3_expiracao_usa_timestamp_e_nao_numero_de_execucoes():
    """
    Um unico ciclo que chega 9 horas depois da criacao (cron que falhou o dia
    inteiro) tem de expirar a zona -- antes isso levaria 8 execucoes.
    """
    zone = m._nova_zona("B", "venda", 100.0, 1.0, T0)
    pair_state = m.default_pair_state()
    pair_state["zone"] = zone
    pair_state["status"] = "zona_mapeada_setup_B"

    tarde = T0 + 9 * H
    candles = candles_planos(30, 98.0) + [make_candle(tarde, 98, 98.2, 97.8, 98)]
    m.process_single_pair("TEST", pair_state, candles, candles_planos(60, 98.0),
                          "lateral", 1.0)
    assert pair_state["zone"] is None, (
        "BUG v5 #3 REGREDIU: a zona sobreviveu a um gap de 9 candles porque a "
        "expiracao conta execucoes do script, nao candles."
    )
    assert pair_state["status"].startswith("zona_expirada")


# ---------------------------------------------------------------------------
# v5, item 5 -- alvo mais recente vs mais proximo
# ---------------------------------------------------------------------------

def test_v5_item5_alvo_recente_vs_proximo():
    """
    Caso real: XRP compra manteve alvo_sugerido 1.4388 enquanto o preco caia de
    1.4028 para 1.3597, inflando o R:R de 3.36 para 8.40 -- porque a regra pega
    o pivo oposto MAIS RECENTE, nao o mais PROXIMO. Versao sintetica: um topo
    proximo (106) mais antigo e um topo distante (112) mais recente -- o pior
    caso, que e exatamente o que acontece quando o preco cai e deixa para tras
    um topo alto e recente.
    """
    seq = [100, 101, 102, 103, 104, 106, 104, 103, 102, 101,
           100, 99, 98, 112, 97, 96, 95, 94, 93, 92, 91]
    candles = []
    for i, c in enumerate(seq):
        o = seq[i - 1] if i > 0 else c
        candles.append(make_candle(T0 + i * H, o, max(o, c) + 0.05,
                                   min(o, c) - 0.05, c))
    px = candles[-1]["close"]
    recente = m.nearest_target_candidate("compra", candles, px)
    proximo = m.nearest_target_candidate("compra", candles, px, modo="proximo")
    assert recente is not None and proximo is not None, "cenario mal construido"
    assert proximo < recente, (
        f"esperava alvos diferentes: proximo={proximo}, recente={recente} -- "
        f"o cenario precisa de dois pivos opostos em distancias diferentes"
    )


def test_v5_item5_compute_suggestion_devolve_os_dois_alvos():
    candles = candles_alta_com_rompimento()
    zone = m._nova_zona("A", "venda", 107.0, 1.0, candles[-1]["ts"])
    sug = m.compute_suggestion(zone, candles, 1.0)
    for campo in ("alvo_sugerido", "rr_sugerido", "regra_alvo", "alvo_recente",
                  "rr_recente", "alvo_proximo", "rr_proximo"):
        assert campo in sug, f"compute_suggestion nao devolveu o campo '{campo}'"


def test_v6_alvo_autoritativo_e_proximo():
    """
    A regra autoritativa foi trocada de 'recente' para 'proximo' na v6, depois
    do replay mostrar que exigir mais R:R piorava monotonicamente o resultado
    -- sintoma de que 'recente' selecionava alvos distantes e velhos, nao
    teses melhores. alvo_sugerido/rr_sugerido devem refletir isso agora.
    """
    seq = [100, 101, 102, 103, 104, 106, 104, 103, 102, 101,
           100, 99, 98, 112, 97, 96, 95, 94, 93, 92, 91]
    candles = []
    for i, c in enumerate(seq):
        o = seq[i - 1] if i > 0 else c
        candles.append(make_candle(T0 + i * H, o, max(o, c) + 0.05,
                                   min(o, c) - 0.05, c))
    zone = m._nova_zona("A", "compra", 90.0, 1.0, candles[-1]["ts"])
    sug = m.compute_suggestion(zone, candles, 1.0)
    assert sug["regra_alvo"] == "proximo", (
        f"regra_alvo deveria ser 'proximo' (autoritativa na v6), veio "
        f"'{sug['regra_alvo']}'"
    )
    assert sug["alvo_sugerido"] == sug["alvo_proximo"] != sug["alvo_recente"], (
        "alvo_sugerido deveria ser igual ao alvo_proximo (autoritativo) e "
        "diferente do alvo_recente (secundario) neste cenario"
    )


# ---------------------------------------------------------------------------
# v5, item 7 -- um cooldown por DIRECAO
# ---------------------------------------------------------------------------

def test_v5_item7_cooldowns_por_direcao_nao_se_sobrescrevem():
    cds = {
        "compra": {"level": 100.0, "until_ts": T0 + 8 * H},
        "venda": {"level": 200.0, "until_ts": T0 + 8 * H},
    }
    assert m.level_blocked_by_cooldown(cds, "compra", 100.0, 1.0, T0)
    assert m.level_blocked_by_cooldown(cds, "venda", 200.0, 1.0, T0), (
        "BUG v5 #7 REGREDIU: cooldown de uma direcao apagou o da outra."
    )
    assert not m.level_blocked_by_cooldown(cds, "compra", 200.0, 1.0, T0), \
        "nivel de outra direcao nao deveria bloquear"
    assert not m.level_blocked_by_cooldown(cds, "compra", 100.0, 1.0, T0 + 9 * H), \
        "cooldown ja deveria ter expirado"


def test_v5_item7_migracao_do_slot_unico_preserva_cooldown():
    """load_state() converte o formato antigo sem perder o cooldown ativo."""
    antigo = {"level": 55.0, "direction": "venda", "until_ts": T0 + 8 * H}
    assert m.level_blocked_by_cooldown(antigo, "venda", 55.0, 1.0, T0), (
        "level_blocked_by_cooldown deveria aceitar o formato antigo enquanto o "
        "state.json nao passou pela migracao"
    )


# ---------------------------------------------------------------------------
# desfecho mecanico -- base de mae_r/mfe_r, do backfill e da calibracao
# ---------------------------------------------------------------------------

def test_desfecho_mecanico_stop_antes_do_alvo_no_mesmo_candle():
    """Convencao conservadora: stop e alvo no mesmo candle -> conta o stop."""
    candles = [make_candle(T0 + H, 100, 102.5, 98.5, 101)]
    r, motivo, _, _, n = m.desfecho_mecanico("compra", 100.0, 99.0, 102.0, 2.0,
                                             T0, candles)
    assert r == -1.0 and motivo == "stop_automatico", \
        f"esperava stop primeiro, veio {r} / {motivo}"
    assert n == 1


def test_desfecho_mecanico_mae_mfe_em_multiplos_de_r():
    # compra em 100, stop 99 -> risco 1.0. Candle vai a 99.5 e 101.5.
    candles = [make_candle(T0 + H, 100, 101.5, 99.5, 101)]
    r, _, mae, mfe, _ = m.desfecho_mecanico("compra", 100.0, 99.0, 105.0, 5.0,
                                            T0, candles)
    assert r is None, "nao deveria ter resolvido (nem stop nem alvo tocados)"
    assert abs(mae - 0.5) < 1e-9, f"MAE esperado 0.5R, veio {mae}"
    assert abs(mfe - 1.5) < 1e-9, f"MFE esperado 1.5R, veio {mfe}"


def test_desfecho_mecanico_ignora_candles_anteriores_a_confirmacao():
    """Nao pode olhar para tras da confirmacao -- seria vazamento de futuro."""
    antes = make_candle(T0 - H, 100, 200, 50, 100)   # varreria tudo
    depois = make_candle(T0 + H, 100, 100.2, 99.8, 100)
    r, _, mae, mfe, _ = m.desfecho_mecanico("compra", 100.0, 99.0, 105.0, 5.0,
                                            T0, [antes, depois])
    assert r is None, "o candle anterior a confirmacao nao pode resolver o trade"
    assert mae <= 0.21 and mfe <= 0.21, f"MAE/MFE contaminados: {mae}/{mfe}"


def test_desfecho_mecanico_sem_breakeven_apos_r_e_identico_a_antes():
    """breakeven_apos_r=None (o default, o que producao sempre usa) nao pode
    mudar nenhum resultado -- essa opcao existe so pro replay testar a ideia."""
    candles = [make_candle(T0 + H, 100, 101.5, 98.9, 99.0)]  # vai a favor, volta e estoura o stop
    r1 = m.desfecho_mecanico("compra", 100.0, 99.0, 110.0, 10.0, T0, candles)
    r2 = m.desfecho_mecanico("compra", 100.0, 99.0, 110.0, 10.0, T0, candles,
                             breakeven_apos_r=None)
    assert r1 == r2 == (-1.0, "stop_automatico", 1.1, 1.5, 1)


def test_desfecho_mecanico_breakeven_zera_perda_depois_de_1r_a_favor():
    """
    Candle 1 leva o preco a +1R (favor); candle 2 volta e bate no stop
    original. Com breakeven_apos_r=1.0, o stop efetivo no candle 2 ja e a
    entrada -- resultado deve ser 0R (breakeven), nao -1R.
    """
    c1 = make_candle(T0 + H, 100, 101, 99.5, 100.8)       # chega a +1R (high=101)
    c2 = make_candle(T0 + 2 * H, 100.8, 100.9, 98.0, 98.5)  # despenca, passa por 100 e por 99
    r, motivo, mae, mfe, n = m.desfecho_mecanico(
        "compra", 100.0, 99.0, 110.0, 10.0, T0, [c1, c2], breakeven_apos_r=1.0
    )
    assert (r, motivo) == (0.0, "breakeven_automatico"), (
        f"esperava breakeven (0.0), veio ({r}, {motivo})"
    )
    assert n == 2


def test_desfecho_mecanico_breakeven_nao_afeta_stop_no_mesmo_candle_que_ativa():
    """
    O candle que primeiro atinge +1R nao pode usar o stop novo NELE MESMO --
    so a partir do candle seguinte. Aqui o candle unico vai a +1R e tambem
    bate no stop original, tudo no mesmo candle: deve continuar valendo -1R.
    """
    c1 = make_candle(T0 + H, 100, 101, 98.5, 99.0)  # toca 101 (+1R) e 98.5 (stop -1R)
    r, motivo, _, _, _ = m.desfecho_mecanico(
        "compra", 100.0, 99.0, 110.0, 10.0, T0, [c1], breakeven_apos_r=1.0
    )
    assert (r, motivo) == (-1.0, "stop_automatico"), (
        f"stop do candle de ativacao nao deveria virar breakeven -- veio ({r}, {motivo})"
    )


def _run_all():
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    falhou = 0
    for t in tests:
        try:
            t()
            print(f"PASS  {t.__name__}")
        except AssertionError as e:
            falhou += 1
            print(f"FAIL  {t.__name__}: {e}")
    print(f"\n{len(tests) - falhou}/{len(tests)} testes passaram")
    if falhou:
        sys.exit(1)


if __name__ == "__main__":
    try:
        _run_all()
    finally:
        os.remove(_TMP_DB.name)  # nunca deixa o .db temporario para tras
