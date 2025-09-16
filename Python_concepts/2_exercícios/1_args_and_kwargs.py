'''Exercício: Função de Cadastro de Usuário
Crie uma função chamada cadastrar_usuario que aceita:
• 	Um número indefinido de argumentos posicionais (*args) representando hobbies do usuário.
• 	Um número indefinido de argumentos nomeados (**kwargs) representando informações pessoais como nome, idade, cidade, etc.
A função deve:
1. 	Imprimir as informações pessoais de forma organizada.
2. 	Imprimir a lista de hobbies, um por linha.'''

# criar a funcao cadastro de usuário
def cadastrar_usuario(*args, **kwargs):
    contadora = 0
    contadorb = 0
    for x in args:
        print(f"Hobbies do usuário: {x}")
    for a in kwargs:
        print(f"{a}:{kwargs[a]}")


cadastrar_usuario('futebol', 'video game', nome='Joaquim', altura=1.74)