from cuadrado import Cuadrado
from triangulo import Triangulo

menu1 = int(input("""
	1. Crear Figura
	2. Salir
Eleccion: """))

while menu1 != 2 and menu1 == 1:
	figura = int(input("""
	1. Cuadrado
	2. Triangulo
	3. Salir
Eleccion: """))

	if figura == 1:
		mi_cuadrado = Cuadrado(int(input("Ingrese el lado: ")))
		opc = int(input("""
	1. Calcular Area
	2. Imprimir
	3. Crear otra figura
Eleccion: """))	
		if opc == 1:
			print ("El area es: ", mi_cuadrado.calcular_area())
			opc2 = int(input("1. Imprimir?" + "\n" + "2. No Imprimir" + "\n" + "Eleccion: "))
			if opc2 == 1:
				print (mi_cuadrado.imprimir())
		elif opc == 2:
			print (mi_cuadrado.imprimir())
			opc2 = int(input("1. Area?" + "\n" + "2. No Imprimir" + "\n" + "Eleccion: "))
			if opc2 == 1:
				print ("El area es: ", mi_cuadrado.calcular_area())
		elif opc == 3:
			menu1 = 1
		else:
			print("Error")
			menu1 = 2

	if figura == 2:
		mi_triangulo = Triangulo((int(input("Ingrese la base: "))), (int(input("Ingrese la altura: "))))
		opc = int(input("""
	1. Calcular Area
	2. Imprimir
	3. Crear otra figura
Eleccion: """))	
		if opc == 1:
			print ("El area es: ", mi_triangulo.calcular_area())
			opc2 = int(input("1. Imprimir?" + "\n" + "2. No Imprimir" + "\n" + "Eleccion: "))
			if opc2 == 1:
				print (mi_triangulo.imprimir())
		elif opc == 2:
			print (mi_triangulo.imprimir())
			opc2 = int(input("1. Area?" + "\n" + "2. No Imprimir" + "\n" + "Eleccion: "))
			if opc2 == 1:
				print ("El area es: ", mi_triangulo.calcular_area())
		elif opc == 3:
			menu1 = 1
		else:
			print("Error")
			menu1 = 2

	if figura == 3:
		menu1 = 2