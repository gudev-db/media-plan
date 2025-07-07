import streamlit as st
import pandas as pd
import google.generativeai as genai
import os
from typing import Dict, Any

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

# Estado da sessão para armazenar resultados intermediários
if 'plano_completo' not in st.session_state:
    st.session_state.plano_completo = {}
if 'current_step' not in st.session_state:
    st.session_state.current_step = 0

# Funções de geração de conteúdo com IA
def gerar_recomendacao_estrategica(params: Dict[str, Any]) -> str:
    """Gera a recomendação estratégica inicial"""
    prompt = f"""
    Como especialista em planejamento de mídia digital, analise os seguintes parâmetros e forneça uma recomendação estratégica:

    **Objetivo da Campanha:** {params['objetivo_campanha']}
    **Tipo de Campanha:** {params['tipo_campanha']}
    **Budget Total:** R$ {params['budget']:,.2f}
    **Ferramentas/Plataformas:** {", ".join(params['ferramentas'])}
    **Localização Primária:** {params['localizacao_primaria']}
    **Localização Secundária:** {params['localizacao_secundaria']}
    **Tipo de Público:** {params['tipo_publico']}
    **Tipos de Criativo:** {", ".join(params['tipo_criativo'])}
    **OKRs:** {", ".join(params['okrs'])}
    **Observações:** {params['observacoes'] or "Nenhuma"}

    Forneça:
    1. Análise estratégica (150-200 palavras)
    2. Principais oportunidades identificadas
    3. Riscos potenciais a considerar
    4. Recomendação geral de abordagem

    Formato: Markdown com headers (##, ###)
    """
    response = modelo_texto.generate_content(prompt)
    return response.text

def gerar_distribuicao_budget(params: Dict[str, Any], recomendacao_estrategica: str) -> str:
    """Gera a distribuição de budget baseada na recomendação estratégica"""
    prompt = f"""
    Com base na seguinte recomendação estratégica:
    {recomendacao_estrategica}

    E nos parâmetros originais:
    - Budget: R$ {params['budget']:,.2f}
    - Plataformas: {", ".join(params['ferramentas'])}
    - Localizações: Primária ({params['localizacao_primaria']}), Secundária ({params['localizacao_secundaria']})
    - OKRs: {", ".join(params['okrs'])}

    Crie uma tabela detalhada de distribuição de budget com:
    1. Divisão por plataforma (% e valor)
    2. Alocação geográfica (primária vs secundária)
    3. Tipos de criativos recomendados para cada
    4. Justificativa para cada alocação

    Inclua também uma breve análise (50-100 palavras) explicando a lógica de distribuição.

    Formato: Markdown com tabelas (use | para divisão)
    """
    response = modelo_texto.generate_content(prompt)
    return response.text

def gerar_previsao_resultados(params: Dict[str, Any], recomendacao_estrategica: str, distribuicao_budget: str) -> str:
    """Gera previsão de resultados baseada nos parâmetros"""
    prompt = f"""
    Com base na estratégia:
    {recomendacao_estrategica}

    E na distribuição de budget:
    {distribuicao_budget}

    Estime os resultados esperados para esta campanha considerando:
    - Objetivo: {params['objetivo_campanha']}
    - OKRs: {", ".join(params['okrs'])}
    - Budget total: R$ {params['budget']:,.2f}

    Forneça:
    1. Tabela com métricas esperadas por plataforma (impressões, alcance, engajamento, etc.)
    2. Estimativa de CPM, CPC, CTR conforme relevante
    3. Análise de potencial desempenho (50-100 palavras)
    4. Principais KPI's a monitorar

    Use dados de benchmark do setor quando aplicável.

    Formato: Markdown com tabelas
    """
    response = modelo_texto.generate_content(prompt)
    return response.text

def gerar_recomendacoes_publico(params: Dict[str, Any], recomendacao_estrategica: str) -> str:
    """Gera recomendações detalhadas de público-alvo"""
    prompt = f"""
    Para a campanha com os seguintes parâmetros:
    - Tipo de Público: {params['tipo_publico']}
    - Objetivo: {params['objetivo_campanha']}
    - Plataformas: {", ".join(params['ferramentas'])}

    E considerando a estratégia geral:
    {recomendacao_estrategica}

    Desenvolva recomendações detalhadas de público-alvo incluindo:
    1. Segmentação recomendada para cada plataforma
    2. Parâmetros de targeting específicos
    3. Tamanho estimado do público
    4. Estratégias de expansão (LAL, interesses, etc.)
    5. Considerações sobre frequência e saturação

    Formato: Markdown com listas e headers
    """
    response = modelo_texto.generate_content(prompt)
    return response.text

def gerar_cronograma(params: Dict[str, Any], recomendacao_estrategica: str, distribuicao_budget: str) -> str:
    """Gera cronograma de implementação"""
    prompt = f"""
    Com base na estratégia:
    {recomendacao_estrategica}

    E na distribuição de budget:
    {distribuicao_budget}

    Crie um cronograma detalhado para implementação desta campanha considerando:
    - Budget total: R$ {params['budget']:,.2f}
    - Plataformas: {", ".join(params['ferramentas'])}
    - OKRs: {", ".join(params['okrs'])}

    Inclua:
    1. Fases de implementação (pré-lançamento, lançamento, otimização)
    2. Distribuição temporal do budget
    3. Principais marcos e entregáveis
    4. Recomendações de frequência de ajustes

    Formato: Markdown com tabelas ou listas numeradas
    """
    response = modelo_texto.generate_content(prompt)
    return response.text

