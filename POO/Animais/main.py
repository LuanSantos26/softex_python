# Importações das classes
from animal import Animal
from mamifero import Mamifero
from ave import Ave
from reptil import Reptil

def main():
    # Criando instâncias dos animais
    leao = Mamifero("Leão", 5, True)
    papagaio = Ave("Papagaio", 2, True)
    cobra = Reptil("Cobra", 3, "escamas")

    # Testando os métodos
    leao.fazer_som()  # Saída: O mamífero está rugindo.
    leao.movimentar()  # Saída: O animal está se movimentando.

    papagaio.fazer_som()  # Saída: O animal está fazendo um som.
    papagaio.movimentar()  # Saída: A ave está voando.

    cobra.fazer_som()  # Saída: O animal está fazendo um som.
    cobra.movimentar()  # Saída: O réptil está rastejando.

if __name__ == "__main__":
    main()
