def get_number(texto):
    try:
        n = input(texto)

        if "." in n:
            n = float(n)

        else:
            n = int(n)

        return n
    except ValueError:
        print("Digite um número")

def get_valid_number(texto):
    n = get_number(texto)

    if n < 0:
        print("Digite um número maior que zero.")

        n = get_valid_number(texto)

    return n