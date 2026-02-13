import streamlit as st

from utils.constants import (
    TIPOS_CAMPANHA,
    ETAPAS_FUNIL,
    KPIS_POR_ETAPA,
    BENCHMARKS_BR,
    PLATAFORMA_OBJETIVOS,
    TEMPLATES_ALOCACAO_BUDGET,
)
from utils.generators import (
    gerar_recomendacao_estrategica,
    gerar_distribuicao_budget,
    gerar_previsao_resultados,
    gerar_recomendacoes_publico,
    gerar_cronograma,
)


def _build_benchmark_context(ferramentas: list) -> str:
    """Monta texto de benchmarks para as plataformas selecionadas."""
    linhas = []
    for plat in ferramentas:
        bench = BENCHMARKS_BR.get(plat)
        if not bench:
            continue
        partes = []
        for metrica, vals in bench.items():
            partes.append(f"{metrica}: {vals['unidade']}{vals['medio']}")
        linhas.append(f"  {plat}: {' | '.join(partes)}")
    return "\n".join(linhas) if linhas else ""


def _build_kpi_hierarchy_summary(metricas: dict) -> dict:
    """Resume os KPIs selecionados em primários, secundários e terciários."""
    primarios = []
    secundarios = []
    terciarios = []
    for nome, info in metricas.items():
        if info.get("selecionada"):
            tier = info.get("hierarquia", "")
            if tier == "primario":
                primarios.append(nome)
            elif tier == "secundario":
                secundarios.append(nome)
            else:
                terciarios.append(nome)
    return {"primarios": primarios, "secundarios": secundarios, "terciarios": terciarios}


def _benchmark_help(kpi_nome: str, ferramentas: list) -> str:
    """Gera help text com benchmarks das plataformas selecionadas para um KPI."""
    partes = []
    mapping = {"CPM": "CPM", "CPC": "CPC", "CTR": "CTR", "CPA": "CPA", "ROAS": "ROAS", "CPL": "CPL"}
    for plat in ferramentas:
        bench = BENCHMARKS_BR.get(plat, {})
        for key, label in mapping.items():
            if key.lower() in kpi_nome.lower() and key in bench:
                v = bench[key]
                partes.append(f"{plat}: {v['unidade']}{v['min']}-{v['max']}")
                break
    return " | ".join(partes) if partes else ""


