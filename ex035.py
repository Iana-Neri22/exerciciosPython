retaUm = float(input('Digite o valor da reta 1 : '))
retaDois = float(input('Digite o valor da reta 2: '))
retaTres = float(input('Digite o valor da reta 3: '))

if retaUm < retaDois + retaTres and retaDois < retaUm + retaTres and retaTres < retaUm + retaDois:
    print('Forma um triângulo')
else:
    print('Não forma um triângulo')
