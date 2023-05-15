from get_functions import *
import math

def main():
    nome_professor = input("nome do professor: ")
    horas_semanais = get_number("horas semanais: ")
    valor_base_hora = get_number("valor da hora: ")
    qualificacao = pegar_qualificacao_valida()
    tempo_experiencia = get_number("tempo de experiência em meses: ")
    filhos_menores = get_number("número de filhos menores que 6 anos: ")
    valor_plano_saude = get_number("valor do plano de saúde: ")

    percentual_bonus_qualificacao = pegar_percentual_qualificacao(qualificacao)

    # incrementado no valor das horas
    valor_base_hora += valor_base_hora * percentual_bonus_qualificacao

    # bonus por tempo de experiência
    tempo_experiencia_anos = tempo_experiencia // 12
    bonus_experiencia = tempo_experiencia_anos * 0.05

    if tempo_experiencia % 12 > 6:
        tempo_experiencia_anos += 1
        bonus_experiencia = tempo_experiencia_anos * 0.05
    

    # incrementar no valor das horas
    valor_base_hora += valor_base_hora * bonus_experiencia

    # bonus por filhos menores
    bonus_filhos = 0
    if filhos_menores > 0:
        bonus_filhos = filhos_menores * 700

    # ressarcer plano de saúde
    valor_renassarcimento_plano_saude = valor_plano_saude * 0.05
    if valor_plano_saude >= 1000:
        valor_renassarcimento_plano_saude = 500

    # auxilio combustivel
    auxilio_combustivel = math.floor( horas_semanais / 8 * 30)

    # salario base semanal
    salario_base_semanal = valor_base_hora * horas_semanais

    # salario base mensal
    salario_base_mensal = salario_base_semanal * 4.5 + bonus_filhos + valor_renassarcimento_plano_saude + auxilio_combustivel

    # salario bruto
    salario_bruto = salario_base_mensal

    # calcular inss
    inss = 0
    if salario_base_mensal <= 1302:
        inss = salario_base_mensal * 0.075
    elif salario_base_mensal <= 2500:
        inss = salario_base_mensal * 0.09
    elif salario_base_mensal <= 3900:
        inss = salario_base_mensal * 0.12
    elif salario_base_mensal <= 7500:
        inss = salario_base_mensal * 0.14
    else:
        inss = salario_base_mensal * 0.16

    salario_liquido = salario_base_mensal - inss

    # calcular ir
    ir = 0
    if salario_liquido > 5000:
        ir = (salario_liquido - 2000) * 0.275

    # salario liquido
    salario_liquido = salario_liquido - ir
    # mostrar resultados na tela
    print(5 * "=", "FOLHA DE PAGAMENTO", 5 * "=")
    print(f"professor: {nome_professor}")
    print(f"valor base hora: R$ {valor_base_hora:.2f}")
    print(f"salário base semanal: R$ {salario_base_semanal:.2f}")
    print(f"salário base mensal: R$ {salario_base_mensal:.2f}")
    print(" --- bônus ---")
    print(f"bônus qualificação: {percentual_bonus_qualificacao * 100:.2f}%")
    print(f"bônus experiência: {bonus_experiencia * 100:.2f}%")
    print(f"bônus filhos: R$ {bonus_filhos:.2f}")
    print(f"renassarcimento plano de saúde: R$ {valor_renassarcimento_plano_saude:.2f}")
    print(f"auxílio combustível: R$ {auxilio_combustivel:.2f}")
    print(f"salário bruto: R$ {salario_bruto:.2f}")
    print(" --- descontos ---")
    print(f"INSS: R$ {inss:.2f}")
    print(f"IR: R$ {ir:.2f}")
    print(f"salário líquido: R$ {salario_liquido:.2f}")


def pegar_qualificacao_valida(texto = "qualificação: "):
    qualificacoes_validas = ["especialização", "mestrado", "doutorado"]

    qualificacao = input(texto)

    if qualificacao not in qualificacoes_validas:
        print("qualificação inválida, qualificações válidas: especialização, mestrado ou doutorado")

        qualificacao = pegar_qualificacao_valida(texto)
    
    return qualificacao


def pegar_percentual_qualificacao(qualificacao):
    if qualificacao == "especialização":
        valor_bonus_qualificacao = 0.20
    elif qualificacao == "mestrado":
        valor_bonus_qualificacao = 0.30
    elif qualificacao == "doutorado":
        valor_bonus_qualificacao = 0.50

    return valor_bonus_qualificacao


if __name__ == "__main__": 
    main()