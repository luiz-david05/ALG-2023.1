def pegar_numero(texto):
    try:
        n = input(texto)

        if "." in n:
            n = float(n)

        else:
            n = int(n)
        return n

    except ValueError:
        print("Digite um valor valido seu imoral.")

        
