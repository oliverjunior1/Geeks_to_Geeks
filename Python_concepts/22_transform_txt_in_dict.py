dicionario = {}

with open("dados.txt", 'r') as arquivo:
    for linha in arquivo:
        if ':' in linha:
            chave, valor = linha.strip().split(':',1)
            dicionario[chave.strip()] = valor.strip()

print(dicionario)