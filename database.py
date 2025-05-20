import sqlite3 as sql

conexao = sql.connect('main.db')

cursor = conexao.cursor()

cursor.execute(
    """
    create table Filmes if not exists(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        ano INTEGER NOT NULL,
        nota REAL NOT NULL
    );
    """
)

conexao.close()
print('Tabela criada com sucesso!')