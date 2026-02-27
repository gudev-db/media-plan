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
                "descricao": (
                    "O Alcance representa o número de pessoas únicas que foram expostas ao seu anúncio durante o período "
                    "da campanha. Diferentemente das impressões, que contam cada exibição individual (incluindo repetições "
                    "para a mesma pessoa), o alcance mede a amplitude real da sua comunicação — quantas pessoas distintas "
                    "receberam sua mensagem. Na etapa de Consciência, o alcance é considerado o KPI mais importante segundo "
                    "Byron Sharp, que demonstrou em 'How Brands Grow' que o crescimento de marca vem primariamente da "
                    "aquisição de novos compradores e compradores leves, e não da fidelização dos já existentes.\n\n"
                    "Para campanhas de awareness, maximizar o alcance deve ser prioridade sobre frequência. Conforme a "
                    "pesquisa do Ehrenberg-Bass Institute, marcas que priorizam alcance amplo sobre segmentação excessiva "
                    "constroem disponibilidade mental de forma mais eficiente. No contexto brasileiro, onde o CPM do Meta "
                    "Ads é 70-94% inferior à média global, existe uma oportunidade significativa de alcançar grandes "
                    "audiências com investimentos relativamente menores. A regra geral é que 95% dos potenciais compradores "
                    "não estão prontos para comprar agora (LinkedIn B2B Institute), mas precisam estar no conjunto mental "
                    "de consideração para compras futuras — e isso só acontece se forem alcançados.\n\n"
                    "Na prática, o alcance deve ser cruzado com a frequência (Impressões / Alcance) para garantir que a "
                    "distribuição está saudável. Uma frequência entre 1,5 e 3,0 por semana é o ponto ideal para awareness: "
                    "suficiente para gerar lembrança sem causar fadiga. Se o alcance está baixo em relação ao budget investido, "
                    "isso pode indicar segmentação muito restritiva, CPM elevado, ou problemas de competição no leilão."
                ),
            },
            {
                "nome": "Impressões",
                "formula": "Total de exibições do anúncio",
                "faixa_tipica": "2-3x o alcance com frequência saudável",
                "quando_usar": "Para medir volume total de exposição",
                "descricao": (
                    "As Impressões representam o número total de vezes que o seu anúncio foi exibido, incluindo múltiplas "
                    "exibições para a mesma pessoa. Enquanto o alcance conta pessoas únicas, as impressões contam exposições "
                    "totais. Se uma pessoa viu seu anúncio 3 vezes, isso conta como 1 de alcance e 3 de impressões. "
                    "Na etapa de Consciência, as impressões são fundamentais porque sustentam o princípio psicológico do "
                    "Efeito de Mera Exposição (Zajonc, 1968): a exposição repetida a um estímulo gera familiaridade, e "
                    "familiaridade gera preferência. Pesquisas mostram que audiências expostas 5-7 vezes a um anúncio têm "
                    "até 8x mais probabilidade de converter posteriormente.\n\n"
                    "A relação entre impressões e alcance define a frequência média da campanha. Uma proporção de 2-3x "
                    "(impressões sendo 2 a 3 vezes o alcance) indica uma frequência saudável para awareness. Acima de 4x "
                    "começa o risco de fadiga do anúncio, onde o efeito positivo da repetição se inverte e passa a gerar "
                    "irritação. O custo por mil impressões (CPM) é a métrica de eficiência diretamente associada: dividindo "
                    "o budget total pelas impressões e multiplicando por 1000, você obtém quanto está pagando por cada "
                    "mil exibições. No Brasil, CPMs médios variam de R$8-25 no Meta Ads, R$5-35 no Google Ads, e R$5-20 "
                    "no TikTok, oferecendo alta eficiência de exposição comparado a mercados globais.\n\n"
                    "Para otimizar impressões em campanhas de awareness, priorize formatos de alto impacto visual "
                    "(vídeo curto, carrosséis, formatos de tela cheia) e segmentação ampla. Segundo Binet & Field, "
                    "campanhas de construção de marca devem ser emocionais, de amplo alcance e focadas em criar fama "
                    "e distinção — e as impressões são o veículo que entrega essa mensagem ao maior número de vezes possível."
                ),
            },
            {
                "nome": "CPM",
                "formula": "(Custo total / Impressões) x 1000",
                "faixa_tipica": "R$8-25 (varia por plataforma e segmentação)",
                "quando_usar": "Para avaliar eficiência de custo por exposição",
                "descricao": (
                    "O CPM (Custo por Mil Impressões) é a métrica fundamental de eficiência de custo em campanhas de "
                    "awareness. Ele indica quanto você está pagando para que seu anúncio seja exibido mil vezes. A fórmula "
                    "é simples: (Custo Total / Impressões) x 1000. Por exemplo, se você investiu R$15.000 e obteve "
                    "1.000.000 de impressões, seu CPM é R$15,00. Esta é a métrica que conecta diretamente o investimento "
                    "financeiro ao volume de exposição obtido, sendo essencial para comparar a eficiência entre plataformas, "
                    "formatos de anúncio e segmentações de público.\n\n"
                    "O CPM varia significativamente conforme a plataforma, o formato, a segmentação e a sazonalidade. "
                    "No mercado brasileiro, o Meta Ads oferece CPMs entre R$8-25, enquanto o Google Ads varia de R$5-35. "
                    "LinkedIn, por ser uma plataforma B2B com audiência de alto valor, apresenta CPMs entre R$30-80. "
                    "TikTok e Mídia Programática tendem a oferecer CPMs mais competitivos (R$5-20 e R$3-20 respectivamente). "
                    "Um CPM mais baixo não é necessariamente melhor — audiências mais qualificadas naturalmente custam mais. "
                    "O importante é avaliar o CPM em contexto: quanto mais próximo do público-alvo ideal, mais aceitável "
                    "é um CPM elevado.\n\n"
                    "Para otimizar o CPM, considere: ampliar a segmentação (audiências muito restritas elevam o CPM por "
                    "competição no leilão), testar diferentes formatos (vídeo e Reels frequentemente têm CPMs mais baixos "
                    "que estáticos em feeds), evitar períodos de alta competição (Black Friday, Natal, Carnaval elevam "
                    "CPMs drasticamente), e utilizar estratégias de lance adequadas. Segundo Byron Sharp, na etapa de "
                    "awareness a prioridade deve ser alcançar o máximo de pessoas na categoria com o menor custo por "
                    "exposição, o que torna o CPM o termômetro primário de eficiência nesta fase."
                ),
            },
        ],
        "secundarios": [
            {
                "nome": "Frequência",
                "formula": "Impressões / Alcance",
                "faixa_tipica": "1.5-3.0 para awareness; acima de 4 gera fadiga",
                "quando_usar": "Para controlar saturação de audiência",
                "descricao": (
                    "A Frequência mede quantas vezes, em média, cada pessoa única foi exposta ao seu anúncio. "
                    "É calculada dividindo o total de impressões pelo alcance. Por exemplo, se a campanha gerou "
                    "3.000.000 de impressões para um alcance de 1.000.000 de pessoas, a frequência média é 3,0. "
                    "Na etapa de Consciência, a frequência é o regulador entre exposição suficiente e fadiga: "
                    "exposições demais irritam, exposições de menos não geram lembrança.\n\n"
                    "O ponto ideal para awareness situa-se entre 1,5 e 3,0 exposições por semana. Pesquisas sobre "
                    "o Efeito de Mera Exposição mostram que a relação entre frequência e preferência segue uma curva "
                    "em formato de U invertido: as primeiras exposições aumentam a familiaridade e o afeto positivo, "
                    "mas a partir de certo ponto (geralmente acima de 4-5 exposições semanais sem rotação de criativos), "
                    "o efeito se inverte e gera rejeição. Byron Sharp recomenda priorizar alcance sobre frequência — "
                    "é melhor alcançar mais pessoas com frequência moderada do que poucas pessoas muitas vezes."
                ),
            },
            {
                "nome": "Brand Lift",
                "formula": "% aumento em reconhecimento pós-campanha",
                "faixa_tipica": "3-15% de lift dependendo da categoria",
                "quando_usar": "Para medir impacto real na percepção de marca",
                "descricao": (
                    "O Brand Lift mede a elevação real na lembrança, reconhecimento ou percepção de marca causada "
                    "pela campanha. Diferentemente de métricas de entrega (impressões, alcance), o Brand Lift avalia "
                    "se a exposição realmente gerou impacto cognitivo — ou seja, se as pessoas lembram mais da marca "
                    "após a campanha do que antes. É medido por meio de pesquisas pré e pós-campanha, ou por estudos "
                    "oferecidos pelas plataformas (Meta Brand Lift Study, YouTube Brand Lift).\n\n"
                    "Este é o indicador que melhor valida se uma campanha de awareness está cumprindo seu propósito "
                    "estratégico. Conforme Binet & Field demonstraram, os efeitos de construção de marca levam 6+ meses "
                    "para se materializar completamente em resultados de negócio. Portanto, o Brand Lift é o indicador "
                    "intermediário mais confiável de que a campanha está no caminho certo. Lifts entre 3-15% são típicos, "
                    "sendo que anúncios em podcast podem gerar até 13 pontos percentuais de aumento em awareness."
                ),
            },
            {
                "nome": "Custo por Alcance (CPR)",
                "formula": "Custo total / Alcance",
                "faixa_tipica": "R$0.01-0.05 por pessoa alcançada",
                "quando_usar": "Para comparar eficiência entre plataformas",
                "descricao": (
                    "O Custo por Alcance (CPR) indica quanto você está pagando, em média, para que uma pessoa única "
                    "seja exposta ao seu anúncio. Enquanto o CPM mede o custo por mil exibições (incluindo repetições), "
                    "o CPR mede o custo por pessoa alcançada, tornando-o mais preciso para avaliar a eficiência de "
                    "campanhas de awareness onde o objetivo é maximizar a cobertura da audiência-alvo.\n\n"
                    "No mercado brasileiro, CPRs típicos variam entre R$0,01 e R$0,05 por pessoa. Plataformas com "
                    "CPMs mais baixos e menor sobreposição de audiência tendem a oferecer melhores CPRs. O CPR é "
                    "especialmente útil para comparar o desempenho entre plataformas de forma justa: uma plataforma "
                    "com CPM mais alto pode ter CPR similar se alcançar mais pessoas únicas com menos repetição."
                ),
            },
            {
                "nome": "Share of Voice",
                "formula": "Impressões da marca / Total da categoria",
                "faixa_tipica": "Depende do setor; buscar >10% em nichos",
                "quando_usar": "Para avaliar presença relativa no mercado",
                "descricao": (
                    "O Share of Voice (SOV) mede a participação da sua marca no volume total de publicidade da "
                    "categoria. Se o total de impressões de anúncios no seu segmento é de 100 milhões e sua marca "
                    "gerou 10 milhões, seu SOV é de 10%. Esta métrica é crucial porque pesquisas do IPA (Institute "
                    "of Practitioners in Advertising) demonstram uma correlação direta entre Share of Voice e Share "
                    "of Market: marcas que mantêm SOV acima do seu market share tendem a crescer, e vice-versa.\n\n"
                    "Binet & Field chamam essa diferença de ESOV (Excess Share of Voice) e demonstram que cada 10 "
                    "pontos percentuais de ESOV geram aproximadamente 0,5% de crescimento de market share ao ano. "
                    "Para marcas desafiadoras que buscam crescer, manter o SOV acima do market share é essencial. "
                    "No contexto brasileiro, onde os CPMs são significativamente menores que a média global, "
                    "existe uma oportunidade de conquistar SOV elevado com investimentos proporcionalmente menores."
                ),
            },
        ],
        "terciarios": [
            {
                "nome": "Visualizações",
                "formula": "Total de visualizações do anúncio/vídeo",
                "faixa_tipica": "R$0.02-0.10 por view; 3s+ para vídeo",
                "quando_usar": "Para medir volume de views em vídeo ou conteúdo",
                "descricao": (
                    "As Visualizações contabilizam quantas vezes o conteúdo de vídeo ou anúncio foi assistido "
                    "por pelo menos o tempo mínimo estipulado pela plataforma (3 segundos no Meta Ads, 30 "
                    "segundos ou duração total no YouTube). Na etapa de Consciência, visualizações de vídeo "
                    "são particularmente relevantes porque formatos audiovisuais geram lembrança de marca "
                    "superior a estáticos — pesquisas mostram que vídeos com storytelling emocional produzem "
                    "até 2x mais recall do que banners. O custo por visualização (CPV) típico no Brasil "
                    "varia de R$0,02 a R$0,10, tornando o vídeo um dos formatos mais eficientes para "
                    "construção de awareness em larga escala.\n\n"
                    "Como métrica terciária em Consciência, as visualizações complementam o alcance e as "
                    "impressões ao indicar engajamento passivo com o conteúdo. Porém, é crucial não "
                    "confundir visualizações com engajamento real: uma view de 3 segundos em autoplay "
                    "no feed não necessariamente indica interesse genuíno. A métrica mais informativa é "
                    "a taxa de conclusão do vídeo (VCR), que revela se a audiência está realmente "
                    "absorvendo a mensagem ou apenas rolando o feed."
                ),
            },
            {
                "nome": "Engajamento",
                "formula": "Curtidas + Comentários + Compartilhamentos + Salvamentos",
                "faixa_tipica": "0.5-2% de taxa sobre impressões",
                "quando_usar": "Indicador de ressonância e interação",
                "descricao": (
                    "O Engajamento total soma todas as interações ativas do usuário com o anúncio: "
                    "curtidas, comentários, compartilhamentos e salvamentos. Na etapa de Consciência, "
                    "esta métrica funciona como indicador de ressonância — se o conteúdo está gerando "
                    "reações, significa que está ultrapassando a barreira da indiferença, o que é "
                    "essencial para construir memória de marca. Taxas de engajamento de 0,5-2% sobre "
                    "impressões são típicas para campanhas de awareness, sendo que conteúdos nativos "
                    "(que se parecem com posts orgânicos) tendem a performar melhor que formatos "
                    "claramente publicitários.\n\n"
                    "Apesar de relevante, o engajamento é terciário em Consciência porque o objetivo "
                    "primário desta etapa é exposição ampla (alcance e impressões), não interação. "
                    "Um erro comum é otimizar campanhas de awareness para engajamento, o que faz o "
                    "algoritmo privilegiar uma audiência pequena e engajada em vez de maximizar o "
                    "alcance — contradizendo o princípio de Byron Sharp de 'reach over frequency'. "
                    "O engajamento deve ser monitorado como sinal de qualidade do criativo, mas não "
                    "como objetivo de otimização da campanha nesta etapa."
                ),
            },
            {
                "nome": "Comentários",
                "formula": "Total de comentários no anúncio",
                "faixa_tipica": "0.01-0.1% das impressões",
                "quando_usar": "Para medir nível de conversa e interesse ativo",
                "descricao": (
                    "Os Comentários representam a forma mais ativa de engajamento — exigem que o "
                    "usuário pare, reflita e escreva uma resposta, o que demanda muito mais esforço "
                    "cognitivo do que uma curtida ou compartilhamento. Na Consciência, taxas de "
                    "comentário de 0,01-0,1% sobre impressões são normais. Uma taxa acima disso "
                    "sugere que o criativo está provocando reações fortes (positivas ou negativas), "
                    "o que em awareness pode ser desejável pois gera 'fama' e discussão — conforme "
                    "Binet & Field, campanhas que geram buzz têm efeitos de longo prazo mais "
                    "pronunciados sobre métricas de marca.\n\n"
                    "É essencial monitorar o sentimento dos comentários, não apenas o volume. "
                    "Um alto volume de comentários negativos pode indicar desalinhamento entre "
                    "a mensagem e os valores da audiência, algo particularmente sensível no Brasil "
                    "onde consumidores são vocais nas redes sociais. Comentários também funcionam "
                    "como sinais para o algoritmo de distribuição: posts com muitos comentários "
                    "recebem mais alcance orgânico, amplificando o investimento pago."
                ),
            },
            {
                "nome": "Custo Total",
                "formula": "Soma de todo investimento na campanha",
                "faixa_tipica": "= Budget alocado para a etapa",
                "quando_usar": "Para controlar gasto total vs. planejado",
                "descricao": (
                    "O Custo Total é a soma de todos os investimentos realizados na campanha, "
                    "incluindo veiculação de mídia, taxas de plataforma e eventuais custos de "
                    "produção de criativos. Na etapa de Consciência, controlar o custo total "
                    "contra o budget planejado é fundamental para garantir que a alocação "
                    "recomendada pelo framework de Binet & Field (tipicamente 60% do budget "
                    "total para construção de marca) esteja sendo respeitada. Desvios "
                    "significativos podem indicar problemas de pacing ou competição elevada "
                    "no leilão publicitário.\n\n"
                    "O custo total deve ser analisado em relação às métricas de entrega: "
                    "se o custo está no planejado mas o alcance está muito abaixo, o CPM "
                    "está mais alto que o previsto e ajustes são necessários (ampliar "
                    "segmentação, mudar formato, alterar lance). Monitorar o custo total "
                    "diariamente evita surpresas ao final da campanha e permite "
                    "redistribuição de budget entre conjuntos de anúncios ou plataformas "
                    "conforme a performance em tempo real."
                ),
            },
            {
                "nome": "Custo Diário",
                "formula": "Custo total / Dias de veiculação",
                "faixa_tipica": "Budget / dias do período",
                "quando_usar": "Para monitorar pacing diário de investimento",
                "descricao": (
                    "O Custo Diário representa o valor médio investido por dia de campanha, "
                    "calculado dividindo o custo total pelos dias de veiculação. Na etapa de "
                    "Consciência, o monitoramento do custo diário é essencial para garantir "
                    "um pacing saudável — distribuição uniforme do budget ao longo do período "
                    "evita concentrar toda a verba nos primeiros dias e ficar sem investimento "
                    "no final. Plataformas como Meta Ads oferecem opções de 'budget diário' "
                    "e 'budget vitalício' que automatizam parte desse controle, mas picos de "
                    "demanda (finais de semana, eventos sazonais) podem distorcer o gasto.\n\n"
                    "Desvios de mais de 15-20% no custo diário em relação ao planejado "
                    "merecem investigação: gastos acima do esperado podem indicar CPMs mais "
                    "altos (competição no leilão), enquanto gastos abaixo sugerem que a "
                    "campanha não está conseguindo entregar (audiência muito restrita, lance "
                    "muito baixo, ou problemas de aprovação de criativos). O ideal é "
                    "combinar custo diário com métricas de entrega diária para identificar "
                    "tendências antes que comprometam o resultado final."
                ),
            },
            {
                "nome": "Cliques",
                "formula": "Total de cliques no anúncio",
                "faixa_tipica": "Depende de CTR e volume de impressões",
                "quando_usar": "Indicador secundário em awareness; foco é exposição",
                "descricao": (
                    "Os Cliques contabilizam o número total de vezes que usuários clicaram no "
                    "anúncio, seja para visitar o site, perfil da marca ou qualquer link de "
                    "destino. Na etapa de Consciência, cliques são uma métrica terciária porque "
                    "o objetivo primário é exposição e lembrança, não tráfego. No entanto, "
                    "cliques em campanhas de awareness servem como 'bônus' — pessoas que, além "
                    "de serem expostas, demonstram interesse ativo suficiente para explorar mais "
                    "sobre a marca.\n\n"
                    "Um erro estratégico comum é otimizar campanhas de awareness para cliques, "
                    "o que faz o algoritmo buscar pessoas propensas a clicar (frequentemente "
                    "'clicadores compulsivos' que não geram valor real) em vez de maximizar "
                    "alcance e exposição. Conforme Byron Sharp, o alcance amplo é mais valioso "
                    "que engajamento profundo nesta etapa. Os cliques devem ser monitorados "
                    "para diagnóstico (um volume muito alto pode indicar CTA inadequado para "
                    "awareness; um volume muito baixo pode indicar criativo pouco atrativo), "
                    "mas não devem ser o critério de sucesso."
                ),
            },
            {
                "nome": "CTR",
                "formula": "(Cliques / Impressões) x 100",
                "faixa_tipica": "0.3-1.5% para awareness (menor que outras etapas)",
                "quando_usar": "Para monitorar atratividade do criativo",
                "descricao": (
                    "O CTR (Click-Through Rate) na etapa de Consciência reflete a taxa de "
                    "cliques sobre impressões, tipicamente entre 0,3-1,5% — significativamente "
                    "menor do que em etapas posteriores do funil. Isso é esperado e saudável: "
                    "em awareness, os criativos são desenhados para gerar lembrança e "
                    "familiaridade, não necessariamente para provocar cliques imediatos. "
                    "Conforme Binet & Field, campanhas de construção de marca devem priorizar "
                    "impacto emocional e memorabilidade sobre resposta direta, o que "
                    "naturalmente resulta em CTRs mais baixos.\n\n"
                    "Ainda assim, o CTR terciário em awareness funciona como termômetro do "
                    "criativo: se está abaixo de 0,3%, o conteúdo pode estar pouco atrativo "
                    "ou irrelevante para a audiência. Se está acima de 1,5%, pode indicar "
                    "que o criativo tem um tom muito promocional ou de resposta direta, "
                    "inadequado para awareness. O CTR ideal nesta etapa é 'moderado' — "
                    "suficiente para confirmar relevância, sem desviar o algoritmo do "
                    "objetivo de maximizar alcance."
                ),
            },
            {
                "nome": "CPC",
                "formula": "Custo total / Cliques",
                "faixa_tipica": "R$0.30-3.00 dependendo da plataforma",
                "quando_usar": "Para referência; não é métrica principal em awareness",
                "descricao": (
                    "O CPC (Custo por Clique) em campanhas de Consciência varia de R$0,30 a "
                    "R$3,00 dependendo da plataforma e segmentação. É uma métrica terciária "
                    "nesta etapa porque o objetivo não é gerar cliques, mas sim exposição — "
                    "portanto, otimizar para CPC em awareness é um erro estratégico que "
                    "desvia a campanha do seu propósito. No entanto, monitorar o CPC fornece "
                    "contexto sobre a eficiência geral e permite comparações históricas e "
                    "entre plataformas.\n\n"
                    "CPCs em awareness tendem a ser mais altos do que em campanhas otimizadas "
                    "para tráfego justamente porque as campanhas não estão sendo otimizadas "
                    "para esse evento. Isso é normal e esperado. Um CPC muito baixo em "
                    "awareness pode até ser um sinal de alerta: pode indicar que o algoritmo "
                    "está priorizando 'clicadores compulsivos' — audiências com alta propensão "
                    "a clicar mas baixa propensão a criar memória de marca — comprometendo "
                    "a qualidade do alcance em troca de cliques baratos."
                ),
            },
            {
                "nome": "CPA",
                "formula": "Custo total / Total de conversões",
                "faixa_tipica": "Muito alto em awareness; não é foco",
                "quando_usar": "Apenas para referência de baseline",
                "descricao": (
                    "O CPA (Custo por Aquisição) em awareness representa o custo para gerar "
                    "uma conversão a partir de campanhas de topo de funil. Este valor tende a "
                    "ser muito alto — frequentemente 5-10x maior que o CPA de campanhas de "
                    "conversão — e isso é absolutamente esperado. Campanhas de awareness não "
                    "são desenhadas para converter imediatamente; elas constroem a base de "
                    "familiaridade e consideração que alimentará conversões futuras. Julgar o "
                    "sucesso de awareness pelo CPA é um dos erros mais comuns e destrutivos "
                    "em mídia digital.\n\n"
                    "Conforme Binet & Field demonstraram extensivamente, os efeitos de "
                    "construção de marca levam 6+ meses para se materializar em resultados "
                    "de negócio. Portanto, o CPA em awareness deve ser registrado apenas "
                    "como baseline — servindo para análises futuras de atribuição multi-touch "
                    "que cruzam a exposição inicial em awareness com conversões posteriores "
                    "em etapas inferiores do funil. Marcas que cortam investimento em "
                    "awareness por CPA alto inevitavelmente veem o CPA de conversão subir "
                    "meses depois, quando o pipeline de consideração seca."
                ),
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
                "descricao": (
                    "O CTR (Click-Through Rate ou Taxa de Cliques) é o percentual de pessoas que, ao verem o anúncio, "
                    "decidiram clicar nele. É calculado dividindo o número de cliques pelo número de impressões e "
                    "multiplicando por 100. Na etapa de Interesse, o CTR é o termômetro primário de relevância e "
                    "atratividade do conteúdo: um CTR alto indica que a mensagem e o criativo estão ressoando com a "
                    "audiência, despertando curiosidade suficiente para motivar uma ação. Conforme o modelo STDC de "
                    "Kaushik, esta é a transição entre 'See' (exposição passiva) e 'Think' (exploração ativa).\n\n"
                    "Os benchmarks de CTR variam drasticamente por plataforma e formato. Em redes sociais (Meta Ads), "
                    "CTRs entre 0,8% e 2,5% são considerados saudáveis, enquanto no Google Ads Search, CTRs de 3-8% "
                    "são normais devido à natureza ativa da busca. TikTok In-Feed pode alcançar 1,5-3% graças ao formato "
                    "nativo. Display ads têm CTRs naturalmente mais baixos (0,1-0,5%) por serem publicidade de interrupção. "
                    "O importante é contextualizar o CTR: comparar com benchmarks da mesma plataforma, formato e segmento.\n\n"
                    "Para otimizar o CTR na etapa de Interesse, o princípio da 'Lacuna de Curiosidade' é o mais poderoso: "
                    "criativos que abrem uma questão sem respondê-la completamente motivam o clique para saber mais. "
                    "Textos com promessas de valor claro ('Descubra como...', '5 passos para...'), imagens intrigantes "
                    "e vídeos com ganchos nos primeiros 3 segundos impulsionam significativamente o CTR."
                ),
            },
            {
                "nome": "Cliques",
                "formula": "Total de cliques no anúncio",
                "faixa_tipica": "Depende de CTR e impressões",
                "quando_usar": "Para medir volume de interesse gerado",
                "descricao": (
                    "Os Cliques representam o volume absoluto de interações ativas com o anúncio — cada vez que alguém "
                    "toca ou clica no seu conteúdo, seja para visitar o site, assistir um vídeo em tela cheia, ou expandir "
                    "um carrossel. Na etapa de Interesse, os cliques são o indicador primário de que a audiência passou "
                    "da exposição passiva para a exploração ativa. É o primeiro sinal comportamental de que a comunicação "
                    "despertou curiosidade real, diferentemente de impressões (que medem apenas exposição).\n\n"
                    "O volume de cliques é diretamente proporcional a duas variáveis: o CTR e o número de impressões. "
                    "Essa relação matemática permite projeções precisas: se o budget gera N impressões e o CTR esperado "
                    "é T%, os cliques projetados são N x T / 100. Por exemplo, 500.000 impressões com CTR de 1,5% geram "
                    "7.500 cliques. Entretanto, volume de cliques sem qualidade é uma métrica de vaidade — 1.000 cliques "
                    "que resultam em bounce imediato valem menos que 200 cliques com engajamento profundo no site.\n\n"
                    "Na prática, é essencial cruzar o volume de cliques com métricas pós-clique: tempo na página, "
                    "páginas por sessão e taxa de rejeição. Isso revela se os cliques estão gerando interesse genuíno "
                    "ou apenas cliques acidentais/desalinhados."
                ),
            },
            {
                "nome": "CPC",
                "formula": "Custo total / Cliques",
                "faixa_tipica": "R$0.30-3.00 (Social); R$1.00-8.00 (Search)",
                "quando_usar": "Para avaliar custo de gerar interesse",
                "descricao": (
                    "O CPC (Custo por Clique) é a métrica de eficiência financeira central na etapa de Interesse. "
                    "Calculado dividindo o custo total pelo número de cliques, ele revela quanto você está pagando "
                    "para que cada pessoa demonstre interesse ativo no seu conteúdo. O CPC está intrinsecamente ligado "
                    "ao CTR e ao CPM pela fórmula: CPC = CPM / (CTR x 10). Isso significa que melhorar o CTR reduz "
                    "automaticamente o CPC, mesmo que o CPM permaneça estável.\n\n"
                    "No mercado brasileiro, o CPC do Meta Ads para e-commerce é em média $0,38 — 66% abaixo da média "
                    "global de $1,14. Isso representa uma vantagem competitiva significativa para gerar tráfego de "
                    "interesse com eficiência. No Google Ads, CPCs variam amplamente por setor: marketing/publicidade "
                    "média de $4,22, enquanto e-commerce geral fica entre R$1-3. LinkedIn, por ser B2B premium, tem "
                    "CPCs entre R$5-25, mas a qualidade do tráfego compensa para segmentos corporativos.\n\n"
                    "Para reduzir o CPC, foque em melhorar a qualidade e relevância do anúncio (Quality Score no Google, "
                    "Relevance Score no Meta), testar múltiplos criativos para encontrar os de melhor CTR, e otimizar "
                    "a segmentação para audiências com maior propensão a engajar com o conteúdo."
                ),
            },
        ],
        "secundarios": [
            {
                "nome": "Taxa de Engajamento",
                "formula": "(Engajamentos / Alcance) x 100",
                "faixa_tipica": "1-5% em social media",
                "quando_usar": "Para medir profundidade de interesse",
                "descricao": (
                    "A Taxa de Engajamento mede o percentual de pessoas alcançadas que interagiram "
                    "ativamente com o conteúdo — curtidas, comentários, compartilhamentos, salvamentos "
                    "e cliques. Diferentemente de métricas passivas como impressões, o engajamento indica "
                    "que a audiência não apenas viu, mas respondeu ao conteúdo. Na etapa de Interesse, "
                    "esta métrica é crucial porque valida que a mensagem ressoou o suficiente para gerar "
                    "uma ação voluntária. Taxas entre 1-5% são consideradas saudáveis em redes sociais, "
                    "sendo que acima de 3% indica ressonância forte com a audiência.\n\n"
                    "É fundamental medir a taxa sobre ALCANCE, não sobre impressões, para evitar distorções "
                    "causadas por frequência alta. Engajamento alto com tráfego de baixa qualidade (bounce "
                    "rate alto, tempo no site baixo) pode indicar conteúdo que entretém mas não conecta à "
                    "marca — o que Kaushik chamaria de 'entretenimento sem propósito comercial'. O ideal "
                    "é que o engajamento social se traduza em visitas ao site ou consumo de conteúdo mais "
                    "profundo, validando a progressão do Interesse para Consideração."
                ),
            },
            {
                "nome": "ThruPlay",
                "formula": "Vídeos assistidos até o final ou 15s+",
                "faixa_tipica": "15-40% de completion rate",
                "quando_usar": "Para medir interesse genuíno no conteúdo",
                "descricao": (
                    "ThruPlay é a métrica do Meta Ads que contabiliza visualizações de vídeo de 15 "
                    "segundos ou mais (ou até o final, se o vídeo for mais curto). Na etapa de Interesse, "
                    "ela é um indicador superior às visualizações simples (3 segundos) porque confirma "
                    "que o espectador ESCOLHEU continuar assistindo após os primeiros segundos — evidência "
                    "de interesse genuíno no conteúdo, não apenas exposição passiva no feed. Taxas de "
                    "conclusão entre 15-40% são referência para conteúdo de interesse.\n\n"
                    "Cruzar ThruPlay com ações pós-visualização (visitas ao site, buscas pela marca) "
                    "valida se o consumo de vídeo está gerando interesse acionável. Um ThruPlay alto "
                    "com zero tráfego subsequente pode indicar conteúdo que entretém mas não conecta à "
                    "marca. Para otimizar ThruPlay na etapa de Interesse, priorize vídeos educacionais "
                    "curtos (15-60s) com hook forte nos primeiros 3 segundos e branded elements visíveis "
                    "antes dos 5 segundos, conforme recomendado por Byron Sharp para construção de "
                    "distinctive assets."
                ),
            },
            {
                "nome": "Tempo Médio na Página",
                "formula": "Soma tempo na página / Total de sessões",
                "faixa_tipica": "30s-2min para landing pages",
                "quando_usar": "Para avaliar qualidade do tráfego gerado",
                "descricao": (
                    "O Tempo Médio na Página mede quanto tempo os visitantes passam consumindo o conteúdo "
                    "de destino após clicarem no anúncio. Na etapa de Interesse, esta métrica é um "
                    "validador essencial de qualidade do tráfego: um tempo alto (30s-2min) indica que o "
                    "visitante encontrou conteúdo relevante e está explorando, enquanto tempo muito baixo "
                    "(<10s) sugere desalinhamento entre a promessa do anúncio e o conteúdo da página.\n\n"
                    "Sempre cruze o Tempo Médio com Páginas por Sessão e Taxa de Rejeição para uma visão "
                    "completa. Um visitante que passa 2 minutos lendo um artigo e depois navega para mais "
                    "2 páginas demonstra interesse genuíno — esse perfil de tráfego é o que alimenta a "
                    "progressão para a etapa de Consideração. Se o tempo é alto mas o bounce rate também "
                    "é alto (>70%), o conteúdo está engajando mas não oferece um próximo passo claro."
                ),
            },
        ],
        "terciarios": [
            {
                "nome": "Compartilhamentos",
                "formula": "Total de shares do conteúdo",
                "faixa_tipica": "0.1-0.5% das impressões",
                "quando_usar": "Indicador de conteúdo com potencial viral",
                "descricao": (
                    "Os Compartilhamentos medem quantas vezes o conteúdo foi ativamente "
                    "redistribuído pelos usuários para suas redes pessoais. Na etapa de Interesse, "
                    "compartilhar é o sinal mais forte de valor percebido — o usuário está "
                    "colocando sua reputação pessoal ao endossar o conteúdo para amigos e "
                    "seguidores. Taxas de compartilhamento de 0,1-0,5% sobre impressões são "
                    "típicas, sendo que conteúdo educacional e surpreendente tende a gerar mais "
                    "shares do que conteúdo puramente promocional.\n\n"
                    "Compartilhamentos também funcionam como multiplicador orgânico do investimento: "
                    "cada share gera exposição gratuita para uma audiência que confia na fonte "
                    "(o amigo que compartilhou), aumentando tanto alcance quanto credibilidade. "
                    "No Brasil, o WhatsApp é o principal canal de compartilhamento e não é "
                    "rastreável pelas plataformas (dark social), o que significa que os números "
                    "reportados subestimam significativamente o compartilhamento real."
                ),
            },
            {
                "nome": "Salvamentos",
                "formula": "Total de saves/bookmarks",
                "faixa_tipica": "0.2-1% do alcance",
                "quando_usar": "Sinal forte de intenção futura",
                "descricao": (
                    "Os Salvamentos (saves/bookmarks) indicam que o usuário considerou o conteúdo "
                    "valioso o suficiente para querer acessá-lo novamente no futuro. Na etapa de "
                    "Interesse, esta é uma das métricas mais reveladoras de intenção — quem salva "
                    "está sinalizando 'vou voltar a isso', o que demonstra interesse genuíno e "
                    "consideração futura. Taxas de 0,2-1% sobre o alcance são referência, sendo "
                    "que conteúdo utilitário (tutoriais, listas, guias) gera mais saves que "
                    "conteúdo inspiracional.\n\n"
                    "Nos algoritmos do Instagram e TikTok, salvamentos são um dos sinais mais "
                    "fortes de qualidade, pesando mais que curtidas na distribuição orgânica. "
                    "Para a etapa de Interesse, investir em conteúdo 'salvável' (checklists, "
                    "dicas práticas, infográficos com dados úteis) amplifica o alcance orgânico "
                    "e cria touchpoints futuros gratuitos quando o usuário revisita o conteúdo "
                    "salvo — reforçando a familiaridade com a marca sem custo adicional."
                ),
            },
            {
                "nome": "Impressões",
                "formula": "Total de exibições do anúncio",
                "faixa_tipica": "Depende de budget e CPM da plataforma",
                "quando_usar": "Para monitorar volume de exposição",
                "descricao": (
                    "As Impressões na etapa de Interesse contabilizam o total de exibições do "
                    "anúncio, incluindo repetições para a mesma pessoa. Embora o foco principal "
                    "em Interesse seja gerar cliques e engajamento (não apenas exposição), as "
                    "impressões servem como denominador essencial para calcular CTR e taxa de "
                    "engajamento, permitindo avaliar a eficiência dos criativos.\n\n"
                    "Monitorar impressões em Interesse também ajuda a identificar problemas de "
                    "entrega: se as impressões estão muito abaixo do esperado para o budget "
                    "investido, pode haver problemas de segmentação, lance ou aprovação de "
                    "criativos. Impressões desproporcionalmente altas em relação aos cliques "
                    "(CTR muito baixo) indicam que o conteúdo está sendo distribuído mas não "
                    "está despertando interesse — sinal para testar novos criativos ou revisar "
                    "a segmentação."
                ),
            },
            {
                "nome": "CPM",
                "formula": "(Custo total / Impressões) x 1000",
                "faixa_tipica": "R$8-25 dependendo da plataforma",
                "quando_usar": "Para monitorar eficiência de distribuição",
                "descricao": (
                    "O CPM (Custo por Mil Impressões) em Interesse indica o custo de entrega "
                    "do conteúdo para a audiência-alvo. Como terciário nesta etapa, o CPM é "
                    "monitorado para controle de eficiência mas não é o critério de otimização "
                    "— o CPC e CTR são mais relevantes porque refletem o objetivo de gerar "
                    "engajamento ativo, não apenas exposição.\n\n"
                    "CPMs em campanhas de Interesse tendem a ser ligeiramente mais altos que em "
                    "Awareness porque a segmentação é mais refinada (audiências de interesse "
                    "ou lookalike vs. broad). No Brasil, CPMs de R$8-25 são referência para "
                    "Meta Ads em campanhas de tráfego/engajamento. Se o CPM subir acima de "
                    "R$30, investigar: pode ser competição sazonal, audiência saturada ou "
                    "frequência excessiva no mesmo público."
                ),
            },
            {
                "nome": "Alcance",
                "formula": "Usuários únicos impactados",
                "faixa_tipica": "Varia por budget e segmentação",
                "quando_usar": "Para monitorar expansão de audiência",
                "descricao": (
                    "O Alcance em Interesse mede o número de pessoas únicas expostas ao conteúdo. "
                    "Diferentemente de Consciência (onde alcance é primário), em Interesse o "
                    "alcance é terciário porque o foco migra da amplitude da exposição para a "
                    "qualidade da interação — é preferível um alcance menor com alto CTR do "
                    "que alcance amplo sem engajamento.\n\n"
                    "Monitorar o alcance em Interesse é útil para garantir que a audiência "
                    "não está se esgotando: se o alcance cai enquanto as impressões sobem, "
                    "a frequência está aumentando e a campanha pode estar impactando as mesmas "
                    "pessoas repetidamente sem gerar novos cliques — sinal de fadiga que "
                    "exige rotação de criativos ou expansão de segmentação."
                ),
            },
            {
                "nome": "Frequência",
                "formula": "Impressões / Alcance",
                "faixa_tipica": "2-4 para interesse; monitorar fadiga",
                "quando_usar": "Para controlar saturação de audiência",
                "descricao": (
                    "A Frequência em Interesse indica quantas vezes, em média, cada pessoa viu "
                    "o anúncio. Para esta etapa, frequências de 2-4 são típicas e aceitáveis — "
                    "a audiência precisa de mais exposições para processar conteúdo de "
                    "aprofundamento do que conteúdo de awareness. Porém, acima de 5 exposições "
                    "sem conversão em clique, a fadiga se instala e o efeito se torna negativo.\n\n"
                    "A frequência ideal em Interesse depende do formato: vídeos longos podem "
                    "tolerar menor frequência (o conteúdo é mais denso), enquanto estáticos "
                    "podem precisar de mais repetições para fixar a mensagem. Cruzar frequência "
                    "com CTR ao longo do tempo revela o ponto de saturação: quando o CTR começa "
                    "a cair com a frequência subindo, é hora de trocar criativos."
                ),
            },
            {
                "nome": "Visualizações",
                "formula": "Total de visualizações do anúncio/vídeo",
                "faixa_tipica": "R$0.02-0.10 por view",
                "quando_usar": "Para medir volume de views em vídeo ou conteúdo",
                "descricao": (
                    "As Visualizações de vídeo em Interesse medem quantas vezes o conteúdo "
                    "audiovisual foi assistido. Na transição de Consciência para Interesse, "
                    "o foco muda de views de 3 segundos (exposição) para views mais longas "
                    "(ThruPlay/15s+), que demonstram engajamento real com o conteúdo. "
                    "Views curtas em Interesse sugerem que o gancho do vídeo não está "
                    "conectando com a audiência.\n\n"
                    "Para maximizar visualizações de qualidade nesta etapa, priorize "
                    "conteúdo educacional, demonstrações de produto e storytelling que "
                    "aprofunde o conhecimento sobre a marca. O custo por view (CPV) de "
                    "R$0,02-0,10 torna o vídeo um dos formatos mais eficientes para "
                    "nutrir interesse no mercado brasileiro."
                ),
            },
            {
                "nome": "Engajamento",
                "formula": "Curtidas + Comentários + Compartilhamentos + Salvamentos",
                "faixa_tipica": "1-3% de taxa sobre impressões",
                "quando_usar": "Indicador agregado de interação",
                "descricao": (
                    "O Engajamento total em Interesse soma todas as interações ativas com o "
                    "conteúdo. Na etapa de Interesse, taxas de engajamento de 1-3% sobre "
                    "impressões são típicas — mais altas que em Awareness porque o conteúdo "
                    "é mais direcionado e a audiência está mais receptiva à interação. "
                    "O engajamento nesta etapa valida que o conteúdo está cumprindo seu "
                    "papel de nutrir curiosidade e construir familiaridade.\n\n"
                    "Desagregue o engajamento para entender a qualidade: curtidas indicam "
                    "aprovação passiva, compartilhamentos indicam alto valor percebido, "
                    "salvamentos indicam intenção futura, e comentários indicam conversa ativa. "
                    "Cada tipo de engajamento revela algo diferente sobre a jornada do "
                    "consumidor na etapa de Interesse."
                ),
            },
            {
                "nome": "Comentários",
                "formula": "Total de comentários no anúncio",
                "faixa_tipica": "0.02-0.2% das impressões",
                "quando_usar": "Para medir nível de conversa e interesse ativo",
                "descricao": (
                    "Os Comentários em Interesse revelam o nível de conversa ativa que o "
                    "conteúdo está gerando. Taxas de 0,02-0,2% sobre impressões são referência. "
                    "Diferentemente de curtidas (reação instantânea), comentar exige reflexão "
                    "e formulação de pensamento, sendo um dos sinais mais fortes de que o "
                    "conteúdo provocou processamento cognitivo — exatamente o que a etapa de "
                    "Interesse busca: fazer a audiência pensar sobre a marca.\n\n"
                    "Analise o conteúdo dos comentários para extrair insights qualitativos: "
                    "perguntas sobre o produto indicam consideração; menções de amigos indicam "
                    "potencial viral; objeções de preço ou funcionalidade revelam barreiras "
                    "que o conteúdo de Consideração deve endereçar. No Brasil, responder "
                    "comentários rapidamente (dentro de 1 hora) gera loops de engajamento "
                    "que amplificam o alcance orgânico do post."
                ),
            },
            {
                "nome": "CPA",
                "formula": "Custo total / Total de conversões",
                "faixa_tipica": "R$20-150 dependendo do segmento",
                "quando_usar": "Para referência; não é foco em etapa de interesse",
                "descricao": (
                    "O CPA (Custo por Aquisição) em Interesse é uma métrica de referência, "
                    "não de otimização. Assim como em Awareness, o CPA tende a ser alto "
                    "nesta etapa porque o objetivo não é conversão direta, mas sim geração "
                    "de tráfego e engajamento que alimentem as etapas inferiores do funil. "
                    "Valores típicos de R$20-150 variam por segmento e modelo de negócio.\n\n"
                    "Registrar o CPA em Interesse serve para análises de atribuição "
                    "multi-touch: entender quanto custou cada touchpoint de interesse que "
                    "eventualmente contribuiu para uma conversão lá na frente. Modelos de "
                    "atribuição mais sofisticados (linear, time-decay, data-driven) "
                    "redistribuem crédito de conversão para esses touchpoints iniciais, "
                    "revelando o verdadeiro valor das campanhas de Interesse."
                ),
            },
            {
                "nome": "Custo Total",
                "formula": "Soma de todo investimento na campanha",
                "faixa_tipica": "= Budget alocado para a etapa",
                "quando_usar": "Para controlar gasto total vs. planejado",
                "descricao": (
                    "O Custo Total em Interesse representa o investimento acumulado nas "
                    "campanhas desta etapa do funil. Monitorar contra o budget planejado "
                    "garante aderência à estratégia de distribuição — se o plano alocava "
                    "20% do budget para Interesse e o gasto está em 30%, há desequilíbrio "
                    "que pode comprometer etapas posteriores.\n\n"
                    "O custo total deve ser cruzado com o volume de cliques e engajamento "
                    "gerado para calcular a eficiência global da etapa. Se o custo está "
                    "no planejado mas os cliques estão muito abaixo, o CPC está elevado e "
                    "intervenções são necessárias — testar novos criativos, ajustar "
                    "segmentação, ou redistribuir budget entre plataformas."
                ),
            },
            {
                "nome": "Custo Diário",
                "formula": "Custo total / Dias de veiculação",
                "faixa_tipica": "Budget / dias do período",
                "quando_usar": "Para monitorar pacing diário de investimento",
                "descricao": (
                    "O Custo Diário em Interesse permite monitorar o ritmo de investimento "
                    "ao longo da campanha. Em campanhas otimizadas para cliques ou engajamento, "
                    "o gasto diário pode variar mais do que em campanhas de alcance, pois o "
                    "algoritmo concentra investimento nos momentos de maior propensão a "
                    "engajamento da audiência.\n\n"
                    "Variações de até 20% no custo diário são normais em campanhas de Interesse "
                    "com budget vitalício. Flutuações maiores merecem investigação: podem "
                    "indicar que o algoritmo encontrou um público altamente responsivo (gasto "
                    "concentrado) ou que está tendo dificuldade de entregar (gasto disperso e "
                    "abaixo do planejado)."
                ),
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
                "descricao": (
                    "Na etapa de Consideração, o CTR assume um papel diferente do que na etapa de Interesse. Aqui, "
                    "a audiência já conhece a marca e demonstrou curiosidade inicial — agora está ativamente avaliando "
                    "opções e comparando soluções. Um CTR elevado nesta fase indica que o conteúdo de consideração "
                    "(depoimentos, demos, comparativos, cases de sucesso) está efetivamente convencendo a audiência a "
                    "aprofundar a avaliação. Conforme o modelo McKinsey CDJ, os touchpoints durante a avaliação ativa "
                    "são 2-3x mais influentes do que durante a consideração inicial.\n\n"
                    "Os benchmarks de CTR para consideração são naturalmente mais altos que para awareness (1,0-3,0% "
                    "vs 0,3-1,5%) porque a audiência já possui intenção. No Google Ads Search, termos de comparação "
                    "('melhor X', 'X vs Y', 'review de X') alcançam CTRs de 3-8%. Em remarketing de visitantes do "
                    "site, CTRs de 2-5% são comuns porque a audiência já demonstrou familiaridade.\n\n"
                    "Para maximizar o CTR em consideração, o conteúdo deve abordar diretamente as dúvidas e objeções "
                    "do prospect. Prova social (Cialdini) torna-se o mecanismo de persuasão dominante: depoimentos, "
                    "avaliações, números de clientes e cases de sucesso com resultados mensuráveis são os formatos "
                    "que mais impulsionam o CTR nesta etapa."
                ),
            },
            {
                "nome": "CPC",
                "formula": "Custo total / Cliques",
                "faixa_tipica": "R$0.50-5.00 dependendo da plataforma",
                "quando_usar": "Para otimizar custo de engajamento qualificado",
                "descricao": (
                    "O CPC na etapa de Consideração reflete o custo de engajar uma audiência que já está avaliando "
                    "soluções. Diferentemente da etapa de Interesse, onde qualquer clique conta, aqui o CPC deve ser "
                    "avaliado em conjunto com a qualidade do engajamento pós-clique. Um CPC mais alto pode ser "
                    "perfeitamente aceitável se os cliques resultam em tempo elevado no site, múltiplas páginas "
                    "visitadas, e micro-conversões (download de material, inscrição em webinar, solicitação de demo).\n\n"
                    "Conforme a teoria de Binet & Field, a etapa de Consideração marca o território de Ativação, "
                    "onde a mensagem pode ser mais racional e focada em features/benefícios. Audiências de "
                    "remarketing (visitantes do site, engajadores profundos) tendem a ter CPCs menores e qualidade "
                    "de clique superior. No Brasil, CPCs de consideração variam de R$0,50-5,00 em social media e "
                    "R$1,00-8,00 em search, sendo que keywords de comparação e avaliação possuem CPC moderado mas "
                    "alta taxa de conversão posterior."
                ),
            },
            {
                "nome": "Taxa de Engajamento",
                "formula": "(Engajamentos / Alcance) x 100",
                "faixa_tipica": "2-6% para conteúdo de consideração",
                "quando_usar": "Para medir profundidade de avaliação",
                "descricao": (
                    "A Taxa de Engajamento na Consideração mede o percentual de pessoas alcançadas que interagiram "
                    "ativamente com o conteúdo — curtidas, comentários, compartilhamentos, salvamentos, cliques. "
                    "Diferentemente de etapas anteriores, aqui o engajamento tem um peso qualitativo maior: "
                    "comentários com dúvidas sobre o produto indicam avaliação ativa, salvamentos sugerem intenção "
                    "de retornar ao conteúdo, e compartilhamentos significam que a pessoa considera a informação "
                    "valiosa o suficiente para repassar à sua rede.\n\n"
                    "Na prática, uma taxa de engajamento de 2-6% é considerada saudável para conteúdo de "
                    "consideração. Taxas acima de 3% indicam forte ressonância. O engajamento deve ser medido "
                    "sobre o alcance (não sobre impressões), pois isso reflete o percentual real de pessoas que "
                    "escolheram interagir. Pesquisas do mercado B2B mostram que compradores interagem com 3-7 "
                    "peças de conteúdo antes de falar com vendas, tornando a taxa de engajamento em cada peça "
                    "um indicador de progressão no funil de avaliação."
                ),
            },
        ],
        "secundarios": [
            {
                "nome": "ThruPlay",
                "formula": "Vídeos assistidos até o final ou 15s+",
                "faixa_tipica": "20-50% completion rate",
                "quando_usar": "Para conteúdo educativo/demonstrativo",
                "descricao": (
                    "Na etapa de Consideração, o ThruPlay ganha importância especial quando "
                    "usado para vídeos de demonstração de produto, depoimentos de clientes e "
                    "comparativos. Taxas de 20-50% são esperadas — maiores que na etapa de "
                    "Interesse porque a audiência já está avaliando ativamente. Um prospect "
                    "que assiste a um demo completo de 2 minutos está significativamente mais "
                    "avançado na jornada de compra do que quem apenas viu um vídeo educacional.\n\n"
                    "Cruzar ThruPlay com micro-conversões (solicitação de orçamento, download de "
                    "case study) permite identificar quais vídeos estão efetivamente movendo prospects "
                    "da consideração para a intenção. No McKinsey CDJ, os touchpoints na fase de "
                    "Avaliação Ativa são 2-3x mais influentes que na consideração inicial, o que "
                    "torna cada ThruPlay de um vídeo de demo um ponto de contato de alto valor."
                ),
            },
            {
                "nome": "Cliques no Link",
                "formula": "Cliques que levam ao site/landing page",
                "faixa_tipica": "60-80% dos cliques totais são no link",
                "quando_usar": "Para medir intenção de saber mais",
                "descricao": (
                    "Cliques no Link distinguem interações que levam o usuário para fora da plataforma "
                    "(ao site, landing page ou app) de cliques internos (expandir texto, ver perfil). "
                    "Na Consideração, é uma métrica de suporte essencial porque confirma que a audiência "
                    "não está apenas engajando superficialmente na plataforma — está dando o passo de "
                    "sair para avaliar a oferta em profundidade. Espera-se que 60-80% dos cliques totais "
                    "sejam cliques no link em campanhas de consideração bem-direcionadas.\n\n"
                    "Se o percentual de cliques no link for baixo (<50%), pode indicar que os criativos "
                    "geram curiosidade visual mas não fornecem motivação suficiente para investigar mais. "
                    "A solução é reforçar o CTA no criativo e alinhar a promessa do anúncio com o "
                    "conteúdo da página de destino — o desalinhamento entre anúncio e destino é um dos "
                    "erros mais comuns da etapa de Consideração."
                ),
            },
            {
                "nome": "CPM",
                "formula": "(Custo total / Impressões) x 1000",
                "faixa_tipica": "R$12-35 para audiências mais qualificadas",
                "quando_usar": "Para monitorar eficiência de distribuição",
                "descricao": (
                    "Na Consideração, o CPM é uma métrica de monitoramento (não de sucesso) que reflete "
                    "o custo de distribuir conteúdo para audiências mais qualificadas. CPMs entre R$12-35 "
                    "são típicos para audiências de remarketing e lookalikes qualificadas no Brasil — "
                    "naturalmente mais altos que em Awareness porque a audiência é mais restrita e valiosa. "
                    "Um CPM crescente não é necessariamente negativo se os KPIs primários (CTR, engajamento "
                    "profundo, micro-conversões) também estão crescendo.\n\n"
                    "Atenção: usar CPM como métrica de sucesso em Consideração é um erro conceitual. O "
                    "CPM é métrica primária de Awareness. Na Consideração, serve apenas como indicador de "
                    "eficiência de distribuição e como componente de cálculo para projetar volumes de "
                    "cliques e conversões."
                ),
            },
            {
                "nome": "Bounce Rate",
                "formula": "(Sessões de página única / Total sessões) x 100",
                "faixa_tipica": "30-60% para landing pages de campanha",
                "quando_usar": "Para avaliar relevância do tráfego",
                "descricao": (
                    "A Bounce Rate (Taxa de Rejeição) mede o percentual de visitantes que acessam a "
                    "página de destino e saem sem interagir mais. Na etapa de Consideração, uma bounce "
                    "rate entre 30-60% é referência para landing pages de campanha. Abaixo de 30% é "
                    "excelente e indica conteúdo altamente relevante para a audiência. Acima de 70% é "
                    "um sinal de alerta que indica desalinhamento entre o criativo/anúncio e o conteúdo "
                    "da página, segmentação inadequada ou problemas de UX/carregamento.\n\n"
                    "É um indicador INVERSO — quanto menor, melhor. Na Consideração, cruze bounce rate "
                    "com tempo na página e páginas por sessão: um visitante que permanece 3 minutos em "
                    "uma página de comparação e depois navega para a página de preços está em avaliação "
                    "ativa (McKinsey CDJ). Já um visitante que sai em 5 segundos provavelmente recebeu "
                    "uma mensagem desalinhada no anúncio."
                ),
            },
        ],
        "terciarios": [
            {
                "nome": "Páginas por Sessão",
                "formula": "Total pageviews / Total sessões",
                "faixa_tipica": "1.5-3.0 páginas por sessão",
                "quando_usar": "Para medir exploração do site",
                "descricao": (
                    "Páginas por Sessão mede a média de páginas que cada visitante explora "
                    "após clicar no anúncio. Na etapa de Consideração, este é um dos indicadores "
                    "mais reveladores de avaliação ativa: um prospect que navega de 1,5 a 3 "
                    "páginas está comparando opções, lendo depoimentos e explorando "
                    "funcionalidades — comportamento típico de quem está decidindo entre "
                    "alternativas, conforme descrito pelo McKinsey Consumer Decision Journey.\n\n"
                    "Combine páginas por sessão com as páginas específicas visitadas (pricing, "
                    "features, cases, sobre nós) para mapear o percurso de avaliação. Se a "
                    "maioria dos visitantes acessa a página de produto e sai sem ver preços, "
                    "pode haver uma barreira de confiança ou informação insuficiente. Valores "
                    "abaixo de 1,5 em Consideração indicam que o site não está facilitando "
                    "a exploração — revisar navegação, conteúdo e CTAs internos."
                ),
            },
            {
                "nome": "Custo por Engajamento",
                "formula": "Custo total / Total de engajamentos",
                "faixa_tipica": "R$0.10-1.00 por engajamento",
                "quando_usar": "Para otimizar custo de interação",
                "descricao": (
                    "O Custo por Engajamento (CPE) indica quanto cada interação ativa com o "
                    "conteúdo está custando. Em Consideração, CPEs entre R$0,10-1,00 são "
                    "referência, sendo que engajamentos mais valiosos (comentários, "
                    "compartilhamentos, salvamentos) naturalmente custam mais que curtidas. "
                    "O CPE é útil para comparar a eficiência de diferentes formatos e "
                    "criativos dentro da mesma etapa.\n\n"
                    "Porém, o CPE deve ser contextualizado: um criativo com CPE de R$0,50 "
                    "que gera engajamentos superficiais (curtidas) é menos valioso que um "
                    "com CPE de R$1,50 que gera comentários com dúvidas sobre o produto — "
                    "o segundo indica avaliação ativa, o primeiro pode ser apenas apreciação "
                    "estética. Em Consideração, priorize a qualidade do engajamento sobre "
                    "o custo unitário."
                ),
            },
            {
                "nome": "Cliques",
                "formula": "Total de cliques no anúncio",
                "faixa_tipica": "Depende de CTR e volume de impressões",
                "quando_usar": "Para medir volume de tráfego gerado",
                "descricao": (
                    "O volume total de Cliques em Consideração mede quantas interações ativas "
                    "a campanha gerou. Como terciário nesta etapa, os cliques são um "
                    "componente de cálculo (CTR, CPC) mais do que um indicador isolado de "
                    "sucesso. A qualidade do clique importa mais que o volume: 500 cliques "
                    "que resultam em 50 micro-conversões valem mais que 5.000 cliques com "
                    "90% de bounce rate.\n\n"
                    "Em Consideração, diferencie cliques totais de cliques no link (outbound). "
                    "Cliques que levam o usuário ao site/landing page são mais valiosos do que "
                    "cliques no perfil ou expansão de imagem. O Meta Ads reporta ambos — "
                    "foque no 'Link Clicks' para avaliar a geração real de tráfego qualificado "
                    "para avaliação."
                ),
            },
            {
                "nome": "Impressões",
                "formula": "Total de exibições do anúncio",
                "faixa_tipica": "Depende de budget e CPM",
                "quando_usar": "Para monitorar volume de exposição",
                "descricao": (
                    "As Impressões em Consideração servem como denominador para cálculo de "
                    "CTR e taxa de engajamento, não como métrica de sucesso isolada. O volume "
                    "de impressões nesta etapa é tipicamente menor que em Awareness e Interesse "
                    "porque as audiências são mais restritas (remarketing, custom audiences) "
                    "e qualificadas.\n\n"
                    "Se as impressões estão muito abaixo do budget alocado, pode indicar que "
                    "a audiência de remarketing é muito pequena — sinal para ampliar a "
                    "captação de audiência nas etapas superiores do funil. Esta é a lógica "
                    "de interdependência de etapas: Consideração depende de Interesse, que "
                    "depende de Consciência."
                ),
            },
            {
                "nome": "Alcance",
                "formula": "Usuários únicos impactados",
                "faixa_tipica": "Varia por budget e segmentação",
                "quando_usar": "Para monitorar expansão de audiência",
                "descricao": (
                    "O Alcance em Consideração mede quantas pessoas únicas foram expostas ao "
                    "conteúdo de avaliação. Nesta etapa, o alcance é naturalmente menor porque "
                    "estamos falando com um subconjunto qualificado da audiência de Interesse. "
                    "Comparar o alcance de Consideração com o de Interesse revela a taxa de "
                    "progressão do funil — idealmente 20-40% da audiência de Interesse deve "
                    "ser alcançada em Consideração.\n\n"
                    "Um alcance muito baixo em Consideração pode indicar que poucas pessoas "
                    "estão avançando no funil (problema de qualidade do tráfego anterior) ou "
                    "que a segmentação de remarketing é muito restritiva. Expanda as janelas "
                    "de remarketing (de 7 para 14-30 dias) se o alcance for insuficiente."
                ),
            },
            {
                "nome": "Frequência",
                "formula": "Impressões / Alcance",
                "faixa_tipica": "2-5 para consideração",
                "quando_usar": "Para controlar saturação; frequência maior aceitável nesta etapa",
                "descricao": (
                    "A Frequência em Consideração pode ser mais alta que nas etapas anteriores "
                    "(2-5 vs 1,5-3 em Awareness) porque a audiência está ativamente avaliando "
                    "e mais receptiva a múltiplas exposições. Prospects em fase de comparação "
                    "frequentemente precisam ver a mensagem mais vezes para processar "
                    "informações racionais (features, preços, depoimentos).\n\n"
                    "Porém, acima de 6 a audiência de remarketing provavelmente já decidiu — "
                    "ou pela marca ou por um concorrente. Frequência excessiva em Consideração "
                    "pode ser desperdício de budget que seria mais bem investido em ampliar "
                    "o funil (Awareness/Interesse) ou em oferecer um incentivo de conversão "
                    "(Intenção)."
                ),
            },
            {
                "nome": "Visualizações",
                "formula": "Total de visualizações do anúncio/vídeo",
                "faixa_tipica": "R$0.02-0.10 por view",
                "quando_usar": "Para medir consumo de conteúdo demonstrativo",
                "descricao": (
                    "As Visualizações de vídeo em Consideração focam em conteúdo demonstrativo "
                    "e de prova social: demos de produto, walkthroughs, depoimentos de clientes, "
                    "comparativos detalhados. Nesta etapa, a taxa de conclusão é mais importante "
                    "que o volume bruto de views — um prospect que assiste 95% de um vídeo de "
                    "demo está muito mais qualificado que um que assiste 10%.\n\n"
                    "Vídeos de consideração tendem a ser mais longos (30s-3min) e informativos. "
                    "CPVs de R$0,02-0,10 são referência, mas o valor real está no conteúdo "
                    "consumido: vídeos que respondem objeções específicas (preço, funcionalidade, "
                    "confiança) têm impacto desproporcional na progressão para Intenção."
                ),
            },
            {
                "nome": "Engajamento",
                "formula": "Curtidas + Comentários + Compartilhamentos + Salvamentos",
                "faixa_tipica": "2-6% de taxa para conteúdo de consideração",
                "quando_usar": "Indicador de avaliação ativa do conteúdo",
                "descricao": (
                    "O Engajamento total em Consideração reflete a interação ativa com conteúdo "
                    "de avaliação. Taxas de 2-6% são típicas — mais altas que em Interesse "
                    "porque o conteúdo é mais relevante para uma audiência que já conhece a "
                    "marca. Cada tipo de engajamento tem significado diferente nesta etapa: "
                    "salvamentos indicam 'vou voltar para comparar', compartilhamentos indicam "
                    "'confio o suficiente para recomendar', comentários indicam 'tenho dúvidas "
                    "específicas'.\n\n"
                    "Analise o mix de engajamento, não apenas o total. Em Consideração, "
                    "comentários com perguntas sobre funcionalidades, preços ou disponibilidade "
                    "são os sinais mais valiosos — indicam prospects em avaliação ativa que "
                    "podem ser convertidos com uma resposta rápida e informativa."
                ),
            },
            {
                "nome": "Comentários",
                "formula": "Total de comentários no anúncio",
                "faixa_tipica": "0.02-0.3% das impressões",
                "quando_usar": "Para medir dúvidas e interesse qualificado",
                "descricao": (
                    "Os Comentários em Consideração são particularmente valiosos porque "
                    "frequentemente contêm perguntas específicas sobre o produto ou serviço: "
                    "'Funciona para X?', 'Quanto custa?', 'Tem desconto para Y?'. Estas são "
                    "sinais claros de intenção comercial e oportunidades de conversão. "
                    "Taxas de 0,02-0,3% sobre impressões são referência, sendo que conteúdo "
                    "de comparação tende a gerar mais comentários.\n\n"
                    "Implementar um protocolo de resposta rápida a comentários em Consideração "
                    "pode transformar essa métrica de monitoramento em canal de vendas. "
                    "Responder dentro de 1 hora com informações úteis e personalizadas "
                    "demonstra atenção e pode ser o empurrão final para a conversão. "
                    "No Brasil, 76% dos consumidores esperam resposta em até 24h nas redes."
                ),
            },
            {
                "nome": "CPA",
                "formula": "Custo total / Total de conversões",
                "faixa_tipica": "R$20-150 dependendo do segmento",
                "quando_usar": "Para referência de custo de micro-conversões",
                "descricao": (
                    "O CPA em Consideração mede o custo por micro-conversão — ações que "
                    "demonstram avaliação avançada como download de material, inscrição em "
                    "webinar, solicitação de demo ou cadastro em newsletter. CPAs de R$20-150 "
                    "são típicos dependendo do segmento, sendo que B2B tolera CPAs maiores "
                    "devido ao ticket médio mais alto.\n\n"
                    "Diferente de Awareness/Interesse onde o CPA é apenas referência, em "
                    "Consideração ele começa a ter relevância estratégica porque as "
                    "micro-conversões são indicadores concretos de progressão no funil. "
                    "Comparar o CPA de diferentes micro-conversões revela quais ações "
                    "geram leads mais qualificados ao menor custo."
                ),
            },
            {
                "nome": "Custo Total",
                "formula": "Soma de todo investimento na campanha",
                "faixa_tipica": "= Budget alocado para a etapa",
                "quando_usar": "Para controlar gasto total vs. planejado",
                "descricao": (
                    "O Custo Total em Consideração representa o investimento acumulado em "
                    "campanhas de meio de funil. Esta etapa tipicamente recebe 15-25% do "
                    "budget total conforme frameworks de alocação. Monitorar o gasto contra "
                    "o planejado garante que a estratégia de full-funnel está sendo "
                    "respeitada e que recursos não estão sendo realocados de forma reativa.\n\n"
                    "Cruze o custo total com o volume de micro-conversões para calcular a "
                    "eficiência global da etapa. Se o custo está no orçamento mas as "
                    "micro-conversões estão abaixo, a eficiência está comprometida e "
                    "intervenções são necessárias — testar landing pages, revisar ofertas "
                    "ou ajustar criativos de consideração."
                ),
            },
            {
                "nome": "Custo Diário",
                "formula": "Custo total / Dias de veiculação",
                "faixa_tipica": "Budget / dias do período",
                "quando_usar": "Para monitorar pacing diário de investimento",
                "descricao": (
                    "O Custo Diário em Consideração controla o ritmo de investimento ao "
                    "longo da campanha. Campanhas de remarketing nesta etapa podem ter "
                    "variações de gasto maiores porque dependem do volume de audiência "
                    "gerada nas etapas anteriores — se uma campanha de Awareness teve "
                    "pico de alcance na semana passada, a audiência de remarketing de "
                    "Consideração cresce e o gasto pode aumentar nos dias seguintes.\n\n"
                    "Monitorar essa dinâmica de interdependência entre etapas ajuda a "
                    "entender o fluxo do funil: o custo diário de Consideração deve "
                    "acompanhar, com lag de 3-7 dias, os picos de tráfego gerados por "
                    "Interesse e Awareness."
                ),
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
                "descricao": (
                    "Leads Gerados é a contagem total de contatos qualificados capturados pela campanha — formulários "
                    "preenchidos, cadastros realizados, solicitações de orçamento, agendamentos de demonstração ou "
                    "qualquer ação que transforme um visitante anônimo em um contato identificável no funil de vendas. "
                    "Na etapa de Intenção, este é o KPI principal porque representa a transição concreta do interesse "
                    "para a ação: a pessoa não apenas se interessou pelo conteúdo, ela forneceu seus dados em troca "
                    "de algo, sinalizando disposição para avançar no relacionamento comercial.\n\n"
                    "Conforme o modelo STDC de Kaushik, esta é a fase 'Think' avançada / 'Do' inicial, onde o "
                    "prospect possui intenção comercial formada e está buscando a confirmação final. O volume de "
                    "leads depende de três variáveis: o tráfego qualificado gerado (cliques), a taxa de conversão "
                    "da landing page/formulário, e a relevância da oferta (lead magnet). Pesquisas mostram que leads "
                    "contatados nos primeiros 5 minutos têm 9x mais probabilidade de converter do que aqueles "
                    "contatados após 30 minutos.\n\n"
                    "É fundamental diferenciar volume de qualidade. Leads baratos que nunca convertem consomem "
                    "recursos de vendas sem retorno. Por isso, o volume de leads deve sempre ser cruzado com a "
                    "taxa de qualificação (MQL para SQL) e com o CPL para avaliar a eficiência real da campanha."
                ),
            },
            {
                "nome": "CPL (Custo por Lead)",
                "formula": "Custo total / Total de leads",
                "faixa_tipica": "R$5-50 (B2C); R$30-200 (B2B)",
                "quando_usar": "Para avaliar eficiência de captação",
                "descricao": (
                    "O CPL (Custo por Lead) revela quanto a campanha está pagando, em média, para capturar cada "
                    "lead. É calculado dividindo o investimento total pelo número de leads gerados. Na etapa de "
                    "Intenção, o CPL é o termômetro de eficiência financeira: ele conecta o investimento em mídia "
                    "ao resultado tangível de geração de pipeline. Um CPL saudável depende do segmento — B2C "
                    "tipicamente opera entre R$5-50 por lead, enquanto B2B pode variar de R$30-200, refletindo "
                    "o maior valor de cada oportunidade comercial.\n\n"
                    "O CPL está diretamente ligado ao CPC e à taxa de conversão da landing page pela fórmula: "
                    "CPL = CPC / Taxa de Conversão. Isso significa que existem duas alavancas para reduzir o CPL: "
                    "diminuir o CPC (melhorando qualidade dos anúncios e segmentação) ou aumentar a taxa de "
                    "conversão (otimizando a landing page, formulário e oferta). No Brasil, o Meta Ads Lead Ads "
                    "oferece CPLs competitivos por eliminar a fricção de redirecionamento ao site, e o WhatsApp "
                    "Click-to-Chat está se tornando o canal de captura de leads mais eficiente do mercado.\n\n"
                    "Atenção ao erro clássico: otimizar puramente por CPL mais baixo sem considerar a qualidade "
                    "downstream. 100 leads a R$5 que não convertem custam mais do que 10 leads a R$50 com 30% de "
                    "taxa de fechamento. Sempre cruze o CPL com métricas de qualidade (taxa SQL, pipeline gerado)."
                ),
            },
            {
                "nome": "Taxa de Conversão de Lead",
                "formula": "(Leads / Cliques) x 100",
                "faixa_tipica": "2-10% dependendo da oferta e segmento",
                "quando_usar": "Para otimizar landing pages e ofertas",
                "descricao": (
                    "A Taxa de Conversão de Lead mede o percentual de visitantes (cliques) que efetivamente se "
                    "tornaram leads ao preencher um formulário, fazer um cadastro ou realizar outra ação de "
                    "captura. É calculada dividindo o total de leads pelo total de cliques e multiplicando por 100. "
                    "Se 1.000 pessoas clicaram no anúncio e 50 preencheram o formulário, a taxa é de 5%. "
                    "Esta métrica é o diagnóstico da eficiência da landing page e da oferta: se muitas pessoas "
                    "clicam mas poucas convertem, o problema está entre o anúncio e a ação final.\n\n"
                    "Benchmarks variam por contexto: landing pages com foco único convertem em média 6,6% "
                    "(mediana do mercado), podendo chegar a 10-15% com otimização agressiva. Lead magnets de "
                    "alto valor percebido (ferramentas gratuitas, calculadoras, consultorias) convertem mais que "
                    "conteúdos genéricos. Cada campo adicional no formulário reduz a taxa de conversão em 5-10%, "
                    "por isso formulários de intenção devem capturar o mínimo viável (nome, email, telefone) e "
                    "qualificar em etapas posteriores.\n\n"
                    "A taxa de conversão é especialmente importante no cruzamento com CPC para determinar o CPL: "
                    "se o CPC é R$2,00 e a taxa de conversão é 5%, o CPL é R$40,00. Melhorar a taxa de conversão "
                    "de 5% para 7% reduziria o CPL para R$28,57 — uma economia de 28% sem alterar o investimento."
                ),
            },
        ],
        "secundarios": [
            {
                "nome": "Adições ao Carrinho",
                "formula": "Total de add-to-cart events",
                "faixa_tipica": "5-15% do tráfego para e-commerce",
                "quando_usar": "Para e-commerce; mede intenção de compra",
                "descricao": (
                    "Adições ao Carrinho medem o número de vezes que um produto foi adicionado ao "
                    "carrinho de compras. Na etapa de Intenção, é um dos sinais mais fortes de intenção "
                    "de compra no e-commerce — o prospect avaliou o produto e deu o primeiro passo "
                    "concreto em direção à transação. Taxas de 5-15% do tráfego são referência para "
                    "e-commerce no Brasil. Cada adição ao carrinho representa um prospect que pode "
                    "ser recuperado via remarketing caso não conclua a compra.\n\n"
                    "A taxa de abandono de carrinho média é de 70%, o que torna as Adições ao Carrinho "
                    "um estágio crítico do funil. Cruzar com Inícios de Checkout permite identificar "
                    "onde a fricção ocorre: se muitos adicionam mas poucos iniciam o checkout, o problema "
                    "pode ser frete, preço final ou falta de opções de pagamento. Campanhas de "
                    "recuperação via WhatsApp no Brasil alcançam valor médio de R$557,67 por carrinho "
                    "recuperado."
                ),
            },
            {
                "nome": "Inícios de Checkout",
                "formula": "Total de initiate-checkout events",
                "faixa_tipica": "40-70% dos que adicionaram ao carrinho",
                "quando_usar": "Para medir avanço no funil de compra",
                "descricao": (
                    "Inícios de Checkout contam quantos usuários avançaram da adição ao carrinho para "
                    "o processo de checkout. Na etapa de Intenção, é o penúltimo passo antes da conversão "
                    "e indica intenção de compra quase concretizada. A taxa esperada é de 40-70% dos "
                    "que adicionaram ao carrinho — se estiver abaixo de 40%, há fricção significativa "
                    "no caminho (custos surpresa de frete, falta de Pix/boleto, cadastro obrigatório).\n\n"
                    "No contexto brasileiro, a inclusão de Pix como opção de pagamento e a exibição "
                    "clara de parcelamento ('12x sem juros') no início do checkout são fatores que "
                    "elevam significativamente esta taxa. A diferença entre Adições ao Carrinho e "
                    "Inícios de Checkout é um dos melhores diagnósticos de UX do e-commerce: cada ponto "
                    "de melhoria neste gap se traduz diretamente em receita."
                ),
            },
            {
                "nome": "CPC",
                "formula": "Custo total / Cliques",
                "faixa_tipica": "R$1.00-8.00 para público de intenção",
                "quando_usar": "Para monitorar custo de tráfego qualificado",
                "descricao": (
                    "Na etapa de Intenção, o CPC reflete o custo de atrair tráfego com alta qualificação "
                    "de compra. CPCs entre R$1-8 são típicos para audiências de intenção no Brasil, "
                    "naturalmente mais altos que em etapas anteriores porque a audiência é mais valiosa "
                    "e a competição por estes cliques é maior (especialmente em Search Ads para "
                    "palavras-chave transacionais como 'comprar', 'preço', 'perto de mim').\n\n"
                    "O CPC em Intenção deve SEMPRE ser cruzado com CPL e taxa de conversão do lead. "
                    "Um CPC alto que gera leads de alta qualidade (SQL rate >30%) é superior a um CPC "
                    "baixo que gera leads frios. A otimização não é reduzir o CPC ao mínimo, mas "
                    "maximizar a relação entre custo do clique e qualidade do lead gerado."
                ),
            },
        ],
        "terciarios": [
            {
                "nome": "Downloads/Inscrições",
                "formula": "Total de downloads ou inscrições",
                "faixa_tipica": "Varia por tipo de material",
                "quando_usar": "Para ofertas de conteúdo rico (ebooks, webinars)",
                "descricao": (
                    "Downloads e Inscrições medem ações específicas de captura em campanhas "
                    "de lead generation: downloads de ebooks, whitepapers, templates; inscrições "
                    "em webinars, newsletters ou ferramentas gratuitas. Na Intenção, cada "
                    "download/inscrição é uma micro-conversão que captura dados do prospect "
                    "e sinaliza interesse específico no tema — informação valiosa para "
                    "segmentação e nutrição posterior.\n\n"
                    "O volume e tipo de download revela o estágio de decisão do prospect: "
                    "downloads de conteúdo educacional indicam exploração inicial, enquanto "
                    "downloads de comparativos, planilhas de ROI ou ferramentas de cálculo "
                    "indicam avaliação avançada. Esta distinção permite segmentar leads por "
                    "maturidade e personalizar as sequências de nutrição."
                ),
            },
            {
                "nome": "Mensagens Recebidas",
                "formula": "Total de mensagens via Messenger/WhatsApp/DM",
                "faixa_tipica": "R$1-10 por mensagem recebida",
                "quando_usar": "Para campanhas com CTA de mensagem",
                "descricao": (
                    "Mensagens Recebidas contam o total de conversas iniciadas pelos usuários "
                    "via Messenger, WhatsApp Business ou Direct Message. No Brasil, onde o "
                    "WhatsApp tem 99% de penetração e 55% de taxa de conversão em campanhas "
                    "de vendas, esta métrica é especialmente estratégica para a etapa de "
                    "Intenção. O custo por mensagem (R$1-10) frequentemente resulta em CPL "
                    "efetivo muito competitivo porque a conversa direta acelera a qualificação.\n\n"
                    "Campanhas Click-to-WhatsApp são um dos formatos mais eficientes do "
                    "Meta Ads no Brasil para Intenção. A conversa direta permite qualificar "
                    "o lead em tempo real, tirar dúvidas e direcionar para a conversão — "
                    "tudo dentro do canal preferido do consumidor brasileiro, eliminando "
                    "fricção de redirecionamento para landing pages."
                ),
            },
            {
                "nome": "Impressões",
                "formula": "Total de exibições do anúncio",
                "faixa_tipica": "Depende de budget e CPM",
                "quando_usar": "Para monitorar volume de exposição",
                "descricao": (
                    "As Impressões em Intenção servem como indicador de volume de entrega "
                    "e denominador para cálculos de CTR. Nesta etapa, o volume de impressões "
                    "é tipicamente menor que em etapas superiores porque a audiência é "
                    "mais restrita e qualificada — remarketing de visitantes, custom "
                    "audiences e lookalikes de compradores.\n\n"
                    "Impressões muito abaixo do esperado em Intenção podem indicar que o "
                    "funil superior não está gerando audiência suficiente. Impressões muito "
                    "acima com poucos leads sugerem que a segmentação está incluindo "
                    "audiências pouco qualificadas que diluem a eficiência."
                ),
            },
            {
                "nome": "Cliques",
                "formula": "Total de cliques no anúncio",
                "faixa_tipica": "Depende de CTR e volume de impressões",
                "quando_usar": "Para medir volume de tráfego qualificado",
                "descricao": (
                    "Os Cliques em Intenção representam o tráfego direcionado à landing page "
                    "de captura de leads ou checkout. Nesta etapa, cada clique tem custo e "
                    "valor maiores que em etapas anteriores porque a audiência é mais "
                    "qualificada e a expectativa de conversão é maior. O volume de cliques "
                    "é o 'input' do funil de conversão: Cliques x Taxa de Conversão = Leads.\n\n"
                    "Monitorar o volume de cliques vs. leads/conversões permite calcular a "
                    "taxa de conversão em tempo real e identificar rapidamente quedas de "
                    "performance na landing page. Se os cliques estão estáveis mas os leads "
                    "caíram, o problema está na página de destino, não no anúncio."
                ),
            },
            {
                "nome": "CTR",
                "formula": "(Cliques / Impressões) x 100",
                "faixa_tipica": "1-3% para campanhas de intenção",
                "quando_usar": "Para monitorar eficiência dos criativos",
                "descricao": (
                    "O CTR em Intenção reflete a eficácia dos criativos em motivar uma "
                    "audiência já qualificada a clicar. Taxas de 1-3% são típicas, podendo "
                    "chegar a 5%+ em remarketing de abandono de carrinho ou audiências "
                    "muito quentes. Um CTR nesta faixa confirma que a mensagem e a oferta "
                    "estão alinhadas com a intenção da audiência.\n\n"
                    "CTR abaixo de 1% em Intenção é preocupante: se a audiência tem intenção "
                    "mas não clica, o criativo pode estar genérico demais ou não comunicar "
                    "a urgência/benefício da oferta. Testes A/B de CTA (ex: 'Baixe grátis' "
                    "vs 'Agende uma demo' vs 'Fale com um especialista') geralmente revelam "
                    "qual abordagem melhor converte esta audiência específica."
                ),
            },
            {
                "nome": "CPM",
                "formula": "(Custo total / Impressões) x 1000",
                "faixa_tipica": "R$15-40 para audiências de intenção",
                "quando_usar": "Para monitorar custo de distribuição",
                "descricao": (
                    "O CPM em Intenção é naturalmente mais elevado (R$15-40) do que em "
                    "etapas anteriores porque as audiências são mais restritas e valiosas — "
                    "remarketing, custom audiences de visitantes, e lookalikes de "
                    "compradores. A competição por essas audiências no leilão publicitário "
                    "eleva o custo de distribuição.\n\n"
                    "Como terciário em Intenção, o CPM é monitorado apenas para controle — "
                    "a métrica de eficiência relevante é o CPL, não o CPM. Um CPM alto "
                    "com CPL baixo é perfeitamente aceitável: significa que o algoritmo "
                    "está alcançando as pessoas certas (caras de alcançar, mas baratas "
                    "de converter)."
                ),
            },
            {
                "nome": "CPA",
                "formula": "Custo total / Total de conversões",
                "faixa_tipica": "R$20-150 dependendo do segmento",
                "quando_usar": "Para avaliar custo de micro-conversões (leads, cadastros)",
                "descricao": (
                    "O CPA em Intenção mede o custo por ação de conversão completada. "
                    "Nesta etapa, o CPA é mais operacional que nas anteriores — já não é "
                    "apenas referência, mas sim um indicador ativo de eficiência. CPAs de "
                    "R$20-150 são típicos dependendo do segmento, sendo que B2B tolera "
                    "CPAs mais altos pelo valor do cliente gerado.\n\n"
                    "O CPA deve ser avaliado contra o valor esperado da conversão: se um "
                    "lead gerado por R$50 tem 20% de probabilidade de fechar um negócio "
                    "de R$5.000, o CPA efetivo do cliente é R$250 — viável ou não depende "
                    "das margens do negócio. Esta análise conecta Intenção ao LTV na "
                    "etapa de Retenção."
                ),
            },
            {
                "nome": "Alcance",
                "formula": "Usuários únicos impactados",
                "faixa_tipica": "Menor que awareness; audiência mais qualificada",
                "quando_usar": "Para monitorar tamanho da audiência atingida",
                "descricao": (
                    "O Alcance em Intenção é naturalmente menor que nas etapas anteriores, "
                    "refletindo a filtragem progressiva do funil. A audiência aqui é composta "
                    "por pessoas que já demonstraram interesse e consideração — remarketing "
                    "de visitantes do site, engajadores profundos, custom audiences de "
                    "interação com formulários parciais.\n\n"
                    "Comparar o alcance de Intenção com o de etapas anteriores revela a "
                    "saúde do funil: se Awareness alcançou 500k pessoas e Intenção alcança "
                    "apenas 5k (1%), o funil pode estar perdendo audiência em excesso nas "
                    "etapas intermediárias. A taxa saudável varia por segmento mas "
                    "tipicamente 2-5% do alcance de Awareness deve chegar a Intenção."
                ),
            },
            {
                "nome": "Frequência",
                "formula": "Impressões / Alcance",
                "faixa_tipica": "3-6 para intenção; remarketing aceita mais",
                "quando_usar": "Para controlar saturação em audiências quentes",
                "descricao": (
                    "A Frequência em Intenção pode ser mais alta (3-6) do que em etapas "
                    "anteriores porque a audiência já tem interesse formado e está mais "
                    "receptiva a múltiplas mensagens. Em remarketing de carrinho abandonado, "
                    "frequências de até 8-10 podem ser aceitáveis nos primeiros 3 dias "
                    "pós-abandono, desde que os criativos sejam dinâmicos e relevantes.\n\n"
                    "Porém, frequência alta com ausência de conversão é desperdício: se "
                    "após 6+ exposições o prospect não converteu, provavelmente decidiu "
                    "não comprar e continuar impactando só gera irritação. Defina "
                    "frequency caps e migre prospects não-convertidos para campanhas de "
                    "nurturing de menor intensidade."
                ),
            },
            {
                "nome": "Visualizações",
                "formula": "Total de visualizações do anúncio/vídeo",
                "faixa_tipica": "R$0.03-0.15 por view",
                "quando_usar": "Para vídeos demonstrativos de produto/serviço",
                "descricao": (
                    "As Visualizações de vídeo em Intenção focam em conteúdo de última milha: "
                    "demonstrações detalhadas, tutoriais de uso, depoimentos de clientes "
                    "satisfeitos, unboxings. CPVs de R$0,03-0,15 são referência. Nesta etapa, "
                    "vídeos com prova social (Cialdini) e demonstração de resultados concretos "
                    "são os mais eficazes para converter intenção em ação.\n\n"
                    "A taxa de conclusão de vídeo em Intenção tende a ser mais alta que em "
                    "etapas anteriores porque a audiência já está investida na decisão. "
                    "Vídeos que terminam com CTA claro e urgência ('Oferta válida até...') "
                    "maximizam a conversão pós-visualização."
                ),
            },
            {
                "nome": "Engajamento",
                "formula": "Curtidas + Comentários + Compartilhamentos + Salvamentos",
                "faixa_tipica": "1-4% de taxa sobre impressões",
                "quando_usar": "Indicador de interesse qualificado",
                "descricao": (
                    "O Engajamento em Intenção é um indicador de que a mensagem comercial "
                    "está ressoando com a audiência qualificada. Taxas de 1-4% sobre "
                    "impressões são típicas. Nesta etapa, engajamento social pode "
                    "funcionar como catalisador de conversão: comentários positivos e "
                    "depoimentos de outros compradores criam prova social que reduz a "
                    "percepção de risco.\n\n"
                    "Em Intenção, preste atenção especial a comentários com objeções "
                    "('É caro', 'Funciona mesmo?', 'Tempo de entrega?') — responder "
                    "publicamente com informações claras não apenas ajuda quem comentou "
                    "mas também todos os outros prospects que estão lendo os comentários "
                    "antes de decidir."
                ),
            },
            {
                "nome": "Comentários",
                "formula": "Total de comentários no anúncio",
                "faixa_tipica": "0.02-0.3% das impressões",
                "quando_usar": "Para medir dúvidas pré-conversão",
                "descricao": (
                    "Os Comentários em Intenção são frequentemente dúvidas pré-conversão "
                    "diretas: 'Qual o prazo de entrega?', 'Aceita Pix?', 'Tem garantia?'. "
                    "Cada pergunta destas é uma oportunidade de venda — o prospect está "
                    "prestes a converter mas precisa de uma última informação. Taxas de "
                    "0,02-0,3% sobre impressões são referência.\n\n"
                    "Montar uma equipe de resposta rápida para comentários em campanhas "
                    "de Intenção pode transformar esta métrica terciária em canal direto "
                    "de conversão. No Brasil, responder com link direto para WhatsApp "
                    "é uma prática altamente eficaz que combina a visibilidade pública "
                    "do comentário com a privacidade e conveniência do chat."
                ),
            },
            {
                "nome": "Custo Total",
                "formula": "Soma de todo investimento na campanha",
                "faixa_tipica": "= Budget alocado para a etapa",
                "quando_usar": "Para controlar gasto total vs. planejado",
                "descricao": (
                    "O Custo Total em Intenção deve ser monitorado contra o budget "
                    "planejado e contra o volume de leads gerados. Esta etapa tipicamente "
                    "recebe 15-20% do budget em estratégias de full-funnel. Gastar o "
                    "budget planejado sem gerar o volume esperado de leads indica "
                    "ineficiência que precisa ser diagnosticada (criativo, segmentação, "
                    "landing page).\n\n"
                    "Compare o custo total com o valor do pipeline gerado: se R$10.000 "
                    "investidos geraram 200 leads com valor potencial de R$500.000, o "
                    "investimento está altamente eficiente. Esta visão conecta o custo "
                    "operacional ao impacto nos negócios."
                ),
            },
            {
                "nome": "Custo Diário",
                "formula": "Custo total / Dias de veiculação",
                "faixa_tipica": "Budget / dias do período",
                "quando_usar": "Para monitorar pacing diário de investimento",
                "descricao": (
                    "O Custo Diário em Intenção pode ser mais volátil que em etapas "
                    "anteriores porque campanhas otimizadas para conversão concentram "
                    "investimento nos momentos de maior probabilidade de conversão — "
                    "o algoritmo 'aprende' quando a audiência está mais propensa a "
                    "converter e gasta mais nesses períodos.\n\n"
                    "Variações de 30-40% no custo diário são aceitáveis em campanhas "
                    "de Intenção com budget vitalício. O importante é que o gasto "
                    "acumulado esteja alinhado com o planejamento e que o custo diário "
                    "esteja gerando leads proporcionalmente."
                ),
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
                "descricao": (
                    "Conversões representam o número total de ações desejadas completadas pela audiência da campanha "
                    "— compras realizadas, assinaturas efetivadas, cadastros completados, agendamentos confirmados ou "
                    "qualquer outra ação que constitua o objetivo final de negócio. Na etapa de Conversão/Ação, esta "
                    "é a métrica definitiva de sucesso: todo o investimento em awareness, interesse, consideração e "
                    "intenção culmina aqui. Conforme o modelo STDC de Kaushik, esta é a fase 'Do' — o momento da "
                    "transação, onde a audiência está pronta para agir.\n\n"
                    "A taxa de conversão global média para e-commerce é de 3,17%, mas varia enormemente por nicho, "
                    "plataforma e origem do tráfego. Search ads convertem a 3,75-4,40%, enquanto display ads ficam "
                    "em 0,57-0,77% — uma diferença de 5-6x que reflete a diferença de intenção entre busca ativa "
                    "e publicidade de interrupção. Landing pages focadas em conversão única alcançam taxas medianas "
                    "de 6,6%. Para B2B, a taxa de visitante para lead é 2-5%, e de oportunidade para fechamento "
                    "é 15-30%.\n\n"
                    "O volume de conversões é o resultado final, mas deve ser contextualizado pelo CPA (quanto custou "
                    "cada conversão), pelo ROAS (quanto retorno cada real investido gerou) e pela qualidade da "
                    "conversão (ticket médio, LTV potencial). Conforme Binet & Field, campanhas de conversão COLHEM "
                    "a demanda criada pelas etapas anteriores — elas não criam demanda do zero."
                ),
            },
            {
                "nome": "CPA (Custo por Aquisição)",
                "formula": "Custo total / Total de conversões",
                "faixa_tipica": "R$20-150 (e-commerce); R$50-500 (serviços)",
                "quando_usar": "Para avaliar eficiência de conversão",
                "descricao": (
                    "O CPA (Custo por Aquisição) mede quanto a campanha está pagando, em média, para gerar cada "
                    "conversão. É a métrica que conecta diretamente o investimento em mídia ao resultado de negócio. "
                    "Calculado dividindo o custo total pelo número de conversões, o CPA é o KPI que responde à "
                    "pergunta fundamental de performance: 'quanto custa adquirir um cliente/venda através desta "
                    "campanha?'. Para e-commerce no Brasil, CPAs entre R$20-150 são típicos, enquanto serviços "
                    "de maior ticket podem ter CPAs de R$50-500.\n\n"
                    "O CPA é resultado de toda a cadeia de métricas: CPM, CTR, CPC, taxa de conversão da landing "
                    "page, e taxa de checkout. A fórmula expandida é: CPA = CPC / Taxa de Conversão, ou ainda "
                    "CPA = CPM / (CTR x Taxa de Conversão x 10). Isso revela múltiplas alavancas de otimização: "
                    "melhorar qualquer elo da cadeia reduz o CPA. Uma melhoria de 1% na taxa de conversão do site "
                    "pode reduzir o CPA em 20-30% sem alterar o investimento em mídia.\n\n"
                    "Atenção ao contexto de atribuição: o CPA varia drasticamente conforme o modelo de atribuição "
                    "utilizado. Last-click tende a inflar o CPA de campanhas de awareness e subestimar o de "
                    "remarketing. Multi-touch attribution oferece visão mais equilibrada. Conforme Binet & Field, "
                    "julgar todo o funil pelo CPA overvalora o last-touch e subinveste em brand building."
                ),
            },
            {
                "nome": "ROAS",
                "formula": "Receita gerada / Investimento em mídia",
                "faixa_tipica": "2x-6x para e-commerce; 1.5x-3x para serviços",
                "quando_usar": "Para campanhas com rastreamento de receita",
                "descricao": (
                    "O ROAS (Return On Ad Spend) é a métrica definitiva de retorno financeiro em campanhas de "
                    "conversão. Calculado dividindo a receita gerada pelo investimento em mídia, um ROAS de 4x "
                    "significa que cada R$1 investido retornou R$4 em receita. Para a maioria das marcas, ROAS "
                    "de 3:1 é considerado o mínimo saudável, 4:1 é bom, e 6:1+ indica audiências altamente "
                    "qualificadas (geralmente remarketing ou base de clientes).\n\n"
                    "O ROAS depende de duas variáveis: o volume de conversões e o ticket médio. A fórmula "
                    "expandida é: ROAS = (Conversões x Ticket Médio) / Investimento. Isso significa que o ROAS "
                    "pode melhorar tanto por redução do CPA quanto por aumento do ticket médio (upsell, cross-sell). "
                    "No mercado brasileiro, o ROAS médio para Meta Ads é 3,5x e para Google Ads é 4,0x, mas "
                    "campanhas de remarketing para base de clientes podem atingir 8-10x.\n\n"
                    "Cuidado com a interpretação isolada do ROAS. Conforme Binet & Field alertam, ROAS alto em "
                    "remarketing pode estar 'roubando' crédito de conversões que aconteceriam organicamente "
                    "(problema de incrementalidade). ROAS de awareness será sempre baixo no curto prazo — mas "
                    "é esse investimento que alimenta o pipeline para conversões futuras. Avaliar ROAS sem "
                    "considerar o funil completo leva a subinvestimento em brand building e declínio de longo prazo."
                ),
            },
        ],
        "secundarios": [
            {
                "nome": "Ticket Médio",
                "formula": "Receita total / Número de conversões",
                "faixa_tipica": "Varia por segmento; monitorar tendência",
                "quando_usar": "Para avaliar qualidade das conversões",
                "descricao": (
                    "O Ticket Médio (AOV — Average Order Value) mede o valor médio de cada transação "
                    "gerada pela campanha. Na etapa de Conversão, complementa diretamente o ROAS: "
                    "não basta ter muitas conversões se o valor por transação é baixo demais para "
                    "justificar o investimento. A fórmula ROAS = (Conversões × Ticket Médio) / Budget "
                    "mostra que um aumento de 20% no ticket médio tem o mesmo efeito no ROAS que "
                    "um aumento de 20% nas conversões — mas frequentemente é mais fácil de atingir.\n\n"
                    "Estratégias para elevar o ticket médio incluem: cross-sell e upsell na landing page, "
                    "faixas de frete grátis acima de um valor mínimo (fortemente eficaz no Brasil), "
                    "bundles de produtos e ofertas progressivas ('compre 2, leve 3'). Monitorar a "
                    "tendência do ticket médio ao longo da campanha é essencial — se cair, pode "
                    "indicar que a campanha está atraindo compradores de menor poder aquisitivo."
                ),
            },
            {
                "nome": "Taxa de Conversão",
                "formula": "(Conversões / Cliques) x 100",
                "faixa_tipica": "1-5% (e-commerce); 5-15% (lead gen)",
                "quando_usar": "Para otimizar funil de conversão",
                "descricao": (
                    "A Taxa de Conversão mede o percentual de visitantes (ou cliques) que completam a "
                    "ação desejada. Na Conversão/Ação, é o indicador direto de eficiência do funil final: "
                    "de todos que chegaram à landing page, quantos compraram ou se cadastraram? Benchmarks "
                    "médios são 1-5% para e-commerce e 5-15% para lead gen. Search Ads convertem a "
                    "3,75-4,40% contra 0,57-0,77% do Display, refletindo a diferença de intenção.\n\n"
                    "A taxa de conversão é função de múltiplas variáveis: qualidade do tráfego (audiências "
                    "de remarketing convertem 4-10x mais que frias), alinhamento mensagem/landing page, "
                    "UX da página (mobile-first é obrigatório com 60% do tráfego vindo de mobile), e "
                    "sinais de confiança (selos, avaliações, garantia). Otimizar a taxa de conversão "
                    "em 1 ponto percentual pode ter impacto maior no ROAS do que reduzir o CPC em 20%."
                ),
            },
            {
                "nome": "Receita Total",
                "formula": "Soma de todas as transações atribuídas",
                "faixa_tipica": "Meta = Budget x ROAS alvo",
                "quando_usar": "Para medir resultado financeiro absoluto",
                "descricao": (
                    "A Receita Total é o valor financeiro absoluto gerado pelas conversões da campanha. "
                    "É a métrica que conecta diretamente o investimento em mídia ao resultado de negócio. "
                    "A meta pode ser calculada como Budget × ROAS alvo: se o budget é R$50.000 e o ROAS "
                    "alvo é 4x, a meta de receita é R$200.000. Monitorar receita em tempo real permite "
                    "ajustar a alocação de budget para plataformas e campanhas de maior contribuição.\n\n"
                    "Atenção à atribuição: a receita atribuída depende do modelo de atribuição usado "
                    "(last-click, first-click, multi-touch, data-driven). Modelos de last-click "
                    "supervalorizam a receita de campanhas de conversão e subvalorizam awareness/consideração "
                    "que geraram a demanda inicial. Binet & Field alertam que otimizar apenas pela receita "
                    "atribuída de curto prazo leva ao subinvestimento em construção de marca."
                ),
            },
            {
                "nome": "CTR",
                "formula": "(Cliques / Impressões) x 100",
                "faixa_tipica": "1.5-4% para campanhas de conversão",
                "quando_usar": "Para monitorar eficiência dos criativos",
                "descricao": (
                    "Na etapa de Conversão, o CTR é uma métrica de suporte que indica a eficiência dos "
                    "criativos em gerar cliques entre a audiência exposta. CTRs de 1,5-4% são referência "
                    "para campanhas de conversão — maiores que em Awareness (0,3-1,5%) porque a audiência "
                    "é mais qualificada e os criativos contêm CTAs diretos e ofertas específicas. Um CTR "
                    "abaixo de 1% em conversão sugere que o criativo não está comunicando a oferta de "
                    "forma convincente.\n\n"
                    "Embora importante para diagnóstico, o CTR em Conversão NÃO é indicador de sucesso — "
                    "CTR alto com taxa de conversão baixa indica que o anúncio atrai cliques mas a "
                    "landing page não converte (problema de alinhamento mensagem/destino). O foco deve "
                    "ser no que acontece DEPOIS do clique: taxa de conversão, CPA e ROAS são os "
                    "verdadeiros indicadores de sucesso nesta etapa."
                ),
            },
        ],
        "terciarios": [
            {
                "nome": "Custo por Resultado",
                "formula": "Custo total / Resultados",
                "faixa_tipica": "Depende do tipo de resultado rastreado",
                "quando_usar": "Quando 'resultado' não é necessariamente venda",
                "descricao": (
                    "O Custo por Resultado é uma métrica genérica que divide o investimento "
                    "pelo número de 'resultados' conforme definido no objetivo da campanha — "
                    "que pode ser venda, lead, cadastro, instalação de app ou qualquer evento "
                    "rastreado. Na Conversão/Ação, permite avaliar eficiência quando o 'resultado' "
                    "não é necessariamente uma venda direta (ex: agendamento de visita técnica, "
                    "matrícula em curso gratuito, solicitação de orçamento).\n\n"
                    "O valor aceitável depende inteiramente do tipo de resultado e do valor "
                    "monetário associado. Compare o custo por resultado com o valor gerado "
                    "pelo resultado para determinar a viabilidade. Esta métrica é mais flexível "
                    "que o CPA tradicional e permite avaliar campanhas com objetivos não-"
                    "transacionais dentro da etapa de conversão."
                ),
            },
            {
                "nome": "Frequência de Compra",
                "formula": "Transações / Compradores únicos",
                "faixa_tipica": "1.1-1.5x no período de campanha",
                "quando_usar": "Para campanhas com público recorrente",
                "descricao": (
                    "A Frequência de Compra mede quantas transações cada comprador único "
                    "realizou durante o período da campanha. Na etapa de Conversão/Ação, "
                    "valores de 1,1-1,5x indicam que alguns compradores estão retornando "
                    "para comprar mais de uma vez — um sinal precoce de fidelização. "
                    "Quando a frequência é 1,0 (cada comprador compra exatamente uma vez), "
                    "a campanha está funcionando apenas em aquisição, sem gerar recorrência.\n\n"
                    "Cruzar frequência de compra com o canal de aquisição revela quais "
                    "campanhas geram compradores mais recorrentes. Frequências acima de "
                    "1,3x são indicadores positivos de que a experiência de compra foi "
                    "satisfatória e a marca conquistou espaço na consideração habitual — "
                    "estes compradores são candidatos ideais para segmentar em campanhas "
                    "de Retenção/Fidelização."
                ),
            },
            {
                "nome": "Impressões",
                "formula": "Total de exibições do anúncio",
                "faixa_tipica": "Depende de budget e CPM",
                "quando_usar": "Para monitorar volume de exposição",
                "descricao": (
                    "As Impressões em Conversão/Ação são a métrica mais distante do objetivo "
                    "da etapa — servem apenas como componente de cálculo (CPM, CTR) e "
                    "indicador de entrega da campanha. O volume é tipicamente o menor de "
                    "todas as etapas porque as audiências de conversão são as mais "
                    "restritas (remarketing de carrinho, lookalike de compradores).\n\n"
                    "Se as impressões em Conversão são desproporcionalmente altas em "
                    "relação às conversões, o targeting pode estar muito amplo — incluindo "
                    "audiências que não têm intenção real de compra. Refinar a segmentação "
                    "para focar nos sinais de intenção mais fortes melhora a eficiência "
                    "de toda a etapa."
                ),
            },
            {
                "nome": "Cliques",
                "formula": "Total de cliques no anúncio",
                "faixa_tipica": "Depende de CTR e volume de impressões",
                "quando_usar": "Para medir volume de tráfego ao site",
                "descricao": (
                    "Os Cliques em Conversão/Ação representam o tráfego direcionado "
                    "diretamente ao ponto de conversão — página de produto, checkout, "
                    "landing page de venda. Cada clique nesta etapa tem expectativa de "
                    "conversão significativamente maior que em etapas anteriores porque "
                    "a audiência já foi filtrada pelo funil.\n\n"
                    "O volume de cliques é o 'input' da taxa de conversão: Cliques x "
                    "Taxa de Conversão = Vendas/Conversões. Monitorar em tempo real "
                    "permite projetar resultados e intervir rapidamente se a taxa de "
                    "conversão cair — investigar problemas no site, estoque esgotado, "
                    "erros de checkout ou desalinhamento entre oferta do anúncio e "
                    "página de destino."
                ),
            },
            {
                "nome": "CPC",
                "formula": "Custo total / Cliques",
                "faixa_tipica": "R$1.00-8.00 para público de conversão",
                "quando_usar": "Para monitorar custo de tráfego qualificado",
                "descricao": (
                    "O CPC em Conversão/Ação é naturalmente mais alto (R$1-8) que em etapas "
                    "anteriores porque as audiências de conversão são premium — competição "
                    "alta por remarketing de carrinho, keywords transacionais e custom "
                    "audiences de compradores. No Google Ads, palavras-chave como 'comprar', "
                    "'preço' e 'frete grátis' têm CPCs 2-3x maiores que keywords "
                    "informacionais.\n\n"
                    "O CPC deve ser avaliado em relação ao CPA e ROAS, não isoladamente. "
                    "Um CPC de R$8 que gera vendas de R$200 com taxa de conversão de 5% "
                    "resulta em CPA de R$160 e ROAS de 1,25x — o que pode ou não ser "
                    "viável dependendo das margens. O CPC em conversão é componente de "
                    "cálculo, não métrica de sucesso."
                ),
            },
            {
                "nome": "CPM",
                "formula": "(Custo total / Impressões) x 1000",
                "faixa_tipica": "R$15-45 para audiências de conversão",
                "quando_usar": "Para monitorar custo de distribuição",
                "descricao": (
                    "O CPM em Conversão/Ação é o mais alto do funil (R$15-45) por refletir "
                    "a alta competição por audiências de alta intenção. Em períodos sazonais "
                    "como Black Friday, Natal e Dia das Mães, CPMs de conversão podem "
                    "triplicar, tornando essencial o planejamento antecipado e a construção "
                    "de audiências de remarketing antes das datas de pico.\n\n"
                    "Na etapa de Conversão, o CPM é irrelevante como métrica de sucesso — "
                    "o que importa é ROAS e CPA. Um CPM de R$60 que gera ROAS de 5x é "
                    "infinitamente superior a um CPM de R$10 que não converte. Monitorar "
                    "o CPM serve apenas para diagnosticar mudanças na competitividade do "
                    "leilão e planejar budgets sazonais."
                ),
            },
            {
                "nome": "Alcance",
                "formula": "Usuários únicos impactados",
                "faixa_tipica": "Audiência menor e mais qualificada",
                "quando_usar": "Para monitorar cobertura da audiência-alvo",
                "descricao": (
                    "O Alcance em Conversão/Ação é o menor de todas as etapas, refletindo "
                    "a filtragem progressiva do funil. A audiência aqui é composta por "
                    "prospects de altíssima qualificação: abandonadores de carrinho, "
                    "visitantes de página de produto, leads quentes e clientes anteriores. "
                    "É uma audiência pequena mas com a maior probabilidade de conversão.\n\n"
                    "Se o alcance em Conversão é muito pequeno para atingir os objetivos "
                    "de vendas, o problema não está em Conversão — está nas etapas "
                    "anteriores que não estão gerando audiência qualificada suficiente. "
                    "Escalar vendas exige escalar o funil inteiro, não apenas aumentar "
                    "investimento em conversão com audiência limitada."
                ),
            },
            {
                "nome": "Frequência",
                "formula": "Impressões / Alcance",
                "faixa_tipica": "4-8 para conversão; remarketing aceita alta frequência",
                "quando_usar": "Para controlar repetição em audiências de conversão",
                "descricao": (
                    "A Frequência em Conversão/Ação pode ser a mais alta do funil (4-8), "
                    "especialmente em remarketing de carrinho abandonado nos primeiros "
                    "3-7 dias pós-abandono. A audiência nesta etapa está próxima da decisão "
                    "e pode precisar de múltiplos lembretes/incentivos para concluir a "
                    "compra. Dynamic Product Ads com frequência controlada são uma das "
                    "táticas mais eficientes neste cenário.\n\n"
                    "Porém, após 7-10 dias sem conversão, a frequência deve ser reduzida "
                    "drasticamente — o prospect provavelmente já comprou de um concorrente "
                    "ou desistiu. Frequência excessiva neste cenário apenas gera irritação "
                    "e pode prejudicar a percepção da marca. Defina frequency caps e "
                    "regras de exclusão baseadas em tempo."
                ),
            },
            {
                "nome": "Visualizações",
                "formula": "Total de visualizações do anúncio/vídeo",
                "faixa_tipica": "R$0.03-0.15 por view",
                "quando_usar": "Para vídeos de produto/depoimentos",
                "descricao": (
                    "As Visualizações de vídeo em Conversão/Ação focam em conteúdo de "
                    "última milha: vídeos de unboxing, depoimentos de compradores, "
                    "demonstrações rápidas de uso e provas de resultado. Na etapa final "
                    "do funil, vídeos curtos (15-30s) com forte prova social e CTA "
                    "claro são os mais eficazes para converter intenção em ação.\n\n"
                    "A taxa de conclusão nesta etapa tende a ser alta porque a audiência "
                    "já está interessada no produto. Vídeos que terminam com oferta "
                    "limitada ('Últimas unidades', 'Desconto válido até amanhã') "
                    "combinam urgência (princípio de Escassez de Cialdini) com prova "
                    "social para maximizar a conversão pós-view."
                ),
            },
            {
                "nome": "Engajamento",
                "formula": "Curtidas + Comentários + Compartilhamentos + Salvamentos",
                "faixa_tipica": "1-3% de taxa sobre impressões",
                "quando_usar": "Indicador secundário de ressonância",
                "descricao": (
                    "O Engajamento em Conversão/Ação serve menos como indicador de "
                    "sucesso da campanha e mais como canal de prova social para outros "
                    "prospects. Comentários positivos ('Comprei e adorei!', 'Chegou "
                    "rápido'), avaliações e fotos de compradores criam um ciclo virtuoso "
                    "de confiança que beneficia todos os prospects que visualizam o anúncio.\n\n"
                    "Em conversão, engajamento orgânico positivo funciona como amplificador "
                    "de eficácia: anúncios com muitos comentários positivos convertem "
                    "melhor porque reduzem a percepção de risco de compra. Por isso, "
                    "manter os comentários limpos e responder dúvidas rapidamente é "
                    "estratégico, não apenas operacional."
                ),
            },
            {
                "nome": "Comentários",
                "formula": "Total de comentários no anúncio",
                "faixa_tipica": "0.01-0.2% das impressões",
                "quando_usar": "Para medir dúvidas e social proof",
                "descricao": (
                    "Os Comentários em Conversão/Ação são canal direto de social proof "
                    "e atendimento pré-venda. Compradores que compartilham experiências "
                    "positivas nos comentários geram o efeito de prova social descrito "
                    "por Cialdini — um dos gatilhos mais poderosos para conversão. "
                    "Simultaneamente, dúvidas sobre frete, troca, garantia e pagamento "
                    "são oportunidades de fechar vendas em tempo real.\n\n"
                    "Um protocolo de resposta rápida a comentários em anúncios de "
                    "conversão pode ter ROI excepcional: cada dúvida respondida "
                    "publicamente beneficia todos os futuros visualizadores do anúncio. "
                    "No Brasil, direcionar para DM/WhatsApp após resposta pública é "
                    "a prática mais eficaz para converter dúvidas em vendas."
                ),
            },
            {
                "nome": "Custo Total",
                "formula": "Soma de todo investimento na campanha",
                "faixa_tipica": "= Budget alocado para a etapa",
                "quando_usar": "Para controlar gasto total vs. planejado",
                "descricao": (
                    "O Custo Total em Conversão/Ação é o investimento mais diretamente "
                    "vinculado a receita — cada real investido aqui deve gerar retorno "
                    "mensurável via ROAS. Esta etapa tipicamente recebe 20-40% do budget "
                    "conforme Binet & Field (porção de ativação), sendo a fatia mais "
                    "diretamente ligada a resultados de curto prazo.\n\n"
                    "O custo total deve ser comparado com a receita gerada para calcular "
                    "o ROAS da etapa: Receita / Custo Total. Se o ROAS está abaixo do "
                    "target, diagnosticar onde a cadeia está falhando: CPC alto, taxa "
                    "de conversão baixa ou ticket médio insuficiente."
                ),
            },
            {
                "nome": "Custo Diário",
                "formula": "Custo total / Dias de veiculação",
                "faixa_tipica": "Budget / dias do período",
                "quando_usar": "Para monitorar pacing diário de investimento",
                "descricao": (
                    "O Custo Diário em Conversão/Ação é tipicamente o mais volátil do "
                    "funil porque campanhas otimizadas para conversão (CPA/ROAS target) "
                    "concentram gasto nos momentos de maior probabilidade de compra — "
                    "finais de semana, horários de pico e proximidade de datas sazonais "
                    "podem gerar variações de 50%+ no gasto diário.\n\n"
                    "Para campanhas com budget vitalício e otimização por conversão, "
                    "confie no algoritmo para distribuir o gasto conforme a oportunidade. "
                    "Monitorar diariamente é importante para detectar anomalias, mas "
                    "variações dentro do orçamento total não são preocupantes se o "
                    "ROAS se mantém saudável."
                ),
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
                "descricao": (
                    "A Taxa de Retenção mede o percentual de clientes que permanecem ativos e comprando ao longo do "
                    "tempo. É calculada dividindo o número de clientes retidos pelo total no início do período e "
                    "multiplicando por 100. Na etapa de Retenção/Fidelização, esta é a métrica-mestre porque representa "
                    "a capacidade da marca de manter sua base — e pesquisas consistentemente demonstram que aumentar a "
                    "retenção em apenas 5% pode elevar os lucros em até 75%. Vender para clientes existentes tem "
                    "margens superiores e taxas de fechamento muito maiores do que aquisição de novos.\n\n"
                    "Os benchmarks variam por modelo de negócio: e-commerce tipicamente opera com retenção mensal de "
                    "60-80%, enquanto SaaS pode alcançar 85-95%. A retenção deve ser medida em cohorts (grupos de "
                    "clientes adquiridos no mesmo período) para identificar tendências e impacto de campanhas "
                    "específicas. No modelo McKinsey CDJ, clientes satisfeitos entram no 'Loyalty Loop', pulando as "
                    "fases de avaliação e comprando diretamente — o cenário ideal de retenção.\n\n"
                    "Conforme Byron Sharp, no entanto, fidelidade é parcialmente um artefato estatístico de "
                    "penetração (Lei da Dupla Penalidade). Isso não invalida o foco em retenção, mas sugere que "
                    "o crescimento sustentável exige um equilíbrio entre reter a base existente e adquirir novos "
                    "clientes. Investir exclusivamente em retenção sem alimentar o topo do funil eventualmente "
                    "leva a estagnação."
                ),
            },
            {
                "nome": "LTV (Lifetime Value)",
                "formula": "Ticket médio x Frequência x Tempo de retenção",
                "faixa_tipica": "3-5x o CPA para ser saudável",
                "quando_usar": "Para avaliar valor de longo prazo do cliente",
                "descricao": (
                    "O LTV (Lifetime Value ou Valor Vitalício do Cliente) estima a receita total que um cliente "
                    "gera ao longo de todo o seu relacionamento com a marca. É calculado multiplicando o ticket "
                    "médio pela frequência de compra e pelo tempo médio de retenção. Por exemplo: se o ticket "
                    "médio é R$150, a frequência é 4 compras por ano, e o tempo de retenção é 3 anos, o LTV é "
                    "R$1.800. Esta métrica é fundamental porque define o limite máximo de investimento aceitável "
                    "em aquisição — o CPA nunca deve exceder o LTV.\n\n"
                    "A regra geral de saúde financeira é que o LTV deve ser pelo menos 3-5x o CPA. Se o CPA é "
                    "R$100 e o LTV é R$500, a relação LTV:CPA é de 5:1, indicando um negócio saudável. Quando "
                    "essa relação cai abaixo de 3:1, o custo de aquisição está corroendo a rentabilidade. O LTV "
                    "também orienta decisões de budget entre etapas do funil: investir mais em retenção aumenta o "
                    "LTV, o que permite investir mais em aquisição mantendo a proporção saudável.\n\n"
                    "O LTV pode ser melhorado em três dimensões: aumentar o ticket médio (estratégias de upsell e "
                    "cross-sell), aumentar a frequência de compra (campanhas de reengajamento, programas de "
                    "fidelidade), e aumentar o tempo de retenção (melhorar experiência, reduzir churn). Cada "
                    "melhoria em qualquer uma dessas variáveis tem efeito multiplicador sobre o LTV total."
                ),
            },
            {
                "nome": "Taxa de Recompra",
                "formula": "(Compras recorrentes / Total de clientes) x 100",
                "faixa_tipica": "20-40% em 90 dias para e-commerce",
                "quando_usar": "Para medir efetividade de retenção",
                "descricao": (
                    "A Taxa de Recompra mede o percentual de clientes que realizaram pelo menos uma compra adicional "
                    "dentro de um período definido. É o indicador mais direto de fidelidade comportamental — não mede "
                    "intenção ou satisfação, mas a ação concreta de voltar a comprar. Para e-commerce, taxas de "
                    "recompra de 20-40% em 90 dias são consideradas saudáveis, enquanto marcas com forte programa "
                    "de fidelidade podem alcançar 40-60%.\n\n"
                    "No contexto do modelo CDJ da McKinsey, a taxa de recompra é o indicador do 'Loyalty Loop': "
                    "clientes que compram novamente sem passar pelas fases de avaliação ativa demonstram que a marca "
                    "conquistou um espaço privilegiado na sua decisão de compra. Conforme Kotler 5A, esses clientes "
                    "estão no estágio 'Advocate' — além de comprar, potencialmente indicam a marca.\n\n"
                    "Para aumentar a taxa de recompra, campanhas de remarketing para base de clientes são o "
                    "investimento mais eficiente do funil (ROAS típico de 4-10x). No Brasil, o WhatsApp Business "
                    "está se provando o canal mais eficaz para recompra, com taxa de conversão de 55% e valor médio "
                    "de carrinho recuperado de R$557,67. Programas de fidelidade com recompensas alcançáveis e "
                    "relevantes também impulsionam a recompra significativamente."
                ),
            },
        ],
        "secundarios": [
            {
                "nome": "ROAS (Retenção)",
                "formula": "Receita gerada / Investimento em mídia",
                "faixa_tipica": "4x-10x para remarketing de clientes existentes",
                "quando_usar": "Para avaliar eficiência de reinvestimento",
                "descricao": (
                    "O ROAS (Return on Ad Spend) na etapa de Retenção mede a receita gerada para cada real "
                    "investido em campanhas direcionadas à base de clientes existentes. É calculado dividindo "
                    "a receita atribuída pela campanha pelo investimento em mídia. Na Retenção, o ROAS esperado "
                    "é significativamente mais alto do que em etapas anteriores — tipicamente 4x a 10x — porque "
                    "a audiência já conhece a marca, já comprou e tem barreiras de conversão muito menores. "
                    "Conforme Binet & Field, campanhas de ativação para base existente operam com eficiência "
                    "muito superior justamente porque o 'trabalho pesado' de construção de marca já foi feito "
                    "nas etapas anteriores do funil.\n\n"
                    "Um ROAS de retenção abaixo de 4x é preocupante porque indica que o custo de reengajar "
                    "clientes existentes está se aproximando do custo de adquirir novos — o que anula a "
                    "vantagem econômica fundamental da retenção. Se isso ocorrer, investigar: a segmentação "
                    "pode estar incluindo clientes inativos há muito tempo (que se comportam como novos), "
                    "ou a oferta pode não ser relevante o suficiente para a base. No Brasil, campanhas de "
                    "remarketing via WhatsApp combinadas com Meta Ads apresentam os maiores ROAS de retenção "
                    "(6-12x), enquanto campanhas de email retargeting ficam na faixa de 4-8x. O ROAS de "
                    "retenção deve ser analisado junto com o LTV: um ROAS de 4x pode ser aceitável se o "
                    "cliente reativado gerar compras recorrentes nos meses seguintes."
                ),
            },
            {
                "nome": "NPS (Net Promoter Score)",
                "formula": "% Promotores - % Detratores",
                "faixa_tipica": "30-70 é considerado bom",
                "quando_usar": "Para medir satisfação e propensão a indicar",
                "descricao": (
                    "O NPS (Net Promoter Score) mede a disposição dos clientes em recomendar a marca para "
                    "outras pessoas, classificando-os em Promotores (notas 9-10), Neutros (7-8) e Detratores "
                    "(0-6). O score final é calculado subtraindo o percentual de Detratores do percentual de "
                    "Promotores, resultando em um índice de -100 a +100. Na etapa de Retenção/Fidelização, "
                    "o NPS é um indicador secundário estratégico porque captura a dimensão emocional e "
                    "relacional da fidelidade — algo que métricas puramente transacionais como Taxa de "
                    "Recompra não conseguem medir. Conforme o modelo Kotler 5A, clientes com alto NPS "
                    "estão no estágio 'Advocate' (Apologia), o nível mais alto de relacionamento com a "
                    "marca, onde não apenas compram mas promovem ativamente.\n\n"
                    "Scores acima de 30 são considerados bons, acima de 50 são excelentes e acima de 70 "
                    "são de classe mundial. No Brasil, o consumidor tende a ser mais expressivo tanto na "
                    "promoção quanto na detração, gerando distribuições mais polarizadas. O NPS deve ser "
                    "correlacionado com as campanhas de retenção para medir não apenas se o cliente voltou "
                    "a comprar, mas se a experiência pós-compra está criando advogados da marca. Um NPS "
                    "alto com taxa de recompra baixa sugere satisfação sem hábito de compra (oportunidade "
                    "para campanhas de frequência). Um NPS baixo com taxa de recompra alta indica compra "
                    "por conveniência ou falta de alternativa — uma posição frágil que qualquer concorrente "
                    "pode desestabilizar. O ideal é que ambas as métricas cresçam juntas, sinalizando "
                    "fidelidade genuína tanto comportamental quanto atitudinal."
                ),
            },
            {
                "nome": "Churn Rate",
                "formula": "(Clientes perdidos / Total clientes) x 100",
                "faixa_tipica": "2-8% mensal para e-commerce",
                "quando_usar": "Para monitorar perda de base",
                "descricao": (
                    "O Churn Rate (Taxa de Cancelamento) mede o percentual de clientes que deixaram de "
                    "comprar ou cancelaram seu relacionamento com a marca dentro de um período definido. "
                    "É o inverso complementar da Taxa de Retenção: se a retenção mensal é 92%, o churn é "
                    "8%. Para e-commerce, taxas de churn mensal de 2-8% são típicas, enquanto para SaaS "
                    "o aceitável é 1-3% mensal. Na etapa de Retenção/Fidelização, o Churn Rate funciona "
                    "como 'alarme' — enquanto a Taxa de Retenção mostra quem ficou, o Churn revela "
                    "ativamente quem está saindo e permite ação corretiva. Conforme a Lei da Dupla "
                    "Penalidade de Byron Sharp, marcas menores sofrem duplamente: menos compradores E "
                    "menor frequência de compra — o que torna o controle de churn ainda mais crítico "
                    "para marcas em crescimento.\n\n"
                    "O churn deve ser analisado em cohorts para identificar padrões: se clientes adquiridos "
                    "por campanhas de desconto agressivo apresentam churn significativamente maior, isso "
                    "indica que o desconto atraiu compradores oportunistas sem real afinidade com a marca "
                    "(um diagnóstico crucial para ajustar estratégias de aquisição). No Brasil, o churn "
                    "tende a ser mais alto em mercados com muitas promoções sazonais (Black Friday, Dia do "
                    "Consumidor), onde clientes compram por oportunidade e não por lealdade. Campanhas de "
                    "retenção devem focar especificamente nos segmentos com maior propensão ao churn — "
                    "modelos preditivos de churn que combinam dados de frequência de compra, engajamento "
                    "com comunicações e recência da última compra (análise RFM) são extremamente eficazes "
                    "para direcionar investimentos de retenção onde o risco de perda é maior."
                ),
            },
        ],
        "terciarios": [
            {
                "nome": "Taxa de Abertura de Email",
                "formula": "(Emails abertos / Emails enviados) x 100",
                "faixa_tipica": "15-30% dependendo do segmento",
                "quando_usar": "Para campanhas de CRM/email marketing",
                "descricao": (
                    "A Taxa de Abertura de Email mede o percentual de destinatários que "
                    "abriram o email da campanha de retenção. Taxas de 15-30% são referência "
                    "dependendo do segmento e qualidade da base. Para retenção, a taxa de "
                    "abertura é o primeiro indicador de que a base está engajada com as "
                    "comunicações da marca — se cai abaixo de 15%, pode indicar fadiga da "
                    "base, assuntos pouco atrativos ou entrega na aba de promoções/spam.\n\n"
                    "No Brasil, email marketing para base própria tem ROAS médio de 42:1, "
                    "tornando-o um dos canais mais eficientes para retenção. Segmentar a "
                    "base por RFM (Recência, Frequência, Monetário) e personalizar "
                    "assuntos e conteúdo por segmento eleva taxas de abertura "
                    "significativamente. Combinado com campanhas de remarketing via Meta "
                    "Ads (Custom Audience de emails), cria uma estratégia omnichannel "
                    "de retenção altamente eficaz."
                ),
            },
            {
                "nome": "Engajamento em Fidelidade",
                "formula": "Membros ativos / Total membros",
                "faixa_tipica": "30-50% de engajamento ativo",
                "quando_usar": "Para marcas com programa de pontos/benefícios",
                "descricao": (
                    "O Engajamento em Fidelidade mede o percentual de membros do programa "
                    "de fidelidade que estão ativamente participando — acumulando pontos, "
                    "resgatando benefícios, subindo de nível. Taxas de 30-50% de engajamento "
                    "ativo são referência. Se a taxa cair abaixo de 30%, o programa pode "
                    "estar falhando em entregar valor percebido suficiente para motivar "
                    "participação contínua — recompensas inacessíveis, mecânicas "
                    "complexas ou benefícios pouco relevantes.\n\n"
                    "No contexto de Retenção/Fidelização, esta métrica indica a eficácia "
                    "do programa como ferramenta de retenção. Membros ativos de programas "
                    "de fidelidade gastam em média 12-18% mais que não-membros e têm "
                    "frequência de compra 20-40% superior. Campanhas de mídia que promovem "
                    "o programa de fidelidade para clientes existentes (via Custom "
                    "Audiences) podem aumentar significativamente a taxa de adesão e "
                    "engajamento, fortalecendo o loop de retenção."
                ),
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
        "Diversos frameworks acadêmicos consolidados descrevem a jornada do consumidor "
        "através de perspectivas complementares, porém distintas. O insight central que permeia "
        "todos os modelos é que cada etapa do funil exige objetivos fundamentalmente diferentes, "
        "métricas específicas, abordagens criativas próprias e alocação de budget distinta. "
        "Não existe uma métrica ou abordagem universal que funcione igualmente em todas as "
        "etapas — e tentar usar a mesma régua para fases diferentes é o erro estratégico "
        "mais comum e destrutivo em planejamento de mídia digital."
    ),
    "frameworks": {
        "AIDA": {
            "author": "E. St. Elmo Lewis (1898)",
            "stages": ["Attention", "Interest", "Desire", "Action"],
            "key_insight": (
                "O modelo de funil de marketing mais antigo e influente. Propõe uma progressão linear "
                "que começa no cognitivo (Atenção/Awareness), avança para o afetivo (Interesse e Desejo) "
                "e culmina no comportamental (Ação/Compra). Embora seja a base conceitual de quase todo "
                "pensamento sobre funil, sua principal limitação é assumir um caminho estritamente linear "
                "e ignorar completamente a fase pós-compra, fidelização e advocacy. Modelos mais modernos "
                "como STDC, McKinsey CDJ e Kotler 5A evoluíram a partir do AIDA para corrigir essas lacunas."
            ),
        },
        "See-Think-Do-Care (STDC)": {
            "author": "Avinash Kaushik / Google (2013)",
            "stages": ["See", "Think", "Do", "Care"],
            "key_insight": (
                "Foca em clusters de intenção da audiência ao invés de dados demográficos. "
                "'See' = a maior audiência qualificada possível, sem intenção comercial ainda. "
                "'Think' = pessoas que estão ativamente considerando soluções na categoria. "
                "'Do' = audiência pronta para realizar a transação. "
                "'Care' = clientes existentes com 2+ transações.\n\n"
                "O princípio crítico do STDC é que cada etapa DEVE ter conteúdo diferente, canais "
                "diferentes E mensuração diferente. Avaliar campanhas 'See' (awareness) por métricas "
                "de 'Do' (como CPA) é, segundo Kaushik, o erro mais comum e destrutivo do marketing "
                "digital. Isso leva ao subinvestimento sistemático em construção de marca e ao declínio "
                "de crescimento no longo prazo."
            ),
            "metrics_by_stage": {
                "See": "Impressões, Alcance, Brand Lift, Novos visitantes, Pesquisas de awareness",
                "Think": "CTR, Taxa de engajamento, Páginas/sessão, Tempo no site, Visitas de retorno",
                "Do": "Taxa de conversão, CPA, ROAS, Receita, Transações",
                "Care": "LTV, Taxa de recompra, NPS, Taxa de retenção, Taxa de indicação",
            },
        },
        "McKinsey Consumer Decision Journey (CDJ)": {
            "author": "McKinsey & Company (David Court et al., 2009)",
            "stages": [
                "Consideração Inicial",
                "Avaliação Ativa",
                "Momento da Compra",
                "Experiência Pós-Compra",
                "Loop de Fidelidade",
            ],
            "key_insight": (
                "Desafia frontalmente o modelo linear de funil. Descobertas-chave baseadas em banco "
                "de dados de 125.000+ jornadas em 350 marcas de 30 setores: (1) Marcas presentes no "
                "conjunto de consideração inicial têm 3x mais probabilidade de serem compradas. "
                "(2) Consumidores podem ADICIONAR marcas durante a avaliação ativa, não apenas "
                "eliminar — o funil não é apenas um processo de estreitamento. (3) O 'Loop de "
                "Fidelidade' permite que clientes satisfeitos pulem completamente a avaliação e "
                "recomprem diretamente — o cenário ideal de retenção. (4) Os touchpoints durante a "
                "avaliação ativa são 2-3x mais influentes do que durante a consideração inicial, "
                "tornando o investimento em conteúdo de consideração proporcionalmente mais valioso."
            ),
        },
        "Kotler 5A (Marketing 4.0)": {
            "author": "Philip Kotler, Hermawan Kartajaya, Iwan Setiawan (2017)",
            "stages": ["Aware", "Appeal", "Ask", "Act", "Advocate"],
            "key_insight": (
                "Não é um funil fixo; consumidores podem entrar em qualquer etapa e circular entre elas. "
                "O objetivo final é 'Advocate' — transformar clientes em promotores ativos da marca. "
                "Reconhece a influência social em todas as etapas. Na economia conectada, o caminho "
                "de Aware (Conhecer) até Advocate (Recomendar) pode ser acelerado pela influência da "
                "comunidade, tornando o boca-a-boca e o marketing de influência elementos críticos em "
                "todas as fases do funil."
            ),
        },
        "RACE (Smart Insights)": {
            "author": "Dave Chaffey / Smart Insights (2010)",
            "stages": ["Reach", "Act", "Convert", "Engage"],
            "key_insight": (
                "Framework prático de marketing digital. Cada etapa possui KPIs claros e mensuráveis: "
                "Reach/Alcance (visitantes únicos, impressões, seguidores), Act/Interagir (taxa de "
                "rejeição, páginas por visita, metas concluídas), Convert/Converter (vendas, receita, "
                "ticket médio, lucro), Engage/Engajar (compras repetidas, satisfação, taxa de advocacy). "
                "Precedido por uma fase 'Plan' para definição de estratégia e objetivos, tornando o "
                "framework operacionalmente completo para equipes de mídia digital."
            ),
        },
        "Forrester Customer Lifecycle": {
            "author": "Forrester Research",
            "stages": ["Discover", "Explore", "Buy", "Engage"],
            "key_insight": (
                "Coloca o cliente no centro absoluto da análise. Enfatiza que 'Discover' (Descoberta) "
                "pode ser ativo ou passivo — nem todo prospect chega por busca intencional. A fase "
                "'Engage' (Engajar) é contínua e pós-compra, reconhecendo que a experiência com a "
                "marca continua indefinidamente. Propõe abandonar a metáfora do funil em favor de "
                "um ciclo de vida sem ponto final fixo, onde cada interação alimenta a próxima."
            ),
        },
        "Binet_and_Field": {
            "author": "Les Binet & Peter Field (IPA, 2013+)",
            "key_insight": (
                "Não é um modelo de funil propriamente, mas o framework de alocação de budget mais "
                "importante e empiricamente fundamentado do marketing moderno. Baseado na análise "
                "do IPA Databank com 996+ campanhas ao longo de décadas:\n\n"
                "(1) A divisão ótima é ~60% construção de marca / 40% ativação para marcas de consumo. "
                "(2) Construção de marca e ativação são trabalhos fundamentalmente diferentes que NÃO "
                "devem ser combinados no mesmo criativo. (3) Efeitos de marca se acumulam ao longo de "
                "meses e anos; efeitos de ativação alcançam pico em dias e decaem rapidamente. "
                "(4) A regra 60/40 não é absoluta — varia por categoria, maturidade da marca, faixa "
                "de preço e posição competitiva. (5) Para B2B: marcas novas precisam de 65% ativação / "
                "35% marca inicialmente, mas líderes B2B maduros devem mudar para 72% marca / 28% "
                "ativação. (6) Marcas premium podem precisar de 70:30 favorecendo construção de marca. "
                "(7) Campanhas emocionais produzem efeitos de longo prazo maiores; campanhas racionais "
                "geram ativação de curto prazo mais forte."
            ),
        },
        "Byron_Sharp_How_Brands_Grow": {
            "author": "Byron Sharp / Ehrenberg-Bass Institute (2010)",
            "key_insight": (
                "Desafia o pensamento tradicional de funil com leis empíricas do comportamento de "
                "compra. Leis fundamentais: (1) O crescimento vem primariamente da aquisição de "
                "novos compradores e compradores leves, NÃO da fidelização dos existentes. "
                "(2) Disponibilidade Mental (saliência da marca em situações de compra) e "
                "Disponibilidade Física (facilidade de encontrar e comprar) são os dois motores "
                "de crescimento. (3) Marcas devem mirar TODOS na categoria, não segmentos de nicho. "
                "(4) Ativos distintivos de marca (cores, logos, jingles) importam mais do que "
                "posicionamento diferenciado. (5) Publicidade contínua é melhor que campanhas "
                "intermitentes (bursts) — parar e recomeçar causa decaimento de memória de marca. "
                "(6) Fidelidade é em grande parte um artefato estatístico de penetração "
                "(Lei da Dupla Penalidade).\n\n"
                "Implicações para planejamento de mídia: priorizar ALCANCE sobre frequência, "
                "manter presença always-on, usar targeting amplo, e investir em ativos criativos "
                "distintivos ao invés de hierarquias complexas de mensagens."
            ),
        },
    },
}

