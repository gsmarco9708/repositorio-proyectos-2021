import sys

def imprimir(x, m, r):
	if(x == 1):
		f = "RENOVARSE"
	if(x == 2):
		f = "RECIBIR MANTENIMIENTO"
	if(x == 3):
		f = "OPTIMAS CONDICIONES"
	if(x == 4):
		f = "MECANICO"

	texto = open("taxi.txt", "a")
	texto.write("***************" + "\n" + "MODELO: " + str(m) + "\n" + "RECORRIDO: " + str(r) + "\n" + "ESTADO: " + f + "\n")
	texto.close()

def lectura():
	tex = open("taxi.txt", "r")
	lectura = tex.read()
	print(lectura)
	tex.close()

def mecanico(modelo,recorrido):
	
	if(modelo < 2007 and recorrido > 20000):
		print("DEBE RENOVARSE")
		x = 1
	elif( modelo >= 2007 and modelo <= 2013 and recorrido > 20000):
		print("RECIBIR MANTENIMIENTO")
		x = 2
	elif( modelo > 2013 and recorrido < 10000):
		print("OPTIMAS CONDICIONES")
		x = 3
	else:
		print("MECANICO")
		x = 4
	
	imprimir(x, modelo, recorrido)

def ingreso():
	a = int(input("INGRESE MODELO DEL CARRO: "))
	b = int(input("INGRESE RECORRDIO DEL VEHICULO: "))
	mecanico(a,b)

while True:

	print(""" 

		>>>>>>>>> 1) INGRESO TAXI
		>>>>>>>>> 2) VER HISTORIAL
		>>>>>>>>> 3) SALIR


		""")

	op = int(input("OPCION: "))
	if op == 1:
		ingreso()
	elif(op == 2):
		lectura()
	elif(op == 3):
		print("SALIENDO")
		sys.exit()
	else:
		print("INGRESE UNA OPCION CORRECTA")


	


	
