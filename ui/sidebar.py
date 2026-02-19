import streamlit as st

from auth.session import logout_user, is_authenticated


def render_sidebar():
    with st.sidebar:
        if not is_authenticated():
            return None

        st.markdown(f"### 👤 {st.session_state.user_nome}")
        st.caption(st.session_state.user_email)
        st.markdown("---")

        page = st.radio(
            "Navegação",
            ["📋 Criar Plano", "📂 Meus Planos", "📊 Exemplos", "⚙️ Meu Perfil"],
            key="nav_radio",
            label_visibility="collapsed",
        )

        st.markdown("---")
        if st.button("Sair", use_container_width=True):
            logout_user()
            try:
                if hasattr(st, "user") and st.user.is_logged_in:
                    st.logout()
            except Exception:
                pass
            st.rerun()

        return page
