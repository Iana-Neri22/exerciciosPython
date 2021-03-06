lista = []
controle = 'S'

while controle == 'S':
    numero = int(input('Digite um número: '))
    lista.append(numero)
    controle = input('Deseja continuar? [S/N]').strip().upper()

    while controle != 'S' and controle != 'N':
        controle = input('Deseja continuar? [S/N]').strip().upper()

lista.sort(reverse=True)

print(f'Foram digitados {len(lista)} números')
print(lista)
if lista.__contains__(5):
    print('O número 5 está na lista')
else:
    print('O número 5 não está na lista')