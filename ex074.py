import random

tupla = (random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9), random.randint(1, 9))

print(f'Os valores sorteados foram: {tupla}')
print(f'O menor valor sorteado foi: {min(tupla)}')
print(f'O maior valor sorteado foi: {max(tupla)}')
