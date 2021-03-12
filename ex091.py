import random

jogadores = []
jogador = {}

for c in range(0, 4):
    jogador['nome'] = 'Jogador ' + str(c + 1)
    jogador['numero'] = random.randint(1, 6)
    jogadores.append(jogador.copy())

print('Valores sorteados:')
for jogador in jogadores:
    for v in jogador.values():
        print(f'{v}', end=' ')
    print()

print('Ranking')
newlist = sorted(jogadores, key=lambda k: k['numero'], reverse=True)

for c, jogador in enumerate(newlist):
    print(f'{c + 1}º lugar: ', end='')
    for v in jogador.values():
        print(f'{v}', end=' ')
    print()