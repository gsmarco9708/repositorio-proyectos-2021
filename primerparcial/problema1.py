import sys
import psycopg2 as p

def guardad(a,b,c,d):
	conexion = p.connect(database = "PrimerParcial", user = "postgres", password = "sagastumeG9708")
	cursor1 = conexion.cursor()
	sql = "insert into Datos(GENERO, CANTIDAD, PROMEDIO_PESO, PROMEDIO_ALTURA) values (%s,%s,%s,%s)"
	dato = (a, str(b), str(c), str(d))
	cursor1.execute(sql, dato)
	conexion.commit()

def dato():
	try:
		cantidad = int(input("INGRESE CANTIDAD DE PERSONAS: "))
	except:
		print("INGRESE UN VALOR ADECUADO!!!!")
	try:
		peso = float(input("INGRESE EL PESO: "))
		altura = float(input("INGRESE ALTURA: "))
		peso2 = float(input("INGRESE EL PESO: "))
		altura2 = float(input("INGRESE ALTURA: "))
		peso3 = float(input("INGRESE EL PESO: "))
		altura3 = float(input("INGRESE ALTURA: "))
	except:
		print("INGRESE VALORES ADECUADOS!!!! ")

	try:
		genero = str(input("INGRESE GENERO: "))
	except:
		print("INGRESE LETRAS NO NUMEROS!!!!")

	if(genero == 'M' or genero == 'm'):
		pesot= peso2 + peso3 + peso
		alturat= altura + altura2 +  altura3
		print("CANTIDAD DE HOMBRES: " + str(cantidad))
		

	if(genero == 'F' or genero == 'f'):
		pesot= peso2 + peso3 + peso
		alturat= altura + altura2 +  altura3
		print("CANTIDAD DE MUJERES: " + str(cantidad))
			
	propeso = pesot/cantidad
	proaltura = alturat / cantidad
	print("PROMEDIO ALTURA: " + str(proaltura))
	print("PROMEDIO PESO: " + str(propeso))
	guardad(genero, cantidad, propeso, proaltura)
	
while True:

	print(""" 

	>>>>>>>>>>>>>> (1) INGRESO DE DATOS
	>>>>>>>>>>>>>> (2) HISTORIAL
	>>>>>>>>>>>>>> (3) SALIR

""")

	try:
		op = int(input("OPCION: "))
	except:
		print("INGRESE NUMERO DE OPCION VALIDO")
		op = '?'

	if op == 1:
		dato()
	elif op == 2:
		leer()
	elif op == 3:
		print("SALIENDO")
		sys.exit()
	else:
		print("INGRESE UNA OPCION CORRECTA")