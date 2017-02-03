import sqlite3
conn = sqlite3.connect('personas.db')

conn.execute("INSERT INTO Persona(familia_id, nombre, apellido, edad) VALUES(10, 'Willi', 'Rosal', 17)")
conn.execute("INSERT INTO Persona(familia_id, nombre, apellido, edad) VALUES(20, 'Karen', 'Caballeros', 16)")
conn.execute("INSERT INTO Persona(familia_id, nombre, apellido, edad) VALUES(10, 'Emanuel', 'Rosal', 15)")
conn.execute("INSERT INTO Persona(familia_id, nombre, apellido, edad) VALUES(10, 'David', 'Rosal', 14)")
conn.execute("INSERT INTO Persona(familia_id, nombre, apellido, edad) VALUES(10, 'Pablo', 'Rosal', 12)")

conn.execute("INSERT INTO Persona(familia_id, nombre, apellido, edad) VALUES(1, 'Willi', 'Rosal', 17)")
conn.execute("INSERT INTO Persona(familia_id, nombre, apellido, edad) VALUES(2, 'Karen', 'Caballeros', 16)")
conn.execute("INSERT INTO Persona(familia_id, nombre, apellido, edad) VALUES(1, 'Emanuel', 'Rosal', 15)")
conn.execute("INSERT INTO Persona(familia_id, nombre, apellido, edad) VALUES(1, 'David', 'Rosal', 14)")
conn.execute("INSERT INTO Persona(familia_id, nombre, apellido, edad) VALUES(1, 'Pablo', 'Rosal', 12)")

conn.commit()
conn.close()