frase = input('Digite uma frase: ').strip().upper()
print('A letra a aparece {} vezes'.format(frase.count('A')))
print('A letra a aparece a primeira vez na posição {}'.format(frase.find('A')))
print('A letra a aparece pela última vez na posição {}'.format(frase.rfind('A')))


