controle = 'S'
lista = []

while controle == 'S':
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    lista.append([[nome, nota1, nota2]])

    controle = input('Deseja continuar? [S/N]').strip().upper()

    while controle != 'S' and controle != 'N':
        controle = input('Deseja continuar? [S/N]').strip().upper()

    if controle == 'N':
        break

for c, listas in enumerate(lista):
    #print(c)
    print(listas[c])
    #media = ((listas[c][1]) + listas[c][2]) / 2
    #print(c, listas[c][0], {media})

mostrar = int(input('Mostrar notas de qual aluno? 999 interrompe'))
print(lista[mostrar][1], lista[mostrar][2])

while mostrar != 999:
    mostrar = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    print(lista[mostrar][1], lista[mostrar][2])