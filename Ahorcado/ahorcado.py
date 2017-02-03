from funciones_ahorcado import palabras, muneco, ganarPerder
import random

print ("Ahorcado")
num = random.randrange(0, 99)
palabra = palabras(num)
#print (palabra) #innecesario
print (len(palabra) * "_ ")

lpalabra = list(palabra)
espacios = list(len(palabra) * "_")
dibujo = 0

while dibujo < 7 and espacios != lpalabra:
	letra = input("Ingrese una letra: ")
	
	if letra in palabra:
		for cont in range(len(lpalabra)): #Cambia el espacio vacio por la letra acertada.
			if lpalabra[cont] == letra:
				espacios[cont] = letra
		
		print (" ".join(espacios))
		print ("")

	else:
		print (muneco(dibujo))
		dibujo = dibujo + 1

		print (" ".join(espacios))
		print ("")

print (ganarPerder(espacios, lpalabra, dibujo, palabra))