FUNNEL_STAGE_DEEP_KNOWLEDGE = {

    "Consciência (Awareness)": {
        "theoretical_alignment": {
            "AIDA": "Atenção — capturar atenção cognitiva em um cenário de mídia saturado e competitivo",
            "STDC": "See — a maior audiência qualificada possível, ainda sem intenção comercial",
            "McKinsey_CDJ": "Construção do Conjunto de Consideração Inicial — marcas consideradas primeiro têm 3x mais probabilidade de serem compradas",
            "Kotler_5A": "Aware — consumidores conhecem a marca através de publicidade, boca-a-boca ou experiência anterior",
            "RACE": "Reach — construção de audiência através de SEO, conteúdo, redes sociais e mídia paga",
            "Forrester": "Discover — descoberta de marca ativa ou passiva através de múltiplos touchpoints",
            "Byron_Sharp": "Construção de Disponibilidade Mental — criando e reforçando estruturas de memória vinculadas a situações de compra",
            "Binet_Field": "Território de Construção de Marca — campanhas emocionais, de amplo alcance e criadoras de fama",
        },
        "metric_interpretation": {
            "meaningful_metrics": {
                "primary": [
                    "Alcance (usuários únicos expostos)",
                    "Brand Lift (medido via pesquisas ou estudos de plataforma)",
                    "Lift de Lembrança de Anúncio (Ad Recall Lift)",
                    "CPM (eficiência de custo por exposição)",
                    "Share of Voice (presença competitiva)",
                ],
                "secondary": [
                    "Frequência (controlada em 1,5-3,0x; acima de 4 gera fadiga mas também aprofunda lembrança)",
                    "Taxa de conclusão de vídeo (para campanhas video-first)",
                    "Taxa de novos visitantes (% de visitantes inéditos no site vindos da campanha)",
                    "Aumento no volume de buscas pela marca (indicador de efeito halo)",
                ],
            },
            "vanity_metrics_warning": (
                "Na etapa de awareness, CPA, ROAS e métricas de conversão direta são quase "
                "sempre MÉTRICAS DE VAIDADE. Medir campanhas de awareness por conversão é o "
                "erro mais destrutivo do marketing digital (Kaushik). Efeitos de marca levam 6+ "
                "meses para se materializar completamente em resultados de negócio (Binet & Field). "
                "Usar métricas de fundo de funil para julgar campanhas de topo de funil leva ao "
                "subinvestimento sistemático em construção de marca e causa declínio de "
                "crescimento no longo prazo."
            ),
            "benchmarks": {
                "frequency": "4+ exposições geram o maior lift de lembrança de marca; 8-12 exposições totais criam lembrança duradoura. Frequência semanal de 2-4x recomendada como ponto de partida.",
                "brand_lift": "3-15% de lift dependendo da categoria, qualidade criativa e peso de mídia. Anúncios em podcast podem aumentar awareness em 13 pontos percentuais.",
                "video_views": "Audiências expostas 5-7 vezes a anúncios têm até 8x mais probabilidade de converter depois do que audiências de exposição única (efeito de mera exposição).",
                "cpm_brazil": "CPM do Meta Ads no Brasil: faixa de $1,77-$5,26 (70-94% abaixo do benchmark global). Vantagem de custo significativa para construção de marca.",
            },
        },
        "budget_allocation": {
            "binet_field_guidance": (
                "Awareness se enquadra diretamente na categoria CONSTRUÇÃO DE MARCA do framework de "
                "Binet & Field. É aqui que os 60% (da regra 60/40) devem ser concentrados. "
                "Campanhas de construção de marca devem ser: emocionais ao invés de racionais, "
                "de targeting amplo, usando canais de alcance massivo, com criativos focados em "
                "fama e distinção ao invés de features de produto ou calls-to-action diretos."
            ),
            "funnel_budget_split": (
                "Frameworks comuns sugerem: divisão 60-30-10 (60% awareness, 30% meio de funil, "
                "10% fundo de funil) como template inicial. Pesquisa Fospha: marcas de melhor "
                "desempenho alocam apenas 10% para fundo de funil, enquanto 25% vai para awareness "
                "e consideração. Empresas em crescimento: 40-50% topo de funil. Entrantes em novos "
                "mercados: 50-60% topo de funil para estabelecer awareness de base. Abordagem "
                "full-funnel mostra até 45% de aumento em ROI vs campanhas de etapa única."
            ),
        },
        "creative_and_messaging": {
            "psychological_principles": {
                "mere_exposure_effect": (
                    "A exposição repetida a um estímulo gera familiaridade, e familiaridade gera "
                    "preferência. O efeito aumenta a fluência perceptual (facilidade de processamento), "
                    "que cria afeto positivo. Campanhas de topo de funil que geram 'impressões de passagem' "
                    "são eficazes por esse mecanismo mesmo sem gerar ação imediata. No entanto, a relação "
                    "segue uma curva em U invertido: exposições iniciais aumentam a preferência, mas "
                    "exposição EXCESSIVA eventualmente a diminui (fadiga do anúncio)."
                ),
                "cognitive_load_theory": (
                    "Pessoas preferem estímulos simples que exigem baixo esforço mental. Criativos de "
                    "awareness devem minimizar a carga cognitiva: mensagem simples, ativos de marca claros, "
                    "sem detalhes complexos de produto. Poluição visual causa sobrecarga cognitiva e "
                    "prejudica a formação de memória de marca. Uma mensagem central por criativo. O cérebro "
                    "processa informação visual 60.000x mais rápido que texto — priorize storytelling visual."
                ),
                "cialdini_applicable": [
                    "Prova Social — mostrar popularidade, presença de mercado, número de usuários",
                    "Afinidade — usar personagens identificáveis, estilos de vida aspiracionais, humor",
                    "Autoridade — endosso de especialistas, sinais de liderança no setor",
                ],
            },
            "content_strategy": (
                "Conteúdo em vídeo domina awareness: 88% dos profissionais de marketing afirmam que "
                "vídeo melhorou o ROI. 96% dos espectadores usam vídeos para aprender sobre produtos. "
                "Vídeos curtos geram 2,5x mais engajamento que formatos longos em redes sociais. "
                "Storytelling emocional com arco narrativo (personagens identificáveis, conflito, "
                "resolução) é o mais eficaz. Música e elementos visuais reforçam a lembrança de marca. "
                "O criativo deve ser brandado cedo (nos primeiros 3 segundos para vídeo) com ativos "
                "distintivos de marca conforme Byron Sharp."
            ),
            "format_recommendations": [
                "Vídeo (6-15s para social, 15-30s para YouTube/CTV)",
                "Carrossel com progressão de história da marca",
                "Display de alto impacto (takeover, intersticial)",
                "Anúncios de áudio (podcast, streaming de música)",
                "Conteúdo de influenciador (branded entertainment)",
            ],
        },
        "platform_stage_alignment": {
            "YouTube": {
                "why": (
                    "75% das pessoas dizem que anúncios no YouTube aumentam o conhecimento sobre novas marcas. "
                    "70% afirmaram ter comprado uma marca após vê-la no YouTube. Bumper ads não puláveis "
                    "(6s) são ideais para construção de frequência. TrueView para alcance maximiza a "
                    "audiência única. O YouTube também oferece estudos robustos de Brand Lift para mensuração."
                ),
                "best_formats": "Bumper Ads, TrueView In-Stream, Masthead",
            },
            "Meta (Instagram/Facebook)": {
                "why": (
                    "Anúncios em vídeo aumentam o awareness de marca em até 57% (pesquisa interna do Meta). "
                    "Alcance massivo no Brasil (Instagram: 92% dos usuários de internet, Facebook: 81,5%). "
                    "CPMs baixos no Brasil ($1,77-$5,26). Audiências lookalike avançadas para targeting "
                    "amplo e eficiente. O formato Reels impulsiona alto engajamento para awareness."
                ),
                "best_formats": "Reels, Stories, Video Feed Ads, Carousel",
            },
            "TikTok": {
                "why": (
                    "91,7 milhões de usuários com 18+ no Brasil (início de 2025). Formato nativo de "
                    "vídeo curto maximiza o efeito de mera exposição. Maior potencial de viralidade "
                    "orgânica. O algoritmo favorece descoberta de conteúdo sobre grafos de seguidores, "
                    "tornando-o ideal para alcançar novas audiências. Gen Z e millennials jovens são "
                    "altamente indexados."
                ),
                "best_formats": "In-Feed Video, TopView, Branded Hashtag Challenge",
            },
            "Programática/Display": {
                "why": (
                    "77% da receita de anúncios digitais no Brasil será programática até 2028. "
                    "Permite alcance massivo em milhares de publishers. Frequency capping avançado "
                    "entre canais. DV360/Trade Desk possibilitam gestão de alcance/frequência "
                    "cross-platform. Excelente para complementar o alcance social com alcance web."
                ),
                "best_formats": "Rich Media, Video Pre-roll, Skins de alto impacto, CTV/OTT",
            },
        },
        "common_mistakes": {
            "medir_com_metricas_erradas": (
                "Julgar campanhas de awareness por CPA ou ROAS. Este é o erro #1 segundo Kaushik, "
                "Binet & Field e Sharp. Efeitos de marca levam meses para se materializar em dados de "
                "vendas. Isso leva ao subinvestimento sistemático em construção de marca."
            ),
            "gestao_errada_de_frequencia": (
                "Ou muito baixa (1-2x, insuficiente para lembrança) ou muito alta (>8x sem rotação "
                "de criativos, causando fadiga do anúncio). A curva em U invertido do efeito de mera "
                "exposição significa que existe uma janela ótima de exposição."
            ),
            "targeting_muito_restrito": (
                "A pesquisa de Byron Sharp mostra que marcas crescem alcançando compradores leves "
                "e não-compradores. Segmentação excessiva na etapa de awareness limita o alcance "
                "e aumenta o CPM. 95% dos potenciais clientes não estão prontos para comprar agora "
                "(LinkedIn B2B Institute), mas precisam estar no conjunto mental de consideração "
                "para compras futuras."
            ),
            "mensagem_focada_em_produto": (
                "Usar mensagens focadas em features de produto para uma audiência sem intenção "
                "de categoria. Criativos de awareness devem focar em emoção, história da marca "
                "e ativos distintivos, não em especificações ou preços. Binet & Field mostram "
                "que campanhas emocionais superam as racionais para efeitos de marca de longo prazo."
            ),
            "publicidade_intermitente": (
                "Byron Sharp: milhões desperdiçados em campanhas burst que se dissipam no silêncio. "
                "Evidências mostram que publicidade contínua always-on mantém a disponibilidade "
                "mental melhor do que flights pesados intermitentes."
            ),
            "ignorar_topo_de_funil": (
                "Superinvestir em conversão de fundo de funil enquanto negligencia awareness. "
                "Isso ignora 95% dos potenciais clientes que ainda não estão prontos para comprar. "
                "Cria um 'funil furado' onde a marca falha em alimentar novos prospects."
            ),
        },
        "brazil_specifics": {
            "dados_de_mercado": (
                "Redes sociais concentraram 53% de todo o investimento em anúncios digitais no Brasil (2024). "
                "O CPM do Meta Ads no Brasil é em média 70-94% abaixo do benchmark global — eficiência "
                "de custo excepcional para campanhas de awareness. "
                "Mercado de anúncios digitais no Brasil: R$37,9 bilhões em 2024, crescimento de 8% YoY. "
                "Mobile representa 56,88% do gasto em anúncios digitais. "
                "Instagram alcança 92% dos usuários de internet brasileiros — plataforma dominante para awareness. "
                "WhatsApp alcança 93,7% mas é primariamente uma ferramenta de meio/fundo de funil."
            ),
            "consideracoes_culturais": (
                "Consumidores brasileiros respondem fortemente a conteúdo emocional, humorístico e "
                "impulsionado por música. Períodos de Carnaval e Independência veem maior atividade "
                "social e CPMs mais altos. Marketing de influência é profundamente enraizado na cultura "
                "brasileira — considere parcerias com criadores para awareness. Gen Z no Brasil é "
                "fortemente nativa do TikTok."
            ),
            "penetracao_plataformas": {
                "WhatsApp": "93,7% dos usuários de internet",
                "Instagram": "92% dos usuários de internet",
                "Facebook": "81,5% dos usuários de internet",
                "TikTok": "63,9% dos usuários de internet (91,7M usuários 18+)",
                "YouTube": "144 milhões de usuários",
                "Telegram": "57,1% dos usuários de internet",
            },
        },
    },

    "Interesse": {
        "theoretical_alignment": {
            "AIDA": "Interest — o prospect começa a se engajar com a mensagem da marca e explora mais",
            "STDC": "Transição entre See e Think — a audiência está curiosa mas ainda não avaliando soluções",
            "McKinsey_CDJ": "Fortalecimento do Conjunto Inicial de Consideração — garantindo que a marca permaneça top-of-mind durante a absorção passiva",
            "Kotler_5A": "Appeal — a marca cria curiosidade e atração; consumidores ficam intrigados",
            "RACE": "Act — primeiras interações, cliques, engajamento com conteúdo",
            "Forrester": "Exploração Inicial — início da pesquisa multicanal",
            "Byron_Sharp": "Reforço da Disponibilidade Mental através de pontos de entrada de categoria e ativos distintivos",
            "Binet_Field": "Zona de sobreposição entre construção de marca e ativação — conteúdo deve pender para emocional/educacional",
        },
        "metric_interpretation": {
            "meaningful_metrics": {
                "primary": [
                    "CTR (Taxa de Cliques) — indica relevância criativa e curiosidade da audiência",
                    "Taxa de Engajamento — profundidade da interação com o conteúdo",
                    "CPC (Custo por Clique) — eficiência na geração de interesse",
                    "Taxa de Conclusão de Vídeo / ThruPlay — consumo genuíno de conteúdo",
                ],
                "secondary": [
                    "Tempo no site / página (qualidade do tráfego gerado)",
                    "Páginas por sessão (profundidade de exploração do conteúdo)",
                    "Taxa de rejeição (indicador inverso — quanto menor, melhor)",
                    "Salvamentos/Favoritos (sinal forte de intenção futura)",
                    "Compartilhamentos (viralidade e ressonância do conteúdo)",
                    "Taxa de visitas de retorno (interesse contínuo)",
                ],
            },
            "vanity_metrics_warning": (
                "Na etapa de interesse, volume bruto de cliques sem contexto de qualidade é uma "
                "métrica de vaidade. 1.000 cliques que bounceiam imediatamente valem menos que "
                "100 cliques que passam 3 minutos no site. Sempre combine CTR com métricas de "
                "comportamento pós-clique. Da mesma forma, alta taxa de engajamento em posts sociais "
                "que não se traduz em visitas ao site ou exploração mais profunda pode indicar "
                "entretenimento sem conexão com a marca."
            ),
            "benchmarks": {
                "ctr": "Meta: 1,5%+ forte para e-commerce. TikTok in-feed: 1,5-3%. Search: 3-8%. Display: 0,3-1%. Melhoria sobre o CTR da etapa de awareness (0,3-1,5%) é esperada.",
                "taxa_engajamento": "1-5% em redes sociais é considerado saudável. >3% é forte. A taxa deve ser medida sobre alcance, não impressões.",
                "conclusao_video": "15-40% de taxa de conclusão para ThruPlay (15s+). Maior indica interesse genuíno no conteúdo.",
                "tempo_na_pagina": "30s-2min para landing pages. >2 páginas por sessão indica exploração forte.",
                "cpc_brasil": "CPC do Meta no Brasil para e-commerce em média $0,38 (66% menor que o global de $1,14). Google Ads no Brasil varia: $1-8 dependendo da indústria.",
            },
        },
        "budget_allocation": {
            "binet_field_guidance": (
                "A etapa de interesse se posiciona na sobreposição entre construção de marca e "
                "ativação. O conteúdo deve ser primariamente educacional/entretenimento (caráter de "
                "construção de marca) mas pode incluir CTAs suaves para engajamento mais profundo "
                "(caráter de ativação). É aqui que a divisão 60/40 começa a se mesclar."
            ),
            "funnel_budget_split": (
                "Dentro da alocação de 'meio de funil' (tipicamente 20-30% do budget total), "
                "atividades da etapa de interesse competem com consideração. Campanhas de interesse "
                "devem receber aproximadamente 10-15% do budget total. Para marcas novas construindo "
                "audiência inicial, isso pode aumentar para 15-20%."
            ),
        },
        "creative_and_messaging": {
            "psychological_principles": {
                "lacuna_de_curiosidade": (
                    "Conteúdo que abre uma lacuna de conhecimento impulsiona cliques e engajamento. "
                    "Títulos e ganchos devem prometer valor sem entregá-lo completamente, "
                    "compelindo a audiência a clicar/assistir para resolver a lacuna."
                ),
                "teoria_da_carga_cognitiva": (
                    "Na etapa de interesse, audiências toleram um pouco mais de carga cognitiva "
                    "que em awareness, mas ainda preferem conteúdo escaneável e visual. Conteúdo "
                    "educacional deve usar revelação progressiva — revelar complexidade gradualmente."
                ),
                "cialdini_applicable": [
                    "Compromisso/Consistência — pequenos engajamentos iniciais (baixar um guia, assinar newsletter) aumentam a probabilidade de conversão futura",
                    "Prova Social — contadores de engajamento, depoimentos, sinais de 'tendência'",
                    "Afinidade — conteúdo identificável, expressão da personalidade da marca",
                ],
            },
            "content_strategy": (
                "Conteúdo educacional, divertido ou que resolve problemas ressoa mais. "
                "Posts de blog, guias práticos, vídeos curtos, infográficos que destacam como "
                "o produto/serviço aborda dores. Webinars, newsletters e conteúdo interativo "
                "como quizzes impulsionam engajamento mais profundo. "
                "O conteúdo deve demonstrar expertise sem ser abertamente promocional."
            ),
            "format_recommendations": [
                "Vídeo educacional curto (15-60s)",
                "Posts carrossel com dicas/insights",
                "Conteúdo de blog promovido via social/display",
                "Conteúdo interativo (quizzes, calculadoras, enquetes)",
                "Campanhas de captação de email/newsletter",
                "Patrocínio de podcast/colaborações com criadores",
            ],
        },
        "platform_stage_alignment": {
            "Meta (Instagram/Facebook)": {
                "why": (
                    "Objetivos de campanha de tráfego e engajamento são bem otimizados. "
                    "Os formatos de carrossel e Reels do Instagram incentivam o consumo de conteúdo. "
                    "Cliques com custo eficiente no Brasil ($0,38 CPC). Audiências lookalike de "
                    "engajadores refinam o targeting além do awareness amplo."
                ),
                "best_formats": "Carousel, Reels, Stories com swipe-up, Collection Ads",
            },
            "Google Ads (Display/Discovery)": {
                "why": (
                    "Campanhas Discovery alcançam usuários navegando conteúdo no Gmail, YouTube "
                    "e feed Discover — ideais para distribuição de conteúdo na etapa de interesse. "
                    "A rede Display permite alcance amplo mas contextualmente relevante. "
                    "Anúncios display responsivos auto-otimizam combinações criativas."
                ),
                "best_formats": "Discovery Ads, Responsive Display Ads, Gmail Ads",
            },
            "TikTok": {
                "why": (
                    "Formato de conteúdo nativo incentiva exploração e compartilhamento. "
                    "O algoritmo surfaça conteúdo para usuários interessados independente do "
                    "número de seguidores. Spark Ads permitem promover conteúdo orgânico que já "
                    "demonstrou engajamento. Forte para conteúdo educacional/divertido que "
                    "constrói afinidade com a marca."
                ),
                "best_formats": "In-Feed Video, Spark Ads (orgânico impulsionado), Branded Effects",
            },
            "Plataformas de conteúdo (blogs, Medium, LinkedIn)": {
                "why": (
                    "Plataformas de conteúdo longo são ideais para engajamento de interesse mais "
                    "profundo. Conteúdo otimizado para SEO proporciona geração orgânica sustentável "
                    "de interesse. LinkedIn é particularmente eficaz para conteúdo B2B na etapa "
                    "de interesse."
                ),
                "best_formats": "Artigos patrocinados, Posts de thought leadership, Documentos carrossel do LinkedIn",
            },
        },
        "common_mistakes": {
            "trafego_sem_qualidade": (
                "Otimizar para cliques sem monitorar comportamento pós-clique. "
                "Alto volume de cliques com taxa de rejeição de 90%+ indica desalinhamento "
                "entre criativo e landing page ou targeting de audiência irrelevante."
            ),
            "desalinhamento_landing_page": (
                "O criativo do anúncio promete uma coisa, a landing page entrega outra. "
                "A transição do anúncio ao destino deve ser contínua em mensagem, "
                "design visual e proposta de valor."
            ),
            "pular_para_conversao": (
                "Tentar vender antes que o prospect tenha desenvolvido interesse suficiente. "
                "CTAs de conversão prematuros em campanhas de interesse criam fricção "
                "e reduzem a eficácia geral da campanha."
            ),
            "conteudo_generico": (
                "Produzir conteúdo auto-promocional ao invés de material genuinamente útil/divertido. "
                "Conteúdo da etapa de interesse deve fornecer valor primeiro, associação de marca em segundo."
            ),
            "sem_proximo_passo": (
                "Gerar interesse sem um caminho claro para aprofundar o engajamento. "
                "Todo ponto de contato de interesse deve ter um próximo passo natural em direção à consideração."
            ),
        },
        "brazil_specifics": {
            "dados_de_mercado": (
                "O CPC do Meta no Brasil é 66% menor que a média global — excelente valor para "
                "campanhas de tráfego e engajamento. Redes sociais representam 53% do gasto em "
                "anúncios digitais. Publicidade de busca é o maior segmento digital (R$4,1B em 2024). "
                "Consumo de vídeo curto extremamente alto — Reels e TikTok dominam o consumo de "
                "conteúdo na etapa de interesse."
            ),
            "consideracoes_culturais": (
                "Audiências brasileiras engajam fortemente com storytelling e conteúdo orientado "
                "por personalidade. Conteúdo de criadores/influenciadores gera maior engajamento "
                "que conteúdo produzido pela marca. Conteúdo em português com referências culturais "
                "locais supera significativamente conteúdo internacional traduzido. "
                "Consumo mobile-first: 76% do consumo de anúncios digitais será mobile até 2028."
            ),
        },
    },

    "Consideração": {
        "theoretical_alignment": {
            "AIDA": "Desire — construção de preferência e avaliação de alternativas",
            "STDC": "Think — considerando ativamente soluções de categoria, pesquisando e comparando",
            "McKinsey_CDJ": "Avaliação Ativa — a fase crítica onde marcas são adicionadas ou removidas da consideração. Pontos de contato aqui são 2-3x mais influentes que durante a consideração inicial.",
            "Kotler_5A": "Ask — consumidores pesquisam ativamente, perguntam a pares, leem avaliações, comparam opções",
            "RACE": "Act tardio / Convert inicial — visitantes engajados avaliando a oferta",
            "Forrester": "Exploração Profunda — pesquisa multicanal sobre a marca e concorrentes",
            "Byron_Sharp": "Disponibilidade Física se torna crítica — a marca deve ser encontrável quando buscada ativamente",
            "Binet_Field": "Território de ativação começa — mensagens racionais sobre features/benefícios se tornam mais apropriadas",
        },
        "metric_interpretation": {
            "meaningful_metrics": {
                "primary": [
                    "CTR (mais alto esperado nesta etapa: 1-3%)",
                    "Métricas de qualidade de engajamento (comentários, salvamentos, compartilhamentos)",
                    "Tempo em páginas de produto/comparação",
                    "Profundidade de consumo de conteúdo (white papers, cases, demos visualizados)",
                    "Micro-conversões (cadastro em newsletter, adições à wishlist, solicitações de orçamento)",
                ],
                "secondary": [
                    "Taxa de visitas de retorno (avaliação multi-sessão)",
                    "Páginas por sessão em páginas de produto/solução",
                    "Taxa de conclusão de vídeo para demos de produto",
                    "Taxa de crescimento de audiência de remarketing",
                    "Aumento de buscas por termos de marca",
                ],
            },
            "vanity_metrics_warning": (
                "Na etapa de consideração, engajamento superficial (curtidas, reações) sem "
                "comportamento de avaliação mais profundo é uma métrica de vaidade. Alguém que "
                "curte um post mas nunca visita a página do produto não está verdadeiramente em "
                "consideração. Foque em comportamentos de avaliação: visitas a páginas de comparação, "
                "downloads de fichas técnicas, solicitações de demo, leitura de avaliações. "
                "Compradores B2B interagem com 3-7 peças de conteúdo antes de falar com vendas."
            ),
            "benchmarks": {
                "ctr": "1,0-3,0% esperado para campanhas de consideração. Maior que awareness (0,3-1,5%) porque a audiência tem intenção.",
                "micro_conversao": "Taxas de micro-conversão na consideração: 2-5% para downloads de conteúdo, 1-3% para inscrições em webinars, 5-15% para cadastros de email.",
                "impacto_nurturing": "Empresas com nurturing eficaz têm 50% mais leads prontos para venda a um custo 33% menor. Leads nutridos gastam 47% mais que leads não nutridos.",
                "consumo_conteudo": "B2B: 3-7 peças de conteúdo consumidas antes da conversa com vendas. B2C: 2-4 touchpoints típicos antes da decisão de compra.",
            },
        },
        "budget_allocation": {
            "binet_field_guidance": (
                "A etapa de consideração está firmemente no território de ATIVAÇÃO segundo Binet & Field. "
                "É aqui que os 40% (da regra 60/40) começam a se concentrar. A mensagem pode ser "
                "mais racional, focada em features e diretamente comparativa. No entanto, mantenha "
                "elementos emocionais para sustentar o halo de marca construído no awareness."
            ),
            "funnel_budget_split": (
                "Consideração tipicamente recebe 15-25% do budget total. "
                "Dentro do meio de funil (interesse + consideração combinados), consideração "
                "deve receber a maior parcela porque essas audiências estão mais próximas da "
                "conversão. Budgets de remarketing para audiências na etapa de consideração "
                "são tipicamente o gasto mais eficiente do funil."
            ),
        },
        "creative_and_messaging": {
            "psychological_principles": {
                "prova_social": (
                    "Na consideração, a prova social se torna o mecanismo de persuasão dominante. "
                    "Depoimentos, cases de sucesso, notas de avaliação, contagem de usuários e "
                    "endossos de pares abordam diretamente a mentalidade de avaliação. "
                    "Pessoas seguem o que outros estão fazendo — mostre que outros já escolheram sua solução."
                ),
                "autoridade": (
                    "Endossos de especialistas, certificações, prêmios e conteúdo de thought "
                    "leadership estabelecem credibilidade durante a fase de avaliação. "
                    "Validação de terceiros é mais persuasiva que afirmações da própria marca."
                ),
                "cialdini_applicable": [
                    "Prova Social — avaliações, depoimentos, cases de sucesso, contagem de usuários (primário)",
                    "Autoridade — endossos de especialistas, certificações, prêmios, menções na mídia",
                    "Compromisso/Consistência — trials gratuitos, amostras, primeiros passos de baixo risco",
                    "Afinidade — histórias de clientes com as quais prospects se identificam",
                ],
            },
            "content_strategy": (
                "Conteúdo comparativo, demos detalhados de produto, depoimentos de clientes, "
                "cases de sucesso com resultados mensuráveis. Webinars, guias de compra, calculadoras "
                "de ROI. O conteúdo deve abordar objeções diretamente e demonstrar vantagens "
                "competitivas. O formato deve acomodar engajamento mais profundo — vídeos mais "
                "longos, páginas detalhadas."
            ),
            "format_recommendations": [
                "Vídeos de demo de produto (60s-3min)",
                "Vídeos/carrosséis de depoimentos de clientes",
                "Guias de comparação e infográficos",
                "Anúncios de webinar/sessões ao vivo",
                "Anúncios de remarketing com prova social",
                "Carrosséis ou document ads de cases de sucesso",
                "Configuradores/calculadoras interativas de produto",
            ],
        },
        "platform_stage_alignment": {
            "Google Ads (Search)": {
                "why": (
                    "Search captura intenção de avaliação ativa. Usuários pesquisando 'melhor [produto]', "
                    "'[produto] vs [concorrente]', '[produto] avaliações' estão em consideração. "
                    "Search é um canal 'pull' conectando com indivíduos buscando soluções ativamente. "
                    "Taxas de conversão para search: 3,75% vs 0,77% para display."
                ),
                "best_formats": "Search Ads (palavras-chave de categoria e comparação), Responsive Search Ads",
            },
            "YouTube": {
                "why": (
                    "Vídeos de review e comparação de produtos são a 2ª categoria de conteúdo no YouTube. "
                    "O formato mais longo permite demonstração detalhada de produto. "
                    "Anúncios no YouTube com demos de produto impulsionam intenção de consideração. "
                    "TrueView In-Stream só cobra por visualizações engajadas (30s+ ou conclusão)."
                ),
                "best_formats": "TrueView In-Stream, Video Discovery Ads (aparece nos resultados de busca)",
            },
            "Meta (Instagram/Facebook)": {
                "why": (
                    "Remarketing para visitantes do site e engajadores é altamente eficiente. "
                    "Anúncios dinâmicos podem mostrar produtos relevantes baseados no comportamento "
                    "de navegação. O formato carrossel permite comparação multi-feature ou multi-produto. "
                    "Lead ads capturam dados da etapa de consideração sem sair da plataforma."
                ),
                "best_formats": "Campanhas de remarketing, Dynamic Ads, Lead Ads, Carousel",
            },
            "LinkedIn (B2B)": {
                "why": (
                    "Ecossistema profissional onde decisores avaliam soluções ativamente. "
                    "Thought Leadership Ads têm taxas de engajamento 5-10x maiores que conteúdo "
                    "patrocinado de empresa. Combinar cargo + setor + porte da empresa permite "
                    "targeting preciso de ICP. Document ads permitem compartilhar cases nativamente."
                ),
                "best_formats": "Thought Leadership Ads, Document Ads, Sponsored Content, Conversation Ads",
            },
        },
        "common_mistakes": {
            "tratar_todos_leads_igual": (
                "Empresas frequentemente usam conteúdo genérico de meio de funil que não atende "
                "indústrias, cargos ou dores específicas. Metade dos leads qualificados não está "
                "pronta para comprar imediatamente — nurturing segmentado é crítico. "
                "Conteúdo personalizado performa 3,2x melhor."
            ),
            "pular_para_conversao": (
                "Empurrar a compra antes que o prospect tenha avaliado completamente. "
                "Isso é especialmente danoso em B2B onde ciclos de decisão são longos. "
                "A etapa de consideração não pode ser apressada."
            ),
            "sem_estrategia_remarketing": (
                "Falhar em construir e ativar audiências de remarketing das campanhas de awareness. "
                "Visitantes do site que engajaram com conteúdo de awareness são a audiência de "
                "consideração de maior valor. Não retargetá-los desperdiça o investimento em awareness."
            ),
            "falta_variedade_conteudo": (
                "Mostrar a mesma mensagem repetidamente sem progredir a narrativa. "
                "Audiências de consideração precisam de peças de conteúdo diferentes que abordem "
                "aspectos diferentes da avaliação: features, preços, depoimentos, cases de sucesso, "
                "suporte de implementação, etc."
            ),
            "followup_inadequado": (
                "Criar ótimo conteúdo de meio de funil mas falhar no acompanhamento. "
                "Sem follow-ups estratégicos, leads perdem interesse ou escolhem concorrentes. "
                "Metade dos leads qualificados não está pronta para comprar imediatamente, "
                "tornando o nurturing crucial."
            ),
        },
        "brazil_specifics": {
            "dados_de_mercado": (
                "Publicidade de busca é o maior segmento de anúncios digitais no Brasil (R$4,1B em 2024). "
                "CPC do Google Ads no Brasil varia por indústria: marketing/publicidade a $4,22. "
                "WhatsApp é cada vez mais usado para conversas na etapa de consideração — "
                "95% das interações digitais marca-consumidor ocorrem no WhatsApp. "
                "Retail Media cresceu 41% YoY para R$3,5B — anúncios de listagem de produtos "
                "são pontos de contato chave de consideração em plataformas de marketplace."
            ),
            "consideracoes_culturais": (
                "Consumidores brasileiros dependem fortemente de recomendações de pares e opiniões "
                "de influenciadores durante a consideração. Grupos de WhatsApp e comentários no "
                "Instagram servem como canais de prova social. A cultura de avaliações está crescendo "
                "mas é menos madura que nos mercados EUA/UE. Comparação de preços é profundamente "
                "enraizada no comportamento de compra brasileiro — conteúdo comparativo performa "
                "muito bem."
            ),
        },
    },

    "Intenção": {
        "theoretical_alignment": {
            "AIDA": "Desire tardio / Action inicial — o prospect decidiu agir e está escolhendo onde/como",
            "STDC": "Think tardio / Do inicial — intenção comercial está se formando mas a transação ainda não ocorreu",
            "McKinsey_CDJ": "Momento da Compra se aproximando — o consumidor está estreitando para a seleção final",
            "Kotler_5A": "Ask tardio / Act inicial — a decisão está quase tomada, o prospect busca a confirmação final",
            "RACE": "Convert inicial — o prospect está demonstrando sinais de compra",
            "Forrester": "Exploração tardia / Compra inicial — avaliando condições finais de compra",
            "Byron_Sharp": "Disponibilidade Física é primordial — a marca DEVE ser facilmente comprável quando a intenção se forma",
            "Binet_Field": "Território puro de Ativação — mensagens de curto prazo, racionais e direcionadas à ação",
        },
        "metric_interpretation": {
            "meaningful_metrics": {
                "primary": [
                    "Leads Gerados (leads qualificados entrando no pipeline)",
                    "Custo por Lead (CPL) — eficiência da captura de leads",
                    "Taxa de conversão lead-para-oportunidade",
                    "Taxa de conclusão de formulário",
                    "Taxa de solicitação de demo/trial",
                ],
                "secondary": [
                    "Score de qualidade do lead (proporção SQL vs MQL)",
                    "Tempo do lead ao primeiro contato",
                    "Taxa de criação de carrinho (e-commerce)",
                    "Visitas à página de preços",
                    "Share de impressões de busca em palavras-chave de alta intenção",
                ],
            },
            "vanity_metrics_warning": (
                "Na etapa de intenção, VOLUME de leads sem avaliação de qualidade é enganoso. "
                "100 leads a R$25 de CPL que nunca convertem valem menos que 10 leads a R$250 "
                "de CPL que fecham a 30%. Sempre acompanhe o CPL junto com métricas de qualidade "
                "do lead (taxa de SQL, taxa de conversão do pipeline). Da mesma forma, adições ao "
                "carrinho sem conclusão de checkout indicam fricção no caminho de conversão, "
                "não intenção verdadeira."
            ),
            "benchmarks": {
                "conversao_lead": "Taxa média de conversão para Google Ads B2B: 3,04%. Com targeting de dados de intenção: significativamente maior. 94% dos profissionais de marketing B2B dizem que taxas de conversão de leads aumentam com dados de intenção.",
                "palavras_chave_alta_intencao": "Palavras-chave de fundo de funil (comprar, pedir, preço, demo, trial) têm o CPC mais alto mas também as maiores taxas de conversão. Search ads: 3,75% de conversão vs 0,77% do display.",
                "performance_retargeting": "Campanhas de retargeting usando sinais comportamentais de intenção (páginas visualizadas, tempo no site, início de formulários) superam significativamente o targeting frio.",
            },
        },
        "budget_allocation": {
            "binet_field_guidance": (
                "A etapa de intenção é ATIVAÇÃO PURA segundo Binet & Field. Este é o núcleo do "
                "budget de 40% para ativação. A mensagem deve ser direta, racional, focada em "
                "benefícios com calls-to-action claros. Mensuração de ROI de curto prazo é "
                "apropriada aqui."
            ),
            "funnel_budget_split": (
                "Intenção tipicamente recebe 10-20% do budget total. "
                "Este é frequentemente o gasto de maior ROAS do funil porque as audiências "
                "demonstraram sinais de compra. No entanto, este pool é limitado por "
                "quanto investimento em awareness/interesse/consideração gerou intenção. "
                "Subfinanciar topo de funil = audiência de intenção menor = menos para gastar aqui."
            ),
        },
        "creative_and_messaging": {
            "psychological_principles": {
                "escassez": (
                    "Quando as pessoas acreditam que algo é escasso, elas querem mais. "
                    "Ofertas por tempo limitado, contadores regressivos e mensagens de "
                    "disponibilidade limitada aceleram a intenção em ação. Mais poderoso nesta "
                    "etapa porque o prospect já quer comprar — a escassez fornece a urgência "
                    "para agir AGORA."
                ),
                "reciprocidade": (
                    "Pessoas tendem a retribuir um favor. Trials gratuitos, demos, consultorias "
                    "e conteúdo exclusivo na etapa de intenção criam um senso de obrigação. "
                    "O prospect recebe valor e se sente compelido a reciprocar com a compra."
                ),
                "cialdini_applicable": [
                    "Escassez — tempo limitado, disponibilidade limitada, ofertas exclusivas (primário nesta etapa)",
                    "Reciprocidade — trials gratuitos, consultorias, prévias exclusivas",
                    "Compromisso/Consistência — trial-para-compra, escalação de pequeno para grande",
                    "Prova Social — depoimentos orientados à conversão ('eu comprei e aqui está meu resultado')",
                ],
            },
            "content_strategy": (
                "Conteúdo de resposta direta: iscas digitais, ofertas de trial gratuito, "
                "agendamento de demos, informações de preço, comparações competitivas com "
                "posicionamento claro de vencedor. Landing pages com formulários curtos "
                "(3-5 campos máximo para captura inicial). Mensagens baseadas em urgência "
                "com propostas de valor claras. Remarketing agressivo para visitantes que "
                "visualizaram páginas de preços/produto."
            ),
            "format_recommendations": [
                "Search ads em palavras-chave de alta intenção (comprar, preço, demo, trial)",
                "Formulários de geração de leads (Meta Lead Ads, LinkedIn Lead Gen Forms)",
                "Anúncios de remarketing com CTAs fortes e ofertas",
                "Landing pages otimizadas para conversão",
                "Shopping ads (para e-commerce)",
                "Anúncios click-to-WhatsApp (alto desempenho específico do Brasil)",
            ],
        },
        "platform_stage_alignment": {
            "Google Ads (Search)": {
                "why": (
                    "A plataforma dominante de captura de intenção. Usuários buscando ativamente "
                    "com intenção comercial (palavras-chave transacionais). Search ads convertem a "
                    "3,75-4,40% entre indústrias — a maior taxa de qualquer formato de anúncio. "
                    "Search é marketing 'pull' — você captura intenção existente ao invés de criá-la. "
                    "Targeting de palavras-chave como 'comprar', 'preço', 'perto de mim', 'melhor' "
                    "captura demanda de fundo de funil."
                ),
                "best_formats": "Search Ads, Shopping Ads, Local Service Ads",
            },
            "Meta Ads (Lead Ads)": {
                "why": (
                    "Lead Ads capturam intenção sem sair da plataforma, reduzindo fricção. "
                    "Formulários pré-preenchidos usando dados do perfil do Facebook aumentam "
                    "taxas de conclusão. Retargeting de visitantes do site que mostraram sinais "
                    "de intenção (visualizações de página de produto, adições ao carrinho) é "
                    "altamente eficiente."
                ),
                "best_formats": "Lead Ads, Anúncios otimizados para conversão, Dynamic Product Ads",
            },
            "LinkedIn (Geração de Leads B2B)": {
                "why": (
                    "Lead Gen Forms pré-preenchem com dados profissionais (cargo, empresa, email). "
                    "Campanhas de InMail alcançam decisores diretamente. "
                    "Sinais de intenção B2B (download de conteúdo, participação em webinar) podem "
                    "ser rastreados. CPL mais alto mas tipicamente maior qualidade de lead para B2B."
                ),
                "best_formats": "Lead Gen Forms, Sponsored InMail, Conversation Ads",
            },
            "WhatsApp (específico do Brasil)": {
                "why": (
                    "WhatsApp converte 6x mais que e-commerce tradicional no Brasil. "
                    "93,7% de penetração significa que é o canal de captura de intenção mais acessível. "
                    "Anúncios click-to-WhatsApp no Meta + comércio conversacional = captura de intenção "
                    "sem fricção. Valor médio de carrinho recuperado: R$557,67 (aumento de 432% em relação "
                    "a 2023). Chatbots de IA lidam com 80% das conversas comerciais sem intervenção humana."
                ),
                "best_formats": "Anúncios Click-to-WhatsApp, Campanhas WhatsApp Business API",
            },
        },
        "common_mistakes": {
            "formularios_longos_demais": (
                "Cada campo adicional no formulário reduz a taxa de conclusão em 5-10%. "
                "Formulários de lead da etapa de intenção devem capturar dados mínimos viáveis "
                "(nome, email, telefone) e qualificar através do follow-up, não antecipadamente."
            ),
            "followup_lento": (
                "O tempo de resposta ao lead é crítico. Leads contatados em até 5 minutos têm "
                "9x mais probabilidade de converter do que aqueles contatados após 30 minutos. "
                "Automação para resposta imediata é essencial."
            ),
            "cpl_sem_qualidade": (
                "Otimizar para o menor CPL sem rastrear a conversão downstream. "
                "Leads baratos que nunca convertem desperdiçam recursos de vendas. "
                "Acompanhe CPL junto com taxa de SQL e conversão de pipeline."
            ),
            "ausencia_na_busca": (
                "Se a marca não está presente no Google quando prospects buscam com intenção, "
                "concorrentes capturam essa demanda. O share de impressões de busca em "
                "palavras-chave de alta intenção deve ser monitorado — perder share de "
                "impressões significa perder intenção."
            ),
            "ignorar_abandono_carrinho": (
                "A taxa média de abandono de carrinho é 70%. Não ter sequências automatizadas "
                "de recuperação (email, WhatsApp, retargeting) deixa receita massiva na mesa."
            ),
        },
        "brazil_specifics": {
            "dados_de_mercado": (
                "Campanhas de marketing via WhatsApp cresceram 64% em volume em 2024, alcançando "
                "59,2M de mensagens. Taxa de conversão do WhatsApp: 55% (vs e-commerce tradicional). "
                "Apenas 40% das empresas brasileiras usam campanhas automatizadas no WhatsApp — "
                "gap de oportunidade. Anúncios click-to-WhatsApp são o formato de anúncio Meta "
                "de crescimento mais rápido no Brasil. Google Ads search permanece como o maior "
                "segmento de anúncios digitais em R$4,1B."
            ),
            "consideracoes_culturais": (
                "Consumidores brasileiros preferem interação pessoal e humana mesmo em canais "
                "digitais. 59% dos consumidores não gostam de respostas automatizadas — equilibre "
                "automação com toque humano. Comércio conversacional via WhatsApp é culturalmente "
                "natural no Brasil. Métodos de pagamento boleto e Pix reduzem fricção na fronteira "
                "intenção/conversão. Consumidores brasileiros são altamente sensíveis a preço — "
                "comparação de compras é comportamento padrão."
            ),
        },
    },

    "Conversão/Ação": {
        "theoretical_alignment": {
            "AIDA": "Ação — o comportamento final, a compra ou cadastro",
            "STDC": "Do — o momento da transação, audiência pronta para agir",
            "McKinsey_CDJ": "Momento da Compra — o fechamento acontece, a marca é escolhida",
            "Kotler_5A": "Act — o consumidor completa a compra/cadastro",
            "RACE": "Convert — vendas, receita e lucro gerados",
            "Forrester": "Buy — processo de compra, experiência de checkout, satisfação com preço",
            "Byron_Sharp": "Disponibilidade Física é crítica — um caminho sem fricção até a compra determina o sucesso",
            "Binet_Field": "Pico de Ativação — campanhas de curto prazo, racionais e focadas em transação",
        },
        "metric_interpretation": {
            "meaningful_metrics": {
                "primary": [
                    "Conversões (total de transações/cadastros)",
                    "CPA (Custo por Aquisição)",
                    "ROAS (Retorno sobre Investimento em Anúncios)",
                    "Taxa de Conversão (visitantes para compradores)",
                    "Receita / Valor da Transação",
                ],
                "secondary": [
                    "Ticket Médio (AOV)",
                    "Taxa de abandono de carrinho (oportunidade de recuperação)",
                    "Taxa de conclusão de checkout",
                    "Custo por pedido vs valor vitalício do cliente",
                    "Atribuição (first-touch vs last-touch vs multi-touch)",
                ],
            },
            "vanity_metrics_warning": (
                "Na etapa de conversão, ROAS sem contexto pode ser enganoso. "
                "ROAS alto em remarketing pode estar tomando crédito por conversões que "
                "teriam acontecido de qualquer forma (problema de atribuição). CPA muito baixo em "
                "audiências de remarketing é esperado — a verdadeira questão é incrementalidade. "
                "Atenção também: julgar o desempenho de TODO o funil por métricas da etapa de "
                "conversão supervaloriza o last-touch e subvaloriza a construção de marca (Binet & Field)."
            ),
            "benchmarks": {
                "conversion_rate": "Média global de e-commerce: 3,17%. Nichos de alto desempenho: 5-15%. Mediana de landing pages: 6,6%. B2B Visitante-para-Lead: 2-5%, Oportunidade-para-Fechamento: 15-30%.",
                "search_vs_display": "Search ads: 3,75-4,40% de taxa de conversão. Display ads: 0,57-0,77%. Search é 5-6x mais eficiente em conversão.",
                "roas_targets": "Metas de ROAS variam: 3:1 mínimo para a maioria das marcas, 4:1 saudável, 6:1+ para audiências de remarketing/retenção. Campanhas de awareness NÃO devem ser medidas por ROAS.",
                "cart_abandonment": "Abandono de carrinho médio: 70%. Campanhas de recuperação podem recapturar 5-15% dos carrinhos abandonados.",
            },
        },
        "budget_allocation": {
            "binet_field_guidance": (
                "Conversão é a etapa definitiva de ativação. Todo o propósito dos 40% de budget "
                "de ativação culmina aqui. No entanto, o insight crítico de Binet & Field é que "
                "alocar excessivamente em conversão às custas de construção de marca cria picos "
                "de curto prazo mas declínio de longo prazo. A etapa de conversão COLHE a demanda "
                "criada pela construção de marca — ela não pode criar demanda do zero."
            ),
            "funnel_budget_split": (
                "Conversão tipicamente recebe 10-20% do budget total. Dados Fospha: marcas de "
                "melhor desempenho alocam apenas 10% para fundo de funil. Alocação maior (20-30%) "
                "é apropriada para marcas maduras com awareness forte e grandes audiências aquecidas. "
                "Para e-commerce em temporadas de pico (Black Friday, Natal), aumento temporário "
                "para 30-40% é comum."
            ),
        },
        "creative_and_messaging": {
            "psychological_principles": {
                "scarcity_and_urgency": (
                    "Contadores regressivos, indicadores de estoque limitado e ofertas por tempo "
                    "limitado impulsionam ação imediata. Mais eficaz quando o prospect já está "
                    "motivado — a escassez supera a última hesitação."
                ),
                "social_proof_at_conversion": (
                    "No momento da compra, depoimentos, notas de avaliação, selos de confiança "
                    "e sinais como 'X pessoas compraram hoje' reduzem a ansiedade e confirmam "
                    "a decisão. Sinais de confiança reduzem a fricção de conversão."
                ),
                "loss_aversion": (
                    "Pessoas sentem perdas 2x mais intensamente do que ganhos equivalentes. "
                    "Enquadrar o custo de NÃO agir (perder a oferta, perder a oportunidade) "
                    "é mais motivador do que enquadrar o que ganham."
                ),
                "cialdini_applicable": [
                    "Escassez — tempo/estoque limitado (principal motor de conversão)",
                    "Prova Social — avaliações, selos de confiança, contagens de compras",
                    "Reciprocidade — itens bônus, frete grátis acima de valor mínimo",
                    "Compromisso/Consistência — 'complete seu pedido' para abandonadores de carrinho",
                    "Unidade — pertencimento à comunidade da marca ('junte-se a 50.000+ clientes')",
                ],
            },
            "content_strategy": (
                "Resposta direta com CTA claro. Landing pages focadas em uma única ação. "
                "Sinais de confiança: depoimentos, selos de segurança, política de garantia/devolução. "
                "Alinhamento mensagem-anúncio é crítico (o que o anúncio diz deve corresponder à landing page). "
                "Otimização mobile-first (60% do tráfego é mobile). "
                "Teste A/B contínuo de headlines, CTAs e apresentação de ofertas."
            ),
            "format_recommendations": [
                "Search ads com extensões de preço, sitelinks e extensões de avaliação",
                "Shopping ads / Anúncios de listagem de produtos",
                "Remarketing para abandonadores de carrinho com imagens dos produtos",
                "Anúncios dinâmicos de produto mostrando itens visualizados/adicionados ao carrinho",
                "Landing pages com objetivo único de conversão",
                "Mensagens de recuperação via WhatsApp (específico do Brasil)",
                "Sequências de recuperação por email (carrinho/formulário abandonado)",
            ],
        },
        "platform_stage_alignment": {
            "Google Ads (Search/Shopping)": {
                "why": (
                    "Search captura os usuários de maior intenção. Taxas de conversão de 3,75-4,40% "
                    "são inigualáveis por qualquer outro canal. Shopping ads mostram preço, imagem do "
                    "produto e avaliações diretamente nos resultados — reduzindo fricção até a compra. "
                    "Campanhas Performance Max otimizam em todas as superfícies do Google para conversão."
                ),
                "best_formats": "Search Ads (termos de marca + transacionais), Shopping, Performance Max",
            },
            "Meta Ads (Conversion campaigns)": {
                "why": (
                    "Campanhas com objetivo de conversão usando Advantage+ Shopping otimizam entre "
                    "posicionamentos para máximo de compras. Anúncios dinâmicos de produto mostram "
                    "exatamente os produtos que o usuário visualizou/adicionou ao carrinho. Audiências "
                    "personalizadas de visitantes aquecidos convertem a taxas 4-10x maiores que audiências frias."
                ),
                "best_formats": "Advantage+ Shopping, Dynamic Product Ads, Collection Ads, campanhas de conversão",
            },
            "Google Ads (Remarketing)": {
                "why": (
                    "Remarketing display captura usuários em milhões de sites após demonstrarem "
                    "intenção de compra. Combinado com listas de remarketing para Search (RLSA), "
                    "permite ajustes de lance para visitantes conhecidos. Remarketing no YouTube "
                    "recaptura atenção através de vídeo."
                ),
                "best_formats": "RLSA, Display Remarketing, YouTube Remarketing",
            },
        },
        "common_mistakes": {
            "message_mismatch": (
                "O anúncio diz 'Ganhe uma auditoria gratuita' mas a landing page promove consultoria paga. "
                "Essa desconexão destrói taxas de conversão. Continuidade do anúncio à landing page "
                "em mensagem, visuais e oferta é essencial."
            ),
            "landing_page_friction": (
                "Formulários com campos demais, sem otimização mobile, paredes de texto, "
                "CTAs fracos ('Enviar' ao invés de 'Quero Meu Teste Grátis'), sem sinais de confiança. "
                "40% dos consumidores migram para concorrentes após uma experiência mobile ruim."
            ),
            "homepage_as_destination": (
                "Direcionar tráfego de conversão para a homepage ao invés de landing pages dedicadas. "
                "Landing pages devem ser hiperfocadas em um único objetivo de conversão. "
                "Homepages possuem distrações e caminhos de saída demais."
            ),
            "ignoring_attribution": (
                "Aceitar o ROAS pelo valor de face sem entender o modelo de atribuição. "
                "Atribuição last-click supervaloriza campanhas de conversão e subvaloriza "
                "awareness/consideração. Atribuição multi-touch oferece visão mais precisa."
            ),
            "cold_audience_conversion": (
                "Gastar budget de conversão em audiências frias que nunca ouviram falar da marca. "
                "Campanhas de conversão são mais eficientes com audiências aquecidas de remarketing. "
                "Campanhas de conversão para audiências frias têm CPA 5-10x mais alto."
            ),
            "no_testing_culture": (
                "Não fazer testes A/B em landing pages, CTAs, ofertas e textos de anúncios. "
                "Otimização de conversão é um processo contínuo, não uma configuração única. "
                "Marcas de referência testam 10+ variações de criativo simultaneamente."
            ),
        },
        "brazil_specifics": {
            "dados_de_mercado": (
                "CPC do Facebook Ads para e-commerce no Brasil: $0,38 (66% abaixo da média global). "
                "WhatsApp converte 6x mais que e-commerce tradicional — canal crítico de conversão. "
                "Pix reduziu drasticamente a fricção de checkout desde 2020. "
                "Boleto bancário ainda relevante para consumidores sem conta bancária. "
                "Black Friday é o maior evento de conversão (nota: Brasil também tem seus próprios "
                "picos sazonais no Carnaval e Dia das Crianças em 12 de outubro)."
            ),
            "consideracoes_culturais": (
                "Parcelamento é esperado pelo consumidor brasileiro — exibir '12x sem juros' "
                "aumenta significativamente as taxas de conversão. Faixas de frete grátis são um "
                "grande motor de conversão. CPM e CPC disparam no Carnaval, Independência, "
                "Dia das Crianças, Black Friday e Natal — ajustar budgets conforme necessidade. "
                "Selos de confiança (nota do Reclame Aqui, certificado SSL) são sinais de "
                "confiança importantes para o consumidor brasileiro."
            ),
        },
    },

    "Retenção/Fidelização": {
        "theoretical_alignment": {
            "AIDA": "Pós-AIDA — o modelo original não aborda retenção (uma limitação importante)",
            "STDC": "Care — clientes existentes com 2+ transações. A etapa mais negligenciada segundo Kaushik.",
            "McKinsey_CDJ": "Experiência Pós-Compra + Loop de Fidelidade — clientes satisfeitos pulam a avaliação e recompram diretamente, criando um ciclo virtuoso",
            "Kotler_5A": "Advocate — o objetivo final: clientes se tornam promotores ativos da marca",
            "RACE": "Engage — compras recorrentes, satisfação, advocacy, Net Promoter Score",
            "Forrester": "Engage — experiência contínua pós-compra com a marca em todos os canais",
            "Byron_Sharp": "Desafia o foco em fidelidade — Sharp argumenta que crescimento vem da aquisição, não da fidelidade. Fidelidade é em grande parte subproduto de market share (Lei da Dupla Penalidade). No entanto, reduzir churn desnecessário permanece importante.",
            "Binet_Field": "Construção de marca contribui para retenção através de disponibilidade mental sustentada. Ativação impulsiona recompra através de CRM, email e resposta direta.",
        },
        "metric_interpretation": {
            "meaningful_metrics": {
                "primary": [
                    "Valor Vitalício do Cliente (CLV) — receita total ao longo de todo o relacionamento",
                    "Taxa de Retenção / Taxa de Churn",
                    "Taxa de Recompra",
                    "ROAS em campanhas de retenção (tipicamente 4-10x, o mais alto do funil)",
                    "Net Promoter Score (NPS)",
                ],
                "secondary": [
                    "Score de Satisfação do Cliente (CSAT)",
                    "Tempo médio entre compras",
                    "Taxa de cross-sell / upsell",
                    "Taxa de indicação",
                    "Taxas de engajamento de email (abertura, clique, conversão)",
                    "Taxa de reativação (clientes dormentes)",
                ],
            },
            "vanity_metrics_warning": (
                "Na etapa de retenção, NPS bruto sem ação é uma métrica de vaidade. "
                "Taxas de abertura de email sozinhas não indicam fidelidade (indicam qualidade do "
                "assunto). Números de inscrição em programas de fidelidade não significam nada se os "
                "membros não engajam ativamente ou resgatam. Foque em métricas de fidelidade "
                "COMPORTAMENTAL: frequência de recompra, compras entre categorias e comportamentos "
                "de advocacy (indicações, avaliações)."
            ),
            "benchmarks": {
                "impacto_retencao": "Aumentar a retenção em apenas 5% pode aumentar os lucros em 75%. Vender para clientes existentes tem melhores margens e taxas de fechamento do que nova aquisição.",
                "formula_clv": "CLV = Valor Médio de Compra × Frequência de Compra × Vida Útil do Cliente. Melhoria em qualquer variável se compõe ao longo do tempo.",
                "roas_retencao": "ROAS em campanhas de retenção: 4-10x (o mais alto do funil porque a audiência já é qualificada e tem histórico de compras).",
                "falha_programa_fidelidade": "77% dos programas de fidelidade falham em 3 anos. 78% dos consumidores abandonam programas com limites difíceis de recompensa. 33% saem quando as recompensas são irrelevantes.",
            },
        },
        "budget_allocation": {
            "binet_field_guidance": (
                "Retenção usa AMBOS construção de marca (mantendo disponibilidade mental e "
                "conexão emocional) e ativação (CRM, email, ofertas diretas). "
                "O marketing mais custo-eficiente é para clientes existentes. "
                "No entanto, Sharp alerta contra alocar excessivamente em fidelidade "
                "às custas da aquisição — crescimento fundamentalmente requer novos clientes."
            ),
            "funnel_budget_split": (
                "Retenção tipicamente recebe 5-15% do budget total de mídia paga. "
                "No entanto, canais próprios (email, WhatsApp, CRM) devem ser a ferramenta "
                "primária de retenção, o que não consome budget de mídia. "
                "Remarketing pago para clientes existentes complementa os canais próprios. "
                "O gasto mais eficiente do funil, mas limitado pelo tamanho da base de clientes."
            ),
        },
        "creative_and_messaging": {
            "psychological_principles": {
                "reciprocidade": (
                    "Ofertas exclusivas, acesso antecipado e recompensas de fidelidade criam "
                    "um senso de tratamento especial que incentiva fidelidade recíproca. "
                    "Experiências positivas inesperadas (descontos surpresa, ofertas de aniversário) "
                    "geram reciprocidade mais forte do que as esperadas."
                ),
                "compromisso_consistencia": (
                    "Uma vez que clientes se identificam como usuários da marca, a consistência "
                    "impulsiona comportamento repetido. Marketing baseado em identidade ('como "
                    "cliente [Marca]') reforça o autoconceito. Pequenos compromissos (avaliações, "
                    "indicações, seguidores sociais) aprofundam o comprometimento."
                ),
                "unidade": (
                    "O princípio mais recente de Cialdini. Criar um senso de identidade compartilhada "
                    "e pertencimento à comunidade ('você é um dos nossos'). Comunidades de marca, "
                    "tiers VIP e acesso exclusivo alavancam este poderoso mecanismo de retenção."
                ),
                "cialdini_applicable": [
                    "Reciprocidade — recompensas de fidelidade, acesso exclusivo, presentes inesperados",
                    "Compromisso/Consistência — modelos de assinatura, reforço de identidade",
                    "Unidade — pertencimento à comunidade, status VIP, identidade compartilhada",
                    "Prova Social — 'Outros clientes como você também compraram...'",
                    "Escassez — ofertas exclusivas para membros, vagas VIP limitadas",
                ],
            },
            "content_strategy": (
                "Comunicação personalizada orientada por CRM. Fluxos de email: pós-compra, "
                "reativação, aniversário, cross-sell/upsell. Programas de fidelidade com "
                "recompensas significativas e alcançáveis. Conteúdo exclusivo e acesso antecipado. "
                "Conteúdo gerado pelo usuário e solicitação de avaliações. Programas de indicação. "
                "Conteúdo de sucesso do cliente mostrando como extrair mais valor do produto."
            ),
            "format_recommendations": [
                "Sequências de email personalizadas (pós-compra, win-back, cross-sell)",
                "Mensagens WhatsApp Business (alto desempenho específico do Brasil)",
                "Remarketing de audiência personalizada no Meta/Google",
                "Comunicações do programa de fidelidade",
                "Campanhas de conteúdo gerado pelo usuário",
                "Anúncios de programa de indicação/embaixador",
                "Notificações push de aplicativo",
                "Campanhas SMS/RCS",
            ],
        },
        "platform_stage_alignment": {
            "Email Marketing": {
                "why": (
                    "Canal de maior ROI para retenção ($36-42 de retorno por $1 gasto). "
                    "Canal totalmente próprio sem dependência de plataforma. Segmentação "
                    "e personalização baseadas em histórico de compras, comportamento de "
                    "navegação e nível de engajamento. Fluxos automatizados escalam sem custo incremental."
                ),
                "best_formats": "Sequências pós-compra, Séries de win-back, Cross-sell/upsell, Atualizações de fidelidade",
            },
            "WhatsApp Business (específico do Brasil)": {
                "why": (
                    "93,7% de penetração no Brasil — o canal de retenção mais acessível. "
                    "95% das interações marca-consumidor ocorrem no WhatsApp. "
                    "Taxas de abertura vastamente superiores ao email. Comércio conversacional "
                    "permite upsell/cross-sell em tempo real. Agentes de IA resolveram 80% das "
                    "conversas sem intervenção humana em 2024, com aumento de 150% em conversão."
                ),
                "best_formats": "Atualizações de pedido, Ofertas personalizadas, Mensagens de reativação, Recuperação de carrinho",
            },
            "Meta Ads (Audiências Personalizadas)": {
                "why": (
                    "Targeting de lista CRM permite alcançar clientes existentes com mensagens "
                    "personalizadas no Facebook, Instagram e Messenger. Anúncios dinâmicos mostram "
                    "produtos relevantes de cross-sell baseados no histórico de compras. "
                    "ROAS em audiências de clientes tipicamente 4-10x."
                ),
                "best_formats": "Campanhas de Custom Audience, Dynamic Ads, Catalog Sales",
            },
            "Google Ads (Customer Match)": {
                "why": (
                    "Listas de Customer Match permitem retargeting no Search, YouTube, Display "
                    "e Gmail. Campanhas RLSA podem ajustar lances para clientes recorrentes. "
                    "Anúncios no YouTube podem entregar storytelling de marca para clientes existentes."
                ),
                "best_formats": "Customer Match, RLSA, Retargeting no YouTube",
            },
        },
        "common_mistakes": {
            "ignorar_clientes_existentes": (
                "O erro de retenção mais comum: gastar todo o budget adquirindo novos clientes "
                "enquanto ignora a base existente. Segmentos de clientes existentes são as "
                "audiências publicitárias mais eficientes mas são frequentemente subatendidos."
            ),
            "tratar_clientes_como_prospects": (
                "Mostrar mensagens de aquisição para clientes existentes. Clientes que já "
                "compraram não precisam ser convencidos novamente — precisam de novos motivos "
                "para engajar, não o mesmo pitch repetido."
            ),
            "falhas_design_programa_fidelidade": (
                "77% dos programas de fidelidade falham em 3 anos. Razões comuns: "
                "(1) Limites difíceis de recompensa (78% abandonam por isso). "
                "(2) Recompensas irrelevantes (33% saem). "
                "(3) Regras excessivamente complexas. "
                "(4) Puramente transacional sem conexão emocional. "
                "(5) Personalização inadequada (80%+ clientes preferem experiências personalizadas). "
                "(6) Um único ponto de contato tóxico pode levar 72% dos clientes fiéis para um concorrente."
            ),
            "sem_segmentacao_por_recencia": (
                "Tratar todos os clientes da mesma forma independente da data da última compra. "
                "Segmentação RFM (Recência, Frequência, Monetário) é crítica. "
                "Um cliente que comprou ontem precisa de mensagens diferentes de um que "
                "não compra há 6 meses."
            ),
            "dependencia_excessiva_descontos": (
                "Treinar clientes a esperar promoções destrói margens. "
                "Retenção eficaz usa benefícios de valor agregado (acesso exclusivo, conteúdo, "
                "comunidade) junto com ofertas promocionais estratégicas."
            ),
        },
        "brazil_specifics": {
            "dados_de_mercado": (
                "Volume de marketing via WhatsApp cresceu 64% em 2024. Taxa de conversão no "
                "WhatsApp: 55%. Valor médio de carrinho recuperado: R$557,67 (aumento de 432% em "
                "relação a 2023). 70% das empresas brasileiras usam WhatsApp para marketing, mas "
                "apenas 40% usam campanhas automatizadas — oportunidade significativa de automação. "
                "Agentes de IA conduziram 90.000 conversas comerciais em 2024, resolvendo 80% "
                "sem intervenção humana."
            ),
            "consideracoes_culturais": (
                "WhatsApp é O canal de retenção no Brasil — mais importante que email. "
                "59% dos consumidores preferem interações semelhantes a humanas, não mensagens "
                "automatizadas robóticas. Consumidores brasileiros esperam comunicação responsiva, "
                "amigável e informal. Programas de fidelidade devem considerar hábitos de pagamento "
                "brasileiros (recompensas Pix, cashback, benefícios de parcelamento). "
                "Eventos culturais (Carnaval, Copa do Brasil, novelas) fornecem ganchos de "
                "engajamento para comunicações de retenção."
            ),
        },
    },
}

