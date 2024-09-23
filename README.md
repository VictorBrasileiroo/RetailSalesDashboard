# **Retail Sales Dashboard**

Este projeto cria um dashboard interativo para visualização e análise de dados de vendas no varejo. Utilizando o dataset de vendas, que inclui informações como ID de transações, datas, categorias de produtos, gênero, quantidade de produtos vendidos e faturamento, o dashboard permite explorar e entender as tendências de vendas ao longo do tempo e os padrões de compra dos clientes. 

## **Funcionalidades Principais**
- Filtros interativos por mês para explorar os dados.
- Gráficos que mostram a quantidade de produtos vendidos por categoria.
- Análise de faturamento por categoria e gênero.
- Distribuição do faturamento total por gênero e tipo de produto.
- Tendências de faturamento ao longo do tempo.

## **Tecnologias Utilizadas**
- **Python**: Linguagem principal do projeto.
- **Streamlit**: Ferramenta para criação do dashboard interativo.
- **Pandas**: Biblioteca para manipulação e análise de dados.
- **Plotly**: Usado para gerar gráficos interativos.
  
## **Dataset**
<a href='https://www.kaggle.com/datasets/mohammadtalib786/retail-sales-dataset'>Link para o Dataset</a><br><br>
O dataset contém as seguintes colunas:
- **Transaction ID**: ID único da transação.
- **Date**: Data da transação.
- **Customer ID**: ID único do cliente.
- **Gender**: Gênero do cliente (Masculino/Feminino).
- **Age**: Idade do cliente.
- **Product Category**: Categoria do produto (Ex: Beleza, Vestuário, Eletrônicos, etc.).
- **Quantity**: Quantidade de produtos comprados.
- **Price per Unit**: Preço por unidade do produto.
- **Total Amount**: Total pago na transação.

## **Pré-requisitos**
- **Python 3.8+**
- Instalar as bibliotecas necessárias:
  ```bash
  pip install streamlit pandas plotly
  ```

## Como Executar:
1.Clone o repositório:
  ```bash
  git clone https://github.com/VictorBrasileiroo/RetailSalesDashboard.git
  ```
2.Navegue até o diretório:
  ```bash
  cd retail-sales-dashboard
  ```
3.Execute o dashboard:
  ```bash
  streamlit run data.py
  ```

## **Explicação do Código**
O código está dividido em várias seções:

- **Leitura dos Dados**: Os dados são carregados a partir de um arquivo CSV.
- **Preprocessamento**: As datas são convertidas para o formato `datetime`, e novos campos são criados, como o mês para facilitar os filtros.
- **Criação de Gráficos**:
  - **Faturamento ao Longo do Tempo**: Um gráfico de linha que mostra a evolução do faturamento total.
  - **Quantidade de Produtos por Categoria**: Um gráfico de barras que exibe a quantidade de produtos vendidos por tipo.
  - **Faturamento por Categoria e Gênero**: Gráfico de barras agrupadas que mostra o faturamento dividido por categorias e gênero dos clientes.
  - **Distribuição do Faturamento por Gênero**: Um gráfico de pizza que exibe a proporção do faturamento gerado por clientes masculinos e femininos.
  - **Distribuição por Categoria de Produto**: Outro gráfico de pizza que detalha o faturamento por tipo de produto.

## Autores:
| Nome                                   | Número de Matrícula | E-mail                  | Curso               |
|----------------------------------------|---------------------|-------------------------|---------------------|
| Victor André Lopes Brasileiro          | 202407269           | valb1@ic.ufal.br       | Ciência da Computação |

## **Licença**
Este projeto está licenciado sob os termos da [MIT License](LICENSE).
