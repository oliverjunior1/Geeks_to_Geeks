# import time
# time.sleep(5)
# print("Estamos voltando")

sum = 0
while True:
  num = int(input("coloque os números para ver a soma ou 00 para sair: "))
  if num != 00:
    sum += num
  else:
    print(sum)
    break