import datetime

anoNascimento = int(input('Digite o ano de nascimento do atleta: '))
anoAtual = datetime.datetime.now().year
idade = anoAtual - anoNascimento

if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Júnior')
elif idade <= 20:
    print('Sênior')
else:
    print('Master')

