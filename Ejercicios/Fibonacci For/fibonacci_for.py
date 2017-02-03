def fibonacci_for(n):
	lista = [1,1]
	if n == 0:
		return 0
	else:
		for i in range (n):
			lista.append(lista[i] + lista[i+1])
		return lista[n]
	input()