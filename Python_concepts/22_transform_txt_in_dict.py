dicionario = {}

with open("dados.txt", 'r') as arquivo:
    for line in arquivo:
        if ':' in line:
            chave, valor = line.strip().split(':',1)
            dicionario[chave.strip()] = valor.strip()

print(dicionario)