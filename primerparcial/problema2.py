import numpy as np
import sys
import psycopg2 as p

def cono():
	try:
		radio = float(input("INGRESE EL RADIO DEL CONO: "))
		a = float(input("INGRESE ALTURA DEL CONO: "))
		g = float(input("INGRESE LA GENERATRIZ DEL CONO: "))
	except:
		print("INGRESE VALORES CORRECTOS")

	base = 2* np.pi*radio*radio
	print("AREA DE BASE: " + str(base))

	lateral = (np.pi*radio*g)
	print("AREA LATERAL: " + str(lateral))

	total = base + (np.pi*radio*g)
	print("AREA TOTAL: " + str(total))

	v = (np.pi*a*radio*radio)/3
	print("VOLUMEN DEL CONO: " + str(v) + "cm^3")
	guardad(radio, a, g, base, lateral, total, v)

def guardad(a,b,c,d,e,f,g):
	conexion = p.connect(database = "PrimerParcial", user = "postgres", password = "sagastumeG9708")
	cursor1 = conexion.cursor()
	sql = "insert into Cono(RADIO, ALTURA, GENERATRIZ, AREA_BASE, AREA_LATERAL, AREA_TOTAL, VOLUMEN) values (%s,%s,%s,%s,%s,%s,%s)"
	dato = (str(a), str(b), str(c), str(d), str(e), str(f), str(g))
	cursor1.execute(sql, dato)
	conexion.commit()

while True:
	print("""
		>>>>>>>>>> (1) DATOS CONO
		>>>>>>>>>> (2) SALIR
		""")
	op = int(input("OPCION: "))
	if op == 1:
		cono()
	elif op == 2:
		print("SALIENDO")
		sys.exit()
	else:
		print("INGRESE UNA OPCION CORRECTA")

