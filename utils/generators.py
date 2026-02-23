from typing import Dict, Any

from utils.constants.constants import BENCHMARKS_BR, TEMPLATES_ALOCACAO_BUDGET, KPIS_POR_ETAPA, PLATAFORMA_OBJETIVOS


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


_FUNNEL_STAGE_CONTEXT = {
    "Consciência (Awareness)": {
        "objetivo": "Maximizar exposição e alcance da marca junto ao público-alvo",
        "abordagem": (
            "Formatos de alto impacto visual (vídeo, carrossel). Frequência controlada entre 1.5-3x. "
            "Segmentação ampla por interesses e demográficos. Priorizar plataformas de alcance massivo "
            "(Meta, YouTube, TikTok). Otimizar para impressões e CPM baixo."
        ),
        "plataformas_ideais": "Meta Ads, YouTube, TikTok, Mídia Programática",
        "metricas_foco": "Alcance, Impressões, CPM, Frequência",
        "erros_comuns": "Frequência excessiva (>4x), segmentação muito restrita, foco prematuro em conversão",
    },
    "Interesse": {
        "objetivo": "Gerar cliques, engajamento e tráfego qualificado ao conteúdo da marca",
        "abordagem": (
            "Conteúdo educativo e demonstrativo. CTAs para landing pages. Vídeos curtos e carrosseis informativos. "
            "Segmentação por interesses específicos e lookalike de engajadores. "
            "Otimizar para cliques e CTR, monitorando qualidade do tráfego (tempo no site, bounce rate)."
        ),
        "plataformas_ideais": "Meta Ads, Google Ads (Display/Discovery), TikTok",
        "metricas_foco": "CTR, Cliques, CPC, Taxa de Engajamento",
        "erros_comuns": "Tráfego sem qualificação, landing pages desalinhadas, CPC alto por segmentação genérica",
    },
    "Consideração": {
        "objetivo": "Aprofundar avaliação do produto/serviço e nutrir o interesse do prospect",
        "abordagem": (
            "Conteúdo comparativo, depoimentos, demonstrações de produto. Remarketing de engajadores. "
            "Formatos mais longos (vídeo, carrossel detalhado). Segmentação por comportamento e visitas anteriores. "
            "Otimizar para engajamento qualificado e micro-conversões."
        ),
        "plataformas_ideais": "Meta Ads, Google Ads (Search/YouTube), LinkedIn (B2B)",
        "metricas_foco": "CTR, CPC, Taxa de Engajamento, ThruPlay",
        "erros_comuns": "Pular direto para conversão, não ter conteúdo intermediário, ignorar remarketing",
    },
    "Intenção": {
        "objetivo": "Capturar leads qualificados e sinalizar intenção de compra/ação",
        "abordagem": (
            "Formulários de lead, ofertas diretas, trial/demo. Remarketing agressivo de visitantes do site. "
            "Segmentação por intenção (search keywords, visitantes de páginas-chave). "
            "Otimizar para CPL e taxa de conversão de lead. Landing pages com formulários curtos."
        ),
        "plataformas_ideais": "Google Ads (Search), Meta Ads (Lead Ads), LinkedIn (Lead Gen Forms)",
        "metricas_foco": "Leads Gerados, CPL, Taxa de Conversão de Lead, CPC",
        "erros_comuns": "Formulários longos demais, falta de follow-up rápido, CPL sem qualificação",
    },
    "Conversão/Ação": {
        "objetivo": "Converter prospects em clientes pagantes com máximo ROAS",
        "abordagem": (
            "Ofertas urgentes, provas sociais, remarketing de carrinho abandonado. "
            "Segmentação estreita: remarketing de visitantes quentes, lookalike de compradores. "
            "Otimizar para CPA e ROAS. Formatos com CTA direto (comprar, assinar, agendar). "
            "Frequência alta aceitável (4-8x) para audiências quentes."
        ),
        "plataformas_ideais": "Google Ads (Search/Shopping), Meta Ads (Conversão), Mídia Programática (Retargeting)",
        "metricas_foco": "Conversões, CPA, ROAS, Taxa de Conversão",
        "erros_comuns": "Budget em audiência fria, criativo genérico, não testar variações de oferta",
    },
    "Retenção/Fidelização": {
        "objetivo": "Manter clientes ativos, estimular recompra e aumentar LTV",
        "abordagem": (
            "Campanhas de CRM, email marketing, remarketing de clientes existentes. "
            "Programas de fidelidade, ofertas exclusivas, cross-sell/upsell. "
            "Segmentação por histórico de compra e engajamento com a marca. "
            "ROAS tende a ser muito mais alto (4-10x) pois audiência já é qualificada."
        ),
        "plataformas_ideais": "Meta Ads (Custom Audiences), Google Ads (Remarketing), Email Marketing",
        "metricas_foco": "Taxa de Retenção, LTV, Taxa de Recompra, ROAS",
        "erros_comuns": "Ignorar base existente, tratar cliente igual prospect, não segmentar por recência",
    },
}


