def main():
    soma = 0
    quant = 0
    idade = int(input())

    while idade > 0:
        soma += idade
        quant += 1
        idade = int(input())
    
    media = calcular_media(soma, quant)
    print(f'{media:.2f}')


def calcular_media(soma, quant):
    return soma / quant


if __name__ == "__main__":
    main()