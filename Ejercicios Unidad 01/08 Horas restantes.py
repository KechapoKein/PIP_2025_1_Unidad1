def main():
    hora = int(input("Ingresa la hora actual en formato 24 horas (0-23): "))

    if 0 <= hora <= 23:
        horas_restantes = 24 - hora
        print(f"Quedan {horas_restantes} pa que se acabe el dia")

if __name__ == "__main__":
    main()
