from random import randrange

randomNumber = randrange(11)
choosenNumber = ""
contador = 0

while not (randomNumber == choosenNumber):
    choosenNumber = int(input('Escreva um número de 0 a 10: '))
    contador += 1

print('Você ganhou!')
print('Foram necessários {} palpite(s)'.format(contador))
