def leiaInt(frase):
    valor = ''

    while type(valor) != int:
        try:
            valor = int(input(frase))
        except ValueError:
            print('ERRO: Por favor, digite um número inteiro válido.')

    return valor

def leiaFloat(frase):
    valor = ''

    while type(valor) != float:
        try:
            valor = float(input(frase))
        except ValueError:
            print('ERRO: Por favor, digite um número real válido.')

    return valor


inteiro = leiaInt('Digite um inteiro: ')
real = leiaFloat('Digite um real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')