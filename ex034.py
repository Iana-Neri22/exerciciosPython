salario = float(input('Informe o seu salário: R$'))

if salario >= 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

print('O aumento será de: R${:.2f} e o salário será de R$ {:.2f}'.format(aumento, salario + aumento))


