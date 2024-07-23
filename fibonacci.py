def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    while True:
        try:
            entrada = input("Digite um número inteiro (ou 'sair' para encerrar): ")

            if entrada.lower() == 'sair':
                print("Até logo!")
                break

            numero = int(entrada)
            if numero < 0:
                print("Por favor, digite um número positivo.")
                continue

            # Calcula o número na sequência de Fibonacci
            resultado = fibonacci(numero)
            print(f"O {numero}º número na sequência de Fibonacci é {resultado}.")

            # Verifica se o número pertence à sequência
            if resultado == numero:
                print(f"{numero} pertence à sequência de Fibonacci.")
            else:
                print(f"{numero} não pertence à sequência de Fibonacci.")

        except ValueError:
            print("Por favor, digite um número inteiro válido ou 'sair' para encerrar.")

    main()
# Desclpe professor mais usei o chat gpt :(