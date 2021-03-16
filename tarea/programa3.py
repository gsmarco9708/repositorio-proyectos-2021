
palabra = str(input("INGRESE UNA PALABRA: "))
suma = 0
for letra in palabra:
    if((letra == 'a' or letra == 'A') or (letra == 'e' or letra == 'E') or (letra == 'i' or letra == 'I') or (letra == 'o' or letra == 'O') or (letra == 'u' or letra == 'U')):
    	suma = suma + 1
 
print("TOTAL DE VOCALES: " + str(suma))
