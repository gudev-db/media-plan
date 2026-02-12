import streamlit as st

from config.config import init_page, init_gemini, init_session_state
from auth.session import init_auth_state, is_authenticated
from auth.authentication import render_auth_page, handle_google_callback
from utils.styles import apply_custom_css
from ui.sidebar import render_sidebar
from ui.form import render_form
from ui.results import render_results
from ui.examples import render_examples
from ui.dashboard import render_dashboard
from ui.profile import render_profile
from ui.footer import render_footer

init_page()
apply_custom_css()
init_session_state()
init_auth_state()


 # handle_google_callback()

if not is_authenticated():
    render_auth_page()
    st.stop()
modelo = init_gemini()
current_page = render_sidebar()

# Router de páginas
if current_page == "📋 Criar Plano":
    st.title("📊 IA para Planejamento de Mídia")
    st.markdown(
        "**Crie planos de mídia otimizados com alocação automática de verba "
        "por estratégia, plataforma e localização.**"
    )
    render_form(modelo)
    render_results()

elif current_page == "📂 Meus Planos":
    render_dashboard()

elif current_page == "📊 Exemplos":
    render_examples()

elif current_page == "⚙️ Meu Perfil":
    render_profile()

render_footer()
