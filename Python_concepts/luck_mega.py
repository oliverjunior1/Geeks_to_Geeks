import random

def luck_sena():
    x = random.sample(range(1,61), 6)
    return sorted(x)
y = luck_sena()
print(f"The luck numbers for the megasena are: {y}")