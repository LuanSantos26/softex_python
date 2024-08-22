from conta import Conta_Bancaria

def main():
    titular = input("Digite o nome do titular da conta: ")
    senha = input("Digite a senha da conta: ")
    conta = Conta_Bancaria(titular, senha)

    while True:
        print("\nMenu:")
        print("1. Consultar Saldo")
        print("2. Depositar")
        print("3. Sacar")
        print("4. Alterar Senha")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            senha = input("Digite a senha: ")
            print(conta.consultar_saldo(senha))
        elif opcao == "2":
            valor = float(input("Digite o valor a ser depositado: "))
            senha = input("Digite a senha: ")
            print(conta.depositar(valor, senha))
        elif opcao == "3":
            valor = float(input("Digite o valor a ser sacado: "))
            senha = input("Digite a senha: ")
            print(conta.sacar(valor, senha))
        elif opcao == "4":
            senha_atual = input("Digite a senha atual: ")
            nova_senha = input("Digite a nova senha: ")
            print(conta.alterar_senha(senha_atual, nova_senha))
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

    main()
