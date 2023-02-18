# Recebendo os dados do usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operador = input("Digite o operador (+, -, *, /): ")

# Realizando o cálculo de acordo com o operador fornecido
if operador == "+":
    resultado = numero1 + numero2
elif operador == "-":
    resultado = numero1 - numero2
elif operador == "*":
    resultado = numero1 * numero2
elif operador == "/":
    resultado = numero1 / numero2
else:
    print("Operador inválido.")
    resultado = None

# Imprimindo o resultado ou a mensagem de erro, se necessário
if resultado is not None:
    print("Resultado: ", resultado)
