def main():
    a, b, c, d = map(int, input().split())

    if a == b or a == c or a == d or b == c or b == d or c == d:
        print("S")
    elif a + b == c or a + b == d or a + c == b or a + c == d or a + d == b or a + d == c or b + c == a or b + c == d or b + d == a or b + d == c or c + d == a or c + d == b:
        print("S")
    else:
        print("N")

if __name__ == "__main__":
    main()