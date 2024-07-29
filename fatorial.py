def fatorial():
    numero=int(input('Digite um numero para calcular fatorial: '))
    resultado=1

    if numero > 0:
        for n in range(1, numero+1):
         resultado *= n

        print(resultado)
    else:
        print('Não é possivel calcular fatorial de 0 ou você digitou uma letra.')
fatorial()