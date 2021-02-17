valorCasa = float(input("Digite o valor da casa: R$"))
salario = float(input("Digite seu salário: R$"))
anos = int(input('Em quantos anos você vai pagar a casa? '))

prestacao = valorCasa / (anos * 12)

if prestacao > salario * 0.3:
    print('O empréstimo foi negado')
else:
    print('O empréstimo foi aprovado')

