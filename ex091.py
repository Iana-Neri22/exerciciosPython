import random

jogador = {}

for c in range(0, 5):
    jogador['nome'] = 'Jogador ' + str(c)
    jogador['numero'] = random.randint(1, 6)
    jogador.copy()

print('Valores sorteados:')
for k, v in jogador.items():
        print(f'{v}')
