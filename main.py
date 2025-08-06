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

# Dicionários de métricas por etapa do funil
METRICAS_POR_ETAPA = {
    'Topo': ['Impressões', 'Alcance', 'Frequência', 'CPM', 'Brand Lift', 'Engajamento', 'Video Views'],
    'Meio': ['Engajamento', 'CTR', 'Cliques', 'Tempo no Site', 'Pages per Visit', 'Video Completions', 'Lead Generation'],
    'Fundo': ['Conversões', 'ROAS', 'CPA', 'Valor da Conversão', 'Leads Qualificados', 'Vendas', 'Custo por Lead']
}

def detectar_etapa_funil(nome_campanha: str) -> str:
    """Detecta automaticamente a etapa do funil com base no nome da campanha"""
    nome = nome_campanha.lower()
    
    # Palavras-chave para cada etapa
    topo_keywords = ['awareness', 'consciencia', 'alcance', 'branding', 'marca', 'topo', 'reconhecimento']
    meio_keywords = ['consideracao', 'consideração', 'engajamento', 'video', 'vídeo', 'traffic', 'tráfego', 'meio']
    fundo_keywords = ['conversao', 'conversão', 'venda', 'sales', 'lead', 'performance', 'fundo', 'compra']
    
    if any(keyword in nome for keyword in topo_keywords):
        return 'Topo'
    elif any(keyword in nome for keyword in meio_keywords):
        return 'Meio'
    elif any(keyword in nome for keyword in fundo_keywords):
        return 'Fundo'
    else:
        return 'Topo'  # Default para topo de funil se não identificar

# Funções de geração de conteúdo com IA
def gerar_recomendacao_estrategica(params: Dict[str, Any]) -> str:
    """Gera a recomendação estratégica inicial"""
    etapa_funil = detectar_etapa_funil(params['objetivo_campanha'])
    okrs_relevantes = METRICAS_POR_ETAPA[etapa_funil]
    
    prompt = f"""
    Como especialista em planejamento de mídia digital, analise os seguintes parâmetros e forneça uma recomendação estratégica:

    **Campanha:** {params['objetivo_campanha']} (Etapa do Funil: {etapa_funil})
    **Tipo de Campanha:** {params['tipo_campanha']}
    **Budget Total:** R$ {params['budget']:,.2f}
    **Período da Campanha:** {params['periodo']}
    **Ferramentas/Plataformas:** {", ".join(params['ferramentas'])}
    **Localização Primária:** {params['localizacao_primaria']}
    **Localização Secundária:** {params['localizacao_secundaria']}
    **Tipo de Público:** {params['tipo_publico']}
    **Tipos de Criativo:** {", ".join(params['tipo_criativo'])}
    **OKRs Relevantes para {etapa_funil} do Funil:** {", ".join(okrs_relevantes)}
    **Detalhes da Ação:** {params['detalhes_acao'] or "Nenhum"}
    **Observações:** {params['observacoes'] or "Nenhuma"}

    Forneça:
    1. Análise estratégica focada em {etapa_funil} do funil (150-200 palavras)
    2. Principais oportunidades para a etapa {etapa_funil}
    3. Riscos potenciais específicos para esta etapa
    4. Recomendação geral de abordagem com foco nos OKRs: {", ".join(okrs_relevantes)}

    Dicas:
    - Mantenha o foco absoluto nos OKRs relevantes para {etapa_funil} do funil
    - Considere apenas os tipos de criativo solicitados
    - Adapte ao período especificado

    Formato: Markdown com headers (##, ###)
    """
    response = modelo_texto.generate_content(prompt)
    return response.text

