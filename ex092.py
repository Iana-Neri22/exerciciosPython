import datetime

anoAtual = datetime.datetime.now().year
pessoa = {}

pessoa['nome'] = input('Nome: ')
anoNascimento = int(input('Ano de nascimento: '))
pessoa['idade'] = anoAtual - anoNascimento
pessoa['ctps'] = int(input('Carteira de Trabalho: (0 não tem): '))

if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário R$'))
    pessoa['aposentadoria'] = (pessoa['contratação'] + 35) - anoNascimento

for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')
