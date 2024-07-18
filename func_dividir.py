def dividir():
    try:
        numerador =  int(input('Digite o numerador desejado: '))
        denominador = int(input('Digite o denominador desejado: '))

        resultado = numerador/denominador

        print ('O resultado é ',resultado)
    except ZeroDivisionError:
        print('O denominado não pode ser 0.')
    except Exception:
        print ('Ocorreu um erro interno, fale com o suporte...')

dividir()