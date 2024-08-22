from conta_bancaria import Conta_Bancaria
class Conta_corrente(Conta_Bancaria):
    def __init__(self, titular, senha, limite):
        super().__init__(titular, senha)
        self.limite = limite 
        
    def sacar(self, valor):
        if valor < self.__saldo + self.limite:
            self.__saldo -= valor
        return False