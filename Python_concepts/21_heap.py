nota_1 = float(input("Digite a nota 1: "))
nota_2 = float(input("Digite a nota 2: "))

media = (nota_1+nota_2)/2

if media == 10:
  print("Parabéns")
elif media >= 5:
  print("Aprovado")
else:
  print("Reprovado")