# Analise de dados para a Policia Militar do Distrito Federal -PMDF
- Aluno: Guilherme de Paula Alves
- Nome do projeto : Relatório de Análise Criminal para a Policia Militar do Distrito Federal - PMDF

## 📌 Visão Geral do Projeto
Este projeto tem como objetivo analisar dados criminais do Distrito Federal, fornecendo insights estratégicos para a Polícia Militar e outros órgãos de segurança. Utilizando técnicas de Analise de dados e Visualização de Dados, foram identificados padrões temporais, geográficos e comportamentais que podem auxiliar no planejamento operacional.

## 📊 Dados Analisados
Período: 2022 - 2024

Fontes: [Base de Dados e Notas Metodológicas dos Gestores Estaduais - Sinesp VDE 2015 a 2025](https://www.gov.br/mj/pt-br/assuntos/sua-seguranca/seguranca-publica/estatistica/dados-nacionais-1/base-de-dados-e-notas-metodologicas-dos-gestores-estaduais-sinesp-vde-2022-e-2023) 

Localização: Regiões administrativas do DF

Eventos: Tipos de ocorrências registradas (homicídios, roubos, apreensões, etc.)

Vítimas: Distribuição por gênero e quantidade

Armas e Drogas: Dados de apreensões

Órgãos Responsáveis: Polícia Militar, Civil, Bombeiros, etc.

## 1.📈 Análise Temporal

Objetivo: **Identificar variações sazonais e tendências ao longo do tempo.**

Principais insights encontrados:
- Meses com maior incidência de crimes
- Eventos mais frequentes em cada ano
- Comparativo anual (2022 vs. 2023 vs. 2024)

Exemplo de Gráfico:
(Inserir imagem da evolução mensal aqui)

## 2. 🗺️ Análise Geográfica

Objetivo: **Mapear as regiões com maior criminalidade e os tipos de crimes mais comuns em cada área.**

Principais Insights:

- Top 15 regiões com mais ocorrências
- Relação entre tipo de crime e localidade
- Áreas prioritárias para patrulhamento

Exemplo de Gráfico:
(Inserir imagem do heatmap de crimes por região aqui)

## 3. 👥 Análise de Vítimas

Objetivo: **Compreender o perfil das vítimas para políticas de prevenção.**

Principais Insights:

- Distribuição por gênero (masculino, feminino, não informado)
- Eventos com maior número de vítimas
- Relação entre tipo de crime e quantidade de vítimas

Exemplo de Gráfico:
(Inserir gráfico de pizza ou barras aqui)

## 4. 🔫 Análise de Armas Apreendidas

Objetivo: **Identificar os tipos de armas mais comuns e suas origens.**

Principais Insights:

- Armas mais frequentes (pistolas, revólveres, fuzis, etc.)
- Regiões com maior apreensão
- Relação entre tipo de arma e tipo de crime

Exemplo de Gráfico:
(Inserir gráfico de barras horizontais aqui)

## 5. 💊 Análise de Drogas Apreendidas
Objetivo: **Mapear o tráfico e consumo de substâncias ilícitas.**

**Principais Insights:**
- Tipos de drogas mais apreendidas (cocaína, maconha, etc.)
- Variação temporal das apreensões
- Locais de maior incidência

Exemplo de Gráfico:
(Inserir gráfico de evolução temporal aqui)

## 6. 👮 Análise por Órgão Responsável
Objetivo: **Avaliar a atuação das instituições em diferentes tipos de ocorrência.**

**Principais Insights:**
- Distribuição de atendimentos por órgão (PM, PC, Bombeiros, etc.)
- Principais eventos associados a cada instituição
- Eficiência operacional comparativa

Exemplo de Gráfico:
(Inserir heatmap de eventos por órgão aqui)

## 🛠️ Contexto Técnico - Ferramentas Utilizadas

**Linguagem:** Python (Pandas, NumPy, Matplotlib, Seaborn)

**Banco de Dados:** PostgreSQL (dados hospedados na Microsoft Azure)

**Visualização:** Gráficos interativos (Plotly), heatmaps, séries temporais

**Metodologia:**
- Extração: Consulta direta ao banco de dados (SQLAlchemy).
- Limpeza: Tratamento de valores nulos e padronização.
- Análise: Agregação de dados e identificação de padrões.

## 🎯 Recomendações para Ação Policial

Reforço em Regiões Críticas:

Foco em {{REGIÃO_1}}, {{REGIÃO_2}} e {{REGIÃO_3}} (maior incidência de crimes).

Operações Específicas:

Intensificar apreensão de {{ARMA_MAIS_COMUM}} em {{LOCAL_ALVO}}.
Aumentar patrulhamento em {{MÊS_CRÍTICO}} (pico de ocorrências).

Treinamento e Recursos:

Capacitação para {{ÓRGÃO}} em {{TIPO_DE_CRIME}}.

📌 Resumo

- Gráfico 1 - Evolução Temporal
- Gráfico 2 - Heatmap Geográfico
- Gráfico 3 - Distribuição de Vítimas
- Gráfico 4 - Tipos de Armas
- Gráfico 5 - Apreensão de Drogas
- Gráfico 6 - Eventos por Órgão
