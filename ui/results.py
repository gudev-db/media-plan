import streamlit as st

from utils.pdf_generator import generate_pdf
from utils.docx_generator import generate_docx


def render_results():
    if st.session_state.current_step >= 1 and 'params' in st.session_state:
        etapa_funil = st.session_state.params.get('etapa_funil', 'Topo')
        st.success(f"**Etapa do Funil Selecionada:** {etapa_funil}")

        okrs_selecionados = []
        metas_definidas = []

        if 'metricas' in st.session_state.params:
            okrs_selecionados = [k for k, v in st.session_state.params['metricas'].items() if v['selecionada']]
            metas_definidas = [f"{k}: {v['valor']}" for k, v in st.session_state.params['metricas'].items() if v['selecionada'] and v['valor']]

            if okrs_selecionados:
                st.info(f"**OKRs Selecionados:** {', '.join(okrs_selecionados)}")
            if metas_definidas:
                st.info(f"**Metas Definidas:** {', '.join(metas_definidas)}")
        else:
            st.warning("Nenhuma métrica foi configurada ainda.")

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

        if all(key in st.session_state.plano_completo for key in ['recomendacao_estrategica', 'distribuicao_budget', 'previsao_resultados', 'recomendacoes_publico', 'cronograma']):
            plano_completo_md = "\n\n".join([
                f"# 📊 Plano de Mídia Completo ({etapa_funil} do Funil)\n",
                f"**Campanha:** {st.session_state.params['objetivo_campanha']}",
                f"**Budget:** R$ {st.session_state.params['budget']:,.2f}",
                f"**Período:** {st.session_state.params['periodo']}",
                f"**OKRs Selecionados:** {', '.join(okrs_selecionados) if okrs_selecionados else 'A serem otimizados'}",
                f"**Metas Definidas:** {', '.join(metas_definidas) if metas_definidas else 'Nenhuma específica'}\n",
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

            nome_arquivo = f"plano_midia_{etapa_funil}_{st.session_state.params['objetivo_campanha'][:30]}"

            st.markdown("### 📥 Baixar Plano")
            col_md, col_pdf, col_docx = st.columns(3)

            with col_md:
                st.download_button(
                    label="📄 Markdown",
                    data=plano_completo_md,
                    file_name=f"{nome_arquivo}.md",
                    mime="text/markdown",
                    use_container_width=True,
                )

            with col_pdf:
                pdf_data = generate_pdf(
                    st.session_state.params,
                    st.session_state.plano_completo,
                )
                st.download_button(
                    label="📕 PDF",
                    data=pdf_data,
                    file_name=f"{nome_arquivo}.pdf",
                    mime="application/pdf",
                    use_container_width=True,
                )

            with col_docx:
                docx_data = generate_docx(
                    st.session_state.params,
                    st.session_state.plano_completo,
                )
                st.download_button(
                    label="📘 Word (DOCX)",
                    data=docx_data,
                    file_name=f"{nome_arquivo}.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    use_container_width=True,
                )
