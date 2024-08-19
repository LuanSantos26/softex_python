class conta_bancaria:
    def __init__(self, titular, saldo, consultar_saldo, depositar, sacar, validar_senha, alterar_senha):
        self.titular = titular
        self.saldo = saldo
        self.consultar_saldo = consultar_saldo
        self.depositar = depositar
        self.sacar = sacar
        self.validar_senha = validar_senha
        self.alterar_senha = alterar_senha
        
    def exibir_saldo():
        print (f'Ola {self.titular} seu saldo é de {self.saldo}')