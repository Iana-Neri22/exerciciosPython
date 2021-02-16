from random import shuffle

alunoUm = input('Digite o número de primeiro aluno: ')
alunoDois = input('Digite o número do segundo aluno: ')
alunoTres = input('Digite o número do terceiro aluno: ')
alunoQuatro = input('Digite o número do quarto aluno: ')
lista = [alunoUm, alunoDois, alunoTres, alunoQuatro]
shuffle(lista)
print('A ordem de apresentação dos alunos é: {}'.format(lista))

