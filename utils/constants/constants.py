TIPOS_CAMPANHA = [
    "Reconhecimento de Marca",
    "Alcance",
    "Tráfego",
    "Engajamento",
    "Visualizações de Vídeo",
    "Geração de Leads",
    "Promoção de App",
    "Vendas/Conversões",
    "Vendas de Catálogo",
    "Remarketing/Retargeting",
    "Branding Institucional",
]
ETAPAS_FUNIL = [
    "Consciência (Awareness)",
    "Interesse",
    "Consideração",
    "Intenção",
    "Conversão/Ação",
    "Retenção/Fidelização",
]
LEGACY_FUNNEL_MAP = {
    "Topo": "Consciência (Awareness)",
    "Meio": "Consideração",
    "Fundo": "Conversão/Ação",
}
KPIS_POR_ETAPA = {
    "Consciência (Awareness)": {
        "primarios": [
            {
                "nome": "Alcance",
                "formula": "Usuários únicos impactados",
                "faixa_tipica": "Varia por budget; ref: 1M alcance para ~R$15k-25k",
                "quando_usar": "Sempre em campanhas de awareness",
                "descricao": "Número de pessoas únicas que viram seu anúncio",
            },
            {
                "nome": "Impressões",
                "formula": "Total de exibições do anúncio",
                "faixa_tipica": "2-3x o alcance com frequência saudável",
                "quando_usar": "Para medir volume total de exposição",
                "descricao": "Número total de vezes que seu anúncio foi exibido",
            },
            {
                "nome": "CPM",
                "formula": "(Custo total / Impressões) x 1000",
                "faixa_tipica": "R$8-25 (varia por plataforma e segmentação)",
                "quando_usar": "Para avaliar eficiência de custo por exposição",
                "descricao": "Custo por mil impressões",
            },
        ],
        "secundarios": [
            {
                "nome": "Frequência",
                "formula": "Impressões / Alcance",
                "faixa_tipica": "1.5-3.0 para awareness; acima de 4 gera fadiga",
                "quando_usar": "Para controlar saturação de audiência",
                "descricao": "Média de vezes que cada pessoa viu seu anúncio",
            },
            {
                "nome": "Brand Lift",
                "formula": "% aumento em reconhecimento pós-campanha",
                "faixa_tipica": "3-15% de lift dependendo da categoria",
                "quando_usar": "Para medir impacto real na percepção de marca",
                "descricao": "Elevação na lembrança/reconhecimento de marca",
            },
            {
                "nome": "Custo por Alcance (CPR)",
                "formula": "Custo total / Alcance",
                "faixa_tipica": "R$0.01-0.05 por pessoa alcançada",
                "quando_usar": "Para comparar eficiência entre plataformas",
                "descricao": "Custo médio para alcançar uma pessoa única",
            },
            {
                "nome": "Share of Voice",
                "formula": "Impressões da marca / Total da categoria",
                "faixa_tipica": "Depende do setor; buscar >10% em nichos",
                "quando_usar": "Para avaliar presença relativa no mercado",
                "descricao": "Participação da marca no volume total de anúncios da categoria",
            },
        ],
        "terciarios": [
            {
                "nome": "Visualizações",
                "formula": "Total de visualizações do anúncio/vídeo",
                "faixa_tipica": "R$0.02-0.10 por view; 3s+ para vídeo",
                "quando_usar": "Para medir volume de views em vídeo ou conteúdo",
                "descricao": "Total de visualizações do anúncio ou vídeo",
            },
            {
                "nome": "Engajamento",
                "formula": "Curtidas + Comentários + Compartilhamentos + Salvamentos",
                "faixa_tipica": "0.5-2% de taxa sobre impressões",
                "quando_usar": "Indicador de ressonância e interação",
                "descricao": "Total de interações com o anúncio",
            },
            {
                "nome": "Comentários",
                "formula": "Total de comentários no anúncio",
                "faixa_tipica": "0.01-0.1% das impressões",
                "quando_usar": "Para medir nível de conversa e interesse ativo",
                "descricao": "Número de comentários recebidos no anúncio",
            },
            {
                "nome": "Custo Total",
                "formula": "Soma de todo investimento na campanha",
                "faixa_tipica": "= Budget alocado para a etapa",
                "quando_usar": "Para controlar gasto total vs. planejado",
                "descricao": "Investimento total realizado na campanha",
            },
            {
                "nome": "Custo Diário",
                "formula": "Custo total / Dias de veiculação",
                "faixa_tipica": "Budget / dias do período",
                "quando_usar": "Para monitorar pacing diário de investimento",
                "descricao": "Valor médio gasto por dia de campanha",
            },
            {
                "nome": "Cliques",
                "formula": "Total de cliques no anúncio",
                "faixa_tipica": "Depende de CTR e volume de impressões",
                "quando_usar": "Indicador secundário em awareness; foco é exposição",
                "descricao": "Número total de cliques no anúncio",
            },
            {
                "nome": "CTR",
                "formula": "(Cliques / Impressões) x 100",
                "faixa_tipica": "0.3-1.5% para awareness (menor que outras etapas)",
                "quando_usar": "Para monitorar atratividade do criativo",
                "descricao": "Taxa de cliques sobre impressões",
            },
            {
                "nome": "CPC",
                "formula": "Custo total / Cliques",
                "faixa_tipica": "R$0.30-3.00 dependendo da plataforma",
                "quando_usar": "Para referência; não é métrica principal em awareness",
                "descricao": "Custo médio por clique",
            },
            {
                "nome": "CPA",
                "formula": "Custo total / Total de conversões",
                "faixa_tipica": "Muito alto em awareness; não é foco",
                "quando_usar": "Apenas para referência de baseline",
                "descricao": "Custo médio por aquisição/conversão",
            },
        ],
    },
    "Interesse": {
        "primarios": [
            {
                "nome": "CTR",
                "formula": "(Cliques / Impressões) x 100",
                "faixa_tipica": "0.5-2.0% (Search: 3-8%; Display: 0.3-1%)",
                "quando_usar": "Para medir atratividade do anúncio",
                "descricao": "Taxa de cliques sobre impressões",
            },
            {
                "nome": "Cliques",
                "formula": "Total de cliques no anúncio",
                "faixa_tipica": "Depende de CTR e impressões",
                "quando_usar": "Para medir volume de interesse gerado",
                "descricao": "Número total de cliques no anúncio",
            },
            {
                "nome": "CPC",
                "formula": "Custo total / Cliques",
                "faixa_tipica": "R$0.30-3.00 (Social); R$1.00-8.00 (Search)",
                "quando_usar": "Para avaliar custo de gerar interesse",
                "descricao": "Custo médio por clique",
            },
        ],
        "secundarios": [
            {
                "nome": "Taxa de Engajamento",
                "formula": "(Engajamentos / Alcance) x 100",
                "faixa_tipica": "1-5% em social media",
                "quando_usar": "Para medir profundidade de interesse",
                "descricao": "Percentual de pessoas que interagiram com o conteúdo",
            },
            {
                "nome": "ThruPlay",
                "formula": "Vídeos assistidos até o final ou 15s+",
                "faixa_tipica": "15-40% de completion rate",
                "quando_usar": "Para medir interesse genuíno no conteúdo",
                "descricao": "Visualizações completas ou de 15+ segundos (Meta)",
            },
            {
                "nome": "Tempo Médio na Página",
                "formula": "Soma tempo na página / Total de sessões",
                "faixa_tipica": "30s-2min para landing pages",
                "quando_usar": "Para avaliar qualidade do tráfego gerado",
                "descricao": "Duração média das visitas à página de destino",
            },
        ],
        "terciarios": [
            {
                "nome": "Compartilhamentos",
                "formula": "Total de shares do conteúdo",
                "faixa_tipica": "0.1-0.5% das impressões",
                "quando_usar": "Indicador de conteúdo com potencial viral",
                "descricao": "Número de vezes que o conteúdo foi compartilhado",
            },
            {
                "nome": "Salvamentos",
                "formula": "Total de saves/bookmarks",
                "faixa_tipica": "0.2-1% do alcance",
                "quando_usar": "Sinal forte de intenção futura",
                "descricao": "Número de vezes que o conteúdo foi salvo",
            },
            {
                "nome": "Impressões",
                "formula": "Total de exibições do anúncio",
                "faixa_tipica": "Depende de budget e CPM da plataforma",
                "quando_usar": "Para monitorar volume de exposição",
                "descricao": "Número total de vezes que seu anúncio foi exibido",
            },
            {
                "nome": "CPM",
                "formula": "(Custo total / Impressões) x 1000",
                "faixa_tipica": "R$8-25 dependendo da plataforma",
                "quando_usar": "Para monitorar eficiência de distribuição",
                "descricao": "Custo por mil impressões",
            },
            {
                "nome": "Alcance",
                "formula": "Usuários únicos impactados",
                "faixa_tipica": "Varia por budget e segmentação",
                "quando_usar": "Para monitorar expansão de audiência",
                "descricao": "Número de pessoas únicas que viram seu anúncio",
            },
            {
                "nome": "Frequência",
                "formula": "Impressões / Alcance",
                "faixa_tipica": "2-4 para interesse; monitorar fadiga",
                "quando_usar": "Para controlar saturação de audiência",
                "descricao": "Média de vezes que cada pessoa viu seu anúncio",
            },
            {
                "nome": "Visualizações",
                "formula": "Total de visualizações do anúncio/vídeo",
                "faixa_tipica": "R$0.02-0.10 por view",
                "quando_usar": "Para medir volume de views em vídeo ou conteúdo",
                "descricao": "Total de visualizações do anúncio ou vídeo",
            },
            {
                "nome": "Engajamento",
                "formula": "Curtidas + Comentários + Compartilhamentos + Salvamentos",
                "faixa_tipica": "1-3% de taxa sobre impressões",
                "quando_usar": "Indicador agregado de interação",
                "descricao": "Total de interações com o anúncio",
            },
            {
                "nome": "Comentários",
                "formula": "Total de comentários no anúncio",
                "faixa_tipica": "0.02-0.2% das impressões",
                "quando_usar": "Para medir nível de conversa e interesse ativo",
                "descricao": "Número de comentários recebidos no anúncio",
            },
            {
                "nome": "CPA",
                "formula": "Custo total / Total de conversões",
                "faixa_tipica": "R$20-150 dependendo do segmento",
                "quando_usar": "Para referência; não é foco em etapa de interesse",
                "descricao": "Custo médio por aquisição/conversão",
            },
            {
                "nome": "Custo Total",
                "formula": "Soma de todo investimento na campanha",
                "faixa_tipica": "= Budget alocado para a etapa",
                "quando_usar": "Para controlar gasto total vs. planejado",
                "descricao": "Investimento total realizado na campanha",
            },
            {
                "nome": "Custo Diário",
                "formula": "Custo total / Dias de veiculação",
                "faixa_tipica": "Budget / dias do período",
                "quando_usar": "Para monitorar pacing diário de investimento",
                "descricao": "Valor médio gasto por dia de campanha",
            },
        ],
    },
    "Consideração": {
        "primarios": [
            {
                "nome": "CTR",
                "formula": "(Cliques / Impressões) x 100",
                "faixa_tipica": "1.0-3.0% para consideração",
                "quando_usar": "Indicador principal de avaliação ativa",
                "descricao": "Taxa de cliques sobre impressões",
            },
            {
                "nome": "CPC",
                "formula": "Custo total / Cliques",
                "faixa_tipica": "R$0.50-5.00 dependendo da plataforma",
                "quando_usar": "Para otimizar custo de engajamento qualificado",
                "descricao": "Custo médio por clique",
            },
            {
                "nome": "Taxa de Engajamento",
                "formula": "(Engajamentos / Alcance) x 100",
                "faixa_tipica": "2-6% para conteúdo de consideração",
                "quando_usar": "Para medir profundidade de avaliação",
                "descricao": "Percentual de pessoas que interagiram ativamente",
            },
        ],
        "secundarios": [
            {
                "nome": "ThruPlay",
                "formula": "Vídeos assistidos até o final ou 15s+",
                "faixa_tipica": "20-50% completion rate",
                "quando_usar": "Para conteúdo educativo/demonstrativo",
                "descricao": "Visualizações completas de vídeo",
            },
            {
                "nome": "Cliques no Link",
                "formula": "Cliques que levam ao site/landing page",
                "faixa_tipica": "60-80% dos cliques totais são no link",
                "quando_usar": "Para medir intenção de saber mais",
                "descricao": "Cliques que direcionam para página externa",
            },
            {
                "nome": "CPM",
                "formula": "(Custo total / Impressões) x 1000",
                "faixa_tipica": "R$12-35 para audiências mais qualificadas",
                "quando_usar": "Para monitorar eficiência de distribuição",
                "descricao": "Custo por mil impressões",
            },
            {
                "nome": "Bounce Rate",
                "formula": "(Sessões de página única / Total sessões) x 100",
                "faixa_tipica": "30-60% para landing pages de campanha",
                "quando_usar": "Para avaliar relevância do tráfego",
                "descricao": "Taxa de rejeição na página de destino",
            },
        ],
        "terciarios": [
            {
                "nome": "Páginas por Sessão",
                "formula": "Total pageviews / Total sessões",
                "faixa_tipica": "1.5-3.0 páginas por sessão",
                "quando_usar": "Para medir exploração do site",
                "descricao": "Média de páginas visitadas por sessão",
            },
            {
                "nome": "Custo por Engajamento",
                "formula": "Custo total / Total de engajamentos",
                "faixa_tipica": "R$0.10-1.00 por engajamento",
                "quando_usar": "Para otimizar custo de interação",
                "descricao": "Custo médio por interação com o conteúdo",
            },
            {
                "nome": "Cliques",
                "formula": "Total de cliques no anúncio",
                "faixa_tipica": "Depende de CTR e volume de impressões",
                "quando_usar": "Para medir volume de tráfego gerado",
                "descricao": "Número total de cliques no anúncio",
            },
            {
                "nome": "Impressões",
                "formula": "Total de exibições do anúncio",
                "faixa_tipica": "Depende de budget e CPM",
                "quando_usar": "Para monitorar volume de exposição",
                "descricao": "Número total de vezes que seu anúncio foi exibido",
            },
            {
                "nome": "Alcance",
                "formula": "Usuários únicos impactados",
                "faixa_tipica": "Varia por budget e segmentação",
                "quando_usar": "Para monitorar expansão de audiência",
                "descricao": "Número de pessoas únicas que viram seu anúncio",
            },
            {
                "nome": "Frequência",
                "formula": "Impressões / Alcance",
                "faixa_tipica": "2-5 para consideração",
                "quando_usar": "Para controlar saturação; frequência maior aceitável nesta etapa",
                "descricao": "Média de vezes que cada pessoa viu seu anúncio",
            },
            {
                "nome": "Visualizações",
                "formula": "Total de visualizações do anúncio/vídeo",
                "faixa_tipica": "R$0.02-0.10 por view",
                "quando_usar": "Para medir consumo de conteúdo demonstrativo",
                "descricao": "Total de visualizações do anúncio ou vídeo",
            },
            {
                "nome": "Engajamento",
                "formula": "Curtidas + Comentários + Compartilhamentos + Salvamentos",
                "faixa_tipica": "2-6% de taxa para conteúdo de consideração",
                "quando_usar": "Indicador de avaliação ativa do conteúdo",
                "descricao": "Total de interações com o anúncio",
            },
            {
                "nome": "Comentários",
                "formula": "Total de comentários no anúncio",
                "faixa_tipica": "0.02-0.3% das impressões",
                "quando_usar": "Para medir dúvidas e interesse qualificado",
                "descricao": "Número de comentários recebidos no anúncio",
            },
            {
                "nome": "CPA",
                "formula": "Custo total / Total de conversões",
                "faixa_tipica": "R$20-150 dependendo do segmento",
                "quando_usar": "Para referência de custo de micro-conversões",
                "descricao": "Custo médio por aquisição/conversão",
            },
            {
                "nome": "Custo Total",
                "formula": "Soma de todo investimento na campanha",
                "faixa_tipica": "= Budget alocado para a etapa",
                "quando_usar": "Para controlar gasto total vs. planejado",
                "descricao": "Investimento total realizado na campanha",
            },
            {
                "nome": "Custo Diário",
                "formula": "Custo total / Dias de veiculação",
                "faixa_tipica": "Budget / dias do período",
                "quando_usar": "Para monitorar pacing diário de investimento",
                "descricao": "Valor médio gasto por dia de campanha",
            },
        ],
    },
    "Intenção": {
        "primarios": [
            {
                "nome": "Leads Gerados",
                "formula": "Total de formulários preenchidos / cadastros",
                "faixa_tipica": "Taxa de conversão de lead: 2-8% do tráfego",
                "quando_usar": "Para campanhas de geração de leads",
                "descricao": "Número de leads qualificados capturados",
            },
            {
                "nome": "CPL (Custo por Lead)",
                "formula": "Custo total / Total de leads",
                "faixa_tipica": "R$5-50 (B2C); R$30-200 (B2B)",
                "quando_usar": "Para avaliar eficiência de captação",
                "descricao": "Custo médio por lead gerado",
            },
            {
                "nome": "Taxa de Conversão de Lead",
                "formula": "(Leads / Cliques) x 100",
                "faixa_tipica": "2-10% dependendo da oferta e segmento",
                "quando_usar": "Para otimizar landing pages e ofertas",
                "descricao": "Percentual de visitantes que se tornaram leads",
            },
        ],
        "secundarios": [
            {
                "nome": "Adições ao Carrinho",
                "formula": "Total de add-to-cart events",
                "faixa_tipica": "5-15% do tráfego para e-commerce",
                "quando_usar": "Para e-commerce; mede intenção de compra",
                "descricao": "Número de produtos adicionados ao carrinho",
            },
            {
                "nome": "Inícios de Checkout",
                "formula": "Total de initiate-checkout events",
                "faixa_tipica": "40-70% dos que adicionaram ao carrinho",
                "quando_usar": "Para medir avanço no funil de compra",
                "descricao": "Número de usuários que iniciaram o checkout",
            },
            {
                "nome": "CPC",
                "formula": "Custo total / Cliques",
                "faixa_tipica": "R$1.00-8.00 para público de intenção",
                "quando_usar": "Para monitorar custo de tráfego qualificado",
                "descricao": "Custo médio por clique",
            },
        ],
        "terciarios": [
            {
                "nome": "Downloads/Inscrições",
                "formula": "Total de downloads ou inscrições",
                "faixa_tipica": "Varia por tipo de material",
                "quando_usar": "Para ofertas de conteúdo rico (ebooks, webinars)",
                "descricao": "Ações de download ou inscrição realizadas",
            },
            {
                "nome": "Mensagens Recebidas",
                "formula": "Total de mensagens via Messenger/WhatsApp/DM",
                "faixa_tipica": "R$1-10 por mensagem recebida",
                "quando_usar": "Para campanhas com CTA de mensagem",
                "descricao": "Total de conversas iniciadas pelo usuário",
            },
            {
                "nome": "Impressões",
                "formula": "Total de exibições do anúncio",
                "faixa_tipica": "Depende de budget e CPM",
                "quando_usar": "Para monitorar volume de exposição",
                "descricao": "Número total de vezes que seu anúncio foi exibido",
            },
            {
                "nome": "Cliques",
                "formula": "Total de cliques no anúncio",
                "faixa_tipica": "Depende de CTR e volume de impressões",
                "quando_usar": "Para medir volume de tráfego qualificado",
                "descricao": "Número total de cliques no anúncio",
            },
            {
                "nome": "CTR",
                "formula": "(Cliques / Impressões) x 100",
                "faixa_tipica": "1-3% para campanhas de intenção",
                "quando_usar": "Para monitorar eficiência dos criativos",
                "descricao": "Taxa de cliques sobre impressões",
            },
            {
                "nome": "CPM",
                "formula": "(Custo total / Impressões) x 1000",
                "faixa_tipica": "R$15-40 para audiências de intenção",
                "quando_usar": "Para monitorar custo de distribuição",
                "descricao": "Custo por mil impressões",
            },
            {
                "nome": "CPA",
                "formula": "Custo total / Total de conversões",
                "faixa_tipica": "R$20-150 dependendo do segmento",
                "quando_usar": "Para avaliar custo de micro-conversões (leads, cadastros)",
                "descricao": "Custo médio por aquisição/conversão",
            },
            {
                "nome": "Alcance",
                "formula": "Usuários únicos impactados",
                "faixa_tipica": "Menor que awareness; audiência mais qualificada",
                "quando_usar": "Para monitorar tamanho da audiência atingida",
                "descricao": "Número de pessoas únicas que viram seu anúncio",
            },
            {
                "nome": "Frequência",
                "formula": "Impressões / Alcance",
                "faixa_tipica": "3-6 para intenção; remarketing aceita mais",
                "quando_usar": "Para controlar saturação em audiências quentes",
                "descricao": "Média de vezes que cada pessoa viu seu anúncio",
            },
            {
                "nome": "Visualizações",
                "formula": "Total de visualizações do anúncio/vídeo",
                "faixa_tipica": "R$0.03-0.15 por view",
                "quando_usar": "Para vídeos demonstrativos de produto/serviço",
                "descricao": "Total de visualizações do anúncio ou vídeo",
            },
            {
                "nome": "Engajamento",
                "formula": "Curtidas + Comentários + Compartilhamentos + Salvamentos",
                "faixa_tipica": "1-4% de taxa sobre impressões",
                "quando_usar": "Indicador de interesse qualificado",
                "descricao": "Total de interações com o anúncio",
            },
            {
                "nome": "Comentários",
                "formula": "Total de comentários no anúncio",
                "faixa_tipica": "0.02-0.3% das impressões",
                "quando_usar": "Para medir dúvidas pré-conversão",
                "descricao": "Número de comentários recebidos no anúncio",
            },
            {
                "nome": "Custo Total",
                "formula": "Soma de todo investimento na campanha",
                "faixa_tipica": "= Budget alocado para a etapa",
                "quando_usar": "Para controlar gasto total vs. planejado",
                "descricao": "Investimento total realizado na campanha",
            },
            {
                "nome": "Custo Diário",
                "formula": "Custo total / Dias de veiculação",
                "faixa_tipica": "Budget / dias do período",
                "quando_usar": "Para monitorar pacing diário de investimento",
                "descricao": "Valor médio gasto por dia de campanha",
            },
        ],
    },
    "Conversão/Ação": {
        "primarios": [
            {
                "nome": "Conversões",
                "formula": "Total de ações desejadas completadas",
                "faixa_tipica": "Taxa: 1-5% do tráfego qualificado",
                "quando_usar": "Métrica principal de performance",
                "descricao": "Número de conversões realizadas (compras, cadastros, etc.)",
            },
            {
                "nome": "CPA (Custo por Aquisição)",
                "formula": "Custo total / Total de conversões",
                "faixa_tipica": "R$20-150 (e-commerce); R$50-500 (serviços)",
                "quando_usar": "Para avaliar eficiência de conversão",
                "descricao": "Custo médio por conversão realizada",
            },
            {
                "nome": "ROAS",
                "formula": "Receita gerada / Investimento em mídia",
                "faixa_tipica": "2x-6x para e-commerce; 1.5x-3x para serviços",
                "quando_usar": "Para campanhas com rastreamento de receita",
                "descricao": "Retorno sobre investimento em anúncios",
            },
        ],
        "secundarios": [
            {
                "nome": "Ticket Médio",
                "formula": "Receita total / Número de conversões",
                "faixa_tipica": "Varia por segmento; monitorar tendência",
                "quando_usar": "Para avaliar qualidade das conversões",
                "descricao": "Valor médio por transação",
            },
            {
                "nome": "Taxa de Conversão",
                "formula": "(Conversões / Cliques) x 100",
                "faixa_tipica": "1-5% (e-commerce); 5-15% (lead gen)",
                "quando_usar": "Para otimizar funil de conversão",
                "descricao": "Percentual de cliques que resultaram em conversão",
            },
            {
                "nome": "Receita Total",
                "formula": "Soma de todas as transações atribuídas",
                "faixa_tipica": "Meta = Budget x ROAS alvo",
                "quando_usar": "Para medir resultado financeiro absoluto",
                "descricao": "Receita total gerada pela campanha",
            },
            {
                "nome": "CTR",
                "formula": "(Cliques / Impressões) x 100",
                "faixa_tipica": "1.5-4% para campanhas de conversão",
                "quando_usar": "Para monitorar eficiência dos criativos",
                "descricao": "Taxa de cliques sobre impressões",
            },
        ],
        "terciarios": [
            {
                "nome": "Custo por Resultado",
                "formula": "Custo total / Resultados",
                "faixa_tipica": "Depende do tipo de resultado rastreado",
                "quando_usar": "Quando 'resultado' não é necessariamente venda",
                "descricao": "Custo médio por resultado obtido",
            },
            {
                "nome": "Frequência de Compra",
                "formula": "Transações / Compradores únicos",
                "faixa_tipica": "1.1-1.5x no período de campanha",
                "quando_usar": "Para campanhas com público recorrente",
                "descricao": "Média de compras por cliente único",
            },
            {
                "nome": "Impressões",
                "formula": "Total de exibições do anúncio",
                "faixa_tipica": "Depende de budget e CPM",
                "quando_usar": "Para monitorar volume de exposição",
                "descricao": "Número total de vezes que seu anúncio foi exibido",
            },
            {
                "nome": "Cliques",
                "formula": "Total de cliques no anúncio",
                "faixa_tipica": "Depende de CTR e volume de impressões",
                "quando_usar": "Para medir volume de tráfego ao site",
                "descricao": "Número total de cliques no anúncio",
            },
            {
                "nome": "CPC",
                "formula": "Custo total / Cliques",
                "faixa_tipica": "R$1.00-8.00 para público de conversão",
                "quando_usar": "Para monitorar custo de tráfego qualificado",
                "descricao": "Custo médio por clique",
            },
            {
                "nome": "CPM",
                "formula": "(Custo total / Impressões) x 1000",
                "faixa_tipica": "R$15-45 para audiências de conversão",
                "quando_usar": "Para monitorar custo de distribuição",
                "descricao": "Custo por mil impressões",
            },
            {
                "nome": "Alcance",
                "formula": "Usuários únicos impactados",
                "faixa_tipica": "Audiência menor e mais qualificada",
                "quando_usar": "Para monitorar cobertura da audiência-alvo",
                "descricao": "Número de pessoas únicas que viram seu anúncio",
            },
            {
                "nome": "Frequência",
                "formula": "Impressões / Alcance",
                "faixa_tipica": "4-8 para conversão; remarketing aceita alta frequência",
                "quando_usar": "Para controlar repetição em audiências de conversão",
                "descricao": "Média de vezes que cada pessoa viu seu anúncio",
            },
            {
                "nome": "Visualizações",
                "formula": "Total de visualizações do anúncio/vídeo",
                "faixa_tipica": "R$0.03-0.15 por view",
                "quando_usar": "Para vídeos de produto/depoimentos",
                "descricao": "Total de visualizações do anúncio ou vídeo",
            },
            {
                "nome": "Engajamento",
                "formula": "Curtidas + Comentários + Compartilhamentos + Salvamentos",
                "faixa_tipica": "1-3% de taxa sobre impressões",
                "quando_usar": "Indicador secundário de ressonância",
                "descricao": "Total de interações com o anúncio",
            },
            {
                "nome": "Comentários",
                "formula": "Total de comentários no anúncio",
                "faixa_tipica": "0.01-0.2% das impressões",
                "quando_usar": "Para medir dúvidas e social proof",
                "descricao": "Número de comentários recebidos no anúncio",
            },
            {
                "nome": "Custo Total",
                "formula": "Soma de todo investimento na campanha",
                "faixa_tipica": "= Budget alocado para a etapa",
                "quando_usar": "Para controlar gasto total vs. planejado",
                "descricao": "Investimento total realizado na campanha",
            },
            {
                "nome": "Custo Diário",
                "formula": "Custo total / Dias de veiculação",
                "faixa_tipica": "Budget / dias do período",
                "quando_usar": "Para monitorar pacing diário de investimento",
                "descricao": "Valor médio gasto por dia de campanha",
            },
        ],
    },
    "Retenção/Fidelização": {
        "primarios": [
            {
                "nome": "Taxa de Retenção",
                "formula": "(Clientes retidos / Clientes no início) x 100",
                "faixa_tipica": "60-80% mensal para e-commerce; 85-95% SaaS",
                "quando_usar": "Métrica principal de fidelização",
                "descricao": "Percentual de clientes que permanecem ativos",
            },
            {
                "nome": "LTV (Lifetime Value)",
                "formula": "Ticket médio x Frequência x Tempo de retenção",
                "faixa_tipica": "3-5x o CPA para ser saudável",
                "quando_usar": "Para avaliar valor de longo prazo do cliente",
                "descricao": "Valor total esperado de um cliente ao longo do tempo",
            },
            {
                "nome": "Taxa de Recompra",
                "formula": "(Compras recorrentes / Total de clientes) x 100",
                "faixa_tipica": "20-40% em 90 dias para e-commerce",
                "quando_usar": "Para medir efetividade de retenção",
                "descricao": "Percentual de clientes que compraram novamente",
            },
        ],
        "secundarios": [
            {
                "nome": "ROAS (Retenção)",
                "formula": "Receita gerada / Investimento em mídia",
                "faixa_tipica": "4x-10x para remarketing de clientes existentes",
                "quando_usar": "Para avaliar eficiência de reinvestimento",
                "descricao": "Retorno sobre investimento em campanhas de retenção",
            },
            {
                "nome": "NPS (Net Promoter Score)",
                "formula": "% Promotores - % Detratores",
                "faixa_tipica": "30-70 é considerado bom",
                "quando_usar": "Para medir satisfação e propensão a indicar",
                "descricao": "Índice de satisfação e lealdade do cliente",
            },
            {
                "nome": "Churn Rate",
                "formula": "(Clientes perdidos / Total clientes) x 100",
                "faixa_tipica": "2-8% mensal para e-commerce",
                "quando_usar": "Para monitorar perda de base",
                "descricao": "Taxa de cancelamento/abandono de clientes",
            },
        ],
        "terciarios": [
            {
                "nome": "Taxa de Abertura de Email",
                "formula": "(Emails abertos / Emails enviados) x 100",
                "faixa_tipica": "15-30% dependendo do segmento",
                "quando_usar": "Para campanhas de CRM/email marketing",
                "descricao": "Percentual de emails abertos pela base",
            },
            {
                "nome": "Engajamento em Fidelidade",
                "formula": "Membros ativos / Total membros",
                "faixa_tipica": "30-50% de engajamento ativo",
                "quando_usar": "Para marcas com programa de pontos/benefícios",
                "descricao": "Nível de participação em programas de fidelidade",
            },
        ],
    },
}

