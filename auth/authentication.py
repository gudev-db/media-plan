import re

import streamlit as st

from db.connection import get_database
from db.user_repository import (
    create_user_email,
    verify_password,
    find_or_create_google_user,
)
from auth.session import login_user


def render_auth_page():
    st.markdown(
        "<div style='max-width:480px;margin:0 auto;'>",
        unsafe_allow_html=True,
    )
    st.markdown("## 📊 Planejamento de Mídia com IA")
    st.markdown("Faça login ou crie sua conta para continuar.")
    st.markdown("---")

    if st.session_state.get("auth_page") == "register":
        _render_register_form()
    else:
        _render_login_page()

    st.markdown("</div>", unsafe_allow_html=True)


def _render_login_page():
    st.subheader("Entrar")

    try:
        if st.button("Entrar com Google", type="primary", use_container_width=True):
            st.login("google")
    except Exception:
        st.caption("Google OAuth não configurado. Use email/senha.")

    st.markdown("---")
    st.markdown("**Ou entre com email e senha:**")

    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input("Senha", type="password")
        submitted = st.form_submit_button("Entrar", use_container_width=True)

    if submitted:
        if not email or not password:
            st.error("Preencha todos os campos.")
            return
        try:
            db = get_database()
            user = verify_password(db, email, password)
            if user:
                login_user(user)
                st.rerun()
            else:
                st.error("Email ou senha incorretos.")
        except Exception as e:
            st.error(f"Erro ao conectar ao banco de dados: {e}")

    st.markdown("---")
    if st.button("Não tem conta? Cadastre-se", use_container_width=True):
        st.session_state.auth_page = "register"
        st.rerun()


def _render_register_form():
    """Formulário de cadastro com email/senha."""
    st.subheader("Criar Conta")

    with st.form("register_form"):
        nome = st.text_input("Nome Completo*")
        email = st.text_input("Email*")
        password = st.text_input("Senha* (mínimo 6 caracteres)", type="password")
        password_confirm = st.text_input("Confirmar Senha*", type="password")
        submitted = st.form_submit_button("Criar Conta", use_container_width=True)

    if submitted:
        errors = _validate_registration(nome, email, password, password_confirm)
        if errors:
            for e in errors:
                st.error(e)
        else:
            try:
                db = get_database()
                user = create_user_email(db, email, password, nome)
                login_user(user)
                st.success("Conta criada com sucesso!")
                st.rerun()
            except Exception as e:
                if "duplicate key" in str(e).lower():
                    st.error("Este email já está cadastrado. Faça login.")
                else:
                    st.error(f"Erro ao criar conta: {e}")

    st.markdown("---")
    if st.button("Já tem conta? Faça login", use_container_width=True):
        st.session_state.auth_page = "login"
        st.rerun()


def handle_google_callback():
    if not hasattr(st, "user"):
        return False

    try:
        if st.user.is_logged_in:
            if st.session_state.get("authenticated"):
                return True
            db = get_database()
            user = find_or_create_google_user(
                db,
                google_sub=st.user.get("sub", st.user.get("email", "")),
                email=st.user.get("email", ""),
                nome=st.user.get("name", ""),
                avatar_url=st.user.get("picture", None),
            )
            login_user(user)
            return True
    except Exception:
        pass
    return False


def _validate_registration(nome, email, password, password_confirm):
    errors = []
    if not nome or len(nome.strip()) < 2:
        errors.append("Nome deve ter pelo menos 2 caracteres.")
    if not email or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        errors.append("Email inválido.")
    if not password or len(password) < 6:
        errors.append("Senha deve ter pelo menos 6 caracteres.")
    if password != password_confirm:
        errors.append("As senhas não coincidem.")
    return errors
