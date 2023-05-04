from get_functions import *


def main():
    valor_hora = get_valid_number("valor da hora: ")
    nome = input("nome: ")
    qtd_hrs_semanais = get_valid_number("quantidade de horas semanais: ")
    duracao_aula = get_valid_number("duração da aula: ")
    qualificao = pegar_qualificacao_valida("qualificação: ")
    experiencia = get_valid_number("experiência(em meses): ")
    qtd_filhos = get_number("quantidade de filhos menores de 6 anos de idade: ")
    valor_plano = get_valid_number("valor do plano de saúde: ")

    # calcular bonus de qualificação
    bonus_qualificacao = valor_hora * 0.20
    if qualificao == "M":
        bonus_qualificacao = valor_hora * 0.30
    elif qualificao == "D":
        bonus_qualificacao = valor_hora * 0.50

    # bonus tempo de experiência
    experiencia = 12
    bonus_experiencia = valor_hora * 0.05

    if experiencia > 12:
        experiencia_anos = (experiencia // 12) * 0.05
        bonus_experiencia = valor_hora * experiencia_anos
    
    salario_semanal = (valor_hora + bonus_qualificacao + bonus_experiencia) * qtd_hrs_semanais

    salario_mensal = salario_semanal * 4.5

    # calcular auxilio creche
    auxilio_creche = 0

    if qtd_filhos >= 1:
        auxilio_creche = qtd_filhos * 700
    
    # ressarcimento sáude
    ressarcimento = valor_plano * 0.5
    if valor_plano >= 1000:
        ressarcimento = 500

    # auxilio combustivel
    qtd_aulas = qtd_hrs_semanais // duracao_aula
    auxilio_comustivel = 0
    if qtd_aulas >= 8:
        auxilio_combustivel = (qtd_aulas // 8) * 30 

    # salário bruto
    salario_bruto = salario_mensal + auxilio_creche + auxilio_combustivel + ressarcimento

    # descontos
    # previdência social
    if salario_mensal <= 1302:
        inss = salario_mensal * 0.075
    elif salario_mensal > 1302 and salario_mensal <= 2500:
        inss = salario_mensal * 0.09
    elif salario_mensal > 2500 and salario_mensal <= 3900:
        inss = salario_mensal * 0.12
    elif salario_mensal > 3900 and salario_mensal <= 7500:
        inss = salario_mensal * 0.14
    elif salario_mensal > 7500:
        inss = salario_mensal * 0.16

    # imposto de renda
    ir = 0
    if salario_mensal > 5000:
        ir = (salario_mensal - 5000) * 0.275

    # total descontos
    total_descontos = ir + inss

    # salário líquido
    salario_liquido =  salario_bruto - total_descontos
    
    
    # mostrar dados
    print( "\n", 4 * "-", "contracheque mensal detalhado", 4 * "-")
    print(f"\nnome do professor: {nome}")
    print(f"valor hora: R$ {valor_hora:.2f}")
    print(f"sálario base semanal: R$ {salario_semanal:.2f}")
    print("\n", 4 * "-", "ganhos", 4 * "-")
    print(f"salário base mensal: R$ {salario_mensal:.2f}")
    print(f"auxílio creche: R$ {auxilio_creche:.2f}")
    print(f"auxílio combustível: R$ {auxilio_combustivel:.2f}")
    print(f"salário bruto: R$ {salario_bruto:.2f}")
    print("\n", 4 * "-", "descontos", 4 * "-")
    print(f"previdência: R$ {inss:.2f}")
    print(f"imposto de renda: R$ {ir:.2f}")
    print(f"total descontos: R$ {total_descontos:.2f}")
    print("\n", 4 * "-", "salário líquido", 4 * "-")
    print(f"R$ {salario_liquido:.2f}")


def pegar_qualificacao_valida(texto = "qualificação: "):
    qualificao = input(texto)
    opcoes = ["E", "M", "D"]

    if qualificao not in opcoes:
        print(f"opções válidas: E - especialização, M - mestrado e D - doutorado.")

        qualificao = pegar_qualificacao_valida()

    return qualificao


if __name__ == "__main__":
    main()