PLATAFORMA_OBJETIVOS = {
    "Meta Ads (Facebook/Instagram)": [
        "Reconhecimento de Marca", "Alcance", "Tráfego", "Engajamento",
        "Visualizações de Vídeo", "Geração de Leads", "Vendas/Conversões",
        "Vendas de Catálogo", "Remarketing/Retargeting", "Promoção de App",
    ],
    "Google Ads": [
        "Reconhecimento de Marca", "Tráfego", "Vendas/Conversões",
        "Geração de Leads", "Promoção de App", "Alcance",
        "Vendas de Catálogo",
    ],
    "TikTok": [
        "Reconhecimento de Marca", "Alcance", "Tráfego", "Engajamento",
        "Visualizações de Vídeo", "Vendas/Conversões", "Geração de Leads",
    ],
    "LinkedIn": [
        "Reconhecimento de Marca", "Tráfego", "Engajamento",
        "Geração de Leads", "Branding Institucional",
    ],
    "YouTube": [
        "Reconhecimento de Marca", "Alcance", "Visualizações de Vídeo",
        "Tráfego", "Vendas/Conversões",
    ],
    "Mídia Programática": [
        "Reconhecimento de Marca", "Alcance", "Tráfego",
        "Remarketing/Retargeting", "Vendas/Conversões",
    ],
    "Twitter": [
        "Reconhecimento de Marca", "Alcance", "Engajamento", "Tráfego",
    ],
    "Pinterest": [
        "Reconhecimento de Marca", "Tráfego", "Vendas de Catálogo",
        "Engajamento",
    ],
}

