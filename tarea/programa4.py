numero = int(input("INGRESE UN NUMERO: "))
suma = numero
resta = numero - 1

while resta > 0:
	suma = suma + resta
	resta = resta - 1

print("LA SUMA DE SUS NUMEROS CONSECUTIVOS ES: " + str(suma))
	
	
