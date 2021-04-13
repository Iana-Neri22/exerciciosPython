from datetime import datetime

def voto(anoNascimento):
    anoAtual = datetime.today().year
    idade = anoAtual - anoNascimento

    if 16 <= idade < 18 or idade >= 60:
        print('Voto opicional.')
    elif 18 <= idade < 60:
        print('Voto obrigatório.')
    else:
        print('Voto negado')

anoNascimento = int(input('Digite o ano de nascimento: '))
voto(anoNascimento)