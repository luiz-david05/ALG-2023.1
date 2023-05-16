def main():
    tipo_cha = int(input())

    respostas = map(int, input().split())

    soma = 0
    for i in respostas:
        if i == tipo_cha:
           soma += 1
    
    print(soma)


if __name__ == "__main__":
    main()