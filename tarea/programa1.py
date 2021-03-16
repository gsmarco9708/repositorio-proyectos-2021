while True:	
	try:
		num1 = int(input("\nINGRESE PRIMER NUMERO: \n"))
		num2 = int(input("\nINGRESE SEGUNDO NUMERO: \n"))
		num3 = int(input("\n INGRESE TERCEER NUMERO: \n"))
	except:

		print("INGRESE UN NUMERO ENTERO!")

	if(num1 == num2 and num1 == num3 and num2 == num3):
		print("TODOS LOS NUMEROS SON IGUALES")

	else:

		if(num1 > num2 and num1 > num3):
			suma = num1 + num2 + num3
			print("SUMA TOTAL: " + str(suma))
		if(num2 > num1 and num2 > num3):
			mul = num1*num2*num3
			print("MULTIPLICACION TOTAL: " + str(mul))
		if(num3 > num1 and num3 > num2):
			print("CONCATENACION: "+ " " +str(num1) + " " +str(num2) + " " +str(num3))
		if (num1 == num2):
			print("EN UNICO NUMERO DIFERENTE ES: " + str(num3))
		elif num1 == num3:
			print("EN UNICO NUMERO DIFERENTE ES: " + str(num2))
		elif num2 == num3:
			print("EN UNICO NUMERO DIFERENTE ES: " + str(num1))
		else:
			pass

