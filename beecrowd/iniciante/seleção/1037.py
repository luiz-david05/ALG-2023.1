def main():
    n = float(input())
    intervalo = definir_intervalo(n)

    print(intervalo)


def definir_intervalo(n):
    if 0 <= n <= 25:
        intervalo = "Intervalo [0,25]"

    elif 25 < n <= 50:
        intervalo = "Intervalo (25,50]"
    
    elif 50 < n <= 75:
        intervalo = "Intervalo (50,75]"

    elif 75 < n <= 100:
        intervalo = "Intervalo (75,100]"

    else:
        intervalo = "Fora de intervalo"

    return intervalo


if __name__ == "__main__":
    main()
        
    # with open("1037.txt" , "r") as entrada:
    #     n = float(entrada.readline())