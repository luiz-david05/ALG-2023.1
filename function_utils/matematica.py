def divisores(n):
    divisores = []
    
    for i in range(1, n + 1):
        if eh_inteiro(i) and eh_divisor(i, n):
            divisores.append(i)
    
    return divisores


def eh_inteiro(n): return n % 1 == 0


def eh_divisor(n1, n2): return n1 % n2 == 0


def mmc(n1, n2):
    mmc = n1 if n1 > n2 else n2

    while not (eh_divisor(mmc, n1) and eh_divisor(mmc, n2)):
        mmc += 1

    return mmc


def eh_par(n): return n % 2 == 0


def eh_impar(n): return not eh_par(n)


def eh_positivo(n): return n >= 0


def eh_negativo(n): return not eh_positivo(n)


def eh_primo(n):
    if n <= 1:
        return False
    
    i = 2

    while i < n:
        if eh_multiplo(n, i):
            return False
        
        i += 1

    return True


def eh_multiplo(n1, n2): return n1 % n2 == 0


def fatorial(n):
    if n < 0:
        return None

    if n == 0:
        return 1

    fatorial = 1

    while n > 0:
        fatorial *= n
        n -= 1

    return fatorial


def raiz(n, indice):
    if n < 0:
        return None

    if indice < 0:
        return None

    if indice == 0:
        return None

    if indice == 1:
        return n

    raiz = 1

    while not eh_raiz(n, raiz, indice):
        raiz += 1

    return raiz


def eh_raiz(n, raiz, indice): return raiz ** indice == n


def eh_numero_perfeito(n):
    if n < 0:
        return False

    if n == 0:
        return True

    soma_divisores = 0

    for divisor in divisores(n):
        soma_divisores += divisor

    return soma_divisores == n


def raiz_quadrada(n): return raiz(n, 2)


def raiz_cubica(n): return raiz(n, 3)