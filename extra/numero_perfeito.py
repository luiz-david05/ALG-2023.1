from get_functions import *

def main():
    n1 = get_valid_number("1° número: ")
    n2 = get_valid_number("2° número: ")

    soma = verificar_numero_perfeito(n1, n2)

    if soma == n1:
        print(f"{n1} é um número perfeito")

    else:
        print(f"{n1} não é um número perfeito")
        

def verificar_numero_perfeito(n1, n2):
    soma = 0
    i = 1
    maior = 0

    if n1 < n2:
        maior = n2

    else:
        maior = n1

    while i < maior:
        if n1 % i == 0:
            soma += i
        
        i += 1

    return soma


if __name__ == "__main__":
    main()