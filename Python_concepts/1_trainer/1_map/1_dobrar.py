def triplicar(x):
    return x**3

y = [1,2,3,4,5]

z = map(triplicar, y)

print(list(z))