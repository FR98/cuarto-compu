import codecs
import random


file = codecs.open("listado-general.txt", "r", "utf-8")

todas_palabras = []
buenas_palabras = []

for word in file:

	if len(word) > 6:
		todas_palabras.append(word)


desea_continuar = True
while desea_continuar:

	i = random.randint(0, len(todas_palabras))
	word = todas_palabras[i]

	print(word)

	r = input("Esta palabra te gusta? ")
	if r == "s":
		buenas_palabras.append(word)

	desea_continuar = input("Continuar? ") == "s"

out_file = codecs.open("listado-general-limpio.txt", "a", "utf-8")

for word in buenas_palabras:
	out_file.write(word + "\r\n")

out_file.close()