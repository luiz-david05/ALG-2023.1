def main():
    n1, n2, n3, n4 = list(map(float, input().split(" ")))

    media = calcular_media_ponderada(n1, n2, n3, n4)   

    print(f"Media: {media:.1f}")

    if media >= 7:
        print("Aluno aprovado.")

    elif media >= 5 and media <= 6.9:
        print("Aluno em exame.")

        nota_exame = float(input())
        print(f"Nota do exame: {nota_exame:.1f}")

        media_exame = (media + nota_exame) / 2

        if media_exame >= 5:
            print(f"Aluno aprovado.")

        else:
            print("Aluno reprovado.")

        print(f"Media final: {media_exame:.1f}")

    else:
        print("Aluno reprovado.")


def calcular_media_ponderada(n1, n2, n3, n4):
    return ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10


if __name__ == "__main__":
    main()



    # with open("1040.txt" , "r") as entrada:
    #     n1, n2, n3, n4 = list(map(float, entrada.readline().split(" ")))
    #     nota_exame = float(entrada.readline())