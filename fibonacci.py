def fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
        print(a, b)   
    return b == numero

def main():
    try: 
        numero_digitado = int(input('digite um numero inteiro para verificar se ele faz parte da sequencia Fibonacci: '))
        if fibonacci(numero_digitado):
            print(f"{numero_digitado} faz parte da sequencia Fibonacci")
        else:
            print(f"{numero_digitado} não faz parte da sequencia Fibonacci")
    except ValueError:
        print("número digitado não é inteiro.")


main()