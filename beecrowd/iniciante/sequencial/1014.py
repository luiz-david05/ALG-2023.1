def main():
    variaveis = [float(input()) for _ in range(2)]
    consumo_medio = calcular_consumo_medio(*variaveis)

    print(f"{consumo_medio:.3f} km/l")


def calcular_consumo_medio(x, y):
    return x / y


if __name__ == "__main__":
    main()

    # with open("1014.txt" , "r") as entrada:
    #     variaveis = [float(entrada.readline()) for _ in range(2)]