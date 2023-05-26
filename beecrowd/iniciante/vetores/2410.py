def main():
    n = int(input())

    alunos = set()
    for _ in range(n):
        alunos.add(int(input()))

    print(len(alunos))


if __name__ == '__main__':
    main()