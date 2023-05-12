def main():
    a, b, c = list(map(float, input().split()))

    eh_triangulo = a + b > c and b + c > a and c + a > b
    
    if eh_triangulo:
        perimetro = a + b + c

        print(f"Perimetro = {perimetro:.1f}")
    else:
        area_trapezio  = (a + b) / 2 * c
        print(f"Area = {area_trapezio:.1f}")


main()