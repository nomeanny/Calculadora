# Defina as operações matematicas
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero"
    return a / b

#Crie um menu para a calculadora
print("Calculadora em Python")
print("---------------------")

while True:
    print("Selecione uma opção: ")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = soma(num1, num2)
        print("Resultado:",  resultado)

    elif opcao == "2":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = subtracao(num1, num2)
        print("Resultado:",  resultado)

    elif opcao == "3":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = multiplicacao(num1, num2)
        print("Resultado:",  resultado)

    elif opcao == "4":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = divisao(num1, num2)
        print("Resultado:",  resultado)

    elif opcao == "5":
        print("Até logo!")
        break

    else:
        print("Opção inválida. Por favor, tente novamente.")