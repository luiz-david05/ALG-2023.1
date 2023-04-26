def get_number(text):
    try:
        n = input(text)

        if "." in n:
            n = float(n)
    
        else:
            n = int(n)

        return n
    except ValueError:
        print(f"Digite um número.")


def get_valid_number(text):
    n = get_number(text)

    if n <= 0:
        print(f"Digite um número maior que 0.")

        n = get_valid_number(text)

    return n
