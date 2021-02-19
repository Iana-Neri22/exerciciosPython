from random import choice

jogador = input('Digite papel, pedra ou tesoura: ').upper().strip()
lista = ['PEDRA', 'PAPEL', 'TESOURA']
computador = choice(lista)
print(computador)

if jogador == computador:
    print('Empate')
elif jogador == 'PEDRA' and computador == 'PAPEL':
    print('Computador Venceu')
elif jogador == 'PEDRA' and computador == 'TESOURA':
    print('Jogador venceu')
elif jogador == 'PAPEL' and computador == 'PEDRA':
    print('Jogador venceu')
elif jogador == 'PAPEL' and computador == 'TESOURA':
    print('Computador venceu')
elif jogador == 'TESOURA' and computador == 'PEDRA':
    print('Computador venceu')
elif jogador == 'TESOURA' and computador == 'PAPEL':
    print('Jogador venceu')



