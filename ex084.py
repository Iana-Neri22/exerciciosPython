lista = []
controle = 'S'
listaLeves = []
listaPesados = []
maiorPeso = 0
menorPeso = 0

while True:
    lista.append([
        input('Digite o nome: '),
        float(input('Digite o peso: '))
    ])

    controle = input('Deseja continuar? [S/N]').strip().upper()
    while controle != 'S' and controle != 'N':
        controle = input('Deseja continuar? [S/N]').strip().upper()

    if controle == 'N':
        break

for c, pessoa in enumerate(lista):
    if c == 0:
        maiorPeso = pessoa[1]
        menorPeso = pessoa[1]
    elif pessoa[1] > maiorPeso:
        maiorPeso = pessoa[1]
    elif pessoa[1] < menorPeso:
        menorPeso = pessoa[1]

for pessoa in lista:
    if pessoa[1] == maiorPeso:
        listaPesados.append(pessoa[0])
    elif pessoa[1] == menorPeso:
        listaLeves.append(pessoa[0])


print(f'Foram cadastradas {len(lista)} pessoas')
print(f'O maior peso foi de {maiorPeso}. Peso de {listaPesados}')
print(f'O menor peso foi de {menorPeso}. Peso de {listaLeves}')
