from get_functions import *

def sum_user_input():
    valores = []
    while True:
        valor = get_number("valor: ")
        valores.append(valor)
        awnser = get_valid_awnser("devo continuar: ")

        if awnser == "não":
            break
     
    sum = sum_values(valor, valores)

    print(f"soma dos valores = {sum}")

def sum_values(valor, valores):
    # somar valores
    
    sum = 0

    for valor in valores:
        sum += valor

    return sum
    

def get_valid_awnser(text):
  awnser = input(text)
  
  valid_awnser = ["sim", "não"]

  if awnser not in valid_awnser:
    print("respostas válidas: sim ou não")

    awnser = get_valid_awnser(text)

  return awnser


sum_user_input()