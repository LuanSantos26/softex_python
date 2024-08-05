    #caracteristica - atributos - variavel
class Carro:
    def __init__(self, marca, modelo, ano, cor, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = velocidade
    #comportamentos - métodos -> funções
    def exibir_infos(self):
        marca = "Honda"
        modelo = "Civic"
        ano = 2010
        cor = "Preto"
        velocidade = 0
        print(f"Marca: {self.marca} , Modelo: {self.modelo} ,ano: {self.ano} ,cor: {self.cor} ,velocidade:{self.velocidade} mk/h ")
        

#alt + seta move o codigo...