from get_functions import *

def main():
    ano_1 = get_valid_number("Digite um ano: ")
    ano_2 = get_valid_number("Digite outro ano: ")

    if ano_1 == ano_2:
        print(f"Digite anos diferentes. Digite-os novamente.")

        main()
    
    else:
        if ano_1 > ano_2:
            ano_menor = ano_2
            ano_maior = ano_1
        else:
            ano_menor = ano_1
            ano_maior = ano_2

        print(f"\nlista de anos bissextos entre {ano_menor} e {ano_maior}:")

        ano_atual = ano_menor

        while ano_atual < ano_maior:
            if eh_bissexto(ano_atual):
                print(ano_atual)

            ano_atual += 1


def eh_bissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


if __name__ == "__main__":
    main()
        
# def ano_bissexto(text):
#     ano = get_valid_value(text)

#     while True:
#         if ano % 4 == 0:
#             if ano % 100 == 0:
#                 if ano % 400 == 0:
#                     break
                
#                 else:
#                     print(f"{ano} não é um ano bissexto. Digite um ano novamente")

#                     ano = ano_bissexto(text)

#             else:
#                 break
                


#         else:
#             print(f"{ano} não é um ano bissexto. Digite um ano novamente.")

#             ano = ano_bissexto(text)

#     return ano


# if __name__ == "__main__":
#     main()


  
     



     

