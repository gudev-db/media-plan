from typing import Dict, Any

from utils.constants.constants import BENCHMARKS_BR, TEMPLATES_ALOCACAO_BUDGET, KPIS_POR_ETAPA, PLATAFORMA_OBJETIVOS, get_enriched_funnel_context, CROSS_STAGE_PRINCIPLES


def _extract_okrs(params: Dict[str, Any]):
    okrs_escolhidos = [k for k, v in params['metricas'].items() if v['selecionada']]
    metas_especificas = [f"{k}: {v['valor']}" for k, v in params['metricas'].items() if v['selecionada'] and v['valor']]

    primarios = [k for k, v in params['metricas'].items() if v['selecionada'] and v.get('hierarquia') == 'primario']
    secundarios = [k for k, v in params['metricas'].items() if v['selecionada'] and v.get('hierarquia') in ('secundario', 'terciario')]

    return okrs_escolhidos, metas_especificas, primarios, secundarios


def _get_benchmark_block(params: Dict[str, Any]) -> str:
    contexto = params.get('benchmarks_contexto', '')
    if contexto:
        return f"\n    **Benchmarks Brasil (referência):**\n{contexto}\n"

    linhas = []
    for plat in params.get('ferramentas', []):
        bench = BENCHMARKS_BR.get(plat)
        if not bench:
            continue
        partes = []
        for metrica, vals in bench.items():
            partes.append(f"{metrica}: {vals['unidade']}{vals['min']}-{vals['max']} (méd. {vals['medio']})")
        linhas.append(f"    - {plat}: {' | '.join(partes)}")
    return "\n    **Benchmarks Brasil (referência):**\n" + "\n".join(linhas) + "\n" if linhas else ""


def _get_templates_block(params: Dict[str, Any]) -> str:
    linhas = []
    for nome, tpl in TEMPLATES_ALOCACAO_BUDGET.items():
        dist = ", ".join(f"{k}: {v}%" for k, v in tpl["distribuicao"].items() if v > 0)
        linhas.append(f"    - {nome}: {dist}")
    return "\n    **Templates de Alocação (referência):**\n" + "\n".join(linhas) + "\n"


def _get_kpi_definitions_block(params: Dict[str, Any]) -> str:
    """Injeta definições, fórmulas e faixas típicas dos KPIs selecionados."""
    etapa = params.get('etapa_funil', '')
    kpis_etapa = KPIS_POR_ETAPA.get(etapa, {})
    selecionados = {k for k, v in params.get('metricas', {}).items() if v.get('selecionada')}
    if not selecionados:
        return ""

    linhas = []
    for tier in ("primarios", "secundarios", "terciarios"):
        for kpi in kpis_etapa.get(tier, []):
            if kpi["nome"] in selecionados:
                linhas.append(
                    f"    - **{kpi['nome']}** ({tier[:-1].title()}): "
                    f"{kpi['descricao']}. "
                    f"Fórmula: {kpi['formula']}. "
                    f"Faixa típica: {kpi['faixa_tipica']}. "
                    f"Quando usar: {kpi['quando_usar']}"
                )
    if not linhas:
        return ""
    return "\n    **Definições dos KPIs selecionados:**\n" + "\n".join(linhas) + "\n"


def _get_funnel_stage_context(params: Dict[str, Any]) -> str:
    etapa = params.get('etapa_funil', '')
    enriched = get_enriched_funnel_context(etapa)
    if not enriched:
        return ""

    cross_stage = CROSS_STAGE_PRINCIPLES
    bloco = enriched + f"""
=== PRINCIPIOS CROSS-STAGE (aplicar sempre) ===
- REGRA DE ALINHAMENTO DE METRICAS: {cross_stage['metrics_alignment_rule']}
- SINERGIA FULL-FUNNEL: {cross_stage['full_funnel_synergy']}
- EFEITOS HALO: {cross_stage['halo_effects']}
- COMPLEXIDADE DE ATRIBUICAO: {cross_stage['attribution_complexity']}
"""
    return bloco


