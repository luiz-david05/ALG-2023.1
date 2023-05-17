def main():
    notas_validas = 0
    soma = 0

    while notas_validas < 2:
        nota = float(input())
        if nota >= 0 and nota <= 10:
            soma += nota
            notas_validas += 1
        else:
            print("nota invalida")

    media = calcular_media(soma, notas_validas)
    print(f"media = {media:.2f}")


def calcular_media(soma, n):
    return soma / n


if __name__ == "__main__":
    main()