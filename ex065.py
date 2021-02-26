fechar = 'S'
contadorNumeros = 0
soma = 0
maiorNumero = 0
menorNumero = 0

while fechar != 'N':
    numero = int(input('Digite um número:'))
    contadorNumeros += 1
    soma += numero

    if numero > maiorNumero:
        maiorNumero = numero
    if contadorNumeros == 1:
        menorNumero = numero
    elif numero < menorNumero:
        menorNumero = numero

    fechar = input('Quer continuar? [S/N]').upper().strip()

media = soma / contadorNumeros
print('Você digitou {} números e a média foi {}'.format(contadorNumeros, media))
print('O maior valor foi {} e o menor foi {}'.format(maiorNumero, menorNumero))