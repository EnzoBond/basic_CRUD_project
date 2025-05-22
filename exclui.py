import sqlite3 as sql

conexao = sql.connect('main.db')
cursor =  conexao.cursor()

id = (1,2)
cursor.execute(
    """
    DELETE FROM Filmes
    WHERE id in (?, ?)
    """,
    id
)

conexao.commit()
print("Dados excluídos com sucesso")