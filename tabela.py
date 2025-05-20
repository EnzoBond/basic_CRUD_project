import sqlite3 as sql

conexao = sql.connect('main.db')

cursor = conexao.cursor()