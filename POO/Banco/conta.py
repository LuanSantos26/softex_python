class Conta_Bancaria:
    def __init__(self, titular, senha):
        self.titular = titular
        self.__saldo = 0
        self.__senha = senha

    def consultar_saldo(self, senha):
        if self.__validar_senha(senha):
            return f"Saldo: R${self.__saldo:.2f}"
        else:
            return "Senha incorreta."

    def depositar(self, valor, senha):
        if self.__validar_senha(senha):
            if valor > 0:
                self.__saldo += valor
                return f"Depósito de R${valor:.2f} realizado com sucesso."
            else:
                return "Valor de depósito inválido."
        else:
            return "Senha incorreta."

    def sacar(self, valor, senha):
        if self.__validar_senha(senha):
            if 0 < valor <= self.__saldo:
                self.__saldo -= valor
                return f"Saque de R${valor:.2f} realizado com sucesso."
            else:
                return "Saldo insuficiente ou valor de saque inválido."
        else:
            return "Senha incorreta."

    def alterar_senha(self, senha_atual, nova_senha):
        if self.__validar_senha(senha_atual):
            self.__senha = nova_senha
            return "Senha alterada com sucesso."
        else:
            return "Senha atual incorreta."

    def __validar_senha(self, senha):
        return self.__senha == senha