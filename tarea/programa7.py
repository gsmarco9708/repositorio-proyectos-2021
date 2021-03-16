import sys
print("INGRESE UN NUMERO POSITIVO: ")
numero = int(input("NUMERO: "))
fac = numero
resta = fac - 1

def lectura():
	tex = open("PROGRAMA7.txt", "r")
	lectura = tex.read()
	print(lectura)
	tex.close()

def imprimir(a):

	print("EL FACTORAIL ES: " + str(a))
	texto = open("PROGRAMA7.txt", "a")
	texto.write("*********" + "\n"
	+ str(a) + "\n")
	texto.close()
	print("\n *** GUARDADO *** \n ")
	
	print("DESEA VER EL HISTORIAL? s/n")
	op = str(input("OPCION: "))
	if(op == 's'):
		lectura()
	else:
		print("SALIENDO")
		sys.exit()

if numero % 7 == 0:

	while resta >= 1:
		fac = fac*resta
		resta = resta - 1
	imprimir(fac)
else:
	print("EL NUMERO NO ES DIVISIBLE DENTRO DE 7")


