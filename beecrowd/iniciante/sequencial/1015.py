def main():
    x1, y1 = list(map(float, input().split(" ")))
    x2, y2 = list(map(float, input().split(" ")))
    
    distancia = calcular_distancia_plano_cartesiano(x1, y1, x2, y2)

    print(f"{distancia:.4f}")

def calcular_distancia_plano_cartesiano(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


if __name__ == "__main__":
    main()


    # with open("1015.txt" , "r") as entrada:
    #     x1, y1 = list(map(float, entrada.readline().split(" ")))
    #     x2, y2 = list(map(float, entrada.readline().split(" ")))