def render_form(modelo):
    st.header("Informações do Plano de Mídia")

    with st.form("plano_midia_form"):
        col1, col2 = st.columns(2, gap="small")

        with col1:
            objetivo_campanha = st.text_input(
                "Nome/Objetivo da Campanha*",
                placeholder="Ex: Campanha de Awareness - Marca X",
                value="Campanha de Awareness - Marca X"
            )

            tipo_campanha = st.selectbox(
                "Tipo de Campanha*",
                TIPOS_CAMPANHA,
                index=0
            )

            etapa_funil = st.selectbox(
                "Etapa do Funil*",
                ETAPAS_FUNIL,
                index=0,
                help="Consciência: Exposição | Interesse: Atração | Consideração: Avaliação | Intenção: Decisão | Conversão: Ação | Retenção: Fidelização"
            )

            budget = st.number_input(
                "Budget Total (R$)*",
                min_value=1000,
                value=100000,
                step=1000
            )

            periodo = st.selectbox(
                "Período da Campanha*",
                ["1 mês", "2 meses", "3 meses", "6 meses", "1 ano"],
                index=0
            )

        with col2:
            ferramentas = st.multiselect(
                "Ferramentas/Plataformas*",
                ["Meta Ads (Facebook/Instagram)", "Google Ads", "TikTok", "LinkedIn",
                 "YouTube", "Mídia Programática", "Twitter", "Pinterest"],
                default=["Meta Ads (Facebook/Instagram)", "Google Ads"]
            )

            localizacao_primaria = st.text_input(
                "Localização Primária (Estados)*",
                placeholder="Ex: MT, GO, RS",
                value="MT, GO, RS"
            )

            localizacao_secundaria = st.text_input(
                "Localização Secundária (Cidades)",
                placeholder="Ex: Rio de Janeiro, São Paulo, Cuiabá",
                value="Rio de Janeiro, São Paulo, Cuiabá"
            )

            tipo_publico = st.selectbox(
                "Tipo de Público*",
                ["Interesses", "Lookalike Audience (LAL)", "Base de Clientes",
                 "Retargeting", "Comportamento", "Demográfico"],
                index=0
            )

            tipo_criativo = st.multiselect(
                "Tipos de Criativo*",
                ["Estático", "Vídeo", "Carrossel", "Motion", "Story", "Coleção"],
                default=["Estático", "Vídeo"]
            )

        # ── KPIs Hierárquicos ──────────────────────────────────────
        kpis_etapa = KPIS_POR_ETAPA.get(etapa_funil, {})
        metricas = {}

        # Primários — sempre visíveis, pré-selecionados
        primarios = kpis_etapa.get("primarios", [])
        if primarios:
            st.markdown("**KPIs Primários** *(indicadores-chave para esta etapa)*")
            for kpi in primarios:
                nome = kpi["nome"]
                bench_help = _benchmark_help(nome, ferramentas)
                help_txt = kpi["faixa_tipica"]
                if bench_help:
                    help_txt += f" — Benchmarks: {bench_help}"

                col_a, col_b = st.columns([1, 2], gap="small")
                with col_a:
                    selecionada = st.checkbox(
                        nome, value=True,
                        key=f"check_{etapa_funil}_{nome}",
                        help=kpi["descricao"]
                    )
                with col_b:
                    valor = st.text_input(
                        f"Meta para {nome}",
                        placeholder=kpi["faixa_tipica"],
                        key=f"input_{etapa_funil}_{nome}",
                        disabled=not selecionada,
                        help=help_txt
                    )
                metricas[nome] = {
                    "selecionada": selecionada,
                    "valor": valor,
                    "descricao": kpi["descricao"],
                    "hierarquia": "primario",
                    "formula": kpi["formula"],
                }

        # Secundários — dentro de expander
        secundarios = kpis_etapa.get("secundarios", [])
        if secundarios:
            with st.expander("Indicadores Secundários"):
                for kpi in secundarios:
                    nome = kpi["nome"]
                    bench_help = _benchmark_help(nome, ferramentas)
                    help_txt = kpi["faixa_tipica"]
                    if bench_help:
                        help_txt += f" — Benchmarks: {bench_help}"

                    col_a, col_b = st.columns([1, 2], gap="small")
                    with col_a:
                        selecionada = st.checkbox(
                            nome, value=False,
                            key=f"check_{etapa_funil}_{nome}",
                            help=kpi["descricao"]
                        )
                    with col_b:
                        valor = st.text_input(
                            f"Meta para {nome}",
                            placeholder=kpi["faixa_tipica"],
                            key=f"input_{etapa_funil}_{nome}",
                            disabled=not selecionada,
                            help=help_txt
                        )
                    metricas[nome] = {
                        "selecionada": selecionada,
                        "valor": valor,
                        "descricao": kpi["descricao"],
                        "hierarquia": "secundario",
                        "formula": kpi["formula"],
                    }

        # Terciários — dentro de expander colapsado
        terciarios = kpis_etapa.get("terciarios", [])
        if terciarios:
            with st.expander("Indicadores Terciários (Avançado)"):
                for kpi in terciarios:
                    nome = kpi["nome"]
                    bench_help = _benchmark_help(nome, ferramentas)
                    help_txt = kpi["faixa_tipica"]
                    if bench_help:
                        help_txt += f" — Benchmarks: {bench_help}"

                    col_a, col_b = st.columns([1, 2], gap="small")
                    with col_a:
                        selecionada = st.checkbox(
                            nome, value=False,
                            key=f"check_{etapa_funil}_{nome}",
                            help=kpi["descricao"]
                        )
                    with col_b:
                        valor = st.text_input(
                            f"Meta para {nome}",
                            placeholder=kpi["faixa_tipica"],
                            key=f"input_{etapa_funil}_{nome}",
                            disabled=not selecionada,
                            help=help_txt
                        )
                    metricas[nome] = {
                        "selecionada": selecionada,
                        "valor": valor,
                        "descricao": kpi["descricao"],
                        "hierarquia": "terciario",
                        "formula": kpi["formula"],
                    }

        detalhes_acao = st.text_area(
            "Detalhes da Ação*",
            placeholder="Descreva o produto/serviço/evento que será promovido",
            value="Campanha de produtos agrícolas para pequenos e médios produtores"
        )

        observacoes = st.text_area(
            "Observações Adicionais",
            placeholder="Informações extras sobre a campanha, concorrentes, etc."
        )

        submitted = st.form_submit_button("Gerar Plano de Mídia")

    if submitted:
        if not objetivo_campanha or not tipo_campanha or not budget or not ferramentas or not localizacao_primaria or not detalhes_acao:
            st.error("Por favor, preencha todos os campos (*)")
        else:
            benchmarks_contexto = _build_benchmark_context(ferramentas)
            kpis_hierarquia = _build_kpi_hierarchy_summary(metricas)

            params = {
                'objetivo_campanha': objetivo_campanha,
                'tipo_campanha': tipo_campanha,
                'etapa_funil': etapa_funil,
                'budget': budget,
                'periodo': periodo,
                'ferramentas': ferramentas,
                'localizacao_primaria': localizacao_primaria,
                'localizacao_secundaria': localizacao_secundaria,
                'tipo_publico': tipo_publico,
                'tipo_criativo': tipo_criativo,
                'metricas': metricas,
                'detalhes_acao': detalhes_acao,
                'observacoes': observacoes,
                'benchmarks_contexto': benchmarks_contexto,
                'kpis_hierarquia': kpis_hierarquia,
            }

            st.session_state.current_step = 1
            st.session_state.params = params

            with st.spinner(f'Gerando plano completo para {etapa_funil} do funil...'):
                pc = st.session_state.plano_completo
                pc['recomendacao_estrategica'] = gerar_recomendacao_estrategica(modelo, params)
                pc['distribuicao_budget'] = gerar_distribuicao_budget(modelo, params, pc['recomendacao_estrategica'])
                pc['previsao_resultados'] = gerar_previsao_resultados(modelo, params, pc['recomendacao_estrategica'], pc['distribuicao_budget'])
                pc['recomendacoes_publico'] = gerar_recomendacoes_publico(modelo, params, pc['recomendacao_estrategica'])
                pc['cronograma'] = gerar_cronograma(modelo, params, pc['recomendacao_estrategica'], pc['distribuicao_budget'])

            from auth.session import is_authenticated, get_current_user_id
            if is_authenticated():
                try:
                    from db.connection import get_database
                    from db.plan_repository import save_plan
                    db = get_database()
                    user_id = get_current_user_id()
                    save_plan(
                        db, user_id,
                        nome_plano=params['objetivo_campanha'],
                        params=params,
                        resultado=st.session_state.plano_completo,
                    )
                    st.success("✅ Plano gerado e salvo automaticamente!")
                except Exception as e:
                    st.warning(f"Não foi possível salvar: {e}")
