frutas=["pessego", "maça", "abacaxi","uva", "laranja" ]
print(frutas[2])
frutas.append("abacate")#acrescenta algo na lista no ultimo indice.
print(frutas)
frutas.insert(1,"banana")#acrescenta na ordem desejada na lista ou apenas modifica o indice.
print(frutas)
frutas.remove("abacaxi") #remove algo da lista.
print(frutas)
frutas.pop(4)#O método pop deve ser utilizado para remover um elemento com um índice específico.
print(frutas[-1])
#del frutas [0:1]
#print(frutas)
for i in range (len(frutas)):
    print(frutas[i])

for i in range (len(frutas)):
    if frutas != 'banana':
        print(frutas)