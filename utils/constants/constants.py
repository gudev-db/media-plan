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

THEORETICAL_FRAMEWORKS = {
    "summary": (
        "Multiple established frameworks describe the customer journey through "
        "overlapping but distinct lenses. The key insight across all models is that "
        "different stages require fundamentally different objectives, metrics, creative "
        "approaches, and budget allocation. No single metric or approach works across "
        "all stages."
    ),
    "frameworks": {
        "AIDA": {
            "author": "E. St. Elmo Lewis (1898)",
            "stages": ["Attention", "Interest", "Desire", "Action"],
            "key_insight": (
                "The oldest marketing funnel model. Linear progression from cognitive "
                "(awareness) to affective (interest/desire) to behavioral (action). "
                "Limitation: assumes a strictly linear path and ignores post-purchase loyalty."
            ),
        },
        "See-Think-Do-Care (STDC)": {
            "author": "Avinash Kaushik / Google (2013)",
            "stages": ["See", "Think", "Do", "Care"],
            "key_insight": (
                "Focuses on audience intent clusters rather than demographics. "
                "'See' = largest qualified audience (no commercial intent yet). "
                "'Think' = actively considering category solutions. "
                "'Do' = ready to transact. "
                "'Care' = existing customers with 2+ transactions. "
                "Critical principle: each stage must have DIFFERENT content, channels, "
                "AND measurement. Judging 'See' campaigns by 'Do' metrics (e.g., CPA) "
                "is the most common and destructive mistake in digital marketing."
            ),
            "metrics_by_stage": {
                "See": "Impressions, Reach, Brand Lift, New visitors, Awareness surveys",
                "Think": "CTR, Engagement rate, Pages/session, Time on site, Return visits",
                "Do": "Conversion rate, CPA, ROAS, Revenue, Transactions",
                "Care": "LTV, Repeat purchase rate, NPS, Retention rate, Referral rate",
            },
        },
        "McKinsey Consumer Decision Journey (CDJ)": {
            "author": "McKinsey & Company (David Court et al., 2009)",
            "stages": [
                "Initial Consideration",
                "Active Evaluation",
                "Moment of Purchase",
                "Post-Purchase Experience",
                "Loyalty Loop",
            ],
            "key_insight": (
                "Challenges the linear funnel model. Key findings: (1) Brands in the "
                "initial consideration set are 3x more likely to be purchased. "
                "(2) Consumers can ADD brands during active evaluation, not just narrow down. "
                "(3) The 'loyalty loop' allows satisfied customers to bypass evaluation "
                "entirely and repurchase directly. (4) Touch points during active evaluation "
                "are 2-3x more influential than during initial consideration. "
                "Database covers 125,000+ journeys across 350 brands in 30 industries."
            ),
        },
        "Kotler 5A (Marketing 4.0)": {
            "author": "Philip Kotler, Hermawan Kartajaya, Iwan Setiawan (2017)",
            "stages": ["Aware", "Appeal", "Ask", "Act", "Advocate"],
            "key_insight": (
                "Not a fixed funnel; customers can enter at any stage and spiral back. "
                "The ultimate goal is 'Advocate' - turning customers into active promoters. "
                "Acknowledges social influence at every stage. In the connected economy, "
                "the path from Aware to Advocate can be accelerated by community influence, "
                "making word-of-mouth critical at all stages."
            ),
        },
        "RACE (Smart Insights)": {
            "author": "Dave Chaffey / Smart Insights (2010)",
            "stages": ["Reach", "Act", "Convert", "Engage"],
            "key_insight": (
                "Practical digital marketing framework. Each stage has clear KPIs: "
                "Reach (unique visitors, impressions, fans), Act (bounce rate, pages/visit, "
                "goal completions), Convert (sales, revenue, AOV, profit), "
                "Engage (repeat purchases, satisfaction, advocacy rate). "
                "Preceded by a 'Plan' phase for strategy and objective setting."
            ),
        },
        "Forrester Customer Lifecycle": {
            "author": "Forrester Research",
            "stages": ["Discover", "Explore", "Buy", "Engage"],
            "key_insight": (
                "Puts the customer at center. Emphasizes that 'Discover' can be active "
                "or passive. The 'Engage' phase is ongoing and post-purchase, recognizing "
                "that the brand experience continues indefinitely. Ditch the funnel metaphor "
                "in favor of a lifecycle that has no fixed end point."
            ),
        },
        "Binet_and_Field": {
            "author": "Les Binet & Peter Field (IPA, 2013+)",
            "key_insight": (
                "Not a funnel model per se, but the most important budget allocation "
                "framework. Based on IPA Databank analysis of 996+ campaigns: "
                "(1) Optimal split is ~60% brand building / 40% activation for consumer brands. "
                "(2) Brand building and activation are fundamentally different jobs that "
                "should NOT be combined in the same creative. "
                "(3) Brand effects compound over time; activation effects decay within days. "
                "(4) 60/40 is not an iron rule - it varies by category, brand maturity, "
                "price point, and competitive position. "
                "(5) For B2B: new brands need 65% activation / 35% brand initially, "
                "but mature B2B leaders should shift to 72% brand / 28% activation. "
                "(6) Premium brands may need 70:30 favoring brand building. "
                "(7) Emotional campaigns produce larger long-term effects; rational "
                "campaigns drive stronger short-term activation."
            ),
        },
        "Byron_Sharp_How_Brands_Grow": {
            "author": "Byron Sharp / Ehrenberg-Bass Institute (2010)",
            "key_insight": (
                "Challenges traditional funnel thinking. Key laws: "
                "(1) Growth comes primarily from acquiring new/light buyers, not loyalty. "
                "(2) Mental availability (brand salience in buying situations) and "
                "physical availability (ease of finding/buying) are the two growth drivers. "
                "(3) Brands should target EVERYONE in the category, not niche segments. "
                "(4) Distinctive brand assets (colors, logos, jingles) matter more than "
                "differentiated positioning. (5) Continuous advertising is better than "
                "bursts/flights - stop-start causes brand memory decay. "
                "(6) Loyalty is mostly a statistical artifact of penetration (Double Jeopardy Law). "
                "Implication for media planning: prioritize REACH over frequency, "
                "maintain always-on presence, use broad targeting, invest in distinctive "
                "creative assets rather than complex messaging hierarchies."
            ),
        },
    },
}

