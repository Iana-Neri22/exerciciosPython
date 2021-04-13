def pyHelp():
    print('Sistema de ajuda pyhelp')
    funcBiblioteca = input('Função ou biblioteca: ').lower()

    while funcBiblioteca != 'fim':
        help(funcBiblioteca)

        funcBiblioteca = input('Função ou biblioteca: ').lower()

    print('Até logo')

pyHelp()
