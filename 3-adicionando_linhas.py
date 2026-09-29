from datetime import datetime
import streamlit as st
import pandas as pd

caminho_datasets = "datasets"

df_compras = pd.read_csv(f"{caminho_datasets}/compras.csv", sep=";", decimal=",", index_col=0)
df_lojas = pd.read_csv(f"{caminho_datasets}/lojas.csv", sep=";", decimal=",")
df_produtos = pd.read_csv(f"{caminho_datasets}/produtos.csv", sep=";", decimal=",")

#cancado a coluna cidade/estado para facilitar a seleção da loja
#criando nova coluna cidade/estado no DataFrame de lojas, concatenando as colunas cidade e estado
df_lojas["cidade/estado"] = df_lojas["cidade"] + '/' + df_lojas["estado"]
#convertendo a coluna vendedores de string para lista
lista_lojas = df_lojas["cidade/estado"].to_list()
loja_selecionada = st.sidebar.selectbox("Selecione a loja:", lista_lojas)

#Selecionando o vendedor com base na loja selecionada
lista_vendedores = df_lojas.loc[df_lojas["cidade/estado"] == loja_selecionada, "vendedores"].iloc[0]
#Extrair a lista de vendedores da string, removendo os colchetes e aspas simples,
#e separando por vírgula
lista_vendedores = lista_vendedores.strip("][").replace("'", '').split(", ")
#Selecionando o vendedor com base na loja selecionada
vendedor_selecionado = st.sidebar.selectbox("Selecione o vendedor:", lista_vendedores)

#Selecionando o produto com base na lista de produtos
lista_produtos = df_produtos["nome"].to_list()
produto_selecionado = st.sidebar.selectbox("Selecione o produto:", lista_produtos)

#Nome do cliente para digitar na barra lateral esquerda
nome_cliente = st.sidebar.text_input("Nome do Cliente")
#Escolher o genero do cliente com base em uma lista de opções
genero_selecionado = st.sidebar.selectbox("Gênero do Cliente:", ["masculino", "feminino"])

forma_pagto_selecionado = st.sidebar.selectbox("Forma de Pagamento", ["cartão de crédito", "boleto", "pix", "dinheiro"])

#adicionar um botão para adicionar uma nova linha no DataFrame de compras com base nas informações 
#selecionadas na barra lateral esquerda
if st.sidebar.button("Adicionar Nova Compra"):
    lista_adicionar = [df_compras["id_compra"].max() + 1 if not df_compras.empty else 1,
                        loja_selecionada,
                        vendedor_selecionado,
                        produto_selecionado,
                        nome_cliente,
                        genero_selecionado,
                        forma_pagto_selecionado 
                      ]
    df_compras.loc[datetime.now()] = lista_adicionar
    
    df_compras.to_csv(f"{caminho_datasets}/compras.csv", index=False, decimal=",", sep=";")
    
    st.success("Compra adicionada")
    
st.dataframe(df_compras)