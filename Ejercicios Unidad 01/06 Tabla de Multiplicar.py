def main():
    numero = int(input("Ingresa un numero a multiplicar: "))

    print(f"Tabla del {numero} :")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

if __name__ == "__main__":
    main()
