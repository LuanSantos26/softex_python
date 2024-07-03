numeros = []
for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

soma = sum(numeros)
media = soma / len(numeros)

print(f"Soma dos números: {soma:.2f}")
print(f"Média dos números: {media:.2f}")



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
