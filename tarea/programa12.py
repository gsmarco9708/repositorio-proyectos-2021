import sys

def imprimir():
	
	tex = open("NOTAS.txt", "r")
	lectura = tex.read()
	print(lectura)
	tex.close()

def promedio(a,b,c):
	x = (a+b+c)/3
	print("PROMEDIO: " + str(x))
	apro = " "

	if(x >= 60):
		print("APROBADO")
		apro = "APROBADO"
	else:
		print("REPROBADO")
		apro = "REPROBADO"

	texto = open("NOTAS.txt", "a")
	texto.write("***************" + "\n" "PROMEDIO: " + str(x) + "\n" + "NOTA: "  + apro + "\n" )
	texto.close()

def notas():

	print("INGRESE NOTA 1: ")
	nota1 = float(input())

	print("INGRESE NOTA 2: ")
	nota2 = float(input())

	print("INGRESE NOTA 3: ")
	nota3 = float(input())

	promedio(nota1, nota2, nota3)

while True:
	print("""

		>>>>>>>> (1) INGRESAR NOTA
		>>>>>>>> (2) HISTORIAL
		>>>>>>>> (3) SALIR

		""")

	op = int(input("OPCION: "))

	if(op == 1):
		notas()
	elif(op == 2):
		imprimir()
	elif(op == 3):
		print("\n SALIENDO \n")
		sys.exit()
	else:
		print("INGRESE UNA OPCION VALIDA")
