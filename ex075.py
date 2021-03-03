primeiroNumero = int(input('Digite o primeiro número: '))
segundoNumero = int(input('Digite o segundo número: '))
terceiroNumero = int(input('Digite o terceiro número: '))
quartoNumero = int(input('Digite o quarto número: '))

tupla = (primeiroNumero, segundoNumero, terceiroNumero, quartoNumero)
numerosPares = []

for c in tupla:
    if c % 2 == 0:
        numerosPares.append(c)

print(f'Os valores digitados foram {tupla}')
print(f'O número nove apareceu {tupla.count(9)} vezes')
if tupla.__contains__(3):
    print(f'O primeiro número 3 foi digitado na posição {tupla.index(3)}')
else:
    print('O número 3 não foi digitado nenhuma vez')
print(f'Os números pares são {numerosPares}')
