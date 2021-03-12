jogador = {}

jogador['nome'] = input('Nome do jogador: ')
jogador['gols'] = []
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))

for c in (0, partidas):
    jogador['gols'].append(int(input(f'Quantos gols na partida {c}? ')))

for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')

print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
