def prob_6 (lista):
	for a in range (len(lista)-1, 0, -1):
		for b in range (a):
			if lista[b] > lista[b+1]:
				c= lista[b]
				lista[b] = lista[b+1]
				lista[b+1] = c
	return lista