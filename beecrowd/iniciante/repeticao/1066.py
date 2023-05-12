def main():
    valores = [int(input()) for _ in range(5)]

    valores_pares = 0
    valores_impares = 0
    valores_positivos = 0
    valores_negativos = 0
    for i in valores:
        if i % 2 == 0:
            valores_pares += 1
        else:
            valores_impares += 1

        if i > 0:
            valores_positivos += 1
        elif i < 0:
            valores_negativos += 1

    print(f"{valores_pares} valor(es) par(es)")
    print(f"{valores_impares} valor(es) impar(es)")
    print(f"{valores_positivos} valor(es) positivo(s)")
    print(f"{valores_negativos} valor(es) negativo(s)")


main()