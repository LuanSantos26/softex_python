def main():
    # Inicialização das variáveis
    notas = []
    soma = 0

    # Leitura das notas até que seja informado -1
    while True:
        nota = input("Digite uma nota (ou -1 para encerrar): ")
        if nota == "-1":
            break
        else:
            nota = float(nota)
            notas.append(nota)
            soma += nota

    # Quantidade de valores lidos
    quantidade = len(notas)
    print(f"Foram lidas {quantidade} notas.")

    # Exibição dos valores na ordem informada
    print("Notas na ordem informada:")
    for nota in notas:
        print(nota, end=" ")

    # Exibição dos valores na ordem inversa
    print("\nNotas na ordem inversa:")
    for nota in reversed(notas):
        print(nota, end=" ")

    # Cálculo da média
    if quantidade > 0:
        media = soma / quantidade
        print(f"\nMédia das notas: {media:.2f}")

        # Quantidade de valores acima da média
        acima_media = sum(1 for nota in notas if nota > media)
        print(f"Quantidade de notas acima da média: {acima_media}")

        # Quantidade de valores abaixo de sete
        abaixo_sete = sum(1 for nota in notas if nota < 7)
        print(f"Quantidade de notas abaixo de sete: {abaixo_sete}")
    else:
        print("Nenhuma nota foi informada.")
        
if __name__ == "__main__":
    main()
