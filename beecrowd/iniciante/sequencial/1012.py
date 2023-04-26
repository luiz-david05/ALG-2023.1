def main():
    a , b , c = list(map(float, (input().split(" "))))

    area_triangulo, area_circulo, area_trapezio, area_quadrado, area_retangulo = calcular_area(a, b, c)

    print(f"TRIANGULO: {area_triangulo:.3f}")
    print(f"CIRCULO: {area_circulo:.3f}")
    print(f"TRAPEZIO: {area_trapezio:.3f}")
    print(f"QUADRADO: {area_quadrado:.3f}")
    print(f"RETANGULO: {area_retangulo:.3f}")


def calcular_area(a, b, c):
    area_triangulo = a * c / 2
    area_circulo = 3.14159 * c ** 2
    area_trapezio = (a + b) * c / 2
    area_quadrado = b ** 2
    area_retangulo = a * b

    return area_triangulo, area_circulo, area_trapezio, area_quadrado, area_retangulo


if __name__ == "__main__":
    main()
    
    # with open("1012.txt" , "r") as entrada:
    #     a , b , c = list(map(float, (entrada.readline().split(" "))))