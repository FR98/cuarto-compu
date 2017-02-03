class Radio():
	def __init__(self, marca):
		self.marca = marca
		self.encendido = False
		self.volumen = 0
		self.en_fm = True
		self.emisora_am = 300
		self.emisora_fm = 87.0

	def encender(self):
		self.encendido = True
	def apagar(self):
		self.encendido = False
	def subir_volumen(self):
		if self.volumen >= 100:
			self.volumen = 100
		else:
			self.volumen += 5
	def bajar_volumen(self):
		if self.volumen <= 0:
			self.volumen = 0
		else:
			self.volumen -= 5	
	def cambiar_frecuencia(self):
		self.en_fm = not self.en_fm
	def subir_emisora(self):
		if self.en_fm == True:
			if self.emisora_fm >= 107.0:
				self.emisora_fm = 87.0
			else:
				self.emisora_fm += 0.5
		else:
			if self.emisora_am >= 1300:
				self.emisora_am = 300
			else:
				self.emisora_am += 40
	def bajar_emisora(self):
		if self.en_fm == True:
			if self.emisora_fm <= 87.0:
				self.emisora_fm = 107.0
			else:
				self.emisora_fm -= 0.5
		else:
			if self.emisora_am <= 300:
				self.emisora_am = 1300
			else:
				self.emisora_am -= 40