def gerar_distribuicao_budget(params: Dict[str, Any], recomendacao_estrategica: str) -> str:
    """Gera a distribuição de budget baseada na recomendação estratégica"""
    etapa_funil = detectar_etapa_funil(params['objetivo_campanha'])
    
    prompt = f"""
    Com base na seguinte recomendação estratégica (Etapa {etapa_funil} do Funil):
    {recomendacao_estrategica}

    E nos parâmetros originais:
    - Budget: R$ {params['budget']:,.2f}
    - Período: {params['periodo']}
    - Plataformas: {", ".join(params['ferramentas'])}
    - Localizações: Primária ({params['localizacao_primaria']}), Secundária ({params['localizacao_secundaria']})
    - Tipos de Criativo: {", ".join(params['tipo_criativo'])}

    Crie uma tabela detalhada de distribuição de budget OTIMIZADA PARA {etapa_funil} DO FUNIL com:
    1. Divisão por plataforma (% e valor)
    2. Alocação geográfica (primária vs secundária)
    3. Tipos de criativos recomendados (APENAS: {", ".join(params['tipo_criativo'])})
    4. Justificativa estratégica para cada alocação considerando a etapa {etapa_funil}

    REGRAS:
    - Distribuição deve maximizar os OKRs da etapa {etapa_funil}
    - Não sugerir criativos fora dos tipos especificados
    - Manter foco absoluto nos estados solicitados
    - Adaptar ao período da campanha

    Inclua também uma breve análise (50-100 palavras) explicando como a distribuição atende à etapa {etapa_funil}.

    Formato: Markdown com tabelas (use | para divisão)
    """
    response = modelo_texto.generate_content(prompt)
    return response.text

def gerar_previsao_resultados(params: Dict[str, Any], recomendacao_estrategica: str, distribuicao_budget: str) -> str:
    """Gera previsão de resultados baseada nos parâmetros"""
    etapa_funil = detectar_etapa_funil(params['objetivo_campanha'])
    okrs_relevantes = METRICAS_POR_ETAPA[etapa_funil]
    
    prompt = f"""
    Com base na estratégia para {etapa_funil} do funil:
    {recomendacao_estrategica}

    E na distribuição de budget:
    {distribuicao_budget}

    Estime os resultados ESPERADOS PARA ETAPA {etapa_funil} considerando:
    - Budget total: R$ {params['budget']:,.2f}
    - Período: {params['periodo']}
    - OKRs Relevantes: {", ".join(okrs_relevantes)}

    Forneça:
    1. Tabela com métricas ESPECÍFICAS PARA {etapa_funil} (focar em: {", ".join(okrs_relevantes)})
    2. Estimativas realistas baseadas em benchmarks de {etapa_funil}
    3. Análise de potencial desempenho (50-100 palavras)
    4. KPIs CHAVE para monitorar em {etapa_funil}

    DICAS:
    - Ignorar métricas não relevantes para {etapa_funil}
    - Manter foco nos OKRs: {", ".join(okrs_relevantes)}
    - Usar benchmarks realistas para a etapa

    Formato: Markdown com tabelas
    """
    response = modelo_texto.generate_content(prompt)
    return response.text

def gerar_recomendacoes_publico(params: Dict[str, Any], recomendacao_estrategica: str) -> str:
    """Gera recomendações detalhadas de público-alvo"""
    etapa_funil = detectar_etapa_funil(params['objetivo_campanha'])
    
    prompt = f"""
    Para a campanha na etapa {etapa_funil} do funil com:
    - Tipo de Público: {params['tipo_publico']}
    - Objetivo: {params['objetivo_campanha']}
    - Plataformas: {", ".join(params['ferramentas'])}
    - Localizações: {params['localizacao_primaria']} (primária), {params['localizacao_secundaria']} (secundária)

    E considerando a estratégia para {etapa_funil}:
    {recomendacao_estrategica}

    Desenvolva recomendações de público OTIMIZADAS PARA {etapa_funil} DO FUNIL incluindo:
    1. Segmentação específica para objetivos de {etapa_funil}
    2. Parâmetros de targeting focados em {etapa_funil}
    3. Estratégias de expansão adequadas para {etapa_funil}
    4. Considerações sobre frequência e saturação

    REGRAS:
    - Manter foco absoluto nos estados especificados
    - Adaptar recomendações à etapa {etapa_funil}
    - Priorizar estratégias adequadas para {etapa_funil}

    Formato: Markdown com listas e headers
    """
    response = modelo_texto.generate_content(prompt)
    return response.text

