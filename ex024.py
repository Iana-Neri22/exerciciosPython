cidade = input('Digite o nome da cidade:').strip()
cidade = cidade.split()
isSanto = cidade[0].upper().__contains__('SANTO')
print(isSanto)
