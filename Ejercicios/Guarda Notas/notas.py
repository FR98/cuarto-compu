notas = []
pre = "si"

while pre == "si":
	notas.append(int(input("Ingrese una nota: ")))
	pre = input("Desea ingresar una nota? si/no: ")

anotas = open("notas.txt", 'w')

for nota in notas:

	anotas.write(str(nota) + "\n")

anotas.close()