def main():
     
     quantidades=5
     soma=0
     for i in range (quantidades):
         numero=int(input(f"digite o {i+1} numero: "))
         soma=soma+numero
     media=soma/quantidades

     print("soma:", soma)
     print("edia:", media)
main()


# Solicita ao usuário para digitar 5 números
numeros = []
for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

# Encontra o maior número na lista
maior_numero = numeros[0]
for num in numeros:
    if num > maior_numero:
        maior_numero = num

# Exibe o maior número
print(f"O maior número é: {maior_numero:.2f}")

