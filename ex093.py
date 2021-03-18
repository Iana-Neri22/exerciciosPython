jogadores = []
jogador = {}
controle = 'S'
contador = 0

while controle == 'S':
    jogador['cod'] = contador
    jogador['nome'] = input('Nome do jogador: ')
    jogador['gols'] = []
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    total = 0
    contador += 1

    for c in range(0, partidas):
        jogador['gols'].append(int(input(f'Quantos gols na partida {c}? ')))
        total += jogador['gols'][c]

    jogador['total'] = total

    jogadores.append(jogador.copy())

    controle = input('Quer continuar [S/N]? ').upper().strip()

for jogador in jogadores:
        print(f'{jogador}')


mostrarDados = int(input('Mostrar dados de qual jogador?'))
while mostrarDados > jogadores.__len__():
    mostrarDados = int(input('Mostrar dados de qual jogador?'))

while mostrarDados != 999:
    print(f'Levantamento do jogador {jogadores[mostrarDados]["nome"]}')
    for c, v in enumerate(jogadores[mostrarDados]['gols']):
        print(f'No jogo {c} fez {v} gols.')

    mostrarDados = int(input('Mostrar dados de qual jogador? [999 para]'))
    if mostrarDados > jogadores.__len__():
        print('Código Inválido')
        mostrarDados = int(input('Mostrar dados de qual jogador? [999 para]'))

print('Programa encerrado.')


