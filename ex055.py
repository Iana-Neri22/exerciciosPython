maiorPeso = 0
menorPeso = 1000

for c in range(0, 5):
    peso = float(input('Digite o peso em kg:'))

    if peso > maiorPeso:
        maiorPeso = peso
    if peso < menorPeso:
        menorPeso = peso

print('O maior peso foi {}kg e o menor peso foi {}kg'.format(maiorPeso, menorPeso))
