from radio import Radio

objeto_radio = Radio(input("Ingrese una marca: "))

desea_continuar = True

while desea_continuar:

	print ("Marca: ", objeto_radio.marca)
	print ("Encendido: ", objeto_radio.encendido)
	print ("Volumen: ", objeto_radio.volumen)
	print ("Fm: ", objeto_radio.en_fm)
	print ("Emisora AM: ", objeto_radio.emisora_am)
	print ("Emisora FM: ", objeto_radio.emisora_fm)

	if objeto_radio.encendido == False:
		opcion = int(input(("1. Encender: ")))
		if opcion == 1:
			objeto_radio.encender()
	if objeto_radio.encendido == True:
		opcion2 = int(input(("""
	1. Apagar 
	2. Subir Volumen
	3. Bajar Volumen
	4. Cambiar Frecuencia
	5. Subir Emisora
	6. Bajar Emisora
""")))
		if opcion2 == 1:
			objeto_radio.apagar()
			desea_continuar = input("Desea continuar? si/no ")
			if desea_continuar == "no":
				desea_continuar = False
		elif opcion2 == 2:
			objeto_radio.subir_volumen()
		elif opcion2 == 3:
			objeto_radio.bajar_volumen()
		elif opcion2 == 4:
			objeto_radio.cambiar_frecuencia()
		elif opcion2 == 5:
			objeto_radio.subir_emisora()
		elif opcion2 == 6:
			objeto_radio.bajar_emisora()

