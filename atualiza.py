import sqlite3 as sql

conexao = sql.connect('main.db')
cursor = conexao.cursor()

id = 1
cursor.execute(
    """
        UPDATE Filmes SET nome = ?
        WHERE id = ?
    """,
    ("Homem Aranha", id)
)

conexao.commit()
print("Dados alterados com sucesso!")