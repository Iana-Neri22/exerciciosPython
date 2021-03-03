palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR',
            'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for palavra in palavras:
    print(f'\n {palavra} temos', end=' ')

    for letra in palavra:
        if letra in 'AEIOU':
            print(letra, end= ' ')

