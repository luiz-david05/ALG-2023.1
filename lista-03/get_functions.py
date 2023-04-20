def get_number(text):
    while True:
        try:
            n = input(text)
            if "." in n:
                n = float(n)
            else:
                n = int(n)
            return n
        except ValueError:
            print("Digite um número válido.")


def get_positive_number(text="n: "):
    n = get_number(text)

    if n <= 0:
        print("Digite um número maior que 0.")

        n = get_positive_number(text)

    return n

