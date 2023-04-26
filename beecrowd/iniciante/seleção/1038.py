def main():
    cod, qtd = list(map(int, input().split(" ")))
    valor = calcular_valor_a_pagar(cod, qtd)

    print(f"Total: R$ {valor:.2f}")


def calcular_valor_a_pagar(cod, qtd):
    if cod == 1:
        valor = qtd * 4

    elif cod == 2:
        valor = qtd * 4.5

    elif cod == 3:
        valor = qtd * 5

    elif cod == 4:
        valor = qtd * 2

    elif cod == 5:
        valor = qtd * 1.5

    return valor


if __name__ == "__main__":
    main()
    
    # with open("1038.txt" , "r") as entrada:
    #     cod, qtd = list(map(int, entrada.readline().split(" ")))