BUDGET_ALLOCATION_FRAMEWORKS = {
    "binet_field_60_40": {
        "name": "Regra 60/40 de Binet & Field",
        "description": (
            "Baseado na análise do IPA Databank com 996+ campanhas. A divisão ótima é ~60% "
            "construção de marca / 40% ativação de vendas para marcas de consumo. Construção "
            "de marca é emocional, de amplo alcance e criadora de fama. Ativação é racional, "
            "segmentada e orientada a ação. As duas abordagens NÃO devem ser combinadas no "
            "mesmo criativo — são trabalhos fundamentalmente diferentes."
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
            "Efeitos de marca se acumulam ao longo de 3-6+ meses. Efeitos de ativação alcançam "
            "pico em dias e decaem rapidamente. Investir excessivamente em ativação cria picos de "
            "curto prazo mas causa erosão de marca no longo prazo. As campanhas mais eficazes "
            "combinam AMBOS os tipos, mas em execuções criativas SEPARADAS."
        ),
    },
    "funnel_budget_splits": {
        "60_30_10_model": {
            "name": "Divisão Full-Funnel 60-30-10",
            "description": "Modelo tradicional: 60% awareness, 30% meio de funil, 10% fundo de funil",
            "awareness": 60,
            "consideration": 30,
            "conversion": 10,
            "when_to_use": "Marcas novas ou marcas entrando em novos mercados com baixo awareness",
        },
        "balanced_growth_model": {
            "name": "Divisão de Crescimento Equilibrado",
            "description": "Para marcas estabelecidas com awareness moderado",
            "awareness": 40,
            "consideration": 35,
            "conversion": 25,
            "when_to_use": "Empresas em fase de crescimento com awareness de base estabelecido",
        },
        "performance_heavy_model": {
            "name": "Divisão Pesada em Performance",
            "description": "Para marcas maduras com awareness forte, focadas em eficiência de conversão",
            "awareness": 25,
            "consideration": 35,
            "conversion": 40,
            "when_to_use": "Marcas maduras em temporada de pico ou com awareness forte existente",
        },
        "fospha_top_performers": {
            "name": "Padrão Fospha Top Performers",
            "description": "Padrão observado nas marcas de melhor desempenho",
            "awareness_and_consideration": 90,
            "conversion": 10,
            "when_to_use": "Marcas que priorizam crescimento sustentável de longo prazo sobre extração de curto prazo",
        },
    },
    "brazil_specific_considerations": (
        "No Brasil, os CPMs mais baixos (70-94% abaixo da média global) significam que budgets "
        "de construção de marca rendem mais do que em mercados maduros. O prêmio de conversão "
        "de 6x do WhatsApp significa que o fundo de funil pode ser mais eficiente via comércio "
        "conversacional. Redes sociais dominam com 53% do investimento digital, favorecendo "
        "construção de marca visual/vídeo. Picos sazonais (Carnaval, Dia das Crianças, Black "
        "Friday, Natal) exigem realocação temporária para conversão durante períodos de alta demanda."
    ),
}

