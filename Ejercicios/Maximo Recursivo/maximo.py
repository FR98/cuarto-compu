def maximo(lista):
	if len(lista) == 1:
		return lista[0]

	if lista[0] > maximo(lista[1:]):
		return lista[0]
	else:
		return maximo(lista[1:])
