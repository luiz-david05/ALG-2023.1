def main():
    dias = int(input())

    ano, meses, dias_restantes = calcular_idade_anos_meses_dias(dias)

    print(f"{ano} ano(s)\n{meses} mes(es)\n{dias_restantes} dia(s)")


def calcular_idade_anos_meses_dias(dias):
    ano, dias = divmod(dias, 365)
    meses, dias_restantes = divmod(dias, 30)

    return ano, meses, dias_restantes


if __name__ == "__main__":
    main()

    # with open("1020.txt" , "r") as entrada:
    #     dias = int(entrada.readline())