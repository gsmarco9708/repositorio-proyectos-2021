n = 1
impar = 0
suma = 0
def imprimir(a):
	texto = open("HISTORIAL.txt", "a")
	texto.write("*********" + "\n"
	+ str(a) + "\n")
	texto.close()

while impar < 100:
	impar = (2*n)-1
	n = n + 1
	print(str(impar), end=" ")
	imprimir(impar)
	try:
		impar = (2*n)-1
		suma = suma + 1
	except:
		pass

print("\n" + "LA CANTIDAD DE NUMEROS IMPERES ES: " + str(suma))
print("\n GUARDADO \n")
print("DESEA VER EL HISTORIAL? SI/NO")
opcion = str(input("OPCION: "))
if(opcion == 'si'):
	f = open('HISTORIAL.txt','r')
	mensaje = f.read()
	print(mensaje)
	f.close()

