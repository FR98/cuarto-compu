def prob_12(num): 
	
	#Separar cifras.
	a = num % 10 #Unidades
	b = ((num % 100) - (num % 10)) // 10 #Decenas
	c = ((num % 1000) - (num % 100)) // 100	#Centenas
	d = ((num % 10000) - (num % 1000)) // 1000 #Mil

	if num <= 1000 and num >= 0:

		#Para mil.
		if d == 0:
			res= ("")
		elif d == 1:
			res= ("One thousand")

		#Para centenas. 
		if c == 0:
			res2= ("")
		elif c == 1:
			res2= ("one hundred ")
		elif c == 2:
			res2= ("two hundred ")	
		elif c == 3:
			res2= ("three hundred ")	
		elif c == 4:
			res2= ("four hundred ")
		elif c == 5:
			res2= ("five hundred ")
		elif c == 6:
			res2= ("six hundred ")
		elif c == 7:
			res2= ("seven hundred ")
		elif c == 8:
			res2= ("eight hundred ")
		elif c == 9:
			res2= ("nine hundred ")

		#Para decenas si hay centenas.	
		if c != 0 and b != 1:
			if b == 0:
				res3= ("")
			elif b == 2:
				res3= ("and twenty ")
			elif b == 3:
				res3= ("and thirty ")
			elif b == 4:
				res3= ("and fourty ")
			elif b == 5:
				res3= ("and fifty ")
			elif b == 6:
				res3= ("and sixty ")
			elif b ==7:
				res3= ("and seventy ")
			elif b == 8:
				res3= ("and eighty ")
			elif b == 9:
				res3= ("and ninety ")
		

		#Para decenas si no hay centenas.
		if c == 0 and b != 1: 
			if b == 0:
				res3= ("")	
			elif b == 2:
				res3= ("twenty ")
			elif b == 3:
				res3= ("thirty ")
			elif b == 4:
				res3= ("fourty ")
			elif b == 5:
				res3= ("fifty ")
			elif b == 6:
				res3= ("sixty ")
			elif b ==7:
				res3= ("seventy ")
			elif b == 8:
				res3= ("eighty ")
			elif b == 9:
				res3= ("ninety ")		

		#Para decenas si la decena es 1 y hay centenas.		
		elif b == 1 and c != 0:
			if a == 0:
				res3= ("and ten.")
			elif a == 1:
				res3= ("and eleven.")
			elif a == 2:
				res3= ("and twelve.")
			elif a == 3:
				res3= ("and thirteen.")	
			elif a == 4:
				res3= ("and fourteen.")
			elif a == 5:
				res3= ("and fifteen.")
			elif a == 6:
				res3= ("and sixteen.")
			elif a == 7:
				res3= ("and seventeen.")
			elif a == 8:
				res3= ("and eighteen.")
			elif a == 9:
				res3= ("and nineteen.")

		#Para decenas si la decena es 1 y no hay centenas.		
		elif b == 1 and c == 0:
			if a == 0:
				res3= ("ten.")
			elif a == 1:
				res3= ("eleven.")
			elif a == 2:
				res3= ("twelve.")
			elif a == 3:
				res3= ("thirteen.")	
			elif a == 4:
				res3= ("fourteen.")
			elif a == 5:
				res3= ("fifteen.")
			elif a == 6:
				res3= ("sixteen.")
			elif a == 7:
				res3= ("seventeen.")
			elif a == 8:
				res3= ("eighteen.")
			elif a == 9:
				res3= ("nineteen.")	

		#Para unidades si la decena no es uno ni cero.		
		if b != 1 and b != 0:		
			if a == 0:
				res4= (".")
			elif a == 1:
				res4= ("one.")
			elif a == 2:
				res4= ("two.")
			elif a == 3:
				res4= ("three.")
			elif a == 4:
				res4= ("four.")
			elif a == 5:
				res4= ("five.")
			elif a == 6:
				res4= ("six.")
			elif a == 7:
				res4= ("seven.")
			elif a == 8:
				res4= ("eight.")
			elif a == 9:
				res4= ("nine.")

		#Para las unidades si la decena es cero y hay centenas.		
		elif b == 0 and c != 0:
			if a == 0:
				res4= (".")
			elif a == 1:
				res4= ("and one.")
			elif a == 2:
				res4= ("and two.")
			elif a == 3:
				res4= ("and three.")
			elif a == 4:
				res4= ("and four.")
			elif a == 5:
				res4= ("and five.")
			elif a == 6:
				res4= ("and six.")
			elif a == 7:
				res4= ("and seven.")
			elif a == 8:
				res4= ("and eight.")
			elif a == 9:
				res4= ("and nine.")	

		#Para las unidades si no hay decena ni centena. 		
		elif b == 0 and c == 0:
			if a == 0:
				res4= (".")
			elif a == 1:
				res4= ("one.")
			elif a == 2:
				res4= ("two.")
			elif a == 3:
				res4= ("three.")
			elif a == 4:
				res4= ("four.")
			elif a == 5:
				res4= ("five.")
			elif a == 6:
				res4= ("six.")
			elif a == 7:
				res4= ("seven.")
			elif a == 8:
				res4= ("eight.")
			elif a == 9:
				res4= ("nine.")		

		#Para la unidad si la decena es 1.
		elif b == 1:
			res4= ""	

		return(res + res2 + res3 + res4)

	else:
		return ("Error, el numero debe ser menor o igual que 1000.")
