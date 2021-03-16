import sys
import math

def guardar(x, y):
	if(y == 1):
		f = "CIRCULO"
	if(y == 2):
		f = "CUADRADO"
	if(y == 3):
		f = "RECTANGULO"
	if(y == 4):
		f = "TRIANGULO"

	texto = open("AREAS.txt", "a")
	texto.write("***************" + "\n" "FIGURA: " + f + "\n" + "AREA: " + str(x) + "\n" )
	texto.close()
	
def circulo(a,b):
	area = ((2*math.pi)*(a*a))
	print("EL AREA ES: " + str(area) + "\n")
	guardar(area,b)

def cuadrado(a,b):
	area = a*a
	print("EL AREA ES: " + str(area) + "\n")
	guardar(area,b)
	
def rectangulo(a,b,c):
	area = a*b
	print("EL AREA ES: " + str(area) + "\n")
	guardar(area,c)

def triangulo(a,b,c):
	area = (1/2)*a*b
	print("EL AREA ES: " + str(area) + "\n")
	guardar(area,c)

def lectura():
	tex = open("AREAS.txt", "r")
	lectura = tex.read()
	print(lectura)
	tex.close()
	
def menu(figura):

	if(figura == 1):
			
		r = float(input("INGRESE EL RADIO DEL CIRCULO: "))
		circulo(r,figura)

	elif(figura == 2):
		
		lado = float(input("INGRESE EL VALOR DEL LADO: "))
		cuadrado(lado, figura)

	elif(figura == 3):
		
		lado1 = float(input("INGRESE EL VALOR DEL LADO 1: "))
		lado2 = float(input("INGRESE EL VALOR DEL LADO 2: "))
		rectangulo(lado1, lado2, figura)

	elif(figura == 4):
		
		base = float(input("INGRESE EL VALOR DEL LA BASE: "))
		altura = float(input("INGRESE EL VALOR DE LA ALTURA: "))
		triangulo(base, altura, figura)

	elif(figura == 5):
		lectura()

	elif(figura == 6):
		print("***** SALIENDO *****")
		sys.exit()
	else:
		print("INGRESE UNA OPCION VALIDA")
		
while True:
	print(""" \n SELECCIONE LA FIGURA A LA QUE DESEA CALCULAR EL AREA:

	>>>>>>>>>>     (1) CIRCULO
	>>>>>>>>>>     (2) CUADRADO
	>>>>>>>>>>     (3) RECTANGULO
	>>>>>>>>>>     (4) TRIANGULO

	>>>>>>>>>>     (5) HISTORIAL
	>>>>>>>>>>     (6) SALIR

	\n """)

	op = int(input("OPCION: "))
	print("\n")
	menu(op)
	