def _get_funnel_rules_block(etapa_funil: str, primarios: list, secundarios: list) -> str:
    """Gera bloco de regras prescritivas sobre funil para injetar em todos os prompts."""
    return f"""
    === REGRAS CRÍTICAS DE ANÁLISE POR ETAPA DO FUNIL ===

    A etapa do funil é "{etapa_funil}". Isso determina TODA a lógica de análise:

    1. HIERARQUIA DE MÉTRICAS (OBRIGATÓRIA):
       - KPIs PRIMÁRIOS desta etapa: {", ".join(primarios) if primarios else "os definidos para " + etapa_funil}
         → São o FOCO ABSOLUTO da análise. Toda recomendação DEVE ser orientada a maximizá-los.
       - KPIs SECUNDÁRIOS: {", ".join(secundarios) if secundarios else "de suporte"}
         → Servem de SUPORTE e diagnóstico. Mencioná-los como monitoramento, nunca como objetivo.
       - KPIs TERCIÁRIOS / de outras etapas:
         → NUNCA devem ser apresentados como relevantes. Se mencionados, OBRIGATORIAMENTE
           adicionar aviso: "⚠️ Métrica de referência apenas — não é indicador de sucesso para {etapa_funil}."

    2. REGRA DE OURO (Kaushik / Binet & Field / Byron Sharp):
       - NUNCA julgar uma campanha por métricas de outra etapa do funil.
       - Exemplo: Campanha de Awareness medida por CPA = erro conceitual grave.
       - Exemplo: Campanha de Conversão medida por Alcance = análise irrelevante.
       - Cada etapa tem seus próprios critérios de sucesso, benchmarks e alavancas de otimização.

    3. FRAMEWORK TEÓRICO APLICÁVEL:
       - Awareness: Binet & Field (60/40), Byron Sharp (Mental Availability, Reach > Frequency),
         Kaushik STDC ("See" = sem intenção comercial, medir por exposição e lembrança).
       - Interesse: Zona de sobreposição brand building / ativação. Medir engajamento qualitativo.
       - Consideração: Território de ATIVAÇÃO (Binet & Field). Social proof, autoridade, comparação.
       - Intenção: Leads, micro-conversões. CPL e taxa de conversão de lead são o norte.
       - Conversão/Ação: Performance pura. CPA, ROAS, receita. Métricas de vaidade = alcance/impressões.
       - Retenção: LTV, recompra, churn. Métricas de aquisição são irrelevantes aqui.

    4. ALERTAS DE MÉTRICAS DE VAIDADE:
       - Sempre que mencionar uma métrica que NÃO é primária para a etapa, classificá-la
         explicitamente como "métrica de referência" ou "métrica de vaidade para esta etapa".
       - Incluir uma seção "⚠️ Métricas que NÃO indicam sucesso nesta etapa" quando aplicável.
    """


def gerar_recomendacao_estrategica(modelos, params: Dict[str, Any]) -> str:
    etapa_funil = params['etapa_funil']
    okrs_escolhidos, metas_especificas, primarios, secundarios = _extract_okrs(params)
    benchmark_block = _get_benchmark_block(params)
    kpi_defs_block = _get_kpi_definitions_block(params)
    funnel_context = _get_funnel_stage_context(params)
    funnel_rules = _get_funnel_rules_block(etapa_funil, primarios, secundarios)

    prompt = f"""
    Analise os seguintes parâmetros e forneça uma recomendação estratégica:

    **Campanha:** {params['objetivo_campanha']} (Etapa do Funil: {etapa_funil})
    **Tipo de Campanha:** {params['tipo_campanha']}
    **Budget Total:** R$ {params['budget']:,.2f}
    **Período da Campanha:** {params['periodo']}
    **Ferramentas/Plataformas:** {", ".join(params['ferramentas'])}
    **Localização Primária:** {params['localizacao_primaria']}
    **Localização Secundária:** {params['localizacao_secundaria']}
    **Tipo de Público:** {params['tipo_publico']}
    **Tipos de Criativo:** {", ".join(params['tipo_criativo'])}
    **KPIs Primários (foco):** {", ".join(primarios) if primarios else "A serem definidos"}
    **KPIs Secundários (monitoramento):** {", ".join(secundarios) if secundarios else "Nenhum selecionado"}
    **Metas Específicas:** {", ".join(metas_especificas) if metas_especificas else "Nenhuma meta específica"}
    **Detalhes da Ação:** {params['detalhes_acao'] or "Nenhum"}
    **Observações:** {params['observacoes'] or "Nenhuma"}
    {funnel_rules}
    {funnel_context}
    {kpi_defs_block}
    {benchmark_block}

    Forneça OBRIGATORIAMENTE todas as seções abaixo:

    ## Análise Estratégica
    Análise focada em "{etapa_funil}" do funil (200-300 palavras). Deve:
    - Referenciar explicitamente o framework teórico aplicável (ex: "Segundo Binet & Field..." / "Conforme modelo STDC de Kaushik...")
    - Justificar por que os KPIs primários escolhidos são os corretos para esta etapa
    - Conectar a estratégia criativa ao objetivo da etapa (ex: awareness = emocional/broad reach; conversão = racional/targeted)

    ## Oportunidades para KPIs Primários
    Para CADA KPI primário selecionado:
    - Como maximizá-lo dado o budget, plataformas e período
    - Benchmark esperado no mercado brasileiro
    - Alavancas específicas de otimização

    ## Riscos e Anti-padrões
    Riscos ESPECÍFICOS para a etapa "{etapa_funil}" (use os erros comuns do contexto acima):
    - Erros de mensuração (medir com métricas erradas)
    - Erros de targeting (audiência inadequada para a etapa)
    - Erros de criativo (mensagem desalinhada com o momento do funil)

    ## ⚠️ Métricas que NÃO indicam sucesso nesta etapa
    Liste 2-3 métricas que podem parecer importantes mas são INADEQUADAS
    para avaliar sucesso em "{etapa_funil}", explicando por quê.

    ## Recomendação Geral
    Abordagem macro alinhada ao contexto da etapa (80-120 palavras).

    REGRAS ADICIONAIS:
    - Foco absoluto nos KPIs primários: {", ".join(primarios) if primarios else "gerar sugestões apropriadas"}
    - Monitore secundários: {", ".join(secundarios) if secundarios else "gerar sugestões"}
    - Use os benchmarks brasileiros como base para estimativas realistas
    - Use as definições e fórmulas dos KPIs para orientar a análise
    - Considere as metas específicas quando fornecidas
    - Adapte ao período especificado

    Formato: Markdown com headers (##, ###)
    """
    response = modelos["estrategista"].generate_content(prompt)
    return response.text


