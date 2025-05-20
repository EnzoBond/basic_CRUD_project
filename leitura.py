import sqlite3 as sql

conexao =  sql.connect('main.db')
cursor = conexao.cursor()

dados = cursor.execute("SELECT * FROM Filmes")

print(dados.fetchall())