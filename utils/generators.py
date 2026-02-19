from typing import Dict, Any

from utils.constants import BENCHMARKS_BR, TEMPLATES_ALOCACAO_BUDGET


def _extract_okrs(params: Dict[str, Any]):
    """Extrai OKRs selecionados, metas, e separação por hierarquia."""
    okrs_escolhidos = [k for k, v in params['metricas'].items() if v['selecionada']]
    metas_especificas = [f"{k}: {v['valor']}" for k, v in params['metricas'].items() if v['selecionada'] and v['valor']]

    primarios = [k for k, v in params['metricas'].items() if v['selecionada'] and v.get('hierarquia') == 'primario']
    secundarios = [k for k, v in params['metricas'].items() if v['selecionada'] and v.get('hierarquia') in ('secundario', 'terciario')]

    return okrs_escolhidos, metas_especificas, primarios, secundarios


def _get_benchmark_block(params: Dict[str, Any]) -> str:
    """Formata benchmarks das plataformas selecionadas como bloco de texto."""
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
    """Formata templates de alocação como referência."""
    linhas = []
    for nome, tpl in TEMPLATES_ALOCACAO_BUDGET.items():
        dist = ", ".join(f"{k}: {v}%" for k, v in tpl["distribuicao"].items() if v > 0)
        linhas.append(f"    - {nome}: {dist}")
    return "\n    **Templates de Alocação (referência):**\n" + "\n".join(linhas) + "\n"


def gerar_recomendacao_estrategica(modelos, params: Dict[str, Any]) -> str:
    """Gera a recomendacao estrategica inicial. Usa o modelo Estrategista."""
    etapa_funil = params['etapa_funil']
    okrs_escolhidos, metas_especificas, primarios, secundarios = _extract_okrs(params)
    benchmark_block = _get_benchmark_block(params)

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
    {benchmark_block}
    Forneça:
    1. Análise estratégica focada em {etapa_funil} do funil (150-200 palavras)
    2. Principais oportunidades para os KPIs primários selecionados
    3. Riscos potenciais específicos para esta etapa
    4. Recomendação geral de abordagem

    Dicas:
    - Foco absoluto nos KPIs primários: {", ".join(primarios) if primarios else "gerar sugestões apropriadas"}
    - Monitore secundários: {", ".join(secundarios) if secundarios else "gerar sugestões"}
    - Use os benchmarks brasileiros como base para estimativas realistas
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
    - Destaque os KPIs primários: {", ".join(primarios) if primarios else "foco na etapa do funil"}
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

    prompt = f"""
    Para a campanha na etapa {etapa_funil} do funil com:
    - Tipo de Público: {params['tipo_publico']}
    - Objetivo: {params['objetivo_campanha']}
    - Plataformas: {", ".join(params['ferramentas'])}
    - Localizações: {params['localizacao_primaria']} (primária), {params['localizacao_secundaria']} (secundária)
    - KPIs Primários: {", ".join(primarios) if primarios else "A serem otimizados"}
    - KPIs Secundários: {", ".join(secundarios) if secundarios else "Nenhum"}
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

    prompt = f"""
    Com base na estratégia para {etapa_funil} do funil:
    {recomendacao_estrategica}

    E na distribuição de budget:
    {distribuicao_budget}

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
