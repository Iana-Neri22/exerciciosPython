continua = 'S'
total = 0
mais1000 = 0
maisBaratoPreco = 0
maisBaratoNome = ''

while continua == 'S':
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o preço do produto: '))

    if total == 0:
        maisBaratoPreco = preco
        maisBaratoNome = nome
    elif preco < maisBaratoPreco:
        maisBaratoPreco = preco
        maisBaratoNome = nome

    total += preco

    if preco > 1000:
        mais1000 += 1

    continua = ''

    while continua != 'S' and continua != 'N':
        continua = input('Deseja continuar? [S/N]').strip().upper()

    if continua == 'N':
        break

print(f'O total gasto foi R${total:.2f}')
print(f'{mais1000} produtos custam mais de R$1000,00')
print(f'O produto mais barato foi {maisBaratoNome} que custa {maisBaratoPreco:.2f}')