def gerar_distribuicao_budget(modelos, params: Dict[str, Any], recomendacao_estrategica: str) -> str:
    """Gera a distribuicao de budget. Usa o modelo Controller Financeiro."""
    etapa_funil = params['etapa_funil']
    okrs_escolhidos, metas_especificas, primarios, secundarios = _extract_okrs(params)
    benchmark_block = _get_benchmark_block(params)
    templates_block = _get_templates_block(params)
    kpi_defs_block = _get_kpi_definitions_block(params)
    funnel_context = _get_funnel_stage_context(params)
    funnel_rules = _get_funnel_rules_block(etapa_funil, primarios, secundarios)

    prompt = f"""
    Com base na seguinte recomendação estratégica (Etapa {etapa_funil} do Funil):
    {recomendacao_estrategica}

    E nos parâmetros originais:
    - Budget: R$ {params['budget']:,.2f}
    - Período: {params['periodo']}
    - Plataformas: {", ".join(params['ferramentas'])}
    - Localizações: Primária ({params['localizacao_primaria']}), Secundária ({params['localizacao_secundaria']})
    - Tipos de Criativo: {", ".join(params['tipo_criativo'])}
    - KPIs Primários: {", ".join(primarios) if primarios else "A serem otimizados"}
    - KPIs Secundários: {", ".join(secundarios) if secundarios else "Nenhum"}
    - Metas: {", ".join(metas_especificas) if metas_especificas else "Nenhuma específica"}
    {funnel_rules}
    {funnel_context}
    {kpi_defs_block}
    {benchmark_block}
    {templates_block}

    Crie uma distribuição de budget OTIMIZADA PARA A ETAPA "{etapa_funil}" com as seções:

    ## Tabela de Alocação por Plataforma
    | Plataforma | % do Budget | Valor (R$) | Objetivo na Etapa | KPI Alvo |
    Para cada plataforma, justificar a alocação em função da etapa do funil:
    - Em Awareness: priorizar plataformas com menor CPM e maior alcance
    - Em Interesse: priorizar plataformas com melhor CPC e engajamento
    - Em Consideração: priorizar plataformas com remarketing eficiente e CTR alto
    - Em Intenção: priorizar plataformas com melhor CPL e conversão de leads
    - Em Conversão: priorizar plataformas com melhor CPA/ROAS
    - Em Retenção: priorizar canais de CRM, remarketing de base, email

    ## Alocação Geográfica
    Distribuição entre localização primária e secundária com justificativa.

    ## Alocação por Tipo de Criativo
    APENAS os tipos: {", ".join(params['tipo_criativo'])}
    Para cada tipo, explicar por que é adequado para a etapa "{etapa_funil}":
    - Awareness: vídeo curto emocional, carrosséis de marca, formatos de alto impacto
    - Interesse: conteúdo educativo, tutoriais, carrosséis informativos
    - Consideração: demos, depoimentos, comparativos, casos de sucesso
    - Conversão: ofertas diretas, urgência, prova social, CTA claro

    ## Justificativa Estratégica
    Análise de 80-120 palavras conectando:
    - Como a distribuição maximiza os KPIs PRIMÁRIOS da etapa
    - Referência ao framework teórico (Binet & Field para split brand/activation)
    - Por que essa distribuição é ESPECÍFICA para "{etapa_funil}" e seria diferente em outra etapa

    REGRAS:
    - Use os benchmarks brasileiros para estimar volumes realistas
    - Use os templates de alocação como referência para a distribuição por etapa
    - Priorize os KPIs primários: {", ".join(primarios) if primarios else "otimize para a etapa do funil"}
    - Não sugerir criativos fora dos tipos especificados
    - Manter foco absoluto nos estados solicitados
    - Para CADA linha da tabela, indicar qual KPI primário aquela alocação visa maximizar

    Formato: Markdown com tabelas (use | para divisão)
    """
    response = modelos["financeiro"].generate_content(prompt)
    return response.text


