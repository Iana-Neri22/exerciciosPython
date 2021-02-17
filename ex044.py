preco = float(input('Digite o preço do produto: R$'))
condicaoPagamento = input('Digite a condição de pagamento: ')

if condicaoPagamento == 'vista dinheiro' or condicaoPagamento == 'vista cheque':
    total = preco - (preco * 0.10)
elif condicaoPagamento == 'vista cartao':
    total = preco - (preco * 0.5)
elif condicaoPagamento == 'cartao 2':
    total = preco
else:
    total = preco + (preco * 0.20)

print('O preço final do produto será R${}'.format(total))
