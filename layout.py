import streamlit as st
import dados as ds
import datetime as dt

currentYear = dt.datetime.now().year

st.title("Filmes")
filmes = ds.obter_dados()

nome = st.text_input("Nome")
ano = st.number_input("Ano do filme:", min_value=1900, max_value=currentYear)
nota = st.slider("Nota", min_value=0.0, max_value=10.0, format="%0.1f")

if st.button("Adicionar filme"):
    ds.insere_dados(nome, ano, nota)
    filmes = ds.obter_dados()
    st.success("Filme adicionado com sucesso")

@st.dialog(title="Escolha qual filme você deseja excluir:", width="small")
def excluir_filme(id):
    st.write("Escolha filme para excluir:")
    id = st.selectbox("Filme", filmes)
    if st.button("Confimar"):
        ds.exclui_dados(id)
        filmes = ds.obter_dados()
        st.success("Filme excluido com sucesso")

if st.button("Excluir filme"):
    excluir_filme()

if st.button("Nova Tabela"):
    ds.nova_tabela()
    filmes = ds.obter_dados()
    st.success("Tabela criada com sucesso")

if st.button("Excluir tabela"):
    ds.exclui_tabela()
    filmes = ds.obter_dados()
    st.success("Tabela excluida com sucesso")

if st.button("Atualizar tabela"):
    filmes = ds.obter_dados()
    st.success("Tabela atualizada com sucesso")
    
def atualizar_tabela():
    filmes = ds.obter_dados()
    return filmes

st.header("Lista de filmes")
st.table(filmes)