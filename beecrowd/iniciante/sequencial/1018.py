def main():
    valor = int(input())

    print(valor)

    distribuir_notas(valor)


def distribuir_notas(valor):
    notas = [100, 50, 20, 10, 5, 2, 1]
    resto = valor

    for nota in notas:
        qtd_notas = resto // nota
        resto %= nota

        print(f"{qtd_notas} nota(s) de R$ {nota},00")
    

if __name__ == "__main__":
    main()

    
    # with open("1018.txt" , "r") as entrada:
    #     valor = int(entrada.readline())