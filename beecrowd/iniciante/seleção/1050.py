def main():
    ddd = int(input())

    print(verificar_ddd(ddd))


def verificar_ddd(ddd):
    destino = ''
    if ddd == 61:
        destino = "Brasilia"
    elif ddd == 71:
        destino = "Salvador"
    elif ddd == 11:
        destino = "Sao Paulo"
    elif ddd == 21:
        destino = "Rio de Janeiro"
    elif ddd == 32:
        destino = "Juiz de Fora"
    elif ddd == 19:
        destino = "Campinas"
    elif ddd == 27:
        destino = "Vitoria"
    elif ddd == 31:
        destino = "Belo Horizonte"
    else:
        destino = "DDD nao cadastrado"

    return destino

    
main()