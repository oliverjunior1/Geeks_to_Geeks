import random

choice = int(input("Choice 1 for lotofacil, and 2 for megasena: "))

def megasena():
    x = sorted(random.sample(range(1,61),6))
    return print(x)

def lotofacil():
    x = sorted(random.sample(range(1,26),15))
    return print(x)

match choice:
    case 1:
        lotofacil()
    case 2:
        megasena()
    case _:
        print("Invalid number, put 1 or 2!")
