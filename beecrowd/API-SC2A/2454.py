def main():
    p, r = map(int, input().split())

    if p == 0:
        print("C")
    elif r == 0:
        print("B")
    else:
        print("A")

if __name__ == "__main__":
    main()