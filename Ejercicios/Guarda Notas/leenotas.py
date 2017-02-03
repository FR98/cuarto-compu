anotas = open("notas.txt",'r')

lineas = anotas.readlines()

for leer in lineas:
	print (leer)

anotas.close()

input()