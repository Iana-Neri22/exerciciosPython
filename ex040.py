notaUm = float(input('Digite a primeira nota: '))
notaDois = float(input('Digite a segunda nota:'))
media = (notaUm + notaDois) / 2

if media < 5.0:
    print('Reprovado')
elif media >= 5.0 and 6.9:
    print('Recuperação')
else:
    print('Aprovado')