FUNNEL_STAGE_DEEP_KNOWLEDGE = {

    "Consciência (Awareness)": {
        "theoretical_alignment": {
            "AIDA": "Attention - capturing cognitive attention in a crowded media landscape",
            "STDC": "See - the largest qualified audience with no commercial intent yet",
            "McKinsey_CDJ": "Building the Initial Consideration Set - brands considered first are 3x more likely to be purchased",
            "Kotler_5A": "Aware - consumers learn about the brand through advertising, WOM, or past experience",
            "RACE": "Reach - building audience through SEO, content, social, paid media",
            "Forrester": "Discover - active or passive brand discovery across touchpoints",
            "Byron_Sharp": "Building Mental Availability - creating and refreshing memory structures linked to buying situations",
            "Binet_Field": "Brand Building territory - emotional, broad-reach, fame-creating campaigns",
        },
        "metric_interpretation": {
            "meaningful_metrics": {
                "primary": [
                    "Reach (unique users exposed)",
                    "Brand Lift (measured via surveys or platform studies)",
                    "Ad Recall Lift",
                    "CPM (cost efficiency of exposure)",
                    "Share of Voice (competitive presence)",
                ],
                "secondary": [
                    "Frequency (controlled at 1.5-3.0x; 4+ generates fatigue but also deepens recall)",
                    "Video completion rate (for video-first campaigns)",
                    "New visitor rate (% first-time site visitors from campaign)",
                    "Branded search volume increase (halo effect indicator)",
                ],
            },
            "vanity_metrics_warning": (
                "At the awareness stage, CPA, ROAS, and direct conversion metrics are almost "
                "always VANITY metrics. Measuring awareness campaigns by conversion is the most "
                "destructive error in digital marketing (Kaushik). Brand effects take 6+ months "
                "to fully materialize in business outcomes (Binet & Field). Using bottom-funnel "
                "metrics to judge top-funnel campaigns will systematically underinvest in brand "
                "building and cause long-term growth decline."
            ),
            "benchmarks": {
                "frequency": "4+ exposures generate highest brand recall lift; 8-12 total exposures create lasting recall. Weekly frequency of 2-4x recommended as starting point.",
                "brand_lift": "3-15% lift depending on category, creative quality, and media weight. Podcast ads specifically can increase awareness by 13 percentage points.",
                "video_views": "Viewers seeing ads 5-7 times are up to 8x more likely to convert later than single-exposure audiences (mere exposure effect).",
                "cpm_brazil": "Meta Ads CPM in Brazil: $1.77-$5.26 range (70-94% below global benchmark). Significant cost advantage for brand building.",
            },
        },
        "budget_allocation": {
            "binet_field_guidance": (
                "Awareness falls squarely in the BRAND BUILDING category of Binet & Field's framework. "
                "This is where the 60% (of the 60/40 rule) should be concentrated. "
                "Brand building campaigns should be: emotional rather than rational, broadly targeted, "
                "using mass-reach channels, with creative focused on fame and distinctiveness rather "
                "than product features or calls-to-action."
            ),
            "funnel_budget_split": (
                "Common frameworks suggest: "
                "60-30-10 split (60% awareness, 30% mid-funnel, 10% bottom-funnel) as a starting template. "
                "Fospha research: top-performing brands allocate only 10% to bottom funnel while 25% goes "
                "to awareness and consideration. "
                "Growth-stage companies: 40-50% upper funnel. "
                "New market entrants: 50-60% upper funnel to establish baseline awareness. "
                "Full-funnel approach shows up to 45% increase in ROI vs single-stage campaigns."
            ),
        },
        "creative_and_messaging": {
            "psychological_principles": {
                "mere_exposure_effect": (
                    "Repeated exposure to a stimulus breeds familiarity, and familiarity breeds liking. "
                    "The effect increases perceptual fluency (ease of processing), which creates positive "
                    "affect. Top-of-funnel campaigns generating 'flyby impressions' are effective through "
                    "this mechanism even if they don't drive immediate action. However, the relationship "
                    "follows an inverted U-shape: initial exposures increase liking, but EXCESSIVE exposure "
                    "eventually decreases it (ad fatigue)."
                ),
                "cognitive_load_theory": (
                    "People prefer simple stimuli that require low mental effort. Awareness creative should "
                    "minimize cognitive load: simple messaging, clear brand assets, no complex product details. "
                    "Visual clutter causes cognitive strain and undermines brand memory formation. "
                    "One core message per creative. The brain processes visual information 60,000x faster "
                    "than text - prioritize visual storytelling."
                ),
                "cialdini_applicable": [
                    "Social Proof - show popularity, market presence, user counts",
                    "Liking - use relatable characters, aspirational lifestyles, humor",
                    "Authority - expert endorsements, industry leadership signals",
                ],
            },
            "content_strategy": (
                "Video content dominates awareness: 88% of marketers say video improved ROI. "
                "96% of viewers rely on videos to learn about products. Short-form video gets "
                "2.5x more engagement than long-form on social platforms. "
                "Emotional storytelling with narrative arc (relatable characters, conflict, resolution) "
                "is most effective. Music and visual elements enhance brand recall. "
                "Creative should be branded early (within first 3 seconds for video) with "
                "distinctive brand assets per Byron Sharp."
            ),
            "format_recommendations": [
                "Video (6-15s for social, 15-30s for YouTube/CTV)",
                "Carousel with brand story progression",
                "High-impact display (takeover, interstitial)",
                "Audio ads (podcast, music streaming)",
                "Influencer content (branded entertainment)",
            ],
        },
        "platform_stage_alignment": {
            "YouTube": {
                "why": (
                    "75% of people say YouTube ads make them more aware of new brands. "
                    "70% said they bought a brand after seeing it on YouTube. Non-skippable bumper "
                    "ads (6s) are ideal for frequency-building. TrueView for reach maximizes unique "
                    "audience. YouTube also provides robust Brand Lift Studies for measurement."
                ),
                "best_formats": "Bumper Ads, TrueView In-Stream, Masthead",
            },
            "Meta (Instagram/Facebook)": {
                "why": (
                    "Video ads increase brand awareness by up to 57% (Meta internal research). "
                    "Massive reach in Brazil (Instagram: 92% of internet users, Facebook: 81.5%). "
                    "Low CPMs in Brazil ($1.77-$5.26). Advanced lookalike audiences for efficient "
                    "broad targeting. Reels format drives high engagement for awareness."
                ),
                "best_formats": "Reels, Stories, Video Feed Ads, Carousel",
            },
            "TikTok": {
                "why": (
                    "91.7 million users aged 18+ in Brazil (early 2025). Short-form video native "
                    "format maximizes mere exposure effect. Highest organic virality potential. "
                    "Algorithm favors content discovery over follower graphs, making it ideal for "
                    "reaching new audiences. Gen Z and young millennials heavily indexed."
                ),
                "best_formats": "In-Feed Video, TopView, Branded Hashtag Challenge",
            },
            "Programmatic/Display": {
                "why": (
                    "77% of Brazil digital ad revenue will be programmatic by 2028. "
                    "Enables massive reach across thousands of publishers. Advanced frequency "
                    "capping across channels. DV360/Trade Desk enable cross-platform reach/frequency "
                    "management. Good for complementing social reach with web reach."
                ),
                "best_formats": "Rich Media, Video Pre-roll, High-impact skins, CTV/OTT",
            },
        },
        "common_mistakes": {
            "measuring_with_wrong_metrics": (
                "Judging awareness campaigns by CPA or ROAS. This is the #1 mistake per Kaushik, "
                "Binet & Field, and Sharp. Brand effects take months to materialize in sales data. "
                "This leads to systematic underinvestment in brand building."
            ),
            "frequency_mismanagement": (
                "Either too low (1-2x, insufficient for recall) or too high (>8x without creative "
                "rotation, causing ad fatigue). The inverted U-shape of the mere exposure effect means "
                "there is an optimal exposure window."
            ),
            "targeting_too_narrow": (
                "Byron Sharp's research shows brands grow by reaching light and non-buyers. "
                "Over-segmentation at awareness stage limits reach and increases CPM. "
                "95% of potential customers aren't ready to buy now (LinkedIn B2B Institute), "
                "but need to be in the mental consideration set for future purchases."
            ),
            "product_focused_messaging": (
                "Using product-feature messaging for an audience with no category intent. "
                "Awareness creative should focus on emotion, brand story, and distinctive assets, "
                "not specifications or pricing. Binet & Field show emotional campaigns outperform "
                "rational ones for long-term brand effects."
            ),
            "stop_start_advertising": (
                "Byron Sharp: millions wasted on burst campaigns that dissipate into silence. "
                "Evidence shows continuous always-on advertising maintains mental availability "
                "better than intermittent heavy flights."
            ),
            "ignoring_upper_funnel": (
                "Over-investing in bottom-funnel conversion while neglecting awareness. "
                "This ignores 95% of potential customers who aren't ready to buy yet. "
                "Creates a 'leaky funnel' where the brand fails to feed new prospects."
            ),
        },
        "brazil_specifics": {
            "market_data": (
                "Social Media concentrated 53% of all digital ad investment in Brazil (2024). "
                "Meta Ads CPM in Brazil averages 70-94% below global benchmark - exceptional "
                "cost efficiency for awareness campaigns. "
                "Brazil digital ad market: R$37.9 billion in 2024, 8% YoY growth. "
                "Mobile represents 56.88% of digital ad spend. "
                "Instagram reaches 92% of Brazilian internet users - dominant awareness platform. "
                "WhatsApp reaches 93.7% but is primarily a mid/bottom funnel tool."
            ),
            "cultural_considerations": (
                "Brazilian consumers respond strongly to emotional, humorous, and music-driven content. "
                "Carnival and Independence Day periods see increased social activity and higher CPMs. "
                "Influencer marketing is deeply embedded in Brazilian culture - consider creator "
                "partnerships for awareness. Gen Z in Brazil is heavily TikTok-native."
            ),
            "platform_penetration": {
                "WhatsApp": "93.7% of internet users",
                "Instagram": "92% of internet users",
                "Facebook": "81.5% of internet users",
                "TikTok": "63.9% of internet users (91.7M users 18+)",
                "YouTube": "144 million users",
                "Telegram": "57.1% of internet users",
            },
        },
    },

    "Interesse": {
        "theoretical_alignment": {
            "AIDA": "Interest - the prospect begins to engage with the brand message and explores further",
            "STDC": "Transition between See and Think - audience is curious but not yet evaluating solutions",
            "McKinsey_CDJ": "Strengthening the Initial Consideration Set - ensuring the brand stays top-of-mind during passive absorption",
            "Kotler_5A": "Appeal - the brand creates curiosity and attraction; consumers are intrigued",
            "RACE": "Act - first interactions, clicking through, engaging with content",
            "Forrester": "Early Explore - beginning multichannel research",
            "Byron_Sharp": "Reinforcing Mental Availability through category entry points and distinctive assets",
            "Binet_Field": "Overlap zone between brand building and activation - content should lean emotional/educational",
        },
        "metric_interpretation": {
            "meaningful_metrics": {
                "primary": [
                    "CTR (Click-Through Rate) - indicates creative relevance and audience curiosity",
                    "Engagement Rate - depth of interaction with content",
                    "CPC (Cost Per Click) - efficiency of generating interest",
                    "Video Completion Rate / ThruPlay - genuine content consumption",
                ],
                "secondary": [
                    "Time on site / page (quality of traffic generated)",
                    "Pages per session (content exploration depth)",
                    "Bounce rate (inverse indicator - lower is better)",
                    "Saves/Bookmarks (strong future intent signal)",
                    "Shares (virality and content resonance)",
                    "Return visit rate (ongoing interest)",
                ],
            },
            "vanity_metrics_warning": (
                "At the interest stage, raw click volume without quality context is a vanity metric. "
                "1,000 clicks that bounce immediately are worth less than 100 clicks that spend "
                "3 minutes on site. Always pair CTR with post-click behavior metrics. "
                "Similarly, high engagement rate on social posts that doesn't translate to any "
                "site visits or deeper exploration may indicate entertainment without brand connection."
            ),
            "benchmarks": {
                "ctr": "Meta: 1.5%+ strong for ecommerce. TikTok in-feed: 1.5-3%. Search: 3-8%. Display: 0.3-1%. Improvement over awareness-stage CTR (0.3-1.5%) expected.",
                "engagement_rate": "1-5% on social media considered healthy. >3% is strong. Rate should be measured on reach, not impressions.",
                "video_completion": "15-40% completion rate for ThruPlay (15s+). Higher indicates genuine content interest.",
                "time_on_page": "30s-2min for landing pages. >2 pages per session indicates strong exploration.",
                "cpc_brazil": "Meta Brazil ecommerce CPC averaged $0.38 (66% lower than global $1.14). Google Ads Brazil varies: $1-8 depending on industry.",
            },
        },
        "budget_allocation": {
            "binet_field_guidance": (
                "Interest stage sits in the overlap between brand building and activation. "
                "Content should be primarily educational/entertaining (brand building character) "
                "but can include soft CTAs for deeper engagement (activation character). "
                "This is where the 60/40 split starts to blend."
            ),
            "funnel_budget_split": (
                "Within the 'mid-funnel' allocation (typically 20-30% of total budget), "
                "interest-stage activities compete with consideration. Interest campaigns "
                "should receive roughly 10-15% of total budget. For new brands building "
                "initial audience, this may increase to 15-20%."
            ),
        },
        "creative_and_messaging": {
            "psychological_principles": {
                "curiosity_gap": (
                    "Content that opens a knowledge gap drives clicks and engagement. "
                    "Headlines and hooks should promise value without fully delivering it, "
                    "compelling the audience to click/watch to resolve the gap."
                ),
                "cognitive_load_theory": (
                    "At the interest stage, audiences tolerate slightly more cognitive load than "
                    "awareness but still prefer scannable, visual content. Educational content "
                    "should use progressive disclosure - reveal complexity gradually."
                ),
                "cialdini_applicable": [
                    "Commitment/Consistency - small initial engagements (downloading a guide, signing up for newsletter) increase likelihood of future conversion",
                    "Social Proof - engagement counts, testimonials, 'trending' signals",
                    "Liking - relatable content, brand personality expression",
                ],
            },
            "content_strategy": (
                "Educational, entertaining, or problem-solving content resonates most. "
                "Blog posts, how-to guides, short videos, infographics that highlight how "
                "the product/service addresses pain points. Webinars, newsletters, and "
                "interactive content like quizzes drive deeper engagement. "
                "Content should demonstrate expertise without being overtly promotional."
            ),
            "format_recommendations": [
                "Short-form educational video (15-60s)",
                "Carousel posts with tips/insights",
                "Blog content promoted via social/display",
                "Interactive content (quizzes, calculators, polls)",
                "Email newsletter sign-up campaigns",
                "Podcast sponsorship/creator collaborations",
            ],
        },
        "platform_stage_alignment": {
            "Meta (Instagram/Facebook)": {
                "why": (
                    "Traffic and engagement campaign objectives are well-optimized. "
                    "Instagram's carousel and Reels formats encourage content consumption. "
                    "Cost-efficient clicks in Brazil ($0.38 CPC). Lookalike audiences of "
                    "engagers refine targeting beyond broad awareness."
                ),
                "best_formats": "Carousel, Reels, Stories with swipe-up, Collection Ads",
            },
            "Google Ads (Display/Discovery)": {
                "why": (
                    "Discovery campaigns reach users browsing content across Gmail, YouTube, "
                    "and Discover feed - ideal for interest-stage content distribution. "
                    "Display network enables broad but contextually relevant reach. "
                    "Responsive display ads auto-optimize creative combinations."
                ),
                "best_formats": "Discovery Ads, Responsive Display Ads, Gmail Ads",
            },
            "TikTok": {
                "why": (
                    "Native content format encourages exploration and sharing. "
                    "Algorithm surfaces content to interested users regardless of follower count. "
                    "Spark Ads allow promoting organic content that already demonstrated engagement. "
                    "Strong for educational/entertaining content that builds brand affinity."
                ),
                "best_formats": "In-Feed Video, Spark Ads (boosted organic), Branded Effects",
            },
            "Content platforms (blogs, Medium, LinkedIn)": {
                "why": (
                    "Long-form content platforms are ideal for deeper interest engagement. "
                    "SEO-optimized content provides sustainable organic interest generation. "
                    "LinkedIn is particularly effective for B2B interest-stage content."
                ),
                "best_formats": "Sponsored articles, Thought leadership posts, LinkedIn Carousel documents",
            },
        },
        "common_mistakes": {
            "traffic_without_quality": (
                "Optimizing for clicks without monitoring post-click behavior. "
                "High click volume with 90%+ bounce rate indicates creative/landing page mismatch "
                "or irrelevant audience targeting."
            ),
            "landing_page_misalignment": (
                "Ad creative promises one thing, landing page delivers another. "
                "The transition from ad to destination must be seamless in messaging, "
                "visual design, and value proposition."
            ),
            "skipping_to_conversion": (
                "Trying to sell before the prospect has developed sufficient interest. "
                "Premature conversion CTAs in interest-stage campaigns create friction "
                "and reduce overall campaign effectiveness."
            ),
            "generic_content": (
                "Producing self-promotional content instead of genuinely useful/entertaining material. "
                "Interest-stage content should provide value first, brand association second."
            ),
            "no_next_step": (
                "Generating interest with no clear path to deepen engagement. "
                "Every interest touchpoint should have a natural next step toward consideration."
            ),
        },
        "brazil_specifics": {
            "market_data": (
                "Brazil's CPC on Meta is 66% lower than global average - excellent value for "
                "traffic and engagement campaigns. Social media represents 53% of digital ad spend. "
                "Search advertising is the largest digital segment (R$4.1B in 2024). "
                "Short-form video consumption extremely high - Reels and TikTok dominate "
                "interest-stage content consumption."
            ),
            "cultural_considerations": (
                "Brazilian audiences heavily engage with storytelling and personality-driven content. "
                "Creator/influencer content drives higher engagement than brand-produced content. "
                "Portuguese-language content with local cultural references significantly "
                "outperforms translated international content. "
                "Mobile-first consumption: 76% of digital ad consumption will be mobile by 2028."
            ),
        },
    },

    "Consideração": {
        "theoretical_alignment": {
            "AIDA": "Desire - building preference and evaluating alternatives",
            "STDC": "Think - actively considering category solutions, researching and comparing",
            "McKinsey_CDJ": "Active Evaluation - the critical phase where brands are added or removed from consideration. Touch points here are 2-3x more influential than during initial consideration.",
            "Kotler_5A": "Ask - consumers actively research, ask peers, read reviews, compare options",
            "RACE": "Late Act / early Convert - engaged visitors evaluating the offering",
            "Forrester": "Deep Explore - multi-channel research about brand and competitors",
            "Byron_Sharp": "Physical Availability becoming critical - brand must be findable when actively searched",
            "Binet_Field": "Activation territory begins - rational messaging about features/benefits becomes more appropriate",
        },
        "metric_interpretation": {
            "meaningful_metrics": {
                "primary": [
                    "CTR (higher expected at this stage: 1-3%)",
                    "Engagement quality metrics (comments, saves, shares)",
                    "Time on product/comparison pages",
                    "Content consumption depth (white papers, case studies, demos viewed)",
                    "Micro-conversions (newsletter signup, wishlist adds, quote requests)",
                ],
                "secondary": [
                    "Return visit rate (multi-session evaluation)",
                    "Pages per session on product/solution pages",
                    "Video completion rate for product demos",
                    "Remarketing audience growth rate",
                    "Search query branded terms increase",
                ],
            },
            "vanity_metrics_warning": (
                "At consideration stage, surface-level engagement (likes, reactions) without "
                "deeper evaluation behavior is a vanity metric. Someone who likes a post but "
                "never visits the product page is not truly in consideration. Focus on evaluation "
                "behaviors: comparison page visits, spec sheet downloads, demo requests, "
                "review reading. B2B buyers interact with 3-7 content pieces before talking to sales."
            ),
            "benchmarks": {
                "ctr": "1.0-3.0% expected for consideration campaigns. Higher than awareness (0.3-1.5%) because audience has intent.",
                "micro_conversion": "Consideration micro-conversion rates: 2-5% for content downloads, 1-3% for webinar registrations, 5-15% for email signups.",
                "nurturing_impact": "Companies with effective nurturing have 50% more sales-ready leads at 33% lower cost. Nurtured leads spend 47% more than non-nurtured leads.",
                "content_consumption": "B2B: 3-7 content pieces consumed before sales conversation. B2C: 2-4 touchpoints typical before purchase decision.",
            },
        },
        "budget_allocation": {
            "binet_field_guidance": (
                "Consideration stage is firmly in ACTIVATION territory per Binet & Field. "
                "This is where the 40% (of 60/40) begins to concentrate. Messaging can be "
                "more rational, feature-focused, and directly comparative. However, maintain "
                "emotional elements to sustain the brand halo built in awareness."
            ),
            "funnel_budget_split": (
                "Consideration typically receives 15-25% of total budget. "
                "Within mid-funnel (combined interest + consideration), consideration "
                "should receive the majority share because these audiences are closer to "
                "conversion. Remarketing budgets for consideration-stage audiences "
                "are typically the most efficient spend in the funnel."
            ),
        },
        "creative_and_messaging": {
            "psychological_principles": {
                "social_proof": (
                    "At consideration, social proof becomes the dominant persuasion mechanism. "
                    "Testimonials, case studies, review scores, user counts, and peer "
                    "endorsements directly address the evaluation mindset. "
                    "People follow what others are doing - show that others have chosen your solution."
                ),
                "authority": (
                    "Expert endorsements, certifications, awards, and thought leadership "
                    "content establish credibility during the evaluation phase. "
                    "Third-party validation is more persuasive than brand claims."
                ),
                "cialdini_applicable": [
                    "Social Proof - reviews, testimonials, case studies, user counts (primary)",
                    "Authority - expert endorsements, certifications, awards, media mentions",
                    "Commitment/Consistency - free trials, samples, low-risk first steps",
                    "Liking - customer stories that prospects can relate to",
                ],
            },
            "content_strategy": (
                "Comparative content, detailed product demos, customer testimonials, "
                "case studies with measurable results. Webinars, buying guides, ROI calculators. "
                "Content should directly address objections and demonstrate competitive advantages. "
                "Format should accommodate deeper engagement - longer video, detailed pages."
            ),
            "format_recommendations": [
                "Product demo videos (60s-3min)",
                "Customer testimonial videos/carousels",
                "Comparison guides and infographics",
                "Webinar/live session ads",
                "Remarketing ads with social proof",
                "Case study carousel or document ads",
                "Interactive product configurators/calculators",
            ],
        },
        "platform_stage_alignment": {
            "Google Ads (Search)": {
                "why": (
                    "Search captures active evaluation intent. Users researching 'best [product]', "
                    "'[product] vs [competitor]', '[product] reviews' are in consideration. "
                    "Search is a 'pull' channel connecting with individuals actively seeking solutions. "
                    "Conversion rates for search: 3.75% vs 0.77% for display."
                ),
                "best_formats": "Search Ads (category and comparison keywords), Responsive Search Ads",
            },
            "YouTube": {
                "why": (
                    "Product review and comparison videos are the #2 content category on YouTube. "
                    "Longer format allows detailed product demonstration. "
                    "YouTube ads with product demos drive consideration intent. "
                    "TrueView In-Stream only charges for engaged views (30s+ or completion)."
                ),
                "best_formats": "TrueView In-Stream, Video Discovery Ads (appears in search results)",
            },
            "Meta (Instagram/Facebook)": {
                "why": (
                    "Remarketing to website visitors and engagers is highly efficient. "
                    "Dynamic ads can show relevant products based on browsing behavior. "
                    "Carousel format allows multi-feature or multi-product comparison. "
                    "Lead ads capture consideration-stage data without leaving the platform."
                ),
                "best_formats": "Remarketing campaigns, Dynamic Ads, Lead Ads, Carousel",
            },
            "LinkedIn (B2B)": {
                "why": (
                    "Professional ecosystem where decision-makers actively evaluate solutions. "
                    "Thought Leadership Ads see engagement rates 5-10x higher than company "
                    "sponsored content. Combining job title + industry + company size enables "
                    "precise ICP targeting. Document ads allow sharing case studies natively."
                ),
                "best_formats": "Thought Leadership Ads, Document Ads, Sponsored Content, Conversation Ads",
            },
        },
        "common_mistakes": {
            "treating_all_leads_alike": (
                "Companies often use generic mid-funnel content that misses specific industries, "
                "roles, or pain points. Half of qualified leads aren't ready to buy immediately - "
                "segmented nurturing is critical. Personalized content performs 3.2x better."
            ),
            "skipping_to_conversion": (
                "Pushing for purchase before the prospect has fully evaluated. "
                "This is especially damaging in B2B where decision cycles are long. "
                "The consideration stage cannot be rushed."
            ),
            "no_remarketing_strategy": (
                "Failing to build and activate remarketing audiences from awareness campaigns. "
                "Website visitors who engaged with awareness content are the highest-value "
                "consideration audience. Not retargeting them wastes the awareness investment."
            ),
            "lack_of_content_variety": (
                "Showing the same message repeatedly without progressing the narrative. "
                "Consideration audiences need different content pieces that address different "
                "aspects of their evaluation: features, pricing, testimonials, case studies, "
                "implementation support, etc."
            ),
            "poor_followup": (
                "Creating great mid-funnel content but failing to follow up. "
                "Without strategic follow-ups, leads lose interest or choose competitors. "
                "Half of qualified leads aren't ready to buy immediately, making nurturing crucial."
            ),
        },
        "brazil_specifics": {
            "market_data": (
                "Search advertising is the largest digital ad segment in Brazil (R$4.1B in 2024). "
                "Google Ads CPC in Brazil varies by industry: marketing/advertising at $4.22. "
                "WhatsApp is increasingly used for consideration-stage conversations - "
                "95% of brand-consumer digital interactions occur on WhatsApp. "
                "Retail Media grew 41% YoY to R$3.5B - product listing ads are key "
                "consideration touchpoints on marketplace platforms."
            ),
            "cultural_considerations": (
                "Brazilian consumers heavily rely on peer recommendations and influencer opinions "
                "during consideration. WhatsApp groups and Instagram comments serve as social "
                "proof channels. Review culture is growing but less mature than US/EU markets. "
                "Price comparison is deeply embedded in Brazilian shopping behavior - "
                "comparison content performs very well."
            ),
        },
    },

    "Intenção": {
        "theoretical_alignment": {
            "AIDA": "Late Desire / early Action - the prospect has decided to act and is choosing where/how",
            "STDC": "Late Think / early Do - commercial intent is forming but transaction hasn't occurred",
            "McKinsey_CDJ": "Moment of Purchase approaching - the consumer is narrowing to final selection",
            "Kotler_5A": "Late Ask / early Act - the decision is nearly made, the prospect is looking for the final confirmation",
            "RACE": "Early Convert - the prospect is demonstrating purchase signals",
            "Forrester": "Late Explore / early Buy - evaluating final purchase conditions",
            "Byron_Sharp": "Physical Availability is paramount - the brand MUST be easily purchasable when intent forms",
            "Binet_Field": "Pure Activation territory - short-term, rational, action-driving messaging",
        },
        "metric_interpretation": {
            "meaningful_metrics": {
                "primary": [
                    "Leads Generated (qualified leads entering pipeline)",
                    "Cost Per Lead (CPL) - efficiency of lead capture",
                    "Lead-to-opportunity conversion rate",
                    "Form completion rate",
                    "Demo/trial request rate",
                ],
                "secondary": [
                    "Lead quality score (SQL vs MQL ratio)",
                    "Time from lead to first contact",
                    "Cart creation rate (ecommerce)",
                    "Pricing page visits",
                    "Search impression share on high-intent keywords",
                ],
            },
            "vanity_metrics_warning": (
                "At the intent stage, lead VOLUME without quality assessment is misleading. "
                "100 leads at $5 CPL that never convert are worth less than 10 leads at $50 CPL "
                "that close at 30%. Always track CPL alongside lead quality metrics (SQL rate, "
                "pipeline conversion rate). Similarly, cart additions without checkout completion "
                "indicate friction in the conversion path, not true intent."
            ),
            "benchmarks": {
                "lead_conversion": "Average conversion rate for Google Ads B2B: 3.04%. With intent data targeting: significantly higher. 94% of B2B marketers say lead conversion rates increase with intent data.",
                "high_intent_keywords": "Bottom-funnel keywords (buy, order, price, demo, trial) have highest CPC but also highest conversion rates. Search ads: 3.75% conversion vs display's 0.77%.",
                "retargeting_performance": "Retargeting campaigns using behavioral intent signals (pages viewed, time on site, form starts) significantly outperform cold targeting.",
            },
        },
        "budget_allocation": {
            "binet_field_guidance": (
                "Intent stage is PURE ACTIVATION per Binet & Field. This is the core of the "
                "40% activation budget. Messaging should be direct, rational, benefit-focused "
                "with clear calls-to-action. Short-term ROI measurement is appropriate here."
            ),
            "funnel_budget_split": (
                "Intent typically receives 10-20% of total budget. "
                "This is often the highest-ROAS spend in the funnel because audiences "
                "have demonstrated purchase signals. However, this pool is limited by "
                "how much awareness/interest/consideration investment generated intent. "
                "Underfunding upper funnel = smaller intent audience = less to spend here."
            ),
        },
        "creative_and_messaging": {
            "psychological_principles": {
                "scarcity": (
                    "When people believe something is in short supply, they want it more. "
                    "Limited-time offers, countdown timers, and limited availability messaging "
                    "accelerate intent to action. Most powerful at this stage because the "
                    "prospect already wants to buy - scarcity provides the urgency to act NOW."
                ),
                "reciprocity": (
                    "People tend to return a favor. Free trials, demos, consultations, and "
                    "exclusive content at the intent stage create a sense of obligation. "
                    "The prospect receives value and feels compelled to reciprocate with purchase."
                ),
                "cialdini_applicable": [
                    "Scarcity - limited time, limited availability, exclusive offers (primary at this stage)",
                    "Reciprocity - free trials, consultations, exclusive previews",
                    "Commitment/Consistency - trial-to-purchase, small-to-large escalation",
                    "Social Proof - conversion-oriented testimonials ('I bought and here's my result')",
                ],
            },
            "content_strategy": (
                "Direct-response content: lead magnets, free trial offers, demo scheduling, "
                "pricing information, competitive comparisons with clear winner positioning. "
                "Landing pages with short forms (3-5 fields max for initial capture). "
                "Urgency-driven messaging with clear value propositions. "
                "Remarketing aggressive for site visitors who viewed pricing/product pages."
            ),
            "format_recommendations": [
                "Search ads on high-intent keywords (buy, price, demo, trial)",
                "Lead generation forms (Meta Lead Ads, LinkedIn Lead Gen Forms)",
                "Remarketing ads with strong CTAs and offers",
                "Landing pages optimized for conversion",
                "Shopping ads (for ecommerce)",
                "WhatsApp click-to-chat ads (Brazil-specific high performer)",
            ],
        },
        "platform_stage_alignment": {
            "Google Ads (Search)": {
                "why": (
                    "THE dominant intent-capture platform. Users actively searching with "
                    "commercial intent (transactional keywords). Search ads convert at "
                    "3.75-4.40% across industries - highest of any ad format. "
                    "Search is 'pull' marketing - you capture existing intent rather than "
                    "creating it. Keyword targeting on 'buy', 'price', 'near me', 'best' "
                    "captures bottom-funnel demand."
                ),
                "best_formats": "Search Ads, Shopping Ads, Local Service Ads",
            },
            "Meta Ads (Lead Ads)": {
                "why": (
                    "Lead Ads capture intent without leaving the platform, reducing friction. "
                    "Pre-filled forms using Facebook profile data increase completion rates. "
                    "Retargeting website visitors who showed intent signals "
                    "(product page views, cart additions) is highly efficient."
                ),
                "best_formats": "Lead Ads, Conversion-optimized ads, Dynamic Product Ads",
            },
            "LinkedIn (B2B Lead Gen)": {
                "why": (
                    "Lead Gen Forms pre-populate with professional data (title, company, email). "
                    "InMail campaigns reach decision-makers directly. "
                    "B2B intent signals (content download, webinar attendance) can be tracked. "
                    "Higher CPL but typically higher lead quality for B2B."
                ),
                "best_formats": "Lead Gen Forms, Sponsored InMail, Conversation Ads",
            },
            "WhatsApp (Brazil-specific)": {
                "why": (
                    "WhatsApp converts 6x more than traditional ecommerce in Brazil. "
                    "93.7% penetration means it's the most accessible intent-capture channel. "
                    "Click-to-WhatsApp ads on Meta + conversational commerce = frictionless intent capture. "
                    "Average recovered cart value: R$557.67 (432% increase from 2023). "
                    "AI chatbots handle 80% of commercial conversations without human intervention."
                ),
                "best_formats": "Click-to-WhatsApp Ads, WhatsApp Business API campaigns",
            },
        },
        "common_mistakes": {
            "forms_too_long": (
                "Every additional form field reduces completion rate by 5-10%. "
                "Intent-stage lead forms should capture minimum viable data (name, email, "
                "phone) and qualify through follow-up, not upfront."
            ),
            "slow_followup": (
                "Lead response time is critical. Leads contacted within 5 minutes are "
                "9x more likely to convert than those contacted after 30 minutes. "
                "Automation for immediate response is essential."
            ),
            "cpl_without_quality": (
                "Optimizing for lowest CPL without tracking downstream conversion. "
                "Cheap leads that never convert waste sales resources. "
                "Track CPL alongside SQL rate and pipeline conversion."
            ),
            "missing_search_presence": (
                "If the brand isn't present on Google when prospects search with intent, "
                "competitors capture that demand. Search impression share on high-intent "
                "keywords should be monitored - losing impression share means losing intent."
            ),
            "ignoring_cart_abandonment": (
                "Average cart abandonment rate is 70%. Not having automated recovery "
                "sequences (email, WhatsApp, retargeting) leaves massive revenue on the table."
            ),
        },
        "brazil_specifics": {
            "market_data": (
                "WhatsApp marketing campaigns grew 64% in volume in 2024, reaching 59.2M messages. "
                "WhatsApp conversion rate: 55% (vs traditional ecommerce). "
                "Only 40% of Brazilian companies use automated WhatsApp campaigns - opportunity gap. "
                "Click-to-WhatsApp ads are the fastest-growing Meta ad format in Brazil. "
                "Google Ads search remains the largest digital ad segment at R$4.1B."
            ),
            "cultural_considerations": (
                "Brazilian consumers prefer personal, human interaction even in digital channels. "
                "59% of consumers dislike automated responses - balance automation with "
                "human touch. WhatsApp conversational commerce is culturally natural in Brazil. "
                "Boleto and Pix payment methods reduce friction at intent/conversion boundary. "
                "Brazilian consumers are highly price-sensitive - comparison shopping is default behavior."
            ),
        },
    },

    "Conversão/Ação": {
        "theoretical_alignment": {
            "AIDA": "Action - the final behavior, the purchase or sign-up",
            "STDC": "Do - the transaction moment, audience ready to act",
            "McKinsey_CDJ": "Moment of Purchase - closure happens, brand is chosen",
            "Kotler_5A": "Act - the consumer completes the purchase/sign-up",
            "RACE": "Convert - sales, revenue, profit generated",
            "Forrester": "Buy - purchase process, checkout experience, satisfaction with price",
            "Byron_Sharp": "Physical Availability critical - frictionless path to purchase determines success",
            "Binet_Field": "Peak Activation - short-term, rational, transaction-focused campaigns",
        },
        "metric_interpretation": {
            "meaningful_metrics": {
                "primary": [
                    "Conversions (total transactions/sign-ups)",
                    "CPA (Cost Per Acquisition)",
                    "ROAS (Return On Ad Spend)",
                    "Conversion Rate (visitors to buyers)",
                    "Revenue / Transaction Value",
                ],
                "secondary": [
                    "AOV (Average Order Value)",
                    "Cart abandonment rate (recovery opportunity)",
                    "Checkout completion rate",
                    "Cost per order vs customer lifetime value",
                    "Attribution (first-touch vs last-touch vs multi-touch)",
                ],
            },
            "vanity_metrics_warning": (
                "At conversion stage, ROAS without context is potentially misleading. "
                "High ROAS on retargeting may be taking credit for conversions that would "
                "have happened anyway (attribution problem). Very low CPA on retargeting "
                "audiences is expected - the real question is incrementality. "
                "Also beware: judging ENTIRE funnel performance by conversion-stage metrics "
                "overvalues last-touch and undervalues brand building (per Binet & Field)."
            ),
            "benchmarks": {
                "conversion_rate": "Global ecommerce average: 3.17%. Top-performing niches: 5-15%. Landing pages median: 6.6%. B2B Visitor-to-Lead: 2-5%, Opportunity-to-Closed: 15-30%.",
                "search_vs_display": "Search ads: 3.75-4.40% conversion rate. Display ads: 0.57-0.77%. Search is 5-6x more efficient at conversion.",
                "roas_targets": "ROAS targets vary: 3:1 minimum for most brands, 4:1 healthy, 6:1+ for remarketing/retention audiences. Brand awareness campaigns should NOT be measured by ROAS.",
                "cart_abandonment": "Average cart abandonment: 70%. Recovery campaigns can recapture 5-15% of abandoned carts.",
            },
        },
        "budget_allocation": {
            "binet_field_guidance": (
                "Conversion is the ultimate activation stage. The entire purpose of the 40% "
                "activation budget culminates here. However, Binet & Field's critical insight "
                "is that over-allocating to conversion at the expense of brand building "
                "creates short-term spikes but long-term decline. The conversion stage "
                "HARVESTS demand created by brand building - it cannot create demand from nothing."
            ),
            "funnel_budget_split": (
                "Conversion typically receives 10-20% of total budget. "
                "Fospha data: top-performing brands allocate only 10% to bottom funnel. "
                "Higher allocation (20-30%) is appropriate for mature brands with strong "
                "awareness and large warm audiences. For ecommerce during peak seasons "
                "(Black Friday, Christmas), temporary increase to 30-40% is common."
            ),
        },
        "creative_and_messaging": {
            "psychological_principles": {
                "scarcity_and_urgency": (
                    "Countdown timers, limited stock indicators, and time-limited offers "
                    "drive immediate action. Most effective when the prospect is already "
                    "motivated - scarcity overcomes the final hesitation."
                ),
                "social_proof_at_conversion": (
                    "At the moment of purchase, testimonials, review scores, trust badges, "
                    "and 'X people bought this today' signals reduce anxiety and confirm "
                    "the decision. Trust signals reduce conversion friction."
                ),
                "loss_aversion": (
                    "People feel losses 2x more strongly than equivalent gains. "
                    "Framing the cost of NOT acting (missing the deal, losing the opportunity) "
                    "is more motivating than framing what they gain."
                ),
                "cialdini_applicable": [
                    "Scarcity - limited time/stock (primary conversion driver)",
                    "Social Proof - reviews, trust badges, purchase counts",
                    "Reciprocity - bonus items, free shipping thresholds",
                    "Commitment/Consistency - 'complete your order' for cart abandoners",
                    "Unity - brand community belonging ('join 50,000+ customers')",
                ],
            },
            "content_strategy": (
                "Direct-response with clear CTA. Landing pages laser-focused on single action. "
                "Trust signals: testimonials, security badges, guarantee/return policy. "
                "Message-ad alignment is critical (what the ad says must match the landing page). "
                "Mobile-first optimization (60% of traffic is mobile). "
                "A/B test headlines, CTAs, and offer presentations continuously."
            ),
            "format_recommendations": [
                "Search ads with price extensions, sitelinks, review extensions",
                "Shopping ads / Product listing ads",
                "Remarketing ads for cart abandoners with product images",
                "Dynamic product ads showing viewed/carted items",
                "Landing pages with single conversion goal",
                "WhatsApp recovery messages (Brazil-specific)",
                "Email recovery sequences (abandoned cart/form)",
            ],
        },
        "platform_stage_alignment": {
            "Google Ads (Search/Shopping)": {
                "why": (
                    "Search captures the highest-intent users. Conversion rates of 3.75-4.40% "
                    "are unmatched by any other channel. Shopping ads show price, product image, "
                    "and reviews directly in SERP - reducing friction to purchase. "
                    "Performance Max campaigns optimize across Google surfaces for conversion."
                ),
                "best_formats": "Search Ads (brand + transactional terms), Shopping, Performance Max",
            },
            "Meta Ads (Conversion campaigns)": {
                "why": (
                    "Conversion objective campaigns with Advantage+ Shopping optimize across "
                    "placements for maximum purchases. Dynamic product ads show the exact "
                    "products users viewed/carted. Custom audiences of warm visitors convert "
                    "at 4-10x the rate of cold audiences."
                ),
                "best_formats": "Advantage+ Shopping, Dynamic Product Ads, Collection Ads, Conversion campaigns",
            },
            "Google Ads (Remarketing)": {
                "why": (
                    "Display remarketing captures users across millions of sites after "
                    "they've shown purchase intent. Combined with search remarketing lists "
                    "(RLSA), enables bid adjustments for known visitors. "
                    "YouTube remarketing recaptures attention through video."
                ),
                "best_formats": "RLSA, Display Remarketing, YouTube Remarketing",
            },
        },
        "common_mistakes": {
            "message_mismatch": (
                "Ad says 'Get a free audit' but landing page pushes paid consultation. "
                "This disconnect kills conversion rates. Ad-to-landing-page continuity "
                "in messaging, visuals, and offer is essential."
            ),
            "landing_page_friction": (
                "Forms with too many fields, no mobile optimization, walls of text, "
                "weak CTAs ('Submit' instead of 'Get My Free Trial'), no trust signals. "
                "40% of consumers switch to competitors after a poor mobile experience."
            ),
            "homepage_as_destination": (
                "Driving conversion traffic to homepage instead of dedicated landing pages. "
                "Landing pages should be laser-focused on a single conversion goal. "
                "Homepages have too many distractions and exit paths."
            ),
            "ignoring_attribution": (
                "Taking ROAS at face value without understanding attribution model. "
                "Last-click attribution overvalues conversion campaigns and undervalues "
                "awareness/consideration. Multi-touch attribution provides more accurate picture."
            ),
            "cold_audience_conversion": (
                "Spending conversion budget on cold audiences who have never heard of the brand. "
                "Conversion campaigns are most efficient when targeting warm, remarketing audiences. "
                "Cold conversion campaigns have 5-10x higher CPA."
            ),
            "no_testing_culture": (
                "Not A/B testing landing pages, CTAs, offers, and ad copy. "
                "Conversion optimization is a continuous process, not a one-time setup. "
                "Top brands test 10+ creative variations simultaneously."
            ),
        },
        "brazil_specifics": {
            "market_data": (
                "Brazil ecommerce Facebook Ads CPC: $0.38 (66% below global). "
                "WhatsApp converts 6x more than traditional ecommerce - critical conversion channel. "
                "Pix payment method has dramatically reduced checkout friction since 2020. "
                "Boleto bancario still relevant for unbanked/underbanked consumers. "
                "Black Friday is the biggest conversion event (note: Brazil also has its own "
                "seasonal peaks around Carnival, Children's Day Oct 12)."
            ),
            "cultural_considerations": (
                "Installment payments (parcelamento) are expected by Brazilian consumers - "
                "displaying '12x sem juros' significantly lifts conversion rates. "
                "Free shipping thresholds are a major conversion driver. "
                "CPM and CPC spike around Carnival, Independence Day, Children's Day, "
                "Black Friday, and Christmas - adjust budgets accordingly. "
                "Trust badges (Reclame Aqui reputation score, SSL certificate) are "
                "important trust signals for Brazilian consumers."
            ),
        },
    },

    "Retenção/Fidelização": {
        "theoretical_alignment": {
            "AIDA": "Post-AIDA - the original model does not address retention (a major limitation)",
            "STDC": "Care - existing customers with 2+ transactions. The most neglected stage per Kaushik.",
            "McKinsey_CDJ": "Post-Purchase Experience + Loyalty Loop - satisfied customers bypass evaluation and repurchase directly, creating a virtuous cycle",
            "Kotler_5A": "Advocate - the ultimate goal: customers become active brand promoters",
            "RACE": "Engage - repeat purchases, satisfaction, advocacy, Net Promoter Score",
            "Forrester": "Engage - ongoing post-purchase brand experience across all channels",
            "Byron_Sharp": "Challenges loyalty focus - Sharp argues growth comes from acquisition, not loyalty. Loyalty is largely a byproduct of market share (Double Jeopardy Law). However, reducing unnecessary churn is still important.",
            "Binet_Field": "Brand building contributes to retention through sustained mental availability. Activation drives repeat purchase through CRM, email, and direct response.",
        },
        "metric_interpretation": {
            "meaningful_metrics": {
                "primary": [
                    "Customer Lifetime Value (CLV) - total revenue over entire relationship",
                    "Retention Rate / Churn Rate",
                    "Repeat Purchase Rate",
                    "ROAS on retention campaigns (typically 4-10x, highest in funnel)",
                    "Net Promoter Score (NPS)",
                ],
                "secondary": [
                    "Customer Satisfaction Score (CSAT)",
                    "Average time between purchases",
                    "Cross-sell / upsell rate",
                    "Referral rate",
                    "Email engagement rates (open, click, conversion)",
                    "Reactivation rate (dormant customers)",
                ],
            },
            "vanity_metrics_warning": (
                "At retention stage, raw NPS without action is a vanity metric. "
                "Email open rates alone don't indicate loyalty (they indicate subject line quality). "
                "Loyalty program enrollment numbers mean nothing if members don't actively "
                "engage or redeem. Focus on BEHAVIORAL loyalty metrics: repeat purchase "
                "frequency, cross-category purchasing, and advocacy behaviors (referrals, reviews)."
            ),
            "benchmarks": {
                "retention_impact": "Increasing retention by just 5% can increase profits by 75%. Selling to existing customers has better margins and close rates than new acquisition.",
                "clv_formula": "CLV = Average Purchase Value x Purchase Frequency x Customer Lifespan. Improvement in any variable compounds over time.",
                "roas_retention": "ROAS on retention campaigns: 4-10x (highest in funnel because audience is already qualified and has purchase history).",
                "loyalty_program_failure": "77% of loyalty programs fail within 3 years. 78% of consumers abandon programs with difficult reward thresholds. 33% leave when rewards are irrelevant.",
            },
        },
        "budget_allocation": {
            "binet_field_guidance": (
                "Retention uses BOTH brand building (maintaining mental availability and "
                "emotional connection) and activation (CRM, email, direct offers). "
                "The most cost-efficient marketing is to existing customers. "
                "However, Sharp warns against over-allocating to loyalty at the expense "
                "of acquisition - growth fundamentally requires new customers."
            ),
            "funnel_budget_split": (
                "Retention typically receives 5-15% of total paid media budget. "
                "However, owned channels (email, WhatsApp, CRM) should be the primary "
                "retention tool, which doesn't consume media budget. "
                "Paid remarketing to existing customers supplements owned channels. "
                "The most efficient spend in the funnel but limited by customer base size."
            ),
        },
        "creative_and_messaging": {
            "psychological_principles": {
                "reciprocity": (
                    "Exclusive offers, early access, and loyalty rewards create a sense "
                    "of special treatment that encourages reciprocal loyalty. "
                    "Unexpected positive experiences (surprise discounts, birthday offers) "
                    "generate stronger reciprocity than expected ones."
                ),
                "commitment_consistency": (
                    "Once customers identify as brand users, consistency drives repeat behavior. "
                    "Identity-based marketing ('as a [Brand] customer') reinforces self-concept. "
                    "Small commitments (reviews, referrals, social follows) deepen commitment."
                ),
                "unity": (
                    "Cialdini's newest principle. Creating a sense of shared identity and "
                    "community belonging ('you're one of us'). Brand communities, VIP tiers, "
                    "and exclusive access leverage this powerful retention mechanism."
                ),
                "cialdini_applicable": [
                    "Reciprocity - loyalty rewards, exclusive access, unexpected gifts",
                    "Commitment/Consistency - subscription models, identity reinforcement",
                    "Unity - community membership, VIP status, shared identity",
                    "Social Proof - 'Other customers like you also bought...'",
                    "Scarcity - exclusive member-only offers, limited VIP slots",
                ],
            },
            "content_strategy": (
                "CRM-driven personalized communication. Email flows: post-purchase, "
                "reactivation, anniversary, cross-sell/upsell. Loyalty programs with "
                "meaningful, achievable rewards. Exclusive content and early access. "
                "User-generated content and review solicitation. Referral programs. "
                "Customer success content showing how to get more value from the product."
            ),
            "format_recommendations": [
                "Personalized email sequences (post-purchase, win-back, cross-sell)",
                "WhatsApp Business messages (Brazil-specific high performer)",
                "Custom audience remarketing on Meta/Google",
                "Loyalty program communications",
                "User-generated content campaigns",
                "Referral/ambassador program ads",
                "App push notifications",
                "SMS/RCS campaigns",
            ],
        },
        "platform_stage_alignment": {
            "Email Marketing": {
                "why": (
                    "Highest ROI channel for retention ($36-42 return per $1 spent). "
                    "Fully owned channel with no platform dependency. Segmentation "
                    "and personalization based on purchase history, browsing behavior, "
                    "and engagement level. Automated flows scale without incremental cost."
                ),
                "best_formats": "Post-purchase sequences, Win-back series, Cross-sell/upsell, Loyalty updates",
            },
            "WhatsApp Business (Brazil-specific)": {
                "why": (
                    "93.7% penetration in Brazil - the most accessible retention channel. "
                    "95% of brand-consumer interactions occur on WhatsApp. "
                    "Open rates vastly exceed email. Conversational commerce enables "
                    "real-time upsell/cross-sell. AI agents resolved 80% of conversations "
                    "without human intervention in 2024, with 150% increase in conversion."
                ),
                "best_formats": "Order updates, Personalized offers, Reactivation messages, Cart recovery",
            },
            "Meta Ads (Custom Audiences)": {
                "why": (
                    "CRM list targeting enables reaching existing customers with tailored "
                    "messages across Facebook, Instagram, and Messenger. Dynamic ads show "
                    "relevant cross-sell products based on purchase history. "
                    "ROAS on customer audiences typically 4-10x."
                ),
                "best_formats": "Custom Audience campaigns, Dynamic Ads, Catalog Sales",
            },
            "Google Ads (Customer Match)": {
                "why": (
                    "Customer Match lists enable retargeting across Search, YouTube, Display, "
                    "and Gmail. RLSA campaigns can adjust bids for returning customers. "
                    "YouTube ads can deliver brand storytelling to existing customers."
                ),
                "best_formats": "Customer Match, RLSA, YouTube retargeting",
            },
        },
        "common_mistakes": {
            "ignoring_existing_customers": (
                "The most common retention mistake: spending all budget acquiring new customers "
                "while ignoring the existing base. Existing customer segments are the most "
                "efficient advertising audiences but are often underserved."
            ),
            "treating_customers_as_prospects": (
                "Showing acquisition messaging to existing customers. Customers who already "
                "bought don't need to be convinced again - they need new reasons to engage, "
                "not the same pitch repeated."
            ),
            "loyalty_program_design_failures": (
                "77% of loyalty programs fail within 3 years. Common reasons: "
                "(1) Difficult reward thresholds (78% abandon for this reason). "
                "(2) Irrelevant rewards (33% leave). "
                "(3) Overly complex rules. "
                "(4) Purely transactional without emotional connection. "
                "(5) Inadequate personalization (80%+ customers prefer personalized experiences). "
                "(6) Single toxic touchpoint can swing 72% of loyal customers to a competitor."
            ),
            "no_segmentation_by_recency": (
                "Treating all customers the same regardless of last purchase date. "
                "RFM segmentation (Recency, Frequency, Monetary) is critical. "
                "A customer who bought yesterday needs different messaging than one "
                "who hasn't bought in 6 months."
            ),
            "over_reliance_on_discounts": (
                "Training customers to wait for promotions destroys margins. "
                "Effective retention uses value-added benefits (exclusive access, content, "
                "community) alongside strategic promotional offers."
            ),
        },
        "brazil_specifics": {
            "market_data": (
                "WhatsApp marketing volume grew 64% in 2024. Conversion rate on WhatsApp: 55%. "
                "Average recovered cart value: R$557.67 (432% increase from 2023). "
                "70% of Brazilian companies use WhatsApp for marketing, but only 40% "
                "use automated campaigns - significant automation opportunity. "
                "AI agents conducted 90,000 commercial conversations in 2024, resolving "
                "80% without human intervention."
            ),
            "cultural_considerations": (
                "WhatsApp is THE retention channel in Brazil - more important than email. "
                "59% of consumers prefer human-like interactions, not robotic automated messages. "
                "Brazilian consumers expect responsive, friendly, and informal communication. "
                "Loyalty programs should consider Brazilian payment habits (Pix rewards, "
                "cashback, installment benefits). "
                "Cultural events (Carnival, Copa do Brasil, novelas) provide engagement "
                "hooks for retention communications."
            ),
        },
    },
}

