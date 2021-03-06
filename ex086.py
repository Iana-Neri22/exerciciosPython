matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = 0
maiorValor = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]}]', end='')
        if matriz[l][c] % 2 == 0:
            somaPares += matriz[l][c]
    print()

for c in range(0, 3):
    if c == 0:
        maiorValor = matriz[1][c]
    elif matriz[1][c] > maiorValor:
        maiorValor = matriz[1][c]

print(f'A soma dos números pares é {somaPares}')
print(f'A soma dos valores da terceira coluna é: {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
print(f'O maior valor da segunda linha é {maiorValor}')
