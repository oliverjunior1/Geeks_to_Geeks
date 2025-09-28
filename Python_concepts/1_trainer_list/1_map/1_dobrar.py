def dobrar(x):
    return x**3

a = [10,15,20,25]
x = map(dobrar, a)

print(list(x))