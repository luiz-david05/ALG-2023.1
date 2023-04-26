def main():
    nome_vendedor = input()
    valores = [float(input()) for _ in range(2)]

    salario_bonus = calculate_salary_with_bonus(*valores)

    print(f"TOTAL = R$ {salario_bonus:.2f}")

def calculate_salary_with_bonus(salario, vendas):
  comissao = vendas * 0.15
  salario_bonus = salario + comissao

  return salario_bonus


if __name__ == "__main__":
   main()

    # with open("1009.txt" , "r") as entrada:
    #   nome_vendedor = entrada.readline()
    #   valores = [float(entrada.readline()) for _ in range(2)]