import sys

escaleno = "ESCALENO"
equilatero = "EQUILATERO"
isosceles = "ISOSCELES"

def imprimir(a):
	h = open('HTRIANGULOS.txt','a')
	mensaje = h.write("\n"+ "*****************" + "\n"+ "TRIANGULO: " + str(a))
	print(mensaje)
	h.close()

def lectura():
	f = open('HTRIANGULOS.txt','r')
	men = f.read()
	print(men)
	f.close()

def figura():
	if(lado1 == lado2 and lado1 == lado3 and lado2 == lado3):
		print("A INGRESA UN TRIANGULO: " + equilatero)
		imprimir(equilatero)
	elif(lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
		print("A INGRESA UN TRIANGULO: " + isosceles)
		imprimir(isosceles)
	else:
		print("A INGRESADO UN TRIANGULO: " + escaleno)
		imprimir(escaleno)

	print("DESEA CONSULTAR EL HOSTORIA? s/n")
	opcion = str(input("OPCION: "))
	if(opcion == 's'):
		lectura()
	if(opcion == 'n'):
		print("SALIENDO")
		sys.exit()

print("*********** INGRESE LOS LADOS DEL TRIANGULO, NUMEROS ENTEROS POSITIVOS **********" + "\n")

try:
	lado1=float(input("LADO 1: "))
	lado2=float(input("LADO 2: "))
	lado3=float(input("LADO 3: "))

except:
	print("INGRESE UN VALOR ENTERO!!")

figura()










 