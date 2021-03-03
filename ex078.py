numbers = [int(input('Digite um número: '))
    , int(input('Digite um número: '))
    , int(input('Digite um número: '))
    , int(input('Digite um número: '))
    , int(input('Digite um número: '))]

print(f'O maior valor digitado foi {max(numbers)} na posição {numbers.index(max(numbers))}')
print(f'O menos valor digitado foi {min(numbers)} na posição {numbers.index(min(numbers))}')
