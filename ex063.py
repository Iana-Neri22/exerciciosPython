print('Sequência de Fibonacci')
numero = int(input('Quantos termos você quer mostrar? '))
termoUm = 0
termoDois = 1
contador = 1
numeroSequencia = 0
numeroAnterior = 1

print('{} {}'.format(termoUm, termoDois), end='')

while contador <= numero - 2:
    termoTres = termoUm + termoDois
    print(' {}'.format(termoTres), end='')

    termoUm = termoDois
    termoDois = termoTres
    contador += 1

