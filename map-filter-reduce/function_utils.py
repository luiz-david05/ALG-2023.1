def get_int(texto):
    n = input(texto)

    try:
        return int(n)
    except ValueError:
        print("Digite um número inteiro válido!")
        n = get_int(texto)
    
    return n


def get_positive_number(texto):
    n = get_int(texto)

    if n > 0:
        return n
    else:
        print("Digite um número positivo!")
        return get_positive_number(texto)