def prob_4(palabra, longparra):
	lista = list(palabra)
	longi = len(lista)
	parte1 = ("*" * ((longparra - longi) // 2))
	return parte1 + palabra + parte1