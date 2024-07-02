def main():
    try:
        numero = int(input("Digite um número inteiro menor que 1000: "))

        if numero >= 1000 or numero < 0:
            print("Número inválido. Digite um valor entre 0 e 999.")
            return

        centenas = numero // 100
        dezenas = (numero % 100) // 10
        unidades = numero % 10

        print(f"Centenas: {centenas}")
        print(f"Dezenas: {dezenas}")
        print(f"Unidades: {unidades}")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro válido.")

if __name__ == "__main__":
    main()
