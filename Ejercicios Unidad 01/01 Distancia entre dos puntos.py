import math

def main():
    x1 = float(input("Ingresa la coordenada X del primer punto: "))
    y1 = float(input("Ingresa la coordenada Y del primer punto: "))
    x2 = float(input("Ingresa la coordenada X del segundo punto: "))
    y2 = float(input("Ingresa la coordenada Y del segundo punto: "))

    distancia = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

    print(f"La distancia entre los dos puntos es: {distancia}")

if __name__ == "__main__":
    main()
