def main():
    a, b, c = map(float, input().split())

    a, b, c = ordenar_valores_em_ordem_decrescente(a, b, c)

    if eh_triangulo(a, b, c):
        if eh_triangulo_retangulo(a, b, c):
            print("TRIANGULO RETANGULO")
        if eh_triangulo_acutangulo(a, b, c):
            print("TRIANGULO ACUTANGULO")
        if eh_triangulo_obtusangulo(a, b, c):
            print("TRIANGULO OBTUSANGULO")
        if eh_triangulo_equilatero(a, b, c):
            print("TRIANGULO EQUILATERO")   
        if eh_triangulo_isosceles(a, b, c):
            print("TRIANGULO ISOSCELES")
    else:
        print("NAO FORMA TRIANGULO")


def ordenar_valores_em_ordem_decrescente(a, b, c):
    return sorted([a, b, c], reverse=True)
    
def eh_triangulo(a, b, c):
    return a + b > c and b + c > a and c + a > b

def eh_triangulo_retangulo(a, b, c):
    return eh_triangulo(a, b, c) and a ** 2 == b ** 2 + c ** 2

def eh_triangulo_obtusangulo(a, b, c):
    return eh_triangulo(a, b, c) and a ** 2 > b ** 2 + c ** 2

def eh_triangulo_acutangulo(a, b, c):
    return eh_triangulo(a, b, c) and a ** 2 < b ** 2 + c ** 2

def eh_triangulo_equilatero(a, b, c):
    return eh_triangulo(a, b, c) and b == a == c

def eh_triangulo_isosceles(a, b, c):
    return eh_triangulo(a, b, c) and (a == b and b != c or b == c and c != a or c == a and a != b)


main()