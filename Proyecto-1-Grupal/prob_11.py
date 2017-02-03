def prob_11 (frase):
	separar = frase.split()
	sinEspacios = "".join(separar)
	reversa = sinEspacios[::-1]
	if sinEspacios == reversa:
		return "Si es palindromo"
	else:
		return "No es palindromo"

