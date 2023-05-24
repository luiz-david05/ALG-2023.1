def pegar_numero(texto):
    try:
        n = input(texto)

        if "." in n:
            n = float(n)

        else:
            n = int(n)

        return n
    except ValueError:
        print("Digite um número")

        n = pegar_numero(texto)

        return n


def pegar_numero_positivo(texto):
    n = pegar_numero(texto)

    if n < 0:
        print("Digite um número positivo")

        n = pegar_numero_positivo(texto)

    return n