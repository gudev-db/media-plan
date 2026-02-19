from typing import Optional, Dict, Any

import streamlit as st
from bson import ObjectId


def init_auth_state():
    """Inicializa todas as keys de autenticação no session state."""
    defaults = {
        "authenticated": False,
        "user_id": None,
        "user_nome": None,
        "user_email": None,
        "user_data": None,
        "auth_page": "login",
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def login_user(user: Dict[str, Any]):
    st.session_state.authenticated = True
    st.session_state.user_id = str(user["_id"])
    st.session_state.user_nome = user.get("nome", "Usuário")
    st.session_state.user_email = user.get("email", "")
    st.session_state.user_data = user


def logout_user():
    """Limpa session state de autenticação."""
    keys = ["authenticated", "user_id", "user_nome", "user_email", "user_data"]
    for key in keys:
        if key in st.session_state:
            del st.session_state[key]
    st.session_state.authenticated = False


def is_authenticated() -> bool:
    """Verifica se há usuário autenticado na sessão."""
    return st.session_state.get("authenticated", False)


def get_current_user_id() -> Optional[ObjectId]:
    uid = st.session_state.get("user_id")
    return ObjectId(uid) if uid else None
