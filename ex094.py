pessoas = []
continua = 'S'

while continua == 'S':

    nome = input('Nome: ')
    sexo = input('Sexo [M/F]: ').strip().upper()

    while sexo != 'M' and sexo != 'F':
        sexo = input('Sexo [M/F]: ').strip().upper()

    idade = int(input('Idade: '))

    pessoas.append({
        'nome': nome,
        'sexo': sexo,
        'idade': idade
    })

    continua = input('Quer continuar [S/N]? ').strip().upper()
    while continua != 'S' and continua != 'N':
        continua = input('Quer continuar [S/N]? ').strip().upper()

totalIdades = 0
totalPessoas = pessoas.__len__()
mulheresCadastradas = []

for pessoa in pessoas:
    totalIdades += pessoa['idade']

    if pessoa['sexo'] == 'F':
        mulheresCadastradas.append(pessoa['nome'])

media = totalIdades / totalPessoas

print(f'O grupo tem {totalPessoas} pessoas.')
print(f'A média de idade é de {media} anos.')
print(f'As mulheres cadastradas foram {mulheresCadastradas}')
print(f'Lista das pessoas que estão acima da média: ')

for pessoa in pessoas:
    if pessoa['idade'] > media:
        for k, v in pessoa.items():
            print(f'{k} = {v}', end=' ')
        print()
