numero = int(input('Digite um número: '))
multiplicador = numero - 1
soma = 0

while not multiplicador == 1:
    if soma == 0:
        soma += numero * multiplicador
    else:
        soma += soma * multiplicador
    multiplicador -= 1

print('O fatorial de {} é {}'.format(numero, soma))
