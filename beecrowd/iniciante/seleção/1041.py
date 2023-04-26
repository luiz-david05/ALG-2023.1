
def main():
    x, y = list(map(float, input().split(" ")))

    if x > 0 and y > 0:
        print("Q1")

    elif x < 0 and y > 0:
        print("Q2")
    
    elif x < 0 and y < 0:
        print("Q3")

    elif x > 0 and y < 0:
        print("Q4")

    elif x == 0 and y == 0:
        print("Origem")

    elif x == 0:
        print("Eixo Y")
    
    else:
        print("Eixo X")



if __name__ == "__main__":
    main()

    # with open("1041.txt" , "r") as entrada:
    #     x, y = list(map(float, entrada.readline().split(" ")))