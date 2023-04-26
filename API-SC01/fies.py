from get_functions import *
import math


def main():
    # pedir dados
    nome_curso = input("nome do curso: ")
    duracao_curso = pegar_duracao_valida("duração: ")
    valor_mensalidade = get_valid_number("valor da mensalidade: ")
    selic = 13.75 / 100
    salario_minimo = 1302
    total_renda_familiar = 2500
    qtd_membros_familia = 4
    ano_inicio_curso = 2022
    semestre_inicio = 1

    # calcular renda per capita
    renda_percapita = total_renda_familiar / qtd_membros_familia

    # verificar quanto aplicar da taxa selic

    if renda_percapita <= 1.5 * salario_minimo:
        juros = selic * 0.10

    elif renda_percapita > 1.5 * salario_minimo and renda_percapita <= 2 * salario_minimo:
        juros = selic * 0.15

    elif renda_percapita > 2 * salario_minimo and renda_percapita <= 2.5 * salario_minimo:
        juros = selic * 0.20

    elif renda_percapita > 2.5 * salario_minimo:
        juros = selic * 0.25

    # verificar se a renda familiar será aprovada no programa

    if total_renda_familiar > 3 * salario_minimo:
        print(f"Sua renda familiar está acima de 3 sálarios mínimos, ou seja: Não está apta para participar do FIES.")

    else:
        # calcular valor pago durante o curso

        valor_pago = duracao_curso * 50

        # calcular valor pago na carência de 18 meses após concluir o curso

        valor_carencia = 18 * 50


        # calcular valor do curso

        valor_curso = duracao_curso * valor_mensalidade

        # calcular saldo devedor
        valor_total_juros = valor_curso * juros

        saldo_devedor = valor_curso + valor_total_juros - (valor_pago + valor_carencia)

        # parcelar curso em até 4x a duração do curso

        valor_parcela_mensal = saldo_devedor / duracao_curso * 4

        #  calcular valor mínimo que o aluno deve ter de renda para pagar o curso após terminar o périodo de carência

        renda_minima = valor_parcela_mensal * 0.10

        # calcular ano/semestre que o aluno irá iniciar o pagamento do FIES

        ano_inicio_pagamento = math.floor(ano_inicio_curso + ((duracao_curso + 18) / 12))

        # calcular semestre

        if semestre_inicio % 2 == 1:
            semestre1 = 1

        else:
            semestre1 = 2
        
        if ano_inicio_pagamento % 2 == 1:
            semestre2 = 1

        else:
            semestre2 = 2

        semestre_inicio_pagamento = semestre1 + semestre2 - 1

        # calcular ano/semestre que o aluno irá concluir o pagamento do FIES

        ano_conclusao_pagamento = math.floor((saldo_devedor / renda_minima) / 12) + ano_inicio_pagamento

        # semestre de conclusão do pagamento

        if semestre_inicio_pagamento % 2 == 1:
            semestre_conclusao1 = 1

        else:
            semestre_conclusao1 = 2

        if semestre_inicio_pagamento % 2 == 1:
            semestre_conclusao2 = 1

        else:
            semestre_conclusao2 = 2

        semestre_conclusao_pagamento = semestre_conclusao1 + semestre_conclusao2 - 1



        # exibir dados

        print("\nSua renda familiar é de até 3 sálarios mínimos, ou seja: Está apta para participar do FIES.")
        print(f"\nvalor a ser financiado: R$ {valor_curso:.2f}")
        print(f"valor total do juros: R$ {valor_total_juros:.2f}")
        print(f"valor total a pagar: R$ {saldo_devedor:.2f}")
        print(f"valor a ser pago durante o curso: R$ {valor_pago:.2f} ")
        print(f"valor a ser pago durante o périodo de carência: R$ {valor_carencia:.2f}")
        print(f"sua renda mínima deve ser de no mínimo: R$ {renda_minima:.2f} ao iniciar o pagamento do financiamento")
        print(f"ano/semestre em que o aluno iniciará o pagamento: {ano_inicio_pagamento} / {semestre_inicio_pagamento}")
        print(f"ano/semestre em que o aluno concluirá o pagamento (baseado em quê o aluno pagará apenas 10% da sua renda): {ano_conclusao_pagamento} / {semestre_conclusao_pagamento}")


def pegar_duracao_valida(texto):
    duracao = get_valid_number(texto)

    if duracao < 36 and duracao % 6 != 0:
        print(f"os cursos tem duração em meses múltiplos de 6 e a duração mínima é de 36 meses (2.5 anos)")

        duracao = pegar_duracao_valida(texto)

    return duracao


if __name__ == "__main__":
    main()

    
