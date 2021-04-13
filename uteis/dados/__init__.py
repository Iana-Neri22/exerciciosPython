import os

def leiaDinheiro(frase):
    valor = input(frase).replace(',', '.')

    while valor.isalpha() or valor.strip() == '':
        valor = input(frase)

    return float(valor)


def menu():
    try:
        with open("cursoemvideo.txt") as file:
            print('Arquivo já existe')
    except IOError:
        open("cursoemvideo.txt", "w+")
        print('Arquivo criado')

    opcao = 0

    while not opcao == 3:

        print('Menu Principal')
        print('1- Ver pessoas cadastradas')
        print('2- Cadastrar nova pessoa')
        print('3- Sair do sistema')

        try:
            opcao = int(input('Sua opção: '))
        except TypeError:
            print('ERRO: Por favor, digite um número inteiro válido.')
        except ValueError:
            print('ERRO: Por favor, digite um número inteiro válido.')

        if 0 >= opcao or opcao > 3:
            print('ERRO! Digite uma opçã válida')
        elif opcao == 1:
            verPessoasCadastradas()
        elif opcao == 2:
            print('Opção 2')
        elif opcao == 3:
            print('Opção 3')
        elif opcao == 3:
            print('Saindo do sistema... Até logo!')

def verPessoasCadastradas():
    with open("cursoemvideo.txt", 'r', encoding='utf-8') as file:
        print(file.read())
