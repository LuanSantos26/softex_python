class carro:
    #caracteristica - atributos - variavel
    marca = "Civic"
    modelo = "Honda"
    ano = 2010
    cor = "Preto"
    velocidade = 0
    #comportamentos - métodos -> funções
    def acelerar(self, velocidade_nova):
        self.velocidade += velocidade_nova
        print(f"O carro acelerou para {self.velocidade} km/h")
        if self.velocidade > 200:
            print("Velocidade excedida!")


#alt + seta move o codigo...