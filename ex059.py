menu = 0

primeiroNumero = int(input('Digite o primeiro número: '))
segundoNumero = int(input('Digite o segundo número: '))

while not menu == 5:

    menu = int(input(' [1] somar \n [2] multiplicar \n [3] maior \n [4] novos números \n [5] sair do programa'))

    if menu == 1:
        print(primeiroNumero + segundoNumero)
    elif menu == 2:
        print(primeiroNumero * segundoNumero)
    elif menu == 3:
        if primeiroNumero > segundoNumero:
            print(primeiroNumero)
        elif segundoNumero > primeiroNumero:
            print(segundoNumero)
        else:
            print('Os números são iguais')
    elif menu == 4:
        primeiroNumero = int(input('Digite o primeiro número: '))
        segundoNumero = int(input('Digite o segundo número: '))
    elif menu != 5:
        print('Opção inválida.')

print('Programa fechado')