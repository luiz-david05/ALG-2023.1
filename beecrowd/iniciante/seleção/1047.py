def main():
    hora_inicio, minuto_inicio, hora_fim, minuto_fim = map(int, input().split())

    hora, minuto = calcular_duracao_do_jogo(hora_inicio, minuto_inicio, hora_fim, minuto_fim)

    print(f"O JOGO DUROU {hora} HORA(S) E {minuto} MINUTO(S)")


def calcular_duracao_do_jogo(hora_inicio, minuto_inicio, hora_fim, minuto_fim):
    hora = hora_fim - hora_inicio
    minuto = minuto_fim - minuto_inicio

    if minuto < 0:
        minuto += 60
        hora -= 1
        
    if hora < 0:
        hora += 24


    if hora == 0 and minuto == 0:
        hora = 24

    return hora, minuto


if __name__ == '__main__':
    main()