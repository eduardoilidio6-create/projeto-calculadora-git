"""
Módulo de Calculadora Científica/Básica em Python

"""

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("Erro: Não é possível dividir por zero.")
    return a / b

def exibir_menu():
    print("\n--- CALCULADORA COLABORATIVA ---")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("0. Sair")

def main():
    while True:
        exibir_menu()
        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao == 0:
                print("Encerrando a calculadora. Até logo!")
                break
            
            if opcao in [1, 2, 3, 4]:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
                
                if opcao == 1:
                    print(f"Resultado: {num1} + {num2} = {somar(num1, num2)}")
                elif opcao == 2:
                    print(f"Resultado: {num1} - {num2} = {subtrair(num1, num2)}")
                elif opcao == 3:
                    print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
                elif opcao == 4:
                    try:
                        print(f"Resultado: {num1} / {num2} = {dividir(num1, num2)}")
                    except ValueError as e:
                        print(e)
            else:
                print("Opção inválida! Escolha um número entre 0 e 4.")
        except ValueError:
            print("Entrada inválida! Por favor, digite números válidos.")

if __name__ == "__main__":
    main()
