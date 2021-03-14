pessoas = []
continua = 'S'

while continua == 'S':

    pessoas.append({
    'nome': input('Nome: '),
    'sexo': input('Sexo [M/F]: ').strip().upper(),
    'idade': int(input('Idade: '))
    })

    continua = input('Quer continuar [S/N]? ').strip().upper()
    while continua != 'S' and continua != 'N':
        continua = input('Quer continuar [S/N]? ').strip().upper()

totalIdades = 0
totalPessoas = pessoas.count(pessoas)
mulheresCadastradas = []

for pessoa in pessoas:
    totalIdades += pessoa[]

media = totalIdades / totalPessoas

print(f'O grupo tem {totalPessoas} pessoas.')
print(f'A média de idade é de {media} anos.')
#print(f'As mulheres cadastradas foram {}')

