import datetime

anoNascimento = int(input('Em qual ano você nasceu? '))
anoAtual = datetime.datetime.now().year
idade = anoAtual - anoNascimento

if idade < 18:
    print('Você ainda vai se alistar, falta {} anos.'.format(18 - idade))
elif idade == 18:
    print('Está na época de você se alistar.')
else:
    print('Você já passou {} anos do prazo de alistamento'.format(idade - 18))
