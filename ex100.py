import random

def sorteia(numeros):
    for c in range(0, 5):
        numeros.append(random.randint(0, 9))

def somaPar(numeros):
    soma = 0

    for numero in numeros:
        if numero % 2 == 0:
            soma += numero
    print(f'Somando os valores pares de {numeros}, temos {soma}.')

numeros = []
sorteia(numeros)
somaPar(numeros)
