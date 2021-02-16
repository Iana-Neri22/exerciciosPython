from random import choice

alunoUm = input('Digite o número de primeiro aluno: ')
alunoDois = input('Digite o número do segundo aluno: ')
alunoTres = input('Digite o número do terceiro aluno: ')
alunoQuatro = input('Digite o número do quarto aluno: ')
print('O aluno escolhido foi: {}'.format(choice([alunoUm, alunoDois, alunoTres, alunoQuatro])))

