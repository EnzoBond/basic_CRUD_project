import sqlite3 as sql
import database as db

def connect_db():
    conexao = sql.connect('main.db')
    return conexao


def insere_dados(nome, ano, nota):
    conexao = connect_db()
    cursor = conexao.cursor()

    cursor.execute(
        """
        INSERT INTO Filmes (nome, ano, nota)
        VALUES (?, ?, ?)
        """,
        (nome, ano, nota)
    )

    conexao.commit()
    conexao.close()

def obter_dados():
    conexao = connect_db()
    cursor = conexao.cursor()
    cursor.execute("""SELECT * FROM Filmes;""")
    dados = cursor.fetchall()
    cursor.close()
    return dados


def exclui_dados(id):
    conexao = connect_db()
    cursor = conexao.cursor()

    cursor.execute(
        """
        DELETE FROM Filmes
        WHERE id = ?
        """,
        (id,)
    )

    conexao.commit()
    conexao.close()

def exclui_tabela():
    conexao = connect_db()
    cursor = conexao.cursor()

    cursor.execute("DROP TABLE Filmes")

    conexao.commit()
    conexao.close()

def nova_tabela():
    db.nova_tabela()
