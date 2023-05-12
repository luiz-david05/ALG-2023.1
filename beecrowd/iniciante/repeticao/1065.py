def main():
    valores = [int(input()) for _ in range(5)]

    numeros_pares = 0
    for _ in valores:
        if _ % 2 == 0:
            numeros_pares += 1
    
    print(f"{numeros_pares} valores pares")


main()
