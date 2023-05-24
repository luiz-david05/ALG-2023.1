def main():
    vetor = criar_vetorv2(100)

    vetor = preencher_vetorv5(vetor) 
    for i in range(len(vetor)):
        print(f"N[{i}] = {vetor[i]:.4f}")


def criar_vetorv2(tamanho):
    vetor = [0] * tamanho
    return vetor


def preencher_vetorv5(vetor):
    valor = float(input())
    for i in range(len(vetor)):
        vetor[i] = valor
        valor /= 2
    return vetor


if __name__ == "__main__":
    main()
