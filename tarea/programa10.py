a = 0
e = 0
i = 0
o = 0
u = 0
def imprimir(a,e,i,o,u):

	print("CANTIDAD DE VOCALES: ")
	print("A = " + str(a))
	print("E = " + str(e))
	print("I = " + str(i))
	print("O = " + str(o))
	print("U = " + str(u))

print("INGRESE UNA PALABRA: " + "\n")
try:
	palabra = str(input())
except:
	print("INGRESE LETRAS NO NUMEROS NI CARACTERES")

print("PALBRA INGRESADA: " + palabra)

for letra in palabra:
	if(letra == 'a' or letra == 'A'):
		a = a + 1
	if(letra == 'e' or letra == 'E'):
		e = e + 1
	if(letra == 'i' or letra == 'I'):
		i = i + 1
	if(letra == 'o' or letra == 'O'):
		o = o + 1
	if( letra == 'u' or letra == 'U'):
		u = u + 1
	
imprimir(a,e,i,o,u)