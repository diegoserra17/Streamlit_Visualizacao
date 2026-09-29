import streamlit as st
import pandas as pd

caminho_arquivo = "datasets/compras.csv"

df_compras = pd.read_csv(caminho_arquivo, sep=";", decimal=",", index_col=0)

#selecionando colunas
colunas = list(df_compras.columns)
#colocando a seleção de colunas na barra lateral esquerda
colunas_selecionadas = st.sidebar.multiselect("Selecione as colunas:", colunas, colunas)


col1, col2 = st.sidebar.columns(2)
#trazer todas as colunas menos a coluna id_compra para o selectbox
col_filtro = col1.selectbox("Selecione a coluna", 
               [c for c in colunas if c not in["id_compra"]])
#Como o selectbox não aceita valores nulos, vamos criar uma lista de valores únicos da 
#coluna selecionada, removendo os valores nulos
valor_filtro = col2.selectbox("Selecione o valor",
               list(df_compras[col_filtro].unique()))

#criar dois botões, um para filtrar e outro para limpar o filtro
st_filtrar = col1.button("Filtrar")
st_limpar = col2.button("Limpar")

#Filtrando o DataFrame de compras com base na coluna e valor selecionados, e exibindo apenas 
#as colunas selecionadas
if st_filtrar:
    st.dataframe(df_compras.loc[df_compras[col_filtro] == valor_filtro, colunas_selecionadas])
elif st_limpar:
    st.dataframe(df_compras[colunas_selecionadas])
else:
    st.dataframe(df_compras[colunas_selecionadas])