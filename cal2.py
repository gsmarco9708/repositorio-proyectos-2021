import psycopg2 as p


def sumar(): 
    x = a + b
    print (("RRESULTADO: "), (x))
    print("\n")
    conexion1 = p.connect(database="Bitacora", user="postgres", password="sagastumeG9708")
    cursor1=conexion1.cursor()
    sql="insert into Datos(operacion,numero1,numero2,resultado) values (%s,%s,%s,%s)"
    datos = ('SUMA',str(a),str(b), str(x))
    cursor1.execute(sql, datos)
    conexion1.commit()


def restar():#Definimos la función restar
    x = a - b
    print (("RRESULTADO: "), (x))
    print("\n")
    conexion1 = p.connect(database="Bitacora", user="postgres", password="sagastumeG9708")
    cursor1=conexion1.cursor()
    sql="insert into Datos(operacion,numero1,numero2,resultado) values (%s,%s,%s,%s)"
    datos = ('RESTA',str(a),str(b), str(x))
    cursor1.execute(sql, datos)
    conexion1.commit()


def multiplicar():#Definimos la función multiplicar
    x = a * b
    print (("RRESULTADO: "), (x))
    print("\n")
    conexion1 = p.connect(database="Bitacora", user="postgres", password="sagastumeG9708")
    cursor1=conexion1.cursor()
    sql="insert into Datos(operacion,numero1,numero2,resultado) values (%s,%s,%s,%s)"
    datos = ('MULTIPLICACION',str(a),str(b), str(x))
    cursor1.execute(sql, datos)
    conexion1.commit()

def dividir():#Definimos la función dividir
    if(b == 0):
        print("¡¡¡¡¡¡¡¡¡ LA  OPERACION NO SE PUEDE RALIZAR !!!!!!!!!")
    else:
        x = a / b
        print (("RRESULTADO: "), (x))
        print("\n")
        conexion1 = p.connect(database="Bitacora", user="postgres", password="sagastumeG9708")
        cursor1=conexion1.cursor()
        sql="insert into Datos(operacion,numero1,numero2,resultado) values (%s,%s,%s,%s)"
        datos = ('DIVISION',str(a),str(b), str(x))
        cursor1.execute(sql, datos)
        conexion1.commit()

while True: #Creamos un bucle
    try: #Intentamos obtener los datos de entrada
        a = float(input("\n INGRESE PRIMER NUMERO: \n")) #Solicitamos el 1er numero 
        b = float(input("\n INGRESE SEGUNDO NUMERO: \n"))#Solicitamos el 2do numero 
        print (("QUE OPERACION DESEA REALIZAR ENTRE"), (a), ("Y"), (b), ("?\n")) 
        op = str(input(""" SELECCIONE UNA DE LAS SIGUIENTES OPCIONES: 
        1 >>>>>>> SUMA
        2 >>>>>>> RESTA
        3 >>>>>>> MULTIPLICACION
        4 >>>>>>> DIVISION
        5 >>>>>>> SALIR \n"""))
        
    except: #Error
        print ("¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡ INGRESE UN VALOR CORRECTO !!!!!!!!!!!!!!!!!!!!!")
        op = '?'

    if op == '1':#Si el usuario elige opción 1 llamamos a sumar
        sumar()
        #break
    elif op == '2':#Si el usuario elige opción 1 llamamos a restar
        restar()
        #break
    elif op == '3':#Si el usuario elige opción 1 llamamos a multiplicar
        multiplicar()
        #break
    elif op == '4':#Si el usuario elige opción 1 llamamos a dividir
        dividir()
        #break
    elif op == '5':
        break
    else:
        print ("""!!!!!!!!!!!!!!!!! INGRESE UNA OPCION VALIDA ¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡""") 






