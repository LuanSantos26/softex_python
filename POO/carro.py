class Carro:
    #caracteristica - atributos - variavel
    marca = "Honda"
    modelo = "Civic"
    ano = 2010
    cor = "Preto"
    velocidade = 0
    #comportamentos - métodos -> funções
    def exibir_infos(self):
        self.marca = "Honda"
        self.modelo = "Civic"
        self.ano = 2010
        self.cor = "Preto"
        self.velocidade = 0
        print(f"Marca: {self.marca} , Modelo: {self.modelo} ,ano: {self.ano} ,cor: {self.cor} ,velocidade:{self.velocidade} mk/h ")
        

#alt + seta move o codigo...