BUDGET_ALLOCATION_FRAMEWORKS = {
    "binet_field_60_40": {
        "name": "Binet & Field 60/40 Rule",
        "description": (
            "Based on IPA Databank analysis of 996+ campaigns. Optimal split is ~60% "
            "brand building / 40% sales activation for consumer brands. Brand building is "
            "emotional, broad-reach, fame-creating. Activation is rational, targeted, "
            "action-driving. The two should NOT be combined in the same creative."
        ),
        "variations_by_context": {
            "consumer_brands_default": {"brand": 60, "activation": 40},
            "premium_brands": {"brand": 70, "activation": 30},
            "b2b_new_brand": {"brand": 35, "activation": 65},
            "b2b_mature_leader": {"brand": 72, "activation": 28},
            "new_innovative_brand": {"brand": 40, "activation": 60},
            "commodity_low_price": {"brand": 50, "activation": 50},
        },
        "key_principle": (
            "Brand effects compound over 3-6+ months. Activation effects peak within days "
            "and decay rapidly. Over-investing in activation creates short-term spikes but "
            "long-term brand erosion. The most effective campaigns combine BOTH but in "
            "SEPARATE creative executions."
        ),
    },
    "funnel_budget_splits": {
        "60_30_10_model": {
            "name": "60-30-10 Full Funnel Split",
            "description": "Traditional model: 60% awareness, 30% mid-funnel, 10% bottom-funnel",
            "awareness": 60,
            "consideration": 30,
            "conversion": 10,
            "when_to_use": "New brands or brands entering new markets with low awareness",
        },
        "balanced_growth_model": {
            "name": "Balanced Growth Split",
            "description": "For established brands with moderate awareness",
            "awareness": 40,
            "consideration": 35,
            "conversion": 25,
            "when_to_use": "Growth-stage companies with established baseline awareness",
        },
        "performance_heavy_model": {
            "name": "Performance-Heavy Split",
            "description": "For mature brands with strong awareness focused on conversion efficiency",
            "awareness": 25,
            "consideration": 35,
            "conversion": 40,
            "when_to_use": "Mature brands in peak season or with strong existing awareness",
        },
        "fospha_top_performers": {
            "name": "Fospha Top Performers Pattern",
            "description": "Observed pattern in highest-performing brands",
            "awareness_and_consideration": 90,
            "conversion": 10,
            "when_to_use": "Brands prioritizing long-term sustainable growth over short-term extraction",
        },
    },
    "brazil_specific_considerations": (
        "In Brazil, the lower CPMs (70-94% below global) mean brand-building budgets "
        "go further than in mature markets. WhatsApp's 6x conversion premium means "
        "bottom-funnel can be more efficient through conversational commerce. "
        "Social media dominates at 53% of digital spend, favoring visual/video brand building. "
        "Seasonal spikes (Carnival, Children's Day, Black Friday, Christmas) require "
        "temporary reallocation toward conversion during peak demand periods."
    ),
}

