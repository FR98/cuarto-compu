class Mapa(object):
	def __init__(self, el_mapa):
		self.mapa = el_mapa
		self.largo = len(self.mapa[0])
		self.alto = len(self.mapa)
		self.robot = None
		self.fichas_posicion_actual = None

	def asignar_robot(self, objeto_robot):
		self.robot = objeto_robot		

	def imprimir_mapa(self):
		resultado = ""
		resultado += ("_" * self.largo + "\n")
		for i in range(self.alto):
			for j in range(len(self.mapa[i])):
				if j == self.robot.x and i == self.robot.y:
					resultado += self.robot.direccion
				elif self.mapa[i][j] == "0":
					resultado += (" ")
				else:
					resultado += (self.mapa[i][j])
			resultado += ("|" + "\n")
		resultado += ("-" * self.largo + "|")
		return resultado

	def fichas_posicion_robot(self):
		self.fichas_posicion_actual = int(self.mapa[self.robot.y][self.robot.x]) #Guarda la cantidad de fichas en la posicion actual del robot