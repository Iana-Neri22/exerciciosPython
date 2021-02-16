from random import randrange

randomNumber = randrange(6)
choosenNumber = int(input('Escreva um número de 0 a 5: '))

print('Você acertou o número era {}'.format(randomNumber) if randomNumber == choosenNumber else 'Você errou, era {}'.format(randomNumber))
