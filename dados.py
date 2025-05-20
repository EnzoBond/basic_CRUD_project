import sqlite3 as sql

conexao = sql.connect('main.db')
cursor = conexao.cursor()

cursor.execute(
    """
        INSERT INTO Filmes(nome, ano, nota) VALUES ('Os Vingadores','2022','8.0')

    """
)

conexao.commit()
conexao.close()


