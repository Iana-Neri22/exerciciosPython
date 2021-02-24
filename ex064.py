numero = 0
soma = 0
contador = 0

while numero != 999:
    numero = int(input('Digite um número: '))
    contador += 1
    if numero != 999:
        soma += numero

print('Foram digitados {} números'.format(contador))
print('A soma entre eles foi de {}'.format(numero))
