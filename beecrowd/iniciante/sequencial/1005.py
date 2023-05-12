def main():
  a, b = [float(input()) for _ in range(2)]

  media = calculate_media(a, b)

  print(f"MEDIA = {media:.5f}")


def calculate_media(n1, n2):
  return ((n1 * 3.5) + (n2 * 7.5)) / 11


if __name__ == "__main__":
  main()

  
  
  # with open("1005.txt", "r") as entrada:
  #   a = float(entrada.readline())
  #   b = float(entrada.readline())