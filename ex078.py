numbers = [int(input('Digite um número: '))
    , int(input('Digite um número: '))
    , int(input('Digite um número: '))
    , int(input('Digite um número: '))
    , int(input('Digite um número: '))]

highestNumbers = []
lowestNumbers = []
positionsHigh = []
positionsLow = []

for c, number in enumerate(numbers):
    if c == 0:
        highestNumbers.append(number)
        lowestNumbers.append(number)
        positionsHigh.append(numbers.index(number))
        positionsLow.append(numbers.index(number))
    elif number > max(highestNumbers):
        highestNumbers.remove(max(highestNumbers))
        highestNumbers.append(number)
        positionsHigh.remove(max(positionsHigh))
        positionsHigh.append(number)
    elif number == max(highestNumbers):
        highestNumbers.append(number)
        positionsHigh.append(number)
    elif number < min(lowestNumbers):
        lowestNumbers.remove(min(lowestNumbers))
        lowestNumbers.append(number)
    elif number == min(lowestNumbers):
        lowestNumbers.append(number)


print(f'O maior valor digitado foi {max(numbers)} na posição {positionsHigh}')
print(f'O menor valor digitado foi {min(numbers)} na posição {numbers.index(min(numbers))}')
