import random

def mega():
    x = sorted(random.sample(range(1,61), 6))
    return x

print(mega())