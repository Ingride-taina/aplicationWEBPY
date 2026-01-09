import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")

df_reviews = pd.read_csv("Data/customer reviews.csv")
df_top100_books = pd.read_csv("Data/Top-100 Trending Books.csv")


price_max= df_top100_books["book price"].max()
price_min= df_top100_books["book price"].min()

#criando o slider no sidebar, definindo o valor minimo e maximo e o valor inicial
max_price = st.sidebar.slider("Price Range", 
                              price_min, 
                              price_max, 
                              price_max)
#filtro do dataframe baseado no valor selecionado no slider ou seja cada vez que o valor do slider mudar o dataframe será atualizado
df_books= df_top100_books[df_top100_books["book price"]<= max_price]

#Título da página e exibição do dataframe filtrado
st.title(" Top 100 Críticas de Livros Best-Sellados na Amazon")
df_books

#criando gráficos de barras e histograma
fig=px.bar(df_books["year of publication"].value_counts())
fig2=px.histogram(df_books["book price"])

#mostrando os gráficos lado a lado
col1,col2=st.columns(2)
col1.plotly_chart(fig)
col2.plotly_chart(fig2)