def gerar_cronograma(params: Dict[str, Any], recomendacao_estrategica: str, distribuicao_budget: str) -> str:
    """Gera cronograma de implementação"""
    etapa_funil = detectar_etapa_funil(params['objetivo_campanha'])
    
    prompt = f"""
    Com base na estratégia para {etapa_funil} do funil:
    {recomendacao_estrategica}

    E na distribuição de budget:
    {distribuicao_budget}

    Crie um cronograma OTIMIZADO PARA ETAPA {etapa_funil} considerando:
    - Budget total: R$ {params['budget']:,.2f}
    - Período: {params['periodo']}
    - Plataformas: {", ".join(params['ferramentas'])}

    Inclua:
    1. Fases de implementação adequadas para {etapa_funil}
    2. Distribuição temporal do budget
    3. Marcos importantes para {etapa_funil}
    4. Frequência de ajustes recomendada

    DICAS:
    - Adaptar cronograma aos objetivos de {etapa_funil}
    - Não incluir fases irrelevantes para {etapa_funil}
    - Manter realismo no período especificado

    Formato: Markdown com tabelas ou listas numeradas
    """
    response = modelo_texto.generate_content(prompt)
    return response.text

# Abas principais
tab1, tab2 = st.tabs(["📋 Criar Novo Plano", "📊 Exemplos por Etapa"])

