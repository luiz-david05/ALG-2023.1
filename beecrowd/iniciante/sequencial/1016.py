def main():
    distancia = int(input())
    
    tempo = calcular_tempo_necessario(distancia)

    print(f"{tempo} minutos")


def calcular_tempo_necessario(distancia):
    return distancia * 2


if __name__ == "__main__":
    main()


    # with open("1016.txt" , "r") as entrada:
    #     distancia = int(entrada.readline())