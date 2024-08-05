CONSTANTE=3.14 # Em python não existe constante, apenas um acordo de boas praticas entre programadores, toda variavel escrita com caps lock é uma constante.
idade=25
nome="Luan"
print(f'meu nome é {nome} e eu tenho {idade} anos')
# o f serve para concatenar uma frase inteira usando variavel numericas e do tipo string.
print(int(idade))
preco="10.50"
print(float(preco))
print(nome,idade)
print(nome,idade, end= "...\n")# esse exemplo serve para quebra de linha.
print(nome,idade, sep= "#") # a hashtag serve como separador.