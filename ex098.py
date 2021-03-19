def contador(inicio, fim, passo):
    if inicio < fim:
        for c in range(inicio, fim + 1, passo):
            print(c)
    else:
        for c in range(inicio, fim, -passo):
            print(c)


print('Contagem personalizada')
inicio = int(input('Digite o início: '))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o passo: '))

contador(1, 10, 1)
print()
contador(10, 0, 2)
print()
contador(inicio, fim, passo)
