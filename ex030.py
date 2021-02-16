numero = int(input('Digite um número inteiro:'))
resto = numero % 2

print('O número {} é par'.format(numero) if resto == 0 else 'O número {} é impar'.format(numero))
