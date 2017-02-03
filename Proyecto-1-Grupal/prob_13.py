def prob_13(n):
	lista = [ ]
	for cont in range(1, n):
		if (n % cont == 0):
			lista.append(cont)

	suma = 0

	for i in lista:
		suma += i

	return "Divisores propios: ", lista, "Suma: ", suma