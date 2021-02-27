numero = 0
soma = 0
contador = 0

while numero != 999:
    numero = int(input('Digite um número: (999 para parar)'))
    if numero == 999:
        break
    contador += 1
    soma += numero

print(f'Foram digitados {contador} números.')
print(f'A soma entre eles foi de {soma}')