with tab1:
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
            st.error("Por favor, preencha todos os campos obrigatórios (*)")
        else:
            # Detectar etapa do funil automaticamente
            etapa_funil = detectar_etapa_funil(objetivo_campanha)
            okrs_relevantes = METRICAS_POR_ETAPA[etapa_funil]
            
            # Armazenar parâmetros na sessão
            params = {
                'objetivo_campanha': objetivo_campanha,
                'tipo_campanha': tipo_campanha,
                'budget': budget,
                'periodo': periodo,
                'ferramentas': ferramentas,
                'localizacao_primaria': localizacao_primaria,
                'localizacao_secundaria': localizacao_secundaria,
                'tipo_publico': tipo_publico,
                'tipo_criativo': tipo_criativo,
                'detalhes_acao': detalhes_acao,
                'observacoes': observacoes,
                'etapa_funil': etapa_funil,
                'okrs_relevantes': okrs_relevantes
            }
            
            st.session_state.current_step = 1
            st.session_state.params = params
            
            # Gerar todo o conteúdo de uma vez
            with st.spinner(f'Gerando plano completo para {etapa_funil} do funil...'):
                st.session_state.plano_completo['recomendacao_estrategica'] = gerar_recomendacao_estrategica(params)
                st.session_state.plano_completo['distribuicao_budget'] = gerar_distribuicao_budget(params, st.session_state.plano_completo['recomendacao_estrategica'])
                st.session_state.plano_completo['previsao_resultados'] = gerar_previsao_resultados(params, st.session_state.plano_completo['recomendacao_estrategica'], st.session_state.plano_completo['distribuicao_budget'])
                st.session_state.plano_completo['recomendacoes_publico'] = gerar_recomendacoes_publico(params, st.session_state.plano_completo['recomendacao_estrategica'])
                st.session_state.plano_completo['cronograma'] = gerar_cronograma(params, st.session_state.plano_completo['recomendacao_estrategica'], st.session_state.plano_completo['distribuicao_budget'])
    
    # Exibir resultados
    if st.session_state.current_step >= 1:
        etapa_funil = st.session_state.params.get('etapa_funil', 'Topo')
        st.success(f"**Etapa do Funil Detectada:** {etapa_funil}")
        
        st.markdown("## 📌 Recomendação Estratégica")
        st.markdown(st.session_state.plano_completo.get('recomendacao_estrategica', 'Em processamento...'))
        
        st.markdown("## 📊 Distribuição de Budget")
        st.markdown(st.session_state.plano_completo.get('distribuicao_budget', 'Em processamento...'))
        
        st.markdown("## 📈 Previsão de Resultados")
        st.markdown(st.session_state.plano_completo.get('previsao_resultados', 'Em processamento...'))
        
        st.markdown("## 🎯 Recomendações de Público")
        st.markdown(st.session_state.plano_completo.get('recomendacoes_publico', 'Em processamento...'))
        
        st.markdown("## 📅 Cronograma Sugerido")
        st.markdown(st.session_state.plano_completo.get('cronograma', 'Em processamento...'))
        
        # Botão para baixar o plano completo
        if all(key in st.session_state.plano_completo for key in ['recomendacao_estrategica', 'distribuicao_budget', 'previsao_resultados', 'recomendacoes_publico', 'cronograma']):
            plano_completo = "\n\n".join([
                f"# 📊 Plano de Mídia Completo ({etapa_funil} do Funil)\n",
                f"**Campanha:** {st.session_state.params['objetivo_campanha']}",
                f"**Budget:** R$ {st.session_state.params['budget']:,.2f}",
                f"**Período:** {st.session_state.params['periodo']}\n",
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
                file_name=f"plano_midia_{etapa_funil}_{st.session_state.params['objetivo_campanha'][:30]}.md",
                mime="text/markdown"
            )

with tab2:
    st.header("Exemplos por Etapa do Funil")
    
    tab_topo, tab_meio, tab_fundo = st.tabs(["Topo", "Meio", "Fundo"])
    
    with tab_topo:
        st.markdown("""
        ### 📋 Exemplo - Topo do Funil (Awareness)
        **Campanha:** Conscientização da Marca X  
        **Objetivo:** Aumentar reconhecimento de marca  
        **Budget:** R$ 150.000,00  
        **Período:** 2 meses  
        **OKRs Relevantes:** Impressões, Alcance, Frequência, CPM, Brand Lift  
        """)
        
        st.markdown("""
        #### 📊 Alocação Recomendada:
        | Plataforma | % Budget | Valor (R$) | Criativos Principais |
        |------------|----------|------------|----------------------|
        | Meta Ads | 50% | 75.000 | Vídeo (60%), Estático (40%) |
        | YouTube | 30% | 45.000 | Vídeo (100%) |
        | Programática | 20% | 30.000 | Banner (70%), Vídeo (30%) |
        
        #### 📈 Métricas Esperadas:
        - Impressões: ~5.000.000
        - Alcance: ~2.200.000
        - Frequência média: 2.3
        - CPM: R$ 15-20
        """)
    
    with tab_meio:
        st.markdown("""
        ### 📋 Exemplo - Meio do Funil (Consideração)
        **Campanha:** Engajamento Produto Y  
        **Objetivo:** Gerar interesse no produto  
        **Budget:** R$ 80.000,00  
        **Período:** 1 mês  
        **OKRs Relevantes:** Engajamento, CTR, Video Views, Lead Generation  
        """)
        
        st.markdown("""
        #### 📊 Alocação Recomendada:
        | Plataforma | % Budget | Valor (R$) | Criativos Principais |
        |------------|----------|------------|----------------------|
        | Meta Ads | 40% | 32.000 | Carrossel (50%), Vídeo (50%) |
        | LinkedIn | 30% | 24.000 | Estático (70%), Vídeo (30%) |
        | Google Ads | 30% | 24.000 | Display (60%), Vídeo (40%) |
        
        #### 📈 Métricas Esperadas:
        - CTR: 1.8-2.5%
        - Video Views: ~500.000
        - Leads: ~2.000
        """)
    
    with tab_fundo:
        st.markdown("""
        ### 📋 Exemplo - Fundo do Funil (Conversão)
        **Campanha:** Vendas Produto Z  
        **Objetivo:** Gerar vendas diretas  
        **Budget:** R$ 120.000,00  
        **Período:** 3 semanas  
        **OKRs Relevantes:** Conversões, ROAS, CPA, Vendas  
        """)
        
        st.markdown("""
        #### 📊 Alocação Recomendada:
        | Plataforma | % Budget | Valor (R$) | Criativos Principais |
        |------------|----------|------------|----------------------|
        | Meta Ads | 60% | 72.000 | Coleção (70%), Estático (30%) |
        | Google Ads | 40% | 48.000 | Shopping (100%) |
        
        #### 📈 Métricas Esperadas:
        - Conversões: ~1.500
        - ROAS: 3.5x
        - CPA: R$ 80-100
        """)

# Rodapé
st.markdown("---")
st.caption("""
Ferramenta de IA para Planejamento de Mídia - Otimize suas campanhas com alocação inteligente de budget por etapa do funil.
""")
