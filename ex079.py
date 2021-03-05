controle = 'S'
lista = []

while controle == 'S':
    numero = int(input('Digite um número: '))
    if numero not in lista:
        lista.append(numero)
        print('Número adicionado')
    else:
        print('Número duplicado')

    controle = input('Deseja continuar? [S/N]').strip().upper()

    while controle != 'S' and controle != 'N':
        controle = input('Deseja continuar? [S/N]').strip().upper()

print(sorted(lista))
