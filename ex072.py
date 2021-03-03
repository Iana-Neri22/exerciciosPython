#numero = int(input('Digite um número entre 0 e 20: '))
numero = 99
extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze','doze', 'treze', 'catorze', 'quinze', 'dezeseis', 'dezete', 'dezoito', 'dezenove', 'vinte')
controle = 'S'

while (numero < 0 or numero > 20) and controle == 'S':
    numero = int(input('Digite um número entre 0 e 20: '))
    print(f'Você digitou o número {extenso[numero]}')    
    controle = input('Deseja continuar? [S/N]').upper().strip()
    numero = 99

