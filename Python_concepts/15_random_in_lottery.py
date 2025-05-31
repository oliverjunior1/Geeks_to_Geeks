import random

def loto_facil():
    x = sorted(random.sample(range(1,26), 15))
    return x

print(loto_facil())
