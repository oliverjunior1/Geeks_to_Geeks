#🧠 Desafio: Criando um sistema de pedidos de lanche
# Imagine que você está desenvolvendo um sistema para registrar pedidos em uma lanchonete. Cada pedido pode ter:
# - Vários itens (hambúrguer, batata, refrigerante…)
# - E várias opções extras (como tamanho, tipo de pão, molho, etc.)
# Você vai usar *args para os itens do pedido e **kwargs para os detalhes extras.
#
# 🧪 Exercício
# Crie uma função chamada  que aceite:
# • 	Qualquer número de itens como argumentos posicionais ()
# • 	Qualquer número de opções extras como argumentos nomeados ()
# A função deve:
# 1. 	Imprimir os itens do pedido.
# 2. 	Imprimir os detalhes extras.
# 3. 	Retornar uma string formatada com o resumo do pedido.

def registrar_pedido(*args, **kwargs):
    print("Itens do pedido:")
    for item in args:
        print(f"- {item}")

    print("\nDetalhes extras:")
    for chave, valor in kwargs.items():
        print(f"- {chave}: {valor}")

    resumo = f"\nResumo: Pedido com {len(args)} itens e {len(kwargs)} opções extras registrado com sucesso!"
    return resumo


# Exemplo de uso
resposta = registrar_pedido(
    "hambúrguer", "batata frita",
    bebida="refrigerante",
    tamanho="grande",
    molho="barbecue"
)

print(resposta)