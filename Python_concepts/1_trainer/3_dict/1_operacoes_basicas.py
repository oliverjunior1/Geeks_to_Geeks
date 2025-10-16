# Objetivo: Contar quantas vezes cada palavra aparece em uma frase
# digitada pelo usuário.

a = {
    'x':1,
    'y':2,
    'z':3,
    'w':4
}

# Acessar valor pela chave
print(a['x'])

# Adicionar novo par
a['b']=5
print(a)

# Alterar valor
a['y'] = 5
print(a)

# Remover chave
del a['b']
print(a)

# Ver todas as chaves
print(a.keys())

# Ver todos os valores
print(a.values())

# Ver todos os pares
print(a.items())