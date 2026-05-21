def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

def exibir_menu():
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")
    return input("Opção: ")

while True:
    opcao = exibir_menu()
    
    if opcao == '5':
        break
        
    if opcao in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Número 1: "))
            num2 = float(input("Número 2: "))
            
            if opcao == '1':
                print(soma(num1, num2))
            elif opcao == '2':
                print(subtracao(num1, num2))
            elif opcao == '3':
                print(multiplicacao(num1, num2))
            elif opcao == '4':
                print(divisao(num1, num2))
                
        except ValueError:
            print("Erro: Entrada inválida.")
    else:
        print("Opção inválida.")
