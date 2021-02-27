import random

contadorVitorias = 0
controle = ''

while True:

    valor = int(input('Diga um valor: '))
    parImpar = input('Par ou Ímpar? [P/I]').upper().strip()
    valorComputador = random.randint(0, 10)
    soma = valor + valorComputador

    if soma % 2 == 0:
        controle = 'P'
    else:
        controle = 'I'

    print(f'Você jogou {valor} e o computador {valorComputador}. Total de {soma} deu {controle}')

    if parImpar == controle:
        print('Você ganhou')
        contadorVitorias += 1
    else:
        print('Você perdeu')
        break

print(f'GAME OVER! Você venceu {contadorVitorias} vezes')