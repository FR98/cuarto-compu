from palindromo import es_palindromo

pre = "si"

while pre == "si":
	palabra = input("Ingrese una palabra: ")
	print(es_palindromo(palabra))
	pre = input("Desea continuar? ")