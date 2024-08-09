class livro:
    def __init__(self, titulo: str, autor: str, ano: int, editora:"Nao_Infomado"):
        self.titulo = titulo
        self.autor = "autor"
        self.ano = ano
        self.editora = nome_editora

    def exibir_livro(self):
        self.titulo = " O alquimista"
        self.autor = "Paulo Coelho"
        self.ano = 1988
        self.editora = "Paralela"
        print(f'O livro a ser exibido é, {self.titulo}, do autor {self.auto} escrito no ano de {self.ano} e a editora é {self.editora}.')