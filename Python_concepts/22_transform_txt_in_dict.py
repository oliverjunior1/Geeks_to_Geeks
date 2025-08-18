dicionario = {}

with open('dados.txt', 'r') as arquivo:
    for line in arquivo:
        if ':' in line:
            x, y = line.strip().split(':',1)
            dicionario[x.strip()]=y.strip()


print(dicionario)