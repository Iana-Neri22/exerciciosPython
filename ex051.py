primeiroTermo = int(input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razão da progressão aritmética: '))
decimo = primeiroTermo + (10 -1) * razao

for c in range(primeiroTermo, decimo + razao, razao):
    print(primeiroTermo)
    primeiroTermo += razao
