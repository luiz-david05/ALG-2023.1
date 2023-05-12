from get_functions import *


def q1():
    n =  get_number("n: ")

    print(f"número inteiros entre 1 e {n}:")
    for i in range(1, n + 1):
        print(f">>> {i}")


def q2():
    n = get_number("n: ")

    print(f"número inteiros pares entre 1 e {n}:")
    for i in range(1, n + 1):
        if eh_par(i):
            print(f">>> {i}")


def q3():
    a0 = get_number("a0: ")
    limite = get_number("limite: ")
    razao = get_number("razão: ")

    i = a0
    print("termos geradsos pela pa:")
    for i in range(i, limite, razao):
        print(f">>> {i}")


def q4():
    a0 = get_number("a0: ")
    limite = get_number("limite: ")
    razao = get_number("razão: ")

    i = a0
    print("termos gerados pela pg:")
    for i in range(i, limite, razao * i):
        print(f">>> {i}")


q4()