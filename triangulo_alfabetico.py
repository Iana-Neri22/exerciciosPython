n = int(input())
alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

contador = 1
index_alfabeto = 0
for i in range(1, n + 1):
    print(f'{alfabeto[index_alfabeto] * contador}')
    contador += 1
    index_alfabeto += 1