CROSS_STAGE_PRINCIPLES = {
    "metrics_alignment_rule": (
        "NUNCA julgue uma campanha por métricas de outra etapa do funil. "
        "Campanhas de Awareness medidas por CPA sempre parecerão fracassos. "
        "Campanhas de Conversão medidas por alcance sempre parecerão ineficientes. "
        "Cada etapa tem seus próprios critérios de sucesso, benchmarks e alavancas de otimização. "
        "Este é o princípio isolado mais importante em planejamento de mídia."
    ),
    "full_funnel_synergy": (
        "A abordagem full-funnel entrega até 45% mais ROI do que campanhas de etapa única "
        "e 7% de lift em vendas offline. Cada etapa alimenta a próxima: awareness cria audiências "
        "de consideração, consideração cria audiências de intenção, intenção cria audiências de "
        "conversão. Subinvestir em qualquer etapa cria um gargalo que limita todo o funil. "
        "Dados da Amazon: campanhas usando 2+ soluções de vídeo tiveram 142% mais visualizações "
        "de página de produto e 84% mais taxa de compra vs campanhas de solução única."
    ),
    "halo_effects": (
        "Para muitas marcas, os efeitos halo de campanhas de topo de funil geram mais receita "
        "do que conversões diretas. Esses efeitos incluem: aumento do tráfego orgânico, crescimento "
        "do volume de buscas pela marca, aumento do tráfego direto, crescimento de seguidores em "
        "redes sociais e mídia espontânea/PR. Esses efeitos frequentemente não são capturados em "
        "modelos de atribuição last-click, levando a uma subvalorização sistemática do investimento "
        "em awareness."
    ),
    "byron_sharp_vs_funnel": (
        "O trabalho de Byron Sharp desafia o pensamento tradicional de funil ao argumentar que: "
        "(1) Crescimento vem da aquisição, não da fidelidade. "
        "(2) Targeting deve ser amplo, não de nicho. "
        "(3) Alcance importa mais que frequência. "
        "(4) Ativos distintivos importam mais que posicionamento diferenciado. "
        "Isso não invalida o planejamento baseado em funil, mas sugere que até campanhas de "
        "'consideração' e 'conversão' devem manter elementos de amplo alcance e ativos "
        "distintivos de marca, ao invés de se tornarem puramente racionais/funcionais."
    ),
    "attribution_complexity": (
        "Nenhum modelo de atribuição isolado captura o quadro completo. Last-click supervaloriza "
        "a etapa de conversão. First-click supervaloriza awareness. Modelos multi-touch tentam "
        "equilibrar, mas exigem implementação sofisticada. Testes de incrementalidade (geo-lift "
        "studies, conversion lift studies) oferecem a medição mais precisa do impacto real da "
        "campanha em cada etapa. Media Mix Modeling (MMM) é essencial para compreender os "
        "efeitos de longo prazo da construção de marca."
    ),
}


