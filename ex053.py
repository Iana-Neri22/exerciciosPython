frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::1]

if junto == inverso:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')

