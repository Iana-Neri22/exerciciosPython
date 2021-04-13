def leiaInt(frase):
    valor = input(frase)
    if valor.isnumeric() == False:
        print('Valor não é numérico')
        valor = input(frase)
    return valor


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
