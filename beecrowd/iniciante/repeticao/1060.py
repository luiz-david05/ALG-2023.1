def main():
    valores = [float(input()) for _ in range(6)]

    contador_positivos = 0
    for valor in valores:
        if valor > 0:
            contador_positivos += 1
    
    print(f"{contador_positivos} valores positivos")


if __name__ == "__main__":
    main()
    
    # with open("1060.txt" , "r") as entrada:
    #     valores = [float(entrada.readline()) for _ in range(6)]