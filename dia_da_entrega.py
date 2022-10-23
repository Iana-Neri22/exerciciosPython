dia_semana = input()
dias_entrega = int(input())
dias_semana = ('domingo', 'segunda', 'terca', 'quarta',
              'quinta', 'sexta', 'sabado')
posicao = dias_semana.index(dia_semana)
index_total = posicao + dias_entrega
len_tuple = len(dias_semana)

if dias_entrega == 0:
  print('chega hoje!')
else:
  if index_total < len_tuple:
    print(f'sera entregue {dias_semana[index_total]}')
  else:
    resto = index_total - len_tuple
    print(f'sera entregue {dias_semana[resto]}')
