def main():
  valores = [float(input()) for _ in range(3)]

  salario = calculate_salary(*valores)

  print(f"NUMBER = {int(valores[0])}")
  print(f"SALARY = U$ {salario:.2f}")


def calculate_salary(number, hour, value_hour):
  return hour * value_hour


if __name__ == "__main__":
  main()

  # with open("1008.txt" , "r") as entrada:
  #   valores = [float(entrada.readline()) for _ in range(3)]