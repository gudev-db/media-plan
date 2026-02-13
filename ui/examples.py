import streamlit as st


def render_examples():
    st.header("Exemplos por Etapa do Funil")

    tab_awareness, tab_consideracao, tab_conversao = st.tabs([
        "Consciência (Awareness)", "Consideração", "Conversão/Ação"
    ])

    with tab_awareness:
        st.markdown("""
        ### Exemplo - Consciência (Awareness)
        **Campanha:** Lançamento de Marca no Agronegócio
        **Objetivo:** Construir reconhecimento de marca entre produtores rurais
        **Tipo de Campanha:** Reconhecimento de Marca
        **Etapa do Funil:** Consciência (Awareness)

        **KPIs Primários:**
        - Alcance: 2.500.000 pessoas únicas
        - Impressões: 7.000.000
        - CPM: R$ 12-18

        **KPIs Secundários (monitoramento):**
        - Frequência: manter entre 1.8-2.5
        - Brand Lift: alvo de 8%+
        - Share of Voice: >15% no segmento
        """)

        st.markdown("""
        #### Alocação Recomendada (Budget: R$ 150.000):
        | Plataforma | % Budget | Valor (R$) | Benchmarks | Criativos |
        |------------|----------|-----------|------------|-----------|
        | Meta Ads | 60% | 90.000 | CPM R$15 / Alcance ~6M imp. | Vídeo 60%, Estático 40% |
        | YouTube | 25% | 37.500 | CPV R$0.06 / ~625k views | Vídeo 100% |
        | Programática | 15% | 22.500 | CPM R$10 / ~2.2M imp. | Banner 70%, Vídeo 30% |

        **Total estimado:** ~9.2M impressões, ~3.5M alcance, CPM médio R$16
        """)

    with tab_consideracao:
        st.markdown("""
        ### Exemplo - Consideração
        **Campanha:** Engajamento para Software B2B
        **Objetivo:** Gerar interesse qualificado em decisores
        **Tipo de Campanha:** Engajamento
        **Etapa do Funil:** Consideração

        **KPIs Primários:**
        - CTR: 1.5-2.5%
        - CPC: R$ 2.00-5.00
        - Taxa de Engajamento: 3-5%

        **KPIs Secundários (monitoramento):**
        - ThruPlay: >25% completion rate
        - Bounce Rate: <45%
        - Páginas por Sessão: >2.0
        """)

        st.markdown("""
        #### Alocação Recomendada (Budget: R$ 80.000):
        | Plataforma | % Budget | Valor (R$) | Benchmarks | Criativos |
        |------------|----------|-----------|------------|-----------|
        | Meta Ads | 35% | 28.000 | CPC R$1.20 / ~23k cliques | Carrossel 50%, Vídeo 50% |
        | LinkedIn | 30% | 24.000 | CPC R$12 / ~2k cliques qualificados | Estático 60%, Vídeo 40% |
        | Google Ads | 25% | 20.000 | CPC R$3.50 / ~5.7k cliques | Search 70%, Display 30% |
        | YouTube | 10% | 8.000 | CPV R$0.06 / ~133k views | Vídeo 100% |

        **Total estimado:** ~30.7k cliques, CTR médio 1.8%, CPC médio R$2.60
        """)

    with tab_conversao:
        st.markdown("""
        ### Exemplo - Conversão/Ação
        **Campanha:** Vendas de E-commerce - Black Friday
        **Objetivo:** Maximizar vendas com ROAS positivo
        **Tipo de Campanha:** Vendas/Conversões
        **Etapa do Funil:** Conversão/Ação

        **KPIs Primários:**
        - Conversões: 2.000+ vendas
        - CPA: R$ 45-70
        - ROAS: 4.0x+

        **KPIs Secundários (monitoramento):**
        - Ticket Médio: R$ 180+
        - Taxa de Conversão: >3%
        - Receita Total: R$ 360.000+
        """)

        st.markdown("""
        #### Alocação Recomendada (Budget: R$ 120.000):
        | Plataforma | % Budget | Valor (R$) | Benchmarks | Criativos |
        |------------|----------|-----------|------------|-----------|
        | Meta Ads | 45% | 54.000 | CPA R$55 / ~980 conv. / ROAS 3.5x | Coleção 60%, Carrossel 40% |
        | Google Ads | 40% | 48.000 | CPA R$80 / ~600 conv. / ROAS 4.0x | Shopping 80%, Search 20% |
        | Remarketing | 15% | 18.000 | CPA R$35 / ~515 conv. / ROAS 6.0x | Estático 50%, Carrossel 50% |

        **Total estimado:** ~2.095 conversões, CPA médio R$57, ROAS médio 4.2x, Receita ~R$377k
        """)
