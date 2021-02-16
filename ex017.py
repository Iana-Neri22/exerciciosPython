from math import hypot

catetoOposto = float(input('Digite o cateto oposto:'))
catetoAdjacente = float(input('Digite o cateto adjacente: '))
print('A hipotenusa do triângulo é {:.2f}'.format(hypot(catetoAdjacente, catetoOposto)))

