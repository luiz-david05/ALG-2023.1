def main():
    valores = [float(input()) for _ in range(6)]

    numeros_positivos = 0
    soma_positivos = 0
    for i in valores:
        if i >= 0:
            numeros_positivos += 1
            soma_positivos += i

    media_positivos = soma_positivos / numeros_positivos

    print(f"{numeros_positivos} valores positivos")
    print(f"{media_positivos:.1f}")


main()