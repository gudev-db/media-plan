import streamlit as st


def render_examples():
    st.header("Exemplos por Etapa do Funil")

    tab_topo, tab_meio, tab_fundo = st.tabs(["Topo", "Meio", "Fundo"])

    with tab_topo:
        st.markdown("""
        ### 📋 Exemplo - Topo do Funil (Awareness)
        **Campanha:** Conscientização da Marca X
        **Objetivo:** Aumentar reconhecimento de marca
        **Etapa do Funil:** Topo
        **OKRs Típicos:** Impressões, Alcance, Frequência, CPM
        """)

        st.markdown("""
        #### 🎯 Metas Recomendadas:
        - Impressões: 5.000.000
        - Alcance: 2.200.000
        - Frequência média: 2.3
        - CPM: R$ 15-20

        #### 📊 Alocação Recomendada:
        | Plataforma | % Budget | Valor (R$) | Criativos Principais |
        |------------|----------|------------|----------------------|
        | Meta Ads | 50% | 75.000 | Vídeo (60%), Estático (40%) |
        | YouTube | 30% | 45.000 | Vídeo (100%) |
        | Programática | 20% | 30.000 | Banner (70%), Vídeo (30%) |
        """)

    with tab_meio:
        st.markdown("""
        ### 📋 Exemplo - Meio do Funil (Consideração)
        **Campanha:** Engajamento Produto Y
        **Objetivo:** Gerar interesse no produto
        **Etapa do Funil:** Meio
        **OKRs Típicos:** CTR, Video Views, Engajamento
        """)

        st.markdown("""
        #### 🎯 Metas Recomendadas:
        - CTR: 1.8-2.5%
        - Video Views: 500.000
        - Engajamento: 3.5%

        #### 📊 Alocação Recomendada:
        | Plataforma | % Budget | Valor (R$) | Criativos Principais |
        |------------|----------|------------|----------------------|
        | Meta Ads | 40% | 32.000 | Carrossel (50%), Vídeo (50%) |
        | LinkedIn | 30% | 24.000 | Estático (70%), Vídeo (30%) |
        | Google Ads | 30% | 24.000 | Display (60%), Vídeo (40%) |
        """)

    with tab_fundo:
        st.markdown("""
        ### 📋 Exemplo - Fundo do Funil (Conversão)
        **Campanha:** Vendas Produto Z
        **Objetivo:** Gerar vendas diretas
        **Etapa do Funil:** Fundo
        **OKRs Típicos:** Conversões, ROAS, CPA
        """)

        st.markdown("""
        #### 🎯 Metas Recomendadas:
        - Conversões: 1.500
        - ROAS: 3.5x
        - CPA: R$ 80-100

        #### 📊 Alocação Recomendada:
        | Plataforma | % Budget | Valor (R$) | Criativos Principais |
        |------------|----------|------------|----------------------|
        | Meta Ads | 60% | 72.000 | Coleção (70%), Estático (30%) |
        | Google Ads | 40% | 48.000 | Shopping (100%) |
        """)
