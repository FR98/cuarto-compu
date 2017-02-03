from figura import FiguraGeometrica

class Cuadrado(FiguraGeometrica):

	def __init__(self, lado):
		super().__init__(lado, lado)

	# override
	def imprimir(self):
		resultado = ""

		for i in range(self.altura):
			resultado += "* " * (self.base) + "\n"
		return resultado