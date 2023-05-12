import math


def main():
    while True:
        try:
            xf, yf, xi, yi, vi, r1, r2 = map(int, input().split())

            distancia = calcular_distancia(xf, yf, xi, yi)

            if distancia + 1.5 * vi <= r1 + r2:
                print('Y')
            else:
                print('N')
        except EOFError:
            break


def calcular_distancia(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


if __name__ == '__main__':  
    main()
