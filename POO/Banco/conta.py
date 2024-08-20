class conta:
    def __init__(self, titular, saldo, senha):
        self.titular = titular
        self.__saldo = saldo
        self.__senha = senha
        
    def exibir_saldo():
        print (f'Ola {self.titular} seu saldo é de {self.saldo}')