# Função para extrair seções de forma segura
def extract_section(response_text: str, section_title: str) -> str:
    """Extrai uma seção específica do texto da resposta"""
    if section_title in response_text:
        parts = response_text.split(section_title)
        if len(parts) > 1:
            next_section = parts[1].find("##")
            if next_section != -1:
                return parts[1][:next_section].strip()
            return parts[1].strip()
    return "Seção não encontrada na resposta."

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
            # Armazenar parâmetros na sessão
            params = {
                'objetivo_campanha': objetivo_campanha,
                'tipo_campanha': tipo_campanha,
                'budget': budget,
                'ferramentas': ferramentas,
                'localizacao_primaria': localizacao_primaria,
                'localizacao_secundaria': localizacao_secundaria,
                'tipo_publico': tipo_publico,
                'tipo_criativo': tipo_criativo,
                'okrs': okrs,
                'observacoes': observacoes
            }
            
            st.session_state.current_step = 1
            st.session_state.params = params
            
    # Processamento em etapas
    if st.session_state.current_step >= 1:
        with st.spinner('Gerando recomendação estratégica...'):
            if 'recomendacao_estrategica' not in st.session_state.plano_completo:
                st.session_state.plano_completo['recomendacao_estrategica'] = gerar_recomendacao_estrategica(st.session_state.params)
            
            st.markdown("## 📌 Recomendação Estratégica")
            st.markdown(st.session_state.plano_completo['recomendacao_estrategica'])
            
            if st.button("Próxima Etapa: Distribuição de Budget"):
                st.session_state.current_step = 2
    
    if st.session_state.current_step >= 2:
        with st.spinner('Calculando distribuição de budget...'):
            if 'distribuicao_budget' not in st.session_state.plano_completo:
                st.session_state.plano_completo['distribuicao_budget'] = gerar_distribuicao_budget(
                    st.session_state.params,
                    st.session_state.plano_completo['recomendacao_estrategica']
                )
            
            st.markdown("## 📊 Distribuição de Budget")
            st.markdown(st.session_state.plano_completo['distribuicao_budget'])
            
            if st.button("Próxima Etapa: Previsão de Resultados"):
                st.session_state.current_step = 3
    
    if st.session_state.current_step >= 3:
        with st.spinner('Estimando resultados...'):
            if 'previsao_resultados' not in st.session_state.plano_completo:
                st.session_state.plano_completo['previsao_resultados'] = gerar_previsao_resultados(
                    st.session_state.params,
                    st.session_state.plano_completo['recomendacao_estrategica'],
                    st.session_state.plano_completo['distribuicao_budget']
                )
            
            st.markdown("## 📈 Previsão de Resultados")
            st.markdown(st.session_state.plano_completo['previsao_resultados'])
            
            if st.button("Próxima Etapa: Recomendações de Público"):
                st.session_state.current_step = 4
    
    if st.session_state.current_step >= 4:
        with st.spinner('Desenvolvendo recomendações de público...'):
            if 'recomendacoes_publico' not in st.session_state.plano_completo:
                st.session_state.plano_completo['recomendacoes_publico'] = gerar_recomendacoes_publico(
                    st.session_state.params,
                    st.session_state.plano_completo['recomendacao_estrategica']
                )
            
            st.markdown("## 🎯 Recomendações de Público")
            st.markdown(st.session_state.plano_completo['recomendacoes_publico'])
            
            if st.button("Próxima Etapa: Cronograma"):
                st.session_state.current_step = 5
    
    if st.session_state.current_step >= 5:
        with st.spinner('Criando cronograma...'):
            if 'cronograma' not in st.session_state.plano_completo:
                st.session_state.plano_completo['cronograma'] = gerar_cronograma(
                    st.session_state.params,
                    st.session_state.plano_completo['recomendacao_estrategica'],
                    st.session_state.plano_completo['distribuicao_budget']
                )
            
            st.markdown("## 📅 Cronograma Sugerido")
            st.markdown(st.session_state.plano_completo['cronograma'])
            
            # Botão para baixar o plano completo
            plano_completo = "\n\n".join([
                "# 📊 Plano de Mídia Completo\n",
                f"**Campanha:** {st.session_state.params['objetivo_campanha']}",
                f"**Budget:** R$ {st.session_state.params['budget']:,.2f}\n",
                "## 📌 Recomendação Estratégica",
                st.session_state.plano_completo['recomendacao_estrategica'],
                "## 📊 Distribuição de Budget",
                st.session_state.plano_completo['distribuicao_budget'],
                "## 📈 Previsão de Resultados",
                st.session_state.plano_completo['previsao_resultados'],
                "## 🎯 Recomendações de Público",
                st.session_state.plano_completo['recomendacoes_publico'],
                "## 📅 Cronograma Sugerido",
                st.session_state.plano_completo['cronograma']
            ])
            
            st.download_button(
                label="📥 Baixar Plano Completo",
                data=plano_completo,
                file_name=f"plano_midia_{st.session_state.params['objetivo_campanha']}_{st.session_state.params['budget']}.md",
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
