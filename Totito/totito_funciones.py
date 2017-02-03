def jugador1(j1, totito):
	elec = ord(j1) - 65
	totito[elec // 3][elec % 3] = "X"
	nuevoTotito = ""
	for i in totito:
		for j in i:
			nuevoTotito += j + " "
		nuevoTotito += "\n"
	return nuevoTotito

def jugador2(j2, totito):
	elec = ord(j2) - 65
	totito[elec // 3][elec % 3] = "O"
	nuevoTotito = ""
	for i in totito:
		for j in i:
			nuevoTotito += j + " "
		nuevoTotito += "\n"
	return nuevoTotito
	
def ganador(totito):
	#Convierte X y O en 1 y -1
	para_sumar = []
	for i in totito:
		para_sumar_fila = []
		for j in i:
			if j == "X":
				para_sumar_fila.append(1)
			elif j == "O":
				para_sumar_fila.append(-1)
			else:
				para_sumar_fila.append(0)	
		para_sumar.append(para_sumar_fila)

	sumas = []
	suma_diagonal1 = 0
	suma_diagonal2 = 0
	#Para las filas
	for fila in para_sumar:
		sumas.append(sum(fila))
	#Para las columnas
	for columna in range (3):
		sumas.append(para_sumar[0][columna] + para_sumar[1][columna] + para_sumar[2][columna])
	#Para las diagonales
	for d in range (3):
		suma_diagonal1 += para_sumar[d][d]
		suma_diagonal2 += para_sumar[d][2 - d]
	sumas.append(suma_diagonal1)
	sumas.append(suma_diagonal2)
	#Verificacion del ganador
	if 3 in sumas:
		return "Ganador: Jugador 1"
	elif -3 in sumas:
		return "Ganador: Jugador 2"
	else:
		return ""