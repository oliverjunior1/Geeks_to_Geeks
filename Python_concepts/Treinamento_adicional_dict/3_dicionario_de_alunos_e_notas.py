# Criar um dicionário com nomes de alunos e suas notas. Calcular a média geral.

alunos = {
    "Ana":8.5,
    "Bruno":7.0,
    "Joaquim":6.7,
    "Joao":7.5
}

soma = sum(alunos.values())
media = soma/len(alunos)

print(media)