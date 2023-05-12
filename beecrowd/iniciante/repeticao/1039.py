import math


def main():
    while True:
        try:
            r1, x1, y1, r2, x2, y2 = map(int, input().split())

            if r1 >= calcular_distancia(x1, y1, x2, y2) + r2:
                print("RICO")
            else:
                print("MORTO")
        except EOFError:
            break

def calcular_distancia(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


if __name__ == '__main__':
    main()  