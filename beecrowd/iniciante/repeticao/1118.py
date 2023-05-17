def main():
    resposta =  0
    while resposta != "2":
        soma, notas_validas = pegar_notas_validas()

        media = calcular_media(soma, notas_validas)
        print(f"media = {media:.2f}")
        
        soma = 0
        notas_validas = 0

        resposta = validar_resposta()

        if resposta == 1:
            soma, notas_validas = pegar_notas_validas()
            media = calcular_media(soma, notas_validas)
            print(f"media = {media:.2f}")

    
def calcular_media(soma, n):
    return soma / n


def validar_nota(nota):
    return nota >= 0 and nota <= 10


def pegar_notas_validas():
    notas_validas = 0
    soma = 0

    while notas_validas < 2:
        nota = float(input())
        if validar_nota(nota):
            soma += nota
            notas_validas += 1
        else:
            print("nota invalida")

    return soma, notas_validas


def validar_resposta():
    resposta = input("novo calculo (1-sim 2-nao)\n")
    while resposta != "1" and resposta != "2":
        resposta = input("novo calculo (1-sim 2-nao)\n")
    return resposta


if __name__ == "__main__":
    main()