CROSS_STAGE_PRINCIPLES = {
    "metrics_alignment_rule": (
        "NEVER judge a campaign by metrics from a different funnel stage. "
        "Awareness campaigns measured by CPA will always look like failures. "
        "Conversion campaigns measured by reach will always look inefficient. "
        "Each stage has its own success criteria, benchmarks, and optimization levers. "
        "This is the most important single principle in media planning."
    ),
    "full_funnel_synergy": (
        "Full-funnel approach delivers up to 45% higher ROI than single-stage campaigns "
        "and 7% lift in offline sales. Each stage feeds the next: awareness creates "
        "consideration audiences, consideration creates intent audiences, intent creates "
        "conversion audiences. Under-investing in any stage creates a bottleneck. "
        "Amazon data: campaigns using 2+ video solutions had 142% higher detail page view "
        "rate and 84% higher purchase rate vs single-solution campaigns."
    ),
    "halo_effects": (
        "For many brands, halo effects from upper-funnel campaigns drive more revenue than "
        "direct conversions. These include: increased organic traffic, branded search volume "
        "growth, direct traffic increases, social media follower growth, and PR/earned media. "
        "These effects are often uncaptured in last-click attribution models."
    ),
    "byron_sharp_vs_funnel": (
        "Byron Sharp's work challenges traditional funnel thinking by arguing that: "
        "(1) Growth comes from acquisition, not loyalty. "
        "(2) Targeting should be broad, not niche. "
        "(3) Reach matters more than frequency. "
        "(4) Distinctive assets matter more than differentiated positioning. "
        "This doesn't invalidate funnel-based planning but suggests that even 'consideration' "
        "and 'conversion' campaigns should maintain broad reach elements and distinctive "
        "brand assets rather than becoming purely rational/functional."
    ),
    "attribution_complexity": (
        "No single attribution model captures the full picture. Last-click overvalues "
        "conversion stage. First-click overvalues awareness. Multi-touch models attempt "
        "balance but require sophisticated implementation. Incrementality testing (geo-lift "
        "studies, conversion lift studies) provides the most accurate measurement of true "
        "campaign impact at each stage. Media mix modeling (MMM) is essential for "
        "understanding long-term brand building effects."
    ),
}


