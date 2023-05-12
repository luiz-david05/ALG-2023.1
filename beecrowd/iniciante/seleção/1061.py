def main():
    dia_inicio = int(input().split()[1])
    hora_inicio, minuto_inicio, segundo_inicio = map(int, input().split(':'))

    dia_fim = int(input().split()[1])
    hora_fim, minuto_fim, segundo_fim = map(int, input().split(':'))

    dia, hora, minuto, segundo = calcula_tempo(dia_inicio, hora_inicio, minuto_inicio, segundo_inicio, dia_fim, hora_fim, minuto_fim, segundo_fim)

    print(f'{dia} dia(s)')
    print(f'{hora} hora(s)')
    print(f'{minuto} minuto(s)')
    print(f'{segundo} segundo(s)')


def calcula_tempo(dia_inicio, hora_inicio, minuto_inicio, segundo_inicio, dia_fim, hora_fim, minuto_fim, segundo_fim):
    dias = dia_fim - dia_inicio
    horas = hora_fim - hora_inicio
    minutos = minuto_fim - minuto_inicio
    segundos = segundo_fim - segundo_inicio

    if segundos < 0:
        segundos += 60
        minutos -= 1
    
    if minutos < 0:
        minutos += 60
        horas -= 1
    
    if horas < 0:
        horas += 24
        dias -= 1
    
    return dias, horas, minutos, segundos


if __name__ == '__main__':
    main()