import streamlit as st
import pandas as pd
import google.generativeai as genai
import os

# Configuração inicial
st.set_page_config(
    layout="wide",
    page_title="IA de Planejamento de Mídia",
    page_icon="📊"
)

# CSS personalizado
st.markdown("""
<style>
    /* Estilos gerais */
    .main {
        background-color: #f5f7fa;
    }
    .stTextInput input, .stSelectbox select, .stTextArea textarea {
        border-radius: 8px !important;
        border: 1px solid #d1d5db !important;
    }
    .stButton button {
        background-color: #4f46e5 !important;
        color: white !important;
        border-radius: 8px !important;
        padding: 10px 24px !important;
        font-weight: 500 !important;
    }
    .stButton button:hover {
        background-color: #4338ca !important;
    }
    /* Cards de resultado */
    .result-card {
        background-color: white;
        border-radius: 12px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    /* Tabelas */
    table {
        width: 100%;
        border-collapse: collapse;
    }
    th, td {
        padding: 12px;
        text-align: left;
        border-bottom: 1px solid #e5e7eb;
    }
    th {
        background-color: #f9fafb;
        font-weight: 600;
    }
    /* Abas */
    .stTabs [aria-selected="true"] {
        color: #4f46e5 !important;
        font-weight: 600 !important;
    }
</style>
""", unsafe_allow_html=True)

# Inicializar Gemini
gemini_api_key = os.getenv("GEM_API_KEY")
genai.configure(api_key=gemini_api_key)
modelo_texto = genai.GenerativeModel("gemini-1.5-flash")

# Título do aplicativo
st.title("📊 IA para Planejamento de Mídia")
st.markdown("""
**Crie planos de mídia otimizados com alocação automática de verba por estratégia, plataforma e localização.**
""")

# Abas principais
tab1, tab2 = st.tabs(["📋 Criar Novo Plano", "📊 Exemplos e Modelos"])

