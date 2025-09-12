frase = input("digite uma frase: ").lower()
palavras = frase.split()
contador = {}

for palavra in palavras:
    if palavra in contador:
        contador[palavra] += 1
    else:
        contador[palavra] = 1

print("Contagem de palavras:")
for k, v in contador.items():
    print(f"{k}: {v}")