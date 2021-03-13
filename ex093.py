jogador = {}

jogador['nome'] = input('Nome do jogador: ')
jogador['gols'] = []
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
total = 0

for c in range(0, partidas):
    jogador['gols'].append(int(input(f'Quantos gols na partida {c}? ')))
    total += jogador['gols'][c]

jogador['total'] = total

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')

print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')

for c, v in enumerate(jogador['gols']):
    print(f'Na partida {c}, fez {v} gols.')

print(f'Foi um total de {jogador["total"]} gols')
