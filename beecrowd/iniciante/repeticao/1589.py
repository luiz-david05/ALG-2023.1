def main():
    t = int(input())

    for _ in range(t):
        r1, r2 = map(int, input().split())
        print(r1 + r2)


if __name__ == "__main__":
    main()