class Robot(object):
	def __init__(self):
		self.x = None
		self.y = None
		self.direccion = "^"
		self.fichas_recogidas = 0
		self.mapa = None

	def asignar_mapa(self, objeto_mapa):
		self.mapa = objeto_mapa

	def buscar_robot(self):
		for y in range(len(self.mapa.mapa)):
			for x in range(len(self.mapa.mapa[y])):
				if (self.mapa.mapa[y][x] == "^") or (self.mapa.mapa[y][x] == "v") or (self.mapa.mapa[y][x] == "<") or (self.mapa.mapa[y][x] == ">"):
					self.x = x #Guarda la ubicacion del robot
					self.y = y #Guarda la ubicacion del robot
					self.direccion = self.mapa.mapa[y][x] #Guarda la direccion del robot
					self.mapa.mapa[y][x] = "0" #Borra la posicion inicial del robot

	def MOVE(self):
		if (self.direccion == "^" and self.y != 0):
			self.y -= 1
		elif (self.direccion == ">" and self.x != (self.mapa.largo - 1)):
			self.x += 1
		elif (self.direccion == "v" and self.y != (self.mapa.alto - 1)):
			self.y += 1
		elif (self.direccion == "<" and self.x != 0):
			self.x -= 1

	def ROTATE(self):
		if (self.direccion == "^"):
			self.direccion = ">"
		elif (self.direccion == ">"):
			self.direccion = "v"
		elif (self.direccion == "v"):
			self.direccion = "<"
		elif (self.direccion == "<"):
			self.direccion = "^"

	def PICK(self):
		if self.mapa.fichas_posicion_actual > 0:
			self.fichas_recogidas += 1 #Aumenta el conteo de fichas recogidas
			self.mapa.fichas_posicion_actual -= 1 #Resta el numero de fichas en el mapa
		self.mapa.mapa[self.y][self.x] = str(self.mapa.fichas_posicion_actual) #Cambia el numero de fichas en el mapa