def ficha(nome, qtdeGols):
    print(f'O jogador {nome} fez {qtdeGols} gols(s) no campeonato.')


nome = input('Nome do jogador: ')
qtdeGols = input('Número de gols: ')

if qtdeGols.isnumeric():
    qtdeGols = qtdeGols
else:
    qtdeGols = 0

if nome.strip() == '':
    nome = 'desconhecido'

ficha(nome, qtdeGols)
