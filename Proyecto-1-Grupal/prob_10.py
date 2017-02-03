import math

def prob_10(tu1, tu2, tu3):

	
	d1= math.sqrt( (((tu2[0]) - (tu1[0]))**2) + (((tu2[1]) - (tu1[1]))**2) )
	d2= math.sqrt( (((tu3[0]) - (tu2[0]))**2) + (((tu3[1]) - (tu2[1]))**2) )
	d3= math.sqrt( (((tu1[0]) - (tu3[0]))**2) + (((tu1[1]) - (tu3[1]))**2) )

	if d1 == d2 and d2 == d3:
		respuesta= ("Es un traingulo equilatero.")

	elif d1 == d2 and d2 != d3:
		respuesta= ("Es un triangulo isoceles.")

	elif d1 == d3 and d3 != d2:
		respuesta= ("Es un triangulo isoceles.")
		
	elif d2 == d3 and d3 != d1:
		respuesta= ("Es un triangulo isoceles.")			

	elif d1 != d2 and d2 != d3 and d1 != d3:
		respuesta= ("Es un triangulo escaleno.")	

	return respuesta	