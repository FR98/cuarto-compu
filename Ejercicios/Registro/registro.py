

estudiantes = {

}

pre = "si"

while pre == "si":
	menu = int(input("Escoja un numero: "  + "\n 1. Crear estudiante" + "\n 2. Ingresar notas" + "\n 3. Reporte de Notas" + "\n 4. Salir" + "\n "))
	if menu == 1:
		nombre = input("Ingrese el nombre del estudiante: ")
		estudiantes[nombre] = []
	

	if menu == 2:
		pre2 = "si"
		while pre2 == "si":
			print (estudiantes)
			est = input("Ingrese el nombre del estudiante a ingresar notas: ")
			nota = int(input("Ingrese la nota del estudiante: "))
			if nota >= 0 and nota <= 100:
				estudiantes[est] += [nota]
			else:
				print("Ingrese una nota valida")
			pre2 = input("Desea continuar? ")

	if menu == 3:
		name = input("Ingrese el nombre del estudiante que desea visualizar: ")
		print(estudiantes[name])
		suma = 0
		for i in (estudiantes[name]):
			suma += i
			promedio = suma/len(estudiantes[name])
		print ("Promedio: ", promedio)

	pre = input("Volver al menu? ")

	if menu == 4:
		pre = "no"