def main():
    seg = int(input())

    hr, min, seg_restantes = calcular_duracao_evento(seg)

    print(f"{hr}:{min}:{seg_restantes}")

def calcular_duracao_evento(seg):
    # usando divmod para calcular o resultado da divisão e o resto da divisão simultaneamente

    hr, seg = divmod(seg, 3600)
    min, seg_restantes = divmod(seg, 60)

    return hr, min, seg_restantes


if __name__ == "__main__":
    main()

    # with open("1019.txt" , "r") as entrada:
    #     seg = int(entrada.readline())