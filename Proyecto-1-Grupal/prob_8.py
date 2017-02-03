
def prob_8(altura):
	cont = altura
	resultado = ""
	while cont > 0:
		for i in range(0, altura):
			resultado += (" "*(altura-i-1) + "* " * (i+1) + "\n")
			cont = cont - 1
	return resultado		