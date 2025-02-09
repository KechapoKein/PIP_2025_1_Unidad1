def main():
    perimetro = int(input("Ingresa el perimetro del pentagono: "))
    apotema = int(input("Ingresa la apotema del pentagono: "))

    area = (perimetro * apotema) // 2

    print(f"El area del pentagono es: {area}")

if __name__ == "__main__":
    main()
