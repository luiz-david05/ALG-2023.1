def main():
    quantidade_anoes, distancia = map(int, input().split())

    quantidade_pessoas = quantidade_anoes + 2

    qtd_dias = distancia / quantidade_pessoas

    print(f"{qtd_dias:.2f}")


if __name__ == '__main__':
    main()