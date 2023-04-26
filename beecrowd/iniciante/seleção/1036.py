def main():
    a, b, c = list(map(float, input().split(" ")))
    
    delta = calcular_delta(a, b, c)

    if a == 0 or delta < 0:
        print("Impossivel calcular")

    else:
        x1, x2 = calcular_raizes(a, b, delta)

        print(f"R1 = {x1:.5f}")
        print(f"R2 = {x2:.5f}")


def calcular_delta(a, b, c):
    return b ** 2 - 4 * a * c


def calcular_raizes(a, b, delta):
    x1 = (-b + (delta ** 0.5)) / (2 * a)
    x2 = (-b - (delta ** 0.5)) / (2 * a)

    return x1, x2


if __name__ == "__main__":
    main()


    # with open("1036.txt" , "r") as entrada:
    #     a, b, c = list(map(float, entrada.readline().split(" ")))