def gerar_previsao_resultados(modelos, params: Dict[str, Any], recomendacao_estrategica: str, distribuicao_budget: str) -> str:
    """Gera previsao de resultados. Usa o modelo Analista de Performance."""
    etapa_funil = params['etapa_funil']
    okrs_escolhidos, metas_especificas, primarios, secundarios = _extract_okrs(params)
    benchmark_block = _get_benchmark_block(params)
    kpi_defs_block = _get_kpi_definitions_block(params)
    funnel_context = _get_funnel_stage_context(params)
    funnel_rules = _get_funnel_rules_block(etapa_funil, primarios, secundarios)

    prompt = f"""
    Com base na estratégia para "{etapa_funil}" do funil:
    {recomendacao_estrategica}

    E na distribuição de budget:
    {distribuicao_budget}

    Parâmetros:
    - Budget total: R$ {params['budget']:,.2f}
    - Período: {params['periodo']}
    - KPIs Primários: {", ".join(primarios) if primarios else "A serem otimizados"}
    - KPIs Secundários: {", ".join(secundarios) if secundarios else "Nenhum"}
    - Metas: {", ".join(metas_especificas) if metas_especificas else "Nenhuma específica"}
    {funnel_rules}
    {funnel_context}
    {kpi_defs_block}
    {benchmark_block}

    Gere a projeção de resultados com as seguintes seções OBRIGATÓRIAS:

    ## 1. KPIs Primários — Projeção Detalhada (FOCO PRINCIPAL)
    Tabela com os KPIs PRIMÁRIOS desta etapa ("{etapa_funil}") em 3 cenários:

    | KPI (Primário) | Fórmula | Cenário Pessimista | Cenário Realista | Cenário Otimista |

    Para CADA KPI primário, mostrar:
    - A fórmula utilizada no cálculo
    - O benchmark de referência usado (fonte: mercado brasileiro)
    - O cálculo explícito (ex: "R$70.000 / R$15 CPM × 1000 = 4.666.667 impressões")
    ESTES são os indicadores de sucesso da campanha. Devem receber 60%+ do espaço da análise.

    ## 2. KPIs Secundários — Monitoramento
    Tabela mais concisa com KPIs secundários:

    | KPI (Secundário) | Fórmula | Projeção Realista | Papel nesta etapa |

    Explicar para cada um: "Este KPI serve para [diagnóstico/otimização], não para julgar sucesso."

    ## 3. Métricas de Referência (NÃO são indicadores de sucesso)
    Para métricas terciárias ou de outras etapas que podem aparecer nos dashboards:

    | Métrica | Projeção Estimada | ⚠️ Por que NÃO medir sucesso por ela |

    Exemplo para Awareness: CPA, CPC, CTR → "Métricas de fundo de funil. Usar como referência
    de baseline apenas. Julgar awareness por CPA é o erro #1 em mídia digital (Kaushik, Binet & Field)."

    Exemplo para Conversão: Impressões, Alcance → "Métricas de topo de funil. Em conversão,
    o volume de impressões é irrelevante se não gera transações."

    ## 4. Estimativas Detalhadas por Plataforma
    Para cada plataforma, calcular volumes usando benchmarks:
    - Budget alocado → benchmark → volume projetado
    - Mostrar cálculo: "R$X / CPM R$Y × 1000 = Z impressões"

    ## 5. Análise de Potencial Desempenho
    100-150 palavras conectando:
    - Quais KPIs primários têm maior potencial de entrega
    - Quais riscos podem comprometer a projeção
    - O que monitorar nos primeiros dias para validar as premissas
    - Referência ao framework teórico: por que ESSES KPIs são os corretos para "{etapa_funil}"

    ## 6. Dashboard de Monitoramento Recomendado
    Organizar os KPIs por prioridade de acompanhamento:
    - 🔴 CRÍTICOS (primários): verificar DIARIAMENTE
    - 🟡 IMPORTANTES (secundários): verificar SEMANALMENTE
    - ⚪ REFERÊNCIA (terciários): verificar apenas em revisões quinzenais

    REGRAS DE CÁLCULO:
    - Use OBRIGATORIAMENTE os benchmarks brasileiros fornecidos
    - Use as fórmulas dos KPIs listadas acima para calcular projeções
    - Calcule: Budget / CPM × 1000 = impressões; Budget / CPC = cliques; etc.
    - Considere as metas específicas quando fornecidas
    - NUNCA coloque KPIs de outra etapa na tabela principal sem o aviso de referência

    Formato: Markdown com tabelas
    """
    response = modelos["performance"].generate_content(prompt)
    return response.text


