preco = float(input('Digite o preço das compras: R$'))
print('Escolha uma opção de pagamento:')
print('1: Pagamento à vista em dinheiro ou cheque')
print('2: À vista no cartão')
print('3: 2 x no cartão')
print('4: 3 x ou mais no cartão')
condicaoPagamento = int(input('Digite a condição de pagamento: '))

if condicaoPagamento == 1:
    total = preco - (preco * 0.10)
elif condicaoPagamento == 2:
    total = preco - (preco * 0.05)
elif condicaoPagamento == 3:
    total = preco
elif condicaoPagamento == 4:
    total = preco + (preco * 0.20)
else:
    total = preco
    print('Opção inválida')

print('O preço final das compras será R${:.2f}'.format(total))
