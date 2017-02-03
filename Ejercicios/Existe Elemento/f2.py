def f2(n1, lista):
	if n1 == lista[0]:
		return True

	if n1 != lista[0]:
		return f2(n1, lista[1:])