def gerar_recomendacoes_publico(modelos, params: Dict[str, Any], recomendacao_estrategica: str) -> str:
    """Gera recomendacoes de publico-alvo. Usa o modelo Especialista de Audiência."""
    etapa_funil = params['etapa_funil']
    okrs_escolhidos, _, primarios, secundarios = _extract_okrs(params)
    benchmark_block = _get_benchmark_block(params)
    kpi_defs_block = _get_kpi_definitions_block(params)
    funnel_context = _get_funnel_stage_context(params)
    funnel_rules = _get_funnel_rules_block(etapa_funil, primarios, secundarios)

    prompt = f"""
    Para a campanha na etapa "{etapa_funil}" do funil com:
    - Tipo de Público: {params['tipo_publico']}
    - Objetivo: {params['objetivo_campanha']}
    - Plataformas: {", ".join(params['ferramentas'])}
    - Localizações: {params['localizacao_primaria']} (primária), {params['localizacao_secundaria']} (secundária)
    - KPIs Primários: {", ".join(primarios) if primarios else "A serem otimizados"}
    - KPIs Secundários: {", ".join(secundarios) if secundarios else "Nenhum"}
    {funnel_rules}
    {funnel_context}
    {kpi_defs_block}
    {benchmark_block}
    E considerando a estratégia geral:
    {recomendacao_estrategica}

    Desenvolva recomendações de público OTIMIZADAS PARA A ETAPA "{etapa_funil}" com as seções:

    ## Lógica de Segmentação por Etapa do Funil
    Antes de detalhar os segmentos, explicar o PRINCÍPIO de targeting para "{etapa_funil}":
    - Awareness: targeting AMPLO (Byron Sharp). Alcançar o maior número de pessoas na categoria.
      Segmentação excessiva é um erro. Priorizar alcance sobre precisão.
    - Interesse: targeting por INTERESSES e comportamentos. Audiências que demonstram curiosidade
      na categoria mas sem intenção de compra. Lookalikes de engajadores.
    - Consideração: targeting QUALIFICADO. Remarketing de visitantes, engajadores profundos.
      Lookalikes de leads/clientes. Audiências in-market.
    - Intenção: targeting de ALTA INTENÇÃO. Remarketing de carrinho, visitantes de página de preço,
      leads quentes. Keywords de compra (search).
    - Conversão: targeting CIRÚRGICO. Remarketing dinâmico, listas de leads quentes, audiences de
      purchase intent. ROAS-optimized bidding.
    - Retenção: targeting de BASE. Listas de clientes, compradores recentes, segmentos de LTV.

    ## Segmentos Recomendados por Plataforma
    Para cada plataforma, detalhar:
    - Segmentos específicos adequados para "{etapa_funil}"
    - Parâmetros de targeting (interesses, comportamentos, demographics)
    - Tamanho estimado da audiência
    - CPM/CPC esperado para este segmento no Brasil

    ## Estratégia de Frequência e Saturação
    Adequar à etapa:
    - Awareness: frequência 1.5-3.0x semanal (evitar fadiga; priorizar alcance único)
    - Interesse: frequência 2-4x (reforço sem pressão)
    - Consideração: frequência 3-5x (repetição aceitável, audiência já engajada)
    - Conversão: frequência 4-8x (remarketing agressivo justificado pela intenção)
    - Retenção: frequência controlada (evitar irritar clientes existentes)

    ## Estratégias de Expansão
    Como ampliar audiência SEM perder alinhamento com a etapa do funil.

    ## Benchmarks de Performance por Segmento
    Tabela com CPM, CTR e performance esperada por segmento, referenciando dados do Brasil.

    REGRAS:
    - Manter foco absoluto nos estados especificados
    - A abordagem de targeting DEVE refletir a etapa "{etapa_funil}" — segmentação ampla para
      awareness, cirúrgica para conversão. Não usar abordagem genérica.
    - Justificar cada escolha de segmento em função do KPI primário que visa atingir
    - Usar benchmarks brasileiros para expectativas realistas

    Formato: Markdown com listas e headers
    """
    response = modelos["audiencia"].generate_content(prompt)
    return response.text


