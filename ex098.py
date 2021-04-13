def contador(inicio, fim, passo):

    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1

    if inicio < fim:
        for c in range(inicio, fim + passo, passo):
            print(c, end=' ')
    else:
        for c in range(inicio, fim - passo, - passo):
            print(c, end=' ')


contador(1, 10, 1)
print()
contador(10, 0, 2)
print()

print('Contagem personalizada')
inicio = int(input('Digite o início: '))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o passo: '))

contador(inicio, fim, passo)
