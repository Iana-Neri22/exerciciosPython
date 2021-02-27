continua = 'S'
totalMaior18 = 0
totalHomens = 0
totalMulherMenor20 = 0
sexo = ''
continua == ''

while continua == 'S':

    continua = ''

    print('Cadastre uma pessoa')
    idade = int(input('Idade: '))

    while sexo != 'M' and sexo != 'F':
        sexo = input('Sexo [M/F]: ').strip().upper()

    if idade > 18:
        totalMaior18 += 1
    if sexo == 'M':
        totalHomens += 1
    if sexo == 'F' and idade < 20:
        totalMulherMenor20 += 1

    sexo = ''
    while continua != 'S' and continua != 'N':
        continua = input('Quer continuar? [S/N]').strip().upper()

    if continua == 'N':
        break

print(f'Total de pessoas com mais de 18 anos {totalMaior18}.')
print(f'Ao todo temos {totalHomens} homens cadastrados.')
print(f'E temos {totalMulherMenor20} mulher com menos de 20 anos')
