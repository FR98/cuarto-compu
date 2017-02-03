def es_palindromo(palabra):
	cola = []
	pila1 = []
	pila = []

	for letra in palabra:
		pila1.append(letra)
		cola.append(letra)

	for i in pila1[0:]:
		pila.append(pila1.pop())

	print (cola)
	print (pila)

	if pila == cola:
		return True
	return False