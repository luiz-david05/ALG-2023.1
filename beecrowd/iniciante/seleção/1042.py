def main():
    n1, n2, n3 = list(map(int, input().split()))

    numbers = [n1, n2, n3]

    numbers.sort()

    for i in numbers:
        print(i)

    print(f"\n{n1}\n{n2}\n{n3}")

main()

    # with open("1042.txt" , "r") as entrada:
    #     n1, n2, n3 = list(map(int, entrada.readline().split()))