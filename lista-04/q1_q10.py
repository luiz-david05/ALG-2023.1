from get_functions import pegar_numero

def q1():
    n = 1

    while n != 0:
        n = pegar_numero("digite os numeros: ")
        print(f"numero = {n}")

        i = 1

        while i <= n:
            if n % i == 0:
                print(f"divisores do numero {n}: {i}")

            i += 1


def q2():
    n1 = pegar_numero("numero 1: ")
    n2 = pegar_numero("numero 2: ")

    if n1 > n2:
        mmc = n1

    else:
        mmc = n2

    while not (eh_multiplo(mmc, n1) and eh_multiplo(mmc, n2)):
        mmc += 1

    print(f"mmc de {n1} e {n2} = {mmc}")

def eh_multiplo(n1, n2): return n1 % n2 == 0

def q3():
    n1 = pegar_numero("numero 1: ")
    n2 = pegar_numero("numero 2: ")

    if n1 > n2:
        menor = n1
        maior = n2

    else:
        menor = n2
        maior = n1

    # euclides
    dividendo = maior
    divisor = menor

    while divisor != 0:
        resto = dividendo % divisor
        dividendo = divisor
        divisor = resto

    mdc = dividendo

    print(f"mdc de {n1} e {n2} = {mdc}")
        
def q4():
    n1 = pegar_numero("numero: ")

    divisao = n1 / 2
    dividendo = n1

    while divisao > 1:
        print(f"resultado de {dividendo} / 2 = {divisao}")
        dividendo = divisao

        divisao /= 2
    
    print(f"resultado da utima divisao = {dividendo} / 2  = {divisao}")


