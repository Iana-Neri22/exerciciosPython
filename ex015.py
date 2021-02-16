dias = int(input('Quantos dias o carro foi alugado? '))
kmRodados = float(input('Quantos km rodados? '))
total = (dias * 60) + (kmRodados * 0.15)
print('O total a pagar é de R${:.2f}'.format(total))
