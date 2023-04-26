def main():
  
  notas = [float(input()) for _ in range(3)]
  
  media = calculate_media_three_notes(*notas)

  print(f"MEDIA = {media:.1f}")


def calculate_media_three_notes(a, b, c):
  return ((a * 2) + (b * 3) + (c * 5)) / 10


if __name__ == "__main__":
  main()


# O asterisco (*) antes de um objeto em Python é o operador de desempacotamento, que é usado para desempacotar iteráveis (como listas, tuplas, etc.) em argumentos separados em uma chamada de função.
# operador de desempacotamento "*"
# Usando o operador de desempacotamento, podemos passar uma lista (ou outra estrutura de dados iterável) como argumento para uma função de forma mais conveniente e legível.


# Se não usássemos o operador de desempacotamento, teríamos que passar cada elemento da lista separadamente, como em calculate_media_three_notes(notas[0], notas[1], notas[2]). Isso pode se tornar tedioso e difícil de ler se a lista for grande ou se tivermos muitas variáveis separadas para passar como argumentos.

  # with open("1006.txt" , "r") as entrada:
  #   notas = [float(entrada.readline()) for _ in range(3)]