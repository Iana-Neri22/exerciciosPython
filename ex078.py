numbers = []

for c in range(0, 5):
    numbers.append(input('Digite um número: '))

highestNumbers = []
lowestNumbers = []
positionsHigh = []
positionsLow = []

print(f'O maior valor digitado foi {max(numbers)} na posição ', end='')
for i, number in enumerate(numbers):
    if number == max(numbers):
        print(i, end=' ')

print(f'\n O menor valor digitado foi {min(numbers)} na posição ', end='')
for i, number in enumerate(numbers):
    if number == min(numbers):
        print(i, end=' ')
