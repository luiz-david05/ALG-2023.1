def main():
      cod_1, qtd_1, value_1 = list(map(float, input().split(" ")))
      cod_2, qtd_2, value_2 = list(map(float, input().split(" ")))

      valor_prod_1 = calculate_prod_value(qtd_1, value_1)
      valor_prod_2 = calculate_prod_value(qtd_2, value_2)

      valor_total = valor_prod_1 + valor_prod_2

      print(f"VALOR A PAGAR: R$ {valor_total:.2f}")


def calculate_prod_value(qtt, value):
   return qtt * value


if __name__ == "__main__":
   main()

    # with open("1010.txt" , "r") as entrada:
    #   cod_1, qtd_1, value_1 = list(map(float, entrada.readline().split(" ")))
    #   cod_2, qtd_2, value_2 = list(map(float, entrada.readline().split(" ")))


