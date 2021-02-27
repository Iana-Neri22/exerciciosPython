import math

valorSaque = int(input('Qual valor você quer sacar? R$'))
total = valorSaque
contador50 = 0
contador20 = 0
contador10 = 0
contador1 = 0

if valorSaque >= 50:
    contador50 += math.floor(valorSaque / 50)
    valorSaque = valorSaque % 50
    print(f'Total de {contador50:.0f} cédulas de R$50')

if valorSaque >= 20:
    contador20 += math.floor(valorSaque / 20)
    valorSaque = valorSaque % 20
    print(f'Total de {contador20:.0f} cédulas de R$20')

if valorSaque >= 10:
    contador10 += math.floor(valorSaque / 10)
    valorSaque = valorSaque % 10
    print(f'Total de {contador10:.0f} cédulas de R$10')

if valorSaque > 0 and valorSaque < 10:
    contador1 += math.floor(valorSaque / 1)
    print(f'Total de {contador1:.0f} cédulas de R$1')