with tab1:
    st.header("Informações do Plano de Mídia")
    
    with st.form("plano_midia_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            objetivo_campanha = st.selectbox(
                "Objetivo da Campanha*",
                ["Awareness", "Consideração", "Compra/Leads"],
                index=0
            )
            
            tipo_campanha = st.selectbox(
                "Tipo de Campanha*",
                ["Alcance", "Engajamento", "Tráfego", "Conversão"],
                index=0
            )
            
            budget = st.number_input(
                "Budget Total (R$)*",
                min_value=1000,
                value=100000,
                step=1000
            )
            
            ferramentas = st.multiselect(
                "Ferramentas/Plataformas*",
                ["Meta Ads (Facebook/Instagram)", "Google Ads", "TikTok", "LinkedIn", 
                 "YouTube", "Mídia Programática", "Twitter", "Pinterest"],
                default=["Meta Ads (Facebook/Instagram)", "Google Ads"]
            )
            
        with col2:
            localizacao_primaria = st.text_input(
                "Localização Primária (Estados)*",
                placeholder="Ex: MT, GO, RS",
                value="MT, GO, RS"
            )
            
            localizacao_secundaria = st.text_input(
                "Localização Secundária (Estados)",
                placeholder="Ex: SP, MG, RJ",
                value="SP, MG, RJ"
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
        
        okrs = st.multiselect(
            "OKRs (Objetivos-chave)*",
            ["Impressões", "Engajamento", "Sessões", "Video Views", 
             "CTR", "Conversões", "ROAS", "Alcance"],
            default=["Impressões", "Engajamento"]
        )
        
        observacoes = st.text_area(
            "Observações Adicionais",
            placeholder="Informações extras sobre a campanha, concorrentes, etc."
        )
        
        submitted = st.form_submit_button("Gerar Plano de Mídia")
    
    if submitted:
        if not objetivo_campanha or not tipo_campanha or not budget or not ferramentas:
            st.error("Por favor, preencha todos os campos obrigatórios (*)")
        else:
            with st.spinner('Analisando dados e criando plano de mídia otimizado...'):
                # Construir prompt para a IA
                prompt = f"""
                Você é um especialista em planejamento de mídia digital. Crie um plano detalhado com base nestes parâmetros:

                **Objetivo da Campanha:** {objetivo_campanha}
                **Tipo de Campanha:** {tipo_campanha}
                **Budget Total:** R$ {budget:,.2f}
                **Ferramentas/Plataformas:** {", ".join(ferramentas)}
                **Localização Primária:** {localizacao_primaria}
                **Localização Secundária:** {localizacao_secundaria}
                **Tipo de Público:** {tipo_publico}
                **Tipos de Criativo:** {", ".join(tipo_criativo)}
                **OKRs:** {", ".join(okrs)}
                **Observações:** {observacoes or "Nenhuma"}

                **Saída Esperada:**
                1. **Recomendação Estratégica**: Breve análise (100-150 palavras) explicando a estratégia recomendada
                2. **Distribuição de Budget**: Tabela mostrando a divisão percentual e valores por:
                   - Plataforma
                   - Localização (primária/secundária)
                   - Tipo de criativo
                3. **Previsão de Resultados**: Tabela com métricas esperadas para cada plataforma
                4. **Recomendações de Público**: Detalhamento dos públicos-alvo sugeridos
                5. **Cronograma Sugerido**: Distribuição temporal do budget

                **Formato:**
                - Use markdown com headers (##, ###)
                - Tabelas em formato markdown
                - Dados concretos e justificativas
                - Foco em performance e ROI

                **Exemplo de tabela esperada:**
                | Plataforma       | % Budget | Valor (R$) | Foco Principal | Criativos Recomendados |
                |------------------|----------|------------|-----------------|------------------------|
                | Meta Ads         | 45%      | 45.000,00  | Alcance         | Vídeo, Carrossel       |
                """
                
                # Chamar a IA
                response = modelo_texto.generate_content(prompt)
                
                # Exibir resultados
                st.success("Plano de Mídia gerado com sucesso!")
                
                # Dividir a resposta em seções
                resposta = response.text
                
                st.markdown("## 📌 Recomendação Estratégica")
                st.markdown(resposta.split("## 📌 Recomendação Estratégica")[1].split("##")[0])
                
                if "## 📊 Distribuição de Budget" in resposta:
                    st.markdown("## 📊 Distribuição de Budget")
                    st.markdown(resposta.split("## 📊 Distribuição de Budget")[1].split("##")[0])
                
                if "## 📈 Previsão de Resultados" in resposta:
                    st.markdown("## 📈 Previsão de Resultados")
                    st.markdown(resposta.split("## 📈 Previsão de Resultados")[1].split("##")[0])
                
                if "## 🎯 Recomendações de Público" in resposta:
                    st.markdown("## 🎯 Recomendações de Público")
                    st.markdown(resposta.split("## 🎯 Recomendações de Público")[1].split("##")[0])
                
                if "## 📅 Cronograma Sugerido" in resposta:
                    st.markdown("## 📅 Cronograma Sugerido")
                    st.markdown(resposta.split("## 📅 Cronograma Sugerido")[1])
                
                # Botão para baixar o plano
                st.download_button(
                    label="📥 Baixar Plano Completo",
                    data=resposta,
                    file_name=f"plano_midia_{objetivo_campanha}_{budget}.md",
                    mime="text/markdown"
                )

with tab2:
    st.header("Modelos e Exemplos de Planejamento")
    
    st.markdown("""
    ### 📋 Modelo de Plano de Mídia (Exemplo)
    
    **Campanha:** Syngenta - Awareness
    **Budget:** R$ 100.000,00
    """)
    
    # Tabela de exemplo
    exemplo_data = {
        "Plataforma": ["Meta Ads", "Google Ads", "TikTok", "Total"],
        "% Budget": ["45%", "35%", "20%", "100%"],
        "Investimento (R$)": ["45.000", "35.000", "20.000", "100.000"],
        "Localização Primária": ["70%", "65%", "75%", ""],
        "Localização Secundária": ["30%", "35%", "25%", ""],
        "Criativos": ["Vídeo (60%), Estático (40%)", "Display (50%), Vídeo (50%)", "Vídeo (100%)", ""],
        "OKRs Principais": ["Impressões, Alcance", "Impressões, CTR", "Video Views", ""]
    }
    
    st.dataframe(pd.DataFrame(exemplo_data), hide_index=True)
    
    st.markdown("""
    ### 📊 Métricas Esperadas (Exemplo)
    """)
    
    metricas_data = {
        "Plataforma": ["Meta Ads", "Google Ads", "TikTok"],
        "Impressões": ["2.500.000", "1.800.000", "1.200.000"],
        "CPM (R$)": ["18,00", "19,44", "16,67"],
        "Alcance": ["1.100.000", "850.000", "600.000"],
        "Video Views": ["450.000", "300.000", "800.000"],
        "Engajamento": ["3,2%", "1,8%", "4,5%"]
    }
    
    st.dataframe(pd.DataFrame(metricas_data), hide_index=True)
    
    st.markdown("""
    ### 📌 Dicas para Otimização
    1. **Priorize plataformas** conforme o público-alvo
    2. **Teste diferentes criativos** e alocações de budget
    3. **Ajuste geotargeting** baseado em performance
    4. **Monitore frequência** para evitar saturação
    5. **Reavalie semanalmente** e redistribua verba
    """)

# Rodapé
st.markdown("---")
st.caption("""
Ferramenta de IA para Planejamento de Mídia - Otimize suas campanhas com alocação inteligente de budget.
""")
