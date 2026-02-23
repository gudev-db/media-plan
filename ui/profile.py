import streamlit as st
from bson import ObjectId
from db.connection import get_database
from db.user_repository import update_profile, get_user_by_id


def render_profile():
    st.header("⚙️ Meu Perfil")

    user_data = st.session_state.get("user_data", {})

    col1, col2 = st.columns([1, 2], gap="small")

    with col1:
        st.markdown("### 👤")

        criado_em = user_data.get("criado_em")
        if criado_em:
            st.markdown(f"**Membro desde:** {criado_em.strftime('%d/%m/%Y')}")

    with col2:
        with st.form("profile_form"):
            nome = st.text_input("Nome", value=user_data.get("nome", ""))
            email = st.text_input(
                "Email", value=user_data.get("email", ""), disabled=True
            )
            empresa = st.text_input(
                "Empresa", value=user_data.get("empresa", "") or ""
            )
            cargo = st.text_input(
                "Cargo", value=user_data.get("cargo", "") or ""
            )
            submitted = st.form_submit_button(
                "Salvar Alterações", use_container_width=True
            )

        if submitted:
            db = get_database()
            user_id = ObjectId(st.session_state.user_id)
            success = update_profile(
                db,
                user_id,
                {"nome": nome.strip(), "empresa": empresa.strip(), "cargo": cargo.strip()},
            )
            if success:
                updated_user = get_user_by_id(db, user_id)
                st.session_state.user_data = updated_user
                st.session_state.user_nome = updated_user["nome"]
                st.success("Perfil atualizado com sucesso!")
            else:
                st.info("Nenhuma alteração detectada.")
