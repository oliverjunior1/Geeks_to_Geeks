dicionario = {}

with open('dados.txt') as arquivo:
    for linha in arquivo:
        if ':' in linha:
            chave, valor = linha.strip().split(':',1)
            dicionario[chave.split()] = valor.split()

print(dicionario)