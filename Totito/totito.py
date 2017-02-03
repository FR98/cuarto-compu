from totito_funciones import jugador1, jugador2, ganador
print ("")
print ("Totito")
print ("")
totito = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]

print (totito[0][0], totito[0][1], totito[0][2])
print (totito[1][0], totito[1][1], totito[1][2])
print (totito[2][0], totito[2][1], totito[2][2])
print ("")

for turnos in range (0, 4):

	if (ganador(totito) != "Ganador: Jugador 1") and (ganador(totito) != "Ganador: Jugador 2"):

		j1 = input("Jugador 1 escoja ubicacion: ")
		print (jugador1(j1.upper(), totito))
		print (ganador(totito))

		if (ganador(totito) != "Ganador: Jugador 1") and (ganador(totito) != "Ganador: Jugador 2"):
			j2 = input("Jugador 2 escoja ubicacion: ")
			print (jugador2(j2.upper(), totito))
			print (ganador(totito))

if (ganador(totito) != "Ganador: Jugador 1") and (ganador(totito) != "Ganador: Jugador 2"):
	j1 = input("Jugador 1 escoja ubicacion: ")
	print (jugador1(j1.upper(), totito))
	print (ganador(totito))

fin = input("")