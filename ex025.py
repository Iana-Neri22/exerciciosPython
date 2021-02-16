nome = input('Digite seu nome:').strip().upper()
isSilva = nome.__contains__('SILVA')
print('Seu nome tem Silva? {}'.format(isSilva))