BENCHMARKS_BR = {
    "Meta Ads (Facebook/Instagram)": {
        "CPM": {"min": 8.0, "max": 25.0, "medio": 15.0, "unidade": "R$"},
        "CPC": {"min": 0.30, "max": 3.00, "medio": 1.20, "unidade": "R$"},
        "CTR": {"min": 0.8, "max": 2.5, "medio": 1.5, "unidade": "%"},
        "CPA": {"min": 15.0, "max": 120.0, "medio": 55.0, "unidade": "R$"},
        "ROAS": {"min": 2.0, "max": 6.0, "medio": 3.5, "unidade": "x"},
        "CPL": {"min": 5.0, "max": 50.0, "medio": 20.0, "unidade": "R$"},
    },
    "Google Ads": {
        "CPM": {"min": 5.0, "max": 35.0, "medio": 18.0, "unidade": "R$"},
        "CPC": {"min": 1.00, "max": 8.00, "medio": 3.50, "unidade": "R$"},
        "CTR": {"min": 2.0, "max": 8.0, "medio": 4.5, "unidade": "%"},
        "CPA": {"min": 25.0, "max": 200.0, "medio": 80.0, "unidade": "R$"},
        "ROAS": {"min": 2.0, "max": 8.0, "medio": 4.0, "unidade": "x"},
        "CPL": {"min": 10.0, "max": 80.0, "medio": 35.0, "unidade": "R$"},
    },
    "TikTok": {
        "CPM": {"min": 5.0, "max": 20.0, "medio": 10.0, "unidade": "R$"},
        "CPC": {"min": 0.20, "max": 2.00, "medio": 0.80, "unidade": "R$"},
        "CTR": {"min": 0.5, "max": 2.0, "medio": 1.2, "unidade": "%"},
        "CPA": {"min": 10.0, "max": 80.0, "medio": 35.0, "unidade": "R$"},
        "ROAS": {"min": 1.5, "max": 5.0, "medio": 3.0, "unidade": "x"},
        "CPL": {"min": 3.0, "max": 30.0, "medio": 12.0, "unidade": "R$"},
    },
    "LinkedIn": {
        "CPM": {"min": 30.0, "max": 80.0, "medio": 50.0, "unidade": "R$"},
        "CPC": {"min": 5.00, "max": 25.00, "medio": 12.00, "unidade": "R$"},
        "CTR": {"min": 0.3, "max": 1.0, "medio": 0.6, "unidade": "%"},
        "CPA": {"min": 50.0, "max": 500.0, "medio": 180.0, "unidade": "R$"},
        "CPL": {"min": 30.0, "max": 200.0, "medio": 80.0, "unidade": "R$"},
    },
    "YouTube": {
        "CPM": {"min": 10.0, "max": 30.0, "medio": 18.0, "unidade": "R$"},
        "CPV": {"min": 0.02, "max": 0.15, "medio": 0.06, "unidade": "R$"},
        "VTR": {"min": 15.0, "max": 40.0, "medio": 25.0, "unidade": "%"},
        "CTR": {"min": 0.3, "max": 1.5, "medio": 0.7, "unidade": "%"},
    },
    "Mídia Programática": {
        "CPM": {"min": 3.0, "max": 20.0, "medio": 10.0, "unidade": "R$"},
        "CPC": {"min": 0.50, "max": 5.00, "medio": 2.00, "unidade": "R$"},
        "CTR": {"min": 0.1, "max": 0.5, "medio": 0.25, "unidade": "%"},
        "CPA": {"min": 20.0, "max": 150.0, "medio": 60.0, "unidade": "R$"},
    },
    "Twitter": {
        "CPM": {"min": 8.0, "max": 25.0, "medio": 15.0, "unidade": "R$"},
        "CPC": {"min": 0.50, "max": 4.00, "medio": 1.80, "unidade": "R$"},
        "CTR": {"min": 0.5, "max": 2.0, "medio": 1.0, "unidade": "%"},
    },
    "Pinterest": {
        "CPM": {"min": 5.0, "max": 15.0, "medio": 9.0, "unidade": "R$"},
        "CPC": {"min": 0.30, "max": 2.50, "medio": 1.00, "unidade": "R$"},
        "CTR": {"min": 0.5, "max": 2.5, "medio": 1.3, "unidade": "%"},
    },
}

