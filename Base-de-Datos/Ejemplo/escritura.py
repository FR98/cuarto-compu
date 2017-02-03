import sqlite3
conn = sqlite3.connect('personas.db')

conn.execute("INSERT INTO Familia(nombre) VALUES('Familia 1')")
conn.execute("INSERT INTO Familia(nombre) VALUES('Familia 2')")
conn.execute("INSERT INTO Familia(nombre) VALUES('Familia 3')")
conn.execute("INSERT INTO Familia(nombre) VALUES('Familia 4')")
conn.execute("INSERT INTO Familia(nombre) VALUES('Familia 5')")


conn.commit()
conn.close()