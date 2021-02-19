frase = input('Digite uma frase: ').strip()
fraseInvertida = frase[::-1].strip()

print(frase)
print(fraseInvertida)

if frase == fraseInvertida:
    print('É um políndromo')
else:
    print('Não é um políndromo')

