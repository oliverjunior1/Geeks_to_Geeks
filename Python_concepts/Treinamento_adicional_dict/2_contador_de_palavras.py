# Objetivo: Contar quantas vezes cada palavra aparece em uma frase
# digitada pelo usuário.

frase = input("Digite uma frase:")
palavras = frase.split()
contador = {}

for palavra in palavras:
    if palavra in contador:
        contador[palavra] += 1
    else:
        contador[palavra] = 1

print("Contagem de palavras:")
