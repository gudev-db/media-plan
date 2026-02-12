from typing import Dict, Any


def _extract_okrs(params: Dict[str, Any]):
    """Extrai OKRs selecionados e metas especificas dos parametros."""
    okrs_escolhidos = [k for k, v in params['metricas'].items() if v['selecionada']]
    metas_especificas = [f"{k}: {v['valor']}" for k, v in params['metricas'].items() if v['selecionada'] and v['valor']]
    return okrs_escolhidos, metas_especificas


def gerar_recomendacao_estrategica(modelo, params: Dict[str, Any]) -> str:
    """Gera a recomendacao estrategica inicial."""
    etapa_funil = params['etapa_funil']
    okrs_escolhidos, metas_especificas = _extract_okrs(params)

    prompt = f"""
    Como especialista em planejamento de mídia digital, analise os seguintes parâmetros e forneça uma recomendação estratégica:

    **Campanha:** {params['objetivo_campanha']} (Etapa do Funil: {etapa_funil})
    **Tipo de Campanha:** {params['tipo_campanha']}
    **Budget Total:** R$ {params['budget']:,.2f}
    **Período da Campanha:** {params['periodo']}
    **Ferramentas/Plataformas:** {", ".join(params['ferramentas'])}
    **Localização Primária:** {params['localizacao_primaria']}
    **Localização Secundária:** {params['localizacao_secundaria']}
    **Tipo de Público:** {params['tipo_publico']}
    **Tipos de Criativo:** {", ".join(params['tipo_criativo'])}
    **OKRs Escolhidos:** {", ".join(okrs_escolhidos) if okrs_escolhidos else "A serem definidos"}
    **Metas Específicas:** {", ".join(metas_especificas) if metas_especificas else "Nenhuma meta específica"}
    **Detalhes da Ação:** {params['detalhes_acao'] or "Nenhum"}
    **Observações:** {params['observacoes'] or "Nenhuma"}

    Forneça:
    1. Análise estratégica focada em {etapa_funil} do funil (150-200 palavras)
    2. Principais oportunidades para os OKRs selecionados
    3. Riscos potenciais específicos para esta etapa
    4. Recomendação geral de abordagem

    Dicas:
    - Mantenha o foco absoluto nos OKRs selecionados: {", ".join(okrs_escolhidos) if okrs_escolhidos else "gerar sugestões apropriadas"}
    - Considere as metas específicas quando fornecidas
    - Adapte ao período especificado

    Formato: Markdown com headers (##, ###)
    """
    response = modelo.generate_content(prompt)
    return response.text


def gerar_distribuicao_budget(modelo, params: Dict[str, Any], recomendacao_estrategica: str) -> str:
    """Gera a distribuicao de budget baseada na recomendacao estrategica."""
    etapa_funil = params['etapa_funil']
    okrs_escolhidos, metas_especificas = _extract_okrs(params)

    prompt = f"""
    Com base na seguinte recomendação estratégica (Etapa {etapa_funil} do Funil):
    {recomendacao_estrategica}

    E nos parâmetros originais:
    - Budget: R$ {params['budget']:,.2f}
    - Período: {params['periodo']}
    - Plataformas: {", ".join(params['ferramentas'])}
    - Localizações: Primária ({params['localizacao_primaria']}), Secundária ({params['localizacao_secundaria']})
    - Tipos de Criativo: {", ".join(params['tipo_criativo'])}
    - OKRs: {", ".join(okrs_escolhidos) if okrs_escolhidos else "A serem otimizados"}
    - Metas: {", ".join(metas_especificas) if metas_especificas else "Nenhuma específica"}

    Crie uma tabela detalhada de distribuição de budget OTIMIZADA PARA OS OKRs SELECIONADOS com:
    1. Divisão por plataforma (% e valor)
    2. Alocação geográfica (primária vs secundária)
    3. Tipos de criativos recomendados (APENAS: {", ".join(params['tipo_criativo'])})
    4. Justificativa estratégica para cada alocação

    REGRAS:
    - Priorize os OKRs selecionados: {", ".join(okrs_escolhidos) if okrs_escolhidos else "otimize para a etapa do funil"}
    - Considere as metas específicas quando fornecidas
    - Não sugerir criativos fora dos tipos especificados
    - Manter foco absoluto nos estados solicitados

    Inclua também uma breve análise (50-100 palavras) explicando como a distribuição atende aos objetivos.

    Formato: Markdown com tabelas (use | para divisão)
    """
    response = modelo.generate_content(prompt)
    return response.text


