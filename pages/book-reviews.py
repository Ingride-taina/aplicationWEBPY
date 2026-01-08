import streamlit as st
import pandas as pd
import plotly.express as px

#remove as margens laterais da página
st.set_page_config(layout="wide")

df_reviews= pd.read_csv("Data/customer reviews.csv")
df_top100_books = pd.read_csv("Data/Top-100 Trending Books.csv")
st.title("Book Reviews")

#st.write(df_reviews.columns) <- verifica os titulos da coluna na tabela 

#df marcando o indicice de títulos um por um com UNIQUE e armazenando na variável books
bookslist =  df_top100_books ["book title"].unique()
# variável  que cria a caixa de seleção no sidebar -> titulo: Books, armazena o valor selecionado na variável booklist
book= st.sidebar.selectbox("Books", bookslist)

 # filtro do dataframe para mostrar apenas as informações do livro selecionado
df_book = df_top100_books[df_top100_books["book title"]== book]
df_book_reviews = df_reviews[df_reviews["book name"]== book]

#esse esquema fazcom que cada variavel pegue a informações especificadas de dentro do [] e faz com que apareça na página
#o iloc[0] pega o primeiro valor do livro selecionado no dataframe
book_title = df_book["book title"].iloc[0]
book_genre = df_book["genre"].iloc[0]
book_price = df_book['book price'].iloc[0]
book_rating = df_book["rating"].iloc[0]
book_year = df_book["year of publication"].iloc[0]

# esse f antes do texto faz com que seja possível inserir variáveis dentro do texto ou seja faz com que o texto da variavel seja formatado dentro do texto
st.title(f"📖 {book_title}")
st.subheader(book_genre)

#criando colunas para descrições abaixo do título
col1, col2, col3 = st.columns(3)

col1.metric( "Price", book_price)
col2.metric("Rating", book_rating)
col3.metric("Year of Publication", book_year)

st.divider() #linha de divisão
#mostrando as reviews do livro selecionado com um loop
for row in df_book_reviews.values:
    message= st.chat_message(f"{row[4]}")
    message.write (f"**{row[2]}**")
    message.write (row[5])