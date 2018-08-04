from utilidades import cargar_mapa, cargar_instrucciones
from mapa import Mapa
from robot import Robot
import time

nombre_mapa = "mapas/" + (input("Ingrese el nombre del mapa: ")) + ".txt"
el_mapa = cargar_mapa(nombre_mapa)

nombre_instrucciones = "instrucciones/" + (input("Ingrese el nombre de las instrucciones: ")) + ".txt"
instrucciones = cargar_instrucciones(nombre_instrucciones)

objeto_mapa = Mapa(el_mapa) #Crea el objeto Mapa
objeto_robot = Robot() #Crea el objeto Robot
objeto_mapa.asignar_robot(objeto_robot) #Asigna robot a mapa
objeto_robot.asignar_mapa(objeto_mapa) #Asigna mapa a robot
objeto_robot.buscar_robot() #Busca el robot
print()
print("Robot: ", objeto_robot.x, ",", objeto_robot.y, objeto_robot.direccion) #Imprime posicion y direccion del robot
print(objeto_mapa.imprimir_mapa())
print()
for instruccion in instrucciones:
	print(instruccion)
	
	if instruccion == "MOVE":
		objeto_robot.MOVE()
		#print(objeto_mapa.imprimir_mapa())
		objeto_mapa.fichas_posicion_robot()
		if objeto_mapa.fichas_posicion_actual > 0:
			print("Fichas en el lugar: ", objeto_mapa.fichas_posicion_actual)
	elif instruccion == "ROTATE":
		objeto_robot.ROTATE()
		#print(objeto_mapa.imprimir_mapa())
	elif instruccion == "PICK":
		objeto_robot.PICK()
		#print(objeto_mapa.imprimir_mapa())
		print("Fichas en el lugar: ", objeto_mapa.fichas_posicion_actual)
		print("Fichas recogidas: ", objeto_robot.fichas_recogidas)
	else:
		print("INSTRUCCION NO VALIDA!")
	print(objeto_mapa.imprimir_mapa())
	print()
	time.sleep(1)

print()
print("Robot: ", objeto_robot.x, ",", objeto_robot.y, objeto_robot.direccion) #Imprime posicion y direccion del robot
print("Fichas recogidas: ", objeto_robot.fichas_recogidas)