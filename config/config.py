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
def init_gemini():
    gemini_api_key = os.getenv("GEM_API_KEY")
    genai.configure(api_key=gemini_api_key)
    return genai.GenerativeModel("gemini-2.0-flash")
def init_session_state():
    if 'plano_completo' not in st.session_state:
        st.session_state.plano_completo = {}
    if 'current_step' not in st.session_state:
        st.session_state.current_step = 0
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "📋 Criar Plano"
