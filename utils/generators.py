from typing import Dict, Any, List, Optional
import base64

from utils.constants.constants import BENCHMARKS_BR, TEMPLATES_ALOCACAO_BUDGET, KPIS_POR_ETAPA, PLATAFORMA_OBJETIVOS, get_enriched_funnel_context, CROSS_STAGE_PRINCIPLES, _get_funnel_metric_doctrine


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
    doctrine = _get_funnel_metric_doctrine(etapa_funil)
    return f"""
    ╔══════════════════════════════════════════════════════════════════════════╗
    ║  INSTRUÇÃO MÁXIMA: TODA ANÁLISE DEVE SER ANCORADA À ETAPA DO FUNIL    ║
    ║  Etapa atual: "{etapa_funil}"                                          ║
    ║  Esta instrução tem PRIORIDADE ABSOLUTA sobre qualquer outra.          ║
    ╚══════════════════════════════════════════════════════════════════════════╝

    {doctrine}

    === REGRAS CRÍTICAS DE ANÁLISE POR ETAPA DO FUNIL ===

    A etapa do funil é "{etapa_funil}". Isso determina TODA a lógica de análise.
    Cada parágrafo, tabela, recomendação e cálculo que você produzir DEVE explicitar
    por que é relevante para "{etapa_funil}" e não para outra etapa.

    1. HIERARQUIA DE MÉTRICAS (OBRIGATÓRIA):
       - KPIs PRIMÁRIOS desta etapa: {", ".join(primarios) if primarios else "os definidos para " + etapa_funil}
         → São o FOCO ABSOLUTO da análise. Toda recomendação DEVE ser orientada a maximizá-los.
         → SEMPRE que citar um KPI primário, JUSTIFIQUE por que ele é primário para "{etapa_funil}"
           com referência a pelo menos um framework teórico (Binet & Field, Byron Sharp, Kaushik, etc.)
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

    3. ANCORAGEM OBRIGATÓRIA AO FUNIL EM CADA SEÇÃO:
       - Em TODA seção do documento, iniciar com uma frase que conecte ao funil:
         "Para a etapa de {etapa_funil}, [análise]..."
         "Dado que estamos em {etapa_funil}, [recomendação]..."
       - Em toda tabela, incluir uma coluna ou nota que explique a relevância para a etapa.
       - Em toda recomendação, explicar por que seria DIFERENTE se a etapa fosse outra.

    4. ALERTAS DE MÉTRICAS DE VAIDADE:
       - Sempre que mencionar uma métrica que NÃO é primária para a etapa, classificá-la
         explicitamente como "métrica de referência" ou "métrica de vaidade para esta etapa".
       - Incluir uma seção "⚠️ Métricas que NÃO indicam sucesso nesta etapa" quando aplicável.
       - Usar a DOUTRINA DE MÉTRICAS acima como base para justificar o que medir e o que não medir.

    5. FUNDAMENTAÇÃO TEÓRICA OBRIGATÓRIA:
       - Toda recomendação estratégica DEVE citar pelo menos um framework teórico.
       - Use: Binet & Field (60/40, brand vs activation), Byron Sharp (How Brands Grow, Mental/Physical
         Availability), Kaushik STDC (See-Think-Do-Care), McKinsey CDJ (Consumer Decision Journey),
         Cialdini (princípios de persuasão), Kotler 5A, RACE, Forrester.
       - Não cite frameworks genericamente. Explique COMO o framework se aplica à decisão específica.
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

    ## Análise Estratégica da Etapa "{etapa_funil}"
    Análise focada em "{etapa_funil}" do funil (300-400 palavras). DEVE OBRIGATORIAMENTE:

    1. ABRIR com uma contextualização teórica da etapa (2-3 parágrafos):
       - O que significa estar em "{etapa_funil}" segundo os frameworks acadêmicos
       - Qual é o OBJETIVO CENTRAL desta etapa (ex: Awareness = plantar marca na memória de longo prazo;
         Conversão = capturar demanda gerada nas etapas anteriores)
       - Por que os KPIs primários escolhidos são os CORRETOS para esta etapa, citando Binet & Field,
         Byron Sharp, Kaushik STDC ou McKinsey CDJ (não genericamente, mas explicando a lógica)

    2. CONECTAR a estratégia ao momento do funil:
       - Awareness: criativo emocional, alcance amplo, frequência controlada, zero pressão de venda
       - Interesse: conteúdo educacional/entretenimento, CTAs suaves, métricas de engajamento qualitativo
       - Consideração: social proof, autoridade, comparação, remarketing de engajadores
       - Intenção: resposta direta, formulários curtos, urgência, leads qualificados
       - Conversão: CTA direto, landing pages focadas, remarketing agressivo, sinais de confiança
       - Retenção: personalização, CRM, exclusividade, canais próprios (email, WhatsApp)

    3. EXPLICAR por que esta estratégia seria DIFERENTE se a etapa fosse outra (1 parágrafo):
       Exemplo: "Se esta campanha fosse de Conversão ao invés de Awareness, priorizaríamos CPA e ROAS
       ao invés de Alcance e CPM, e o criativo seria racional com CTA direto ao invés de emocional."

    ## Cruzamento de Métricas e Insights Estratégicos
    Esta seção é CRÍTICA. Cruze os KPIs selecionados entre si e com os benchmarks para gerar insights acionáveis.
    Para cada combinação relevante, mostre:

    **Relações entre métricas (exemplos obrigatórios se as métricas estiverem selecionadas):**
    - CPM x Impressões: "Com budget de R$X e CPM médio de R$Y na plataforma Z, projetamos ~N impressões. Se o CPM subir para R$W (cenário pessimista), as impressões caem para ~M."
    - CPM x Alcance x Frequência: "Com ~N impressões e frequência-alvo de F, estimamos alcance de ~A pessoas únicas."
    - CPC x Cliques x Budget: "Com budget de R$X e CPC médio de R$Y, estimamos ~N cliques. Para atingir meta de M cliques, precisaríamos de R$Z."
    - CTR x Impressões x Cliques: "Se CTR for T% sobre N impressões, geramos ~C cliques. Cada ponto percentual de melhoria no CTR equivale a +D cliques adicionais."
    - CPA x Conversões x Budget: "Com CPA-alvo de R$X e budget de R$Y, projetamos ~N conversões."
    - ROAS x Ticket Médio x Conversões: "Para ROAS de Xx com budget de R$Y, precisamos de R$Z em receita, ou seja, ~N conversões com ticket médio de R$W."

    **Tabela de Cruzamento:**
    | Métrica A | Métrica B | Relação | Cálculo com dados da campanha | Insight |
    (Preencha com pelo menos 4 cruzamentos usando os KPIs selecionados e benchmarks reais)

    **Análise de sensibilidade:**
    - O que acontece se o CPM/CPC variar 20% para cima ou para baixo?
    - Qual é o impacto de uma melhoria de 0.5% no CTR sobre o volume final?
    - Qual é o "break-even" de cada métrica para atingir as metas definidas?

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

    ## Métricas que NÃO indicam sucesso nesta etapa
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
    - Na seção de cruzamento, SEMPRE faça cálculos reais com os números da campanha (budget, período, benchmarks)
    - Adapte ao período especificado

    REGRA INVIOLÁVEL DE ANCORAGEM AO FUNIL:
    - Em CADA seção, CADA parágrafo deve ter pelo menos uma menção explícita à etapa "{etapa_funil}"
    - NUNCA produza uma recomendação genérica que funcionaria para qualquer etapa
    - SEMPRE explique por que a recomendação é ESPECÍFICA para "{etapa_funil}"
    - Se citar uma métrica que não é primária para esta etapa, OBRIGATORIAMENTE adicionar:
      "⚠️ Esta métrica não é indicador de sucesso em {etapa_funil} — usar apenas como referência."
    - Usar os frameworks teóricos (Binet & Field, Byron Sharp, Kaushik STDC) para JUSTIFICAR
      cada decisão, não apenas como decoração. O leitor deve entender a LÓGICA por trás da escolha.

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

    ## Lógica de Alocação para "{etapa_funil}" (Fundamentação)
    Abrir com 2 parágrafos explicando:
    - Por que a alocação de budget para "{etapa_funil}" é DIFERENTE de outras etapas
    - Qual framework teórico orienta esta distribuição (Binet & Field 60/40, Fospha, etc.)
    - Se estamos em Awareness: explicar por que plataformas de maior alcance e menor CPM recebem mais
    - Se estamos em Conversão: explicar por que plataformas de maior taxa de conversão recebem mais
    - Quanto do budget total do funil esta etapa deveria receber e por quê

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

    ## 0. Por que ESTES KPIs para "{etapa_funil}" (Fundamentação Teórica)
    Antes de qualquer tabela, abrir com 2-3 parágrafos que JUSTIFIQUEM conceitualmente:
    - Por que os KPIs primários escolhidos são os corretos para a etapa "{etapa_funil}" do funil
    - Qual framework teórico sustenta esta escolha (Binet & Field, Byron Sharp, Kaushik, McKinsey)
    - Quais métricas seriam ERRADAS para avaliar sucesso nesta etapa e por quê
    - Exemplo para Awareness: "Segundo Kaushik (modelo STDC), a audiência 'See' não tem intenção
      comercial. Medir CPA ou ROAS é conceitualmente inadequado porque estamos medindo conversão
      em uma audiência que ainda não está pronta para converter. Binet & Field demonstram que
      efeitos de construção de marca levam 6+ meses para se materializar em vendas..."
    - Exemplo para Conversão: "Na etapa de Ação do AIDA, a audiência já foi qualificada pelo
      funil inteiro. Aqui, métricas de exposição (alcance, impressões) são irrelevantes — o
      que importa é a taxa de conversão e o custo por aquisição..."

    ## 1. KPIs Primários — Projeção Detalhada (FOCO PRINCIPAL)
    Tabela com os KPIs PRIMÁRIOS desta etapa ("{etapa_funil}") em 3 cenários:

    | KPI (Primário) | Por que é primário em {etapa_funil} | Fórmula | Cenário Pessimista | Cenário Realista | Cenário Otimista |

    Para CADA KPI primário, mostrar:
    - Por que este KPI é PRIMÁRIO para "{etapa_funil}" (1-2 frases com referência teórica)
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

    ## 4. Cruzamento Integrado de Métricas
    SEÇÃO CRÍTICA: Cruze TODAS as métricas projetadas entre si para gerar insights compostos.

    **Cadeia de métricas (mostrar o fluxo completo):**
    Budget → CPM → Impressões → Frequência → Alcance Único → CTR → Cliques → CPC efetivo → Taxa de Conversão → Conversões → CPA efetivo → Receita → ROAS

    Para cada elo da cadeia que envolva KPIs selecionados, mostre:
    - O cálculo explícito com números da campanha
    - Como a variação de um elo impacta toda a cadeia posterior
    - Exemplo: "Se o CPM subir de R$15 para R$20 (+33%), as impressões caem 25%, o que reduz o alcance proporcional e, consequentemente, os cliques esperados caem de X para Y."

    **Tabela de Interdependência:**
    | Se esta métrica variar | Impacto em | Magnitude | Ação recomendada |
    (Mínimo 5 linhas com cenários realistas)

    **Pontos de alavancagem:**
    Identifique quais 2-3 métricas, se otimizadas, geram o maior efeito cascata positivo sobre os KPIs primários.

    ## 5. Estimativas Detalhadas por Plataforma
    Para cada plataforma, calcular volumes usando benchmarks:
    - Budget alocado → benchmark → volume projetado
    - Mostrar cálculo: "R$X / CPM R$Y × 1000 = Z impressões"
    - Cruzar com outras métricas: "Dessas Z impressões, com CTR de T%, esperamos C cliques a CPC efetivo de R$W"

    ## 6. Análise de Potencial Desempenho
    100-150 palavras conectando:
    - Quais KPIs primários têm maior potencial de entrega
    - Quais riscos podem comprometer a projeção
    - O que monitorar nos primeiros dias para validar as premissas
    - Referência ao framework teórico: por que ESSES KPIs são os corretos para "{etapa_funil}"

    ## 7. Dashboard de Monitoramento Recomendado
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

    ## Por que o Targeting Muda por Etapa do Funil (Fundamentação)
    Abrir com 2-3 parágrafos conceituais explicando:
    - Segundo Byron Sharp, marcas crescem alcançando light buyers e non-buyers — o que isso
      significa para o targeting em "{etapa_funil}"?
    - Como o modelo STDC de Kaushik define a audiência desta etapa (See/Think/Do/Care)?
    - Qual é o ERRO mais comum de targeting nesta etapa e por que ele ocorre?
    - Exemplo: em Awareness, o erro é segmentar demais (alcançar apenas heavy buyers),
      enquanto em Conversão, o erro é segmentar pouco (gastar em audiências frias).

    ## Lógica de Segmentação por Etapa do Funil
    Detalhar o PRINCÍPIO de targeting para "{etapa_funil}":
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

    ## Princípios Temporais para "{etapa_funil}" (Fundamentação)
    Abrir com 2 parágrafos explicando como o TEMPO funciona diferente em cada etapa do funil:
    - Awareness: Byron Sharp argumenta que "always-on" contínuo é superior a bursts. Binet & Field
      mostram que efeitos de marca levam 6+ meses para se materializar. Implicação: campanhas de
      awareness precisam de constância, não de picos de investimento.
    - Interesse: learning phase das plataformas exige tempo de otimização. Front-loading é comum
      seguido de otimização progressiva.
    - Consideração: nurturing é um processo — não se pode apressar avaliação. Sequências de
      retargeting devem ter espaçamento adequado.
    - Intenção: tempo de resposta é CRÍTICO — leads contatados em 5 min convertem 9x mais.
    - Conversão: concentrar budget em períodos de alta intenção (sazonalidade, paydays).
    - Retenção: alinhamento com ciclos de recompra e lifetime do cliente.
    Explicar qual destes princípios se aplica à campanha atual em "{etapa_funil}".

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


def gerar_analise_criativo(modelos, params: Dict[str, Any], imagens: List[Any]) -> str:
    """Analisa criativos (imagens) enviados pelo usuário e cruza com os OKRs/metas da campanha."""
    etapa_funil = params['etapa_funil']
    okrs_escolhidos, metas_especificas, primarios, secundarios = _extract_okrs(params)
    funnel_rules = _get_funnel_rules_block(etapa_funil, primarios, secundarios)
    funnel_context = _get_funnel_stage_context(params)
    kpi_defs_block = _get_kpi_definitions_block(params)

    prompt_text = f"""
    Você é um Diretor de Criação e Estratégia de Mídia Digital com 15+ anos de experiência
    no mercado brasileiro. Analise os criativos (imagens) enviados e avalie o alinhamento
    com as metas e OKRs da campanha.

    **Contexto da Campanha:**
    - Objetivo: {params['objetivo_campanha']}
    - Tipo de Campanha: {params['tipo_campanha']}
    - Etapa do Funil: {etapa_funil}
    - Plataformas: {", ".join(params['ferramentas'])}
    - Público-Alvo: {params['tipo_publico']}
    - Tipos de Criativo Planejados: {", ".join(params['tipo_criativo'])}
    - KPIs Primários: {", ".join(primarios) if primarios else "A serem definidos"}
    - KPIs Secundários: {", ".join(secundarios) if secundarios else "Nenhum"}
    - Metas Específicas: {", ".join(metas_especificas) if metas_especificas else "Nenhuma meta específica"}
    - Detalhes da Ação: {params['detalhes_acao'] or "Nenhum"}
    {funnel_rules}
    {funnel_context}
    {kpi_defs_block}

    ## Fundamentação: O que a Etapa "{etapa_funil}" Exige dos Criativos
    ANTES de analisar as imagens, abra com 2-3 parágrafos explicando:
    - Segundo Binet & Field, qual é o papel do criativo em "{etapa_funil}"?
      (Awareness = emocional, brand building, ativos distintivos | Conversão = racional, CTA direto, urgência)
    - Segundo Byron Sharp, quais ativos distintivos (distinctive assets) o criativo DEVE ter em "{etapa_funil}"?
    - Quais princípios de Cialdini são mais relevantes para criativos nesta etapa?
    - O que um criativo ERRADO para esta etapa parece? (ex: CTA agressivo em awareness = erro conceitual)

    Para CADA criativo enviado, forneça OBRIGATORIAMENTE:

    ## Análise Individual do Criativo [número]

    ### Descrição Visual
    Descreva detalhadamente o que você vê na imagem: elementos visuais, cores, texto,
    composição, hierarquia visual, call-to-action (se houver).

    ### Alinhamento com a Etapa do Funil ({etapa_funil}) — Nota: X/10
    Avalie de 1 a 10 o alinhamento do criativo com a etapa do funil.
    A justificativa DEVE ser fundamentada nos frameworks teóricos:

    - **Binet & Field**: O criativo está alinhado com construção de marca (emocional, amplo) ou
      ativação (racional, targeted)? A etapa "{etapa_funil}" pede qual abordagem?
    - **Byron Sharp**: O criativo usa ativos distintivos da marca (cores, logo, personagens)?
      Em "{etapa_funil}", qual é o papel dos distinctive assets?
    - **Cialdini**: Quais princípios de persuasão o criativo emprega? São os corretos para
      "{etapa_funil}" ou seriam mais adequados para outra etapa?
    - **Kaushik STDC**: A mensagem está adequada para a audiência desta etapa
      (See = sem intenção | Think = curiosa | Do = pronta para agir | Care = cliente existente)?

    ### Alinhamento com os OKRs e Metas
    Para cada KPI primário selecionado, avalie se o criativo contribui para atingi-lo:
    - O criativo favorece a maximização de {", ".join(primarios) if primarios else "KPIs primários"}?
    - Existe algum elemento que PREJUDICA o desempenho dos KPIs?
    - Estimativa qualitativa de impacto: alto / médio / baixo
    - **Se o criativo favorece KPIs de OUTRA etapa ao invés dos primários desta**, apontar explicitamente:
      "⚠️ Este criativo parece otimizado para [outra etapa], não para {etapa_funil}."

    ### Pontos Fortes
    Liste os elementos visuais e de comunicação que estão bem executados
    PARA A ETAPA "{etapa_funil}" especificamente.

    ### Pontos de Melhoria
    Liste ajustes necessários com sugestões específicas e acionáveis:
    - O que mudar no texto/copy para melhor se adequar a "{etapa_funil}"?
    - O que mudar nos elementos visuais?
    - O que mudar na composição/layout?
    - O que mudar no CTA? (CTA agressivo em awareness = ruim; CTA suave em conversão = ruim)
    - Qual princípio de Cialdini poderia ser adicionado ou reforçado?

    ### Veredicto
    O criativo está ALINHADO / PARCIALMENTE ALINHADO / DESALINHADO com a etapa "{etapa_funil}"?
    Justifique em 2-3 frases com referência teórica.

    ---

    Após analisar todos os criativos, forneça:

    ## Análise Comparativa
    Se mais de um criativo foi enviado, compare-os:
    - Qual é mais adequado para a etapa "{etapa_funil}" e por quê (com referência teórica)?
    - Qual tem maior potencial de performance nos KPIs primários?
    - Sugestão de hierarquia para teste A/B

    ## ⚠️ Alertas de Desalinhamento com o Funil
    Se algum criativo está otimizado para uma etapa DIFERENTE de "{etapa_funil}", detalhar:
    - Para qual etapa o criativo parece ter sido feito
    - O que precisaria mudar para realinhá-lo com "{etapa_funil}"
    - Exemplo: "Este criativo tem CTA de compra direta, mais adequado para Conversão.
      Para {etapa_funil}, recomendamos substituir por [sugestão]."

    ## Recomendações Gerais para os Criativos
    - Padrões positivos e negativos observados
    - Coerência visual entre os criativos (se múltiplos)
    - Adequação ao público-alvo e plataformas selecionadas
    - Sugestões de variações para teste
    - Princípios de Cialdini adicionais que poderiam ser incorporados

    Formato: Markdown com headers (##, ###). Responda INTEGRALMENTE em português brasileiro.
    """

    content_parts = [prompt_text]
    for img_data in imagens:
        content_parts.append(img_data)

    response = modelos["estrategista"].generate_content(content_parts)
    return response.text
