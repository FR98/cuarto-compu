import sqlite3
conn = sqlite3.connect('personas.db')

resultados = conn.execute("SELECT * FROM Familia")

for resultado in resultados:
	print(resultado)

conn.commit()
conn.close()