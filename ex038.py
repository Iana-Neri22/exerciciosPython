primeiroNumero = int(input('Digite o primeiro número: '))
segundoNumero = int(input('Digite o segundo número: '))

if primeiroNumero > segundoNumero:
    print('O primeiro número é maior.')
elif segundoNumero > primeiroNumero:
    print('O segundo número é maior.')
else:
    print('Não existe valor maior, os dois são iguais.')
