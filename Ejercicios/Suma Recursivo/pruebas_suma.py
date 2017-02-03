from suma import suma

lista = []
pre = "si"
while pre == "si":
	n = int(input("Ingrese otro numero: "))
	lista.append(n)
	pre = input("Desea continuar? si/no ")

print ("La suma es: ", suma(lista))

input()