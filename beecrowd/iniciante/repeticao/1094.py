def main():
    n = int(input())
   
    total = 0
    total_coelho = 0
    total_rato = 0
    total_sapo = 0

    for i in range(n):
        quantidade, tipo = input().split()
        quantidade = int(quantidade)

        total += quantidade

        total_coelho, total_rato, total_sapo = calcular_quantidade_animais(tipo, quantidade, total_coelho, total_rato, total_sapo)

    percentual_coelho, percentual_rato, percentual_sapo = calcular_percentual(total, total_coelho, total_rato, total_sapo)

    print(f"Total: {total} cobaias")
    print(f"Total de coelhos: {total_coelho}")
    print(f"Total de ratos: {total_rato}")
    print(f"Total de sapos: {total_sapo}")
    print(f"Percentual de coelhos: {percentual_coelho:.2f} %")
    print(f"Percentual de ratos: {percentual_rato:.2f} %")
    print(f"Percentual de sapos: {percentual_sapo:.2f} %")


def calcular_quantidade_animais(tipo, quantidade, total_coelho, total_rato, total_sapo):
    if tipo == 'C':
        total_coelho += quantidade
    elif tipo == 'R':
        total_rato += quantidade
    elif tipo == 'S':
        total_sapo += quantidade

    return total_coelho, total_rato, total_sapo


def calcular_percentual(total, total_coelho, total_rato, total_sapo):
    percentual_coelho = (total_coelho / total) * 100
    percentual_rato = (total_rato / total) * 100
    percentual_sapo = (total_sapo / total) * 100

    return percentual_coelho, percentual_rato, percentual_sapo


if __name__ == "__main__":
    main()