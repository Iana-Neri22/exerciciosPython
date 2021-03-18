def area(largura, comprimento):
    area = largura * comprimento
    print(f'A área de um terreno {comprimento}x{largura} é de {area}.')

print('Controle de terrenos')
print('-' * 30)
largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (c): '))
area(largura, comprimento)