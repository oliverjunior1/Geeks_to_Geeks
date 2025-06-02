import random

def luck():
    x = sorted(random.sample(range(1,61),6))
    return print(x)

luck()