# 🧩 Exercício: Calculadora Flexível
# Crie uma função chamada calculadora_flexivel  que aceita:
# • 	Um número indefinido de valores numéricos via *args.
# • 	Um argumento nomeado obrigatório chamado operacao via **kwargs, que pode ser "soma", "subtracao","multiplicação"  ou "divisao".

def calculadora_flexivel(*args, **kwargs):
    operacao = kwargs.get("operacao")
    if not operacao:
        return "Erro: operação não informada."
    if not args:
        return None

    resultado = args[0]
    for a in args[1:]:
        match operacao:
            case "soma":
                resultado += a
            case "subtracao":
                resultado -= a
            case "multiplicacao":
                resultado *= a
            case "divisao":
                resultado /= a
            case _:
                return "Erro: operação inválida."
    return resultado

# Teste
print(calculadora_flexivel(1, 2, 3, 4, operacao='multiplicacao'))  # Deve retornar 24



# A função deve:
# 1. 	Verificar qual operação foi solicitada.
# 2. 	Aplicar essa operação sobre os valores recebidos em *args.
# 3. 	Retornar o resultado final.
# 💡 Exemplo de chamada da função