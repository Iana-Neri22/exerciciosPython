lista = [[], []]

for c in range(0, 7):
    numero = int(input('Digite um número:'))

    if numero % 2 == 0:
        lista[0].append(numero)
    else:
        lista[1].append(numero)

lista[0].sort()
lista[1].sort()

print(f'Os valores digitados pares foram {lista[0]}')
print(f'Os valores digitados ímpares foram {lista[1]}')