def _get_funnel_stage_context(params: Dict[str, Any]) -> str:
    """Injeta contexto estratégico da etapa do funil selecionada."""
    etapa = params.get('etapa_funil', '')
    ctx = _FUNNEL_STAGE_CONTEXT.get(etapa)
    if not ctx:
        return ""

    bloco = f"""
    **Contexto Estratégico da Etapa "{etapa}":**
    - Objetivo principal: {ctx['objetivo']}
    - Abordagem recomendada: {ctx['abordagem']}
    - Plataformas ideais para esta etapa: {ctx['plataformas_ideais']}
    - Métricas de foco: {ctx['metricas_foco']}
    - Erros comuns a evitar: {ctx['erros_comuns']}
"""
    return bloco


def gerar_recomendacao_estrategica(modelos, params: Dict[str, Any]) -> str:
    etapa_funil = params['etapa_funil']
    okrs_escolhidos, metas_especificas, primarios, secundarios = _extract_okrs(params)
    benchmark_block = _get_benchmark_block(params)
    kpi_defs_block = _get_kpi_definitions_block(params)
    funnel_context = _get_funnel_stage_context(params)

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
    {funnel_context}
    {kpi_defs_block}
    {benchmark_block}
    Forneça:
    1. Análise estratégica focada em {etapa_funil} do funil (150-200 palavras)
    2. Principais oportunidades para os KPIs primários selecionados
    3. Riscos potenciais específicos para esta etapa (considere os erros comuns listados acima)
    4. Recomendação geral de abordagem alinhada ao contexto da etapa

    Dicas:
    - Foco absoluto nos KPIs primários: {", ".join(primarios) if primarios else "gerar sugestões apropriadas"}
    - Monitore secundários: {", ".join(secundarios) if secundarios else "gerar sugestões"}
    - Use os benchmarks brasileiros como base para estimativas realistas
    - Use as definições e fórmulas dos KPIs para orientar a análise
    - Considere a abordagem recomendada para a etapa do funil
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
    {funnel_context}
    {kpi_defs_block}
    {benchmark_block}
    {templates_block}
    Crie uma tabela detalhada de distribuição de budget OTIMIZADA PARA OS KPIs SELECIONADOS com:
    1. Divisão por plataforma (% e valor)
    2. Alocação geográfica (primária vs secundária)
    3. Tipos de criativos recomendados (APENAS: {", ".join(params['tipo_criativo'])})
    4. Justificativa estratégica para cada alocação

    REGRAS:
    - Use os benchmarks brasileiros para estimar volumes realistas (impressões, cliques, etc.)
    - Use os templates de alocação como referência para a distribuição por etapa
    - Priorize os KPIs primários: {", ".join(primarios) if primarios else "otimize para a etapa do funil"}
    - Considere as metas específicas quando fornecidas
    - Não sugerir criativos fora dos tipos especificados
    - Manter foco absoluto nos estados solicitados

    Inclua também uma breve análise (50-100 palavras) explicando como a distribuição atende aos objetivos.

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

    prompt = f"""
    Com base na estratégia para {etapa_funil} do funil:
    {recomendacao_estrategica}

    E na distribuição de budget:
    {distribuicao_budget}

    Estime os resultados ESPERADOS considerando:
    - Budget total: R$ {params['budget']:,.2f}
    - Período: {params['periodo']}
    - KPIs Primários: {", ".join(primarios) if primarios else "A serem otimizados"}
    - KPIs Secundários: {", ".join(secundarios) if secundarios else "Nenhum"}
    - Metas: {", ".join(metas_especificas) if metas_especificas else "Nenhuma específica"}
    {funnel_context}
    {kpi_defs_block}
    {benchmark_block}
    Forneça:
    1. Tabela com métricas ESPECÍFICAS para os KPIs selecionados com 3 cenários:
       - **Pessimista**: Usando benchmark mínimo das plataformas
       - **Realista**: Usando benchmark médio
       - **Otimista**: Usando benchmark máximo
    2. Estimativas realistas baseadas nos benchmarks brasileiros fornecidos
    3. Análise de potencial desempenho (50-100 palavras)
    4. KPIs CHAVE para monitorar (primários em destaque, secundários como suporte)

    DICAS:
    - Use OBRIGATORIAMENTE os benchmarks brasileiros fornecidos para calcular estimativas
    - Use as fórmulas dos KPIs listadas acima para calcular projeções precisas
    - Destaque os KPIs primários: {", ".join(primarios) if primarios else "foco na etapa do funil"}
    - Considere o contexto da etapa do funil para definir expectativas realistas
    - Considere as metas específicas quando fornecidas
    - Calcule volumes baseados em: Budget / CPM * 1000 para impressões, Budget / CPC para cliques, etc.

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

    prompt = f"""
    Para a campanha na etapa {etapa_funil} do funil com:
    - Tipo de Público: {params['tipo_publico']}
    - Objetivo: {params['objetivo_campanha']}
    - Plataformas: {", ".join(params['ferramentas'])}
    - Localizações: {params['localizacao_primaria']} (primária), {params['localizacao_secundaria']} (secundária)
    - KPIs Primários: {", ".join(primarios) if primarios else "A serem otimizados"}
    - KPIs Secundários: {", ".join(secundarios) if secundarios else "Nenhum"}
    {funnel_context}
    {kpi_defs_block}
    {benchmark_block}
    E considerando a estratégia geral:
    {recomendacao_estrategica}

    Desenvolva recomendações de público OTIMIZADAS PARA OS OBJETIVOS incluindo:
    1. Segmentação específica para os KPIs primários selecionados
    2. Parâmetros de targeting focados nos objetivos
    3. Estratégias de expansão adequadas
    4. Considerações sobre frequência e saturação
    5. Benchmarks de performance esperada por segmento

    REGRAS:
    - Manter foco absoluto nos estados especificados
    - Adaptar recomendações aos KPIs primários selecionados
    - Priorizar estratégias adequadas para a etapa {etapa_funil}
    - Usar benchmarks para definir expectativas realistas

    Formato: Markdown com listas e headers
    """
    response = modelos["audiencia"].generate_content(prompt)
    return response.text


def gerar_cronograma(modelos, params: Dict[str, Any], recomendacao_estrategica: str, distribuicao_budget: str) -> str:
    """Gera cronograma de implementacao. Usa o modelo Gestor de Projetos."""
    etapa_funil = params['etapa_funil']
    okrs_escolhidos, _, primarios, secundarios = _extract_okrs(params)
    funnel_context = _get_funnel_stage_context(params)

    prompt = f"""
    Com base na estratégia para {etapa_funil} do funil:
    {recomendacao_estrategica}

    E na distribuição de budget:
    {distribuicao_budget}
    {funnel_context}
    Crie um cronograma OTIMIZADO considerando:
    - Budget total: R$ {params['budget']:,.2f}
    - Período: {params['periodo']}
    - Plataformas: {", ".join(params['ferramentas'])}
    - KPIs Primários: {", ".join(primarios) if primarios else "A serem otimizados"}
    - KPIs Secundários: {", ".join(secundarios) if secundarios else "Nenhum"}

    Inclua:
    1. Fases de implementação adequadas
    2. Distribuição temporal do budget
    3. Marcos importantes e checkpoints de performance
    4. Frequência de ajustes recomendada
    5. Gatilhos de otimização baseados nos KPIs primários

    DICAS:
    - Adaptar cronograma aos objetivos específicos
    - Não incluir fases irrelevantes
    - Manter realismo no período especificado
    - Definir KPIs de controle em cada fase

    Formato: Markdown com tabelas ou listas numeradas
    """
    response = modelos["gestor"].generate_content(prompt)
    return response.text
