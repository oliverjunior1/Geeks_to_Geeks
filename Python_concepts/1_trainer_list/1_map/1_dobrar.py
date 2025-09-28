def dobrar(x):
    return x*2

numeros = [1,2,3,4,5]
resultado = map(dobrar, numeros)

print(list(resultado))