def gerar_previsao_resultados(modelo, params: Dict[str, Any], recomendacao_estrategica: str, distribuicao_budget: str) -> str:
    """Gera previsao de resultados baseada nos parametros."""
    etapa_funil = params['etapa_funil']
    okrs_escolhidos, metas_especificas = _extract_okrs(params)

    prompt = f"""
    Com base na estratégia para {etapa_funil} do funil:
    {recomendacao_estrategica}

    E na distribuição de budget:
    {distribuicao_budget}

    Estime os resultados ESPERADOS considerando:
    - Budget total: R$ {params['budget']:,.2f}
    - Período: {params['periodo']}
    - OKRs: {", ".join(okrs_escolhidos) if okrs_escolhidos else "A serem otimizados"}
    - Metas: {", ".join(metas_especificas) if metas_especificas else "Nenhuma específica"}

    Forneça:
    1. Tabela com métricas ESPECÍFICAS para os OKRs selecionados
    2. Estimativas realistas baseadas em benchmarks
    3. Análise de potencial desempenho (50-100 palavras)
    4. KPIs CHAVE para monitorar

    DICAS:
    - Destaque os OKRs selecionados: {", ".join(okrs_escolhidos) if okrs_escolhidos else "foco na etapa do funil"}
    - Considere as metas específicas quando fornecidas
    - Use benchmarks realistas para o setor

    Formato: Markdown com tabelas
    """
    response = modelo.generate_content(prompt)
    return response.text


def gerar_recomendacoes_publico(modelo, params: Dict[str, Any], recomendacao_estrategica: str) -> str:
    """Gera recomendacoes detalhadas de publico-alvo."""
    etapa_funil = params['etapa_funil']
    okrs_escolhidos, _ = _extract_okrs(params)

    prompt = f"""
    Para a campanha na etapa {etapa_funil} do funil com:
    - Tipo de Público: {params['tipo_publico']}
    - Objetivo: {params['objetivo_campanha']}
    - Plataformas: {", ".join(params['ferramentas'])}
    - Localizações: {params['localizacao_primaria']} (primária), {params['localizacao_secundaria']} (secundária)
    - OKRs: {", ".join(okrs_escolhidos) if okrs_escolhidos else "A serem otimizados"}

    E considerando a estratégia geral:
    {recomendacao_estrategica}

    Desenvolva recomendações de público OTIMIZADAS PARA OS OBJETIVOS incluindo:
    1. Segmentação específica para os OKRs selecionados
    2. Parâmetros de targeting focados nos objetivos
    3. Estratégias de expansão adequadas
    4. Considerações sobre frequência e saturação

    REGRAS:
    - Manter foco absoluto nos estados especificados
    - Adaptar recomendações aos OKRs selecionados
    - Priorizar estratégias adequadas para a etapa {etapa_funil}

    Formato: Markdown com listas e headers
    """
    response = modelo.generate_content(prompt)
    return response.text


def gerar_cronograma(modelo, params: Dict[str, Any], recomendacao_estrategica: str, distribuicao_budget: str) -> str:
    """Gera cronograma de implementacao."""
    etapa_funil = params['etapa_funil']
    okrs_escolhidos, _ = _extract_okrs(params)

    prompt = f"""
    Com base na estratégia para {etapa_funil} do funil:
    {recomendacao_estrategica}

    E na distribuição de budget:
    {distribuicao_budget}

    Crie um cronograma OTIMIZADO considerando:
    - Budget total: R$ {params['budget']:,.2f}
    - Período: {params['periodo']}
    - Plataformas: {", ".join(params['ferramentas'])}
    - OKRs: {", ".join(okrs_escolhidos) if okrs_escolhidos else "A serem otimizados"}

    Inclua:
    1. Fases de implementação adequadas
    2. Distribuição temporal do budget
    3. Marcos importantes
    4. Frequência de ajustes recomendada

    DICAS:
    - Adaptar cronograma aos objetivos específicos
    - Não incluir fases irrelevantes
    - Manter realismo no período especificado

    Formato: Markdown com tabelas ou listas numeradas
    """
    response = modelo.generate_content(prompt)
    return response.text
