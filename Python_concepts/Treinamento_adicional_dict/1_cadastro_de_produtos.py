produtos = {
    "mouse":50.0,
    "teclado":120.0,
    "monitor":899.99
}

nome = input("Digite o nome do produto: ").lower()

if nome in produtos:
    print(f"Preço: R$ {produtos[nome]:.2f}")
else:
    print("Produto não encontrado.")