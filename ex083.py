expressao = input('Digite a expressão matemática: ')

parentesesAbertos = expressao.count('(')
parentesesFechados = expressao.count(')')

if parentesesFechados == parentesesAbertos:
    print('Expressão válida')
else:
    print('Expressão inválida')
