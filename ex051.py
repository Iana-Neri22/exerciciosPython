primeiroTermo = int(input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razão da progressão aritmética: '))
contador = 1
total = 0
termo = primeiroTermo
mais = 10

while mais != 0:
    total = total + mais
    while contador < total:
        print(termo)
        termo += razao
        contador += 1

    mais = int(input('Quantos termos você quer mostrar a mais? '))

print('Programa finalizado!')
