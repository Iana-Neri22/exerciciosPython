def maior(numeros):
    print('Analisando os valores passados...')
    if len(numeros) != 0:
        print(f'{numeros}. Foram informados {len(numeros)} valores ao todo.')
        print(f'O maior número informado foi {max(numeros)}.')
    else:
        print(f'{numeros}. Foram informados 0 valores ao todo.')
        print(f'O maior número informado foi 0.')



maior([2, 9, 4, 5, 7, 1])
maior([4, 7, 0])
maior([1, 2])
maior([6])
maior([])