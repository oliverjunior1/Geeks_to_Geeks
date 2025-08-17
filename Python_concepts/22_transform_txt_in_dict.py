dicionario = {}

with open('dados.txt', 'r') as arquivo:
    for linhas in arquivo:
        if ':' in linhas:
            chave, valor = linhas.strip().split(':', 1)
            dicionario[chave.strip()] = valor.strip()

print(dicionario)