def get_enriched_funnel_context(etapa: str) -> str:
    stage_data = FUNNEL_STAGE_DEEP_KNOWLEDGE.get(etapa)
    if not stage_data:
        return ""

    theoretical = stage_data.get("theoretical_alignment", {})
    metrics = stage_data.get("metric_interpretation", {})
    budget = stage_data.get("budget_allocation", {})
    creative = stage_data.get("creative_and_messaging", {})
    platforms = stage_data.get("platform_stage_alignment", {})
    mistakes = stage_data.get("common_mistakes", {})
    brazil = stage_data.get("brazil_specifics", {})

    theory_lines = []
    for framework, alignment in theoretical.items():
        theory_lines.append(f"  - {framework}: {alignment}")
    theory_block = "\n".join(theory_lines)

    meaningful = metrics.get("meaningful_metrics", {})
    primary_metrics = ", ".join(meaningful.get("primary", []))
    secondary_metrics = ", ".join(meaningful.get("secondary", []))

    vanity_warning = metrics.get("vanity_metrics_warning", "")

    benchmarks = metrics.get("benchmarks", {})
    bench_lines = []
    for key, value in benchmarks.items():
        bench_lines.append(f"  - {key}: {value}")
    bench_block = "\n".join(bench_lines)

    binet_guidance = budget.get("binet_field_guidance", "")
    funnel_split = budget.get("funnel_budget_split", "")

    psych = creative.get("psychological_principles", {})
    psych_lines = []
    for principle, description in psych.items():
        if principle != "cialdini_applicable":
            if isinstance(description, str):
                psych_lines.append(f"  - {principle}: {description}")
    cialdini = psych.get("cialdini_applicable", [])
    cialdini_lines = [f"    - {c}" for c in cialdini]

    content_strategy = creative.get("content_strategy", "")
    formats = creative.get("format_recommendations", [])
    format_lines = [f"  - {f}" for f in formats]

    platform_lines = []
    for platform, info in platforms.items():
        platform_lines.append(
            f"  - {platform}: {info.get('why', '')} | Best formats: {info.get('best_formats', '')}"
        )
    platform_block = "\n".join(platform_lines)

    mistake_lines = []
    for mistake, description in mistakes.items():
        mistake_lines.append(f"  - {mistake}: {description}")
    mistakes_block = "\n".join(mistake_lines)

    brazil_market = brazil.get("market_data", "")
    brazil_culture = brazil.get("cultural_considerations", "")

    enriched = f"""
=== CONTEXTO ESTRATEGICO APROFUNDADO: "{etapa}" ===

**ALINHAMENTO TEORICO (Frameworks Academicos):**
{theory_block}

**METRICAS SIGNIFICATIVAS:**
  Primarias: {primary_metrics}
  Secundarias: {secondary_metrics}

**ALERTA - METRICAS DE VAIDADE NESTA ETAPA:**
{vanity_warning}

**BENCHMARKS DE REFERENCIA:**
{bench_block}

**ALOCACAO DE BUDGET (Binet & Field):**
{binet_guidance}

**ALOCACAO POR FUNIL:**
{funnel_split}

**PRINCIPIOS PSICOLOGICOS APLICAVEIS:**
{chr(10).join(psych_lines)}
  Principios de Cialdini mais relevantes:
{chr(10).join(cialdini_lines)}

**ESTRATEGIA DE CONTEUDO:**
{content_strategy}

**FORMATOS RECOMENDADOS:**
{chr(10).join(format_lines)}

**ALINHAMENTO PLATAFORMA-ETAPA:**
{platform_block}

**ERROS COMUNS E ANTI-PADROES (PESQUISA):**
{mistakes_block}

**ESPECIFICIDADES DO MERCADO BRASILEIRO:**
  Dados de mercado: {brazil_market}
  Consideracoes culturais: {brazil_culture}
"""
    return enriched
