peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print('IMC {:.1f} Abaixo do peso'.format(imc))
elif 18.5 <= imc < 25:
    print('IMC {:.1f} Peso ideal'.format(imc))
elif 25 <= imc < 30:
    print('IMC {:.1f} Sobrepeso'.format(imc))
elif 30 <= imc < 40:
    print('IMC {:.1f} Obesidade'.format(imc))
else:
    print('IMC {:.1f} Obesidade mórbida'.format(imc))