def _get_funnel_metric_doctrine(etapa: str) -> str:
    """Gera doutrina conceitual profunda sobre como interpretar métricas nesta etapa do funil.

    Esta função produz um bloco de texto extenso, conceitual e prescritivo que instrui a IA
    a analisar métricas SEMPRE à luz da etapa do funil, com fundamentação teórica.
    """
    doctrines = {
        "Consciência (Awareness)": """
    DOUTRINA DE MÉTRICAS PARA CONSCIÊNCIA (AWARENESS)

    A etapa de Consciência existe para plantar a marca na memória de longo prazo do consumidor.
    Segundo o modelo "How Brands Grow" de Byron Sharp, marcas crescem primariamente através da
    aquisição de novos compradores leves (light buyers), o que exige alcance massivo e repetição
    controlada. Binet & Field demonstraram em "The Long and the Short of It" que campanhas de
    construção de marca (emocionais, de amplo alcance) geram efeitos de negócio que se acumulam
    ao longo de 6+ meses, enquanto campanhas de ativação geram picos de curto prazo que decaem
    rapidamente. A implicação direta é: métricas de conversão (CPA, ROAS, leads) são
    CONCEITUALMENTE INADEQUADAS para avaliar awareness porque medem efeitos de curto prazo em
    uma estratégia que opera no longo prazo.

    O que medir e por quê:
    - ALCANCE e IMPRESSÕES são as métricas primárias porque refletem diretamente o objetivo:
      quantas pessoas foram expostas à marca. O efeito de mera exposição (Zajonc, 1968) demonstra
      que a simples exposição repetida gera familiaridade e preferência, mesmo sem atenção consciente.
    - CPM (Custo por Mil Impressões) é a métrica de eficiência porque mede o custo de cada exposição.
      Um CPM mais baixo significa mais exposições por real investido, e no Brasil o Meta Ads oferece
      CPMs 70-94% abaixo do benchmark global, tornando-o excepcionalmente eficiente para awareness.
    - FREQUÊNCIA deve ser controlada entre 1.5-4x por semana. Abaixo disso, a exposição é insuficiente
      para gerar lembrança. Acima de 8x sem rotação criativa, gera fadiga (a curva em U invertido do
      efeito de mera exposição). A frequência ótima para brand lift está entre 4-7 exposições totais.
    - BRAND LIFT é o indicador mais direto de sucesso em awareness, mas requer estudos específicos
      (Brand Lift Studies do Meta/Google/YouTube).

    O que NÃO medir (e por quê):
    - CPA em awareness é um ERRO CONCEITUAL. Kaushik (modelo STDC) define a audiência de "See" como
      pessoas SEM intenção comercial. Cobrar conversão de quem não tem intenção é medir o termômetro
      errado. É como julgar uma escola pela receita dos alunos no primeiro mês de aula.
    - ROAS em awareness é igualmente inadequado. O retorno de campanhas de marca se materializa em
      6-18 meses (Binet & Field), não no período da campanha. Medir ROAS imediato em awareness leva
      ao subinvestimento crônico em marca — o erro mais custoso do marketing digital.
    - CTR em awareness é uma métrica secundária no máximo. Baixo CTR é ESPERADO e ACEITÁVEL porque
      o objetivo não é gerar cliques, mas gerar exposição e memorização.
    """,

        "Interesse": """
    DOUTRINA DE MÉTRICAS PARA INTERESSE

    A etapa de Interesse é a transição entre a exposição passiva (Consciência) e a avaliação ativa
    (Consideração). No modelo STDC de Avinash Kaushik, é a fronteira entre "See" e "Think" — a
    audiência demonstrou curiosidade mas ainda não está avaliando soluções ativamente. No framework
    de Binet & Field, o Interesse ocupa a ZONA DE SOBREPOSIÇÃO entre construção de marca (60%) e
    ativação (40%): o conteúdo deve ser predominantemente emocional/educacional mas pode incluir
    CTAs suaves para engajamento mais profundo. No modelo de Byron Sharp, esta é a fase de reforço
    da Disponibilidade Mental — a marca já foi exposta e agora precisa criar associações com pontos
    de entrada de categoria (Category Entry Points) para ser lembrada quando a necessidade surgir.

    O que medir e por quê:
    - CTR (Taxa de Cliques) é primário porque indica RELEVÂNCIA CRIATIVA: se a audiência exposta
      na fase de awareness clica, significa que a mensagem ressoou e gerou curiosidade suficiente
      para buscar mais informação. Um CTR de 1.5%+ é forte para e-commerce no Meta.
    - CPC (Custo por Clique) é a métrica de EFICIÊNCIA nesta etapa. No Brasil, o Meta oferece CPC
      médio de $0.38 para e-commerce (66% menor que a média global), tornando a geração de interesse
      particularmente custo-eficiente.
    - ENGAJAMENTO QUALITATIVO (tempo no site, páginas por sessão, taxa de rejeição) é CRÍTICO.
      1.000 cliques que bounceiam em 3 segundos valem menos que 100 cliques que navegam 3 páginas
      por 2+ minutos. Sempre cruze CTR com comportamento pós-clique.
    - TAXA DE CONCLUSÃO DE VÍDEO (ThruPlay 15s+) indica consumo genuíno de conteúdo, não apenas
      exposição passiva.

    O que NÃO medir (e por quê):
    - VOLUME BRUTO DE CLIQUES sem contexto de qualidade é métrica de vaidade. Alto volume + 90%
      de bounce rate = dinheiro desperdiçado em tráfego irrelevante.
    - CPA/ROAS permanecem PREMATUROS. A audiência está curiosa, não comprando. Cobrar conversão
      de quem está explorando é como pedir casamento no primeiro encontro — gera rejeição.
    - CONVERSÕES DIRETAS desta etapa devem ser tratadas como bônus, não como objetivo. Se
      aparecerem, ótimo, mas a etapa existe para nutrir interesse, não para fechar vendas.
    """,

        "Consideração": """
    DOUTRINA DE MÉTRICAS PARA CONSIDERAÇÃO

    A etapa de Consideração é onde o framework McKinsey Consumer Decision Journey se torna mais
    crítico: é a fase de "Avaliação Ativa" onde marcas são ADICIONADAS ou REMOVIDAS do conjunto
    de consideração. Pesquisas mostram que os touchpoints nesta fase são 2-3x mais influentes que
    na consideração inicial. No modelo STDC de Kaushik, é o coração do "Think" — a audiência está
    ATIVAMENTE pesquisando e comparando soluções. Segundo Binet & Field, estamos firmemente no
    território de ATIVAÇÃO (os 40% da regra 60/40): a mensagem pode ser mais racional, focada em
    features e diretamente comparativa, mas deve manter elementos emocionais para sustentar o halo
    de marca construído no awareness. Byron Sharp adiciona que a Disponibilidade Física se torna
    crítica — a marca DEVE ser facilmente encontrável quando buscada ativamente.

    O que medir e por quê:
    - CTR QUALIFICADO (1-3% esperado, maior que awareness) indica que audiências com intenção estão
      respondendo ao conteúdo. CTR abaixo de 1% na consideração sugere que o criativo não está
      ressoando com a audiência que avalia alternativas.
    - MICRO-CONVERSÕES são o indicador chave: downloads de conteúdo (2-5%), inscrições em webinars
      (1-3%), cadastros de email (5-15%), adições à wishlist, solicitações de orçamento. Cada uma
      indica progressão no funil sem exigir a compra.
    - ENGAJAMENTO PROFUNDO (comentários, salvamentos, compartilhamentos) distingue quem está
      genuinamente avaliando de quem apenas passou os olhos.
    - CRESCIMENTO DA AUDIÊNCIA DE REMARKETING é um KPI estratégico: quantas pessoas novas entraram
      nas listas de retargeting após interagir com conteúdo de consideração?

    O que NÃO medir (e por quê):
    - ENGAJAMENTO SUPERFICIAL (curtidas, reações) sem comportamento de avaliação mais profundo é
      vaidade. Alguém que curte um post mas nunca visita a página do produto NÃO está considerando.
    - IMPRESSÕES/ALCANCE são métricas de awareness, não de consideração. Volume de exposição é
      irrelevante se a audiência não está se aprofundando na avaliação.
    - CONVERSÃO PREMATURA: empurrar para compra antes da avaliação completa é especialmente danoso
      em B2B (ciclos de decisão longos) e prejudica a confiança construída.
    """,

        "Intenção": """
    DOUTRINA DE MÉTRICAS PARA INTENÇÃO

    A etapa de Intenção é onde a intenção comercial se cristaliza. No modelo AIDA, é a fronteira
    entre Desire e Action — o prospect decidiu agir e está escolhendo onde e como. No STDC de
    Kaushik, é o final do "Think" entrando no "Do" — a transação está próxima mas ainda não
    ocorreu. Segundo Binet & Field, estamos em ATIVAÇÃO PURA: este é o núcleo dos 40% de budget
    de ativação, com mensagens diretas, racionais e focadas em benefícios com CTAs claros. Byron
    Sharp enfatiza que a Disponibilidade Física é PRIMORDIAL — se a marca não é facilmente
    comprável quando a intenção se forma, o prospect irá para um concorrente.

    O que medir e por quê:
    - LEADS GERADOS (leads qualificados entrando no pipeline) é a métrica-chave. Mas ATENÇÃO:
      não é volume bruto de leads — é volume de leads QUALIFICADOS. 100 leads a R$25 CPL que
      nunca convertem valem menos que 10 leads a R$250 CPL que fecham a 30%.
    - CPL (Custo por Lead) é a métrica de eficiência, mas SEMPRE deve ser cruzado com a taxa
      de SQL (Sales Qualified Lead). CPL baixo com taxa de SQL de 5% é pior que CPL alto com
      taxa de SQL de 40%.
    - TAXA DE CONVERSÃO DE LEAD (lead → oportunidade → venda) é o indicador de qualidade
      downstream que valida se os leads gerados são genuínos.
    - TAXA DE CONCLUSÃO DE FORMULÁRIO indica a eficiência do mecanismo de captura. Cada campo
      adicional reduz completions em 5-10%.

    O que NÃO medir (e por quê):
    - VOLUME DE LEADS sem avaliação de qualidade é o erro clássico desta etapa. O departamento
      de marketing celebra 1.000 leads baratos enquanto vendas reclama que nenhum converte.
    - IMPRESSÕES/ALCANCE são completamente irrelevantes aqui. A audiência é pequena e qualificada
      — o que importa é captura, não exposição.
    - ENGAJAMENTO DE CONTEÚDO (curtidas, compartilhamentos) tem utilidade zero na etapa de
      intenção. Se o prospect está pronto para comprar, ele quer um formulário ou botão de
      compra, não um artigo educacional.
    """,

        "Conversão/Ação": """
    DOUTRINA DE MÉTRICAS PARA CONVERSÃO/AÇÃO

    A etapa de Conversão é onde toda a estratégia de funil culmina. No modelo AIDA, é a "Ação"
    final. No STDC de Kaushik, é o "Do" — a audiência está pronta para transacionar. Segundo
    Binet & Field, esta é a etapa de pico de ativação: campanhas de curto prazo, racionais e
    focadas em transação. O insight crítico de Binet & Field é que alocar EXCESSIVAMENTE em
    conversão às custas de construção de marca cria picos de curto prazo mas DECLÍNIO de longo
    prazo. A conversão COLHE a demanda criada pela construção de marca — ela não pode criar
    demanda do zero. Byron Sharp complementa: a Disponibilidade Física (caminho sem fricção até
    a compra) determina o sucesso.

    O que medir e por quê:
    - CONVERSÕES (total de transações/cadastros) é a métrica final absoluta desta etapa. É o
      indicador direto de sucesso: quantas pessoas completaram a ação desejada?
    - CPA (Custo por Aquisição) é a métrica de eficiência. Benchmarks: 3,75-4,40% de taxa de
      conversão para Search Ads, 0,57-0,77% para Display. O CPA aceitável depende do LTV do
      cliente — CPA de R$200 é excelente se o LTV é R$5.000.
    - ROAS (Return on Ad Spend) é o indicador de retorno financeiro. Metas: 3:1 mínimo para a
      maioria das marcas, 4:1 saudável, 6:1+ para remarketing/retenção. MAS: ROAS sem contexto
      de atribuição é enganoso — ROAS alto em remarketing pode estar tomando crédito por
      conversões que teriam acontecido organicamente (problema de incrementalidade).
    - TICKET MÉDIO (AOV) complementa as conversões: não basta converter, o valor por transação
      também importa.

    O que NÃO medir (e por quê):
    - IMPRESSÕES e ALCANCE em conversão são métricas de awareness. Se você tem 10 milhões de
      impressões e zero vendas, o awareness falhou — mas medir impressões na conversão é
      olhar para o indicador errado.
    - ROAS pelo valor de face sem modelo de atribuição. Atribuição last-click SUPERVALORIZA
      campanhas de conversão e SUBVALORIZA awareness/consideração. Multi-touch é mais preciso.
    - CTR em conversão é secundário no máximo. O que importa é o que acontece DEPOIS do clique.
    """,

        "Retenção/Fidelização": """
    DOUTRINA DE MÉTRICAS PARA RETENÇÃO/FIDELIZAÇÃO

    A etapa de Retenção é frequentemente a mais negligenciada e a mais lucrativa. No modelo STDC
    de Kaushik, é "Care" — clientes existentes com 2+ transações, a etapa que ele considera a
    mais subinvestida em marketing digital. No McKinsey CDJ, clientes satisfeitos criam um "Loop
    de Fidelidade" que pula a avaliação e vai direto à recompra, criando um ciclo virtuoso. No
    modelo de Kotler (5A), o objetivo é criar "Advocates" — clientes que se tornam promotores
    ativos da marca. Byron Sharp, no entanto, DESAFIA o foco excessivo em fidelidade: ele
    argumenta que crescimento vem primariamente da aquisição de novos compradores e que fidelidade
    é em grande parte subproduto do market share (Lei da Dupla Penalidade). Ainda assim, reduzir
    churn desnecessário permanece importante. Binet & Field mostram que retenção usa AMBOS
    construção de marca (mantendo disponibilidade mental e conexão emocional) e ativação (CRM,
    email, ofertas diretas).

    O que medir e por quê:
    - CLV (Customer Lifetime Value) é a métrica-rainha da retenção. CLV = Valor Médio de Compra ×
      Frequência de Compra × Vida Útil do Cliente. Aumentar a retenção em apenas 5% pode aumentar
      os lucros em 75%. Melhoria em qualquer variável se compõe exponencialmente ao longo do tempo.
    - TAXA DE RETENÇÃO / CHURN RATE é o indicador direto de sucesso. Vender para clientes existentes
      tem melhores margens e taxas de fechamento do que nova aquisição.
    - TAXA DE RECOMPRA indica comportamento de fidelidade REAL (não declarado). É a prova concreta
      de que o cliente voltou e transacionou novamente.
    - ROAS EM CAMPANHAS DE RETENÇÃO é tipicamente o mais alto do funil inteiro (4-10x) porque a
      audiência já é qualificada e tem histórico de compras.

    O que NÃO medir (e por quê):
    - NPS bruto sem ação é vaidade. Um NPS alto que não se traduz em recompras ou indicações é
      apenas uma pesquisa satisfatória, não evidência de fidelidade comportamental.
    - TAXA DE ABERTURA DE EMAIL sozinha indica qualidade do assunto, não fidelidade. Foque em
      taxas de conversão dos emails, não apenas aberturas.
    - INSCRIÇÕES EM PROGRAMAS DE FIDELIDADE não significam nada se membros não resgatam. 77% dos
      programas de fidelidade falham em 3 anos justamente por medir inscrição ao invés de
      engajamento ativo.
    - MÉTRICAS DE AQUISIÇÃO (alcance, impressões, novos visitantes) são irrelevantes para retenção.
      Aqui o objetivo é aprofundar relacionamentos existentes, não expandir a base.
    """,
    }

    return doctrines.get(etapa, "")


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
            f"  - {platform}: {info.get('why', '')} | Melhores formatos: {info.get('best_formats', '')}"
        )
    platform_block = "\n".join(platform_lines)

    mistake_lines = []
    for mistake, description in mistakes.items():
        mistake_lines.append(f"  - {mistake}: {description}")
    mistakes_block = "\n".join(mistake_lines)

    brazil_market = brazil.get("dados_de_mercado", "") or brazil.get("market_data", "")
    brazil_culture = brazil.get("consideracoes_culturais", "") or brazil.get("cultural_considerations", "")

    metric_doctrine = _get_funnel_metric_doctrine(etapa)

    enriched = f"""
=== CONTEXTO ESTRATÉGICO APROFUNDADO: "{etapa}" ===

{metric_doctrine}

**ALINHAMENTO TEÓRICO (Frameworks Acadêmicos):**
{theory_block}

**MÉTRICAS SIGNIFICATIVAS:**
  Primárias: {primary_metrics}
  Secundárias: {secondary_metrics}

**ALERTA — MÉTRICAS DE VAIDADE NESTA ETAPA:**
{vanity_warning}

**BENCHMARKS DE REFERÊNCIA:**
{bench_block}

**ALOCAÇÃO DE BUDGET (Binet & Field):**
{binet_guidance}

**ALOCAÇÃO POR FUNIL:**
{funnel_split}

**PRINCÍPIOS PSICOLÓGICOS APLICÁVEIS:**
{chr(10).join(psych_lines)}
  Princípios de Cialdini mais relevantes:
{chr(10).join(cialdini_lines)}

**ESTRATÉGIA DE CONTEÚDO:**
{content_strategy}

**FORMATOS RECOMENDADOS:**
{chr(10).join(format_lines)}

**ALINHAMENTO PLATAFORMA-ETAPA:**
{platform_block}

**ERROS COMUNS E ANTI-PADRÕES (PESQUISA):**
{mistakes_block}

**ESPECIFICIDADES DO MERCADO BRASILEIRO:**
  Dados de mercado: {brazil_market}
  Considerações culturais: {brazil_culture}
"""
    return enriched
