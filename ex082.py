controle = 'S'
lista = []
listaImpares = []
listaPares = []

while controle == 'S':
    numero = int(input('Digite um número: '))
    lista.append(numero)
    controle = input('Deseja continuar [S/N]?').strip().upper()

    if controle == 'N':
        break

    while controle != 'S':
        controle = input('Deseja continuar [S/N]?').strip().upper()

for item in lista:
    if item % 2 == 0:
        listaPares.append(item)
    else:
        listaImpares.append(item)

print(lista)
print(listaImpares)
print(listaPares)
