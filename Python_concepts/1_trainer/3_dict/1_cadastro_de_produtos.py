# Objetivo: Criar um dicionário com produtos e seus preços. Permitir ao usuário consultar o preço
# de um produto digitando o nome.

precos = {
    "teclado":14.99,
    "mouse":12.00,
    "notebook":2999.00,
    "gabinete":200.00
}

procurar_produto = input("Clique para procurar o produto: ")

if procurar_produto in precos:
    print(precos[procurar_produto])