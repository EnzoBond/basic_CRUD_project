import streamlit as st
import dados as ds
import datetime

currentYear = datetime.datetime.now().year

st.title("Filmes")
filmes = ds.obter_dados()

nome = st.text_input("Nome")
ano = st.number_input("Ano do filme:", min_value=1900, max_value=currentYear)
nota = st.slider("Nota", min_value=0.0, max_value=10.0)

if st.button("Adicionar filme"):
    ds.insere_dados(nome, ano, nota)
    st.success("Filme adicionado com sucesso")

if st.button("Excluir filme"):
    ds.exclui_dados(1)
    st.success("Filme excluido com sucesso")

if st.button("Nova Tabela"):
    ds.nova_tabela()
    st.success("Tabela criada com sucesso")

if st.button("Excluir tabela"):
    ds.exclui_tabela()
    st.success("Tabela excluida com sucesso")

if st.button("Atualizar tabela"):
    filmes = ds.obter_dados()
    st.success("Tabela atualizada com sucesso")
    
def atualizar_tabela():
    filmes = ds.obter_dados()
    return filmes

st.header("Lista de filmes")
st.table(filmes)