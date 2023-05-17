def main():
    n = int(input())

    for i in range(n):
        x, y = map(int, input().split())
        if y == 0:
            print("divisao impossivel")
        else:
            divisao = x / y
            print(f"{divisao:.1f}")
    

if __name__ == "__main__":
    main()