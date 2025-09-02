dicionario = {}

with open('dados.txt', 'r') as archivo:
    for line in archivo:
        if ':' in line:
            chave, valor = line.strip().split(':', 1)
            archivo[chave.strip()] = valor.strip()

print(dicionario)