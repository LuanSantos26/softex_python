def main():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Qual operação você deseja realizar (+, -, *, /)? ")

        if operacao == "+":
            resultado = num1 + num2
        elif operacao == "-":
            resultado = num1 - num2
        elif operacao == "*":
            resultado = num1 * num2
        elif operacao == "/":
            resultado = num1 / num2
        else:
            print("Operação inválida. Escolha +, -, *, ou /.")
            return

        if resultado % 2 == 0:
            par_impar = "par"
        else:
            par_impar = "ímpar"

        if resultado >= 0:
            pos_neg = "positivo"
        else:
            pos_neg = "negativo"

        if resultado.is_integer():
            inteiro_decimal = "inteiro"
        else:
            inteiro_decimal = "decimal"

        print(f"Resultado: {resultado:.2f} ({par_impar}, {pos_neg}, {inteiro_decimal})")
    except ValueError:
        print("Entrada inválida. Digite números válidos.")

if __name__ == "__main__":
    main()
