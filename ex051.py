primeiroTermo = int(input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razão da progressão aritmética: '))

for c in range(0, 10, razao):
    print(primeiroTermo)
    primeiroTermo += razao
