soma = 0

for c in range(1, 7):
    numero = int(input('Digite um número inteiro: '))
    if numero % 2 == 0:
        soma += numero

print('A soma dos número é: {}'.format(soma))
