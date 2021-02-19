from datetime import date

anoAtual = date.today().year
maioresIdade = 0
menoresIdade = 0

for c in range(0, 7):
        anoNascimento = int(input('Digite o ano de nascimento: '))
        if (anoAtual - anoNascimento) >= 21:
            maioresIdade += 1
        else:
            menoresIdade += 1

print('{} são maiores de idade e {} são menores de idade.'.format(maioresIdade, menoresIdade))
