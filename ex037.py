numero = int(input('Escreva um número: '))
baseConversao = int(input('Escolha a base de conversão. \n 1 para binário \n 2 para octal \n 3 para hexadecimal'))

if baseConversao == 1:
    print(bin(numero)[2:])
elif baseConversao == 2:
    print(oct(numero)[2:])
elif baseConversao == 3:
    print(hex(numero)[2:])
else:
    print('Base de conversão inválida.')

