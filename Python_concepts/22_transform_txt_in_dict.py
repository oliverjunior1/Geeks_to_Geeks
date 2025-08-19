dicionario = {}
with open('dados.txt', 'r') as archive:
    for line in archive:
        if ':' in line:
            x, y = line.strip().split(':',1)
            dicionario[x.strip()] = y.strip()

print(dicionario)