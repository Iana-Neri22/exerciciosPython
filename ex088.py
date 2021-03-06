from random import sample

numeroJogos = int(input('Quantos jogos você quer que eu sorteie? '))
lista = []

for c in range(0, numeroJogos):
    lista.append(sample(range(1, 60), 6))

for c, listas in enumerate(lista):
    lista[c].sort()
    print(f'Jogo {c + 1}: {lista[c]}')
