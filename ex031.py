distancia = float(input('Digite a distância da viagem em km: '))

if distancia <= 200:
    precoPassagem = distancia * 0.50
else:
    precoPassagem = distancia * 0.45
print('O preço da passagem é de {:.2f} reais'.format(precoPassagem))
