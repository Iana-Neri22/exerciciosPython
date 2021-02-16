from calendar import isleap

ano = int(input('Digite um ano: '))
isBissexto = isleap(ano)

print('O ano {} é bissexto'.format(ano) if isBissexto else 'O ano {} não é bissexto'.format(ano))