def gerar_cronograma(modelos, params: Dict[str, Any], recomendacao_estrategica: str, distribuicao_budget: str) -> str:
    """Gera cronograma de implementacao. Usa o modelo Gestor de Projetos."""
    etapa_funil = params['etapa_funil']
    okrs_escolhidos, _, primarios, secundarios = _extract_okrs(params)
    funnel_context = _get_funnel_stage_context(params)
    funnel_rules = _get_funnel_rules_block(etapa_funil, primarios, secundarios)

    prompt = f"""
    Com base na estratégia para "{etapa_funil}" do funil:
    {recomendacao_estrategica}

    E na distribuição de budget:
    {distribuicao_budget}
    {funnel_rules}
    {funnel_context}

    Crie um cronograma OTIMIZADO PARA A ETAPA "{etapa_funil}" com as seções:

    Parâmetros:
    - Budget total: R$ {params['budget']:,.2f}
    - Período: {params['periodo']}
    - Plataformas: {", ".join(params['ferramentas'])}
    - KPIs Primários: {", ".join(primarios) if primarios else "A serem otimizados"}
    - KPIs Secundários: {", ".join(secundarios) if secundarios else "Nenhum"}

    ## Visão Geral do Cronograma
    Resumo das fases com % de budget em cada uma.

    ## Fases Detalhadas
    Para CADA fase, incluir:
    - Período (dias/semanas)
    - Objetivo da fase
    - Budget alocado (R$ e %)
    - Tabela de atividades: | Dia/Semana | Atividade | Plataforma | Budget (R$) |
    - **KPIs de controle da fase**: quais KPIs PRIMÁRIOS monitorar e quais valores esperar
    - **Gatilhos de otimização**: condições específicas que exigem ajuste (ex: "Se CPM > R$25, rever segmentação")
    - **Gatilhos de alerta**: condições que indicam problema (ex: "Se frequência < 1.5 na semana 2, audiência muito ampla")

    ## Checkpoints de Performance
    Momentos-chave para avaliar a campanha contra os KPIs PRIMÁRIOS:
    - O que medir em cada checkpoint
    - Valores de referência esperados (benchmark)
    - Decisões possíveis: escalar, ajustar ou pivotar

    ## Pacing de Budget
    Como o investimento deve ser distribuído ao longo do tempo, adequado à etapa:
    - Awareness: investimento mais uniforme (always-on é melhor que bursts, conforme Byron Sharp)
    - Interesse/Consideração: pode usar front-loading para learning phase, depois otimização
    - Conversão: pode concentrar em períodos de maior intenção (ex: sazonalidade, paydays)
    - Retenção: distribuição contínua alinhada a ciclos de recompra

    ## Frequência de Ajustes
    - O que verificar diariamente, semanalmente, quinzenalmente
    - Baseado nos KPIs PRIMÁRIOS da etapa, não em métricas genéricas

    REGRAS:
    - As fases devem ser ESPECÍFICAS para "{etapa_funil}" — não usar cronograma genérico
    - Cada checkpoint deve avaliar KPIs PRIMÁRIOS, não terciários
    - Gatilhos devem referenciar benchmarks brasileiros reais
    - Manter realismo no período especificado: {params['periodo']}
    - Não incluir fases irrelevantes para a etapa do funil

    Formato: Markdown com tabelas e listas numeradas
    """
    response = modelos["gestor"].generate_content(prompt)
    return response.text
