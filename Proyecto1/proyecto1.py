def prob_1(n):
	return n % 2 == 0

def prob_2(f):
	return (f-32)*(5/9)

def prob_3(base, potencia):
	for i in range (potencia-1):
		res = base * base
	return res

def prob_4(palabra, longparra):
	lista = list(palabra)
	longi = len(lista)
	parte1 = ("*" * ((longparra - longi) // 2))
	return parte1 + palabra + parte1

def prob_5(l1, l2):
	return [(l1[1] * l2[2] - l1[2] * l2[1]), (l1[2] * l2[0] - l1[0] * l2[2]), (l1[0] * l2[1] - l1[1] * l2[0])]