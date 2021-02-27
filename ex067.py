numero = 0

while numero >= 0:
    numero = int(input('Quer ver a tabuada de qual valor?'))

    if numero < 0:
        break

    contador = 1
    while contador <= 10:
        print(f'{numero} x {contador} = {numero * contador}')
        contador += 1
print('Encerrado')
