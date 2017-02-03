class FiguraGeometrica(object):
	def __init__(self, base, altura):
		self.base = base
		self.altura = altura
	def imprimir(self):
		return ""
	def calcular_area(self):
		return self.base * self.altura
		