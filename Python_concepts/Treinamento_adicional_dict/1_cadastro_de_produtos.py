# Objetivo: Criar um dicionário com produtos e seus preços. Permitir ao usuário consultar o preço
# de um produto digitando o nome.

produtos = {
    "teclado":14.99,
    "mouse":14.50,
    "notebook":2599.99,
    "impressora":399.99
}

produto_search = input("Digite o produto para ver o preço? ")

if produto_search in produtos:
    print(produtos[produto_search])
else:
    print("Produto inválido")