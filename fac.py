from datetime import datetime

now = datetime.now()
num = int(input("\n" + "INGRESE UN NUMERO: "))
fac = num
resta = fac - 1

def imprimir(a):

	print("\n" + "NUMERO: "+ str(num) + "\n" + "FACTORIAL: " + str(a))
	fecha = now.date()
	hora = now.time()

	texto = open("FACTORIAL.txt", "a")
	texto.write("********************************************************************" + "\n"
	+ "NUMERO: " + str(num) + "\n" s
	+ "FACTORIAL: " + str(a) + "\n" + "FECHA: " + str(fecha)
	+ "\n" + "HORA: " + str(hora) + "\n")

	texto.close()

	print("\n GUARDADO \n")


while resta >= 1:
	
	fac = fac*(resta)
	resta = resta - 1
imprimir(fac)
	

	

	




	



	




