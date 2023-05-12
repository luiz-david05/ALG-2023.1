def main():
    salario = float(input())

    aumento, percentual = calcular_aumento_e_taxa_percentual(salario)

    novo_salario = salario + aumento

    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {aumento:.2f}")
    print(f"Em percentual: {percentual}")


def calcular_aumento_e_taxa_percentual(salario):
    if salario >= 0 and salario <= 400:
        reajuste = 0.15
        percentual = "15 %"
    elif salario > 400 and salario <= 800:
        reajuste = 0.12
        percentual = "12 %"
    elif salario > 800 and salario <= 1200:
        reajuste = 0.10
        percentual = "10 %"
    elif salario > 1200 and salario <= 2000:
        reajuste = 0.07
        percentual = "7 %"
    elif salario > 2000:
        reajuste = 0.04
        percentual = "4 %"

    aumento = salario * reajuste

    return aumento, percentual


main()