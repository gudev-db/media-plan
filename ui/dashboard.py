import streamlit as st
from bson import ObjectId
from db.connection import get_database
from db.plan_repository import get_user_plans, delete_plan, count_user_plans
from utils.pdf_generator import generate_pdf
from utils.docx_generator import generate_docx


def render_dashboard():
    st.header("📂 Meus Planos de Mídia")

    db = get_database()
    user_id = ObjectId(st.session_state.user_id)
    total = count_user_plans(db, user_id)

    if total == 0:
        st.info("Você ainda não tem planos salvos. Crie um novo plano para começar!")
        return

    st.markdown(f"**Total de planos:** {total}")
    plans = get_user_plans(db, user_id)

    for plan in plans:
        plan_id = str(plan["_id"])
        params = plan.get("params", {})
        resultado = plan.get("resultado", {})
        criado = plan.get("criado_em")
        data_str = criado.strftime("%d/%m/%Y %H:%M") if criado else "N/A"

        with st.expander(f"📋 {plan['nome_plano']} — {data_str}", expanded=False):
            col_info1, col_info2 = st.columns(2, gap="small")
            with col_info1:
                st.markdown(f"**Campanha:** {params.get('objetivo_campanha', 'N/A')}")
                st.markdown(f"**Budget:** R$ {params.get('budget', 0):,.2f}")
            with col_info2:
                st.markdown(f"**Etapa:** {params.get('etapa_funil', 'N/A')}")
                st.markdown(f"**Período:** {params.get('periodo', 'N/A')}")

            if params.get("ferramentas"):
                st.markdown(f"**Plataformas:** {', '.join(params['ferramentas'])}")

            st.markdown("---")

            if resultado.get("recomendacao_estrategica"):
                with st.container():
                    st.markdown("#### 📌 Recomendação Estratégica")
                    st.markdown(resultado["recomendacao_estrategica"])
                    st.markdown("#### 📊 Distribuição de Budget")
                    st.markdown(resultado.get("distribuicao_budget", ""))
                    st.markdown("#### 📈 Previsão de Resultados")
                    st.markdown(resultado.get("previsao_resultados", ""))
                    st.markdown("#### 🎯 Recomendações de Público")
                    st.markdown(resultado.get("recomendacoes_publico", ""))
                    st.markdown("#### 📅 Cronograma Sugerido")
                    st.markdown(resultado.get("cronograma", ""))

            st.markdown("---")

            col_pdf, col_docx, col_del = st.columns([2, 2, 1], gap="small")


            with col_pdf:
                try:
                    pdf_data = generate_pdf(params, resultado)
                    st.download_button(
                        "📥 Baixar PDF",
                        data=pdf_data,
                        file_name=f"plano_{plan['nome_plano'][:20]}.pdf",
                        mime="application/pdf",
                        key=f"pdf_{plan_id}",
                        use_container_width=True,
                    )
                except Exception as e:
                    st.warning(f"Erro ao gerar PDF: {e}")

            with col_docx:
                try:
                    docx_data = generate_docx(params, resultado)
                    st.download_button(
                        "📥 Baixar DOCX",
                        data=docx_data,
                        file_name=f"plano_{plan['nome_plano'][:20]}.docx",
                        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                        key=f"docx_{plan_id}",
                        use_container_width=True,
                    )
                except Exception as e:
                    st.warning(f"Erro ao gerar DOCX: {e}")

            with col_del:
                if st.button(
                    "🗑️ Excluir",
                    key=f"del_{plan_id}",
                    type="secondary",
                    use_container_width=True,
                ):
                    delete_plan(db, plan["_id"], user_id)
                    st.success("Plano excluído.")
                    st.rerun()
