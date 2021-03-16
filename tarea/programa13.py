import sys

def escribir(a,b):

	texto = open("AÑO.txt", "a")
	texto.write("***************" + "\n" "AÑO: " + str(a) + "\n" + "ESTADO: "  + b + "\n" )
	texto.close()

def lectura():
	tex = open("AÑO.txt", "r")
	lectura = tex.read()
	print(lectura)
	tex.close()

def calculo():
	x = " "
	ano = int(input("INGRESE SU AÑO DE NACIMIENTO: "))

	if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):

		print("ES BISISESTO")
		x = "BISISESTO"
	else:
		print("NO ES BISIESTO")
		x = "NO BISIESTO"

	escribir(ano, x)

while True:
	print(""" 

		SELECCIONE UNA OPCION

		>>>>>>> (1) INGRESAR AÑO
		>>>>>>> (2) HISTORIAL
		>>>>>>> (3) SALIR

		""")
	op = int(input("OPCION: "))

	if(op == 1):
		calculo()
	elif(op == 2):
		lectura()
	elif(op == 3):
		print("SALIENDO")
		sys.exit()
	else:
		print("INGRESE UNA OPCION VALIDA")

	


	
