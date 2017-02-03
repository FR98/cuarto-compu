def palabras(num):
	lista_palabras = ["arbol", "casa", "iguana", "pozo", "computadora", "lluvia", "monitor", "carro", "dinosaurio", "mesa", "comedor", "cocina", "tiburon", "zorro", "caballo", "perro", "gato", "cocodrilo", "cama", "popo", "camilla", "sueter", "pantalon", "collar", "falda", "maceta", "vestido", "rojo", "azul", "negro", "blanco", "azucar", "sal", "salida", "comida", "tamal", "pizza", "taco", "teclado", "amarillo", "dado", "murcielago", "escritorio", "poporopos", "palomitas", "soda", "gorila", "mango", "mambo", "motocicleta", "bicicleta", "castillo", "automovil", "princesa", "principe", "rey", "reina", "amaca", "playa", "arena", "nubes", "calzoneta", "luna", "estrellas", "sol", "planetas", "terremoto", "huracan", "fatiga", "remordimiento", "mujer", "bicentenario", "medallista", "sobrebarato", "billete", "alegrar", "recitador", "pamplina", "alfarero", "turborreactor", "asistencia", "fotonovela", "agencia", "disparada", "impresionar", "generatriz", "sentenciar", "vestimenta", "grosedad", "obseso", "apologico", "parlamentar", "criador", "mofeta", "coherencia", "fragmento", "seminarista", "adinerado", "minusvalidez", "lacteo"]
	return lista_palabras[num]
	
def muneco(dibujo):
	muneco = [
"""
  ___________
 |          |
 |
 |
 |
 | 
_|_""",

"""
  ___________
 |          |
 |         ( )
 |
 | 
 |
_|_""",
		
""" 
  ___________
 |          |
 |         ( )
 |          | 
 |
 | 
_|_""", 

""" 
  ___________
 |          |
 |         ( )
 |         /| 
 |
 | 
_|_""", 

"""
  ___________
 |          |
 |         ( )
 |         /|\ 
 |
 | 
_|_""", 
		
""" 
  ___________
 |          |
 |         ( )
 |         /|\ 
 |         / 
 |
_|_""", 
		
"""
  ___________
 |          |
 |         ( )
 |         /|\ 
 |         / \ 
 |
_|_"""]
	return muneco[dibujo]

def ganarPerder(espacios, lpalabra, dibujo, palabra):
	if espacios == lpalabra:
		return "Ganaste"
	if dibujo == 7:
		return "Perdiste, la palabra era: " + palabra