import sqlite3
conn = sqlite3.connect('personas.db')

conn.execute("CREATE TABLE Familia(id integer primary key autoincrement, nombre text)")
conn.execute("CREATE TABLE Persona(id integer primary key autoincrement, familia_id integer, nombre text, apellido text, edad integer, FOREIGN KEY (familia_id) REFERENCES Familia(id))")

conn.commit()
conn.close()
