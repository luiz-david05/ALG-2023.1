def main():
    n = int(input())

    for i in range(n):
        a, b, c = map(float, input().split())
        print(f"{calcular_media_ponderada(a, b, c):.1f}")


def calcular_media_ponderada(a, b, c):
    return (a * 2 + b * 3 + c * 5) / 10


if __name__ == "__main__":
    main()