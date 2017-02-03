from f2 import f2

n1 = int(input("Ingrese un numero: "))

lista = []
pre = "si"

while pre == "si":
	n = int(input("Ingrese un numero para la lista: "))
	lista.append(n)
	pre = input("Desea continuar con la lista? ")

print (f2(n1, lista))