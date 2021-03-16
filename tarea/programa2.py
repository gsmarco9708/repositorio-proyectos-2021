def main():
    print("********** DIVISORES **********")
    numero = int(input("INGRESE UN NUMERO MAYOR A CERO: "))

    if numero <= 0:
        print("ERROR!!!")
    else:
        print(f"DIVISORES DE {numero} SON:  ", end="")
        for i in range(1, numero + 1):
            if numero % i == False:
                print(i, end=" ")


if __name__ == "__main__":
    main()