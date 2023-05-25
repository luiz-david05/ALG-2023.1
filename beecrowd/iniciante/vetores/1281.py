def main():
    qtd_idas = int(input())

    for i in range(qtd_idas):
        qtd_produtos = int(input())
        produtos = {}
        for j in range(qtd_produtos):
            produto, preco = input().split()
            produtos[produto] = float(preco)

        qtd_compras = int(input())
        total = 0
        for j in range(qtd_compras):
            produto, qtd = input().split()
            total += produtos[produto] * int(qtd)

        print(f'R$ {total:.2f}')


if __name__ == '__main__':
    main()


# iniciar dicionário vazio e ir adicionando os produtos e preços
# depois, ler as compras e ir somando os preços
# no final, imprimir o total
