import os
import secrets
from pathlib import Path
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

# Carrega .env do diretório config
_env_path = Path(__file__).parent / ".env"
load_dotenv(_env_path)


def _sync_secrets_toml():
    secrets_path = Path(__file__).resolve().parent.parent / ".streamlit" / "secrets.toml"
    secrets_path.parent.mkdir(exist_ok=True)

    client_id = os.getenv("GOOGLE_OAUTH_CLIENT_ID", "")
    client_secret = os.getenv("GOOGLE_OAUTH_CLIENT_SECRET", "")
    cookie = secrets.token_urlsafe(32)

    if secrets_path.exists():
        content = secrets_path.read_text(encoding="utf-8")
        for line in content.splitlines():
            if line.startswith("cookie_secret") and "CHANGE_ME" not in line:
                cookie = line.split("=", 1)[1].strip().strip('"')
                break

    secrets_path.write_text(
        f'[auth]\n'
        f'redirect_uri = "http://localhost:8501/oauth2callback"\n'
        f'cookie_secret = "{cookie}"\n'
        f'\n'
        f'[auth.google]\n'
        f'client_id = "{client_id}"\n'
        f'client_secret = "{client_secret}"\n'
        f'server_metadata_url = "https://accounts.google.com/.well-known/openid-configuration"\n',
        encoding="utf-8",
    )

_sync_secrets_toml()

def init_page():
    st.set_page_config(
        layout="wide",
        page_title="Sistema de Planejamento de Mídia",
        page_icon="📊"
    )
def init_gemini_models():
    gemini_api_key = os.getenv("GEM_API_KEY")
    genai.configure(api_key=gemini_api_key)

    especialistas = {
        "estrategista": (
            "Você é um Diretor de Planejamento de Mídia Digital com 15+ anos de experiência "
            "no mercado brasileiro. Sua especialidade é análise estratégica de campanhas: "
            "identificar oportunidades, avaliar riscos, definir abordagens macro e alinhar "
            "objetivos de mídia com objetivos de negócio. Você pensa em termos de funil, "
            "posicionamento de marca e vantagem competitiva. Sempre responda em português brasileiro."
        ),
        "financeiro": (
            "Você é um Controller de Mídia / Media Buyer sênior especializado em alocação "
            "de budget e otimização de investimento em mídia digital no Brasil. Sua expertise "
            "é distribuir verbas entre plataformas, formatos e regiões para maximizar ROI. "
            "Você trabalha com tabelas detalhadas, justificativas financeiras e benchmarks "
            "de mercado. Sempre responda em português brasileiro."
        ),
        "performance": (
            "Você é um Analista de Performance / Growth Analyst com profundo conhecimento "
            "em métricas de mídia digital e benchmarks do mercado brasileiro. Sua especialidade "
            "é projetar resultados com base em dados, criar cenários (pessimista/realista/otimista) "
            "e calcular estimativas usando CPM, CPC, CTR, CPA, ROAS e outras métricas. "
            "Você é rigoroso com números e fórmulas. Sempre responda em português brasileiro."
        ),
        "audiencia": (
            "Você é um Especialista em Audiência e Segmentação com experiência em targeting "
            "avançado em Meta Ads, Google Ads, TikTok, LinkedIn e programática no Brasil. "
            "Sua expertise é definir segmentos de público, estratégias de lookalike, "
            "retargeting, behavioral targeting e otimização de frequência. Você conhece "
            "profundamente o comportamento do consumidor brasileiro. Sempre responda em português brasileiro."
        ),
        "gestor": (
            "Você é um Gestor de Projetos de Campanhas Digitais / Traffic Manager com "
            "experiência em cronogramas, fases de implementação, pacing de budget e "
            "checkpoints de performance. Sua especialidade é criar timelines realistas "
            "com marcos claros, gatilhos de otimização e distribuição temporal de investimento. "
            "Sempre responda em português brasileiro."
        ),
    }

    return {
        chave: genai.GenerativeModel(
            "gemini-2.0-flash",
            system_instruction=instrucao,
        )
        for chave, instrucao in especialistas.items()
    }
def init_session_state():
    if 'plano_completo' not in st.session_state:
        st.session_state.plano_completo = {}
    if 'current_step' not in st.session_state:
        st.session_state.current_step = 0
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "📋 Criar Plano"
