def main():
    a, b, c, d, e = map(int, input().split())

    sequencia = [a, b, c, d, e]
    sequencia_ordenada = sorted([a, b, c, d, e])
    sequencia_inversa = sequencia_ordenada[::-1]

    if sequencia == sequencia_ordenada:
        print("C")
    elif sequencia == sequencia_inversa:
        print("D")
    else:
        print("N")

    
if __name__ == "__main__":
    main()