def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1

    if inicio < fim or passo <= 0:
        for c in range(inicio, fim + passo, passo):
            print(c, end=' ')
    elif passo >= 0:
        for c in range(inicio, fim - passo, - passo):
            print(c, end=' ')


print('Contagem personalizada')
inicio = int(input('Digite o início: '))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o passo: '))

contador(1, 10, 1)
print()
contador(10, 0, 2)
print()
contador(inicio, fim, passo)
