def main():
    valor = int(input())

    print(verificar_mes(valor))


def verificar_mes(valor):
    meses = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November","December"]

    # indice começa em 0, por isso o -1
    return meses[valor - 1]
    

if __name__ == '__main__':
    main()