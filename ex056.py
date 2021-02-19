somaIdade = 0
mulheresMenos20 = 0
nomeHomemVelho = ''
idadeHomemVelho = 0

for c in range(0, 4):
    nome = input('Qual o nome? ')
    idade = int(input('Qual é a idade? '))
    sexo = input('Qual o sexo? \n M: Masculino \n F: Feminino')

    if sexo == 'F' and idade < 20:
        mulheresMenos20 += 1
    if sexo == 'M' and idade > idadeHomemVelho:
        nomeHomemVelho = nome

    somaIdade += idade

mediaIdade = somaIdade / 4

print('A média de idade do grupo é de {} anos:'.format(mediaIdade))
print('O nome do homem mais velho é {}'.format(nomeHomemVelho))
print('{} mulheres têm menos de 20 anos.'.format(mulheresMenos20))
