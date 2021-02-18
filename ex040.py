notaUm = float(input('Digite a primeira nota: '))
notaDois = float(input('Digite a segunda nota:'))
media = (notaUm + notaDois) / 2

if media < 5.0:
    print('Média {:.1f} Reprovado'.format(media))
elif 5.0 <= media <= 6.9:
    print('Média {:.1f} Recuperação'.format(media))
else:
    print('Média {:.1f} Aprovado'.format(media))




