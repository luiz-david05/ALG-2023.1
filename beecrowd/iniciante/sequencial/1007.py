def main():
  valores = [int(input()) for _ in range(4)]

  diff = calculate_diff(*valores)

  print(f"DIFERENCA = {diff}")


def calculate_diff(a, b, c, d):
  return a * b - c * d


if __name__ == "__main__":
  main()

  
  # with open("1007.txt" , "r") as entrada:
  #   valores = [int(entrada.readline()) for _ in range(4)]