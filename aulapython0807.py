lista_frutas = ['Manga', 'Jaca', 'Morango', 'Maça', 'Goiaba']
print(f'Minha lista completa >>>> {lista_frutas}')
print(f'{lista_frutas[2]} é o 3º elemento da minha lista')
lista_frutas[1] = 'Banana'
print(lista_frutas)

lista_frutas.append('Abacate')
print(lista_frutas)

del lista_frutas[2]
print(lista_frutas)

deletar = lista_frutas.pop(-1)
print(f'Foi removido o {deletar}, pois era o meu ultimo elemento')
print(lista_frutas)
print(f'Minha lista tem {len(lista_frutas)} elementos')

for i in range(len(lista_frutas)):
    if lista_frutas[i] != 'Banana':
        print(lista_frutas[i], end=', ')