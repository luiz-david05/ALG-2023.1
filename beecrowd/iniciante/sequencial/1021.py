def main():
    valor = float(input())

    distribuir_notas_e_moedas(valor)


def distribuir_notas_e_moedas(valor):
    notas = [10000, 5000, 2000, 1000, 500, 200]
    resto = int(valor * 100)

    print("NOTAS:")
    for nota in notas:
        qtd_notas, resto = divmod(resto, nota)

        print(f"{int(qtd_notas)} nota(s) de R$ {(nota / 100):.2f}")

    moedas = [100, 50, 25, 10, 5, 1 ]

    print("MOEDAS:")

    for moeda in moedas:
        qtd_moedas, resto = divmod(resto, moeda)
                                       
        print(f"{int(qtd_moedas)} moeda(s) de R$ {(moeda / 100):.2f}")
            

if __name__ == "__main__":
    main()


    # with open("1021.txt", "r") as entrada:
    #     valor = float(entrada.readline())














# import math

# valor = float(input())

# resto = valor
# nota_100 = math.trunc(resto / 100)
# resto %= 100
# nota_50 = math.trunc(resto / 50)
# resto %= 50
# nota_20 = math.trunc(resto / 20)
# resto %= 20
# nota_10 = math.trunc(resto / 10)
# resto %= 10
# nota_5 = math.trunc(resto / 5)
# resto %= 5
# nota_2 = math.trunc(resto / 2)
# resto %= 2

# # moedas
# resto *= 100
# moeda_1 = math.trunc(resto / 100)
# resto %= 100
# moeda_50 = math.trunc(resto / 50)
# resto %= 50
# moeda_25 = math.trunc(resto / 25)
# resto %= 25
# moeda_10 = math.trunc(resto / 10)
# resto %= 10
# moeda_5 = math.trunc(resto / 5)
# resto %= 5

# resto = round(resto)

# print("NOTAS:")
# print(f"{nota_100} nota(s) de R$ 100.00")
# print(f"{nota_50} nota(s) de R$ 50.00")
# print(f"{nota_20} nota(s) de R$ 20.00")
# print(f"{nota_10} nota(s) de R$ 10.00")
# print(f"{nota_5} nota(s) de R$ 5.00")
# print(f"{nota_2} nota(s) de R$ 2.00")

# print("MOEDAS:")
# print(f"{moeda_1} moeda(s) de R$ 1.00")
# print(f"{moeda_50} moeda(s) de R$ 0.50")
# print(f"{moeda_25} moeda(s) de R$ 0.25")
# print(f"{moeda_10} moeda(s) de R$ 0.10")
# print(f"{moeda_5} moeda(s) de R$ 0.05")
# print(f"{resto} moeda(s) de R$ 0.01")
