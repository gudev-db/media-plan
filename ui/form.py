import streamlit as st

from utils.constants import METRICAS_POR_ETAPA, DESCRICOES_METRICAS
from utils.generators import (
    gerar_recomendacao_estrategica,
    gerar_distribuicao_budget,
    gerar_previsao_resultados,
    gerar_recomendacoes_publico,
    gerar_cronograma,
)


def render_form(modelo):
    st.header("Informações do Plano de Mídia")

    with st.form("plano_midia_form"):
        col1, col2 = st.columns(2)

        with col1:
            objetivo_campanha = st.text_input(
                "Nome/Objetivo da Campanha*",
                placeholder="Ex: Campanha de Awareness - Marca X",
                value="Campanha de Awareness - Marca X"
            )

            tipo_campanha = st.selectbox(
                "Tipo de Campanha*",
                ["Alcance", "Engajamento", "Tráfego", "Conversão"],
                index=0
            )

            etapa_funil = st.selectbox(
                "Etapa do Funil*",
                ["Topo", "Meio", "Fundo"],
                index=0,
                help="Topo: Conscientização | Meio: Consideração | Fundo: Conversão"
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

        st.markdown("**Selecione e defina metas para os OKRs:**")

        metricas = {}
        for metrica in METRICAS_POR_ETAPA[etapa_funil]:
            col1, col2 = st.columns([1, 2])
            with col1:
                selecionada = st.checkbox(metrica, value=True, key=f"check_{metrica}")
            with col2:
                valor = st.text_input(
                    f"Meta para {metrica}",
                    placeholder=f"Ex: 500.000 {metrica.split()[0]}" if " " in metrica else f"Ex: 500.000 {metrica}",
                    key=f"input_{metrica}",
                    disabled=not selecionada
                )
            metricas[metrica] = {
                'selecionada': selecionada,
                'valor': valor,
                'descricao': DESCRICOES_METRICAS.get(metrica, "")
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
                'observacoes': observacoes
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
