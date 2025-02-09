def main():
    num = int(input("Ingresa un número entero positivo: "))

    if num >= 0:
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i

        print(f"El factorial de {num} es: {factorial}")

if __name__ == "__main__":
    main()