TEMPLATES_ALOCACAO_BUDGET = {
    "Marca Nova / Lançamento": {
        "descricao": "Foco em awareness e construção de audiência",
        "distribuicao": {
            "Consciência (Awareness)": 40,
            "Interesse": 25,
            "Consideração": 20,
            "Intenção": 10,
            "Conversão/Ação": 5,
            "Retenção/Fidelização": 0,
        },
    },
    "E-commerce / Performance": {
        "descricao": "Foco em conversões com suporte de awareness",
        "distribuicao": {
            "Consciência (Awareness)": 15,
            "Interesse": 10,
            "Consideração": 15,
            "Intenção": 20,
            "Conversão/Ação": 30,
            "Retenção/Fidelização": 10,
        },
    },
    "B2B / Geração de Leads": {
        "descricao": "Foco em leads qualificados com nurturing",
        "distribuicao": {
            "Consciência (Awareness)": 20,
            "Interesse": 20,
            "Consideração": 25,
            "Intenção": 25,
            "Conversão/Ação": 10,
            "Retenção/Fidelização": 0,
        },
    },
    "Branding / Institucional": {
        "descricao": "Foco em presença de marca e reputação",
        "distribuicao": {
            "Consciência (Awareness)": 45,
            "Interesse": 25,
            "Consideração": 15,
            "Intenção": 5,
            "Conversão/Ação": 5,
            "Retenção/Fidelização": 5,
        },
    },
    "Retenção / CRM": {
        "descricao": "Foco em base existente e recompra",
        "distribuicao": {
            "Consciência (Awareness)": 5,
            "Interesse": 5,
            "Consideração": 10,
            "Intenção": 15,
            "Conversão/Ação": 25,
            "Retenção/Fidelização": 40,
        },
    },
}

def _build_descricoes():
    """Flat dict nome→descrição extraído de KPIS_POR_ETAPA."""
    desc = {}
    for hierarquia in KPIS_POR_ETAPA.values():
        for tier in ("primarios", "secundarios", "terciarios"):
            for kpi in hierarquia.get(tier, []):
                if kpi["nome"] not in desc:
                    desc[kpi["nome"]] = kpi["descricao"]
    return desc

def _build_metricas_por_etapa():
    """Flat list de nomes de KPIs por etapa (compat com código antigo)."""
    result = {}
    for etapa, hierarquia in KPIS_POR_ETAPA.items():
        nomes = []
        for tier in ("primarios", "secundarios", "terciarios"):
            for kpi in hierarquia.get(tier, []):
                if kpi["nome"] not in nomes:
                    nomes.append(kpi["nome"])
        result[etapa] = nomes
    for old_key, new_key in LEGACY_FUNNEL_MAP.items():
        if new_key in result:
            result[old_key] = result[new_key]
    return result

DESCRICOES_METRICAS = _build_descricoes()
METRICAS_POR_ETAPA = _build_metricas_por_etapa()
