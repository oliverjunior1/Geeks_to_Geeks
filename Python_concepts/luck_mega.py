import random

def luck():
    x = random.sample(range(1,61),6)
    return sorted(x)

x = luck()
print(x)