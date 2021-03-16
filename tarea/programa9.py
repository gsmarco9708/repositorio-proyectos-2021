print("INGRESE PRIMER NUMERO: ")
num1 = int(input())
print("INGRESE SEGUNDO NUMERO: ")
num2 = int(input())

if(num1 > num2):
	print( "EL PRIMERO NUMERO ES MAYOR")
	while num1 >= num2:
		print("SUSECION: "+str(num1))
		num1 = num1-1
else:
	print("EL SEGUNDO NUMERO ES MAYOR")
	while num2 >= num1:
		print("SUSECION: " + str(num2))
		num2 = num2 - 1

