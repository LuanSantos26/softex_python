import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    numeros_tentados = []

    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número secreto entre 1 e 100.")

    while True:
        try:
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1
            numeros_tentados.append(palpite)

            if palpite < numero_secreto:
                print("Tente um número maior.")
            elif palpite > numero_secreto:
                print("Tente um número menor.")
            else:
                print(f"Parabéns! Você acertou o número secreto {numero_secreto} em {tentativas} tentativas.")
                print(f"Números que você tentou: {numeros_tentados}")
                break
        except ValueError:
            print("Por favor, digite um número válido.")

jogo_adivinhacao()
