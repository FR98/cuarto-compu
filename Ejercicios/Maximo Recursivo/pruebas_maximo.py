from maximo import maximo

lista = []
pre = "si"
while pre == "si":
	n = int(input("Ingrese otro numero: "))
	lista.append(n)
	pre = input("Desea continuar? si/no ")

print ("El maximo de la lista es: ", maximo(lista))

input()