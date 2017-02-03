def prob_9 (n1, n2, n3):
	lista = [n1, n2, n3]
	lista.sort()
	if ((lista[2]) ** 2) == ((lista[0]) ** 2) + ((lista[1]) ** 2):
		return "Los numeros son de un triangulo rectangulo"
