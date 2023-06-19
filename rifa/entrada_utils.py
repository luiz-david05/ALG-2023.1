def get_number(texto):
    n = input(texto)

    try:
        if "." in n:
            return float(n)
        else:
            return int(n)
    except ValueError:
        print("Valor inválido!")
        n = get_number(texto)
        return n
    

def get_pontos():
    pontos = []
    with open("pontos.txt", "r") as f:
        for line in f:
            pontos.append(line.strip())
    return pontos