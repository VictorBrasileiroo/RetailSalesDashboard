import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(layout="wide")

# Carregar os dados
try:
    df = pd.read_csv("retail_sales_dataset.csv")
except Exception as e:
    st.error(f"Erro ao carregar o arquivo: {e}")
    st.stop()

# Preprocessamento dos dados
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values('Date')
df['Month'] = df['Date'].apply(lambda x: str(x.year) + "-" + str(x.month))

# Sidebar para selecionar o mês
st.sidebar.header("Filtros")
month = st.sidebar.selectbox("Mês", df['Month'].unique())
dfFiltado = df[df["Month"] == month]

# Criação das colunas para os gráficos
col5, col1, col2 = st.columns(3) 
col3, col4 = st.columns(2)

# Gráfico 5 --> Faturamento Total ao Longo do Tempo
with col5:
    df['YearMonth'] = df['Date'].dt.to_period('M').astype(str)
    dfTemporal = df.groupby('YearMonth')['Total Amount'].sum().reset_index()
    figTemporal = px.line(dfTemporal, x='YearMonth', y='Total Amount', 
                          title='Faturamento Total ao Longo do Tempo')
    st.plotly_chart(figTemporal, use_container_width=True)

# Gráfico 1 --> Quantidade de Produtos
with col1:
    figQnt = px.bar(dfFiltado, x="Product Category", y="Quantity", 
                    title="Quantidade de Produtos por Tipo de Produto")
    st.plotly_chart(figQnt, use_container_width=True)

# Gráfico 2 --> Faturamento por Categoria e Gênero
with col2:
    dfAgrupado = dfFiltado.groupby(['Product Category', 'Gender'])['Total Amount'].sum().reset_index()
    figCat = px.bar(dfAgrupado, x="Product Category", y="Total Amount", color="Gender",
                    title="Faturamento Total por Categoria de Produto e Gênero")
    st.plotly_chart(figCat, use_container_width=True)

# Gráfico 3 --> Distribuição do Faturamento por Gênero
with col3:
    dfGender = dfFiltado.groupby('Gender')['Total Amount'].sum().reset_index()
    figGender = px.pie(dfGender, values="Total Amount", names="Gender", 
                       title="Distribuição do Faturamento Por Gênero")
    st.plotly_chart(figGender, use_container_width=True)

# Gráfico 4 --> Distribuição do Faturamento por Tipo de Produto
with col4:
    dfCatGroup = dfFiltado.groupby('Product Category')['Total Amount'].sum().reset_index()
    figCatGroup = px.pie(dfCatGroup, values="Total Amount", names="Product Category", 
                         title="Distribuição do Faturamento Por Tipo de Produto")
    st.plotly_chart(figCatGroup, use_container_width=True)
