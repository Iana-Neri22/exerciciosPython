numero = 0
soma = 0
contador = 0

while numero != 999:
    numero = int(input('Digite um número: '))
    if numero != 999:
        soma += numero
        contador += 1

print('Foram digitados {} números'.format(contador))
print('A soma entre eles foi de {}'.format(soma))
