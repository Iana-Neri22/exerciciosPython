velocidadeCarro = float(input('Escreve a velocidade do carro: '))

if velocidadeCarro > 80:
    print('Você foi multado em {:.2f} reias'.format((velocidadeCarro - 80) * 7))
else:
    print('Dirija bem')


