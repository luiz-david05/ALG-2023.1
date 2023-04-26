def main():
    variaveis = [int(input()) for _ in range(2)]
    qtd_combustivel = calcular_gasto_combustivel(*variaveis)

    print(f"{qtd_combustivel:.3f}")

def calcular_gasto_combustivel(tempo, velocidade):
    return tempo * velocidade / 12


if __name__ == "__main__":
    main()


    # with open("1017.txt" , "r") as entrada:
    #     variaveis = [int(entrada.readline()) for _ in range(2)]